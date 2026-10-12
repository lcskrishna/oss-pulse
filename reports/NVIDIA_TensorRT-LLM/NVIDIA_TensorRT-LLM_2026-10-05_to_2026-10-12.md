# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-10-05 → 2026-10-12  |  **Total commits:** 138

## ✨ New Features This Week

- **2026-10-12** [#20077](https://github.com/NVIDIA/TensorRT-LLM/pull/20077) — [TRTLLM-16956][feat] Modeling V2 dynamic switch with LLM config and args (#20077)
- **2026-10-12** [#20093](https://github.com/NVIDIA/TensorRT-LLM/pull/20093) — [None][feat] Let a model require KV cache manager v2 instead of being demoted to v1 (#20093)
- **2026-10-12** [#20142](https://github.com/NVIDIA/TensorRT-LLM/pull/20142) — [None][infra] Add TensorRT-LLM Release 1.4 section to release notes (#20142)
- **2026-10-12** [#17495](https://github.com/NVIDIA/TensorRT-LLM/pull/17495) — [None][feat] BREAKING: Default to KV cache manager V2 and Python transceiver (#17495)
- **2026-10-12** [#19338](https://github.com/NVIDIA/TensorRT-LLM/pull/19338) — [None][feat] Upgrade Blackwell cuteDSL MLA kernel for packed q heads and compact input (#19338)
- **2026-10-12** [#19272](https://github.com/NVIDIA/TensorRT-LLM/pull/19272) — [None][feat] Wire Rubin locality-domain execution through PyTorch models (#19272)
- **2026-10-11** [#19727](https://github.com/NVIDIA/TensorRT-LLM/pull/19727) — [TRTLLM-16621][feat] Support DeepSeek-V4.1-Flash (#19727)
- **2026-10-11** [#17876](https://github.com/NVIDIA/TensorRT-LLM/pull/17876) — [None][feat] Multimodal encoder cache unification (#17876)
- **2026-10-10** [#19719](https://github.com/NVIDIA/TensorRT-LLM/pull/19719) — [TRTLLM-16708][feat] Honor per-request seeds in batched TorchSampler sampling via the fused kernel (#19719)
- **2026-10-10** [#19391](https://github.com/NVIDIA/TensorRT-LLM/pull/19391) — [TRTLLM-16857][feat] Add RoPE precision options to NVFP4 cold-page compression (#19391)
- _…and 23 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#20083](https://github.com/NVIDIA/TensorRT-LLM/issues/20083) | [Bug]: Ray orchestrator: NcclEP builds its EP communicator from MPI_CO | Inference runtime, Disaggregated serving | 2026-10-12 |
| [#20138](https://github.com/NVIDIA/TensorRT-LLM/issues/20138) | [Bug]: Qwen3-VL E/PD handoff drops per-frame timestamp tokens and fram | Disaggregated serving, Multimodal | 2026-10-12 |
| [#19634](https://github.com/NVIDIA/TensorRT-LLM/issues/19634) | [Bug]: multi-node trtllm-serve with the MPI orchestrator (trtllm-llmap | Inference runtime, Disaggregated serving | 2026-10-10 |
| [#20082](https://github.com/NVIDIA/TensorRT-LLM/issues/20082) | [Bug]: Ray orchestrator with attention DP and TRTLLM_FORCE_COMM_METHOD | Disaggregated serving, Scale-out | 2026-10-10 |
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-10-08 |
| [#19994](https://github.com/NVIDIA/TensorRT-LLM/issues/19994) | [Feature]: Whisper serving parity in trtllm-serve — /v1/audio/transcri | LLM API, OpenAI API | 2026-10-08 |
| [#19951](https://github.com/NVIDIA/TensorRT-LLM/issues/19951) | [Bug]: Helix all-to-all receive path: restored payload words reach the | Customized kernels | 2026-10-08 |
| [#19913](https://github.com/NVIDIA/TensorRT-LLM/issues/19913) | [Bug]: Upgrade XGrammar: qwen_xml compilation errors and tool-call loo | bug, Customized kernels | 2026-10-07 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-10-05 |
| [#19820](https://github.com/NVIDIA/TensorRT-LLM/issues/19820) | [New Model]: Apertus (swiss-ai/Apertus-8B-Instruct-2509, swiss-ai/Aper | new model | 2026-10-02 |
| [#19666](https://github.com/NVIDIA/TensorRT-LLM/issues/19666) | [Feature]: EFA should work out of the box on NGC TRTLLM release image  | feature request, OOTB | 2026-10-01 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-10-01 |
| [#19726](https://github.com/NVIDIA/TensorRT-LLM/issues/19726) | [Feature][RFC]: Compact active beam rows during VBWS decode in the PyT | Pytorch, Model optimization | 2026-09-30 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-09-28 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-09-21 |
| [#19232](https://github.com/NVIDIA/TensorRT-LLM/issues/19232) | [RFC]: Disaggregated request preprocessing | triaged, Investigating, LLM API, Disaggregated serving, RFC, Frontend | 2026-09-16 |
| [#19242](https://github.com/NVIDIA/TensorRT-LLM/issues/19242) | [Bug]: KVCacheBlock and its radix tree LookupNode own each other with  | KV-Cache Management | 2026-09-16 |
| [#19240](https://github.com/NVIDIA/TensorRT-LLM/issues/19240) | [Bug]: mixtureOfExpertsTest crashes with SEGV when a parameter set has | Customized kernels | 2026-09-16 |
| [#19059](https://github.com/NVIDIA/TensorRT-LLM/issues/19059) | [Bug]: C++17 build cannot compile torch 2.12 headers with nvcc, but C+ | Pytorch | 2026-09-15 |
| [#19172](https://github.com/NVIDIA/TensorRT-LLM/issues/19172) | [Bug]: Async prompt-embedding H2D outlives its pooled-pinned source; t | bug, Triton backend, Inference runtime | 2026-09-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 25 |
| Executor / Runtime | 22 |
| Attention | 17 |
| Speculative Decoding | 13 |
| Other | 13 |
| MoE | 11 |
| Quantization | 10 |
| Disaggregation / KV | 9 |
| Torch Path (_torch) | 8 |
| Models | 8 |
| Perf | 1 |
| LoRA | 1 |

## CI / Infra  (25 commits)

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
- **2026-10-10** [`7179c5b01b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7179c5b01b) [#20074](https://github.com/NVIDIA/TensorRT-LLM/pull/20074)
  [None][ci] waive pre-existing test failures on main (#20074)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-09** [`cbde30dcba`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbde30dcba) [#20015](https://github.com/NVIDIA/TensorRT-LLM/pull/20015)
  [https://nvbugs/6890897][test] Fix startup telemetry architecture expectation and unwaive test (#20015)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/usage/test_e2e_capture.py`_
- **2026-10-09** [`3536bb5b78`](https://github.com/NVIDIA/TensorRT-LLM/commit/3536bb5b78) [#19594](https://github.com/NVIDIA/TensorRT-LLM/pull/19594)
  [TRTLLM-10804][infra] Restore release checks in nightly releases (#19594)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-09** [`eaedb86ec1`](https://github.com/NVIDIA/TensorRT-LLM/commit/eaedb86ec1) [#20025](https://github.com/NVIDIA/TensorRT-LLM/pull/20025)
  [None][infra] Add blossom-ci authorized users (#20025)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-10-09** [`40eb9cb079`](https://github.com/NVIDIA/TensorRT-LLM/commit/40eb9cb079) [#19589](https://github.com/NVIDIA/TensorRT-LLM/pull/19589)
  [None][infra] Retry the mypy type-check step in the build stage (#19589)
  _Files: `jenkins/Build.groovy`_
- **2026-10-08** [`e2852d987c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2852d987c) [#19963](https://github.com/NVIDIA/TensorRT-LLM/pull/19963)
  [None][infra] Disable BOLT premerge consume (#19963)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-08** [`b90ff2158e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b90ff2158e) [#19409](https://github.com/NVIDIA/TensorRT-LLM/pull/19409)
  [TRTLLM-16185][infra] route documentation changes to docs and CPU validation (#19409)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/agent_flow_rule.py` _+8 more__
- **2026-10-08** [`3ec3019ee0`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ec3019ee0) [#19946](https://github.com/NVIDIA/TensorRT-LLM/pull/19946)
  [None][infra] Waive 3 failed cases for main in post-merge 3007 (#19946)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-08** [`b27b1e9c90`](https://github.com/NVIDIA/TensorRT-LLM/commit/b27b1e9c90) [#19945](https://github.com/NVIDIA/TensorRT-LLM/pull/19945)
  [https://nvbugs/6890897][chore] Waive failing test 10/07 (#19945)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-07** [`0e8843eede`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e8843eede) [#19931](https://github.com/NVIDIA/TensorRT-LLM/pull/19931)
  [None][ci] waive pre-existing test failures on main (#19931)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-07** [`446e8d9236`](https://github.com/NVIDIA/TensorRT-LLM/commit/446e8d9236) [#19622](https://github.com/NVIDIA/TensorRT-LLM/pull/19622)
  [TRTLLM-16569][infra] finalize existing logs after capture errors (#19622)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/test_common/s3_output.py`, `tests/unittest/test_s3_output.py`_
- **2026-10-07** [`b9dd9b9630`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9dd9b9630) [#19919](https://github.com/NVIDIA/TensorRT-LLM/pull/19919)
  [None][infra] Waive 1 failed cases for main in post-merge 3005 (#19919)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-06** [`687af96ddb`](https://github.com/NVIDIA/TensorRT-LLM/commit/687af96ddb) [#18677](https://github.com/NVIDIA/TensorRT-LLM/pull/18677)
  [TRTLLMINF-336][infra] Enable BOLT premerge consume (#18677)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-06** [`0970204df7`](https://github.com/NVIDIA/TensorRT-LLM/commit/0970204df7) [#19603](https://github.com/NVIDIA/TensorRT-LLM/pull/19603)
  [TRTLLMINF-336][infra] Publish and test the post-merge BOLTed build beside canonical (#19603)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`_
- **2026-10-06** [`bba2b17635`](https://github.com/NVIDIA/TensorRT-LLM/commit/bba2b17635) [#18802](https://github.com/NVIDIA/TensorRT-LLM/pull/18802)
  [TRTLLM-15885][infra] validate CBTS coverage DB compatibility (#18802)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/coverage_selection/SELECTION.md`, `jenkins/scripts/cbts/coverage_selection/artifact.py` _+6 more__
- **2026-10-06** [`542080a14a`](https://github.com/NVIDIA/TensorRT-LLM/commit/542080a14a) [#19875](https://github.com/NVIDIA/TensorRT-LLM/pull/19875)
  [None][infra] Waive 3 failed cases for main in post-merge 3003 (#19875)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-06** [`fe6d98cb6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe6d98cb6b) [#19879](https://github.com/NVIDIA/TensorRT-LLM/pull/19879)
  [None][infra] Waive 1 failed cases for main in post-merge 3003 (#19879)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-06** [`3c4d0f181b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c4d0f181b) [#19878](https://github.com/NVIDIA/TensorRT-LLM/pull/19878)
  [None][infra] Add blossom-ci authorized users (#19878)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-10-06** [`47c6487fe2`](https://github.com/NVIDIA/TensorRT-LLM/commit/47c6487fe2) [#19637](https://github.com/NVIDIA/TensorRT-LLM/pull/19637)
  [https://nvbugs/6616036][test] Unwaive test (#19637)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-05** [`dc6f88de69`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc6f88de69) [#19431](https://github.com/NVIDIA/TensorRT-LLM/pull/19431)
  [TRTLLMINF-336][infra] Activate BOLT optimization of the SBSA release image wheel (#19431)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `scripts/bolt/internal/apply_latest.sh` _+2 more__
- **2026-10-05** [`d1db352d64`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1db352d64)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Executor / Runtime  (22 commits)

- **2026-10-12** [`9cb84a22bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cb84a22bb) [#18310](https://github.com/NVIDIA/TensorRT-LLM/pull/18310)
  [https://nvbugs/6661863][fix] Allocate one `PyMem_RawCalloc`'d `_DLPackBlock` (managed tensor + inline… (#18310)
  _Files: `tensorrt_llm/_dlpack_utils.py`, `tensorrt_llm/executor/proxy.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/waives.txt` _+2 more__
- **2026-10-11** [`4393129960`](https://github.com/NVIDIA/TensorRT-LLM/commit/4393129960) [#17876](https://github.com/NVIDIA/TensorRT-LLM/pull/17876)
  [None][feat] Multimodal encoder cache unification (#17876)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py` _+21 more__
- **2026-10-09** [`d3b9e521fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3b9e521fb)
  feat(openengine): support multiple gRPC frontend processes
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/grpc/openengine/README.md`, `tensorrt_llm/grpc/openengine/control.py`, `tensorrt_llm/grpc/openengine/coordinator.py` _+13 more__
- **2026-10-09** [`dbe3a7659a`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbe3a7659a) [#19494](https://github.com/NVIDIA/TensorRT-LLM/pull/19494)
  [https://nvbugs/6791675][fix] Propagate client sys.path to remote MPI workers (#19494)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/_mpi_session_test_tasks.py`, `tests/unittest/llmapi/_run_mpi_comm_task.py` _+1 more__
- **2026-10-09** [`ff94288d99`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff94288d99) [#19935](https://github.com/NVIDIA/TensorRT-LLM/pull/19935)
  [None][fix] GLM tool and reasoning parsers: streaming matches the whole-text parse (#19935)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tensorrt_llm/serve/tool_parser/base_tool_parser.py`, `tensorrt_llm/serve/tool_parser/glm47_parser.py`, `tensorrt_llm/serve/tool_parser/glm4_parser.py` _+3 more__
- **2026-10-09** [`5f229bf9ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f229bf9ca) [#20019](https://github.com/NVIDIA/TensorRT-LLM/pull/20019)
  [https://nvbugs/6812588][fix] Bound Qwen3.5 batch/seq len in multi-node disagg tests (#20019)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes.py`, `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes_service_discovery.py`_
- **2026-10-09** [`b2d9ec3be0`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2d9ec3be0) [#19748](https://github.com/NVIDIA/TensorRT-LLM/pull/19748)
  [None][fix] Enforce KV correction when overlap scheduling runs with speculation (#19748)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/executor/test_py_executor_creator_overlap_spec_guard.py`_
- **2026-10-08** [`ce2e2f8b70`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce2e2f8b70) [#19821](https://github.com/NVIDIA/TensorRT-LLM/pull/19821)
  [TRTLLM-16282][feat] Add sparse KV offload and GPU metadata publication (#19821)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batch.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batch.h` _+18 more__
- **2026-10-08** [`ec357dd9e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec357dd9e4) [#19585](https://github.com/NVIDIA/TensorRT-LLM/pull/19585)
  [TRTLLM-16617][chore] remove obsolete TensorRT telemetry compatibility paths (#19585)
  _Files: `.github/CODEOWNERS`, `docs/source/helper.py`, `tensorrt_llm/usage/schemas/README.md`, `tensorrt_llm/usage/usage_lib.py` _+4 more__
- **2026-10-08** [`2e2a3cb925`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e2a3cb925) [#19892](https://github.com/NVIDIA/TensorRT-LLM/pull/19892)
  [None][fix] route Qwen3.6/3.8 VLM checkpoints to the generic Qwen3.5 VLM wrapper (#19892)
  _Files: `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+6 more__
- **2026-10-08** [`e5a9341138`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5a9341138) [#19484](https://github.com/NVIDIA/TensorRT-LLM/pull/19484)
  [None][refactor] BREAKING: Migrate LlmRequest fields to Python (#19484)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `cpp/tensorrt_llm/executor/request.cpp` _+23 more__
- **2026-10-08** [`b031dbe6f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/b031dbe6f0) [#19791](https://github.com/NVIDIA/TensorRT-LLM/pull/19791)
  [None][fix] skip unused multimodal encoder IPC handles (#19791)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/unittest/_torch/executor/test_multimodal_embedding_lengths.py`_
- **2026-10-08** [`1ab9f5525e`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ab9f5525e) [#19643](https://github.com/NVIDIA/TensorRT-LLM/pull/19643)
  [https://nvbugs/6697099][fix] Keep MPI progress alive on the PP sample-state relay thread (#19643)
  _Files: `tensorrt_llm/_torch/pyexecutor/pp_utils.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_pp_mpi_progress_pump.py`_
- **2026-10-07** [`ef1b238cff`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef1b238cff) [#19869](https://github.com/NVIDIA/TensorRT-LLM/pull/19869)
  [TRTLLM-16772][fix] Release async IPC payloads with garbage collection disabled (#19869)
  _Files: `tensorrt_llm/executor/ipc.py`, `tests/unittest/executor/test_ipc.py`_
- **2026-10-07** [`0f4c99e739`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f4c99e739) [#19226](https://github.com/NVIDIA/TensorRT-LLM/pull/19226)
  [#19225][fix] Keep markdown fences in DeepSeek V3 streamed content (#19226)
  _Files: `tensorrt_llm/serve/tool_parser/deepseekv3_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-07** [`70193ec43b`](https://github.com/NVIDIA/TensorRT-LLM/commit/70193ec43b) [#19583](https://github.com/NVIDIA/TensorRT-LLM/pull/19583)
  [TRTLLM-16614][chore] Remove more TRT leftovers (#19583)
  _Files: `tensorrt_llm/bench/benchmark/__init__.py`, `tensorrt_llm/bench/benchmark/low_latency.py`, `tensorrt_llm/bench/benchmark/utils/general.py`, `tensorrt_llm/bench/dataclasses/configuration.py` _+5 more__
- **2026-10-07** [`602c90be1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/602c90be1c) [#19758](https://github.com/NVIDIA/TensorRT-LLM/pull/19758)
  [#19756][fix] Parse hyphenated function names in the Kimi K2 tool parser (#19758)
  _Files: `tensorrt_llm/serve/tool_parser/kimi_k2_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-06** [`46473dcfb7`](https://github.com/NVIDIA/TensorRT-LLM/commit/46473dcfb7) [#19598](https://github.com/NVIDIA/TensorRT-LLM/pull/19598)
  [TRTLLM-16761][feat] Capture partial telemetry context for LLM startup failures (#19598)
  _Files: `README.md`, `tensorrt_llm/bench/benchmark/low_latency.py`, `tensorrt_llm/bench/benchmark/throughput.py`, `tensorrt_llm/commands/_telemetry.py` _+11 more__
- **2026-10-06** [`db359c23cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/db359c23cc) [#19359](https://github.com/NVIDIA/TensorRT-LLM/pull/19359)
  [None][feat] support C++ streaming KV events with multimodal payloads (#19359)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventData.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventData.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventManager.cpp` _+13 more__
- **2026-10-06** [`f7e671a1f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7e671a1f2) [#19754](https://github.com/NVIDIA/TensorRT-LLM/pull/19754)
  [None][test] Exercise SWA endpoint retention against real page eviction (#19754)
  _Files: `tests/unittest/_torch/executor/kv_cache/test_kvcm2_integration.py`_
- **2026-10-05** [`276cc12ff5`](https://github.com/NVIDIA/TensorRT-LLM/commit/276cc12ff5) [#19811](https://github.com/NVIDIA/TensorRT-LLM/pull/19811)
  [TRTLLM-16757][fix] Forward-port configuration model-list telemetry capture to main (#19811)
  _Files: `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/usage/llmapi_config.py`, `tests/unittest/usage/test_llmapi_config_capture.py`, `tests/unittest/usage/test_llmapi_model_sequences.py`_
- **2026-10-05** [`82f980469f`](https://github.com/NVIDIA/TensorRT-LLM/commit/82f980469f) [#19552](https://github.com/NVIDIA/TensorRT-LLM/pull/19552)
  [TRTLLMINF-15][build] Remove Conan from the C++ build (#19552)
  _Files: `.github/CODEOWNERS`, `.gitignore`, `.pre-commit-config.yaml`, `3rdparty/cpp-thirdparty.md` _+18 more__

## Attention  (17 commits)

- **2026-10-12** [`afc1fa2744`](https://github.com/NVIDIA/TensorRT-LLM/commit/afc1fa2744) [#17495](https://github.com/NVIDIA/TensorRT-LLM/pull/17495)
  [None][feat] BREAKING: Default to KV cache manager V2 and Python transceiver (#17495)
  _Files: `examples/disaggregated/slurm/service_discovery_example/launch.slurm`, `examples/disaggregated/slurm/simple_example/ctx_extra-llm-api-config.yaml`, `examples/disaggregated/slurm/simple_example/gen_extra-llm-api-config.yaml`, `examples/dwdp/reproduce.py` _+80 more__
- **2026-10-12** [`9257aaefbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9257aaefbb) [#19338](https://github.com/NVIDIA/TensorRT-LLM/pull/19338)
  [None][feat] Upgrade Blackwell cuteDSL MLA kernel for packed q heads and compact input (#19338)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp16.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp8.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_helpers.py`_
- **2026-10-11** [`16df7eaf25`](https://github.com/NVIDIA/TensorRT-LLM/commit/16df7eaf25) [#19727](https://github.com/NVIDIA/TensorRT-LLM/pull/19727)
  [TRTLLM-16621][feat] Support DeepSeek-V4.1-Flash (#19727)
- **2026-10-10** [`fcc4432bef`](https://github.com/NVIDIA/TensorRT-LLM/commit/fcc4432bef) [#19719](https://github.com/NVIDIA/TensorRT-LLM/pull/19719)
  [TRTLLM-16708][feat] Honor per-request seeds in batched TorchSampler sampling via the fused kernel (#19719)
  _Files: `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernels.h`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernelsCommon.cuh`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingMultiCta.cu`, `cpp/tensorrt_llm/thop/fusedSamplingOp.cpp` _+17 more__
- **2026-10-10** [`c49005724c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c49005724c) [#19391](https://github.com/NVIDIA/TensorRT-LLM/pull/19391)
  [TRTLLM-16857][feat] Add RoPE precision options to NVFP4 cold-page compression (#19391)
  _Files: `cpp/tensorrt_llm/kernels/nvfp4ColdPageKernels.cu`, `cpp/tests/unit_tests/kernels/nvfp4ColdPageKernelsTest.cpp`, `docs/source/developer-guide/kv-cache-compression-development.md`, `docs/source/features/kv-cache-compression.md` _+10 more__
- **2026-10-09** [`34fcc38aac`](https://github.com/NVIDIA/TensorRT-LLM/commit/34fcc38aac) [#19790](https://github.com/NVIDIA/TensorRT-LLM/pull/19790)
  [https://nvbugs/6849051][fix] The shared mock helper sets `get_fp4_mla_page_table_spec = None` and both… (#19790)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/speculative/test_eagle3.py`_
- **2026-10-09** [`348192ae71`](https://github.com/NVIDIA/TensorRT-LLM/commit/348192ae71) [#19746](https://github.com/NVIDIA/TensorRT-LLM/pull/19746)
  [None][fix] Refuse paged-context FMHA configurations whose fused context kernel is absent (#19746)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py`, `tests/unittest/_torch/attention/test_attention_op_sync.py`, `tests/unittest/_torch/attention/test_trtllm_paged_context_fmha_gate.py`_
- **2026-10-08** [`ac3ec50919`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac3ec50919) [#19825](https://github.com/NVIDIA/TensorRT-LLM/pull/19825)
  [None][perf] Enable tiled FP8 context FMHA for head_dim 256 on SM120 (#19825)
  _Files: `cpp/kernels/fmha_v2/setup.py`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fmhaRunner.cpp`_
- **2026-10-08** [`8f973fbe7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/8f973fbe7d) [#19873](https://github.com/NVIDIA/TensorRT-LLM/pull/19873)
  [None][fix] Add a static tile scheduler override for context FMHA (#19873)
  _Files: `cpp/tensorrt_llm/common/envUtils.cpp`, `cpp/tensorrt_llm/common/envUtils.h`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`_
- **2026-10-08** [`25f142cdb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/25f142cdb8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+5 more__
- **2026-10-07** [`7329182abe`](https://github.com/NVIDIA/TensorRT-LLM/commit/7329182abe) [#19306](https://github.com/NVIDIA/TensorRT-LLM/pull/19306)
  [TRTLLM-15261][feat] Test stale pointers held by captured graph in metadata (#19306)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py` _+3 more__
- **2026-10-07** [`febb02eab5`](https://github.com/NVIDIA/TensorRT-LLM/commit/febb02eab5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+6 more__
- **2026-10-07** [`d3c825800d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3c825800d) [#18496](https://github.com/NVIDIA/TensorRT-LLM/pull/18496)
  [TRTLLM-16040][feat] Refresh SM90 SageAttention onto the per-thread-quantized kernel, Integrate to VisualGen (#18496)
  _Files: `cpp/kernels/fmha_v2/fmha_test.py`, `cpp/kernels/fmha_v2/setup.py`, `cpp/kernels/fmha_v2/src/fmha/warpspec/compute.h`, `cpp/kernels/fmha_v2/src/fmha/warpspec/dma.h` _+34 more__
- **2026-10-06** [`af645b7806`](https://github.com/NVIDIA/TensorRT-LLM/commit/af645b7806) [#19213](https://github.com/NVIDIA/TensorRT-LLM/pull/19213)
  [None][fix] Scope KVCM warmup capacity constraints to DeepSeek V4 (#19213)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+7 more__
- **2026-10-06** [`e0d1e933c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0d1e933c7) [#19731](https://github.com/NVIDIA/TensorRT-LLM/pull/19731)
  [None][perf] MiniMax-M3: native P128 draft KV view for the NVFP4 hybrid cache (#19731)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/msa_scatter.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/trtllm_gen_dense_decode.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+4 more__
- **2026-10-05** [`cb03225c13`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb03225c13) [#19709](https://github.com/NVIDIA/TensorRT-LLM/pull/19709)
  [None][fix] Honor selector strides in MSA short-query attention (#19709)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/unittest/_torch/attention/sparse/msa/test_minimax_m3_sparse_attn_decode.py`_
- **2026-10-05** [`d27e97f6de`](https://github.com/NVIDIA/TensorRT-LLM/commit/d27e97f6de) [#19768](https://github.com/NVIDIA/TensorRT-LLM/pull/19768)
  [None][perf] reuse MiniMax-M3 NVFP4 query-length buffer (#19768)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`_

## Speculative Decoding  (13 commits)

- **2026-10-12** [`dc8451c508`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc8451c508) [#20064](https://github.com/NVIDIA/TensorRT-LLM/pull/20064)
  [TRTLLM-16901][fix] SID-GR optimization 1/N: Fix speculative beam d2h races (#20064)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_features.py`, `tests/unittest/_torch/sampler/test_beam_search_speculative_d2h.py`_
- **2026-10-12** [`7f011f1020`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f011f1020) [#19490](https://github.com/NVIDIA/TensorRT-LLM/pull/19490)
  [TRTLLM-16593][fix] Size expanded draft probabilities by batch capacity (#19490)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/test_rejection_buffers_guard.py`_
- **2026-10-12** [`cf71337fbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf71337fbe) [#20076](https://github.com/NVIDIA/TensorRT-LLM/pull/20076)
  [None][test] Update MiniMax M3 EAGLE3 draft model directory (#20076)
  _Files: `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep16_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep8_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tep2_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tp4_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml` _+4 more__
- **2026-10-10** [`553989e4a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/553989e4a7) [#20000](https://github.com/NVIDIA/TensorRT-LLM/pull/20000)
  [https://nvbugs/6718911][fix] Clear stale disagg rendezvous files before each perf-sanity attempt (#20000)
  _Files: `jenkins/scripts/perf/disaggregated/slurm_launch_draft.sh`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-10-09** [`6e0bc48760`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e0bc48760) [#19818](https://github.com/NVIDIA/TensorRT-LLM/pull/19818)
  [TRTLLM-14620][feat] Add DSpark confidence verification policy (#19818)
  _Files: `tensorrt_llm/_torch/speculative/dspark_planner.py`, `tensorrt_llm/_torch/speculative/dspark_schedule.py`, `tensorrt_llm/_torch/speculative/dspark_verify.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dspark_cost_table.py` _+3 more__
- **2026-10-09** [`6dc2552919`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dc2552919) [#19745](https://github.com/NVIDIA/TensorRT-LLM/pull/19745)
  [None][fix] Admit unpaired draft KV mirrors at scheduling time and recompute a prompt tail on cache hits (#19745)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py` _+7 more__
- **2026-10-09** [`24d0f2716f`](https://github.com/NVIDIA/TensorRT-LLM/commit/24d0f2716f) [#19707](https://github.com/NVIDIA/TensorRT-LLM/pull/19707)
  [TRTLLM-14620][feat] Add ragged DSpark verification semantics (#19707)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/penalties.py`, `tensorrt_llm/_torch/speculative/dspark.py`, `tensorrt_llm/_torch/speculative/interface.py` _+9 more__
- **2026-10-09** [`af13c159ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/af13c159ab)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+5 more__
- **2026-10-08** [`147f70f9c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/147f70f9c1) [#19588](https://github.com/NVIDIA/TensorRT-LLM/pull/19588)
  [None][test] Migrate disaggregated E2E tests to C++ bounce buffers (#19588)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_overlap_transceiver_runtime_python_bounce.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/scripts/perf-sanity/disaggregated/gb200_gpt-oss-120b-fp4_1k1k_con64_ctx1_tp1_gen1_tp4_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_gpt-oss-120b-fp4_8k1k_con1024_ctx1_tp1_gen1_tp4_eplb0_mtp0_ccb-NIXL.yaml` _+18 more__
- **2026-10-07** [`b57220da7b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b57220da7b) [#19899](https://github.com/NVIDIA/TensorRT-LLM/pull/19899)
  [None][fix] Fix torch.compile eagle3 AL (#19899)
  _Files: `tensorrt_llm/_torch/compilation/multi_stream/auto_multi_stream.py`, `tests/unittest/_torch/compilation/test_auto_multi_stream.py`_
- **2026-10-07** [`7efa053a89`](https://github.com/NVIDIA/TensorRT-LLM/commit/7efa053a89) [#19744](https://github.com/NVIDIA/TensorRT-LLM/pull/19744)
  [None][feat] Weight the draft KV budget split by per-request spend (#19744)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_budget_split.py`_
- **2026-10-06** [`b3be283b97`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3be283b97) [#19696](https://github.com/NVIDIA/TensorRT-LLM/pull/19696)
  [TRTLLM-15761][refactor] Parameterize decoder invocation state and separate decoder-only engine state (#19696)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/common.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/utils.py`, `tests/unittest/_torch/executor/engine/test_common.py` _+6 more__
- **2026-10-06** [`61332ba9f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/61332ba9f6) [#19891](https://github.com/NVIDIA/TensorRT-LLM/pull/19891)
  [TRTLLM-16773][fix] fix dummy slot issue (#19891)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/mtp.py`, `tests/unittest/_torch/speculative/test_spec_slot_pool_sizing.py`_

## Other  (13 commits)

- **2026-10-12** [`7895a682da`](https://github.com/NVIDIA/TensorRT-LLM/commit/7895a682da) [#20150](https://github.com/NVIDIA/TensorRT-LLM/pull/20150)
  [None][test] Split QA test lists by GPU marker requirements (#20150)
  _Files: `scripts/split_qa_by_gpu.py`, `tests/unittest/scripts/test_split_qa_by_gpu.py`_
- **2026-10-12** [`4f442e50a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f442e50a5) [#19809](https://github.com/NVIDIA/TensorRT-LLM/pull/19809)
  [https://nvbugs/6838020][fix] Tolerate near-tie greedy flips in KV pool rebalance accuracy test (#19809)
  _Files: `tests/integration/defs/accuracy/test_kv_pool_rebalance_accuracy.py`_
- **2026-10-12** [`aaf3e07c1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaf3e07c1e) [#20148](https://github.com/NVIDIA/TensorRT-LLM/pull/20148)
  [TRTLLMINF-481][fix] handle outdated unresolved review threads (#20148)
  _Files: `.github/workflows/full-premerge-approval-signal.yml`, `.github/workflows/full-premerge-approval.yml`_
- **2026-10-10** [`8d9ca405f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d9ca405f1) [#16262](https://github.com/NVIDIA/TensorRT-LLM/pull/16262)
  [None][chore] remove orphaned process_streaming_events helper (#16262)
  _Files: `tensorrt_llm/serve/responses_utils.py`_
- **2026-10-09** [`dc56f5ccb2`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc56f5ccb2) [#19872](https://github.com/NVIDIA/TensorRT-LLM/pull/19872)
  [None][fix] Ignore virtualenv and editable-install entries in the pytest sys.path check (#19872)
  _Files: `tests/test_common/magic_import_hooks.py`, `tests/unittest/others/test_magic_import.py`_
- **2026-10-08** [`45c7060ab1`](https://github.com/NVIDIA/TensorRT-LLM/commit/45c7060ab1) [#19930](https://github.com/NVIDIA/TensorRT-LLM/pull/19930)
  [None][fix] Isolate serve performance test logs across concurrent launches (#19930)
  _Files: `tests/integration/defs/perf/utils.py`_
- **2026-10-08** [`5f1b2490cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f1b2490cc) [#19766](https://github.com/NVIDIA/TensorRT-LLM/pull/19766)
  [None][fix] agent-flow: spill oversized system prompts to a file and forward Claude CLI stderr (#19766)
  _Files: `agent-flow/agent_flow/backends/claude_code.py`, `agent-flow/tests/test_backends.py`_
- **2026-10-08** [`edc41150e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/edc41150e6) [#19957](https://github.com/NVIDIA/TensorRT-LLM/pull/19957)
  [None][fix] Keep FetchContent patch command a single shell argument (#19957)
  _Files: `3rdparty/CMakeLists.txt`_
- **2026-10-08** [`b8af588782`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8af588782) [#19553](https://github.com/NVIDIA/TensorRT-LLM/pull/19553)
  [https://nvbugs/6782263][fix] Serialize HF remote-code loading when building tokenizers (#19553)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`_
- **2026-10-07** [`a1f562a696`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1f562a696) [#19858](https://github.com/NVIDIA/TensorRT-LLM/pull/19858)
  [None][fix] OpenEngine: release completed results and honor TRTLLM_SERVER_DISABLE_GC (#19858)
  _Files: `tensorrt_llm/grpc/openengine/server.py`, `tensorrt_llm/grpc/openengine/servicer.py`, `tests/unittest/grpc/openengine/test_openengine.py`, `tests/unittest/grpc/openengine/test_servicer.py`_
- **2026-10-07** [`1e84796dd3`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e84796dd3) [#19927](https://github.com/NVIDIA/TensorRT-LLM/pull/19927)
  [None][chore] Remove unused negative-test helpers (#19927)
  _Files: `tests/integration/defs/triton_server/trt_test_alternative.py`, `tests/integration/defs/trt_test_alternative.py`_
- **2026-10-06** [`5cf80d611f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cf80d611f) [#19697](https://github.com/NVIDIA/TensorRT-LLM/pull/19697)
  [https://nvbugs/6840916][fix] Clean up orphaned perf test workers on failure (#19697)
  _Files: `tests/integration/defs/perf/utils.py`_
- **2026-10-06** [`089d586d83`](https://github.com/NVIDIA/TensorRT-LLM/commit/089d586d83) [#19830](https://github.com/NVIDIA/TensorRT-LLM/pull/19830)
  [None][fix] kdaDecode legacy: __syncwarp before the lane-0 block-reduce stores (#19830)
  _Files: `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeLegacy.cu`_

## MoE  (11 commits)

- **2026-10-12** [`e67c26201a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e67c26201a) [#19272](https://github.com/NVIDIA/TensorRT-LLM/pull/19272)
  [None][feat] Wire Rubin locality-domain execution through PyTorch models (#19272)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+30 more__
- **2026-10-09** [`01a3a967a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/01a3a967a9) [#19929](https://github.com/NVIDIA/TensorRT-LLM/pull/19929)
  [TRTLLM-16770][fix] Fix W4A16 NVFP4 MoE dequantization and EPLB migration, and add Nemotron-H to EPLB allowlist (#19929)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/moe/fused_moe/moe_load_balancer.py`, `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/unittest/_torch/moe/test_moe_load_balancer.py` _+1 more__
- **2026-10-09** [`bcaf5e6c97`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcaf5e6c97) [#19183](https://github.com/NVIDIA/TensorRT-LLM/pull/19183)
  [None][feat] Rubin merge-back: SM107 MoE, CFT release op, MegaMoE multi-node bootstrap, core runtime fixes (#19183)
  _Files: `cpp/tensorrt_llm/thop/moe/communication/moeAlltoAllOp.cpp`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/manual_mma_128dp.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/utils.py` _+15 more__
- **2026-10-09** [`a82b8a4dd4`](https://github.com/NVIDIA/TensorRT-LLM/commit/a82b8a4dd4) [#20009](https://github.com/NVIDIA/TensorRT-LLM/pull/20009)
  [None][chore] update bench_moe situ support list (#20009)
  _Files: `tests/microbenchmarks/bench_moe/build.py`, `tests/microbenchmarks/bench_moe/specs.py`_
- **2026-10-08** [`3beeef3a5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3beeef3a5f) [#18485](https://github.com/NVIDIA/TensorRT-LLM/pull/18485)
  [TRTLLM-14620][feat] Add ragged sparse-attention row contracts (#18485)
  _Files: `cpp/tensorrt_llm/kernels/IndexerTopK.h`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.h`, `cpp/tensorrt_llm/kernels/indexerTopK.cu` _+25 more__
- **2026-10-08** [`2681ed10c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/2681ed10c9) [#19896](https://github.com/NVIDIA/TensorRT-LLM/pull/19896)
  [TRTLLM-15762][refactor] Migrate decoder execution and private resources into the runner family (#19896)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py` _+39 more__
- **2026-10-08** [`535c3e08b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/535c3e08b6) [#19749](https://github.com/NVIDIA/TensorRT-LLM/pull/19749)
  [None][feat] MoE scheduler: optional finalize-before-combine and FP4 scale-layout contract fix (#19749)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/communication/base.py`, `tensorrt_llm/_torch/moe/fused_moe/communication/deep_ep_low_latency.py`, `tensorrt_llm/_torch/moe/fused_moe/configurable_moe.py` _+10 more__
- **2026-10-08** [`ce436a9b4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce436a9b4e) [#17067](https://github.com/NVIDIA/TensorRT-LLM/pull/17067)
  [None][feat] Support K-EXAONE-2 in the PyTorch backend (#17067)
  _Files: `docs/source/developer-guide/telemetry.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/checkpoints/hf/exaone_moe_weight_mapper.py` _+9 more__
- **2026-10-07** [`4a36c5b2fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a36c5b2fb) [#19901](https://github.com/NVIDIA/TensorRT-LLM/pull/19901)
  [None][fix] Cache resolved MegaMoE kernel descriptors across forwards (#19901)
  _Files: `tensorrt_llm/_torch/moe/custom_ops/cute_dsl_megamoe_custom_op.py`_
- **2026-10-06** [`481e98eb4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/481e98eb4f) [#19539](https://github.com/NVIDIA/TensorRT-LLM/pull/19539)
  [None][chore] CUTEDSL_FC12 phase-specific smem AB stages with FC2 epilogue overlay (#19539)
  _Files: `.pre-commit-config.yaml`, `pyproject.toml`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_grouped_blockscaled_gemm_fused_fc12.py`, `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`_
- **2026-10-05** [`2ef828c4c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ef828c4c9) [#19445](https://github.com/NVIDIA/TensorRT-LLM/pull/19445)
  [None][build] Improve C++ build structure (#19445)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt`, `cpp/tensorrt_llm/executor/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/cutlass_kernels/CMakeLists.txt` _+4 more__

## Quantization  (10 commits)

- **2026-10-12** [`d7882af43f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7882af43f) [#20077](https://github.com/NVIDIA/TensorRT-LLM/pull/20077)
  [TRTLLM-16956][feat] Modeling V2 dynamic switch with LLM config and args (#20077)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/modeling_v2_rule.py`, `tensorrt_llm/_torch/_experimental/__init__.py` _+22 more__
- **2026-10-12** [`f11628197f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f11628197f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-10-11** [`f84a4ba7f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/f84a4ba7f2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+3 more__
- **2026-10-10** [`41fed06b60`](https://github.com/NVIDIA/TensorRT-LLM/commit/41fed06b60)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+7 more__
- **2026-10-09** [`03425410c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/03425410c5) [#20012](https://github.com/NVIDIA/TensorRT-LLM/pull/20012)
  [https://nvbugs/6700265][test] Unwaive TestDeepSeekV3Lite test_fp8_block_scales (#20012)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-09** [`4ea5b0c7fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ea5b0c7fd) [#19237](https://github.com/NVIDIA/TensorRT-LLM/pull/19237)
  [None][feat] Split VisualGen LPIPS golden media by model family and refresh goldens (#19237)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_fp8_blockwise_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_nvfp4_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/flux1_nvfp4_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/glm_image_nvfp4_lpips_golden.json` _+25 more__
- **2026-10-08** [`aa8a4523ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa8a4523ab) [#19918](https://github.com/NVIDIA/TensorRT-LLM/pull/19918)
  [https://nvbugs/6810945][fix] Remove stale Kimi FP8 tests and gate Rubin coverage (#19918)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/thop/parallel/test_kimi_k3_fp8_weight_read_linear.py`_
- **2026-10-07** [`72688933d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/72688933d5) [#19810](https://github.com/NVIDIA/TensorRT-LLM/pull/19810)
  [https://nvbugs/6838021][test] Unwaive MiniMax-M3 MXFP8 piecewise CUDA graph test on B300 (#19810)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-06** [`37d332fa1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/37d332fa1c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+5 more__
- **2026-10-05** [`bb367fc8c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb367fc8c1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__

## Disaggregation / KV  (9 commits)

- **2026-10-12** [`ca3a6c4c62`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca3a6c4c62) [#20093](https://github.com/NVIDIA/TensorRT-LLM/pull/20093)
  [None][feat] Let a model require KV cache manager v2 instead of being demoted to v1 (#20093)
  _Files: `tensorrt_llm/llmapi/llm_utils.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-10-12** [`a8d7911bed`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8d7911bed) [#19857](https://github.com/NVIDIA/TensorRT-LLM/pull/19857)
  [https://nvbugs/6865617][fix] Poll the disagg gen-init KV receive fence instead of blocking the overlap scheduler (#19857)
  _Files: `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/disaggregation/coordinator_harness.py` _+2 more__
- **2026-10-12** [`caed3b4e67`](https://github.com/NVIDIA/TensorRT-LLM/commit/caed3b4e67) [#19928](https://github.com/NVIDIA/TensorRT-LLM/pull/19928)
  [https://nvbugs/6818106][fix] Compare disaggregated logprobs on the KV reuse path (#19928)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_
- **2026-10-10** [`e1b0ee3032`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1b0ee3032) [#19171](https://github.com/NVIDIA/TensorRT-LLM/pull/19171)
  [TRTLLM-12891][feat] Integrate Mooncake connector into KVCMv2 (#19171)
  _Files: `docs/source/features/kv-cache-connector.md`, `examples/disaggregated/slurm/benchmark/disaggr_torch.slurm`, `examples/disaggregated/slurm/benchmark/submit.py`, `examples/llm-api/configs/trtllm_mooncake_store_connector_extra.yaml` _+49 more__
- **2026-10-09** [`94df4836f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/94df4836f2) [#19939](https://github.com/NVIDIA/TensorRT-LLM/pull/19939)
  [None][perf] Format the AUX-delivery debug message only when debug lo… (#19939)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_sender_aux_debug_log.py`_
- **2026-10-09** [`fbbeac3265`](https://github.com/NVIDIA/TensorRT-LLM/commit/fbbeac3265) [#19895](https://github.com/NVIDIA/TensorRT-LLM/pull/19895)
  [https://nvbugs/6842946][test] Unwaive Qwen3-VL disaggregated KV cache tests (#19895)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-08** [`d2487301ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2487301ca) [#19801](https://github.com/NVIDIA/TensorRT-LLM/pull/19801)
  [None][fix] prevent multimodal scheduling stalls on the KV cache V2 scheduler (#19801)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/executor/multimodal_utils.py`, `tests/unittest/_torch/executor/test_multimodal_scheduler.py`_
- **2026-10-06** [`2914df8aa6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2914df8aa6) [#19663](https://github.com/NVIDIA/TensorRT-LLM/pull/19663)
  [None][test] Add KV transfer lifecycle acceptance regressions (#19663)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/unittest/disaggregated/lifecycle_acceptance.md`, `tests/unittest/disaggregated/test_transfer_lifecycle_acceptance.py`, `tests/unittest/disaggregated/test_transfer_lifecycle_gpu.py` _+2 more__
- **2026-10-06** [`2b2c5be2dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b2c5be2dc) [#17306](https://github.com/NVIDIA/TensorRT-LLM/pull/17306)
  [None][fix] Support beam search with C++ KVCacheManagerV2 (#17306)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+26 more__

## Torch Path (_torch)  (8 commits)

- **2026-10-12** [`5e3265ebc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e3265ebc9) [#20021](https://github.com/NVIDIA/TensorRT-LLM/pull/20021)
  [None][fix] Keep a one-rank DeviceMeshTopology off the job-wide device mesh (#20021)
  _Files: `tensorrt_llm/_torch/device_mesh.py`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_mapping.py`_
- **2026-10-09** [`92d23a8379`](https://github.com/NVIDIA/TensorRT-LLM/commit/92d23a8379) [#19506](https://github.com/NVIDIA/TensorRT-LLM/pull/19506)
  [TRTLLM-16667][feat] Add Minimax H3 Parallel Tiled VAE Decoding and Ulysses Support (#19506)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/minimax-h3-bf16-8gpu.yaml` _+11 more__
- **2026-10-09** [`b5a0afd6b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5a0afd6b8) [#19679](https://github.com/NVIDIA/TensorRT-LLM/pull/19679)
  [TRTLLMINF-474][infra] Upgrade NGC PyTorch base image to 26.09 (#19679)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `docker/common/install_cuda_libs.sh`, `docker/common/install_mooncake.sh` _+7 more__
- **2026-10-08** [`58fd2d3fc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/58fd2d3fc8) [#19600](https://github.com/NVIDIA/TensorRT-LLM/pull/19600)
  [https://nvbugs/6729495][fix] Restore Nemotron-H weight-update coverage (#19600)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/install_mamba.sh`, `jenkins/scripts/slurm_install.sh`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-10-06** [`d3c788b086`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3c788b086) [#19500](https://github.com/NVIDIA/TensorRT-LLM/pull/19500)
  [#19495][fix] Align LTX-2 scale factors with tensor axes (#19500)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/types.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/video_vae/video_vae.py`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_
- **2026-10-06** [`aa026bf86d`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa026bf86d) [#19657](https://github.com/NVIDIA/TensorRT-LLM/pull/19657)
  [TRTLLM-16670][feat] Add MiniMax H3 ref2va mode support (#19657)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/minimax-h3-ref2va-bf16-1gpu.yaml`, `examples/visual_gen/models/minimax_h3.py` _+8 more__
- **2026-10-06** [`6603d00dc2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6603d00dc2) [#19613](https://github.com/NVIDIA/TensorRT-LLM/pull/19613)
  [None][perf] Allow prefix-tokenization cache for MiniMax-M3 text-only prompts (#19613)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3_vl.py`, `tensorrt_llm/inputs/registry.py`_
- **2026-10-06** [`8780061e79`](https://github.com/NVIDIA/TensorRT-LLM/commit/8780061e79) [#18636](https://github.com/NVIDIA/TensorRT-LLM/pull/18636)
  [None][perf] use index copy for multimodal fusion (#18636)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tests/unittest/_torch/multimodal/test_fuse_input_embeds.py`_

## Models  (8 commits)

- **2026-10-12** [`49334c15ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/49334c15ce) [#20026](https://github.com/NVIDIA/TensorRT-LLM/pull/20026)
  [None][test] Prune Kimi-K2 accuracy tests (#20026)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/perf/_model_paths.py` _+7 more__
- **2026-10-11** [`55279c109f`](https://github.com/NVIDIA/TensorRT-LLM/commit/55279c109f) [#19797](https://github.com/NVIDIA/TensorRT-LLM/pull/19797)
  [None][perf] use GEMM patch projection and reuse fused QKV in Qwen vision encoders (#19797)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tests/unittest/_torch/modeling/test_modeling_qwen2vl.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3vl.py`_
- **2026-10-09** [`49ec573042`](https://github.com/NVIDIA/TensorRT-LLM/commit/49ec573042) [#20020](https://github.com/NVIDIA/TensorRT-LLM/pull/20020)
  [https://nvbugs/6278337][fix] Unwaive DeepSeekV3Lite bf16 PP4 tests (#20020)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-08** [`cc63e66daf`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc63e66daf) [#19958](https://github.com/NVIDIA/TensorRT-LLM/pull/19958)
  [https://nvbugs/6345827][test] Unwaive DeepSeekV3Lite disagg MTP test_auto_dtype on H20 and H100 (#19958)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-08** [`f891b3d9ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/f891b3d9ba) [#19829](https://github.com/NVIDIA/TensorRT-LLM/pull/19829)
  [None][fix] Kimi K3 attn_res kernels: order the ws_stats reads and fence the slot releases (#19829)
  _Files: `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.cu`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.cu`, `tests/unittest/_torch/modules/kimi_k3_attn_res/test_attn_res_proxy_fences.py`_
- **2026-10-08** [`807a036f06`](https://github.com/NVIDIA/TensorRT-LLM/commit/807a036f06) [#19885](https://github.com/NVIDIA/TensorRT-LLM/pull/19885)
  [None][fix] Kimi K3 KDA prefill: cap the scratch caches at 2 entries (#19885)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_custom_ops.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modules/kimi_kda/test_kda_buf_cache_bounded.py`_
- **2026-10-07** [`a40d97aa57`](https://github.com/NVIDIA/TensorRT-LLM/commit/a40d97aa57) [#19260](https://github.com/NVIDIA/TensorRT-LLM/pull/19260)
  [TRTLLM-16217][test] Add VR200 4-GPU serve perf cases for DeepSeek V4 Pro and Kimi K3 (#19260)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-10-07** [`dcdd9576b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/dcdd9576b4) [#19178](https://github.com/NVIDIA/TensorRT-LLM/pull/19178)
  [None][test] Replace TinyLlama-1.1B-Chat-v1.0 with Qwen3-0.6B in tests (#19178)

## Perf  (1 commits)

- **2026-10-12** [`f0df326ed6`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0df326ed6) [#19794](https://github.com/NVIDIA/TensorRT-LLM/pull/19794)
  [None][perf] Decode RGB and grayscale JPEGs with torchvision in ImageMediaIO (#19794)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tests/unittest/inputs/test_image_decode.py`_

## LoRA  (1 commits)

- **2026-10-05** [`dc31d8ddef`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc31d8ddef) [#19701](https://github.com/NVIDIA/TensorRT-LLM/pull/19701)
  [TRTLLM-16672][feat] MiniMax H3 Turbo LoRA Tensor Name Mapping (#19701)
  _Files: `tensorrt_llm/_torch/visual_gen/runtime_lora.py`, `tests/unittest/_torch/visual_gen/test_runtime_lora.py`_

---
_Generated 2026-10-12 17:48 UTC_