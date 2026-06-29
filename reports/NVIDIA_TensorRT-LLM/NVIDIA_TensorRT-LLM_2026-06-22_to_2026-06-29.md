# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-06-22 → 2026-06-29  |  **Total commits:** 151

## ✨ New Features This Week

- **2026-06-29** [#15644](https://github.com/NVIDIA/TensorRT-LLM/pull/15644) — [None][feat] add CI-enforced stability gate for trtllm-serve HTTP schema (#15644)
- **2026-06-29** [#15656](https://github.com/NVIDIA/TensorRT-LLM/pull/15656) — [None][feat] Optimize trtllmgen moe routing (#15656)
- **2026-06-29** [#14246](https://github.com/NVIDIA/TensorRT-LLM/pull/14246) — [TRTLLM-12751][feat] visual-gen /metrics iteration stats producer (#14246)
- **2026-06-29** [#14984](https://github.com/NVIDIA/TensorRT-LLM/pull/14984) — [None][feat] Cache LTX2 merged LoRA weight (#14984)
- **2026-06-28** [#15102](https://github.com/NVIDIA/TensorRT-LLM/pull/15102) — [TRTLLM-13265][feat] Fuse LTX-2 Gate + Residual + Norm + AdaLN modulation(ShiftScale) + Quant kernels (#15102)
- **2026-06-28** [#15414](https://github.com/NVIDIA/TensorRT-LLM/pull/15414) — [None][feat] DSv4: model, tokenizer, and integration coverage (#15414)
- **2026-06-28** [#14815](https://github.com/NVIDIA/TensorRT-LLM/pull/14815) — [None][feat] Support inflight weight update (#14815)
- **2026-06-27** [#14654](https://github.com/NVIDIA/TensorRT-LLM/pull/14654) — [None][feat] Converge VisualGen LPIPS and VBench test generation (#14654)
- **2026-06-27** [#15409](https://github.com/NVIDIA/TensorRT-LLM/pull/15409) — [None][feat] DSv4: sparse MLA attention backend (#15409)
- **2026-06-26** [#14962](https://github.com/NVIDIA/TensorRT-LLM/pull/14962) — [None][feat] add MXFP8 weight format + CUTLASS W8A8 Linear and MoE (#14962)
- _…and 34 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |
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
| CI / Infra | 37 |
| MoE | 18 |
| Attention | 17 |
| Torch Path (_torch) | 15 |
| Executor / Runtime | 14 |
| Models | 14 |
| Quantization | 12 |
| Other | 7 |
| Disaggregation / KV | 7 |
| Speculative Decoding | 4 |
| Docs / Examples | 3 |
| LoRA | 1 |
| Perf | 1 |
| AutoDeploy | 1 |

## CI / Infra  (37 commits)

- **2026-06-29** [`fde8e0aab8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fde8e0aab8) [#15644](https://github.com/NVIDIA/TensorRT-LLM/pull/15644)
  [None][feat] add CI-enforced stability gate for trtllm-serve HTTP schema (#15644)
  _Files: `tests/unittest/api_stability/references/trtllm_serve_api.yaml`, `tests/unittest/api_stability/test_serve_api.py`_
- **2026-06-29** [`0bba015066`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bba015066) [#15705](https://github.com/NVIDIA/TensorRT-LLM/pull/15705)
  [None][infra] Waive 5 failed cases for main in post-merge 2811 (#15705)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`47333fa193`](https://github.com/NVIDIA/TensorRT-LLM/commit/47333fa193) [#15686](https://github.com/NVIDIA/TensorRT-LLM/pull/15686)
  [None][test] Waive 4 failed cases for main in QA CI (#15686)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`33c7717a9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/33c7717a9c) [#15667](https://github.com/NVIDIA/TensorRT-LLM/pull/15667)
  [None][test] Waive 2 failed cases for main in QA CI (#15667)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`f5002e93f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5002e93f4) [#15700](https://github.com/NVIDIA/TensorRT-LLM/pull/15700)
  [None][infra] Waive 9 failed cases for main in post-merge 2810 (#15700)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`f1789c1417`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1789c1417) [#15688](https://github.com/NVIDIA/TensorRT-LLM/pull/15688)
  [None][test] Waive 1 failed cases for main in QA CI (#15688)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`267b2596ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/267b2596ab) [#15678](https://github.com/NVIDIA/TensorRT-LLM/pull/15678)
  [None][test] Waive 1 failed cases for main in QA CI (#15678)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-27** [`eaf5693b3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/eaf5693b3a) [#14654](https://github.com/NVIDIA/TensorRT-LLM/pull/14654)
  [None][feat] Converge VisualGen LPIPS and VBench test generation (#14654)
  _Files: `scripts/visualgen_eval/visual_gen_lpips_score_eval.py`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/flux1_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/flux2_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/wan21_t2v_lpips_golden_video.json` _+4 more__
- **2026-06-27** [`c25c23f717`](https://github.com/NVIDIA/TensorRT-LLM/commit/c25c23f717)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+3 more__
- **2026-06-26** [`64ac565892`](https://github.com/NVIDIA/TensorRT-LLM/commit/64ac565892) [#15665](https://github.com/NVIDIA/TensorRT-LLM/pull/15665)
  [https://nvbugs/6248837][chore] waive memory polluters (#15665)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-26** [`86bb1f4612`](https://github.com/NVIDIA/TensorRT-LLM/commit/86bb1f4612) [#15614](https://github.com/NVIDIA/TensorRT-LLM/pull/15614)
  [None][infra] take test durations into account to determine cbts splits num (#15614)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/blocks.py` _+3 more__
- **2026-06-25** [`ef79d8be5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef79d8be5f) [#15623](https://github.com/NVIDIA/TensorRT-LLM/pull/15623)
  [None][infra] Fix node list query failing on tcsh login nodes (#15623)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-25** [`34242e400a`](https://github.com/NVIDIA/TensorRT-LLM/commit/34242e400a) [#15609](https://github.com/NVIDIA/TensorRT-LLM/pull/15609)
  [None][test] Waive hang issues (#15609)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-25** [`cddfb3d75b`](https://github.com/NVIDIA/TensorRT-LLM/commit/cddfb3d75b) [#15620](https://github.com/NVIDIA/TensorRT-LLM/pull/15620)
  [None][infra] Waive 15 failed cases for main in post-merge 2804 (#15620)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-25** [`7cc568c4ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/7cc568c4ee) [#15592](https://github.com/NVIDIA/TensorRT-LLM/pull/15592)
  [None][infra] use default split when CBTS test-db download fails (#15592)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-25** [`ad0f363aac`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad0f363aac) [#15549](https://github.com/NVIDIA/TensorRT-LLM/pull/15549)
  [None][infra] add blossom-ci authorized users (#15549)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-06-25** [`07e3c3fcbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/07e3c3fcbd) [#15585](https://github.com/NVIDIA/TensorRT-LLM/pull/15585)
  [None][test] Waive failed unittest on all devices (nvbugs/6335726) (#15585)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`65923e7f25`](https://github.com/NVIDIA/TensorRT-LLM/commit/65923e7f25) [#15147](https://github.com/NVIDIA/TensorRT-LLM/pull/15147)
  [TRTLLMINF-111][infra] Reuse image sqsh file (#15147)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-24** [`91c1e4a377`](https://github.com/NVIDIA/TensorRT-LLM/commit/91c1e4a377) [#15581](https://github.com/NVIDIA/TensorRT-LLM/pull/15581)
  waive hang issues (#15581)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`ca13cf32aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca13cf32aa) [#15576](https://github.com/NVIDIA/TensorRT-LLM/pull/15576)
  [None][test] waive hang issues (#15576)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`d3c0d83b2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3c0d83b2c) [#15579](https://github.com/NVIDIA/TensorRT-LLM/pull/15579)
  [None][test] Waive 2 failed cases for main in QA CI (#15579)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`45d56a85e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/45d56a85e7) [#15568](https://github.com/NVIDIA/TensorRT-LLM/pull/15568)
  [None][ci] move more test cases to post merge (#15568)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-06-24** [`fb43138ac1`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb43138ac1) [#15570](https://github.com/NVIDIA/TensorRT-LLM/pull/15570)
  [None][test] Waive 6 failed cases for main in QA CI (#15570)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`6a4d8caee8`](https://github.com/NVIDIA/TensorRT-LLM/commit/6a4d8caee8) [#15571](https://github.com/NVIDIA/TensorRT-LLM/pull/15571)
  [None][infra] Waive 3 failed cases for main in post-merge 2802 (#15571)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`91dc1458b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/91dc1458b5) [#15548](https://github.com/NVIDIA/TensorRT-LLM/pull/15548)
  [None][infra] split single-node perf sanity GB200 (#15548)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-23** [`31d4301459`](https://github.com/NVIDIA/TensorRT-LLM/commit/31d4301459) [#15510](https://github.com/NVIDIA/TensorRT-LLM/pull/15510)
  [None][test] Waive 4 failed cases for main in QA CI (#15510)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`2275d1ec29`](https://github.com/NVIDIA/TensorRT-LLM/commit/2275d1ec29) [#15499](https://github.com/NVIDIA/TensorRT-LLM/pull/15499)
  [None][test] Waive 1 failed cases for main in QA CI (#15499)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`aea4086af0`](https://github.com/NVIDIA/TensorRT-LLM/commit/aea4086af0) [#15504](https://github.com/NVIDIA/TensorRT-LLM/pull/15504)
  [None][test] Waive 9 failed cases for main in QA CI (#15504)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`259b71f664`](https://github.com/NVIDIA/TensorRT-LLM/commit/259b71f664) [#15535](https://github.com/NVIDIA/TensorRT-LLM/pull/15535)
  [None][test] Waive 10 failed cases for main in post-merge (#15535)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`cfc4e8bd5c`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfc4e8bd5c) [#15511](https://github.com/NVIDIA/TensorRT-LLM/pull/15511)
  [None][test] Remove 60 closed-bug waive entries for main (#15511)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`55fa04d601`](https://github.com/NVIDIA/TensorRT-LLM/commit/55fa04d601) [#15505](https://github.com/NVIDIA/TensorRT-LLM/pull/15505)
  [None][test] Waive 4 failed cases for main in QA CI (#15505)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`2ce56a3601`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ce56a3601) [#15506](https://github.com/NVIDIA/TensorRT-LLM/pull/15506)
  [None][test] Waive 11 failed cases for main in QA CI (#15506)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`3448424dd2`](https://github.com/NVIDIA/TensorRT-LLM/commit/3448424dd2) [#15509](https://github.com/NVIDIA/TensorRT-LLM/pull/15509)
  [None][test] Waive 3 failed cases for main in QA CI (#15509)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`c32154f0b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c32154f0b7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-06-22** [`f53602696d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f53602696d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-06-22** [`4d7bf0dc95`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d7bf0dc95) [#15237](https://github.com/NVIDIA/TensorRT-LLM/pull/15237)
  [TRTLLMINF-81][feat] Avoid failed runners on infra retry (#15237)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-22** [`416bdb27b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/416bdb27b4) [#15341](https://github.com/NVIDIA/TensorRT-LLM/pull/15341)
  [None][test] Waive 2 failed cases for main in QA CI (#15341)
  _Files: `tests/integration/test_lists/waives.txt`_

## MoE  (18 commits)

- **2026-06-29** [`552f462864`](https://github.com/NVIDIA/TensorRT-LLM/commit/552f462864) [#15656](https://github.com/NVIDIA/TensorRT-LLM/pull/15656)
  [None][feat] Optimize trtllmgen moe routing (#15656)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomPolicy.cuh`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingKernelTopK.cuh`_
- **2026-06-29** [`28acbad14b`](https://github.com/NVIDIA/TensorRT-LLM/commit/28acbad14b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+47 more__
- **2026-06-28** [`b6d186af57`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6d186af57) [#12643](https://github.com/NVIDIA/TensorRT-LLM/pull/12643)
  [TRTLLM-11715][infra] Upgrade dependencies for dlfw 26.04 stack (#12643)
  _Files: `README.md`, `constraints.txt`, `cpp/include/tensorrt_llm/runtime/virtualMemory.h`, `cpp/tensorrt_llm/deep_ep/CMakeLists.txt` _+26 more__
- **2026-06-28** [`5b6c3ed915`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b6c3ed915) [#15624](https://github.com/NVIDIA/TensorRT-LLM/pull/15624)
  [TRTLLM-13629][test] Optimize MoE CI test-db (#15624)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+6 more__
- **2026-06-26** [`8613f0c9d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/8613f0c9d0) [#14962](https://github.com/NVIDIA/TensorRT-LLM/pull/14962)
  [None][feat] add MXFP8 weight format + CUTLASS W8A8 Linear and MoE (#14962)
  _Files: `cpp/include/tensorrt_llm/common/quantization.h`, `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm_configs.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`, `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.h` _+35 more__
- **2026-06-26** [`0cc7e4e109`](https://github.com/NVIDIA/TensorRT-LLM/commit/0cc7e4e109) [#15543](https://github.com/NVIDIA/TensorRT-LLM/pull/15543)
  [TRTLLM-13575][feat] Add EPLB support for Qwen3.5 (#15543)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/moe_load_balancer.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus.yml`_
- **2026-06-26** [`9882d4f7b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9882d4f7b0) [#15541](https://github.com/NVIDIA/TensorRT-LLM/pull/15541)
  [None][test] Add modularized perf tests (attention + MoE discrete/continuous) (#15541)
  _Files: `tests/microbenchmarks/attention_perf/attention_perf_harness.py`, `tests/microbenchmarks/attention_perf/conftest.py`, `tests/microbenchmarks/attention_perf/golden_attention.json`, `tests/microbenchmarks/attention_perf/test_attention_perf_module.py` _+2 more__
- **2026-06-25** [`bcb94419ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcb94419ae) [#13476](https://github.com/NVIDIA/TensorRT-LLM/pull/13476)
  [TRTLLM-12242][feat] Add Marlin NVFP4 backend for MoE and Linear on Hopper (#13476)
  _Files: `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/marlin/marlin.cuh`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4.h`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4_dispatch_utils.cpp` _+39 more__
- **2026-06-25** [`a51931ad2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a51931ad2f) [#15538](https://github.com/NVIDIA/TensorRT-LLM/pull/15538)
  [https://nvbugs/6166097][fix] Fix CuteDSL NVFP4 EPLB weight layout (#15538)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/quantization.py`, `tests/scripts/perf/disaggregated/gb200_wideep_accuracy-deepseek-r1-fp4_1k1k_ctx2_gen1_dep16_bs128_eplb288_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_accuracy-deepseek-r1-fp4_gpqa_diamond_1k1k_ctx2_gen1_dep16_bs128_eplb288_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_1k1k_ctx2_gen1_dep16_bs128_eplb288_mtp3_ccb-NIXL.yaml` _+2 more__
- **2026-06-24** [`7193f41a31`](https://github.com/NVIDIA/TensorRT-LLM/commit/7193f41a31) [#15014](https://github.com/NVIDIA/TensorRT-LLM/pull/15014)
  [TRTLLM-13246][feat] Wave 1: migrate aliases to setup_aliases and stage GMS RO load (#15014)
  _Files: `tensorrt_llm/_torch/memory/gpu_memory_backend.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_exaone_moe.py`, `tensorrt_llm/_torch/models/modeling_glm.py` _+7 more__
- **2026-06-24** [`71613f9d8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/71613f9d8c) [#15402](https://github.com/NVIDIA/TensorRT-LLM/pull/15402)
  [None][feat] DSv4 prep: MoE routing and backend support (#15402)
  _Files: `3rdparty/fetch_content.json`, `cpp/tensorrt_llm/kernels/customMoeRoutingKernels.cu`, `cpp/tensorrt_llm/kernels/customMoeRoutingKernels.h`, `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu` _+44 more__
- **2026-06-24** [`4a88020618`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a88020618) [#15531](https://github.com/NVIDIA/TensorRT-LLM/pull/15531)
  [#14874][feat] AutoDeploy : Perf optimization for gpt-oss-120b for low conc (#15531)
  _Files: `examples/auto_deploy/model_registry/configs/gpt_oss.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/trtllm_attention.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/distributed/trtllm_dist.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py` _+1 more__
- **2026-06-24** [`65d1bfb997`](https://github.com/NVIDIA/TensorRT-LLM/commit/65d1bfb997) [#15304](https://github.com/NVIDIA/TensorRT-LLM/pull/15304)
  [TRTLLM-35882][feat] cute dsl gvr-topk load-balance optimization (#15304)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_load_balance.py`, `tests/scripts/cute_dsl_kernels/top_k/run_gvr_topk.py` _+1 more__
- **2026-06-24** [`6b7f57aaf0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b7f57aaf0) [#15575](https://github.com/NVIDIA/TensorRT-LLM/pull/15575)
  [None][chore] Remove nv-internal-release guardword comments in mega_moe_nvfp4 (#15575)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/moe_persistent_scheduler.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/moe_utils.py`_
- **2026-06-24** [`cdd62303b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/cdd62303b6) [#15440](https://github.com/NVIDIA/TensorRT-LLM/pull/15440)
  [None][fix] Stabilize perf-sanity tests (#15440)
  _Files: `jenkins/scripts/perf/local/submit.py`, `tensorrt_llm/_torch/modules/fused_moe/moe_load_balancer.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus_perf_sanity.yml` _+22 more__
- **2026-06-24** [`82490479fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/82490479fa) [#15258](https://github.com/NVIDIA/TensorRT-LLM/pull/15258)
  [None][perf] Cutedsl NVF4 MOE: grouped/swiglu GEMM: Fix acc pipeline release arrive threads + FC2 meta stage code clean (#15258)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_swiglu_fusion.py`_
- **2026-06-24** [`b41876f144`](https://github.com/NVIDIA/TensorRT-LLM/commit/b41876f144) [#15381](https://github.com/NVIDIA/TensorRT-LLM/pull/15381)
  [None][feat] DSv4 prep: IndexerTopK and TopK primitives (#15381)
  _Files: `cpp/tensorrt_llm/kernels/IndexerTopK.h`, `cpp/tensorrt_llm/kernels/heuristicTopKDecode.cu`, `cpp/tensorrt_llm/kernels/heuristicTopKDecode.h`, `cpp/tensorrt_llm/kernels/indexerTopK.cu` _+4 more__
- **2026-06-22** [`e1135bbdfa`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1135bbdfa) [#15128](https://github.com/NVIDIA/TensorRT-LLM/pull/15128)
  [https://nvbugs/6273846][test] gate GPT-OSS TRTLLM Gen MoE tests to SM100/SM103 (#15128)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_

## Attention  (17 commits)

- **2026-06-28** [`5ec0c84ad1`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ec0c84ad1) [#15102](https://github.com/NVIDIA/TensorRT-LLM/pull/15102)
  [TRTLLM-13265][feat] Fuse LTX-2 Gate + Residual + Norm + AdaLN modulation(ShiftScale) + Quant kernels (#15102)
  _Files: `cpp/tensorrt_llm/kernels/fusedDiTGateResidNormShiftScaleKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTGateResidNormShiftScaleKernel.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/fusedDiTGateResidNormShiftScaleOp.cpp` _+5 more__
- **2026-06-28** [`6f7c57c6c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f7c57c6c2) [#15414](https://github.com/NVIDIA/TensorRT-LLM/pull/15414)
  [None][feat] DSv4: model, tokenizer, and integration coverage (#15414)
  _Files: `docs/source/models/supported-models.md`, `examples/models/core/deepseek_v4/README.md`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/configs/__init__.py` _+42 more__
- **2026-06-27** [`aaffa2f9fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaffa2f9fe) [#15409](https://github.com/NVIDIA/TensorRT-LLM/pull/15409)
  [None][feat] DSv4: sparse MLA attention backend (#15409)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py` _+21 more__
- **2026-06-26** [`4ab9bc54c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ab9bc54c1) [#15627](https://github.com/NVIDIA/TensorRT-LLM/pull/15627)
  [TRTLLM-12982][chore] improve multi-item scoring request validation (#15627)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/llmapi/llm.py`_
- **2026-06-26** [`2e33221d6d`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e33221d6d) [#15622](https://github.com/NVIDIA/TensorRT-LLM/pull/15622)
  [#15565][fix] AutoDeploy: Fix Super MTP IMA introduced by checkpointing replay (#15622)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/auto_deploy/shim/interface.py`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+2 more__
- **2026-06-26** [`2ee936ecb1`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ee936ecb1) [#15611](https://github.com/NVIDIA/TensorRT-LLM/pull/15611)
  [https://nvbugs/6368480][fix] Cache the SM count once in FmhaDispatcher's constructor and reuse the cached… (#15611)
  _Files: `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.h`_
- **2026-06-26** [`99f8613a7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/99f8613a7e) [#15288](https://github.com/NVIDIA/TensorRT-LLM/pull/15288)
  [TRTLLM-13247][feat] Wave 2: stage Linear and Attention transforms (#15288)
  _Files: `tensorrt_llm/_torch/memory/gpu_memory_backend.py`, `tensorrt_llm/_torch/modules/attention.py`, `tensorrt_llm/_torch/modules/linear.py`, `tests/unittest/_torch/pyexecutor/test_model_loader_gms.py` _+1 more__
- **2026-06-25** [`a02214a487`](https://github.com/NVIDIA/TensorRT-LLM/commit/a02214a487) [#15399](https://github.com/NVIDIA/TensorRT-LLM/pull/15399)
  [TRTLLM-13371][perf] LTX-2 FA4: enable split-KV heuristic (num_splits=0) for low-occupancy cross-attn (#15399)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/flash_attn4.py`_
- **2026-06-25** [`157e5339cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/157e5339cf) [#15416](https://github.com/NVIDIA/TensorRT-LLM/pull/15416)
  [TRTLLM-12982][chore] relocate `torch_multi_arange` (#15416)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+7 more__
- **2026-06-25** [`c7362be2bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7362be2bc) [#15394](https://github.com/NVIDIA/TensorRT-LLM/pull/15394)
  [None][feat] DSv4: sparse cache manager adapter (#15394)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/llmapi/__init__.py` _+5 more__
- **2026-06-25** [`70a7528cc1`](https://github.com/NVIDIA/TensorRT-LLM/commit/70a7528cc1) [#14993](https://github.com/NVIDIA/TensorRT-LLM/pull/14993)
  [https://nvbugs/6224637][fix] Enable CuTe DSL BF16 kernels for SM100 PP (#14993)
  _Files: `tensorrt_llm/_torch/modules/attention.py`, `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`bd6db6c6d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd6db6c6d8) [#15303](https://github.com/NVIDIA/TensorRT-LLM/pull/15303)
  [None][fix] LTX-2: re-enable Ulysses for v2a cross-attention (#15303)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`_
- **2026-06-24** [`660aede9c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/660aede9c4) [#15429](https://github.com/NVIDIA/TensorRT-LLM/pull/15429)
  [TRTLLM-13490][feat] Support cross-attention with FlashInfer TRTLLM-Gen kernels on Blackwell (#15429)
  _Files: `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/trtllmGenFusedOps.h`, `cpp/tensorrt_llm/thop/trtllmGenQKVProcessOp.cpp` _+8 more__
- **2026-06-24** [`1d4648c661`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d4648c661) [#14829](https://github.com/NVIDIA/TensorRT-LLM/pull/14829)
  [TRTLLM-13123][feat] CUDA graph wrapper for multimodal encoders (#14829)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/_torch/models/modeling_radio.py` _+13 more__
- **2026-06-24** [`270800978e`](https://github.com/NVIDIA/TensorRT-LLM/commit/270800978e) [#15413](https://github.com/NVIDIA/TensorRT-LLM/pull/15413)
  [TRTLLM-12982][perf] reuse multi-item scoring position_ids and params (#15413)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/star_flashinfer.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+5 more__
- **2026-06-24** [`29d08276db`](https://github.com/NVIDIA/TensorRT-LLM/commit/29d08276db) [#15379](https://github.com/NVIDIA/TensorRT-LLM/pull/15379)
  [None][feat] DSv4 prep: compressor and mHC primitives (#15379)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/compressorKernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu` _+21 more__
- **2026-06-23** [`439ad220b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/439ad220b1) [#15456](https://github.com/NVIDIA/TensorRT-LLM/pull/15456)
  [None][fix] AutoDeploy: handle torch dist all_gather in multi_stream MLA transform (#15456)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/multi_stream_attn.py`, `tests/unittest/auto_deploy/singlegpu/custom_ops/test_multi_stream_attn.py`_

## Torch Path (_torch)  (15 commits)

- **2026-06-29** [`f2160af48d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f2160af48d) [#15670](https://github.com/NVIDIA/TensorRT-LLM/pull/15670)
  [None][chore] split unittest/_torch/visual_gen (#15670)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-06-29** [`b02b6b4642`](https://github.com/NVIDIA/TensorRT-LLM/commit/b02b6b4642) [#15626](https://github.com/NVIDIA/TensorRT-LLM/pull/15626)
  [None][perf] DSv4 follow-up: autotuner updates (#15626)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/modules/mhc/mhc_cuda.py`, `tests/unittest/_torch/misc/test_autotuner.py` _+1 more__
- **2026-06-26** [`24be596d76`](https://github.com/NVIDIA/TensorRT-LLM/commit/24be596d76) [#15361](https://github.com/NVIDIA/TensorRT-LLM/pull/15361)
  [TRTLLM-12762][test] Add Test coverage for MiniMax Model with multi-node, M2.5 checkpoints eval (#15361)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+2 more__
- **2026-06-25** [`edb14ee3f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/edb14ee3f2) [#15593](https://github.com/NVIDIA/TensorRT-LLM/pull/15593)
  [TRTLLM-13612][test] Remove unreferenced accuracy tests and orphaned … (#15593)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-06-25** [`407cbc0c70`](https://github.com/NVIDIA/TensorRT-LLM/commit/407cbc0c70) [#15586](https://github.com/NVIDIA/TensorRT-LLM/pull/15586)
  [TRTLLM-13601][test] Clean up Nemotron test cases (#15586)
  _Files: `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api.py` _+8 more__
- **2026-06-25** [`b37a5aa75f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b37a5aa75f) [#15583](https://github.com/NVIDIA/TensorRT-LLM/pull/15583)
  [https://nvbugs/6274932] [fix] Fix and unwaive step3p7 test cases (#15583)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-25** [`1b9c66a789`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b9c66a789) [#13170](https://github.com/NVIDIA/TensorRT-LLM/pull/13170)
  [TRTLLM-11353][feat] API to configure TeaCache coefficients (#13170)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/cache/teacache_accelerator.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux2.py` _+12 more__
- **2026-06-25** [`e828cac8f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/e828cac8f3) [#15559](https://github.com/NVIDIA/TensorRT-LLM/pull/15559)
  [#12715][fix] Disable NCCL window buffers on GB10 (#15559)
  _Files: `cpp/tensorrt_llm/common/ncclUtils.cpp`, `cpp/tensorrt_llm/common/ncclUtils.h`, `cpp/tests/unit_tests/multi_gpu/ncclUtilsTest.cpp`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py` _+1 more__
- **2026-06-24** [`f28a832214`](https://github.com/NVIDIA/TensorRT-LLM/commit/f28a832214) [#15527](https://github.com/NVIDIA/TensorRT-LLM/pull/15527)
  [https://nvbugs/6276842][test] Loosen rtol/atol on encoder CUDA graph logits parity check (#15527)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_encode.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`f75d79583d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f75d79583d) [#14706](https://github.com/NVIDIA/TensorRT-LLM/pull/14706)
  [None][fix] fix FA4 install in devel docker (#14706)
  _Files: `docker/Dockerfile.multi`, `docker/common/install_fa4.sh`, `jenkins/current_image_tags.properties`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-06-24** [`dd13680a9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd13680a9a) [#14710](https://github.com/NVIDIA/TensorRT-LLM/pull/14710)
  [https://nvbugs/6185146][fix] Use `mat_a.new_empty([m, n_out//2])` / `input_scale.new_empty([sf_size])` in the (#14710)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/modules/gated_mlp.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-24** [`9e9137f314`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e9137f314) [#15545](https://github.com/NVIDIA/TensorRT-LLM/pull/15545)
  [None][fix] Fix passing scaled timestep to time_embedder in Cosmos3 (#15545)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`_
- **2026-06-24** [`0ff7b4acba`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ff7b4acba) [#15294](https://github.com/NVIDIA/TensorRT-LLM/pull/15294)
  [https://nvbugs/6264844][fix] Fix wrong NCCL fallback in nemotron-h (#15294)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`_
- **2026-06-24** [`aeb169a637`](https://github.com/NVIDIA/TensorRT-LLM/commit/aeb169a637) [#15170](https://github.com/NVIDIA/TensorRT-LLM/pull/15170)
  [None][test] fix Cosmos3 tests after VisualGen config split (#15170)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/test_cosmos3_pipeline.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_transformer.py`_
- **2026-06-22** [`f7dd7ec542`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7dd7ec542) [#15229](https://github.com/NVIDIA/TensorRT-LLM/pull/15229)
  [None][feat] VisualGen: async mp4 encode + fixed noise latent via env vars (#15229)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tensorrt_llm/serve/openai_video_routes.py`_

## Executor / Runtime  (14 commits)

- **2026-06-29** [`d913524adf`](https://github.com/NVIDIA/TensorRT-LLM/commit/d913524adf) [#14246](https://github.com/NVIDIA/TensorRT-LLM/pull/14246)
  [TRTLLM-12751][feat] visual-gen /metrics iteration stats producer (#14246)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/visual_gen/visual_gen.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+2 more__
- **2026-06-28** [`aa9297b587`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa9297b587) [#15302](https://github.com/NVIDIA/TensorRT-LLM/pull/15302)
  [None][fix] Fall back to NVLink P2P when NVLS fabric is unprovisioned (#15302)
  _Files: `cpp/include/tensorrt_llm/runtime/ipcNvlsMemory.h`, `cpp/tensorrt_llm/common/opUtils.cpp`, `cpp/tensorrt_llm/runtime/ipcNvlsMemory.cu`_
- **2026-06-28** [`27cabe56f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/27cabe56f1) [#14815](https://github.com/NVIDIA/TensorRT-LLM/pull/14815)
  [None][feat] Support inflight weight update (#14815)
  _Files: `tensorrt_llm/_ray_utils.py`, `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+1 more__
- **2026-06-26** [`0722c5f47d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0722c5f47d) [#15546](https://github.com/NVIDIA/TensorRT-LLM/pull/15546)
  [https://nvbugs/6293536][fix] Stage KV block offsets through a fresh host buffer (#15546)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/test_kv_block_offset_overlap_race.py`_
- **2026-06-26** [`d73862a3b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/d73862a3b0) [#14837](https://github.com/NVIDIA/TensorRT-LLM/pull/14837)
  [TRTLLM-13712][feat] Add Qwen-Image-Bench evaluator (#14837)
  _Files: `examples/models/core/multimodal/README.md`, `examples/models/core/multimodal/qwen_image_bench_eval.py`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py` _+9 more__
- **2026-06-25** [`85fc146683`](https://github.com/NVIDIA/TensorRT-LLM/commit/85fc146683) [#15629](https://github.com/NVIDIA/TensorRT-LLM/pull/15629)
  Revert "[TRTLLM-12622][feat] Add native post-processing hook to trtllm-serve" (#15629)
  _Files: `docs/source/features/post-processor-hook.md`, `docs/source/index.rst`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/postproc_worker.py` _+15 more__
- **2026-06-25** [`a8f0efc57f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8f0efc57f) [#15589](https://github.com/NVIDIA/TensorRT-LLM/pull/15589)
  [https://nvbugs/6346546][fix] fix mRoPE CUDA graph gate for text requests (#15589)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`_
- **2026-06-25** [`ca81b2a5ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca81b2a5ea) [#15106](https://github.com/NVIDIA/TensorRT-LLM/pull/15106)
  [None][feat] Add BaseResourceManager-based KV-cache compression manager framework (#15106)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+2 more__
- **2026-06-24** [`5e9b88d0ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e9b88d0ff) [#15239](https://github.com/NVIDIA/TensorRT-LLM/pull/15239)
  [TRTLLM-12622][feat] Add native post-processing hook to trtllm-serve (#15239)
  _Files: `docs/source/features/post-processor-hook.md`, `docs/source/index.rst`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/postproc_worker.py` _+15 more__
- **2026-06-23** [`8412a17e38`](https://github.com/NVIDIA/TensorRT-LLM/commit/8412a17e38) [#15254](https://github.com/NVIDIA/TensorRT-LLM/pull/15254)
  [#10710][fix] clarify and align trtllm-bench runtime logging  (#15254)
  _Files: `tensorrt_llm/bench/benchmark/low_latency.py`, `tensorrt_llm/bench/benchmark/throughput.py`, `tensorrt_llm/bench/benchmark/utils/general.py`_
- **2026-06-23** [`beb922f98a`](https://github.com/NVIDIA/TensorRT-LLM/commit/beb922f98a) [#15461](https://github.com/NVIDIA/TensorRT-LLM/pull/15461)
  [None][fix] Fix encoder-decoder beam search corruption via per-slot fragmentPointerDevice (#15461)
  _Files: `cpp/include/tensorrt_llm/batch_manager/runtimeBuffers.h`, `cpp/tensorrt_llm/batch_manager/runtimeBuffers.cpp`, `cpp/tensorrt_llm/batch_manager/trtGptModelInflightBatching.cpp`, `cpp/tensorrt_llm/batch_manager/utils/inflightBatchingUtils.cpp` _+2 more__
- **2026-06-23** [`683a70c17a`](https://github.com/NVIDIA/TensorRT-LLM/commit/683a70c17a) [#14160](https://github.com/NVIDIA/TensorRT-LLM/pull/14160)
  [TRTLLM-13550][feat] WideEP FT: add MPI signal handler replacement (1d.0) (#14160)
  _Files: `cpp/include/tensorrt_llm/runtime/utils/mpiUtils.h`, `cpp/tensorrt_llm/runtime/utils/mpiUtils.cpp`, `cpp/tests/unit_tests/runtime/CMakeLists.txt`, `cpp/tests/unit_tests/runtime/mpiUtilsTest.cpp`_
- **2026-06-22** [`9ed7ce468b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ed7ce468b) [#15471](https://github.com/NVIDIA/TensorRT-LLM/pull/15471)
  [https://nvbugs/6337235][test] Fix MX/GMS model loader fixtures (#15471)
  _Files: `tests/unittest/_torch/pyexecutor/test_model_loader_gms.py`, `tests/unittest/_torch/pyexecutor/test_model_loader_mx.py`_
- **2026-06-22** [`e47359c4fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e47359c4fd) [#15423](https://github.com/NVIDIA/TensorRT-LLM/pull/15423)
  [None][fix] AutoDeploy: Fixed wrong dist_backend AUTO detection when using trtllm-llmapi-launch (#15423)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/distributed/trtllm_dist.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/sharding.py`, `tests/unittest/auto_deploy/multigpu/transformations/library/test_dist_backend.py`_

## Models  (14 commits)

- **2026-06-29** [`798989ab79`](https://github.com/NVIDIA/TensorRT-LLM/commit/798989ab79) [#15646](https://github.com/NVIDIA/TensorRT-LLM/pull/15646)
  [None][chore] Decrease the qwen3.5 ci test time (#15646)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-06-26** [`a9f90a4f53`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9f90a4f53) [#15567](https://github.com/NVIDIA/TensorRT-LLM/pull/15567)
  [https://nvbugs/6344612][test] relax GPT-OSS GPQA references due to high variance in random sampling (#15567)
  _Files: `tests/integration/defs/accuracy/references/gpqa_diamond.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-06-26** [`4164b932c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4164b932c6) [#15652](https://github.com/NVIDIA/TensorRT-LLM/pull/15652)
  [https://nvbugs/6248783][test] Unwaive Qwen3 skip softmax test (#15652)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-26** [`0937da20a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0937da20a1) [#15481](https://github.com/NVIDIA/TensorRT-LLM/pull/15481)
  [https://nvbugs/6239637][fix] Unwaive Qwen3.5 cases on A100 platform (#15481)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-26** [`0425801b33`](https://github.com/NVIDIA/TensorRT-LLM/commit/0425801b33) [#15566](https://github.com/NVIDIA/TensorRT-LLM/pull/15566)
  [#15613][fix] Gemma4 multimodal: fix vision TP and xgrammar startup crashes (#15566)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4_vision.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`_
- **2026-06-26** [`29e4b658bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/29e4b658bb) [#15580](https://github.com/NVIDIA/TensorRT-LLM/pull/15580)
  [TRTLLM-13444][test] Add Qwen-Image text-to-image unit tests (#15580)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/visual_gen/test_qwen_image_infer.py`, `tests/unittest/_torch/visual_gen/test_qwen_image_pipeline.py`_
- **2026-06-25** [`6fbe366ceb`](https://github.com/NVIDIA/TensorRT-LLM/commit/6fbe366ceb) [#15591](https://github.com/NVIDIA/TensorRT-LLM/pull/15591)
  [TRTLLM-13600][test] Clean up Qwen3 test cases (#15591)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml` _+1 more__
- **2026-06-25** [`948db5a82a`](https://github.com/NVIDIA/TensorRT-LLM/commit/948db5a82a) [#15240](https://github.com/NVIDIA/TensorRT-LLM/pull/15240)
  [https://nvbugs/6256531][test] Unwaive Llama guided decoding xgrammar (#15240)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-25** [`4c4c74a09e`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c4c74a09e) [#15206](https://github.com/NVIDIA/TensorRT-LLM/pull/15206)
  [https://nvbugs/6094068][fix] Fix Qwen3-Next bf16 4gpu test (#15206)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-25** [`158d684c62`](https://github.com/NVIDIA/TensorRT-LLM/commit/158d684c62) [#15180](https://github.com/NVIDIA/TensorRT-LLM/pull/15180)
  [#15179][fix] Add necessary methods for guided decoding in Kimi K2.5 (#15180)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`_
- **2026-06-24** [`214aa51683`](https://github.com/NVIDIA/TensorRT-LLM/commit/214aa51683) [#15322](https://github.com/NVIDIA/TensorRT-LLM/pull/15322)
  [None][chore] Small cleanups to MultimodalModelMixin (#15322)
  _Files: `tensorrt_llm/_torch/models/modeling_mistral.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tests/unittest/_torch/multimodal/test_mm_encoder_cross_iter_prefetch.py` _+1 more__
- **2026-06-24** [`654fb29350`](https://github.com/NVIDIA/TensorRT-LLM/commit/654fb29350) [#15544](https://github.com/NVIDIA/TensorRT-LLM/pull/15544)
  [TRTLLM-13599][test] Refine Qwen3.5 test cases (#15544)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+6 more__
- **2026-06-24** [`01622f6e85`](https://github.com/NVIDIA/TensorRT-LLM/commit/01622f6e85)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-06-24** [`77752ea751`](https://github.com/NVIDIA/TensorRT-LLM/commit/77752ea751) [#15453](https://github.com/NVIDIA/TensorRT-LLM/pull/15453)
  [https://nvbugs/6271740][test] Update llm_perf_core.yml to include new performance test for DeepSeek R1 0528 FP4 model (#15453)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Quantization  (12 commits)

- **2026-06-29** [`70c5e430c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/70c5e430c8) [#15659](https://github.com/NVIDIA/TensorRT-LLM/pull/15659)
  [None][fix] GLM-5.1 NVFP4 fallback to AR-Norm fusion for unquantized dense layers (#15659)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`_
- **2026-06-28** [`85665f5fd3`](https://github.com/NVIDIA/TensorRT-LLM/commit/85665f5fd3)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+41 more__
- **2026-06-27** [`434dc3345d`](https://github.com/NVIDIA/TensorRT-LLM/commit/434dc3345d) [#15421](https://github.com/NVIDIA/TensorRT-LLM/pull/15421)
  [https://nvbugs/6301807][fix] Fix FP8 rowwise linear reference precision (#15421)
  _Files: `tests/unittest/_torch/thop/parallel/test_fp8_rowwise_linear.py`_
- **2026-06-26** [`4b7b5ce7d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b7b5ce7d3) [#15299](https://github.com/NVIDIA/TensorRT-LLM/pull/15299)
  [TRTLLM-13370][perf] LTX2 + WAN: Fuse MLP up-GEMM + bias + GELU(tanh) + NVFP4-quant into CuteDSL epilogue (#15299)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_blockscaled_gemm_act_fusion.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/utils.py`, `tensorrt_llm/_torch/modules/linear.py` _+6 more__
- **2026-06-26** [`d419595e40`](https://github.com/NVIDIA/TensorRT-LLM/commit/d419595e40) [#15650](https://github.com/NVIDIA/TensorRT-LLM/pull/15650)
  [None][test] Add Qwen3.5-397B-A17B-NVFP4 B200 aggregated perf-sanity tests (#15650)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml`, `tests/scripts/perf-sanity/aggregated/qwen3_5_397b_fp4_blackwell.yaml`_
- **2026-06-26** [`3f1659c1ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f1659c1ba) [#15437](https://github.com/NVIDIA/TensorRT-LLM/pull/15437)
  [None][test] add GLM nvfp4 stress test (#15437)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp4ep4_gentp4ep4_glm5_nvfp4_dp_tllm.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_stress.txt`_
- **2026-06-26** [`5731f65572`](https://github.com/NVIDIA/TensorRT-LLM/commit/5731f65572)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+45 more__
- **2026-06-25** [`c346995a86`](https://github.com/NVIDIA/TensorRT-LLM/commit/c346995a86)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+49 more__
- **2026-06-24** [`ccabbea3d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccabbea3d5) [#15235](https://github.com/NVIDIA/TensorRT-LLM/pull/15235)
  [None][feat] Add Qwen Image visual generation examples (#15235)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/configs/qwen-image-fp8-1gpu.yaml`, `examples/visual_gen/models/qwen_image.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen.py` _+1 more__
- **2026-06-24** [`8607f16982`](https://github.com/NVIDIA/TensorRT-LLM/commit/8607f16982) [#15393](https://github.com/NVIDIA/TensorRT-LLM/pull/15393)
  [https://nvbugs/6156233][fix] Lower GSM8K reference for the three GPT-OSS/20B-MXFP4 entries with… (#15393)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media.zip`, `tests/integration/test_lists/waives.txt`_
- **2026-06-23** [`93feb57eca`](https://github.com/NVIDIA/TensorRT-LLM/commit/93feb57eca) [#15382](https://github.com/NVIDIA/TensorRT-LLM/pull/15382)
  [None][feat] Add Gemma-4 NVFP4 quantized models to AutoDeploy registry (#15382)
  _Files: `examples/auto_deploy/model_registry/models.yaml`_
- **2026-06-22** [`a8c595521e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8c595521e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/lookahead/poetry.lock` _+35 more__

## Other  (7 commits)

- **2026-06-29** [`20e0e915e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/20e0e915e1) [#15663](https://github.com/NVIDIA/TensorRT-LLM/pull/15663)
  [None][test] record per-case hostname in perf result CSV (#15663)
  _Files: `tests/integration/defs/perf/utils.py`_
- **2026-06-26** [`8e6a089d5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e6a089d5f) [#15596](https://github.com/NVIDIA/TensorRT-LLM/pull/15596)
  [https://nvbugs/6062416][fix] Cache NCCL window allocation failures by size (#15596)
  _Files: `cpp/tensorrt_llm/common/ncclUtils.cpp`, `cpp/tensorrt_llm/common/ncclUtils.h`, `cpp/tests/unit_tests/multi_gpu/ncclUtilsTest.cpp`_
- **2026-06-26** [`c766fc27d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c766fc27d0) [#11685](https://github.com/NVIDIA/TensorRT-LLM/pull/11685)
  [None][fix] User/tjohnsen/evict empty blocks first (#11685)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`_
- **2026-06-23** [`07270b7e9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/07270b7e9e) [#15427](https://github.com/NVIDIA/TensorRT-LLM/pull/15427)
  [https://nvbugs/6290345][fix] Fix allreduce benchmark input setup (#15427)
  _Files: `tests/microbenchmarks/all_reduce.py`_
- **2026-06-23** [`0996d9d8e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0996d9d8e5) [#12294](https://github.com/NVIDIA/TensorRT-LLM/pull/12294)
  [#3237][fix] Support negative numbers in MajorityVote digit validation (#12294)
  _Files: `tensorrt_llm/scaffolding/math_utils.py`, `tests/unittest/scaffolding/test_math_utils.py`_
- **2026-06-22** [`eddaa3ad45`](https://github.com/NVIDIA/TensorRT-LLM/commit/eddaa3ad45) [#15517](https://github.com/NVIDIA/TensorRT-LLM/pull/15517)
  [None][fix] avoid type checking failures due to pip dependency resolution (#15517)
  _Files: `requirements-dev.txt`_
- **2026-06-22** [`2e6abd183e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e6abd183e) [#15422](https://github.com/NVIDIA/TensorRT-LLM/pull/15422)
  [https://nvbugs/6179661][fix] Harden disagg cache transceiver teardown (#15422)
  _Files: `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.cpp`_

## Disaggregation / KV  (7 commits)

- **2026-06-28** [`b6eacd1f72`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6eacd1f72) [#15356](https://github.com/NVIDIA/TensorRT-LLM/pull/15356)
  [TRTLLM-12721][fix] Bound V2 context transfer polling (#15356)
  _Files: `cpp/include/tensorrt_llm/batch_manager/disaggTransferAdmissionController.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp` _+22 more__
- **2026-06-25** [`33bf59e49f`](https://github.com/NVIDIA/TensorRT-LLM/commit/33bf59e49f) [#14646](https://github.com/NVIDIA/TensorRT-LLM/pull/14646)
  [https://nvbugs/6021427][fix] BREAKING CHANGE: Make request chat_template opt-in (#14646)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/serve/openai_disagg_server.py`, `tensorrt_llm/serve/openai_protocol.py` _+4 more__
- **2026-06-25** [`f193c7b9e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/f193c7b9e7) [#15222](https://github.com/NVIDIA/TensorRT-LLM/pull/15222)
  [None][feat] Dis-agg transceiver mass integration from the DSV4 branch (#15222)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/agentBindings.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.h`, `cpp/tests/unit_tests/executor/transferAgentTest.cpp` _+20 more__
- **2026-06-25** [`970df5b8c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/970df5b8c7) [#15301](https://github.com/NVIDIA/TensorRT-LLM/pull/15301)
  [None][test] GPT-OSS disagg test for transceiver v2 (#15301)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml`_
- **2026-06-24** [`eb0cbdb74b`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb0cbdb74b) [#15378](https://github.com/NVIDIA/TensorRT-LLM/pull/15378)
  [None][feat] DSv4 prep: runtime cache foundations (#15378)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `tensorrt_llm/_torch/auto_deploy/_compat.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+32 more__
- **2026-06-24** [`4768e6febc`](https://github.com/NVIDIA/TensorRT-LLM/commit/4768e6febc) [#15539](https://github.com/NVIDIA/TensorRT-LLM/pull/15539)
  [https://nvbugs/6344108][fix] skip TestNemotron3Super120B on pre-blackwell (#15539)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`_
- **2026-06-23** [`e2c7c4f496`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2c7c4f496) [#15443](https://github.com/NVIDIA/TensorRT-LLM/pull/15443)
  [None][test] Un-waive K2.5 Thinking FP4 disagg-NIXL e2e/gen_only tests (#15443)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_kimi-k25-thinking-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp0_ccb-NIXL.yaml`_

## Speculative Decoding  (4 commits)

- **2026-06-26** [`69ea407eb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/69ea407eb3) [#15017](https://github.com/NVIDIA/TensorRT-LLM/pull/15017)
  [https://nvbugs/6269778][fix] Fix overallocation of draft KV cache (#15017)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/__init__.py`, `tensorrt_llm/_torch/speculative/utils.py`, `tensorrt_llm/llmapi/llm_args.py` _+2 more__
- **2026-06-26** [`9c7492db7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c7492db7a) [#15153](https://github.com/NVIDIA/TensorRT-LLM/pull/15153)
  [https://nvbugs/6274614][fix] remove spec tokens env for stress test (#15153)
  _Files: `tests/scripts/perf/disaggregated/gb200_stress-gpt-oss-120b-fp4_8k1k_ctx1_tp1_gen1_tp4_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_1k1k_ctx2_gen1_dep16_bs128_eplb288_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_8k1k_ctx2_gen1_dep32_bs128_eplb288_mtp3_ccb-NIXL.yaml`_
- **2026-06-24** [`1047091fcb`](https://github.com/NVIDIA/TensorRT-LLM/commit/1047091fcb) [#14988](https://github.com/NVIDIA/TensorRT-LLM/pull/14988)
  [None][feat] Eagle 3.1 -- Support post-norm and per-aux fc_norm for Eagle3 draft models (#14988)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`_
- **2026-06-23** [`2965eca42b`](https://github.com/NVIDIA/TensorRT-LLM/commit/2965eca42b) [#15325](https://github.com/NVIDIA/TensorRT-LLM/pull/15325)
  [https://nvbugs/6306936][test] Re-enable AutoDeploy disagg tests (#15325)
  _Files: `examples/auto_deploy/model_registry/configs/super_v3_mtp.yaml`, `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tests/integration/defs/disaggregated/test_ad_disagg.py`, `tests/integration/defs/disaggregated/test_ad_disagg_trtllm_serve.py` _+4 more__

## Docs / Examples  (3 commits)

- **2026-06-26** [`09a8d57484`](https://github.com/NVIDIA/TensorRT-LLM/commit/09a8d57484) [#15606](https://github.com/NVIDIA/TensorRT-LLM/pull/15606)
  [None][chore] Update .gitattributes (#15606)
  _Files: `.gitattributes`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media.zip`_
- **2026-06-25** [`3069bcb331`](https://github.com/NVIDIA/TensorRT-LLM/commit/3069bcb331) [#15236](https://github.com/NVIDIA/TensorRT-LLM/pull/15236)
  [https://nvbugs/6215688][fix] Fix visual gen test leaked issue (#15236)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen.py`_
- **2026-06-23** [`eb2bddd894`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb2bddd894) [#15551](https://github.com/NVIDIA/TensorRT-LLM/pull/15551)
  [None][chore] Bump version to 1.3.0rc20 (#15551)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## LoRA  (1 commits)

- **2026-06-29** [`8d9c890e50`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d9c890e50) [#14984](https://github.com/NVIDIA/TensorRT-LLM/pull/14984)
  [None][feat] Cache LTX2 merged LoRA weight (#14984)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_

## Perf  (1 commits)

- **2026-06-26** [`a6f29f500e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6f29f500e) [#15587](https://github.com/NVIDIA/TensorRT-LLM/pull/15587)
  [None][doc] Add deploy guide for Minimax M3 (#15587)
  _Files: `docs/source/_static/config_db.json`, `docs/source/deployment-guide/deployment-guide-for-minimax-m3-on-trtllm.md`, `docs/source/deployment-guide/index.rst`, `docs/source/models/supported-models.md` _+3 more__

## AutoDeploy  (1 commits)

- **2026-06-26** [`3e10db96f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e10db96f0) [#15630](https://github.com/NVIDIA/TensorRT-LLM/pull/15630)
  [None][infra] AutoDeploy: Add trtllm runner for standalone llm-c (#15630)
  _Files: `examples/auto_deploy/llmc/create_standalone_package.py`_

---
_Generated 2026-06-29 12:45 UTC_