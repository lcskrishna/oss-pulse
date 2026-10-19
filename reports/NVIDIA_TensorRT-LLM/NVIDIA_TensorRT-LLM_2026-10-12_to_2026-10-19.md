# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-10-12 → 2026-10-19  |  **Total commits:** 210

## ✨ New Features This Week

- **2026-10-19** [#20593](https://github.com/NVIDIA/TensorRT-LLM/pull/20593) — [None][test] Add coverage for Qwen3ForCausalLM (#20593)
- **2026-10-19** [#20432](https://github.com/NVIDIA/TensorRT-LLM/pull/20432) — [None][feat] Add spec_dec_variant to telemetry (#20432)
- **2026-10-17** [#19960](https://github.com/NVIDIA/TensorRT-LLM/pull/19960) — [None][feat] Kimi K3 optimizations on Rubin (#19960)
- **2026-10-16** [#19604](https://github.com/NVIDIA/TensorRT-LLM/pull/19604) — [None][feat] Add opt-in MiniMax-H3 sleep/wake support (#19604)
- **2026-10-16** [#20147](https://github.com/NVIDIA/TensorRT-LLM/pull/20147) — [TRTLLM-16780][feat] Honor per-request seeds in one-model speculative decoding's acceptance step (#20147)
- **2026-10-16** [#19546](https://github.com/NVIDIA/TensorRT-LLM/pull/19546) — [None][doc] Add MoE Performance Guide and Perf Dashboard (#19546)
- **2026-10-16** [#20461](https://github.com/NVIDIA/TensorRT-LLM/pull/20461) — [None][infra] Add blossom-ci authorized users (#20461)
- **2026-10-16** [#19894](https://github.com/NVIDIA/TensorRT-LLM/pull/19894) — [TRTLLMINF-439][infra] Add GR100 post-merge single-GPU stage (#19894)
- **2026-10-16** [#19713](https://github.com/NVIDIA/TensorRT-LLM/pull/19713) — [None][feat] VisualGen: token-sharded tensor parallelism (tp_layout) for Wan (#19713)
- **2026-10-16** [#19077](https://github.com/NVIDIA/TensorRT-LLM/pull/19077) — [None][feat] make KVCacheManagerV2 pool rebalancing parameters configurable (#19077)
- _…and 26 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-17** [`e88d19ca3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e88d19ca3b) [#19960](https://github.com/NVIDIA/TensorRT-LLM/pull/19960) — [None][feat] Kimi K3 optimizations on Rubin (#19960)
- **2026-10-15** [`7adc880405`](https://github.com/NVIDIA/TensorRT-LLM/commit/7adc880405) [#19387](https://github.com/NVIDIA/TensorRT-LLM/pull/19387) — [None][test] Validate Kimi default KVCM V2 accuracy and disaggregated transfer (#19387)
- **2026-10-14** [`30dc23ffe5`](https://github.com/NVIDIA/TensorRT-LLM/commit/30dc23ffe5) [#19987](https://github.com/NVIDIA/TensorRT-LLM/pull/19987) — [https://nvbugs/6812332][fix] Reshape the KDA decode fallback core to match prefill (#19987)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#19994](https://github.com/NVIDIA/TensorRT-LLM/issues/19994) | [Feature]: Whisper serving parity in trtllm-serve — /v1/audio/transcri | LLM API, OpenAI API | 2026-10-19 |
| [#20586](https://github.com/NVIDIA/TensorRT-LLM/issues/20586) | [Bug]: DeepSeek-V4.1 vision tower fails on SM107: cuDNN SDPA "No valid | Customized kernels, Pytorch | 2026-10-19 |
| [#20508](https://github.com/NVIDIA/TensorRT-LLM/issues/20508) | [Bug]: FP8 block-scale Linear hits a device-side assert on SM107: Deep | Customized kernels, Pytorch | 2026-10-17 |
| [#20504](https://github.com/NVIDIA/TensorRT-LLM/issues/20504) | [Bug]: Breakable prefill CUDA graphs replay corrupted outputs for some | Customized kernels | 2026-10-17 |
| [#20376](https://github.com/NVIDIA/TensorRT-LLM/issues/20376) | [Bug]: Grouped MLA generation cubins are registered as Dense in kernel | Customized kernels | 2026-10-15 |
| [#20407](https://github.com/NVIDIA/TensorRT-LLM/issues/20407) | [Feature]: Structured profiling metadata for distributed inference tra | feature request, Scale-out | 2026-10-15 |
| [#20237](https://github.com/NVIDIA/TensorRT-LLM/issues/20237) | [New Model]: Add pplx-decider support | feature request, new model | 2026-10-13 |
| [#20083](https://github.com/NVIDIA/TensorRT-LLM/issues/20083) | [Bug]: Ray orchestrator: NcclEP builds its EP communicator from MPI_CO | Inference runtime, Disaggregated serving | 2026-10-12 |
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
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-09-21 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 55 |
| Attention | 38 |
| MoE | 23 |
| Executor / Runtime | 19 |
| Quantization | 15 |
| Other | 13 |
| Disaggregation / KV | 12 |
| Torch Path (_torch) | 12 |
| Models | 7 |
| Speculative Decoding | 7 |
| ROCm / AMD | 3 |
| LoRA | 2 |
| Docs / Examples | 2 |
| Perf | 2 |

## CI / Infra  (55 commits)

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
- **2026-10-18** [`8e4f13322e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e4f13322e) [#20523](https://github.com/NVIDIA/TensorRT-LLM/pull/20523)
  [None][infra] Waive 1 failed cases for main in pre-merge 64813 (#20523)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-17** [`8b2ac2d08e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b2ac2d08e) [#20252](https://github.com/NVIDIA/TensorRT-LLM/pull/20252)
  [https://nvbugs/6919405][fix] Keep the 26.08 CUDA forward-compat driver on the 26.09 image (#20252)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `docker/common/install_cuda_compat.sh`, `jenkins/current_image_tags.properties`_
- **2026-10-17** [`347ca75662`](https://github.com/NVIDIA/TensorRT-LLM/commit/347ca75662) [#20505](https://github.com/NVIDIA/TensorRT-LLM/pull/20505)
  [None][infra] Waive 4 failed cases for main in pre-merge 64735 (#20505)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-17** [`20d5469559`](https://github.com/NVIDIA/TensorRT-LLM/commit/20d5469559) [#20418](https://github.com/NVIDIA/TensorRT-LLM/pull/20418)
  [https://nvbugs/6843484][fix] Keep multi-node aggregated perf-sanity jobs in one NVLink domain (#20418)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-17** [`acb83ac268`](https://github.com/NVIDIA/TensorRT-LLM/commit/acb83ac268) [#20135](https://github.com/NVIDIA/TensorRT-LLM/pull/20135)
  [TRTLLM-10804][infra] Run guardwords scan in nightly releases (#20135)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-17** [`700d9f4e29`](https://github.com/NVIDIA/TensorRT-LLM/commit/700d9f4e29)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-10-17** [`e5eedf3c9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5eedf3c9b) [#20500](https://github.com/NVIDIA/TensorRT-LLM/pull/20500)
  [None][infra] Waive 1 failed cases for main in pre-merge 64680 (#20500)
- **2026-10-17** [`3b54cd6e8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b54cd6e8f) [#20478](https://github.com/NVIDIA/TensorRT-LLM/pull/20478)
  [None][infra] Waive 1 failed cases for main in pre-merge 64667 (#20478)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-17** [`c962eddaa4`](https://github.com/NVIDIA/TensorRT-LLM/commit/c962eddaa4) [#20496](https://github.com/NVIDIA/TensorRT-LLM/pull/20496)
  [None][fix] disable bolt (#20496)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-16** [`625d654944`](https://github.com/NVIDIA/TensorRT-LLM/commit/625d654944)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-10-16** [`fc52f0adee`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc52f0adee)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-10-16** [`a857768f9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a857768f9f) [#20057](https://github.com/NVIDIA/TensorRT-LLM/pull/20057)
  [https://nvbugs/6811958][chore] Unwaive test_build_capture_manifest_matches_committed_golden (#20057)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-16** [`0404764530`](https://github.com/NVIDIA/TensorRT-LLM/commit/0404764530) [#18299](https://github.com/NVIDIA/TensorRT-LLM/pull/18299)
  [TRTLLM-15891][infra] Refactor CBTS Collection (#18299)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/__init__.py` _+73 more__
- **2026-10-16** [`426d357522`](https://github.com/NVIDIA/TensorRT-LLM/commit/426d357522) [#20457](https://github.com/NVIDIA/TensorRT-LLM/pull/20457)
  [https://nvbugs/6902353][chore] Waive test_transfer_lifecycle_gpu[destination_fatal] (#20457)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-16** [`7e4b83e588`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e4b83e588) [#20461](https://github.com/NVIDIA/TensorRT-LLM/pull/20461)
  [None][infra] Add blossom-ci authorized users (#20461)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-10-16** [`e95cdbdadc`](https://github.com/NVIDIA/TensorRT-LLM/commit/e95cdbdadc) [#19894](https://github.com/NVIDIA/TensorRT-LLM/pull/19894)
  [TRTLLMINF-439][infra] Add GR100 post-merge single-GPU stage (#19894)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_gr100.yml`_
- **2026-10-16** [`3f69cd26b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f69cd26b9)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`_
- **2026-10-16** [`9ec1bf3e58`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ec1bf3e58)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`_
- **2026-10-15** [`13e19d6cf3`](https://github.com/NVIDIA/TensorRT-LLM/commit/13e19d6cf3)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`_
- **2026-10-15** [`cb7bb1fb4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb7bb1fb4f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-10-15** [`3b082f8d0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b082f8d0f) [#20240](https://github.com/NVIDIA/TensorRT-LLM/pull/20240)
  [TRTLLMINF-486][infra] Get sonar-scanner-cli from internal Artifactory and verify its SHA-256 (#20240)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`_
- **2026-10-15** [`26927494ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/26927494ae)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-10-15** [`dac1641c60`](https://github.com/NVIDIA/TensorRT-LLM/commit/dac1641c60) [#20427](https://github.com/NVIDIA/TensorRT-LLM/pull/20427)
  [None][infra] Waive 1 failed cases for main in pre-merge 64375 (#20427)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-15** [`39372c40ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/39372c40ef) [#18353](https://github.com/NVIDIA/TensorRT-LLM/pull/18353)
  [TRTLLMINF-353][infra] skip test stages during maintenance (#18353)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/config/maintenance_stages.txt` _+1 more__
- **2026-10-15** [`65b82d9744`](https://github.com/NVIDIA/TensorRT-LLM/commit/65b82d9744) [#20153](https://github.com/NVIDIA/TensorRT-LLM/pull/20153)
  [TRTLLMINF-488][infra] Fix rerun junit reporting (#20153)
  _Files: `jenkins/scripts/test_rerun.py`, `tests/integration/defs/utils/periodic_junit.py`_
- **2026-10-14** [`9657c59188`](https://github.com/NVIDIA/TensorRT-LLM/commit/9657c59188) [#19562](https://github.com/NVIDIA/TensorRT-LLM/pull/19562)
  [None][infra] Reuse PLC pipeline result if commit not changed (#19562)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/find_plc_build.py`_
- **2026-10-14** [`02f5556523`](https://github.com/NVIDIA/TensorRT-LLM/commit/02f5556523) [#20304](https://github.com/NVIDIA/TensorRT-LLM/pull/20304)
  [None][infra] Waive 2 failed cases for main in pre-merge 64155 (#20304)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`5be7646849`](https://github.com/NVIDIA/TensorRT-LLM/commit/5be7646849) [#20302](https://github.com/NVIDIA/TensorRT-LLM/pull/20302)
  [None][infra] Waive 1 failed cases for main in pre-merge 64154 (#20302)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`0c40309906`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c40309906) [#20296](https://github.com/NVIDIA/TensorRT-LLM/pull/20296)
  [None][infra] Waive 2 failed cases for main in pre-merge 64127 (#20296)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`91404de7bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/91404de7bc) [#20042](https://github.com/NVIDIA/TensorRT-LLM/pull/20042)
  [None][fix] Enable VMM CUDA IPC in Kubernetes GPU CI (#20042)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`4643a6b36c`](https://github.com/NVIDIA/TensorRT-LLM/commit/4643a6b36c) [#19258](https://github.com/NVIDIA/TensorRT-LLM/pull/19258)
  [TRTLLMINF-381][fix] classify CI failures from originating step logs (#19258)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`, `tests/unittest/tools/test_infra_dry_run_pipeline.py`_
- **2026-10-14** [`5c7fc3c7d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c7fc3c7d6) [#19013](https://github.com/NVIDIA/TensorRT-LLM/pull/19013)
  [TRTLLM-16315][infra] relax CBTS import-time coverage bounds (#19013)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/coverage_selection/SELECTION.md`, `jenkins/scripts/cbts/coverage_selection/selector.py`, `jenkins/scripts/cbts/coverage_tier.py` _+7 more__
- **2026-10-14** [`32f9c4f5a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/32f9c4f5a6) [#20024](https://github.com/NVIDIA/TensorRT-LLM/pull/20024)
  [TRTLLMINF-336][fix] Stop emitting cortex-a53-843419 veneers in BOLT builds (#20024)
  _Files: `cpp/CMakeLists.txt`, `jenkins/L0_MergeRequest.groovy`, `scripts/bolt/apply_bolt.py`, `scripts/bolt/bolt_lib.sh` _+2 more__
- **2026-10-14** [`bfb4bcb013`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfb4bcb013)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-10-14** [`6785e36319`](https://github.com/NVIDIA/TensorRT-LLM/commit/6785e36319) [#20220](https://github.com/NVIDIA/TensorRT-LLM/pull/20220)
  [https://nvbugs/6911105][fix] Remove sparse metadata preparation waiver (#20220)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`f0f4fc4a5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0f4fc4a5e) [#20161](https://github.com/NVIDIA/TensorRT-LLM/pull/20161)
  [https://nvbugs/6852440][fix] Set constraint to fastapi version (#20161)
  _Files: `requirements.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-10-13** [`dce099d2ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/dce099d2ae)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-10-13** [`a9c05a59fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9c05a59fb)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-10-13** [`57c7691ccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/57c7691ccf) [#20235](https://github.com/NVIDIA/TensorRT-LLM/pull/20235)
  [https://nvbugs/6902353][chore] waive test_transfer_lifecycle_gpu (#20235)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-13** [`7d06892599`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d06892599) [#20198](https://github.com/NVIDIA/TensorRT-LLM/pull/20198)
  [https://nvbugs/6762594][test] Run VisualGen key padding mask parity test in CPU CI (#20198)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`_
- **2026-10-13** [`31c1a3f44d`](https://github.com/NVIDIA/TensorRT-LLM/commit/31c1a3f44d) [#20234](https://github.com/NVIDIA/TensorRT-LLM/pull/20234)
  [None][infra] Waive 8 failed cases for main in pre-merge 63914 (#20234)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-13** [`8e5644fb36`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e5644fb36) [#20219](https://github.com/NVIDIA/TensorRT-LLM/pull/20219)
  [None][infra] Waive 3 failed cases for main in pre-merge 63827 (#20219)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-13** [`fced9ff984`](https://github.com/NVIDIA/TensorRT-LLM/commit/fced9ff984) [#20118](https://github.com/NVIDIA/TensorRT-LLM/pull/20118)
  [None][infra] Waive 2 failed cases for main in post-merge 3014 (#20118)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-13** [`823851e1af`](https://github.com/NVIDIA/TensorRT-LLM/commit/823851e1af) [#20179](https://github.com/NVIDIA/TensorRT-LLM/pull/20179)
  [None][infra] Waive 2 failed cases for main in pre-merge 63757 (#20179)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-12** [`efeda44574`](https://github.com/NVIDIA/TensorRT-LLM/commit/efeda44574) [#20142](https://github.com/NVIDIA/TensorRT-LLM/pull/20142)
  [None][infra] Add TensorRT-LLM Release 1.4 section to release notes (#20142)
  _Files: `docs/source/release-notes.md`_
- **2026-10-12** [`760a584b9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/760a584b9a) [#20130](https://github.com/NVIDIA/TensorRT-LLM/pull/20130)
  [None][infra] Waive 1 failed cases for main in post-merge 3014 (#20130)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-12** [`1558ad7f8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/1558ad7f8b)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-10-12** [`7fe9683123`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fe9683123) [#20107](https://github.com/NVIDIA/TensorRT-LLM/pull/20107)
  [None][infra] Waive 1 failed cases for main in pre-merge 63586 (#20107)
  _Files: `tests/integration/test_lists/waives.txt`_

## Attention  (38 commits)

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
- **2026-10-18** [`729fb044e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/729fb044e5) [#20250](https://github.com/NVIDIA/TensorRT-LLM/pull/20250)
  [https://nvbugs/6919819][fix] Give non-attention-DP overlap runs the retiring-request seat headroom (#20250)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`, `tests/unittest/_torch/executor/test_seq_slot_sizing.py`_
- **2026-10-16** [`7ebcf4debc`](https://github.com/NVIDIA/TensorRT-LLM/commit/7ebcf4debc) [#19302](https://github.com/NVIDIA/TensorRT-LLM/pull/19302)
  [https://nvbugs/6713231][fix] Guard Whisper cross-KV reuse without encoder tokens (#19302)
  _Files: `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp`, `cpp/tests/unit_tests/batch_manager/capacitySchedulerTest.cpp`, `docs/source/models/encoder-decoder.md`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+6 more__
- **2026-10-16** [`dac84b01a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/dac84b01a6) [#20164](https://github.com/NVIDIA/TensorRT-LLM/pull/20164)
  [https://nvbugs/6900756][fix] Bound packed indexer prefill logits by grouping context requests (#20164)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/__init__.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-10-16** [`4dee061ea6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4dee061ea6) [#18599](https://github.com/NVIDIA/TensorRT-LLM/pull/18599)
  [https://nvbugs/6691772][fix] Update trtllm-gen fmha autotuner to enable 96 head MLA (#18599)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `examples/kimi_k3/disagg/README.md`, `examples/kimi_k3/disagg/benchmark_kimi_k3_dep16.yaml`, `examples/kimi_k3/disagg/ctx_config.yaml` _+8 more__
- **2026-10-16** [`bb1600f99a`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb1600f99a) [#20151](https://github.com/NVIDIA/TensorRT-LLM/pull/20151)
  [https://nvbugs/6836304][fix] Forward-port stale MPI worker env fix to main and unwaive multimodal tests (#20151)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_flashinfer_workspace.py`, `tests/unittest/llmapi/test_mpi_session.py` _+1 more__
- **2026-10-16** [`38dc88e996`](https://github.com/NVIDIA/TensorRT-LLM/commit/38dc88e996) [#19713](https://github.com/NVIDIA/TensorRT-LLM/pull/19713)
  [None][feat] VisualGen: token-sharded tensor parallelism (tp_layout) for Wan (#19713)
  _Files: `docs/source/models/visual-generation.md`, `jenkins/L0_MergeRequest.groovy`, `tensorrt_llm/_torch/visual_gen/attention/attention.py`, `tensorrt_llm/_torch/visual_gen/models/modeling.py` _+19 more__
- **2026-10-16** [`c4afddb48c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4afddb48c) [#20006](https://github.com/NVIDIA/TensorRT-LLM/pull/20006)
  [None][perf] primsTS dense bf16, qk-bf16/pv-fp8, fp8 fmha context bringup (#20006)
  _Files: `docs/source/features/visualgen-quantized-attention.md`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py`, `tensorrt_llm/_torch/attention/backends/fmha/interface.py`, `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py` _+8 more__
- **2026-10-16** [`4271011718`](https://github.com/NVIDIA/TensorRT-LLM/commit/4271011718) [#20159](https://github.com/NVIDIA/TensorRT-LLM/pull/20159)
  [TRTLLM-16992][perf] Use paged attention for MiniMax-M3 dense layers (#20159)
  _Files: `docs/source/deployment-guide/deployment-guide-for-minimax-m3-on-trtllm.md`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py` _+6 more__
- **2026-10-15** [`5e67a3d9a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e67a3d9a4) [#20239](https://github.com/NVIDIA/TensorRT-LLM/pull/20239)
  [None][infra] Reuse rank processes across visual_gen multi-GPU tests (#20239)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/visual_gen/multi_gpu/_visual_gen_dist_utils.py`, `tests/unittest/_torch/visual_gen/multi_gpu/_worker_pool.py`, `tests/unittest/_torch/visual_gen/multi_gpu/conftest.py` _+26 more__
- **2026-10-15** [`03748030c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/03748030c6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`_
- **2026-10-15** [`7dc9012cad`](https://github.com/NVIDIA/TensorRT-LLM/commit/7dc9012cad) [#20143](https://github.com/NVIDIA/TensorRT-LLM/pull/20143)
  [TRTLLM-16336][feat] Add the qwen4_exp modeling_v2 target for Qwen3.8-Flash-Next-NVFP4 (#20143)
- **2026-10-15** [`172b96d051`](https://github.com/NVIDIA/TensorRT-LLM/commit/172b96d051) [#20251](https://github.com/NVIDIA/TensorRT-LLM/pull/20251)
  [None][perf] Score only visible pools on BF16 tensor cores in the GLM-5.3-Flash indexer (#20251)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/kernels.py`, `tensorrt_llm/_torch/models/modeling_glm5_next.py`, `tests/unittest/_torch/attention/sparse/glm_kpool/test_kernels.py` _+1 more__
- **2026-10-15** [`69a455ae97`](https://github.com/NVIDIA/TensorRT-LLM/commit/69a455ae97) [#20097](https://github.com/NVIDIA/TensorRT-LLM/pull/20097)
  [None][test] Migrate attention fixtures and prims-ts validation to KV cache V2 (#20097)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/microbenchmarks/attention_perf/attention_perf_harness.py`, `tests/microbenchmarks/bench_fp4_mla_decode.py`, `tests/unittest/_torch/attention/backend_case.py` _+15 more__
- **2026-10-15** [`e87862cfc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/e87862cfc8) [#20256](https://github.com/NVIDIA/TensorRT-LLM/pull/20256)
  [https://nvbugs/6921137][fix] Fix CuTe MLA page-table batch bounds (#20256)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`d68ea55c12`](https://github.com/NVIDIA/TensorRT-LLM/commit/d68ea55c12) [#19974](https://github.com/NVIDIA/TensorRT-LLM/pull/19974)
  [None][perf] MiniMax-M3: remove the host overhead that made NVFP4 KV slower than FP8 (#19974)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/triton_sparse_decode.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/compilation/utils.py` _+6 more__
- **2026-10-14** [`519661ad32`](https://github.com/NVIDIA/TensorRT-LLM/commit/519661ad32) [#20215](https://github.com/NVIDIA/TensorRT-LLM/pull/20215)
  [TRTLLM-15864][chore] Add deprecated forwarding shims for the old VisualGen attention paths (#20215)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py`, `tensorrt_llm/_torch/visual_gen/modules/__init__.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+1 more__
- **2026-10-14** [`9fd8917839`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fd8917839) [#20062](https://github.com/NVIDIA/TensorRT-LLM/pull/20062)
  [None][fix] Fix SM120 DSA KV append crash on missing _cached_stride_factor (#20062)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa_flashinfer.py`_
- **2026-10-14** [`39ea47f971`](https://github.com/NVIDIA/TensorRT-LLM/commit/39ea47f971) [#19856](https://github.com/NVIDIA/TensorRT-LLM/pull/19856)
  [TRTLLM-16770][feat] Support LiLiCorr draft checkpoints in DFlash (#19856)
  _Files: `docs/source/features/speculative-decoding.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/models/modeling_lilicorr.py` _+6 more__
- **2026-10-14** [`c98b9765d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/c98b9765d8) [#19988](https://github.com/NVIDIA/TensorRT-LLM/pull/19988)
  [None][fix] Kimi K3 / KDA / MNNVL / DFlash: fixes for defects on main (#19988)
  _Files: `cpp/tensorrt_llm/common/lamportUtils.cuh`, `cpp/tensorrt_llm/kernels/communicationKernels/mnnvlAllreduceKernels.cu`, `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`, `cpp/tensorrt_llm/kernels/quantization.cu` _+33 more__
- **2026-10-14** [`f33e0e5fd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/f33e0e5fd5) [#20278](https://github.com/NVIDIA/TensorRT-LLM/pull/20278)
  [None][doc] Add KV cache compression tech blog (#20278)
  _Files: `README.md`, `docs/source/blogs/media/tech_blog30_disk_sweep.svg`, `docs/source/blogs/media/tech_blog30_framework.svg`, `docs/source/blogs/media/tech_blog30_hooks_flow.svg` _+16 more__
- **2026-10-14** [`57aef0357b`](https://github.com/NVIDIA/TensorRT-LLM/commit/57aef0357b) [#20214](https://github.com/NVIDIA/TensorRT-LLM/pull/20214)
  [TRTLLM-15864][chore] Consolidate the VisualGen attention domain under _torch/visual_gen/attention/ (#20214)
  _Files: `.github/CODEOWNERS`, `cpp/tensorrt_llm/thop/asyncUlyssesOp.cpp`, `docs/source/blogs/tech_blog/blog25_Scaling_Video_Generation_Across_NVL72_Rack_with_TensorRT-LLM.md`, `docs/source/features/visualgen-quantized-attention.md` _+73 more__
- **2026-10-14** [`095513baf3`](https://github.com/NVIDIA/TensorRT-LLM/commit/095513baf3) [#20218](https://github.com/NVIDIA/TensorRT-LLM/pull/20218)
  [TRTLLM-15863][feat] Export the Attention module-layer classes from _torch.attention lazily (#20218)
  _Files: `tensorrt_llm/_torch/attention/__init__.py`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_sparse_mla.py`, `tensorrt_llm/_torch/attention/backends/sparse/registry.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+1 more__
- **2026-10-14** [`b7aa5f8b26`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7aa5f8b26) [#20037](https://github.com/NVIDIA/TensorRT-LLM/pull/20037)
  [None][fix] Fix issues in the build system during reconfiguration (#20037)
  _Files: `3rdparty/CMakeLists.txt`, `3rdparty/README.md`, `3rdparty/patch_dependency.py`, `cpp/CMakeLists.txt` _+3 more__
- **2026-10-14** [`38e23b0793`](https://github.com/NVIDIA/TensorRT-LLM/commit/38e23b0793) [#20127](https://github.com/NVIDIA/TensorRT-LLM/pull/20127)
  [None][feat] Support NVFP4 GLM-5.3-Flash checkpoints (#20127)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/glm5_next_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_glm5_next.py`, `tests/unittest/_torch/modeling/test_glm5_next_contracts.py`_
- **2026-10-14** [`c169557c5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/c169557c5f) [#20096](https://github.com/NVIDIA/TensorRT-LLM/pull/20096)
  [None][test] Fix encoder-decoder replay fixtures and duration IDs (#20096)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/llmapi/test_llm_api_pytorch_bart.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_t5.py`, `tests/unittest/_torch/attention/test_attention.py` _+3 more__
- **2026-10-13** [`e440723f9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e440723f9f) [#20221](https://github.com/NVIDIA/TensorRT-LLM/pull/20221)
  [https://nvbugs/6891758][fix] Fence Helix all-to-all shared writes before async bulk copy (#20221)
  _Files: `cpp/tensorrt_llm/kernels/helixAllToAll.cu`, `tests/unittest/_torch/attention/test_helix_alltoall_fifo.py`_
- **2026-10-13** [`af4692075f`](https://github.com/NVIDIA/TensorRT-LLM/commit/af4692075f) [#20063](https://github.com/NVIDIA/TensorRT-LLM/pull/20063)
  [https://nvbugs/6762590][test] Run Qwen-Image VisualGen unit tests in CI (#20063)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/unittest/_torch/visual_gen/multi_gpu/test_qwen_image_attention_parallel.py`_
- **2026-10-13** [`3af95a0e99`](https://github.com/NVIDIA/TensorRT-LLM/commit/3af95a0e99) [#20203](https://github.com/NVIDIA/TensorRT-LLM/pull/20203)
  [https://nvbugs/6908030][test] Use IPv4 loopback for VisualGen test rendezvous (#20203)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_attn2d_attention.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_cosmos3_transformer_parallel.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_flux2_transformer_parallel.py` _+22 more__
- **2026-10-13** [`fca08032f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/fca08032f7) [#20155](https://github.com/NVIDIA/TensorRT-LLM/pull/20155)
  [None][chore] Refresh PrimTS vendor source onto FlashInfer main (#20155)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py`, `tensorrt_llm/_torch/attention/backends/prims_ts/__init__.py` _+50 more__
- **2026-10-12** [`8fb3037883`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fb3037883) [#20054](https://github.com/NVIDIA/TensorRT-LLM/pull/20054)
  [None][chore] Update trtllm-gen FMHA artifacts (#20054)
- **2026-10-12** [`afc1fa2744`](https://github.com/NVIDIA/TensorRT-LLM/commit/afc1fa2744) [#17495](https://github.com/NVIDIA/TensorRT-LLM/pull/17495)
  [None][feat] BREAKING: Default to KV cache manager V2 and Python transceiver (#17495)
  _Files: `examples/disaggregated/slurm/service_discovery_example/launch.slurm`, `examples/disaggregated/slurm/simple_example/ctx_extra-llm-api-config.yaml`, `examples/disaggregated/slurm/simple_example/gen_extra-llm-api-config.yaml`, `examples/dwdp/reproduce.py` _+80 more__
- **2026-10-12** [`9257aaefbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9257aaefbb) [#19338](https://github.com/NVIDIA/TensorRT-LLM/pull/19338)
  [None][feat] Upgrade Blackwell cuteDSL MLA kernel for packed q heads and compact input (#19338)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp16.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp8.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_helpers.py`_

## MoE  (23 commits)

- **2026-10-19** [`47de5e4c9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/47de5e4c9c) [#20390](https://github.com/NVIDIA/TensorRT-LLM/pull/20390)
  [None][perf] GLM-5.3-Flash C++ kernel speedups: vectorized FP8 1x128 quant and 288-expert router GEMM (#20390)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm_kernel.cuh`, `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`, `cpp/tensorrt_llm/thop/dsv3RouterGemmOp.cpp`, `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py` _+1 more__
- **2026-10-19** [`a3766d68f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3766d68f9) [#20134](https://github.com/NVIDIA/TensorRT-LLM/pull/20134)
  [TRTLLM-15766][refactor] Decouple decoder tests from private methods and split DecoderRunner by phase (#20134)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py` _+45 more__
- **2026-10-16** [`c226e2d77c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c226e2d77c) [#19867](https://github.com/NVIDIA/TensorRT-LLM/pull/19867)
  [None][chore] Remove is_first_draft dead code (#19867)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/speculative/eagle3.py` _+12 more__
- **2026-10-16** [`b519164514`](https://github.com/NVIDIA/TensorRT-LLM/commit/b519164514) [#20283](https://github.com/NVIDIA/TensorRT-LLM/pull/20283)
  [https://nvbugs/6902355][fix] Keep TopK rows in the DSA sparse MLA test KV pool (#20283)
  _Files: `tests/unittest/_torch/attention/sparse/dsa/test_dsa_sparse_mla.py`_
- **2026-10-16** [`a0835b3d4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0835b3d4f) [#19981](https://github.com/NVIDIA/TensorRT-LLM/pull/19981)
  [TRTLLM-16972][fix] Reclaim idle eager CUTLASS MoE workspace (#19981)
  _Files: `cpp/tensorrt_llm/thop/moe/cutlass/eagerMoeWorkspace.h`, `cpp/tensorrt_llm/thop/moe/cutlass/eagerMoeWorkspaceScope.h`, `cpp/tensorrt_llm/thop/moe/cutlass/moeOp.cpp`, `cpp/tests/unit_tests/thop/CMakeLists.txt` _+11 more__
- **2026-10-16** [`45a126a65b`](https://github.com/NVIDIA/TensorRT-LLM/commit/45a126a65b) [#19546](https://github.com/NVIDIA/TensorRT-LLM/pull/19546)
  [None][doc] Add MoE Performance Guide and Perf Dashboard (#19546)
  _Files: `docs/source/_ext/trtllm_moe_dashboard.py`, `docs/source/_static/moe-perf-dashboard/config.js`, `docs/source/_static/moe-perf-dashboard/data.js`, `docs/source/_static/moe_dashboard.css` _+6 more__
- **2026-10-16** [`0c1882b28b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c1882b28b) [#20290](https://github.com/NVIDIA/TensorRT-LLM/pull/20290)
  [None][fix] Reduce deterministic GVR V2 top-K overflow overhead (#20290)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_deterministic.py`_
- **2026-10-16** [`3d4c17ced8`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d4c17ced8) [#20277](https://github.com/NVIDIA/TensorRT-LLM/pull/20277)
  [https://nvbugs/6919819][perf] Autotune the CuTeDSL FC2 N tile again when the override is unset (#20277)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tests/unittest/_torch/moe/fused_moe/test_cutedsl_fc2_tuning.py`_
- **2026-10-15** [`ed87ab0b01`](https://github.com/NVIDIA/TensorRT-LLM/commit/ed87ab0b01) [#17410](https://github.com/NVIDIA/TensorRT-LLM/pull/17410)
  [TRTLLM-14146][fix] Correct CuteDSL MoE autotune routing inputs (#17410)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`_
- **2026-10-15** [`559b04e0e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/559b04e0e9) [#20205](https://github.com/NVIDIA/TensorRT-LLM/pull/20205)
  [None][chore] Remove ArrayView and use `std::span` instead (#20205)
  _Files: `cpp/CMakeLists.txt`, `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/common/arrayView.h`, `cpp/include/tensorrt_llm/executor/tensor.h` _+38 more__
- **2026-10-15** [`d955ed3028`](https://github.com/NVIDIA/TensorRT-LLM/commit/d955ed3028) [#20362](https://github.com/NVIDIA/TensorRT-LLM/pull/20362)
  [None][test] Patch moe_comm_serving_timeouts in the phase-selective warmup test (#20362)
  _Files: `tests/unittest/_torch/compilation/test_phase_selective_forward.py`_
- **2026-10-15** [`ff7ea92dfb`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff7ea92dfb) [#19959](https://github.com/NVIDIA/TensorRT-LLM/pull/19959)
  [None][fix] Rubin merge-back: correctness fixes (#19959)
  _Files: `cpp/tensorrt_llm/deep_ep/CMakeLists.txt`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/moe/communication/moeAlltoAllOp.cpp`, `cpp/tensorrt_llm/thop/moe/trtllmGen/fp4BlockScaleMoe.cpp` _+45 more__
- **2026-10-14** [`03a7b7f865`](https://github.com/NVIDIA/TensorRT-LLM/commit/03a7b7f865) [#20246](https://github.com/NVIDIA/TensorRT-LLM/pull/20246)
  [None][fix] Merge back #19593 from release/1.3: Make MoE communication timeouts follow the warmup phase (#20246)
  _Files: `3rdparty/CMakeLists.txt`, `3rdparty/fetch_content.json`, `3rdparty/patches/deep_ep_runtime_timeout.patch`, `3rdparty/patches/deepgemm_configurable_barrier_timeout.patch` _+20 more__
- **2026-10-14** [`8d09d17134`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d09d17134) [#19016](https://github.com/NVIDIA/TensorRT-LLM/pull/19016)
  [TRTLLM-16316][feat] Generalize Runtime Sleep/Wakeup for LLM and `trtllm-serve` (#19016)
  _Files: `docs/source/features/sleep-wakeup.md`, `docs/source/index.rst`, `tensorrt_llm/_torch/async_llm.py`, `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py` _+27 more__
- **2026-10-14** [`d44cfdae3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d44cfdae3f) [#20181](https://github.com/NVIDIA/TensorRT-LLM/pull/20181)
  [None][feat] CUTEDSL: switch the Rubin NVFP4 FC1 weight layout to gate16/up16 (#20181)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_gather_grouped_blockscaled_gemm_act_fusion.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_grouped_blockscaled_gemm_fused_fc12.py`, `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+2 more__
- **2026-10-13** [`3729107c0b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3729107c0b) [#19860](https://github.com/NVIDIA/TensorRT-LLM/pull/19860)
  [None][fix] Align GDN recurrent Q/K normalization with prefill (#19860)
  _Files: `tensorrt_llm/_torch/modules/fla/cached_replay.py`, `tensorrt_llm/_torch/modules/fla/fused_recurrent.py`, `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tests/unittest/_torch/modules/mamba/test_gdn_replay_recurrent.py`_
- **2026-10-13** [`b0f8dd0920`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0f8dd0920) [#20098](https://github.com/NVIDIA/TensorRT-LLM/pull/20098)
  [None][test] Migrate model and executor fixtures to KV cache manager V2 (#20098)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_h200.yml`, `tests/unittest/_torch/debugger/test_debugger_addon.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`, `tests/unittest/_torch/modeling/test_modeling_afmoe.py` _+14 more__
- **2026-10-13** [`42c1abfefb`](https://github.com/NVIDIA/TensorRT-LLM/commit/42c1abfefb) [#20081](https://github.com/NVIDIA/TensorRT-LLM/pull/20081)
  [None][fix] Restore routing-weight dtype after NcclEP dispatch (#20081)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/communication/nccl_ep.py`, `tests/unittest/_torch/moe/test_moe_comm.py`_
- **2026-10-13** [`b22283a1b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/b22283a1b6) [#20100](https://github.com/NVIDIA/TensorRT-LLM/pull/20100)
  [None][feat] Deterministic mode for the self-sampling GVR V2 top-K decode (fp32) (#20100)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/params.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py` _+5 more__
- **2026-10-12** [`2647f76a1b`](https://github.com/NVIDIA/TensorRT-LLM/commit/2647f76a1b) [#20123](https://github.com/NVIDIA/TensorRT-LLM/pull/20123)
  [None][fix] bench_moe: release each candidate's MoE module before next one (#20123)
  _Files: `tests/microbenchmarks/bench_moe/case_runner.py`_
- **2026-10-12** [`371d5d0bc4`](https://github.com/NVIDIA/TensorRT-LLM/commit/371d5d0bc4) [#19488](https://github.com/NVIDIA/TensorRT-LLM/pull/19488)
  [None][chore] enable cutedsl rubin fc1 swiglu clamp (#19488)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_gather_grouped_blockscaled_gemm_act_fusion.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`, `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`_
- **2026-10-12** [`a4390ca755`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4390ca755) [#19610](https://github.com/NVIDIA/TensorRT-LLM/pull/19610)
  [None][refactor] overhaul NVLink one-sided all-to-all (#19610)
  _Files: `.claude/skills/trtllm-moe-develop/SKILL.md`, `.claude/skills/trtllm-moe-develop/references/moe-canonical-code-examples.md`, `.pre-commit-config.yaml`, `cpp/tensorrt_llm/common/envUtils.cpp` _+49 more__
- **2026-10-12** [`e67c26201a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e67c26201a) [#19272](https://github.com/NVIDIA/TensorRT-LLM/pull/19272)
  [None][feat] Wire Rubin locality-domain execution through PyTorch models (#19272)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+30 more__

## Executor / Runtime  (19 commits)

- **2026-10-19** [`df28262e26`](https://github.com/NVIDIA/TensorRT-LLM/commit/df28262e26) [#20442](https://github.com/NVIDIA/TensorRT-LLM/pull/20442)
  [None][fix] Keep MiniMax-M3 streaming and non-streaming reasoning parsing in step (#20442)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_
- **2026-10-17** [`2f5bb049f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f5bb049f3) [#20424](https://github.com/NVIDIA/TensorRT-LLM/pull/20424)
  [https://nvbugs/6713424][fix] Flush the HF streaming detokenizer on the final response; fix the AgentX aiperf install check (#20424)
  _Files: `tensorrt_llm/_torch/models/checkpoints/mistral/tokenizer.py`, `tensorrt_llm/tokenizer/tokenizer.py`, `tests/integration/defs/perf/agentx_client.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+2 more__
- **2026-10-16** [`e8bf8b09a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8bf8b09a0) [#19986](https://github.com/NVIDIA/TensorRT-LLM/pull/19986)
  [TRTLLM-16619][doc] Remove stale execution backend guidance (#19986)
  _Files: `docs/source/commands/trtllm-serve/run-benchmark-with-trtllm-serve.md`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `examples/README.md`, `examples/longbench/README.md` _+5 more__
- **2026-10-16** [`3ac4e61255`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ac4e61255) [#20453](https://github.com/NVIDIA/TensorRT-LLM/pull/20453)
  [https://nvbugs/6893965][fix] Extend disagg server start timeout in multi-node disagg test (#20453)
  _Files: `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes.py`, `tests/unittest/llmapi/apps/openai_server.py`_
- **2026-10-15** [`26756f2a81`](https://github.com/NVIDIA/TensorRT-LLM/commit/26756f2a81) [#20399](https://github.com/NVIDIA/TensorRT-LLM/pull/20399)
  [https://nvbugs/6800223][fix] Fix stale KvCacheCreator fixtures in budget split tests (#20399)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_budget_split.py`_
- **2026-10-15** [`7c03f0e8d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c03f0e8d1) [#19906](https://github.com/NVIDIA/TensorRT-LLM/pull/19906)
  [None][feat] Publish serving configuration schemas (#19906)
  _Files: `.gitattributes`, `AGENTS.md`, `docker/Dockerfile.multi`, `docs/source/_ext/trtllm_schema_assets.py` _+16 more__
- **2026-10-15** [`4290a08bd4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4290a08bd4) [#20191](https://github.com/NVIDIA/TensorRT-LLM/pull/20191)
  [TRTLLM-16460][fix] deepseek_v4 tokenizer: do not deep-copy the OpenAI server's pending media loads (#20191)
  _Files: `tensorrt_llm/tokenizer/deepseek_v4/tokenizer.py`, `tests/unittest/llmapi/test_deepseek_v4_tokenizer.py`_
- **2026-10-15** [`0a594e29e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a594e29e4) [#19967](https://github.com/NVIDIA/TensorRT-LLM/pull/19967)
  [TRTLLM-16628][refactor] BREAKING: Remove unused LlmRequest fields (#19967)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `cpp/tensorrt_llm/nanobind/bindings.cpp`, `cpp/tests/unit_tests/batch_manager/agentTreeTest.cpp` _+4 more__
- **2026-10-15** [`a77de9e3bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/a77de9e3bf) [#20030](https://github.com/NVIDIA/TensorRT-LLM/pull/20030)
  [https://nvbugs/6650817][fix] Drive MPI progress from a native thread on PP ranks (#20030)
  _Files: `cpp/include/tensorrt_llm/runtime/utils/mpiUtils.h`, `cpp/tensorrt_llm/nanobind/bindings.cpp`, `cpp/tensorrt_llm/runtime/utils/mpiUtils.cpp`, `tensorrt_llm/_torch/pyexecutor/pp_utils.py` _+3 more__
- **2026-10-14** [`701772a14d`](https://github.com/NVIDIA/TensorRT-LLM/commit/701772a14d) [#20244](https://github.com/NVIDIA/TensorRT-LLM/pull/20244)
  [None][perf] Cut per-response overhead in the LLM API streaming result path (#20244)
  _Files: `tensorrt_llm/_utils.py`, `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/result.py`, `tests/unittest/llmapi/test_executor.py`_
- **2026-10-14** [`7c44c537ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c44c537ac) [#18366](https://github.com/NVIDIA/TensorRT-LLM/pull/18366)
  [TRTLLM-16012][feat] Restrict torch.compile to piecewise graph capture only (#18366)
  _Files: `docs/source/features/torch_compile_and_piecewise_cuda_graph.md`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/config.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+7 more__
- **2026-10-14** [`2442169f07`](https://github.com/NVIDIA/TensorRT-LLM/commit/2442169f07) [#19440](https://github.com/NVIDIA/TensorRT-LLM/pull/19440)
  [None][feat] Stream native KV events and expose routing load (#19440)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_events.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_load.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+30 more__
- **2026-10-14** [`41bfd1da2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/41bfd1da2f) [#20175](https://github.com/NVIDIA/TensorRT-LLM/pull/20175)
  [None][infra] Vulnerability fix (#20175)
  _Files: `constraints.txt`, `docker/common/install_etcd.sh`, `jenkins/current_image_tags.properties`, `requirements.txt` _+3 more__
- **2026-10-13** [`bde219f642`](https://github.com/NVIDIA/TensorRT-LLM/commit/bde219f642) [#18897](https://github.com/NVIDIA/TensorRT-LLM/pull/18897)
  [TRTLLM-16212][feat] Unified caching via TRTLLM_CACHE_DIR environment variable (#18897)
  _Files: `docs/source/llm-api/index.md`, `examples/models/core/deepseek_v3/README.md`, `tensorrt_llm/__init__.py`, `tensorrt_llm/_bootstrap.py` _+7 more__
- **2026-10-13** [`819441c60f`](https://github.com/NVIDIA/TensorRT-LLM/commit/819441c60f) [#20189](https://github.com/NVIDIA/TensorRT-LLM/pull/20189)
  [https://nvbugs/6812588][fix] Apply the cluster UCX rules in multi-node disagg tests (#20189)
  _Files: `jenkins/scripts/perf/cluster_env.py`, `tests/integration/test_lists/waives.txt`, `tests/test_common/cluster_env.py`, `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes.py` _+2 more__
- **2026-10-13** [`8c339ee74d`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c339ee74d) [#20177](https://github.com/NVIDIA/TensorRT-LLM/pull/20177)
  [None][fix] Set use_kv_cache_manager_v2="auto" in required-V2 resolution tests (#20177)
  _Files: `tests/unittest/llmapi/test_llm_args.py`_
- **2026-10-13** [`9176cc8b76`](https://github.com/NVIDIA/TensorRT-LLM/commit/9176cc8b76) [#19886](https://github.com/NVIDIA/TensorRT-LLM/pull/19886)
  [None][refactor] Component-local C++ Tests (#19886)
  _Files: `AGENTS.md`, `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/common/CMakeLists.txt`, `cpp/tensorrt_llm/executor/CMakeLists.txt` _+9 more__
- **2026-10-13** [`3aef97c511`](https://github.com/NVIDIA/TensorRT-LLM/commit/3aef97c511) [#20158](https://github.com/NVIDIA/TensorRT-LLM/pull/20158)
  [https://nvbugs/6891541][fix] Stop the stats RPC server on GenerationExecutorWorker shutdown (#20158)
  _Files: `tensorrt_llm/executor/worker.py`_
- **2026-10-12** [`9cb84a22bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cb84a22bb) [#18310](https://github.com/NVIDIA/TensorRT-LLM/pull/18310)
  [https://nvbugs/6661863][fix] Allocate one `PyMem_RawCalloc`'d `_DLPackBlock` (managed tensor + inline… (#18310)
  _Files: `tensorrt_llm/_dlpack_utils.py`, `tensorrt_llm/executor/proxy.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/waives.txt` _+2 more__

## Quantization  (15 commits)

- **2026-10-19** [`d4624cb517`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4624cb517)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+6 more__
- **2026-10-18** [`1dcd5eacf4`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dcd5eacf4)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+5 more__
- **2026-10-16** [`df4b424b00`](https://github.com/NVIDIA/TensorRT-LLM/commit/df4b424b00)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/jenkins/scripts/cbts/poetry.lock` _+5 more__
- **2026-10-16** [`778c6c1b1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/778c6c1b1a) [#20403](https://github.com/NVIDIA/TensorRT-LLM/pull/20403)
  [https://nvbugs/6926547][fix] Route FLUX.2 linear_in quantization sca… (#20403)
  _Files: `tensorrt_llm/_torch/visual_gen/models/flux/transformer_flux2.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/visual_gen/test_flux2_load_weights.py`_
- **2026-10-16** [`c264cd1823`](https://github.com/NVIDIA/TensorRT-LLM/commit/c264cd1823) [#20204](https://github.com/NVIDIA/TensorRT-LLM/pull/20204)
  [None][fix] Enable SM107 NVFP4 CuTe DSL dispatch (#20204)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tests/unittest/_torch/thop/parallel/test_fp4_linear.py`_
- **2026-10-15** [`a6142c9209`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6142c9209)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+3 more__
- **2026-10-15** [`8ef998b7cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ef998b7cc) [#20282](https://github.com/NVIDIA/TensorRT-LLM/pull/20282)
  [https://nvbugs/6878353][test] Unwaive DeepSeekV3Lite nvfp4 tp4 torch_compile test on DGX_B300 (#20282)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-15** [`eb745f8501`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb745f8501) [#20271](https://github.com/NVIDIA/TensorRT-LLM/pull/20271)
  [https://nvbugs/6905381][fix] Fix CUDA-core GEMM launch for wide FP8 outputs (#20271)
  _Files: `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemm.cu`, `cpp/tests/unit_tests/kernels/cudaCoreGemm/cudaCoreGemmKernelTest.cpp`_
- **2026-10-14** [`c581a16227`](https://github.com/NVIDIA/TensorRT-LLM/commit/c581a16227)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-10-14** [`800f991cb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/800f991cb0) [#20131](https://github.com/NVIDIA/TensorRT-LLM/pull/20131)
  [None][chore] Remove permanently skipped DeepSeek-V3-Lite CUTEDSL FP8 tests (#20131)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-10-14** [`681cff123b`](https://github.com/NVIDIA/TensorRT-LLM/commit/681cff123b) [#20046](https://github.com/NVIDIA/TensorRT-LLM/pull/20046)
  [None][test] Migrate Nemotron and Mamba validation to KV cache V2 (#20046)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_mamba_bs1_concurrency2.yaml`, `tests/integration/test_lists/qa/llm_function_core.txt` _+3 more__
- **2026-10-14** [`f9637256af`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9637256af) [#20071](https://github.com/NVIDIA/TensorRT-LLM/pull/20071)
  [TRTLLM-14620][feat] Integrate calibrated DSpark confidence scoring (#20071)
  _Files: `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/models/modeling_dspark_v41.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/speculative/dspark.py` _+9 more__
- **2026-10-13** [`9515ea8854`](https://github.com/NVIDIA/TensorRT-LLM/commit/9515ea8854)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+4 more__
- **2026-10-12** [`d7882af43f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7882af43f) [#20077](https://github.com/NVIDIA/TensorRT-LLM/pull/20077)
  [TRTLLM-16956][feat] Modeling V2 dynamic switch with LLM config and args (#20077)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/modeling_v2_rule.py`, `tensorrt_llm/_torch/_experimental/__init__.py` _+22 more__
- **2026-10-12** [`f11628197f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f11628197f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__

## Other  (13 commits)

- **2026-10-19** [`335e0b1057`](https://github.com/NVIDIA/TensorRT-LLM/commit/335e0b1057) [#19980](https://github.com/NVIDIA/TensorRT-LLM/pull/19980)
  [None][chore] Sync Claude Code agents and skills from trtllm-agent-toolkit (#19980)
- **2026-10-16** [`2df58914a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/2df58914a1) [#20420](https://github.com/NVIDIA/TensorRT-LLM/pull/20420)
  [https://nvbugs/6913517][fix] Drop launcher spawn-proxy env in the disagg cancel marathon (#20420)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/test_disagg_cancel_stress.py`_
- **2026-10-16** [`6544bcd91a`](https://github.com/NVIDIA/TensorRT-LLM/commit/6544bcd91a) [#20294](https://github.com/NVIDIA/TensorRT-LLM/pull/20294)
  [None][test] Exclude Inductor subproc threads from integration threadleak check (#20294)
  _Files: `tests/integration/defs/pytest.ini`_
- **2026-10-15** [`c9b18eefa7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9b18eefa7) [#20121](https://github.com/NVIDIA/TensorRT-LLM/pull/20121)
  [None][fix] Restrict large-model four-GPU perf cases to VR200 (#20121)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-10-15** [`e30418f343`](https://github.com/NVIDIA/TensorRT-LLM/commit/e30418f343) [#20190](https://github.com/NVIDIA/TensorRT-LLM/pull/20190)
  [TRTLLM-16460][fix] indexer K-cache gather/scatter: compute the contiguous-side offset in 64 bits (#20190)
  _Files: `cpp/tensorrt_llm/kernels/indexerKCacheGather.cu`, `cpp/tensorrt_llm/kernels/indexerKCacheScatter.cu`_
- **2026-10-15** [`bb18d369b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb18d369b5) [#20305](https://github.com/NVIDIA/TensorRT-LLM/pull/20305)
  [None][test] Add a timeout to the subprocess.run call in test_bolt (#20305)
  _Files: `tests/unittest/scripts/test_bolt.py`_
- **2026-10-14** [`91c9b6d1cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/91c9b6d1cc) [#20274](https://github.com/NVIDIA/TensorRT-LLM/pull/20274)
  [None][test] Drop fastapi upper-bound assertion from web framework security floors test (#20274)
  _Files: `tests/unittest/others/test_web_dependency_security.py`_
- **2026-10-13** [`eef4a51043`](https://github.com/NVIDIA/TensorRT-LLM/commit/eef4a51043) [#17733](https://github.com/NVIDIA/TensorRT-LLM/pull/17733)
  [None][fix] raise clear error for prompt file with no usable prompts (#17733)
  _Files: `tensorrt_llm/bench/benchmark/visual_gen_utils.py`_
- **2026-10-13** [`d4658506ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4658506ba) [#19739](https://github.com/NVIDIA/TensorRT-LLM/pull/19739)
  [TRTLLM-16602][fix] Make the waiting-for-feedback stale PR lifecycle bot-aware (#19739)
  _Files: `.github/scripts/stale_pr_feedback.js`, `.github/scripts/stale_pr_feedback.test.js`, `.github/workflows/auto-close-inactive-issues.yml`, `.github/workflows/stale-pr-feedback-tests.yml`_
- **2026-10-13** [`92ba55a216`](https://github.com/NVIDIA/TensorRT-LLM/commit/92ba55a216) [#19977](https://github.com/NVIDIA/TensorRT-LLM/pull/19977)
  [TRTLLM-16304][feat] Upgrade the infrastructure of modeling V2 (#19977)
- **2026-10-12** [`7895a682da`](https://github.com/NVIDIA/TensorRT-LLM/commit/7895a682da) [#20150](https://github.com/NVIDIA/TensorRT-LLM/pull/20150)
  [None][test] Split QA test lists by GPU marker requirements (#20150)
  _Files: `scripts/split_qa_by_gpu.py`, `tests/unittest/scripts/test_split_qa_by_gpu.py`_
- **2026-10-12** [`4f442e50a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f442e50a5) [#19809](https://github.com/NVIDIA/TensorRT-LLM/pull/19809)
  [https://nvbugs/6838020][fix] Tolerate near-tie greedy flips in KV pool rebalance accuracy test (#19809)
  _Files: `tests/integration/defs/accuracy/test_kv_pool_rebalance_accuracy.py`_
- **2026-10-12** [`aaf3e07c1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaf3e07c1e) [#20148](https://github.com/NVIDIA/TensorRT-LLM/pull/20148)
  [TRTLLMINF-481][fix] handle outdated unresolved review threads (#20148)
  _Files: `.github/workflows/full-premerge-approval-signal.yml`, `.github/workflows/full-premerge-approval.yml`_

## Disaggregation / KV  (12 commits)

- **2026-10-19** [`51ef11b73c`](https://github.com/NVIDIA/TensorRT-LLM/commit/51ef11b73c) [#20140](https://github.com/NVIDIA/TensorRT-LLM/pull/20140)
  [https://nvbugs/6899682][fix] Isolate disaggregated client outputs per test (#20140)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_
- **2026-10-16** [`84f14da455`](https://github.com/NVIDIA/TensorRT-LLM/commit/84f14da455) [#20031](https://github.com/NVIDIA/TensorRT-LLM/pull/20031)
  [https://nvbugs/6836097][test] Restrict UCX TCP to loopback in single-node disagg tests (#20031)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-16** [`9e8e5a270e`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e8e5a270e) [#20032](https://github.com/NVIDIA/TensorRT-LLM/pull/20032)
  [https://nvbugs/6888251][test] Disable THP for KV cache V2 host tiers in disagg tests (#20032)
  _Files: `tests/integration/defs/disaggregated/disagg_test_utils.py`_
- **2026-10-16** [`2e9c7c378f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e9c7c378f) [#19077](https://github.com/NVIDIA/TensorRT-LLM/pull/19077)
  [None][feat] make KVCacheManagerV2 pool rebalancing parameters configurable (#19077)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp` _+12 more__
- **2026-10-15** [`097d2adf4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/097d2adf4a) [#19940](https://github.com/NVIDIA/TensorRT-LLM/pull/19940)
  [None][perf] Do not block the executor on KV bounce recv-region backp… (#19940)
  _Files: `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py`, `tests/unittest/disaggregated/test_bounce.py`_
- **2026-10-15** [`306a8a7c30`](https://github.com/NVIDIA/TensorRT-LLM/commit/306a8a7c30) [#19492](https://github.com/NVIDIA/TensorRT-LLM/pull/19492)
  [https://nvbugs/6728119][fix] Keep NCCL off PCIe P2P in disagg tests on pre-Hopper nodes (#19492)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-14** [`f1ac7fd530`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1ac7fd530) [#20050](https://github.com/NVIDIA/TensorRT-LLM/pull/20050)
  [None][test] Migrate ordinary disaggregated coverage to KV cache manager V2 (#20050)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+6 more__
- **2026-10-14** [`5f2e6cdc8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f2e6cdc8b) [#19722](https://github.com/NVIDIA/TensorRT-LLM/pull/19722)
  [TRTLLM-16186][feat] Add KV cache lending API for transfer backends (#19722)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/sharing/__init__.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/sharing/_fetch_ledger.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/sharing/_identity.py` _+25 more__
- **2026-10-13** [`8cf7f19d28`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cf7f19d28) [#20122](https://github.com/NVIDIA/TensorRT-LLM/pull/20122)
  [https://nvbugs/6877253][fix] Disagg MTP KVCache Transfer AL Test (#20122)
  _Files: `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_h200.yml` _+1 more__
- **2026-10-12** [`ca3a6c4c62`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca3a6c4c62) [#20093](https://github.com/NVIDIA/TensorRT-LLM/pull/20093)
  [None][feat] Let a model require KV cache manager v2 instead of being demoted to v1 (#20093)
  _Files: `tensorrt_llm/llmapi/llm_utils.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-10-12** [`a8d7911bed`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8d7911bed) [#19857](https://github.com/NVIDIA/TensorRT-LLM/pull/19857)
  [https://nvbugs/6865617][fix] Poll the disagg gen-init KV receive fence instead of blocking the overlap scheduler (#19857)
  _Files: `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/disaggregation/coordinator_harness.py` _+2 more__
- **2026-10-12** [`caed3b4e67`](https://github.com/NVIDIA/TensorRT-LLM/commit/caed3b4e67) [#19928](https://github.com/NVIDIA/TensorRT-LLM/pull/19928)
  [https://nvbugs/6818106][fix] Compare disaggregated logprobs on the KV reuse path (#19928)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_

## Torch Path (_torch)  (12 commits)

- **2026-10-16** [`060a2554b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/060a2554b9) [#19604](https://github.com/NVIDIA/TensorRT-LLM/pull/19604)
  [None][feat] Add opt-in MiniMax-H3 sleep/wake support (#19604)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/pipeline_minimax_h3.py`, `tensorrt_llm/_torch/visual_gen/pipeline.py`, `tensorrt_llm/_torch/visual_gen/pipeline_loader.py` _+8 more__
- **2026-10-16** [`e921fa39b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/e921fa39b0) [#20350](https://github.com/NVIDIA/TensorRT-LLM/pull/20350)
  [https://nvbugs/6920456][fix] Describe PyTorch as the sole execution backend in the architecture overview (#20350)
  _Files: `docs/source/torch/arch_overview.md`_
- **2026-10-15** [`9ae867c757`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ae867c757) [#20281](https://github.com/NVIDIA/TensorRT-LLM/pull/20281)
  [TRTLLM-10804][doc] Document NGC PyTorch wheel installation (#20281)
  _Files: `docs/source/installation/installation-guide.md`_
- **2026-10-14** [`783136904c`](https://github.com/NVIDIA/TensorRT-LLM/commit/783136904c) [#15772](https://github.com/NVIDIA/TensorRT-LLM/pull/15772)
  [TRTLLM-12288][feat] revert all the changes of the PR#14775 (#15772)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+1 more__
- **2026-10-14** [`5ee2f5f96f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ee2f5f96f) [#20004](https://github.com/NVIDIA/TensorRT-LLM/pull/20004)
  [https://nvbugs/6762593][fix] Add untracked Wan test files to CI test lists (#20004)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/unittest/_torch/visual_gen/test_wan_i2v_reference_conditioning.py`_
- **2026-10-14** [`4b128c5e57`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b128c5e57) [#19772](https://github.com/NVIDIA/TensorRT-LLM/pull/19772)
  [None][perf] Fuse MiniMax-H3 AdaLN RMSNorm with per-token modulation (#19772)
  _Files: `tensorrt_llm/_torch/visual_gen/models/minimax_h3/fused_adaln.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/transformer_minimax_h3.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/visual_gen/test_minimax_h3_fused_adaln.py` _+1 more__
- **2026-10-13** [`da676ffb8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/da676ffb8b) [#18561](https://github.com/NVIDIA/TensorRT-LLM/pull/18561)
  [TRTLLM-16104][test] Add ModelExpress post-merge accuracy canaries (#18561)
  _Files: `docs/source/features/model-express.md`, `jenkins/L0_Test.groovy`, `tests/integration/defs/model_express/mx_e2e_worker.py`, `tests/integration/defs/model_express/mx_harness.py` _+4 more__
- **2026-10-13** [`4e564a0acc`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e564a0acc) [#19862](https://github.com/NVIDIA/TensorRT-LLM/pull/19862)
  [None][infra] switch mirrors from URM to PDX (#19862)
  _Files: `docker/Dockerfile.multi`, `docker/common/install_base.sh`, `docker/common/install_mpi4py.sh`, `docker/common/install_nixl.sh` _+9 more__
- **2026-10-13** [`eaefddcecd`](https://github.com/NVIDIA/TensorRT-LLM/commit/eaefddcecd) [#19859](https://github.com/NVIDIA/TensorRT-LLM/pull/19859)
  [None][fix] Preserve indexed GDN state during Triton autotuning (#19859)
  _Files: `tensorrt_llm/_torch/modules/fla/chunk_delta_h.py`, `tests/unittest/_torch/modules/mamba/test_chunk_gdn_autotune.py`_
- **2026-10-13** [`30917618fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/30917618fb) [#19799](https://github.com/NVIDIA/TensorRT-LLM/pull/19799)
  [None][perf] reduce multimodal encoder output copies (#19799)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tests/unittest/_torch/multimodal/test_encoder_group.py`, `tests/unittest/_torch/multimodal/test_multimodal_mixin.py`_
- **2026-10-13** [`945657ee69`](https://github.com/NVIDIA/TensorRT-LLM/commit/945657ee69) [#19774](https://github.com/NVIDIA/TensorRT-LLM/pull/19774)
  [None][perf] Speed up MiniMax-H3 video-VAE decode losslessly (#19774)
  _Files: `tensorrt_llm/_torch/visual_gen/models/minimax_h3/parallel_vae.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/pipeline_minimax_h3.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/integration/defs/examples/visual_gen/visual_gen_test_utils.py` _+4 more__
- **2026-10-12** [`5e3265ebc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e3265ebc9) [#20021](https://github.com/NVIDIA/TensorRT-LLM/pull/20021)
  [None][fix] Keep a one-rank DeviceMeshTopology off the job-wide device mesh (#20021)
  _Files: `tensorrt_llm/_torch/device_mesh.py`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_mapping.py`_

## Models  (7 commits)

- **2026-10-19** [`fda7ebd410`](https://github.com/NVIDIA/TensorRT-LLM/commit/fda7ebd410) [#20593](https://github.com/NVIDIA/TensorRT-LLM/pull/20593)
  [None][test] Add coverage for Qwen3ForCausalLM (#20593)
  _Files: `tests/unittest/_torch/modeling/test_modeling_qwen3.py`_
- **2026-10-19** [`066332abd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/066332abd5) [#19405](https://github.com/NVIDIA/TensorRT-LLM/pull/19405)
  [https://nvbugs/6784181][fix] Add an exact-path SPHINX_GENERATED_DOC_PAGES allowlist keyed off helper.py's… (#19405)
  _Files: `tests/integration/defs/test_doc.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-17** [`5de29bb28f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5de29bb28f) [#20514](https://github.com/NVIDIA/TensorRT-LLM/pull/20514)
  [None][doc] Document Qwen3.5 GB300 agentic serving (#20514)
  _Files: `docs/source/deployment-guide/deployment-guide-for-qwen3.8-qwen3.5-on-trtllm.md`, `examples/configs/curated/qwen3.5-gb300-agentic-decode.yaml`, `examples/configs/curated/qwen3.5-gb300-agentic-prefill.yaml`, `examples/configs/curated/qwen3.5-gb300-agentic.env`_
- **2026-10-16** [`f952e41390`](https://github.com/NVIDIA/TensorRT-LLM/commit/f952e41390) [#20210](https://github.com/NVIDIA/TensorRT-LLM/pull/20210)
  [None][test] Update the gemma4 and Qwen3.6 case for spark (#20210)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/defs/perf/pytorch_model_config.py`_
- **2026-10-15** [`bf0e298f11`](https://github.com/NVIDIA/TensorRT-LLM/commit/bf0e298f11) [#20233](https://github.com/NVIDIA/TensorRT-LLM/pull/20233)
  [https://nvbugs/6919428][fix] Keep DeepSeek-V4 TP decode all-reduces off NCCL (#20233)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tests/unittest/_torch/modeling/test_modeling_deepseekv4.py`_
- **2026-10-14** [`06fc0b1f5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/06fc0b1f5e) [#20084](https://github.com/NVIDIA/TensorRT-LLM/pull/20084)
  [None][perf] Avoid cuBLAS's fallback in the KDA prefill projection (#20084)
  _Files: `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tests/unittest/_torch/modules/kimi_kda/test_kda_prefill_op.py`_
- **2026-10-12** [`49334c15ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/49334c15ce) [#20026](https://github.com/NVIDIA/TensorRT-LLM/pull/20026)
  [None][test] Prune Kimi-K2 accuracy tests (#20026)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/perf/_model_paths.py` _+7 more__

## Speculative Decoding  (7 commits)

- **2026-10-18** [`3163e66b2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3163e66b2c) [#20163](https://github.com/NVIDIA/TensorRT-LLM/pull/20163)
  [None][test] Kimi-K3 and MiniMax-M3 AgentX perf-sanity cases, AgentX single-phase lanes, drop gpt-oss (#20163)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/benchmark_utils.py`, `jenkins/scripts/perf/disaggregated/dwdp_ctx_rank.sh` _+30 more__
- **2026-10-16** [`7fafb022ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fafb022ee) [#20147](https://github.com/NVIDIA/TensorRT-LLM/pull/20147)
  [TRTLLM-16780][feat] Honor per-request seeds in one-model speculative decoding's acceptance step (#20147)
  _Files: `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernels.cu`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernels.h`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernelsCommon.cuh`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernelsInternal.h` _+22 more__
- **2026-10-15** [`dba325dc1f`](https://github.com/NVIDIA/TensorRT-LLM/commit/dba325dc1f) [#20188](https://github.com/NVIDIA/TensorRT-LLM/pull/20188)
  [TRTLLM-16944][refactor] Simplify TorchSampler strategy grouping and fast path around the fused sampling kernel (#20188)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/__init__.py`, `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py` _+18 more__
- **2026-10-15** [`15f060c9f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/15f060c9f8) [#18876](https://github.com/NVIDIA/TensorRT-LLM/pull/18876)
  [None][feat] Develop agent flow orchestration and support parallel execution of perf agent and modeling agent based on it (#18876)
  _Files: `agent-flow/agent_flow/git_worktree.py`, `agent-flow/agent_flow/jobs/__init__.py`, `agent-flow/agent_flow/jobs/kinds.py`, `agent-flow/agent_flow/jobs/registry.py` _+53 more__
- **2026-10-12** [`dc8451c508`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc8451c508) [#20064](https://github.com/NVIDIA/TensorRT-LLM/pull/20064)
  [TRTLLM-16901][fix] SID-GR optimization 1/N: Fix speculative beam d2h races (#20064)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_features.py`, `tests/unittest/_torch/sampler/test_beam_search_speculative_d2h.py`_
- **2026-10-12** [`7f011f1020`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f011f1020) [#19490](https://github.com/NVIDIA/TensorRT-LLM/pull/19490)
  [TRTLLM-16593][fix] Size expanded draft probabilities by batch capacity (#19490)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/test_rejection_buffers_guard.py`_
- **2026-10-12** [`cf71337fbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf71337fbe) [#20076](https://github.com/NVIDIA/TensorRT-LLM/pull/20076)
  [None][test] Update MiniMax M3 EAGLE3 draft model directory (#20076)
  _Files: `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep16_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep8_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tep2_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tp4_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml` _+4 more__

## ROCm / AMD  (3 commits)

- **2026-10-17** [`e88d19ca3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e88d19ca3b) [#19960](https://github.com/NVIDIA/TensorRT-LLM/pull/19960)
  [None][feat] Kimi K3 optimizations on Rubin (#19960)
  _Files: `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`, `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.h`, `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingCustomKernels.cuh`, `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingCustomPolicy.cuh` _+64 more__
- **2026-10-15** [`7adc880405`](https://github.com/NVIDIA/TensorRT-LLM/commit/7adc880405) [#19387](https://github.com/NVIDIA/TensorRT-LLM/pull/19387)
  [None][test] Validate Kimi default KVCM V2 accuracy and disaggregated transfer (#19387)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/defs/accuracy/test_kimi3.py`, `tests/integration/test_lists/waives.txt` _+2 more__
- **2026-10-14** [`30dc23ffe5`](https://github.com/NVIDIA/TensorRT-LLM/commit/30dc23ffe5) [#19987](https://github.com/NVIDIA/TensorRT-LLM/pull/19987)
  [https://nvbugs/6812332][fix] Reshape the KDA decode fallback core to match prefill (#19987)
  _Files: `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tests/integration/defs/accuracy/test_kimi3.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus.yml` _+1 more__

## LoRA  (2 commits)

- **2026-10-19** [`72cd8b57a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/72cd8b57a3) [#20477](https://github.com/NVIDIA/TensorRT-LLM/pull/20477)
  [https://nvbugs/6939562][fix] Bound module_out_sizes read in LoRA param-fill kernel (#20477)
  _Files: `cpp/tensorrt_llm/kernels/lora/loraGroupGEMMParamFillRowReorderFusion.cu`_
- **2026-10-14** [`51b993b814`](https://github.com/NVIDIA/TensorRT-LLM/commit/51b993b814) [#20212](https://github.com/NVIDIA/TensorRT-LLM/pull/20212)
  [TRTLLM-16993][fix] Preserve LoRA cache when evictable pages are insufficient (#20212)
  _Files: `cpp/tensorrt_llm/runtime/loraCache.cpp`, `cpp/tests/unit_tests/batch_manager/peftCacheManagerTest.cpp`, `cpp/tests/unit_tests/runtime/loraCacheTest.cpp`_

## Docs / Examples  (2 commits)

- **2026-10-14** [`341eb99301`](https://github.com/NVIDIA/TensorRT-LLM/commit/341eb99301) [#18433](https://github.com/NVIDIA/TensorRT-LLM/pull/18433)
  [https://nvbugs/6564113][test] Warm up KV-cache transfer connections before disagg e2e perf sanity (#18433)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/defs/perf/time_breakdown_metrics.py`, `tests/unittest/others/test_perf_sanity_connection_warmup.py`_
- **2026-10-13** [`8fa0c60f92`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fa0c60f92)
  [None][chore] Bump version to 1.4.0rc1
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## Perf  (2 commits)

- **2026-10-13** [`e871c4132f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e871c4132f) [#19992](https://github.com/NVIDIA/TensorRT-LLM/pull/19992)
  [https://nvbugs/6658015][fix] Pin uvloop<0.23.0 to restore trtllm-serve streaming throughput (#19992)
  _Files: `requirements.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-10-12** [`f0df326ed6`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0df326ed6) [#19794](https://github.com/NVIDIA/TensorRT-LLM/pull/19794)
  [None][perf] Decode RGB and grayscale JPEGs with torchvision in ImageMediaIO (#19794)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tests/unittest/inputs/test_image_decode.py`_

---
_Generated 2026-10-19 15:39 UTC_