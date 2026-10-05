# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-09-28 → 2026-10-05  |  **Total commits:** 114

## ✨ New Features This Week

- **2026-10-05** [#19701](https://github.com/NVIDIA/TensorRT-LLM/pull/19701) — [TRTLLM-16672][feat] MiniMax H3 Turbo LoRA Tensor Name Mapping (#19701)
- **2026-10-03** [#17476](https://github.com/NVIDIA/TensorRT-LLM/pull/17476) — [None][feat] Load static FP8 Cosmos3 Nano/Super checkpoints without re-quantizing them (#17476)
- **2026-10-03** [#19717](https://github.com/NVIDIA/TensorRT-LLM/pull/19717) — [None][feat] Add iter_perf_stats_interval to sample iteration stats (#19717)
- **2026-10-03** [#19311](https://github.com/NVIDIA/TensorRT-LLM/pull/19311) — [None][feat] Report per-request speculative-decoding acceptance on the response (#19311)
- **2026-10-02** [#18060](https://github.com/NVIDIA/TensorRT-LLM/pull/18060) — [TRTLLM-15447][feat] Add model startup stage timing metrics (#18060)
- **2026-10-02** [#19439](https://github.com/NVIDIA/TensorRT-LLM/pull/19439) — [TRTLLM-16707][feat] Support model_kwargs with encoder CUDA graphs (#19439)
- **2026-10-02** [#19784](https://github.com/NVIDIA/TensorRT-LLM/pull/19784) — [https://nvbugs/6783973][doc] Stop listing supported SA speculation as a Kimi K3 limitation (#19784)
- **2026-10-02** [#19597](https://github.com/NVIDIA/TensorRT-LLM/pull/19597) — [None][feat] Load quantized Nemotron-H MTP replacements (#19597)
- **2026-10-02** [#19702](https://github.com/NVIDIA/TensorRT-LLM/pull/19702) — [TRTLLM-15824][feat] Enable EVS handoff for Nemotron-H in EPD (#19702)
- **2026-10-02** [#19670](https://github.com/NVIDIA/TensorRT-LLM/pull/19670) — [None][feat] Add configurable SWA endpoint retention priority (#19670)
- _…and 15 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-10-02** [`f7518a6427`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7518a6427) [#19674](https://github.com/NVIDIA/TensorRT-LLM/pull/19674) — [None][fix] Fail stop executor worlds on unproven KV retirement (#19674)
- **2026-09-30** [`84de36ed03`](https://github.com/NVIDIA/TensorRT-LLM/commit/84de36ed03) [#19545](https://github.com/NVIDIA/TensorRT-LLM/pull/19545) — [None][fix] Gate disaggregated KV block reuse admission on verified write coverage (#19545)
- **2026-09-29** [`00bdcb6ed7`](https://github.com/NVIDIA/TensorRT-LLM/commit/00bdcb6ed7) [#19378](https://github.com/NVIDIA/TensorRT-LLM/pull/19378) — [None][fix] Retire KV transfer ownership after late backend completion (#19378)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-10-05 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-10-05 |
| [#19820](https://github.com/NVIDIA/TensorRT-LLM/issues/19820) | [New Model]: Apertus (swiss-ai/Apertus-8B-Instruct-2509, swiss-ai/Aper | new model | 2026-10-02 |
| [#19666](https://github.com/NVIDIA/TensorRT-LLM/issues/19666) | [Feature]: EFA should work out of the box on NGC TRTLLM release image  | feature request, OOTB | 2026-10-01 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-10-01 |
| [#19726](https://github.com/NVIDIA/TensorRT-LLM/issues/19726) | [Feature][RFC]: Compact active beam rows during VBWS decode in the PyT | Pytorch, Model optimization | 2026-09-30 |
| [#19634](https://github.com/NVIDIA/TensorRT-LLM/issues/19634) | [Bug]: multi-node MPI-orchestrator serve hangs at IPC init (queues bin | Inference runtime, Disaggregated serving | 2026-09-29 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-09-28 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-09-21 |
| [#19232](https://github.com/NVIDIA/TensorRT-LLM/issues/19232) | [RFC]: Disaggregated request preprocessing | triaged, Investigating, LLM API, Disaggregated serving, RFC, Frontend | 2026-09-16 |
| [#19242](https://github.com/NVIDIA/TensorRT-LLM/issues/19242) | [Bug]: KVCacheBlock and its radix tree LookupNode own each other with  | KV-Cache Management | 2026-09-16 |
| [#19240](https://github.com/NVIDIA/TensorRT-LLM/issues/19240) | [Bug]: mixtureOfExpertsTest crashes with SEGV when a parameter set has | Customized kernels | 2026-09-16 |
| [#19059](https://github.com/NVIDIA/TensorRT-LLM/issues/19059) | [Bug]: C++17 build cannot compile torch 2.12 headers with nvcc, but C+ | Pytorch | 2026-09-15 |
| [#19172](https://github.com/NVIDIA/TensorRT-LLM/issues/19172) | [Bug]: Async prompt-embedding H2D outlives its pooled-pinned source; t | bug, Triton backend, Inference runtime | 2026-09-14 |
| [#19067](https://github.com/NVIDIA/TensorRT-LLM/issues/19067) | [Bug]: -a 107-real is silently folded to 100, no SM107 code is generat | Infra | 2026-09-11 |
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-09-09 |
| [#18847](https://github.com/NVIDIA/TensorRT-LLM/issues/18847) | [Bug] Worker CPU affinity is applied process-wide in shared-process de | Inference runtime | 2026-09-07 |
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-09-02 |
| [#18407](https://github.com/NVIDIA/TensorRT-LLM/issues/18407) | [Bug]: KVCacheV2Scheduler retains active PEFT adapters after KV suspen | KV-Cache Management, Lora/P-tuning, Pytorch | 2026-08-30 |
| [#18156](https://github.com/NVIDIA/TensorRT-LLM/issues/18156) | KV-cache-aware router never matches LoRA or salted requests: lora_id i | Disaggregated serving | 2026-08-24 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 33 |
| Executor / Runtime | 21 |
| Attention | 14 |
| Quantization | 13 |
| Other | 6 |
| MoE | 6 |
| Docs / Examples | 4 |
| Torch Path (_torch) | 4 |
| LoRA | 3 |
| ROCm / AMD | 3 |
| Disaggregation / KV | 3 |
| Speculative Decoding | 2 |
| Models | 2 |

## CI / Infra  (33 commits)

- **2026-10-05** [`d1db352d64`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1db352d64)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-10-03** [`704fd8fadf`](https://github.com/NVIDIA/TensorRT-LLM/commit/704fd8fadf)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+6 more__
- **2026-10-02** [`70af7c74af`](https://github.com/NVIDIA/TensorRT-LLM/commit/70af7c74af) [#19602](https://github.com/NVIDIA/TensorRT-LLM/pull/19602)
  [TRTLLMINF-336][infra] Pin one BOLT profile bundle per pipeline (#19602)
  _Files: `jenkins/BoltProfileGen.groovy`, `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy` _+2 more__
- **2026-10-02** [`790fdc5bd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/790fdc5bd9) [#19778](https://github.com/NVIDIA/TensorRT-LLM/pull/19778)
  [None][ci] waive pre-existing test failures on main (#19778)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-01** [`2693657388`](https://github.com/NVIDIA/TensorRT-LLM/commit/2693657388) [#19781](https://github.com/NVIDIA/TensorRT-LLM/pull/19781)
  [None][chore] Waive flaky test on main (#19781)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-01** [`9b9607d830`](https://github.com/NVIDIA/TensorRT-LLM/commit/9b9607d830) [#19752](https://github.com/NVIDIA/TensorRT-LLM/pull/19752)
  [None][infra] Reduce semantic review PR timeline noise (#19752)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/semantic-review.md`, `.github/workflows/semantic-review.yml`_
- **2026-10-01** [`ee510fc85d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee510fc85d) [#19700](https://github.com/NVIDIA/TensorRT-LLM/pull/19700)
  [https://nvbugs/6843918][fix] Fix gen_only perf-sanity metric bucket, gonc gen-only env, and unwaive fixed cases (#19700)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/waives.txt`_
- **2026-10-01** [`d6ebc4dc07`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6ebc4dc07) [#19763](https://github.com/NVIDIA/TensorRT-LLM/pull/19763)
  [None][test] Waive 1 failed cases for main in QA CI (#19763)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-01** [`f7643d6e3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7643d6e3e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`, `security_scanning/triton_backend/poetry.lock` _+1 more__
- **2026-09-30** [`fc2f8543e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc2f8543e0) [#19742](https://github.com/NVIDIA/TensorRT-LLM/pull/19742)
  [None][infra] Waive 1 failed cases for main in pre-merge 62544 (#19742)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`f937cdec45`](https://github.com/NVIDIA/TensorRT-LLM/commit/f937cdec45) [#19429](https://github.com/NVIDIA/TensorRT-LLM/pull/19429)
  [TRTLLMINF-336][infra] Apply BOLT to the released SBSA wheel (#19429)
  _Files: `jenkins/BoltProfileGen.groovy`, `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`, `scripts/bolt/apply_bolt.py` _+4 more__
- **2026-09-30** [`a44ccaa2a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/a44ccaa2a0) [#19730](https://github.com/NVIDIA/TensorRT-LLM/pull/19730)
  [None][infra] Waive 3 failed cases for main in pre-merge 62514 (#19730)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`e10d917017`](https://github.com/NVIDIA/TensorRT-LLM/commit/e10d917017) [#19728](https://github.com/NVIDIA/TensorRT-LLM/pull/19728)
  [None][infra] Waive 2 failed cases for main in pre-merge 62511 (#19728)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`50f85bfe3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/50f85bfe3e) [#19642](https://github.com/NVIDIA/TensorRT-LLM/pull/19642)
  [None][test] Remove 32 closed-bug waive entries for main (#19642)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`a8fa509f05`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8fa509f05) [#19725](https://github.com/NVIDIA/TensorRT-LLM/pull/19725)
  [None][infra] Waive 1 failed cases for main in pre-merge 62506 (#19725)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`6c0d4f3df8`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c0d4f3df8) [#19711](https://github.com/NVIDIA/TensorRT-LLM/pull/19711)
  [https://nvbugs/6848775][waive] Waive test_minimax_m3_piecewise_empty_adp_rank_preserves_caches (#19711)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-30** [`19c521e255`](https://github.com/NVIDIA/TensorRT-LLM/commit/19c521e255) [#19691](https://github.com/NVIDIA/TensorRT-LLM/pull/19691)
  [None][infra] Waive 3 failed cases for main in post-merge 2990 (#19691)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`bcb288a211`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcb288a211)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-09-29** [`af131fc340`](https://github.com/NVIDIA/TensorRT-LLM/commit/af131fc340) [#19695](https://github.com/NVIDIA/TensorRT-LLM/pull/19695)
  [None][test] Waive 10 failed cases for main in QA CI (#19695)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`ffa8689309`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffa8689309) [#19689](https://github.com/NVIDIA/TensorRT-LLM/pull/19689)
  [None][infra] Add blossom-ci authorized users (#19689)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-09-29** [`eeaf22bbec`](https://github.com/NVIDIA/TensorRT-LLM/commit/eeaf22bbec) [#19687](https://github.com/NVIDIA/TensorRT-LLM/pull/19687)
  [None][test] Waive 2 failed cases for main in QA CI (#19687)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`e0337567b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0337567b2) [#19686](https://github.com/NVIDIA/TensorRT-LLM/pull/19686)
  [None][test] Waive 1 failed cases for main in QA CI (#19686)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`010a3d3f2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/010a3d3f2a) [#19684](https://github.com/NVIDIA/TensorRT-LLM/pull/19684)
  [None][test] Waive 5 failed cases for main in QA CI (#19684)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`99977b5805`](https://github.com/NVIDIA/TensorRT-LLM/commit/99977b5805) [#19677](https://github.com/NVIDIA/TensorRT-LLM/pull/19677)
  [None][test] Waive 4 failed cases for main in QA CI (#19677)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`132ab800cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/132ab800cb) [#19672](https://github.com/NVIDIA/TensorRT-LLM/pull/19672)
  [None][test] Waive 5 failed cases for main in QA CI (#19672)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`30117f9b9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/30117f9b9b) [#19671](https://github.com/NVIDIA/TensorRT-LLM/pull/19671)
  [None][test] Waive 6 failed cases for main in QA CI (#19671)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-28** [`5054e82a6d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5054e82a6d) [#19669](https://github.com/NVIDIA/TensorRT-LLM/pull/19669)
  [None][chore] Waive failing tests (#19669)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-28** [`a8aae0421c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8aae0421c) [#19655](https://github.com/NVIDIA/TensorRT-LLM/pull/19655)
  [https://nvbugs/6831694][fix] Unwaive MSA cache-view and warmup policy tests (#19655)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-28** [`7c280a7707`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c280a7707) [#19662](https://github.com/NVIDIA/TensorRT-LLM/pull/19662)
  [None][infra] Waive 1 failed cases for main in pre-merge 62247 (#19662)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-28** [`7dfacfb583`](https://github.com/NVIDIA/TensorRT-LLM/commit/7dfacfb583)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-09-28** [`f00e9627fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/f00e9627fa) [#19621](https://github.com/NVIDIA/TensorRT-LLM/pull/19621)
  [None][infra] Add scheduled CodeRabbit semantic checks (#19621)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_cases.js`, `.github/scripts/semantic_review_cursor.js` _+8 more__
- **2026-09-28** [`48a1a0c3a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/48a1a0c3a0)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-09-28** [`7caae681b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/7caae681b6)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Executor / Runtime  (21 commits)

- **2026-10-05** [`276cc12ff5`](https://github.com/NVIDIA/TensorRT-LLM/commit/276cc12ff5) [#19811](https://github.com/NVIDIA/TensorRT-LLM/pull/19811)
  [TRTLLM-16757][fix] Forward-port configuration model-list telemetry capture to main (#19811)
  _Files: `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/usage/llmapi_config.py`, `tests/unittest/usage/test_llmapi_config_capture.py`, `tests/unittest/usage/test_llmapi_model_sequences.py`_
- **2026-10-05** [`82f980469f`](https://github.com/NVIDIA/TensorRT-LLM/commit/82f980469f) [#19552](https://github.com/NVIDIA/TensorRT-LLM/pull/19552)
  [TRTLLMINF-15][build] Remove Conan from the C++ build (#19552)
  _Files: `.github/CODEOWNERS`, `.gitignore`, `.pre-commit-config.yaml`, `3rdparty/cpp-thirdparty.md` _+18 more__
- **2026-10-04** [`cf5dc9f970`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf5dc9f970) [#19770](https://github.com/NVIDIA/TensorRT-LLM/pull/19770)
  [https://nvbugs/6809357][fix] Drain incompatible cached test worker pools (#19770)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/test_common/session_reuse.py`, `tests/unittest/llmapi/test_session_reuse.py`_
- **2026-10-03** [`78dac6256b`](https://github.com/NVIDIA/TensorRT-LLM/commit/78dac6256b) [#18813](https://github.com/NVIDIA/TensorRT-LLM/pull/18813)
  [None][Perf] Resolve the runtime JIT issue (#18813)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_k3_mamba_metadata.py` _+7 more__
- **2026-10-03** [`d2a87d360b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2a87d360b) [#19717](https://github.com/NVIDIA/TensorRT-LLM/pull/19717)
  [None][feat] Add iter_perf_stats_interval to sample iteration stats (#19717)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/usage/llm_args_golden_manifest.json` _+4 more__
- **2026-10-02** [`5e2758b832`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e2758b832) [#19439](https://github.com/NVIDIA/TensorRT-LLM/pull/19439)
  [TRTLLM-16707][feat] Support model_kwargs with encoder CUDA graphs (#19439)
  _Files: `docs/source/features/embeddings.md`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/encoder.py`, `tensorrt_llm/commands/serve.py` _+10 more__
- **2026-10-02** [`6096aa814d`](https://github.com/NVIDIA/TensorRT-LLM/commit/6096aa814d) [#19702](https://github.com/NVIDIA/TensorRT-LLM/pull/19702)
  [TRTLLM-15824][feat] Enable EVS handoff for Nemotron-H in EPD (#19702)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/mm_encoder.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py` _+4 more__
- **2026-10-02** [`5ce4cb57cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ce4cb57cb) [#19670](https://github.com/NVIDIA/TensorRT-LLM/pull/19670)
  [None][feat] Add configurable SWA endpoint retention priority (#19670)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/llmapi/llm_utils.py` _+4 more__
- **2026-10-02** [`b75bcd1458`](https://github.com/NVIDIA/TensorRT-LLM/commit/b75bcd1458) [#19743](https://github.com/NVIDIA/TensorRT-LLM/pull/19743)
  [None][fix] Latch cached_tokens from the prefix reuse decision, not the decode position (#19743)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/llm_request_factory.py`, `tests/unittest/_torch/executor/test_disagg_receive_ordering.py` _+2 more__
- **2026-10-02** [`51d5777be1`](https://github.com/NVIDIA/TensorRT-LLM/commit/51d5777be1) [#19235](https://github.com/NVIDIA/TensorRT-LLM/pull/19235)
  [None][feat] Mooncake store part 1: pool, CLI, and V2 scheduler preemption (#19235)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/pyexecutor/connectors/mooncake_store/__init__.py`, `tensorrt_llm/_torch/pyexecutor/connectors/mooncake_store/config.py`, `tensorrt_llm/_torch/pyexecutor/connectors/mooncake_store/donor.py` _+16 more__
- **2026-10-01** [`8cfee7777d`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cfee7777d) [#19704](https://github.com/NVIDIA/TensorRT-LLM/pull/19704)
  [None][fix] Keep exit telemetry independent of blocked heartbeats (#19704)
  _Files: `tensorrt_llm/usage/usage_lib.py`, `tests/unittest/llmapi/test_llm_telemetry.py`, `tests/unittest/llmapi/test_llm_telemetry_payload.py`, `tests/unittest/usage/test_cli_telemetry.py` _+3 more__
- **2026-10-01** [`80509acfc0`](https://github.com/NVIDIA/TensorRT-LLM/commit/80509acfc0) [#19555](https://github.com/NVIDIA/TensorRT-LLM/pull/19555)
  [TRTLLM-16630][feat] Add CLI config overrides (#19555)
  _Files: `.pre-commit-config.yaml`, `docs/source/commands/trtllm-serve/run-benchmark-with-trtllm-serve.md`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `legacy-files.txt` _+13 more__
- **2026-10-01** [`28c5d5a5c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/28c5d5a5c5) [#19457](https://github.com/NVIDIA/TensorRT-LLM/pull/19457)
  [None][fix] Report context-length-exceeded with OpenAI-style message and error code (#19457)
  _Files: `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/serve/openai_disagg_server.py`, `tensorrt_llm/serve/openai_protocol.py` _+3 more__
- **2026-10-01** [`95cb50c358`](https://github.com/NVIDIA/TensorRT-LLM/commit/95cb50c358) [#19658](https://github.com/NVIDIA/TensorRT-LLM/pull/19658)
  [None][perf] Accept a flat int32 array as GenerationRequest prompt without materializing a list (#19658)
  _Files: `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/request.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/executor/test_generation_request_array_prompt.py`_
- **2026-09-30** [`a6179fec6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6179fec6e) [#19499](https://github.com/NVIDIA/TensorRT-LLM/pull/19499)
  [None][feat] Add a per-model serving-extension registry to the OpenAI server (#19499)
  _Files: `tensorrt_llm/serve/extensions/__init__.py`, `tensorrt_llm/serve/extensions/gpt_oss.py`, `tensorrt_llm/serve/extensions/kimi_k3.py`, `tensorrt_llm/serve/openai_protocol.py` _+5 more__
- **2026-09-30** [`bdd012579f`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdd012579f) [#19156](https://github.com/NVIDIA/TensorRT-LLM/pull/19156)
  [None][fix] Prevent unintended dynamic NVRTC linkage through pg_utils (#19156)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/common/CMakeLists.txt`, `cpp/tensorrt_llm/common/ncclUtils.cpp`, `cpp/tensorrt_llm/common/ncclUtils.h` _+3 more__
- **2026-09-30** [`e336a2e5ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/e336a2e5ee) [#19620](https://github.com/NVIDIA/TensorRT-LLM/pull/19620)
  [None][fix] Keep telemetry heartbeats running for long-lived sessions (#19620)
  _Files: `tensorrt_llm/usage/schema.py`, `tensorrt_llm/usage/schemas/README.md`, `tensorrt_llm/usage/usage_lib.py`, `tests/unittest/usage/test_llmapi_config_capture.py` _+1 more__
- **2026-09-29** [`affd824617`](https://github.com/NVIDIA/TensorRT-LLM/commit/affd824617) [#19456](https://github.com/NVIDIA/TensorRT-LLM/pull/19456)
  [None][fix] Tear down cleanly when multi-rank warmup fails (#19456)
  _Files: `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/unittest/_torch/executor/test_distributed_warmup_oom.py` _+1 more__
- **2026-09-29** [`71b26c3fd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/71b26c3fd1) [#19522](https://github.com/NVIDIA/TensorRT-LLM/pull/19522)
  [None][feat] agent flow: add per-role backend routing & casebook switch (#19522)
  _Files: `agent-flow/agent_flow/agent_runtime.py`, `agent-flow/agent_flow/backends/__init__.py`, `agent-flow/agent_flow/backends/claude_code.py`, `agent-flow/agent_flow/backends/codex.py` _+27 more__
- **2026-09-28** [`f2b6531e5d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f2b6531e5d) [#19595](https://github.com/NVIDIA/TensorRT-LLM/pull/19595)
  [None][fix] Report public runtime architectures in telemetry (#19595)
  _Files: `AGENTS.md`, `README.md`, `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/usage/architecture_allowlist.py` _+5 more__
- **2026-09-28** [`a4f358a3a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4f358a3a1) [#17974](https://github.com/NVIDIA/TensorRT-LLM/pull/17974)
  [TRTLLM-12891][feat] Include KV connector prefixes in V2 scheduler budgeting (#17974)
  _Files: `docs/source/features/kv-cache-connector.md`, `examples/llm-api/llm_kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/prefix_load_completion.py` _+15 more__

## Attention  (14 commits)

- **2026-10-03** [`ace058d1f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/ace058d1f5) [#17476](https://github.com/NVIDIA/TensorRT-LLM/pull/17476)
  [None][feat] Load static FP8 Cosmos3 Nano/Super checkpoints without re-quantizing them (#17476)
  _Files: `examples/visual_gen/configs/cosmos3-fp8-1gpu.yaml`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py` _+21 more__
- **2026-10-02** [`8046c42d93`](https://github.com/NVIDIA/TensorRT-LLM/commit/8046c42d93) [#18060](https://github.com/NVIDIA/TensorRT-LLM/pull/18060)
  [TRTLLM-15447][feat] Add model startup stage timing metrics (#18060)
  _Files: `docs/source/llm-api/index.md`, `tensorrt_llm/_startup.py`, `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/pyexecutor/breakable_cuda_graph_runner.py` _+11 more__
- **2026-10-02** [`8403820d82`](https://github.com/NVIDIA/TensorRT-LLM/commit/8403820d82) [#19808](https://github.com/NVIDIA/TensorRT-LLM/pull/19808)
  [https://nvbugs/6862662][chore] waive test_attention_mla (#19808)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-10-02** [`8a3c90311e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a3c90311e) [#18705](https://github.com/NVIDIA/TensorRT-LLM/pull/18705)
  [https://nvbugs/6720547][fix] Exclude padded Cosmos3 text from sequence-parallel attention (#18705)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+5 more__
- **2026-10-01** [`cc71759303`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc71759303) [#19502](https://github.com/NVIDIA/TensorRT-LLM/pull/19502)
  [TRTLLM-16283][feat] Prepare DeepSeek V4 attention for sparse KV offload (#19502)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/kernels.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/metadata.py` _+8 more__
- **2026-09-30** [`6bfc3ad499`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bfc3ad499) [#19626](https://github.com/NVIDIA/TensorRT-LLM/pull/19626)
  [https://nvbugs/6812347][fix] Include the SM107 trtllm-gen context FMHA kernels (#19626)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`_
- **2026-09-30** [`324a51deff`](https://github.com/NVIDIA/TensorRT-LLM/commit/324a51deff) [#18079](https://github.com/NVIDIA/TensorRT-LLM/pull/18079)
  [None][feat] add VisualGen VSA and SOL sparse attention on PrimTS block-sparse FMHA (#18079)
  _Files: `docs/source/features/visualgen-sparse-attention.md`, `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py` _+64 more__
- **2026-09-30** [`f53d031b6d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f53d031b6d) [#19154](https://github.com/NVIDIA/TensorRT-LLM/pull/19154)
  [None][refactor] BREAKING: Remove the Python backend of KVCacheManagerV2 (#19154)
  _Files: `.gitignore`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/cudaVirtMem.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/exceptions.h` _+80 more__
- **2026-09-29** [`7950afe401`](https://github.com/NVIDIA/TensorRT-LLM/commit/7950afe401) [#19113](https://github.com/NVIDIA/TensorRT-LLM/pull/19113)
  [None][fix] Guard MiniMax-M3 FP8 indexer against padded -1 cache slots (#19113)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/msa_utils.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/paged_cache.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/triton_sparse_decode.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/trtllm_gen_dense_decode.py` _+6 more__
- **2026-09-29** [`ae4aa5d6c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae4aa5d6c9) [#19654](https://github.com/NVIDIA/TensorRT-LLM/pull/19654)
  [None][fix] Gate Flash-Next FP8 concurrency-16 perf on B300/GB300 (#19654)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-29** [`f08592ada0`](https://github.com/NVIDIA/TensorRT-LLM/commit/f08592ada0) [#19591](https://github.com/NVIDIA/TensorRT-LLM/pull/19591)
  [None][chore] Update trtllm-gen FMHA artifacts (#19591)
- **2026-09-28** [`f9beeba215`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9beeba215) [#19292](https://github.com/NVIDIA/TensorRT-LLM/pull/19292)
  [None][fix] Disable FA4 2CTA by default for VisualGen (#19292)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/flash_attn4.py`_
- **2026-09-28** [`27ba69c781`](https://github.com/NVIDIA/TensorRT-LLM/commit/27ba69c781) [#19543](https://github.com/NVIDIA/TensorRT-LLM/pull/19543)
  [https://nvbugs/6820152][test] Enforce VisualGen test requirements (#19543)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_wan.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/multi_gpu/test_attn2d_attention.py` _+5 more__
- **2026-09-28** [`73102db45c`](https://github.com/NVIDIA/TensorRT-LLM/commit/73102db45c) [#19667](https://github.com/NVIDIA/TensorRT-LLM/pull/19667)
  [https://nvbugs/6842831][fix] Restore FlashInfer GDN decode test collection (#19667)
  _Files: `tests/unittest/_torch/modules/mamba/test_flashinfer_gdn_decode.py`_

## Quantization  (13 commits)

- **2026-10-05** [`bb367fc8c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb367fc8c1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__
- **2026-10-04** [`bf414e3729`](https://github.com/NVIDIA/TensorRT-LLM/commit/bf414e3729) [#19661](https://github.com/NVIDIA/TensorRT-LLM/pull/19661)
  [https://nvbugs/6763479][chore] Update GLM-Image goldens (#19661)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/glm_image_fp8_blockwise_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/glm_image_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/glm_image_nvfp4_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media.zip` _+2 more__
- **2026-10-04** [`fc0876cfd6`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc0876cfd6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__
- **2026-10-02** [`06ad135dfa`](https://github.com/NVIDIA/TensorRT-LLM/commit/06ad135dfa)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-09-30** [`6ae42bb892`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ae42bb892)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+5 more__
- **2026-09-30** [`ea8f40586b`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea8f40586b) [#19692](https://github.com/NVIDIA/TensorRT-LLM/pull/19692)
  [None][fix] Increase DeepSeek V4 FP8 perf server startup timeout (#19692)
  _Files: `tests/integration/defs/perf/test_perf.py`_
- **2026-09-30** [`fe5e1415b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe5e1415b5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-09-30** [`111687f92f`](https://github.com/NVIDIA/TensorRT-LLM/commit/111687f92f) [#19675](https://github.com/NVIDIA/TensorRT-LLM/pull/19675)
  [None][test] Add coverage for TritonMXFP4LinearMethod.apply (#19675)
  _Files: `tests/unittest/_torch/modules/test_triton_linear.py`_
- **2026-09-29** [`d594b622c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/d594b622c4) [#19633](https://github.com/NVIDIA/TensorRT-LLM/pull/19633)
  [https://nvbugs/6801102][fix] Registered the measured GSM8K reference (89.083) for MXFP8 + FP8 KV cache… (#19633)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-09-29** [`1e4e65ce75`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e4e65ce75)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+6 more__
- **2026-09-28** [`b5109d949f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5109d949f) [#19656](https://github.com/NVIDIA/TensorRT-LLM/pull/19656)
  [https://nvbugs/6835139][chore] Unwaive test_compiled_mxfp8_warmup_backend_selection (#19656)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-28** [`336c4337a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/336c4337a0) [#16889](https://github.com/NVIDIA/TensorRT-LLM/pull/16889)
  [None][feat] Add Qwen-Image-Layered FP8 and Cache-DiT support (#16889)
  _Files: `docs/source/models/supported-models.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/qwen-image-layered-fp8-1gpu.yaml`, `tensorrt_llm/_torch/visual_gen/cache/cache_dit_enablers.py` _+3 more__
- **2026-09-28** [`c2220eef33`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2220eef33)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__

## Other  (6 commits)

- **2026-10-02** [`ff5a62eca2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff5a62eca2) [#19805](https://github.com/NVIDIA/TensorRT-LLM/pull/19805)
  [None][fix] Disable interactions between automated PR reviewers (#19805)
  _Files: `.coderabbit.yaml`, `.github/scripts/semantic_review.test.js`, `.github/semantic-review.md`, `.github/workflows/semantic-review.yml` _+1 more__
- **2026-10-02** [`a81da8a5a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/a81da8a5a8) [#19780](https://github.com/NVIDIA/TensorRT-LLM/pull/19780)
  [https://nvbugs/6801108][fix] Set NCCL env vars before ncclGetUniqueId in getComm (#19780)
  _Files: `cpp/tensorrt_llm/common/opUtils.cpp`_
- **2026-09-30** [`1553b52449`](https://github.com/NVIDIA/TensorRT-LLM/commit/1553b52449) [#19720](https://github.com/NVIDIA/TensorRT-LLM/pull/19720)
  [None][chore] agent-flow: bump claude-agent-sdk to 0.2.162 and default model to claude-opus-5-5 (#19720)
  _Files: `agent-flow/agent_flow/config.py`, `agent-flow/pyproject.toml`_
- **2026-09-28** [`ca937c9501`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca937c9501) [#19651](https://github.com/NVIDIA/TensorRT-LLM/pull/19651)
  [None][fix] Require integration evidence in semantic review prompts (#19651)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_cases.js`, `.github/semantic-review-prompt.md` _+1 more__
- **2026-09-28** [`cc608b774a`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc608b774a) [#19649](https://github.com/NVIDIA/TensorRT-LLM/pull/19649)
  [None][fix] Publish semantic reviews with per-PR commit statuses (#19649)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_request.js`, `.github/scripts/semantic_review_request.test.js` _+2 more__
- **2026-09-28** [`a66196b125`](https://github.com/NVIDIA/TensorRT-LLM/commit/a66196b125) [#19577](https://github.com/NVIDIA/TensorRT-LLM/pull/19577)
  [None][fix] Make integrator gain gate authoritative (#19577)
  _Files: `agent-flow/agent_flow/workflows/perf_optimize/progress.py`, `agent-flow/agent_flow/workflows/perf_optimize/workflow.py`, `agent-flow/tests/workflows/perf_optimize/test_progress.py`, `agent-flow/tests/workflows/perf_optimize/test_workflow.py`_

## MoE  (6 commits)

- **2026-10-02** [`50356f3ee3`](https://github.com/NVIDIA/TensorRT-LLM/commit/50356f3ee3) [#19597](https://github.com/NVIDIA/TensorRT-LLM/pull/19597)
  [None][feat] Load quantized Nemotron-H MTP replacements (#19597)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_h_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_next_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen4_exp_weight_mapper.py` _+14 more__
- **2026-09-30** [`14863787ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/14863787ca) [#19644](https://github.com/NVIDIA/TensorRT-LLM/pull/19644)
  [None][fix] Move the CuteDSL locality domain weight split into staged hooks (#19644)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`, `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`_
- **2026-09-30** [`6592b5d53f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6592b5d53f) [#19217](https://github.com/NVIDIA/TensorRT-LLM/pull/19217)
  [TRTLLM-16404][fix] support post-SiLU clamp in CUTLASS MoE (#19217)
  _Files: `cpp/tensorrt_llm/kernels/moe/cutlass/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/moe/cutlass/moe_kernels.cu`, `cpp/tensorrt_llm/kernels/moe/cutlass/moe_kernels.cuh`, `cpp/tensorrt_llm/thop/moe/cutlass/moeOp.cpp` _+13 more__
- **2026-09-30** [`7fe1dd2ba6`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fe1dd2ba6) [#19682](https://github.com/NVIDIA/TensorRT-LLM/pull/19682)
  [None][perf] MoE routing: small-token single-block kernel for <= 8 tokens in the trtllm-gen custom routing (#19682)
  _Files: `cpp/tensorrt_llm/kernels/moe/trtllmGen/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingCustomKernels.cuh`, `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingCustomPolicy.cuh`, `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingCustomSelection.h` _+3 more__
- **2026-09-28** [`50e3b40aa1`](https://github.com/NVIDIA/TensorRT-LLM/commit/50e3b40aa1) [#17028](https://github.com/NVIDIA/TensorRT-LLM/pull/17028)
  [#17027][fix] Realign misaligned int32 index slices in FlashInfer GDN decode (#17028)
  _Files: `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_gdn_decode.py`_
- **2026-09-28** [`d21a8cebbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/d21a8cebbd) [#19136](https://github.com/NVIDIA/TensorRT-LLM/pull/19136)
  [None][feat] Add GLM-5.3-Flash (glm5_next) support (#19136)
  _Files: `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.h`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeLegacy.cu`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeOptimized.cu`, `cpp/tensorrt_llm/thop/kdaDecodeOp.cpp` _+55 more__

## Docs / Examples  (4 commits)

- **2026-10-02** [`f388b7c6a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/f388b7c6a5) [#19750](https://github.com/NVIDIA/TensorRT-LLM/pull/19750)
  [None][fix] Preserve OpenEngine conversation context and prefill handoffs (#19750)
  _Files: `tensorrt_llm/grpc/openengine/README.md`, `tensorrt_llm/grpc/openengine/request_mapping.py`, `tensorrt_llm/grpc/openengine/servicer.py`, `tensorrt_llm/grpc/openengine/streaming.py` _+1 more__
- **2026-09-30** [`abddfc9914`](https://github.com/NVIDIA/TensorRT-LLM/commit/abddfc9914) [#19715](https://github.com/NVIDIA/TensorRT-LLM/pull/19715)
  [None][feat] agent-flow: snapshot the composed prompts into the workspace (#19715)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/__init__.py`, `agent-flow/agent_flow/prompts.py`, `agent-flow/agent_flow/workflows/perf_analyze/README.md` _+8 more__
- **2026-09-29** [`bcdc2d5aaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcdc2d5aaf) [#19616](https://github.com/NVIDIA/TensorRT-LLM/pull/19616)
  [None][chore] Bump version to 1.4.0rc0 (#19616)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-09-29** [`d949656a4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d949656a4f)
  [None][chore] Bump version to 1.3.0rc30
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## Torch Path (_torch)  (4 commits)

- **2026-10-01** [`de1d696889`](https://github.com/NVIDIA/TensorRT-LLM/commit/de1d696889) [#19741](https://github.com/NVIDIA/TensorRT-LLM/pull/19741)
  [https://nvbugs/6625695][fix] Compare teacher-forced logits in the Nemotron VL video batch-equivalence test (#19741)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_nemotron_h_multimodal.py`_
- **2026-10-01** [`0d3bbd257d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d3bbd257d) [#19504](https://github.com/NVIDIA/TensorRT-LLM/pull/19504)
  [None][fix] Cosmos3: pin cosmos_guardrail 0.3.2, fetch only the guardrail files it loads, fix the install hint (#19504)
  _Files: `examples/visual_gen/models/cosmos3/README.md`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/guardrails.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+1 more__
- **2026-09-29** [`313c4858e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/313c4858e4) [#19648](https://github.com/NVIDIA/TensorRT-LLM/pull/19648)
  [TRTLLM-15824][feat] Enable EVS for Nemotron Super 3.5 VL (#19648)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py`, `tests/unittest/_torch/modeling/test_nemotron_h_multimodal_preprocessing.py`_
- **2026-09-28** [`0c58480ca6`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c58480ca6) [#19019](https://github.com/NVIDIA/TensorRT-LLM/pull/19019)
  [None][doc] Update the docs for the NGC PyTorch 26.08 and torch 2.14.0 upgrades (#19019)
  _Files: `README.md`, `docs/source/installation/installation-guide.md`_

## LoRA  (3 commits)

- **2026-10-05** [`dc31d8ddef`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc31d8ddef) [#19701](https://github.com/NVIDIA/TensorRT-LLM/pull/19701)
  [TRTLLM-16672][feat] MiniMax H3 Turbo LoRA Tensor Name Mapping (#19701)
  _Files: `tensorrt_llm/_torch/visual_gen/runtime_lora.py`, `tests/unittest/_torch/visual_gen/test_runtime_lora.py`_
- **2026-10-01** [`534e1f8ad9`](https://github.com/NVIDIA/TensorRT-LLM/commit/534e1f8ad9) [#19371](https://github.com/NVIDIA/TensorRT-LLM/pull/19371)
  [TRTLLM-16654][feat] vendor OpenEngine Python bindings (#19371)
  _Files: `.gitattributes`, `.pre-commit-config.yaml`, `3rdparty/vendor_sources.lock.yaml`, `docker/Dockerfile.multi` _+55 more__
- **2026-09-30** [`a223c73d83`](https://github.com/NVIDIA/TensorRT-LLM/commit/a223c73d83) [#19592](https://github.com/NVIDIA/TensorRT-LLM/pull/19592)
  [TRTLLM-15760][refactor] Establish model runner contracts and shared model invocation (#19592)
  _Files: `tensorrt_llm/_torch/pyexecutor/encoder_executor.py`, `tensorrt_llm/_torch/pyexecutor/engine/input_buffers.py`, `tensorrt_llm/_torch/pyexecutor/engine/lora.py`, `tensorrt_llm/_torch/pyexecutor/engine/model_call.py` _+19 more__

## ROCm / AMD  (3 commits)

- **2026-10-02** [`f7518a6427`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7518a6427) [#19674](https://github.com/NVIDIA/TensorRT-LLM/pull/19674)
  [None][fix] Fail stop executor worlds on unproven KV retirement (#19674)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tests/unittest/disaggregated/test_kv_transfer_fail_stop.py` _+4 more__
- **2026-09-30** [`84de36ed03`](https://github.com/NVIDIA/TensorRT-LLM/commit/84de36ed03) [#19545](https://github.com/NVIDIA/TensorRT-LLM/pull/19545)
  [None][fix] Gate disaggregated KV block reuse admission on verified write coverage (#19545)
  _Files: `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/fetch.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/utils.py` _+5 more__
- **2026-09-29** [`00bdcb6ed7`](https://github.com/NVIDIA/TensorRT-LLM/commit/00bdcb6ed7) [#19378](https://github.com/NVIDIA/TensorRT-LLM/pull/19378)
  [None][fix] Retire KV transfer ownership after late backend completion (#19378)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_transfer_late_settlement.py`, `tests/unittest/disaggregated/test_transfer_ownership_regressions.py`_

## Disaggregation / KV  (3 commits)

- **2026-10-02** [`80f1809362`](https://github.com/NVIDIA/TensorRT-LLM/commit/80f1809362) [#19580](https://github.com/NVIDIA/TensorRT-LLM/pull/19580)
  [TRTLLM-16282][feat] Add sparse KV cache configuration and tier-aware locking (#19580)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/common.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h` _+16 more__
- **2026-10-01** [`6f43d7edab`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f43d7edab) [#19673](https://github.com/NVIDIA/TensorRT-LLM/pull/19673)
  [None][fix] Bound unproven KV retirement with non-resettable deadlines (#19673)
  _Files: `tensorrt_llm/_torch/disaggregation/native/retirement.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_retirement_deadline.py`, `tests/unittest/disaggregated/test_task_handle.py` _+2 more__
- **2026-09-29** [`ae3531adf3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae3531adf3) [#19351](https://github.com/NVIDIA/TensorRT-LLM/pull/19351)
  [None][fix] Validate unused chat template controls and normalize router tool arguments (#19351)
  _Files: `tensorrt_llm/inputs/chat_template_guard.py`, `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/anthropic_adapter.py`, `tensorrt_llm/serve/chat_tokenization.py` _+9 more__

## Speculative Decoding  (2 commits)

- **2026-10-03** [`4151db3c2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/4151db3c2e) [#19311](https://github.com/NVIDIA/TensorRT-LLM/pull/19311)
  [None][feat] Report per-request speculative-decoding acceptance on the response (#19311)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/postproc_worker.py`, `tensorrt_llm/executor/result.py`, `tensorrt_llm/llmapi/llm_args.py` _+12 more__
- **2026-10-02** [`ca37c9f725`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca37c9f725) [#19785](https://github.com/NVIDIA/TensorRT-LLM/pull/19785)
  [None][perf] MTP draft loop: select rows with a prefix slice from draft step 1 (#19785)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`_

## Models  (2 commits)

- **2026-10-02** [`f1a48e6c47`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1a48e6c47) [#19784](https://github.com/NVIDIA/TensorRT-LLM/pull/19784)
  [https://nvbugs/6783973][doc] Stop listing supported SA speculation as a Kimi K3 limitation (#19784)
  _Files: `examples/kimi_k3/README.md`_
- **2026-09-29** [`2c9fb23842`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c9fb23842) [#19581](https://github.com/NVIDIA/TensorRT-LLM/pull/19581)
  [None][fix] wait for K1 readers before reusing KDA prefill stages (#19581)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/kimi_k3_kda/fused_k123.py`, `tests/unittest/_torch/modules/kimi_kda/test_kda_prefill_state_parity.py`_

---
_Generated 2026-10-05 17:13 UTC_