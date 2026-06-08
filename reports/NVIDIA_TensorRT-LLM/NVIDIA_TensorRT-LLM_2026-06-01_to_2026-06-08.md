# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-06-01 → 2026-06-08  |  **Total commits:** 155

## ✨ New Features This Week

- **2026-06-08** [#14845](https://github.com/NVIDIA/TensorRT-LLM/pull/14845) — [None][feat] Enable disk cache config for KV cache v2 (#14845)
- **2026-06-08** [#15038](https://github.com/NVIDIA/TensorRT-LLM/pull/15038) — [TRTLLM-13262][ci] Move non-default-feature tests to post merge (#15038)
- **2026-06-08** [#14835](https://github.com/NVIDIA/TensorRT-LLM/pull/14835) — [None][feat] AutoDeploy: propagate layer_type hint across pattern-matcher rewrites (#14835)
- **2026-06-08** [#14923](https://github.com/NVIDIA/TensorRT-LLM/pull/14923) — [TRTLLM-12507][feat] Cudagraph support for routed-expert MoE LoRA with Cutlass backend - Part 1 (#14923)
- **2026-06-08** [#15015](https://github.com/NVIDIA/TensorRT-LLM/pull/15015) — [TRTLLM-12648][test] implement disagg cancellation canary thread (#15015)
- **2026-06-07** [#14812](https://github.com/NVIDIA/TensorRT-LLM/pull/14812) — [#10710][feat] Make explicit CLI flags take precedence over --config / --extra_llm_api_options YAML (#14812)
- **2026-06-07** [#14964](https://github.com/NVIDIA/TensorRT-LLM/pull/14964) — [TRTLLM-13177][doc] Add Nemotron 3 Ultra doc (#14964)
- **2026-06-07** [#13723](https://github.com/NVIDIA/TensorRT-LLM/pull/13723) — [#13718][feat] AutoDeploy MoE all-to-all: cache + runtime max-tokens (#13723)
- **2026-06-06** [#14976](https://github.com/NVIDIA/TensorRT-LLM/pull/14976) — [None][feat] Add LTX-2 visual generation example (#14976)
- **2026-06-06** [#13148](https://github.com/NVIDIA/TensorRT-LLM/pull/13148) — [None][feat] Afmoe trinity support (#13148)
- _…and 29 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-06-05 |
| [#13318](https://github.com/NVIDIA/TensorRT-LLM/issues/13318) | [Bug]: Scheduler deadlock on main + #12976 + #13029: AssertionError to | bug, KV-Cache Management, Pytorch | 2026-06-04 |
| [#14826](https://github.com/NVIDIA/TensorRT-LLM/issues/14826) | [Bug]: Using the official tensorrt llm whisper conversion script does  | bug, Triton backend | 2026-06-03 |
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-26 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |
| [#14100](https://github.com/NVIDIA/TensorRT-LLM/issues/14100) | [Bug] trtllm-serve /v1/chat/completions: audio_url with data: URI base | bug, Multimodal | 2026-05-14 |
| [#10663](https://github.com/NVIDIA/TensorRT-LLM/issues/10663) | [Bug]: Exceptions in PyTorch workflow worker processes lead to hanging | bug, Investigating, Speculative Decoding, Pytorch | 2026-05-13 |
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
| CI / Infra | 37 |
| Executor / Runtime | 19 |
| MoE | 19 |
| Attention | 18 |
| Other | 11 |
| Quantization | 10 |
| Models | 9 |
| Disaggregation / KV | 8 |
| Torch Path (_torch) | 8 |
| Docs / Examples | 6 |
| AutoDeploy | 5 |
| Speculative Decoding | 3 |
| Perf | 1 |
| LoRA | 1 |

## CI / Infra  (37 commits)

- **2026-06-08** [`09c21b65df`](https://github.com/NVIDIA/TensorRT-LLM/commit/09c21b65df) [#15038](https://github.com/NVIDIA/TensorRT-LLM/pull/15038)
  [TRTLLM-13262][ci] Move non-default-feature tests to post merge (#15038)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b300.yml`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus.yml`_
- **2026-06-08** [`2febb372b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/2febb372b5) [#15089](https://github.com/NVIDIA/TensorRT-LLM/pull/15089)
  [None][infra] Waive 1 failed cases for main in pre-merge 41894 (#15089)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`28dc25e68b`](https://github.com/NVIDIA/TensorRT-LLM/commit/28dc25e68b) [#15056](https://github.com/NVIDIA/TensorRT-LLM/pull/15056)
  [None][test] Waive 15 failed cases for main in QA CI (#15056)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`7e49baaa9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e49baaa9a) [#15077](https://github.com/NVIDIA/TensorRT-LLM/pull/15077)
  [None][test] waive weekly qa ci failure cases (#15077)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`26325305d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/26325305d6) [#15082](https://github.com/NVIDIA/TensorRT-LLM/pull/15082)
  [None][infra] Waive 3 failed cases for main in post-merge 2765 (#15082)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`5fa68a4755`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa68a4755) [#15080](https://github.com/NVIDIA/TensorRT-LLM/pull/15080)
  [None][infra] Waive 11 failed cases for main in post-merge 2765 (#15080)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`8be182d2d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/8be182d2d3) [#15058](https://github.com/NVIDIA/TensorRT-LLM/pull/15058)
  [https://nvbugs/6260907][fix] unwaive test (#15058)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-07** [`ec6b284062`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec6b284062)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/whisper/poetry.lock`, `security_scanning/examples/models/core/whisper/pyproject.toml`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
- **2026-06-06** [`e47f26e31b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e47f26e31b) [#14684](https://github.com/NVIDIA/TensorRT-LLM/pull/14684)
  [TRTLLM-13027][ci] Relocate under-using tests to right-sized stages (#14684)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-06-05** [`fb5bd448f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb5bd448f7) [#14948](https://github.com/NVIDIA/TensorRT-LLM/pull/14948)
  [https://nvbugs/5859886][fix] Remove the waiver (#14948)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-05** [`2336e47656`](https://github.com/NVIDIA/TensorRT-LLM/commit/2336e47656) [#15003](https://github.com/NVIDIA/TensorRT-LLM/pull/15003)
  [None][infra] Waive 11 failed cases for main in post-merge 2760 (#15003)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-05** [`6387eac155`](https://github.com/NVIDIA/TensorRT-LLM/commit/6387eac155) [#14528](https://github.com/NVIDIA/TensorRT-LLM/pull/14528)
  [TRTLLM-12893][infra] Parallelize post stages: Rerun Report, Test Coverage, and AI Failure Analysis (#14528)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-06-05** [`316430f805`](https://github.com/NVIDIA/TensorRT-LLM/commit/316430f805) [#14997](https://github.com/NVIDIA/TensorRT-LLM/pull/14997)
  [None] [waive] Waive the failed step3p7 test case due to ckpt update (#14997)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-05** [`45d4d54ed3`](https://github.com/NVIDIA/TensorRT-LLM/commit/45d4d54ed3) [#14989](https://github.com/NVIDIA/TensorRT-LLM/pull/14989)
  [None][test] Fix the ci disagg perf local submit test scope too large issue to avoid HF Model not found (#14989)
  _Files: `jenkins/scripts/perf/local/submit.py`_
- **2026-06-04** [`8c39de8240`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c39de8240) [#14928](https://github.com/NVIDIA/TensorRT-LLM/pull/14928)
  [None][infra] fix cbts json decode (#14928)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/tools/dryrun.py`_
- **2026-06-04** [`0f5dc5a05e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f5dc5a05e) [#14946](https://github.com/NVIDIA/TensorRT-LLM/pull/14946)
  [None][test] update bug ids in waives (#14946)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`023ac8201f`](https://github.com/NVIDIA/TensorRT-LLM/commit/023ac8201f) [#14616](https://github.com/NVIDIA/TensorRT-LLM/pull/14616)
  [TRTLLM-8236][infra] fix platform tag for public wheel (#14616)
  _Files: `jenkins/L0_Test.groovy`, `scripts/build_wheel.py`_
- **2026-06-04** [`846d0f4109`](https://github.com/NVIDIA/TensorRT-LLM/commit/846d0f4109) [#14925](https://github.com/NVIDIA/TensorRT-LLM/pull/14925)
  [None][infra] Waive 11 failed cases for main in post-merge 2757 (#14925)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`86d08f4c2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/86d08f4c2e) [#14025](https://github.com/NVIDIA/TensorRT-LLM/pull/14025)
  [None][infra] Source code and container vulnerability fix (#14025)
  _Files: `constraints.txt`, `docker/Dockerfile.multi`, `examples/scaffolding/contrib/open_deep_research/TavilyMCP/uv.lock`, `jenkins/current_image_tags.properties` _+3 more__
- **2026-06-04** [`e1212ad0b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1212ad0b6) [#14896](https://github.com/NVIDIA/TensorRT-LLM/pull/14896)
  [None][test] Waive 1 failed cases for main in QA CI (#14896)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`d64b217c01`](https://github.com/NVIDIA/TensorRT-LLM/commit/d64b217c01) [#14866](https://github.com/NVIDIA/TensorRT-LLM/pull/14866)
  [https://nvbugs/6050489][chore] unwaive tests (#14866)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`abc6ba20e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/abc6ba20e2) [#14857](https://github.com/NVIDIA/TensorRT-LLM/pull/14857)
  [None][test] Waive 1 failed cases for main in QA CI (#14857)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`d0cfcde1a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0cfcde1a6) [#14545](https://github.com/NVIDIA/TensorRT-LLM/pull/14545)
  [None][test] Remove 28 closed-bug waive entries for main (#14545)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`66577ac980`](https://github.com/NVIDIA/TensorRT-LLM/commit/66577ac980) [#14883](https://github.com/NVIDIA/TensorRT-LLM/pull/14883)
  [None][infra] Waive 5 failed cases for main in post-merge 2755 (#14883)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`e1ed5e05b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1ed5e05b2) [#14792](https://github.com/NVIDIA/TensorRT-LLM/pull/14792)
  [None][test] Waive 9 failed cases for main in QA CI (#14792)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`74ec2a1fce`](https://github.com/NVIDIA/TensorRT-LLM/commit/74ec2a1fce) [#14630](https://github.com/NVIDIA/TensorRT-LLM/pull/14630)
  [None][chore] Make submit.py can run single GPU test and accept customized config file (#14630)
  _Files: `jenkins/scripts/perf/local/submit.py`_
- **2026-06-02** [`4cc2d8a796`](https://github.com/NVIDIA/TensorRT-LLM/commit/4cc2d8a796) [#14854](https://github.com/NVIDIA/TensorRT-LLM/pull/14854)
  [None][test] Waive 11 failed cases for main in post-merge (#14854)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`a2996aed19`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2996aed19) [#14839](https://github.com/NVIDIA/TensorRT-LLM/pull/14839)
  [None][test] Waive 2 failed cases for main in QA CI (#14839)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`125c0da3a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/125c0da3a2) [#14783](https://github.com/NVIDIA/TensorRT-LLM/pull/14783)
  [None][test] Waive 1 failed cases for main in QA CI (#14783)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`06e3a776b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/06e3a776b2) [#14787](https://github.com/NVIDIA/TensorRT-LLM/pull/14787)
  [None][test] Waive 6 failed cases for main in QA CI (#14787)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`b9453fcf76`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9453fcf76) [#14791](https://github.com/NVIDIA/TensorRT-LLM/pull/14791)
  [None][test] Waive 7 failed cases for main in QA CI (#14791)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`12ea8ef22b`](https://github.com/NVIDIA/TensorRT-LLM/commit/12ea8ef22b) [#14789](https://github.com/NVIDIA/TensorRT-LLM/pull/14789)
  [None][test] Waive 5 failed cases for main in QA CI (#14789)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-01** [`d2fd17b03c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2fd17b03c) [#14559](https://github.com/NVIDIA/TensorRT-LLM/pull/14559)
  [TRTLLM-12971][infra] Fix parse classname logic in timeout result (#14559)
  _Files: `jenkins/scripts/generate_timeout_xml.py`_
- **2026-06-01** [`0b96e3a3b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b96e3a3b4) [#14802](https://github.com/NVIDIA/TensorRT-LLM/pull/14802)
  [None][infra] Waive 12 failed cases for main in post-merge 2749 (#14802)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-01** [`35cce74734`](https://github.com/NVIDIA/TensorRT-LLM/commit/35cce74734) [#14809](https://github.com/NVIDIA/TensorRT-LLM/pull/14809)
  [None][test] Update precision of previous device step time (#14809)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-06-01** [`6b36b0e9f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b36b0e9f7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-06-01** [`9ed1669593`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ed1669593) [#14661](https://github.com/NVIDIA/TensorRT-LLM/pull/14661)
  [None][infra] Update new .test_durations (#14661)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`_

## Executor / Runtime  (19 commits)

- **2026-06-08** [`ca2bc5ee4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca2bc5ee4c) [#14994](https://github.com/NVIDIA/TensorRT-LLM/pull/14994)
  [None][perf] kv_cache_manager_v2: batch block-key SHA-256 hashing (#14994)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-06-07** [`dcd4e903e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/dcd4e903e3) [#14812](https://github.com/NVIDIA/TensorRT-LLM/pull/14812)
  [#10710][feat] Make explicit CLI flags take precedence over --config / --extra_llm_api_options YAML (#14812)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/release-notes.md`, `tensorrt_llm/bench/benchmark/__init__.py`, `tensorrt_llm/bench/benchmark/low_latency.py` _+8 more__
- **2026-06-07** [`bedad859d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/bedad859d7) [#14943](https://github.com/NVIDIA/TensorRT-LLM/pull/14943)
  [None][feat] AutoDeploy: Fix hardcoded configs (#14943)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tests/unittest/auto_deploy/singlegpu/shim/test_engine.py`_
- **2026-06-05** [`86f9602057`](https://github.com/NVIDIA/TensorRT-LLM/commit/86f9602057) [#14578](https://github.com/NVIDIA/TensorRT-LLM/pull/14578)
  [TRTLLM-12714][feat] KVCacheManagerV2: wire PyExecutor rebalance hook (single GPU, aggregated for now) (#14578)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/llmapi/llm_args.py` _+7 more__
- **2026-06-05** [`d5de55ea44`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5de55ea44) [#14524](https://github.com/NVIDIA/TensorRT-LLM/pull/14524)
  [https://nvbugs/6210714][fix] Fix mamba block calculation (#14524)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py`_
- **2026-06-05** [`bd17d1b73f`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd17d1b73f) [#14905](https://github.com/NVIDIA/TensorRT-LLM/pull/14905)
  [https://nvbugs/6240420][fix] Clamp KV pool window sizes to max_seq_len (#14905)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`8361d427b3`](https://github.com/NVIDIA/TensorRT-LLM/commit/8361d427b3) [#14869](https://github.com/NVIDIA/TensorRT-LLM/pull/14869)
  [None][perf] Use a Triton kernel for Cpp mamba hybrid state update (#14869)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`_
- **2026-06-04** [`4437cb937d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4437cb937d) [#14900](https://github.com/NVIDIA/TensorRT-LLM/pull/14900)
  [None][fix] Add nemotron-v3 as the proper nemotron-h reasoning parser (#14900)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`, `tests/unittest/llmapi/test_reasoning_parser.py`_
- **2026-06-03** [`fbf66e92df`](https://github.com/NVIDIA/TensorRT-LLM/commit/fbf66e92df) [#14770](https://github.com/NVIDIA/TensorRT-LLM/pull/14770)
  [TRTLLM-13077][feat] Decompose post_load_weights() (#14770)
  _Files: `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/integration/test_lists/test-db/l0_sanity_check.yml`, `tests/unittest/_torch/pyexecutor/test_model_loader_mx.py`_
- **2026-06-03** [`3630e16b14`](https://github.com/NVIDIA/TensorRT-LLM/commit/3630e16b14) [#14863](https://github.com/NVIDIA/TensorRT-LLM/pull/14863)
  [https://nvbugs/6211193][fix] etcd listen all interfaces (#14863)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes_service_discovery.py`_
- **2026-06-03** [`c938efa9e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c938efa9e0) [#14457](https://github.com/NVIDIA/TensorRT-LLM/pull/14457)
  [https://nvbugs/6195110][fix] Restore DeepSeek shared-weights vanilla MTP path (#14457)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`c798fd9677`](https://github.com/NVIDIA/TensorRT-LLM/commit/c798fd9677) [#13240](https://github.com/NVIDIA/TensorRT-LLM/pull/13240)
  [#13082][fix] Fix-multimodal embedding mismatch (#13240)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_vila.py`, `tests/unittest/_torch/multimodal/test_fuse_input_embeds.py`, `tests/unittest/_torch/multimodal/test_multimodal_runtime.py`_
- **2026-06-02** [`cd38dfb2e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd38dfb2e1) [#14800](https://github.com/NVIDIA/TensorRT-LLM/pull/14800)
  [https://nvbugs/6226933][fix] canonicalize multimodal cache-key serialization to prevent hash collisions (#14800)
  _Files: `tensorrt_llm/inputs/multimodal.py`, `tensorrt_llm/inputs/multimodal_data.py`, `tests/unittest/llmapi/test_llm_kv_cache_events.py`_
- **2026-06-02** [`efb71c7447`](https://github.com/NVIDIA/TensorRT-LLM/commit/efb71c7447) [#14725](https://github.com/NVIDIA/TensorRT-LLM/pull/14725)
  [None][fix] Cherry-pick kv_cache_manager_v2 fixes to main (#14725)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-06-01** [`059de9cbe1`](https://github.com/NVIDIA/TensorRT-LLM/commit/059de9cbe1) [#14020](https://github.com/NVIDIA/TensorRT-LLM/pull/14020)
  [None][fix] PyExecutor Hang in Disagg TP Prefill (#14020)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-06-01** [`2e6f602ece`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e6f602ece) [#14509](https://github.com/NVIDIA/TensorRT-LLM/pull/14509)
  [None][fix] Stabilize Mamba replay state update (#14509)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tensorrt_llm/_torch/modules/mamba/replay_selective_state_update.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+1 more__
- **2026-06-01** [`3ec9e9b04c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ec9e9b04c) [#12735](https://github.com/NVIDIA/TensorRT-LLM/pull/12735)
  [https://nvbugs/6038228][fix] Propagate event loop errors to await_responses callers (#12735)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tests/unittest/_torch/executor/test_py_executor.py`, `tests/unittest/executor/test_event_loop_error_broadcast.py`_
- **2026-06-01** [`7a9c1865de`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a9c1865de) [#14730](https://github.com/NVIDIA/TensorRT-LLM/pull/14730)
  [None][feat] Tune mamba config by env variables (#14730)
  _Files: `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`_
- **2026-06-01** [`a422420db9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a422420db9) [#14782](https://github.com/NVIDIA/TensorRT-LLM/pull/14782)
  [https://nvbugs/6244695][fix] Revert Pass IPC HMAC key through file descriptor (#14782)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/unittest/executor/test_launcher_envs.py`_

## MoE  (19 commits)

- **2026-06-08** [`98a88f7f49`](https://github.com/NVIDIA/TensorRT-LLM/commit/98a88f7f49) [#14923](https://github.com/NVIDIA/TensorRT-LLM/pull/14923)
  [TRTLLM-12507][feat] Cudagraph support for routed-expert MoE LoRA with Cutlass backend - Part 1 (#14923)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_device_path.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_pointer_expand.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_problem_builder.h` _+9 more__
- **2026-06-07** [`47666de06c`](https://github.com/NVIDIA/TensorRT-LLM/commit/47666de06c) [#13723](https://github.com/NVIDIA/TensorRT-LLM/pull/13723)
  [#13718][feat] AutoDeploy MoE all-to-all: cache + runtime max-tokens (#13723)
  _Files: `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/torch_moe.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py` _+15 more__
- **2026-06-06** [`4279e5b4d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/4279e5b4d8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+48 more__
- **2026-06-06** [`d7a5872596`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7a5872596) [#13148](https://github.com/NVIDIA/TensorRT-LLM/pull/13148)
  [None][feat] Afmoe trinity support (#13148)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/afmoe_weight_mapper.py` _+3 more__
- **2026-06-04** [`8e5d9e27bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e5d9e27bb) [#12353](https://github.com/NVIDIA/TensorRT-LLM/pull/12353)
  [TRTLLM-11508][refactor] Merge Eagle3 and MTP-eagle one-model workers (#12353)
  _Files: `tensorrt_llm/_torch/models/modeling_exaone_moe.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/__init__.py` _+6 more__
- **2026-06-04** [`a8c4007284`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8c4007284) [#13925](https://github.com/NVIDIA/TensorRT-LLM/pull/13925)
  [None][fix] Fix AutoDeploy accuracy tests (#13925)
  _Files: `examples/auto_deploy/llmc/create_standalone_package.py`, `examples/auto_deploy/model_registry/configs/gemma4_moe.yaml`, `tensorrt_llm/_torch/auto_deploy/_compat.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mla/rope_metadata.py` _+17 more__
- **2026-06-04** [`33b0a32995`](https://github.com/NVIDIA/TensorRT-LLM/commit/33b0a32995) [#14592](https://github.com/NVIDIA/TensorRT-LLM/pull/14592)
  [TRTLLM-12214][perf] DeepGemmFusedMoE: fuse masked gather + finalize-scale into one Triton kernel (#14592)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_deepgemm.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/integration/test_lists/test-db/l0_h100.yml` _+1 more__
- **2026-06-04** [`33efef26ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/33efef26ef)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+51 more__
- **2026-06-04** [`6dc60cb2a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dc60cb2a7) [#14711](https://github.com/NVIDIA/TensorRT-LLM/pull/14711)
  [None][feat] Support Step-3.7-Flash model (#14711)
  _Files: `docs/source/features/speculative-decoding.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+18 more__
- **2026-06-03** [`06388ece45`](https://github.com/NVIDIA/TensorRT-LLM/commit/06388ece45)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+50 more__
- **2026-06-03** [`6824bd8836`](https://github.com/NVIDIA/TensorRT-LLM/commit/6824bd8836) [#14801](https://github.com/NVIDIA/TensorRT-LLM/pull/14801)
  [TRTLLM-12507][feat] Per-expert lora support with Cutlass backend (#14801)
  _Files: `cpp/tensorrt_llm/thop/moeOp.cpp`, `docs/source/features/lora.md`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/models/modeling_qwen_moe.py` _+14 more__
- **2026-06-02** [`6ef7b387c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ef7b387c6) [#14667](https://github.com/NVIDIA/TensorRT-LLM/pull/14667)
  [https://nvbugs/6221450][fix] AutoDeploy: Qwen3.5 400B NVFP4 accuracy regression fix (#14667)
  _Files: `examples/auto_deploy/model_registry/configs/qwen3.5_moe_400b.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/swiglu.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_qwen3_5_moe.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_swiglu.py` _+1 more__
- **2026-06-02** [`33e0ee3aaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/33e0ee3aaf) [#13645](https://github.com/NVIDIA/TensorRT-LLM/pull/13645)
  [None][feat] Enable flashifner gdn decoding kernel for qwen3.5 (#13645)
  _Files: `tensorrt_llm/_torch/modules/fla/chunk.py`, `tensorrt_llm/_torch/modules/fla/chunk_delta_h.py`, `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/fla/fused_recurrent.py` _+3 more__
- **2026-06-02** [`ca004112c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca004112c7) [#14602](https://github.com/NVIDIA/TensorRT-LLM/pull/14602)
  [TRTLLM-35882][feat] Add cute dsl gvr top-k decode kernel (#14602)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/scripts/cute_dsl_kernels/top_k/run_gvr_topk.py` _+1 more__
- **2026-06-02** [`6222112ff9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6222112ff9) [#14477](https://github.com/NVIDIA/TensorRT-LLM/pull/14477)
  [#14588][fix] [AutoDeploy] Fix OOM of DeepSeek-R1 NVFP4 for tp=4 (#14477)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`_
- **2026-06-01** [`02a65b57ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/02a65b57ec) [#14194](https://github.com/NVIDIA/TensorRT-LLM/pull/14194)
  [#12702][feat] Autodeploy deprecate the legacy triton attention (#14194)
  _Files: `.claude/skills/ad-sharding-ir-port/SKILL.md`, `examples/auto_deploy/cookbooks/gemma_4_trtllm_cookbook.ipynb`, `examples/auto_deploy/model_registry/configs/gemma4_dense.yaml`, `examples/auto_deploy/model_registry/configs/gemma4_e2b.yaml` _+21 more__
- **2026-06-01** [`441eaae20d`](https://github.com/NVIDIA/TensorRT-LLM/commit/441eaae20d) [#14453](https://github.com/NVIDIA/TensorRT-LLM/pull/14453)
  [None][feat] Refactor DWDP from CUDA IPC to CUDA VMM + MNNVL composite VA (#14453)
  _Files: `examples/disaggregated/slurm/benchmark/disaggr_torch_dwdp.slurm`, `examples/disaggregated/slurm/benchmark/start_worker_dwdp.sh`, `examples/disaggregated/slurm/benchmark/submit_dwdp.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+30 more__
- **2026-06-01** [`71a188ccd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/71a188ccd8) [#14775](https://github.com/NVIDIA/TensorRT-LLM/pull/14775)
  [TRTLLM-12288][feat] Support Nemotron-H nvfp4 ckpt on Hopper (#14775)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/modules/fused_moe/quantization.py`, `tensorrt_llm/_torch/modules/fused_moe/triton_dequant_nvfp4.py` _+3 more__
- **2026-06-01** [`cde996386b`](https://github.com/NVIDIA/TensorRT-LLM/commit/cde996386b) [#14803](https://github.com/NVIDIA/TensorRT-LLM/pull/14803)
  [None][test] Update moe backend for ctx and acceptance length env (#14803)
  _Files: `tests/scripts/perf-sanity/aggregated/config_database_b200_nvl.yaml`, `tests/scripts/perf-sanity/aggregated/config_database_h200_sxm.yaml`, `tests/scripts/perf-sanity/aggregated/deepseek_r1_fp4_v2_2_nodes_blackwell.yaml`, `tests/scripts/perf-sanity/aggregated/deepseek_r1_fp4_v2_2_nodes_grace_blackwell.yaml` _+44 more__

## Attention  (18 commits)

- **2026-06-08** [`6dee167373`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dee167373) [#14851](https://github.com/NVIDIA/TensorRT-LLM/pull/14851)
  [https://nvbugs/6185446][fix] Add warmup for trtllm-gen fmha JIT kernels (#14851)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/xqaParams.h` _+12 more__
- **2026-06-05** [`fdcdcb3605`](https://github.com/NVIDIA/TensorRT-LLM/commit/fdcdcb3605) [#14999](https://github.com/NVIDIA/TensorRT-LLM/pull/14999)
  [None][fix] AutoDeploy: Move hf_id_to_local_model_dir to function for GLM4.7 Flash test (#14999)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`_
- **2026-06-05** [`21ffdc7279`](https://github.com/NVIDIA/TensorRT-LLM/commit/21ffdc7279) [#14759](https://github.com/NVIDIA/TensorRT-LLM/pull/14759)
  [None][feat] Add AutoDeploy support for StepFun Step-3.7-Flash (#14759)
  _Files: `examples/auto_deploy/cookbooks/step_3.7_flash_trtllm_cookbook.ipynb`, `examples/auto_deploy/model_registry/configs/step-3.7-flash.yaml`, `examples/auto_deploy/model_registry/models.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/flashinfer_attention.py` _+4 more__
- **2026-06-05** [`df2d5b93cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/df2d5b93cd) [#14906](https://github.com/NVIDIA/TensorRT-LLM/pull/14906)
  [https://nvbugs/6248764][fix] Normalize non-sliding KV windows to full attention in AutoDeploy (#14906)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/kvcache.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`910826b041`](https://github.com/NVIDIA/TensorRT-LLM/commit/910826b041) [#14921](https://github.com/NVIDIA/TensorRT-LLM/pull/14921)
  [TRTLLMINF-69][infra] Migrate A100X-FMHA-Post-Merge-1 and A100X-Triton-Post-Merge-[1,2] to SLURM (#14921)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-04** [`27af2e529d`](https://github.com/NVIDIA/TensorRT-LLM/commit/27af2e529d) [#14613](https://github.com/NVIDIA/TensorRT-LLM/pull/14613)
  [https://nvbugs/6193836][test] Use EP=8 + attention DP for minimax_m2.5 8-GPU perf (#14613)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-06-04** [`c16ce24641`](https://github.com/NVIDIA/TensorRT-LLM/commit/c16ce24641) [#14326](https://github.com/NVIDIA/TensorRT-LLM/pull/14326)
  [None][feat] Add encoder CUDA graph support to llm.encode() (#14326)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h`, `tensorrt_llm/_torch/attention_backend/flashinfer.py` _+20 more__
- **2026-06-03** [`5f64e7d2b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f64e7d2b0) [#14768](https://github.com/NVIDIA/TensorRT-LLM/pull/14768)
  [https://nvbugs/6104831][fix] Enforce request and buffer index lifecycle integrity (#14768)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.h`, `cpp/tensorrt_llm/batch_manager/cacheFormatter.cpp` _+9 more__
- **2026-06-03** [`b2bb0ad113`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2bb0ad113) [#13944](https://github.com/NVIDIA/TensorRT-LLM/pull/13944)
  [None][feat] VisualGen: Attention2D + Ulysses & Multi-GPU LPIPS Evals (#13944)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/mapping.py` _+17 more__
- **2026-06-03** [`af9568a4b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/af9568a4b8) [#14814](https://github.com/NVIDIA/TensorRT-LLM/pull/14814)
  [None][chore] add attention module owner for VisualGen (#14814)
  _Files: `.github/CODEOWNERS`_
- **2026-06-03** [`a24c3d4231`](https://github.com/NVIDIA/TensorRT-LLM/commit/a24c3d4231) [#13725](https://github.com/NVIDIA/TensorRT-LLM/pull/13725)
  [#12359][feat] AutoDeploy: Support SSM replay kernel for MTP with FlashInfer (#13725)
  _Files: `examples/auto_deploy/model_registry/configs/super_v3_mtp.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/flashinfer_backend_mamba.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/triton_backend_causal_conv.py` _+11 more__
- **2026-06-03** [`17ccf334da`](https://github.com/NVIDIA/TensorRT-LLM/commit/17ccf334da) [#14853](https://github.com/NVIDIA/TensorRT-LLM/pull/14853)
  [None][feat] Reserve one more slots for attention_dp in mixed mamba cache manager (#14853)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py` _+1 more__
- **2026-06-02** [`209f3717b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/209f3717b0) [#14536](https://github.com/NVIDIA/TensorRT-LLM/pull/14536)
  [https://nvbugs/6191524][fix] In MLA.forward_context, also call the warmup when has_cached_kv_for_mla_context  (#14536)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/modules/attention.py`_
- **2026-06-02** [`18724f7f60`](https://github.com/NVIDIA/TensorRT-LLM/commit/18724f7f60) [#14049](https://github.com/NVIDIA/TensorRT-LLM/pull/14049)
  [None][fix] synchronize MLA cache reuse fallback metadata (#14049)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/executor/test_py_executor_creator_mla_cache_reuse_sync.py`_
- **2026-06-02** [`260b80fd69`](https://github.com/NVIDIA/TensorRT-LLM/commit/260b80fd69) [#14700](https://github.com/NVIDIA/TensorRT-LLM/pull/14700)
  [None][fix] AutoDeploy: Unwaive llmc standalone tests (#14700)
  _Files: `examples/auto_deploy/llmc/create_standalone_package.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/normalization/rms_norm.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_minimax_m2.py`, `tensorrt_llm/_torch/auto_deploy/models/quant_config_reader.py` _+6 more__
- **2026-06-02** [`702e39d2a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/702e39d2a6) [#14805](https://github.com/NVIDIA/TensorRT-LLM/pull/14805)
  [None][chore] Update flashinfer-python from 0.6.12rc2 to 0.6.12 (#14805)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-06-01** [`d5b19bdb16`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5b19bdb16) [#14774](https://github.com/NVIDIA/TensorRT-LLM/pull/14774)
  [https://nvbugs/6240561][fix] Autodeploy fix the deepseek accuracy drop (#14774)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_mla.py`, `tests/unittest/auto_deploy/singlegpu/models/test_deepseek_custom.py`_
- **2026-06-01** [`f402178281`](https://github.com/NVIDIA/TensorRT-LLM/commit/f402178281) [#14459](https://github.com/NVIDIA/TensorRT-LLM/pull/14459)
  [https://nvbugs/6117811][fix] Fix XQA IMA for invalid pages with sliding window (#14459)
  _Files: `3rdparty/fetch_content.json`, `cpp/kernels/xqa/CMakeLists.txt`, `cpp/kernels/xqa/ldgsts.cuh`, `cpp/kernels/xqa/mha.cu` _+4 more__

## Other  (11 commits)

- **2026-06-05** [`f0ca41883e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0ca41883e) [#14992](https://github.com/NVIDIA/TensorRT-LLM/pull/14992)
  [None][test] remove outdated model in perf test (#14992)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-06-04** [`222d9e87d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/222d9e87d4) [#14888](https://github.com/NVIDIA/TensorRT-LLM/pull/14888)
  [NVBUG-6248780][fix] Add --decoupled flag to benchmark_core_model in multi-instance test (#14888)
  _Files: `tests/integration/defs/triton_server/test_triton_llm.py`_
- **2026-06-04** [`941c7781ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/941c7781ad) [#14952](https://github.com/NVIDIA/TensorRT-LLM/pull/14952)
  [None][test] Decrease P1 models number and merge sanity test list into core (#14952)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`, `tests/integration/test_lists/qa/llm_perf_sanity.yml`_
- **2026-06-04** [`b7ca2a62d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7ca2a62d8) [#14929](https://github.com/NVIDIA/TensorRT-LLM/pull/14929)
  [None][test] update rtx6k test list (#14929)
  _Files: `tests/integration/test_lists/qa/llm_function_rtx6k.txt`_
- **2026-06-03** [`a163d749b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/a163d749b5) [#14538](https://github.com/NVIDIA/TensorRT-LLM/pull/14538)
  [None][chore] redact internal NVIDIA URLs from exec-slurm-compile skill (#14538)
  _Files: `.claude/skills/exec-slurm-compile/SKILL.md`, `.claude/skills/exec-slurm-compile/scripts/enroot-import`_
- **2026-06-03** [`3959914c1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/3959914c1d) [#14420](https://github.com/NVIDIA/TensorRT-LLM/pull/14420)
  [None][fix] propagate chat prompt token ids (#14420) (#14859)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/postprocess_handlers.py`_
- **2026-06-03** [`a336495167`](https://github.com/NVIDIA/TensorRT-LLM/commit/a336495167) [#14723](https://github.com/NVIDIA/TensorRT-LLM/pull/14723)
  [None][fix] release v1 KV blocks on MAX_UTILIZATION pause (#14723)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/test_lists/test-db/l0_perf.yml`_
- **2026-06-03** [`f7f92f4334`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7f92f4334) [#14855](https://github.com/NVIDIA/TensorRT-LLM/pull/14855)
  [None][fix] Use renamed get_param_count_and_checkpoint_size in hybrid configs (#14855)
  _Files: `tensorrt_llm/bench/build/dataclasses.py`_
- **2026-06-03** [`e94830c515`](https://github.com/NVIDIA/TensorRT-LLM/commit/e94830c515) [#14750](https://github.com/NVIDIA/TensorRT-LLM/pull/14750)
  [None][fix] Pipe stderr separately in subprocess calls to improve error reporting in Allure (#14750) (#14750)
  _Files: `tests/integration/defs/perf/utils.py`_
- **2026-06-02** [`66262cfe89`](https://github.com/NVIDIA/TensorRT-LLM/commit/66262cfe89) [#14807](https://github.com/NVIDIA/TensorRT-LLM/pull/14807)
  [TRTLLM-12648][test] implement disagg cancel stress metrics_thread (#14807)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/_testing.py`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_log_scanner.py`, `tests/integration/defs/stress_test/disagg_cancel/test_metrics_thread.py`_
- **2026-06-01** [`5f5b77239a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f5b77239a) [#14671](https://github.com/NVIDIA/TensorRT-LLM/pull/14671)
  [None][test] Update datasets path (#14671)
  _Files: `tests/integration/defs/perf/test_perf.py`_

## Quantization  (10 commits)

- **2026-06-08** [`02f6b2fcd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/02f6b2fcd5) [#14835](https://github.com/NVIDIA/TensorRT-LLM/pull/14835)
  [None][feat] AutoDeploy: propagate layer_type hint across pattern-matcher rewrites (#14835)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/swiglu.py`, `tensorrt_llm/_torch/auto_deploy/utils/node_utils.py`, `tensorrt_llm/_torch/auto_deploy/utils/pattern_matcher.py`, `tests/unittest/auto_deploy/singlegpu/transformations/library/test_fuse_swiglu.py` _+1 more__
- **2026-06-08** [`71debd51a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/71debd51a3)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+44 more__
- **2026-06-06** [`520262d850`](https://github.com/NVIDIA/TensorRT-LLM/commit/520262d850) [#14976](https://github.com/NVIDIA/TensorRT-LLM/pull/14976)
  [None][feat] Add LTX-2 visual generation example (#14976)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/configs/ltx2-t2v-fp4-1gpu.yaml`, `examples/visual_gen/configs/ltx2-t2v-fp8-1gpu.yaml`, `examples/visual_gen/models/ltx2.py`_
- **2026-06-05** [`81e86a5260`](https://github.com/NVIDIA/TensorRT-LLM/commit/81e86a5260)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/baichuan/poetry.lock`, `security_scanning/examples/models/contrib/falcon/poetry.lock` _+16 more__
- **2026-06-04** [`00187c0d96`](https://github.com/NVIDIA/TensorRT-LLM/commit/00187c0d96) [#14930](https://github.com/NVIDIA/TensorRT-LLM/pull/14930)
  [None][fix] Update dataset identifier for cnn_dailymail to use namespaced repo in quantization scripts (#14930)
  _Files: `tensorrt_llm/quantization/quantize_by_modelopt.py`_
- **2026-06-03** [`7e8082ec7b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e8082ec7b) [#13722](https://github.com/NVIDIA/TensorRT-LLM/pull/13722)
  [#5247][fix] auto-detect local cnn_dailymail dataset by directory layout (#13722)
  _Files: `tensorrt_llm/quantization/quantize_by_modelopt.py`, `tests/unittest/others/test_quantize_calib_dataset.py`_
- **2026-06-03** [`514afc8a9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/514afc8a9f) [#14660](https://github.com/NVIDIA/TensorRT-LLM/pull/14660)
  [TRTLLM-13022][test] remove deprecated models from tests (#14660)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml` _+45 more__
- **2026-06-02** [`e58e7587c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/e58e7587c6) [#14697](https://github.com/NVIDIA/TensorRT-LLM/pull/14697)
  [https://nvbugs/5940460][fix] Harden FP8 quant fusion matching after PyTorch 26.02 update (#14697)
  _Files: `tensorrt_llm/_torch/compilation/backend.py`, `tensorrt_llm/_torch/compilation/patterns/__init__.py`, `tensorrt_llm/_torch/compilation/patterns/ar_residual_norm.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-06-02** [`4ba59c0e78`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ba59c0e78)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+46 more__
- **2026-06-02** [`c482b81513`](https://github.com/NVIDIA/TensorRT-LLM/commit/c482b81513) [#14793](https://github.com/NVIDIA/TensorRT-LLM/pull/14793)
  [https://nvbugs/6240561][fix] Fix AutoDeploy DeepSeek-R1 accuracy drop (#14793)
  _Files: `tensorrt_llm/_torch/auto_deploy/utils/fp8_dequant.py`, `tests/unittest/auto_deploy/singlegpu/custom_ops/quantization/test_quant.py`_

## Models  (9 commits)

- **2026-06-08** [`2cad6db1db`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cad6db1db) [#15035](https://github.com/NVIDIA/TensorRT-LLM/pull/15035)
  [TRTLLM-13259][ci] Merge DGX_H100 DeepSeek and GptOss stages (#15035)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-08** [`b4d44d33ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4d44d33ba) [#14884](https://github.com/NVIDIA/TensorRT-LLM/pull/14884)
  [https://nvbugs/6153955][test] unwaive GPT-OSS w4 DP4 CUTLASS (#14884)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-06** [`3b2109310d`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b2109310d) [#15010](https://github.com/NVIDIA/TensorRT-LLM/pull/15010)
  [https://nvbugs/6272668][infra] Unwaive DSR1 and Qwen3.5 again (#15010)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-06** [`d639c5793a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d639c5793a) [#14977](https://github.com/NVIDIA/TensorRT-LLM/pull/14977)
  [https://nvbugs/6250866][fix] Fix deep ep partial warp sync for gptoss shapes (#14977)
  _Files: `3rdparty/fetch_content.json`, `3rdparty/patches/deep_ep_intranode_combine_fix.patch`_
- **2026-06-04** [`a50b5e2dfc`](https://github.com/NVIDIA/TensorRT-LLM/commit/a50b5e2dfc) [#13852](https://github.com/NVIDIA/TensorRT-LLM/pull/13852)
  [https://nvbugs/6143787][fix] Add `kv_cache_config = KvCacheConfig(free_gpu_memory_fraction=0.6)` to TestQwen3 (#13852)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`7374d1f3a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/7374d1f3a6) [#14766](https://github.com/NVIDIA/TensorRT-LLM/pull/14766)
  [None][fix] Fix config sharing issue for Qwen3-VL (#14766)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tests/integration/test_lists/test-db/l0_l40s.yml`, `tests/unittest/_torch/modeling/test_modeling_qwen3vl.py`_
- **2026-06-03** [`e5b8094de2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5b8094de2) [#14846](https://github.com/NVIDIA/TensorRT-LLM/pull/14846)
  [https://nvbugs/6248987][fix] Made the slow-tokenizer swap lazy and idempotent. `__init__` now just sets `_slo (#14846)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`_
- **2026-06-03** [`180eedb9e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/180eedb9e1) [#13449](https://github.com/NVIDIA/TensorRT-LLM/pull/13449)
  [None][feat] Add Qwen image support (#13449)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/serve/README.md`, `examples/visual_gen/serve/configs/qwen_image.yml` _+8 more__
- **2026-06-02** [`178c8f4257`](https://github.com/NVIDIA/TensorRT-LLM/commit/178c8f4257) [#14870](https://github.com/NVIDIA/TensorRT-LLM/pull/14870)
  [https://nvbugs/6240561][fix] Unwaive DeepSeek R1 accuracy test (#14870)
  _Files: `tests/integration/test_lists/waives.txt`_

## Disaggregation / KV  (8 commits)

- **2026-06-08** [`c93c63d215`](https://github.com/NVIDIA/TensorRT-LLM/commit/c93c63d215) [#14845](https://github.com/NVIDIA/TensorRT-LLM/pull/14845)
  [None][feat] Enable disk cache config for KV cache v2 (#14845)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/disaggregated/test_cache_transceiver_single_process.py`, `tests/unittest/disaggregated/test_kv_transfer.py` _+1 more__
- **2026-06-08** [`86f33e6a5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/86f33e6a5a) [#14935](https://github.com/NVIDIA/TensorRT-LLM/pull/14935)
  [https://nvbugs/6245317][test] set Harmony tiktoken env for GPT-OSS disagg (#14935)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_
- **2026-06-04** [`2a934fcbff`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a934fcbff) [#14949](https://github.com/NVIDIA/TensorRT-LLM/pull/14949)
  [https://nvbugs/6222480][fix] Fix stress (#14949)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`864240ba13`](https://github.com/NVIDIA/TensorRT-LLM/commit/864240ba13) [#14939](https://github.com/NVIDIA/TensorRT-LLM/pull/14939)
  [https://nvbugs/5979673][fix] Unwaive test_agent_multi_backends.py::test_run_with_different_env (#14939)
  _Files: `tensorrt_llm/_torch/disaggregation/nixl/_agent_py.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-03** [`aa4276d473`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa4276d473) [#14856](https://github.com/NVIDIA/TensorRT-LLM/pull/14856)
  [None][test] Update DSV32 32k4k config to avoid timeout issue (#14856)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-v32-fp4_32k4k_con2048_ctx1_dep4_gen1_dep32_eplb288_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v32-fp4_32k4k_con2048_ctx1_dep4_gen1_dep32_eplb288_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-v32-fp4_32k4k_con2048_ctx1_dep4_gen1_dep32_eplb288_mtp1_ccb-NIXL.yaml` _+3 more__
- **2026-06-02** [`460adc715d`](https://github.com/NVIDIA/TensorRT-LLM/commit/460adc715d) [#14748](https://github.com/NVIDIA/TensorRT-LLM/pull/14748)
  [None][feat] Add KV cache prefetch (#14748)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_storage_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-06-01** [`2f9b85a4df`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f9b85a4df) [#14436](https://github.com/NVIDIA/TensorRT-LLM/pull/14436)
  [None][feat] Upgrade NIXL to v1.0.1 and UCX to 1.21 (#14436)
  _Files: `docker/common/install_nixl.sh`, `docker/common/install_ucx.sh`, `jenkins/L0_Test.groovy`, `jenkins/current_image_tags.properties` _+3 more__
- **2026-06-01** [`70ab8fb512`](https://github.com/NVIDIA/TensorRT-LLM/commit/70ab8fb512) [#13972](https://github.com/NVIDIA/TensorRT-LLM/pull/13972)
  [TRTLLM-12596][feat] Support simple logprob format (#13972)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tensorrt_llm/disaggregated_params.py`, `tensorrt_llm/executor/base_worker.py` _+10 more__

## Torch Path (_torch)  (8 commits)

- **2026-06-08** [`b8d17d708c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8d17d708c) [#14836](https://github.com/NVIDIA/TensorRT-LLM/pull/14836)
  [None][chore] Increase GB200-4_GPUs-PyTorch shards (#14836)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-05** [`52ba2bbfe1`](https://github.com/NVIDIA/TensorRT-LLM/commit/52ba2bbfe1) [#14021](https://github.com/NVIDIA/TensorRT-LLM/pull/14021)
  [TRTLLM-12527][feat] Parallelize multi-shard visual-gen checkpoint loading and pre-fetch checking (#14021)
  _Files: `tensorrt_llm/_torch/visual_gen/checkpoints/prefetch.py`, `tensorrt_llm/_torch/visual_gen/checkpoints/weight_loader.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`_
- **2026-06-05** [`501b5c2232`](https://github.com/NVIDIA/TensorRT-LLM/commit/501b5c2232) [#14892](https://github.com/NVIDIA/TensorRT-LLM/pull/14892)
  [https://nvbugs/6248744][fix] Added `trust_remote_code=True` to the `LLM(...)` constructor and removed the… (#14892)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-05** [`73c824cc51`](https://github.com/NVIDIA/TensorRT-LLM/commit/73c824cc51) [#14824](https://github.com/NVIDIA/TensorRT-LLM/pull/14824)
  [TRTLLM-11410][feat] Cosmos3 Support (#14824)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/configs/cosmos3-nano-1gpu.yaml`, `examples/visual_gen/configs/cosmos3-super-4gpu.yaml` _+7 more__
- **2026-06-04** [`07180493c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/07180493c8) [#14890](https://github.com/NVIDIA/TensorRT-LLM/pull/14890)
  [TRTLLM-12870][feat] Support num_images_per_prompt for FLUX pipelines (#14890)
  _Files: `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux2.py`, `tests/unittest/_torch/visual_gen/test_flux_pipeline.py`_
- **2026-06-03** [`8edd72e1d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/8edd72e1d2) [#14749](https://github.com/NVIDIA/TensorRT-LLM/pull/14749)
  [None][test] Remove duplicate test cases in llm_perf_core file (#14749)
  _Files: `.coderabbit.yaml`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-06-03** [`328ef0bda6`](https://github.com/NVIDIA/TensorRT-LLM/commit/328ef0bda6) [#14818](https://github.com/NVIDIA/TensorRT-LLM/pull/14818)
  [None][fix] LTX-2 audio PE pad: use token-axis seq_dim=1 for token-major rope (#14818)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_ltx2_ulysses.py`_
- **2026-06-02** [`5db9414cbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/5db9414cbe) [#14639](https://github.com/NVIDIA/TensorRT-LLM/pull/14639)
  [https://nvbugs/6179761][fix] Save LTX-2 BF16 weights to speed up perf (#14639)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_

## Docs / Examples  (6 commits)

- **2026-06-08** [`0e0ee2731a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e0ee2731a) [#15015](https://github.com/NVIDIA/TensorRT-LLM/pull/15015)
  [TRTLLM-12648][test] implement disagg cancellation canary thread (#15015)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_canary.py`_
- **2026-06-05** [`3e17560fe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e17560fe3) [#14981](https://github.com/NVIDIA/TensorRT-LLM/pull/14981)
  [None][feat] add Wan I2V generation example (#14981)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/configs/wan2.2-i2v-fp4-1gpu.yaml`, `examples/visual_gen/models/wan_i2v.py`_
- **2026-06-05** [`4574851dae`](https://github.com/NVIDIA/TensorRT-LLM/commit/4574851dae) [#14920](https://github.com/NVIDIA/TensorRT-LLM/pull/14920)
  [TRTLLM-12648][test] implement disagg cancellation injector thread (#14920)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_injector.py`, `tests/integration/defs/stress_test/disagg_cancel/test_log_scanner.py`_
- **2026-06-03** [`bcdf418926`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcdf418926) [#14872](https://github.com/NVIDIA/TensorRT-LLM/pull/14872)
  [None][chore] Bump version to 1.3.0rc18 (#14872)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-06-02** [`c3f6d981b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3f6d981b1) [#14685](https://github.com/NVIDIA/TensorRT-LLM/pull/14685)
  [TRTLLM-13028][doc] Add VisualGen API walkthrough example and docs page (#14685)
  _Files: `docs/source/helper.py`, `docs/source/index.rst`, `examples/visual_gen/api_walkthrough.py`, `tests/integration/defs/examples/test_visual_gen.py` _+4 more__
- **2026-06-01** [`4e12ff7b75`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e12ff7b75) [#14632](https://github.com/NVIDIA/TensorRT-LLM/pull/14632)
  [TRTLLM-13015][feat] drop complex visual_gen CLI example scripts (#14632)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/models/wan_t2v.py`, `examples/visual_gen/visual_gen_flux.py` _+5 more__

## AutoDeploy  (5 commits)

- **2026-06-05** [`37ece3f922`](https://github.com/NVIDIA/TensorRT-LLM/commit/37ece3f922) [#14954](https://github.com/NVIDIA/TensorRT-LLM/pull/14954)
  [https://nvbugs/6160629][fix] AutoDeploy: Fix manual seed setting for standalone tests (#14954)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/singlegpu/custom_ops/rope/test_rope_op_variants.py`_
- **2026-06-05** [`58da60af29`](https://github.com/NVIDIA/TensorRT-LLM/commit/58da60af29) [#15001](https://github.com/NVIDIA/TensorRT-LLM/pull/15001)
  [None][fix] Uncomment Qwen3.5 and DSR1 from model registry so that they can run f… (#15001)
  _Files: `examples/auto_deploy/model_registry/models.yaml`_
- **2026-06-04** [`c17611cf25`](https://github.com/NVIDIA/TensorRT-LLM/commit/c17611cf25) [#14894](https://github.com/NVIDIA/TensorRT-LLM/pull/14894)
  [None][chore] Autodeploy unwaive 5888827, 6200112 (#14894)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-04** [`8b0eba936a`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b0eba936a) [#14795](https://github.com/NVIDIA/TensorRT-LLM/pull/14795)
  [https://nvbugs/6244474][fix] AutoDeploy: skip explicit shape-prop after MLIR elementwise fusion (#14795)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/mlir_elementwise_fusion.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`96534502f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/96534502f1) [#14686](https://github.com/NVIDIA/TensorRT-LLM/pull/14686)
  [None][chore] Update AD model list (#14686)
  _Files: `examples/auto_deploy/model_registry/configs/granite_4.0_h_small.yaml`, `examples/auto_deploy/model_registry/configs/granite_4.0_micro.yaml`, `examples/auto_deploy/model_registry/configs/granite_4.0_tiny_preview.yaml`, `examples/auto_deploy/model_registry/configs/hunyuan_a13b_ep.yaml` _+2 more__

## Speculative Decoding  (3 commits)

- **2026-06-05** [`6818233752`](https://github.com/NVIDIA/TensorRT-LLM/commit/6818233752) [#14995](https://github.com/NVIDIA/TensorRT-LLM/pull/14995)
  [https://nvbugs/5546507][https://nvbugs/5612313][test] Remove obsolet… (#14995)
  _Files: `tests/integration/defs/examples/test_eagle.py`, `tests/integration/defs/examples/test_phi.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-06-02** [`f57f4aa85b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f57f4aa85b) [#14721](https://github.com/NVIDIA/TensorRT-LLM/pull/14721)
  [https://nvbugs/6222480][test] fix stress test issue on H100 (#14721)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_eagle_triton.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_eagle_trtllm.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_triton.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+5 more__
- **2026-06-01** [`06456e1a3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/06456e1a3a) [#14479](https://github.com/NVIDIA/TensorRT-LLM/pull/14479)
  [TRTLLM-10947][perf] eagle3: use cudaMemcpy2DAsync custom op for hidden-state capture (#14479)
  _Files: `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/inplaceSliceCopyOp.cpp`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/__init__.py` _+3 more__

## Perf  (1 commits)

- **2026-06-07** [`428cc3eb68`](https://github.com/NVIDIA/TensorRT-LLM/commit/428cc3eb68) [#14964](https://github.com/NVIDIA/TensorRT-LLM/pull/14964)
  [TRTLLM-13177][doc] Add Nemotron 3 Ultra doc (#14964)
  _Files: `docs/source/_static/config_db.json`, `docs/source/deployment-guide/deployment-guide-for-nemotron-3-on-trtllm.md`, `docs/source/deployment-guide/index.rst`, `docs/source/models/supported-models.md` _+4 more__

## LoRA  (1 commits)

- **2026-06-03** [`6ab50053e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ab50053e6) [#14708](https://github.com/NVIDIA/TensorRT-LLM/pull/14708)
  [None][perf] Reduce OpenAI stream postprocess overhead (#14708)
  _Files: `tensorrt_llm/serve/harmony_adapter.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/postprocess_handlers.py`, `tests/unittest/llmapi/apps/test_harmony_parsing.py` _+1 more__

---
_Generated 2026-06-08 12:48 UTC_