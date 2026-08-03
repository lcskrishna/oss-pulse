# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-07-27 → 2026-08-03  |  **Total commits:** 192

## ✨ New Features This Week

- **2026-08-03** [#17047](https://github.com/NVIDIA/TensorRT-LLM/pull/17047) — [None][test] add e2e key model perf test (#17047)
- **2026-08-03** [#16908](https://github.com/NVIDIA/TensorRT-LLM/pull/16908) — [TRTLLM-13948][feat] Set DeepSeekV3 to use Python KV-cache transceiver V2 by default (#16908)
- **2026-08-03** [#16714](https://github.com/NVIDIA/TensorRT-LLM/pull/16714) — [None][feat] Add paged KV cache support to Vanilla attention (#16714)
- **2026-08-03** [#17161](https://github.com/NVIDIA/TensorRT-LLM/pull/17161) — [TRTLLM-14772][doc] Add sudo to apt prerequisites (#17161)
- **2026-08-03** [#17099](https://github.com/NVIDIA/TensorRT-LLM/pull/17099) — [None][test] Add back 1k1k cases for qa side (#17099)
- **2026-08-03** [#17101](https://github.com/NVIDIA/TensorRT-LLM/pull/17101) — [None][test] Add back new ctx and gen only case (#17101)
- **2026-08-01** [#13385](https://github.com/NVIDIA/TensorRT-LLM/pull/13385) — [None][feat] Add duration-based execution to benchmark (#13385)
- **2026-08-01** [#16814](https://github.com/NVIDIA/TensorRT-LLM/pull/16814) — [None][feat] Enable PyTorch profiler traces for VisualGen (#16814)
- **2026-07-31** [#15806](https://github.com/NVIDIA/TensorRT-LLM/pull/15806) — [None][feat] Support DSA MTP indexer top-k sharing (#15806)
- **2026-07-31** [#16458](https://github.com/NVIDIA/TensorRT-LLM/pull/16458) — [TRTLLM-12352][feat] complete MX post-transform qualification foundation (#16458)
- _…and 42 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-28** [`2a7231d0de`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a7231d0de) [#16932](https://github.com/NVIDIA/TensorRT-LLM/pull/16932) — [None][test] Update CODEOWNERS to refine QA ownership by adding specific roles for performance/function/serving testing (#16932)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17016](https://github.com/NVIDIA/TensorRT-LLM/issues/17016) | [RFC]: Add openengine gRPC server support to trtllm-serve | RFC | 2026-08-03 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-07-29 |
| [#17020](https://github.com/NVIDIA/TensorRT-LLM/issues/17020) | `trtllm-eval aime25`/`aime26` silently disable thinking on DeepSeek-V4 | — | 2026-07-29 |
| [#17013](https://github.com/NVIDIA/TensorRT-LLM/issues/17013) | [RFC]: Reduce overhead in KV cache event publishing | RFC | 2026-07-29 |
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

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 50 |
| Attention | 24 |
| Executor / Runtime | 24 |
| MoE | 22 |
| Torch Path (_torch) | 17 |
| Other | 12 |
| Speculative Decoding | 12 |
| Disaggregation / KV | 11 |
| Quantization | 10 |
| Models | 7 |
| Docs / Examples | 1 |
| ROCm / AMD | 1 |
| Perf | 1 |

## CI / Infra  (50 commits)

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
- **2026-08-02** [`1e97b8ed5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e97b8ed5a)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-08-02** [`3bf44f31d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bf44f31d5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-02** [`27f2d1ccc2`](https://github.com/NVIDIA/TensorRT-LLM/commit/27f2d1ccc2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-01** [`fdf7bd5f8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fdf7bd5f8e) [#17096](https://github.com/NVIDIA/TensorRT-LLM/pull/17096)
  [None][infra] Always install latest openssl, libssl3t64 (#17096)
  _Files: `docker/common/install_base.sh`_
- **2026-08-01** [`09b6bea164`](https://github.com/NVIDIA/TensorRT-LLM/commit/09b6bea164) [#16753](https://github.com/NVIDIA/TensorRT-LLM/pull/16753)
  [https://nvbugs/6450338][fix] Default to FP32 accumulation in allreduce fusion kernels (#16753)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/allReduceFusionKernels.cu`, `tests/integration/test_lists/waives.txt`_
- **2026-08-01** [`b1365968ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1365968ec) [#17131](https://github.com/NVIDIA/TensorRT-LLM/pull/17131)
  [https://nvbugs/6541322][fix] Unwaive fixed test (#17131)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-31** [`e6568c3f8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6568c3f8f) [#17070](https://github.com/NVIDIA/TensorRT-LLM/pull/17070)
  [None][infra] Bump version to 1.3.0rc24 (#17070)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-07-31** [`be9afadb19`](https://github.com/NVIDIA/TensorRT-LLM/commit/be9afadb19) [#17109](https://github.com/NVIDIA/TensorRT-LLM/pull/17109)
  [None][infra] Add blossom-ci authorized users (#17109)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-31** [`9e6af133d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e6af133d4) [#17079](https://github.com/NVIDIA/TensorRT-LLM/pull/17079)
  [None][infra] Waive 1 failed cases for main in pre-merge 50924 (#17079)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`b8a4af190d`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8a4af190d) [#17066](https://github.com/NVIDIA/TensorRT-LLM/pull/17066)
  [https://nvbugs/6487836][chore] unwaive test_performance_alignment[1] (#17066)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`88bfcaeec3`](https://github.com/NVIDIA/TensorRT-LLM/commit/88bfcaeec3) [#16694](https://github.com/NVIDIA/TensorRT-LLM/pull/16694)
  [None][infra] Container vulnerability fix (#16694)
  _Files: `constraints.txt`, `docker/Dockerfile.multi`, `docker/common/install_base.sh`, `docker/common/install_etcd.sh` _+1 more__
- **2026-07-30** [`05efb7db98`](https://github.com/NVIDIA/TensorRT-LLM/commit/05efb7db98) [#16725](https://github.com/NVIDIA/TensorRT-LLM/pull/16725)
  [None][infra] Select UCX env for perf sanity by cluster name (#16725)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/cluster_env.py`, `jenkins/scripts/perf/local/configs/example.conf`, `jenkins/scripts/perf/local/run_disagg.sh` _+5 more__
- **2026-07-30** [`da5b62fbeb`](https://github.com/NVIDIA/TensorRT-LLM/commit/da5b62fbeb) [#16996](https://github.com/NVIDIA/TensorRT-LLM/pull/16996)
  [TRTLLMINF-250][infra] Change jnlp image from urm.nvidia.com to artifactory.pdx.nvidia.com (#16996)
  _Files: `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy` _+3 more__
- **2026-07-30** [`787ee9403b`](https://github.com/NVIDIA/TensorRT-LLM/commit/787ee9403b) [#17044](https://github.com/NVIDIA/TensorRT-LLM/pull/17044)
  [None][test] Waive 1 failed cases for main in QA CI (#17044)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`af1d452086`](https://github.com/NVIDIA/TensorRT-LLM/commit/af1d452086) [#17045](https://github.com/NVIDIA/TensorRT-LLM/pull/17045)
  [None][test] Waive 1 failed cases for main in QA CI (#17045)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`49efbc1bc2`](https://github.com/NVIDIA/TensorRT-LLM/commit/49efbc1bc2) [#16946](https://github.com/NVIDIA/TensorRT-LLM/pull/16946)
  [None][infra] Remove unused GitLab token env from pytest (#16946)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/conftest.py`_
- **2026-07-30** [`c0eac26d4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0eac26d4a) [#17041](https://github.com/NVIDIA/TensorRT-LLM/pull/17041)
  [None][infra] Waive 15 failed cases for main in post-merge 2869 (#17041)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`9c345f8939`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c345f8939) [#16980](https://github.com/NVIDIA/TensorRT-LLM/pull/16980)
  [https://nvbugs/6529626][fix] Pin mcp<2.0.0 and unwaive the scaffolding tests (#16980)
  _Files: `requirements.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`f20ea652dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/f20ea652dd) [#15484](https://github.com/NVIDIA/TensorRT-LLM/pull/15484)
  [https://nvbugs/6337224][fix] Update PERF_SANITY_DIR to include `aggregated/`; in `recipe_to_server_config`… (#15484)
  _Files: `scripts/generate_config_database_tests.py`_
- **2026-07-29** [`34490115e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/34490115e0) [#16989](https://github.com/NVIDIA/TensorRT-LLM/pull/16989)
  [None][infra] Waive 5 failed cases for main in post-merge 2865 (#16989)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`d9c53cced0`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9c53cced0) [#16978](https://github.com/NVIDIA/TensorRT-LLM/pull/16978)
  [None][infra] Waive 1 failed cases for main in pre-merge 50457 (#16978)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`0f3f850605`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f3f850605) [#16985](https://github.com/NVIDIA/TensorRT-LLM/pull/16985)
  [None][test] Waive 1 failed cases for main in QA CI (#16985)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`6b75514be1`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b75514be1) [#16984](https://github.com/NVIDIA/TensorRT-LLM/pull/16984)
  [None][test] Waive 1 failed cases for main in QA CI (#16984)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`15dbae9098`](https://github.com/NVIDIA/TensorRT-LLM/commit/15dbae9098) [#16982](https://github.com/NVIDIA/TensorRT-LLM/pull/16982)
  [None][test] Waive 7 failed cases for main in QA CI (#16982)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`71fbbc2ca1`](https://github.com/NVIDIA/TensorRT-LLM/commit/71fbbc2ca1) [#16983](https://github.com/NVIDIA/TensorRT-LLM/pull/16983)
  [None][test] Waive 1 failed cases for main in QA CI (#16983)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`058bbe3dbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/058bbe3dbb) [#16979](https://github.com/NVIDIA/TensorRT-LLM/pull/16979)
  [None][test] Waive 4 failed cases for main in QA CI (#16979)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`0f542f30c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f542f30c5) [#16754](https://github.com/NVIDIA/TensorRT-LLM/pull/16754)
  [None][chore] add user (#16754)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-28** [`095ab2cb58`](https://github.com/NVIDIA/TensorRT-LLM/commit/095ab2cb58) [#15669](https://github.com/NVIDIA/TensorRT-LLM/pull/15669)
  [None][fix] Don't re-run the SLURM monitor on a terminal job failure (#15669)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-28** [`9833c64871`](https://github.com/NVIDIA/TensorRT-LLM/commit/9833c64871) [#16950](https://github.com/NVIDIA/TensorRT-LLM/pull/16950)
  [None][test] Waive 7 failed cases for main in QA CI (#16950)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`90f78681a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/90f78681a0) [#16947](https://github.com/NVIDIA/TensorRT-LLM/pull/16947)
  [None][test] Waive 1 failed cases for main in QA CI (#16947)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`201adecdda`](https://github.com/NVIDIA/TensorRT-LLM/commit/201adecdda) [#16915](https://github.com/NVIDIA/TensorRT-LLM/pull/16915)
  [https://nvbugs/6510284][fix] Cap gen-only benchmark queue size (#16915)
  _Files: `jenkins/scripts/perf/local/submit.py`, `jenkins/scripts/perf/submit.py`, `tests/unittest/scripts/test_perf_submit.py`_
- **2026-07-28** [`65b1e53241`](https://github.com/NVIDIA/TensorRT-LLM/commit/65b1e53241) [#16409](https://github.com/NVIDIA/TensorRT-LLM/pull/16409)
  [https://nvbugs/6435112][test] Unwaive Wan 2.2 I2V perf sanity test (#16409)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`99d61db0f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/99d61db0f1) [#16934](https://github.com/NVIDIA/TensorRT-LLM/pull/16934)
  [None][test] Waive 7 failed cases for main in QA CI (#16934)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-27** [`888fa1700d`](https://github.com/NVIDIA/TensorRT-LLM/commit/888fa1700d) [#16446](https://github.com/NVIDIA/TensorRT-LLM/pull/16446)
  [TRTLLMINF-40][fix] Introduce a SLURM dispatcher pod "finalizer" (#16446)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-27** [`0f5e15e0dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f5e15e0dc) [#16886](https://github.com/NVIDIA/TensorRT-LLM/pull/16886)
  [None][fix] Clarify explicit post-merge stage CI label (#16886)
  _Files: `docs/source/developer-guide/ci-overview.md`_
- **2026-07-27** [`1ae9b86f12`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ae9b86f12) [#16882](https://github.com/NVIDIA/TensorRT-LLM/pull/16882)
  [None][infra] Waive 21 failed cases for main in post-merge 2862 (#16882)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-27** [`9129f4eaf5`](https://github.com/NVIDIA/TensorRT-LLM/commit/9129f4eaf5)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Attention  (24 commits)

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
- **2026-07-31** [`946f9c5fbf`](https://github.com/NVIDIA/TensorRT-LLM/commit/946f9c5fbf) [#15806](https://github.com/NVIDIA/TensorRT-LLM/pull/15806)
  [None][feat] Support DSA MTP indexer top-k sharing (#15806)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/modules/mla.py`, `tensorrt_llm/_torch/speculative/eagle3.py` _+6 more__
- **2026-07-31** [`72434f872e`](https://github.com/NVIDIA/TensorRT-LLM/commit/72434f872e) [#17075](https://github.com/NVIDIA/TensorRT-LLM/pull/17075)
  [TRTLLM-14709][infra] Require packaging>=24.2 for FlashInfer source builds (#17075)
  _Files: `requirements.txt`_
- **2026-07-31** [`85620fd98e`](https://github.com/NVIDIA/TensorRT-LLM/commit/85620fd98e) [#16590](https://github.com/NVIDIA/TensorRT-LLM/pull/16590)
  [TRTLLM-13230][feat] support min_p sampling for TorchSampler (#16590)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py` _+8 more__
- **2026-07-30** [`a9dcdb3e5c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9dcdb3e5c) [#16439](https://github.com/NVIDIA/TensorRT-LLM/pull/16439)
  [None][fix] Add mutex to avoid potentially concurrent modifications to `std::unordered_map` (#16439)
  _Files: `cpp/tensorrt_llm/common/opUtils.cpp`, `cpp/tensorrt_llm/common/opUtils.h`, `cpp/tensorrt_llm/thop/attentionOp.cpp`_
- **2026-07-30** [`60fddd869b`](https://github.com/NVIDIA/TensorRT-LLM/commit/60fddd869b) [#16561](https://github.com/NVIDIA/TensorRT-LLM/pull/16561)
  [None][feat] MTP one-model `advanced_sampling_mode`: skip redundant top-k / top-p filter kernels with additional config enum (#16561)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`, `tensorrt_llm/_torch/speculative/eagle3_dynamic_tree.py`, `tensorrt_llm/_torch/speculative/interface.py` _+4 more__
- **2026-07-30** [`1c052b4d72`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c052b4d72) [#16929](https://github.com/NVIDIA/TensorRT-LLM/pull/16929)
  [None][fix] cascade: wire workspace regardless of multi_block_mode (#16929)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`_
- **2026-07-30** [`86e7571dd6`](https://github.com/NVIDIA/TensorRT-LLM/commit/86e7571dd6) [#16142](https://github.com/NVIDIA/TensorRT-LLM/pull/16142)
  [None][perf] Add Qwen Image VisualGen perf fastpaths (#16142)
  _Files: `tensorrt_llm/_torch/visual_gen/models/qwen_image/pipeline_qwen_image.py`, `tensorrt_llm/_torch/visual_gen/models/qwen_image/transformer_qwen_image.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_qwen_image_attention_parallel.py` _+1 more__
- **2026-07-29** [`2e1a997afb`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e1a997afb) [#11575](https://github.com/NVIDIA/TensorRT-LLM/pull/11575)
  [#8384][fix] use dict.get() instead of getattr() for rope_scaling dict access (#11575)
  _Files: `tensorrt_llm/_torch/modules/qk_norm_attention.py`_
- **2026-07-29** [`b0043529f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0043529f2) [#16981](https://github.com/NVIDIA/TensorRT-LLM/pull/16981)
  [TRTLLM-14736][chore] Split the sampler package into per-feature modules (#16981)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/demollm.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/__init__.py`, `tensorrt_llm/_torch/pyexecutor/sampler/finish_reasons.py` _+15 more__
- **2026-07-29** [`c9a26296db`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9a26296db) [#16793](https://github.com/NVIDIA/TensorRT-LLM/pull/16793)
  [https://nvbugs/6490033][fix] Relaxed the assertion to accept both `is_eagle3()` and… (#16793)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`a1e5771003`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1e5771003) [#16783](https://github.com/NVIDIA/TensorRT-LLM/pull/16783)
  [None][perf] Preserve default V2 KV cache pool sizing (#16783)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/integration/defs/perf/_model_paths.py` _+4 more__
- **2026-07-29** [`f6125fb347`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6125fb347) [#16856](https://github.com/NVIDIA/TensorRT-LLM/pull/16856)
  [None][perf] Avoid Index-K cache materialization for MSA (#16856)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_indexer.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_utils.py` _+3 more__
- **2026-07-28** [`5ac2259600`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ac2259600) [#16836](https://github.com/NVIDIA/TensorRT-LLM/pull/16836)
  [None][feat] Batched physical KV-cache compaction for KV cache compression (#16836)
  _Files: `cpp/tensorrt_llm/kernels/unfusedAttentionKernels.h`, `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_bf16_bf16.cu`, `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt` _+9 more__
- **2026-07-28** [`e552a61ccc`](https://github.com/NVIDIA/TensorRT-LLM/commit/e552a61ccc) [#16502](https://github.com/NVIDIA/TensorRT-LLM/pull/16502)
  [TRTLLM-14502][feat] LTX-2 two-stage: dual-topology parallel Stage 2 (cfg folds into ulysses) (#16502)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/mapping.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py` _+8 more__
- **2026-07-28** [`d6a2d25c7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6a2d25c7a) [#16598](https://github.com/NVIDIA/TensorRT-LLM/pull/16598)
  [TRTLLM-11875][feat] BREAKING: MambaCacheManager based on KVCacheManagerV2 & agentic prefix caching (#16598)
  _Files: `docs/source/developer-guide/telemetry.md`, `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/disaggregation/native/mixers/attention/peer.py` _+55 more__
- **2026-07-28** [`6219c2e5a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/6219c2e5a1) [#16890](https://github.com/NVIDIA/TensorRT-LLM/pull/16890)
  [https://nvbugs/6450333][test] Unwaive DeepSeek V4 Flash auto dtype test (#16890)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`d7be54b5e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7be54b5e6) [#16143](https://github.com/NVIDIA/TensorRT-LLM/pull/16143)
  [None][perf] Enable FLUX2 VisualGen fused NVFP4 SwiGLU path (#16143)
  _Files: `tensorrt_llm/_torch/visual_gen/models/flux/attention.py`, `tensorrt_llm/_torch/visual_gen/models/flux/joint_proj.py`, `tensorrt_llm/_torch/visual_gen/models/flux/transformer_flux2.py`, `tests/unittest/_torch/visual_gen/test_flux_transformer.py`_
- **2026-07-27** [`151db5de6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/151db5de6e) [#15123](https://github.com/NVIDIA/TensorRT-LLM/pull/15123)
  [https://nvbugs/6157892][fix] Mistral format refactor (#15123)
  _Files: `examples/llm-api/quickstart_advanced.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/checkpoints/mistral/config_loader.py` _+12 more__
- **2026-07-27** [`d12c85e62b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d12c85e62b) [#16838](https://github.com/NVIDIA/TensorRT-LLM/pull/16838)
  [https://nvbugs/6507109][infra] Split slow DGX B300 attention unit tests (#16838)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b300.yml`_
- **2026-07-27** [`9de6c94798`](https://github.com/NVIDIA/TensorRT-LLM/commit/9de6c94798) [#16789](https://github.com/NVIDIA/TensorRT-LLM/pull/16789)
  [None][perf] Skip DeepGEMM clean_logits in DSA indexer prefill on custom top-k path (#16789)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`_

## Executor / Runtime  (24 commits)

- **2026-08-01** [`a9544e0ded`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9544e0ded) [#13385](https://github.com/NVIDIA/TensorRT-LLM/pull/13385)
  [None][feat] Add duration-based execution to benchmark (#13385)
  _Files: `tensorrt_llm/bench/benchmark/__init__.py`, `tensorrt_llm/bench/benchmark/low_latency.py`, `tensorrt_llm/bench/benchmark/throughput.py`, `tensorrt_llm/bench/benchmark/utils/asynchronous.py` _+3 more__
- **2026-08-01** [`7e6692a474`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e6692a474) [#16814](https://github.com/NVIDIA/TensorRT-LLM/pull/16814)
  [None][feat] Enable PyTorch profiler traces for VisualGen (#16814)
  _Files: `docs/source/developer-guide/perf-analysis.md`, `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`, `tensorrt_llm/_torch/visual_gen/models/qwen_image/pipeline_qwen_image.py` _+9 more__
- **2026-07-31** [`330470901e`](https://github.com/NVIDIA/TensorRT-LLM/commit/330470901e) [#16746](https://github.com/NVIDIA/TensorRT-LLM/pull/16746)
  [https://nvbugs/6441022][fix] Enable CUDA graph for final context token computation (#16746)
  _Files: `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/defs/kv_cache/test_final_single_token_context_cuda_graph.py` _+4 more__
- **2026-07-31** [`731d293dd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/731d293dd7) [#16458](https://github.com/NVIDIA/TensorRT-LLM/pull/16458)
  [TRTLLM-12352][feat] complete MX post-transform qualification foundation (#16458)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py` _+9 more__
- **2026-07-31** [`7443b7f02b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7443b7f02b) [#16958](https://github.com/NVIDIA/TensorRT-LLM/pull/16958)
  [https://nvbugs/5708901][perf] avoid logits copies when computing logprobs (#16958)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/unittest/_torch/sampler/test_logits_logprobs.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-07-31** [`e34d3d47f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/e34d3d47f1) [#17112](https://github.com/NVIDIA/TensorRT-LLM/pull/17112)
  [https://nvbugs/6537081][fix] Fix import error (#17112)
  _Files: `tensorrt_llm/llmapi/__init__.py`_
- **2026-07-31** [`b1b8dbd9e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1b8dbd9e4) [#16815](https://github.com/NVIDIA/TensorRT-LLM/pull/16815)
  [None][fix] Bind explicit DP rank for new conversations (#16815)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tests/unittest/_torch/executor/test_adp_router.py`_
- **2026-07-31** [`932d3b97cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/932d3b97cc) [#16644](https://github.com/NVIDIA/TensorRT-LLM/pull/16644)
  [TRTLLM-14177][feat] support reference images in FLUX.2 (#16644)
  _Files: `examples/visual_gen/models/flux2.py`, `tensorrt_llm/_torch/visual_gen/cache/teacache.py`, `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux.py` _+9 more__
- **2026-07-31** [`dc7f325b46`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc7f325b46) [#16971](https://github.com/NVIDIA/TensorRT-LLM/pull/16971)
  [https://nvbugs/6523767][fix] Size MPI worker-identity barrier timeout to cover worker bootstrap (#16971)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/test_common/session_prefetcher.py`, `tests/test_common/session_reuse.py`, `tests/unittest/llmapi/test_mpi_session.py` _+2 more__
- **2026-07-31** [`10a9432c61`](https://github.com/NVIDIA/TensorRT-LLM/commit/10a9432c61) [#16554](https://github.com/NVIDIA/TensorRT-LLM/pull/16554)
  [TRTLLM-14304][feat] Integrate embeddings cache with encoder side-stream (#16554)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+10 more__
- **2026-07-30** [`01a04f0762`](https://github.com/NVIDIA/TensorRT-LLM/commit/01a04f0762) [#16485](https://github.com/NVIDIA/TensorRT-LLM/pull/16485)
  [TRTLLM-13229][feat] implement repetition / frequency / presence penalties for TorchSampler (#16485)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/penalties.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py` _+3 more__
- **2026-07-30** [`d0b60a163b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0b60a163b) [#16943](https://github.com/NVIDIA/TensorRT-LLM/pull/16943)
  [https://nvbugs/6523880][fix] Restored the `legacy-files.txt` entry and regenerated the three derived… (#16943)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+1 more__
- **2026-07-29** [`4b2e48b2b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b2e48b2b2) [#16944](https://github.com/NVIDIA/TensorRT-LLM/pull/16944)
  [None][fix] Keep MRoPE delta read slots dense across mixed batches (#16944)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py` _+1 more__
- **2026-07-28** [`f9ac468a91`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9ac468a91) [#16141](https://github.com/NVIDIA/TensorRT-LLM/pull/16141)
  [TRTLLM-12341][feat] Add Whisper support to the PyTorch backend (#16141)
  _Files: `docs/source/models/encoder-decoder.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/modeling_whisper.py`, `tensorrt_llm/_torch/modules/layer_norm.py` _+10 more__
- **2026-07-28** [`3f701587bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f701587bc) [#16897](https://github.com/NVIDIA/TensorRT-LLM/pull/16897)
  [https://nvbugs/6507955][fix] use net_max_seq_len for request admisson instead of inflated one (#16897)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/llmapi/test_llm.py`_
- **2026-07-28** [`05edf29f3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/05edf29f3a) [#16688](https://github.com/NVIDIA/TensorRT-LLM/pull/16688)
  [https://nvbugs/6484986][fix] cancel pending UCX receive (#16688)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/ucx_utils/ucxCacheCommunicator.cpp`, `cpp/tests/CMakeLists.txt`, `cpp/tests/unit_tests/executor/CMakeLists.txt`, `cpp/tests/unit_tests/executor/ucxCommTest.cpp` _+1 more__
- **2026-07-28** [`03d4be4af2`](https://github.com/NVIDIA/TensorRT-LLM/commit/03d4be4af2) [#16866](https://github.com/NVIDIA/TensorRT-LLM/pull/16866)
  [https://nvbugs/6240584][fix] Qwen3ToolParser: bare-JSON fallback for reasoning-preceded tool calls (#16866)
  _Files: `tensorrt_llm/serve/tool_parser/qwen3_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-07-28** [`5e4a1543af`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e4a1543af) [#16770](https://github.com/NVIDIA/TensorRT-LLM/pull/16770)
  [None][test] Enable session prefetch for all test stages (#16770)
  _Files: `tests/test_common/session_prefetcher.py`, `tests/unittest/llmapi/test_session_prefetcher.py`_
- **2026-07-28** [`c4f33538bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4f33538bf) [#15976](https://github.com/NVIDIA/TensorRT-LLM/pull/15976)
  [None][feat] Support MiniCPM-V 4.6 (image + video) on the PyTorch backend (#15976)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/minicpmv4_6.py`, `tensorrt_llm/_torch/models/__init__.py` _+4 more__
- **2026-07-27** [`cfeca001e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfeca001e2) [#16337](https://github.com/NVIDIA/TensorRT-LLM/pull/16337)
  [None][feat] Generic Mixed Modality Support (#16337)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_qwen2vl.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/inputs/media_io.py` _+4 more__
- **2026-07-27** [`155847d427`](https://github.com/NVIDIA/TensorRT-LLM/commit/155847d427) [#16841](https://github.com/NVIDIA/TensorRT-LLM/pull/16841)
  [https://nvbugs/6507081][fix] Refresh the fakes only — add `reasoning_parser = None` to… (#16841)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-07-27** [`6046f34e1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/6046f34e1a) [#16763](https://github.com/NVIDIA/TensorRT-LLM/pull/16763)
  [https://nvbugs/6198785][fix] Unify phase-1 CUDA graph cleanup (#16763)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-27** [`1b4ffc0291`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b4ffc0291) [#16829](https://github.com/NVIDIA/TensorRT-LLM/pull/16829)
  [TRTLLM-14475][chore] Self-sufficient transfer-agent dlopen and drop onnx/modelopt deps (#16829)
  _Files: `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/transferAgent.cpp`, `examples/layer_wise_benchmarks/sample_performance_alignment.sh` _+8 more__
- **2026-07-27** [`b8ff548a5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8ff548a5f) [#16791](https://github.com/NVIDIA/TensorRT-LLM/pull/16791)
  [None][perf] prepare_inputs: avoid O(seq_len) get_tokens(0) marshalling on the host (#16791)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_

## MoE  (22 commits)

- **2026-07-31** [`1c797cf7ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c797cf7ab) [#16642](https://github.com/NVIDIA/TensorRT-LLM/pull/16642)
  [TRTLLM-14497][feat] Add BF16/FP8 refit for qwen3.5_397b (#16642)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py` _+13 more__
- **2026-07-31** [`f10a22e978`](https://github.com/NVIDIA/TensorRT-LLM/commit/f10a22e978) [#17051](https://github.com/NVIDIA/TensorRT-LLM/pull/17051)
  [None][fix] Fix Qwen3Next MoE expert-quant probe and GDN verify tensor alignment (#17051)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/modules/fla/fused_sigmoid_gating_recurrent.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/models/test_qwen3_next_moe_quant.py`_
- **2026-07-31** [`a2df74eef6`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2df74eef6) [#16662](https://github.com/NVIDIA/TensorRT-LLM/pull/16662)
  [None][feat] Enable MM encoder cache on Qwen3.x and Gemma4 VLMs (#16662)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_gemma4_unified.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_mistral.py` _+11 more__
- **2026-07-31** [`138eb4302d`](https://github.com/NVIDIA/TensorRT-LLM/commit/138eb4302d) [#17009](https://github.com/NVIDIA/TensorRT-LLM/pull/17009)
  [TRTLLM-14609][chore] Remove ENABLE_CONFIGURABLE_MOE escape hatch and remaining MoE legacy relics (#17009)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py` _+12 more__
- **2026-07-30** [`83c0eb1ca1`](https://github.com/NVIDIA/TensorRT-LLM/commit/83c0eb1ca1) [#16514](https://github.com/NVIDIA/TensorRT-LLM/pull/16514)
  [https://nvbugs/6463829][fix] Fix fp8 MoE test (#16514)
  _Files: `cpp/tensorrt_llm/thop/moeOp.cpp`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tests/unittest/_torch/lora/test_moe_lora_grouped_gemm.py`_
- **2026-07-30** [`ffba1a6085`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffba1a6085) [#16673](https://github.com/NVIDIA/TensorRT-LLM/pull/16673)
  [None][chore] update DeepGEMM to 2.6.1 (#16673)
  _Files: `3rdparty/fetch_content.json`, `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`, `scripts/attribution/data/dependency_metadata.yml`, `scripts/attribution/data/files_to_dependency.yml` _+1 more__
- **2026-07-29** [`960530bc27`](https://github.com/NVIDIA/TensorRT-LLM/commit/960530bc27) [#16859](https://github.com/NVIDIA/TensorRT-LLM/pull/16859)
  [None][perf] Fuse MiniMax-M3 MoE routing (#16859)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.cu`, `tensorrt_llm/_torch/models/modeling_step3p7.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/_torch/modules/fused_moe/routing.py` _+2 more__
- **2026-07-29** [`f5cbe6b3e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5cbe6b3e4) [#15756](https://github.com/NVIDIA/TensorRT-LLM/pull/15756)
  [None][feat] Improve cute dsl radix top-k (#15756)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/block_scan.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/filtered_top_k_decode_varlen.py` _+5 more__
- **2026-07-29** [`c4afe88087`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4afe88087) [#16865](https://github.com/NVIDIA/TensorRT-LLM/pull/16865)
  [TRTLLM-14609][chore] Remove legacy MoE path in DenseGEMMFusedMoE (#16865)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_densegemm.py`_
- **2026-07-29** [`7e8eb8f1a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e8eb8f1a1) [#16190](https://github.com/NVIDIA/TensorRT-LLM/pull/16190)
  [None][feat] Update CuTeDSL MegaMoE kernels (#16190)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_megamoe_custom_op.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/contract.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/custom_ext.py` _+28 more__
- **2026-07-29** [`cb44a40296`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb44a40296) [#16862](https://github.com/NVIDIA/TensorRT-LLM/pull/16862)
  [TRTLLM-14609][chore] Remove legacy MoE path in TRTLLMGenFusedMoE (#16862)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`_
- **2026-07-28** [`e2b714554f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2b714554f) [#16745](https://github.com/NVIDIA/TensorRT-LLM/pull/16745)
  [None][fix] Keep chunked-MoE size vectors identical across attention-DP ranks (#16745)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`_
- **2026-07-28** [`1b9cbfa125`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b9cbfa125) [#16861](https://github.com/NVIDIA/TensorRT-LLM/pull/16861)
  [TRTLLM-14609][chore] Remove legacy MoE path in CutlassFusedMoE (#16861)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`_
- **2026-07-28** [`4d4e8aa297`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d4e8aa297) [#16945](https://github.com/NVIDIA/TensorRT-LLM/pull/16945)
  [None][fix] Update DeepSeek V4 Flash-Base MoE backend configuration in model YAML (#16945)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`_
- **2026-07-28** [`729eb4e786`](https://github.com/NVIDIA/TensorRT-LLM/commit/729eb4e786) [#16930](https://github.com/NVIDIA/TensorRT-LLM/pull/16930)
  [None][test] Add missing test durations for MiniMaxM3, Step3_7, and MoE LoR… (#16930)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-28** [`343a20b035`](https://github.com/NVIDIA/TensorRT-LLM/commit/343a20b035) [#16864](https://github.com/NVIDIA/TensorRT-LLM/pull/16864)
  [TRTLLM-14609][chore] Remove legacy MoE path in DeepGemmFusedMoE (#16864)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_deepgemm.py`_
- **2026-07-28** [`ede2cad578`](https://github.com/NVIDIA/TensorRT-LLM/commit/ede2cad578) [#16863](https://github.com/NVIDIA/TensorRT-LLM/pull/16863)
  [TRTLLM-14609][chore] Remove legacy MoE path in CuteDslFusedMoE (#16863)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`_
- **2026-07-28** [`7a64f26604`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a64f26604) [#16881](https://github.com/NVIDIA/TensorRT-LLM/pull/16881)
  [https://nvbugs/6479863][fix] Use scalar SwiGLU limit for DeepSeek V4 FP8 MoE (#16881)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`_
- **2026-07-28** [`f3d4c85461`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3d4c85461) [#16457](https://github.com/NVIDIA/TensorRT-LLM/pull/16457)
  [None][perf] GVR top-K decode: enable R0 histogram-ladder admission by default (#16457)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_load_balance.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-07-28** [`89c6635316`](https://github.com/NVIDIA/TensorRT-LLM/commit/89c6635316)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+33 more__
- **2026-07-27** [`1dd8b97d53`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dd8b97d53) [#16830](https://github.com/NVIDIA/TensorRT-LLM/pull/16830)
  [None][feat] Add kimi_k2/glm_5 grouped routing and fused router to bench_moe (#16830)
  _Files: `tests/microbenchmarks/bench_moe/mapping.py`, `tests/microbenchmarks/bench_moe/search.py`, `tests/microbenchmarks/bench_moe/specs.py`_
- **2026-07-27** [`49e16c983d`](https://github.com/NVIDIA/TensorRT-LLM/commit/49e16c983d) [#16203](https://github.com/NVIDIA/TensorRT-LLM/pull/16203)
  [https://nvbugs/6433376][fix] Update the Dense test to mirror the MoE sibling — assert `bfloat16` under… (#16203)
  _Files: `tests/integration/test_lists/waives.txt`_

## Torch Path (_torch)  (17 commits)

- **2026-08-03** [`9cc292ce00`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cc292ce00) [#17047](https://github.com/NVIDIA/TensorRT-LLM/pull/17047)
  [None][test] add e2e key model perf test (#17047)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-03** [`64eae0800e`](https://github.com/NVIDIA/TensorRT-LLM/commit/64eae0800e) [#17049](https://github.com/NVIDIA/TensorRT-LLM/pull/17049)
  [https://nvbugs/6528742][test] Disable V2 in legacy Mamba test (#17049)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-07-31** [`0a0de1c3ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a0de1c3ed) [#16906](https://github.com/NVIDIA/TensorRT-LLM/pull/16906)
  [None][perf] Fuse QK-norm + RoPE and overlap qkv/idx_qk math (#16906)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/unittest/_torch/models/test_minimax_m3.py`_
- **2026-07-31** [`55d55ff4f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/55d55ff4f3) [#17091](https://github.com/NVIDIA/TensorRT-LLM/pull/17091)
  [None][perf] AllReduce + ResidualAdd + RMSNorm (#17091)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`_
- **2026-07-31** [`066bab170a`](https://github.com/NVIDIA/TensorRT-LLM/commit/066bab170a) [#16690](https://github.com/NVIDIA/TensorRT-LLM/pull/16690)
  [None][feat] Support the DMD2-distilled Cosmos3 4-step image-to-video checkpoint (#16690)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py` _+7 more__
- **2026-07-31** [`8e602fa520`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e602fa520) [#17057](https://github.com/NVIDIA/TensorRT-LLM/pull/17057)
  [None][refactor] Clean up model paths and remove deprecated configurations in performance tests (#17057)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/sampler_options_config.py`_
- **2026-07-30** [`a146f66933`](https://github.com/NVIDIA/TensorRT-LLM/commit/a146f66933) [#16905](https://github.com/NVIDIA/TensorRT-LLM/pull/16905)
  [None][perf] Fused SwiGLU-OAI (#16905)
  _Files: `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/_torch/modules/swiglu.py` _+1 more__
- **2026-07-30** [`6eb951e28c`](https://github.com/NVIDIA/TensorRT-LLM/commit/6eb951e28c) [#15095](https://github.com/NVIDIA/TensorRT-LLM/pull/15095)
  [https://nvbugs/6276841][fix] When torch_compile=True, pass kv_cache_config=KvCacheConfig(free_gpu_memory_fra… (#15095)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`eed4d5ae31`](https://github.com/NVIDIA/TensorRT-LLM/commit/eed4d5ae31) [#16926](https://github.com/NVIDIA/TensorRT-LLM/pull/16926)
  [https://nvbugs/6517842][fix] Handle mutable tensor lists in remove c… (#16926)
  _Files: `tensorrt_llm/_torch/compilation/remove_copy_pass.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/compilation/test_remove_copy_pass.py`_
- **2026-07-30** [`78ab4e71ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/78ab4e71ce) [#16563](https://github.com/NVIDIA/TensorRT-LLM/pull/16563)
  [None][feat] Support the DMD2-distilled Cosmos3-Super-Text2Image-4Step checkpoint (#16563)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/configs/cosmos3-t2i-1gpu.yaml`, `examples/visual_gen/models/cosmos3/README.md` _+14 more__
- **2026-07-29** [`4b9012b965`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b9012b965) [#16904](https://github.com/NVIDIA/TensorRT-LLM/pull/16904)
  [None][perf] Fuse index-q/index-k projections in MinimaxM3 (#16904)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/unittest/_torch/models/test_minimax_m3.py`_
- **2026-07-29** [`fa5be69a98`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa5be69a98) [#16817](https://github.com/NVIDIA/TensorRT-LLM/pull/16817)
  [None][feat] Multimodal encoder cache: per-item partial hits (#16817)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tests/unittest/_torch/multimodal/test_multimodal_mixin.py`_
- **2026-07-29** [`af64dffab1`](https://github.com/NVIDIA/TensorRT-LLM/commit/af64dffab1) [#16716](https://github.com/NVIDIA/TensorRT-LLM/pull/16716)
  [TRTLLM-14551][perf] avoid GDN state reset host synchronization (#16716)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_gdn_kernel_optimizations.py`_
- **2026-07-29** [`e240d4a435`](https://github.com/NVIDIA/TensorRT-LLM/commit/e240d4a435) [#16794](https://github.com/NVIDIA/TensorRT-LLM/pull/16794)
  [TRTLLM-14571][infra] Enable container-local AutoTuner cache in CI (#16794)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/autotuner.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-07-29** [`9d508eb1e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d508eb1e9) [#16782](https://github.com/NVIDIA/TensorRT-LLM/pull/16782)
  [TRTLLM-14541][fix] VisualGen: deterministic autotuner tactics across runs and ranks (#16782)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/visual_gen/cuda_graph_runner.py`, `tensorrt_llm/_torch/visual_gen/mapping.py`, `tensorrt_llm/_torch/visual_gen/pipeline.py` _+3 more__
- **2026-07-27** [`9fe5853263`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fe5853263) [#16677](https://github.com/NVIDIA/TensorRT-LLM/pull/16677)
  [None][feat] VisualGen TP with Attn2D (#16677)
  _Files: `tensorrt_llm/_torch/visual_gen/mapping.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/unittest/_torch/visual_gen/multi_gpu/test_visual_gen_mapping.py` _+1 more__
- **2026-07-27** [`7982aa9701`](https://github.com/NVIDIA/TensorRT-LLM/commit/7982aa9701) [#16844](https://github.com/NVIDIA/TensorRT-LLM/pull/16844)
  [https://nvbugs/6501376][fix] Test-only fix — drop the `if hidden_size % 2 != 0: with pytest.raises(...)`… (#16844)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/multi_gpu/test_linear.py`_

## Other  (12 commits)

- **2026-08-03** [`37335543e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/37335543e6) [#17101](https://github.com/NVIDIA/TensorRT-LLM/pull/17101)
  [None][test] Add back new ctx and gen only case (#17101)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`_
- **2026-07-31** [`9f2d3c66f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f2d3c66f9) [#16752](https://github.com/NVIDIA/TensorRT-LLM/pull/16752)
  [None][feat] Log running metric estimates during long lm-eval runs (#16752)
  _Files: `tensorrt_llm/evaluate/lm_eval.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/others/test_lm_eval.py`_
- **2026-07-30** [`5b6a3e5195`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b6a3e5195) [#16964](https://github.com/NVIDIA/TensorRT-LLM/pull/16964)
  [None][test] Stabilize TRTLLM scaffolding worker test (#16964)
  _Files: `tests/unittest/scaffolding/test_worker.py`_
- **2026-07-30** [`1b0b2aef33`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b0b2aef33) [#16966](https://github.com/NVIDIA/TensorRT-LLM/pull/16966)
  [None][test] Stabilize scaffolding LLM tests (#16966)
  _Files: `tests/unittest/scaffolding/test_scaffolding.py`_
- **2026-07-30** [`c0df3b382f`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0df3b382f) [#16988](https://github.com/NVIDIA/TensorRT-LLM/pull/16988)
  [None][test] update coderabbit prompt (#16988)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-07-30** [`d0543dc1cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0543dc1cd) [#16851](https://github.com/NVIDIA/TensorRT-LLM/pull/16851)
  [None][fix] Increase max top logprobs limit (#16851)
  _Files: `tensorrt_llm/sampling_params.py`_
- **2026-07-29** [`c45ad837c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/c45ad837c5) [#16820](https://github.com/NVIDIA/TensorRT-LLM/pull/16820)
  [https://nvbugs/6163690][fix] Use PreTrainedTokenizerFast in trtllm-bench prepare_dataset to avoid NemotronH config parsing error (#16820)
  _Files: `tensorrt_llm/bench/dataset/prepare_dataset.py`_
- **2026-07-29** [`ebd197f776`](https://github.com/NVIDIA/TensorRT-LLM/commit/ebd197f776) [#16403](https://github.com/NVIDIA/TensorRT-LLM/pull/16403)
  [TRTLLM-13409][test] fail fast + surface server logs when a perf-sanity server dies or never becomes healthy (#16403)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/test-db/l0_cpu_arm.yml`, `tests/integration/test_lists/test-db/l0_cpu_x86.yml`, `tests/test_common/error_utils.py` _+2 more__
- **2026-07-29** [`87afac8d3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/87afac8d3e) [#15329](https://github.com/NVIDIA/TensorRT-LLM/pull/15329)
  [#15327][feat] Add per-request priority support to OpenAI chat/completions (#15329)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/api_stability/references/trtllm_serve_api.yaml`_
- **2026-07-28** [`a63ef1f132`](https://github.com/NVIDIA/TensorRT-LLM/commit/a63ef1f132) [#16853](https://github.com/NVIDIA/TensorRT-LLM/pull/16853)
  [None][test] Stabilize scaffolding OpenAI worker tests (#16853)
  _Files: `tests/unittest/scaffolding/test_worker.py`_
- **2026-07-27** [`e95cb90e16`](https://github.com/NVIDIA/TensorRT-LLM/commit/e95cb90e16) [#16884](https://github.com/NVIDIA/TensorRT-LLM/pull/16884)
  [None][fix] Drop stale benchmarks copies from Dockerfile.multi (#16884)
  _Files: `docker/Dockerfile.multi`_
- **2026-07-27** [`9f5b377664`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f5b377664) [#16894](https://github.com/NVIDIA/TensorRT-LLM/pull/16894)
  [None][test] Adjust timeout cases in QA perf test (#16894)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_

## Speculative Decoding  (12 commits)

- **2026-07-31** [`376d21939b`](https://github.com/NVIDIA/TensorRT-LLM/commit/376d21939b) [#16990](https://github.com/NVIDIA/TensorRT-LLM/pull/16990)
  [None][fix] reserve draft KV at disagg transition for gen-only-dspark case (#16990)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_kv_cache_v2_capacity_only.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-07-31** [`d91d41a43e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d91d41a43e) [#17128](https://github.com/NVIDIA/TensorRT-LLM/pull/17128)
  [https://nvbugs/6451425][fix] Remove llama3 eagle test waive (#17128)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-31** [`b118fc3580`](https://github.com/NVIDIA/TensorRT-LLM/commit/b118fc3580) [#17033](https://github.com/NVIDIA/TensorRT-LLM/pull/17033)
  [TRTLLM-14779][fix] Clear capture-only sampling override from cached CUDA graph metadata (#17033)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/speculative/test_capture_override_leak.py`_
- **2026-07-31** [`2fa17cbf3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fa17cbf3d) [#15343](https://github.com/NVIDIA/TensorRT-LLM/pull/15343)
  [https://nvbugs/6287561][fix] Add `get_sm_version() < 90` check at the top of `run_MTP()` in… (#15343)
  _Files: `examples/llm-api/llm_speculative_decoding.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`353a4ee254`](https://github.com/NVIDIA/TensorRT-LLM/commit/353a4ee254) [#16762](https://github.com/NVIDIA/TensorRT-LLM/pull/16762)
  [None][fix] SpecDecOneEngineForCausalLM: accept optional hidden_size/vocab_size for composite configs (#16762)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`, `tests/unittest/_torch/modeling/test_modeling_speculative.py`_
- **2026-07-30** [`2a5baabf8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a5baabf8e) [#16759](https://github.com/NVIDIA/TensorRT-LLM/pull/16759)
  [None][fix] SA spec dec: promote accepted hybrid recurrent states in-worker (#16759)
  _Files: `tensorrt_llm/_torch/speculative/sa_worker.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/speculative/test_sa_hybrid_state_promotion.py`_
- **2026-07-29** [`99bdffc4c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/99bdffc4c3) [#16717](https://github.com/NVIDIA/TensorRT-LLM/pull/16717)
  [https://nvbugs/6487040][test] Wait for gen-log end-of-write sentinel before parsing per-iter step time (#16717)
  _Files: `jenkins/scripts/perf/disaggregated/slurm_launch_draft.sh`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`b883d55139`](https://github.com/NVIDIA/TensorRT-LLM/commit/b883d55139) [#16674](https://github.com/NVIDIA/TensorRT-LLM/pull/16674)
  [None][feat] cache transceiver test in Perf sanity (#16674)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/report.py`, `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/disaggregated/slurm_ct_precheck_gate.sh` _+16 more__
- **2026-07-29** [`2b2bf97f83`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b2bf97f83) [#16938](https://github.com/NVIDIA/TensorRT-LLM/pull/16938)
  [None][fix] enable static EPLB for the one-model DSpark drafter (#16938)
  _Files: `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dspark_eplb_config.py`_
- **2026-07-29** [`097cbc102b`](https://github.com/NVIDIA/TensorRT-LLM/commit/097cbc102b) [#16832](https://github.com/NVIDIA/TensorRT-LLM/pull/16832)
  [https://nvbugs/6503299][fix] Default fabric memory KV pool for Python cache transceiver (#16832)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_gpt-oss-120b-fp4_1k1k_con64_ctx1_tp1_gen1_tp4_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_gpt-oss-120b-fp4_8k1k_con1024_ctx1_tp1_gen1_tp4_eplb0_mtp0_ccb-NIXL.yaml` _+6 more__
- **2026-07-28** [`1f1acea26d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f1acea26d) [#16594](https://github.com/NVIDIA/TensorRT-LLM/pull/16594)
  [TRTLLM-13233][feat] Support no_repeat_ngram_size in TorchSampler and refactor token-ban handling into its own submodule (#16594)
  _Files: `.pre-commit-config.yaml`, `docs/source/features/sampling.md`, `pyproject.toml`, `tensorrt_llm/_torch/pyexecutor/llm_request.py` _+7 more__
- **2026-07-27** [`93924532ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/93924532ff) [#16805](https://github.com/NVIDIA/TensorRT-LLM/pull/16805)
  [None][fix] Fix disaggregated draft token accounting (#16805)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/createNewDecoderRequests.cpp`, `cpp/tests/unit_tests/batch_manager/llmRequestTest.cpp`, `tests/unittest/_torch/executor/test_request_utils.py` _+1 more__

## Disaggregation / KV  (11 commits)

- **2026-08-03** [`aa535e5d41`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa535e5d41) [#16908](https://github.com/NVIDIA/TensorRT-LLM/pull/16908)
  [TRTLLM-13948][feat] Set DeepSeekV3 to use Python KV-cache transceiver V2 by default (#16908)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml` _+2 more__
- **2026-08-03** [`ef1e9f5f6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef1e9f5f6f) [#17099](https://github.com/NVIDIA/TensorRT-LLM/pull/17099)
  [None][test] Add back 1k1k cases for qa side (#17099)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1024_ctx1_dep4_gen1_dep32_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con3072_ctx1_dep4_gen1_dep4_eplb0_mtp1_ccb-NIXL.yaml` _+6 more__
- **2026-07-31** [`37a7c09818`](https://github.com/NVIDIA/TensorRT-LLM/commit/37a7c09818) [#16961](https://github.com/NVIDIA/TensorRT-LLM/pull/16961)
  [https://nvbugs/6510284][fix] Clamp benchmark fill target in PyExecutor (#16961)
  _Files: `examples/disaggregated/slurm/benchmark/submit.py`, `jenkins/scripts/perf/benchmark_utils.py`, `jenkins/scripts/perf/local/submit.py`, `jenkins/scripts/perf/submit.py` _+3 more__
- **2026-07-31** [`19bdfd3136`](https://github.com/NVIDIA/TensorRT-LLM/commit/19bdfd3136) [#16668](https://github.com/NVIDIA/TensorRT-LLM/pull/16668)
  [TRTLLM-14511][feat] BREAKING: refactor per-request perf metrics for multi-process trtllm-server (#16668)
  _Files: `examples/disaggregated/slurm/benchmark/run_benchmark_aiperf.sh`, `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/scaffolding/task.py` _+30 more__
- **2026-07-31** [`d924d9f185`](https://github.com/NVIDIA/TensorRT-LLM/commit/d924d9f185) [#16300](https://github.com/NVIDIA/TensorRT-LLM/pull/16300)
  [TRTLLM-14010][feat] report KV cache transfer state on executor hangs (#16300)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/cacheTransceiver.cpp`, `tensorrt_llm/_torch/disaggregation/transceiver.py` _+4 more__
- **2026-07-30** [`7f7dccf991`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f7dccf991) [#14047](https://github.com/NVIDIA/TensorRT-LLM/pull/14047)
  [None][feat] KVCacheManagerV2 C++ translation (#14047)
  _Files: `.github/CODEOWNERS`, `.pre-commit-config.yaml`, `LICENSE`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt` _+88 more__
- **2026-07-29** [`38389f931d`](https://github.com/NVIDIA/TensorRT-LLM/commit/38389f931d) [#16941](https://github.com/NVIDIA/TensorRT-LLM/pull/16941)
  [https://nvbugs/6465993][fix] unwaive mamba tests (#16941)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`feb83eccd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/feb83eccd0) [#16697](https://github.com/NVIDIA/TensorRT-LLM/pull/16697)
  [https://nvbugs/6226016][fix] Avoid trusting request-controlled router tokenizers (#16697)
  _Files: `tensorrt_llm/serve/router_utils.py`, `tests/unittest/disaggregated/test_router.py`_
- **2026-07-28** [`c82ae76009`](https://github.com/NVIDIA/TensorRT-LLM/commit/c82ae76009) [#16893](https://github.com/NVIDIA/TensorRT-LLM/pull/16893)
  [https://nvbugs/6503293][fix] Restore whole-node GPU visibility for default packing (#16893)
  _Files: `examples/disaggregated/slurm/benchmark/start_worker.sh`, `examples/disaggregated/slurm/benchmark/submit.py`_
- **2026-07-28** [`53659b14b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/53659b14b9) [#16931](https://github.com/NVIDIA/TensorRT-LLM/pull/16931)
  [None][test] Fix test_perf.py to accept kv cache manager v2 format (#16931)
  _Files: `tests/integration/defs/perf/test_perf.py`_
- **2026-07-27** [`b91ffdad91`](https://github.com/NVIDIA/TensorRT-LLM/commit/b91ffdad91) [#16355](https://github.com/NVIDIA/TensorRT-LLM/pull/16355)
  [TRTLLM-13642][feat] Add perf sanity tests for Llama-3.1-8B and Gemma-3-1B and verify cache transceiver V2 support (#16355)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/scripts/perf-sanity/disaggregated/gb200_gemma-3-1b-bf16_1k1k_con256_ctx1_tp1_gen1_tp1_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_llama-3.1-8b-bf16_1k1k_con256_ctx1_tp1_gen1_tp1_eplb0_mtp0_ccb-NIXL.yaml`_

## Quantization  (10 commits)

- **2026-08-02** [`0a462b2d82`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a462b2d82)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+9 more__
- **2026-07-31** [`78a1e6adf9`](https://github.com/NVIDIA/TensorRT-LLM/commit/78a1e6adf9) [#16672](https://github.com/NVIDIA/TensorRT-LLM/pull/16672)
  [https://nvbugs/6478692][fix] Pass `max_workers=16` to `_build` in `EPDVariant.nano_omni_fp8` (mirroring… (#16672)
  _Files: `tests/integration/defs/accuracy/test_epd_disagg_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`8624ec9726`](https://github.com/NVIDIA/TensorRT-LLM/commit/8624ec9726) [#16933](https://github.com/NVIDIA/TensorRT-LLM/pull/16933)
  [https://nvbugs/6424956][fix] Support large FP8 quantization grids (#16933)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu`, `tests/unittest/_torch/thop/parallel/test_fp8_quantize.py`_
- **2026-07-29** [`2f113fdb29`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f113fdb29) [#16997](https://github.com/NVIDIA/TensorRT-LLM/pull/16997)
  [https://nvbugs/6210714][test] Unwaive TestQwen3_5_35B_A3B fp8 block reuse test (#16997)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-29** [`4235bef946`](https://github.com/NVIDIA/TensorRT-LLM/commit/4235bef946) [#16095](https://github.com/NVIDIA/TensorRT-LLM/pull/16095)
  [TRTLLM-14135][feat] Add Qwen-Image-Edit-2511 support (#16095)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/qwen-image-edit-2511-fp8-1gpu.yaml` _+10 more__
- **2026-07-28** [`78dd19c2f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/78dd19c2f5) [#15762](https://github.com/NVIDIA/TensorRT-LLM/pull/15762)
  [TRTLLM-11780][feat] Wan 2.2 layernorm + shiftscale + quant fusion (#15762)
  _Files: `cpp/tensorrt_llm/kernels/fusedAdaptiveLayerNormKernel.cu`, `cpp/tensorrt_llm/kernels/fusedAdaptiveLayerNormKernel.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/fusedAdaptiveLayerNormOp.cpp` _+6 more__
- **2026-07-28** [`becf773b5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/becf773b5a) [#16833](https://github.com/NVIDIA/TensorRT-LLM/pull/16833)
  [None][fix] Fix nemotron-h quant and loading config (#16833)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_h_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_utils.py`_
- **2026-07-27** [`aae253ef60`](https://github.com/NVIDIA/TensorRT-LLM/commit/aae253ef60) [#12705](https://github.com/NVIDIA/TensorRT-LLM/pull/12705)
  [#15673][fix] Enable CUDA core fast path for SM89/SM120/SM121 (#12705)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/quant.py`, `tensorrt_llm/_torch/modules/linear.py`_
- **2026-07-27** [`55e9b2fe92`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e9b2fe92) [#16831](https://github.com/NVIDIA/TensorRT-LLM/pull/16831)
  [None][fix] Resolve NVFP4 mixed-precision base layers for the DSpark draft (#16831)
  _Files: `tensorrt_llm/_torch/models/modeling_dspark.py`_
- **2026-07-27** [`da39470b13`](https://github.com/NVIDIA/TensorRT-LLM/commit/da39470b13) [#16878](https://github.com/NVIDIA/TensorRT-LLM/pull/16878)
  [https://nvbugs/6479324][test] Remove waiver for fixed qwen3_5_4b_fp8_stress disaggregated stress test (#16878)
  _Files: `tests/integration/test_lists/waives.txt`_

## Models  (7 commits)

- **2026-08-03** [`48a42a674a`](https://github.com/NVIDIA/TensorRT-LLM/commit/48a42a674a) [#17197](https://github.com/NVIDIA/TensorRT-LLM/pull/17197)
  [None][test] Update performance test configuration for qwen3 model to reduce request count from 256 to 64, optimizing resource usage during benchmarking (#17197)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-07-30** [`5c5ef98866`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c5ef98866) [#16975](https://github.com/NVIDIA/TensorRT-LLM/pull/16975)
  [https://nvbugs/6305404][chore] Unwaive DeepSeek V3 Lite L0 test (#16975)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-30** [`c083da6b64`](https://github.com/NVIDIA/TensorRT-LLM/commit/c083da6b64) [#16384](https://github.com/NVIDIA/TensorRT-LLM/pull/16384)
  [TRTLLM-14287][feat] Qwen Image CFG parallelism support (#16384)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/qwen_image/pipeline_qwen_image.py`, `tests/unittest/_torch/visual_gen/test_qwen_image_infer.py` _+2 more__
- **2026-07-29** [`2341c704a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2341c704a6) [#16936](https://github.com/NVIDIA/TensorRT-LLM/pull/16936)
  [None][fix] Fix Qwen3.5 weight-load memory growth and MTP CUTLASS fallback (#16936)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_weight_loader.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/models/modeling_utils.py`_
- **2026-07-29** [`09d87155de`](https://github.com/NVIDIA/TensorRT-LLM/commit/09d87155de) [#16924](https://github.com/NVIDIA/TensorRT-LLM/pull/16924)
  [https://nvbugs/6255417][fix] Unwaive qwen3next ci test (#16924)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-28** [`cfebf191f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfebf191f3) [#15096](https://github.com/NVIDIA/TensorRT-LLM/pull/15096)
  [None][feat] Add Qwen-Image-Layered baseline support (#15096)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/qwen-image-layered-1gpu.yaml` _+13 more__
- **2026-07-28** [`798e419524`](https://github.com/NVIDIA/TensorRT-LLM/commit/798e419524) [#16891](https://github.com/NVIDIA/TensorRT-LLM/pull/16891)
  [https://nvbugs/6479837][fix] Fix OOM of Qwen3_5_35B on a single a100 (#16891)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_

## Docs / Examples  (1 commits)

- **2026-08-03** [`1a00238748`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a00238748) [#17161](https://github.com/NVIDIA/TensorRT-LLM/pull/17161)
  [TRTLLM-14772][doc] Add sudo to apt prerequisites (#17161)
  _Files: `docs/source/installation/build-from-source.md`_

## ROCm / AMD  (1 commits)

- **2026-07-28** [`2a7231d0de`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a7231d0de) [#16932](https://github.com/NVIDIA/TensorRT-LLM/pull/16932)
  [None][test] Update CODEOWNERS to refine QA ownership by adding specific roles for performance/function/serving testing (#16932)
  _Files: `.github/CODEOWNERS`_

## Perf  (1 commits)

- **2026-07-27** [`08289b629f`](https://github.com/NVIDIA/TensorRT-LLM/commit/08289b629f) [#16799](https://github.com/NVIDIA/TensorRT-LLM/pull/16799)
  [None][perf] Optimize Blackwell fused MHC half-MMA kernel (#16799)
  _Files: `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`_

---
_Generated 2026-08-03 11:41 UTC_