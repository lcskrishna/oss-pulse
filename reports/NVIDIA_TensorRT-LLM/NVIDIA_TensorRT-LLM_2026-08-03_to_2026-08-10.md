# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-08-03 → 2026-08-10  |  **Total commits:** 197

## ✨ New Features This Week

- **2026-08-10** [#16942](https://github.com/NVIDIA/TensorRT-LLM/pull/16942) — [None][feat] Opt GPT-OSS in to KV cache manager V2 by default (#16942)
- **2026-08-08** [#17334](https://github.com/NVIDIA/TensorRT-LLM/pull/17334) — [TRTLLM-14815][feat] Enable disaggregated serving for Kimi K3 (#17334)
- **2026-08-08** [#17333](https://github.com/NVIDIA/TensorRT-LLM/pull/17333) — [TRTLLM-14813][doc] Add Kimi K3 examples and deployment guide (#17333)
- **2026-08-08** [#16162](https://github.com/NVIDIA/TensorRT-LLM/pull/16162) — [None][feat] Add FastWan2.2 TI2V-5B DMD pipeline (3-step text-to-video) (#16162)
- **2026-08-07** [#16511](https://github.com/NVIDIA/TensorRT-LLM/pull/16511) — [TRTLLM-12720][feat] Support nvfp4 w4a16 on sm120 (#16511)
- **2026-08-07** [#17394](https://github.com/NVIDIA/TensorRT-LLM/pull/17394) — [None][infra] Enable source code scanning for nightly release (#17394)
- **2026-08-07** [#17360](https://github.com/NVIDIA/TensorRT-LLM/pull/17360) — [None][feat] Default MiniMax M2 to KV cache manager V2 (#17360)
- **2026-08-07** [#17125](https://github.com/NVIDIA/TensorRT-LLM/pull/17125) — [None][feat] Default Kimi K2.5 to KV cache manager V2 (#17125)
- **2026-08-07** [#17119](https://github.com/NVIDIA/TensorRT-LLM/pull/17119) — [TRTLLM-14822][feat] deprecate WIDEEP MoE backend (#17119)
- **2026-08-07** [#17270](https://github.com/NVIDIA/TensorRT-LLM/pull/17270) — [TRTLLM-14934][feat] add MoE implementation identity and contract layer (#17270)
- _…and 30 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#16827](https://github.com/NVIDIA/TensorRT-LLM/issues/16827) | [Performance]: MAX_UTILIZATION causes a 40.6% output-throughput drop a | KV-Cache Management, Pytorch, General perf | 2026-08-09 |
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-08-09 |
| [#17437](https://github.com/NVIDIA/TensorRT-LLM/issues/17437) | [Bug]: Interior control-token rejection can split a tool-call prelude  | Speculative Decoding | 2026-08-08 |
| [#17016](https://github.com/NVIDIA/TensorRT-LLM/issues/17016) | [RFC]: Add openengine gRPC server support to trtllm-serve | RFC | 2026-08-03 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-07-29 |
| [#17020](https://github.com/NVIDIA/TensorRT-LLM/issues/17020) | `trtllm-eval aime25`/`aime26` silently disable thinking on DeepSeek-V4 | — | 2026-07-29 |
| [#17013](https://github.com/NVIDIA/TensorRT-LLM/issues/17013) | [RFC]: Reduce overhead in KV cache event publishing | RFC | 2026-07-29 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-07-25 |
| [#16459](https://github.com/NVIDIA/TensorRT-LLM/issues/16459) | [Bug]: Preserve per-item processed metadata when computing multimodal  | Multimodal | 2026-07-21 |
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |
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

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 65 |
| Attention | 24 |
| MoE | 22 |
| Executor / Runtime | 21 |
| Models | 17 |
| Disaggregation / KV | 15 |
| Torch Path (_torch) | 10 |
| Other | 7 |
| Quantization | 6 |
| Speculative Decoding | 3 |
| Docs / Examples | 3 |
| AutoDeploy | 2 |
| Compilation / Graph | 1 |
| LoRA | 1 |

## CI / Infra  (65 commits)

- **2026-08-10** [`07a559193f`](https://github.com/NVIDIA/TensorRT-LLM/commit/07a559193f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-10** [`3bffdc314e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bffdc314e) [#17418](https://github.com/NVIDIA/TensorRT-LLM/pull/17418)
  [https://nvbugs/6567065][fix] Unwaive some fixed cases (#17418)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`d0b5862877`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0b5862877)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-10** [`fa73933d22`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa73933d22) [#17458](https://github.com/NVIDIA/TensorRT-LLM/pull/17458)
  [None][infra] Waive 23 failed cases for main in post-merge 2894 (#17458)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`5761d00e50`](https://github.com/NVIDIA/TensorRT-LLM/commit/5761d00e50) [#17442](https://github.com/NVIDIA/TensorRT-LLM/pull/17442)
  [None][infra] Unwaive 5 disagg gen only cases (#17442)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`cba210a39d`](https://github.com/NVIDIA/TensorRT-LLM/commit/cba210a39d) [#17407](https://github.com/NVIDIA/TensorRT-LLM/pull/17407)
  [None][infra] Waive 12 failed cases for main in post-merge 2889 (#17407)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`5ea61f33df`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ea61f33df)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-09** [`cc678cd683`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc678cd683) [#17443](https://github.com/NVIDIA/TensorRT-LLM/pull/17443)
  [None][infra] Waive 1 failed cases for main in pre-merge 52592 (#17443)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-09** [`1d7c771da7`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d7c771da7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-08** [`3d1596b755`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d1596b755)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-08** [`c9496304d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9496304d4)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-07** [`81db688249`](https://github.com/NVIDIA/TensorRT-LLM/commit/81db688249) [#17424](https://github.com/NVIDIA/TensorRT-LLM/pull/17424)
  [None][infra] Waive 2 failed cases for main in pre-merge 52390 (#17424)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-07** [`6c055a6bf9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c055a6bf9) [#17394](https://github.com/NVIDIA/TensorRT-LLM/pull/17394)
  [None][infra] Enable source code scanning for nightly release (#17394)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-07** [`f0dc88f22b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0dc88f22b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-07** [`378136e093`](https://github.com/NVIDIA/TensorRT-LLM/commit/378136e093)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-07** [`95e76ba38a`](https://github.com/NVIDIA/TensorRT-LLM/commit/95e76ba38a) [#17402](https://github.com/NVIDIA/TensorRT-LLM/pull/17402)
  [None][infra] Waive 1 failed cases for main in pre-merge 52367 (#17402)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-07** [`92e7c88301`](https://github.com/NVIDIA/TensorRT-LLM/commit/92e7c88301) [#17400](https://github.com/NVIDIA/TensorRT-LLM/pull/17400)
  [None][infra] Add blossom-ci authorized users (#17400)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-08-07** [`cc092ade7c`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc092ade7c) [#17356](https://github.com/NVIDIA/TensorRT-LLM/pull/17356)
  [TRTLLMINF-240][infra] stabilize nightly Docker stage selection (#17356)
  _Files: `jenkins/BuildDockerImage.groovy`_
- **2026-08-07** [`8836813742`](https://github.com/NVIDIA/TensorRT-LLM/commit/8836813742) [#17350](https://github.com/NVIDIA/TensorRT-LLM/pull/17350)
  [None][infra] Unwaive perf-sanity disagg gen_only cases (#17350)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-07** [`5cc76ef73f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cc76ef73f) [#17310](https://github.com/NVIDIA/TensorRT-LLM/pull/17310)
  [https://nvbugs/6506920][fix] Recover DSpark E2E coverage (#17310)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-08-07** [`ba92c2ac22`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba92c2ac22) [#16510](https://github.com/NVIDIA/TensorRT-LLM/pull/16510)
  [None][infra] Using agent to triage risks detected from PLC pipeline (#16510)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`, `jenkins/scripts/pulse_in_pipeline_scanning/main.py`, `jenkins/scripts/pulse_in_pipeline_scanning/submit_preapproved_candidates.py`, `jenkins/scripts/pulse_in_pipeline_scanning/submit_report.py` _+4 more__
- **2026-08-07** [`e1a952a0ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1a952a0ed) [#17385](https://github.com/NVIDIA/TensorRT-LLM/pull/17385)
  [None][infra] Waive 1 failed cases for main in pre-merge 52242 (#17385)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-07** [`05507c02e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/05507c02e2) [#17384](https://github.com/NVIDIA/TensorRT-LLM/pull/17384)
  [None][infra] Waive 2 failed cases for main in pre-merge 52229 (#17384)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`2a40e27d91`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a40e27d91)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-06** [`e3e5ccaf0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3e5ccaf0c) [#17354](https://github.com/NVIDIA/TensorRT-LLM/pull/17354)
  [None][infra] Waive 1 failed cases for main in pre-merge 52106 (#17354)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`182c54099e`](https://github.com/NVIDIA/TensorRT-LLM/commit/182c54099e) [#17304](https://github.com/NVIDIA/TensorRT-LLM/pull/17304)
  [None][infra] Stop CBTS coverage writes from failing the stage results tar (#17304)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/coverage_utils/README.md`, `jenkins/scripts/cbts/coverage_utils/sitecustomize.py`_
- **2026-08-06** [`2cbc8beda0`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cbc8beda0) [#17248](https://github.com/NVIDIA/TensorRT-LLM/pull/17248)
  [TRTLLMINF-240][infra] L0 job enhancement for automatic nightly release (#17248)
  _Files: `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy` _+2 more__
- **2026-08-06** [`409bccf293`](https://github.com/NVIDIA/TensorRT-LLM/commit/409bccf293) [#17340](https://github.com/NVIDIA/TensorRT-LLM/pull/17340)
  [None][infra] Waive 11 failed cases for main in post-merge 2887 (#17340)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`80b9301f66`](https://github.com/NVIDIA/TensorRT-LLM/commit/80b9301f66) [#17338](https://github.com/NVIDIA/TensorRT-LLM/pull/17338)
  [None][infra] Waive 3 failed cases for main in pre-merge 52038 (#17338)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`be9b16c99a`](https://github.com/NVIDIA/TensorRT-LLM/commit/be9b16c99a) [#17335](https://github.com/NVIDIA/TensorRT-LLM/pull/17335)
  [None][infra] Waive 18 failed cases for main in post-merge 2887 (#17335)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`75fb937426`](https://github.com/NVIDIA/TensorRT-LLM/commit/75fb937426) [#17329](https://github.com/NVIDIA/TensorRT-LLM/pull/17329)
  [None][test] Waive 3 failed cases for main in QA CI (#17329)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`22184ba7cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/22184ba7cb) [#17140](https://github.com/NVIDIA/TensorRT-LLM/pull/17140)
  [None][fix] Bound GEN log sentinel wait (#17140)
  _Files: `jenkins/scripts/perf/submit.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/scripts/test_perf_sanity_helpers.py`, `tests/unittest/scripts/test_perf_submit.py`_
- **2026-08-05** [`e5e3821270`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5e3821270) [#17130](https://github.com/NVIDIA/TensorRT-LLM/pull/17130)
  [None][fix] Suppress agent-path junit for monitor-detected SLURM infra retries (#17130)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-05** [`ad5b1eda35`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad5b1eda35) [#17309](https://github.com/NVIDIA/TensorRT-LLM/pull/17309)
  [https://nvbugs/6528742][test] Unwaive Nemotron V3 Super Mamba tests (#17309)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`7f1f219fe0`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f1f219fe0) [#16977](https://github.com/NVIDIA/TensorRT-LLM/pull/16977)
  [None][infra] Enable OCI-AGA cluster for GB300 (#16977)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus.yml`_
- **2026-08-05** [`c761f3ac4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c761f3ac4a) [#17280](https://github.com/NVIDIA/TensorRT-LLM/pull/17280)
  [None][infra] Waive 5 failed cases for main in post-merge 2885 (#17280)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`67579d8ba4`](https://github.com/NVIDIA/TensorRT-LLM/commit/67579d8ba4) [#17272](https://github.com/NVIDIA/TensorRT-LLM/pull/17272)
  [None][infra] Waive 19 failed cases for main in post-merge 2884 (#17272)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`91fb4433c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/91fb4433c5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-08-04** [`1982523277`](https://github.com/NVIDIA/TensorRT-LLM/commit/1982523277) [#17255](https://github.com/NVIDIA/TensorRT-LLM/pull/17255)
  [TRTLLMINF-40][fix] Throw typed InfraFailure when SLURM submission yields no job ID (#17255)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-04** [`721c46b8c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/721c46b8c2) [#17134](https://github.com/NVIDIA/TensorRT-LLM/pull/17134)
  [None][fix] Align perf launcher with pytest shard (#17134)
  _Files: `jenkins/scripts/perf/submit.py`, `tests/unittest/scripts/test_perf_submit.py`_
- **2026-08-04** [`0d31abb6c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d31abb6c1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-04** [`114d84903e`](https://github.com/NVIDIA/TensorRT-LLM/commit/114d84903e) [#17207](https://github.com/NVIDIA/TensorRT-LLM/pull/17207)
  [https://nvbugs/6550126][fix] Renamed the integration test's kwarg and its constant to… (#17207)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-04** [`0448fe9b94`](https://github.com/NVIDIA/TensorRT-LLM/commit/0448fe9b94) [#17136](https://github.com/NVIDIA/TensorRT-LLM/pull/17136)
  [TRTLLMINF-237][infra] Adopt resourceLedger.withResource for BuildDockerImage (#17136)
  _Files: `jenkins/BuildDockerImage.groovy`_
- **2026-08-04** [`0a6d932303`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a6d932303) [#16578](https://github.com/NVIDIA/TensorRT-LLM/pull/16578)
  [TRTLLMINF-218][infra] Gate multi-GPU CI stages behind 'ci: full pre-merge approved' label (#16578)
  _Files: `.github/workflows/bot-command.yml`, `.github/workflows/full-premerge-approval.yml`, `docs/source/developer-guide/ci-overview.md`, `jenkins/L0_MergeRequest.groovy` _+1 more__
- **2026-08-04** [`a61c531693`](https://github.com/NVIDIA/TensorRT-LLM/commit/a61c531693) [#17058](https://github.com/NVIDIA/TensorRT-LLM/pull/17058)
  [TRTLLMINF-257][infra] fix build status miss in gitlab when trigger by timer or by hand (#17058)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-04** [`392ded7ee8`](https://github.com/NVIDIA/TensorRT-LLM/commit/392ded7ee8) [#17065](https://github.com/NVIDIA/TensorRT-LLM/pull/17065)
  [https://nvbugs/6533919][fix] Report unknown stages on stderr with `difflib` near-miss hints, distinguish… (#17065)
  _Files: `docs/source/developer-guide/ci-overview.md`, `scripts/test_to_stage_mapping.py`, `tests/unittest/tools/test_test_to_stage_mapping.py`_
- **2026-08-04** [`164a0e380e`](https://github.com/NVIDIA/TensorRT-LLM/commit/164a0e380e) [#17038](https://github.com/NVIDIA/TensorRT-LLM/pull/17038)
  [https://nvbugs/6481375][test] Unwaive passing DSV3-Lite tests (#17038)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`73efcee592`](https://github.com/NVIDIA/TensorRT-LLM/commit/73efcee592) [#17133](https://github.com/NVIDIA/TensorRT-LLM/pull/17133)
  [None][infra] Migrate GB200 jobs off of aws-dfw (#17133)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-03** [`624521576f`](https://github.com/NVIDIA/TensorRT-LLM/commit/624521576f) [#17214](https://github.com/NVIDIA/TensorRT-LLM/pull/17214)
  [https://nvbugs/6550708][infra] Re-enable Cosmos3 distilled tests (#17214)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`7b50104221`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b50104221) [#17181](https://github.com/NVIDIA/TensorRT-LLM/pull/17181)
  [None][infra] Waive 4 failed cases for main in pre-merge 51340 (#17181)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`c5427c5dd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5427c5dd7) [#17184](https://github.com/NVIDIA/TensorRT-LLM/pull/17184)
  [None][infra] Waive 1 failed cases for main in pre-merge 51267 (#17184)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`d8b25c5acb`](https://github.com/NVIDIA/TensorRT-LLM/commit/d8b25c5acb) [#17203](https://github.com/NVIDIA/TensorRT-LLM/pull/17203)
  [None][test] Waive 1 failed cases for main in QA CI (#17203)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`bd39b9c494`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd39b9c494) [#17201](https://github.com/NVIDIA/TensorRT-LLM/pull/17201)
  [None][test] Waive 2 failed cases for main in QA CI (#17201)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`fff6b88bfe`](https://github.com/NVIDIA/TensorRT-LLM/commit/fff6b88bfe) [#17198](https://github.com/NVIDIA/TensorRT-LLM/pull/17198)
  [None][fix] Remove unexistent tests in waive.txt (#17198)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`455067c413`](https://github.com/NVIDIA/TensorRT-LLM/commit/455067c413) [#16835](https://github.com/NVIDIA/TensorRT-LLM/pull/16835)
  [None][infra] CBTS coverage data enhancement (#16835)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/coverage_utils/README.md`, `jenkins/scripts/cbts/coverage_utils/cbts_plugin.py`, `jenkins/scripts/cbts/coverage_utils/cbts_pystart.py` _+2 more__
- **2026-08-03** [`93e7c91763`](https://github.com/NVIDIA/TensorRT-LLM/commit/93e7c91763) [#17187](https://github.com/NVIDIA/TensorRT-LLM/pull/17187)
  [None][test] Waive 5 failed cases for main in QA CI (#17187)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`8e5a56482e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e5a56482e) [#17186](https://github.com/NVIDIA/TensorRT-LLM/pull/17186)
  [TRTLLM-14907][test] Waive 5 failed cases for main in QA CI (#17186)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`74f3ccfea0`](https://github.com/NVIDIA/TensorRT-LLM/commit/74f3ccfea0) [#17180](https://github.com/NVIDIA/TensorRT-LLM/pull/17180)
  [None][test] Waive 6 failed cases for main in QA CI (#17180)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`fb591d870e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb591d870e) [#17177](https://github.com/NVIDIA/TensorRT-LLM/pull/17177)
  [None][test] Waive 1 failed cases for main in QA CI (#17177)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`6414941fe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/6414941fe3) [#17176](https://github.com/NVIDIA/TensorRT-LLM/pull/17176)
  [None][test] Waive 8 failed cases for main in QA CI (#17176)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`24d0a8e1ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/24d0a8e1ca) [#17174](https://github.com/NVIDIA/TensorRT-LLM/pull/17174)
  [None][infra] Waive 13 failed cases for main in post-merge 2876 (#17174)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`0d77dbd5b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d77dbd5b6) [#16949](https://github.com/NVIDIA/TensorRT-LLM/pull/16949)
  [None][test] Waive 7 failed cases for main in QA CI (#16949)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`0ed6624984`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ed6624984) [#16986](https://github.com/NVIDIA/TensorRT-LLM/pull/16986)
  [None][test] Waive 4 failed cases for main in QA CI (#16986)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`6b199b9f16`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b199b9f16) [#17108](https://github.com/NVIDIA/TensorRT-LLM/pull/17108)
  [None][test] Waive 3 failed cases for main in QA CI (#17108)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-03** [`fea3bf4733`](https://github.com/NVIDIA/TensorRT-LLM/commit/fea3bf4733)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Attention  (24 commits)

- **2026-08-10** [`4ec478dede`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ec478dede) [#17445](https://github.com/NVIDIA/TensorRT-LLM/pull/17445)
  [None][fix] Kimi K3 MLA: pass attn_output to MLA.forward_impl (#17445)
  _Files: `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`_
- **2026-08-09** [`1cef02e901`](https://github.com/NVIDIA/TensorRT-LLM/commit/1cef02e901) [#17282](https://github.com/NVIDIA/TensorRT-LLM/pull/17282)
  [None][fix] fix disagg overlap slot headroom without MTP (#17282)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_deepseek_v3_lite_attention_dp_overlap.yaml` _+3 more__
- **2026-08-09** [`52d08b1415`](https://github.com/NVIDIA/TensorRT-LLM/commit/52d08b1415) [#16706](https://github.com/NVIDIA/TensorRT-LLM/pull/16706)
  [None][perf] optimize encoder-decoder PyTorch performance (#16706)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `docs/source/models/encoder-decoder.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+19 more__
- **2026-08-08** [`937bacc2ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/937bacc2ab) [#17327](https://github.com/NVIDIA/TensorRT-LLM/pull/17327)
  [TRTLLM-14814][feat] Kimi K3 serving parsers, chat template, and speculative decoding (suffix automaton + DFlash scaffold) (#17327)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `examples/kimi_k3/README.md`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/attention_backend/utils.py` _+20 more__
- **2026-08-07** [`8fa2a6f59d`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fa2a6f59d) [#17416](https://github.com/NVIDIA/TensorRT-LLM/pull/17416)
  [None][fix] Set in_mtp_draft_loop on the synthetic DSA metadata stub (#17416)
  _Files: `tests/unittest/_torch/attention/sparse/dsa/test_req_idx_per_token.py`_
- **2026-08-07** [`57287cec8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/57287cec8c) [#16379](https://github.com/NVIDIA/TensorRT-LLM/pull/16379)
  [None][fix] laguna: honour attention_factor as final YaRN scaling coefficient (#16379)
  _Files: `tensorrt_llm/_torch/models/modeling_laguna.py`_
- **2026-08-07** [`b40c29bb33`](https://github.com/NVIDIA/TensorRT-LLM/commit/b40c29bb33) [#17286](https://github.com/NVIDIA/TensorRT-LLM/pull/17286)
  [None][fix] Warm up flashinfer sampling module during engine warmup (#17286)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`_
- **2026-08-07** [`5a47974235`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a47974235) [#16925](https://github.com/NVIDIA/TensorRT-LLM/pull/16925)
  [https://nvbugs/6513132][fix] DSA: rebuild token-to-request map inside the MTP draft loop (#16925)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tests/unittest/_torch/attention/sparse/dsa/test_req_idx_per_token.py`_
- **2026-08-06** [`63eb095097`](https://github.com/NVIDIA/TensorRT-LLM/commit/63eb095097) [#17243](https://github.com/NVIDIA/TensorRT-LLM/pull/17243)
  [https://nvbugs/6545424][perf] Enable Qwen3.5 fused ops under torch.c… (#17243)
  _Files: `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/modules/fused_ops/fused_qk_norm_rope_gate.py`, `tensorrt_llm/_torch/modules/mamba/layernorm_gated.py`, `tensorrt_llm/_torch/modules/qk_norm_attention.py` _+3 more__
- **2026-08-05** [`3e16ef2409`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e16ef2409) [#17225](https://github.com/NVIDIA/TensorRT-LLM/pull/17225)
  [None][feat] Add Kimi K3 KDA prefill/MTP decode CuTe DSL kernels and fused attention-residual kernel (#17225)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.cu` _+15 more__
- **2026-08-05** [`7e239d6377`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e239d6377) [#15138](https://github.com/NVIDIA/TensorRT-LLM/pull/15138)
  [None][feat] add CuteDSL FP8/FP16 MLA decode attention fmha lib (#15138)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+12 more__
- **2026-08-05** [`e88d42ab7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e88d42ab7a) [#16558](https://github.com/NVIDIA/TensorRT-LLM/pull/16558)
  [None][perf] Allocate DSA indexer k-cache only for layers that own an indexer (#16558)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/executor/dataTransceiverState.h`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.cpp` _+22 more__
- **2026-08-05** [`6d72d24b8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d72d24b8f) [#17247](https://github.com/NVIDIA/TensorRT-LLM/pull/17247)
  [None][fix] Announce MTP shapes to attention metadata in layer-wise benchmarks (#17247)
  _Files: `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`_
- **2026-08-04** [`d7fe72a5a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7fe72a5a3) [#17165](https://github.com/NVIDIA/TensorRT-LLM/pull/17165)
  [TRTLLM-14904][fix] Work around flashinfer 0.6.15 autotuner cache-key hash/eq inconsistency (#17165)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-08-04** [`603da8f4ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/603da8f4ac) [#16568](https://github.com/NVIDIA/TensorRT-LLM/pull/16568)
  [https://nvbugs/6442073][fix] Enforce a fixed max_seq_len for Qwen's AttentionOp caching purposes (#16568)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_encoder.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+4 more__
- **2026-08-04** [`536326f01b`](https://github.com/NVIDIA/TensorRT-LLM/commit/536326f01b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+10 more__
- **2026-08-04** [`3904311f5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3904311f5e) [#17106](https://github.com/NVIDIA/TensorRT-LLM/pull/17106)
  [None][feat] Enable block reuse for flashinfer (#17106)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/unittest/_torch/executor/test_py_executor_creator_mla_cache_reuse_sync.py`, `tests/unittest/llmapi/test_llm_pytorch.py`_
- **2026-08-04** [`6af4e0be43`](https://github.com/NVIDIA/TensorRT-LLM/commit/6af4e0be43) [#17092](https://github.com/NVIDIA/TensorRT-LLM/pull/17092)
  [None][perf] Deduplicate plan builds for MinimaxM3 in eager mode (#17092)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/msa_sparse_gqa.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_indexer.py`_
- **2026-08-04** [`048ae4acde`](https://github.com/NVIDIA/TensorRT-LLM/commit/048ae4acde) [#15833](https://github.com/NVIDIA/TensorRT-LLM/pull/15833)
  [None][feat] Add Gemma4 MTP assistant support (#15833)
  _Files: `docs/source/models/supported-models.md`, `examples/llm-api/quickstart_advanced.py`, `examples/models/core/gemma/README.md`, `tensorrt_llm/_torch/attention_backend/flashinfer.py` _+17 more__
- **2026-08-04** [`b0086164b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0086164b8) [#16957](https://github.com/NVIDIA/TensorRT-LLM/pull/16957)
  [None][feat] Add TriAttention KV-cache compression method (#16957)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.h`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2Utils.cpp`, `examples/kv_cache_compression/triattention.md` _+25 more__
- **2026-08-03** [`7e2fca051d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e2fca051d) [#17055](https://github.com/NVIDIA/TensorRT-LLM/pull/17055)
  [https://nvbugs/6533916][fix] Make sparse attention example runnable (#17055)
  _Files: `examples/llm-api/llm_sparse_attention.py`_
- **2026-08-03** [`ea39429f92`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea39429f92) [#16714](https://github.com/NVIDIA/TensorRT-LLM/pull/16714)
  [None][feat] Add paged KV cache support to Vanilla attention (#16714)
  _Files: `tensorrt_llm/_torch/attention_backend/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/attention/backend_capability.py`, `tests/unittest/_torch/attention/test_vanilla_attention.py`_
- **2026-08-03** [`c0836f0f1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0836f0f1d) [#16399](https://github.com/NVIDIA/TensorRT-LLM/pull/16399)
  [https://nvbugs/6368562][fix] Reserve fp8 context-MLA attention workspace in KV cache estimation (#16399)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+7 more__
- **2026-08-03** [`bf1ddb7e3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/bf1ddb7e3e) [#17118](https://github.com/NVIDIA/TensorRT-LLM/pull/17118)
  [None][chore] Give MLA model-owned aux streams via aux_stream_dict (#17118)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/modules/mla.py` _+1 more__

## MoE  (22 commits)

- **2026-08-10** [`ec044a2e1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec044a2e1a) [#17293](https://github.com/NVIDIA/TensorRT-LLM/pull/17293)
  [https://nvbugs/6434512][fix] Select Marlin for Qwen3.5 MoE on Hopper (#17293)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl_moe.py`_
- **2026-08-08** [`6ba3de1cbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ba3de1cbd) [#17376](https://github.com/NVIDIA/TensorRT-LLM/pull/17376)
  [https://nvbugs/6482566][fix] Make MoE all-to-all completion-flag timeout phase-aware (#17376)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h`, `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+1 more__
- **2026-08-07** [`a88f889c9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a88f889c9c) [#16511](https://github.com/NVIDIA/TensorRT-LLM/pull/16511)
  [TRTLLM-12720][feat] Support nvfp4 w4a16 on sm120 (#16511)
  _Files: `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/marlin/marlin.cuh`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4.h`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4_gemm.cu` _+24 more__
- **2026-08-07** [`2c96f9424a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c96f9424a) [#17332](https://github.com/NVIDIA/TensorRT-LLM/pull/17332)
  [TRTLLM-14813][test] Port Kimi K3 unit tests and wire GB300 L0 stages (#17332)
  _Files: `tests/integration/test_lists/test-db/l0_gb300_multi_gpus.yml`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py`, `tests/unittest/_torch/modules/kimi_kda/test_kda_decode_op.py`, `tests/unittest/_torch/modules/moe/test_kimi_k3_mlp.py` _+3 more__
- **2026-08-07** [`a87741ef3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/a87741ef3d) [#12733](https://github.com/NVIDIA/TensorRT-LLM/pull/12733)
  [None][refactor] Unify sparse attention framework with clean backend interfaces (#12733)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`, `cpp/tensorrt_llm/kernels/sparseAttentionKernels.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp` _+77 more__
- **2026-08-07** [`f8190db37b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f8190db37b) [#17119](https://github.com/NVIDIA/TensorRT-LLM/pull/17119)
  [TRTLLM-14822][feat] deprecate WIDEEP MoE backend (#17119)
  _Files: `docs/source/deployment-guide/deployment-guide-for-deepseek-r1-on-trtllm.md`, `examples/layer_wise_benchmarks/README.md`, `examples/layer_wise_benchmarks/run.py`, `examples/llm-api/llm_sparse_attention.py` _+23 more__
- **2026-08-07** [`d274d61b35`](https://github.com/NVIDIA/TensorRT-LLM/commit/d274d61b35) [#17270](https://github.com/NVIDIA/TensorRT-LLM/pull/17270)
  [TRTLLM-14934][feat] add MoE implementation identity and contract layer (#17270)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/impl_base.py`, `tensorrt_llm/_torch/modules/fused_moe/impl_contract.py`, `tensorrt_llm/_torch/modules/fused_moe/impl_identity.py`_
- **2026-08-06** [`36922c7283`](https://github.com/NVIDIA/TensorRT-LLM/commit/36922c7283) [#17269](https://github.com/NVIDIA/TensorRT-LLM/pull/17269)
  [TRTLLM-14813][feat] Add Kimi K3 (KimiLinear) model (#17269)
  _Files: `cpp/tensorrt_llm/thop/kdaDecodeOp.cpp`, `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/kimi_linear.py`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+45 more__
- **2026-08-06** [`253797c041`](https://github.com/NVIDIA/TensorRT-LLM/commit/253797c041) [#17196](https://github.com/NVIDIA/TensorRT-LLM/pull/17196)
  [None][fix] Fix Qwen3 w4a8 model execution failure and add unit test (re-open of #14527) (#17196)
  _Files: `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+3 more__
- **2026-08-06** [`bc334fb786`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc334fb786) [#17328](https://github.com/NVIDIA/TensorRT-LLM/pull/17328)
  [https://nvbugs/6564714][fix] Fix the FP8BlockScaleMoERunner get_fallback_tactic (#17328)
  _Files: `tensorrt_llm/_torch/custom_ops/trtllm_gen_custom_ops.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`4aea8b1d78`](https://github.com/NVIDIA/TensorRT-LLM/commit/4aea8b1d78) [#17175](https://github.com/NVIDIA/TensorRT-LLM/pull/17175)
  [None][chore] Update flashinfer-python from 0.6.15 to 0.6.16 (#17175)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml` _+2 more__
- **2026-08-06** [`a1c13ffb82`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1c13ffb82) [#17344](https://github.com/NVIDIA/TensorRT-LLM/pull/17344)
  [https://nvbugs/6567403][fix] Waive hanging MoE multi-GPU tests on Hopper (#17344)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`60ff8b7843`](https://github.com/NVIDIA/TensorRT-LLM/commit/60ff8b7843) [#15887](https://github.com/NVIDIA/TensorRT-LLM/pull/15887)
  [https://nvbugs/5805494][fix] Use int64 indexing in trtllm-gen block-scale MoE kernels (#15887)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`_
- **2026-08-05** [`1dfb7b1345`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dfb7b1345) [#17190](https://github.com/NVIDIA/TensorRT-LLM/pull/17190)
  [TRTLLM-14701][feat] Update trtllm-gen batchedGemm kernel drop for Kimi K3 MoE (#17190)
- **2026-08-05** [`d010c62971`](https://github.com/NVIDIA/TensorRT-LLM/commit/d010c62971) [#16603](https://github.com/NVIDIA/TensorRT-LLM/pull/16603)
  [https://nvbugs/6379316][fix] Reject MNNVL on split NVLink topology (#16603)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`, `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/modules/fused_moe/communication/deep_ep_low_latency.py` _+4 more__
- **2026-08-05** [`a6aeaff46c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6aeaff46c) [#17290](https://github.com/NVIDIA/TensorRT-LLM/pull/17290)
  [TRTLLM-13696][test] Part2.2: Migrate CPU only tests - generic, models, disagg (#17290)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/integration/test_lists/test-db/l0_h100.yml` _+80 more__
- **2026-08-05** [`9564b3b4ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/9564b3b4ff) [#17153](https://github.com/NVIDIA/TensorRT-LLM/pull/17153)
  [https://nvbugs/6517834][fix] Fix attn_dense LoRA input dim and Triton MoE padded-view output (#17153)
  _Files: `cpp/tensorrt_llm/runtime/loraModule.cpp`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`, `tests/integration/defs/examples/test_gpt.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`975efd3f32`](https://github.com/NVIDIA/TensorRT-LLM/commit/975efd3f32) [#17120](https://github.com/NVIDIA/TensorRT-LLM/pull/17120)
  [None][fix] Fix Qwen3.5 MoE fallback, GDN alignment, FP8 activation, and draft KV cache (#17120)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h` _+9 more__
- **2026-08-05** [`89bba4cfd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/89bba4cfd9) [#15297](https://github.com/NVIDIA/TensorRT-LLM/pull/15297)
  [None][feat] Share Expert Fusion with cherry-pick #11143 (#15297)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingDeepSeek.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingKernel.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h` _+20 more__
- **2026-08-04** [`a2387bc541`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2387bc541) [#16498](https://github.com/NVIDIA/TensorRT-LLM/pull/16498)
  [TRTLLM-13696][test] Part2.1: Migrate CPU only tests - runtime (#16498)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/llmapi/llm_args.py`, `tests/README.md`, `tests/integration/defs/test_unittests.py` _+81 more__
- **2026-08-04** [`7a8d73de51`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a8d73de51) [#16749](https://github.com/NVIDIA/TensorRT-LLM/pull/16749)
  [None][feat] Enable Marlin NVFP4 on Ada Lovelace (#16749)
  _Files: `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/marlin/marlin.cuh`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4.h`, `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4_gemm.cu` _+16 more__
- **2026-08-03** [`563bf12e2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/563bf12e2b) [#16956](https://github.com/NVIDIA/TensorRT-LLM/pull/16956)
  [https://nvbugs/6517844][fix] Fall back to DeepEP when NCCL-EP lacks shared memory (#16956)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/communication/communication_factory.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modules/moe/test_communication_factory.py`_

## Executor / Runtime  (21 commits)

- **2026-08-10** [`f13a0be917`](https://github.com/NVIDIA/TensorRT-LLM/commit/f13a0be917) [#17281](https://github.com/NVIDIA/TensorRT-LLM/pull/17281)
  [TRTLLM-15151][chore] load models lazily (#17281)
  _Files: `tensorrt_llm/__init__.py`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_auto.py` _+27 more__
- **2026-08-09** [`d16d01ff29`](https://github.com/NVIDIA/TensorRT-LLM/commit/d16d01ff29) [#15043](https://github.com/NVIDIA/TensorRT-LLM/pull/15043)
  [None][fix] Enforce Responses conversation history capacity (#15043)
  _Files: `tensorrt_llm/serve/responses_utils.py`, `tests/unittest/llmapi/test_responses_utils.py`_
- **2026-08-07** [`9ac759cca5`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ac759cca5) [#17278](https://github.com/NVIDIA/TensorRT-LLM/pull/17278)
  [None][fix] Tolerate ADP pad-dummy surplus instead of asserting (#17278)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`, `tests/unittest/_torch/executor/test_seq_slot_sizing.py`_
- **2026-08-07** [`102173a632`](https://github.com/NVIDIA/TensorRT-LLM/commit/102173a632) [#17254](https://github.com/NVIDIA/TensorRT-LLM/pull/17254)
  [TRTLLM-14831][chore] Consolidate package bootstrap and relocate restricted deserialization (#17254)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+8 more__
- **2026-08-07** [`3cadcf0a9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3cadcf0a9b) [#17401](https://github.com/NVIDIA/TensorRT-LLM/pull/17401)
  [https://nvbugs/6555875][fix] refresh OpenAIServer test fake (#17401)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-08-07** [`57f2781e4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/57f2781e4e) [#16768](https://github.com/NVIDIA/TensorRT-LLM/pull/16768)
  [TRTLLM-14345][feat] Improve the GDN Replay Kernel Under Low Latency (#16768)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/modules/fla/cached_replay.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py` _+8 more__
- **2026-08-07** [`530ad05a0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/530ad05a0a) [#17289](https://github.com/NVIDIA/TensorRT-LLM/pull/17289)
  [https://nvbugs/6482589][fix] Make CuError pickle-safe across process boundaries (#17289)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_exceptions.py`_
- **2026-08-06** [`2224cb764f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2224cb764f) [#17213](https://github.com/NVIDIA/TensorRT-LLM/pull/17213)
  [TRTLLM-14953][feat] Add ability to honour generation_config.json sampling defaults (#17213)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/llmapi/llm.py` _+10 more__
- **2026-08-06** [`1745a6e689`](https://github.com/NVIDIA/TensorRT-LLM/commit/1745a6e689) [#17157](https://github.com/NVIDIA/TensorRT-LLM/pull/17157)
  [#17156][fix] Flush buffered text in DeepSeekR1Parser.finish() (#17157)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_
- **2026-08-06** [`9a2ff2ebc5`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a2ff2ebc5) [#17352](https://github.com/NVIDIA/TensorRT-LLM/pull/17352)
  [https://nvbugs/6567403][fix] Revert #17010 to unblock DGX_H100 PyTorch-Others-1 stage timeout (#17352)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`02540d6580`](https://github.com/NVIDIA/TensorRT-LLM/commit/02540d6580) [#16170](https://github.com/NVIDIA/TensorRT-LLM/pull/16170)
  [https://nvbugs/6388153][fix] Relay PP sample states synchronously on… (#16170)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`4f55d80c19`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f55d80c19) [#17277](https://github.com/NVIDIA/TensorRT-LLM/pull/17277)
  [None][fix] BREAKING Block reuse policy rename and add more tests (#17277)
  _Files: `docs/source/developer-guide/telemetry.md`, `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+6 more__
- **2026-08-05** [`a23e8decb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/a23e8decb5) [#17162](https://github.com/NVIDIA/TensorRT-LLM/pull/17162)
  [TRTLLM-14903][fix] Free partially-allocated warmup dummy KV blocks and count spec extra tokens in warmup block estimates (#17162)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/integration/defs/kv_cache/test_prefix_aware_scheduling.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-08-05** [`7608520881`](https://github.com/NVIDIA/TensorRT-LLM/commit/7608520881) [#17159](https://github.com/NVIDIA/TensorRT-LLM/pull/17159)
  [#17158][fix] Reject NaN top_p, min_p and temperature in SamplingParams (#17159)
  _Files: `tensorrt_llm/sampling_params.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_sampling_params.py`_
- **2026-08-05** [`0eea487886`](https://github.com/NVIDIA/TensorRT-LLM/commit/0eea487886) [#17205](https://github.com/NVIDIA/TensorRT-LLM/pull/17205)
  [https://nvbugs/6550727][fix] Pin `_force_non_greedy_for_capture=False` on the test double so it models a… (#17205)
  _Files: `tests/unittest/_torch/executor/test_pytorch_model_engine.py`_
- **2026-08-04** [`fd0b4bbf2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd0b4bbf2c) [#17172](https://github.com/NVIDIA/TensorRT-LLM/pull/17172)
  [TRTLLM-14864][feat] Support per-request seed in TorchSampler (#17172)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_common.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_strategy.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-08-04** [`60e7fcaeaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/60e7fcaeaf) [#17010](https://github.com/NVIDIA/TensorRT-LLM/pull/17010)
  [https://nvbugs/6525011][fix] Store the owning output tensor in _graph_output_refs for each graph's lifetime… (#17010)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-04** [`43d6fa410c`](https://github.com/NVIDIA/TensorRT-LLM/commit/43d6fa410c) [#17122](https://github.com/NVIDIA/TensorRT-LLM/pull/17122)
  [None][fix] KVCacheManagerV2: keep partial rewind endpoints reusable via per-page token coverage (#17122)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/introspection.cpp` _+14 more__
- **2026-08-03** [`ec852e140f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec852e140f) [#17149](https://github.com/NVIDIA/TensorRT-LLM/pull/17149)
  [None][fix] Mark prototype status for API flag index_share_for_mtp_iteration (#17149)
  _Files: `tensorrt_llm/llmapi/llm_args.py`_
- **2026-08-03** [`992b738dda`](https://github.com/NVIDIA/TensorRT-LLM/commit/992b738dda) [#16155](https://github.com/NVIDIA/TensorRT-LLM/pull/16155)
  [None][feat] Cosmos3 video-to-video (V2V) generation (#16155)
  _Files: `.gitignore`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `examples/visual_gen/models/cosmos3/prompts/v2v.json` _+31 more__
- **2026-08-03** [`bbadfb75a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbadfb75a1) [#17077](https://github.com/NVIDIA/TensorRT-LLM/pull/17077)
  [TRTLLM-14808][fix] MNNVL partial-allocation cleanup and warmup compile fix (#17077)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_

## Models  (17 commits)

- **2026-08-10** [`ae4520506f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae4520506f) [#17421](https://github.com/NVIDIA/TensorRT-LLM/pull/17421)
  [None][fix] Kimi K3: eager CUDA-graph buffer allocation and prebuilt fused-verify constants (#17421)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tests/unittest/_torch/modeling/test_kimi_kda_fused_verify_parity.py`_
- **2026-08-09** [`1511d31c21`](https://github.com/NVIDIA/TensorRT-LLM/commit/1511d31c21) [#17398](https://github.com/NVIDIA/TensorRT-LLM/pull/17398)
  [https://nvbugs/6388363][test] Unwaive the test of TestDeepSeekV3Lite… (#17398)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-08** [`b74ef37451`](https://github.com/NVIDIA/TensorRT-LLM/commit/b74ef37451) [#17375](https://github.com/NVIDIA/TensorRT-LLM/pull/17375)
  [https://nvbugs/6428096][fix] Unwaive DeepSeekV3Lite compiled tp2pp2 (#17375)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-08** [`d7053e55a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7053e55a7) [#17333](https://github.com/NVIDIA/TensorRT-LLM/pull/17333)
  [TRTLLM-14813][doc] Add Kimi K3 examples and deployment guide (#17333)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `docs/source/deployment-guide/index.rst`, `examples/kimi_k3/README.md`, `examples/kimi_k3/eval_extra_llm_options.yaml` _+9 more__
- **2026-08-07** [`4b69c59b41`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b69c59b41) [#17423](https://github.com/NVIDIA/TensorRT-LLM/pull/17423)
  [https://nvbugs/6523751][fix] Raise per-test timeout for gpt-oss-120b on SM120 (#17423)
  _Files: `tests/integration/test_lists/test-db/l0_rtx_pro_6000.yml`_
- **2026-08-07** [`0c746e1591`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c746e1591) [#17386](https://github.com/NVIDIA/TensorRT-LLM/pull/17386)
  [https://nvbugs/6487038][test] Unwaive GB300 Kimi gen-only (#17386)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`b21a3b4030`](https://github.com/NVIDIA/TensorRT-LLM/commit/b21a3b4030) [#16920](https://github.com/NVIDIA/TensorRT-LLM/pull/16920)
  [https://nvbugs/6490049][test] Unwaive GB300 Kimi disagg e2e (#16920)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`b775e80a5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b775e80a5a) [#17155](https://github.com/NVIDIA/TensorRT-LLM/pull/17155)
  [https://nvbugs/6428094][chore] Unwaive DeepSeekV3Lite tp2pp2 test (#17155)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-06** [`05d7947480`](https://github.com/NVIDIA/TensorRT-LLM/commit/05d7947480) [#17231](https://github.com/NVIDIA/TensorRT-LLM/pull/17231)
  [https://nvbugs/6550127][fix] Support Gemma4 multimodal cache partial hits (#17231)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_gemma4_multimodal.py`_
- **2026-08-05** [`a36b49d4fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/a36b49d4fa) [#17100](https://github.com/NVIDIA/TensorRT-LLM/pull/17100)
  [None][doc] Fix broken figures and math rendering in tech blogs 25 and 26 (#17100)
  _Files: `docs/source/blogs/tech_blog/blog25_Scaling_Video_Generation_Across_NVL72_Rack_with_TensorRT-LLM.md`, `docs/source/blogs/tech_blog/blog26_DeepSeek_V4_on_NVIDIA_Blackwell_Model_Specific_and_Agentic_Workload_Optimizations_in_TensorRT-LLM.md`_
- **2026-08-05** [`50edd73817`](https://github.com/NVIDIA/TensorRT-LLM/commit/50edd73817) [#17054](https://github.com/NVIDIA/TensorRT-LLM/pull/17054)
  [TRTLLM-14702][feat] Integrate Kimi K3 KDA decode kernel (#17054)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kdaDecode/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.cu` _+6 more__
- **2026-08-04** [`78639d2f68`](https://github.com/NVIDIA/TensorRT-LLM/commit/78639d2f68) [#17217](https://github.com/NVIDIA/TensorRT-LLM/pull/17217)
  [https://nvbugs/6426847][fix] Unwaive DeepSeekV3Lite MTP test (#17217)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-04** [`b469fb3bfe`](https://github.com/NVIDIA/TensorRT-LLM/commit/b469fb3bfe) [#17228](https://github.com/NVIDIA/TensorRT-LLM/pull/17228)
  [https://nvbugs/6533913][docs] Update pinned container for GPT OSS (#17228)
  _Files: `docs/source/blogs/tech_blog/blog09_Deploying_GPT_OSS_on_TRTLLM.md`_
- **2026-08-04** [`f54798762e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f54798762e) [#17234](https://github.com/NVIDIA/TensorRT-LLM/pull/17234)
  [None][fix] Add opt-in pinned staging for weight-load H2D copies (#17234)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tensorrt_llm/_torch/pinned_weight_staging.py`, `tests/unittest/_torch/misc/test_pinned_weight_staging.py`_
- **2026-08-03** [`dbe6a41890`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbe6a41890) [#16809](https://github.com/NVIDIA/TensorRT-LLM/pull/16809)
  [TRTLLM-13694][perf] Refresh recipe configs from latest benchmark data (#16809)
  _Files: `docs/source/_static/config_db.json`, `examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp4_conc16.yaml`, `examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp4_conc8.yaml`, `examples/configs/database/deepseek-ai/DeepSeek-R1-0528/B200/1k1k_tp8_conc128.yaml` _+53 more__
- **2026-08-03** [`43edf6257b`](https://github.com/NVIDIA/TensorRT-LLM/commit/43edf6257b) [#16339](https://github.com/NVIDIA/TensorRT-LLM/pull/16339)
  [None][feat] Qwen-Image TeaCache/Cache-DiT Support (#16339)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/cache/cache_dit_accelerator.py`, `tensorrt_llm/_torch/visual_gen/cache/cache_dit_enablers.py` _+8 more__
- **2026-08-03** [`48a42a674a`](https://github.com/NVIDIA/TensorRT-LLM/commit/48a42a674a) [#17197](https://github.com/NVIDIA/TensorRT-LLM/pull/17197)
  [None][test] Update performance test configuration for qwen3 model to reduce request count from 256 to 64, optimizing resource usage during benchmarking (#17197)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Disaggregation / KV  (15 commits)

- **2026-08-10** [`67dd1b7ed8`](https://github.com/NVIDIA/TensorRT-LLM/commit/67dd1b7ed8) [#16942](https://github.com/NVIDIA/TensorRT-LLM/pull/16942)
  [None][feat] Opt GPT-OSS in to KV cache manager V2 by default (#16942)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tensorrt_llm/llmapi/llm_utils.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+1 more__
- **2026-08-08** [`4d02d80eaa`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d02d80eaa) [#17334](https://github.com/NVIDIA/TensorRT-LLM/pull/17334)
  [TRTLLM-14815][feat] Enable disaggregated serving for Kimi K3 (#17334)
  _Files: `examples/disaggregated/slurm/benchmark/run_benchmark.sh`, `examples/disaggregated/slurm/benchmark/start_server.sh`, `examples/disaggregated/slurm/benchmark/start_worker.sh`, `examples/disaggregated/slurm/cache_transceiver_test/configs/kda_payload_kimi_k3.yaml` _+21 more__
- **2026-08-07** [`9deec37606`](https://github.com/NVIDIA/TensorRT-LLM/commit/9deec37606) [#17360](https://github.com/NVIDIA/TensorRT-LLM/pull/17360)
  [None][feat] Default MiniMax M2 to KV cache manager V2 (#17360)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm2.py`_
- **2026-08-07** [`a9be9ecf23`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9be9ecf23) [#17125](https://github.com/NVIDIA/TensorRT-LLM/pull/17125)
  [None][feat] Default Kimi K2.5 to KV cache manager V2 (#17125)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`_
- **2026-08-07** [`1c4b569aed`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c4b569aed) [#17252](https://github.com/NVIDIA/TensorRT-LLM/pull/17252)
  [None][test] Remove selected GPT-OSS V1 KV cache tests from CI (#17252)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/qa/llm_function_rtx6k.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+2 more__
- **2026-08-07** [`33c6270c35`](https://github.com/NVIDIA/TensorRT-LLM/commit/33c6270c35) [#17397](https://github.com/NVIDIA/TensorRT-LLM/pull/17397)
  [https://nvbugs/6523520][fix] Halve gb200 r1-fp4 128k8k con128 multi_round to fit perf-sanity budget (#17397)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-08-07** [`e447b6c201`](https://github.com/NVIDIA/TensorRT-LLM/commit/e447b6c201) [#17389](https://github.com/NVIDIA/TensorRT-LLM/pull/17389)
  [None][test] Remove UCX cases on qa side (#17389)
  _Files: `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-UCX.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp1_ccb-UCX.yaml` _+12 more__
- **2026-08-07** [`706eca30f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/706eca30f5) [#16993](https://github.com/NVIDIA/TensorRT-LLM/pull/16993)
  [None][fix] Filter empty aux buffers from NIXL transfers (#16993)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/agentBindings.cpp`, `tensorrt_llm/_torch/disaggregation/native/auxiliary.py`, `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py` _+3 more__
- **2026-08-06** [`b7a9d6f5d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7a9d6f5d7) [#17163](https://github.com/NVIDIA/TensorRT-LLM/pull/17163)
  [None][fix] Drain in-flight requests before clearing the KV cache reuse state (#17163)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.h`, `tensorrt_llm/llmapi/rlhf_utils.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache_manager.py` _+1 more__
- **2026-08-04** [`e409c1469c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e409c1469c) [#16430](https://github.com/NVIDIA/TensorRT-LLM/pull/16430)
  [None][feat] make disaggregated server keep-alive timeout configurable (#16430)
  _Files: `docs/source/features/disagg-serving.md`, `examples/disaggregated/README.md`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/llmapi/disagg_utils.py` _+8 more__
- **2026-08-04** [`be935006cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/be935006cb) [#16693](https://github.com/NVIDIA/TensorRT-LLM/pull/16693)
  [None][chore] Remove unused server_endpoint field from RankInfo (#16693)
  _Files: `tensorrt_llm/_torch/disaggregation/native/rank_info.py`, `tests/unittest/disaggregated/region/test_block.py`, `tests/unittest/disaggregated/test_peer.py`, `tests/unittest/disaggregated/test_pool_matching.py` _+1 more__
- **2026-08-04** [`ad254e58bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad254e58bd) [#16883](https://github.com/NVIDIA/TensorRT-LLM/pull/16883)
  [None][feat] BREAKING Support saving last N turns in per-conversation policy (#16883)
  _Files: `docs/source/developer-guide/telemetry.md`, `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+9 more__
- **2026-08-04** [`2ff7e8b596`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ff7e8b596) [#16002](https://github.com/NVIDIA/TensorRT-LLM/pull/16002)
  [https://nvbugs/6003113][fix] BREAKING CHANGE: Authenticate disagg request to verify encoded_opaque_state and ctx_info_endpoint (#16002)
  _Files: `examples/disaggregated/README.md`, `examples/disaggregated/slurm/service_discovery_example/launch.slurm`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/commands/serve.py` _+20 more__
- **2026-08-03** [`aa535e5d41`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa535e5d41) [#16908](https://github.com/NVIDIA/TensorRT-LLM/pull/16908)
  [TRTLLM-13948][feat] Set DeepSeekV3 to use Python KV-cache transceiver V2 by default (#16908)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml` _+2 more__
- **2026-08-03** [`ef1e9f5f6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef1e9f5f6f) [#17099](https://github.com/NVIDIA/TensorRT-LLM/pull/17099)
  [None][test] Add back 1k1k cases for qa side (#17099)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1024_ctx1_dep4_gen1_dep32_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con3072_ctx1_dep4_gen1_dep4_eplb0_mtp1_ccb-NIXL.yaml` _+6 more__

## Torch Path (_torch)  (10 commits)

- **2026-08-10** [`685a6c0d5b`](https://github.com/NVIDIA/TensorRT-LLM/commit/685a6c0d5b) [#17003](https://github.com/NVIDIA/TensorRT-LLM/pull/17003)
  [TRTLLM-14798][perf] Fuse Wan DupUp3D output mapping (#17003)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/dup_up3d.py`, `tensorrt_llm/_torch/visual_gen/models/wan/wan_vae.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/visual_gen/test_wan_dup_up3d.py`_
- **2026-08-08** [`4c2a114f95`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c2a114f95) [#16162](https://github.com/NVIDIA/TensorRT-LLM/pull/16162)
  [None][feat] Add FastWan2.2 TI2V-5B DMD pipeline (3-step text-to-video) (#16162)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/wan/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/wan/defaults.py` _+9 more__
- **2026-08-06** [`8e588da4a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e588da4a2) [#17322](https://github.com/NVIDIA/TensorRT-LLM/pull/17322)
  [None][test] Run thop custom-op schema checks in the CPU pre-merge stage (#17322)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/thop/parallel_hw_agnostic/test_custom_ops.py`_
- **2026-08-06** [`f9b2457819`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9b2457819) [#17303](https://github.com/NVIDIA/TensorRT-LLM/pull/17303)
  [None][test] Adjust perf test cases to avoid OOM and remove outdated test cases (#17303)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-06** [`a993952764`](https://github.com/NVIDIA/TensorRT-LLM/commit/a993952764) [#16992](https://github.com/NVIDIA/TensorRT-LLM/pull/16992)
  [https://nvbugs/6327149][fix] Handle EXAONE 4.5 33B memory constraints (#16992)
  _Files: `tensorrt_llm/_torch/models/modeling_exaone4_5.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_exaone4_5.py`_
- **2026-08-05** [`5533f66328`](https://github.com/NVIDIA/TensorRT-LLM/commit/5533f66328) [#17302](https://github.com/NVIDIA/TensorRT-LLM/pull/17302)
  [https://nvbugs/6561547][fix] Change both fixtures from `scope="module"` to `scope="class"` so the ~84 GB is… (#17302)
  _Files: `tests/unittest/_torch/visual_gen/test_wan22_t2v_pipeline.py`_
- **2026-08-04** [`fe401c7bfa`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe401c7bfa) [#17002](https://github.com/NVIDIA/TensorRT-LLM/pull/17002)
  [TRTLLM-14554][perf] Batch Wan VAE decode along the temporal axis (#17002)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/parallel_vae.py`, `tensorrt_llm/_torch/visual_gen/models/wan/wan_vae.py`, `tests/unittest/_torch/visual_gen/test_wan_vae.py`_
- **2026-08-03** [`ac534c6d59`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac534c6d59) [#17212](https://github.com/NVIDIA/TensorRT-LLM/pull/17212)
  [https://nvbugs/6550708][fix] initialize profiler in Cosmos3 test fixture (#17212)
  _Files: `tests/unittest/_torch/visual_gen/test_cosmos3_distilled.py`_
- **2026-08-03** [`9cc292ce00`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cc292ce00) [#17047](https://github.com/NVIDIA/TensorRT-LLM/pull/17047)
  [None][test] add e2e key model perf test (#17047)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-03** [`64eae0800e`](https://github.com/NVIDIA/TensorRT-LLM/commit/64eae0800e) [#17049](https://github.com/NVIDIA/TensorRT-LLM/pull/17049)
  [https://nvbugs/6528742][test] Disable V2 in legacy Mamba test (#17049)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_

## Other  (7 commits)

- **2026-08-07** [`a6ea52f7ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6ea52f7ea) [#17390](https://github.com/NVIDIA/TensorRT-LLM/pull/17390)
  [None][test] Enable overlap schedule on qa side for disagg perf (#17390)
- **2026-08-06** [`aafc4ebf80`](https://github.com/NVIDIA/TensorRT-LLM/commit/aafc4ebf80) [#17183](https://github.com/NVIDIA/TensorRT-LLM/pull/17183)
  [None][test] Fix perf-core timeouts and 96G-part coverage for large-checkpoint cases (#17183)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-06** [`77bc7f012c`](https://github.com/NVIDIA/TensorRT-LLM/commit/77bc7f012c) [#17098](https://github.com/NVIDIA/TensorRT-LLM/pull/17098)
  [None][test] Enable warmup request for gen_only perf sanity lanes (#17098)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-08-06** [`1310036e0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/1310036e0a) [#17060](https://github.com/NVIDIA/TensorRT-LLM/pull/17060)
  [None][fix] Stop NVLink probe from throwing on out-of-range link indices (#17060)
  _Files: `tensorrt_llm/_mnnvl_utils.py`_
- **2026-08-05** [`9cb1a9208f`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cb1a9208f) [#17250](https://github.com/NVIDIA/TensorRT-LLM/pull/17250)
  [None][chore] Fix guardword (#17250)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp`_
- **2026-08-04** [`6db4f3425f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6db4f3425f) [#16848](https://github.com/NVIDIA/TensorRT-LLM/pull/16848)
  [None][fix] Update VisualGen test CODEOWNERS (#16848)
  _Files: `.github/CODEOWNERS`_
- **2026-08-03** [`37335543e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/37335543e6) [#17101](https://github.com/NVIDIA/TensorRT-LLM/pull/17101)
  [None][test] Add back new ctx and gen only case (#17101)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`_

## Quantization  (6 commits)

- **2026-08-10** [`0fa708be4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fa708be4e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-08-08** [`bbe28287d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbe28287d1) [#17093](https://github.com/NVIDIA/TensorRT-LLM/pull/17093)
  [None][perf] Fold q/k/v quantization into qknorm_rope_fused kernel & remove contiguous (#17093)
  _Files: `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedQKNormRopeOp.cpp`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+1 more__
- **2026-08-07** [`0ed138a09d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ed138a09d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+3 more__
- **2026-08-06** [`f12c5e58a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/f12c5e58a7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+7 more__
- **2026-08-06** [`0b650e655c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b650e655c) [#17301](https://github.com/NVIDIA/TensorRT-LLM/pull/17301)
  [https://nvbugs/5945081][fix] un-waive DeepSeek-V3-Lite NVFP4 pp4 CUTLASS test (#17301)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-05** [`220149c1c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/220149c1c0) [#16683](https://github.com/NVIDIA/TensorRT-LLM/pull/16683)
  [TRTLLM-14557][test] Add single-device visual-gen feature accuracy regression tests (#16683)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/examples/visual_gen/conftest.py`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_fp8_blockwise_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_nvfp4_lpips_golden.json` _+33 more__

## Speculative Decoding  (3 commits)

- **2026-08-08** [`d8b67db260`](https://github.com/NVIDIA/TensorRT-LLM/commit/d8b67db260) [#17082](https://github.com/NVIDIA/TensorRT-LLM/pull/17082)
  [TRTLLM-14708][fix] Populate speculative-decoding request perf metrics in the PyTorch one-engine flow (#17082)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/speculative/drafter.py` _+8 more__
- **2026-08-07** [`fb9d4720f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb9d4720f1) [#17361](https://github.com/NVIDIA/TensorRT-LLM/pull/17361)
  [None][fix] tolerate windowed-group speculative spill in disagg KV send (#17361)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_cache_reuse_adapter.py`_
- **2026-08-05** [`f1f773f6f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1f773f6f1) [#16072](https://github.com/NVIDIA/TensorRT-LLM/pull/16072)
  [TRTLLM-14138][fix] Pre-allocate CUDA graph padding dummy during warmup (#16072)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py` _+4 more__

## Docs / Examples  (3 commits)

- **2026-08-08** [`bcc0327185`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcc0327185) [#17076](https://github.com/NVIDIA/TensorRT-LLM/pull/17076)
  [https://nvbugs/6533914][docs] Fix trtllm-bench prepare-dataset: --tokenizer is not a valid global option (#17076)
  _Files: `docs/source/commands/trtllm-bench.rst`, `docs/source/legacy/performance/perf-benchmarking.md`, `tensorrt_llm/commands/bench.py`_
- **2026-08-06** [`1ddd407315`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ddd407315) [#17337](https://github.com/NVIDIA/TensorRT-LLM/pull/17337)
  [None][test] default the disagg cache-transceiver precheck to off (#17337)
  _Files: `tests/scripts/perf-sanity/cache_transceiver_precheck/README.md`, `tests/scripts/perf-sanity/cache_transceiver_precheck/precheck_config.py`, `tests/unittest/others/test_cache_transceiver_precheck_config.py`_
- **2026-08-03** [`1a00238748`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a00238748) [#17161](https://github.com/NVIDIA/TensorRT-LLM/pull/17161)
  [TRTLLM-14772][doc] Add sudo to apt prerequisites (#17161)
  _Files: `docs/source/installation/build-from-source.md`_

## AutoDeploy  (2 commits)

- **2026-08-09** [`a7e32703e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7e32703e7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+2 more__
- **2026-08-07** [`803ddeeeba`](https://github.com/NVIDIA/TensorRT-LLM/commit/803ddeeeba)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_

## Compilation / Graph  (1 commits)

- **2026-08-06** [`5048333f1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5048333f1a) [#17357](https://github.com/NVIDIA/TensorRT-LLM/pull/17357)
  [None][ci] Trigger multi-GPU tests for CUDA graph runner changes (#17357)
  _Files: `jenkins/L0_MergeRequest.groovy`_

## LoRA  (1 commits)

- **2026-08-06** [`08d6a856ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/08d6a856ab) [#17138](https://github.com/NVIDIA/TensorRT-LLM/pull/17138)
  [https://nvbugs/6265490][fix] Defer LoRA path validation (#17138)
  _Files: `tensorrt_llm/executor/request.py`, `tests/unittest/executor/test_base_worker.py`_

---
_Generated 2026-08-10 09:46 UTC_