# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-07-06 → 2026-07-13  |  **Total commits:** 203

## ✨ New Features This Week

- **2026-07-13** [#15752](https://github.com/NVIDIA/TensorRT-LLM/pull/15752) — [None][feat] add commit min snapshot for SSM reuse (#15752)
- **2026-07-13** [#16053](https://github.com/NVIDIA/TensorRT-LLM/pull/16053) — [None][feat] Support externally provided MPI sessions with explicit ownership (#16053)
- **2026-07-13** [#15823](https://github.com/NVIDIA/TensorRT-LLM/pull/15823) — [None][feat] add per-model KV cache manager v2 auto selection (#15823)
- **2026-07-13** [#16054](https://github.com/NVIDIA/TensorRT-LLM/pull/16054) — [None][feat] Add an opt-in raw-weight cache to the HF weight loader (#16054)
- **2026-07-11** [#15900](https://github.com/NVIDIA/TensorRT-LLM/pull/15900) — [TRTLLM-13776][feat] Add Piecewise CUDA Graph support for Qwen3.5/Qwen3.6 MoE model (#15900)
- **2026-07-11** [#16074](https://github.com/NVIDIA/TensorRT-LLM/pull/16074) — [TRTLLM-14138][perf] Add fused kernels for Gemma4 serving (#16074)
- **2026-07-10** [#15424](https://github.com/NVIDIA/TensorRT-LLM/pull/15424) — [TRTLLM-13035][feat] Native /v1/embeddings dynamic batching for encoder-only models (#15424)
- **2026-07-10** [#16114](https://github.com/NVIDIA/TensorRT-LLM/pull/16114) — [None][test] KV cache manager v2: add V2 + VSWA multi-GPU test coverage (#16114)
- **2026-07-10** [#16113](https://github.com/NVIDIA/TensorRT-LLM/pull/16113) — [None][test] bench_moe: add nsys capture-range support (--nsys) (#16113)
- **2026-07-10** [#15816](https://github.com/NVIDIA/TensorRT-LLM/pull/15816) — [TRTLLM-13409][feat] proxy fast-death detection + sticky EngineDeadError (#15816)
- _…and 30 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-13** [`6c43b3eddc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c43b3eddc) [#16053](https://github.com/NVIDIA/TensorRT-LLM/pull/16053) — [None][feat] Support externally provided MPI sessions with explicit ownership (#16053)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-06-19 |
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
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
| CI / Infra | 57 |
| Executor / Runtime | 28 |
| Attention | 27 |
| MoE | 22 |
| Other | 15 |
| Disaggregation / KV | 13 |
| Quantization | 12 |
| Torch Path (_torch) | 8 |
| Speculative Decoding | 7 |
| AutoDeploy | 5 |
| Models | 4 |
| Perf | 2 |
| ROCm / AMD | 1 |
| Docs / Examples | 1 |
| LoRA | 1 |

## CI / Infra  (57 commits)

- **2026-07-13** [`01291f9466`](https://github.com/NVIDIA/TensorRT-LLM/commit/01291f9466) [#16180](https://github.com/NVIDIA/TensorRT-LLM/pull/16180)
  [https://nvbugs/6379333] [chore] Unwaive test cases (#16180)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`53d2bde62f`](https://github.com/NVIDIA/TensorRT-LLM/commit/53d2bde62f) [#16308](https://github.com/NVIDIA/TensorRT-LLM/pull/16308)
  [https://nvbugs/6437410][chore] Waive a failed test in pre-merge CI (#16308)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`6bd6bb888d`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bd6bb888d) [#16283](https://github.com/NVIDIA/TensorRT-LLM/pull/16283)
  [None][test] Waive 1 failed cases for main in QA CI (#16283)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`75e80082d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/75e80082d3) [#16296](https://github.com/NVIDIA/TensorRT-LLM/pull/16296)
  [None][test] Waive 4 failed cases for main in QA CI (#16296)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`ffe313d5c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffe313d5c3) [#16295](https://github.com/NVIDIA/TensorRT-LLM/pull/16295)
  [None][test] Waive 6 failed cases for main in QA CI (#16295)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`29bda273bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/29bda273bf) [#16271](https://github.com/NVIDIA/TensorRT-LLM/pull/16271)
  [None][test] Waive 9 failed cases for main in QA CI (#16271)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`770ebc5db5`](https://github.com/NVIDIA/TensorRT-LLM/commit/770ebc5db5) [#16292](https://github.com/NVIDIA/TensorRT-LLM/pull/16292)
  [None][infra] Waive 7 failed cases for main in post-merge 2835 (#16292)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-10** [`e523b430c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e523b430c9) [#16206](https://github.com/NVIDIA/TensorRT-LLM/pull/16206)
  [None][chore] Remove pre-installed opencv (#16206)
  _Files: `docker/Dockerfile.multi`, `docker/common/install.sh`, `docs/source/features/multi-modality.md`, `jenkins/L0_Test.groovy` _+5 more__
- **2026-07-10** [`b9838f531b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9838f531b) [#16182](https://github.com/NVIDIA/TensorRT-LLM/pull/16182)
  [TRTLLMINF-191][infra] Make S3 stdout echo opt-in (#16182)
  _Files: `jenkins/L0_Test.groovy`, `tests/test_common/s3_output.py`, `tests/unittest/test_s3_output.py`, `tests/unittest/tools/test_test_to_stage_mapping.py`_
- **2026-07-10** [`aedf23c592`](https://github.com/NVIDIA/TensorRT-LLM/commit/aedf23c592) [#14785](https://github.com/NVIDIA/TensorRT-LLM/pull/14785)
  [https://nvbugs/6221055][fix] added four GB300 rows to agg_unit_mem_df.csv (#14785)
  _Files: `tests/integration/defs/agg_unit_mem_df.csv`, `tests/integration/defs/test_unittests.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-10** [`10d4ae7f96`](https://github.com/NVIDIA/TensorRT-LLM/commit/10d4ae7f96) [#16181](https://github.com/NVIDIA/TensorRT-LLM/pull/16181)
  [None][fix] Improve scope conflict handling in Selector class (#16181)
  _Files: `jenkins/scripts/cbts/main.py`_
- **2026-07-10** [`64bd016071`](https://github.com/NVIDIA/TensorRT-LLM/commit/64bd016071) [#15953](https://github.com/NVIDIA/TensorRT-LLM/pull/15953)
  [TRTLLMINF-113][infra] Refine Setup/Initialize timeout granularity (#15953)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/bash_utils.sh`, `jenkins/scripts/slurm_install.sh`_
- **2026-07-10** [`93175b8142`](https://github.com/NVIDIA/TensorRT-LLM/commit/93175b8142) [#15971](https://github.com/NVIDIA/TensorRT-LLM/pull/15971)
  [TRTLLMINF-172][infra] Block multi-GPU tests when single-GPU tests fail (#15971)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-07-10** [`888fe83949`](https://github.com/NVIDIA/TensorRT-LLM/commit/888fe83949) [#16210](https://github.com/NVIDIA/TensorRT-LLM/pull/16210)
  [None][infra] Add blossom-ci authorized users (#16210)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-09** [`d7beb70d16`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7beb70d16) [#16208](https://github.com/NVIDIA/TensorRT-LLM/pull/16208)
  [None][ci] Update golden telemetry manifest (#16208)
  _Files: `tensorrt_llm/usage/llm_args_golden_manifest.json`_
- **2026-07-09** [`dca857f757`](https://github.com/NVIDIA/TensorRT-LLM/commit/dca857f757) [#16019](https://github.com/NVIDIA/TensorRT-LLM/pull/16019)
  [https://nvbugs/6418912][fix] NVBUG 6418912 integration validation (#16019)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/bufferIndexHolderTest.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`, `jenkins/L0_Test.groovy` _+2 more__
- **2026-07-09** [`cbef223181`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbef223181) [#15428](https://github.com/NVIDIA/TensorRT-LLM/pull/15428)
  [TRTLLMINF-94][infra] Toggle ENABLE_BOLT_COMPATIBLE (#15428)
  _Files: `cpp/CMakeLists.txt`, `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`_
- **2026-07-09** [`93abfe2f27`](https://github.com/NVIDIA/TensorRT-LLM/commit/93abfe2f27) [#16079](https://github.com/NVIDIA/TensorRT-LLM/pull/16079)
  [None][fix] Retry SLURM dispatcher pod launch failures (#16079)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-09** [`fab39a7c05`](https://github.com/NVIDIA/TensorRT-LLM/commit/fab39a7c05) [#15992](https://github.com/NVIDIA/TensorRT-LLM/pull/15992)
  [TRTLLMINF-81][fix] Scope SLURM retry node-avoidance to the target cluster (#15992)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-09** [`7a932cf25c`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a932cf25c) [#16186](https://github.com/NVIDIA/TensorRT-LLM/pull/16186)
  [None][infra] Waive 2 failed cases for main in pre-merge 46981 (#16186)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-09** [`8ef7190ebf`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ef7190ebf) [#15619](https://github.com/NVIDIA/TensorRT-LLM/pull/15619)
  [TRTLLMINF-144][infra] Only display rerun test results in the rerun report (#15619)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/test_rerun.py`_
- **2026-07-09** [`50f0bf43a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/50f0bf43a3) [#16169](https://github.com/NVIDIA/TensorRT-LLM/pull/16169)
  [None][infra] Waive 4 failed cases for main in post-merge 2827 (#16169)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-09** [`3f526cf949`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f526cf949) [#16139](https://github.com/NVIDIA/TensorRT-LLM/pull/16139)
  [https://nvbugs/6422299][fix] Setup dependency for Cosmos3 nano t2v LPIPS test (#16139)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`4cd00bb3da`](https://github.com/NVIDIA/TensorRT-LLM/commit/4cd00bb3da) [#16146](https://github.com/NVIDIA/TensorRT-LLM/pull/16146)
  [https://nvbugs/6427411][chore] Waive additional PP sampler regressions (#16146)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`494a3e671f`](https://github.com/NVIDIA/TensorRT-LLM/commit/494a3e671f) [#16127](https://github.com/NVIDIA/TensorRT-LLM/pull/16127)
  [https://nvbugs/6427411][chore] Waive remaining PP sampler regressions (#16127)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`24d598862d`](https://github.com/NVIDIA/TensorRT-LLM/commit/24d598862d) [#16109](https://github.com/NVIDIA/TensorRT-LLM/pull/16109)
  [None][infra] Waive 23 failed cases for main in post-merge 2826 (#16109)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`367653e430`](https://github.com/NVIDIA/TensorRT-LLM/commit/367653e430) [#16105](https://github.com/NVIDIA/TensorRT-LLM/pull/16105)
  [https://nvbugs/6427411][chore] Waive a failed test in Pre-merge (#16105)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`8c1b230c81`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c1b230c81) [#16103](https://github.com/NVIDIA/TensorRT-LLM/pull/16103)
  [https://nvbugs/6427411][chore] Waive failed tests in Pre-merge (#16103)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`3eb7feb4f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3eb7feb4f9) [#16100](https://github.com/NVIDIA/TensorRT-LLM/pull/16100)
  [None][infra] Waive 1 failed cases for main in pre-merge 46666 (#16100)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`73d3abca84`](https://github.com/NVIDIA/TensorRT-LLM/commit/73d3abca84) [#16097](https://github.com/NVIDIA/TensorRT-LLM/pull/16097)
  [None][test] Waive 2 failed cases for main in QA CI (#16097)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`126461f8db`](https://github.com/NVIDIA/TensorRT-LLM/commit/126461f8db) [#15935](https://github.com/NVIDIA/TensorRT-LLM/pull/15935)
  [https://nvbugs/6236818][ci] Re-enable Verl post-merge CI stage (#15935)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/verl/verl_config.yml`_
- **2026-07-08** [`74e848c60d`](https://github.com/NVIDIA/TensorRT-LLM/commit/74e848c60d) [#16093](https://github.com/NVIDIA/TensorRT-LLM/pull/16093)
  [None][infra] Waive 10 failed cases for main in post-merge 2825 (#16093)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`c01abddb34`](https://github.com/NVIDIA/TensorRT-LLM/commit/c01abddb34) [#16082](https://github.com/NVIDIA/TensorRT-LLM/pull/16082)
  [None][infra] Waive 1 failed cases for main in pre-merge 46573 (#16082)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`148bf8a923`](https://github.com/NVIDIA/TensorRT-LLM/commit/148bf8a923) [#13073](https://github.com/NVIDIA/TensorRT-LLM/pull/13073)
  [TRTLLM-10253][infra] upload test output to storage (#13073)
  _Files: `jenkins/L0_Test.groovy`, `requirements-dev.txt`, `tests/integration/defs/conftest.py`, `tests/integration/defs/local_venv.py` _+5 more__
- **2026-07-07** [`dc499389dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc499389dd) [#16058](https://github.com/NVIDIA/TensorRT-LLM/pull/16058)
  [None][test] Waive 9 failed cases for main in QA CI (#16058)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`32a953bb56`](https://github.com/NVIDIA/TensorRT-LLM/commit/32a953bb56) [#16032](https://github.com/NVIDIA/TensorRT-LLM/pull/16032)
  [None][test] Waive 4 failed cases for main in QA CI (#16032)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`0b0fd5400a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b0fd5400a) [#15830](https://github.com/NVIDIA/TensorRT-LLM/pull/15830)
  [None][infra] add disable-cbts flag to explicitly disable CBTS (#15830)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/tools/report_cbts_decision.py`_
- **2026-07-07** [`fe53bc3e07`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe53bc3e07) [#16039](https://github.com/NVIDIA/TensorRT-LLM/pull/16039)
  [None][infra] waive failing tests in Post Merge (#16039)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`5cefd67c4d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cefd67c4d) [#16046](https://github.com/NVIDIA/TensorRT-LLM/pull/16046)
  [None][infra] Add blossom-ci authorized users (#16046)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-07** [`41143d27b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/41143d27b8) [#16029](https://github.com/NVIDIA/TensorRT-LLM/pull/16029)
  [None][infra] Add blossom-ci authorized users (#16029)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-07** [`ecbeb682af`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecbeb682af) [#16034](https://github.com/NVIDIA/TensorRT-LLM/pull/16034)
  [None][test] Waive 7 failed cases for main in QA CI (#16034)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`39452fd6f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/39452fd6f2) [#16030](https://github.com/NVIDIA/TensorRT-LLM/pull/16030)
  [None][test] Waive 8 failed cases for main in QA CI (#16030)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`28172347c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/28172347c2) [#15979](https://github.com/NVIDIA/TensorRT-LLM/pull/15979)
  [https://nvbugs/6114139][test] Unwaive test_workers_kv_cache_events (#15979)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`a12bef974e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a12bef974e) [#16027](https://github.com/NVIDIA/TensorRT-LLM/pull/16027)
  [None][infra] Waive 16 failed cases for main in post-merge 2824 (#16027)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`011e8490c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/011e8490c1) [#15274](https://github.com/NVIDIA/TensorRT-LLM/pull/15274)
  [None][infra] PLC nightly pipeline update (#15274)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`, `jenkins/scripts/pulse_in_pipeline_scanning/main.py`, `jenkins/scripts/pulse_in_pipeline_scanning/submit_report.py`, `jenkins/scripts/pulse_in_pipeline_scanning/utils/report.py`_
- **2026-07-06** [`65bcb446ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/65bcb446ea) [#15856](https://github.com/NVIDIA/TensorRT-LLM/pull/15856)
  [None][infra] Bump pulse-container-scanner version (#15856)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`_
- **2026-07-06** [`ef6ebc2f2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef6ebc2f2c) [#15977](https://github.com/NVIDIA/TensorRT-LLM/pull/15977)
  [None][test] Waive 1 failed cases for main in QA CI (#15977)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`0044d5b5c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0044d5b5c9) [#15658](https://github.com/NVIDIA/TensorRT-LLM/pull/15658)
  [TRTLLMINF-126][infra] Generate timeout result when the tests all pass in the rerun step (#15658)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-06** [`4f1881d838`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f1881d838) [#15968](https://github.com/NVIDIA/TensorRT-LLM/pull/15968)
  [None][infra] Waive 5 failed cases for main in post-merge 2823 (#15968)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`9727b20ff8`](https://github.com/NVIDIA/TensorRT-LLM/commit/9727b20ff8) [#15874](https://github.com/NVIDIA/TensorRT-LLM/pull/15874)
  [None][infra] Coerce null CBTS PR diffs to empty string (#15874)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/main.py`_
- **2026-07-06** [`a4ed524c2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4ed524c2e) [#15967](https://github.com/NVIDIA/TensorRT-LLM/pull/15967)
  [None][infra] Waive 50 failed cases for main in post-merge 2822 (#15967)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`3b5ce7cdf9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b5ce7cdf9) [#15962](https://github.com/NVIDIA/TensorRT-LLM/pull/15962)
  [None][test] Waive 1 failed cases for main in QA CI (#15962)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`1728261f91`](https://github.com/NVIDIA/TensorRT-LLM/commit/1728261f91) [#15960](https://github.com/NVIDIA/TensorRT-LLM/pull/15960)
  [None][infra] Waive 11 failed cases for main in post-merge 2822 (#15960)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`90f90bea91`](https://github.com/NVIDIA/TensorRT-LLM/commit/90f90bea91) [#15770](https://github.com/NVIDIA/TensorRT-LLM/pull/15770)
  [None][infra] Fix KeyError for test names with spaces in generate_rerun_tests_list (#15770)
  _Files: `jenkins/scripts/test_rerun.py`_
- **2026-07-06** [`56aca69ecf`](https://github.com/NVIDIA/TensorRT-LLM/commit/56aca69ecf) [#15959](https://github.com/NVIDIA/TensorRT-LLM/pull/15959)
  [None][test] Remove 72 closed-bug waive entries for main (#15959)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`1ef55adad9`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ef55adad9)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-07-06** [`16430fd3e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/16430fd3e7) [#15946](https://github.com/NVIDIA/TensorRT-LLM/pull/15946)
  [None][infra] Waive 1 failed cases for main in pre-merge 46289 (#15946)
  _Files: `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (28 commits)

- **2026-07-13** [`17190cf7bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/17190cf7bb) [#15752](https://github.com/NVIDIA/TensorRT-LLM/pull/15752)
  [None][feat] add commit min snapshot for SSM reuse (#15752)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_config.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py` _+4 more__
- **2026-07-13** [`52fc8f465b`](https://github.com/NVIDIA/TensorRT-LLM/commit/52fc8f465b) [#15588](https://github.com/NVIDIA/TensorRT-LLM/pull/15588)
  [https://nvbugs/6330273][fix] Reserve worst-case SWA slots to avoid single-request deadlock (#15588)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_life_cycle_registry.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_storage_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_event_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-07-13** [`d6e9bf3355`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6e9bf3355) [#16248](https://github.com/NVIDIA/TensorRT-LLM/pull/16248)
  [https://nvbugs/6438658][fix] Avoid false disagg benchmark KV exhaustion (#16248)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-07-13** [`696904a6d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/696904a6d3) [#16197](https://github.com/NVIDIA/TensorRT-LLM/pull/16197)
  [None][fix] Fix indexer-k-cache transfer for disagg (#16197)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_
- **2026-07-10** [`b4e7808929`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4e7808929) [#15424](https://github.com/NVIDIA/TensorRT-LLM/pull/15424)
  [TRTLLM-13035][feat] Native /v1/embeddings dynamic batching for encoder-only models (#15424)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/features/embeddings.md`, `docs/source/index.rst`, `docs/source/models/supported-models.md` _+16 more__
- **2026-07-10** [`82159e4e3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/82159e4e3d) [#16050](https://github.com/NVIDIA/TensorRT-LLM/pull/16050)
  [TRTLLM-14040][fix] VisualGen shared-tensor handle: same-process (external-launch) handoff (#16050)
  _Files: `tensorrt_llm/_torch/shared_tensor/shared_tensor.py`, `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/_torch/visual_gen/output.py`, `tests/unittest/visual_gen/test_executor_shared_tensor_ipc.py`_
- **2026-07-10** [`d2d99a07b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2d99a07b1) [#16035](https://github.com/NVIDIA/TensorRT-LLM/pull/16035)
  [https://nvbugs/6208457][fix] Harden spawn proxy HMAC key env variable handling (#16035)
  _Files: `tensorrt_llm/executor/utils.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/unittest/executor/test_launcher_envs.py`_
- **2026-07-10** [`b5a085a1af`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5a085a1af) [#15816](https://github.com/NVIDIA/TensorRT-LLM/pull/15816)
  [TRTLLM-13409][feat] proxy fast-death detection + sticky EngineDeadError (#15816)
  _Files: `tensorrt_llm/executor/__init__.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/result.py`, `tensorrt_llm/executor/utils.py` _+3 more__
- **2026-07-10** [`6929451859`](https://github.com/NVIDIA/TensorRT-LLM/commit/6929451859) [#15892](https://github.com/NVIDIA/TensorRT-LLM/pull/15892)
  [https://nvbugs/6384633][fix] Fix NCCL Shutdown (#15892)
  _Files: `cpp/include/tensorrt_llm/runtime/utils/pgUtils.h`, `cpp/tensorrt_llm/nanobind/process_group/bindings.cpp`, `cpp/tensorrt_llm/runtime/utils/pgUtils.cpp`, `tensorrt_llm/_torch/visual_gen/mapping.py` _+1 more__
- **2026-07-09** [`d72425e78d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d72425e78d) [#16000](https://github.com/NVIDIA/TensorRT-LLM/pull/16000)
  [https://nvbugs/6418090][fix] Add @torch.inference_mode() decorator to… (#16000)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-09** [`8e7b98c09b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e7b98c09b) [#15991](https://github.com/NVIDIA/TensorRT-LLM/pull/15991)
  [https://nvbugs/6418103][fix] Clamp the post-allreduce quota by the pre-allreduce quota (`quota = min(quota… (#15991)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-09** [`9a8ec0567c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a8ec0567c) [#16163](https://github.com/NVIDIA/TensorRT-LLM/pull/16163)
  [TRTLLM-14155][fix] Revert host-side greedy stop checks from #15920 (#16163)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-07-09** [`7412d0bb97`](https://github.com/NVIDIA/TensorRT-LLM/commit/7412d0bb97) [#14636](https://github.com/NVIDIA/TensorRT-LLM/pull/14636)
  [DEP-950][feat] add multi-rank sleep/wakeup support to MPI executor path (#14636)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py` _+4 more__
- **2026-07-09** [`92e3075299`](https://github.com/NVIDIA/TensorRT-LLM/commit/92e3075299) [#16013](https://github.com/NVIDIA/TensorRT-LLM/pull/16013)
  [None][infra] Automate and gate LLM args telemetry manifest updates (#16013)
  _Files: `.github/CODEOWNERS`, `.github/workflows/llm-api-compatibility.yml`, `AGENTS.md`, `CODING_GUIDELINES.md` _+8 more__
- **2026-07-08** [`62b3cc7bbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/62b3cc7bbb) [#15863](https://github.com/NVIDIA/TensorRT-LLM/pull/15863)
  [None][feat] Add low-latency host task dispatch mode for guided decoding (#15863)
  _Files: `cpp/tensorrt_llm/nanobind/runtime/hostfunc.cpp`, `tensorrt_llm/_torch/hostfunc.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/llmapi/llm_args.py` _+4 more__
- **2026-07-08** [`bbe5c5b131`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbe5c5b131) [#16010](https://github.com/NVIDIA/TensorRT-LLM/pull/16010)
  [None][fix] Fix logits post processor for beam search in PyTorch backend (#16010)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`b50a10983c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b50a10983c) [#15520](https://github.com/NVIDIA/TensorRT-LLM/pull/15520)
  [None][doc] Clarify dtype='auto' resolution for LLM and KvCacheConfig (#15520)
  _Files: `tensorrt_llm/llmapi/llm_args.py`_
- **2026-07-07** [`7a56db9886`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a56db9886) [#15249](https://github.com/NVIDIA/TensorRT-LLM/pull/15249)
  [TRTLLM-13383][feat] Add support for Qwen3.5 VL Dense (#15249)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+7 more__
- **2026-07-07** [`9208094543`](https://github.com/NVIDIA/TensorRT-LLM/commit/9208094543) [#15987](https://github.com/NVIDIA/TensorRT-LLM/pull/15987)
  [https://nvbugs/6337235][test] Remove stale MX/GMS model loader skips (#15987)
  _Files: `tests/unittest/_torch/executor/test_model_loader_gms.py`, `tests/unittest/_torch/models/checkpoints/mx/test_mx_checkpoint_loader.py`_
- **2026-07-07** [`187c4c9368`](https://github.com/NVIDIA/TensorRT-LLM/commit/187c4c9368) [#15640](https://github.com/NVIDIA/TensorRT-LLM/pull/15640)
  [TRTLLM-13352][chore] BREAKING: move multimodal related args / env vars (#15640)
  _Files: `examples/llm-api/quickstart_multimodal.py`, `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/multimodal_encoder_graph.py` _+13 more__
- **2026-07-07** [`265e5ea09d`](https://github.com/NVIDIA/TensorRT-LLM/commit/265e5ea09d) [#15387](https://github.com/NVIDIA/TensorRT-LLM/pull/15387)
  [TRTLLM-13249][feat] Wave 4: add MX staged receiver cutover (#15387)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_checkpoint_loader.py`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/unittest/_torch/executor/test_model_loader_mx.py` _+1 more__
- **2026-07-07** [`4f1c3cdcdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f1c3cdcdf) [#15920](https://github.com/NVIDIA/TensorRT-LLM/pull/15920)
  [None][perf] Move greedy stop checks to host (#15920)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-07-06** [`0d97e9c76f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d97e9c76f) [#15654](https://github.com/NVIDIA/TensorRT-LLM/pull/15654)
  [https://nvbugs/6388787][fix] Revert Pass IPC HMAC key through file descriptor (#15654) (#15961)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/ipc.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/executor/worker.py` _+4 more__
- **2026-07-06** [`605dd00734`](https://github.com/NVIDIA/TensorRT-LLM/commit/605dd00734) [#15099](https://github.com/NVIDIA/TensorRT-LLM/pull/15099)
  [https://nvbugs/6248837][fix] Free worker GPU memory on executor shutdown (#15099)
  _Files: `tensorrt_llm/executor/worker.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`ad9866882d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad9866882d) [#15882](https://github.com/NVIDIA/TensorRT-LLM/pull/15882)
  [https://nvbugs/6396420][fix] Restore single-node NVLS over POSIX-FD (#15882)
  _Files: `cpp/include/tensorrt_llm/runtime/ipcNvlsMemory.h`, `cpp/tensorrt_llm/common/opUtils.cpp`, `cpp/tensorrt_llm/runtime/ipcNvlsMemory.cu`, `cpp/tensorrt_llm/runtime/ncclCommunicator.cpp` _+3 more__
- **2026-07-06** [`96b73ddb8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/96b73ddb8e) [#15927](https://github.com/NVIDIA/TensorRT-LLM/pull/15927)
  [https://nvbugs/6337231][fix] Unskip and fix iter-stats unit tests' fake-self predicate (#15927)
  _Files: `tests/unittest/_torch/executor/test_iter_stats_populate.py`_
- **2026-07-06** [`6c22551583`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c22551583) [#15732](https://github.com/NVIDIA/TensorRT-LLM/pull/15732)
  [https://nvbugs/6384951][fix] Fix incorrect error reporting (#15732)
  _Files: `tensorrt_llm/serve/chat_utils.py`, `tests/unittest/llmapi/apps/test_chat_utils.py`_
- **2026-07-06** [`b48661b190`](https://github.com/NVIDIA/TensorRT-LLM/commit/b48661b190) [#15655](https://github.com/NVIDIA/TensorRT-LLM/pull/15655)
  [https://nvbugs/6344107][fix] Enable disagg partial reuse store for PP>1 (#15655)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_

## Attention  (27 commits)

- **2026-07-13** [`e4a8dda776`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4a8dda776) [#16221](https://github.com/NVIDIA/TensorRT-LLM/pull/16221)
  [None][fix] Fix fused mHC output reuse and extend compressor next_n (#16221)
  _Files: `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcFusedHcKernel.cu`, `cpp/tensorrt_llm/thop/compressorOp.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py` _+4 more__
- **2026-07-13** [`4a86ff538d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a86ff538d) [#16073](https://github.com/NVIDIA/TensorRT-LLM/pull/16073)
  [TRTLLM-14138][perf] Make FlashInfer decode plans sync-free with host-built page tables (#16073)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_
- **2026-07-13** [`c47715a2b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c47715a2b2) [#16236](https://github.com/NVIDIA/TensorRT-LLM/pull/16236)
  [None][fix] source DSA metadata from sparse params (#16236)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-07-13** [`9fe5d0f735`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fe5d0f735) [#16167](https://github.com/NVIDIA/TensorRT-LLM/pull/16167)
  [https://nvbugs/6430674][fix] Surgical revert of PR #15838's dispatch guard removal: re-add… (#16167)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-07-13** [`5a5cba0743`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a5cba0743) [#16225](https://github.com/NVIDIA/TensorRT-LLM/pull/16225)
  [None][fix] Correct RocketKV KT cache byte accounting for FP8 KV cache (#16225)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/rocket.py`, `tests/unittest/_torch/attention/sparse/rocketkv/test_rocketkv.py`_
- **2026-07-12** [`1c9a90282d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c9a90282d) [#16160](https://github.com/NVIDIA/TensorRT-LLM/pull/16160)
  [TRTLLM-14198][refactor] Make FlashInfer a hard dependency for the Torch sampler (#16160)
  _Files: `docs/source/developer-guide/telemetry.md`, `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+13 more__
- **2026-07-11** [`cf82c5d902`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf82c5d902) [#16074](https://github.com/NVIDIA/TensorRT-LLM/pull/16074)
  [TRTLLM-14138][perf] Add fused kernels for Gemma4 serving (#16074)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/modules/fused_ops/__init__.py`, `tensorrt_llm/_torch/modules/fused_ops/gelu_tanh_mul_fp4_quant.py` _+9 more__
- **2026-07-10** [`40829782f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/40829782f1) [#16173](https://github.com/NVIDIA/TensorRT-LLM/pull/16173)
  [https://nvbugs/6411873][fix] DSV4: size KV constraint with num_extra_kv_tokens (#16173)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`_
- **2026-07-10** [`459e3c673a`](https://github.com/NVIDIA/TensorRT-LLM/commit/459e3c673a) [#16179](https://github.com/NVIDIA/TensorRT-LLM/pull/16179)
  [None][test] Fix MLA import path in attention perf harness (#16179)
  _Files: `tests/microbenchmarks/attention_perf/attention_perf_harness.py`_
- **2026-07-10** [`6b9f6dce22`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b9f6dce22) [#16104](https://github.com/NVIDIA/TensorRT-LLM/pull/16104)
  [None][chore] Centralize trtllm-gen FMHA unsupported diagnostics (#16104)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-07-09** [`6e3c3bf7c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e3c3bf7c5) [#15974](https://github.com/NVIDIA/TensorRT-LLM/pull/15974)
  [https://nvbugs/6390307][fix] Update trtllm-gen FMHA JIT libraries (#15974)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/aarch64-linux-gnu/libTrtLlmGen.a`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/aarch64-linux-gnu/libTrtLlmGenFmhaLib.a`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/x86_64-linux-gnu/libTrtLlmGen.a`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/x86_64-linux-gnu/libTrtLlmGenFmhaLib.a` _+4 more__
- **2026-07-09** [`7d600ecc1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d600ecc1d) [#15710](https://github.com/NVIDIA/TensorRT-LLM/pull/15710)
  [None][test] DSv4 PR-6 coverage and import safety (#15710)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/triton_prefill.py`, `tensorrt_llm/_torch/cuda_tile_utils.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py` _+7 more__
- **2026-07-09** [`4899f00f32`](https://github.com/NVIDIA/TensorRT-LLM/commit/4899f00f32) [#16028](https://github.com/NVIDIA/TensorRT-LLM/pull/16028)
  [None][perf] Port remaining DeepSeek V4 optimizations to main (#16028)
  _Files: `cpp/tensorrt_llm/kernels/deepseekV4BlockTable.cu`, `cpp/tensorrt_llm/kernels/deepseekV4BlockTable.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/deepseekV4BlockTableOp.cpp` _+9 more__
- **2026-07-09** [`201b0776b3`](https://github.com/NVIDIA/TensorRT-LLM/commit/201b0776b3) [#15661](https://github.com/NVIDIA/TensorRT-LLM/pull/15661)
  [https://nvbugs/6316983][fix] Fix RoPE support in flashinfer trtllm-gen backend (#15661)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/trtllmGenFusedOps.h`, `cpp/tensorrt_llm/thop/trtllmGenQKVProcessOp.cpp`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py` _+1 more__
- **2026-07-09** [`4a48e5a06e`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a48e5a06e) [#15676](https://github.com/NVIDIA/TensorRT-LLM/pull/15676)
  [None][fix] visual_gen FLUX: enable fused DiT QK-norm + RoPE by default (#15676)
  _Files: `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`, `tests/unittest/_torch/visual_gen/test_flux_attention.py`_
- **2026-07-08** [`5ce293fc77`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ce293fc77) [#15897](https://github.com/NVIDIA/TensorRT-LLM/pull/15897)
  [TRTLLM-13175][feat] Support Tensor Parallelism PyTorch encoder-decoder models (#15897)
  _Files: `tensorrt_llm/_torch/models/modeling_bart.py`, `tensorrt_llm/_torch/models/modeling_t5.py`, `tensorrt_llm/_torch/modules/cross_attention.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+5 more__
- **2026-07-08** [`50423007d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/50423007d2) [#16117](https://github.com/NVIDIA/TensorRT-LLM/pull/16117)
  [None][infra] Remove attention op sync test waivers (#16117)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`06df8dafbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/06df8dafbd) [#15542](https://github.com/NVIDIA/TensorRT-LLM/pull/15542)
  [TRTLLM-13212][refactor] Centralize sampling logic, split backends into isolated modules (#15542)
  _Files: `.pre-commit-config.yaml`, `pyproject.toml`, `tensorrt_llm/_torch/auto_deploy/shim/demollm.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py` _+17 more__
- **2026-07-08** [`4860595da3`](https://github.com/NVIDIA/TensorRT-LLM/commit/4860595da3) [#15838](https://github.com/NVIDIA/TensorRT-LLM/pull/15838)
  [None][fix] Unwaive supported attention backend cases (#15838)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+3 more__
- **2026-07-07** [`f2db72397a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f2db72397a) [#16085](https://github.com/NVIDIA/TensorRT-LLM/pull/16085)
  Revert "[https://nvbugs/6403909][fix] unwaive an attention backend test" (#16085)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`d0d5069836`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0d5069836) [#15964](https://github.com/NVIDIA/TensorRT-LLM/pull/15964)
  [https://nvbugs/6403909][fix] unwaive an attention backend test (#15964)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`409b696f0b`](https://github.com/NVIDIA/TensorRT-LLM/commit/409b696f0b) [#14280](https://github.com/NVIDIA/TensorRT-LLM/pull/14280)
  [TRTLLM-12347][feat] enable VSA in VisualGen (#14280)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/__init__.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/fmha.py` _+26 more__
- **2026-07-07** [`9fc59fb0e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fc59fb0e1) [#15417](https://github.com/NVIDIA/TensorRT-LLM/pull/15417)
  [None][refactor] Refine Skip Softmax follow-ups (#15417)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/sparse/params.py` _+19 more__
- **2026-07-07** [`790ea151a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/790ea151a3) [#15956](https://github.com/NVIDIA/TensorRT-LLM/pull/15956)
  [https://nvbugs/6336801][fix] Fix attention op sync test (#15956)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tests/unittest/_torch/attention/test_attention_op_sync.py`_
- **2026-07-07** [`211482b36a`](https://github.com/NVIDIA/TensorRT-LLM/commit/211482b36a) [#15923](https://github.com/NVIDIA/TensorRT-LLM/pull/15923)
  [TRTLLM-13968][fix] Enable MiniMax M3 piecewise CUDA graphs (#15923)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/backend.py`, `tensorrt_llm/_torch/compilation/backend.py`, `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/compilation/utils.py` _+5 more__
- **2026-07-06** [`c5bdcaa49a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5bdcaa49a) [#15848](https://github.com/NVIDIA/TensorRT-LLM/pull/15848)
  [None][perf] Improve inference correctness and perf for Gemma4 (#15848)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py` _+7 more__
- **2026-07-06** [`c45f75fcca`](https://github.com/NVIDIA/TensorRT-LLM/commit/c45f75fcca) [#15869](https://github.com/NVIDIA/TensorRT-LLM/pull/15869)
  [None][chore] Update flashinfer-python from 0.6.12 to 0.6.14 (#15869)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_

## MoE  (22 commits)

- **2026-07-13** [`44c3adf9e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/44c3adf9e6) [#16293](https://github.com/NVIDIA/TensorRT-LLM/pull/16293)
  [https://nvbugs/6428113][fix] Fix TEP token-count handling in MoE Test (#16293)
  _Files: `tests/unittest/_torch/modules/test_moe_routing.py`_
- **2026-07-11** [`33a4545010`](https://github.com/NVIDIA/TensorRT-LLM/commit/33a4545010) [#15900](https://github.com/NVIDIA/TensorRT-LLM/pull/15900)
  [TRTLLM-13776][feat] Add Piecewise CUDA Graph support for Qwen3.5/Qwen3.6 MoE model (#15900)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-11** [`8bcec87697`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bcec87697)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+19 more__
- **2026-07-10** [`2cbdaa0ffa`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cbdaa0ffa) [#16125](https://github.com/NVIDIA/TensorRT-LLM/pull/16125)
  [https://nvbugs/6384375][fix] Cap MXFP4 Hopper swizzle transient GPU memory during MoE weight load (#16125)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`, `tests/unittest/_torch/modules/fused_moe/test_triton_mxfp4_swizzle.py`_
- **2026-07-10** [`fd9166c0a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd9166c0a7) [#16108](https://github.com/NVIDIA/TensorRT-LLM/pull/16108)
  [None][fix] Fix Gemma4 MoE weight loading (#16108)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/gemma4_weight_mapper.py`, `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+1 more__
- **2026-07-10** [`80439345bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/80439345bb) [#16113](https://github.com/NVIDIA/TensorRT-LLM/pull/16113)
  [None][test] bench_moe: add nsys capture-range support (--nsys) (#16113)
  _Files: `tests/microbenchmarks/bench_moe/case_runner.py`, `tests/microbenchmarks/bench_moe/cli.py`, `tests/microbenchmarks/bench_moe/reporting.py`, `tests/microbenchmarks/bench_moe/results.py` _+5 more__
- **2026-07-09** [`216de779c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/216de779c3)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+21 more__
- **2026-07-08** [`1fd24e18ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/1fd24e18ad) [#15432](https://github.com/NVIDIA/TensorRT-LLM/pull/15432)
  [TRTLLM-13250][feat] Wave 5: Enable MX post-transform Llama receiver (#15432)
  _Files: `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/unittest/_torch/executor/test_model_loader_gms.py`, `tests/unittest/_torch/executor/test_model_loader_mx.py` _+3 more__
- **2026-07-08** [`c92ac90ffc`](https://github.com/NVIDIA/TensorRT-LLM/commit/c92ac90ffc) [#16118](https://github.com/NVIDIA/TensorRT-LLM/pull/16118)
  [None][ci] relocate test_qwen_moe_routed_expert_multi_lora_varying_ranks (#16118)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-07-08** [`d163e74407`](https://github.com/NVIDIA/TensorRT-LLM/commit/d163e74407) [#16065](https://github.com/NVIDIA/TensorRT-LLM/pull/16065)
  [https://nvbugs/6422332][fix] Keep SSM cache in weights dtype when ma… (#16065)
  _Files: `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl_moe.py`, `tests/unittest/_torch/modeling/test_qwen_image_bench_modeling.py`_
- **2026-07-08** [`fd271e06f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd271e06f6) [#15899](https://github.com/NVIDIA/TensorRT-LLM/pull/15899)
  [None][test] Modularized attention perf round 2: per-case isolation, device-name keying, GQA/MLA/DSA cases (#15899)
  _Files: `tests/integration/defs/perf/test_utils.py`, `tests/integration/defs/perf/utils.py`, `tests/microbenchmarks/attention_perf/attention_perf_harness.py`, `tests/microbenchmarks/attention_perf/golden_attention.json` _+4 more__
- **2026-07-08** [`bc6248991c`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc6248991c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+22 more__
- **2026-07-07** [`c09fbbdd82`](https://github.com/NVIDIA/TensorRT-LLM/commit/c09fbbdd82) [#15975](https://github.com/NVIDIA/TensorRT-LLM/pull/15975)
  [None][feat] Dispatch GDN MTP target-verify to FlashInfer bf16 kernel (#15975)
  _Files: `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_gdn_verify.py`_
- **2026-07-07** [`4b2760879a`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b2760879a)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+20 more__
- **2026-07-07** [`ef6e513678`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef6e513678) [#15397](https://github.com/NVIDIA/TensorRT-LLM/pull/15397)
  [None][fix] fix bench-moe benchmark bugs (#15397)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`, `tests/microbenchmarks/bench_moe/case_runner.py`, `tests/microbenchmarks/bench_moe/cli.py` _+10 more__
- **2026-07-06** [`a0c406ff88`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0c406ff88) [#15524](https://github.com/NVIDIA/TensorRT-LLM/pull/15524)
  [TRTLLM-12557][feat] WideEP FT: add AlltoAll watchdog (1a.3 + 1a.4) (#15524)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h`, `tensorrt_llm/_torch/alltoall_watchdog.py`, `tensorrt_llm/_torch/distributed/moe_alltoall.py` _+8 more__
- **2026-07-06** [`9f689ec7ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f689ec7ae) [#15386](https://github.com/NVIDIA/TensorRT-LLM/pull/15386)
  [TRTLLM-13248][feat] Wave 3: migrate MoE staged hooks (#15386)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/models/modeling_llama_min_latency.py`, `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl_b12x.py` _+14 more__
- **2026-07-06** [`02715db02f`](https://github.com/NVIDIA/TensorRT-LLM/commit/02715db02f) [#15594](https://github.com/NVIDIA/TensorRT-LLM/pull/15594)
  [https://nvbugs/6299530][fix] Capture Qwen3.5 GDN for piecewise CUDA … (#15594)
  _Files: `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/modules/fla/chunk.py`, `tensorrt_llm/_torch/modules/fla/chunk_o.py` _+8 more__
- **2026-07-06** [`0bfc38926c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bfc38926c) [#15451](https://github.com/NVIDIA/TensorRT-LLM/pull/15451)
  [TRTLLM-13334][fix] Add EP assertion to DenseGEMMFusedMoE (#15451)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_densegemm.py`_
- **2026-07-06** [`f5a1f54ec1`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5a1f54ec1) [#15662](https://github.com/NVIDIA/TensorRT-LLM/pull/15662)
  [TRTLLM-13628][test] Optimize MoE comm test execution (#15662)
  _Files: `tests/unittest/_torch/modules/moe/test_moe_comm.py`_
- **2026-07-06** [`496acab85c`](https://github.com/NVIDIA/TensorRT-LLM/commit/496acab85c) [#15717](https://github.com/NVIDIA/TensorRT-LLM/pull/15717)
  [None][perf] DSv4 follow-up: sparse attention and model defaults (#15717)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu` _+40 more__
- **2026-07-06** [`45fae3eb9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/45fae3eb9f) [#14810](https://github.com/NVIDIA/TensorRT-LLM/pull/14810)
  [#14588][feat] AutoDeploy: DeepSeek-R1 optimization for low concurrency (#14810)
  _Files: `examples/auto_deploy/model_registry/configs/deepseek-r1.yaml`, `examples/auto_deploy/model_registry/configs/gemma3n_e2b_it.yaml`, `examples/auto_deploy/model_registry/models.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/__init__.py` _+20 more__

## Other  (15 commits)

- **2026-07-13** [`11a880f4fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/11a880f4fb) [#16298](https://github.com/NVIDIA/TensorRT-LLM/pull/16298)
  [None][test] Restrict gen-worker per-iter mean to steady-state iterations (#16298)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-07-13** [`3bff181f8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bff181f8a) [#16172](https://github.com/NVIDIA/TensorRT-LLM/pull/16172)
  [https://nvbugs/6323074][fix] fix flaky hang issue for disagg gen-onl… (#16172)
- **2026-07-11** [`f956e6e427`](https://github.com/NVIDIA/TensorRT-LLM/commit/f956e6e427) [#16049](https://github.com/NVIDIA/TensorRT-LLM/pull/16049)
  [None][fix] trtllm-serve VisualGen: bind HTTP port only on rank 0 in multi-rank launch (#16049)
  _Files: `tensorrt_llm/commands/serve.py`_
- **2026-07-10** [`edf8f6f6f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/edf8f6f6f3) [#16091](https://github.com/NVIDIA/TensorRT-LLM/pull/16091)
  [None][refactor] BREAKING: rename server args (#16091)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/unittest/api_stability/references/trtllm_serve_cli.yaml`_
- **2026-07-09** [`046c7874f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/046c7874f9) [#16187](https://github.com/NVIDIA/TensorRT-LLM/pull/16187)
  [None][test] Remove llm_function_l20.txt test list (#16187)
  _Files: `tests/integration/test_lists/qa/llm_function_l20.txt`_
- **2026-07-09** [`00f4687a60`](https://github.com/NVIDIA/TensorRT-LLM/commit/00f4687a60) [#16183](https://github.com/NVIDIA/TensorRT-LLM/pull/16183)
  [None][test] Remove H200 and RTX6000-D for QA perf Test (#16183)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-07-09** [`940050b77a`](https://github.com/NVIDIA/TensorRT-LLM/commit/940050b77a) [#15907](https://github.com/NVIDIA/TensorRT-LLM/pull/15907)
  [TRTLLM-13784][chore] Remove legacy TensorRT-engine Triton backend (#15907)
- **2026-07-09** [`42d047e8f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/42d047e8f0) [#15978](https://github.com/NVIDIA/TensorRT-LLM/pull/15978)
  [None][docs] Default GitHub CLI config directory non-interactively (#15978)
  _Files: `AGENTS.md`_
- **2026-07-07** [`65f16126ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/65f16126ad) [#16015](https://github.com/NVIDIA/TensorRT-LLM/pull/16015)
  [None][build] Add --yes flag to build_wheel.py to skip interactive prompt (#16015)
  _Files: `scripts/build_wheel.py`_
- **2026-07-07** [`c9228d8728`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9228d8728) [#16020](https://github.com/NVIDIA/TensorRT-LLM/pull/16020)
  [None][build] Use cp -rL and skip up-to-date copies in copy_resolving_symlink (#16020)
  _Files: `scripts/build_wheel.py`_
- **2026-07-06** [`7faf4a42a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7faf4a42a8) [#15958](https://github.com/NVIDIA/TensorRT-LLM/pull/15958)
  [https://nvbugs/6337229][fix] Stabilize scaffolding MCP worker test server startup and cleanup (#15958)
  _Files: `tests/unittest/scaffolding/test_bench.py`, `tests/unittest/scaffolding/test_mcp_worker.py`, `tests/unittest/scaffolding/test_worker.py`_
- **2026-07-06** [`4c6e794e22`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c6e794e22) [#15810](https://github.com/NVIDIA/TensorRT-LLM/pull/15810)
  [TRTLLM-13783][test] Remove TensorRT-backend tests (#15810)
- **2026-07-06** [`2c6116012e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c6116012e) [#15925](https://github.com/NVIDIA/TensorRT-LLM/pull/15925)
  [https://nvbugs/6341070][fix] Fix scaffolding MajorityVoteController output handling (#15925)
  _Files: `tensorrt_llm/scaffolding/controller.py`, `tests/unittest/scaffolding/test_scaffolding.py`, `tests/unittest/scaffolding/test_worker.py`_
- **2026-07-06** [`7340eac7f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/7340eac7f7) [#15954](https://github.com/NVIDIA/TensorRT-LLM/pull/15954)
  [None][fix] Ignore valid Faroese code in codespell (#15954)
  _Files: `triton_backend/all_models/whisper/whisper_bls/1/tokenizer.py`_
- **2026-07-06** [`1519f7f341`](https://github.com/NVIDIA/TensorRT-LLM/commit/1519f7f341) [#15781](https://github.com/NVIDIA/TensorRT-LLM/pull/15781)
  [https://nvbugs/6385256][fix] Guard at both layers — add len>0 checks in get_request_num_tokens, return []… (#15781)
  _Files: `tensorrt_llm/serve/openai_disagg_service.py`, `tensorrt_llm/serve/router.py`_

## Disaggregation / KV  (13 commits)

- **2026-07-13** [`5088a4dbde`](https://github.com/NVIDIA/TensorRT-LLM/commit/5088a4dbde) [#15533](https://github.com/NVIDIA/TensorRT-LLM/pull/15533)
  [None][chore] Clean deprecated CppMambaCacheManager (#15533)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/rnnCacheFormatter.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransferLayer.cpp` _+19 more__
- **2026-07-13** [`c883622b6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c883622b6b) [#15823](https://github.com/NVIDIA/TensorRT-LLM/pull/15823)
  [None][feat] add per-model KV cache manager v2 auto selection (#15823)
  _Files: `examples/llm-api/quickstart_advanced.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/llmapi/llm_args.py` _+4 more__
- **2026-07-10** [`b49798f919`](https://github.com/NVIDIA/TensorRT-LLM/commit/b49798f919) [#15737](https://github.com/NVIDIA/TensorRT-LLM/pull/15737)
  [https://nvbugs/6342844][fix] Prevent disaggregated KV transfer stalls (#15737)
  _Files: `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/cacheTransceiver.cpp`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+7 more__
- **2026-07-10** [`e2ce7a69bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2ce7a69bd) [#16114](https://github.com/NVIDIA/TensorRT-LLM/pull/16114)
  [None][test] KV cache manager v2: add V2 + VSWA multi-GPU test coverage (#16114)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/qa/llm_function_rtx6k.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-07-09** [`d18a826af2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d18a826af2) [#16040](https://github.com/NVIDIA/TensorRT-LLM/pull/16040)
  [None][chore] Enable acc for disagg multi node stress test on qa side (#16040)
  _Files: `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_1k1k_ctx2_gen1_dep16_bs128_eplb288_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_8k1k_ctx2_gen1_dep32_bs128_eplb288_mtp3_ccb-NIXL.yaml`_
- **2026-07-08** [`4be213c9c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4be213c9c9) [#16081](https://github.com/NVIDIA/TensorRT-LLM/pull/16081)
  [https://nvbugs/6336747][ci] Waive intermittently hanging E2E tests (#16081)
  _Files: `tests/integration/defs/accuracy/test_epd_disagg_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-07** [`0e3dec01cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e3dec01cf) [#15385](https://github.com/NVIDIA/TensorRT-LLM/pull/15385)
  [None][fix] expose startup KV cache capacity (#15385)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/proxy.py` _+6 more__
- **2026-07-07** [`4b9378523e`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b9378523e) [#15893](https://github.com/NVIDIA/TensorRT-LLM/pull/15893)
  [None][fix] Make cache transceiver transport reporting deterministic (#15893)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/report.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/disaggregated/test_cache_transceiver_harness.py`, `tests/unittest/disaggregated/test_cache_transceiver_harness_report.py`_
- **2026-07-07** [`26d95f2ef7`](https://github.com/NVIDIA/TensorRT-LLM/commit/26d95f2ef7) [#16043](https://github.com/NVIDIA/TensorRT-LLM/pull/16043)
  [https://nvbugs/6303211][fix] set 2 multi_round to save time (#16043)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-07-07** [`3bf37d2538`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bf37d2538) [#15618](https://github.com/NVIDIA/TensorRT-LLM/pull/15618)
  [None][feat] Disaggregated KV-cache bounce transfer (#15618)
  _Files: `tensorrt_llm/_torch/disaggregation/native/bounce/__init__.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/buffer.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/config.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/core.py` _+14 more__
- **2026-07-07** [`9b593ddb1b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9b593ddb1b) [#15755](https://github.com/NVIDIA/TensorRT-LLM/pull/15755)
  [None][feat] add gemma and glm disagg python transceiver test (#15755)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml` _+1 more__
- **2026-07-06** [`ceae332fe6`](https://github.com/NVIDIA/TensorRT-LLM/commit/ceae332fe6) [#15879](https://github.com/NVIDIA/TensorRT-LLM/pull/15879)
  [https://nvbugs/6384622][fix] increase free_mem_frac for failed perf test (#15879)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-07-06** [`0071389094`](https://github.com/NVIDIA/TensorRT-LLM/commit/0071389094) [#15917](https://github.com/NVIDIA/TensorRT-LLM/pull/15917)
  [https://nvbugs/6405665][test] Disable block reuse for KV cache comparison (#15917)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`, `tests/integration/test_lists/waives.txt`_

## Quantization  (12 commits)

- **2026-07-13** [`9a2f5389e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a2f5389e7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+21 more__
- **2026-07-12** [`374cc09c2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/374cc09c2f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/pyproject.toml` _+8 more__
- **2026-07-10** [`c0c12264be`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0c12264be) [#14668](https://github.com/NVIDIA/TensorRT-LLM/pull/14668)
  [https://nvbugs/5970614][fix] Sync CTA before PDL trigger in quantize_with_block_size (#14668)
  _Files: `cpp/tensorrt_llm/kernels/quantization.cuh`, `tests/integration/test_lists/waives.txt`_
- **2026-07-10** [`7b49ba8159`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b49ba8159)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+18 more__
- **2026-07-09** [`1bb55a3e0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/1bb55a3e0c) [#16031](https://github.com/NVIDIA/TensorRT-LLM/pull/16031)
  [TRTLLM-13977][fix] Fix NT3 NVFP4 perf regression in Blackwell (#16031)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`_
- **2026-07-09** [`0336474810`](https://github.com/NVIDIA/TensorRT-LLM/commit/0336474810) [#15703](https://github.com/NVIDIA/TensorRT-LLM/pull/15703)
  [TRTLLM-13709][feat] Add the Qwen3.6 nvfp4 checkpoint support (#15703)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/models/modeling_qwen3_next.py` _+7 more__
- **2026-07-08** [`54cffcd2fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/54cffcd2fb) [#16110](https://github.com/NVIDIA/TensorRT-LLM/pull/16110)
  [https://nvbugs/6388359][test] Unwaive Qwen3-30B-A3B test_w4a8_mxfp4 mxfp8-latency-CUTLASS (#16110)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-08** [`3892f2048a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3892f2048a) [#14947](https://github.com/NVIDIA/TensorRT-LLM/pull/14947)
  [None][opt] Dsv4-Pro attn kernel epilogue fuse RopeQuant (#14947) (#16036)
- **2026-07-07** [`045705139d`](https://github.com/NVIDIA/TensorRT-LLM/commit/045705139d) [#16008](https://github.com/NVIDIA/TensorRT-LLM/pull/16008)
  [TRTLLM-12154][test] Add mixed-stress disagg client and pytest variants for Qwen3-32B FP8 (#16008)
  _Files: `tests/integration/defs/disaggregated/disagg_test_utils.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_stress.txt`, `tests/integration/test_lists/test-db/l0_dgx_h200.yml`_
- **2026-07-07** [`33526e6ca2`](https://github.com/NVIDIA/TensorRT-LLM/commit/33526e6ca2) [#15951](https://github.com/NVIDIA/TensorRT-LLM/pull/15951)
  [None][test] keep MXFP4 block-scale unswizzle on GPU in create_weights (#15951)
- **2026-07-06** [`398e3e75ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/398e3e75ef) [#15970](https://github.com/NVIDIA/TensorRT-LLM/pull/15970)
  [None][test] Increase timeout for Kimi-K2.5 disaggregated nvfp4 test (#15970)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-07-06** [`b52f6073df`](https://github.com/NVIDIA/TensorRT-LLM/commit/b52f6073df) [#15660](https://github.com/NVIDIA/TensorRT-LLM/pull/15660)
  [None][fix] Fix marlin_nvfp4_template.h compilation error (#15660)
  _Files: `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4_template.h`_

## Torch Path (_torch)  (8 commits)

- **2026-07-13** [`e9b8e91dba`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9b8e91dba) [#16054](https://github.com/NVIDIA/TensorRT-LLM/pull/16054)
  [None][feat] Add an opt-in raw-weight cache to the HF weight loader (#16054)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tests/unittest/_torch/models/checkpoints/hf/test_weight_loader.py`_
- **2026-07-09** [`b07c109b80`](https://github.com/NVIDIA/TensorRT-LLM/commit/b07c109b80) [#16122](https://github.com/NVIDIA/TensorRT-LLM/pull/16122)
  [None][test] Reduce Nemotron V3 Super/Ultra pre-merge test cases (#16122)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+2 more__
- **2026-07-08** [`e7b22561ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7b22561ae) [#15839](https://github.com/NVIDIA/TensorRT-LLM/pull/15839)
  [https://nvbugs/6396728][fix] Add module-level `pytestmark = pytest.mark.threadleak(enabled=False)` to… (#15839)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`_
- **2026-07-07** [`94b281b0f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/94b281b0f7) [#15621](https://github.com/NVIDIA/TensorRT-LLM/pull/15621)
  [https://nvbugs/6242591][fix] Fix bugs in Beam Search kernels (#15621)
  _Files: `cpp/tensorrt_llm/kernels/beamSearchKernels.cu`, `cpp/tensorrt_llm/kernels/beamSearchKernels.h`, `cpp/tensorrt_llm/kernels/beamSearchKernels/beamSearchKernelsTemplate.h`, `cpp/tensorrt_llm/kernels/decodingKernels.cu` _+1 more__
- **2026-07-07** [`4d1cb8f792`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d1cb8f792) [#15866](https://github.com/NVIDIA/TensorRT-LLM/pull/15866)
  [https://nvbugs/6321874][fix] Filter `.lock` from `os.listdir(...)` in the test's rank-file count; skip the… (#15866)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-07-07** [`bd7daecfea`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd7daecfea) [#15753](https://github.com/NVIDIA/TensorRT-LLM/pull/15753)
  [TRTLLM-14029][feat] LTX-2 tile-parallel VAE decode (#15753)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/utils_ltx2.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/video_vae/tiling.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/video_vae/video_vae.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/parallel_vae.py` _+3 more__
- **2026-07-06** [`7023aeac4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7023aeac4a) [#15555](https://github.com/NVIDIA/TensorRT-LLM/pull/15555)
  [TRTLLM-13584][feat] add Wan VAE backend (#15555)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan_i2v.py`, `tensorrt_llm/_torch/visual_gen/models/wan/vae_loader.py` _+3 more__
- **2026-07-06** [`1ae65a64ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ae65a64ab) [#15937](https://github.com/NVIDIA/TensorRT-LLM/pull/15937)
  [TRTLLM-13973][fix] Restrict MiniMax M3 dense SDPA backends (#15937)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`_

## Speculative Decoding  (7 commits)

- **2026-07-11** [`b0f3f2936a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0f3f2936a) [#16101](https://github.com/NVIDIA/TensorRT-LLM/pull/16101)
  [https://nvbugs/6427240][fix] Reserve MTP draft tokens in scheduler for one-model speculative decoding (#16101)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-07-09** [`562124ddeb`](https://github.com/NVIDIA/TensorRT-LLM/commit/562124ddeb) [#16165](https://github.com/NVIDIA/TensorRT-LLM/pull/16165)
  [None][fix] Remove redundant residual bound check in EAGLE3 hidden-state capture (#16165)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`_
- **2026-07-09** [`051e9edfe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/051e9edfe3) [#16107](https://github.com/NVIDIA/TensorRT-LLM/pull/16107)
  [TRTLLM-14080][test] Add test coverage for Eagle3ForCausalLM.apply_eagle3_fc (#16107)
  _Files: `tests/integration/test_lists/test-db/l0_a30.yml`, `tests/unittest/_torch/modeling/test_modeling_speculative.py`_
- **2026-07-09** [`60583d27f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/60583d27f3) [#15708](https://github.com/NVIDIA/TensorRT-LLM/pull/15708)
  [https://nvbugs/6103083][fix] Make EAGLE functional on v1 KV cache manager (#15708)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tensorrt_llm/_torch/speculative/eagle3.py`, `tests/unittest/_torch/speculative/test_eagle3.py`_
- **2026-07-07** [`ce67288c92`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce67288c92) [#15765](https://github.com/NVIDIA/TensorRT-LLM/pull/15765)
  [None][perf] Validate GPT-OSS transceiver v2 performance (#15765)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_eagle_triton.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_eagle_trtllm.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_tllm.yaml` _+16 more__
- **2026-07-06** [`4c5f3b06d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c5f3b06d2) [#14990](https://github.com/NVIDIA/TensorRT-LLM/pull/14990)
  [None][test] Add gpt-oss-120b eagle3 accuracy test (#14990)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_spark_func.yml`_
- **2026-07-06** [`c960dd1e4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c960dd1e4e) [#15722](https://github.com/NVIDIA/TensorRT-LLM/pull/15722)
  [None][fix] Remove unreachable model path from MTPDraftModel (#15722)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`_

## AutoDeploy  (5 commits)

- **2026-07-13** [`56033086de`](https://github.com/NVIDIA/TensorRT-LLM/commit/56033086de) [#16285](https://github.com/NVIDIA/TensorRT-LLM/pull/16285)
  [https://nvbugs/6367792][fix] unwaive Nano AutoDeploy tests (#16285)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-12** [`5e7788245e`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e7788245e) [#15351](https://github.com/NVIDIA/TensorRT-LLM/pull/15351)
  [None][fix] AutoDeploy: return fused_weight_dims so fused QKV split sizes are rescaled under TP (#15351)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/sharding.py`, `tests/unittest/auto_deploy/singlegpu/transformations/library/test_determine_fused_weight_dims.py`_
- **2026-07-09** [`d8c3ef48f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/d8c3ef48f9) [#16138](https://github.com/NVIDIA/TensorRT-LLM/pull/16138)
  [None][test] copy AD smoke tests to LLMC standalone (#16138)
  _Files: `examples/auto_deploy/llmc/create_standalone_package.py`, `tests/unittest/auto_deploy/standalone/test_standalone_test_export.py`_
- **2026-07-08** [`7c4d3abafd`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c4d3abafd) [#15726](https://github.com/NVIDIA/TensorRT-LLM/pull/15726)
  [None][infra] Optionally redirect AutoDeploy imports to llm-c (#15726)
  _Files: `examples/auto_deploy/llmc/README.md`, `examples/auto_deploy/llmc/create_standalone_package.py`, `tensorrt_llm/_torch/auto_deploy/__init__.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/sharding.py` _+12 more__
- **2026-07-07** [`f4742f6868`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4742f6868) [#16023](https://github.com/NVIDIA/TensorRT-LLM/pull/16023)
  [https://nvbugs/6422094][fix] Waive failing AutoDeploy UT when testing PR#15923 (#16023)
  _Files: `tests/integration/test_lists/waives.txt`_

## Models  (4 commits)

- **2026-07-08** [`b62f605e59`](https://github.com/NVIDIA/TensorRT-LLM/commit/b62f605e59) [#15997](https://github.com/NVIDIA/TensorRT-LLM/pull/15997)
  [None][fix] Fix Qwen2-VL Transformers 5 compatibility (#15997)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tests/unittest/_torch/modeling/test_modeling_qwen2_5vl.py`_
- **2026-07-07** [`a0bb252ea3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0bb252ea3) [#15598](https://github.com/NVIDIA/TensorRT-LLM/pull/15598)
  [None][perf] Improve Qwen3-VL Preprocessing Perf (#15598)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/commands/serve.py` _+6 more__
- **2026-07-06** [`ca708a1f71`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca708a1f71) [#15957](https://github.com/NVIDIA/TensorRT-LLM/pull/15957)
  [https://nvbugs/6401925][fix] Unwaive DeepSeek V4 compressor corner-case test (#15957)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`b420e72266`](https://github.com/NVIDIA/TensorRT-LLM/commit/b420e72266) [#15547](https://github.com/NVIDIA/TensorRT-LLM/pull/15547)
  [None][fix] Pass dtype to AllReduce ctor to enable MNNVL all-reduce fo… (#15547)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`_

## Perf  (2 commits)

- **2026-07-13** [`a201a43a16`](https://github.com/NVIDIA/TensorRT-LLM/commit/a201a43a16) [#15284](https://github.com/NVIDIA/TensorRT-LLM/pull/15284)
  [None][perf] offload chat template rendering into async (#15284)
  _Files: `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/resource_governor.py`, `tensorrt_llm/serve/responses_utils.py` _+1 more__
- **2026-07-13** [`c7d2498bda`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7d2498bda) [#16126](https://github.com/NVIDIA/TensorRT-LLM/pull/16126)
  [None][perf] serve: opt-in msgspec msgpack transport for disagg orchestrator->worker request body (#16126)
  _Files: `requirements.txt`, `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_server.py`_

## ROCm / AMD  (1 commits)

- **2026-07-13** [`6c43b3eddc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c43b3eddc) [#16053](https://github.com/NVIDIA/TensorRT-LLM/pull/16053)
  [None][feat] Support externally provided MPI sessions with explicit ownership (#16053)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/rpc_proxy.py` _+2 more__

## Docs / Examples  (1 commits)

- **2026-07-10** [`ed3659a865`](https://github.com/NVIDIA/TensorRT-LLM/commit/ed3659a865) [#15608](https://github.com/NVIDIA/TensorRT-LLM/pull/15608)
  [TRTLLM-13406][feat] add in-process NeMo-Skills accuracy benchmarks (#15608)
  _Files: `examples/trtllm-eval/README.md`, `examples/trtllm-eval/install_nemo_skills.sh`, `examples/trtllm-eval/requirements_nemo_skills.txt`, `tensorrt_llm/commands/eval.py` _+3 more__

## LoRA  (1 commits)

- **2026-07-06** [`7c8dde830b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c8dde830b) [#13911](https://github.com/NVIDIA/TensorRT-LLM/pull/13911)
  [TRTLLM-12647][feat] Parallelize LTX-2 LoRA weight loading (#13911)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_

---
_Generated 2026-07-13 11:27 UTC_