# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-06-08 → 2026-06-15  |  **Total commits:** 171

## ✨ New Features This Week

- **2026-06-15** [#15163](https://github.com/NVIDIA/TensorRT-LLM/pull/15163) — [None][feat] skip-softmax on SM120: TMA-load + sync-MMA warp-specialized context FMHA for sm_120/sm_121 (#15163)
- **2026-06-15** [#14476](https://github.com/NVIDIA/TensorRT-LLM/pull/14476) — [None][feat] MNNVL Performance Optimization and FP8/NVFP4 Quant Fusion (#14476)
- **2026-06-15** [#15208](https://github.com/NVIDIA/TensorRT-LLM/pull/15208) — [TRTLLM-11408][test] Add e2e Tensor Parallel LPIPS tests for VisualGen (#15208)
- **2026-06-13** [#14398](https://github.com/NVIDIA/TensorRT-LLM/pull/14398) — [TRTLLM-12842][feat] Maximal LLMAPI capture in usage telemetry (#14398)
- **2026-06-13** [#15185](https://github.com/NVIDIA/TensorRT-LLM/pull/15185) — [None][feat] AutoDeploy: Qwen3.5: Apply whielist based sharding and apply lm_head sharding (#15185)
- **2026-06-12** [#15139](https://github.com/NVIDIA/TensorRT-LLM/pull/15139) — [TRTLLM-12721][feat] Add disagg transfer state consensus (#15139)
- **2026-06-12** [#14876](https://github.com/NVIDIA/TensorRT-LLM/pull/14876) — [TRTLLM-12498][feat] Add support for beam search in disaggregated serving (#14876)
- **2026-06-12** [#15198](https://github.com/NVIDIA/TensorRT-LLM/pull/15198) — [TRTLLM-35882][feat] cute dsl gvr-top multi-cta optimization (#15198)
- **2026-06-12** [#14808](https://github.com/NVIDIA/TensorRT-LLM/pull/14808) — [TRTLLM-12038][feat] Add accuracy tests for nemotron-v3-ultra (#14808)
- **2026-06-12** [#14878](https://github.com/NVIDIA/TensorRT-LLM/pull/14878) — [TRTLLM-13141][feat] Add backend-agnostic SourceIdentity gate for weight sharing (#14878)
- _…and 45 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#15182](https://github.com/NVIDIA/TensorRT-LLM/issues/15182) | [Bug]: Rejection sampling in Kimi K2.6 | bug | 2026-06-10 |
| [#14826](https://github.com/NVIDIA/TensorRT-LLM/issues/14826) | [Bug]: Using the official tensorrt llm whisper conversion script does  | bug, Triton backend | 2026-06-10 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-06-05 |
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
| CI / Infra | 38 |
| MoE | 27 |
| Attention | 25 |
| Quantization | 14 |
| Models | 12 |
| Executor / Runtime | 12 |
| Disaggregation / KV | 11 |
| Torch Path (_torch) | 8 |
| Other | 8 |
| Docs / Examples | 7 |
| AutoDeploy | 7 |
| Speculative Decoding | 2 |

## CI / Infra  (38 commits)

- **2026-06-15** [`1c069d3e0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c069d3e0d) [#15357](https://github.com/NVIDIA/TensorRT-LLM/pull/15357)
  [None][infra] pin pytest and click workaround (#15357)
  _Files: `requirements-dev.txt`, `requirements.txt`_
- **2026-06-15** [`91a271b831`](https://github.com/NVIDIA/TensorRT-LLM/commit/91a271b831) [#15315](https://github.com/NVIDIA/TensorRT-LLM/pull/15315)
  [None][test] Waive 1 failed cases for main in QA CI (#15315)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-15** [`801cde11bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/801cde11bd) [#15210](https://github.com/NVIDIA/TensorRT-LLM/pull/15210)
  [None][infra] Record CBTS decision to OpenSearch for CI-health monitoring (#15210)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/tools/dryrun.py` _+2 more__
- **2026-06-15** [`221a0e10f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/221a0e10f5) [#15358](https://github.com/NVIDIA/TensorRT-LLM/pull/15358)
  [None][infra] Waive 1 failed cases for main in pre-merge 43173 (#15358)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-12** [`c2b7cd91a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2b7cd91a3) [#15326](https://github.com/NVIDIA/TensorRT-LLM/pull/15326)
  [None][infra] Waive 1 failed cases for main in pre-merge 43047 (#15326)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-12** [`82d3811ec8`](https://github.com/NVIDIA/TensorRT-LLM/commit/82d3811ec8) [#15293](https://github.com/NVIDIA/TensorRT-LLM/pull/15293)
  [None][infra] Waive 1 failed cases for main in pre-merge 42836 (#15293)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`67e1097a46`](https://github.com/NVIDIA/TensorRT-LLM/commit/67e1097a46) [#15275](https://github.com/NVIDIA/TensorRT-LLM/pull/15275)
  [None][infra] Waive 10 failed cases for main in pre-merge 42753 (#15275)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`81f7baf15e`](https://github.com/NVIDIA/TensorRT-LLM/commit/81f7baf15e) [#15273](https://github.com/NVIDIA/TensorRT-LLM/pull/15273)
  [None][infra] Waive 8 failed cases for main in pre-merge 42699 (#15273)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`c85965011e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c85965011e) [#15269](https://github.com/NVIDIA/TensorRT-LLM/pull/15269)
  [None][test] Remove stale perf sanity waives (#15269)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`6b7d8cfd45`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b7d8cfd45) [#15253](https://github.com/NVIDIA/TensorRT-LLM/pull/15253)
  [None][infra] Waive 3 failed cases for main in post-merge 2772 (#15253)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`01d8ccbd13`](https://github.com/NVIDIA/TensorRT-LLM/commit/01d8ccbd13) [#15250](https://github.com/NVIDIA/TensorRT-LLM/pull/15250)
  [None][infra] Waive 6 failed cases for main in post-merge 2773 (#15250)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`016fb4c8ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/016fb4c8ef) [#15061](https://github.com/NVIDIA/TensorRT-LLM/pull/15061)
  [None][test] Remove 78 closed-bug waive entries for main (#15061)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`af5a22ebea`](https://github.com/NVIDIA/TensorRT-LLM/commit/af5a22ebea) [#14075](https://github.com/NVIDIA/TensorRT-LLM/pull/14075)
  [TRTLLM-12657][infra] Fix periodic-junit in unittest pytest (#14075)
  _Files: `tests/integration/defs/conftest.py`, `tests/unittest/conftest.py`_
- **2026-06-10** [`69f5add84c`](https://github.com/NVIDIA/TensorRT-LLM/commit/69f5add84c) [#15118](https://github.com/NVIDIA/TensorRT-LLM/pull/15118)
  [https://nvbugs/6272573][ci] Unwaive skipped test (#15118)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/waives.txt`_
- **2026-06-10** [`9c100bb39d`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c100bb39d) [#15195](https://github.com/NVIDIA/TensorRT-LLM/pull/15195)
  [None][test] temporarily waive Cosmos3 B200 failures (#15195)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-10** [`2763557537`](https://github.com/NVIDIA/TensorRT-LLM/commit/2763557537)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/grok/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-06-09** [`ddef2d01e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/ddef2d01e9) [#15008](https://github.com/NVIDIA/TensorRT-LLM/pull/15008)
  [None][fix] unset UCX_TLS=tcp (#15008)
  _Files: `jenkins/scripts/slurm_run.sh`_
- **2026-06-09** [`f39a79cb96`](https://github.com/NVIDIA/TensorRT-LLM/commit/f39a79cb96) [#14871](https://github.com/NVIDIA/TensorRT-LLM/pull/14871)
  [None][chore] Unwaive DSV32 helix tests (#14871)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`b0216c6322`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0216c6322) [#14955](https://github.com/NVIDIA/TensorRT-LLM/pull/14955)
  [None][infra] Add nv-xtf, rahul-steiger-nv, tedzhouhk, tensorrt-cicd to blossom-ci allowlist (#14955)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-06-09** [`58fbfb983f`](https://github.com/NVIDIA/TensorRT-LLM/commit/58fbfb983f) [#14597](https://github.com/NVIDIA/TensorRT-LLM/pull/14597)
  [None][infra] Test DFW with BSL branch (#14597)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/rules/out_of_scope_rule.py`, `scripts/generate_duration.py`, `tests/integration/defs/.test_durations_aws_dfw`_
- **2026-06-09** [`2ee96cf153`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ee96cf153) [#15148](https://github.com/NVIDIA/TensorRT-LLM/pull/15148)
  [https://nvbugs/6278380][unwaive] unwaive ad cases (#15148)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`178f4e64ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/178f4e64ef) [#15142](https://github.com/NVIDIA/TensorRT-LLM/pull/15142)
  [None][infra] CBTS Layer 3: pass test-db via Artifactory instead of env var (#15142)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`_
- **2026-06-09** [`b85270381e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b85270381e) [#15135](https://github.com/NVIDIA/TensorRT-LLM/pull/15135)
  [None][infra] Waive 1 failed cases for main in pre-merge 41821 (#15135)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`34a94ee3ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/34a94ee3ce) [#14819](https://github.com/NVIDIA/TensorRT-LLM/pull/14819)
  [TRTLLMINF-112][infra] Reduce the waiting time between check node is online or not (#14819)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-09** [`6bf3e492a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bf3e492a1) [#14864](https://github.com/NVIDIA/TensorRT-LLM/pull/14864)
  [None][test] Fix disagg test result dir (#14864)
  _Files: `jenkins/scripts/perf/local/run_disagg.sh`, `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`_
- **2026-06-09** [`e9402ab59d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9402ab59d) [#15108](https://github.com/NVIDIA/TensorRT-LLM/pull/15108)
  [None][test] Fix gen_only missing prev_device_step_time race in perf sanity (#15108)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`9349fcc6bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/9349fcc6bd) [#15140](https://github.com/NVIDIA/TensorRT-LLM/pull/15140)
  [None][infra] Waive 4 failed cases for main in post-merge 2769 (#15140)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`c1e9b00682`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1e9b00682) [#14799](https://github.com/NVIDIA/TensorRT-LLM/pull/14799)
  [https://nvbugs/6211189][fix] Lower the reference to 46.5 (matching cross-GPU empirical mean) and remove the t (#14799)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`9af8a16a6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9af8a16a6b) [#14972](https://github.com/NVIDIA/TensorRT-LLM/pull/14972)
  [None][infra] Reduce Docker image layer count in release stage (#14972)
  _Files: `docker/Dockerfile.multi`, `jenkins/current_image_tags.properties`_
- **2026-06-08** [`9eaa46846a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9eaa46846a) [#15083](https://github.com/NVIDIA/TensorRT-LLM/pull/15083)
  [None][test] Half K25 Agg Multi Round to Solve Timeout Issue (#15083)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/aggregated/dynamo_k25_thinking_fp4_blackwell.yaml`, `tests/scripts/perf-sanity/aggregated/k25_thinking_fp4_2_nodes_grace_blackwell.yaml`, `tests/scripts/perf-sanity/aggregated/k25_thinking_fp4_blackwell.yaml` _+1 more__
- **2026-06-08** [`b14794c2dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/b14794c2dc) [#15078](https://github.com/NVIDIA/TensorRT-LLM/pull/15078)
  [https://nvbugs/6162940][chore] Unwaive fixed test (#15078)
  _Files: `tests/integration/test_lists/waives.txt`_
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

## MoE  (27 commits)

- **2026-06-14** [`4f466535a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f466535a4)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+47 more__
- **2026-06-13** [`1283c6b319`](https://github.com/NVIDIA/TensorRT-LLM/commit/1283c6b319) [#11943](https://github.com/NVIDIA/TensorRT-LLM/pull/11943)
  [TRTLLM-12427][perf] Qwen2.5/3/3.5-VL Performance Optimization (#11943)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/gptKernels.cu`, `cpp/tensorrt_llm/kernels/gptKernels.h` _+24 more__
- **2026-06-13** [`ec47baaf17`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec47baaf17) [#15219](https://github.com/NVIDIA/TensorRT-LLM/pull/15219)
  [https://nvbugs/6293015][fix] Add a delegating `@property def vocab_size_padded(self) -> int: return… (#15219)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`_
- **2026-06-13** [`bb32597c1f`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb32597c1f) [#15185](https://github.com/NVIDIA/TensorRT-LLM/pull/15185)
  [None][feat] AutoDeploy: Qwen3.5: Apply whielist based sharding and apply lm_head sharding (#15185)
  _Files: `examples/auto_deploy/model_registry/configs/qwen3.5_moe_400b.yaml`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_qwen3_5_moe.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_swiglu.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/sharding_ir.py` _+1 more__
- **2026-06-12** [`82ca2c5eec`](https://github.com/NVIDIA/TensorRT-LLM/commit/82ca2c5eec) [#15198](https://github.com/NVIDIA/TensorRT-LLM/pull/15198)
  [TRTLLM-35882][feat] cute dsl gvr-top multi-cta optimization (#15198)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/scripts/cute_dsl_kernels/top_k/run_gvr_topk.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-06-12** [`fb7a1d00e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb7a1d00e4) [#14808](https://github.com/NVIDIA/TensorRT-LLM/pull/14808)
  [TRTLLM-12038][feat] Add accuracy tests for nemotron-v3-ultra (#14808)
  _Files: `cpp/tensorrt_llm/kernels/moePrepareKernels.h`, `cpp/tensorrt_llm/thop/moeCommOp.cpp`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml` _+4 more__
- **2026-06-11** [`be7117cf5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/be7117cf5e) [#14881](https://github.com/NVIDIA/TensorRT-LLM/pull/14881)
  [TRTLLM-12507][feat] Cudagraph support for per-expert lora in Cutlass backend - Part 2 (#14881)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_device_path.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_slot_expand.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_lora_slot_expand.cu`, `cpp/tensorrt_llm/thop/moeOp.cpp` _+11 more__
- **2026-06-11** [`19b5d0ea77`](https://github.com/NVIDIA/TensorRT-LLM/commit/19b5d0ea77) [#14006](https://github.com/NVIDIA/TensorRT-LLM/pull/14006)
  [#13858][fix] AutoDeploy fix the piecewise vlm issue (#14006)
  _Files: `examples/auto_deploy/model_registry/configs/gemma4_e2b.yaml`, `examples/auto_deploy/model_registry/configs/gemma4_moe.yaml`, `examples/auto_deploy/model_registry/configs/qwen3.5_moe_35b.yaml`, `examples/auto_deploy/model_registry/configs/qwen3.5_moe_400b.yaml` _+14 more__
- **2026-06-11** [`d96c0df76e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d96c0df76e) [#15092](https://github.com/NVIDIA/TensorRT-LLM/pull/15092)
  [None][feat] Enhance CuteDSL NVF4 MOE (#15092)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`, `tests/scripts/cute_dsl_kernels/run_blockscaled_contiguous_grouped_gemm_finalize_fusion.py` _+1 more__
- **2026-06-11** [`55bbcf4c93`](https://github.com/NVIDIA/TensorRT-LLM/commit/55bbcf4c93)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+51 more__
- **2026-06-10** [`90cb7ffcc3`](https://github.com/NVIDIA/TensorRT-LLM/commit/90cb7ffcc3) [#14971](https://github.com/NVIDIA/TensorRT-LLM/pull/14971)
  [None][chore] Unwaive AutoDeploy accuracy tests (#14971)
  _Files: `examples/auto_deploy/model_registry/configs/gemma4_e2b.yaml`, `examples/auto_deploy/model_registry/models.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` _+2 more__
- **2026-06-10** [`b206f682f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b206f682f5) [#14268](https://github.com/NVIDIA/TensorRT-LLM/pull/14268)
  [None][feat] Indexer TopK: single-block / multi-pass radix (#14268)
  _Files: `cpp/tensorrt_llm/kernels/IndexerTopK.h`, `cpp/tensorrt_llm/kernels/indexerTopK.cu`, `cpp/tensorrt_llm/thop/IndexerTopKOp.cpp`, `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`_
- **2026-06-10** [`2878b30914`](https://github.com/NVIDIA/TensorRT-LLM/commit/2878b30914) [#13729](https://github.com/NVIDIA/TensorRT-LLM/pull/13729)
  [#12632][feat] Add pipeline cache support for AutoDeploy (#13729)
  _Files: `docs/source/features/auto_deploy/pipeline_cache_design.md`, `tensorrt_llm/_torch/auto_deploy/config/default.yaml`, `tensorrt_llm/_torch/auto_deploy/export/export.py`, `tensorrt_llm/_torch/auto_deploy/models/factory.py` _+17 more__
- **2026-06-10** [`9c6cb35611`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c6cb35611) [#15132](https://github.com/NVIDIA/TensorRT-LLM/pull/15132)
  [https://nvbugs/6140226][test] Add DFlash coverage for Qwen3.5 MoE variant (#15132)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-06-10** [`3b945f76ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b945f76ca) [#14944](https://github.com/NVIDIA/TensorRT-LLM/pull/14944)
  [TRTLLM-13052][feat] Enable TRTLLM moe backend for nemotron-h BF16 ckpt (#14944)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/_torch/modules/fused_moe/moe_op_backend.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+5 more__
- **2026-06-09** [`9a7f76f1d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a7f76f1d2) [#15079](https://github.com/NVIDIA/TensorRT-LLM/pull/15079)
  [None][fix] Register Multimodal Placeholders for Qwen3.5 MoE VLM Serving (#15079)
  _Files: `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_qwen3_5_moe.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py`_
- **2026-06-09** [`ffcd8e62f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffcd8e62f3) [#14202](https://github.com/NVIDIA/TensorRT-LLM/pull/14202)
  [#13816][feat] AutoDeploy: Optimize gpt-oss-120b perf (#14202)
  _Files: `examples/auto_deploy/cookbooks/gpt_oss_trtllm_cookbook.ipynb`, `examples/auto_deploy/llmc/create_standalone_package.py`, `examples/auto_deploy/model_registry/configs/gpt_oss.yaml`, `examples/auto_deploy/model_registry/configs/gpt_oss_120b.yaml` _+17 more__
- **2026-06-09** [`884520cefa`](https://github.com/NVIDIA/TensorRT-LLM/commit/884520cefa) [#14778](https://github.com/NVIDIA/TensorRT-LLM/pull/14778)
  [None][feat] Port 13 AutoDeploy custom models to sharding IR + opt them in via registry (#14778)
  _Files: `.claude/skills/ad-sharding-ir-port/SKILL.md`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_cohere.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_deepseek_v2.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_exaone.py` _+13 more__
- **2026-06-09** [`e0a909a354`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0a909a354)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+51 more__
- **2026-06-09** [`680c6c4c58`](https://github.com/NVIDIA/TensorRT-LLM/commit/680c6c4c58) [#13864](https://github.com/NVIDIA/TensorRT-LLM/pull/13864)
  [TRTLLM-12467][feat] EPD improvements (#13864)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/models/modeling_exaone4_5.py` _+36 more__
- **2026-06-09** [`f0ba8c721e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0ba8c721e) [#14591](https://github.com/NVIDIA/TensorRT-LLM/pull/14591)
  [TRTLLM-12214][perf] DeepGemmFusedMoE: skip redundant data expand via fused expand+quant Triton kernel (#14591)
  _Files: `cpp/tensorrt_llm/thop/moeUtilOp.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_deepgemm.py`, `tensorrt_llm/_torch/modules/fused_moe/ops/moe_op_deepgemm.py` _+5 more__
- **2026-06-09** [`451dbb8b2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/451dbb8b2c) [#14590](https://github.com/NVIDIA/TensorRT-LLM/pull/14590)
  [TRTLLM-12214][perf] customMoeRoutingKernel: lower BLOCK_SIZE to 128, raise maxNumBlocks (#14590)
  _Files: `cpp/tensorrt_llm/kernels/customMoeRoutingKernels.cu`, `tests/unittest/_torch/modules/test_moe_routing.py`_
- **2026-06-09** [`ba6ba1f6a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba6ba1f6a0) [#15081](https://github.com/NVIDIA/TensorRT-LLM/pull/15081)
  [https://nvbugs/6212252][fix] Select CUTLASS MoE backend on non-Blackwell SMs in TestQwen3_5_35B_A3B::test_fp8 (#15081)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`6f7aea5bcc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f7aea5bcc) [#15094](https://github.com/NVIDIA/TensorRT-LLM/pull/15094)
  [https://nvbugs/6266705][fix] Gate FlashInfer GDN kernels to supporte… (#15094)
  _Files: `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_utils.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py`_
- **2026-06-09** [`041ed8356a`](https://github.com/NVIDIA/TensorRT-LLM/commit/041ed8356a)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+47 more__
- **2026-06-08** [`1998324082`](https://github.com/NVIDIA/TensorRT-LLM/commit/1998324082) [#14917](https://github.com/NVIDIA/TensorRT-LLM/pull/14917)
  [https://nvbugs/6248757][fix] Avoid running all reduce in aux stream (#14917)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/multi_stream_moe.py`, `tensorrt_llm/_torch/auto_deploy/utils/node_utils.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/multigpu/custom_ops/test_multi_stream_moe_trailing_allreduce.py` _+1 more__
- **2026-06-08** [`98a88f7f49`](https://github.com/NVIDIA/TensorRT-LLM/commit/98a88f7f49) [#14923](https://github.com/NVIDIA/TensorRT-LLM/pull/14923)
  [TRTLLM-12507][feat] Cudagraph support for routed-expert MoE LoRA with Cutlass backend - Part 1 (#14923)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_device_path.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_pointer_expand.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_problem_builder.h` _+9 more__

## Attention  (25 commits)

- **2026-06-15** [`20b6068387`](https://github.com/NVIDIA/TensorRT-LLM/commit/20b6068387) [#15163](https://github.com/NVIDIA/TensorRT-LLM/pull/15163)
  [None][feat] skip-softmax on SM120: TMA-load + sync-MMA warp-specialized context FMHA for sm_120/sm_121 (#15163)
  _Files: `cpp/kernels/fmha_v2/src/fmha/kernel_traits.h`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/README.md`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/compute_sync_mma.h`, `cpp/kernels/fmha_v2/src/fmha/warpspec_sm120/dma_sync_mma.h` _+7 more__
- **2026-06-15** [`870f9b5b82`](https://github.com/NVIDIA/TensorRT-LLM/commit/870f9b5b82) [#14852](https://github.com/NVIDIA/TensorRT-LLM/pull/14852)
  [https://nvbugs/6029882][fix] Fix attentionOp fp8 mla kvreuse workspace calculation (#14852)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tests/integration/test_lists/waives.txt`_
- **2026-06-12** [`f18d18dcc3`](https://github.com/NVIDIA/TensorRT-LLM/commit/f18d18dcc3) [#14555](https://github.com/NVIDIA/TensorRT-LLM/pull/14555)
  [TRTLLM-12963][refactor] LTX-2 attention: drop dead k_pe parameter; require cached cross-attn (#14555)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`, `tests/unittest/_torch/visual_gen/test_ltx2_attention.py`_
- **2026-06-12** [`85d5e6e203`](https://github.com/NVIDIA/TensorRT-LLM/commit/85d5e6e203) [#14680](https://github.com/NVIDIA/TensorRT-LLM/pull/14680)
  [None][refactor] Move KV cache manager V2 to separate file (#14680)
  _Files: `.github/CODEOWNERS`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py` _+16 more__
- **2026-06-12** [`2b3af6d825`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b3af6d825) [#15156](https://github.com/NVIDIA/TensorRT-LLM/pull/15156)
  [None][fix] Fix max_context_length value for attention workspace sizing (#15156)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm.py`_
- **2026-06-11** [`b586ebf361`](https://github.com/NVIDIA/TensorRT-LLM/commit/b586ebf361) [#13395](https://github.com/NVIDIA/TensorRT-LLM/pull/13395)
  [None][doc] Fix stale --disable_xqa reference in legacy docs (#13395)
  _Files: `docs/source/legacy/advanced/gpt-attention.md`_
- **2026-06-11** [`80f18fef12`](https://github.com/NVIDIA/TensorRT-LLM/commit/80f18fef12) [#15141](https://github.com/NVIDIA/TensorRT-LLM/pull/15141)
  [None][refactor] visual_gen Attention: drop redundant enable_ulysses kwarg (rebase artifact from #13978) (#15141)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`_
- **2026-06-11** [`54dec4f707`](https://github.com/NVIDIA/TensorRT-LLM/commit/54dec4f707) [#14961](https://github.com/NVIDIA/TensorRT-LLM/pull/14961)
  [None][feat] enable GQA and cross-attention for attn2d (#14961)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_attn2d_attention.py` _+2 more__
- **2026-06-11** [`a622e30340`](https://github.com/NVIDIA/TensorRT-LLM/commit/a622e30340) [#12958](https://github.com/NVIDIA/TensorRT-LLM/pull/12958)
  [TRTLLM-11538][feat] Blackwell custom mask fmha support (#12958)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaRunnerParams.h` _+10 more__
- **2026-06-11** [`0d44f3303c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d44f3303c) [#15143](https://github.com/NVIDIA/TensorRT-LLM/pull/15143)
  [None][fix] Remove TLLM_RUBIN_FEATURES (#15143)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/trtllmGen_fmha_export/KernelTraits.h`_
- **2026-06-10** [`dab3400857`](https://github.com/NVIDIA/TensorRT-LLM/commit/dab3400857) [#13904](https://github.com/NVIDIA/TensorRT-LLM/pull/13904)
  [None][test] Add MLA chunked-prefill SM dispatch regression coverage (#13904)
  _Files: `tests/unittest/_torch/attention/test_attention_mla.py`_
- **2026-06-10** [`3b4672876f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b4672876f) [#15173](https://github.com/NVIDIA/TensorRT-LLM/pull/15173)
  [None][fix] Clear workspace in run_mla_generation to avoid potential illegal memory access issue (#15173)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm_gen.py`_
- **2026-06-10** [`2148a3e262`](https://github.com/NVIDIA/TensorRT-LLM/commit/2148a3e262) [#14057](https://github.com/NVIDIA/TensorRT-LLM/pull/14057)
  [#11423][feat] AutoDeploy: Basic Disagg Support (#14057)
  _Files: `examples/auto_deploy/model_registry/configs/disagg_ctx.yaml`, `examples/auto_deploy/model_registry/configs/disagg_gen.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/flashinfer_attention.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_attention.py` _+22 more__
- **2026-06-10** [`57413893af`](https://github.com/NVIDIA/TensorRT-LLM/commit/57413893af) [#14891](https://github.com/NVIDIA/TensorRT-LLM/pull/14891)
  [NVBUG-6241842][fix] DSA DSL atom-split: guard against MTP draft next… (#14891)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`3ddef66035`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ddef66035) [#15110](https://github.com/NVIDIA/TensorRT-LLM/pull/15110)
  [None][feat] Support partial RoPE fusion for Hopper kernels in XQA for Laguna (#15110)
  _Files: `cpp/kernels/xqa/defines.h`, `cpp/kernels/xqa/mha.h`, `cpp/kernels/xqa/mha_sm90.cu`, `cpp/kernels/xqa/test/refAttention.h` _+12 more__
- **2026-06-09** [`f1d39ea8a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1d39ea8a8) [#15047](https://github.com/NVIDIA/TensorRT-LLM/pull/15047)
  [None][fix] Fix regression from SageAttention kernel: Use static scheduler (#15047)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-06-09** [`487330e8a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/487330e8a0) [#14618](https://github.com/NVIDIA/TensorRT-LLM/pull/14618)
  [None][feat] Default on FlashInferTrtllmGenAttention (#14618)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/trtllmGenQKVProcessOp.cpp`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/attention_backend/trtllm_gen.py`_
- **2026-06-09** [`484e6c96c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/484e6c96c3) [#15150](https://github.com/NVIDIA/TensorRT-LLM/pull/15150)
  [None][chore] add VisualGen team as the codeowner of the VisualGen Attention (#15150)
  _Files: `.github/CODEOWNERS`_
- **2026-06-09** [`6254f3a161`](https://github.com/NVIDIA/TensorRT-LLM/commit/6254f3a161) [#15088](https://github.com/NVIDIA/TensorRT-LLM/pull/15088)
  [https://nvbugs/6255037][fix] Count DSA indexer K-cache correctly as UINT8 in KV cache size estimate (#15088)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`_
- **2026-06-09** [`5e3af40eeb`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e3af40eeb) [#13978](https://github.com/NVIDIA/TensorRT-LLM/pull/13978)
  [TRTLLM-11457][feat] Async Ulysses pipeline (Enabled for LTX-2 + WAN) (#13978)
  _Files: `cpp/tensorrt_llm/kernels/ulyssesPermuteScatterKernel.cu`, `cpp/tensorrt_llm/kernels/ulyssesPermuteScatterKernel.h`, `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.cu`, `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.h` _+19 more__
- **2026-06-08** [`b2222469cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2222469cc) [#15020](https://github.com/NVIDIA/TensorRT-LLM/pull/15020)
  [https://nvbugs/6261164][fix] In the kvcache insert transform (`_InsertCachedOperator._apply`), when… (#15020)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/flashinfer_backend_mamba.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/triton_backend_causal_conv.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/triton_backend_mamba.py` _+8 more__
- **2026-06-08** [`900d069071`](https://github.com/NVIDIA/TensorRT-LLM/commit/900d069071) [#14714](https://github.com/NVIDIA/TensorRT-LLM/pull/14714)
  [https://nvbugs/6221483][fix] AutoDeploy: Fix Eagle metadata host syncs (#14714)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_eagle.py`, `tests/unittest/auto_deploy/singlegpu/custom_ops/test_switch_to_generate_inplace.py` _+1 more__
- **2026-06-08** [`cb016073a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb016073a1) [#14911](https://github.com/NVIDIA/TensorRT-LLM/pull/14911)
  [#14828][feat] AutoDeploy: support multi KV cache memory pool in trtllm attention (#14911)
  _Files: `examples/auto_deploy/llmc/create_standalone_package.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/trtllm_attention.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/llm_args.py` _+8 more__
- **2026-06-08** [`2bf4d3d46d`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bf4d3d46d) [#14898](https://github.com/NVIDIA/TensorRT-LLM/pull/14898)
  [None][perf] Support Gemma RMSNorm + interleaved mRoPE in fused_qk_no… (#14898)
  _Files: `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedQKNormRopeOp.cpp`, `tensorrt_llm/_torch/models/modeling_qwen3.py` _+3 more__
- **2026-06-08** [`6dee167373`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dee167373) [#14851](https://github.com/NVIDIA/TensorRT-LLM/pull/14851)
  [https://nvbugs/6185446][fix] Add warmup for trtllm-gen fmha JIT kernels (#14851)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/xqaParams.h` _+12 more__

## Quantization  (14 commits)

- **2026-06-15** [`b1ee4ab17e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1ee4ab17e) [#14476](https://github.com/NVIDIA/TensorRT-LLM/pull/14476)
  [None][feat] MNNVL Performance Optimization and FP8/NVFP4 Quant Fusion (#14476)
  _Files: `cpp/tensorrt_llm/common/lamportUtils.cuh`, `cpp/tensorrt_llm/kernels/communicationKernels/mnnvlAllreduceKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/mnnvlAllreduceKernels.h`, `cpp/tensorrt_llm/thop/allreduceOp.cpp` _+3 more__
- **2026-06-13** [`706a91fcc5`](https://github.com/NVIDIA/TensorRT-LLM/commit/706a91fcc5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/baichuan/poetry.lock`, `security_scanning/examples/models/contrib/falcon/poetry.lock` _+16 more__
- **2026-06-12** [`b03b78f300`](https://github.com/NVIDIA/TensorRT-LLM/commit/b03b78f300) [#15310](https://github.com/NVIDIA/TensorRT-LLM/pull/15310)
  Revert "[None][test] Add support for nemotron_3_ultra_550b_nvfp4 model in performance tests and configurations" (#15310)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml` _+1 more__
- **2026-06-12** [`02957e9e1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/02957e9e1e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+55 more__
- **2026-06-11** [`ccc0708ef6`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccc0708ef6) [#14278](https://github.com/NVIDIA/TensorRT-LLM/pull/14278)
  [TRTLLM-12154][test] Add Qwen3-32B FP8 disagg stress test (#14278)
  _Files: `tests/integration/defs/common.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp1_gentp4_qwen3_32b_fp8.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_stress.txt` _+2 more__
- **2026-06-11** [`9ab3501c18`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ab3501c18) [#15067](https://github.com/NVIDIA/TensorRT-LLM/pull/15067)
  [None][fix] Generalize FP8 checkpoint loading for Qwen3.5 (#15067)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py`_
- **2026-06-10** [`62c65216b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/62c65216b6) [#14926](https://github.com/NVIDIA/TensorRT-LLM/pull/14926)
  [None][feat] Enable MTP for Step-3.7 NVFP4 and port Step-3.7VL vision tower to TRT-LLM modules (#14926)
  _Files: `tensorrt_llm/_torch/models/modeling_step3p7.py`, `tensorrt_llm/_torch/models/modeling_step3p7vl.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmmu.yaml` _+6 more__
- **2026-06-10** [`31e730afe2`](https://github.com/NVIDIA/TensorRT-LLM/commit/31e730afe2) [#15166](https://github.com/NVIDIA/TensorRT-LLM/pull/15166)
  [None][test] Add support for nemotron_3_ultra_550b_nvfp4 model in performance tests and configurations (#15166)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml` _+1 more__
- **2026-06-09** [`d62085198c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d62085198c) [#15093](https://github.com/NVIDIA/TensorRT-LLM/pull/15093)
  [TRTLLM-13302][feat] Register NVIDIA Wan2.2-T2V quantized checkpoints (#15093)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tensorrt_llm/visual_gen/visual_gen.py`_
- **2026-06-09** [`45e25230aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/45e25230aa) [#15053](https://github.com/NVIDIA/TensorRT-LLM/pull/15053)
  [TRTLLM-13264][feat] Add native bias epilogue to NVFP4 GEMM (#15053)
  _Files: `cpp/tensorrt_llm/common/cublasMMWrapper.cpp`, `cpp/tensorrt_llm/common/cublasMMWrapper.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp4_gemm/fp4_gemm_template.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp4_gemm/mxfp8_mxfp4_gemm_template_sm100.h` _+12 more__
- **2026-06-09** [`a197a5ea7f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a197a5ea7f) [#15002](https://github.com/NVIDIA/TensorRT-LLM/pull/15002)
  [None][fix] tunable_fp4_quantize: rename misnamed kwarg + add real SF-swizzle control (#15002)
  _Files: `cpp/tensorrt_llm/thop/fp4Quantize.cpp`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`_
- **2026-06-08** [`8036cde5f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/8036cde5f3) [#15086](https://github.com/NVIDIA/TensorRT-LLM/pull/15086)
  [None][infra] Waive TestQwen3NextInstruct nvfp4 cases (#15086)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-08** [`02f6b2fcd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/02f6b2fcd5) [#14835](https://github.com/NVIDIA/TensorRT-LLM/pull/14835)
  [None][feat] AutoDeploy: propagate layer_type hint across pattern-matcher rewrites (#14835)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/swiglu.py`, `tensorrt_llm/_torch/auto_deploy/utils/node_utils.py`, `tensorrt_llm/_torch/auto_deploy/utils/pattern_matcher.py`, `tests/unittest/auto_deploy/singlegpu/transformations/library/test_fuse_swiglu.py` _+1 more__
- **2026-06-08** [`71debd51a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/71debd51a3)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+44 more__

## Models  (12 commits)

- **2026-06-15** [`aa3236b709`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa3236b709)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-06-11** [`d19b6a8d31`](https://github.com/NVIDIA/TensorRT-LLM/commit/d19b6a8d31) [#14832](https://github.com/NVIDIA/TensorRT-LLM/pull/14832)
  [None][fix] Install processor-output validation filter at module import (#14832)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tests/unittest/_torch/modeling/test_modeling_multimodal.py`_
- **2026-06-11** [`84b349faeb`](https://github.com/NVIDIA/TensorRT-LLM/commit/84b349faeb)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/grok/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock`, `security_scanning/examples/models/core/gemma/poetry.lock`, `security_scanning/examples/models/core/recurrentgemma/poetry.lock` _+6 more__
- **2026-06-10** [`0be1447c71`](https://github.com/NVIDIA/TensorRT-LLM/commit/0be1447c71) [#15174](https://github.com/NVIDIA/TensorRT-LLM/pull/15174)
  [TRTLLM-12648][test] enable disagg cancellation stress test (#15174)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/configs/README.md`, `tests/integration/defs/stress_test/disagg_cancel/configs/marathon_cpp_v1_deepseek.yaml`, `tests/integration/defs/stress_test/disagg_cancel/configs/marathon_python_v2_qwen.yaml` _+3 more__
- **2026-06-09** [`736dc22fd6`](https://github.com/NVIDIA/TensorRT-LLM/commit/736dc22fd6) [#15124](https://github.com/NVIDIA/TensorRT-LLM/pull/15124)
  [TRTLLM-12648][test] implement disagg cancellation load thread (#15124)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/configs/marathon_cpp_v1_deepseek.yaml`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_disagg_cancel_stress.py` _+1 more__
- **2026-06-09** [`28845ddf99`](https://github.com/NVIDIA/TensorRT-LLM/commit/28845ddf99) [#14741](https://github.com/NVIDIA/TensorRT-LLM/pull/14741)
  [https://nvbugs/6227203][fix] Remove redundant TikTokenTokenizer shim from KimiK25InputProcessor (#14741)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`24904416a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/24904416a1) [#15112](https://github.com/NVIDIA/TensorRT-LLM/pull/15112)
  [https://nvbugs/6273850][chore] waive TestQwen3_5_4B::test_bf16 for all GPUs (#15112)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`a33dec718d`](https://github.com/NVIDIA/TensorRT-LLM/commit/a33dec718d) [#14399](https://github.com/NVIDIA/TensorRT-LLM/pull/14399)
  [https://nvbugs/6181383][fix] Build inner text/vision/audio sub-configs as empty PretrainedConfig() then setat (#14399)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`09ebc592e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/09ebc592e5) [#15111](https://github.com/NVIDIA/TensorRT-LLM/pull/15111)
  [TRTLLM-11548][doc] Add Qwen3.5 deployment guide doc (#15111)
  _Files: `docs/source/_static/config_db.json`, `docs/source/deployment-guide/deployment-guide-for-qwen3.5-on-trtllm.md`, `docs/source/deployment-guide/index.rst`, `docs/source/models/supported-models.md` _+3 more__
- **2026-06-09** [`bfb45378de`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfb45378de) [#14956](https://github.com/NVIDIA/TensorRT-LLM/pull/14956)
  [None][refactor] split VisualGen pipeline and model configs (#14956)
  _Files: `tensorrt_llm/_torch/visual_gen/__init__.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py` _+25 more__
- **2026-06-08** [`2cad6db1db`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cad6db1db) [#15035](https://github.com/NVIDIA/TensorRT-LLM/pull/15035)
  [TRTLLM-13259][ci] Merge DGX_H100 DeepSeek and GptOss stages (#15035)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-08** [`b4d44d33ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4d44d33ba) [#14884](https://github.com/NVIDIA/TensorRT-LLM/pull/14884)
  [https://nvbugs/6153955][test] unwaive GPT-OSS w4 DP4 CUTLASS (#14884)
  _Files: `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (12 commits)

- **2026-06-13** [`4e1776a0c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e1776a0c4) [#14398](https://github.com/NVIDIA/TensorRT-LLM/pull/14398)
  [TRTLLM-12842][feat] Maximal LLMAPI capture in usage telemetry (#14398)
  _Files: `.github/CODEOWNERS`, `README.md`, `docs/source/_ext/llmapi_config_telemetry.py`, `docs/source/conf.py` _+21 more__
- **2026-06-12** [`19ae0535d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/19ae0535d1) [#15260](https://github.com/NVIDIA/TensorRT-LLM/pull/15260)
  [None][fix] AutoDeploy: set enable_spec_decode on ADEngine for disagg (#15260)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`_
- **2026-06-12** [`db7161b675`](https://github.com/NVIDIA/TensorRT-LLM/commit/db7161b675) [#14970](https://github.com/NVIDIA/TensorRT-LLM/pull/14970)
  [None][fix] Revert "Add PyTorch reset_prefix_cache API (#14970)" (#15306)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/serve/openai_server.py` _+3 more__
- **2026-06-12** [`ae9226e285`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae9226e285) [#14970](https://github.com/NVIDIA/TensorRT-LLM/pull/14970)
  [None][feat] Add PyTorch reset_prefix_cache API (#14970)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/serve/openai_server.py` _+3 more__
- **2026-06-12** [`aef7d47c2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/aef7d47c2f) [#14878](https://github.com/NVIDIA/TensorRT-LLM/pull/14878)
  [TRTLLM-13141][feat] Add backend-agnostic SourceIdentity gate for weight sharing (#14878)
  _Files: `tensorrt_llm/_torch/memory/gpu_memory_backend.py`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py` _+7 more__
- **2026-06-11** [`eb5674b19e`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb5674b19e) [#15016](https://github.com/NVIDIA/TensorRT-LLM/pull/15016)
  [TRTLLM-12534][fix] Nemotron Nano - properly account for text prompts in inflight batching with EVS on (#15016)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/inputs/multimodal.py`, `tests/unittest/_torch/modeling/test_nemotron_nano_preprocessing.py`_
- **2026-06-11** [`bb74da1a3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb74da1a3a) [#14609](https://github.com/NVIDIA/TensorRT-LLM/pull/14609)
  [None][feat] Targeted warmup-waste cleanup (#14609)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine_warmup.py`_
- **2026-06-10** [`6db3233db8`](https://github.com/NVIDIA/TensorRT-LLM/commit/6db3233db8) [#14733](https://github.com/NVIDIA/TensorRT-LLM/pull/14733)
  [TRTLLM-12491][feat] Align VisualGen serve request schema with VisualGenParams (#14733)
  _Files: `examples/visual_gen/serve/README.md`, `examples/visual_gen/serve/async_video_gen.py`, `examples/visual_gen/serve/sync_image_gen.py`, `examples/visual_gen/serve/sync_video_gen.py` _+30 more__
- **2026-06-10** [`9bc43218be`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bc43218be) [#15136](https://github.com/NVIDIA/TensorRT-LLM/pull/15136)
  [https://nvbugs/6280060][fix] Scope disagg-ctx cache-transfer quorum vote to TP instead of WORLD (#15136)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-06-10** [`8e40515046`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e40515046) [#15085](https://github.com/NVIDIA/TensorRT-LLM/pull/15085)
  [None][fix] Fix and unwaive nemotron related bugs (#15085)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm_pytorch.py`_
- **2026-06-09** [`0f7e1db607`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f7e1db607) [#14922](https://github.com/NVIDIA/TensorRT-LLM/pull/14922)
  Fix PyExecutor FPM iteration timing (#14922)
  _Files: `tensorrt_llm/_torch/pyexecutor/adp_iter_stats.py`, `tensorrt_llm/_torch/pyexecutor/perf_metrics_manager.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py` _+2 more__
- **2026-06-08** [`ca2bc5ee4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca2bc5ee4c) [#14994](https://github.com/NVIDIA/TensorRT-LLM/pull/14994)
  [None][perf] kv_cache_manager_v2: batch block-key SHA-256 hashing (#14994)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_

## Disaggregation / KV  (11 commits)

- **2026-06-12** [`380d96a19e`](https://github.com/NVIDIA/TensorRT-LLM/commit/380d96a19e) [#14876](https://github.com/NVIDIA/TensorRT-LLM/pull/14876)
  [TRTLLM-12498][feat] Add support for beam search in disaggregated serving (#14876)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py` _+11 more__
- **2026-06-12** [`c3238810f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3238810f2) [#14373](https://github.com/NVIDIA/TensorRT-LLM/pull/14373)
  [https://nvbugs/6035425][fix] Fix KV cache host splitting logic (#14373)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/unittest/_torch/executor/test_kv_cache_budget_split.py`_
- **2026-06-11** [`835fd6115b`](https://github.com/NVIDIA/TensorRT-LLM/commit/835fd6115b) [#14960](https://github.com/NVIDIA/TensorRT-LLM/pull/14960)
  [None][test] Update K2.5 andGLM-5 into CI Perf Test (#14960)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml` _+44 more__
- **2026-06-11** [`228829c036`](https://github.com/NVIDIA/TensorRT-LLM/commit/228829c036) [#14546](https://github.com/NVIDIA/TensorRT-LLM/pull/14546)
  [TRTLLM-12958][feat] Enable gen-only spec dec (#14546)
  _Files: `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py` _+2 more__
- **2026-06-11** [`cab198d7b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/cab198d7b7) [#15152](https://github.com/NVIDIA/TensorRT-LLM/pull/15152)
  [https://nvbugs/6108994][fix] add kv_transfer_timeout_ms to avoid timeout (#15152)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v32-fp4_32k4k_con256_ctx1_dep8_gen1_dep8_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml` _+3 more__
- **2026-06-10** [`03ed843cd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/03ed843cd7) [#13051](https://github.com/NVIDIA/TensorRT-LLM/pull/13051)
  [None][feat] Preserve cache_salt string in KV cache events (#13051)
  _Files: `benchmarks/cpp/disaggServerBenchmark.cpp`, `benchmarks/cpp/gptManagerBenchmark.cpp`, `cpp/include/tensorrt_llm/batch_manager/blockKey.h`, `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h` _+31 more__
- **2026-06-10** [`2d196f7cdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d196f7cdf) [#15205](https://github.com/NVIDIA/TensorRT-LLM/pull/15205)
  [None][test] Increase kv_transfer_timeout_ms for b200 deepseek-r1 disagg gen_only perf test (#15205)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/b200_deepseek-r1-fp4_8k1k_con1536_ctx1_dep4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-06-09** [`0edbbfe20e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0edbbfe20e) [#14806](https://github.com/NVIDIA/TensorRT-LLM/pull/14806)
  [None][feat] Expose stored block-hash chain to KV cache connector (#14806)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp` _+4 more__
- **2026-06-09** [`a7e4a9b63d`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7e4a9b63d) [#15144](https://github.com/NVIDIA/TensorRT-LLM/pull/15144)
  [TRTLLM-13332][test] Remove TestLlama4ScoutInstruct tests (#15144)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_spark_func.yml` _+2 more__
- **2026-06-08** [`c93c63d215`](https://github.com/NVIDIA/TensorRT-LLM/commit/c93c63d215) [#14845](https://github.com/NVIDIA/TensorRT-LLM/pull/14845)
  [None][feat] Enable disk cache config for KV cache v2 (#14845)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/disaggregated/test_cache_transceiver_single_process.py`, `tests/unittest/disaggregated/test_kv_transfer.py` _+1 more__
- **2026-06-08** [`86f33e6a5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/86f33e6a5a) [#14935](https://github.com/NVIDIA/TensorRT-LLM/pull/14935)
  [https://nvbugs/6245317][test] set Harmony tiktoken env for GPT-OSS disagg (#14935)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`_

## Torch Path (_torch)  (8 commits)

- **2026-06-15** [`26ea499332`](https://github.com/NVIDIA/TensorRT-LLM/commit/26ea499332) [#15256](https://github.com/NVIDIA/TensorRT-LLM/pull/15256)
  [None][refactor] Remove TensorRT performance baseline and update to PyTorch only (#15256)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_run.sh`, `tests/integration/defs/perf/README.md`, `tests/integration/defs/perf/_model_paths.py` _+6 more__
- **2026-06-13** [`cd650702c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd650702c7) [#12902](https://github.com/NVIDIA/TensorRT-LLM/pull/12902)
  [#12715][fix] disable NCCL_SYMMETRIC tactic on GB10 (DGX Spark) (#12902)
  _Files: `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/distributed/ops.py`_
- **2026-06-12** [`be7e978fa2`](https://github.com/NVIDIA/TensorRT-LLM/commit/be7e978fa2) [#15223](https://github.com/NVIDIA/TensorRT-LLM/pull/15223)
  [None][chore] 2 more WAN multi-gpu tests (#15223)
  _Files: `tests/integration/defs/examples/test_visual_gen_multi_gpu.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/multi_gpu/test_wan_pipeline_parallel.py` _+1 more__
- **2026-06-12** [`2dd5c67358`](https://github.com/NVIDIA/TensorRT-LLM/commit/2dd5c67358) [#14841](https://github.com/NVIDIA/TensorRT-LLM/pull/14841)
  [None][fix] Stabilize Mamba replay state update (#14841)
  _Files: `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tensorrt_llm/_torch/modules/mamba/replay_selective_state_update.py`_
- **2026-06-11** [`d3748a31b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3748a31b4) [#12310](https://github.com/NVIDIA/TensorRT-LLM/pull/12310)
  [#12230][fix] Add bounds checking in autotuner _find_nearest_profile for SM121 (#12310)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-06-11** [`205920d5c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/205920d5c7) [#15129](https://github.com/NVIDIA/TensorRT-LLM/pull/15129)
  [https://nvbugs/6278399][fix] Add x86_64 path using CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR with… (#15129)
  _Files: `tensorrt_llm/_torch/modules/dwdp/transport.py`, `tensorrt_llm/_torch/modules/dwdp/vmm.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-11** [`5e3f012a66`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e3f012a66) [#14355](https://github.com/NVIDIA/TensorRT-LLM/pull/14355)
  [https://nvbugs/6143883][fix] Preserve ip:port for trtllm-serve visual-gen (#14355)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/unittest/_torch/visual_gen/test_trtllm_serve_e2e.py`_
- **2026-06-08** [`b8d17d708c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8d17d708c) [#14836](https://github.com/NVIDIA/TensorRT-LLM/pull/14836)
  [None][chore] Increase GB200-4_GPUs-PyTorch shards (#14836)
  _Files: `jenkins/L0_Test.groovy`_

## Other  (8 commits)

- **2026-06-12** [`57bb6ee57a`](https://github.com/NVIDIA/TensorRT-LLM/commit/57bb6ee57a) [#15139](https://github.com/NVIDIA/TensorRT-LLM/pull/15139)
  [TRTLLM-12721][feat] Add disagg transfer state consensus (#15139)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`_
- **2026-06-12** [`44550bc6bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/44550bc6bc) [#14941](https://github.com/NVIDIA/TensorRT-LLM/pull/14941)
  [TRTLLM-10184][chore] Remove legacy XQA precompiled code path (#14941)
- **2026-06-12** [`82ddf75940`](https://github.com/NVIDIA/TensorRT-LLM/commit/82ddf75940) [#15290](https://github.com/NVIDIA/TensorRT-LLM/pull/15290)
  [None][test] Sunset the old disagg test cases for the qa side (#15290)
- **2026-06-10** [`309c76423b`](https://github.com/NVIDIA/TensorRT-LLM/commit/309c76423b) [#14979](https://github.com/NVIDIA/TensorRT-LLM/pull/14979)
  [https://nvbugs/6104831][fix] Port dataTransceiver shared_ptr<LlmRequest> lifetime fix (#14979)
  _Files: `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.h`, `cpp/tests/unit_tests/multi_gpu/cacheTransceiverTest.cpp`_
- **2026-06-10** [`9635f7d0d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9635f7d0d0) [#15066](https://github.com/NVIDIA/TensorRT-LLM/pull/15066)
  [https://nvbugs/6266370][fix] Fix MAX_UTILIZATION reuse token budget on main (#15066)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`_
- **2026-06-10** [`edfc667254`](https://github.com/NVIDIA/TensorRT-LLM/commit/edfc667254) [#14998](https://github.com/NVIDIA/TensorRT-LLM/pull/14998)
  [None][feat] Weight trtllm-bench AR/AL averages by output length (#14998)
  _Files: `tensorrt_llm/bench/dataclasses/reporting.py`, `tensorrt_llm/bench/dataclasses/statistics.py`, `tests/unittest/others/test_bench_statistics.py`_
- **2026-06-09** [`358505c41d`](https://github.com/NVIDIA/TensorRT-LLM/commit/358505c41d) [#12998](https://github.com/NVIDIA/TensorRT-LLM/pull/12998)
  [#12805][fix] Fall back to local cache when loading tokenizer for gated models (#12998)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`_
- **2026-06-09** [`a90fd152a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/a90fd152a5) [#15090](https://github.com/NVIDIA/TensorRT-LLM/pull/15090)
  [https://nvbugs/6194812][test] Update llm_perf_core.yml to require a minimum of 4 GPUs and add new performance tests (#15090)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Docs / Examples  (7 commits)

- **2026-06-15** [`e6c996453b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6c996453b) [#15208](https://github.com/NVIDIA/TensorRT-LLM/pull/15208)
  [TRTLLM-11408][test] Add e2e Tensor Parallel LPIPS tests for VisualGen (#15208)
  _Files: `tests/integration/defs/examples/test_visual_gen_multi_gpu.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-06-11** [`1b360ee894`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b360ee894) [#15268](https://github.com/NVIDIA/TensorRT-LLM/pull/15268)
  [TRTLLM-11403][doc] Cache-DiT documentation (#15268)
  _Files: `docs/source/models/visual-generation.md`_
- **2026-06-10** [`27b52b3bbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/27b52b3bbb) [#15126](https://github.com/NVIDIA/TensorRT-LLM/pull/15126)
  [None][test] Add e2e example tests for flux1/2, ltx2, wan_i2v, and cosmos3 (#15126)
  _Files: `tests/integration/defs/examples/test_visual_gen.py`, `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-06-09** [`48d2b8909a`](https://github.com/NVIDIA/TensorRT-LLM/commit/48d2b8909a) [#15177](https://github.com/NVIDIA/TensorRT-LLM/pull/15177)
  [None][chore] Make image paths absolute in blog22 (#15177)
  _Files: `docs/source/blogs/tech_blog/blog22_Helix_Parallelism_Scaling_Multi_Million_Token_Decoding_with_KV_Cache_Sharding.md`_
- **2026-06-08** [`9827c21e56`](https://github.com/NVIDIA/TensorRT-LLM/commit/9827c21e56) [#14987](https://github.com/NVIDIA/TensorRT-LLM/pull/14987)
  [None][feat] add FLUX visual generation examples (#14987)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/configs/flux1-dev-fp4-1gpu.yaml`, `examples/visual_gen/configs/flux2-dev-fp4-1gpu.yaml`, `examples/visual_gen/models/flux1.py` _+1 more__
- **2026-06-08** [`15d06c0923`](https://github.com/NVIDIA/TensorRT-LLM/commit/15d06c0923) [#15113](https://github.com/NVIDIA/TensorRT-LLM/pull/15113)
  [None][doc] Refine Nemotron Ultra doc (#15113)
  _Files: `docs/source/models/supported-models.md`_
- **2026-06-08** [`0e0ee2731a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e0ee2731a) [#15015](https://github.com/NVIDIA/TensorRT-LLM/pull/15015)
  [TRTLLM-12648][test] implement disagg cancellation canary thread (#15015)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/harness.py`, `tests/integration/defs/stress_test/disagg_cancel/test_canary.py`_

## AutoDeploy  (7 commits)

- **2026-06-12** [`646464bb95`](https://github.com/NVIDIA/TensorRT-LLM/commit/646464bb95) [#15316](https://github.com/NVIDIA/TensorRT-LLM/pull/15316)
  [https://nvbugs/6309375][test] AutoDeploy: Remove stale fallback test (#15316)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/singlegpu/shim/test_llm_config.py`_
- **2026-06-12** [`8e2b7b2e75`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e2b7b2e75) [#15175](https://github.com/NVIDIA/TensorRT-LLM/pull/15175)
  [#14672][fix] AutoDeploy: Vendor OpenELMConfig locally to fix OpenELM config loading (#15175)
  _Files: `examples/auto_deploy/model_registry/models.yaml`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_openelm.py`, `tests/unittest/auto_deploy/singlegpu/models/test_openelm_modeling.py`_
- **2026-06-12** [`5a77356c0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a77356c0d) [#15282](https://github.com/NVIDIA/TensorRT-LLM/pull/15282)
  [None][infra] Waive remaining AutoDeploy Disagg tests until fix lands (#15282)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-10** [`7301075055`](https://github.com/NVIDIA/TensorRT-LLM/commit/7301075055) [#15228](https://github.com/NVIDIA/TensorRT-LLM/pull/15228)
  [None][fix] Fix AutoDeploy transform docs generation (#15228)
  _Files: `docs/source/_ext/trtllm_auto_deploy.py`_
- **2026-06-10** [`74d8a484ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/74d8a484ed) [#15214](https://github.com/NVIDIA/TensorRT-LLM/pull/15214)
  [https://nvbugs/6245279][fix] AutoDeploy: Unwaive accuracy tests (#15214)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`104b9d71bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/104b9d71bb) [#15107](https://github.com/NVIDIA/TensorRT-LLM/pull/15107)
  [https://nvbugs/6244474][fix] AutoDeploy: Remove llama perf test from CI (#15107)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-06-09** [`64497e2026`](https://github.com/NVIDIA/TensorRT-LLM/commit/64497e2026) [#15122](https://github.com/NVIDIA/TensorRT-LLM/pull/15122)
  [None][doc] Add docs for AutoDeploy transforms (#15122)
  _Files: `.gitignore`, `docs/source/_ext/trtllm_auto_deploy.py`, `docs/source/conf.py`, `docs/source/features/auto_deploy/auto-deploy.md` _+14 more__

## Speculative Decoding  (2 commits)

- **2026-06-11** [`00ed78ca0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/00ed78ca0f) [#15023](https://github.com/NVIDIA/TensorRT-LLM/pull/15023)
  [#15022][fix] Guided decoding (xgrammar) + EAGLE-3 + draft_len_schedule reaching 0 crashes during CUDA graph capture, "bitmask must have the same batch size as logits" (#15023)
  _Files: `tensorrt_llm/_torch/pyexecutor/guided_decoder.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-06-09** [`98393f36b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/98393f36b4) [#12636](https://github.com/NVIDIA/TensorRT-LLM/pull/12636)
  [None][feat] Add Prometheus metrics for prompt cache, speculative decoding, perplexity, and batch occupancy (#12636)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/result.py`, `tensorrt_llm/metrics/collector.py` _+4 more__

---
_Generated 2026-06-15 14:36 UTC_