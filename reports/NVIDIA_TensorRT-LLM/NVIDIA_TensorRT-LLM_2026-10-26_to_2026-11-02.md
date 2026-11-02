# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-10-26 → 2026-11-02  |  **Total commits:** 280

## ✨ New Features This Week

- **2026-11-02** [#21210](https://github.com/NVIDIA/TensorRT-LLM/pull/21210) — [None][perf] Enable FlashInfer GDN chunked prefill on SM107 (#21210)
- **2026-11-02** [#21122](https://github.com/NVIDIA/TensorRT-LLM/pull/21122) — [TRTLLM-17125][feat] Preempt requests on KV pressure under aggregated Helix (#21122)
- **2026-11-02** [#20999](https://github.com/NVIDIA/TensorRT-LLM/pull/20999) — [None][test] Add GLM-5.3 core performance coverage (#20999)
- **2026-11-02** [#21331](https://github.com/NVIDIA/TensorRT-LLM/pull/21331) — [None][test] Add DGX Spark agentic and real-text speculative decoding perf cases (#21331)
- **2026-10-31** [#20306](https://github.com/NVIDIA/TensorRT-LLM/pull/20306) — [None][feat] MiniMax-M3 NVFP4 low-latency decode megakernel for modeling_v2 for Blackwell (#20306)
- **2026-10-31** [#20787](https://github.com/NVIDIA/TensorRT-LLM/pull/20787) — [TRTLLM-16598][feat] Sol-Attn: optional Morton (Z-order) token ordering for Wan (#20787)
- **2026-10-31** [#20491](https://github.com/NVIDIA/TensorRT-LLM/pull/20491) — [TRTLLM-17083][feat] Cancel paired GEN on CTX failure or cancellation (#20491)
- **2026-10-31** [#21125](https://github.com/NVIDIA/TensorRT-LLM/pull/21125) — [None][feat] Add image routing metadata to OpenEngine KV events (#21125)
- **2026-10-30** [#21353](https://github.com/NVIDIA/TensorRT-LLM/pull/21353) — [None][doc] Point to model side branches from the supported models page (#21353)
- **2026-10-30** [#19646](https://github.com/NVIDIA/TensorRT-LLM/pull/19646) — [None][feat] Add DynamicEPLB kernels and runtime integration (#19646)
- _…and 48 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-11-02** [`a9be7004c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9be7004c7) [#20049](https://github.com/NVIDIA/TensorRT-LLM/pull/20049) — [None][chore] Remove the Python KV bounce buffer; kv_cache_bounce_size_mb selects the C++ agent bounce (#20049)
- **2026-10-31** [`66190c8fd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/66190c8fd5) [#21175](https://github.com/NVIDIA/TensorRT-LLM/pull/21175) — [None][chore] Update Modeling V2 code and test ownership (#21175)
- **2026-10-30** [`c50ea882ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/c50ea882ef) [#20888](https://github.com/NVIDIA/TensorRT-LLM/pull/20888) — [None][feat] Kimi K3: support NVFP4 KV cache (FP4 MLA) with the hybrid KV cache manager (#20888)
- **2026-10-29** [`e4d5e2eaa7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4d5e2eaa7) [#21158](https://github.com/NVIDIA/TensorRT-LLM/pull/21158) — [TRTLLM-17348][refactor] Reorganize engine and decoder tests around component ownership (#21158)
- **2026-10-27** [`94348c4de6`](https://github.com/NVIDIA/TensorRT-LLM/commit/94348c4de6) [#19575](https://github.com/NVIDIA/TensorRT-LLM/pull/19575) — [None][fix] Python transceiver: run gen-side KV transfer consensus across helix CP ranks under attention-DP (#19575)
- **2026-10-26** [`758c7b5ba4`](https://github.com/NVIDIA/TensorRT-LLM/commit/758c7b5ba4) [#20947](https://github.com/NVIDIA/TensorRT-LLM/pull/20947) — [None][fix] EagerMoeWorkspace test and LoRA tests (#20947)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#21318](https://github.com/NVIDIA/TensorRT-LLM/issues/21318) | [Bug]: Streamed final text keeps the start of a multi-token stop word; | — | 2026-10-30 |
| [#21102](https://github.com/NVIDIA/TensorRT-LLM/issues/21102) | [Feature]: Option to run the OpenEngine gRPC server on pygrpc-native | Frontend | 2026-10-27 |
| [#10024](https://github.com/NVIDIA/TensorRT-LLM/issues/10024) | [Bug] TRTLLM_NIXL_KVCACHE_BACKEND causes rail endpoint serialization m | KV-Cache Management, Disaggregated serving | 2026-10-27 |
| [#20082](https://github.com/NVIDIA/TensorRT-LLM/issues/20082) | [Bug]: Ray orchestrator with attention DP and TRTLLM_FORCE_COMM_METHOD | Disaggregated serving, Scale-out | 2026-10-27 |
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
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-10-08 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-10-05 |
| [#19820](https://github.com/NVIDIA/TensorRT-LLM/issues/19820) | [New Model]: Apertus (swiss-ai/Apertus-8B-Instruct-2509, swiss-ai/Aper | new model | 2026-10-02 |
| [#19666](https://github.com/NVIDIA/TensorRT-LLM/issues/19666) | [Feature]: EFA should work out of the box on NGC TRTLLM release image  | feature request, OOTB | 2026-10-01 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-10-01 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Executor / Runtime | 53 |
| CI / Infra | 51 |
| Attention | 46 |
| MoE | 28 |
| Other | 19 |
| Torch Path (_torch) | 17 |
| Disaggregation / KV | 15 |
| Quantization | 14 |
| Models | 11 |
| Docs / Examples | 9 |
| LoRA | 7 |
| ROCm / AMD | 6 |
| Speculative Decoding | 3 |
| Perf | 1 |

## Executor / Runtime  (53 commits)

- **2026-11-02** [`cbef70dbc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbef70dbc9) [#21349](https://github.com/NVIDIA/TensorRT-LLM/pull/21349)
  [None][test] Run session-reuse unit tests in CPU CI (#21349)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_session_reuse.py`_
- **2026-11-02** [`b6bb149fac`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6bb149fac) [#21266](https://github.com/NVIDIA/TensorRT-LLM/pull/21266)
  [https://nvbugs/7016691][fix] Bound ZeroMqQueue close linger so teardown cannot hang (#21266)
  _Files: `tensorrt_llm/executor/ipc.py`, `tests/unittest/executor/test_ipc.py`_
- **2026-11-02** [`4b697f1e2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b697f1e2a) [#21231](https://github.com/NVIDIA/TensorRT-LLM/pull/21231)
  [None][test] Guard lazy engine initialization and GPU-free imports (#21231)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/executor/test_model_engine_initialization.py`, `tests/unittest/others/test_import_cuda_context.py` _+1 more__
- **2026-11-01** [`7a62522fb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a62522fb8) [#20900](https://github.com/NVIDIA/TensorRT-LLM/pull/20900)
  [https://nvbugs/6858828][fix] Check the FORCE_CHUNK context limit when creating the micro-batch scheduler (#20900)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler.py`, `tests/unittest/_torch/pyexecutor/test_forced_chunk_context_limit.py`_
- **2026-10-31** [`d5752a1c36`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5752a1c36) [#21036](https://github.com/NVIDIA/TensorRT-LLM/pull/21036)
  [TRTLLM-16628][refactor] BREAKING: Remove unused LlmRequest fields (#21036)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/include/tensorrt_llm/executor/serialization.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp` _+32 more__
- **2026-10-31** [`17bfe4e06e`](https://github.com/NVIDIA/TensorRT-LLM/commit/17bfe4e06e) [#21142](https://github.com/NVIDIA/TensorRT-LLM/pull/21142)
  [TRTLLM-17500][fix] Publish cache reset events without waiting for inference (#21142)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventSink.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/streamingEventSink.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/streamingEventSink.h` _+17 more__
- **2026-10-31** [`c8ee74b9fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8ee74b9fe) [#21125](https://github.com/NVIDIA/TensorRT-LLM/pull/21125)
  [None][feat] Add image routing metadata to OpenEngine KV events (#21125)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/kv_cache_events.py`, `tensorrt_llm/grpc/openengine/README.md`, `tensorrt_llm/grpc/openengine/capabilities.py` _+11 more__
- **2026-10-30** [`b6d1a0616f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6d1a0616f) [#19646](https://github.com/NVIDIA/TensorRT-LLM/pull/19646)
  [None][feat] Add DynamicEPLB kernels and runtime integration (#19646)
- **2026-10-30** [`d870ded367`](https://github.com/NVIDIA/TensorRT-LLM/commit/d870ded367) [#20669](https://github.com/NVIDIA/TensorRT-LLM/pull/20669)
  [TRTLLM-14849][chore] Rename tests/unittest/_torch/executor to pyexecutor and split out its connector tests (#20669)
- **2026-10-30** [`a8ec29c58e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8ec29c58e) [#21104](https://github.com/NVIDIA/TensorRT-LLM/pull/21104)
  [None][fix] DeepSeek-V4.1: namespaced Responses tools and calls in the checkpoint's form (#21104)
  _Files: `tensorrt_llm/serve/extensions/__init__.py`, `tensorrt_llm/serve/extensions/deepseek_v41.py`, `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/responses_utils.py` _+6 more__
- **2026-10-30** [`aecb1f224c`](https://github.com/NVIDIA/TensorRT-LLM/commit/aecb1f224c) [#21236](https://github.com/NVIDIA/TensorRT-LLM/pull/21236)
  [https://nvbugs/6997729][fix] Keep UCX on loopback in the disagg perf-metrics test (#21236)
  _Files: `tests/unittest/llmapi/apps/test_disagg_serving_perf_metrics.py`_
- **2026-10-30** [`93e348cfd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/93e348cfd0) [#21072](https://github.com/NVIDIA/TensorRT-LLM/pull/21072)
  [None][fix] Responses: detokenize for the parsers as chat completions does (#21072)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-30** [`0c259e6003`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c259e6003) [#21053](https://github.com/NVIDIA/TensorRT-LLM/pull/21053)
  [None][fix] Responses: a reasoning object turns thinking on; DeepSeek-V4.1 takes OpenAI effort levels (#21053)
  _Files: `tensorrt_llm/serve/responses_utils.py`, `tensorrt_llm/tokenizer/deepseek_v41/tokenizer.py`, `tests/unittest/llmapi/apps/test_chat_template_kwargs_guard.py`, `tests/unittest/llmapi/test_deepseek_v41_tokenizer.py`_
- **2026-10-30** [`1d46219d36`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d46219d36) [#20805](https://github.com/NVIDIA/TensorRT-LLM/pull/20805)
  [https://nvbugs/6899677][fix] Default NCCL_GRAPH_REGISTER=0 before creating the pipeline-parallel NCCL communicator (#20805)
  _Files: `cpp/tensorrt_llm/runtime/ncclCommunicator.cpp`_
- **2026-10-30** [`8fad4ca454`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fad4ca454) [#21148](https://github.com/NVIDIA/TensorRT-LLM/pull/21148)
  [None][fix] Perf metrics: the JSONL writer survives unexpected errors (#21148)
  _Files: `tensorrt_llm/serve/perf_metrics.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/apps/test_request_metrics.py`_
- **2026-10-30** [`4f5e469378`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f5e469378) [#21154](https://github.com/NVIDIA/TensorRT-LLM/pull/21154)
  [None][fix] Chat Completions: accept service_tier and client_metadata (#21154)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/api_stability/references/trtllm_serve_api.yaml`, `tests/unittest/llmapi/apps/test_openai_protocol_chat_agent_fields.py`_
- **2026-10-30** [`267ccd87fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/267ccd87fc) [#21268](https://github.com/NVIDIA/TensorRT-LLM/pull/21268)
  [None][perf] SID-GR 5/N: Reduce client side overhead in beam search (#21268)
  _Files: `tensorrt_llm/executor/result.py`_
- **2026-10-30** [`48cf4f69dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/48cf4f69dd) [#19379](https://github.com/NVIDIA/TensorRT-LLM/pull/19379)
  [TRTLLM-14510][feat] BREAKING: serve: default num_serve_frontends to 8 with single-frontend fallback (#19379)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/commands/serve.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+5 more__
- **2026-10-30** [`b681c74c05`](https://github.com/NVIDIA/TensorRT-LLM/commit/b681c74c05) [#19529](https://github.com/NVIDIA/TensorRT-LLM/pull/19529)
  [None][fix] preserve multimodal UUID in V2 KV events (#19529)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventData.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventData.h` _+20 more__
- **2026-10-30** [`bba275b1ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/bba275b1ab) [#21307](https://github.com/NVIDIA/TensorRT-LLM/pull/21307)
  [None][fix] Apply ruff-format to model_engine.py DSpark properties (#21307)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-10-30** [`4cd6c19923`](https://github.com/NVIDIA/TensorRT-LLM/commit/4cd6c19923) [#21109](https://github.com/NVIDIA/TensorRT-LLM/pull/21109)
  [None][fix] GLM reasoning parser: drop the owed </think> after a tool call; read the thinking mode off the prompt (#21109)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/apps/test_reasoning_prompt_resolution.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_
- **2026-10-30** [`df5fe6d0ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/df5fe6d0ca) [#20764](https://github.com/NVIDIA/TensorRT-LLM/pull/20764)
  [TRTLLM-14892][feat] Qualify the Qwen3.5 dense vision-language root for MX (#20764)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py` _+10 more__
- **2026-10-29** [`9d3b492125`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d3b492125) [#20331](https://github.com/NVIDIA/TensorRT-LLM/pull/20331)
  [https://nvbugs/6700875][fix] Drain cached test MPI pools before a test starts a child process (#20331)
  _Files: `tests/conftest.py`, `tests/integration/test_lists/waives.txt`, `tests/test_common/session_reuse.py`, `tests/test_common/session_reuse_hooks.py` _+1 more__
- **2026-10-29** [`7d8d94684c`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d8d94684c) [#21034](https://github.com/NVIDIA/TensorRT-LLM/pull/21034)
  [#21032][feat] Expose OpenEngine Prometheus metrics (#21034)
  _Files: `security_scanning/poetry.lock`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/rpc/rpc_client.py` _+15 more__
- **2026-10-29** [`23a8d36397`](https://github.com/NVIDIA/TensorRT-LLM/commit/23a8d36397) [#21159](https://github.com/NVIDIA/TensorRT-LLM/pull/21159)
  [TRTLLM-17342][refactor] Remove model_engine.py from legacy formatting and modernize type annotations (#21159)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+1 more__
- **2026-10-29** [`49b31974b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/49b31974b4) [#21237](https://github.com/NVIDIA/TensorRT-LLM/pull/21237)
  [https://nvbugs/6991642][fix] fix test_startup_metrics_by_server_info  (#21237)
  _Files: `tests/unittest/llmapi/test_llm.py`_
- **2026-10-28** [`679936e08f`](https://github.com/NVIDIA/TensorRT-LLM/commit/679936e08f) [#20912](https://github.com/NVIDIA/TensorRT-LLM/pull/20912)
  [https://nvbugs/6973693][fix] Disable KV block reuse in test_llmapi_backend (#20912)
  _Files: `tests/integration/defs/triton_server/test_triton_llmapi.py`_
- **2026-10-28** [`3b4eebcf02`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b4eebcf02) [#21126](https://github.com/NVIDIA/TensorRT-LLM/pull/21126)
  [None][perf] SID-GR 4/N: Skip beam search temperature pass when temperature is 1 (#21126)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`_
- **2026-10-28** [`0cd0a183ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/0cd0a183ca) [#19394](https://github.com/NVIDIA/TensorRT-LLM/pull/19394)
  [None][fix] serve: make multi-frontend metrics, profiling and liveness launcher-owned (#19394)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/_frontend_processes.py`, `tensorrt_llm/serve/multi_frontend.py`, `tensorrt_llm/serve/openai_server.py` _+3 more__
- **2026-10-27** [`0746a23338`](https://github.com/NVIDIA/TensorRT-LLM/commit/0746a23338) [#20905](https://github.com/NVIDIA/TensorRT-LLM/pull/20905)
  [None][refactor] Improve child request creation and preserve request inputs (#20905)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `cpp/tensorrt_llm/nanobind/executor/request.cpp` _+4 more__
- **2026-10-27** [`39f300f1bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/39f300f1bd) [#20446](https://github.com/NVIDIA/TensorRT-LLM/pull/20446)
  [None][feat] Support image inputs in OpenEngine gRPC (#20446)
  _Files: `tensorrt_llm/_torch/shared_tensor/shared_tensor.py`, `tensorrt_llm/grpc/openengine/capabilities.py`, `tensorrt_llm/grpc/openengine/control.py`, `tensorrt_llm/grpc/openengine/errors.py` _+21 more__
- **2026-10-27** [`df95eda398`](https://github.com/NVIDIA/TensorRT-LLM/commit/df95eda398) [#20434](https://github.com/NVIDIA/TensorRT-LLM/pull/20434)
  [https://nvbugs/6913451][fix] Avoid heavy imports in MPI shutdown (#20434)
  _Files: `docs/source/llm-api/index.md`, `setup.py`, `tensorrt_llm/llmapi/_llmapi_mpi_stop.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch` _+7 more__
- **2026-10-27** [`90e573e91d`](https://github.com/NVIDIA/TensorRT-LLM/commit/90e573e91d) [#21061](https://github.com/NVIDIA/TensorRT-LLM/pull/21061)
  [None][feat] Responses: keepalive events while a stream is silent (#21061)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/responses_utils.py`, `tests/unittest/llmapi/apps/test_responses_streaming_events.py`_
- **2026-10-27** [`ab95e84be2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab95e84be2) [#20772](https://github.com/NVIDIA/TensorRT-LLM/pull/20772)
  [None][fix] Count retained snapshots in hybrid cache sizing (#20772)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/mamba_cache_manager/mamba_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_mamba_cache_manager.py`_
- **2026-10-27** [`55f7033f71`](https://github.com/NVIDIA/TensorRT-LLM/commit/55f7033f71) [#20932](https://github.com/NVIDIA/TensorRT-LLM/pull/20932)
  [None][perf] Qwen: one-launch vision RoPE and batched mRoPE prep (#20932)
  _Files: `tensorrt_llm/_torch/models/modeling_cosmos3_edge.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py` _+2 more__
- **2026-10-27** [`a1eebc47dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1eebc47dd) [#21056](https://github.com/NVIDIA/TensorRT-LLM/pull/21056)
  [None][fix] Responses: resolve namespace::tool calls and restore a dropped namespace on replay (#21056)
  _Files: `tensorrt_llm/serve/responses_utils.py`, `tests/unittest/llmapi/apps/test_responses_custom_tools.py`, `tests/unittest/llmapi/apps/test_responses_input_preprocess.py`, `tests/unittest/llmapi/apps/test_responses_stream_final_consistency.py` _+1 more__
- **2026-10-27** [`c932dd8abb`](https://github.com/NVIDIA/TensorRT-LLM/commit/c932dd8abb) [#21055](https://github.com/NVIDIA/TensorRT-LLM/pull/21055)
  [None][fix] DeepSeek-V3.2 encoder: restore the blank lines of the tools preamble (#21055)
  _Files: `tensorrt_llm/tokenizer/deepseek_v32/encoding.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_deepseek_v32_encoding.py`_
- **2026-10-27** [`2bb7b2fd40`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bb7b2fd40) [#20894](https://github.com/NVIDIA/TensorRT-LLM/pull/20894)
  [TRTLLM-17005][refactor] Component-local C++ Tests (Part 4) (#20894)
  _Files: `AGENTS.md`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/bounce/CMakeLists.txt`, `cpp/tests/CMakeLists.txt` _+8 more__
- **2026-10-27** [`32d8adad86`](https://github.com/NVIDIA/TensorRT-LLM/commit/32d8adad86) [#21051](https://github.com/NVIDIA/TensorRT-LLM/pull/21051)
  [None][fix] DeepSeek renderers: tools join the leading system message; V4.1 renders developer as system (#21051)
  _Files: `tensorrt_llm/tokenizer/deepseek_v32/tokenizer.py`, `tensorrt_llm/tokenizer/deepseek_v4/tokenizer.py`, `tensorrt_llm/tokenizer/deepseek_v41/tokenizer.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+3 more__
- **2026-10-27** [`27c339ab53`](https://github.com/NVIDIA/TensorRT-LLM/commit/27c339ab53) [#20600](https://github.com/NVIDIA/TensorRT-LLM/pull/20600)
  [None][perf] V2 scheduler: demote long uncached prefills behind short reqs (#20600)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py` _+3 more__
- **2026-10-27** [`8354c4c398`](https://github.com/NVIDIA/TensorRT-LLM/commit/8354c4c398) [#20803](https://github.com/NVIDIA/TensorRT-LLM/pull/20803)
  [TRTLLM-17226][perf] Reduce sampler logprobs temporary memory (#20803)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/logprobs.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/triton.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_common.py` _+1 more__
- **2026-10-27** [`82844df1a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/82844df1a9) [#20873](https://github.com/NVIDIA/TensorRT-LLM/pull/20873)
  [None][fix] DeepSeek DSML tool parsers: the layout newlines around tool calls are not content (#20873)
  _Files: `tensorrt_llm/serve/tool_parser/deepseekv32_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-27** [`38d2c3ae7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/38d2c3ae7d) [#21025](https://github.com/NVIDIA/TensorRT-LLM/pull/21025)
  [None][fix] DeepSeek DSML tool parsers: keep string parameter values as written (#21025)
  _Files: `tensorrt_llm/serve/tool_parser/deepseekv32_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-10-26** [`832b2cb7f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/832b2cb7f4) [#20830](https://github.com/NVIDIA/TensorRT-LLM/pull/20830)
  [TRTLLM-16810][perf] SID-GR 3/N: Reduce per-step host overhead for wide beam search (#20830)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`_
- **2026-10-26** [`3f83defd8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f83defd8c) [#20643](https://github.com/NVIDIA/TensorRT-LLM/pull/20643)
  [TRTLLM-17144][feat] Load the Muse Spark Open (muse_spark) config (#20643)
  _Files: `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/musespark_open.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+2 more__
- **2026-10-26** [`cefbde86e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/cefbde86e8) [#20842](https://github.com/NVIDIA/TensorRT-LLM/pull/20842)
  [TRTLLM-17241][fix] Start trtllm-render on a host with no GPU driver (#20842)
  _Files: `docs/source/commands/trtllm-serve/render-endpoints.md`, `setup.py`, `tensorrt_llm/serve/render/trtllm-render`, `tests/unittest/llmapi/apps/test_render_standalone.py` _+1 more__
- **2026-10-26** [`e7d3441e77`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7d3441e77) [#21027](https://github.com/NVIDIA/TensorRT-LLM/pull/21027)
  [None][fix] Use decoder mapping for beam-history rank checks (#21027)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/runner.py`_
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

## CI / Infra  (51 commits)

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
- **2026-11-01** [`d2a9c816ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2a9c816ad) [#21378](https://github.com/NVIDIA/TensorRT-LLM/pull/21378)
  [None][infra] Waive 1 failed cases for main in pre-merge 67464 (#21378)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-11-01** [`650336ed6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/650336ed6f) [#20494](https://github.com/NVIDIA/TensorRT-LLM/pull/20494)
  [TRTLLM-17014][infra] Migrate build artifacts from On-prem to AWS Artifactory (#20494)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `jenkins/BoltProfileGen.groovy`, `jenkins/Build.groovy` _+15 more__
- **2026-10-30** [`0a7f070152`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a7f070152) [#20743](https://github.com/NVIDIA/TensorRT-LLM/pull/20743)
  [None][infra] Remove Verl CI stage (#20743)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/cbts/blocks.py`, `tests/integration/defs/verl/.gitignore` _+5 more__
- **2026-10-30** [`6086b1c5d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/6086b1c5d5) [#21320](https://github.com/NVIDIA/TensorRT-LLM/pull/21320)
  [None][infra] Move the pre-merge perf-sanity cases back to post-merge (#21320)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus_perf_sanity.yml`_
- **2026-10-30** [`3a20b06247`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a20b06247) [#21127](https://github.com/NVIDIA/TensorRT-LLM/pull/21127)
  [None][infra] Add retry for Build stage (#21127)
  _Files: `jenkins/Build.groovy`_
- **2026-10-30** [`aca4a7cc3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/aca4a7cc3a) [#21160](https://github.com/NVIDIA/TensorRT-LLM/pull/21160)
  [TRTLLM-16976][feat] Handle closures in CBTS (#21160)
  _Files: `jenkins/scripts/cbts/cbts/command/coverage/collection/pystart_report.py`, `jenkins/scripts/cbts/cbts/command/coverage/selection/explain.py`, `jenkins/scripts/cbts/cbts/coverage/collection/COLLECTION.md`, `jenkins/scripts/cbts/cbts/coverage/collection/README.md` _+7 more__
- **2026-10-30** [`c69d879b4d`](https://github.com/NVIDIA/TensorRT-LLM/commit/c69d879b4d) [#21093](https://github.com/NVIDIA/TensorRT-LLM/pull/21093)
  [None][infra] preserve auto-triggered stages in CBTS coverage tier (#21093)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-29** [`ee6f321204`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee6f321204) [#21264](https://github.com/NVIDIA/TensorRT-LLM/pull/21264)
  [None][infra] Waive 2 failed cases for main in pre-merge 67069 (#21264)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`0d0ea851bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d0ea851bc) [#21098](https://github.com/NVIDIA/TensorRT-LLM/pull/21098)
  [None][infra] Keep CPU test pods off ipp6/ipp9 DC and clean old node blocklists (#21098)
  _Files: `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_Test.groovy`_
- **2026-10-29** [`29cc04e79d`](https://github.com/NVIDIA/TensorRT-LLM/commit/29cc04e79d) [#21252](https://github.com/NVIDIA/TensorRT-LLM/pull/21252)
  [None][infra] Waive 1 failed cases for main in pre-merge 67018 (#21252)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`380a49051f`](https://github.com/NVIDIA/TensorRT-LLM/commit/380a49051f) [#21247](https://github.com/NVIDIA/TensorRT-LLM/pull/21247)
  [None][infra] Waive 2 failed cases for main in pre-merge 66900 (#21247)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`d9c4f3ba3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9c4f3ba3a) [#21241](https://github.com/NVIDIA/TensorRT-LLM/pull/21241)
  [None][infra] restore L40S pre-merge stage 2 (#21241)
  _Files: `jenkins/config/maintenance_stages.txt`_
- **2026-10-29** [`a42093fc31`](https://github.com/NVIDIA/TensorRT-LLM/commit/a42093fc31) [#16911](https://github.com/NVIDIA/TensorRT-LLM/pull/16911)
  [https://nvbugs/6501404][fix] Unwaive test_row_linear_norm_fusion[2-hidden:16-seqlen:2] (#16911)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`d788792b57`](https://github.com/NVIDIA/TensorRT-LLM/commit/d788792b57) [#21243](https://github.com/NVIDIA/TensorRT-LLM/pull/21243)
  [None][infra] Add blossom-ci authorized users (#21243)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-10-29** [`ec91fb889b`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec91fb889b) [#21227](https://github.com/NVIDIA/TensorRT-LLM/pull/21227)
  [https://nvbugs/6985375][test] Remove waiver for the mixed-precision retained-dtype test (#21227)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`b7b797a3aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7b797a3aa) [#21228](https://github.com/NVIDIA/TensorRT-LLM/pull/21228)
  [None][infra] Waive 1 failed cases for main in pre-merge 66887 (#21228)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-29** [`d008a9bf71`](https://github.com/NVIDIA/TensorRT-LLM/commit/d008a9bf71) [#21205](https://github.com/NVIDIA/TensorRT-LLM/pull/21205)
  [https://nvbugs/6988813][test] Unwaive remote MPI submit_sync (#21205)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`f65df75fcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/f65df75fcd) [#21196](https://github.com/NVIDIA/TensorRT-LLM/pull/21196)
  [https://nvbugs/6986044][fix] Re-enable GLM modeling_v2 routing tests (#21196)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`4a40ab1755`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a40ab1755) [#21193](https://github.com/NVIDIA/TensorRT-LLM/pull/21193)
  [None][infra] Waive 1 failed cases for main in pre-merge 66630 (#21193)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`4f613f2681`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f613f2681) [#20964](https://github.com/NVIDIA/TensorRT-LLM/pull/20964)
  [None][test] Remove 75 closed-bug waive entries for main (#20964)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`207a97a716`](https://github.com/NVIDIA/TensorRT-LLM/commit/207a97a716)
  [None][infra] Reuse build-stage wheels for post-merge release images
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-10-28** [`581b83208a`](https://github.com/NVIDIA/TensorRT-LLM/commit/581b83208a) [#21173](https://github.com/NVIDIA/TensorRT-LLM/pull/21173)
  [None][infra] temporarily pause L40S pre-merge stage 2 (#21173)
  _Files: `jenkins/config/maintenance_stages.txt`_
- **2026-10-28** [`ba16910b40`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba16910b40) [#21168](https://github.com/NVIDIA/TensorRT-LLM/pull/21168)
  [None][infra] Waive 2 failed cases for main in post-merge 3038 (#21168)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`5b9a117439`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b9a117439) [#21167](https://github.com/NVIDIA/TensorRT-LLM/pull/21167)
  [None][infra] Waive 3 failed cases for main in post-merge 3038 (#21167)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`e4a2f6b034`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4a2f6b034)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+2 more__
- **2026-10-28** [`ec0f723a8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec0f723a8a) [#20810](https://github.com/NVIDIA/TensorRT-LLM/pull/20810)
  [None][chore] Split CPU stage (#20810)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/generate_duration.py`, `tests/integration/defs/.test_durations`, `tests/unittest/scripts/cbts/test_docs.py`_
- **2026-10-28** [`617ce36de1`](https://github.com/NVIDIA/TensorRT-LLM/commit/617ce36de1) [#20976](https://github.com/NVIDIA/TensorRT-LLM/pull/20976)
  [None][fix] install CBTS CLI dependencies before selection (#20976)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-10-28** [`7f6b49bb4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f6b49bb4f) [#20574](https://github.com/NVIDIA/TensorRT-LLM/pull/20574)
  [TRTLLM-16976][feat] Enable import-time coverage collection for MPI workers (#20574)
  _Files: `jenkins/scripts/cbts/cbts/command/coverage/collection/pystart_report.py`, `jenkins/scripts/cbts/cbts/coverage/collection/COLLECTION.md`, `jenkins/scripts/cbts/cbts/coverage/collection/README.md`, `jenkins/scripts/cbts/cbts/coverage/collection/channel.py` _+13 more__
- **2026-10-28** [`eb6fc51c94`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb6fc51c94) [#21133](https://github.com/NVIDIA/TensorRT-LLM/pull/21133)
  [TRTLLM-17383][infra] Download Boost from AWS Artifactory (#21133)
  _Files: `docker/common/install_base.sh`_
- **2026-10-28** [`f9281290be`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9281290be) [#21140](https://github.com/NVIDIA/TensorRT-LLM/pull/21140)
  [None][infra] Waive 1 failed cases for main in pre-merge 66696 (#21140)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`111027471a`](https://github.com/NVIDIA/TensorRT-LLM/commit/111027471a) [#21141](https://github.com/NVIDIA/TensorRT-LLM/pull/21141)
  [None][infra] Waive 2 failed cases for main in pre-merge 66681 (#21141)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-27** [`e2787a3220`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2787a3220) [#21117](https://github.com/NVIDIA/TensorRT-LLM/pull/21117)
  [None][infra] Waive 1 failed cases for main in pre-merge 66538 (#21117)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-27** [`0d35000f23`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d35000f23) [#21110](https://github.com/NVIDIA/TensorRT-LLM/pull/21110)
  [None][infra] Waive 3 failed cases for main in pre-merge 66510 (#21110)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-27** [`e805aac356`](https://github.com/NVIDIA/TensorRT-LLM/commit/e805aac356) [#21099](https://github.com/NVIDIA/TensorRT-LLM/pull/21099)
  [TRTLLMINF-471][fix] restore default model storage for GH200 (#21099)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-27** [`c8c4e30935`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8c4e30935) [#21091](https://github.com/NVIDIA/TensorRT-LLM/pull/21091)
  [None][infra] Refine CodeRabbit test review guidance (#21091)
  _Files: `.coderabbit.yaml`_
- **2026-10-27** [`0a2a634914`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a2a634914) [#20288](https://github.com/NVIDIA/TensorRT-LLM/pull/20288)
  [https://nvbugs/6702264][fix] Remove Cosmos3 offload test waiver (#20288)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-27** [`d520836120`](https://github.com/NVIDIA/TensorRT-LLM/commit/d520836120)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+2 more__
- **2026-10-27** [`7587cc8e8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7587cc8e8a) [#20696](https://github.com/NVIDIA/TensorRT-LLM/pull/20696)
  [None][infra] Waive 2 failed cases for main in pre-merge 65038 (#20696)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-27** [`715b8fd0d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/715b8fd0d4) [#20439](https://github.com/NVIDIA/TensorRT-LLM/pull/20439)
  [https://nvbugs/6902353][chore] Unwaive transfer lifecycle GPU tests (#20439)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-26** [`30a9367a2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/30a9367a2c) [#19557](https://github.com/NVIDIA/TensorRT-LLM/pull/19557)
  [None][infra] PLC Pipeline update (#19557)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/TensorRT_LLM_PLC.groovy`, `jenkins/scripts/pulse_in_pipeline_scanning/main.py`, `jenkins/scripts/pulse_in_pipeline_scanning/submit_report.py` _+2 more__
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

## Attention  (46 commits)

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
- **2026-10-31** [`6adeccc026`](https://github.com/NVIDIA/TensorRT-LLM/commit/6adeccc026) [#20787](https://github.com/NVIDIA/TensorRT-LLM/pull/20787)
  [TRTLLM-16598][feat] Sol-Attn: optional Morton (Z-order) token ordering for Wan (#20787)
  _Files: `docs/source/features/visualgen-sparse-attention.md`, `tensorrt_llm/_torch/visual_gen/models/modeling.py`, `tensorrt_llm/_torch/visual_gen/models/wan/transformer_wan.py`, `tensorrt_llm/_torch/visual_gen/token_order.py` _+7 more__
- **2026-10-31** [`3302a31746`](https://github.com/NVIDIA/TensorRT-LLM/commit/3302a31746) [#20911](https://github.com/NVIDIA/TensorRT-LLM/pull/20911)
  [None][chore] Update flashinfer-python from 0.6.18 to 0.7.2 (#20911)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `ATTRIBUTIONS-Python.md`, `requirements.txt` _+7 more__
- **2026-10-30** [`c94fc1c5ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/c94fc1c5ad) [#20769](https://github.com/NVIDIA/TensorRT-LLM/pull/20769)
  [None][fix] Run DeepSeek-V4.1-Flash on SM120 (#20769)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/sm120_blockwise_gemm/sm120_fp8_gemm_1d1d.cuh`, `tensorrt_llm/_torch/attention/backends/sparse/csa2/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/csa2/module.py`, `tensorrt_llm/_torch/attention/backends/sparse/csa2/weights.py` _+7 more__
- **2026-10-30** [`8ba3e60cec`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ba3e60cec) [#21050](https://github.com/NVIDIA/TensorRT-LLM/pull/21050)
  [TRTLLM-17333][ci] Replace 8-GPU Ray pre-merge stage with single-GPU GDN decode alignment test (#21050)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/mamba/test_flashinfer_gdn_decode.py`_
- **2026-10-30** [`dc634e7c9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc634e7c9a) [#21131](https://github.com/NVIDIA/TensorRT-LLM/pull/21131)
  [TRTLLM-17359][fix] Preserve per-rank attention-DP KV metrics (#21131)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/_torch/pyexecutor/adp_iter_stats.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/rank_state.py`, `tensorrt_llm/metrics/collector.py` _+4 more__
- **2026-10-30** [`f58c2fecb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/f58c2fecb9) [#21088](https://github.com/NVIDIA/TensorRT-LLM/pull/21088)
  [None][feat] Support layer and buffer reuse policies for attention and SSM (#21088)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+25 more__
- **2026-10-30** [`d06a796ffb`](https://github.com/NVIDIA/TensorRT-LLM/commit/d06a796ffb) [#16309](https://github.com/NVIDIA/TensorRT-LLM/pull/16309)
  [None][feat] Add DSA Vanilla sparse attention (#16309)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/__init__.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/vanilla_backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/registry.py`, `tensorrt_llm/_torch/attention/backends/vanilla.py` _+9 more__
- **2026-10-30** [`eebd9d0fcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/eebd9d0fcf) [#20871](https://github.com/NVIDIA/TensorRT-LLM/pull/20871)
  [TRTLLM-17275][fix] Bound TriAttention eviction workspace with a resident fallback (#20871)
  _Files: `docs/source/features/kv-cache-compression.md`, `examples/kv_cache_compression/triattention.md`, `tensorrt_llm/_torch/kv_cache_compression/triattention/triattention.py`, `tensorrt_llm/_torch/kv_cache_compression/triattention/triattention_cute_score_fused.py` _+6 more__
- **2026-10-30** [`3cded66b68`](https://github.com/NVIDIA/TensorRT-LLM/commit/3cded66b68) [#20359](https://github.com/NVIDIA/TensorRT-LLM/pull/20359)
  [TRTLLM-17054][refactor] Reuse PyExecutor across profiling resource transitions (#20359)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_estimation.py` _+7 more__
- **2026-10-30** [`120ea6b8c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/120ea6b8c7) [#17558](https://github.com/NVIDIA/TensorRT-LLM/pull/17558)
  [None][refactor] Split `thop.attention` into phased fmha (#17558)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/common/CMakeLists.txt`, `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h` _+53 more__
- **2026-10-30** [`c94310bdff`](https://github.com/NVIDIA/TensorRT-LLM/commit/c94310bdff) [#21286](https://github.com/NVIDIA/TensorRT-LLM/pull/21286)
  [https://nvbugs/6907190][test] Prefetch FlashInfer TRT-LLM-Gen artifacts before Ray workers start (#21286)
  _Files: `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`_
- **2026-10-29** [`491b920bdd`](https://github.com/NVIDIA/TensorRT-LLM/commit/491b920bdd) [#20922](https://github.com/NVIDIA/TensorRT-LLM/pull/20922)
  [TRTLLM-17389][feat] Serve MiniMax-M3.1-Flash with its bundled DSpark drafter (#20922)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/models/modeling_dspark.py` _+9 more__
- **2026-10-29** [`29693083e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/29693083e1) [#21129](https://github.com/NVIDIA/TensorRT-LLM/pull/21129)
  [None][feat] KVCM2 core: sparse attention arena, host-backed pools and Batch (#21129)
  _Files: `cpp/tensorrt_llm/batch_manager/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/INDEX_CONVERSION_DESIGN.md` _+66 more__
- **2026-10-29** [`72507c8f83`](https://github.com/NVIDIA/TensorRT-LLM/commit/72507c8f83) [#18111](https://github.com/NVIDIA/TensorRT-LLM/pull/18111)
  [None][feat] Add LTX-2.3 t2v and retake pipeline (#18111)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/ltx23-retake-bf16-1gpu.yaml` _+50 more__
- **2026-10-29** [`cac367c533`](https://github.com/NVIDIA/TensorRT-LLM/commit/cac367c533) [#20797](https://github.com/NVIDIA/TensorRT-LLM/pull/20797)
  [TRTLLM-17096][feat] runtime hooks: model opt-in engine fast paths (#20797)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py` _+9 more__
- **2026-10-29** [`c8b5078cde`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8b5078cde) [#20091](https://github.com/NVIDIA/TensorRT-LLM/pull/20091)
  [https://nvbugs/6890768][fix] Turn TF32 off (allow_tf32=False) around the stub's attention math with a… (#20091)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/multi_gpu/test_attn2d_attention.py`_
- **2026-10-29** [`236d9b9d1b`](https://github.com/NVIDIA/TensorRT-LLM/commit/236d9b9d1b) [#19938](https://github.com/NVIDIA/TensorRT-LLM/pull/19938)
  [None][feat] Paged block-causal K/V cache and cached attention for VisualGen (#19938)
  _Files: `cpp/tensorrt_llm/kernels/blockCausalLayout.cu`, `cpp/tensorrt_llm/kernels/blockCausalLayout.h`, `cpp/tensorrt_llm/kernels/rotateRows.cu`, `cpp/tensorrt_llm/kernels/rotateRows.h` _+30 more__
- **2026-10-29** [`e655dd850d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e655dd850d) [#21022](https://github.com/NVIDIA/TensorRT-LLM/pull/21022)
  [TRTLLM-17005][refactor] Component-local C++ Tests (Part 3a) (#21022)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/cutlass_kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kernelComponents.cmake` _+2 more__
- **2026-10-29** [`5b6da9c7aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b6da9c7aa) [#21046](https://github.com/NVIDIA/TensorRT-LLM/pull/21046)
  [None][fix] Keep target page size for standalone DSpark/DFlash draft KV pool when drafter kernels accept it (#21046)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_budget_split.py`_
- **2026-10-29** [`1ac66826a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ac66826a2) [#21073](https://github.com/NVIDIA/TensorRT-LLM/pull/21073)
  [None][perf] Attention DP: KV-balanced admission of generation-only requests (#21073)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/gen_admission_queue.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/waiting_queue.py` _+10 more__
- **2026-10-29** [`544c45a4b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/544c45a4b6) [#19807](https://github.com/NVIDIA/TensorRT-LLM/pull/19807)
  [TRTLLM-16749][feat] Add MiniMax-H3 text encoder TP support (#19807)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/attention/attention.py`, `tensorrt_llm/_torch/device_mesh.py` _+16 more__
- **2026-10-29** [`46ac6ec3cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/46ac6ec3cd) [#20683](https://github.com/NVIDIA/TensorRT-LLM/pull/20683)
  [TRTLLM-15886][infra] Remove redundant attention unit-test runs from L0 lists (#20683)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+8 more__
- **2026-10-29** [`9c199cdbfc`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c199cdbfc) [#20833](https://github.com/NVIDIA/TensorRT-LLM/pull/20833)
  [TRTLLM-17121][feat] Support phase-dependent MLA heads for Helix prefill (#20833)
  _Files: `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+10 more__
- **2026-10-29** [`f7e0b917e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7e0b917e3) [#20693](https://github.com/NVIDIA/TensorRT-LLM/pull/20693)
  [None][fix] Derive MiniMax-M3 index-K cache layers from the model config (#20693)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/common.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/unittest/_torch/attention/sparse/msa/test_minimax_m3_shared_draft_layers.py`_
- **2026-10-28** [`0b10da8224`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b10da8224) [#21066](https://github.com/NVIDIA/TensorRT-LLM/pull/21066)
  [TRTLLM-17341][refactor] Remove dead code and constant flags left by the runner migration (#21066)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/__init__.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/config.py` _+23 more__
- **2026-10-28** [`2fe91cdfc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fe91cdfc9) [#20755](https://github.com/NVIDIA/TensorRT-LLM/pull/20755)
  [None][perf] Speed up GLM-5.3-Flash serving on Blackwell (#20755)
  _Files: `docs/source/deployment-guide/deployment-guide-for-glm-5.3-flash-on-trtllm.md`, `docs/source/media/glm_5_3_flash_fp8_perf.png`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/kernels.py` _+8 more__
- **2026-10-28** [`1c661a0927`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c661a0927) [#21080](https://github.com/NVIDIA/TensorRT-LLM/pull/21080)
  [None][test] Add DeepSeek-V4.1-Flash, GLM-5.3-Flash, Qwen3.8-Flash-Next, Kimi-K3 and MiniMax-M3 perf-sanity cases (#21080)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_gpus_perf_sanity.yml` _+13 more__
- **2026-10-28** [`b41f992c58`](https://github.com/NVIDIA/TensorRT-LLM/commit/b41f992c58) [#20466](https://github.com/NVIDIA/TensorRT-LLM/pull/20466)
  [None][test] Pick DeepSeek-V4 Flash/Pro/DSpark TP/EP by GPU count (#20466)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+4 more__
- **2026-10-28** [`b613fbe387`](https://github.com/NVIDIA/TensorRT-LLM/commit/b613fbe387) [#20939](https://github.com/NVIDIA/TensorRT-LLM/pull/20939)
  [None][perf] Helix CP: MLA V up-projection before the all-to-all, O(prompt/cp) prompt partition, FIFO all-to-all sender fence, Helix test harness fix (#20939)
  _Files: `cpp/tensorrt_llm/kernels/helixAllToAll.cu`, `cpp/tensorrt_llm/nanobind/executor/request.cpp`, `tensorrt_llm/_torch/attention/attention.py`, `tensorrt_llm/_torch/attention/mla.py` _+7 more__
- **2026-10-27** [`b542326c60`](https://github.com/NVIDIA/TensorRT-LLM/commit/b542326c60) [#17658](https://github.com/NVIDIA/TensorRT-LLM/pull/17658)
  [https://nvbugs/6248648][fix] Materialize KVCM V2 page tables under CC (#17658)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.cu`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.h`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2Utils.cpp` _+11 more__
- **2026-10-27** [`935dc4a801`](https://github.com/NVIDIA/TensorRT-LLM/commit/935dc4a801) [#20940](https://github.com/NVIDIA/TensorRT-LLM/pull/20940)
  [None][perf] One-model spec decode: vocab-parallel token selection, fused DSpark Markov chain and spec tail, drafter TP fusion (#20940)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+15 more__
- **2026-10-27** [`8bd66f6a71`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bd66f6a71) [#20904](https://github.com/NVIDIA/TensorRT-LLM/pull/20904)
  [None][fix] Explain K/V pool coalescing failures; test Qwen3.8-Flash-Next QSA layouts and FP8/NVFP4 KV (#20904)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+3 more__
- **2026-10-27** [`105401ea8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/105401ea8d) [#20467](https://github.com/NVIDIA/TensorRT-LLM/pull/20467)
  [https://nvbugs/6932260][fix] Ensure one-task-per-rank for `MpiSession.submit` (#20467)
  _Files: `docs/source/llm-api/index.md`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/integration/defs/trt_test_alternative.py`, `tests/test_common/grouped_test_utils.py` _+7 more__
- **2026-10-27** [`4b027a381d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b027a381d) [#20759](https://github.com/NVIDIA/TensorRT-LLM/pull/20759)
  [TRTLLM-17086][feat] Agg Helix KV cache, part 1: prefill allocation and sizing (#20759)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+6 more__
- **2026-10-27** [`ae91047ac3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae91047ac3) [#20008](https://github.com/NVIDIA/TensorRT-LLM/pull/20008)
  [TRTLLM-16320][feat] Add FlashInfer ring-buffer replay for GDN MTP (#20008)
  _Files: `tensorrt_llm/_torch/modules/fla/cache_manager.py`, `tensorrt_llm/_torch/modules/fla/flashinfer_cached_replay.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py` _+10 more__
- **2026-10-26** [`c3c1ad3ab8`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3c1ad3ab8) [#20928](https://github.com/NVIDIA/TensorRT-LLM/pull/20928)
  [None][perf] Speed up the post-warmup KV cache NaN/Inf scan (#20928)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/test_resource_manager.py`_
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

## MoE  (28 commits)

- **2026-11-02** [`4c2238ee52`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c2238ee52) [#21225](https://github.com/NVIDIA/TensorRT-LLM/pull/21225)
  [https://nvbugs/6997728][fix] Fix DeepSeek-V4-Pro DEP4 MegaMoE CuTe DSL test: skip HF weight cache for oversized checkpoints, drop hard GSM8K floor, fix bootstrap hang (#21225)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_cute_dsl.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+3 more__
- **2026-11-02** [`df9c1af1c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/df9c1af1c5) [#21271](https://github.com/NVIDIA/TensorRT-LLM/pull/21271)
  [None][perf] GVR V2 reg_clus hint-free path: prefix sample, suffix guard and a bounded exact rescue (#21271)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tests/unittest/_torch/kernels/parallel/test_gvr_selfsampling_topk.py`_
- **2026-10-31** [`2d1a7d170e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d1a7d170e) [#20017](https://github.com/NVIDIA/TensorRT-LLM/pull/20017)
  [#19943][fix] Return an owning fragment from util_convert_type (#20017)
  _Files: `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm/kernel/moe_cute_util.cuh`_
- **2026-10-31** [`09198b7ca2`](https://github.com/NVIDIA/TensorRT-LLM/commit/09198b7ca2) [#21345](https://github.com/NVIDIA/TensorRT-LLM/pull/21345)
  [None][fix] Isolate modeling_v2 tests and scope shared test state (#21345)
  _Files: `jenkins/scripts/cbts/cbts/rules/modeling_v2.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`, `tests/integration/defs/accuracy/modeling_v2/_env.py`, `tests/integration/defs/accuracy/modeling_v2/test_deepseek_v3.py` _+34 more__
- **2026-10-30** [`a0cf142910`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0cf142910) [#21042](https://github.com/NVIDIA/TensorRT-LLM/pull/21042)
  [TRTLLM-17145][feat] Add the Muse Spark Open model (#21042)
  _Files: `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/checkpoints/hf/musespark_open_format.py`, `tensorrt_llm/_torch/models/checkpoints/hf/musespark_open_weight_mapper.py` _+22 more__
- **2026-10-30** [`7aa8f85270`](https://github.com/NVIDIA/TensorRT-LLM/commit/7aa8f85270) [#21257](https://github.com/NVIDIA/TensorRT-LLM/pull/21257)
  [None][test] Add coverage for GlmMoeDsaForCausalLM (#21257)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_deepseekv3.py`_
- **2026-10-30** [`04f92470a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/04f92470a5) [#21256](https://github.com/NVIDIA/TensorRT-LLM/pull/21256)
  [None][test] Add coverage for Glm4MoeForCausalLM (#21256)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_glm.py`_
- **2026-10-30** [`b223f2c6da`](https://github.com/NVIDIA/TensorRT-LLM/commit/b223f2c6da) [#21261](https://github.com/NVIDIA/TensorRT-LLM/pull/21261)
  [None][fix] Kimi K3 modeling_v2: fix checkpoint load and DSpark decode against current shared code (#21261)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp16ep1/modeling.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp16ep1/spec_worker.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp4ep4/modeling.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/kimi_k3_vl/kimi_k3_mxfp4__sm_100__tp16_moetp4ep4/spec_worker.py` _+2 more__
- **2026-10-30** [`ac6fb72d9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac6fb72d9f) [#18555](https://github.com/NVIDIA/TensorRT-LLM/pull/18555)
  [TRTLLM-15314][feat] Support native FP8 MoE LoRA weights (#18555)
  _Files: `cpp/tensorrt_llm/kernels/cuda_graph_grouped_gemm.cu`, `cpp/tensorrt_llm/kernels/cuda_graph_grouped_gemm.h`, `cpp/tensorrt_llm/kernels/moe/cutlass/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/moe/cutlass/include/moe_lora_grouped_gemm.h` _+17 more__
- **2026-10-30** [`a4e0757a8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4e0757a8b) [#17373](https://github.com/NVIDIA/TensorRT-LLM/pull/17373)
  [https://nvbugs/6567554][fix] Default the layer-wise benchmark prefill MoE backend to AUTO (#17373)
  _Files: `examples/layer_wise_benchmarks/README.md`, `examples/layer_wise_benchmarks/run.py`, `tests/unittest/tools/test_layer_wise_benchmarks.py`_
- **2026-10-29** [`e5bcc69442`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5bcc69442) [#21224](https://github.com/NVIDIA/TensorRT-LLM/pull/21224)
  [None][doc] Update MoE Perf Dashboard data to 1.4.0rc2 (#21224)
  _Files: `docs/source/_static/moe-perf-dashboard/data.js`_
- **2026-10-29** [`25f7221963`](https://github.com/NVIDIA/TensorRT-LLM/commit/25f7221963) [#21057](https://github.com/NVIDIA/TensorRT-LLM/pull/21057)
  [TRTLLM-14973][fix] Refuse or honour every input on the B12x MoE path (#21057)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/cutlass/lora.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl_b12x.py`, `tensorrt_llm/_torch/moe/fused_moe/impl_contract.py` _+5 more__
- **2026-10-29** [`0de8b6ff79`](https://github.com/NVIDIA/TensorRT-LLM/commit/0de8b6ff79) [#20072](https://github.com/NVIDIA/TensorRT-LLM/pull/20072)
  [TRTLLM-14620][feat] Add DSpark ragged graph and runtime integration (#20072)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/metadata.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/graphs.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/decoder/inputs.py` _+17 more__
- **2026-10-29** [`5be3334257`](https://github.com/NVIDIA/TensorRT-LLM/commit/5be3334257) [#20941](https://github.com/NVIDIA/TensorRT-LLM/pull/20941)
  [None][perf] Kimi-K3 KDA prefill grid sizing and MTP-verify kernels; DWDP cross-step expert prefetch with configurable slots (#20941)
  _Files: `docs/source/developer-guide/moe-perf-guide.md`, `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/_torch/attention/kernels/blackwell/kimi_k3_kda/kda_mtp_decode_2cta.py`, `tensorrt_llm/_torch/attention/kernels/blackwell/kimi_k3_kda/kda_mtp_decode_v2.py` _+37 more__
- **2026-10-28** [`f4bc8ee407`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4bc8ee407) [#21100](https://github.com/NVIDIA/TensorRT-LLM/pull/21100)
  [https://nvbugs/6165866][fix] Re-enable the TRTLLM-Gen MoE cases skipped for the fixed route-map over-read (#21100)
  _Files: `tests/unittest/_torch/moe/moe_test_utils.py`, `tests/unittest/_torch/moe/test_moe_backend.py`_
- **2026-10-28** [`9cf4530787`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cf4530787) [#20998](https://github.com/NVIDIA/TensorRT-LLM/pull/20998)
  [None][perf] GVR K=2048 reg_clus with block64 sampling and parallel rescue (#20998)
  _Files: `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tensorrt_llm/_torch/kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_deterministic.py`, `tests/unittest/_torch/kernels/parallel/test_gvr_selfsampling_topk.py`_
- **2026-10-28** [`f6c4125c79`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6c4125c79) [#21101](https://github.com/NVIDIA/TensorRT-LLM/pull/21101)
  [https://nvbugs/5961912][test] Re-enable CuteDSL NVFP4 MoE backend tests with large intermediate_size (#21101)
  _Files: `tests/unittest/_torch/moe/moe_test_utils.py`, `tests/unittest/_torch/moe/quantize_utils.py`_
- **2026-10-28** [`8786940e8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8786940e8b) [#20597](https://github.com/NVIDIA/TensorRT-LLM/pull/20597)
  [None][feat] Kimi K3: helix_a2a token-sliced MoE under helix + attention DP (#20597)
  _Files: `tensorrt_llm/_torch/disaggregation/native/mixers/ssm/peer.py`, `tensorrt_llm/_torch/models/modeling_kimi_k3_vl.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+15 more__
- **2026-10-27** [`0a03c3ed05`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a03c3ed05) [#19369](https://github.com/NVIDIA/TensorRT-LLM/pull/19369)
  [TRTLLM-12891][feat] Support attention DP in V2 KV cache connectors (#19369)
  _Files: `docs/source/features/kv-cache-connector.md`, `examples/llm-api/llm_kv_cache_connector_adp.py`, `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/pyexecutor/connectors/kv_cache_connector.py` _+32 more__
- **2026-10-27** [`7b12a0172e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b12a0172e) [#21090](https://github.com/NVIDIA/TensorRT-LLM/pull/21090)
  [TRTLLM-17175][test] Add a CPU test for the CuTe DSL offline loader and fix two drivers (#21090)
  _Files: `docs/source/blogs/tech_blog/blog24_MoE_as_Dense_GEMM.md`, `tensorrt_llm/_torch/kernels/utils/__init__.py`, `tensorrt_llm/_torch/visual_gen/kernels/__init__.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+3 more__
- **2026-10-27** [`0ba9f945f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ba9f945f0) [#20996](https://github.com/NVIDIA/TensorRT-LLM/pull/20996)
  [TRTLLM-15765][refactor] Remove the ModelEngine ABC and settle the executor interface (#20996)
  _Files: `docs/source/llm-api/index.md`, `docs/source/torch/arch_overview.md`, `docs/source/torch/kv_cache_manager.md`, `tensorrt_llm/_torch/distributed/ops.py` _+39 more__
- **2026-10-27** [`43a59c35df`](https://github.com/NVIDIA/TensorRT-LLM/commit/43a59c35df) [#20829](https://github.com/NVIDIA/TensorRT-LLM/pull/20829)
  [None][infra] Select modeling_v2 CI tests by the node a change lands in (#20829)
  _Files: `jenkins/scripts/cbts/cbts/command/main.py`, `jenkins/scripts/cbts/cbts/rules/modeling_v2.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/catalog/_op.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/catalog/activation/flashinfer_silu_and_mul.py` _+39 more__
- **2026-10-27** [`c554d4486d`](https://github.com/NVIDIA/TensorRT-LLM/commit/c554d4486d) [#20227](https://github.com/NVIDIA/TensorRT-LLM/pull/20227)
  [None][fix] Propagate deterministic flags to MoE finalize selection (#20227)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/test_moe_deterministic_config.py`_
- **2026-10-27** [`35cfb8cdbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/35cfb8cdbb) [#20799](https://github.com/NVIDIA/TensorRT-LLM/pull/20799)
  [https://nvbugs/6913452][fix] Fix flaky SF check in CuTe DSL gather act-fusion relu2 test (#20799)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/moe/kernels/parallel/test_cute_dsl_moe.py`_
- **2026-10-26** [`79d1d922dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/79d1d922dc) [#20929](https://github.com/NVIDIA/TensorRT-LLM/pull/20929)
  [TRTLLM-14961][refactor] Give the CuteDSL grouped-GEMM MoE implementations canonical identities (#20929)
  _Files: `.claude/skills/trtllm-moe-develop/SKILL.md`, `.claude/skills/trtllm-moe-develop/references/moe-canonical-code-examples.md`, `.pre-commit-config.yaml`, `docs/source/blogs/tech_blog/blog24_MoE_as_Dense_GEMM.md` _+40 more__
- **2026-10-26** [`ba6c1fc87d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba6c1fc87d) [#18843](https://github.com/NVIDIA/TensorRT-LLM/pull/18843)
  [TRTLLM-16303][refactor] modularize Mamba cache managers (#18843)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/modeling.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/qwen4_exp/qwen3_8_flash_next_nvfp4__sm_103__tp1/ops/ssm/fused_recurrent_gated_delta_rule_cached_replay_update.py`, `tensorrt_llm/_torch/attention/backends/sparse/csa2/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/glm_kpool/cache_manager.py` _+57 more__
- **2026-10-26** [`158252825d`](https://github.com/NVIDIA/TensorRT-LLM/commit/158252825d) [#20789](https://github.com/NVIDIA/TensorRT-LLM/pull/20789)
  [None][refactor] Register modeling_v2 routes with a routes decorator (#20789)
  _Files: `tensorrt_llm/_torch/_experimental/modeling_v2/README.md`, `tensorrt_llm/_torch/_experimental/modeling_v2/__init__.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/_router_index.py`, `tensorrt_llm/_torch/_experimental/modeling_v2/models/__init__.py` _+5 more__
- **2026-10-26** [`3467615c72`](https://github.com/NVIDIA/TensorRT-LLM/commit/3467615c72) [#20681](https://github.com/NVIDIA/TensorRT-LLM/pull/20681)
  [TRTLLM-17175][fix] Fix the post-merge leftovers of the kernel and thop test relayout (#20681)
  _Files: `cpp/include/tensorrt_llm/deep_gemm/scheduler.cuh`, `examples/layer_wise_benchmarks/parser_utils.py`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/kernels/__init__.py` _+10 more__

## Other  (19 commits)

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
- **2026-10-31** [`3d10fbf8ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d10fbf8ff) [#21292](https://github.com/NVIDIA/TensorRT-LLM/pull/21292)
  [None][chore] Hard-link build outputs into the Python package (#21292)
  _Files: `scripts/build_wheel.py`, `tests/unittest/scripts/test_build_wheel_copy_back.py`_
- **2026-10-30** [`54da997a30`](https://github.com/NVIDIA/TensorRT-LLM/commit/54da997a30) [#21200](https://github.com/NVIDIA/TensorRT-LLM/pull/21200)
  [None][refactor] Adopt per-family native libraries for K3 modeling v2 (#21200)
- **2026-10-30** [`c749f53b16`](https://github.com/NVIDIA/TensorRT-LLM/commit/c749f53b16) [#21182](https://github.com/NVIDIA/TensorRT-LLM/pull/21182)
  [None][fix] Preserve serve performance failure logs (#21182)
  _Files: `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/perf/utils.py`_
- **2026-10-29** [`25e2aeb230`](https://github.com/NVIDIA/TensorRT-LLM/commit/25e2aeb230) [#21048](https://github.com/NVIDIA/TensorRT-LLM/pull/21048)
  [https://nvbugs/6982380][fix] Open the Harmony final channel in JSON mode eval prompts (#21048)
  _Files: `tensorrt_llm/evaluate/json_mode_eval.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/evaluate/test_json_mode_eval.py`_
- **2026-10-29** [`87ce6f1aa9`](https://github.com/NVIDIA/TensorRT-LLM/commit/87ce6f1aa9) [#20137](https://github.com/NVIDIA/TensorRT-LLM/pull/20137)
  [None][chore] Clean up GPU architecture handling (#20137)
- **2026-10-29** [`93d31b4894`](https://github.com/NVIDIA/TensorRT-LLM/commit/93d31b4894) [#21071](https://github.com/NVIDIA/TensorRT-LLM/pull/21071)
  [None][fix] Exclude vulnerable filelock releases (#21071)
  _Files: `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-10-28** [`22b5f8ec3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/22b5f8ec3a) [#20762](https://github.com/NVIDIA/TensorRT-LLM/pull/20762)
  [TRTLLM-17217][fix] Use the registered input processor for MX checkpoints (#20762)
  _Files: `tensorrt_llm/inputs/registry.py`, `tests/unittest/inputs/test_create_input_processor.py`_
- **2026-10-28** [`6d20096608`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d20096608) [#20863](https://github.com/NVIDIA/TensorRT-LLM/pull/20863)
  [https://nvbugs/6958731][chore] Report the reason for retryable readiness failures (#20863)
  _Files: `tests/integration/defs/perf/agentx_client.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/scripts/test_perf_client_readiness.py`_
- **2026-10-28** [`4e57f84a30`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e57f84a30) [#21028](https://github.com/NVIDIA/TensorRT-LLM/pull/21028)
  [None][fix] Skip unclassifiable entries in QA GPU split (#21028)
  _Files: `scripts/split_qa_by_gpu.py`, `tests/unittest/scripts/test_split_qa_by_gpu.py`_
- **2026-10-28** [`7b623fb807`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b623fb807) [#20654](https://github.com/NVIDIA/TensorRT-LLM/pull/20654)
  [None][feat] Support video inputs in OpenEngine gRPC (#20654)
  _Files: `tensorrt_llm/grpc/openengine/request_mapping.py`, `tensorrt_llm/inputs/media_io.py`, `tests/unittest/grpc/openengine/test_multimodal.py`, `tests/unittest/grpc/openengine/test_multimodal_conformance.py` _+2 more__
- **2026-10-28** [`c9d2dcc26e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9d2dcc26e) [#21007](https://github.com/NVIDIA/TensorRT-LLM/pull/21007)
  [https://nvbugs/6971730][fix] Keep Inductor's async-compile pool alive (#21007)
  _Files: `tensorrt_llm/_bootstrap.py`, `tests/unittest/test_unified_cache.py`_
- **2026-10-27** [`2d3e60e27e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d3e60e27e) [#21043](https://github.com/NVIDIA/TensorRT-LLM/pull/21043)
  [None][fix] allocate global transfer IDs for OpenEngine prefill (#21043)
  _Files: `tensorrt_llm/grpc/openengine/disagg.py`, `tests/unittest/grpc/openengine/test_servicer.py`_
- **2026-10-26** [`21c22c6440`](https://github.com/NVIDIA/TensorRT-LLM/commit/21c22c6440) [#20832](https://github.com/NVIDIA/TensorRT-LLM/pull/20832)
  [None][build] Improve cpp/tests/CMakeLists.txt (#20832)
  _Files: `cpp/tests/CMakeLists.txt`_
- **2026-10-26** [`b7bfae8eb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7bfae8eb0) [#20748](https://github.com/NVIDIA/TensorRT-LLM/pull/20748)
  [https://nvbugs/6937268][fix] Ignore recoverable pip download retry warnings (#20748)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/test_common/error_utils.py`, `tests/unittest/others/test_http_utils_fail_fast.py`_
- **2026-10-26** [`687359e228`](https://github.com/NVIDIA/TensorRT-LLM/commit/687359e228) [#20892](https://github.com/NVIDIA/TensorRT-LLM/pull/20892)
  [None][test] Remove unused model-path fixtures from integration conft… (#20892)
  _Files: `tests/integration/defs/conftest.py`, `tests/integration/defs/triton_server/conftest.py`_

## Torch Path (_torch)  (17 commits)

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
- **2026-10-30** [`78145f88ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/78145f88ea) [#20406](https://github.com/NVIDIA/TensorRT-LLM/pull/20406)
  [None][perf] Refresh GLM single-node core coverage (#20406)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-10-30** [`63c0ef23be`](https://github.com/NVIDIA/TensorRT-LLM/commit/63c0ef23be) [#21105](https://github.com/NVIDIA/TensorRT-LLM/pull/21105)
  [TRTLLM-17350][perf] Avoid whole-pool SSM copies in custom Mamba2 MTP updates (#21105)
  _Files: `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCache.h`, `cpp/tensorrt_llm/kernels/mamba2MTPSSMCache/mamba2MTPSSMCacheKernel.cuh`, `cpp/tensorrt_llm/thop/mamba2MTPSSMCacheOp.cpp`, `tensorrt_llm/_torch/modules/mamba/selective_state_update.py` _+1 more__
- **2026-10-29** [`be95f2a4c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/be95f2a4c8) [#21094](https://github.com/NVIDIA/TensorRT-LLM/pull/21094)
  [https://nvbugs/6970940][fix] Re-read rank-striped read-ahead extents after the page cache drops them (#21094)
  _Files: `docs/source/features/checkpoint-loading.md`, `tensorrt_llm/_torch/models/checkpoints/hf/rank_striped_read_ahead.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tests/unittest/_torch/models/checkpoints/hf/test_rank_striped_read_ahead.py`_
- **2026-10-29** [`e0892ee756`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0892ee756) [#20330](https://github.com/NVIDIA/TensorRT-LLM/pull/20330)
  [https://nvbugs/6758946][fix] Compare teacher-forced logits in the Nemotron VL image batch-equivalence test (#20330)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_nemotron_h_multimodal.py`_
- **2026-10-29** [`c492171477`](https://github.com/NVIDIA/TensorRT-LLM/commit/c492171477) [#20695](https://github.com/NVIDIA/TensorRT-LLM/pull/20695)
  [None][fix] MiniMax-M3 VL: forward video metadata so videos get timestamps (#20695)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3_vl.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/models/test_minimax_m3_vl.py`_
- **2026-10-28** [`99466ea9ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/99466ea9ad) [#21132](https://github.com/NVIDIA/TensorRT-LLM/pull/21132)
  [None][perf] Avoid output concatenation in eager GDN (#21132)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_gdn_kernel_optimizations.py`_
- **2026-10-28** [`9c5e8e5de3`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c5e8e5de3) [#21068](https://github.com/NVIDIA/TensorRT-LLM/pull/21068)
  [TRTLLMINF-550][infra] Pull CUDA 13 PyTorch wheels from the cu132 mirror (#21068)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-10-28** [`a8ce1074a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8ce1074a6) [#20176](https://github.com/NVIDIA/TensorRT-LLM/pull/20176)
  [TRTLLM-16963][feat] Enable MiniMax-H3 DiT tensor parallelism (#20176)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/minimax-h3-bf16-2gpu.yaml` _+7 more__
- **2026-10-27** [`8c08d34d54`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c08d34d54) [#20814](https://github.com/NVIDIA/TensorRT-LLM/pull/20814)
  [https://nvbugs/6964707][fix] Let comm op-matrix ranks import the installed tensorrt_llm (#20814)
  _Files: `tests/unittest/_torch/modeling_v2/comm/_rank_job.py`_
- **2026-10-27** [`6ba2bec9e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ba2bec9e9) [#20827](https://github.com/NVIDIA/TensorRT-LLM/pull/20827)
  [https://nvbugs/6949270][fix] Size the Wan2.2-I2V serve test start budget to a cold checkpoint read (#20827)
  _Files: `tests/unittest/_torch/visual_gen/test_trtllm_serve_e2e.py`_
- **2026-10-27** [`af32051e19`](https://github.com/NVIDIA/TensorRT-LLM/commit/af32051e19) [#19645](https://github.com/NVIDIA/TensorRT-LLM/pull/19645)
  [TRTLLM-16599][perf] Fuse MiniMax-H3 BF16 QK-norm and rotary embeddings (#19645)
  _Files: `tensorrt_llm/_torch/visual_gen/models/minimax_h3/fused_rope.py`, `tensorrt_llm/_torch/visual_gen/models/minimax_h3/transformer_minimax_h3.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+2 more__
- **2026-10-26** [`8cbe002a43`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cbe002a43) [#20352](https://github.com/NVIDIA/TensorRT-LLM/pull/20352)
  [https://nvbugs/6920455][fix] Correct the PyTorch scheduler page's PP and inflight_request_ids claims (#20352)
  _Files: `docs/source/torch/scheduler.md`_
- **2026-10-26** [`8ea175e248`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ea175e248) [#20228](https://github.com/NVIDIA/TensorRT-LLM/pull/20228)
  [None][fix] Honor deterministic mode in fused mHC dispatch (#20228)
  _Files: `tensorrt_llm/_torch/modules/mhc/mhc_cuda.py`, `tests/unittest/_torch/modules/test_mhc.py`_

## Disaggregation / KV  (15 commits)

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
- **2026-10-31** [`5ec25c55db`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ec25c55db) [#20491](https://github.com/NVIDIA/TensorRT-LLM/pull/20491)
  [TRTLLM-17083][feat] Cancel paired GEN on CTX failure or cancellation (#20491)
  _Files: `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_disagg_service.py`, `tensorrt_llm/serve/router.py`, `tests/unittest/disaggregated/test_disagg_openai_client.py` _+3 more__
- **2026-10-30** [`1a1ba9a0a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a1ba9a0a3) [#20702](https://github.com/NVIDIA/TensorRT-LLM/pull/20702)
  [None][fix] Progress idle disaggregated worker cancellation (#20702)
  _Files: `tensorrt_llm/_torch/disaggregation/kv_cache_transceiver.py`, `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+7 more__
- **2026-10-30** [`a943b18e35`](https://github.com/NVIDIA/TensorRT-LLM/commit/a943b18e35) [#21254](https://github.com/NVIDIA/TensorRT-LLM/pull/21254)
  [https://nvbugs/6944355][fix] Enable the KV bounce buffer for the Qwen3-235B TP1-to-TEP4 con64 disagg perf case (#21254)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb200_qwen3-235b-fp4_8k1k_con64_ctx1_tp1_gen1_tep4_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_qwen3-235b-fp4_8k1k_con64_ctx1_tp1_gen1_tep4_eplb0_mtp0_ccb-NIXL.yaml`_
- **2026-10-30** [`51581f90b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/51581f90b1) [#21219](https://github.com/NVIDIA/TensorRT-LLM/pull/21219)
  [https://nvbugs/7004364][fix] Extend GPU lifecycle startup budget (#21219)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/disaggregated/lifecycle_acceptance.md`, `tests/unittest/disaggregated/test_transfer_lifecycle_gpu.py`_
- **2026-10-27** [`a10e80f748`](https://github.com/NVIDIA/TensorRT-LLM/commit/a10e80f748) [#20474](https://github.com/NVIDIA/TensorRT-LLM/pull/20474)
  [None][docs] Document disaggregated beam-search requirements (#20474)
  _Files: `docs/source/features/sampling.md`_
- **2026-10-27** [`b351c407bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/b351c407bb) [#20884](https://github.com/NVIDIA/TensorRT-LLM/pull/20884)
  [None][feat] Add the blob backend with batch registration, bounded queueing and a CPU end-to-end example (#20884)
  _Files: `tensorrt_llm/_torch/disaggregation/blob/README.md`, `tensorrt_llm/_torch/disaggregation/blob/__init__.py`, `tensorrt_llm/_torch/disaggregation/blob/backend.py`, `tensorrt_llm/_torch/disaggregation/blob/keys.py` _+12 more__
- **2026-10-27** [`a8283516d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8283516d8) [#20979](https://github.com/NVIDIA/TensorRT-LLM/pull/20979)
  [None][fix] Cherry-pick #20393: save logs for stress tests (#20979)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_
- **2026-10-26** [`64c1ce103c`](https://github.com/NVIDIA/TensorRT-LLM/commit/64c1ce103c) [#19883](https://github.com/NVIDIA/TensorRT-LLM/pull/19883)
  [https://nvbugs/6781271][fix] Responses API: agent-client fixes and disaggregated serving (#19883)
  _Files: `docs/source/features/disagg-serving.md`, `docs/source/release-notes.md`, `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_disagg_server.py` _+23 more__
- **2026-10-26** [`6448b1b17f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6448b1b17f) [#19760](https://github.com/NVIDIA/TensorRT-LLM/pull/19760)
  [None][perf] use native protobuf and streamline gRPC result delivery (#19760)
  _Files: `docker/Dockerfile.multi`, `docs/source/installation/containers.md`, `jenkins/current_image_tags.properties`, `tensorrt_llm/grpc/_protobuf.py` _+10 more__
- **2026-10-26** [`61dc60586b`](https://github.com/NVIDIA/TensorRT-LLM/commit/61dc60586b) [#20447](https://github.com/NVIDIA/TensorRT-LLM/pull/20447)
  [https://nvbugs/6920457][fix] Document True as the use_kv_cache_manager_v2 default in the KV cache guide… (#20447)
  _Files: `docs/source/features/kvcache.md`_
- **2026-10-26** [`dd75334918`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd75334918) [#20736](https://github.com/NVIDIA/TensorRT-LLM/pull/20736)
  [None][feat] TTFT-percentile GEN admission for disaggregated serving, and a fix for a context-chunk replay after a skipped forward (#20736)
  _Files: `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/request_utils.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/gen_admission_queue.py` _+10 more__

## Quantization  (14 commits)

- **2026-11-02** [`cf96e9ec51`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf96e9ec51)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-11-02** [`3f59791863`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f59791863) [#21002](https://github.com/NVIDIA/TensorRT-LLM/pull/21002)
  [https://nvbugs/6770977][test] Fix qwen3_32b_fp8 disagg output check and startup budget (#21002)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-11-01** [`0fd58c90ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fd58c90ed) [#19864](https://github.com/NVIDIA/TensorRT-LLM/pull/19864)
  [#19861][fix] Keep encoder-decoder cross KV caches in model dtype (#19864)
  _Files: `docs/source/features/quantization.md`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_t5.py`, `tests/integration/test_lists/test-db/l0_l40s.yml` _+2 more__
- **2026-11-01** [`0054d486f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0054d486f1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+4 more__
- **2026-10-31** [`f405e10b73`](https://github.com/NVIDIA/TensorRT-LLM/commit/f405e10b73) [#20306](https://github.com/NVIDIA/TensorRT-LLM/pull/20306)
  [None][feat] MiniMax-M3 NVFP4 low-latency decode megakernel for modeling_v2 for Blackwell (#20306)
- **2026-10-31** [`bb00a3bbf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb00a3bbf2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-10-30** [`1628e2c244`](https://github.com/NVIDIA/TensorRT-LLM/commit/1628e2c244)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-10-29** [`1e005f0e7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e005f0e7e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-10-29** [`592bd6fd8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/592bd6fd8d) [#20662](https://github.com/NVIDIA/TensorRT-LLM/pull/20662)
  [TRTLLM-16980][feat] modeling_v2: GLM-5.2-NVFP4 sm_103 tep4 target (#20662)
- **2026-10-28** [`1f9b707232`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f9b707232) [#20694](https://github.com/NVIDIA/TensorRT-LLM/pull/20694)
  [None][fix] Load compressed-tensors NVFP4 weights in MiniMax-M3 (#20694)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_laguna.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/unittest/_torch/models/checkpoints/hf/test_minimaxm3_weight_mapper.py` _+1 more__
- **2026-10-28** [`7723a3b34b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7723a3b34b) [#20896](https://github.com/NVIDIA/TensorRT-LLM/pull/20896)
  [None][feat] modeling_v2: build target C++/CUDA as per-family libraries (#20896)
  _Files: `.cmake-format.json`, `.github/CODEOWNERS`, `cpp/CMakeLists.txt`, `cpp/cmake/modules/modeling_v2.cmake` _+33 more__
- **2026-10-27** [`0712980587`](https://github.com/NVIDIA/TensorRT-LLM/commit/0712980587) [#20942](https://github.com/NVIDIA/TensorRT-LLM/pull/20942)
  [None][perf] FP8 block-scale low-M GEMM for decode projections (SM100/103, SM107 tactic tables) (#20942)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/kernels/blackwell/fp8_block_scale_low_m_gemm.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/linear.py` _+2 more__
- **2026-10-27** [`c1d51b22b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1d51b22b2) [#20845](https://github.com/NVIDIA/TensorRT-LLM/pull/20845)
  [https://nvbugs/6820152][fix] Fix Wan I2V example test requiring unavailable NVFP4 checkpoint (#20845)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_wan.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-26** [`f188d62527`](https://github.com/NVIDIA/TensorRT-LLM/commit/f188d62527)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+5 more__

## Models  (11 commits)

- **2026-11-02** [`a962b94f2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a962b94f2b) [#21339](https://github.com/NVIDIA/TensorRT-LLM/pull/21339)
  [None][chore] Reject per-layer KV-head configs in the generic HF weight mapper (#21339)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/gemma4_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3vl_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_mapper.py` _+1 more__
- **2026-11-01** [`309426dd94`](https://github.com/NVIDIA/TensorRT-LLM/commit/309426dd94) [#21037](https://github.com/NVIDIA/TensorRT-LLM/pull/21037)
  [None][perf] Bound OpenEngine image preparation and reuse prefill state (#21037)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/grpc/openengine/README.md`, `tensorrt_llm/grpc/openengine/disagg.py`, `tensorrt_llm/grpc/openengine/preparation.py` _+10 more__
- **2026-11-01** [`5d86481f60`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d86481f60) [#20815](https://github.com/NVIDIA/TensorRT-LLM/pull/20815)
  [None][perf] Qwen3.5 GB300: upstream the AgentX side-branch optimizations (#20815)
- **2026-10-30** [`cecf5f6959`](https://github.com/NVIDIA/TensorRT-LLM/commit/cecf5f6959) [#21255](https://github.com/NVIDIA/TensorRT-LLM/pull/21255)
  [None][test] Add coverage for Gemma4UnifiedForConditionalGeneration (#21255)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_gemma4_unified.py`_
- **2026-10-30** [`08cd9cf6b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/08cd9cf6b6) [#20655](https://github.com/NVIDIA/TensorRT-LLM/pull/20655)
  [None][feat] Support audio inputs in OpenEngine gRPC (#20655)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py`, `tensorrt_llm/_torch/models/modeling_whisper.py`, `tensorrt_llm/grpc/openengine/README.md` _+13 more__
- **2026-10-29** [`0c15889d51`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c15889d51) [#21135](https://github.com/NVIDIA/TensorRT-LLM/pull/21135)
  [https://nvbugs/6907190][chore] Unwaive test_llm_update_weights_qwen35_35b_bf16 (#21135)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-28** [`b72f1c1e6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b72f1c1e6f) [#20893](https://github.com/NVIDIA/TensorRT-LLM/pull/20893)
  [None][feat] Consolidate Kimi K3 native modeling work into main (#19990, #19991) (#20893)
- **2026-10-28** [`186d7f4a71`](https://github.com/NVIDIA/TensorRT-LLM/commit/186d7f4a71) [#21015](https://github.com/NVIDIA/TensorRT-LLM/pull/21015)
  [None][test] Add coverage for Qwen4ExpForConditionalGeneration (#21015)
  _Files: `tests/unittest/_torch/modeling/test_qwen4_exp_support.py`_
- **2026-10-28** [`e2b1544160`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2b1544160) [#21011](https://github.com/NVIDIA/TensorRT-LLM/pull/21011)
  [None][fix] Kimi K3 attn_res persistent fused kernel: 64-bit candidate offsets (#21011)
  _Files: `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.h`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.cu`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.h`, `cpp/tensorrt_llm/thop/attnResOp.cpp` _+1 more__
- **2026-10-28** [`b614d3b1f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/b614d3b1f1) [#20624](https://github.com/NVIDIA/TensorRT-LLM/pull/20624)
  [#19913][chore] Upgrade XGrammar from 0.1.32 to 0.2.8 (#20624)
  _Files: `3rdparty/fetch_content.json`, `3rdparty/patches/xgrammar_cxx20.patch`, `ATTRIBUTIONS-Python.md`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt` _+9 more__
- **2026-10-27** [`dfec072eba`](https://github.com/NVIDIA/TensorRT-LLM/commit/dfec072eba) [#20933](https://github.com/NVIDIA/TensorRT-LLM/pull/20933)
  [https://nvbugs/6962175][fix] Pin GPT-OSS accuracy prompt dates and remove waivers (#20933)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_

## Docs / Examples  (9 commits)

- **2026-10-30** [`7969af8dec`](https://github.com/NVIDIA/TensorRT-LLM/commit/7969af8dec) [#21353](https://github.com/NVIDIA/TensorRT-LLM/pull/21353)
  [None][doc] Point to model side branches from the supported models page (#21353)
  _Files: `docs/source/models/supported-models.md`_
- **2026-10-29** [`6d5d9ff161`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d5d9ff161) [#21197](https://github.com/NVIDIA/TensorRT-LLM/pull/21197)
  [None][fix] Correct TPOT metric direction in perf sanity (#21197)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/others/test_perf_sanity_tpot.py`_
- **2026-10-29** [`ba2dddf54b`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba2dddf54b) [#20744](https://github.com/NVIDIA/TensorRT-LLM/pull/20744)
  [TRTLLM-17448][feat] Support upstream vendor promotion and discoverable bot feedback (#20744)
  _Files: `3rdparty/vendor-sources.md`, `scripts/vendor/README.md`, `scripts/vendor/bot.py`, `scripts/vendor/diagnostics.py` _+4 more__
- **2026-10-29** [`cffb62fde7`](https://github.com/NVIDIA/TensorRT-LLM/commit/cffb62fde7) [#20747](https://github.com/NVIDIA/TensorRT-LLM/pull/20747)
  [https://nvbugs/6926622][doc] Consolidate K-EXAONE supported-model entries (#20747)
  _Files: `docs/source/models/supported-models.md`_
- **2026-10-28** [`18c972e22c`](https://github.com/NVIDIA/TensorRT-LLM/commit/18c972e22c) [#21123](https://github.com/NVIDIA/TensorRT-LLM/pull/21123)
  [None][test] Add a warmup pass before perf-sanity measured clients (#21123)
  _Files: `tests/integration/defs/perf/README.md`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/perf/test_perf_sanity.py` _+3 more__
- **2026-10-28** [`8c9cf15f4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c9cf15f4f)
  [None][chore] Bump version to 1.4.0rc3
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/schemas/trtllm-serve-config.schema.json`, `tensorrt_llm/schemas/trtllm-serve-disagg-config.schema.json` _+2 more__
- **2026-10-28** [`812f9ca883`](https://github.com/NVIDIA/TensorRT-LLM/commit/812f9ca883) [#21171](https://github.com/NVIDIA/TensorRT-LLM/pull/21171)
  [https://nvbugs/7004398][doc] Fix VisualGen example commands and feature matrix (#21171)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/models/cosmos3/README.md` _+1 more__
- **2026-10-27** [`b6751ca780`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6751ca780) [#21097](https://github.com/NVIDIA/TensorRT-LLM/pull/21097)
  [https://nvbugs/6999645][fix] Fix VisualGen MGMN example script (#21097)
  _Files: `examples/visual_gen/serve/benchmark_visual_gen_mgmn_distributed.sh`_
- **2026-10-26** [`3205aeaedb`](https://github.com/NVIDIA/TensorRT-LLM/commit/3205aeaedb) [#20437](https://github.com/NVIDIA/TensorRT-LLM/pull/20437)
  [None][feat] Expose standard gRPC health in OpenEngine (#20437)
  _Files: `requirements.txt`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/grpc/openengine/README.md`, `tensorrt_llm/grpc/openengine/_health.py` _+13 more__

## LoRA  (7 commits)

- **2026-11-02** [`2fc420cd6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fc420cd6c) [#21106](https://github.com/NVIDIA/TensorRT-LLM/pull/21106)
  [None][fix] Anthropic Messages: name the json_schema built from output_config.format (#21106)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_
- **2026-10-28** [`461580bcd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/461580bcd5) [#21030](https://github.com/NVIDIA/TensorRT-LLM/pull/21030)
  [None][feat] Anthropic Messages: keepalive pings while a stream is silent (#21030)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tensorrt_llm/serve/anthropic_protocol.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_
- **2026-10-27** [`55649d139f`](https://github.com/NVIDIA/TensorRT-LLM/commit/55649d139f) [#20866](https://github.com/NVIDIA/TensorRT-LLM/pull/20866)
  [None][fix] Anthropic Messages: sign the thinking blocks the server generates (#20866)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_
- **2026-10-27** [`f0a9de47a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0a9de47a6) [#20881](https://github.com/NVIDIA/TensorRT-LLM/pull/20881)
  [None][fix] Anthropic Messages: accept the thinking display setting (#20881)
  _Files: `tensorrt_llm/serve/anthropic_protocol.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_routes.py`_
- **2026-10-26** [`da002dbcb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/da002dbcb3) [#20874](https://github.com/NVIDIA/TensorRT-LLM/pull/20874)
  [None][fix] Anthropic Messages: no whitespace-only text blocks (#20874)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`_
- **2026-10-26** [`0a97382613`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a97382613) [#20867](https://github.com/NVIDIA/TensorRT-LLM/pull/20867)
  [None][fix] Anthropic Messages: read the chat stream to its end so its metrics are recorded (#20867)
  _Files: `tensorrt_llm/serve/anthropic_adapter.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/llmapi/apps/test_anthropic_adapter.py`, `tests/unittest/llmapi/apps/test_anthropic_routes.py`_
- **2026-10-26** [`a6fde392d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6fde392d0) [#20775](https://github.com/NVIDIA/TensorRT-LLM/pull/20775)
  [TRTLLM-16711][fix] Remove the legacy renderer paths (#20775)
  _Files: `tensorrt_llm/serve/chat_tokenization.py`, `tensorrt_llm/serve/harmony_adapter.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/render/__init__.py` _+9 more__

## ROCm / AMD  (6 commits)

- **2026-11-02** [`a9be7004c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9be7004c7) [#20049](https://github.com/NVIDIA/TensorRT-LLM/pull/20049)
  [None][chore] Remove the Python KV bounce buffer; kv_cache_bounce_size_mb selects the C++ agent bounce (#20049)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/bounce/BounceConfig.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/bounce/BounceTransport.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/transferAgent.cpp` _+87 more__
- **2026-10-31** [`66190c8fd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/66190c8fd5) [#21175](https://github.com/NVIDIA/TensorRT-LLM/pull/21175)
  [None][chore] Update Modeling V2 code and test ownership (#21175)
  _Files: `.github/CODEOWNERS`_
- **2026-10-30** [`c50ea882ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/c50ea882ef) [#20888](https://github.com/NVIDIA/TensorRT-LLM/pull/20888)
  [None][feat] Kimi K3: support NVFP4 KV cache (FP4 MLA) with the hybrid KV cache manager (#20888)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/attention/backends/fmha/fp4_mla.py` _+43 more__
- **2026-10-29** [`e4d5e2eaa7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4d5e2eaa7) [#21158](https://github.com/NVIDIA/TensorRT-LLM/pull/21158)
  [TRTLLM-17348][refactor] Reorganize engine and decoder tests around component ownership (#21158)
  _Files: `.claude/skills/perf-host-optimization/SKILL.md`, `.claude/skills/perf-host-optimization/references/hot-path-files.md`, `.pre-commit-config.yaml`, `legacy-files.txt` _+34 more__
- **2026-10-27** [`94348c4de6`](https://github.com/NVIDIA/TensorRT-LLM/commit/94348c4de6) [#19575](https://github.com/NVIDIA/TensorRT-LLM/pull/19575)
  [None][fix] Python transceiver: run gen-side KV transfer consensus across helix CP ranks under attention-DP (#19575)
  _Files: `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+18 more__
- **2026-10-26** [`758c7b5ba4`](https://github.com/NVIDIA/TensorRT-LLM/commit/758c7b5ba4) [#20947](https://github.com/NVIDIA/TensorRT-LLM/pull/20947)
  [None][fix] EagerMoeWorkspace test and LoRA tests (#20947)
  _Files: `cpp/tests/unit_tests/thop/eagerMoeWorkspaceTest.cpp`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_resource_manager.py`, `tests/unittest/_torch/peft/test_lora_ownership.py`_

## Speculative Decoding  (3 commits)

- **2026-11-02** [`1926cfdccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1926cfdccf) [#21331](https://github.com/NVIDIA/TensorRT-LLM/pull/21331)
  [None][test] Add DGX Spark agentic and real-text speculative decoding perf cases (#21331)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_spark_perf.yml`_
- **2026-10-30** [`e3e0b12d2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3e0b12d2b) [#21041](https://github.com/NVIDIA/TensorRT-LLM/pull/21041)
  [TRTLLM-16618][chore] BREAKING: Remove obsolete TensorRT-backend compatibility surfaces (#21041)
  _Files: `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/include/tensorrt_llm/executor/serialization.h`, `cpp/include/tensorrt_llm/executor/types.h`, `cpp/tensorrt_llm/executor/CMakeLists.txt` _+16 more__
- **2026-10-28** [`deebe2be3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/deebe2be3d) [#20938](https://github.com/NVIDIA/TensorRT-LLM/pull/20938)
  [None][perf] Serving runtime: disagg/KV-transfer/ADP fixes, KV cache manager V2 prefix wait, ConversationRouter prefix placement, KV-balanced ADP admission (#20938)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/utils/copyUtils.cu`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/modules/kimi_kda/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py` _+26 more__

## Perf  (1 commits)

- **2026-10-26** [`cfae4519c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfae4519c3) [#20790](https://github.com/NVIDIA/TensorRT-LLM/pull/20790)
  [https://nvbugs/6900756][perf] KVCMv2: fill the initial host tier in parallel, populate in 4 MiB calls (#20790)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/utils/hostMem.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/utils/hostMem.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/utils/hostMemBacking.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/utils/hostMemBacking.h` _+2 more__

---
_Generated 2026-11-02 18:20 UTC_