# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-11-02 → 2026-11-09  |  **Total commits:** 252

## ✨ New Features This Week

- **2026-11-09** [#20984](https://github.com/NVIDIA/TensorRT-LLM/pull/20984) — [None][feat] Add Cosmos3 per-request sigma grid selection (#20984)
- **2026-11-09** [#21325](https://github.com/NVIDIA/TensorRT-LLM/pull/21325) — [None][infra] Introduce Pyrefly to do type check (#21325)
- **2026-11-09** [#20936](https://github.com/NVIDIA/TensorRT-LLM/pull/20936) — [None][feat] Anthropic Messages: carry the request id in the message id (#20936)
- **2026-11-08** [#21222](https://github.com/NVIDIA/TensorRT-LLM/pull/21222) — [TRTLLM-16806][feat] Enable TRTLLM Ulysses attention for MiniMax-H3 (#21222)
- **2026-11-07** [#18912](https://github.com/NVIDIA/TensorRT-LLM/pull/18912) — [None][feat] Add Gemma4 variable-window attention (#18912)
- **2026-11-06** [#20005](https://github.com/NVIDIA/TensorRT-LLM/pull/20005) — [None][feat] VisualGen: dense FP8 attention and fused QK norm/RoPE/FP8 ops for Rubin (#20005)
- **2026-11-06** [#19612](https://github.com/NVIDIA/TensorRT-LLM/pull/19612) — [None][feat] Optionally release MiniMax-H3 host backups on wake (#19612)
- **2026-11-06** [#21601](https://github.com/NVIDIA/TensorRT-LLM/pull/21601) — [TRTLLM-14620][doc] Add DSpark confidence reproduction guide and benchmark kit (#21601)
- **2026-11-06** [#19735](https://github.com/NVIDIA/TensorRT-LLM/pull/19735) — [#19820][feat] Add Apertus and Apertus 1.5 (text) to the PyTorch backend (#19735)
- **2026-11-06** [#21455](https://github.com/NVIDIA/TensorRT-LLM/pull/21455) — [TRTLLM-17088][feat] Suspend to the host tier under aggregated Helix (#21455)
- _…and 45 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-07** [`9484c59210`](https://github.com/NVIDIA/TensorRT-LLM/commit/9484c59210) [#21538](https://github.com/NVIDIA/TensorRT-LLM/pull/21538) — [None][fix] Port native disaggregation KV result report token - #20723 (#21538)
- **2026-11-04** [`ee1e8e4645`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee1e8e4645) [#20843](https://github.com/NVIDIA/TensorRT-LLM/pull/20843) — [None][chore] Mass merge release/1.3 branch back to main (batch 2) (#20843)
- **2026-11-04** [`a324344095`](https://github.com/NVIDIA/TensorRT-LLM/commit/a324344095) [#21661](https://github.com/NVIDIA/TensorRT-LLM/pull/21661) — [TRTLLM-17615][fix] Initialize ownership in peer rejection test (#21661)
- **2026-11-04** [`b5fb1e2ef4`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5fb1e2ef4) [#18913](https://github.com/NVIDIA/TensorRT-LLM/pull/18913) — [None][feat] Add opt-in disaggregated transfer diagnostics (#18913)
- **2026-11-03** [`da980cce47`](https://github.com/NVIDIA/TensorRT-LLM/commit/da980cce47) [#20708](https://github.com/NVIDIA/TensorRT-LLM/pull/20708) — [None][feat] Attribute KV transfer timeouts to deadline owners and observed progress (#20708)
- **2026-11-03** [`09388e986d`](https://github.com/NVIDIA/TensorRT-LLM/commit/09388e986d) [#21521](https://github.com/NVIDIA/TensorRT-LLM/pull/21521) — [None][chore] Refine infra ownership for tests, vendoring, and Jenkins maintenance (#21521)
- **2026-11-03** [`db98553909`](https://github.com/NVIDIA/TensorRT-LLM/commit/db98553909) [#21272](https://github.com/NVIDIA/TensorRT-LLM/pull/21272) — [None][feat] Protect direct BF16 context-first KV transfers (#21272)
- **2026-11-02** [`a9be7004c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9be7004c7) [#20049](https://github.com/NVIDIA/TensorRT-LLM/pull/20049) — [None][chore] Remove the Python KV bounce buffer; kv_cache_bounce_size_mb selects the C++ agent bounce (#20049)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#21903](https://github.com/NVIDIA/TensorRT-LLM/issues/21903) | [Bug]: qwen3 tool parser: strict tool calls pick the wrong function be | bug, Customized kernels | 2026-11-09 |
| [#21809](https://github.com/NVIDIA/TensorRT-LLM/issues/21809) | [Bug]: Ray orchestrator: the DeepEP buffers bootstrap from an MPI_COMM | Disaggregated serving | 2026-11-06 |
| [#21800](https://github.com/NVIDIA/TensorRT-LLM/issues/21800) | [Bug]: Eagle3 loads a d2t that does not match t2d without any error | Speculative Decoding | 2026-11-06 |
| [#20944](https://github.com/NVIDIA/TensorRT-LLM/issues/20944) | [Bug]: trtllm-gen FMHA JIT bundles CUDA 13.4 headers, but the wheel ac | Customized kernels, Pytorch | 2026-11-03 |
| [#21102](https://github.com/NVIDIA/TensorRT-LLM/issues/21102) | [Feature]: Option to run the OpenEngine gRPC server on pygrpc-native | Frontend | 2026-10-27 |
| [#10024](https://github.com/NVIDIA/TensorRT-LLM/issues/10024) | [Bug] TRTLLM_NIXL_KVCACHE_BACKEND causes rail endpoint serialization m | KV-Cache Management, Disaggregated serving | 2026-10-27 |
| [#20082](https://github.com/NVIDIA/TensorRT-LLM/issues/20082) | [Bug]: Ray orchestrator with attention DP and TRTLLM_FORCE_COMM_METHOD | Disaggregated serving, Scale-out | 2026-10-27 |
| [#20376](https://github.com/NVIDIA/TensorRT-LLM/issues/20376) | [Bug]: Grouped MLA generation cubins are registered as Dense in kernel | Customized kernels | 2026-10-23 |
| [#19994](https://github.com/NVIDIA/TensorRT-LLM/issues/19994) | [Feature]: Whisper serving parity in trtllm-serve — /v1/audio/transcri | LLM API, OpenAI API | 2026-10-19 |
| [#20586](https://github.com/NVIDIA/TensorRT-LLM/issues/20586) | [Bug]: DeepSeek-V4.1 vision tower fails on SM107: cuDNN SDPA "No valid | Customized kernels, Pytorch | 2026-10-19 |
| [#20508](https://github.com/NVIDIA/TensorRT-LLM/issues/20508) | [Bug]: FP8 block-scale Linear hits a device-side assert on SM107: Deep | Customized kernels, Pytorch | 2026-10-17 |
| [#20504](https://github.com/NVIDIA/TensorRT-LLM/issues/20504) | [Bug]: Breakable prefill CUDA graphs replay corrupted outputs for some | Customized kernels | 2026-10-17 |
| [#20407](https://github.com/NVIDIA/TensorRT-LLM/issues/20407) | [Feature]: Structured profiling metadata for distributed inference tra | feature request, Scale-out | 2026-10-15 |
| [#20237](https://github.com/NVIDIA/TensorRT-LLM/issues/20237) | [New Model]: Add pplx-decider support | feature request, new model | 2026-10-13 |
| [#20138](https://github.com/NVIDIA/TensorRT-LLM/issues/20138) | [Bug]: Qwen3-VL E/PD handoff drops per-frame timestamp tokens and fram | Disaggregated serving, Multimodal | 2026-10-12 |
| [#19634](https://github.com/NVIDIA/TensorRT-LLM/issues/19634) | [Bug]: multi-node trtllm-serve with the MPI orchestrator (trtllm-llmap | Inference runtime, Disaggregated serving | 2026-10-10 |
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-10-08 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-10-05 |
| [#19666](https://github.com/NVIDIA/TensorRT-LLM/issues/19666) | [Feature]: EFA should work out of the box on NGC TRTLLM release image  | feature request, OOTB | 2026-10-01 |
| [#19726](https://github.com/NVIDIA/TensorRT-LLM/issues/19726) | [Feature][RFC]: Compact active beam rows during VBWS decode in the PyT | Pytorch, Model optimization | 2026-09-30 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 60 |
| Executor / Runtime | 39 |
| Attention | 37 |
| MoE | 24 |
| Quantization | 18 |
| Disaggregation / KV | 17 |
| Torch Path (_torch) | 15 |
| Other | 14 |
| ROCm / AMD | 8 |
| Models | 7 |
| Docs / Examples | 5 |
| Speculative Decoding | 4 |
| Perf | 2 |
| LoRA | 2 |

## CI / Infra  (60 commits)

- **2026-11-09** [`a34396bb1f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a34396bb1f) [#21813](https://github.com/NVIDIA/TensorRT-LLM/pull/21813)
  [TRTLLMINF-607][infra] Set the version with scripts/bump_version.py and check every version record (#21813)
  _Files: `.pre-commit-config.yaml`, `AGENTS.md`, `docker/Dockerfile.multi`, `docker/common/validate_wheel_metadata.py` _+9 more__
- **2026-11-09** [`6af9bb361b`](https://github.com/NVIDIA/TensorRT-LLM/commit/6af9bb361b) [#21918](https://github.com/NVIDIA/TensorRT-LLM/pull/21918)
  [None][infra] Waive 7 failed cases for main in pre-merge 68832 (#21918)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`15d98e60c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/15d98e60c1) [#19333](https://github.com/NVIDIA/TensorRT-LLM/pull/19333)
  [TRTLLMINF-451][infra] Capture setup timeouts and defer unfinished cleanup until JUnit save (#19333)
  _Files: `tests/integration/defs/utils/periodic_junit.py`, `tests/unittest/tools/test_periodic_junit.py`_
- **2026-11-09** [`10e1d1f07d`](https://github.com/NVIDIA/TensorRT-LLM/commit/10e1d1f07d) [#21026](https://github.com/NVIDIA/TensorRT-LLM/pull/21026)
  [https://nvbugs/6891165][fix] Pass chat_template_kwargs in the request body of the JSON-schema serve example (#21026)
  _Files: `examples/serve/openai_completion_client_json_schema.py`, `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`25e523fcf6`](https://github.com/NVIDIA/TensorRT-LLM/commit/25e523fcf6) [#21920](https://github.com/NVIDIA/TensorRT-LLM/pull/21920)
  [None][infra] Waive 3 failed cases for main in pre-merge 68855 (#21920)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`11961209ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/11961209ab) [#17808](https://github.com/NVIDIA/TensorRT-LLM/pull/17808)
  [TRTLLMINF-207][infra] classify pytest timeout results (#17808)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/generate_timeout_xml.py`, `jenkins/scripts/pytest_timeout_evidence.py`, `requirements-dev.txt` _+3 more__
- **2026-11-09** [`84ac3d8c8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/84ac3d8c8e) [#21817](https://github.com/NVIDIA/TensorRT-LLM/pull/21817)
  [TRTLLMINF-225][infra] Check the root requirement files in pre-commit and reject direct dependencies (#21817)
  _Files: `.pre-commit-config.yaml`, `scripts/check_requirements.py`, `setup.py`, `tests/unittest/scripts/test_check_requirements.py`_
- **2026-11-09** [`c6bc8fdbcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/c6bc8fdbcd) [#21418](https://github.com/NVIDIA/TensorRT-LLM/pull/21418)
  [None][infra] select covered Python files across repository directories (#21418)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/command/coverage/selection/explain.py`, `jenkins/scripts/cbts/cbts/command/main.py`, `jenkins/scripts/cbts/cbts/coverage/selection/SELECTION.md` _+10 more__
- **2026-11-09** [`4a7ca58a84`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a7ca58a84) [#21323](https://github.com/NVIDIA/TensorRT-LLM/pull/21323)
  [None][infra] Narrow CBTS perf selection by changed model aliases (#21323)
  _Files: `jenkins/scripts/cbts/cbts/blocks.py`, `jenkins/scripts/cbts/cbts/coverage/tier.py`, `jenkins/scripts/cbts/cbts/rules/README.md`, `jenkins/scripts/cbts/cbts/rules/perf_model_paths.py` _+2 more__
- **2026-11-09** [`a545268cf3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a545268cf3) [#21691](https://github.com/NVIDIA/TensorRT-LLM/pull/21691)
  [None][fix] Narrow CBTS acceptance reference selection to consumers (#21691)
  _Files: `jenkins/scripts/cbts/cbts/rules/README.md`, `jenkins/scripts/cbts/cbts/rules/tests_def.py`, `tests/unittest/scripts/cbts/test_tests_def.py`_
- **2026-11-09** [`d44d436aa2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d44d436aa2) [#21905](https://github.com/NVIDIA/TensorRT-LLM/pull/21905)
  [None][infra] Waive 2 failed cases for main in post-merge 3062 (#21905)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`a62a52bc6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a62a52bc6f) [#21223](https://github.com/NVIDIA/TensorRT-LLM/pull/21223)
  [TRTLLMINF-472][infra] Migrate test results to artifactory.nvidia.com (#21223)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/cbts/command/coverage/selection/artifact.py`, `jenkins/scripts/cbts/cbts/coverage/selection/SELECTION.md` _+10 more__
- **2026-11-09** [`956139bcd3`](https://github.com/NVIDIA/TensorRT-LLM/commit/956139bcd3) [#21898](https://github.com/NVIDIA/TensorRT-LLM/pull/21898)
  [None][infra] Waive 4 failed cases for main in pre-merge 68838 (#21898)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`9f5114f3aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f5114f3aa)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-11-08** [`0fe08d4772`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fe08d4772) [#21727](https://github.com/NVIDIA/TensorRT-LLM/pull/21727)
  [None][fix] Fix Slurm NCCL and pytest failures, continue nightly scans and trim CI logs (#21727)
  _Files: `jenkins/AGENTS.md`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/local/submit.py` _+5 more__
- **2026-11-08** [`73874e1a54`](https://github.com/NVIDIA/TensorRT-LLM/commit/73874e1a54) [#21838](https://github.com/NVIDIA/TensorRT-LLM/pull/21838)
  [https://nvbugs/7060043][infra] Waive 1 failed case(s) on A10 (#21838)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-08** [`1c496ed9de`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c496ed9de)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-11-07** [`bc80cae520`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc80cae520) [#21823](https://github.com/NVIDIA/TensorRT-LLM/pull/21823)
  [https://nvbugs/6907083][test] Unwaive MiniMax H3 two-GPU Ulysses LPIPS test (#21823)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`6f6fb3458a`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f6fb3458a) [#21730](https://github.com/NVIDIA/TensorRT-LLM/pull/21730)
  [https://nvbugs/7051902][infra] Waive 1 failed case(s) on DGX_H100 (#21730)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`0f7b0a2e39`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f7b0a2e39) [#21772](https://github.com/NVIDIA/TensorRT-LLM/pull/21772)
  [https://nvbugs/6445375][infra] Remove two MiniMax M3 B300 test waivers (#21772)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`3e1fb714d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e1fb714d3) [#21776](https://github.com/NVIDIA/TensorRT-LLM/pull/21776)
  [None][fix] Narrow CBTS test scopes using verified pre-images (#21776)
  _Files: `jenkins/scripts/cbts/cbts/rules/README.md`, `jenkins/scripts/cbts/cbts/rules/tests_def.py`, `tests/unittest/scripts/cbts/test_tests_def.py`_
- **2026-11-06** [`d271729943`](https://github.com/NVIDIA/TensorRT-LLM/commit/d271729943) [#21782](https://github.com/NVIDIA/TensorRT-LLM/pull/21782)
  [None][infra] Let CBTS rules own CPU test selection (#21782)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/command/main.py`, `jenkins/scripts/cbts/cbts/rules/README.md`, `jenkins/scripts/cbts/cbts/rules/docs.py` _+3 more__
- **2026-11-06** [`78bbcf50ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/78bbcf50ed) [#21783](https://github.com/NVIDIA/TensorRT-LLM/pull/21783)
  [None][infra] Add blossom-ci authorized users (#21783)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-11-06** [`8da7537c91`](https://github.com/NVIDIA/TensorRT-LLM/commit/8da7537c91) [#21497](https://github.com/NVIDIA/TensorRT-LLM/pull/21497)
  [TRTLLMINF-579][infra] Rename Check Test List stage to Check-Test-List and mark it skipped when not run (#21497)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-11-06** [`cd31578cb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd31578cb8) [#21761](https://github.com/NVIDIA/TensorRT-LLM/pull/21761)
  [https://nvbugs/7049655][test] Unwaive test_init_from_args_forwards_vision_gpu_normalize (#21761)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`0a96c51533`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a96c51533)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+3 more__
- **2026-11-06** [`47edc012f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/47edc012f3) [#21771](https://github.com/NVIDIA/TensorRT-LLM/pull/21771)
  [None][infra] Waive 1 failed cases for main in pre-merge 68497 (#21771)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`9bd3417770`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bd3417770) [#21765](https://github.com/NVIDIA/TensorRT-LLM/pull/21765)
  [None][infra] Waive 56 failed cases for main in post-merge 3056 (#21765)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`748dc201e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/748dc201e8) [#21713](https://github.com/NVIDIA/TensorRT-LLM/pull/21713)
  [https://nvbugs/7049815][infra] Waive 1 failed case(s) on GB200 (#21713)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`5c78d4fc77`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c78d4fc77) [#21697](https://github.com/NVIDIA/TensorRT-LLM/pull/21697)
  [https://nvbugs/7049062][infra] Waive 2 failed case(s) on GB200 (#21697)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`31af2013e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/31af2013e3) [#21715](https://github.com/NVIDIA/TensorRT-LLM/pull/21715)
  [https://nvbugs/7049813][infra] Waive 1 failed case(s) on GB200 (#21715)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`2106f4ff9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2106f4ff9a) [#21714](https://github.com/NVIDIA/TensorRT-LLM/pull/21714)
  [None][infra] Waive 1 failed cases for main in post-merge 3054 (#21714)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`44de24fde6`](https://github.com/NVIDIA/TensorRT-LLM/commit/44de24fde6) [#21709](https://github.com/NVIDIA/TensorRT-LLM/pull/21709)
  [None][infra] Waive 2 failed cases for main in pre-merge 68245 (#21709)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-05** [`b1e864648d`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1e864648d) [#21488](https://github.com/NVIDIA/TensorRT-LLM/pull/21488)
  [None][refactor] Use a platform-neutral LTX2 perf recipe filename (#21488)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/perf/README_test_visual_gen_perf_sanity.md`, `tests/integration/test_lists/test-db/l0_b200_visual_gen_perf_sanity.yml`, `tests/scripts/perf-sanity/visual_gen/ltx2.yaml`_
- **2026-11-05** [`38ab02f379`](https://github.com/NVIDIA/TensorRT-LLM/commit/38ab02f379) [#21694](https://github.com/NVIDIA/TensorRT-LLM/pull/21694)
  [None][infra] Waive 1 failed cases for main in pre-merge 68197 (#21694)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`f6405a5965`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6405a5965) [#21623](https://github.com/NVIDIA/TensorRT-LLM/pull/21623)
  [https://nvbugs/7044232][infra] Waive 1 failed case(s) on B300 (#21623)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`a32d66602b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a32d66602b) [#21626](https://github.com/NVIDIA/TensorRT-LLM/pull/21626)
  [https://nvbugs/7044104][infra] Waive 4 failed case(s) on CPU (#21626)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`f4c991b9e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4c991b9e6) [#21633](https://github.com/NVIDIA/TensorRT-LLM/pull/21633)
  [None][infra] Waive 1 failed cases for main in pre-merge 68079 (#21633)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`4f70b11ca9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f70b11ca9) [#21617](https://github.com/NVIDIA/TensorRT-LLM/pull/21617)
  [https://nvbugs/7043616][infra] Waive 1 failed case(s) on DGX_B200 (#21617)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`e62e13c29f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e62e13c29f) [#21627](https://github.com/NVIDIA/TensorRT-LLM/pull/21627)
  [None][infra] Waive 1 failed cases for main in pre-merge 68065 (#21627)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`d47a446cad`](https://github.com/NVIDIA/TensorRT-LLM/commit/d47a446cad) [#21608](https://github.com/NVIDIA/TensorRT-LLM/pull/21608)
  [None][infra] Waive 1 failed cases for main in pre-merge 68002 (#21608)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`f1e4d1df7b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1e4d1df7b) [#21464](https://github.com/NVIDIA/TensorRT-LLM/pull/21464)
  [https://nvbugs/7003540][ci] Unwaive fixed bugs. (#21464)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-03** [`47cd51b11b`](https://github.com/NVIDIA/TensorRT-LLM/commit/47cd51b11b) [#18914](https://github.com/NVIDIA/TensorRT-LLM/pull/18914)
  [None][infra] Enabling GCP_IAD in CI (#18914)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-11-03** [`cbc48a4518`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbc48a4518) [#21565](https://github.com/NVIDIA/TensorRT-LLM/pull/21565)
  [None][infra] Waive 1 failed cases for main in post-merge 3051 (#21565)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-03** [`745c1ce409`](https://github.com/NVIDIA/TensorRT-LLM/commit/745c1ce409) [#21562](https://github.com/NVIDIA/TensorRT-LLM/pull/21562)
  [None][infra] Waive 2 failed cases for main in pre-merge 67887 (#21562)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-03** [`7fb3147cdb`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fb3147cdb) [#20398](https://github.com/NVIDIA/TensorRT-LLM/pull/20398)
  [TRTLLMINF-490][infra] Keep SLURM job output and prune it after a retention pe… (#20398)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/PruneSlurmOutputs.groovy`_
- **2026-11-03** [`5865809df3`](https://github.com/NVIDIA/TensorRT-LLM/commit/5865809df3) [#21542](https://github.com/NVIDIA/TensorRT-LLM/pull/21542)
  [None][test] Waive 15 failed cases for main in QA CI (#21542)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-03** [`86c94eb75f`](https://github.com/NVIDIA/TensorRT-LLM/commit/86c94eb75f) [#21326](https://github.com/NVIDIA/TensorRT-LLM/pull/21326)
  [None][infra] improve CBTS hits for formatting and VisualGen changes (#21326)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/command/main.py`, `jenkins/scripts/cbts/cbts/rules/README.md`, `jenkins/scripts/cbts/cbts/rules/base.py` _+3 more__
- **2026-11-03** [`ac0c1fda18`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac0c1fda18) [#20913](https://github.com/NVIDIA/TensorRT-LLM/pull/20913)
  [TRTLLMINF-543][infra] Separate nSpect registration from launch checks and share the release scripts repo with the Kitmaker dry run (#20913)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/ci_versions.properties`_
- **2026-11-03** [`8e4ee6f51b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e4ee6f51b) [#21507](https://github.com/NVIDIA/TensorRT-LLM/pull/21507)
  [None][infra] Waive 5 failed cases for main in post-merge 3049 (#21507)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-03** [`8062ef3a92`](https://github.com/NVIDIA/TensorRT-LLM/commit/8062ef3a92) [#21430](https://github.com/NVIDIA/TensorRT-LLM/pull/21430)
  [TRTLLMINF-577][infra] increase Python dependency installation timeout to 60 minutes (#21430)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-11-03** [`980ea1a440`](https://github.com/NVIDIA/TensorRT-LLM/commit/980ea1a440) [#21387](https://github.com/NVIDIA/TensorRT-LLM/pull/21387)
  [None][test] Remove 36 closed-bug waive entries for main (#21387)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-02** [`88b50e6f90`](https://github.com/NVIDIA/TensorRT-LLM/commit/88b50e6f90) [#21477](https://github.com/NVIDIA/TensorRT-LLM/pull/21477)
  [None][infra] Waive 1 failed cases for main in pre-merge 67682 (#21477)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-02** [`aa4976f3ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa4976f3ca) [#21476](https://github.com/NVIDIA/TensorRT-LLM/pull/21476)
  [None][infra] Waive 1 failed cases for main in pre-merge 67669 (#21476)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-02** [`4969c916f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/4969c916f3) [#21446](https://github.com/NVIDIA/TensorRT-LLM/pull/21446)
  [None][infra] Waive 1 failed cases for main in pre-merge 67629 (#21446)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-02** [`8d4901ee17`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d4901ee17) [#20661](https://github.com/NVIDIA/TensorRT-LLM/pull/20661)
  [None][chore] Remove legacy alternativeTRT CI paths (#20661)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`_
- **2026-11-02** [`4e51a98529`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e51a98529) [#21415](https://github.com/NVIDIA/TensorRT-LLM/pull/21415)
  [None][infra] Waive 14 failed cases for main in post-merge 3048 (#21415)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-02** [`eb5d5c3afa`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb5d5c3afa) [#15398](https://github.com/NVIDIA/TensorRT-LLM/pull/15398)
  [TRTLLMINF-132][infra] Pre-bake fat sqsh to eliminate GPU idle time during CI pip installs (#15398)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/fat_build_inline.sh`, `jenkins/scripts/fat_build_sbatch_body.sh`, `jenkins/scripts/prepare_container.sh` _+2 more__
- **2026-11-02** [`68c1aab405`](https://github.com/NVIDIA/TensorRT-LLM/commit/68c1aab405)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-11-02** [`9c1866b3cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c1866b3cb) [#21398](https://github.com/NVIDIA/TensorRT-LLM/pull/21398)
  [None][infra] Waive 1 failed cases for main in pre-merge 67464 (#21398)
  _Files: `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (39 commits)

- **2026-11-09** [`306b42fe70`](https://github.com/NVIDIA/TensorRT-LLM/commit/306b42fe70) [#21416](https://github.com/NVIDIA/TensorRT-LLM/pull/21416)
  [None][fix] Require the tag of tagged unions in the serve config schemas (#21416)
  _Files: `scripts/generate_trtllm_serve_schemas.py`, `tensorrt_llm/schemas/trtllm-serve-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-disagg-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-visual-gen-config.schema.json` _+1 more__
- **2026-11-09** [`8c4dc73f3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c4dc73f3f) [#21798](https://github.com/NVIDIA/TensorRT-LLM/pull/21798)
  [None][fix] GLM tool parsers: deliver an argument the schema does not type as written (#21798)
  _Files: `tensorrt_llm/serve/tool_parser/glm4_parser.py`, `tensorrt_llm/serve/tool_parser/utils.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-11-09** [`73f161285b`](https://github.com/NVIDIA/TensorRT-LLM/commit/73f161285b) [#21794](https://github.com/NVIDIA/TensorRT-LLM/pull/21794)
  [None][test] expose subprocess output in serving e2e tests (#21794)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/unittest/llmapi/apps/_test_trtllm_serve_benchmark.py`, `tests/unittest/llmapi/apps/_test_trtllm_serve_example.py`, `tests/unittest/llmapi/apps/_test_trtllm_serve_multimodal_benchmark.py` _+2 more__
- **2026-11-07** [`dd484a44ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd484a44ae) [#20813](https://github.com/NVIDIA/TensorRT-LLM/pull/20813)
  [TRTLLM-17054][refactor] Reuse sampling synchronization and sequence slots across warmup phases (#20813)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/seq_slot_manager.py`, `tests/unittest/_torch/pyexecutor/test_executor_resource_rebind.py` _+1 more__
- **2026-11-06** [`2cce1864bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cce1864bd) [#19612](https://github.com/NVIDIA/TensorRT-LLM/pull/19612)
  [None][feat] Optionally release MiniMax-H3 host backups on wake (#19612)
  _Files: `cpp/include/tensorrt_llm/runtime/virtualMemory.h`, `cpp/tensorrt_llm/nanobind/runtime/bindings.cpp`, `cpp/tensorrt_llm/runtime/virtualMemory.cpp`, `cpp/tests/unit_tests/runtime/virtualMemoryTest.cpp` _+10 more__
- **2026-11-06** [`ea5b61c45c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea5b61c45c) [#19735](https://github.com/NVIDIA/TensorRT-LLM/pull/19735)
  [#19820][feat] Add Apertus and Apertus 1.5 (text) to the PyTorch backend (#19735)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_apertus.py` _+8 more__
- **2026-11-06** [`546f0f0f32`](https://github.com/NVIDIA/TensorRT-LLM/commit/546f0f0f32) [#21455](https://github.com/NVIDIA/TensorRT-LLM/pull/21455)
  [TRTLLM-17088][feat] Suspend to the host tier under aggregated Helix (#21455)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/pyexecutor/kv_cache/test_helix_agg_preemption.py`, `tests/unittest/_torch/pyexecutor/kv_cache/test_kv_cache_manager_v2_helix_superblock.py` _+2 more__
- **2026-11-06** [`d884dec5e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/d884dec5e9) [#21428](https://github.com/NVIDIA/TensorRT-LLM/pull/21428)
  [TRTLLM-17519][refactor] Merge PoolingRunner into EncoderRunner with packed and scheduled entry points (#21428)
  _Files: `docs/source/features/embeddings.md`, `tensorrt_llm/_torch/models/modeling_qwen.py`, `tensorrt_llm/_torch/models/modeling_qwen3.py`, `tensorrt_llm/_torch/pyexecutor/encoder_executor.py` _+17 more__
- **2026-11-06** [`59bf30f8bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/59bf30f8bf) [#21375](https://github.com/NVIDIA/TensorRT-LLM/pull/21375)
  [TRTLLM-17527][refactor] transport typed Python request inputs (#21375)
  _Files: `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/request_inputs.py` _+8 more__
- **2026-11-06** [`92b631f859`](https://github.com/NVIDIA/TensorRT-LLM/commit/92b631f859) [#21629](https://github.com/NVIDIA/TensorRT-LLM/pull/21629)
  [None][feat] trtllm_modeling_v2: scoped regression jobs, gate routing and tune-stage robustness (#21629)
  _Files: `agent-flow/agent_flow/workflows/trtllm_modeling_v2/README.md`, `agent-flow/agent_flow/workflows/trtllm_modeling_v2/agents/prompts/templates/common/modeling_v2_layout.md.j2`, `agent-flow/agent_flow/workflows/trtllm_modeling_v2/agents/skills/trtllm-modeling-v2-entry/SKILL.md`, `agent-flow/agent_flow/workflows/trtllm_modeling_v2/checks/harness/test_driver.py` _+28 more__
- **2026-11-06** [`406fa0acdd`](https://github.com/NVIDIA/TensorRT-LLM/commit/406fa0acdd) [#21024](https://github.com/NVIDIA/TensorRT-LLM/pull/21024)
  [TRTLLM-17005][refactor] Component-local C++ Tests (Part 5) (#21024)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/contextTransferCoordinator.cpp`, `cpp/tensorrt_llm/batch_manager/contextTransferVoteReducer.cpp` _+19 more__
- **2026-11-06** [`94bbc04e52`](https://github.com/NVIDIA/TensorRT-LLM/commit/94bbc04e52) [#20556](https://github.com/NVIDIA/TensorRT-LLM/pull/20556)
  [https://nvbugs/6682814][fix] Cherry-pick #20230: Use node IPs for perf-sanity disagg servers and report unresolvable bind hosts (#20556)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/llmapi/test_serve_report_addr.py`_
- **2026-11-05** [`d782229575`](https://github.com/NVIDIA/TensorRT-LLM/commit/d782229575) [#20498](https://github.com/NVIDIA/TensorRT-LLM/pull/20498)
  [TRTLLM-16725][refactor] BREAKING: Use a string enum for checkpoint I/O policy (#20498)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/checkpoint_loader.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/llmapi/__init__.py` _+11 more__
- **2026-11-05** [`7a06809243`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a06809243) [#21417](https://github.com/NVIDIA/TensorRT-LLM/pull/21417)
  [None][fix] Wait for the rank-0 VisualGen worker teardown at external-launch shutdown (#21417)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tests/unittest/_torch/visual_gen/test_executor_lifecycle.py`_
- **2026-11-05** [`e3538a71c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3538a71c9) [#21149](https://github.com/NVIDIA/TensorRT-LLM/pull/21149)
  [None][fix] Chat streaming: send finish_reason on its own chunk (#21149)
  _Files: `tensorrt_llm/serve/postprocess_handlers.py`, `tests/unittest/llmapi/apps/test_responses_usage.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-11-05** [`7818a634de`](https://github.com/NVIDIA/TensorRT-LLM/commit/7818a634de) [#21341](https://github.com/NVIDIA/TensorRT-LLM/pull/21341)
  [#21318][fix] Drop streamed stop-word ids from the final streamed text (#21341)
  _Files: `tensorrt_llm/executor/result.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/executor/test_stop_word_streaming_text.py`_
- **2026-11-05** [`6b7b4ec07c`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b7b4ec07c) [#21686](https://github.com/NVIDIA/TensorRT-LLM/pull/21686)
  [None][test] Fix two ModelEngine tests broken by concurrent merges (#21686)
  _Files: `tests/unittest/_torch/executor/test_model_engine_initialization.py`, `tests/unittest/_torch/pyexecutor/test_model_engine.py`_
- **2026-11-05** [`ec8797b9fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec8797b9fc) [#21035](https://github.com/NVIDIA/TensorRT-LLM/pull/21035)
  [#19902][perf] Size the beam-history copy by generated tokens, not prompt-length spread (#21035)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tests/unittest/_torch/sampler/test_beam_search.py`_
- **2026-11-05** [`78046876fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/78046876fa) [#21410](https://github.com/NVIDIA/TensorRT-LLM/pull/21410)
  [TRTLLM-17518][refactor] Build EncoderExecutor from shared setup components instead of ModelEngine (#21410)
  _Files: `docs/source/torch/arch_overview.md`, `tensorrt_llm/_torch/pyexecutor/encoder_executor.py`, `tensorrt_llm/_torch/pyexecutor/engine/model_setup.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/encoder.py` _+15 more__
- **2026-11-04** [`20c4047ca7`](https://github.com/NVIDIA/TensorRT-LLM/commit/20c4047ca7) [#21482](https://github.com/NVIDIA/TensorRT-LLM/pull/21482)
  [None][fix] Complete queued context cancellations before activation (#21482)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tests/unittest/_torch/pyexecutor/test_py_executor.py`, `tests/unittest/_torch/pyexecutor/test_queued_context_cancellation.py` _+1 more__
- **2026-11-04** [`93f0fcba8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/93f0fcba8c) [#21584](https://github.com/NVIDIA/TensorRT-LLM/pull/21584)
  [TRTLLM-17603][feat] Fail unsupported non-generation requests and executor loops cleanly instead of mid-run (#21584)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py` _+6 more__
- **2026-11-04** [`0160bf7a89`](https://github.com/NVIDIA/TensorRT-LLM/commit/0160bf7a89) [#20973](https://github.com/NVIDIA/TensorRT-LLM/pull/20973)
  [None][perf] Move vision pixel normalization from CPU to GPU (#20973)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4_unified.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py` _+18 more__
- **2026-11-04** [`ddc94409bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ddc94409bd) [#21503](https://github.com/NVIDIA/TensorRT-LLM/pull/21503)
  [None][fix] Kimi K2 tool parser: release the arguments of a call that ends the stream (#21503)
  _Files: `tensorrt_llm/serve/tool_parser/kimi_k2_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-11-04** [`9c0e41287f`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c0e41287f) [#20650](https://github.com/NVIDIA/TensorRT-LLM/pull/20650)
  [https://nvbugs/6953985][fix] Check the KV window crossing before the logger level (#20650)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/pyexecutor/kv_cache/test_kv_cache_v2_capacity_only.py`, `tests/unittest/_torch/pyexecutor/kv_cache/test_kvcm2_integration.py`_
- **2026-11-04** [`0685562125`](https://github.com/NVIDIA/TensorRT-LLM/commit/0685562125) [#21108](https://github.com/NVIDIA/TensorRT-LLM/pull/21108)
  [None][fix] GLM tool parsers: a fresh call in an open call's arguments abandons it (#21108)
  _Files: `tensorrt_llm/serve/tool_parser/glm4_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-11-04** [`9b9556933a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9b9556933a) [#21534](https://github.com/NVIDIA/TensorRT-LLM/pull/21534)
  [TRTLLMINF-586][infra] Add platform context to LLMAPI test stages (#21534)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-11-04** [`446083d814`](https://github.com/NVIDIA/TensorRT-LLM/commit/446083d814) [#21465](https://github.com/NVIDIA/TensorRT-LLM/pull/21465)
  [https://nvbugs/7003528][fix] Align ADP connector fixtures with executor contracts (#21465)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/test_connector_adp.py`_
- **2026-11-04** [`b8b29cd05b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8b29cd05b) [#21489](https://github.com/NVIDIA/TensorRT-LLM/pull/21489)
  [None][fix] Kimi-K3: count Responses usage as Chat Completions does (#21489)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `tensorrt_llm/serve/extensions/kimi_k3.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/postprocess_handlers.py` _+7 more__
- **2026-11-03** [`7924c15a61`](https://github.com/NVIDIA/TensorRT-LLM/commit/7924c15a61) [#21441](https://github.com/NVIDIA/TensorRT-LLM/pull/21441)
  [TRTLLM-17557][fix] Make the configuration-database CLI test runnable (#21441)
  _Files: `docs/source/_static/config_db.json`, `examples/configs/curated/lookup.yaml`, `tests/unittest/llmapi/test_config_database.py`_
- **2026-11-03** [`c26c166b8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c26c166b8e) [#21199](https://github.com/NVIDIA/TensorRT-LLM/pull/21199)
  [https://nvbugs/6858505][fix] Reject an encoder input longer than one encoder iteration at admission (#21199)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_t5.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/pyexecutor/test_py_executor.py` _+1 more__
- **2026-11-03** [`509ef87ffd`](https://github.com/NVIDIA/TensorRT-LLM/commit/509ef87ffd) [#19757](https://github.com/NVIDIA/TensorRT-LLM/pull/19757)
  [#19755][fix] Stream MiniMax-M2 tool-call arguments as deltas (#19757)
  _Files: `tensorrt_llm/serve/tool_parser/minimax_m2_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-11-03** [`55e55b9e2d`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e55b9e2d) [#21391](https://github.com/NVIDIA/TensorRT-LLM/pull/21391)
  [None][fix] Kimi-K3: honour the thinking and effort settings of Anthropic and chat requests (#21391)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `tensorrt_llm/serve/extensions/kimi_k3.py`, `tests/unittest/llmapi/apps/test_kimi_serve_extensions.py`, `tests/unittest/llmapi/apps/test_render_core.py`_
- **2026-11-03** [`31b99bb886`](https://github.com/NVIDIA/TensorRT-LLM/commit/31b99bb886) [#20868](https://github.com/NVIDIA/TensorRT-LLM/pull/20868)
  [None][fix] Responses: final snapshot keeps the status the stream reported (#20868)
  _Files: `tensorrt_llm/serve/responses_utils.py`, `tests/unittest/llmapi/apps/test_responses_stream_final_consistency.py`_
- **2026-11-03** [`3a36d4a5b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a36d4a5b1) [#21065](https://github.com/NVIDIA/TensorRT-LLM/pull/21065)
  [None][feat] Responses: serve a web_search tool the server cannot honour by default; TRTLLM_WEB_SEARCH_UNAVAILABLE=reject keeps the 400 (#21065)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/responses_utils.py`, `tensorrt_llm/serve/responses_web_search.py`, `tensorrt_llm/serve/web_search.py` _+1 more__
- **2026-11-03** [`ff1aa0f7d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff1aa0f7d3) [#21095](https://github.com/NVIDIA/TensorRT-LLM/pull/21095)
  [None][fix] Fix NCCL scope overhead, benchmark graph defaults and KV bounce streams (#21095)
  _Files: `tensorrt_llm/_torch/nccl_window_tensor_scope.py`, `tensorrt_llm/_torch/pyexecutor/engine/model_call.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/bench/dataclasses/configuration.py` _+1 more__
- **2026-11-02** [`4fd6d1cc45`](https://github.com/NVIDIA/TensorRT-LLM/commit/4fd6d1cc45) [#19764](https://github.com/NVIDIA/TensorRT-LLM/pull/19764)
  [#18297][fix] Prevent iteration log shutdown hangs (#19764)
  _Files: `tensorrt_llm/bench/benchmark/low_latency.py`, `tensorrt_llm/bench/benchmark/utils/asynchronous.py`, `tensorrt_llm/bench/benchmark/utils/processes.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+1 more__
- **2026-11-02** [`cbef70dbc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbef70dbc9) [#21349](https://github.com/NVIDIA/TensorRT-LLM/pull/21349)
  [None][test] Run session-reuse unit tests in CPU CI (#21349)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_session_reuse.py`_
- **2026-11-02** [`b6bb149fac`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6bb149fac) [#21266](https://github.com/NVIDIA/TensorRT-LLM/pull/21266)
  [https://nvbugs/7016691][fix] Bound ZeroMqQueue close linger so teardown cannot hang (#21266)
  _Files: `tensorrt_llm/executor/ipc.py`, `tests/unittest/executor/test_ipc.py`_
- **2026-11-02** [`4b697f1e2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b697f1e2a) [#21231](https://github.com/NVIDIA/TensorRT-LLM/pull/21231)
  [None][test] Guard lazy engine initialization and GPU-free imports (#21231)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/executor/test_model_engine_initialization.py`, `tests/unittest/others/test_import_cuda_context.py` _+1 more__

## Attention  (37 commits)

- **2026-11-09** [`e646fa6938`](https://github.com/NVIDIA/TensorRT-LLM/commit/e646fa6938) [#21354](https://github.com/NVIDIA/TensorRT-LLM/pull/21354)
  [None][chore] Refresh PrimTS source onto FlashInfer main (2026-11-07) (#21354)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py`, `tensorrt_llm/_torch/attention/backends/fmha/prims_ts_precompile.py` _+89 more__
- **2026-11-09** [`35ae2c0b35`](https://github.com/NVIDIA/TensorRT-LLM/commit/35ae2c0b35) [#21325](https://github.com/NVIDIA/TensorRT-LLM/pull/21325)
  [None][infra] Introduce Pyrefly to do type check (#21325)
  _Files: `.gitignore`, `.pre-commit-config.yaml`, `AGENTS.md`, `CODING_GUIDELINES.md` _+15 more__
- **2026-11-08** [`2d5b1fb68f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d5b1fb68f) [#21222](https://github.com/NVIDIA/TensorRT-LLM/pull/21222)
  [TRTLLM-16806][feat] Enable TRTLLM Ulysses attention for MiniMax-H3 (#21222)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/attention/backends/trtllm.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/pipeline_minimax_h3.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/transformer_minimax_h3.py` _+6 more__
- **2026-11-07** [`a3febfbfd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3febfbfd0) [#18912](https://github.com/NVIDIA/TensorRT-LLM/pull/18912)
  [None][feat] Add Gemma4 variable-window attention (#18912)
  _Files: `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h` _+20 more__
- **2026-11-06** [`875c4c9f97`](https://github.com/NVIDIA/TensorRT-LLM/commit/875c4c9f97) [#20005](https://github.com/NVIDIA/TensorRT-LLM/pull/20005)
  [None][feat] VisualGen: dense FP8 attention and fused QK norm/RoPE/FP8 ops for Rubin (#20005)
  _Files: `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeFp8Kernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeFp8Kernel.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt` _+14 more__
- **2026-11-06** [`e65d7273a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e65d7273a2) [#21737](https://github.com/NVIDIA/TensorRT-LLM/pull/21737)
  [None][doc] Point MiniMax-M3.1-Flash to its latest release container (#21737)
  _Files: `docs/source/models/supported-models.md`_
- **2026-11-06** [`1796b611cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1796b611cf) [#21372](https://github.com/NVIDIA/TensorRT-LLM/pull/21372)
  [None][feat] Qwen3.8-Flash-Next NVFP4 modeling_v2: one target for TP1/TP4/TEP4/DEP4/DEP2 on GB300 (#21372)
- **2026-11-06** [`0bdadaa4dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bdadaa4dd) [#20714](https://github.com/NVIDIA/TensorRT-LLM/pull/20714)
  [TRTLLM-17238][feat] Add PrimTS sparse core backend for Qwen3.8 QSA attention (#20714)
  _Files: `docs/source/deployment-guide/deployment-guide-for-qwen3.8-flash-next-on-trtllm.md`, `docs/source/release-notes.md`, `tensorrt_llm/_torch/attention/backends/sparse/qsa/module.py`, `tensorrt_llm/_torch/attention/backends/sparse/qsa/params.py` _+6 more__
- **2026-11-06** [`a7a60c3959`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7a60c3959) [#20664](https://github.com/NVIDIA/TensorRT-LLM/pull/20664)
  [None][feat] DSpark Unified KVCache standalone (#20664)
  _Files: `docs/source/features/speculative-decoding.md`, `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+17 more__
- **2026-11-06** [`e365592a7f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e365592a7f) [#21463](https://github.com/NVIDIA/TensorRT-LLM/pull/21463)
  [https://nvbugs/6953985][fix] Keep PyTorch's mimalloc arenas off transparent huge pages (#21463)
  _Files: `tensorrt_llm/__init__.py`, `tensorrt_llm/_bootstrap.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/weights.py`, `tests/unittest/_torch/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/ple/test_modeling_v2_ple_ngram_embed.py` _+1 more__
- **2026-11-06** [`08d7aaa21b`](https://github.com/NVIDIA/TensorRT-LLM/commit/08d7aaa21b) [#21681](https://github.com/NVIDIA/TensorRT-LLM/pull/21681)
  [None][perf] Build MSA fmha_sm100 JIT kernels for the visible GPUs' target only (#21681)
  _Files: `3rdparty/fetch_content.json`, `3rdparty/patches/msa_jit_device_arch.patch`, `tests/unittest/_torch/attention/sparse/msa/test_msa_jit_target.py`_
- **2026-11-05** [`57968941f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/57968941f1) [#21527](https://github.com/NVIDIA/TensorRT-LLM/pull/21527)
  [TRTLLM-17123][feat] Gather cached MLA KV for Helix prefill (#21527)
  _Files: `cpp/tensorrt_llm/kernels/mlaKernels.cu`, `cpp/tensorrt_llm/kernels/mlaKernels.h`, `cpp/tensorrt_llm/thop/mlaPreprocessOp.cpp`, `tensorrt_llm/_torch/attention/backends/trtllm.py` _+6 more__
- **2026-11-05** [`23806a9711`](https://github.com/NVIDIA/TensorRT-LLM/commit/23806a9711) [#21332](https://github.com/NVIDIA/TensorRT-LLM/pull/21332)
  [https://nvbugs/6910975][fix] Keep GDN decodes out of a bounded prefill state workspace (#21332)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/integration/test_lists/test-db/l0_rtx_pro_6000.yml`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py` _+1 more__
- **2026-11-05** [`3dbc06fbc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3dbc06fbc9) [#21319](https://github.com/NVIDIA/TensorRT-LLM/pull/21319)
  [https://nvbugs/6993575][fix] Remove the DeepSeek-V4 metadata recompile and nondeterministic mHC split-K (#21319)
  _Files: `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcFusedHcKernel.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcKernels.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcKernels.h` _+8 more__
- **2026-11-05** [`1399e99609`](https://github.com/NVIDIA/TensorRT-LLM/commit/1399e99609) [#21192](https://github.com/NVIDIA/TensorRT-LLM/pull/21192)
  [https://nvbugs/6858547][fix] Ignore cp_type with one CP rank and require HELIX with more (#21192)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/request_utils.py`, `tensorrt_llm/llmapi/llm_args.py` _+6 more__
- **2026-11-05** [`521a5faf1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/521a5faf1c)
  [None][chore] promote flashinfer-prims-ts source from #20068
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-11-05** [`66ce99b13c`](https://github.com/NVIDIA/TensorRT-LLM/commit/66ce99b13c) [#21409](https://github.com/NVIDIA/TensorRT-LLM/pull/21409)
  [TRTLLM-16460][perf] One-launch decode metadata for QSA rows and GDN replay work items (#21409)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/qsa/kernels.py`, `tensorrt_llm/_torch/attention/backends/sparse/qsa/metadata.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`, `tests/unittest/_torch/attention/sparse/qsa/test_qsa_sparse.py` _+1 more__
- **2026-11-04** [`2a8d8e46f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a8d8e46f6) [#20068](https://github.com/NVIDIA/TensorRT-LLM/pull/20068)
  [None][feat] VC-Attention-QK(16,8) recipes for PrimsTS FMHA context (#20068)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `docs/source/features/visualgen-quantized-attention.md`, `tensorrt_llm/_torch/attention/backends/fmha/interface.py` _+25 more__
- **2026-11-04** [`a0ce6c8474`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0ce6c8474) [#21367](https://github.com/NVIDIA/TensorRT-LLM/pull/21367)
  [TRTLLM-17151][fix] Apply the logit transform and sliding window DFlash drafters declare (#21367)
  _Files: `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/modules/logits_processor.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+5 more__
- **2026-11-04** [`0014b9d093`](https://github.com/NVIDIA/TensorRT-LLM/commit/0014b9d093) [#21547](https://github.com/NVIDIA/TensorRT-LLM/pull/21547)
  [https://nvbugs/7023194][fix] Restore auxiliary KV pool selection for DSA FMHA (#21547)
  _Files: `cpp/tensorrt_llm/thop/attentionOp.h`, `cpp/tests/unit_tests/thop/CMakeLists.txt`, `cpp/tests/unit_tests/thop/fmhaParamsTest.cpp`, `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`da32a87032`](https://github.com/NVIDIA/TensorRT-LLM/commit/da32a87032) [#21021](https://github.com/NVIDIA/TensorRT-LLM/pull/21021)
  [TRTLLM-17229][feat] Extend the mixed-precision KV cache to speculative decoding and the sparse MLA backends (#21021)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/attention/backends/fmha/gqa_decode.py`, `tensorrt_llm/_torch/attention/backends/interface.py` _+26 more__
- **2026-11-03** [`d07468ba9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d07468ba9e) [#20486](https://github.com/NVIDIA/TensorRT-LLM/pull/20486)
  [TRTLLM-16722][feat] Dflash Unified KVCache (#20486)
  _Files: `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/native/rank_info.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py` _+16 more__
- **2026-11-03** [`3c6ab301a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c6ab301a2) [#19786](https://github.com/NVIDIA/TensorRT-LLM/pull/19786)
  [None][perf] DSA: skip the indexer schedule rebuild for index-sharing draft steps and the duplicated kv-lens hook (#19786)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py` _+3 more__
- **2026-11-03** [`ad998a67e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad998a67e1) [#21432](https://github.com/NVIDIA/TensorRT-LLM/pull/21432)
  [TRTLLM-17505][feat] Add the SINK_REQUIRED_ONLY attention reuse policy to KV Cache Manager v2 (#21432)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+4 more__
- **2026-11-03** [`0e4b343f4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e4b343f4c) [#20639](https://github.com/NVIDIA/TensorRT-LLM/pull/20639)
  [None][feat] Run GLM-5.3-Flash sparse attention on SM120 through FlashInfer (#20639)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/kernels.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_glm53_flash.py` _+2 more__
- **2026-11-03** [`9e334fbaae`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e334fbaae) [#21198](https://github.com/NVIDIA/TensorRT-LLM/pull/21198)
  [None][perf] Add opt-in tiled QKV preprocessing (#21198)
  _Files: `docs/source/deployment-guide/deployment-guide-for-qwen3.8-qwen3.5-on-trtllm.md`, `tensorrt_llm/_torch/attention/kernels/fused_qk_norm_rope_gate.py`, `tensorrt_llm/_torch/attention/qk_norm_attention.py`, `tests/unittest/_torch/attention/kernels/test_fused_qk_norm_rope_gate.py`_
- **2026-11-03** [`d6ecb2901c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6ecb2901c) [#21437](https://github.com/NVIDIA/TensorRT-LLM/pull/21437)
  [https://nvbugs/7029762][docs] Link current PyTorch KV cache managers (#21437)
  _Files: `docs/source/features/paged-attention-ifb-scheduler.md`_
- **2026-11-03** [`a649e41d2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a649e41d2c) [#20269](https://github.com/NVIDIA/TensorRT-LLM/pull/20269)
  [#18151][feat] Admit trusted KV hints and carry immutable request metadata (#20269)
  _Files: `docs/source/features/kv-hints.md`, `docs/source/index.rst`, `tensorrt_llm/_torch/disaggregation/orchestration/_kv_hints.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py` _+27 more__
- **2026-11-03** [`1f0801437c`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f0801437c) [#21251](https://github.com/NVIDIA/TensorRT-LLM/pull/21251)
  [https://nvbugs/7011503][fix] Pass max_seq_len to MiniCPM-V 4.6 vision attention metadata (#21251)
  _Files: `tensorrt_llm/_torch/models/modeling_minicpmv4_6.py`, `tests/unittest/_torch/modeling/test_modeling_minicpmv4_6.py`_
- **2026-11-03** [`fee6cfd872`](https://github.com/NVIDIA/TensorRT-LLM/commit/fee6cfd872) [#20709](https://github.com/NVIDIA/TensorRT-LLM/pull/20709)
  [None][feat] Per View KV head transfer (#20709)
  _Files: `tensorrt_llm/_torch/disaggregation/native/mixers/attention/peer.py`, `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py` _+5 more__
- **2026-11-03** [`26ffe4bba6`](https://github.com/NVIDIA/TensorRT-LLM/commit/26ffe4bba6) [#21245](https://github.com/NVIDIA/TensorRT-LLM/pull/21245)
  [TRTLLM-17122][feat] Support owner-only MLA KV writes for Helix prefill (#21245)
  _Files: `cpp/tensorrt_llm/kernels/mlaKernels.cu`, `cpp/tensorrt_llm/kernels/mlaKernels.h`, `cpp/tensorrt_llm/thop/mlaPreprocessOp.cpp`, `tensorrt_llm/_torch/attention/backends/sparse/hooks.py` _+10 more__
- **2026-11-02** [`e71161e393`](https://github.com/NVIDIA/TensorRT-LLM/commit/e71161e393) [#21201](https://github.com/NVIDIA/TensorRT-LLM/pull/21201)
  [TRTLLM-17467][chore] Remove phantom dspark_confidence import hook from accept_stats (#21201)
  _Files: `examples/kimi_k3/measure_dspark_acceptance.py`, `tensorrt_llm/_torch/speculative/accept_stats.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dflash_accept_stats.py`_
- **2026-11-02** [`aff3e27437`](https://github.com/NVIDIA/TensorRT-LLM/commit/aff3e27437) [#21210](https://github.com/NVIDIA/TensorRT-LLM/pull/21210)
  [None][perf] Enable FlashInfer GDN chunked prefill on SM107 (#21210)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_utils.py`, `tests/integration/test_lists/test-db/l0_gr100.yml`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py`_
- **2026-11-02** [`bdcb577a93`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdcb577a93) [#21342](https://github.com/NVIDIA/TensorRT-LLM/pull/21342)
  [None][fix] KDA Small-BH prefill: 64-bit state-pool row stride (#21342)
  _Files: `3rdparty/vendor_patches/flashinfer-kda-bt16.patch`, `3rdparty/vendor_sources.lock.yaml`, `tensorrt_llm/_torch/attention/kernels/blackwell/kimi_k3_kda/kda_chunked_bt16_small_bh.py`, `tests/unittest/_torch/modules/kimi_kda/test_kda_prefill_op.py`_
- **2026-11-02** [`a0030d370a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0030d370a) [#21371](https://github.com/NVIDIA/TensorRT-LLM/pull/21371)
  [https://nvbugs/7016340][test] Remove the MLA mixed-precision KV numeric test (#21371)
  _Files: `tests/unittest/_torch/attention/test_mixed_precision_backends.py`_
- **2026-11-02** [`1989cf4c58`](https://github.com/NVIDIA/TensorRT-LLM/commit/1989cf4c58) [#21183](https://github.com/NVIDIA/TensorRT-LLM/pull/21183)
  [https://nvbugs/6308608][fix] Read request media from local paths only under an allowed directory (#21183)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `examples/serve/openai_chat_client_for_multimodal.py`, `tensorrt_llm/inputs/media_io.py`, `tensorrt_llm/serve/chat_utils.py` _+7 more__
- **2026-11-02** [`269101d133`](https://github.com/NVIDIA/TensorRT-LLM/commit/269101d133) [#20901](https://github.com/NVIDIA/TensorRT-LLM/pull/20901)
  [https://nvbugs/6858845][fix] Let no-KV-cache runners use FlashInfer attention (#20901)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/no_kv_cache.py`, `tests/unittest/_torch/multimodal/test_mm_encoder_standalone.py`, `tests/unittest/_torch/pyexecutor/engine/runners/test_no_kv_cache.py`_

## MoE  (24 commits)

- **2026-11-08** [`c1544b47ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1544b47ec) [#21013](https://github.com/NVIDIA/TensorRT-LLM/pull/21013)
  [TRTLLM-17328][chore] Remove quantized FlashInfer TRTLLM-Gen MoE leaves and FlashInfer two-sided alltoall (#21013)
  _Files: `.claude/skills/trtllm-moe-develop/references/moe-canonical-code-examples.md`, `docs/source/release-notes.md`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/communication/communication_factory.py` _+29 more__
- **2026-11-08** [`fe6938adb1`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe6938adb1) [#21590](https://github.com/NVIDIA/TensorRT-LLM/pull/21590)
  [None][perf] Staircase: Rubin GLM C1 Megakernel (#21590)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/glm_moe_dsa/csrc/CMakeLists.txt`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/glm_moe_dsa/glm_5_2_nvfp4__sm_107__low_latency/_megakernel.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/glm_moe_dsa/glm_5_2_nvfp4__sm_107__low_latency/csrc/glmMegakernel.cu`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/glm_moe_dsa/glm_5_2_nvfp4__sm_107__low_latency/csrc/glmMegakernel.h` _+5 more__
- **2026-11-07** [`0fe3f26a9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fe3f26a9f) [#21692](https://github.com/NVIDIA/TensorRT-LLM/pull/21692)
  [https://nvbugs/7043301][test] Turn off the HF weight cache in the GLM-5.2 SM103 TEP4 GSM8K test (#21692)
  _Files: `tests/integration/defs/accuracy/modeling_v2/test_glm_moe_dsa.py`_
- **2026-11-07** [`c16aa42c1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c16aa42c1c) [#21273](https://github.com/NVIDIA/TensorRT-LLM/pull/21273)
  [None][perf] Fuse NVFP4 activation quant into SwiGLU (SM100+) and add+RMSNorm (SM12x) (#21273)
  _Files: `cpp/tensorrt_llm/kernels/moe/cuteDsl/moeUtils.cu`, `cpp/tensorrt_llm/kernels/moe/cuteDsl/moeUtils.h`, `cpp/tensorrt_llm/kernels/rmsNormFp4QuantKernels.cu`, `cpp/tensorrt_llm/thop/moe/cuteDsl/cuteDslMoeUtilsOp.cpp` _+10 more__
- **2026-11-06** [`14365676e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/14365676e6) [#20703](https://github.com/NVIDIA/TensorRT-LLM/pull/20703)
  [TRTLLM-16725][refactor] BREAKING: Use a string enum for checkpoint formats and simplify checkpoint I/O helpers (#20703)
  _Files: `tensorrt_llm/_torch/models/checkpoints/auto_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/base_checkpoint_loader.py`, `tensorrt_llm/_torch/models/checkpoints/hf/afmoe_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/checkpoint_loader.py` _+52 more__
- **2026-11-06** [`2f528b21d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f528b21d8) [#21400](https://github.com/NVIDIA/TensorRT-LLM/pull/21400)
  [TRTLLM-14978][perf] Kimi-K3 MoE decode front: routing + moe_sort in one launch, CuTe router logits, router-first order, NVFP4 latent_down epilogue (#21400)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/kernels/blackwell/fp8_block_scale_low_m_gemm.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md` _+26 more__
- **2026-11-06** [`abb78b8afd`](https://github.com/NVIDIA/TensorRT-LLM/commit/abb78b8afd) [#21012](https://github.com/NVIDIA/TensorRT-LLM/pull/21012)
  [None][feat] Dense DWDP for Kimi-K3 context servers and a balanced DWDP expert partition (#21012)
  _Files: `cpp/tensorrt_llm/kernels/dwdpFabricGather.cu`, `cpp/tensorrt_llm/kernels/dwdpFabricGather.h`, `cpp/tensorrt_llm/thop/dwdpFabricGatherOp.cpp`, `docs/source/blogs/tech_blog/blog19_DWDP_Distributed_Weight_Data_Parallelism_for_High_Performance_LLM_Inference_on_NVL72.md` _+90 more__
- **2026-11-06** [`8f288165f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/8f288165f1) [#20765](https://github.com/NVIDIA/TensorRT-LLM/pull/20765)
  [TRTLLM-14883][feat] Qualify Qwen3 MoE (CUTLASS BF16) for MX (#20765)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/impl_blocks.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+15 more__
- **2026-11-06** [`a31654bf8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a31654bf8e) [#21545](https://github.com/NVIDIA/TensorRT-LLM/pull/21545)
  [TRTLLMINF-587][infra] Record MoE sub-test unfinished tests in a separate file (#21545)
  _Files: `tests/integration/defs/test_unittests.py`, `tests/unittest/conftest.py`_
- **2026-11-06** [`b1c638a96a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1c638a96a) [#21757](https://github.com/NVIDIA/TensorRT-LLM/pull/21757)
  [None][doc] Update MoE Perf Dashboard data to 1.4.0rc3 (#21757)
  _Files: `docs/source/_static/moe-perf-dashboard/data.js`_
- **2026-11-06** [`f23487d896`](https://github.com/NVIDIA/TensorRT-LLM/commit/f23487d896) [#21401](https://github.com/NVIDIA/TensorRT-LLM/pull/21401)
  [None][fix] DenseGEMM MoE: keep FC1/FC2 global accesses inside the problem (#21401)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/dense_blockscaled_gemm_act_fusion.py`, `tensorrt_llm/_torch/moe/kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`, `tensorrt_llm/_torch/moe/kernels/blackwell/moe_as_dense_gemm/fc1.py`, `tensorrt_llm/_torch/moe/kernels/blackwell/moe_as_dense_gemm/fc2.py` _+1 more__
- **2026-11-05** [`2906625f87`](https://github.com/NVIDIA/TensorRT-LLM/commit/2906625f87) [#21680](https://github.com/NVIDIA/TensorRT-LLM/pull/21680)
  [https://nvbugs/7028059][fix] Fix Qwen MoE native FP8 LoRA reference test configuration (#21680)
  _Files: `tests/integration/defs/llmapi/test_llm_api_pytorch_moe_lora.py`, `tests/integration/test_lists/waives.txt`_
- **2026-11-04** [`c8d7293119`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8d7293119) [#21399](https://github.com/NVIDIA/TensorRT-LLM/pull/21399)
  [TRTLLM-14978][perf] Kimi-K3 decode attention-residual kernel: CuTe DSL PDL mix with the MoE residual folded in, MXFP8 hand-off to KDA, gated/sigmoid low-M GEMM variants (#21399)
  _Files: `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.cu`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.h`, `cpp/tensorrt_llm/thop/attnResOp.cpp`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp4ep4/modeling.py` _+26 more__
- **2026-11-04** [`63468e6543`](https://github.com/NVIDIA/TensorRT-LLM/commit/63468e6543) [#21242](https://github.com/NVIDIA/TensorRT-LLM/pull/21242)
  [None][feat] Add NVFP4_PLUS (E2M1 + UE5M3 per 32) CuteDSL MoE on Rubin (#21242)
  _Files: `docs/source/features/quantization.md`, `examples/models/core/deepseek_v4/README.md`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/kernels/rubin/nvfp4_plus_quantize.py` _+33 more__
- **2026-11-04** [`167ca4518c`](https://github.com/NVIDIA/TensorRT-LLM/commit/167ca4518c) [#21281](https://github.com/NVIDIA/TensorRT-LLM/pull/21281)
  [TRTLLM-17390][fix] Size the separate draft-KV mirror from request history (#21281)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp16ep1/spec_worker.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp4ep4/spec_worker.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/speculative/dflash.py` _+10 more__
- **2026-11-04** [`fac0f14686`](https://github.com/NVIDIA/TensorRT-LLM/commit/fac0f14686) [#19285](https://github.com/NVIDIA/TensorRT-LLM/pull/19285)
  [None][feat] Support FP32, BF16 and FP16 with unified self-sampling GVR templates (#19285)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/top_k/__init__.py`, `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling_bf16.py`, `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling_fp16.py` _+4 more__
- **2026-11-03** [`04de854a9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/04de854a9e) [#21239](https://github.com/NVIDIA/TensorRT-LLM/pull/21239)
  [None][perf] Enable tiled Triton NVFP4 quantization for CuteDSL MoE (#21239)
  _Files: `tensorrt_llm/_torch/kernels/nvfp4_quant.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/cutedsl/grouped_gemm/nvfp4.py`, `tensorrt_llm/_torch/moe/fused_moe/cutedsl/kernel_inputs.py` _+4 more__
- **2026-11-03** [`b189a1525a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b189a1525a) [#21283](https://github.com/NVIDIA/TensorRT-LLM/pull/21283)
  [https://nvbugs/7015107][fix] Keep the Lamport all-reduce clear size in bytes (#21283)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/MiniMaxReduceRMSKernel.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/allReduceFusionKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/allReduceWorkspace.cu`, `cpp/tensorrt_llm/kernels/moe/communication/moeAllReduceFusionKernels.cu` _+4 more__
- **2026-11-03** [`f71076c08a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f71076c08a) [#20704](https://github.com/NVIDIA/TensorRT-LLM/pull/20704)
  [TRTLLM-16725][refactor] Centralize PyTorch distributed initialization (#20704)
  _Files: `tensorrt_llm/_torch/distributed/initialization.py`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_cute_dsl.py`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_deepgemm.py`, `tensorrt_llm/_torch/visual_gen/executor.py` _+2 more__
- **2026-11-03** [`a64db0c08b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a64db0c08b) [#20937](https://github.com/NVIDIA/TensorRT-LLM/pull/20937)
  [TRTLLM-16460][perf] Qwen3.8-Flash-Next NVFP4 modeling_v2 target: GB300 Pareto optimizations for ISL 8K / OSL 1K (#20937)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/kernels/__init__.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/kernels/moe/__init__.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/kernels/moe/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/modeling.py` _+71 more__
- **2026-11-02** [`71b8f3dc74`](https://github.com/NVIDIA/TensorRT-LLM/commit/71b8f3dc74) [#21347](https://github.com/NVIDIA/TensorRT-LLM/pull/21347)
  [https://nvbugs/6908161][fix] Bootstrap NCCL EP from the torch EP group under Ray (#21347)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/nccl_ep_utils.py`_
- **2026-11-02** [`39df047646`](https://github.com/NVIDIA/TensorRT-LLM/commit/39df047646) [#21121](https://github.com/NVIDIA/TensorRT-LLM/pull/21121)
  [https://nvbugs/6993575][fix] Prime MegaMoE tile variants during autotuning (#21121)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_deepgemm.py`, `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/unittest/_torch/moe/test_moe_backend.py`_
- **2026-11-02** [`4c2238ee52`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c2238ee52) [#21225](https://github.com/NVIDIA/TensorRT-LLM/pull/21225)
  [https://nvbugs/6997728][fix] Fix DeepSeek-V4-Pro DEP4 MegaMoE CuTe DSL test: skip HF weight cache for oversized checkpoints, drop hard GSM8K floor, fix bootstrap hang (#21225)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_cute_dsl.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+3 more__
- **2026-11-02** [`df9c1af1c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/df9c1af1c5) [#21271](https://github.com/NVIDIA/TensorRT-LLM/pull/21271)
  [None][perf] GVR V2 reg_clus hint-free path: prefix sample, suffix guard and a bounded exact rescue (#21271)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tests/unittest/_torch/kernels/parallel/test_gvr_selfsampling_topk.py`_

## Quantization  (18 commits)

- **2026-11-09** [`bfeeea33c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfeeea33c6) [#20984](https://github.com/NVIDIA/TensorRT-LLM/pull/20984)
  [None][feat] Add Cosmos3 per-request sigma grid selection (#20984)
  _Files: `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/serve/README.md`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/defaults.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py` _+9 more__
- **2026-11-07** [`bcb64e1459`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcb64e1459) [#21434](https://github.com/NVIDIA/TensorRT-LLM/pull/21434)
  [#20969][fix] Qwen3.5/3.8: default dense NVFP4 checkpoints to Marlin on Ada/Hopper (#21434)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl.py`_
- **2026-11-07** [`ecf1fefa36`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecf1fefa36)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+9 more__
- **2026-11-07** [`9529c835c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/9529c835c7) [#21671](https://github.com/NVIDIA/TensorRT-LLM/pull/21671)
  [https://nvbugs/7028062][fix] Fix MiniMax test subprocess imports (#21671)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling_v2/models/minimax_m3/minimax_m3_nvfp4__sm_103__tp4/comm/_rank_job.py`, `tests/unittest/_torch/modeling_v2/models/minimax_m3/minimax_m3_nvfp4__sm_103__tp8/comm/_rank_job.py`, `tests/unittest/_torch/modeling_v2/models/minimax_m3/minimax_m3_nvfp4__sm_107__tp2/comm/_rank_job.py` _+2 more__
- **2026-11-06** [`5e34112049`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e34112049) [#21601](https://github.com/NVIDIA/TensorRT-LLM/pull/21601)
  [TRTLLM-14620][doc] Add DSpark confidence reproduction guide and benchmark kit (#21601)
  _Files: `examples/models/core/deepseek_v4/CONFIDENCE_REPRODUCTION.md`, `examples/models/core/deepseek_v4/README.md`, `examples/models/core/deepseek_v4/dspark_artifacts/calibration.json`, `examples/models/core/deepseek_v4/dspark_artifacts/costs-b300-dep8.json` _+7 more__
- **2026-11-05** [`51798b84e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/51798b84e6) [#21543](https://github.com/NVIDIA/TensorRT-LLM/pull/21543)
  [TRTLLM-17612][refactor] Remove unused kernels after TensorRT backend removal (#21543)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/epilogue/threadblock/epilogue_per_row_per_col_scale.h`, `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/epilogue/threadblock/epilogue_tensor_op_int32.h`, `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm/collective/builders/sm90_gmma_builder_gated.inl` _+63 more__
- **2026-11-05** [`1686f5c57f`](https://github.com/NVIDIA/TensorRT-LLM/commit/1686f5c57f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-11-05** [`b3634de322`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3634de322) [#20483](https://github.com/NVIDIA/TensorRT-LLM/pull/20483)
  [None][feat] Visual Gen token-sharded TP: gather FP8 block-scale inputs (#20483)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/parallel/token_sharded_modules.py`, `tensorrt_llm/_torch/visual_gen/parallel/token_sharded_tp.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_token_sharded_tp_collectives.py` _+3 more__
- **2026-11-04** [`50745456df`](https://github.com/NVIDIA/TensorRT-LLM/commit/50745456df) [#20623](https://github.com/NVIDIA/TensorRT-LLM/pull/20623)
  [None][feat] MiniMax-M3 NVFP4 low latency decode megakernel for Rubin (sm_107) TP2 / TP4 / TP8 in modeling_v2 (#20623)
- **2026-11-04** [`20bf00803a`](https://github.com/NVIDIA/TensorRT-LLM/commit/20bf00803a)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/pyproject.toml`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-11-03** [`1a296dcde6`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a296dcde6) [#20524](https://github.com/NVIDIA/TensorRT-LLM/pull/20524)
  [TRTLLM-17096][feat] modeling_v2: GLM-5.2 NVFP4 low-latency decode target for GB300 (#20524)
- **2026-11-03** [`c263c45a6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c263c45a6c) [#21426](https://github.com/NVIDIA/TensorRT-LLM/pull/21426)
  [None][test] Add Muse Spark Open NVFP4 core performance coverage (#21426)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-11-03** [`81d2947b92`](https://github.com/NVIDIA/TensorRT-LLM/commit/81d2947b92) [#21421](https://github.com/NVIDIA/TensorRT-LLM/pull/21421)
  [None][test] extend Qwen3 NVFP4 CUTLASS RTX test timeout (#21421)
  _Files: `tests/integration/test_lists/qa/llm_function_rtx6k.txt`_
- **2026-11-03** [`b7a1594ba2`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7a1594ba2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+4 more__
- **2026-11-03** [`8e93b19a69`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e93b19a69) [#21357](https://github.com/NVIDIA/TensorRT-LLM/pull/21357)
  [https://nvbugs/7007647][test] Relax MXFP8 refit logit-overlap threshold to 0.85 (#21357)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`_
- **2026-11-03** [`e95f15e728`](https://github.com/NVIDIA/TensorRT-LLM/commit/e95f15e728) [#20763](https://github.com/NVIDIA/TensorRT-LLM/pull/20763)
  [TRTLLM-17218][fix] Keep merged quantization exclude_modules in checkpoint order (#20763)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/models/quant_config_utils.py`, `tests/unittest/_torch/test_hf_quant_config.py`_
- **2026-11-02** [`cf96e9ec51`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf96e9ec51)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-11-02** [`3f59791863`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f59791863) [#21002](https://github.com/NVIDIA/TensorRT-LLM/pull/21002)
  [https://nvbugs/6770977][test] Fix qwen3_32b_fp8 disagg output check and startup budget (#21002)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_

## Disaggregation / KV  (17 commits)

- **2026-11-09** [`fa976a0bd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa976a0bd7) [#21249](https://github.com/NVIDIA/TensorRT-LLM/pull/21249)
  [https://nvbugs/6988867][fix] Bind the disagg test server to a kernel-assigned port (#21249)
  _Files: `tests/integration/defs/disaggregated/disagg_test_utils.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-11-09** [`6b0af1e4c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b0af1e4c4) [#20936](https://github.com/NVIDIA/TensorRT-LLM/pull/20936)
  [None][feat] Anthropic Messages: carry the request id in the message id (#20936)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tensorrt_llm/serve/openai_disagg_server.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/disaggregated/test_openai_disagg_service.py` _+6 more__
- **2026-11-09** [`00df5adc81`](https://github.com/NVIDIA/TensorRT-LLM/commit/00df5adc81) [#20903](https://github.com/NVIDIA/TensorRT-LLM/pull/20903)
  [https://nvbugs/6858496][fix] Fail disagg gen requests whose grammar matcher cannot be created (#20903)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/guided_decoder.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+5 more__
- **2026-11-09** [`d1118eaad1`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1118eaad1) [#21810](https://github.com/NVIDIA/TensorRT-LLM/pull/21810)
  [https://nvbugs/7042835][test] Unwaive unittest/disaggregated fixed by #21597 (#21810)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`b9ada4876e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9ada4876e) [#21774](https://github.com/NVIDIA/TensorRT-LLM/pull/21774)
  [https://nvbugs/7044831][test] Unwaive the mixed-precision disaggregation tests fixed by #21597 (#21774)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-06** [`3016aded89`](https://github.com/NVIDIA/TensorRT-LLM/commit/3016aded89) [#21516](https://github.com/NVIDIA/TensorRT-LLM/pull/21516)
  [None][fix] Isolate fallback hwloc and add EFA functional CI coverage (#21516)
  _Files: `docker/common/install_base.sh`, `docker/common/install_efa_installer.sh`, `docker/common/install_gdrcopy.sh`, `docker/common/install_nixl.sh` _+9 more__
- **2026-11-06** [`6aa67fbf5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6aa67fbf5f) [#21710](https://github.com/NVIDIA/TensorRT-LLM/pull/21710)
  [None][infra] remove DeepSeek R1 multi-node perf tests (#21710)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_con1_ctx1_pp8_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml` _+18 more__
- **2026-11-05** [`9badd1eb98`](https://github.com/NVIDIA/TensorRT-LLM/commit/9badd1eb98) [#21525](https://github.com/NVIDIA/TensorRT-LLM/pull/21525)
  [None][chore] Deprecate KV cache manager V1 and the C++ cache transceiver (#21525)
  _Files: `docs/source/developer-guide/kv-transfer.md`, `docs/source/features/disagg-serving.md`, `docs/source/features/kvcache.md`, `docs/source/release-notes.md` _+7 more__
- **2026-11-05** [`7d7b098cb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d7b098cb3) [#21597](https://github.com/NVIDIA/TensorRT-LLM/pull/21597)
  [TRTLLM-17229][fix] Resolve the KV-head count of mixed-precision high layers in disaggregated transfer (#21597)
  _Files: `tensorrt_llm/_torch/disaggregation/native/context_first_profile.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py`, `tests/unittest/disaggregated/test_context_first_profile.py`, `tests/unittest/disaggregated/test_extractor.py`_
- **2026-11-05** [`a7e88dee4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7e88dee4a) [#21187](https://github.com/NVIDIA/TensorRT-LLM/pull/21187)
  [https://nvbugs/6813945][fix] Use stored metadata server URLs as is and support etcd credentials and signed server records (#21187)
  _Files: `examples/disaggregated/README.md`, `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/serve/metadata_server.py`, `tensorrt_llm/serve/openai_client.py` _+3 more__
- **2026-11-04** [`a84de55612`](https://github.com/NVIDIA/TensorRT-LLM/commit/a84de55612) [#21541](https://github.com/NVIDIA/TensorRT-LLM/pull/21541)
  [None][test] State the GPU count of multi-GPU QA core tests with markers (#21541)
  _Files: `.coderabbit.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/defs/disaggregated/test_workers.py` _+1 more__
- **2026-11-03** [`f9b3464571`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9b3464571) [#20975](https://github.com/NVIDIA/TensorRT-LLM/pull/20975)
  [TRTLLM-16186][fix] Rows name their slots and regions in the backend contract (#20975)
  _Files: `tensorrt_llm/_torch/disaggregation/base/backend.py`, `tests/unittest/_torch/disaggregation/test_backend_contract.py`_
- **2026-11-03** [`69dfad4da3`](https://github.com/NVIDIA/TensorRT-LLM/commit/69dfad4da3) [#19783](https://github.com/NVIDIA/TensorRT-LLM/pull/19783)
  [None][fix] Enable NIXL LIBFABRIC and update EFA in container images (#19783)
  _Files: `docker/Dockerfile.multi`, `docker/common/install_base.sh`, `docker/common/install_efa_installer.sh`, `docker/common/install_gdrcopy.sh` _+4 more__
- **2026-11-02** [`0eb0539d0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0eb0539d0f) [#21122](https://github.com/NVIDIA/TensorRT-LLM/pull/21122)
  [TRTLLM-17125][feat] Preempt requests on KV pressure under aggregated Helix (#21122)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+7 more__
- **2026-11-02** [`5d2bbc0dda`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d2bbc0dda) [#21412](https://github.com/NVIDIA/TensorRT-LLM/pull/21412)
  [TRTLLM-17557][test] Run the disaggregated launcher telemetry tests in the CPU stage (#21412)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`_
- **2026-11-02** [`4fe736fcff`](https://github.com/NVIDIA/TensorRT-LLM/commit/4fe736fcff) [#21343](https://github.com/NVIDIA/TensorRT-LLM/pull/21343)
  [None][fix] Warmup: no generation shapes on a context-only KV cache (#21343)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/warmup.py`, `tests/unittest/_torch/pyexecutor/engine/runners/decoder/test_warmup.py`_
- **2026-11-02** [`268a14d17a`](https://github.com/NVIDIA/TensorRT-LLM/commit/268a14d17a) [#21314](https://github.com/NVIDIA/TensorRT-LLM/pull/21314)
  [None][test] Improve store driver conformance for fixed pools and shutdown (#21314)
  _Files: `tensorrt_llm/_torch/disaggregation/blob/README.md`, `tensorrt_llm/_torch/disaggregation/blob/store.py`, `tensorrt_llm/_torch/disaggregation/testing/broken_drivers.py`, `tensorrt_llm/_torch/disaggregation/testing/driver_conformance.py` _+2 more__

## Torch Path (_torch)  (15 commits)

- **2026-11-09** [`4f2a3b997b`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f2a3b997b) [#21910](https://github.com/NVIDIA/TensorRT-LLM/pull/21910)
  [None][docs] Clarify Modeling V2 rules for Modeling V1 code, native code and routing (#21910)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`_
- **2026-11-09** [`683a49ef49`](https://github.com/NVIDIA/TensorRT-LLM/commit/683a49ef49) [#21631](https://github.com/NVIDIA/TensorRT-LLM/pull/21631)
  [https://nvbugs/6858527][fix] Check RADIO video_embedder weights when loading, not per video (#21631)
  _Files: `tensorrt_llm/_torch/models/modeling_radio.py`, `tests/unittest/_torch/modeling/test_modeling_radio.py`_
- **2026-11-06** [`682a2b700f`](https://github.com/NVIDIA/TensorRT-LLM/commit/682a2b700f) [#21615](https://github.com/NVIDIA/TensorRT-LLM/pull/21615)
  [TRTLLM-17677][perf] Split the low-M GEMM autotuning race across the tuning group (#21615)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/modules/low_m_gemm.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-11-06** [`bdc99e0871`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdc99e0871) [#21672](https://github.com/NVIDIA/TensorRT-LLM/pull/21672)
  [https://nvbugs/7003528][fix] Restore ADP connector CPU test coverage (#21672)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/test_connector_adp.py`_
- **2026-11-06** [`7cfe7f781f`](https://github.com/NVIDIA/TensorRT-LLM/commit/7cfe7f781f) [#21524](https://github.com/NVIDIA/TensorRT-LLM/pull/21524)
  [None][infra] Retire legacy L0 perf testing and protect QA benchmarks (#21524)
  _Files: `.pre-commit-config.yaml`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/cbts/rules/README.md` _+18 more__
- **2026-11-05** [`eaa88a0fed`](https://github.com/NVIDIA/TensorRT-LLM/commit/eaa88a0fed) [#21684](https://github.com/NVIDIA/TensorRT-LLM/pull/21684)
  [None][fix] causal_conv1d: form conv-state slot offsets in 64 bits (#21684)
  _Files: `cpp/tensorrt_llm/kernels/causalConv1d/causalConv1d.cu`, `cpp/tensorrt_llm/kernels/causalConv1d/causalConv1d.h`, `cpp/tensorrt_llm/thop/causalConv1dOp.cpp`, `tests/unittest/_torch/kernels/parallel_hw_agnostic/test_causal_conv1d_op.py`_
- **2026-11-04** [`eea482f0d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/eea482f0d6) [#21226](https://github.com/NVIDIA/TensorRT-LLM/pull/21226)
  [TRTLLM-16807][feat] Support combined Omni references in video serving (#21226)
  _Files: `examples/visual_gen/serve/README.md`, `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_video_routes.py`, `tensorrt_llm/serve/visual_gen_utils.py` _+1 more__
- **2026-11-04** [`b13f9b6a25`](https://github.com/NVIDIA/TensorRT-LLM/commit/b13f9b6a25) [#21500](https://github.com/NVIDIA/TensorRT-LLM/pull/21500)
  [None][test] Add coverage for Glm5NextForConditionalGeneration (#21500)
  _Files: `tests/unittest/_torch/modeling/test_glm5_next_contracts.py`_
- **2026-11-04** [`b98a7e0fe8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b98a7e0fe8) [#21419](https://github.com/NVIDIA/TensorRT-LLM/pull/21419)
  [None][perf] autotuner: share one CUDA graph pool across a tuning pas… (#21419)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-11-02** [`53529c014e`](https://github.com/NVIDIA/TensorRT-LLM/commit/53529c014e) [#21301](https://github.com/NVIDIA/TensorRT-LLM/pull/21301)
  [TRTLLM-16750][feat] Support CPU offloading for MiniMax-H3 (#21301)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/pipeline_minimax_h3.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/ref2va.py`, `tests/integration/defs/visual_gen/test_minimax_h3_offload.py` _+2 more__
- **2026-11-02** [`2bb8e9d743`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bb8e9d743) [#21396](https://github.com/NVIDIA/TensorRT-LLM/pull/21396)
  [None][fix] Enable the fused per-token AdaLN on SM103 (B300/GB300) (#21396)
  _Files: `tensorrt_llm/_torch/visual_gen/kernels/blackwell/pertoken_adaln/pertoken_adaln.py`, `tensorrt_llm/_torch/visual_gen/models/wan/utils_wan.py`, `tests/unittest/_torch/visual_gen/test_pertoken_adaln.py`, `tests/unittest/_torch/visual_gen/test_wan22_ti2v_5b_pipeline.py`_
- **2026-11-02** [`bc1036f1b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc1036f1b8) [#20999](https://github.com/NVIDIA/TensorRT-LLM/pull/20999)
  [None][test] Add GLM-5.3 core performance coverage (#20999)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-11-02** [`b996f47524`](https://github.com/NVIDIA/TensorRT-LLM/commit/b996f47524) [#21402](https://github.com/NVIDIA/TensorRT-LLM/pull/21402)
  [https://nvbugs/7023113][test] Guard DSpark DEP4 CuTe DSL test by device memory (#21402)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-11-02** [`b1b7ff1de5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1b7ff1de5) [#20285](https://github.com/NVIDIA/TensorRT-LLM/pull/20285)
  [https://nvbugs/6787519][fix] Initialize Nemotron-H-Puzzle configuration correctly (#20285)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tests/unittest/_torch/modeling/test_nemotron_h_puzzle_config.py`_
- **2026-11-02** [`b34ad8c55e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b34ad8c55e) [#21390](https://github.com/NVIDIA/TensorRT-LLM/pull/21390)
  [None][docs] Rewrite Modeling V2 developer guides (#21390)
  _Files: `cpp/tensorrt_llm/modeling_v2/README.md`, `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`_

## Other  (14 commits)

- **2026-11-09** [`52cd3d0753`](https://github.com/NVIDIA/TensorRT-LLM/commit/52cd3d0753) [#21603](https://github.com/NVIDIA/TensorRT-LLM/pull/21603)
  [None][chore] Relax Modeling V2 naming and select Modeling V2 tests by change scope (#21603)
- **2026-11-09** [`82cf1afb0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/82cf1afb0a) [#21795](https://github.com/NVIDIA/TensorRT-LLM/pull/21795)
  [https://nvbugs/6964706][fix] Make KVCacheManagerV2 teardown safe without a CUDA context (#21795)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batch.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+7 more__
- **2026-11-07** [`68a08c57ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/68a08c57ea) [#21812](https://github.com/NVIDIA/TensorRT-LLM/pull/21812)
  [None][refactor] Make GLM Rubin modeling v2 target self-contained (#21812)
- **2026-11-06** [`aea80a0ec8`](https://github.com/NVIDIA/TensorRT-LLM/commit/aea80a0ec8) [#21764](https://github.com/NVIDIA/TensorRT-LLM/pull/21764)
  [None][fix] Declare 16 MPI ranks for multi-node evaluation tests (#21764)
  _Files: `tests/integration/defs/test_e2e.py`_
- **2026-11-05** [`adab54f2b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/adab54f2b6) [#21606](https://github.com/NVIDIA/TensorRT-LLM/pull/21606)
  [None][fix] perf-sanity: let the multi-frontend port reservation pass the trtllm-serve launcher probe (#21606)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/others/test_perf_sanity_port_reservation.py`_
- **2026-11-03** [`508f8dddef`](https://github.com/NVIDIA/TensorRT-LLM/commit/508f8dddef) [#21550](https://github.com/NVIDIA/TensorRT-LLM/pull/21550)
  [https://nvbugs/7013279][fix] Set host_cache_size 0 for the GB300 Nemotron-Ultra-V3 TEP4 MTP6 perf case (#21550)
  _Files: `tests/scripts/perf-sanity/aggregated/gb300_nemotron_ultra_v3_fp4_grace_blackwell.yaml`_
- **2026-11-03** [`1dbdc2162d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dbdc2162d) [#21487](https://github.com/NVIDIA/TensorRT-LLM/pull/21487)
  [None][fix] Visual-Gen Rubin Bringup - Extend three MiniMax-H3 E2E timeouts to 60 minutes (#21487)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-11-03** [`188df5f8c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/188df5f8c2) [#21302](https://github.com/NVIDIA/TensorRT-LLM/pull/21302)
  [https://nvbugs/6949274][fix] Give five QA list cases bounds that cover a cold checkpoint read (#21302)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-11-03** [`64da3ac140`](https://github.com/NVIDIA/TensorRT-LLM/commit/64da3ac140) [#20907](https://github.com/NVIDIA/TensorRT-LLM/pull/20907)
  [TRTLLM-16460][feat] agent-flow: unified trtllm_modeling_v2 workflow for gated ModelingV2 onboarding and perf tuning (#20907)
- **2026-11-03** [`c67c0f4fbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/c67c0f4fbe) [#20501](https://github.com/NVIDIA/TensorRT-LLM/pull/20501)
  [https://nvbugs/6944606][fix] Recognize Rubin GPUs in VisualGen performance tests (#20501)
  _Files: `tests/integration/defs/perf/test_visual_gen_perf_sanity.py`, `tests/scripts/perf-sanity/visual_gen/ltx2_blackwell.yaml`_
- **2026-11-02** [`687dc98aee`](https://github.com/NVIDIA/TensorRT-LLM/commit/687dc98aee) [#21384](https://github.com/NVIDIA/TensorRT-LLM/pull/21384)
  [None][fix] Correctly select zsh in devcontainer (#21384)
  _Files: `.devcontainer/devcontainer.json`_
- **2026-11-02** [`25e52e988a`](https://github.com/NVIDIA/TensorRT-LLM/commit/25e52e988a) [#21411](https://github.com/NVIDIA/TensorRT-LLM/pull/21411)
  [TRTLLM-17556][test] Run every harmony parsing unit test in the CPU stage (#21411)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`_
- **2026-11-02** [`b1352a7919`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1352a7919) [#21413](https://github.com/NVIDIA/TensorRT-LLM/pull/21413)
  [TRTLLM-17557][test] Run the SMG single-frontend guard test in the CPU stage (#21413)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`_
- **2026-11-02** [`b03b1e0ee3`](https://github.com/NVIDIA/TensorRT-LLM/commit/b03b1e0ee3) [#19907](https://github.com/NVIDIA/TensorRT-LLM/pull/19907)
  [https://nvbugs/6842275][fix] Normalize unittest parallel-config keys (#19907)
  _Files: `tests/integration/defs/test_unittests.py`, `tests/unittest/tools/test_unittest_culprits.py`_

## ROCm / AMD  (8 commits)

- **2026-11-07** [`9484c59210`](https://github.com/NVIDIA/TensorRT-LLM/commit/9484c59210) [#21538](https://github.com/NVIDIA/TensorRT-LLM/pull/21538)
  [None][fix] Port native disaggregation KV result report token - #20723 (#21538)
  _Files: `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/native/rank_info.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/_torch/disaggregation/test_disagg_idle_cancellation.py` _+13 more__
- **2026-11-04** [`ee1e8e4645`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee1e8e4645) [#20843](https://github.com/NVIDIA/TensorRT-LLM/pull/20843)
  [None][chore] Mass merge release/1.3 branch back to main (batch 2) (#20843)
  _Files: `cpp/kernels/fmha_v2/setup.py`, `cpp/tensorrt_llm/common/ncclUtils.cpp`, `cpp/tensorrt_llm/common/ncclUtils.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.cpp` _+89 more__
- **2026-11-04** [`a324344095`](https://github.com/NVIDIA/TensorRT-LLM/commit/a324344095) [#21661](https://github.com/NVIDIA/TensorRT-LLM/pull/21661)
  [TRTLLM-17615][fix] Initialize ownership in peer rejection test (#21661)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/disaggregated/test_peer.py`_
- **2026-11-04** [`b5fb1e2ef4`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5fb1e2ef4) [#18913](https://github.com/NVIDIA/TensorRT-LLM/pull/18913)
  [None][feat] Add opt-in disaggregated transfer diagnostics (#18913)
  _Files: `docs/source/features/disagg-serving.md`, `scripts/disagg_transfer_diagnostics.py`, `tensorrt_llm/_torch/disaggregation/diagnostics.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py` _+11 more__
- **2026-11-03** [`da980cce47`](https://github.com/NVIDIA/TensorRT-LLM/commit/da980cce47) [#20708](https://github.com/NVIDIA/TensorRT-LLM/pull/20708)
  [None][feat] Attribute KV transfer timeouts to deadline owners and observed progress (#20708)
  _Files: `tensorrt_llm/_torch/disaggregation/native/ownership.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py` _+4 more__
- **2026-11-03** [`09388e986d`](https://github.com/NVIDIA/TensorRT-LLM/commit/09388e986d) [#21521](https://github.com/NVIDIA/TensorRT-LLM/pull/21521)
  [None][chore] Refine infra ownership for tests, vendoring, and Jenkins maintenance (#21521)
  _Files: `.github/CODEOWNERS`_
- **2026-11-03** [`db98553909`](https://github.com/NVIDIA/TensorRT-LLM/commit/db98553909) [#21272](https://github.com/NVIDIA/TensorRT-LLM/pull/21272)
  [None][feat] Protect direct BF16 context-first KV transfers (#21272)
  _Files: `docs/source/features/disagg-serving.md`, `tensorrt_llm/_torch/disaggregation/kv_cache_transceiver.py`, `tensorrt_llm/_torch/disaggregation/native/context_first_profile.py`, `tensorrt_llm/_torch/disaggregation/native/rank_info.py` _+13 more__
- **2026-11-02** [`a9be7004c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9be7004c7) [#20049](https://github.com/NVIDIA/TensorRT-LLM/pull/20049)
  [None][chore] Remove the Python KV bounce buffer; kv_cache_bounce_size_mb selects the C++ agent bounce (#20049)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/bounce/BounceConfig.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/bounce/BounceTransport.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.cpp` _+87 more__

## Models  (7 commits)

- **2026-11-09** [`769cdb1b78`](https://github.com/NVIDIA/TensorRT-LLM/commit/769cdb1b78) [#21876](https://github.com/NVIDIA/TensorRT-LLM/pull/21876)
  [https://nvbugs/7061740][fix] Update Qwen3.5 checkpoint loader test API (#21876)
  _Files: `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl.py`_
- **2026-11-08** [`b433473ba0`](https://github.com/NVIDIA/TensorRT-LLM/commit/b433473ba0) [#21874](https://github.com/NVIDIA/TensorRT-LLM/pull/21874)
  [https://nvbugs/7047852][fix] Use the default dtype in the Kimi K3 modeling_v2 GSM8K tests (#21874)
  _Files: `tests/integration/defs/accuracy/modeling_v2/test_kimi_k3_vl.py`_
- **2026-11-06** [`13ff76e614`](https://github.com/NVIDIA/TensorRT-LLM/commit/13ff76e614) [#21766](https://github.com/NVIDIA/TensorRT-LLM/pull/21766)
  [https://nvbugs/6921831][test] Add Gemma4 multi-image encoder budget test (#21766)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-11-04** [`19c1f46acc`](https://github.com/NVIDIA/TensorRT-LLM/commit/19c1f46acc) [#21063](https://github.com/NVIDIA/TensorRT-LLM/pull/21063)
  [None][test] Add coverage for DeepseekV41ForConditionalGeneration (#21063)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modeling/test_modeling_deepseekv41_multimodal.py`_
- **2026-11-04** [`8dc9ef5c2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8dc9ef5c2b) [#21504](https://github.com/NVIDIA/TensorRT-LLM/pull/21504)
  [None][test] Add coverage for KimiK25ForConditionalGeneration (#21504)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_kimi_k25.py`_
- **2026-11-04** [`8b502a8218`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b502a8218) [#21505](https://github.com/NVIDIA/TensorRT-LLM/pull/21505)
  [None][test] Add coverage for KimiK3ForConditionalGeneration (#21505)
  _Files: `tests/unittest/_torch/modeling/test_kimi_k3_config_routing.py`_
- **2026-11-02** [`a962b94f2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a962b94f2b) [#21339](https://github.com/NVIDIA/TensorRT-LLM/pull/21339)
  [None][chore] Reject per-layer KV-head configs in the generic HF weight mapper (#21339)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/gemma4_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3vl_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_mapper.py` _+1 more__

## Docs / Examples  (5 commits)

- **2026-11-09** [`1932b8ee59`](https://github.com/NVIDIA/TensorRT-LLM/commit/1932b8ee59) [#21397](https://github.com/NVIDIA/TensorRT-LLM/pull/21397)
  [TRTLLM-17163][test] Muse Spark Open stress settings and disagg cancellation marathon attach mode (#21397)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/configs/README.md`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_disagg_cancel_stress.py`, `tests/integration/defs/stress_test/stress_test.py` _+1 more__
- **2026-11-06** [`7581ea9c4b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7581ea9c4b)
  [None][chore] Bump version to 1.4.0rc4
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/schemas/trtllm-serve-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-disagg-config.schema.json` _+2 more__
- **2026-11-03** [`5d05cf4cb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d05cf4cb9) [#21436](https://github.com/NVIDIA/TensorRT-LLM/pull/21436)
  [https://nvbugs/7029761][docs] Qualify dynamic-tree sliding-window compatibility (#21436)
  _Files: `docs/source/features/feature-combination-matrix.md`_
- **2026-11-03** [`a694d9720f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a694d9720f) [#21355](https://github.com/NVIDIA/TensorRT-LLM/pull/21355)
  [https://nvbugs/6888945][fix] Use TRTLLM-generated FastWan LPIPS golden (#21355)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/fastwan_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media_wan.zip`_
- **2026-11-03** [`94b58a6cac`](https://github.com/NVIDIA/TensorRT-LLM/commit/94b58a6cac) [#21435](https://github.com/NVIDIA/TensorRT-LLM/pull/21435)
  [https://nvbugs/7029760][docs] Split parallelism YAML into independent examples (#21435)
  _Files: `docs/source/features/parallel-strategy.md`_

## Speculative Decoding  (4 commits)

- **2026-11-06** [`e3ba6236c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3ba6236c1) [#21596](https://github.com/NVIDIA/TensorRT-LLM/pull/21596)
  [TRTLLM-14620][feat] Add device re-ranking for DSpark confidence scheduling (#21596)
  _Files: `examples/models/core/deepseek_v4/README.md`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+12 more__
- **2026-11-05** [`877b6ea207`](https://github.com/NVIDIA/TensorRT-LLM/commit/877b6ea207) [#21424](https://github.com/NVIDIA/TensorRT-LLM/pull/21424)
  [None][perf] strict_accept: one compiled variant for every batch (#21424)
  _Files: `tensorrt_llm/_torch/speculative/spec_tail_kernels.py`, `tests/unittest/_torch/speculative/test_spec_tail_kernels.py`_
- **2026-11-03** [`63ef35ea7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/63ef35ea7e) [#20078](https://github.com/NVIDIA/TensorRT-LLM/pull/20078)
  [TRTLLM-14620][feat] Enable opt-in DSpark decode confidence scheduling (#20078)
  _Files: `examples/models/core/deepseek_v4/README.md`, `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/models/modeling_dspark_v41.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+38 more__
- **2026-11-02** [`1926cfdccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1926cfdccf) [#21331](https://github.com/NVIDIA/TensorRT-LLM/pull/21331)
  [None][test] Add DGX Spark agentic and real-text speculative decoding perf cases (#21331)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_spark_perf.yml`_

## Perf  (2 commits)

- **2026-11-06** [`f693627747`](https://github.com/NVIDIA/TensorRT-LLM/commit/f693627747) [#21380](https://github.com/NVIDIA/TensorRT-LLM/pull/21380)
  [None][feat] Staircase: Rubin GLM Optimized Low Latency (Conc up to 56) (#21380)
- **2026-11-03** [`90ca55292b`](https://github.com/NVIDIA/TensorRT-LLM/commit/90ca55292b) [#21502](https://github.com/NVIDIA/TensorRT-LLM/pull/21502)
  [None][fix] revert git pin in 8f04d3a (#21502)
  _Files: `requirements-dev.txt`, `tests/integration/defs/kv_cache/test_prefix_aware_scheduling.py`_

## LoRA  (2 commits)

- **2026-11-03** [`4889d70f66`](https://github.com/NVIDIA/TensorRT-LLM/commit/4889d70f66) [#21176](https://github.com/NVIDIA/TensorRT-LLM/pull/21176)
  [TRTLLM-17273][chore] Remove dead code in trtllm-serve ahead of the module moves (#21176)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/_perf_metrics_schema.py`, `tensorrt_llm/serve/disagg_coordinator.py`, `tensorrt_llm/serve/harmony_adapter.py` _+6 more__
- **2026-11-02** [`2fc420cd6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fc420cd6c) [#21106](https://github.com/NVIDIA/TensorRT-LLM/pull/21106)
  [None][fix] Anthropic Messages: name the json_schema built from output_config.format (#21106)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_

---
_Generated 2026-11-09 18:49 UTC_