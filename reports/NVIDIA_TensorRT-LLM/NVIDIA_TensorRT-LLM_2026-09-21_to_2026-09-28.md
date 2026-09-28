# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-09-21 → 2026-09-28  |  **Total commits:** 144

## ✨ New Features This Week

- **2026-09-28** [#19621](https://github.com/NVIDIA/TensorRT-LLM/pull/19621) — [None][infra] Add scheduled CodeRabbit semantic checks (#19621)
- **2026-09-28** [#19136](https://github.com/NVIDIA/TensorRT-LLM/pull/19136) — [None][feat] Add GLM-5.3-Flash (glm5_next) support (#19136)
- **2026-09-27** [#19056](https://github.com/NVIDIA/TensorRT-LLM/pull/19056) — [TRTLLM-16304][feat] In-tree implementation of staircase (#19056)
- **2026-09-26** [#19422](https://github.com/NVIDIA/TensorRT-LLM/pull/19422) — [None][perf] Add MiniMax-M3 NVFP4 KV cache support (#19422)
- **2026-09-23** [#18231](https://github.com/NVIDIA/TensorRT-LLM/pull/18231) — [None][feat] Add support for mnnvl allreduce under ray orchestrator (#18231)
- **2026-09-23** [#18995](https://github.com/NVIDIA/TensorRT-LLM/pull/18995) — [None][test] Add Helix zero-KV multi-GPU regression coverage (#18995)
- **2026-09-22** [#18478](https://github.com/NVIDIA/TensorRT-LLM/pull/18478) — [None][feat] Rubin fp4 mla core (P1) (#18478)
- **2026-09-22** [#19375](https://github.com/NVIDIA/TensorRT-LLM/pull/19375) — [None][feat] Add opt-in per-request cached KV token logging (#19375)
- **2026-09-22** [#19376](https://github.com/NVIDIA/TensorRT-LLM/pull/19376) — [None][perf] Enable flashinfer gdn prefill on sm120/121 (#19376)
- **2026-09-22** [#16323](https://github.com/NVIDIA/TensorRT-LLM/pull/16323) — [None][chore] Add per-rank routing/scheduling observability to the iteration log (#16323)
- _…and 18 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-24** [`4eee1fb1cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/4eee1fb1cb) [#19377](https://github.com/NVIDIA/TensorRT-LLM/pull/19377) — [None][fix] Preserve KV transfer outcomes independently of polling (#19377)
- **2026-09-23** [`adea5c0720`](https://github.com/NVIDIA/TensorRT-LLM/commit/adea5c0720) [#19477](https://github.com/NVIDIA/TensorRT-LLM/pull/19477) — [TRTLLMINF-391][infra] Upgrade public PyTorch to 2.14 and integrate Triton 3.8 (#19477)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#19501](https://github.com/NVIDIA/TensorRT-LLM/issues/19501) | [RFC] Training/Inference Numerical Consistency for RL Post-Training | RFC | 2026-09-25 |
| [#19634](https://github.com/NVIDIA/TensorRT-LLM/issues/19634) | [Bug]: multi-node MPI-orchestrator serve hangs at IPC init (queues bin | Inference runtime, Disaggregated serving | 2026-09-25 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-09-23 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-09-21 |
| [#19232](https://github.com/NVIDIA/TensorRT-LLM/issues/19232) | [RFC]: Disaggregated request preprocessing | triaged, Investigating, LLM API, Disaggregated serving, RFC, Frontend | 2026-09-16 |
| [#19242](https://github.com/NVIDIA/TensorRT-LLM/issues/19242) | [Bug]: KVCacheBlock and its radix tree LookupNode own each other with  | KV-Cache Management | 2026-09-16 |
| [#19240](https://github.com/NVIDIA/TensorRT-LLM/issues/19240) | [Bug]: mixtureOfExpertsTest crashes with SEGV when a parameter set has | Customized kernels | 2026-09-16 |
| [#19059](https://github.com/NVIDIA/TensorRT-LLM/issues/19059) | [Bug]: C++17 build cannot compile torch 2.12 headers with nvcc, but C+ | Pytorch | 2026-09-15 |
| [#19172](https://github.com/NVIDIA/TensorRT-LLM/issues/19172) | [Bug]: Async prompt-embedding H2D outlives its pooled-pinned source; t | bug, Triton backend, Inference runtime | 2026-09-14 |
| [#19067](https://github.com/NVIDIA/TensorRT-LLM/issues/19067) | [Bug]: -a 107-real is silently folded to 100, no SM107 code is generat | Infra | 2026-09-11 |
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-09-09 |
| [#18847](https://github.com/NVIDIA/TensorRT-LLM/issues/18847) | [Bug] Worker CPU affinity is applied process-wide in shared-process de | Inference runtime | 2026-09-07 |
| [#18687](https://github.com/NVIDIA/TensorRT-LLM/issues/18687) | [Bug]: Cosmos3 sequence-parallel path attends zero-padded text K/V whe | bug, VisualGen | 2026-09-03 |
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-09-02 |
| [#18407](https://github.com/NVIDIA/TensorRT-LLM/issues/18407) | [Bug]: KVCacheV2Scheduler retains active PEFT adapters after KV suspen | KV-Cache Management, Lora/P-tuning, Pytorch | 2026-08-30 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-08-27 |
| [#18156](https://github.com/NVIDIA/TensorRT-LLM/issues/18156) | KV-cache-aware router never matches LoRA or salted requests: lora_id i | Disaggregated serving | 2026-08-24 |
| [#18153](https://github.com/NVIDIA/TensorRT-LLM/issues/18153) | [RFC]: Versioned KV Hints Protocol for TRT-LLM | RFC | 2026-08-24 |
| [#18085](https://github.com/NVIDIA/TensorRT-LLM/issues/18085) | [RFC] DFlash2 for Qwen3.8 on consumer Blackwell: integration boundary  | Speculative Decoding | 2026-08-21 |
| [#17714](https://github.com/NVIDIA/TensorRT-LLM/issues/17714) | [Feature] NcclEP backend hardcodes LOW_LATENCY + RANK_MAJOR; algorithm | Scale-out | 2026-08-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 26 |
| Attention | 21 |
| MoE | 20 |
| Disaggregation / KV | 14 |
| Executor / Runtime | 13 |
| Other | 9 |
| Torch Path (_torch) | 9 |
| Quantization | 8 |
| Speculative Decoding | 7 |
| Models | 7 |
| Docs / Examples | 4 |
| ROCm / AMD | 2 |
| AutoDeploy | 2 |
| LoRA | 1 |
| Compilation / Graph | 1 |

## CI / Infra  (26 commits)

- **2026-09-28** [`f00e9627fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/f00e9627fa) [#19621](https://github.com/NVIDIA/TensorRT-LLM/pull/19621)
  [None][infra] Add scheduled CodeRabbit semantic checks (#19621)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_cases.js`, `.github/scripts/semantic_review_cursor.js` _+8 more__
- **2026-09-28** [`48a1a0c3a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/48a1a0c3a0)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-09-28** [`7caae681b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/7caae681b6)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-09-24** [`261c5cc9c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/261c5cc9c5) [#19609](https://github.com/NVIDIA/TensorRT-LLM/pull/19609)
  [None][infra] Waive 17 failed cases for main in pre-merge 62054 (#19609)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-24** [`09de3549c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/09de3549c1) [#19611](https://github.com/NVIDIA/TensorRT-LLM/pull/19611)
  [None][infra] Waive 1 failed cases for main in pre-merge 62068 (#19611)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`25e9ddadca`](https://github.com/NVIDIA/TensorRT-LLM/commit/25e9ddadca) [#19579](https://github.com/NVIDIA/TensorRT-LLM/pull/19579)
  [None][infra] Waive 1 failed cases for main in pre-merge 61911 (#19579)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`fa2279b355`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa2279b355) [#19569](https://github.com/NVIDIA/TensorRT-LLM/pull/19569)
  [https://nvbugs/6793964][test] Unwaive test_row_linear[2-unbalanced] (#19569)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`1f12d8d152`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f12d8d152) [#19563](https://github.com/NVIDIA/TensorRT-LLM/pull/19563)
  [https://nvbugs/6607482][ci] Remove stale waive (#19563)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`9e23b80e35`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e23b80e35) [#19574](https://github.com/NVIDIA/TensorRT-LLM/pull/19574)
  [https://nvbugs/6825571][test] Unwaive two disagg coordinator CPU tests (#19574)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`6390f3a4b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/6390f3a4b5) [#19572](https://github.com/NVIDIA/TensorRT-LLM/pull/19572)
  [None][infra] Waive 2 failed cases for main in pre-merge 61872 (#19572)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-23** [`c85c11328c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c85c11328c) [#19345](https://github.com/NVIDIA/TensorRT-LLM/pull/19345)
  [None][fix] suppress GCP host detection xtrace in CI images (#19345)
  _Files: `docker/Dockerfile.multi`, `docker/common/install_base.sh`, `docker/common/sh_env_wrapper.sh`, `jenkins/current_image_tags.properties`_
- **2026-09-22** [`34533411d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/34533411d7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
- **2026-09-22** [`143cea45c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/143cea45c7) [#19438](https://github.com/NVIDIA/TensorRT-LLM/pull/19438)
  [https://nvbugs/6535765][fix] Raise Wan 2.2 LPIPS threshold to 0.25 and unwaive (#19438)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/wan22_t2v_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/test_visual_gen_wan.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`945513ae16`](https://github.com/NVIDIA/TensorRT-LLM/commit/945513ae16) [#19327](https://github.com/NVIDIA/TensorRT-LLM/pull/19327)
  [TRTLLMINF-420][fix] Add Jenkins instance name to SLURM job (#19327)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-22** [`546dc94d3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/546dc94d3d) [#19526](https://github.com/NVIDIA/TensorRT-LLM/pull/19526)
  [https://nvbugs/6670227][test] Unwaive DSv4-Pro token-boundary smoke (#19526)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`d78e8bb607`](https://github.com/NVIDIA/TensorRT-LLM/commit/d78e8bb607) [#19524](https://github.com/NVIDIA/TensorRT-LLM/pull/19524)
  [https://nvbugs/6746167][chore] Remove waivers for bugs 6746167 and 6668773 (#19524)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`2af0b729bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/2af0b729bb) [#19525](https://github.com/NVIDIA/TensorRT-LLM/pull/19525)
  [None][test] Remove stale QA waivers (#19525)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`5b07ab8bc6`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b07ab8bc6) [#19474](https://github.com/NVIDIA/TensorRT-LLM/pull/19474)
  [None][ci] waive pre-existing test failures on main (#19474)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`2ca131b3e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ca131b3e6) [#19486](https://github.com/NVIDIA/TensorRT-LLM/pull/19486)
  [None][test] Waive 2 failed cases for main in QA CI (#19486)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`09fe1084df`](https://github.com/NVIDIA/TensorRT-LLM/commit/09fe1084df) [#19479](https://github.com/NVIDIA/TensorRT-LLM/pull/19479)
  [None][infra] Waive 2 failed cases for main in post-merge 2973 (#19479)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`4d368cfe88`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d368cfe88) [#19471](https://github.com/NVIDIA/TensorRT-LLM/pull/19471)
  [None][test] Waive 5 failed cases for main in QA CI (#19471)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`eca9e520e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/eca9e520e3) [#19473](https://github.com/NVIDIA/TensorRT-LLM/pull/19473)
  [None][test] Waive 2 failed cases for main in QA CI (#19473)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`c515ac5031`](https://github.com/NVIDIA/TensorRT-LLM/commit/c515ac5031) [#19152](https://github.com/NVIDIA/TensorRT-LLM/pull/19152)
  [TRTLLMINF-419][infra] Clean up the devel image build (#19152)
  _Files: `constraints.txt`, `docker/Dockerfile.multi`, `docker/Makefile`, `docker/common/install_base.sh` _+11 more__
- **2026-09-21** [`d1c703d659`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1c703d659) [#19467](https://github.com/NVIDIA/TensorRT-LLM/pull/19467)
  [None][test] Waive 1 failed cases for main in QA CI (#19467)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`9ffc9c9dee`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ffc9c9dee)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-09-21** [`f7c29d75dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7c29d75dc) [#19462](https://github.com/NVIDIA/TensorRT-LLM/pull/19462)
  [None][ci] waive pre-existing test failures on main (#19462)
  _Files: `tests/integration/test_lists/waives.txt`_

## Attention  (21 commits)

- **2026-09-26** [`fba7b54e6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/fba7b54e6b) [#19422](https://github.com/NVIDIA/TensorRT-LLM/pull/19422)
  [None][perf] Add MiniMax-M3 NVFP4 KV cache support (#19422)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`, `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedQKNormRopeOp.cpp` _+41 more__
- **2026-09-24** [`68702d59f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/68702d59f9) [#17365](https://github.com/NVIDIA/TensorRT-LLM/pull/17365)
  [https://nvbugs/6813351][fix] Revert "optimize qwen3.5 perf by removing gather and scatter op (#17365)" (#19578)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py`_
- **2026-09-23** [`3cfd52e4fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/3cfd52e4fe) [#19402](https://github.com/NVIDIA/TensorRT-LLM/pull/19402)
  [https://nvbugs/6771023][fix] Trace startup and warmup, allow 900s and unwaive Blackwell PP4 tests (#19402)
  _Files: `tensorrt_llm/_startup.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+11 more__
- **2026-09-23** [`e293b6ad4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e293b6ad4c) [#19423](https://github.com/NVIDIA/TensorRT-LLM/pull/19423)
  [None][perf] Extend MiniMax-M3 piecewise CUDA graphs coverage (#19423)
  _Files: `cpp/tensorrt_llm/thop/fusedQKNormRopeOp.cpp`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/compilation/multi_stream/auto_multi_stream.py`, `tensorrt_llm/_torch/compilation/remove_copy_pass.py` _+20 more__
- **2026-09-23** [`d79ecd55ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/d79ecd55ed) [#19582](https://github.com/NVIDIA/TensorRT-LLM/pull/19582)
  [None][fix] Fix DFlash budget test broken by CachedModelLoader signature change (#19582)
  _Files: `tests/unittest/_torch/speculative/hw_agnostic/test_dflash_config_budget.py`_
- **2026-09-23** [`3cfcb0d962`](https://github.com/NVIDIA/TensorRT-LLM/commit/3cfcb0d962) [#19353](https://github.com/NVIDIA/TensorRT-LLM/pull/19353)
  [None][fix] Refuse paged-context attention when no fused kernel exists (#19353)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tests/integration/defs/llmapi/test_llm_api_pytorch_t5.py` _+1 more__
- **2026-09-23** [`9926aaaf04`](https://github.com/NVIDIA/TensorRT-LLM/commit/9926aaaf04) [#18995](https://github.com/NVIDIA/TensorRT-LLM/pull/18995)
  [None][test] Add Helix zero-KV multi-GPU regression coverage (#18995)
  _Files: `cpp/tensorrt_llm/thop/alltoallOp.cpp`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml`, `tests/unittest/_torch/attention/kernels/parallel_hw_agnostic/test_helix_postprocess.py`, `tests/unittest/_torch/attention/multi_gpu/test_helix_zero_kv.py`_
- **2026-09-22** [`134fa245fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/134fa245fe) [#18478](https://github.com/NVIDIA/TensorRT-LLM/pull/18478)
  [None][feat] Rubin fp4 mla core (P1) (#18478)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/__init__.py`, `tensorrt_llm/_torch/attention/backends/fmha/fp4_mla.py`, `tensorrt_llm/_torch/attention/backends/fmha/interface.py` _+32 more__
- **2026-09-22** [`5ebed4692e`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ebed4692e) [#19466](https://github.com/NVIDIA/TensorRT-LLM/pull/19466)
  [None][fix] DFlash buffer sizing/position fixes and an accurate FlashInfer speculation gate (#19466)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tensorrt_llm/llmapi/llm_args.py` _+5 more__
- **2026-09-22** [`b67762f8bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/b67762f8bb) [#19082](https://github.com/NVIDIA/TensorRT-LLM/pull/19082)
  [None][perf] MLA context: fuse the Q FP8 quantization into the absorb bmm epilogue (CuTe-DSL BF16->FP8 bmm) + RoPE kOutputFp8Q (#19082)
  _Files: `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_gemm_persistent.py`, `tests/unittest/_torch/thop/parallel/test_cute_dsl_bf16_bmm_fp8out.py`_
- **2026-09-22** [`abc69b9c37`](https://github.com/NVIDIA/TensorRT-LLM/commit/abc69b9c37) [#19254](https://github.com/NVIDIA/TensorRT-LLM/pull/19254)
  [https://nvbugs/6758990][fix] Fix MPI flashinfer test failure (#19254)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/_flashinfer_workspace_probe.py`, `tests/unittest/llmapi/_run_mpi_comm_task.py`, `tests/unittest/llmapi/_test_remote_mpi_session.sh` _+1 more__
- **2026-09-22** [`45f2ef17ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/45f2ef17ac) [#19305](https://github.com/NVIDIA/TensorRT-LLM/pull/19305)
  [None][feat] NVFP4 MLA residual switch for DeepSeek-V4 (#19305)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/backend.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/compressor.py`_
- **2026-09-22** [`df08a02802`](https://github.com/NVIDIA/TensorRT-LLM/commit/df08a02802) [#19273](https://github.com/NVIDIA/TensorRT-LLM/pull/19273)
  [None][feat] Helix speculative verify groups: fp8 + fp4 MLA and DSpark (#19273)
  _Files: `cpp/tensorrt_llm/kernels/helixAllToAll.cu`, `cpp/tensorrt_llm/kernels/helixAllToAll.h`, `cpp/tensorrt_llm/kernels/mlaKernels.cu`, `cpp/tensorrt_llm/kernels/mlaKernels.h` _+32 more__
- **2026-09-21** [`0d52c6d296`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d52c6d296) [#19350](https://github.com/NVIDIA/TensorRT-LLM/pull/19350)
  [None][fix] Share speculative capture buffers across CUDA graph buckets (#19350)
  _Files: `tensorrt_llm/_torch/speculative/dflash.py`, `tensorrt_llm/_torch/speculative/dspark.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/speculative/hw_agnostic/test_capture_buffer.py` _+1 more__
- **2026-09-21** [`0d4304aab6`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d4304aab6) [#19493](https://github.com/NVIDIA/TensorRT-LLM/pull/19493)
  [None][fix] Regenerate LLM-args golden manifest for sparse_attention_config.uses_spcompress (#19493)
- **2026-09-21** [`129655ff56`](https://github.com/NVIDIA/TensorRT-LLM/commit/129655ff56) [#19040](https://github.com/NVIDIA/TensorRT-LLM/pull/19040)
  [TRTLLM-16564][feat] MLA-backboned standalone DSpark drafter (Inferact/Kimi-K3-DSpark) (#19040)
  _Files: `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/k3_dspark.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_kda_mtp_ops.py` _+27 more__
- **2026-09-21** [`fca831eac3`](https://github.com/NVIDIA/TensorRT-LLM/commit/fca831eac3) [#19269](https://github.com/NVIDIA/TensorRT-LLM/pull/19269)
  [TRTLLM-16466][fix] Profile cached KV chunks for dense MLA (#19269)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_estimation.py`_
- **2026-09-21** [`157d8692ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/157d8692ae) [#19352](https://github.com/NVIDIA/TensorRT-LLM/pull/19352)
  [None][fix] Warn when DFlash is used with disaggregated serving (#19352)
  _Files: `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-09-21** [`af7d8f8900`](https://github.com/NVIDIA/TensorRT-LLM/commit/af7d8f8900)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+12 more__
- **2026-09-21** [`1041b45f4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/1041b45f4f) [#19138](https://github.com/NVIDIA/TensorRT-LLM/pull/19138)
  [None][feat] enable the GVR Top-K and MTP draft-loop index reuse for the QSA indexer (#19138)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/params.py`, `tensorrt_llm/_torch/attention/backends/sparse/params.py` _+15 more__
- **2026-09-21** [`0921d98862`](https://github.com/NVIDIA/TensorRT-LLM/commit/0921d98862) [#19288](https://github.com/NVIDIA/TensorRT-LLM/pull/19288)
  [None][test] Cover MiniMax-M3 C++ NIXL bounce (#19288)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py` _+2 more__

## MoE  (20 commits)

- **2026-09-28** [`50e3b40aa1`](https://github.com/NVIDIA/TensorRT-LLM/commit/50e3b40aa1) [#17028](https://github.com/NVIDIA/TensorRT-LLM/pull/17028)
  [#17027][fix] Realign misaligned int32 index slices in FlashInfer GDN decode (#17028)
  _Files: `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_gdn_decode.py`_
- **2026-09-28** [`d21a8cebbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/d21a8cebbd) [#19136](https://github.com/NVIDIA/TensorRT-LLM/pull/19136)
  [None][feat] Add GLM-5.3-Flash (glm5_next) support (#19136)
  _Files: `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.h`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeLegacy.cu`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeOptimized.cu`, `cpp/tensorrt_llm/thop/kdaDecodeOp.cpp` _+55 more__
- **2026-09-27** [`052b1158f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/052b1158f2) [#19628](https://github.com/NVIDIA/TensorRT-LLM/pull/19628)
  [https://nvbugs/6801229][fix] Fix Rubin CuTe DSL MoE unit tests (#19628)
  _Files: `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`_
- **2026-09-26** [`923c24fdd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/923c24fdd0) [#19558](https://github.com/NVIDIA/TensorRT-LLM/pull/19558)
  [None][fix] Fix quantized MTP head loading for Nemotron H (#19558)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_nemotron_h_moe_quant.py`_
- **2026-09-23** [`e6c30cc7a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6c30cc7a3) [#19361](https://github.com/NVIDIA/TensorRT-LLM/pull/19361)
  [None][fix] Add SM107 (Rubin) to SM100-family support statements; gate W4A8 NVFP4 FP8 MoE to SM100/103 (#19361)
  _Files: `cpp/tensorrt_llm/cutlass_extensions/include/cutlass_extensions/gemm_configs.h`, `cpp/tensorrt_llm/kernels/communicationKernels/allReduceFusionKernels.cu`, `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.h` _+22 more__
- **2026-09-23** [`a6f4151497`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6f4151497) [#19312](https://github.com/NVIDIA/TensorRT-LLM/pull/19312)
  [None][fix] Keep one-sided MoE combine workspace offset stable (#19312)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/communication/nvlink_one_sided.py`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus.yml`, `tests/unittest/_torch/moe/multi_gpu/test_moe_a2a_workspace.py`, `tests/unittest/_torch/moe/test_moe_a2a_workspace.py`_
- **2026-09-23** [`c3785d305f`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3785d305f) [#18999](https://github.com/NVIDIA/TensorRT-LLM/pull/18999)
  [None][perf] Triton top-k combine for Marlin NVFP4 MoE (#18999)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_marlin.py`, `tensorrt_llm/_torch/moe/fused_moe/marlin/base.py`, `tests/integration/test_lists/test-db/l0_l40s.yml`, `tests/unittest/_torch/moe/test_marlin_triton_sum_topk.py`_
- **2026-09-22** [`1a36f4fed9`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a36f4fed9) [#19376](https://github.com/NVIDIA/TensorRT-LLM/pull/19376)
  [None][perf] Enable flashinfer gdn prefill on sm120/121 (#19376)
  _Files: `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_utils.py`, `tests/integration/test_lists/test-db/l0_gb10.yml` _+3 more__
- **2026-09-22** [`89e2cf0f20`](https://github.com/NVIDIA/TensorRT-LLM/commit/89e2cf0f20) [#19425](https://github.com/NVIDIA/TensorRT-LLM/pull/19425)
  [None][perf] Publish MoE all-to-all counters before the dispatch data issue (#19425)
  _Files: `cpp/tensorrt_llm/kernels/moe/communication/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/moe/communication/moeAlltoAllKernels.h`, `tensorrt_llm/_torch/moe/fused_moe/communication/moe_alltoall.py`, `tensorrt_llm/_torch/moe/fused_moe/communication/nvlink_one_sided.py` _+1 more__
- **2026-09-22** [`c71d6807f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c71d6807f7) [#19512](https://github.com/NVIDIA/TensorRT-LLM/pull/19512)
  [https://nvbugs/6812347][fix] Do not pass expert-count args to the Rubin MoE finalize op (#19512)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`_
- **2026-09-22** [`9cb75f9dc3`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cb75f9dc3) [#19509](https://github.com/NVIDIA/TensorRT-LLM/pull/19509)
  [None][fix] Give test_mnnvl_memory an expert-parallel mapping and assert its checks (#19509)
  _Files: `tests/unittest/_torch/multi_gpu/test_mnnvl_memory.py`_
- **2026-09-22** [`ec5ff4f997`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec5ff4f997) [#19251](https://github.com/NVIDIA/TensorRT-LLM/pull/19251)
  [None][fix] size FP4 block-scale MoE permute buffers from local_num_experts (#19251)
  _Files: `cpp/tensorrt_llm/kernels/moe/trtllmGen/routing/RoutingLlama4.cu`, `cpp/tensorrt_llm/thop/moe/trtllmGen/fp4BlockScaleMoe.cpp`, `cpp/tests/unit_tests/kernels/moe/blockScaleMoeActivationTest.cu`, `cpp/tests/unit_tests/kernels/moe/routing/routingLlama4Test.cpp`_
- **2026-09-22** [`6752b2a326`](https://github.com/NVIDIA/TensorRT-LLM/commit/6752b2a326) [#19244](https://github.com/NVIDIA/TensorRT-LLM/pull/19244)
  [None][doc] GVR V2: Self-Sampling and Multi-Thresholding for Faster Exact Top-K (#19244)
  _Files: `docs/source/blogs/media/gvr_v2/README.md`, `docs/source/blogs/media/gvr_v2/algorithm.svg`, `docs/source/blogs/media/gvr_v2/candidate_work.svg`, `docs/source/blogs/media/gvr_v2/evolution.svg` _+17 more__
- **2026-09-22** [`22eea2948d`](https://github.com/NVIDIA/TensorRT-LLM/commit/22eea2948d) [#19216](https://github.com/NVIDIA/TensorRT-LLM/pull/19216)
  [TRTLLM-16394][refactor] Consolidate and group the cpp MoE torch ops under thop/moe/ (#19216)
  _Files: `.claude/skills/perf-optimization-casebook/references/communication/low-precision-dispatch.md`, `.claude/skills/perf-optimization-casebook/references/kernel-and-fusion/fold-scale-swizzle-into-kernel.md`, `.claude/skills/perf-optimization-casebook/references/kernel-and-fusion/hw-matched-lowprec-moe-gemm.md`, `.claude/skills/perf-optimization-casebook/references/kernel-and-fusion/trtllm-gen-fp4-moe-backend.md` _+22 more__
- **2026-09-22** [`f864910fc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/f864910fc8) [#19249](https://github.com/NVIDIA/TensorRT-LLM/pull/19249)
  [TRTLLMINF-440][infra] Upgrade C++ from 17 to 20 (#19249)
  _Files: `3rdparty/CMakeLists.txt`, `3rdparty/fetch_content.json`, `3rdparty/patches/xgrammar_constexpr.patch`, `3rdparty/patches/xgrammar_cxx20.patch` _+74 more__
- **2026-09-22** [`f1afa79d0b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1afa79d0b) [#19523](https://github.com/NVIDIA/TensorRT-LLM/pull/19523)
  [https://nvbugs/6758594][test] Remove stale GB200 waiver for MoE LoRA varying-ranks test (#19523)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`478218a462`](https://github.com/NVIDIA/TensorRT-LLM/commit/478218a462) [#19091](https://github.com/NVIDIA/TensorRT-LLM/pull/19091)
  [https://nvbugs/6708299][fix] Support group_size=32 for W4A16_NVFP4 and validate NVFP4 group sizes (#19091)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/modules/linear.py` _+10 more__
- **2026-09-21** [`77628ee848`](https://github.com/NVIDIA/TensorRT-LLM/commit/77628ee848) [#19003](https://github.com/NVIDIA/TensorRT-LLM/pull/19003)
  [None][feat] Kimi K3: unlock the CUTEDSL MoE backend for NVFP4 SiTU (#19003)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py` _+4 more__
- **2026-09-21** [`db98912686`](https://github.com/NVIDIA/TensorRT-LLM/commit/db98912686) [#19323](https://github.com/NVIDIA/TensorRT-LLM/pull/19323)
  [None][feat] Support the MegaMoE CuteDSL MoE backend for Qwen3.8-Flash-Next (#19323)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_gb300.yml` _+1 more__
- **2026-09-21** [`5982425ca8`](https://github.com/NVIDIA/TensorRT-LLM/commit/5982425ca8) [#18397](https://github.com/NVIDIA/TensorRT-LLM/pull/18397)
  [None][feat] Router Replay (R3): return per-token MoE routing to training engine in post train. (#18397)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/moe_scheduler.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+15 more__

## Disaggregation / KV  (14 commits)

- **2026-09-27** [`e0448239a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0448239a5) [#19427](https://github.com/NVIDIA/TensorRT-LLM/pull/19427)
  [https://nvbugs/6786712][fix] Re-landed the previously-verified 3-defect payload tree-identically… (#19427)
  _Files: `tensorrt_llm/serve/cluster_storage.py`, `tensorrt_llm/serve/disagg_auto_scaling.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/disaggregated/test_cluster_storage.py` _+2 more__
- **2026-09-24** [`e7eb2de0e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7eb2de0e1) [#19055](https://github.com/NVIDIA/TensorRT-LLM/pull/19055)
  [None][fix] Update Scaffolding MCP transport and KV cache truncation (#19055)
  _Files: `examples/scaffolding/benchmarks/README.md`, `examples/scaffolding/benchmarks/__main__.py`, `examples/scaffolding/benchmarks/agent_benchmark.py`, `examples/scaffolding/benchmarks/coder_benchmark.py` _+40 more__
- **2026-09-23** [`f5ca10543f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5ca10543f) [#19175](https://github.com/NVIDIA/TensorRT-LLM/pull/19175)
  [TRTLLM-16022][fix] Authenticate disaggregated subagent affinity (#19175)
  _Files: `docs/source/features/subagent-routing.md`, `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/serve/disagg_auth.py`, `tensorrt_llm/serve/openai_client.py` _+5 more__
- **2026-09-23** [`d857367593`](https://github.com/NVIDIA/TensorRT-LLM/commit/d857367593) [#19544](https://github.com/NVIDIA/TensorRT-LLM/pull/19544)
  [https://nvbugs/6812588][fix] Stop unbindable IPv6 addresses from reaching disaggregated listeners (#19544)
  _Files: `cpp/tensorrt_llm/common/ipUtils.cpp`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/coordinator_server.py`, `tests/unittest/bindings/test_transfer_agent_bindings.py` _+1 more__
- **2026-09-23** [`58c8164343`](https://github.com/NVIDIA/TensorRT-LLM/commit/58c8164343) [#19444](https://github.com/NVIDIA/TensorRT-LLM/pull/19444)
  [None][fix] Synchronize disaggregated KV receive destinations (#19444)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/executor/test_disagg_receive_ordering.py`_
- **2026-09-22** [`6c33671817`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c33671817) [#19478](https://github.com/NVIDIA/TensorRT-LLM/pull/19478)
  [TRTLLM-15718][test] Add disagg closure tests, demote one E2E to post-merge and replace another with CPU/1-GPU tests (#19478)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_python_transceiver_host_offload.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_a10.yml` _+13 more__
- **2026-09-22** [`67a0328029`](https://github.com/NVIDIA/TensorRT-LLM/commit/67a0328029) [#19480](https://github.com/NVIDIA/TensorRT-LLM/pull/19480)
  [None][fix] fix _CacheReuseAdapterV1 (#19480)
  _Files: `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py`, `tests/unittest/disaggregated/test_cache_reuse_adapter.py`, `tests/unittest/disaggregated/test_kv_transfer.py`_
- **2026-09-22** [`8a06e8e5f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a06e8e5f8) [#19399](https://github.com/NVIDIA/TensorRT-LLM/pull/19399)
  [None][fix] make disagg load balancing router global (#19399)
  _Files: `docs/source/features/disagg-serving.md`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/coordinator_server.py`, `tensorrt_llm/serve/disagg_coordinator.py` _+6 more__
- **2026-09-22** [`83624baf69`](https://github.com/NVIDIA/TensorRT-LLM/commit/83624baf69) [#19424](https://github.com/NVIDIA/TensorRT-LLM/pull/19424)
  [None][test] Disable ctx overlap scheduler for deepseek-v4-pro con8 disagg config (#19424)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v4-pro-fp4_8k1k_con8_ctx1_dep4_gen4_tep8_eplb0_mtp3_ccb-NIXL.yaml`_
- **2026-09-21** [`89429bc9db`](https://github.com/NVIDIA/TensorRT-LLM/commit/89429bc9db) [#19366](https://github.com/NVIDIA/TensorRT-LLM/pull/19366)
  [None][perf] Avoid prefix probes when the KV cache v2 context chunk budget is insufficient (#19366)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_v2_scheduler.py`_
- **2026-09-21** [`b8e337d939`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8e337d939) [#19389](https://github.com/NVIDIA/TensorRT-LLM/pull/19389)
  [https://nvbugs/6758573][test] Unwaive test_disaggregated_python_transceiver_host_offload on A100 (#19389)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`f69c0c59c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/f69c0c59c7) [#19413](https://github.com/NVIDIA/TensorRT-LLM/pull/19413)
  [https://nvbugs/6759021][test] Re-enable disagg single-GPU tests for the MPI orchestrator (#19413)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated_single_gpu.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`9e1d3be303`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e1d3be303) [#18939](https://github.com/NVIDIA/TensorRT-LLM/pull/18939)
  [TRTLLM-13662][feat] transceiver enhancement (#18939)
  _Files: `tensorrt_llm/_torch/disaggregation/base/backend.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py` _+7 more__
- **2026-09-21** [`5399d4e4f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/5399d4e4f4) [#19398](https://github.com/NVIDIA/TensorRT-LLM/pull/19398)
  [https://nvbugs/6603467][test] Cap hybrid-model test batch sizes at 256 (#19398)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Executor / Runtime  (13 commits)

- **2026-09-28** [`a4f358a3a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4f358a3a1) [#17974](https://github.com/NVIDIA/TensorRT-LLM/pull/17974)
  [TRTLLM-12891][feat] Include KV connector prefixes in V2 scheduler budgeting (#17974)
  _Files: `docs/source/features/kv-cache-connector.md`, `examples/llm-api/llm_kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/prefix_load_completion.py` _+15 more__
- **2026-09-23** [`4871aae113`](https://github.com/NVIDIA/TensorRT-LLM/commit/4871aae113) [#18231](https://github.com/NVIDIA/TensorRT-LLM/pull/18231)
  [None][feat] Add support for mnnvl allreduce under ray orchestrator (#18231)
  _Files: `cpp/include/tensorrt_llm/runtime/ipcNvlsMemory.h`, `cpp/include/tensorrt_llm/runtime/mcastGroupComm.h`, `cpp/tensorrt_llm/nanobind/bindings.cpp`, `cpp/tensorrt_llm/nanobind/runtime/bindings.cpp` _+16 more__
- **2026-09-23** [`950c9236c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/950c9236c5) [#19428](https://github.com/NVIDIA/TensorRT-LLM/pull/19428)
  [TRTLLM-16614][chore] Remove more TRT leftovers (#19428)
  _Files: `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/llmapi/llm_utils.py`, `tensorrt_llm/llmapi/mm_encoder.py`, `tensorrt_llm/llmapi/serialization.py` _+2 more__
- **2026-09-23** [`c12c8ea173`](https://github.com/NVIDIA/TensorRT-LLM/commit/c12c8ea173) [#19559](https://github.com/NVIDIA/TensorRT-LLM/pull/19559)
  [None][fix] Guard model_engine access in PyExecutor._handle_responses (#19559)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-09-22** [`f11deff5b3`](https://github.com/NVIDIA/TensorRT-LLM/commit/f11deff5b3) [#19375](https://github.com/NVIDIA/TensorRT-LLM/pull/19375)
  [None][feat] Add opt-in per-request cached KV token logging (#19375)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`_
- **2026-09-22** [`1b61546d27`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b61546d27) [#19496](https://github.com/NVIDIA/TensorRT-LLM/pull/19496)
  [#19485][bugfix] Prevent OOB index in vanilla top-p sampling (#19496)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-09-22** [`cb3fa77647`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb3fa77647) [#16323](https://github.com/NVIDIA/TensorRT-LLM/pull/16323)
  [None][chore] Add per-rank routing/scheduling observability to the iteration log (#16323)
  _Files: `tensorrt_llm/_torch/pyexecutor/profiling.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-09-22** [`02e93994be`](https://github.com/NVIDIA/TensorRT-LLM/commit/02e93994be) [#19533](https://github.com/NVIDIA/TensorRT-LLM/pull/19533)
  [None][ci] Replace blanket unittest/_torch/executor waive with per-test waives (#19533)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`2c8f4660cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c8f4660cc) [#19459](https://github.com/NVIDIA/TensorRT-LLM/pull/19459)
  [None][feat] OpenAI protocol: cap tool enum values and accept parallel_tool_calls (#19459)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/unittest/api_stability/references/trtllm_serve_api.yaml`, `tests/unittest/llmapi/apps/test_openai_protocol_parallel_tool_calls.py`, `tests/unittest/llmapi/apps/test_openai_protocol_tools.py`_
- **2026-09-22** [`0177d83c48`](https://github.com/NVIDIA/TensorRT-LLM/commit/0177d83c48) [#19407](https://github.com/NVIDIA/TensorRT-LLM/pull/19407)
  [#19337][fix] Correct VBWS width tracking and terminal-step finalization (#19407)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tests/unittest/_torch/sampler/test_beam_search.py`_
- **2026-09-22** [`c56d0a54ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/c56d0a54ad) [#19045](https://github.com/NVIDIA/TensorRT-LLM/pull/19045)
  [https://nvbugs/6607482][logging] Add quiet PyExecutor hang diagnostics (#19045)
  _Files: `docs/source/developer-guide/overview.md`, `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tensorrt_llm/_torch/pyexecutor/hang_diagnostics.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+9 more__
- **2026-09-21** [`575f4f9fcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/575f4f9fcf) [#19454](https://github.com/NVIDIA/TensorRT-LLM/pull/19454)
  [None][fix] Responses API: treat explicit null as unset for optional fields (#19454)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/unittest/llmapi/apps/test_responses_input_preprocess.py`_
- **2026-09-21** [`e6b2e73f76`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6b2e73f76) [#18902](https://github.com/NVIDIA/TensorRT-LLM/pull/18902)
  [None][chore] BREAKING: Remove unused code from LlmRequest (#18902)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `cpp/tensorrt_llm/executor/request.cpp` _+19 more__

## Other  (9 commits)

- **2026-09-28** [`ca937c9501`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca937c9501) [#19651](https://github.com/NVIDIA/TensorRT-LLM/pull/19651)
  [None][fix] Require integration evidence in semantic review prompts (#19651)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_cases.js`, `.github/semantic-review-prompt.md` _+1 more__
- **2026-09-28** [`cc608b774a`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc608b774a) [#19649](https://github.com/NVIDIA/TensorRT-LLM/pull/19649)
  [None][fix] Publish semantic reviews with per-PR commit statuses (#19649)
  _Files: `.github/scripts/semantic_review.js`, `.github/scripts/semantic_review.test.js`, `.github/scripts/semantic_review_request.js`, `.github/scripts/semantic_review_request.test.js` _+2 more__
- **2026-09-28** [`a66196b125`](https://github.com/NVIDIA/TensorRT-LLM/commit/a66196b125) [#19577](https://github.com/NVIDIA/TensorRT-LLM/pull/19577)
  [None][fix] Make integrator gain gate authoritative (#19577)
  _Files: `agent-flow/agent_flow/workflows/perf_optimize/progress.py`, `agent-flow/agent_flow/workflows/perf_optimize/workflow.py`, `agent-flow/tests/workflows/perf_optimize/test_progress.py`, `agent-flow/tests/workflows/perf_optimize/test_workflow.py`_
- **2026-09-27** [`83aed1a7ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/83aed1a7ab) [#19056](https://github.com/NVIDIA/TensorRT-LLM/pull/19056)
  [TRTLLM-16304][feat] In-tree implementation of staircase (#19056)
- **2026-09-24** [`8be31b0c99`](https://github.com/NVIDIA/TensorRT-LLM/commit/8be31b0c99) [#17745](https://github.com/NVIDIA/TensorRT-LLM/pull/17745)
  [#17743][fix] Key the legacy lint baseline on POSIX paths (#17745)
  _Files: `scripts/legacy_utils.py`_
- **2026-09-24** [`14729d4a3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/14729d4a3a) [#19599](https://github.com/NVIDIA/TensorRT-LLM/pull/19599)
  [None][chore] update telemetry codeowners (#19599)
  _Files: `.github/CODEOWNERS`_
- **2026-09-21** [`a5df5074dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/a5df5074dd) [#19458](https://github.com/NVIDIA/TensorRT-LLM/pull/19458)
  [None][fix] Validate media data-URIs and gate private-URL fetches behind an opt-in (#19458)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tests/unittest/inputs/test_async_media_loading.py`, `tests/unittest/inputs/test_url_validation.py`_
- **2026-09-21** [`e1deeff3a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1deeff3a5) [#19339](https://github.com/NVIDIA/TensorRT-LLM/pull/19339)
  [None][fix] Reconfigure cmake when build_wheel.py arguments change (#19339)
  _Files: `scripts/build_wheel.py`, `tests/unittest/others/test_build_wheel_reconfigure.py`_
- **2026-09-21** [`c5e250a009`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5e250a009) [#19419](https://github.com/NVIDIA/TensorRT-LLM/pull/19419)
  [None][doc] Keep change rationale in the PR description, not code comments (#19419)
  _Files: `AGENTS.md`_

## Torch Path (_torch)  (9 commits)

- **2026-09-28** [`0c58480ca6`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c58480ca6) [#19019](https://github.com/NVIDIA/TensorRT-LLM/pull/19019)
  [None][doc] Update the docs for the NGC PyTorch 26.08 and torch 2.14.0 upgrades (#19019)
  _Files: `README.md`, `docs/source/installation/installation-guide.md`_
- **2026-09-27** [`9bf6b8b9da`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bf6b8b9da) [#18539](https://github.com/NVIDIA/TensorRT-LLM/pull/18539)
  [TRTLLM-11412][fix] Preserve dense tensor layouts during offloading (#18539)
  _Files: `tensorrt_llm/_torch/visual_gen/offloading.py`, `tests/unittest/_torch/visual_gen/test_offloading.py`_
- **2026-09-24** [`c76f4a8564`](https://github.com/NVIDIA/TensorRT-LLM/commit/c76f4a8564) [#19532](https://github.com/NVIDIA/TensorRT-LLM/pull/19532)
  [None][fix] Compute the Cosmos3 rotary table with a broadcast multiply, not a K=1 matmul (#19532)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_transformer.py`_
- **2026-09-23** [`c61417cac2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c61417cac2) [#19554](https://github.com/NVIDIA/TensorRT-LLM/pull/19554)
  [https://nvbugs/6737124][fix] Get rid of incorrect assertion for DSv4 E2E test (#19554)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`afb6d11649`](https://github.com/NVIDIA/TensorRT-LLM/commit/afb6d11649) [#19101](https://github.com/NVIDIA/TensorRT-LLM/pull/19101)
  [https://nvbugs/6732110][fix] Cache the split communicator in a new `MNNVLAllReduce.allreduce_mnnvl_pending_c… (#19101)
  _Files: `tensorrt_llm/_torch/distributed/ops.py`, `tests/unittest/_torch/distributed/test_mnnvl_allreduce_lifecycle.py`_
- **2026-09-22** [`f3b7eb6e48`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3b7eb6e48) [#19446](https://github.com/NVIDIA/TensorRT-LLM/pull/19446)
  [None][perf] PDL on the missing decode edges (#19446)
  _Files: `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/minimaxM3SelectBlocks.cu`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/minimax_m3_index_decode_score.py`_
- **2026-09-21** [`2480b57f94`](https://github.com/NVIDIA/TensorRT-LLM/commit/2480b57f94) [#19476](https://github.com/NVIDIA/TensorRT-LLM/pull/19476)
  [None][chore] Remove the duplicate Rubin fused FC12 op registration (#19476)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`_
- **2026-09-21** [`25ea5ff833`](https://github.com/NVIDIA/TensorRT-LLM/commit/25ea5ff833) [#19142](https://github.com/NVIDIA/TensorRT-LLM/pull/19142)
  [None][fix] Reject unsupported SM100 sync-object factories (#19142)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/custom_pipeline.py`, `tests/unittest/_torch/cute_dsl_kernels/test_custom_pipeline.py`_
- **2026-09-21** [`79af2e7c97`](https://github.com/NVIDIA/TensorRT-LLM/commit/79af2e7c97) [#19256](https://github.com/NVIDIA/TensorRT-LLM/pull/19256)
  [None][test] Add coverage for WhisperForConditionalGeneration (#19256)
  _Files: `tests/unittest/_torch/modeling/test_modeling_whisper.py`_

## Quantization  (8 commits)

- **2026-09-28** [`c2220eef33`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2220eef33)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__
- **2026-09-27** [`1585f453e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/1585f453e9)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__
- **2026-09-26** [`735c55482f`](https://github.com/NVIDIA/TensorRT-LLM/commit/735c55482f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+5 more__
- **2026-09-24** [`0f0f281e61`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f0f281e61)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-09-23** [`ef9a3340a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef9a3340a3) [#19519](https://github.com/NVIDIA/TensorRT-LLM/pull/19519)
  [https://nvbugs/6771102][fix] Support Qwen3.5 global FP8 checkpoints (#19519)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tests/unittest/_torch/models/checkpoints/hf/test_qwen3_5_weight_mapper.py`_
- **2026-09-22** [`59f5c47f2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/59f5c47f2e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+7 more__
- **2026-09-21** [`bfae45d6d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfae45d6d7) [#18906](https://github.com/NVIDIA/TensorRT-LLM/pull/18906)
  [None][perf] defer dynamic NVFP4 scale finalization for fused GELU MLPs (#18906)
  _Files: `tensorrt_llm/_torch/custom_ops/__init__.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/nvfp4_sfc_finalize.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_blockscaled_gemm_act_fusion.py` _+5 more__
- **2026-09-21** [`dbf9ceb2a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbf9ceb2a5) [#19344](https://github.com/NVIDIA/TensorRT-LLM/pull/19344)
  [None][fix] Use bounded NVFP4 serving configs for MiniMax-M3 perf tests (#19344)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Speculative Decoding  (7 commits)

- **2026-09-27** [`c47ffb6aa0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c47ffb6aa0) [#19513](https://github.com/NVIDIA/TensorRT-LLM/pull/19513)
  [None][chore] Remove dead code in model engine (#19513)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/engine/metadata.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/encoder.py` _+17 more__
- **2026-09-26** [`b88149e535`](https://github.com/NVIDIA/TensorRT-LLM/commit/b88149e535) [#19601](https://github.com/NVIDIA/TensorRT-LLM/pull/19601)
  [TRTLLM-16625][fix] Fix seeded request reproducibility on spec dec (#19601)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_rng_window_counter.py`_
- **2026-09-22** [`8a7239a151`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a7239a151) [#19455](https://github.com/NVIDIA/TensorRT-LLM/pull/19455)
  [None][fix] Drain guided-decoder host functions before GIL-holding forward calls (#19455)
  _Files: `tensorrt_llm/_torch/pyexecutor/guided_decoder.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_guided_hostfunc_drain.py`_
- **2026-09-22** [`ca3c570f22`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca3c570f22) [#19505](https://github.com/NVIDIA/TensorRT-LLM/pull/19505)
  [#19487][fix] Fix CUDA graph spec dec RNG corner case (#19505)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_rng_window_counter.py`_
- **2026-09-22** [`3b3cbc436f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b3cbc436f) [#19531](https://github.com/NVIDIA/TensorRT-LLM/pull/19531)
  [https://nvbugs/6813629][fix] Fix GPT-OSS Eagle3 disaggregated test configuration (#19531)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`9bce93c0a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bce93c0a4) [#19176](https://github.com/NVIDIA/TensorRT-LLM/pull/19176)
  [TRTLLM-16398] [test] Add disaggregated speculative decoding acceptance-length baselines (#19176)
  _Files: `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`_
- **2026-09-21** [`24c76d7a23`](https://github.com/NVIDIA/TensorRT-LLM/commit/24c76d7a23) [#18654](https://github.com/NVIDIA/TensorRT-LLM/pull/18654)
  [None][test] Prune Llama-3.1 8b model from tests (#18654)
  _Files: `tests/integration/defs/conftest.py`, `tests/integration/defs/disaggregated/test_ad_disagg.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_qwen3_8b.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+22 more__

## Models  (7 commits)

- **2026-09-23** [`b911586671`](https://github.com/NVIDIA/TensorRT-LLM/commit/b911586671) [#19571](https://github.com/NVIDIA/TensorRT-LLM/pull/19571)
  [None][models] Avoid GEMM in Gemma4 vision RoPE (#19571)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4_vision.py`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-09-23** [`260c0de1a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/260c0de1a3) [#19530](https://github.com/NVIDIA/TensorRT-LLM/pull/19530)
  [None][test] expand Qwen3.8 test GPU coverage (#19530)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-09-22** [`88c90abee1`](https://github.com/NVIDIA/TensorRT-LLM/commit/88c90abee1) [#18571](https://github.com/NVIDIA/TensorRT-LLM/pull/18571)
  [https://nvbugs/6705034][fix] Route zero-token causal-conv input to the channel-major kernel (#18571)
  _Files: `cpp/tensorrt_llm/thop/causalConv1dOp.cpp`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/kimi_kda/test_kda_prefill_op.py`_
- **2026-09-22** [`cba917db4b`](https://github.com/NVIDIA/TensorRT-LLM/commit/cba917db4b) [#18938](https://github.com/NVIDIA/TensorRT-LLM/pull/18938)
  [TRTLLM-15899][feat] Add new KDA decode non-mtp kernel and dispatch logic (#18938)
  _Files: `cpp/tensorrt_llm/kernels/kdaDecode/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.h`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeDispatcher.cpp`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecodeInternal.h` _+8 more__
- **2026-09-22** [`f7aeaef163`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7aeaef163) [#19470](https://github.com/NVIDIA/TensorRT-LLM/pull/19470)
  [https://nvbugs/6649739][fix] Skip deprecated GPT-OSS Hopper tests and remove stale waivers (#19470)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-22** [`c51cda2e06`](https://github.com/NVIDIA/TensorRT-LLM/commit/c51cda2e06) [#19520](https://github.com/NVIDIA/TensorRT-LLM/pull/19520)
  [https://nvbugs/6626640][test] Remove GPT-OSS RTX PRO 6000 waiver (#19520)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-21** [`a7eae4beee`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7eae4beee) [#19332](https://github.com/NVIDIA/TensorRT-LLM/pull/19332)
  [None][test] Add coverage for DeepseekV32ForCausalLM (#19332)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_deepseekv32.py`_

## Docs / Examples  (4 commits)

- **2026-09-23** [`bc38304d3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc38304d3d)
  [None][chore] Bump version to 1.3.0rc29
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-09-22** [`ef34db4709`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef34db4709) [#19421](https://github.com/NVIDIA/TensorRT-LLM/pull/19421)
  [None][build] remove obsolete cpp_only build option (#19421)
  _Files: `docs/source/installation/build-from-source.md`, `scripts/build_wheel.py`_
- **2026-09-22** [`b02dd150d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/b02dd150d3) [#19433](https://github.com/NVIDIA/TensorRT-LLM/pull/19433)
  [https://nvbugs/6777522][test] Guard VisualGen ffmpeg apt install with timeout and retry (#19433)
  _Files: `tests/integration/defs/examples/visual_gen/conftest.py`, `tests/integration/defs/examples/visual_gen/test_media_deps_install.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`_
- **2026-09-21** [`473fd7195f`](https://github.com/NVIDIA/TensorRT-LLM/commit/473fd7195f) [#19236](https://github.com/NVIDIA/TensorRT-LLM/pull/19236)
  [None][feat] agent-flow: backend-independent tools and required-tool policy (#19236)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/__init__.py`, `agent-flow/agent_flow/backends/claude_code.py`, `agent-flow/agent_flow/backends/codex.py` _+34 more__

## ROCm / AMD  (2 commits)

- **2026-09-24** [`4eee1fb1cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/4eee1fb1cb) [#19377](https://github.com/NVIDIA/TensorRT-LLM/pull/19377)
  [None][fix] Preserve KV transfer outcomes independently of polling (#19377)
  _Files: `tensorrt_llm/_torch/disaggregation/base/backend.py`, `tensorrt_llm/_torch/disaggregation/native/handle.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_peer_fetch.py` _+3 more__
- **2026-09-23** [`adea5c0720`](https://github.com/NVIDIA/TensorRT-LLM/commit/adea5c0720) [#19477](https://github.com/NVIDIA/TensorRT-LLM/pull/19477)
  [TRTLLMINF-391][infra] Upgrade public PyTorch to 2.14 and integrate Triton 3.8 (#19477)
  _Files: `3rdparty/CMakeLists.txt`, `ATTRIBUTIONS-Python.md`, `cpp/CMakeLists.txt`, `docker/common/install_pytorch.sh` _+56 more__

## AutoDeploy  (2 commits)

- **2026-09-24** [`3195913ffd`](https://github.com/NVIDIA/TensorRT-LLM/commit/3195913ffd) [#19028](https://github.com/NVIDIA/TensorRT-LLM/pull/19028)
  [None][chore] BREAKING: Remove AutoDeploy from TensorRT-LLM (#19028)
- **2026-09-23** [`f77d710bab`](https://github.com/NVIDIA/TensorRT-LLM/commit/f77d710bab)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/pyproject.toml` _+5 more__

## LoRA  (1 commits)

- **2026-09-22** [`c7b96cda9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7b96cda9b) [#19151](https://github.com/NVIDIA/TensorRT-LLM/pull/19151)
  [TRTLLM-15820][feat] Expose Nemotron-H VL LoRA configuration hook (#19151)
  _Files: `examples/llm-api/quickstart_multimodal.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py`, `tests/unittest/_torch/modules/tests_lora_modules/nemotron_h_lora_utils.py`, `tests/unittest/_torch/modules/tests_lora_modules/test_nemotron35_vl_lora_adapter.py` _+1 more__

## Compilation / Graph  (1 commits)

- **2026-09-21** [`611263e2fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/611263e2fc) [#19449](https://github.com/NVIDIA/TensorRT-LLM/pull/19449)
  [https://nvbugs/6786567][chore] Remove waiver for SM103 GVR CUDA graph test (#19449)
  _Files: `tests/integration/test_lists/waives.txt`_

---
_Generated 2026-09-28 16:48 UTC_