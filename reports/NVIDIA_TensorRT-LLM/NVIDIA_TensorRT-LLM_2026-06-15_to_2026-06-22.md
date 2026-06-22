# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-06-15 → 2026-06-22  |  **Total commits:** 80

## ✨ New Features This Week

- **2026-06-22** [#15237](https://github.com/NVIDIA/TensorRT-LLM/pull/15237) — [TRTLLMINF-81][feat] Avoid failed runners on infra retry (#15237)
- **2026-06-19** [#14203](https://github.com/NVIDIA/TensorRT-LLM/pull/14203) — [None][feat] Checkpointing variant of replay for MTP for mamba models (#14203)
- **2026-06-19** [#15292](https://github.com/NVIDIA/TensorRT-LLM/pull/15292) — [None][feat] BREAKING: Add MiniMax-M3 PyTorch backend bring-up with API changes (#15292)
- **2026-06-18** [#14322](https://github.com/NVIDIA/TensorRT-LLM/pull/14322) — [None][feat] Side-stream for MM encoder (#14322)
- **2026-06-18** [#15204](https://github.com/NVIDIA/TensorRT-LLM/pull/15204) — [TRTLLM-12807][feat] Add multiple FMHA library support to TRTLLM attention backend (#15204)
- **2026-06-18** [#13302](https://github.com/NVIDIA/TensorRT-LLM/pull/13302) — [TRTLLM-12199][feat] WideEP FT: add EPGroupHealth thread-safe rank mask (1a.1) (#13302)
- **2026-06-17** [#14682](https://github.com/NVIDIA/TensorRT-LLM/pull/14682) — [TRTLLMINF-113][infra] Add timeout protection to Setup/Initialize stages (#14682)
- **2026-06-17** [#14608](https://github.com/NVIDIA/TensorRT-LLM/pull/14608) — [TRTLLM-12950][feat] Add MegaMoECuteDsl NVFP4 MoE backend (#14608)
- **2026-06-17** [#15262](https://github.com/NVIDIA/TensorRT-LLM/pull/15262) — [TRTLLM-13378][feat] Drop legacy --extra_visual_gen_options CLI alias (#15262)
- **2026-06-17** [#15384](https://github.com/NVIDIA/TensorRT-LLM/pull/15384) — [None][feat] DSv4 prep: attention op plumbing (#15384)
- _…and 10 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-06-19 |
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#14826](https://github.com/NVIDIA/TensorRT-LLM/issues/14826) | [Bug]: Using the official tensorrt llm whisper conversion script does  | bug, Triton backend | 2026-06-10 |
| [#13318](https://github.com/NVIDIA/TensorRT-LLM/issues/13318) | [Bug]: Scheduler deadlock on main + #12976 + #13029: AssertionError to | bug, KV-Cache Management, Pytorch | 2026-06-04 |
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-26 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |
| [#14100](https://github.com/NVIDIA/TensorRT-LLM/issues/14100) | [Bug] trtllm-serve /v1/chat/completions: audio_url with data: URI base | bug, Multimodal | 2026-05-14 |
| [#4910](https://github.com/NVIDIA/TensorRT-LLM/issues/4910) | CUDA error CUBLAS_STATUS_EXECUTION_FAILED when launching Qwen2.5-VL-72 | bug, triaged, Scale-out, Model optimization, Multimodal | 2026-03-30 |
| [#5783](https://github.com/NVIDIA/TensorRT-LLM/issues/5783) | Performance Issue: TensorRT-LLM (v0.20.0/v25.06) Significantly Slower  | bug, triaged, Performance, Investigating, Model optimization, General perf | 2026-02-03 |
| [#10615](https://github.com/NVIDIA/TensorRT-LLM/issues/10615) | [Bug]: Llama 3.2 Vision model fails to build using documented steps | bug, Multimodal | 2026-01-19 |
| [#3889](https://github.com/NVIDIA/TensorRT-LLM/issues/3889) | whisper tensorrt-llm drop the model accuracy | bug, Model customization, OOTB | 2025-12-20 |
| [#10024](https://github.com/NVIDIA/TensorRT-LLM/issues/10024) | [Bug] TRTLLM_NIXL_KVCACHE_BACKEND causes rail endpoint serialization m | KV-Cache Management, Disaggregated serving | 2025-12-16 |
| [#10014](https://github.com/NVIDIA/TensorRT-LLM/issues/10014) | [Documentation] AWS EFA/LIBFABRIC deployment guide for disaggregated i | Doc, Disaggregated serving | 2025-12-15 |
| [#3125](https://github.com/NVIDIA/TensorRT-LLM/issues/3125) | Model built with ReDrafter produces substantially lower quality output | bug, triaged, Investigating, Speculative Decoding, Model customization | 2025-09-09 |
| [#2864](https://github.com/NVIDIA/TensorRT-LLM/issues/2864) | Could not run on a machine with dual RTX 5090s, using WSL2 and Docker | bug, triaged, Investigating, Scale-out, Testing | 2025-09-09 |
| [#7080](https://github.com/NVIDIA/TensorRT-LLM/issues/7080) | [Performance]: Can Scaffolding give more information about kvcache-reu | Performance, KV-Cache Management, Scaffolding | 2025-08-22 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 29 |
| Attention | 15 |
| Executor / Runtime | 6 |
| Disaggregation / KV | 6 |
| MoE | 6 |
| Quantization | 5 |
| Models | 4 |
| Other | 3 |
| Torch Path (_torch) | 3 |
| Docs / Examples | 2 |
| AutoDeploy | 1 |

## CI / Infra  (29 commits)

- **2026-06-22** [`4d7bf0dc95`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d7bf0dc95) [#15237](https://github.com/NVIDIA/TensorRT-LLM/pull/15237)
  [TRTLLMINF-81][feat] Avoid failed runners on infra retry (#15237)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-22** [`416bdb27b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/416bdb27b4) [#15341](https://github.com/NVIDIA/TensorRT-LLM/pull/15341)
  [None][test] Waive 2 failed cases for main in QA CI (#15341)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-20** [`53b392e945`](https://github.com/NVIDIA/TensorRT-LLM/commit/53b392e945) [#15319](https://github.com/NVIDIA/TensorRT-LLM/pull/15319)
  [None][test] Waive 3 failed cases for main in QA CI (#15319)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-20** [`d3d1b11ed3`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3d1b11ed3) [#15337](https://github.com/NVIDIA/TensorRT-LLM/pull/15337)
  [None][test] Waive 23 failed cases for main in QA CI (#15337)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-19** [`5e1a28f0af`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e1a28f0af) [#15342](https://github.com/NVIDIA/TensorRT-LLM/pull/15342)
  [None][test] Waive 8 failed cases for main in QA CI (#15342)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-19** [`b9b132b652`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9b132b652) [#15360](https://github.com/NVIDIA/TensorRT-LLM/pull/15360)
  [None][test] Waive 5 failed cases for main in QA CI (#15360)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-19** [`3baa571a90`](https://github.com/NVIDIA/TensorRT-LLM/commit/3baa571a90) [#15391](https://github.com/NVIDIA/TensorRT-LLM/pull/15391)
  [None][test] Waive 9 failed cases for main in post-merge (#15391)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-19** [`30c40dc384`](https://github.com/NVIDIA/TensorRT-LLM/commit/30c40dc384) [#15392](https://github.com/NVIDIA/TensorRT-LLM/pull/15392)
  [None][test] Waive 5 failed cases for main in post-merge (#15392)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-19** [`7060827ef2`](https://github.com/NVIDIA/TensorRT-LLM/commit/7060827ef2) [#14742](https://github.com/NVIDIA/TensorRT-LLM/pull/14742)
  [https://nvbugs/6215678][fix] Point `--output-artifact-dir` at a unique per-run subdir `{model}-openai-complet (#14742)
  _Files: `.gitignore`, `tests/integration/defs/stress_test/stress_test.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-18** [`c25fa744ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/c25fa744ca) [#15478](https://github.com/NVIDIA/TensorRT-LLM/pull/15478)
  [None][infra] Waive 1 failed cases for main in pre-merge 43917 (#15478)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-18** [`5c8a359a07`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c8a359a07) [#15411](https://github.com/NVIDIA/TensorRT-LLM/pull/15411)
  [None][test] Waive 1 failed cases for main in QA CI (#15411)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-18** [`79ea125f0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/79ea125f0e) [#15469](https://github.com/NVIDIA/TensorRT-LLM/pull/15469)
  [None][infra] Waive 18 failed cases for main in pre-merge 43878 (#15469)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`0ffa09f3c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ffa09f3c5) [#15447](https://github.com/NVIDIA/TensorRT-LLM/pull/15447)
  [None][infra] Waive 1 failed cases for main in pre-merge 43712 (#15447)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`52cbeee009`](https://github.com/NVIDIA/TensorRT-LLM/commit/52cbeee009) [#15450](https://github.com/NVIDIA/TensorRT-LLM/pull/15450)
  [None][infra] Waive 2 failed cases for main in post-merge 2785 (#15450)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`821165c083`](https://github.com/NVIDIA/TensorRT-LLM/commit/821165c083) [#15449](https://github.com/NVIDIA/TensorRT-LLM/pull/15449)
  [None][infra] Waive 1 failed cases for main in pre-merge 43720 (#15449)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`40db40233b`](https://github.com/NVIDIA/TensorRT-LLM/commit/40db40233b) [#14682](https://github.com/NVIDIA/TensorRT-LLM/pull/14682)
  [TRTLLMINF-113][infra] Add timeout protection to Setup/Initialize stages (#14682)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-17** [`0e74256c37`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e74256c37) [#15446](https://github.com/NVIDIA/TensorRT-LLM/pull/15446)
  [TRTLLMINF-137][infra] Skip to create perf report when there is not perf test results (#15446)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-17** [`29b228e46a`](https://github.com/NVIDIA/TensorRT-LLM/commit/29b228e46a) [#15395](https://github.com/NVIDIA/TensorRT-LLM/pull/15395)
  [None][infra] Waive 11 failed cases for main in post-merge 2782 (#15395)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`9b77c8e3d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/9b77c8e3d9) [#15439](https://github.com/NVIDIA/TensorRT-LLM/pull/15439)
  [None][infra] Waive 1 failed cases for main in pre-merge 43656 (#15439)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`c025b86607`](https://github.com/NVIDIA/TensorRT-LLM/commit/c025b86607) [#15320](https://github.com/NVIDIA/TensorRT-LLM/pull/15320)
  [None][test] Waive 1 failed cases for main in QA CI (#15320)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-17** [`2b14cfb8f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b14cfb8f4) [#15389](https://github.com/NVIDIA/TensorRT-LLM/pull/15389)
  [None][test] Waive 8 failed cases for main in post-merge (#15389)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-16** [`e45dda92b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/e45dda92b1) [#15364](https://github.com/NVIDIA/TensorRT-LLM/pull/15364)
  [None][infra] Update the new duration base on opensearch result (#15364)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-06-16** [`72ecb9857f`](https://github.com/NVIDIA/TensorRT-LLM/commit/72ecb9857f) [#15377](https://github.com/NVIDIA/TensorRT-LLM/pull/15377)
  [None][test] Waive 1 failed cases for main in QA CI (#15377)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-16** [`f49d09f1e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/f49d09f1e0) [#15373](https://github.com/NVIDIA/TensorRT-LLM/pull/15373)
  [None][infra] Waive 21 failed cases for main in post-merge 2780 (#15373)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-15** [`feca41c600`](https://github.com/NVIDIA/TensorRT-LLM/commit/feca41c600) [#15183](https://github.com/NVIDIA/TensorRT-LLM/pull/15183)
  [TRTLLMINF-103][feat] Keep SLURM timeouts non-retryable (#15183)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-15** [`1c069d3e0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c069d3e0d) [#15357](https://github.com/NVIDIA/TensorRT-LLM/pull/15357)
  [None][infra] pin pytest and click workaround (#15357)
  _Files: `requirements-dev.txt`, `requirements.txt`_
- **2026-06-15** [`91a271b831`](https://github.com/NVIDIA/TensorRT-LLM/commit/91a271b831) [#15315](https://github.com/NVIDIA/TensorRT-LLM/pull/15315)
  [None][test] Waive 1 failed cases for main in QA CI (#15315)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-15** [`801cde11bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/801cde11bd) [#15210](https://github.com/NVIDIA/TensorRT-LLM/pull/15210)
  [None][infra] Record CBTS decision to OpenSearch for CI-health monitoring (#15210)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/tools/dryrun.py` _+2 more__
- **2026-06-15** [`221a0e10f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/221a0e10f5) [#15358](https://github.com/NVIDIA/TensorRT-LLM/pull/15358)
  [None][infra] Waive 1 failed cases for main in pre-merge 43173 (#15358)
  _Files: `tests/integration/test_lists/waives.txt`_

## Attention  (15 commits)

- **2026-06-19** [`a76c818cd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a76c818cd9) [#14203](https://github.com/NVIDIA/TensorRT-LLM/pull/14203)
  [None][feat] Checkpointing variant of replay for MTP for mamba models (#14203)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/flashinfer_backend_mamba.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/replay_metadata.py`, `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py` _+16 more__
- **2026-06-18** [`1aa232a0fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/1aa232a0fc) [#15204](https://github.com/NVIDIA/TensorRT-LLM/pull/15204)
  [TRTLLM-12807][feat] Add multiple FMHA library support to TRTLLM attention backend (#15204)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/__init__.py`, `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention_backend/fmha/interface.py` _+5 more__
- **2026-06-18** [`08f4bb1bf6`](https://github.com/NVIDIA/TensorRT-LLM/commit/08f4bb1bf6) [#15460](https://github.com/NVIDIA/TensorRT-LLM/pull/15460)
  [None][fix] Fix stale sparse attention kwargs (#15460)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-06-17** [`d202244df2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d202244df2) [#15259](https://github.com/NVIDIA/TensorRT-LLM/pull/15259)
  [None][ci] tighten VisualGen CBTS routing (#15259)
  _Files: `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/visual_gen_rule.py`, `tensorrt_llm/bench/benchmark/visual_gen.py`, `tensorrt_llm/commands/utils.py` _+20 more__
- **2026-06-17** [`071c287d13`](https://github.com/NVIDIA/TensorRT-LLM/commit/071c287d13) [#15312](https://github.com/NVIDIA/TensorRT-LLM/pull/15312)
  [https://nvbugs/6270671][fix] Enable multi-block mode for XQA HMMA spec-dec (#15312)
  _Files: `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/decoderXQARunner.cpp`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/decoderXQARunnerUtils.h`_
- **2026-06-17** [`5fe0a177d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fe0a177d7) [#15390](https://github.com/NVIDIA/TensorRT-LLM/pull/15390)
  [None][perf] DSv4 prep: attention fusion custom ops (#15390)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.h`, `cpp/tensorrt_llm/kernels/deepseekV4QNormKernel.cu`, `cpp/tensorrt_llm/kernels/deepseekV4QNormKernel.h` _+10 more__
- **2026-06-17** [`7e243650e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e243650e8) [#15305](https://github.com/NVIDIA/TensorRT-LLM/pull/15305)
  [https://nvbugs/6248837][fix] Densify trtllm-gen fmha warmup grid to catch missing kernels (#15305)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-06-17** [`9a081b8d6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a081b8d6b) [#14687](https://github.com/NVIDIA/TensorRT-LLM/pull/14687)
  [None][refactor] Refactor Skip Softmax Attention Interface (#14687)
  _Files: `docs/source/developer-guide/sparse-attention-development-guide.md`, `docs/source/features/sparse-attention.md`, `docs/source/index.rst`, `docs/source/models/visual-generation.md` _+58 more__
- **2026-06-17** [`18cb08e104`](https://github.com/NVIDIA/TensorRT-LLM/commit/18cb08e104) [#15384](https://github.com/NVIDIA/TensorRT-LLM/pull/15384)
  [None][feat] DSv4 prep: attention op plumbing (#15384)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`_
- **2026-06-16** [`dfad249a21`](https://github.com/NVIDIA/TensorRT-LLM/commit/dfad249a21) [#13919](https://github.com/NVIDIA/TensorRT-LLM/pull/13919)
  [TRTLLM-12339][feat] Support T5 and BART in the PyTorch backend (#13919)
  _Files: `cpp/include/tensorrt_llm/batch_manager/capacityScheduler.h`, `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/common/optionalRef.h`, `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp` _+38 more__
- **2026-06-16** [`d6967a17bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6967a17bf) [#15335](https://github.com/NVIDIA/TensorRT-LLM/pull/15335)
  [TRTLLM-12807][test] Guard thop attention kwarg aliases (#15335)
  _Files: `tests/unittest/_torch/attention_backend/test_attention_op_sync.py`_
- **2026-06-16** [`2ef2ea57ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ef2ea57ad) [#15345](https://github.com/NVIDIA/TensorRT-LLM/pull/15345)
  [TRTLLM-12339][feat] enable TRTLLM cross attention backend (#15345)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h`, `tensorrt_llm/_torch/attention_backend/interface.py` _+2 more__
- **2026-06-15** [`35c970436d`](https://github.com/NVIDIA/TensorRT-LLM/commit/35c970436d) [#14693](https://github.com/NVIDIA/TensorRT-LLM/pull/14693)
  [TRTLLM-12982][feat] support multi item scoring in LLM.encode (#14693)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/star_flashinfer.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+9 more__
- **2026-06-15** [`20b6068387`](https://github.com/NVIDIA/TensorRT-LLM/commit/20b6068387) [#15163](https://github.com/NVIDIA/TensorRT-LLM/pull/15163)
  [None][feat] skip-softmax on SM120: TMA-load + sync-MMA warp-specialized context FMHA for sm_120/sm_121 (#15163)
  _Files: `cpp/kernels/fmha_v2/src/fmha/kernel_traits.h`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/README.md`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/compute_sync_mma.h`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/dma_sync_mma.h` _+7 more__
- **2026-06-15** [`870f9b5b82`](https://github.com/NVIDIA/TensorRT-LLM/commit/870f9b5b82) [#14852](https://github.com/NVIDIA/TensorRT-LLM/pull/14852)
  [https://nvbugs/6029882][fix] Fix attentionOp fp8 mla kvreuse workspace calculation (#14852)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (6 commits)

- **2026-06-22** [`e47359c4fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e47359c4fd) [#15423](https://github.com/NVIDIA/TensorRT-LLM/pull/15423)
  [None][fix] AutoDeploy: Fixed wrong dist_backend AUTO detection when using trtllm-llmapi-launch (#15423)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/distributed/trtllm_dist.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/sharding.py`, `tests/unittest/auto_deploy/multigpu/transformations/library/test_dist_backend.py`_
- **2026-06-18** [`4a8b7af7a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a8b7af7a9) [#14322](https://github.com/NVIDIA/TensorRT-LLM/pull/14322)
  [None][feat] Side-stream for MM encoder (#14322)
  _Files: `tensorrt_llm/_torch/models/modeling_mistral.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py` _+5 more__
- **2026-06-17** [`a590a2d407`](https://github.com/NVIDIA/TensorRT-LLM/commit/a590a2d407) [#14895](https://github.com/NVIDIA/TensorRT-LLM/pull/14895)
  [None][perf] executor: avoid deepcopy of prompt_token_ids on enqueue (#14895)
  _Files: `tensorrt_llm/executor/base_worker.py`_
- **2026-06-16** [`81e57e0760`](https://github.com/NVIDIA/TensorRT-LLM/commit/81e57e0760) [#14702](https://github.com/NVIDIA/TensorRT-LLM/pull/14702)
  [None][feat] Qwen3-VL: support per-request mm_processor_kwargs (#14702)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3vl_preprocess.py` _+1 more__
- **2026-06-15** [`0d4bab9dad`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d4bab9dad) [#13768](https://github.com/NVIDIA/TensorRT-LLM/pull/13768)
  [None][fix] Forward secondary_offload_min_priority to KVCacheManager in PyTorch executor (#13768)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/test_resource_manager.py`_
- **2026-06-15** [`130ae826d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/130ae826d0) [#15125](https://github.com/NVIDIA/TensorRT-LLM/pull/15125)
  [None][fix] Fix beam search log_probs non-determinism with batch_size > 1 (#15125)
  _Files: `cpp/tensorrt_llm/kernels/decodingKernels.cu`, `cpp/tensorrt_llm/kernels/decodingKernels.h`, `cpp/tensorrt_llm/layers/beamSearchLayer.cu`, `cpp/tensorrt_llm/runtime/gptDecoderBatched.cpp` _+3 more__

## Disaggregation / KV  (6 commits)

- **2026-06-19** [`d9041f8e2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9041f8e2f) [#15054](https://github.com/NVIDIA/TensorRT-LLM/pull/15054)
  [None][fix] fix CppMambaHybridCacheManager to handle dp dummy request (#15054)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`_
- **2026-06-16** [`275c1724c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/275c1724c8) [#15149](https://github.com/NVIDIA/TensorRT-LLM/pull/15149)
  [TRTLLM-13333][feat] Add prefetch_reuse_blocks and configurable prefetch count (#15149)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_common.py` _+2 more__
- **2026-06-16** [`163be837f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/163be837f3) [#15246](https://github.com/NVIDIA/TensorRT-LLM/pull/15246)
  [https://nvbugs/6223556][fix] Propagate gen-first ctx usage via aux buffer to postproc (#15246)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/result.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_overlap_gen_first.yaml` _+2 more__
- **2026-06-16** [`f3b718ad74`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3b718ad74) [#14908](https://github.com/NVIDIA/TensorRT-LLM/pull/14908)
  [https://nvbugs/6245861][fix] Gate the two ID None-checks on `finish_reason in _GEN_PENDING_FINISH_REASONS`… (#14908)
  _Files: `tensorrt_llm/serve/openai_disagg_service.py`, `tests/unittest/disaggregated/test_openai_disagg_service.py`_
- **2026-06-16** [`0b0a03e7cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b0a03e7cf) [#15369](https://github.com/NVIDIA/TensorRT-LLM/pull/15369)
  [https://nvbugs/312578][fix] split test_cache_transceiver_single_process (#15369)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/disaggregated/test_cache_transceiver_single_process.py`_
- **2026-06-16** [`09449d4881`](https://github.com/NVIDIA/TensorRT-LLM/commit/09449d4881) [#15272](https://github.com/NVIDIA/TensorRT-LLM/pull/15272)
  [None][fix] pool-qualify KV cache transfer pending keys (#15272)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheTransferManager.h`, `cpp/tensorrt_llm/batch_manager/kvCacheTransferManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`_

## MoE  (6 commits)

- **2026-06-19** [`2a18bd4e40`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a18bd4e40) [#15292](https://github.com/NVIDIA/TensorRT-LLM/pull/15292)
  [None][feat] BREAKING: Add MiniMax-M3 PyTorch backend bring-up with API changes (#15292)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/attention_backend/sparse/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/backend.py` _+26 more__
- **2026-06-18** [`c390d2f7c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/c390d2f7c1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+53 more__
- **2026-06-18** [`9e69568406`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e69568406) [#13302](https://github.com/NVIDIA/TensorRT-LLM/pull/13302)
  [TRTLLM-12199][feat] WideEP FT: add EPGroupHealth thread-safe rank mask (1a.1) (#13302)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/ep_group_health.py`, `tests/unittest/_torch/modules/test_ep_group_health.py`_
- **2026-06-17** [`2772b99bb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/2772b99bb9) [#14608](https://github.com/NVIDIA/TensorRT-LLM/pull/14608)
  [TRTLLM-12950][feat] Add MegaMoECuteDsl NVFP4 MoE backend (#14608)
  _Files: `.claude/skills/trtllm-moe-develop/SKILL.md`, `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml` _+42 more__
- **2026-06-16** [`b7f36735a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7f36735a7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+51 more__
- **2026-06-16** [`e171875352`](https://github.com/NVIDIA/TensorRT-LLM/commit/e171875352) [#15271](https://github.com/NVIDIA/TensorRT-LLM/pull/15271)
  [None][chore] Integration tests for MoE lora & bugfixes (#15271)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_lora_problem_builder.cu`, `cpp/tests/unit_tests/kernels/moeLoraProblemBuilderTest.cu`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/peft/lora/cuda_graph_lora_params.py` _+3 more__

## Quantization  (5 commits)

- **2026-06-22** [`a8c595521e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8c595521e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/lookahead/poetry.lock` _+35 more__
- **2026-06-19** [`4d44595216`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d44595216)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+44 more__
- **2026-06-17** [`6e0c1c2a77`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e0c1c2a77) [#14745](https://github.com/NVIDIA/TensorRT-LLM/pull/14745)
  [TRTLLM-12669][refactor] Eagle3 sampling: auto-detect greedy fast-path, mixed-batch rejection sampling, draft honors target params (#14745)
  _Files: `examples/llm-api/quickstart_advanced.py`, `examples/models/core/nemotron/README_nemotron_super_v3.md`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+12 more__
- **2026-06-17** [`059396899c`](https://github.com/NVIDIA/TensorRT-LLM/commit/059396899c) [#15262](https://github.com/NVIDIA/TensorRT-LLM/pull/15262)
  [TRTLLM-13378][feat] Drop legacy --extra_visual_gen_options CLI alias (#15262)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `examples/visual_gen/configs/ltx2-4gpu.yaml`, `examples/visual_gen/configs/wan2.2-t2v-fp4-1gpu.yaml`, `examples/visual_gen/configs/wan2.2-t2v-fp4-4gpu.yaml` _+14 more__
- **2026-06-15** [`b1ee4ab17e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1ee4ab17e) [#14476](https://github.com/NVIDIA/TensorRT-LLM/pull/14476)
  [None][feat] MNNVL Performance Optimization and FP8/NVFP4 Quant Fusion (#14476)
  _Files: `cpp/tensorrt_llm/common/lamportUtils.cuh`, `cpp/tensorrt_llm/kernels/communicationKernels/mnnvlAllreduceKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/mnnvlAllreduceKernels.h`, `cpp/tensorrt_llm/thop/allreduceOp.cpp` _+3 more__

## Models  (4 commits)

- **2026-06-21** [`6f9e32e4c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f9e32e4c1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/stdit/poetry.lock`, `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/models/core/qwen/pyproject.toml`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+2 more__
- **2026-06-17** [`fd5de7e501`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd5de7e501)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/grok/poetry.lock`, `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/models/core/qwen/pyproject.toml` _+4 more__
- **2026-06-17** [`500ebf2ea3`](https://github.com/NVIDIA/TensorRT-LLM/commit/500ebf2ea3) [#15233](https://github.com/NVIDIA/TensorRT-LLM/pull/15233)
  [#15182][fix] Fix embedding vocab mask for handling rejection sampling in Kimi-K2.5 (#15233)
  _Files: `tensorrt_llm/_torch/modules/embedding.py`_
- **2026-06-15** [`aa3236b709`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa3236b709)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_

## Other  (3 commits)

- **2026-06-17** [`42a3e55ceb`](https://github.com/NVIDIA/TensorRT-LLM/commit/42a3e55ceb) [#15338](https://github.com/NVIDIA/TensorRT-LLM/pull/15338)
  [None][fix] fix tinygemm barrier bug (#15338)
  _Files: `cpp/tensorrt_llm/kernels/tinygemm2/tinygemm2_kernel.cuh`_
- **2026-06-16** [`9206812439`](https://github.com/NVIDIA/TensorRT-LLM/commit/9206812439) [#15323](https://github.com/NVIDIA/TensorRT-LLM/pull/15323)
  [None][test] Fix Mamba hybrid transceiver helper (#15323)
  _Files: `tests/unittest/others/test_kv_cache_transceiver.py`_
- **2026-06-16** [`0ec3250400`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ec3250400) [#15374](https://github.com/NVIDIA/TensorRT-LLM/pull/15374)
  [None][refactor] Enhance pytest integration by updating test node generation to support fixture inheritance and dynamic collection (#15374)
  _Files: `tests/integration/defs/perf/utils.py`_

## Torch Path (_torch)  (3 commits)

- **2026-06-16** [`08fba406d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/08fba406d1) [#15408](https://github.com/NVIDIA/TensorRT-LLM/pull/15408)
  [TRTLLM-12982][chore] NVTX-annotate logits processor (#15408)
  _Files: `tensorrt_llm/_torch/modules/logits_processor.py`_
- **2026-06-16** [`f45172615d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f45172615d) [#15331](https://github.com/NVIDIA/TensorRT-LLM/pull/15331)
  [https://nvbugs/6281014][fix] fix the repeated cute.compile and simpilify the test (#15331)
  _Files: `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus.yml` _+2 more__
- **2026-06-15** [`26ea499332`](https://github.com/NVIDIA/TensorRT-LLM/commit/26ea499332) [#15256](https://github.com/NVIDIA/TensorRT-LLM/pull/15256)
  [None][refactor] Remove TensorRT performance baseline and update to PyTorch only (#15256)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_run.sh`, `tests/integration/defs/perf/README.md`, `tests/integration/defs/perf/_model_paths.py` _+6 more__

## Docs / Examples  (2 commits)

- **2026-06-15** [`7cefb4aa2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7cefb4aa2e) [#15188](https://github.com/NVIDIA/TensorRT-LLM/pull/15188)
  [None][chore] Bump version to 1.3.0rc19 (#15188)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-06-15** [`e6c996453b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6c996453b) [#15208](https://github.com/NVIDIA/TensorRT-LLM/pull/15208)
  [TRTLLM-11408][test] Add e2e Tensor Parallel LPIPS tests for VisualGen (#15208)
  _Files: `tests/integration/defs/examples/test_visual_gen_multi_gpu.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_

## AutoDeploy  (1 commits)

- **2026-06-20** [`3297cb965b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3297cb965b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/grok/poetry.lock` _+8 more__

---
_Generated 2026-06-22 13:47 UTC_