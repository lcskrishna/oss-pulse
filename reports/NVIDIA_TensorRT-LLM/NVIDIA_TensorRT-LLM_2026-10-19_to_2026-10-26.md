# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-10-19 → 2026-10-26  |  **Total commits:** 221

## ✨ New Features This Week

- **2026-10-26** [#20209](https://github.com/NVIDIA/TensorRT-LLM/pull/20209) — [None][feat] Add the PrimTS native sparse MLA FMHA for DeepSeek-V4 generation and enable it by default on SM100 (#20209)
- **2026-10-26** [#20178](https://github.com/NVIDIA/TensorRT-LLM/pull/20178) — [None][feat] Unified kv cache manager foundation (#20178)
- **2026-10-25** [#20213](https://github.com/NVIDIA/TensorRT-LLM/pull/20213) — [None][perf] enable Qwen3.*-VL encoder CUDA graphs via shared setup (#20213)
- **2026-10-24** [#19961](https://github.com/NVIDIA/TensorRT-LLM/pull/19961) — [None][feat] DeepSeek V4 / DSpark optimizations on Rubin (#19961)
- **2026-10-24** [#20517](https://github.com/NVIDIA/TensorRT-LLM/pull/20517) — [None][feat] Staircase: GLM-5.2 NVFP4 low-latency decode target for Rubin (modeling_v2, TP16) (#20517)
- **2026-10-23** [#20307](https://github.com/NVIDIA/TensorRT-LLM/pull/20307) — [None][feat] Add Cosmos3-Edge Reasoner support (#20307)
- **2026-10-23** [#17147](https://github.com/NVIDIA/TensorRT-LLM/pull/17147) — [None][feat] Qwen Image Ulysses perf enhancement (#17147)
- **2026-10-23** [#20452](https://github.com/NVIDIA/TensorRT-LLM/pull/20452) — [TRTLLM-17204][feat] Add First-N/Last-N mixed-precision KV caching using native SWA in KVCM V2 (#20452)
- **2026-10-23** [#20075](https://github.com/NVIDIA/TensorRT-LLM/pull/20075) — [TRTLLM-16958][feat] MXFP8 refit with PCG changes, recompute_active_requests, Ray collectives (#20075)
- **2026-10-23** [#20688](https://github.com/NVIDIA/TensorRT-LLM/pull/20688) — [None][perf] Add torch.compile decorator for mamba replay input prep (#20688)
- _…and 31 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-25** [`b7d6e624d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7d6e624d1) [#20953](https://github.com/NVIDIA/TensorRT-LLM/pull/20953) — [None][infra] Waive 70 failed cases for main in pre-merge 66148 (function-level waives for test_lora_ownership) (#20953)
- **2026-10-24** [`87342f4474`](https://github.com/NVIDIA/TensorRT-LLM/commit/87342f4474) [#20270](https://github.com/NVIDIA/TensorRT-LLM/pull/20270) — [TRTLLM-15763][refactor] Narrow the runner surface, slim engine state, and make the engine's executor interface explicit (#20270)
- **2026-10-23** [`448321fb98`](https://github.com/NVIDIA/TensorRT-LLM/commit/448321fb98) [#20605](https://github.com/NVIDIA/TensorRT-LLM/pull/20605) — [https://nvbugs/6913865][fix] Scope multimodal LoRA to the decoder (#20605)
- **2026-10-22** [`27842d513c`](https://github.com/NVIDIA/TensorRT-LLM/commit/27842d513c) [#19822](https://github.com/NVIDIA/TensorRT-LLM/pull/19822) — [None][chore] Share KV transfer lifecycle enforcement primitives (#19822)
- **2026-10-21** [`a9000fe10e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9000fe10e) [#20117](https://github.com/NVIDIA/TensorRT-LLM/pull/20117) — [TRTLLM-16186][feat] Define backend contract for KV cache transfers (#20117)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#20083](https://github.com/NVIDIA/TensorRT-LLM/issues/20083) | [Bug]: Ray orchestrator: NcclEP builds its EP communicator from MPI_CO | Inference runtime, Disaggregated serving | 2026-10-25 |
| [#20944](https://github.com/NVIDIA/TensorRT-LLM/issues/20944) | [Bug]: trtllm-gen FMHA JIT bundles CUDA 13.4 headers, but the wheel ac | Customized kernels, Pytorch | 2026-10-24 |
| [#20376](https://github.com/NVIDIA/TensorRT-LLM/issues/20376) | [Bug]: Grouped MLA generation cubins are registered as Dense in kernel | Customized kernels | 2026-10-23 |
| [#19994](https://github.com/NVIDIA/TensorRT-LLM/issues/19994) | [Feature]: Whisper serving parity in trtllm-serve — /v1/audio/transcri | LLM API, OpenAI API | 2026-10-19 |
| [#20586](https://github.com/NVIDIA/TensorRT-LLM/issues/20586) | [Bug]: DeepSeek-V4.1 vision tower fails on SM107: cuDNN SDPA "No valid | Customized kernels, Pytorch | 2026-10-19 |
| [#20508](https://github.com/NVIDIA/TensorRT-LLM/issues/20508) | [Bug]: FP8 block-scale Linear hits a device-side assert on SM107: Deep | Customized kernels, Pytorch | 2026-10-17 |
| [#20504](https://github.com/NVIDIA/TensorRT-LLM/issues/20504) | [Bug]: Breakable prefill CUDA graphs replay corrupted outputs for some | Customized kernels | 2026-10-17 |
| [#20407](https://github.com/NVIDIA/TensorRT-LLM/issues/20407) | [Feature]: Structured profiling metadata for distributed inference tra | feature request, Scale-out | 2026-10-15 |
| [#20237](https://github.com/NVIDIA/TensorRT-LLM/issues/20237) | [New Model]: Add pplx-decider support | feature request, new model | 2026-10-13 |
| [#20138](https://github.com/NVIDIA/TensorRT-LLM/issues/20138) | [Bug]: Qwen3-VL E/PD handoff drops per-frame timestamp tokens and fram | Disaggregated serving, Multimodal | 2026-10-12 |
| [#19634](https://github.com/NVIDIA/TensorRT-LLM/issues/19634) | [Bug]: multi-node trtllm-serve with the MPI orchestrator (trtllm-llmap | Inference runtime, Disaggregated serving | 2026-10-10 |
| [#20082](https://github.com/NVIDIA/TensorRT-LLM/issues/20082) | [Bug]: Ray orchestrator with attention DP and TRTLLM_FORCE_COMM_METHOD | Disaggregated serving, Scale-out | 2026-10-10 |
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-10-08 |
| [#19913](https://github.com/NVIDIA/TensorRT-LLM/issues/19913) | [Bug]: Upgrade XGrammar: qwen_xml compilation errors and tool-call loo | bug, Customized kernels | 2026-10-07 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-10-05 |
| [#19820](https://github.com/NVIDIA/TensorRT-LLM/issues/19820) | [New Model]: Apertus (swiss-ai/Apertus-8B-Instruct-2509, swiss-ai/Aper | new model | 2026-10-02 |
| [#19666](https://github.com/NVIDIA/TensorRT-LLM/issues/19666) | [Feature]: EFA should work out of the box on NGC TRTLLM release image  | feature request, OOTB | 2026-10-01 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-10-01 |
| [#19726](https://github.com/NVIDIA/TensorRT-LLM/issues/19726) | [Feature][RFC]: Compact active beam rows during VBWS decode in the PyT | Pytorch, Model optimization | 2026-09-30 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-09-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 50 |
| Attention | 41 |
| Executor / Runtime | 27 |
| MoE | 25 |
| Disaggregation / KV | 17 |
| Other | 14 |
| Torch Path (_torch) | 11 |
| Quantization | 9 |
| Models | 7 |
| LoRA | 6 |
| ROCm / AMD | 5 |
| Docs / Examples | 4 |
| Speculative Decoding | 3 |
| Compilation / Graph | 2 |

## CI / Infra  (50 commits)

- **2026-10-26** [`8053da26e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/8053da26e0) [#20666](https://github.com/NVIDIA/TensorRT-LLM/pull/20666)
  [TRTLLMINF-471][infra] use Austin model scratch for RTX5080, RTXPro6000D and GH200 (#20666)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-26** [`3614f68c39`](https://github.com/NVIDIA/TensorRT-LLM/commit/3614f68c39) [#20786](https://github.com/NVIDIA/TensorRT-LLM/pull/20786)
  [None][test] Remove 87 closed-bug waive entries for main (#20786)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-26** [`49c8fad919`](https://github.com/NVIDIA/TensorRT-LLM/commit/49c8fad919) [#20985](https://github.com/NVIDIA/TensorRT-LLM/pull/20985)
  [https://nvbugs/6826000][test] Remove the AgentX cases from the perf-sanity test lists (#20985)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus_perf_sanity.yml` _+7 more__
- **2026-10-26** [`bb8392995e`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb8392995e)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-10-26** [`b4bfc2f937`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4bfc2f937) [#20584](https://github.com/NVIDIA/TensorRT-LLM/pull/20584)
  [TRTLLMINF-133][infra] Move check testlist stage earlier in CI (#20584)
  _Files: `.pre-commit-config.yaml`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/ci_versions.properties` _+7 more__
- **2026-10-25** [`d876934bb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/d876934bb4) [#20959](https://github.com/NVIDIA/TensorRT-LLM/pull/20959)
  [None][infra] Waive 1 failed cases for main in pre-merge 66075 (#20959)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-25** [`0cb26c4dcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/0cb26c4dcd) [#20960](https://github.com/NVIDIA/TensorRT-LLM/pull/20960)
  [None][infra] Waive 1 failed cases for main in pre-merge 65959 (#20960)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-24** [`fe180a952d`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe180a952d) [#20899](https://github.com/NVIDIA/TensorRT-LLM/pull/20899)
  [None][infra] restore B200 multi-GPU stages (#20899)
  _Files: `jenkins/config/maintenance_stages.txt`_
- **2026-10-24** [`a8094061ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8094061ae) [#20935](https://github.com/NVIDIA/TensorRT-LLM/pull/20935)
  [None][infra] Waive 1 failed cases for main in pre-merge 66096 (#20935)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-24** [`0456f8ff9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0456f8ff9a) [#20927](https://github.com/NVIDIA/TensorRT-LLM/pull/20927)
  [None][infra] Waive 1 failed cases for main in pre-merge 66029 (#20927)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-23** [`f298722651`](https://github.com/NVIDIA/TensorRT-LLM/commit/f298722651)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-10-23** [`9619d5b2ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/9619d5b2ee) [#20895](https://github.com/NVIDIA/TensorRT-LLM/pull/20895)
  [None][infra] Waive 1 failed cases for main in pre-merge 65859 (#20895)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-23** [`3fa0c60e30`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fa0c60e30) [#10574](https://github.com/NVIDIA/TensorRT-LLM/pull/10574)
  [TRTLLM-10155][infra] Update trtllm-release image stage to tritonrelease, and make this build from source, not devel (#10574)
  _Files: `docker/Makefile`, `jenkins/BuildDockerImage.groovy`_
- **2026-10-23** [`c1e5bf2947`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1e5bf2947) [#20885](https://github.com/NVIDIA/TensorRT-LLM/pull/20885)
  [None][infra] Add blossom-ci authorized users (#20885)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-10-23** [`b4da992392`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4da992392) [#19537](https://github.com/NVIDIA/TensorRT-LLM/pull/19537)
  [TRTLLMINF-384][fix] classify failures from Slurm job logs (#19537)
  _Files: `jenkins/L0_Test.groovy`, `tests/unittest/tools/test_infra_dry_run_pipeline.py`_
- **2026-10-23** [`f87f1ff52b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f87f1ff52b)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-10-23** [`b752bf4691`](https://github.com/NVIDIA/TensorRT-LLM/commit/b752bf4691) [#20456](https://github.com/NVIDIA/TensorRT-LLM/pull/20456)
  [None][infra] Get changed files from base_commit for merge queue L0 builds (#20456)
  _Files: `jenkins/L0_MergeRequest.groovy`, `tests/unittest/tools/test_infra_dry_run_pipeline.py`_
- **2026-10-22** [`6cb5a79980`](https://github.com/NVIDIA/TensorRT-LLM/commit/6cb5a79980) [#20479](https://github.com/NVIDIA/TensorRT-LLM/pull/20479)
  [https://nvbugs/6838020][test] Rebalance mid-generation in KV pool rebalance accuracy test (#20479)
  _Files: `tests/integration/defs/accuracy/test_kv_pool_rebalance_accuracy.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-22** [`9cc37929e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cc37929e8) [#20828](https://github.com/NVIDIA/TensorRT-LLM/pull/20828)
  [None][infra] pause B200 multi-GPU stages to relieve the CI queue (#20828)
  _Files: `jenkins/config/maintenance_stages.txt`_
- **2026-10-22** [`4e37789598`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e37789598) [#20818](https://github.com/NVIDIA/TensorRT-LLM/pull/20818)
  [None][infra] Keep cpu_only unit tests in NGC image sanity tests (#20818)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-22** [`4d2c821ffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d2c821ffe) [#20824](https://github.com/NVIDIA/TensorRT-LLM/pull/20824)
  [None][infra] Waive 1 failed cases for main in pre-merge 65737 (#20824)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-22** [`01da104875`](https://github.com/NVIDIA/TensorRT-LLM/commit/01da104875) [#20583](https://github.com/NVIDIA/TensorRT-LLM/pull/20583)
  [TRTLLM-16975][infra] expand CBTS Python coverage collection (#20583)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/cbts/command/coverage/collection/pystart_report.py`, `jenkins/scripts/cbts/cbts/coverage/collection/COLLECTION.md`, `jenkins/scripts/cbts/cbts/coverage/collection/README.md` _+6 more__
- **2026-10-22** [`4945d313d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4945d313d4) [#20099](https://github.com/NVIDIA/TensorRT-LLM/pull/20099)
  [None][infra] Upgrade NIXL to v1.5.0 and UCX to v1.23.x (#20099)
  _Files: `docker/common/install_nixl.sh`, `docker/common/install_ucx.sh`, `jenkins/current_image_tags.properties`, `requirements-dev.txt`_
- **2026-10-22** [`095f025ad6`](https://github.com/NVIDIA/TensorRT-LLM/commit/095f025ad6) [#20791](https://github.com/NVIDIA/TensorRT-LLM/pull/20791)
  [None][infra] Waive 1 failed cases for main in pre-merge 65561 (#20791)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-22** [`0084e98f59`](https://github.com/NVIDIA/TensorRT-LLM/commit/0084e98f59) [#20596](https://github.com/NVIDIA/TensorRT-LLM/pull/20596)
  [TRTLLMINF-342][fix] Unify Docker image orchestration and nightly wheel selection (#20596)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-21** [`8ede99a383`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ede99a383) [#20735](https://github.com/NVIDIA/TensorRT-LLM/pull/20735)
  [None][ci] waive pre-existing test failures on main (#20735)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-21** [`00c184e1f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/00c184e1f8) [#20612](https://github.com/NVIDIA/TensorRT-LLM/pull/20612)
  [None][fix] match nightly release BOLT behavior to postmerge (#20612)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-21** [`61536fd9ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/61536fd9ea) [#10695](https://github.com/NVIDIA/TensorRT-LLM/pull/10695)
  [TRTLLM-9636][infra] Keep run all test stage when check test list failed in post-merge (#10695)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`_
- **2026-10-21** [`fb23b9a661`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb23b9a661) [#20729](https://github.com/NVIDIA/TensorRT-LLM/pull/20729)
  [None][infra] Point the PerfSanityTriage job at an image that exists (#20729)
  _Files: `jenkins/runPerfSanityTriage.groovy`_
- **2026-10-21** [`544ac2f4c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/544ac2f4c4) [#20719](https://github.com/NVIDIA/TensorRT-LLM/pull/20719)
  [None][infra] Waive 1 failed cases for main in pre-merge 65225 (#20719)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-21** [`dbc875d517`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbc875d517) [#20411](https://github.com/NVIDIA/TensorRT-LLM/pull/20411)
  [TRTLLM-16315][infra] bound new dataclasses through CBTS consumers (#20411)
  _Files: `jenkins/scripts/cbts/cbts/coverage/selection/SELECTION.md`, `jenkins/scripts/cbts/cbts/coverage/selection/python_change_analysis.py`, `jenkins/scripts/cbts/cbts/coverage/selection/selector.py`, `tests/unittest/scripts/cbts/_dataclass_helpers.py` _+2 more__
- **2026-10-21** [`807562c203`](https://github.com/NVIDIA/TensorRT-LLM/commit/807562c203) [#20718](https://github.com/NVIDIA/TensorRT-LLM/pull/20718)
  [None][infra] Waive 1 failed cases for main in pre-merge 65225 (#20718)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`557ddcae70`](https://github.com/NVIDIA/TensorRT-LLM/commit/557ddcae70) [#20614](https://github.com/NVIDIA/TensorRT-LLM/pull/20614)
  [None][chore] waive tp2 hang (#20614)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`2d12ed6f29`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d12ed6f29) [#20692](https://github.com/NVIDIA/TensorRT-LLM/pull/20692)
  [None][infra] Waive 1 failed cases for main in pre-merge 65185 (#20692)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`cb01bee6ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb01bee6ce) [#20690](https://github.com/NVIDIA/TensorRT-LLM/pull/20690)
  [None][infra] Waive 1 failed cases for main in pre-merge 65236 (#20690)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`93d46e50e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/93d46e50e0) [#20678](https://github.com/NVIDIA/TensorRT-LLM/pull/20678)
  [None][infra] Waive 1 failed cases for main in pre-merge 65251 (#20678)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`ee7c59aa78`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee7c59aa78) [#20564](https://github.com/NVIDIA/TensorRT-LLM/pull/20564)
  [None][fix] Enforce container wheel version and source commit (#20564)
  _Files: `docker/Dockerfile.multi`, `docker/common/validate_wheel_metadata.py`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy` _+2 more__
- **2026-10-20** [`adc2b088f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/adc2b088f2) [#20581](https://github.com/NVIDIA/TensorRT-LLM/pull/20581)
  [https://nvbugs/6581067][test] Unwaive test_fp4_gemm_bias_per_backend mnk2/mnk3 (#20581)
- **2026-10-20** [`66ff20f205`](https://github.com/NVIDIA/TensorRT-LLM/commit/66ff20f205) [#19048](https://github.com/NVIDIA/TensorRT-LLM/pull/19048)
  [None][infra] Add PrimTS vendor promotion maintainer tool (#19048)
  _Files: `.github/CODEOWNERS`, `.pre-commit-config.yaml`, `3rdparty/vendor-sources.md`, `AGENTS.md` _+10 more__
- **2026-10-20** [`3af4d782e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/3af4d782e4) [#20410](https://github.com/NVIDIA/TensorRT-LLM/pull/20410)
  [TRTLLM-16975][infra] compose CBTS docstring analysis and expand no operation rules (#20410)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/command/main.py`, `jenkins/scripts/cbts/cbts/coverage/selection/SELECTION.md`, `jenkins/scripts/cbts/cbts/coverage/selection/selector.py` _+10 more__
- **2026-10-20** [`8d9cdd4c4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d9cdd4c4c) [#20265](https://github.com/NVIDIA/TensorRT-LLM/pull/20265)
  [None][infra] save cbts shadow run decision to artifact (#20265)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/command/report_decision.py`, `tests/unittest/scripts/cbts/test_report_decision.py`_
- **2026-10-20** [`d6bb0609df`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6bb0609df) [#20493](https://github.com/NVIDIA/TensorRT-LLM/pull/20493)
  [https://nvbugs/6942724][fix] Refresh serving configuration schema snapshots (#20493)
  _Files: `tensorrt_llm/schemas/trtllm-serve-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-disagg-config.schema.json`, `tests/integration/test_lists/waives.txt`_
- **2026-10-19** [`7695494b8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/7695494b8f) [#20475](https://github.com/NVIDIA/TensorRT-LLM/pull/20475)
  [None][doc] Fix CI overview description of post-merge pipeline (#20475)
  _Files: `docs/source/developer-guide/ci-overview.md`_
- **2026-10-19** [`59eab99c89`](https://github.com/NVIDIA/TensorRT-LLM/commit/59eab99c89) [#20579](https://github.com/NVIDIA/TensorRT-LLM/pull/20579)
  [https://nvbugs/6713424][chore] Unwaive GB300 DSpark AgentX con1156 e2e (#20579)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-19** [`ea4d1d812a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea4d1d812a) [#20080](https://github.com/NVIDIA/TensorRT-LLM/pull/20080)
  [TRTLLM-5432][infra] Fetch UCXX's downloads from the mirror and retry build_wheel.py (#20080)
  _Files: `3rdparty/fetch_content.json`, `cpp/CMakeLists.txt`, `jenkins/Build.groovy`_
- **2026-10-19** [`0372799d15`](https://github.com/NVIDIA/TensorRT-LLM/commit/0372799d15) [#20542](https://github.com/NVIDIA/TensorRT-LLM/pull/20542)
  [None][infra] Waive 1 failed cases for main in post-merge 3026 (#20542)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-19** [`e7b8fbb66c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7b8fbb66c) [#20563](https://github.com/NVIDIA/TensorRT-LLM/pull/20563)
  [None][infra] Waive 1 failed cases for main in pre-merge 64813 (#20563)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-19** [`f660c7bf7f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f660c7bf7f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-10-19** [`bdfd08c79d`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdfd08c79d) [#20449](https://github.com/NVIDIA/TensorRT-LLM/pull/20449)
  [None][fix] Pass source repository and commit to PLC container scans (#20449)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-19** [`54eff28f36`](https://github.com/NVIDIA/TensorRT-LLM/commit/54eff28f36)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Attention  (41 commits)

- **2026-10-26** [`1faefd722e`](https://github.com/NVIDIA/TensorRT-LLM/commit/1faefd722e) [#21006](https://github.com/NVIDIA/TensorRT-LLM/pull/21006)
  [None][chore] promote flashinfer-prims-ts source from #20209 (#21006)
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-10-26** [`9ffa6f4395`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ffa6f4395) [#20391](https://github.com/NVIDIA/TensorRT-LLM/pull/20391)
  [TRTLLM-14477][refactor] unify multimodal request data and item metadata (#20391)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `AGENTS.md`, `docs/source/developer-guide/multimodal.md`, `docs/source/developer-guide/overview.md` _+58 more__
- **2026-10-26** [`178ac92fed`](https://github.com/NVIDIA/TensorRT-LLM/commit/178ac92fed) [#20209](https://github.com/NVIDIA/TensorRT-LLM/pull/20209)
  [None][feat] Add the PrimTS native sparse MLA FMHA for DeepSeek-V4 generation and enable it by default on SM100 (#20209)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `docs/source/release-notes.md`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md` _+60 more__
- **2026-10-26** [`dddb74c217`](https://github.com/NVIDIA/TensorRT-LLM/commit/dddb74c217) [#20898](https://github.com/NVIDIA/TensorRT-LLM/pull/20898)
  [None][doc] Fix documentation errors (#20898)
  _Files: `docs/source/commands/trtllm-serve/run-benchmark-with-trtllm-serve.md`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/deployment-guide/deployment-guide-for-deepseek-r1-on-trtllm.md`, `docs/source/deployment-guide/deployment-guide-for-llama3.3-70b-on-trtllm.md` _+10 more__
- **2026-10-26** [`fce28f0726`](https://github.com/NVIDIA/TensorRT-LLM/commit/fce28f0726) [#20178](https://github.com/NVIDIA/TensorRT-LLM/pull/20178)
  [None][feat] Unified kv cache manager foundation (#20178)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/storage/config.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp` _+12 more__
- **2026-10-24** [`d7e0ecac92`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7e0ecac92) [#19961](https://github.com/NVIDIA/TensorRT-LLM/pull/19961)
  [None][feat] DeepSeek V4 / DSpark optimizations on Rubin (#19961)
  _Files: `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+18 more__
- **2026-10-23** [`1586d85375`](https://github.com/NVIDIA/TensorRT-LLM/commit/1586d85375) [#17147](https://github.com/NVIDIA/TensorRT-LLM/pull/17147)
  [None][feat] Qwen Image Ulysses perf enhancement (#17147)
  _Files: `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.cu`, `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.h`, `cpp/tensorrt_llm/thop/ulyssesPostUnscatterOp.cpp`, `docs/source/models/supported-models.md` _+9 more__
- **2026-10-23** [`222676c8d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/222676c8d7) [#20653](https://github.com/NVIDIA/TensorRT-LLM/pull/20653)
  [None][perf] Integrate FlashInfer KDA prefill with fused convolution (#20653)
  _Files: `.pre-commit-config.yaml`, `3rdparty/vendor_patches/flashinfer-kda-bt16.patch`, `3rdparty/vendor_sources.lock.yaml`, `pyproject.toml` _+30 more__
- **2026-10-23** [`b4bfec4baf`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4bfec4baf) [#20452](https://github.com/NVIDIA/TensorRT-LLM/pull/20452)
  [TRTLLM-17204][feat] Add First-N/Last-N mixed-precision KV caching using native SWA in KVCM V2 (#20452)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/attention/attention.py`, `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/attention/backends/interface.py` _+15 more__
- **2026-10-23** [`ae1aa43964`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae1aa43964) [#19877](https://github.com/NVIDIA/TensorRT-LLM/pull/19877)
  [TRTLLM-16754][feat] Commit SWA windows at prefix fork points for sibling reuse (#19877)
  _Files: `docs/source/deployment-guide/deployment-guide-for-qwen3.8-flash-next-on-trtllm.md`, `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/mamba_cache_manager.py` _+13 more__
- **2026-10-23** [`63bf4eadb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/63bf4eadb8) [#20347](https://github.com/NVIDIA/TensorRT-LLM/pull/20347)
  [https://nvbugs/6920459][fix] Point the Sliding Window Attention figure at its own image (#20347)
  _Files: `docs/source/features/long-sequence.md`_
- **2026-10-23** [`854ccee8a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/854ccee8a9) [#20167](https://github.com/NVIDIA/TensorRT-LLM/pull/20167)
  [None][feat] Enable MiniMax-M3 on Rubin (SM107): NVFP4 KV exemption and 128-token paged FMHA kernels (#20167)
  _Files: `docs/source/deployment-guide/deployment-guide-for-minimax-m3-on-trtllm.md`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/triton_sparse_decode.py` _+11 more__
- **2026-10-23** [`d7ec5162ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7ec5162ac) [#20242](https://github.com/NVIDIA/TensorRT-LLM/pull/20242)
  [None][fix] Honor separate V token stride in context FMHA (#20242)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fmhaRunner.cpp`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h` _+9 more__
- **2026-10-23** [`0f3e1d093d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f3e1d093d) [#20276](https://github.com/NVIDIA/TensorRT-LLM/pull/20276)
  [TRTLLM-17033][feat] Qwen3.8-Flash-Next modeling_v2: CUTEDSL, MTP, video, FP8/NVFP4 KV, bf16 state, canonical QSA selection, breakable prefill graph, GB300 fast paths (#20276)
- **2026-10-23** [`12af626ace`](https://github.com/NVIDIA/TensorRT-LLM/commit/12af626ace)
  [None][chore] promote flashinfer-prims-ts source from #20224
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-10-23** [`791a402fc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/791a402fc8) [#20224](https://github.com/NVIDIA/TensorRT-LLM/pull/20224)
  [None][feat] Support PrimsTS SageAttention for VisualGen VSA and SOL (#20224)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionWorkspace.h` _+59 more__
- **2026-10-23** [`36d8aef55e`](https://github.com/NVIDIA/TensorRT-LLM/commit/36d8aef55e) [#20119](https://github.com/NVIDIA/TensorRT-LLM/pull/20119)
  [https://nvbugs/6796296][fix] Pad DSv4 NVFP4 compressed FP8 scratch by one FMHA KV tile (#20119)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/backend.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-23** [`dd63b36fcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd63b36fcf) [#19989](https://github.com/NVIDIA/TensorRT-LLM/pull/19989)
  [None][perf] One-model speculative decoding: host work between steps, worker-produced target logits, KDA drafts' records (#19989)
  _Files: `docs/source/features/torch_compile_and_piecewise_cuda_graph.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_device_copy.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py` _+35 more__
- **2026-10-22** [`e9d64fd54d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9d64fd54d) [#20680](https://github.com/NVIDIA/TensorRT-LLM/pull/20680)
  [None][test] Add Qwen3.8-Flash-Next, DeepSeek-V4.1-Flash and GLM-5.3-Flash perf-sanity cases; reset perf-sanity timeouts (#20680)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/_model_paths.py` _+29 more__
- **2026-10-22** [`82b6190176`](https://github.com/NVIDIA/TensorRT-LLM/commit/82b6190176) [#20742](https://github.com/NVIDIA/TensorRT-LLM/pull/20742)
  [None][fix] Keep GLM-5.3-Flash MTP draft layers in the target KV cache (#20742)
  _Files: `tensorrt_llm/_torch/speculative/utils.py`, `tests/unittest/_torch/modeling/test_glm5_next_contracts.py`_
- **2026-10-22** [`53edc7d4b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/53edc7d4b1) [#20464](https://github.com/NVIDIA/TensorRT-LLM/pull/20464)
  [None][chore] Remove two-model speculative decoding leftovers (#20464)
  _Files: `docs/source/features/sampling.md`, `docs/source/llm-api/index.md`, `pyproject.toml`, `tensorrt_llm/_torch/models/_arch_index.py` _+44 more__
- **2026-10-22** [`2770bbfc8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2770bbfc8a) [#20544](https://github.com/NVIDIA/TensorRT-LLM/pull/20544)
  [None][feat] FP4 MLA disagg (#20544)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fp4_mla/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/fp4_mla/v_cache.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py` _+10 more__
- **2026-10-22** [`0c9b463e34`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c9b463e34) [#19975](https://github.com/NVIDIA/TensorRT-LLM/pull/19975)
  [None][perf] MiniMax-M3: parallelize MSA indexer scoring over cached prefix dimension (#19975)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_indexer.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/warmup.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+4 more__
- **2026-10-21** [`afc1c168fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/afc1c168fd) [#20325](https://github.com/NVIDIA/TensorRT-LLM/pull/20325)
  [None][fix] Resolve attention DP dummy roles from queued requests (#20325)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-10-21** [`ec782566f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec782566f5) [#20314](https://github.com/NVIDIA/TensorRT-LLM/pull/20314)
  [None][fix] Flush overlap KV cache events on every attention DP rank (#20314)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/disaggregation/test_disagg_loop_transcript.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_pool_rebalance.py`_
- **2026-10-21** [`e8127c7c5c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8127c7c5c) [#18547](https://github.com/NVIDIA/TensorRT-LLM/pull/18547)
  [https://nvbugs/6700677][fix] Fix Gemma4 startup on non-SM100 GPUs (#18547)
  _Files: `tensorrt_llm/_torch/attention/backends/interface.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py`, `tensorrt_llm/_torch/attention/qk_norm_attention.py`, `tensorrt_llm/_torch/model_config.py` _+18 more__
- **2026-10-21** [`033f2ea020`](https://github.com/NVIDIA/TensorRT-LLM/commit/033f2ea020) [#19976](https://github.com/NVIDIA/TensorRT-LLM/pull/19976)
  [None][perf] Port the DKG paged MQA logits kernel improvements and default the DSA indexer to CuTe DSL (#19976)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/__init__.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/params.py` _+11 more__
- **2026-10-21** [`5f90e8939d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f90e8939d) [#20387](https://github.com/NVIDIA/TensorRT-LLM/pull/20387)
  [https://nvbugs/6913951][fix] Support FP8 custom-mask context attention (#20387)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention/backends/fmha/triton_custom_mask.py`, `tensorrt_llm/_torch/attention/backends/triton_prefill.py`, `tests/unittest/_torch/attention/test_flashinfer_trtllm_gen_fmha.py` _+2 more__
- **2026-10-21** [`ef913d39b3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef913d39b3) [#20454](https://github.com/NVIDIA/TensorRT-LLM/pull/20454)
  [TRTLLM-16480][perf] Speed up GLM-5.3-Flash sparse attention (#20454)
  _Files: `docs/source/deployment-guide/deployment-guide-for-glm-5.3-flash-on-trtllm.md`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/kernels.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/native_decode.py` _+2 more__
- **2026-10-20** [`4c0197d1e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c0197d1e4) [#20652](https://github.com/NVIDIA/TensorRT-LLM/pull/20652)
  [https://nvbugs/6948129][fix] Test H=96 single-token MLA routing at its measured batch floor (#20652)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/test_cute_dsl_mla.py`_
- **2026-10-20** [`1c5642d208`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c5642d208) [#20034](https://github.com/NVIDIA/TensorRT-LLM/pull/20034)
  [https://nvbugs/6890342][fix] Fix fp4 mla test and update cutedsl to 4.8.0 (#20034)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `ATTRIBUTIONS-Python.md`, `requirements.txt` _+7 more__
- **2026-10-20** [`6b540e1bdb`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b540e1bdb) [#20606](https://github.com/NVIDIA/TensorRT-LLM/pull/20606)
  [TRTLLM-15863][fix] Address review follow-ups on the lazy attention package exports (#20606)
  _Files: `tensorrt_llm/_torch/attention/__init__.py`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_sparse_mla.py`, `tensorrt_llm/_torch/attention/rotary_embedding.py`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_compressor_module.py` _+1 more__
- **2026-10-20** [`5cf7459e97`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cf7459e97) [#20389](https://github.com/NVIDIA/TensorRT-LLM/pull/20389)
  [None][perf] GLM-5.3-Flash: share KDA verify offsets, fuse mHC in every phase, BF16 router GEMM (#20389)
  _Files: `tensorrt_llm/_torch/models/modeling_glm5_next.py`_
- **2026-10-19** [`c6350002f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c6350002f7) [#20048](https://github.com/NVIDIA/TensorRT-LLM/pull/20048)
  [None][fix] Use string cache salts in V2 and migrate LLM API coverage (#20048)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventManager.cpp` _+34 more__
- **2026-10-19** [`395e1e10fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/395e1e10fc) [#20405](https://github.com/NVIDIA/TensorRT-LLM/pull/20405)
  [TRTLLM-17109][perf] Reduce Gemma multimodal attention mask construction peak memory (#20405)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma3.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-10-19** [`321a38cd0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/321a38cd0e) [#20471](https://github.com/NVIDIA/TensorRT-LLM/pull/20471)
  [https://nvbugs/6939212][fix] Unwaive unittest/_torch/attention after the KVCM2 teardown fix (#20471)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-19** [`93951cc32f`](https://github.com/NVIDIA/TensorRT-LLM/commit/93951cc32f) [#20522](https://github.com/NVIDIA/TensorRT-LLM/pull/20522)
  [https://nvbugs/6948011][fix] Shut down attention test KV cache managers on failure paths (#20522)
  _Files: `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`, `tests/unittest/_torch/attention/test_attention.py`, `tests/unittest/_torch/attention/test_attention_mla.py`, `tests/unittest/_torch/attention/test_flashinfer_attention.py`_
- **2026-10-19** [`c941eb61c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c941eb61c7) [#20549](https://github.com/NVIDIA/TensorRT-LLM/pull/20549)
  [https://nvbugs/6933917][docs] Fix VisualGen constructor in sparse at… (#20549)
  _Files: `docs/source/features/visualgen-sparse-attention.md`_
- **2026-10-19** [`85b1b8323b`](https://github.com/NVIDIA/TensorRT-LLM/commit/85b1b8323b) [#20223](https://github.com/NVIDIA/TensorRT-LLM/pull/20223)
  [None][fix] Size the Blackwell spec-dec tree mask for the SwapsMmaAb kernel layout (#20223)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/xqaParams.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaRunnerParams.h` _+7 more__
- **2026-10-19** [`fd744ca06d`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd744ca06d) [#20432](https://github.com/NVIDIA/TensorRT-LLM/pull/20432)
  [None][feat] Add spec_dec_variant to telemetry (#20432)
  _Files: `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/usage/llm_args_golden_manifest.json`, `tensorrt_llm/usage/schemas/README.md` _+3 more__
- **2026-10-19** [`0cd9d0b541`](https://github.com/NVIDIA/TensorRT-LLM/commit/0cd9d0b541) [#19650](https://github.com/NVIDIA/TensorRT-LLM/pull/19650)
  [None][perf] Fill the KVCM2 host tier progressively (#19650)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_compression/nativeColdPageCodec.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batch.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batch.h` _+40 more__

## Executor / Runtime  (27 commits)

- **2026-10-26** [`011316470c`](https://github.com/NVIDIA/TensorRT-LLM/commit/011316470c) [#20851](https://github.com/NVIDIA/TensorRT-LLM/pull/20851)
  [TRTLLM-15764][refactor] Split PyTorchModelEngine construction into named phases (#20851)
  _Files: `.claude/skills/perf-regression-cookbook/references/cuda-graph-and-compile/piecewise-cudagraph-far-ceiling-append.md`, `tensorrt_llm/_torch/pyexecutor/engine/cuda_graph.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-10-26** [`732fd63463`](https://github.com/NVIDIA/TensorRT-LLM/commit/732fd63463) [#20915](https://github.com/NVIDIA/TensorRT-LLM/pull/20915)
  [#19902][fix] Give logits processors each beam's hypothesis under beam search (#20915)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py` _+4 more__
- **2026-10-26** [`99a6fd3a68`](https://github.com/NVIDIA/TensorRT-LLM/commit/99a6fd3a68) [#20839](https://github.com/NVIDIA/TensorRT-LLM/pull/20839)
  [https://nvbugs/6971880][fix] Sync serving schemas on version bumps (#20839)
  _Files: `AGENTS.md`, `scripts/generate_trtllm_serve_schemas.py`, `tensorrt_llm/schemas/trtllm-serve-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-disagg-config.schema.json` _+2 more__
- **2026-10-26** [`c4dd49d511`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4dd49d511) [#20864](https://github.com/NVIDIA/TensorRT-LLM/pull/20864)
  [None][fix] Chat Completions: accept the OpenAI store field (#20864)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/api_stability/references/trtllm_serve_api.yaml`, `tests/unittest/llmapi/apps/test_openai_protocol_chat_store.py`_
- **2026-10-26** [`c9b7c1768e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9b7c1768e) [#20279](https://github.com/NVIDIA/TensorRT-LLM/pull/20279)
  [https://nvbugs/6926284][fix] Align qwen3_coder parameter typing with vLLM (#20279)
  _Files: `tensorrt_llm/serve/tool_parser/qwen3_coder_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-26** [`14765c7d98`](https://github.com/NVIDIA/TensorRT-LLM/commit/14765c7d98) [#20837](https://github.com/NVIDIA/TensorRT-LLM/pull/20837)
  [None][fix] MiniMax-M3: resolve an unprefilled prompt as outside reasoning (#20837)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/apps/test_reasoning_prompt_resolution.py`, `tests/unittest/llmapi/apps/test_render_core.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_
- **2026-10-25** [`7d391a06d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d391a06d7) [#20213](https://github.com/NVIDIA/TensorRT-LLM/pull/20213)
  [None][perf] enable Qwen3.*-VL encoder CUDA graphs via shared setup (#20213)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_glm5_next_vision.py`, `tensorrt_llm/_torch/models/modeling_multimodal_encoder.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py` _+19 more__
- **2026-10-23** [`39a44fab74`](https://github.com/NVIDIA/TensorRT-LLM/commit/39a44fab74) [#20307](https://github.com/NVIDIA/TensorRT-LLM/pull/20307)
  [None][feat] Add Cosmos3-Edge Reasoner support (#20307)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/cosmos3.py`, `tensorrt_llm/_torch/configs/cosmos3_edge.py` _+12 more__
- **2026-10-23** [`461183a90a`](https://github.com/NVIDIA/TensorRT-LLM/commit/461183a90a) [#20883](https://github.com/NVIDIA/TensorRT-LLM/pull/20883)
  [None][test] Fix the _validate_request fakes in test_forward_error_survival (#20883)
  _Files: `tests/unittest/executor/test_forward_error_survival.py`_
- **2026-10-23** [`1526744c78`](https://github.com/NVIDIA/TensorRT-LLM/commit/1526744c78) [#20673](https://github.com/NVIDIA/TensorRT-LLM/pull/20673)
  [https://nvbugs/6891162][fix] Stop test_generate_with_stop_words on the token Qwen3 generates for N (#20673)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-10-23** [`41b0085cd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/41b0085cd1) [#20758](https://github.com/NVIDIA/TensorRT-LLM/pull/20758)
  [https://nvbugs/6891162][fix] Ban the tokens Qwen3 generates in test_generate_with_bad_words (#20758)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-10-23** [`04eb92374b`](https://github.com/NVIDIA/TensorRT-LLM/commit/04eb92374b) [#20222](https://github.com/NVIDIA/TensorRT-LLM/pull/20222)
  [TRTLLM-17005][refactor] Component-local C++ Tests (Part 2) (#20222)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.cpp` _+18 more__
- **2026-10-23** [`b78033a951`](https://github.com/NVIDIA/TensorRT-LLM/commit/b78033a951) [#19997](https://github.com/NVIDIA/TensorRT-LLM/pull/19997)
  [None][feat] qualify Phi3 dense for MX (#19997)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py` _+4 more__
- **2026-10-23** [`e9093e8377`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9093e8377) [#20422](https://github.com/NVIDIA/TensorRT-LLM/pull/20422)
  [https://nvbugs/6932723][feat] Support required tool choice for Nemotron Super 3.5 VL (#20422)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tensorrt_llm/serve/extensions/__init__.py`, `tensorrt_llm/serve/extensions/nemotron.py`, `tensorrt_llm/serve/openai_server.py` _+14 more__
- **2026-10-23** [`7bdfab5f04`](https://github.com/NVIDIA/TensorRT-LLM/commit/7bdfab5f04) [#19850](https://github.com/NVIDIA/TensorRT-LLM/pull/19850)
  [None][feat] Add lm_head_output_dtype for FP32 LM head logits (#19850)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/modules/embedding.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+9 more__
- **2026-10-23** [`679ef1381c`](https://github.com/NVIDIA/TensorRT-LLM/commit/679ef1381c) [#20698](https://github.com/NVIDIA/TensorRT-LLM/pull/20698)
  [https://nvbugs/6758245][fix] Cherry-pick #20429: Keep /metrics from blocking the serving event loop (#20698)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/serve/openai_server.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/apps/test_openai_server_iteration_stats.py`_
- **2026-10-22** [`9c2c80c2ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c2c80c2ca) [#20166](https://github.com/NVIDIA/TensorRT-LLM/pull/20166)
  [TRTLLM-16957][perf] SID-GR Optimization 2/N: Vectorize final beam assembly (#20166)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tests/unittest/_torch/sampler/test_beam_search.py`_
- **2026-10-22** [`af3e5eb257`](https://github.com/NVIDIA/TensorRT-LLM/commit/af3e5eb257) [#20559](https://github.com/NVIDIA/TensorRT-LLM/pull/20559)
  [None][chore] Move hang detector test to CPU stage (#20559)
  _Files: `jenkins/L0_Test.groovy`, `tests/unittest/_torch/executor/test_hang_detector_kill.py`_
- **2026-10-22** [`8926400b41`](https://github.com/NVIDIA/TensorRT-LLM/commit/8926400b41) [#20101](https://github.com/NVIDIA/TensorRT-LLM/pull/20101)
  [None][fix] Honour --num-prompts in the VisionArena benchmark dataset (#20101)
  _Files: `tensorrt_llm/serve/scripts/benchmark_dataset.py`, `tests/unittest/llmapi/apps/_test_trtllm_serve_multimodal_benchmark.py`_
- **2026-10-21** [`370fe4c509`](https://github.com/NVIDIA/TensorRT-LLM/commit/370fe4c509) [#20734](https://github.com/NVIDIA/TensorRT-LLM/pull/20734)
  [TRTLLM-15893][fix] Fix the dead import in the indexer-Q CuTe DSL prewarm (#20734)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/warmup.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine_warmup.py`_
- **2026-10-21** [`a0141d0e56`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0141d0e56) [#20043](https://github.com/NVIDIA/TensorRT-LLM/pull/20043)
  [TRTLLM-17060][refactor] BREAKING: remove obsolete executor backend compatibility (#20043)
  _Files: `cpp/include/tensorrt_llm/batch_manager/common.h`, `cpp/include/tensorrt_llm/runtime/utils/mpiTags.h`, `cpp/tensorrt_llm/executor/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/interfaces.h` _+35 more__
- **2026-10-21** [`69e06b8afb`](https://github.com/NVIDIA/TensorRT-LLM/commit/69e06b8afb) [#20108](https://github.com/NVIDIA/TensorRT-LLM/pull/20108)
  [None][perf] BREAKING: Enable zero-copy mode for Mooncake Store (#20108)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/cudaVirtMem.cpp`, `docs/source/features/kv-cache-connector.md`, `tensorrt_llm/_torch/pyexecutor/connectors/kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/mooncake_store/addressing.py` _+20 more__
- **2026-10-21** [`16d26df5a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/16d26df5a7) [#20608](https://github.com/NVIDIA/TensorRT-LLM/pull/20608)
  [None][fix] Do not lose the MPI Comm Server shutdown request while workers tear down (#20608)
  _Files: `tensorrt_llm/llmapi/mgmn_leader_node.py`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/unittest/llmapi/test_mpi_session.py`_
- **2026-10-21** [`b47eb8fe6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b47eb8fe6b) [#19884](https://github.com/NVIDIA/TensorRT-LLM/pull/19884)
  [None][perf] schedule multimodal encoder items by prefill chunk (#19884)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/engine/multimodal.py` _+10 more__
- **2026-10-20** [`271ed9f22a`](https://github.com/NVIDIA/TensorRT-LLM/commit/271ed9f22a) [#20231](https://github.com/NVIDIA/TensorRT-LLM/pull/20231)
  [https://nvbugs/6613027][fix] Responses API: pass image input to multimodal models (#20231)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/responses_utils.py`, `tests/unittest/inputs/test_chat_template_dispatch.py` _+2 more__
- **2026-10-20** [`2706f4dfb6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2706f4dfb6) [#20180](https://github.com/NVIDIA/TensorRT-LLM/pull/20180)
  [None][feat] Account for connector-provided blocks in KV reuse (#20180)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp` _+17 more__
- **2026-10-19** [`df28262e26`](https://github.com/NVIDIA/TensorRT-LLM/commit/df28262e26) [#20442](https://github.com/NVIDIA/TensorRT-LLM/pull/20442)
  [None][fix] Keep MiniMax-M3 streaming and non-streaming reasoning parsing in step (#20442)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_

## MoE  (25 commits)

- **2026-10-26** [`ba6c1fc87d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba6c1fc87d) [#18843](https://github.com/NVIDIA/TensorRT-LLM/pull/18843)
  [TRTLLM-16303][refactor] modularize Mamba cache managers (#18843)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/modeling.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/ops/ssm/fused_recurrent_gated_delta_rule_cached_replay_update.py`, `tensorrt_llm/_torch/attention/backends/sparse/csa2/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/cache_manager.py` _+57 more__
- **2026-10-26** [`158252825d`](https://github.com/NVIDIA/TensorRT-LLM/commit/158252825d) [#20789](https://github.com/NVIDIA/TensorRT-LLM/pull/20789)
  [None][refactor] Register modeling_v2 routes with a routes decorator (#20789)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`, `tensorrt_llm/_torch/_experimental/modeling_v2/__init__.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/_router_index.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/__init__.py` _+5 more__
- **2026-10-26** [`3467615c72`](https://github.com/NVIDIA/TensorRT-LLM/commit/3467615c72) [#20681](https://github.com/NVIDIA/TensorRT-LLM/pull/20681)
  [TRTLLM-17175][fix] Fix the post-merge leftovers of the kernel and thop test relayout (#20681)
  _Files: `cpp/include/tensorrt_llm/deep_gemm/scheduler.cuh`, `examples/layer_wise_benchmarks/parser_utils.py`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/kernels/__init__.py` _+10 more__
- **2026-10-24** [`032eb456ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/032eb456ec) [#20808](https://github.com/NVIDIA/TensorRT-LLM/pull/20808)
  [https://nvbugs/6973221][fix] Fork CuteDSL MoE input quantization only under multi-stream (#20808)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/moe_scheduler.py`, `tests/unittest/_torch/moe/test_moe_backend.py`_
- **2026-10-24** [`ecae3c97e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecae3c97e2) [#20823](https://github.com/NVIDIA/TensorRT-LLM/pull/20823)
  [None][fix] Apply the NVFP4_AWQ pre-quant scale in MegaMoE CuteDSL (#20823)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/moe/fused_moe/cutlass/w4a16_nvfp4.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl_b12x.py` _+8 more__
- **2026-10-23** [`64ef54ce12`](https://github.com/NVIDIA/TensorRT-LLM/commit/64ef54ce12) [#16198](https://github.com/NVIDIA/TensorRT-LLM/pull/16198)
  [None][fix] Pad INT8-woq MoE intermediate to 64 for tensor-parallel sharding (#16198)
  _Files: `cpp/tensorrt_llm/thop/moe/cutlass/moeOp.cpp`, `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/unittest/_torch/moe/test_moe_backend.py`_
- **2026-10-23** [`4ccdca1e84`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ccdca1e84) [#20106](https://github.com/NVIDIA/TensorRT-LLM/pull/20106)
  [None][perf] optimize gvr v2 under large batchsize and small seqlen (#20106)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tests/unittest/_torch/kernels/parallel/test_gvr_selfsampling_topk.py`_
- **2026-10-23** [`348347ce3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/348347ce3e) [#20075](https://github.com/NVIDIA/TensorRT-LLM/pull/20075)
  [TRTLLM-16958][feat] MXFP8 refit with PCG changes, recompute_active_requests, Ray collectives (#20075)
  _Files: `cpp/tensorrt_llm/kernels/quantization.cuh`, `cpp/tensorrt_llm/thop/allgatherOp.cpp`, `cpp/tensorrt_llm/thop/allreduceOp.cpp`, `cpp/tensorrt_llm/thop/reducescatterOp.cpp` _+47 more__
- **2026-10-23** [`2676d6ba0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2676d6ba0a) [#20779](https://github.com/NVIDIA/TensorRT-LLM/pull/20779)
  [https://nvbugs/6448152][fix] Keep CuteDSL NVFP4 input quantization synchronous for prefill batches (#20779)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`, `tests/unittest/_torch/moe/kernels/parallel/test_cute_dsl_moe.py`_
- **2026-10-23** [`9f445c2a86`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f445c2a86) [#20741](https://github.com/NVIDIA/TensorRT-LLM/pull/20741)
  [TRTLLM-14960][refactor] Give the CUTLASS MoE implementations canonical identities (#20741)
  _Files: `.claude/skills/perf-optimization-casebook/references/kernel-and-fusion/fold-scale-swizzle-into-kernel.md`, `.claude/skills/perf-optimization-casebook/references/kernel-and-fusion/hw-matched-lowprec-moe-gemm.md`, `.claude/skills/trtllm-moe-develop/SKILL.md`, `.claude/skills/trtllm-moe-develop/references/moe-canonical-code-examples.md` _+71 more__
- **2026-10-23** [`8d1c7e0b26`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d1c7e0b26) [#20660](https://github.com/NVIDIA/TensorRT-LLM/pull/20660)
  [TRTLLM-15863][fix] Raise ImportError with the cause when a lazily imported submodule raises AttributeError (#20660)
  _Files: `tensorrt_llm/__init__.py`, `tensorrt_llm/_torch/attention/__init__.py`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/moe/fused_moe/deep_ep_utils.py` _+6 more__
- **2026-10-23** [`3024eb446e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3024eb446e) [#20576](https://github.com/NVIDIA/TensorRT-LLM/pull/20576)
  [None][feat] Kimi K3: DWDP fabric gather and TCPStore rendezvous, KVCM-managed KDA replay buffers (#20576)
  _Files: `cpp/tensorrt_llm/kernels/dwdpFabricGather.cu`, `cpp/tensorrt_llm/kernels/dwdpFabricGather.h`, `cpp/tensorrt_llm/kernels/dwdpFabricGatherTma.cu`, `cpp/tensorrt_llm/kernels/dwdpFabricGatherTma.h` _+58 more__
- **2026-10-23** [`5cbcc9cdc7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cbcc9cdc7) [#20800](https://github.com/NVIDIA/TensorRT-LLM/pull/20800)
  [https://nvbugs/6966263][test] Re-waive the flaky CuTe DSL MoE NVFP4 act-fusion test at its moe/kernels path (#20800)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-22** [`afcf499638`](https://github.com/NVIDIA/TensorRT-LLM/commit/afcf499638) [#20798](https://github.com/NVIDIA/TensorRT-LLM/pull/20798)
  [None][doc] Update MoE Perf Dashboard data to 1.4.0rc1 (0372799d15) (#20798)
  _Files: `docs/source/_static/moe-perf-dashboard/data.js`_
- **2026-10-22** [`86e2cbbb1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/86e2cbbb1e) [#20756](https://github.com/NVIDIA/TensorRT-LLM/pull/20756)
  [https://nvbugs/6951802][fix] Fix stale doc links failing test_http_url_validity (#20756)
  _Files: `docs/source/blogs/tech_blog/blog24_MoE_as_Dense_GEMM.md`, `docs/source/developer-guide/moe-perf-guide.md`_
- **2026-10-22** [`d1c54cb654`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1c54cb654) [#20658](https://github.com/NVIDIA/TensorRT-LLM/pull/20658)
  [TRTLLM-14848][chore] Move the MoE-owned thop unit tests into tests/unittest/_torch/moe/kernels/ (#20658)
  _Files: `.github/CODEOWNERS`, `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml` _+17 more__
- **2026-10-21** [`5d6fbb2062`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d6fbb2062) [#18396](https://github.com/NVIDIA/TensorRT-LLM/pull/18396)
  [None][feat] FLUX.1-dev NVFP4 Static Quant with per-tensor FP8 quantized MHA (sm103 CUTEDSL) (#18396)
  _Files: `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedDiTQKNormRopeOp.cpp`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py` _+23 more__
- **2026-10-21** [`1c7fadcfbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c7fadcfbe) [#20253](https://github.com/NVIDIA/TensorRT-LLM/pull/20253)
  [TRTLLM-17054][refactor] Remove obsolete warmup paths and test-only runtime switches (#20253)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/rocket/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/graphs.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py` _+24 more__
- **2026-10-21** [`4636b6311f`](https://github.com/NVIDIA/TensorRT-LLM/commit/4636b6311f) [#19953](https://github.com/NVIDIA/TensorRT-LLM/pull/19953)
  [https://nvbugs/6812424][fix] Enable CUTLASS MXFP8 MoE on SM107 (#19953)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cutlass.py`_
- **2026-10-20** [`46d9966b54`](https://github.com/NVIDIA/TensorRT-LLM/commit/46d9966b54) [#20055](https://github.com/NVIDIA/TensorRT-LLM/pull/20055)
  [https://nvbugs/6892493][fix] Support MegaMoE CuteDSL TEP for all models (#20055)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/moe/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/moe/fused_moe/create_moe.py` _+7 more__
- **2026-10-20** [`fe92fb923f`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe92fb923f) [#19753](https://github.com/NVIDIA/TensorRT-LLM/pull/19753)
  [TRTLLM-16404][fix] restore CUTLASS MoE compatibility and early feature checks (#19753)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/cutlass_kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/moe/cutlass/moe_kernels.cu`, `cpp/tensorrt_llm/thop/moe/cutlass/moeOp.cpp` _+18 more__
- **2026-10-20** [`8519776be9`](https://github.com/NVIDIA/TensorRT-LLM/commit/8519776be9) [#20267](https://github.com/NVIDIA/TensorRT-LLM/pull/20267)
  [TRTLLM-16984][feat] modeling_v2: default targets for gpt-oss-120b and DeepSeek-R1-0528 NVFP4 on sm_103 (#20267)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`, `tensorrt_llm/_torch/_experimental/modeling_v2/_router_index.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/catalog/_op.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/catalog/activation/flashinfer_silu_and_mul.py` _+67 more__
- **2026-10-20** [`9f83fc4805`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f83fc4805) [#20547](https://github.com/NVIDIA/TensorRT-LLM/pull/20547)
  [None][fix] Pass every expert's input_scale to the glm5_next NVFP4 MoE loader (#20547)
  _Files: `tensorrt_llm/_torch/models/modeling_glm5_next.py`, `tests/unittest/_torch/modeling/test_glm5_next_contracts.py`_
- **2026-10-19** [`47de5e4c9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/47de5e4c9c) [#20390](https://github.com/NVIDIA/TensorRT-LLM/pull/20390)
  [None][perf] GLM-5.3-Flash C++ kernel speedups: vectorized FP8 1x128 quant and 288-expert router GEMM (#20390)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm_kernel.cuh`, `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`, `cpp/tensorrt_llm/thop/dsv3RouterGemmOp.cpp`, `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py` _+1 more__
- **2026-10-19** [`a3766d68f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3766d68f9) [#20134](https://github.com/NVIDIA/TensorRT-LLM/pull/20134)
  [TRTLLM-15766][refactor] Decouple decoder tests from private methods and split DecoderRunner by phase (#20134)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py` _+45 more__

## Disaggregation / KV  (17 commits)

- **2026-10-26** [`61dc60586b`](https://github.com/NVIDIA/TensorRT-LLM/commit/61dc60586b) [#20447](https://github.com/NVIDIA/TensorRT-LLM/pull/20447)
  [https://nvbugs/6920457][fix] Document True as the use_kv_cache_manager_v2 default in the KV cache guide… (#20447)
  _Files: `docs/source/features/kvcache.md`_
- **2026-10-26** [`dd75334918`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd75334918) [#20736](https://github.com/NVIDIA/TensorRT-LLM/pull/20736)
  [None][feat] TTFT-percentile GEN admission for disaggregated serving, and a fix for a context-chunk replay after a skipped forward (#20736)
  _Files: `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/request_utils.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/gen_admission_queue.py` _+10 more__
- **2026-10-25** [`b96ba434e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b96ba434e8) [#20679](https://github.com/NVIDIA/TensorRT-LLM/pull/20679)
  [TRTLLM-17184][fix] Avoid global stop-word buffer growth in the PyTorch sampler (#20679)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tensorrt_llm/_torch/pyexecutor/sampler/finish_reasons.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/triton.py` _+10 more__
- **2026-10-25** [`315f04f225`](https://github.com/NVIDIA/TensorRT-LLM/commit/315f04f225) [#20889](https://github.com/NVIDIA/TensorRT-LLM/pull/20889)
  [None][fix] retry wrapped connection resets with transient budget (#20889)
  _Files: `tensorrt_llm/serve/openai_client.py`, `tests/unittest/disaggregated/test_disagg_openai_client.py`_
- **2026-10-23** [`e139d884a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e139d884a9) [#20388](https://github.com/NVIDIA/TensorRT-LLM/pull/20388)
  [TRTLLM-16628][refactor] BREAKING: Migrate LlmRequest fields to Python (#20388)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/include/tensorrt_llm/executor/serialization.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp` _+27 more__
- **2026-10-23** [`fa2eda12c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa2eda12c4) [#20740](https://github.com/NVIDIA/TensorRT-LLM/pull/20740)
  [https://nvbugs/6960771][fix] Expect decode blocks in V2 KV cache stored events (#20740)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm_kv_cache_events.py`_
- **2026-10-22** [`59f6df243b`](https://github.com/NVIDIA/TensorRT-LLM/commit/59f6df243b) [#20598](https://github.com/NVIDIA/TensorRT-LLM/pull/20598)
  [https://nvbugs/6933668][fix] Fix dead links failing test_http_url_validity (#20598)
  _Files: `tests/unittest/disaggregated/lifecycle_acceptance.md`_
- **2026-10-22** [`b3893e4283`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3893e4283) [#19465](https://github.com/NVIDIA/TensorRT-LLM/pull/19465)
  [TRTLLM-17134][fix] Survive a failed forward step in the executor loops (#19465)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py` _+6 more__
- **2026-10-22** [`d4cfc12f19`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4cfc12f19) [#20129](https://github.com/NVIDIA/TensorRT-LLM/pull/20129)
  [TRTLLM-16186][refactor] Breaking: Drop KV manager V1 support from transceiver V2 (#20129)
  _Files: `docs/source/features/disagg-serving.md`, `examples/disaggregated/slurm/cache_transceiver_test/report.py`, `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `examples/disaggregated/slurm/cache_transceiver_test/submit.py` _+44 more__
- **2026-10-21** [`ec3352fee2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec3352fee2) [#19964](https://github.com/NVIDIA/TensorRT-LLM/pull/19964)
  [TRTLLM-16711][feat] merge two renders into a standalone serve/render for dynamo (#19964)
  _Files: `docs/source/commands/trtllm-serve/index.rst`, `docs/source/commands/trtllm-serve/render-endpoints.md`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `jenkins/L0_MergeRequest.groovy` _+39 more__
- **2026-10-20** [`41913522c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/41913522c7) [#20086](https://github.com/NVIDIA/TensorRT-LLM/pull/20086)
  [None][feat] Add native KV cache retention to KVCM V2 (#20086)
  _Files: `cpp/include/tensorrt_llm/batch_manager/common.h`, `cpp/tensorrt_llm/batch_manager/evictionPolicy.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h` _+52 more__
- **2026-10-20** [`aeca563223`](https://github.com/NVIDIA/TensorRT-LLM/commit/aeca563223) [#19472](https://github.com/NVIDIA/TensorRT-LLM/pull/19472)
  [None][test] Migrate legacy disaggregated E2E transceiver paths (#19472)
- **2026-10-20** [`032ea6d414`](https://github.com/NVIDIA/TensorRT-LLM/commit/032ea6d414) [#20217](https://github.com/NVIDIA/TensorRT-LLM/pull/20217)
  [None][feat] Add the blob store driver boundary and an in-memory test driver (#20217)
  _Files: `tensorrt_llm/_torch/disaggregation/base/memory.py`, `tensorrt_llm/_torch/disaggregation/blob/__init__.py`, `tensorrt_llm/_torch/disaggregation/blob/keys.py`, `tensorrt_llm/_torch/disaggregation/blob/store.py` _+9 more__
- **2026-10-20** [`2325296424`](https://github.com/NVIDIA/TensorRT-LLM/commit/2325296424) [#19887](https://github.com/NVIDIA/TensorRT-LLM/pull/19887)
  [https://nvbugs/6799208][test] Unwaive test_disaggregated_overlap (#19887)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-20** [`fac6d3f794`](https://github.com/NVIDIA/TensorRT-LLM/commit/fac6d3f794) [#19710](https://github.com/NVIDIA/TensorRT-LLM/pull/19710)
  [TRTLLM-14924][feat] Reuse generation KV blocks across turns with KV cache manager V2 (#19710)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_compression_manager.py` _+7 more__
- **2026-10-20** [`d2e7f3b507`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2e7f3b507) [#20272](https://github.com/NVIDIA/TensorRT-LLM/pull/20272)
  [https://nvbugs/6906428][fix] Stop a leader-only precheck failure from deadlocking the instance (#20272)
  _Files: `jenkins/scripts/perf/disaggregated/slurm_ct_precheck_gate.sh`, `tests/scripts/perf-sanity/cache_transceiver_precheck/README.md`, `tests/scripts/perf-sanity/cache_transceiver_precheck/run_precheck.py`, `tests/unittest/others/test_cache_transceiver_precheck_config.py` _+1 more__
- **2026-10-19** [`51ef11b73c`](https://github.com/NVIDIA/TensorRT-LLM/commit/51ef11b73c) [#20140](https://github.com/NVIDIA/TensorRT-LLM/pull/20140)
  [https://nvbugs/6899682][fix] Isolate disaggregated client outputs per test (#20140)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_

## Other  (14 commits)

- **2026-10-26** [`21c22c6440`](https://github.com/NVIDIA/TensorRT-LLM/commit/21c22c6440) [#20832](https://github.com/NVIDIA/TensorRT-LLM/pull/20832)
  [None][build] Improve cpp/tests/CMakeLists.txt (#20832)
  _Files: `cpp/tests/CMakeLists.txt`_
- **2026-10-26** [`b7bfae8eb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7bfae8eb0) [#20748](https://github.com/NVIDIA/TensorRT-LLM/pull/20748)
  [https://nvbugs/6937268][fix] Ignore recoverable pip download retry warnings (#20748)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/test_common/error_utils.py`, `tests/unittest/others/test_http_utils_fail_fast.py`_
- **2026-10-26** [`687359e228`](https://github.com/NVIDIA/TensorRT-LLM/commit/687359e228) [#20892](https://github.com/NVIDIA/TensorRT-LLM/pull/20892)
  [None][test] Remove unused model-path fixtures from integration conft… (#20892)
  _Files: `tests/integration/defs/conftest.py`, `tests/integration/defs/triton_server/conftest.py`_
- **2026-10-25** [`bb631bfbf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb631bfbf2) [#20948](https://github.com/NVIDIA/TensorRT-LLM/pull/20948)
  [TRTLLM-15863][fix] Raise ImportError with the cause when a lazily imported serve module raises AttributeError (#20948)
  _Files: `tensorrt_llm/serve/__init__.py`, `tests/unittest/others/test_lazy_getattr_errors.py`_
- **2026-10-23** [`f035671959`](https://github.com/NVIDIA/TensorRT-LLM/commit/f035671959) [#20880](https://github.com/NVIDIA/TensorRT-LLM/pull/20880)
  [https://nvbugs/6958731][fix] Use the tokenizer chat template when the processor has none (#20880)
  _Files: `tensorrt_llm/inputs/utils.py`, `tests/unittest/inputs/test_chat_template_dispatch.py`_
- **2026-10-23** [`b833b7c9ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/b833b7c9ab) [#20749](https://github.com/NVIDIA/TensorRT-LLM/pull/20749)
  [https://nvbugs/6958731][chore] Report benchmark readiness request rejections (#20749)
  _Files: `tests/integration/defs/perf/agentx_client.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/scripts/test_perf_client_readiness.py`_
- **2026-10-23** [`9f50993e71`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f50993e71) [#20738](https://github.com/NVIDIA/TensorRT-LLM/pull/20738)
  [https://nvbugs/6631760][fix] Bump PyNvVideoCodec to >=2.2.0 to addre… (#20738)
  _Files: `requirements.txt`_
- **2026-10-22** [`491fe185c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/491fe185c6) [#20232](https://github.com/NVIDIA/TensorRT-LLM/pull/20232)
  [None][chore] Mass merge release/1.3 branch back to main (#20232)
- **2026-10-22** [`9e6e04b21c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e6e04b21c) [#20701](https://github.com/NVIDIA/TensorRT-LLM/pull/20701)
  [https://nvbugs/6942751][test] Use MSA backend in MiniMax-M3 multi-node eval test (#20701)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_node4_gpu16.yml`_
- **2026-10-21** [`12accb2d5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/12accb2d5e) [#19920](https://github.com/NVIDIA/TensorRT-LLM/pull/19920)
  [None][fix] hash offline-loaded videos like the serve path (#19920)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tensorrt_llm/inputs/utils.py`, `tests/unittest/inputs/test_video_decode.py`_
- **2026-10-20** [`0829689c52`](https://github.com/NVIDIA/TensorRT-LLM/commit/0829689c52) [#20630](https://github.com/NVIDIA/TensorRT-LLM/pull/20630)
  [None][doc] Remove issue-approval requirement from CONTRIBUTING.md (#20630)
  _Files: `CONTRIBUTING.md`_
- **2026-10-20** [`c018848da6`](https://github.com/NVIDIA/TensorRT-LLM/commit/c018848da6) [#20575](https://github.com/NVIDIA/TensorRT-LLM/pull/20575)
  [None][fix] Encode VisualGen video without a GIL-held frame copy (#20575)
  _Files: `tensorrt_llm/media/encoding.py`_
- **2026-10-20** [`c14609482b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c14609482b) [#19275](https://github.com/NVIDIA/TensorRT-LLM/pull/19275)
  [TRTLLM-14558][chore] Split cute_dsl_kernels/ into the domain kernel trees and consolidate the thop unit tests (#19275)
- **2026-10-19** [`335e0b1057`](https://github.com/NVIDIA/TensorRT-LLM/commit/335e0b1057) [#19980](https://github.com/NVIDIA/TensorRT-LLM/pull/19980)
  [None][chore] Sync Claude Code agents and skills from trtllm-agent-toolkit (#19980)

## Torch Path (_torch)  (11 commits)

- **2026-10-26** [`8ea175e248`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ea175e248) [#20228](https://github.com/NVIDIA/TensorRT-LLM/pull/20228)
  [None][fix] Honor deterministic mode in fused mHC dispatch (#20228)
  _Files: `tensorrt_llm/_torch/modules/mhc/mhc_cuda.py`, `tests/unittest/_torch/modules/test_mhc.py`_
- **2026-10-24** [`f1d8a73f64`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1d8a73f64) [#19721](https://github.com/NVIDIA/TensorRT-LLM/pull/19721)
  [https://nvbugs/6848775][fix] Set `metadata._num_tokens = live_tokens` before `_build_msa_fields()` (what… (#19721)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/multi_gpu/test_minimax_m3_piecewise.py`_
- **2026-10-23** [`90d4dcbb8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/90d4dcbb8f) [#19773](https://github.com/NVIDIA/TensorRT-LLM/pull/19773)
  [None][perf] Fuse SwiGLU into the BF16 gate/up GEMM epilogue on SM100 (#19773)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/modules/gate_up_swiglu_quack.py`, `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/transformer_minimax_h3.py` _+3 more__
- **2026-10-23** [`96de4749c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/96de4749c5) [#20688](https://github.com/NVIDIA/TensorRT-LLM/pull/20688)
  [None][perf] Add torch.compile decorator for mamba replay input prep (#20688)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`_
- **2026-10-23** [`b0af321b0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0af321b0c) [#20334](https://github.com/NVIDIA/TensorRT-LLM/pull/20334)
  [None][fix] Keep low-M GEMM outputs distinct during CUDA graph capture (#20334)
  _Files: `tensorrt_llm/_torch/modules/low_m_gemm.py`_
- **2026-10-23** [`34e813733b`](https://github.com/NVIDIA/TensorRT-LLM/commit/34e813733b) [#20226](https://github.com/NVIDIA/TensorRT-LLM/pull/20226)
  [None][fix] Keep GDN decode recurrence stable in deterministic mixed batches (#20226)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_gdn_mixed_decode.py`_
- **2026-10-23** [`f806023111`](https://github.com/NVIDIA/TensorRT-LLM/commit/f806023111) [#20780](https://github.com/NVIDIA/TensorRT-LLM/pull/20780)
  [https://nvbugs/6812381][fix] Split GB200-4_GPUs-PyTorch-Post-Merge into two shards (#20780)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-23** [`c7fe92ba08`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7fe92ba08) [#20333](https://github.com/NVIDIA/TensorRT-LLM/pull/20333)
  [TRTLLM-17015][feat] VisualGen: wire async_ulysses for MiniMax-H3 (#20333)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/transformer_minimax_h3.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_minimax_h3_parallel.py`, `tests/unittest/_torch/visual_gen/test_minimax_h3_transformer.py`_
- **2026-10-21** [`522daa8cdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/522daa8cdf) [#20699](https://github.com/NVIDIA/TensorRT-LLM/pull/20699)
  [None][perf] MiniMax-M3: BF16-split tensor-core router GEMM (#20699)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/models/test_minimax_m3.py`_
- **2026-10-20** [`d281e21fb7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d281e21fb7) [#20594](https://github.com/NVIDIA/TensorRT-LLM/pull/20594)
  [https://nvbugs/6933914][fix] Handle per-token timesteps in Wan I2V TeaCache (#20594)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tests/unittest/_torch/visual_gen/test_teacache.py`_
- **2026-10-20** [`89df99f672`](https://github.com/NVIDIA/TensorRT-LLM/commit/89df99f672) [#19401](https://github.com/NVIDIA/TensorRT-LLM/pull/19401)
  [TRTLLM-15717][fix] Remove TRTLLM_VIDEO_ASYNC_ENCODE and clean up the encode a delete cancels (#19401)
  _Files: `tensorrt_llm/serve/openai_video_routes.py`, `tests/unittest/_torch/visual_gen/test_trtllm_serve_endpoints.py`_

## Quantization  (9 commits)

- **2026-10-24** [`e707e62fc4`](https://github.com/NVIDIA/TensorRT-LLM/commit/e707e62fc4) [#20517](https://github.com/NVIDIA/TensorRT-LLM/pull/20517)
  [None][feat] Staircase: GLM-5.2 NVFP4 low-latency decode target for Rubin (modeling_v2, TP16) (#20517)
- **2026-10-23** [`bde3302fed`](https://github.com/NVIDIA/TensorRT-LLM/commit/bde3302fed)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+8 more__
- **2026-10-22** [`dfcc6f0d95`](https://github.com/NVIDIA/TensorRT-LLM/commit/dfcc6f0d95) [#20007](https://github.com/NVIDIA/TensorRT-LLM/pull/20007)
  [None][feat] Run static FP8 Cosmos3 with TP/Ulysses/CFG and support the FP8 4-step distilled checkpoints (#20007)
  _Files: `examples/visual_gen/configs/cosmos3-fp8-1gpu.yaml`, `examples/visual_gen/models/cosmos3/README.md`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_cosmos3_transformer_parallel.py` _+1 more__
- **2026-10-22** [`9bb7931d6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bb7931d6e) [#20413](https://github.com/NVIDIA/TensorRT-LLM/pull/20413)
  [https://nvbugs/6932341][fix] Resolve Wan quantization per transformer (#20413)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/config.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/visual_gen/test_model_loader.py`_
- **2026-10-20** [`6ee61c6a66`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ee61c6a66) [#20202](https://github.com/NVIDIA/TensorRT-LLM/pull/20202)
  [None][test] Add GB300 DeepSeek V4.1 NVFP4 DSpark core coverage (#20202)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-10-20** [`d75360ec90`](https://github.com/NVIDIA/TensorRT-LLM/commit/d75360ec90)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+5 more__
- **2026-10-19** [`6774ce4dd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6774ce4dd9)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-10-19** [`4d5f55a301`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d5f55a301) [#20443](https://github.com/NVIDIA/TensorRT-LLM/pull/20443)
  [None][fix] Load MXFP8 fused weight scales with the rows of their weights (#20443)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tests/unittest/_torch/modules/test_mxfp8_linear.py`_
- **2026-10-19** [`d4624cb517`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4624cb517)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+6 more__

## Models  (7 commits)

- **2026-10-24** [`abb94ab8fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/abb94ab8fc) [#20663](https://github.com/NVIDIA/TensorRT-LLM/pull/20663)
  [https://nvbugs/6921831][fix] Schedule Gemma4 multimodal encoder items under the encoder budget (#20663)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4_unified.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tests/unittest/_torch/modeling/test_gemma4_multimodal.py`_
- **2026-10-23** [`af254e4cf5`](https://github.com/NVIDIA/TensorRT-LLM/commit/af254e4cf5) [#20613](https://github.com/NVIDIA/TensorRT-LLM/pull/20613)
  [None][test] Add the Kimi-K3 AgentX ctx_only lanes to GB300 post-merge perf-sanity (#20613)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/agentx_client.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_gen1_node2_gpu8.yml`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_gen1_node4_gpu16.yml` _+2 more__
- **2026-10-21** [`b64da9588f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b64da9588f) [#20671](https://github.com/NVIDIA/TensorRT-LLM/pull/20671)
  [None][test] Add coverage for Gemma4AssistantForCausalLM (#20671)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modeling/test_gemma4_assistant.py`_
- **2026-10-21** [`b44310c96a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b44310c96a) [#20677](https://github.com/NVIDIA/TensorRT-LLM/pull/20677)
  [None][test] Remove DeepSeek-R1 from the CI perf-sanity lists (#20677)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml` _+13 more__
- **2026-10-20** [`75e296f64c`](https://github.com/NVIDIA/TensorRT-LLM/commit/75e296f64c) [#20525](https://github.com/NVIDIA/TensorRT-LLM/pull/20525)
  [None][docs] Explain Nemotron's use of the Qwen3-Coder tool parser (#20525)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/deployment-guide/deployment-guide-for-nemotron-3-on-trtllm.md`, `tensorrt_llm/serve/tool_parser/qwen3_coder_parser.py`_
- **2026-10-19** [`fda7ebd410`](https://github.com/NVIDIA/TensorRT-LLM/commit/fda7ebd410) [#20593](https://github.com/NVIDIA/TensorRT-LLM/pull/20593)
  [None][test] Add coverage for Qwen3ForCausalLM (#20593)
  _Files: `tests/unittest/_torch/modeling/test_modeling_qwen3.py`_
- **2026-10-19** [`066332abd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/066332abd5) [#19405](https://github.com/NVIDIA/TensorRT-LLM/pull/19405)
  [https://nvbugs/6784181][fix] Add an exact-path SPHINX_GENERATED_DOC_PAGES allowlist keyed off helper.py's… (#19405)
  _Files: `tests/integration/defs/test_doc.py`, `tests/integration/test_lists/waives.txt`_

## LoRA  (6 commits)

- **2026-10-26** [`da002dbcb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/da002dbcb3) [#20874](https://github.com/NVIDIA/TensorRT-LLM/pull/20874)
  [None][fix] Anthropic Messages: no whitespace-only text blocks (#20874)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_
- **2026-10-26** [`0a97382613`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a97382613) [#20867](https://github.com/NVIDIA/TensorRT-LLM/pull/20867)
  [None][fix] Anthropic Messages: read the chat stream to its end so its metrics are recorded (#20867)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_routes.py`_
- **2026-10-26** [`a6fde392d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6fde392d0) [#20775](https://github.com/NVIDIA/TensorRT-LLM/pull/20775)
  [TRTLLM-16711][fix] Remove the legacy renderer paths (#20775)
  _Files: `tensorrt_llm/serve/chat_tokenization.py`, `tensorrt_llm/serve/harmony_adapter.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/render/__init__.py` _+9 more__
- **2026-10-24** [`9666d7427a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9666d7427a) [#20774](https://github.com/NVIDIA/TensorRT-LLM/pull/20774)
  [https://nvbugs/6858520][fix] Reload a request's LoRA adapter in the format it was admitted with (#20774)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/request_utils.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/executor/base_worker.py` _+1 more__
- **2026-10-20** [`a584f5e2ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/a584f5e2ae) [#20611](https://github.com/NVIDIA/TensorRT-LLM/pull/20611)
  [TRTLLM-14691][doc] Add documentation on LoRA performance tuning knobs (#20611)
  _Files: `docs/source/features/lora.md`_
- **2026-10-19** [`72cd8b57a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/72cd8b57a3) [#20477](https://github.com/NVIDIA/TensorRT-LLM/pull/20477)
  [https://nvbugs/6939562][fix] Bound module_out_sizes read in LoRA param-fill kernel (#20477)
  _Files: `cpp/tensorrt_llm/kernels/lora/loraGroupGEMMParamFillRowReorderFusion.cu`_

## ROCm / AMD  (5 commits)

- **2026-10-25** [`b7d6e624d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7d6e624d1) [#20953](https://github.com/NVIDIA/TensorRT-LLM/pull/20953)
  [None][infra] Waive 70 failed cases for main in pre-merge 66148 (function-level waives for test_lora_ownership) (#20953)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-24** [`87342f4474`](https://github.com/NVIDIA/TensorRT-LLM/commit/87342f4474) [#20270](https://github.com/NVIDIA/TensorRT-LLM/pull/20270)
  [TRTLLM-15763][refactor] Narrow the runner surface, slim engine state, and make the engine's executor interface explicit (#20270)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md` _+48 more__
- **2026-10-23** [`448321fb98`](https://github.com/NVIDIA/TensorRT-LLM/commit/448321fb98) [#20605](https://github.com/NVIDIA/TensorRT-LLM/pull/20605)
  [https://nvbugs/6913865][fix] Scope multimodal LoRA to the decoder (#20605)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma3vl.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/models/modeling_mistral.py` _+16 more__
- **2026-10-22** [`27842d513c`](https://github.com/NVIDIA/TensorRT-LLM/commit/27842d513c) [#19822](https://github.com/NVIDIA/TensorRT-LLM/pull/19822)
  [None][chore] Share KV transfer lifecycle enforcement primitives (#19822)
  _Files: `tensorrt_llm/_torch/disaggregation/lifecycle/README.md`, `tensorrt_llm/_torch/disaggregation/lifecycle/__init__.py`, `tensorrt_llm/_torch/disaggregation/lifecycle/retirement.py`, `tensorrt_llm/_torch/disaggregation/native/ownership.py` _+4 more__
- **2026-10-21** [`a9000fe10e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9000fe10e) [#20117](https://github.com/NVIDIA/TensorRT-LLM/pull/20117)
  [TRTLLM-16186][feat] Define backend contract for KV cache transfers (#20117)
  _Files: `tensorrt_llm/_torch/disaggregation/base/__init__.py`, `tensorrt_llm/_torch/disaggregation/base/backend.py`, `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/extent.py` _+19 more__

## Docs / Examples  (4 commits)

- **2026-10-23** [`ddc7e3c129`](https://github.com/NVIDIA/TensorRT-LLM/commit/ddc7e3c129) [#20348](https://github.com/NVIDIA/TensorRT-LLM/pull/20348)
  [https://nvbugs/6920458][fix] Correct the stale tokens_per_block default in the long-sequence guide (#20348)
  _Files: `docs/source/features/long-sequence.md`_
- **2026-10-21** [`7f0caf443e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f0caf443e) [#20297](https://github.com/NVIDIA/TensorRT-LLM/pull/20297)
  [https://nvbugs/6925906][fix] Floor gen_only device-step-time baselines at the expected-bucket cutover (#20297)
  _Files: `tests/integration/defs/perf/README_perf_regression_system.md`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/open_search_db_utils.py`, `tests/integration/defs/perf/perf_regression_utils.py` _+2 more__
- **2026-10-21** [`93b17dcdd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/93b17dcdd9)
  [None][chore] Bump version to 1.4.0rc2
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-10-20** [`a341bce742`](https://github.com/NVIDIA/TensorRT-LLM/commit/a341bce742) [#20607](https://github.com/NVIDIA/TensorRT-LLM/pull/20607)
  [TRTLLM-16212][doc] Clarify documentation on TRTLLM_CACHE_DIR unified caching (#20607)
  _Files: `docs/source/llm-api/index.md`_

## Speculative Decoding  (3 commits)

- **2026-10-24** [`a0cee56d3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0cee56d3a) [#20626](https://github.com/NVIDIA/TensorRT-LLM/pull/20626)
  [https://nvbugs/6963167][fix] MiniMax-M3 VL: serve-rendered prompts, video token counts, speculative decoding and KV reuse on multimodal requests (#20626)
  _Files: `docs/source/features/multi-modality.md`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3_vl.py`, `tensorrt_llm/inputs/data.py` _+11 more__
- **2026-10-23** [`5f4e3d2ff5`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f4e3d2ff5) [#20438](https://github.com/NVIDIA/TensorRT-LLM/pull/20438)
  [None][chore] Deprecate ngram/user-provided spec dec (#20438)
  _Files: `docs/source/features/speculative-decoding.md`, `examples/ngram/README.md`, `tensorrt_llm/_torch/speculative/auto_heuristic.py`, `tensorrt_llm/llmapi/llm_args.py`_
- **2026-10-20** [`083447cd22`](https://github.com/NVIDIA/TensorRT-LLM/commit/083447cd22) [#20366](https://github.com/NVIDIA/TensorRT-LLM/pull/20366)
  [#20365][fix] Use the fused DSpark RMSNorm/RoPE kernels on SM107 (#20366)
  _Files: `tensorrt_llm/_torch/custom_ops/dspark_rmsnorm_rope_custom_op.py`, `tests/unittest/_torch/speculative/test_dspark_cute_dsl_rmsnorm_rope.py`_

## Compilation / Graph  (2 commits)

- **2026-10-24** [`61dba71bb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/61dba71bb0) [#19080](https://github.com/NVIDIA/TensorRT-LLM/pull/19080)
  [TRTLLM-15840][test] Restore LTX-2 worker CUDA graph regression (#19080)
- **2026-10-24** [`16f188965f`](https://github.com/NVIDIA/TensorRT-LLM/commit/16f188965f) [#19080](https://github.com/NVIDIA/TensorRT-LLM/pull/19080)
  [TRTLLM-15840][test] Restore LTX-2 worker CUDA graph regression (#19080)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/ltx2_trtllm_backend_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media_ltx2.zip`, `tests/integration/defs/examples/visual_gen/test_visual_gen_ltx2.py`, `tests/integration/test_lists/waives.txt`_

---
_Generated 2026-10-26 15:18 UTC_