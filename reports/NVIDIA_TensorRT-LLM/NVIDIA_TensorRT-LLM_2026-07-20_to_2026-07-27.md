# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-07-20 → 2026-07-27  |  **Total commits:** 180

## ✨ New Features This Week

- **2026-07-27** [#16830](https://github.com/NVIDIA/TensorRT-LLM/pull/16830) — [None][feat] Add kimi_k2/glm_5 grouped routing and fused router to bench_moe (#16830)
- **2026-07-27** [#16355](https://github.com/NVIDIA/TensorRT-LLM/pull/16355) — [TRTLLM-13642][feat] Add perf sanity tests for Llama-3.1-8B and Gemma-3-1B and verify cache transceiver V2 support (#16355)
- **2026-07-26** [#16774](https://github.com/NVIDIA/TensorRT-LLM/pull/16774) — [None][feat] Support DeepSeek-V4 in layer_wise_benchmarks (#16774)
- **2026-07-24** [#15597](https://github.com/NVIDIA/TensorRT-LLM/pull/15597) — [https://nvbugs/6020038][feat] Add NCCL-EP v0.1 MoE communication support (#15597)
- **2026-07-24** [#16795](https://github.com/NVIDIA/TensorRT-LLM/pull/16795) — [None][test] Enable gen_only + ctx_only DeepSeek-V4-Pro perf-sanity on GB300 (#16795)
- **2026-07-24** [#16719](https://github.com/NVIDIA/TensorRT-LLM/pull/16719) — [TRTLLM-14512][feat] multiprocess disagg server prometheus client (#16719)
- **2026-07-24** [#15871](https://github.com/NVIDIA/TensorRT-LLM/pull/15871) — [None][feat] align time metrics between cpp and python cache transceiver (#15871)
- **2026-07-24** [#16828](https://github.com/NVIDIA/TensorRT-LLM/pull/16828) — [None][feat] Add support for MiniMax M3 and Qwen3.6 models in performance tests (#16828)
- **2026-07-24** [#16344](https://github.com/NVIDIA/TensorRT-LLM/pull/16344) — [TRTLLM-13948][test] Add DeepSeek R1/V3.2/V3-Lite disaggregated accuracy tests (#16344)
- **2026-07-24** [#16718](https://github.com/NVIDIA/TensorRT-LLM/pull/16718) — [None][test] Declare supported attention test phases (#16718)
- _…and 34 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#16826](https://github.com/NVIDIA/TensorRT-LLM/issues/16826) | [Bug]: SA (Suffix Automaton) speculative decoding crashes the executor | bug, Inference runtime, Speculative Decoding | 2026-07-27 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-07-25 |
| [#16827](https://github.com/NVIDIA/TensorRT-LLM/issues/16827) | [Performance]: MAX_UTILIZATION causes a 40.6% output-throughput drop a | KV-Cache Management, Pytorch, General perf | 2026-07-25 |
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
| [#3889](https://github.com/NVIDIA/TensorRT-LLM/issues/3889) | whisper tensorrt-llm drop the model accuracy | bug, Model customization, OOTB | 2025-12-20 |
| [#10024](https://github.com/NVIDIA/TensorRT-LLM/issues/10024) | [Bug] TRTLLM_NIXL_KVCACHE_BACKEND causes rail endpoint serialization m | KV-Cache Management, Disaggregated serving | 2025-12-16 |
| [#10014](https://github.com/NVIDIA/TensorRT-LLM/issues/10014) | [Documentation] AWS EFA/LIBFABRIC deployment guide for disaggregated i | Doc, Disaggregated serving | 2025-12-15 |
| [#3125](https://github.com/NVIDIA/TensorRT-LLM/issues/3125) | Model built with ReDrafter produces substantially lower quality output | bug, triaged, Investigating, Speculative Decoding, Model customization | 2025-09-09 |
| [#2864](https://github.com/NVIDIA/TensorRT-LLM/issues/2864) | Could not run on a machine with dual RTX 5090s, using WSL2 and Docker | bug, triaged, Investigating, Scale-out, Testing | 2025-09-09 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 53 |
| Attention | 32 |
| Executor / Runtime | 20 |
| MoE | 16 |
| Disaggregation / KV | 16 |
| Models | 13 |
| Quantization | 12 |
| Torch Path (_torch) | 6 |
| Speculative Decoding | 4 |
| Other | 3 |
| Perf | 3 |
| Compilation / Graph | 1 |
| Docs / Examples | 1 |

## CI / Infra  (53 commits)

- **2026-07-27** [`1ae9b86f12`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ae9b86f12) [#16882](https://github.com/NVIDIA/TensorRT-LLM/pull/16882)
  [None][infra] Waive 21 failed cases for main in post-merge 2862 (#16882)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-27** [`9129f4eaf5`](https://github.com/NVIDIA/TensorRT-LLM/commit/9129f4eaf5)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-24** [`56dedb14ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/56dedb14ff) [#16821](https://github.com/NVIDIA/TensorRT-LLM/pull/16821)
  [None][infra] Waive 14 failed cases for main in post-merge 2855 (#16821)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-24** [`cf492257a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf492257a8) [#16784](https://github.com/NVIDIA/TensorRT-LLM/pull/16784)
  [None][infra] Fix release check failure for .test_durations (#16784)
  _Files: `jenkins/UpdateTestDurations.groovy`, `jenkins/scripts/generate_duration.py`, `tests/integration/defs/.test_durations`_
- **2026-07-24** [`e5287d6080`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5287d6080) [#16819](https://github.com/NVIDIA/TensorRT-LLM/pull/16819)
  [None][infra] Waive 2 failed cases for main in pre-merge 49489 (#16819)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-24** [`35134c2793`](https://github.com/NVIDIA/TensorRT-LLM/commit/35134c2793) [#16808](https://github.com/NVIDIA/TensorRT-LLM/pull/16808)
  [None][infra] Unwaive test_proxy_fast_death tests (#16808)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`f4e692d219`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4e692d219) [#16798](https://github.com/NVIDIA/TensorRT-LLM/pull/16798)
  [None][infra] Waive 4 failed cases for main in pre-merge 49550 (#16798)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`a47577ac86`](https://github.com/NVIDIA/TensorRT-LLM/commit/a47577ac86) [#16786](https://github.com/NVIDIA/TensorRT-LLM/pull/16786)
  [None][infra] Waive 1 failed cases for main in pre-merge 49229 (#16786)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`3867b2a503`](https://github.com/NVIDIA/TensorRT-LLM/commit/3867b2a503) [#16780](https://github.com/NVIDIA/TensorRT-LLM/pull/16780)
  [None][infra] Waive 1 failed cases for main in pre-merge 49424 (#16780)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`c6e0c98aca`](https://github.com/NVIDIA/TensorRT-LLM/commit/c6e0c98aca) [#16781](https://github.com/NVIDIA/TensorRT-LLM/pull/16781)
  [None][infra] Waive 1 failed cases for main in pre-merge 49424 (#16781)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`3d86c7286c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d86c7286c) [#16777](https://github.com/NVIDIA/TensorRT-LLM/pull/16777)
  [TRTLLMINF-188][infra] Require approval for PerfSanity wildcard runs (#16777)
  _Files: `.github/workflows/bot-command.yml`, `docs/source/developer-guide/ci-overview.md`_
- **2026-07-23** [`7418b69a19`](https://github.com/NVIDIA/TensorRT-LLM/commit/7418b69a19) [#16758](https://github.com/NVIDIA/TensorRT-LLM/pull/16758)
  [None][infra] Preview/bump/main (#16758)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-07-22** [`c1483b917a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1483b917a) [#16557](https://github.com/NVIDIA/TensorRT-LLM/pull/16557)
  [TRTLLMINF-102][fix] Surface SLURM device faults to the failure classifier (#16557)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-22** [`f9c253ed32`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9c253ed32) [#16610](https://github.com/NVIDIA/TensorRT-LLM/pull/16610)
  [TRTLLM-14473][chore] Remove legacy TensorRT backend tests examples and CI plumbing (#16610)
- **2026-07-22** [`ea504d1b51`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea504d1b51)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`_
- **2026-07-22** [`8e2816bf67`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e2816bf67) [#16698](https://github.com/NVIDIA/TensorRT-LLM/pull/16698)
  [None][infra] Waive 1 failed cases for main in pre-merge 49101 (#16698)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-22** [`56f28cd7af`](https://github.com/NVIDIA/TensorRT-LLM/commit/56f28cd7af) [#16608](https://github.com/NVIDIA/TensorRT-LLM/pull/16608)
  [TRTLLM-14027][infra] Remove --trt_root and stop installing the TensorRT SDK into images (#16608)
  _Files: `.claude/skills/exec-local-compile/SKILL.md`, `.claude/skills/exec-slurm-compile/SKILL.md`, `.claude/skills/exec-slurm-compile/scripts/compile.sh`, `docker/Dockerfile.multi` _+8 more__
- **2026-07-22** [`412768dfe7`](https://github.com/NVIDIA/TensorRT-LLM/commit/412768dfe7) [#16700](https://github.com/NVIDIA/TensorRT-LLM/pull/16700)
  [None][infra] Waive 21 failed cases for main in post-merge 2850 (#16700)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`c988141a85`](https://github.com/NVIDIA/TensorRT-LLM/commit/c988141a85) [#16682](https://github.com/NVIDIA/TensorRT-LLM/pull/16682)
  [None][infra] Waive 2 failed cases for main in pre-merge 48918 (#16682)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`a75e333c85`](https://github.com/NVIDIA/TensorRT-LLM/commit/a75e333c85) [#16551](https://github.com/NVIDIA/TensorRT-LLM/pull/16551)
  [None][infra] Add per-stage opt to cap/disable stage-level infra retries (#16551)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-21** [`306c8ced74`](https://github.com/NVIDIA/TensorRT-LLM/commit/306c8ced74) [#16675](https://github.com/NVIDIA/TensorRT-LLM/pull/16675)
  [None][infra] Waive 2 failed cases for main in pre-merge 30273 (#16675)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`58298adee3`](https://github.com/NVIDIA/TensorRT-LLM/commit/58298adee3) [#16658](https://github.com/NVIDIA/TensorRT-LLM/pull/16658)
  [TRTLLM-12838][infra] CBTS coverage db audit (#16658)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/coverage_selection/artifact.py`, `jenkins/scripts/cbts/coverage_selection/touch_db.py`, `jenkins/scripts/cbts/tools/coverage_audit.py`_
- **2026-07-21** [`d75cb89a0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d75cb89a0e) [#15602](https://github.com/NVIDIA/TensorRT-LLM/pull/15602)
  [None][infra] Add support to run NGC container scanning in pre-merge (#15602)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-07-21** [`8597530bb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/8597530bb9) [#16665](https://github.com/NVIDIA/TensorRT-LLM/pull/16665)
  [None][infra] fix lfs sync failure (#16665)
  _Files: `.github/workflows/lfs-sync.yml`_
- **2026-07-21** [`9ca56ae77c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ca56ae77c) [#16257](https://github.com/NVIDIA/TensorRT-LLM/pull/16257)
  [None][fix] use explicit errors instead of asserts for real-dataset input (#16257)
  _Files: `tensorrt_llm/bench/dataset/prepare_real_data.py`_
- **2026-07-21** [`3e76376959`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e76376959) [#16660](https://github.com/NVIDIA/TensorRT-LLM/pull/16660)
  [None][infra] Waive 1 failed cases for main in pre-merge 48840 (#16660)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`25f952ba11`](https://github.com/NVIDIA/TensorRT-LLM/commit/25f952ba11) [#16655](https://github.com/NVIDIA/TensorRT-LLM/pull/16655)
  [https://nvbugs/6463814][chore] Unwaive passing perf-sanity disagg tests (#16655)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`c67d0989bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/c67d0989bb) [#16625](https://github.com/NVIDIA/TensorRT-LLM/pull/16625)
  [None][test] Waive hang issues (#16625)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`be77b170e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/be77b170e1) [#16542](https://github.com/NVIDIA/TensorRT-LLM/pull/16542)
  [None][test] remove MiniMax-M2 tp16 multinode eval test case (#16542)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_multinode.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`31d9bfff6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/31d9bfff6b) [#16654](https://github.com/NVIDIA/TensorRT-LLM/pull/16654)
  [None][test] Waive 2 failed cases for main in QA CI (#16654)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`90dbe95d8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/90dbe95d8d) [#16638](https://github.com/NVIDIA/TensorRT-LLM/pull/16638)
  [https://nvbugs/6475622][chore] Unwaive tests (#16638)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`6df6cfc6f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/6df6cfc6f5) [#16268](https://github.com/NVIDIA/TensorRT-LLM/pull/16268)
  [TRTLLMINF-191][infra] Preserve pytest progress with S3 capture (#16268)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/conftest.py`, `tests/integration/defs/pytest.ini`, `tests/integration/defs/test_unittests.py` _+6 more__
- **2026-07-20** [`eb3a7d9f9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb3a7d9f9a) [#16631](https://github.com/NVIDIA/TensorRT-LLM/pull/16631)
  [None][infra] Waive 2 failed cases for main in pre-merge 48727 (#16631)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`5d8a78662f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d8a78662f) [#16622](https://github.com/NVIDIA/TensorRT-LLM/pull/16622)
  [None][test] Waive 1 failed cases for main in QA CI (#16622)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`8bb0c50236`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bb0c50236) [#16591](https://github.com/NVIDIA/TensorRT-LLM/pull/16591)
  [https://nvbugs/6305365][chore] Unwaive piecewise cudagraph related tests (#16591)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`24ae9f4659`](https://github.com/NVIDIA/TensorRT-LLM/commit/24ae9f4659) [#16615](https://github.com/NVIDIA/TensorRT-LLM/pull/16615)
  [None][infra] Waive 1 failed cases for main in pre-merge 48660 (#16615)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`b8604c46ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8604c46ce)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-20** [`a857096693`](https://github.com/NVIDIA/TensorRT-LLM/commit/a857096693) [#16606](https://github.com/NVIDIA/TensorRT-LLM/pull/16606)
  [TRTQA-3278][test] Waive 6 failed cases for main in QA CI (#16606)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`910426f950`](https://github.com/NVIDIA/TensorRT-LLM/commit/910426f950) [#16607](https://github.com/NVIDIA/TensorRT-LLM/pull/16607)
  [TRTQA-3276][test] Waive 3 failed cases for main in QA CI (#16607)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`32110a8544`](https://github.com/NVIDIA/TensorRT-LLM/commit/32110a8544) [#16600](https://github.com/NVIDIA/TensorRT-LLM/pull/16600)
  [None][test] Waive 3 failed cases for main in QA CI (#16600)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`9955555c6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/9955555c6e) [#16604](https://github.com/NVIDIA/TensorRT-LLM/pull/16604)
  [TRTQA-3279][test] Waive 8 failed cases for main in QA CI (#16604)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`af4aff4220`](https://github.com/NVIDIA/TensorRT-LLM/commit/af4aff4220) [#16605](https://github.com/NVIDIA/TensorRT-LLM/pull/16605)
  [None][test] Waive 7 failed cases for main in QA CI (#16605)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`454fed35cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/454fed35cc) [#16480](https://github.com/NVIDIA/TensorRT-LLM/pull/16480)
  [TRTLLMINF-216][infra] use main as default target branch in L0_MergeRequest_PR (#16480)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-07-20** [`5ebcda8c76`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ebcda8c76) [#16602](https://github.com/NVIDIA/TensorRT-LLM/pull/16602)
  [None][test] Waive 7 failed cases for main in QA CI (#16602)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`d42e391e0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d42e391e0c) [#16599](https://github.com/NVIDIA/TensorRT-LLM/pull/16599)
  [None][test] Waive 1 failed cases for main in QA CI (#16599)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`447a628c30`](https://github.com/NVIDIA/TensorRT-LLM/commit/447a628c30) [#16576](https://github.com/NVIDIA/TensorRT-LLM/pull/16576)
  [None][test] Remove 33 closed-bug waive entries for main (#16576)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`826922f147`](https://github.com/NVIDIA/TensorRT-LLM/commit/826922f147) [#16593](https://github.com/NVIDIA/TensorRT-LLM/pull/16593)
  [None][test] Waive 2 failed cases for main in QA CI (#16593)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`3fe4ceb9bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fe4ceb9bc) [#16587](https://github.com/NVIDIA/TensorRT-LLM/pull/16587)
  [None][infra] Waive 5 failed cases for main in post-merge 2844 (#16587)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`3ab71753fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ab71753fe) [#16584](https://github.com/NVIDIA/TensorRT-LLM/pull/16584)
  [None][test] Waive 4 failed cases for main in QA CI (#16584)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`7941475e7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7941475e7e) [#16585](https://github.com/NVIDIA/TensorRT-LLM/pull/16585)
  [None][test] Waive 3 failed cases for main in QA CI (#16585)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`fd4548572f`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd4548572f) [#16582](https://github.com/NVIDIA/TensorRT-LLM/pull/16582)
  [None][infra] Waive 1 failed cases for main in pre-merge 48569 (#16582)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`c253e57976`](https://github.com/NVIDIA/TensorRT-LLM/commit/c253e57976)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-20** [`cf4973d70e`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf4973d70e)
  [None][infra] Auto-update test durations from OpenSearch (last 3 days)
  _Files: `tests/integration/defs/.test_durations`_

## Attention  (32 commits)

- **2026-07-27** [`151db5de6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/151db5de6e) [#15123](https://github.com/NVIDIA/TensorRT-LLM/pull/15123)
  [https://nvbugs/6157892][fix] Mistral format refactor (#15123)
  _Files: `examples/llm-api/quickstart_advanced.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/checkpoints/mistral/config_loader.py` _+12 more__
- **2026-07-27** [`d12c85e62b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d12c85e62b) [#16838](https://github.com/NVIDIA/TensorRT-LLM/pull/16838)
  [https://nvbugs/6507109][infra] Split slow DGX B300 attention unit tests (#16838)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b300.yml`_
- **2026-07-27** [`9de6c94798`](https://github.com/NVIDIA/TensorRT-LLM/commit/9de6c94798) [#16789](https://github.com/NVIDIA/TensorRT-LLM/pull/16789)
  [None][perf] Skip DeepGEMM clean_logits in DSA indexer prefill on custom top-k path (#16789)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`_
- **2026-07-25** [`cf44a1ccee`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf44a1ccee) [#16505](https://github.com/NVIDIA/TensorRT-LLM/pull/16505)
  [https://nvbugs/6465993][fix] use attention cache dtype for disaggregated transfer (#16505)
  _Files: `cpp/tensorrt_llm/batch_manager/cacheFormatter.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.h`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp` _+1 more__
- **2026-07-24** [`4d066d3d98`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d066d3d98) [#16743](https://github.com/NVIDIA/TensorRT-LLM/pull/16743)
  [None][fix] Do not treat a bare fmha_v2_cu directory as completed generation (#16743)
  _Files: `scripts/build_wheel.py`_
- **2026-07-24** [`c1f78d9af1`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1f78d9af1) [#16532](https://github.com/NVIDIA/TensorRT-LLM/pull/16532)
  [None][perf] Fuse DeepSeek-V4 Indexer Q projection with CuTe DSL (#16532)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.h`, `cpp/tensorrt_llm/thop/fp8Quantize.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py` _+7 more__
- **2026-07-24** [`8a6cb4432c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a6cb4432c) [#16718](https://github.com/NVIDIA/TensorRT-LLM/pull/16718)
  [None][test] Declare supported attention test phases (#16718)
  _Files: `tests/unittest/_torch/attention/model_attn_config.py`, `tests/unittest/_torch/attention/test_attention_backends.py`_
- **2026-07-24** [`929f153ea6`](https://github.com/NVIDIA/TensorRT-LLM/commit/929f153ea6) [#13055](https://github.com/NVIDIA/TensorRT-LLM/pull/13055)
  [TRTLLM-9920][feat] Add support for arbitrary KVCache transfer (#13055)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/executor/dataTransceiverState.h`, `cpp/tensorrt_llm/batch_manager/cacheFormatter.cpp` _+23 more__
- **2026-07-24** [`29919947fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/29919947fc) [#16734](https://github.com/NVIDIA/TensorRT-LLM/pull/16734)
  [None][perf] Avoid implicit device-scalar syncs in DeepSeek-V4 ctx sparse metadata (#16734)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_compressor_module.py`_
- **2026-07-23** [`d95f66541d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d95f66541d) [#16757](https://github.com/NVIDIA/TensorRT-LLM/pull/16757)
  [None][fix] Stage DSA indexer block_table H2D through pinned memory (#16757)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`_
- **2026-07-23** [`77774d9121`](https://github.com/NVIDIA/TensorRT-LLM/commit/77774d9121) [#16732](https://github.com/NVIDIA/TensorRT-LLM/pull/16732)
  [None][fix] Make FlashInfer sampling op wrappers opaque to Dynamo (#16732)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`_
- **2026-07-23** [`a1c6908dac`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1c6908dac) [#16420](https://github.com/NVIDIA/TensorRT-LLM/pull/16420)
  [None][feat] top-k: route decode to CuTe DSL GVR top-k in e2e (#16420)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+1 more__
- **2026-07-23** [`8041493cf6`](https://github.com/NVIDIA/TensorRT-LLM/commit/8041493cf6) [#16017](https://github.com/NVIDIA/TensorRT-LLM/pull/16017)
  [TRTLLM-13969][feat] Support MiniMax M3 for Disaggregated Serving (#16017)
  _Files: `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/common/envUtils.cpp`, `cpp/tensorrt_llm/common/envUtils.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.cpp` _+32 more__
- **2026-07-23** [`0a401b4974`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a401b4974) [#16723](https://github.com/NVIDIA/TensorRT-LLM/pull/16723)
  [None][chore] Remove attention backend test waivers (#16723)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`a19410ebaa`](https://github.com/NVIDIA/TensorRT-LLM/commit/a19410ebaa) [#16703](https://github.com/NVIDIA/TensorRT-LLM/pull/16703)
  [TRTLLM-14540][perf] Skip fp32 state round-trip in FlashInfer GDN pre… (#16703)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/fla/fused_state_io.py`_
- **2026-07-22** [`45d1c111ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/45d1c111ec) [#16291](https://github.com/NVIDIA/TensorRT-LLM/pull/16291)
  [TRTLLM-14019][feat] Add MiniMax-M3 MSA sparse attention backend [revised] (#16291)
  _Files: `.gitmodules`, `3rdparty/MSA`, `LICENSE`, `jenkins/Build.groovy` _+37 more__
- **2026-07-22** [`9cd6a493bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cd6a493bf) [#16069](https://github.com/NVIDIA/TensorRT-LLM/pull/16069)
  [https://nvbugs/6422318][fix] Cast cos_sin_cache to float32 at cat-time to satisfy flashinfer's contract… (#16069)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-22** [`7965292b63`](https://github.com/NVIDIA/TensorRT-LLM/commit/7965292b63) [#16709](https://github.com/NVIDIA/TensorRT-LLM/pull/16709)
  [https://nvbugs/6468821][infra] Split slow B300 attention unit tests (#16709)
  _Files: `tests/integration/test_lists/test-db/l0_b300.yml`_
- **2026-07-22** [`858fd17b79`](https://github.com/NVIDIA/TensorRT-LLM/commit/858fd17b79) [#15582](https://github.com/NVIDIA/TensorRT-LLM/pull/15582)
  [None][feat] Support Nemotron dynamic-tree MTP decoding (#15582)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/xqaParams.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h` _+19 more__
- **2026-07-22** [`697738c1f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/697738c1f6) [#16545](https://github.com/NVIDIA/TensorRT-LLM/pull/16545)
  [https://nvbugs/6438658][fix] Fix KV cache estimation capacity (#16545)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/llmapi/llm_args.py` _+3 more__
- **2026-07-21** [`257c8e0657`](https://github.com/NVIDIA/TensorRT-LLM/commit/257c8e0657) [#14875](https://github.com/NVIDIA/TensorRT-LLM/pull/14875)
  [TRTLLM-13117][feat] Implement Uneven TP Linear for VisualGen models (#14875)
  _Files: `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`, `tensorrt_llm/_torch/visual_gen/models/flux/joint_proj.py` _+10 more__
- **2026-07-21** [`1780686625`](https://github.com/NVIDIA/TensorRT-LLM/commit/1780686625) [#16530](https://github.com/NVIDIA/TensorRT-LLM/pull/16530)
  [None][chore] Update flashinfer-python from 0.6.14 to 0.6.15 (#16530)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-07-21** [`27a5ab8cc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/27a5ab8cc9) [#16469](https://github.com/NVIDIA/TensorRT-LLM/pull/16469)
  [TRTLLM-14352][perf] Fuse Qwen3.5/3.6 attention preprocessing (QK-nor… (#16469)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/modules/attention.py`, `tensorrt_llm/_torch/modules/fused_ops/fused_qk_norm_rope_gate.py`, `tensorrt_llm/_torch/modules/qk_norm_attention.py` _+2 more__
- **2026-07-21** [`6fec819bcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/6fec819bcf) [#16319](https://github.com/NVIDIA/TensorRT-LLM/pull/16319)
  [None][fix] avoid attention workspace resize during CUDA graph capture (#16319)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-21** [`5749491cdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/5749491cdf) [#16544](https://github.com/NVIDIA/TensorRT-LLM/pull/16544)
  [None][feat] Support rejection sampling under attention DP (incl. LM-head TP) (#16544)
  _Files: `ruff-legacy-baseline.json`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/interface.py` _+3 more__
- **2026-07-21** [`dea4306f5b`](https://github.com/NVIDIA/TensorRT-LLM/commit/dea4306f5b) [#16616](https://github.com/NVIDIA/TensorRT-LLM/pull/16616)
  [https://nvbugs/6468821][chore] Unwaive GPT-OSS B300 attention backend test (#16616)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`bb90835f8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb90835f8a) [#16427](https://github.com/NVIDIA/TensorRT-LLM/pull/16427)
  [TRTLLM-11875][feat] Support fine-grained context chunk management (#16427)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/microBatchScheduler.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `cpp/tests/unit_tests/batch_manager/microBatchSchedulerTest.cpp` _+14 more__
- **2026-07-21** [`77cf89d99f`](https://github.com/NVIDIA/TensorRT-LLM/commit/77cf89d99f) [#16548](https://github.com/NVIDIA/TensorRT-LLM/pull/16548)
  [https://nvbugs/6451032][fix] Reserve extra dflash context slot for dummy requests (#16548)
  _Files: `tensorrt_llm/_torch/speculative/dflash.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/speculative/hw_agnostic/test_dflash.py`_
- **2026-07-20** [`c7871ca60d`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7871ca60d) [#15831](https://github.com/NVIDIA/TensorRT-LLM/pull/15831)
  [None][feat] VisualGen: Add CuTe DSL JIT kernels for FMHA (#15831)
  _Files: `.gitattributes`, `.gitignore`, `setup.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/__init__.py` _+78 more__
- **2026-07-20** [`6a5caee6ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/6a5caee6ae) [#16627](https://github.com/NVIDIA/TensorRT-LLM/pull/16627)
  [https://nvbugs/6473397][test] Raise BF16 Laguna DFlash memory skip threshold to prevent OOM (#16627)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`d94540b429`](https://github.com/NVIDIA/TensorRT-LLM/commit/d94540b429) [#16466](https://github.com/NVIDIA/TensorRT-LLM/pull/16466)
  [None][fix] Fix DeepSeek V4 KV cache warmup handling and serveral other issues (#16466)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+3 more__
- **2026-07-20** [`52ae70934f`](https://github.com/NVIDIA/TensorRT-LLM/commit/52ae70934f) [#16052](https://github.com/NVIDIA/TensorRT-LLM/pull/16052)
  [TRTLLM-13235][feat] Support bad_words in TorchSampler (#16052)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampling_utils.py` _+3 more__

## Executor / Runtime  (20 commits)

- **2026-07-27** [`b8ff548a5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8ff548a5f) [#16791](https://github.com/NVIDIA/TensorRT-LLM/pull/16791)
  [None][perf] prepare_inputs: avoid O(seq_len) get_tokens(0) marshalling on the host (#16791)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-24** [`e6b7bd0703`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6b7bd0703) [#16550](https://github.com/NVIDIA/TensorRT-LLM/pull/16550)
  [https://nvbugs/6432953][fix] Fix MPI world heap corruption during teardown (#16550)
  _Files: `cpp/tensorrt_llm/runtime/utils/mpiUtils.cpp`_
- **2026-07-24** [`58b9d1589d`](https://github.com/NVIDIA/TensorRT-LLM/commit/58b9d1589d) [#16686](https://github.com/NVIDIA/TensorRT-LLM/pull/16686)
  [None][perf] spec one-model sampling: greedy rows via top_k=1 instead of unconditional vocab argmax (#16686)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampling_utils.py`_
- **2026-07-24** [`37f59acbb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/37f59acbb5) [#16785](https://github.com/NVIDIA/TensorRT-LLM/pull/16785)
  [https://nvbugs/6485885][fix] Stop thinking-budget processor re-forcing the reasoning end tag (#16785)
  _Files: `tensorrt_llm/llmapi/thinking_budget.py`, `tests/unittest/llmapi/test_sampling_params.py`_
- **2026-07-23** [`526c1e3229`](https://github.com/NVIDIA/TensorRT-LLM/commit/526c1e3229) [#16634](https://github.com/NVIDIA/TensorRT-LLM/pull/16634)
  [https://nvbugs/6448152][perf] make C++ context-transfer consensus asynchronous (#16634)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/contextTransferCoordinator.h`, `cpp/include/tensorrt_llm/runtime/utils/mpiTags.h`, `cpp/include/tensorrt_llm/runtime/utils/mpiUtils.h` _+7 more__
- **2026-07-23** [`5a69240c9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a69240c9e) [#16159](https://github.com/NVIDIA/TensorRT-LLM/pull/16159)
  [None][feat] Bind SourceIdentity to checkpoint artifacts (#16159)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/artifact_identity.py`, `tensorrt_llm/_torch/weight_sharing/source_identity.py` _+8 more__
- **2026-07-23** [`83733c4d65`](https://github.com/NVIDIA/TensorRT-LLM/commit/83733c4d65) [#16422](https://github.com/NVIDIA/TensorRT-LLM/pull/16422)
  [None][chore] Add NVTX ranges to per-iteration ADP sync points in PyExecutor (#16422)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-07-23** [`93efd33bfb`](https://github.com/NVIDIA/TensorRT-LLM/commit/93efd33bfb) [#16294](https://github.com/NVIDIA/TensorRT-LLM/pull/16294)
  [None][feat] ADP conversation router: configurable least-queued placement for new conversations (#16294)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/usage/llm_args_golden_manifest.json`, `tests/unittest/_torch/executor/test_adp_router.py`_
- **2026-07-23** [`1d2e79ed27`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d2e79ed27) [#16761](https://github.com/NVIDIA/TensorRT-LLM/pull/16761)
  [https://nvbugs/6499882][fix] Seed _multi_frontend_ipc_dir in bare proxy test helper (#16761)
  _Files: `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-07-22** [`5e877639fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e877639fc) [#16184](https://github.com/NVIDIA/TensorRT-LLM/pull/16184)
  [TRTLLM-13231][feat] Support top_p_decay in the PyTorch TorchSampler (#16184)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampling_utils.py` _+2 more__
- **2026-07-22** [`c54538b05f`](https://github.com/NVIDIA/TensorRT-LLM/commit/c54538b05f) [#16630](https://github.com/NVIDIA/TensorRT-LLM/pull/16630)
  [https://nvbugs/6480574][fix] seed attrs bypassed by __new__ in pool session shutdown test (#16630)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-07-22** [`128d020489`](https://github.com/NVIDIA/TensorRT-LLM/commit/128d020489) [#16106](https://github.com/NVIDIA/TensorRT-LLM/pull/16106)
  [None][fix] Make auto host tier sizing rank-aware in KVCacheManagerV2 (#16106)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/test_kvv2_host_tier_sizing.py`_
- **2026-07-22** [`09e9738355`](https://github.com/NVIDIA/TensorRT-LLM/commit/09e9738355) [#16523](https://github.com/NVIDIA/TensorRT-LLM/pull/16523)
  [TRTLLM-14510][feat] serve: multi-process HTTP frontends on the classic IPC executor path (#16523)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/postproc_worker.py` _+12 more__
- **2026-07-22** [`4610a2a3d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4610a2a3d9) [#16564](https://github.com/NVIDIA/TensorRT-LLM/pull/16564)
  [None][perf] Add batched-pybind fast-path in TorchSampler.update_requests for gpt-oss-120b (#16564)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`_
- **2026-07-21** [`002f099e59`](https://github.com/NVIDIA/TensorRT-LLM/commit/002f099e59) [#16177](https://github.com/NVIDIA/TensorRT-LLM/pull/16177)
  [None][perf] Close Mamba hybrid warmup gap in autotuner warmup (#16177)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-20** [`75c8699a40`](https://github.com/NVIDIA/TensorRT-LLM/commit/75c8699a40) [#16158](https://github.com/NVIDIA/TensorRT-LLM/pull/16158)
  [None][perf] Improve PyTorch encoder-decoder support and performance (#16158)
  _Files: `docs/source/models/encoder-decoder.md`, `tensorrt_llm/_torch/models/modeling_bart.py`, `tensorrt_llm/_torch/models/modeling_t5.py`, `tensorrt_llm/_torch/modules/layer_norm.py` _+13 more__
- **2026-07-20** [`445742c189`](https://github.com/NVIDIA/TensorRT-LLM/commit/445742c189) [#16484](https://github.com/NVIDIA/TensorRT-LLM/pull/16484)
  [https://nvbugs/6438658][fix] Account for resume utilization in KV constraints (#16484)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache_manager.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_storage_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-07-20** [`ee241d25f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee241d25f4) [#16464](https://github.com/NVIDIA/TensorRT-LLM/pull/16464)
  [TRTLLM-14345][feat] Support GDN MTP Replay (#16464)
  _Files: `tensorrt_llm/_torch/modules/fla/cached_replay.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+7 more__
- **2026-07-20** [`a72b6469c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a72b6469c3) [#16226](https://github.com/NVIDIA/TensorRT-LLM/pull/16226)
  [https://nvbugs/6426852][fix] Fix intermittent cuda mapping error (#16226)
  _Files: `tensorrt_llm/executor/ray_executor.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`, `tests/unittest/_torch/ray_orchestrator/single_gpu/test_llm_update_weights.py`_
- **2026-07-20** [`5a4d258798`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a4d258798) [#16312](https://github.com/NVIDIA/TensorRT-LLM/pull/16312)
  [TRTLLM-13409][fix] make proxy shutdown non-blocking when the engine is dead (#16312)
  _Files: `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/unittest/executor/test_proxy_fast_death.py`_

## MoE  (16 commits)

- **2026-07-27** [`1dd8b97d53`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dd8b97d53) [#16830](https://github.com/NVIDIA/TensorRT-LLM/pull/16830)
  [None][feat] Add kimi_k2/glm_5 grouped routing and fused router to bench_moe (#16830)
  _Files: `tests/microbenchmarks/bench_moe/mapping.py`, `tests/microbenchmarks/bench_moe/search.py`, `tests/microbenchmarks/bench_moe/specs.py`_
- **2026-07-27** [`49e16c983d`](https://github.com/NVIDIA/TensorRT-LLM/commit/49e16c983d) [#16203](https://github.com/NVIDIA/TensorRT-LLM/pull/16203)
  [https://nvbugs/6433376][fix] Update the Dense test to mirror the MoE sibling — assert `bfloat16` under… (#16203)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-24** [`f5c2a07052`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5c2a07052) [#15597](https://github.com/NVIDIA/TensorRT-LLM/pull/15597)
  [https://nvbugs/6020038][feat] Add NCCL-EP v0.1 MoE communication support (#15597)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/modules/fused_moe/communication/__init__.py`, `tensorrt_llm/_torch/modules/fused_moe/communication/communication_factory.py`, `tensorrt_llm/_torch/modules/fused_moe/communication/nccl_ep.py` _+7 more__
- **2026-07-24** [`121cf56aed`](https://github.com/NVIDIA/TensorRT-LLM/commit/121cf56aed) [#16653](https://github.com/NVIDIA/TensorRT-LLM/pull/16653)
  [https://nvbugs/6457853][fix] Allow trtllm-gen MoE autotuner when local_num_experts < top_k (#16653)
  _Files: `tensorrt_llm/_torch/custom_ops/trtllm_gen_custom_ops.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-07-24** [`1fae43cc6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/1fae43cc6c) [#15194](https://github.com/NVIDIA/TensorRT-LLM/pull/15194)
  [TRTLLM-13349][perf] Fuse gemma RMSNorm into AllReduce for Qwen3-Next/Qwen3.5… (#15194)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tests/unittest/_torch/models/test_qwen3_next_eager_fusion.py`_
- **2026-07-24** [`16bdc6d875`](https://github.com/NVIDIA/TensorRT-LLM/commit/16bdc6d875) [#16597](https://github.com/NVIDIA/TensorRT-LLM/pull/16597)
  [None][feat] Support MARLIN MoE with MTP and attention DP + EP (#16597)
  _Files: `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_marlin.py` _+9 more__
- **2026-07-24** [`2801e94789`](https://github.com/NVIDIA/TensorRT-LLM/commit/2801e94789) [#16778](https://github.com/NVIDIA/TensorRT-LLM/pull/16778)
  [TRTLLM-14575][fix] MoE: fp32 accumulation in deferred MoEAllReduce finalize (#16778)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAllReduceFusionKernels.cu`_
- **2026-07-23** [`b039094c47`](https://github.com/NVIDIA/TensorRT-LLM/commit/b039094c47) [#12704](https://github.com/NVIDIA/TensorRT-LLM/pull/12704)
  [#11932][fix] Filter CUTLASS MoE GEMM tile configs by device shared memory on SM121 (#12704)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_mixed_input_launcher.inl`_
- **2026-07-22** [`9095cc11d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/9095cc11d1) [#16424](https://github.com/NVIDIA/TensorRT-LLM/pull/16424)
  [None][perf] DSv4 GVR top-k (CuTe DSL): P4 histogram refinement + redundant-warp sync reduction (#16424)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/scripts/cute_dsl_kernels/top_k/run_gvr_topk.py`_
- **2026-07-22** [`97149026d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/97149026d5) [#16546](https://github.com/NVIDIA/TensorRT-LLM/pull/16546)
  [None][feat] Raise the CuTE-DSL top-k decode limit to 16384 and support odd top_k (#16546)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_varlen_util.py`, `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`_
- **2026-07-21** [`6fabfdc2d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/6fabfdc2d4)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+19 more__
- **2026-07-21** [`4fb31cb937`](https://github.com/NVIDIA/TensorRT-LLM/commit/4fb31cb937) [#16611](https://github.com/NVIDIA/TensorRT-LLM/pull/16611)
  [None][test] Add deepseek v4 pro cases on the qa side (#16611)
  _Files: `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/deepseek-v4-pro-eplb/moe_load_balancer_ctx_ep4_384.yaml`, `tests/scripts/perf/disaggregated/deepseek-v4-pro-eplb/moe_load_balancer_gen_ep16_slots384.yaml` _+10 more__
- **2026-07-21** [`d09405681f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d09405681f) [#16617](https://github.com/NVIDIA/TensorRT-LLM/pull/16617)
  [None][fix] DSpark: all-reduce draft MoE output under non-attention-DP TP (#16617)
  _Files: `tensorrt_llm/_torch/models/modeling_dspark.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dspark_attention.py`_
- **2026-07-20** [`6df513420e`](https://github.com/NVIDIA/TensorRT-LLM/commit/6df513420e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+18 more__
- **2026-07-20** [`8bd00e4e3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bd00e4e3e) [#16540](https://github.com/NVIDIA/TensorRT-LLM/pull/16540)
  [None][test] Add DeepSeek-V4-Pro perf sanity cases on GB300 (#16540)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/local/submit.py`, `jenkins/scripts/perf/submit.py`, `tests/integration/defs/perf/_model_paths.py` _+19 more__
- **2026-07-20** [`0b03361010`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b03361010) [#15908](https://github.com/NVIDIA/TensorRT-LLM/pull/15908)
  [None][test] Add opt-in background prefetch of test MPI sessions and model page cache (#15908)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/conftest.py`, `tests/integration/defs/conftest.py`, `tests/integration/defs/pytest.ini` _+12 more__

## Disaggregation / KV  (16 commits)

- **2026-07-27** [`b91ffdad91`](https://github.com/NVIDIA/TensorRT-LLM/commit/b91ffdad91) [#16355](https://github.com/NVIDIA/TensorRT-LLM/pull/16355)
  [TRTLLM-13642][feat] Add perf sanity tests for Llama-3.1-8B and Gemma-3-1B and verify cache transceiver V2 support (#16355)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/scripts/perf-sanity/disaggregated/gb200_gemma-3-1b-bf16_1k1k_con256_ctx1_tp1_gen1_tp1_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_llama-3.1-8b-bf16_1k1k_con256_ctx1_tp1_gen1_tp1_eplb0_mtp0_ccb-NIXL.yaml`_
- **2026-07-24** [`9d7ef31f67`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d7ef31f67) [#16760](https://github.com/NVIDIA/TensorRT-LLM/pull/16760)
  [None][fix] Fix GPT-OSS router token identity (#16760)
  _Files: `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/serve/chat_tokenization.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/router.py` _+3 more__
- **2026-07-24** [`2eef5fe790`](https://github.com/NVIDIA/TensorRT-LLM/commit/2eef5fe790) [#16719](https://github.com/NVIDIA/TensorRT-LLM/pull/16719)
  [TRTLLM-14512][feat] multiprocess disagg server prometheus client (#16719)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/openai_disagg_server.py`, `tests/unittest/disaggregated/test_coordinator_e2e.py`_
- **2026-07-24** [`75b39d4368`](https://github.com/NVIDIA/TensorRT-LLM/commit/75b39d4368) [#16720](https://github.com/NVIDIA/TensorRT-LLM/pull/16720)
  [https://nvbugs/6482576][fix] Fall back to disagg_request_id in Python NIXL decode receiver (#16720)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_request_id.py`_
- **2026-07-24** [`641bbf28ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/641bbf28ff) [#16669](https://github.com/NVIDIA/TensorRT-LLM/pull/16669)
  [TRTLLM-13948][test] Migrate DeepSeek R1/V3.2 disagg perf cases to transceiver V2 (#16669)
  _Files: `tests/scripts/perf-sanity/disaggregated/b200_deepseek-r1-fp4_1k1k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/b200_deepseek-r1-fp4_1k1k_con2048_ctx1_dep4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/b200_deepseek-r1-fp4_1k1k_con256_ctx1_dep4_gen1_dep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/b200_deepseek-r1-fp4_8k1k_con1536_ctx1_dep4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml` _+72 more__
- **2026-07-24** [`8514fa39f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/8514fa39f5) [#15871](https://github.com/NVIDIA/TensorRT-LLM/pull/15871)
  [None][feat] align time metrics between cpp and python cache transceiver (#15871)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.cpp` _+18 more__
- **2026-07-24** [`f1645c48e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1645c48e0) [#16344](https://github.com/NVIDIA/TensorRT-LLM/pull/16344)
  [TRTLLM-13948][test] Add DeepSeek R1/V3.2/V3-Lite disaggregated accuracy tests (#16344)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml`_
- **2026-07-24** [`7d3a4e9796`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d3a4e9796) [#16708](https://github.com/NVIDIA/TensorRT-LLM/pull/16708)
  [https://nvbugs/6426834][fix] Deflake test_kv_transfer: cap NIXL progress threads, pin UCX env (#16708)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/disaggregated/test_agent.py`, `tests/unittest/disaggregated/test_agent_multi_backends.py`, `tests/unittest/disaggregated/test_cache_transceiver_single_process.py` _+5 more__
- **2026-07-22** [`8341fb1c2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/8341fb1c2a) [#12596](https://github.com/NVIDIA/TensorRT-LLM/pull/12596)
  [#12595][feat] Emit initial KV cache stats at startup for external metric scrapers (#12596)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/llmapi/apps/_test_openai_metrics.py`, `tests/unittest/llmapi/apps/_test_openai_prometheus.py` _+1 more__
- **2026-07-21** [`0f21fb8183`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f21fb8183) [#16663](https://github.com/NVIDIA/TensorRT-LLM/pull/16663)
  [https://nvbugs/6475930][fix] set small multi_round to save time (#16663)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-UCX.yaml`_
- **2026-07-21** [`9390924066`](https://github.com/NVIDIA/TensorRT-LLM/commit/9390924066) [#16482](https://github.com/NVIDIA/TensorRT-LLM/pull/16482)
  [TRTLLM-13639][test] Migrate Kimi dis-agg tests to Transceiver v2 and trim tests (#16482)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/unittest/_torch/modeling/test_modeling_kimi_k25.py`_
- **2026-07-21** [`ff976d81a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff976d81a2) [#16515](https://github.com/NVIDIA/TensorRT-LLM/pull/16515)
  [https://nvbugs/6120535][chore] Unwaive DeepSeek V3.2 disaggregated serving test (#16515)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`fd9c32f2b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd9c32f2b0) [#16115](https://github.com/NVIDIA/TensorRT-LLM/pull/16115)
  [None][feat] Add per-conversation KV cache block reuse (#16115)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi` _+7 more__
- **2026-07-20** [`d6add927fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6add927fe) [#15697](https://github.com/NVIDIA/TensorRT-LLM/pull/15697)
  [None][feat] Add TensorRT-LLM runtime integration for KV cache compression (#15697)
  _Files: `tensorrt_llm/_torch/kv_cache_compression/__init__.py`, `tensorrt_llm/_torch/kv_cache_compression/interface.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+9 more__
- **2026-07-20** [`fc88aea0e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc88aea0e8) [#16481](https://github.com/NVIDIA/TensorRT-LLM/pull/16481)
  [https://nvbugs/6314696] [fix] update disaggregated GB200 test configs (#16481)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/test-db/l0_gb200_multi_nodes_perf_sanity_ctx1_node2_gpu8_gen1_node8_gpu32.yml` _+3 more__
- **2026-07-20** [`d1eda80491`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1eda80491) [#16586](https://github.com/NVIDIA/TensorRT-LLM/pull/16586)
  [None][chore] Remove all 1k1k cases from QA's disagg side (#16586)
  _Files: `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/qa/llm_perf_multinode.yml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1024_ctx1_dep4_gen1_dep32_eplb0_mtp0_ccb-NIXL.yaml` _+58 more__

## Models  (13 commits)

- **2026-07-26** [`1562a07dd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/1562a07dd8) [#16774](https://github.com/NVIDIA/TensorRT-LLM/pull/16774)
  [None][feat] Support DeepSeek-V4 in layer_wise_benchmarks (#16774)
  _Files: `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`_
- **2026-07-24** [`021b435274`](https://github.com/NVIDIA/TensorRT-LLM/commit/021b435274) [#16795](https://github.com/NVIDIA/TensorRT-LLM/pull/16795)
  [None][test] Enable gen_only + ctx_only DeepSeek-V4-Pro perf-sanity on GB300 (#16795)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus_perf_sanity.yml`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_ctx12_node1_gpu4_gen1_node2_gpu8.yml`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_ctx1_node1_gpu4_gen4_node2_gpu8.yml` _+2 more__
- **2026-07-24** [`2e2ed4ed1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e2ed4ed1c) [#16797](https://github.com/NVIDIA/TensorRT-LLM/pull/16797)
  [NVBUG-6379624][fix] Enable W4A8 checkpoint loading for Gemma4 K=V layers (#16797)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/gemma4_weight_mapper.py`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-07-24** [`afd0a6692e`](https://github.com/NVIDIA/TensorRT-LLM/commit/afd0a6692e) [#16828](https://github.com/NVIDIA/TensorRT-LLM/pull/16828)
  [None][feat] Add support for MiniMax M3 and Qwen3.6 models in performance tests (#16828)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-07-24** [`2fbb367230`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fbb367230) [#16824](https://github.com/NVIDIA/TensorRT-LLM/pull/16824)
  [https://nvbugs/6473161][chore] unwaive 4 TestLlama3_1 tests (#16824)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`69c3cf84a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/69c3cf84a6) [#16254](https://github.com/NVIDIA/TensorRT-LLM/pull/16254)
  [TRTLLM-13694][feat] Add IBDB recipe provenance and refresh configs (#16254)
  _Files: `docs/source/_static/config_db.json`, `docs/source/_static/config_selector.css`, `docs/source/_static/config_selector.js`, `examples/configs/database/database.py` _+22 more__
- **2026-07-21** [`e3b0f686bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3b0f686bf) [#16661](https://github.com/NVIDIA/TensorRT-LLM/pull/16661)
  [None][test] Add deepseek-v4 B200/B300 test cases for single node GPU. (#16661)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/perf/utils.py` _+1 more__
- **2026-07-21** [`c9c0107812`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9c0107812) [#16659](https://github.com/NVIDIA/TensorRT-LLM/pull/16659)
  [None][doc] Update tech blog (#16659)
  _Files: `docs/source/blogs/tech_blog/blog26_DeepSeek_V4_on_NVIDIA_Blackwell_Model_Specific_and_Agentic_Workload_Optimizations_in_TensorRT-LLM.md`_
- **2026-07-21** [`919e0a1c46`](https://github.com/NVIDIA/TensorRT-LLM/commit/919e0a1c46) [#16493](https://github.com/NVIDIA/TensorRT-LLM/pull/16493)
  [https://nvbugs/6428008][fix] Unwaive one test case of Qwen3_5 (#16493)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-21** [`a95cd0f818`](https://github.com/NVIDIA/TensorRT-LLM/commit/a95cd0f818) [#16537](https://github.com/NVIDIA/TensorRT-LLM/pull/16537)
  [https://nvbugs/6395830][fix] Qwen-VL mRoPE: move seq-slot delta cach… (#16537)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen_image_bench.py`_
- **2026-07-20** [`4e38fb823c`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e38fb823c) [#16479](https://github.com/NVIDIA/TensorRT-LLM/pull/16479)
  [None][feat] Default GPT-OSS to the Python KV-cache transceiver (#16479)
  _Files: `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tests/unittest/_torch/modeling/test_modeling_gpt_oss.py`_
- **2026-07-20** [`56c3734511`](https://github.com/NVIDIA/TensorRT-LLM/commit/56c3734511) [#16588](https://github.com/NVIDIA/TensorRT-LLM/pull/16588)
  [None][infra] Waive B300 Nemotron SuperV3 MTP and Mistral Large3 timeout cases (#16588)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`699e2277a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/699e2277a4) [#16534](https://github.com/NVIDIA/TensorRT-LLM/pull/16534)
  [https://nvbugs/6316983][chore] Unwaive TestQwen2_5_VL_7B::test_auto_dtype (#16534)
  _Files: `tests/integration/test_lists/waives.txt`_

## Quantization  (12 commits)

- **2026-07-27** [`aae253ef60`](https://github.com/NVIDIA/TensorRT-LLM/commit/aae253ef60) [#12705](https://github.com/NVIDIA/TensorRT-LLM/pull/12705)
  [#15673][fix] Enable CUDA core fast path for SM89/SM120/SM121 (#12705)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/quant.py`, `tensorrt_llm/_torch/modules/linear.py`_
- **2026-07-27** [`55e9b2fe92`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e9b2fe92) [#16831](https://github.com/NVIDIA/TensorRT-LLM/pull/16831)
  [None][fix] Resolve NVFP4 mixed-precision base layers for the DSpark draft (#16831)
  _Files: `tensorrt_llm/_torch/models/modeling_dspark.py`_
- **2026-07-27** [`da39470b13`](https://github.com/NVIDIA/TensorRT-LLM/commit/da39470b13) [#16878](https://github.com/NVIDIA/TensorRT-LLM/pull/16878)
  [https://nvbugs/6479324][test] Remove waiver for fixed qwen3_5_4b_fp8_stress disaggregated stress test (#16878)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-25** [`b8e4594d93`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8e4594d93) [#16621](https://github.com/NVIDIA/TensorRT-LLM/pull/16621)
  [https://nvbugs/5948435][chore] Unwaive DeepSeekV3Lite test_nvfp4_4gpus CUTLASS ep4 fp8kv on RTXPro6000D (#16621)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-24** [`3c07ada3c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c07ada3c5) [#16612](https://github.com/NVIDIA/TensorRT-LLM/pull/16612)
  [TRTLLM-14474][chore] Remove legacy python relics and refresh docs after the backend removal (#16612)
  _Files: `.pre-commit-config.yaml`, `AGENTS.md`, `benchmarks/README.md`, `benchmarks/prepare_dataset.py` _+43 more__
- **2026-07-23** [`e16dcc54fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e16dcc54fd) [#16524](https://github.com/NVIDIA/TensorRT-LLM/pull/16524)
  [None][feat] Default GLM-5 to the Python KV-cache transceiver (#16524)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp4ep4_gentp4ep4_glm5_nvfp4_dp_tllm.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_glm-5-fp4_1k1k_con1_ctx1_dep4_gen1_tep4_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_glm-5-fp4_1k1k_con4096_ctx1_dep4_gen1_dep8_eplb256_mtp1_ccb-NIXL.yaml` _+11 more__
- **2026-07-23** [`96360f85ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/96360f85ed) [#16348](https://github.com/NVIDIA/TensorRT-LLM/pull/16348)
  [https://nvbugs/6426850][test] Unwaive Qwen3.5 397B NVFP4 ADP4 TRTLLM test (#16348)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-23** [`f52f3feadd`](https://github.com/NVIDIA/TensorRT-LLM/commit/f52f3feadd) [#16433](https://github.com/NVIDIA/TensorRT-LLM/pull/16433)
  [None][fix] Load DeepSeek V4 mixed-precision NVFP4 checkpoints (#16433)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tests/unittest/_torch/modeling/test_modeling_deepseekv4.py`_
- **2026-07-22** [`09e5d0c318`](https://github.com/NVIDIA/TensorRT-LLM/commit/09e5d0c318) [#16569](https://github.com/NVIDIA/TensorRT-LLM/pull/16569)
  [None][perf] Size the per-tensor FP8 dynamic-quant amax grid to the input (#16569)
  _Files: `cpp/tensorrt_llm/common/cudaFp8Utils.cu`_
- **2026-07-21** [`37ee708cc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/37ee708cc8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+15 more__
- **2026-07-20** [`26e476a4df`](https://github.com/NVIDIA/TensorRT-LLM/commit/26e476a4df) [#16245](https://github.com/NVIDIA/TensorRT-LLM/pull/16245)
  [None][fix] remove unsupported INT8 from trtllm-bench --quantization choices (#16245)
  _Files: `tensorrt_llm/bench/utils/__init__.py`, `tests/unittest/others/test_bench.py`, `tests/unittest/others/test_bench_data.py`_
- **2026-07-20** [`79c62c2276`](https://github.com/NVIDIA/TensorRT-LLM/commit/79c62c2276)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+17 more__

## Torch Path (_torch)  (6 commits)

- **2026-07-27** [`7982aa9701`](https://github.com/NVIDIA/TensorRT-LLM/commit/7982aa9701) [#16844](https://github.com/NVIDIA/TensorRT-LLM/pull/16844)
  [https://nvbugs/6501376][fix] Test-only fix — drop the `if hidden_size % 2 != 0: with pytest.raises(...)`… (#16844)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/multi_gpu/test_linear.py`_
- **2026-07-24** [`a8b540912c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8b540912c) [#16508](https://github.com/NVIDIA/TensorRT-LLM/pull/16508)
  [None][perf] Reordering torch.compile and cache-dit call (#16508)
  _Files: `tensorrt_llm/_torch/visual_gen/cache/cache_dit_enablers.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux2.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2.py` _+5 more__
- **2026-07-23** [`e96c3309f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/e96c3309f3) [#16410](https://github.com/NVIDIA/TensorRT-LLM/pull/16410)
  [https://nvbugs/6445456][fix] Restore inplace ops for functionalization v2 (#16410)
  _Files: `tensorrt_llm/_torch/compilation/remove_copy_pass.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/compilation/test_remove_copy_pass.py`_
- **2026-07-22** [`b294868a77`](https://github.com/NVIDIA/TensorRT-LLM/commit/b294868a77) [#16696](https://github.com/NVIDIA/TensorRT-LLM/pull/16696)
  [None][feat] Add BaseMultimodalDummyInputsBuilder to minimaxm3_vl (#16696)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3_vl.py`_
- **2026-07-22** [`9e96f8b9e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e96f8b9e7) [#16468](https://github.com/NVIDIA/TensorRT-LLM/pull/16468)
  [TRTLLM-14255][fix] migrate MiniMax M3 to loader v2 for TP8 support (#16468)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/minimaxm3_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/unittest/_torch/models/checkpoints/hf/test_minimaxm3_weight_mapper.py`, `tests/unittest/_torch/models/test_minimax_m3.py`_
- **2026-07-20** [`f354b77834`](https://github.com/NVIDIA/TensorRT-LLM/commit/f354b77834) [#16521](https://github.com/NVIDIA/TensorRT-LLM/pull/16521)
  [None][test] Assert MTP acceptance length in ADP + LM-head-TP accuracy tests (#16521)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_

## Speculative Decoding  (4 commits)

- **2026-07-24** [`4b7d719975`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b7d719975) [#16571](https://github.com/NVIDIA/TensorRT-LLM/pull/16571)
  [TRTLLM-14417][fix] Exclude ADP/cuda-graph dummy requests from speculative-decode acceptance stats (#16571)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_iter_stats_populate.py`_
- **2026-07-24** [`0960d59d22`](https://github.com/NVIDIA/TensorRT-LLM/commit/0960d59d22) [#16772](https://github.com/NVIDIA/TensorRT-LLM/pull/16772)
  [#16767][fix] Fix DSpark rolling-window slot collision in disaggregated serving (#16772)
  _Files: `tensorrt_llm/_torch/speculative/dspark.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dspark_worker.py`_
- **2026-07-22** [`1fbd240363`](https://github.com/NVIDIA/TensorRT-LLM/commit/1fbd240363) [#16724](https://github.com/NVIDIA/TensorRT-LLM/pull/16724)
  [https://nvbugs/6442074][fix] Rename MTPEagleDynamicTreeWorker.forward to _forward_impl (#16724)
  _Files: `tensorrt_llm/_torch/speculative/mtp_dynamic_tree.py`_
- **2026-07-20** [`fa54a19df5`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa54a19df5) [#16579](https://github.com/NVIDIA/TensorRT-LLM/pull/16579)
  [https://nvbugs/6442074][fix] Unbreak main: DSparkWorker forward rename + test stub _forward_impl (#16579)
  _Files: `tensorrt_llm/_torch/speculative/dspark.py`, `tests/unittest/_torch/speculative/test_rejection_buffers_guard.py`_

## Other  (3 commits)

- **2026-07-27** [`9f5b377664`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f5b377664) [#16894](https://github.com/NVIDIA/TensorRT-LLM/pull/16894)
  [None][test] Adjust timeout cases in QA perf test (#16894)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-07-21** [`c22a2c0a01`](https://github.com/NVIDIA/TensorRT-LLM/commit/c22a2c0a01) [#16478](https://github.com/NVIDIA/TensorRT-LLM/pull/16478)
  [None][test] update coderabbit prompt (#16478)
  _Files: `.coderabbit.yaml`_
- **2026-07-21** [`88d700f66a`](https://github.com/NVIDIA/TensorRT-LLM/commit/88d700f66a) [#16664](https://github.com/NVIDIA/TensorRT-LLM/pull/16664)
  [None][chore] Add sparse cache manager code owner (#16664)
  _Files: `.github/CODEOWNERS`_

## Perf  (3 commits)

- **2026-07-27** [`08289b629f`](https://github.com/NVIDIA/TensorRT-LLM/commit/08289b629f) [#16799](https://github.com/NVIDIA/TensorRT-LLM/pull/16799)
  [None][perf] Optimize Blackwell fused MHC half-MMA kernel (#16799)
  _Files: `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`_
- **2026-07-23** [`80b4eb3675`](https://github.com/NVIDIA/TensorRT-LLM/commit/80b4eb3675) [#16633](https://github.com/NVIDIA/TensorRT-LLM/pull/16633)
  [None][perf] Optimize fusedQKNormRope Kernel (#16633)
  _Files: `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`_
- **2026-07-20** [`b520c6fc57`](https://github.com/NVIDIA/TensorRT-LLM/commit/b520c6fc57) [#16513](https://github.com/NVIDIA/TensorRT-LLM/pull/16513)
  [None][perf] Preallocate video decode buffer for HF zero-copy handoff (#16513)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tensorrt_llm/inputs/multimodal_data.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/inputs/test_video_decode.py`_

## Compilation / Graph  (1 commits)

- **2026-07-25** [`bfb0fca859`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfb0fca859) [#16775](https://github.com/NVIDIA/TensorRT-LLM/pull/16775)
  [https://nvbugs/6463822][fix] Fix LTX2 CUDA graph test leak issue (#16775)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen.py`_

## Docs / Examples  (1 commits)

- **2026-07-20** [`5d790a05f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d790a05f2) [#16454](https://github.com/NVIDIA/TensorRT-LLM/pull/16454)
  [None][chore] Bump version to 1.3.0rc22 (#16454)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

---
_Generated 2026-07-27 11:36 UTC_