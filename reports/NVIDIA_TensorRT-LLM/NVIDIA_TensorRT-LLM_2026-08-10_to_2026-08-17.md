# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-08-10 → 2026-08-17  |  **Total commits:** 226

## ✨ New Features This Week

- **2026-08-17** [#17487](https://github.com/NVIDIA/TensorRT-LLM/pull/17487) — [TRTLLM-14833][chore] Introduce executor/ray/ for Ray executor integration (#17487)
- **2026-08-17** [#16914](https://github.com/NVIDIA/TensorRT-LLM/pull/16914) — [None][feat] Support DFlash RoPE, sliding-window configuration, and TRTLLM-gen attention backend (#16914)
- **2026-08-17** [#17599](https://github.com/NVIDIA/TensorRT-LLM/pull/17599) — [None][feat] Honor SamplingParams.seed on the one-model speculative path (#17599)
- **2026-08-17** [#17404](https://github.com/NVIDIA/TensorRT-LLM/pull/17404) — [None][infra] Add execution and test-runner skills for Claude Code (#17404)
- **2026-08-17** [#16051](https://github.com/NVIDIA/TensorRT-LLM/pull/16051) — [None][feat] Enforce multimodal encoder runtime budgets with budgeted output storage (#16051)
- **2026-08-16** [#17532](https://github.com/NVIDIA/TensorRT-LLM/pull/17532) — [TRTLLM-14956][refactor] make MoE implementation selection reproducible (#17532)
- **2026-08-15** [#17624](https://github.com/NVIDIA/TensorRT-LLM/pull/17624) — [TRTLLM-15284][feat] add Kimi K3 SiTU MegaMoE support (#17624)
- **2026-08-15** [#16609](https://github.com/NVIDIA/TensorRT-LLM/pull/16609) — [TRTLLM-13579][feat] BREAKING: Support BCG in Prefill (#16609)
- **2026-08-15** [#15562](https://github.com/NVIDIA/TensorRT-LLM/pull/15562) — [None][feat] Add HunyuanVideo 1.5 text-to-video support to VisualGen (#15562)
- **2026-08-15** [#17317](https://github.com/NVIDIA/TensorRT-LLM/pull/17317) — [TRTLLM-13694][infra] Add benchmark refresh mappings (#17317)
- _…and 28 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-12** [`3d3d7c9192`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d3d7c9192) [#17223](https://github.com/NVIDIA/TensorRT-LLM/pull/17223) — [https://nvbugs/6480621][fix] Preserve KV ownership in disaggregated precheck (#17223)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17714](https://github.com/NVIDIA/TensorRT-LLM/issues/17714) | [Feature] NcclEP backend hardcodes LOW_LATENCY + RANK_MAJOR; algorithm | Scale-out | 2026-08-14 |
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-08-13 |
| [#17522](https://github.com/NVIDIA/TensorRT-LLM/issues/17522) | [Bug]: causal_conv1d_triton overwrites conv_state while the convolutio | bug, Triton backend | 2026-08-12 |
| [#10014](https://github.com/NVIDIA/TensorRT-LLM/issues/10014) | [Documentation] AWS EFA/LIBFABRIC deployment guide for disaggregated i | Doc, Disaggregated serving | 2026-08-12 |
| [#16827](https://github.com/NVIDIA/TensorRT-LLM/issues/16827) | [Performance]: MAX_UTILIZATION causes a 40.6% output-throughput drop a | KV-Cache Management, Pytorch, General perf | 2026-08-09 |
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-08-09 |
| [#17437](https://github.com/NVIDIA/TensorRT-LLM/issues/17437) | [Bug]: Interior control-token rejection can split a tool-call prelude  | Speculative Decoding | 2026-08-08 |
| [#17016](https://github.com/NVIDIA/TensorRT-LLM/issues/17016) | [RFC]: Add openengine gRPC server support to trtllm-serve | RFC | 2026-08-03 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-07-29 |
| [#17020](https://github.com/NVIDIA/TensorRT-LLM/issues/17020) | `trtllm-eval aime25`/`aime26` silently disable thinking on DeepSeek-V4 | — | 2026-07-29 |
| [#17013](https://github.com/NVIDIA/TensorRT-LLM/issues/17013) | [RFC]: Reduce overhead in KV cache event publishing | RFC | 2026-07-29 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-07-25 |
| [#16459](https://github.com/NVIDIA/TensorRT-LLM/issues/16459) | [Bug]: Preserve per-item processed metadata when computing multimodal  | Multimodal | 2026-07-21 |
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-26 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |
| [#14100](https://github.com/NVIDIA/TensorRT-LLM/issues/14100) | [Bug] trtllm-serve /v1/chat/completions: audio_url with data: URI base | bug, Multimodal | 2026-05-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 72 |
| Executor / Runtime | 27 |
| Attention | 24 |
| MoE | 20 |
| Quantization | 17 |
| Disaggregation / KV | 15 |
| Speculative Decoding | 14 |
| Models | 11 |
| Torch Path (_torch) | 10 |
| Other | 9 |
| AutoDeploy | 2 |
| Docs / Examples | 2 |
| Perf | 1 |
| LoRA | 1 |
| ROCm / AMD | 1 |

## CI / Infra  (72 commits)

- **2026-08-17** [`e8965de35d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8965de35d) [#17807](https://github.com/NVIDIA/TensorRT-LLM/pull/17807)
  [None][test] Waive 5 failed cases for main in QA CI (#17807)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`4992541c3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/4992541c3a)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-17** [`4111a2a2b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/4111a2a2b8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-08-17** [`2a56053367`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a56053367)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-17** [`988ae8b70b`](https://github.com/NVIDIA/TensorRT-LLM/commit/988ae8b70b) [#17785](https://github.com/NVIDIA/TensorRT-LLM/pull/17785)
  [None][infra] Remove stale perf-sanity waives orphaned by #17609 (#17785)
- **2026-08-17** [`a098858cef`](https://github.com/NVIDIA/TensorRT-LLM/commit/a098858cef) [#17782](https://github.com/NVIDIA/TensorRT-LLM/pull/17782)
  [None][test] Waive two pre-existing DGX_B200 test failures (#17782)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-16** [`210397bedc`](https://github.com/NVIDIA/TensorRT-LLM/commit/210397bedc) [#17679](https://github.com/NVIDIA/TensorRT-LLM/pull/17679)
  [TRTLLMINF-263][infra] authenticate Artifactory nSpect checks (#17679)
  _Files: `jenkins/BuildDockerImage.groovy`_
- **2026-08-16** [`f7110c9f98`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7110c9f98) [#17776](https://github.com/NVIDIA/TensorRT-LLM/pull/17776)
  [None][infra] Waive 1 failed cases for main in pre-merge 54155 (#17776)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-16** [`7ec2a9df3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7ec2a9df3a) [#17775](https://github.com/NVIDIA/TensorRT-LLM/pull/17775)
  [None][infra] Waive 3 failed cases for main in pre-merge 54155 (#17775)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-15** [`07b4848e38`](https://github.com/NVIDIA/TensorRT-LLM/commit/07b4848e38) [#17317](https://github.com/NVIDIA/TensorRT-LLM/pull/17317)
  [TRTLLM-13694][infra] Add benchmark refresh mappings (#17317)
  _Files: `examples/configs/benchmark_refresh_mappings.yaml`_
- **2026-08-15** [`d9c89749d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9c89749d7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-14** [`91107edc70`](https://github.com/NVIDIA/TensorRT-LLM/commit/91107edc70) [#17722](https://github.com/NVIDIA/TensorRT-LLM/pull/17722)
  [https://nvbugs/6550708][test] Unwaive Cosmos3 distilled unit tests fixed by #17212 (#17722)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-14** [`c295f65b7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c295f65b7e) [#17712](https://github.com/NVIDIA/TensorRT-LLM/pull/17712)
  [https://nvbugs/6611817][test] Waive known-flaky disagg + Nemotron tests on DGX_H100 (#17712)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-14** [`7a3b1bf500`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a3b1bf500) [#17704](https://github.com/NVIDIA/TensorRT-LLM/pull/17704)
  [TRTLLMINF-40][fix] Quote SLURM no-job-ID cleanup echo so it no longer exits 127 (#17704)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-14** [`b5bdcf1dd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5bdcf1dd9)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-14** [`87aa25c434`](https://github.com/NVIDIA/TensorRT-LLM/commit/87aa25c434) [#17117](https://github.com/NVIDIA/TensorRT-LLM/pull/17117)
  [https://nvbugs/6427411][test] Re-enable PP regression tests (#17117)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-14** [`ec3cd38c95`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec3cd38c95) [#17615](https://github.com/NVIDIA/TensorRT-LLM/pull/17615)
  [TRTLLMINF-311][infra] Infra-scoped fail-fast: defer K8s infra aborts instead of cascading (#17615)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/TensorRT_LLM_PLC.groovy`, `jenkins/runPerfSanityTriage.groovy`_
- **2026-08-14** [`1ec05bc3cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ec05bc3cf) [#17702](https://github.com/NVIDIA/TensorRT-LLM/pull/17702)
  [None][infra] Waive 1 failed cases for main in pre-merge 53814 (#17702)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-14** [`22d1defd54`](https://github.com/NVIDIA/TensorRT-LLM/commit/22d1defd54) [#17682](https://github.com/NVIDIA/TensorRT-LLM/pull/17682)
  [None][infra] Improve the messages for determining whether failed tests should be r… (#17682)
  _Files: `jenkins/scripts/test_rerun.py`_
- **2026-08-14** [`acdf42664c`](https://github.com/NVIDIA/TensorRT-LLM/commit/acdf42664c)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-14** [`9ff67eba1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ff67eba1e)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-14** [`b51abefc90`](https://github.com/NVIDIA/TensorRT-LLM/commit/b51abefc90) [#17634](https://github.com/NVIDIA/TensorRT-LLM/pull/17634)
  [TRTLLMINF-300][infra] fix slurm_install.sh use broken artifact (#17634)
  _Files: `jenkins/scripts/slurm_install.sh`_
- **2026-08-14** [`0dc0622cb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0dc0622cb9) [#17676](https://github.com/NVIDIA/TensorRT-LLM/pull/17676)
  [None][infra] Add blossom-ci authorized users (#17676)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-08-13** [`82ea383f16`](https://github.com/NVIDIA/TensorRT-LLM/commit/82ea383f16) [#17639](https://github.com/NVIDIA/TensorRT-LLM/pull/17639)
  [None][ci] Run doc build on a CPU pod instead of an a10 GPU tester (#17639)
  _Files: `docs/source/conf.py`, `jenkins/L0_Test.groovy`, `scripts/cuda_driver_stub.py`_
- **2026-08-13** [`581d1aeda2`](https://github.com/NVIDIA/TensorRT-LLM/commit/581d1aeda2) [#17652](https://github.com/NVIDIA/TensorRT-LLM/pull/17652)
  [None][infra] Waive 2 failed cases for main in pre-merge 53612 (#17652)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`dc8cf097fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc8cf097fa)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-13** [`71af059cbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/71af059cbe) [#17496](https://github.com/NVIDIA/TensorRT-LLM/pull/17496)
  [https://nvbugs/6422337][fix] Unwaive testcase (#17496)
- **2026-08-13** [`b414439f5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b414439f5a) [#17626](https://github.com/NVIDIA/TensorRT-LLM/pull/17626)
  [None][test] Waive 5 failed cases for main in QA CI (#17626)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`80d4d8d51d`](https://github.com/NVIDIA/TensorRT-LLM/commit/80d4d8d51d) [#17617](https://github.com/NVIDIA/TensorRT-LLM/pull/17617)
  [None][infra] Waive 4 failed cases for main in post-merge 2899 (#17617)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`ae760155dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae760155dd) [#17616](https://github.com/NVIDIA/TensorRT-LLM/pull/17616)
  [None][infra] Waive 2 failed cases for main in post-merge 2899 (#17616)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`c9116ef0e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9116ef0e0) [#17468](https://github.com/NVIDIA/TensorRT-LLM/pull/17468)
  [None][test] Waive 2 failed cases for main in QA CI (#17468)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`0232413048`](https://github.com/NVIDIA/TensorRT-LLM/commit/0232413048) [#17560](https://github.com/NVIDIA/TensorRT-LLM/pull/17560)
  [None][infra] Run mypy type check in the build stage without pre-commit (#17560)
  _Files: `.pre-commit-config.yaml`, `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`, `pyproject.toml` _+1 more__
- **2026-08-13** [`5fc252b13b`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fc252b13b) [#17383](https://github.com/NVIDIA/TensorRT-LLM/pull/17383)
  [TRTLLM-15157][infra] automate stale PR cleanup (#17383)
  _Files: `.github/scripts/cleanup_stale_prs.test.js`, `.github/workflows/cleanup-stale-prs.yml`, `.github/workflows/precommit-check.yml`, `CONTRIBUTING.md`_
- **2026-08-13** [`6e931c9587`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e931c9587) [#17253](https://github.com/NVIDIA/TensorRT-LLM/pull/17253)
  [None][infra] CBTS code coverage date early save (#17253)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-13** [`2da4a8899a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2da4a8899a) [#17593](https://github.com/NVIDIA/TensorRT-LLM/pull/17593)
  [None][infra] Waive 20 failed cases for main in post-merge 2899 (#17593)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-12** [`7fa3704047`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fa3704047)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-12** [`502cf6ceb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/502cf6ceb5) [#17219](https://github.com/NVIDIA/TensorRT-LLM/pull/17219)
  [https://nvbugs/6550803][fix] Pin `Mock(_force_non_greedy_for_capture=False)` at the test's spec_metadata… (#17219)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-12** [`3612c80eac`](https://github.com/NVIDIA/TensorRT-LLM/commit/3612c80eac) [#17263](https://github.com/NVIDIA/TensorRT-LLM/pull/17263)
  [TRTLLMINF-237][infra] Re-home L0_Test SLURM finalizer (#17263)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-12** [`3a3cbe7acc`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a3cbe7acc) [#17561](https://github.com/NVIDIA/TensorRT-LLM/pull/17561)
  [None][test] Waive test_kda_verify_matches_sequential_decode[2-1] (NaN on B200) (#17561)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-12** [`7f62928b90`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f62928b90) [#17547](https://github.com/NVIDIA/TensorRT-LLM/pull/17547)
  [None][infra] Allow normal review for waiver updates (#17547)
  _Files: `.github/CODEOWNERS`_
- **2026-08-12** [`69eea162cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/69eea162cd) [#17528](https://github.com/NVIDIA/TensorRT-LLM/pull/17528)
  [None][infra] Stop CodeRabbit requiring copyright header on test-list files (#17528)
  _Files: `.coderabbit.yaml`_
- **2026-08-12** [`07b3e82316`](https://github.com/NVIDIA/TensorRT-LLM/commit/07b3e82316) [#16374](https://github.com/NVIDIA/TensorRT-LLM/pull/16374)
  [None][test] Dump a stack traceback when a test hangs (#16374)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/conftest.py`, `tests/integration/defs/utils/periodic_junit.py`, `tests/unittest/tools/test_periodic_junit.py`_
- **2026-08-12** [`a35b8b58a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/a35b8b58a4) [#17542](https://github.com/NVIDIA/TensorRT-LLM/pull/17542)
  [None][infra] Waive 1 failed cases for main in pre-merge 53187 (#17542)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-12** [`ba1a48bffa`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba1a48bffa)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-12** [`59180efa1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/59180efa1c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-12** [`303720d4ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/303720d4ba)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-12** [`f10ad2504b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f10ad2504b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/metadata.json`_
- **2026-08-11** [`40739b13e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/40739b13e7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-11** [`6de751a0f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6de751a0f0) [#17517](https://github.com/NVIDIA/TensorRT-LLM/pull/17517)
  [None][infra] Waive 1 failed cases for main in pre-merge 53139 (#17517)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`4ffb1b2ab6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ffb1b2ab6) [#17504](https://github.com/NVIDIA/TensorRT-LLM/pull/17504)
  [https://nvbugs/6577550][chore] Waive TestNemotron3Super120B::test_ctx_dp2_gen_tp4 (#17504)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`b19a404981`](https://github.com/NVIDIA/TensorRT-LLM/commit/b19a404981)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-11** [`2d6300b089`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d6300b089)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-11** [`afe103e887`](https://github.com/NVIDIA/TensorRT-LLM/commit/afe103e887) [#16739](https://github.com/NVIDIA/TensorRT-LLM/pull/16739)
  [TRTLLMINF-191][infra] Use native pytest capture for S3 logs (#16739)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_run.sh`, `tests/integration/defs/pytest.ini`, `tests/integration/defs/test_unittests.py` _+5 more__
- **2026-08-11** [`27d22ed1b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/27d22ed1b9) [#17444](https://github.com/NVIDIA/TensorRT-LLM/pull/17444)
  [None][test] Remove 85 closed-bug waive entries for main (#17444)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`4985bf0bb6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4985bf0bb6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-11** [`fd2edbaae4`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd2edbaae4) [#17251](https://github.com/NVIDIA/TensorRT-LLM/pull/17251)
  [None][infra] Align VisualGen CBTS rule with CODEOWNERS scope (#17251)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/visual_gen_rule.py`_
- **2026-08-11** [`1a57877fcc`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a57877fcc) [#17359](https://github.com/NVIDIA/TensorRT-LLM/pull/17359)
  [None][infra] Replace --gpus with --gpus-per-node in single node multi gpus (#17359)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-11** [`0e2d5980f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e2d5980f7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-11** [`26c8d773c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/26c8d773c0)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/ray_orchestrator/pyproject.toml`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
- **2026-08-10** [`5c6d65b5b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c6d65b5b7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/triton_backend/poetry.lock`_
- **2026-08-10** [`b582572af4`](https://github.com/NVIDIA/TensorRT-LLM/commit/b582572af4) [#16970](https://github.com/NVIDIA/TensorRT-LLM/pull/16970)
  [TRTLLMINF-213][infra] Artifactory container image migration (#16970)
  _Files: `docker/Dockerfile.multi`, `docker/README.md`, `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy` _+7 more__
- **2026-08-10** [`7801d34fcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/7801d34fcf) [#17432](https://github.com/NVIDIA/TensorRT-LLM/pull/17432)
  [None][infra] Log infra-retry classify declines instead of silent rethrow (#17432)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-10** [`a76f5431e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/a76f5431e2) [#17459](https://github.com/NVIDIA/TensorRT-LLM/pull/17459)
  [https://nvbugs/6517846][fix] Raise AGG server-ready timeout to 3600s and unwaive 4 perf-sanity cases (#17459)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`9f92665449`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f92665449) [#17336](https://github.com/NVIDIA/TensorRT-LLM/pull/17336)
  [None][infra] Recognize SM107 (Rubin) in build config and arch detection (#17336)
  _Files: `cpp/cmake/modules/cuda_configuration.cmake`, `cpp/include/tensorrt_llm/common/cudaUtils.h`, `tensorrt_llm/_utils.py`, `tests/integration/defs/conftest.py`_
- **2026-08-10** [`762d1d4d63`](https://github.com/NVIDIA/TensorRT-LLM/commit/762d1d4d63) [#17467](https://github.com/NVIDIA/TensorRT-LLM/pull/17467)
  [None][test] Waive 5 failed cases for main in QA CI (#17467)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`07a559193f`](https://github.com/NVIDIA/TensorRT-LLM/commit/07a559193f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-10** [`3bffdc314e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bffdc314e) [#17418](https://github.com/NVIDIA/TensorRT-LLM/pull/17418)
  [https://nvbugs/6567065][fix] Unwaive some fixed cases (#17418)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`d0b5862877`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0b5862877)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-10** [`fa73933d22`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa73933d22) [#17458](https://github.com/NVIDIA/TensorRT-LLM/pull/17458)
  [None][infra] Waive 23 failed cases for main in post-merge 2894 (#17458)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`5761d00e50`](https://github.com/NVIDIA/TensorRT-LLM/commit/5761d00e50) [#17442](https://github.com/NVIDIA/TensorRT-LLM/pull/17442)
  [None][infra] Unwaive 5 disagg gen only cases (#17442)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`cba210a39d`](https://github.com/NVIDIA/TensorRT-LLM/commit/cba210a39d) [#17407](https://github.com/NVIDIA/TensorRT-LLM/pull/17407)
  [None][infra] Waive 12 failed cases for main in post-merge 2889 (#17407)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`5ea61f33df`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ea61f33df)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Executor / Runtime  (27 commits)

- **2026-08-17** [`7f4fb2e4d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f4fb2e4d6) [#17426](https://github.com/NVIDIA/TensorRT-LLM/pull/17426)
  [https://nvbugs/6566772][fix] Predicate `idle` on `not self.is_shutdown` so a non-blocking timedelta(0) is… (#17426)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`5b427d9d5d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b427d9d5d) [#17671](https://github.com/NVIDIA/TensorRT-LLM/pull/17671)
  [None][fix] Preserve advanced sampling state through graph capture (#17671)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-08-17** [`2c8522ef04`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c8522ef04) [#17601](https://github.com/NVIDIA/TensorRT-LLM/pull/17601)
  [TRTLLM-15100][test] Prune Nemotron-H functional and un… (#17601)
  _Files: `examples/llm-api/README.md`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` _+7 more__
- **2026-08-17** [`5e09668d0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e09668d0c) [#17487](https://github.com/NVIDIA/TensorRT-LLM/pull/17487)
  [TRTLLM-14833][chore] Introduce executor/ray/ for Ray executor integration (#17487)
  _Files: `.pre-commit-config.yaml`, `docs/source/features/ray-orchestrator.md`, `examples/ray_orchestrator/README.md`, `legacy-files.txt` _+24 more__
- **2026-08-17** [`b87359ec01`](https://github.com/NVIDIA/TensorRT-LLM/commit/b87359ec01) [#17494](https://github.com/NVIDIA/TensorRT-LLM/pull/17494)
  [TRTLLM-11628][perf] Batch the beam-search finish-reason reduction (#17494)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-08-17** [`eb3f6d4644`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb3f6d4644) [#17783](https://github.com/NVIDIA/TensorRT-LLM/pull/17783)
  [None][fix] Fix latent mypy errors in sampler.py (no-any-return, comparison-overlap) (#17783)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`b3e6813918`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3e6813918) [#16051](https://github.com/NVIDIA/TensorRT-LLM/pull/16051)
  [None][feat] Enforce multimodal encoder runtime budgets with budgeted output storage (#16051)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_gemma4_vision.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py` _+40 more__
- **2026-08-16** [`3704662de0`](https://github.com/NVIDIA/TensorRT-LLM/commit/3704662de0) [#17717](https://github.com/NVIDIA/TensorRT-LLM/pull/17717)
  [TRTLLM-15037][fix] KVCM-V2: synchronize auto host-tier quota across ranks (#17717)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`_
- **2026-08-14** [`807c4f6cef`](https://github.com/NVIDIA/TensorRT-LLM/commit/807c4f6cef) [#17677](https://github.com/NVIDIA/TensorRT-LLM/pull/17677)
  [https://nvbugs/6507082][fix] remove a test case of falcon model (#17677)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-08-14** [`09b77e8d5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/09b77e8d5a) [#16687](https://github.com/NVIDIA/TensorRT-LLM/pull/16687)
  [None][fix] Keep ADP ranks in collective lockstep on request errors and fail fast on desync (#16687)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_disagg_inflight_cancel_gate.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-13** [`1f17e7cc3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f17e7cc3f) [#17050](https://github.com/NVIDIA/TensorRT-LLM/pull/17050)
  [TRTLLM-14704][feat] Support multi-modal part of K3 (#17050)
  _Files: `.gitignore`, `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `examples/kimi_k3/README.md`, `examples/kimi_k3/perf_sweep/acc_sweep.sbatch` _+15 more__
- **2026-08-13** [`2e109b047b`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e109b047b) [#17189](https://github.com/NVIDIA/TensorRT-LLM/pull/17189)
  [TRTLLM-14865][feat] Support occurrence penalties with beam search for TorchSampler (#17189)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/penalties.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py` _+3 more__
- **2026-08-13** [`4dc7f4465c`](https://github.com/NVIDIA/TensorRT-LLM/commit/4dc7f4465c) [#17487](https://github.com/NVIDIA/TensorRT-LLM/pull/17487)
  [TRTLLM-14833][chore] Add compatibility shims for the relocated Ray modules (#17487)
  _Files: `tensorrt_llm/_ray_utils.py`, `tensorrt_llm/executor/ray_executor.py`, `tensorrt_llm/executor/ray_gpu_worker.py`, `tensorrt_llm/ray_stub.py` _+4 more__
- **2026-08-11** [`1d7f1330db`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d7f1330db) [#17487](https://github.com/NVIDIA/TensorRT-LLM/pull/17487)
  [TRTLLM-14833][chore] Introduce executor/ray/ for Ray executor integration (#17487)
  _Files: `.pre-commit-config.yaml`, `docs/source/features/ray-orchestrator.md`, `examples/ray_orchestrator/README.md`, `legacy-files.txt` _+16 more__
- **2026-08-12** [`3d30d20964`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d30d20964) [#17447](https://github.com/NVIDIA/TensorRT-LLM/pull/17447)
  [TRTLLM-15216][fix] Kimi K3 on KVCacheManagerV2: conv-state layout and SSM iteration stats (#17447)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py` _+3 more__
- **2026-08-12** [`f8befdc99c`](https://github.com/NVIDIA/TensorRT-LLM/commit/f8befdc99c) [#16921](https://github.com/NVIDIA/TensorRT-LLM/pull/16921)
  [https://nvbugs/6487039][fix] Generalize ADP dummy lifecycle (#16921)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py` _+6 more__
- **2026-08-12** [`157de10dd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/157de10dd1) [#16157](https://github.com/NVIDIA/TensorRT-LLM/pull/16157)
  [TRTLLM-12714][fix] Suspend CUDA-graph padding dummies before pool rebalance adjust() (#16157)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_kv_pool_rebalance.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`_
- **2026-08-12** [`6deb48c1b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/6deb48c1b5) [#17351](https://github.com/NVIDIA/TensorRT-LLM/pull/17351)
  [TRTLLM-15078][test] Remove all DeepSeek-R1-Distill-* tests (#17351)
  _Files: `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/base_perf_pytorch.csv` _+9 more__
- **2026-08-12** [`7a7f957f90`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a7f957f90) [#17345](https://github.com/NVIDIA/TensorRT-LLM/pull/17345)
  [TRTLLM-15076][test] Remove Bielik-11B-v2.2-Instruct an… (#17345)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/perf/_model_paths.py` _+4 more__
- **2026-08-11** [`d727c78646`](https://github.com/NVIDIA/TensorRT-LLM/commit/d727c78646) [#15187](https://github.com/NVIDIA/TensorRT-LLM/pull/15187)
  [#13318][fix] Gracefully fit token budget at prep boundary (#15187)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler.py` _+1 more__
- **2026-08-11** [`346dbaeed5`](https://github.com/NVIDIA/TensorRT-LLM/commit/346dbaeed5) [#16773](https://github.com/NVIDIA/TensorRT-LLM/pull/16773)
  [None][feat] Add Cosmos3-Edge (Nemotron-dense) support (#16773)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py` _+20 more__
- **2026-08-11** [`fea23ffff4`](https://github.com/NVIDIA/TensorRT-LLM/commit/fea23ffff4) [#17305](https://github.com/NVIDIA/TensorRT-LLM/pull/17305)
  [#17146][fix] Resolve reasoning mode from the rendered prompt (#17305)
  _Files: `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/llmapi/reasoning_parser.py`, `tensorrt_llm/serve/openai_protocol.py` _+7 more__
- **2026-08-11** [`0c98e9292a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c98e9292a) [#17308](https://github.com/NVIDIA/TensorRT-LLM/pull/17308)
  [None][perf] enable zero-copy token passing in KVCacheManagerV2 (#17308)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h` _+33 more__
- **2026-08-11** [`27e5b703b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/27e5b703b8) [#16592](https://github.com/NVIDIA/TensorRT-LLM/pull/16592)
  [TRTLLM-13409][feat] hard-kill all ranks when one rank's executor loop crashes (#16592)
  _Files: `docs/source/developer-guide/overview.md`, `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py` _+3 more__
- **2026-08-10** [`6fb2f4fc99`](https://github.com/NVIDIA/TensorRT-LLM/commit/6fb2f4fc99) [#17456](https://github.com/NVIDIA/TensorRT-LLM/pull/17456)
  [None][doc] Note runtime-dependency requirement for the kimi_k3 Slurm container image (#17456)
  _Files: `examples/kimi_k3/README.md`_
- **2026-08-10** [`10689401f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/10689401f1) [#16952](https://github.com/NVIDIA/TensorRT-LLM/pull/16952)
  [https://nvbugs/6475346][fix] Avoid stale CUD… (#16952)
  _Files: `tensorrt_llm/_torch/compilation/backend.py`, `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`f13a0be917`](https://github.com/NVIDIA/TensorRT-LLM/commit/f13a0be917) [#17281](https://github.com/NVIDIA/TensorRT-LLM/pull/17281)
  [TRTLLM-15151][chore] load models lazily (#17281)
  _Files: `tensorrt_llm/__init__.py`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_auto.py` _+27 more__

## Attention  (24 commits)

- **2026-08-17** [`3d311e377e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d311e377e) [#16432](https://github.com/NVIDIA/TensorRT-LLM/pull/16432)
  [None][fix] Declare attention runtime-workspace bytes/token as a backend contract (#16432)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/modules/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+3 more__
- **2026-08-17** [`afee78d207`](https://github.com/NVIDIA/TensorRT-LLM/commit/afee78d207) [#17674](https://github.com/NVIDIA/TensorRT-LLM/pull/17674)
  [TRTLLM-15115][test] Prune Starcoder2-3B functional and unit tests (#17674)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/humaneval.yaml`, `tests/integration/defs/accuracy/test_cli_flow.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_encode.py` _+7 more__
- **2026-08-17** [`2d9e78c96e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d9e78c96e) [#16914](https://github.com/NVIDIA/TensorRT-LLM/pull/16914)
  [None][feat] Support DFlash RoPE, sliding-window configuration, and TRTLLM-gen attention backend (#16914)
  _Files: `docs/source/features/speculative-decoding.md`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py` _+16 more__
- **2026-08-15** [`71f025e9b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/71f025e9b2) [#16857](https://github.com/NVIDIA/TensorRT-LLM/pull/16857)
  [None][perf] Avoid paged MSA K/V materialization during prefill (#16857)
  _Files: `.gitignore`, `.gitmodules`, `3rdparty/CMakeLists.txt`, `3rdparty/MSA` _+12 more__
- **2026-08-15** [`13e8dccc7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/13e8dccc7d) [#16486](https://github.com/NVIDIA/TensorRT-LLM/pull/16486)
  [None][fix] VisualGen: Widen Ulysses async-barrier timeout 10s->60s for multi-node warmup (#16486)
  _Files: `.github/CODEOWNERS`, `cpp/tensorrt_llm/thop/asyncUlyssesOp.cpp`, `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`_
- **2026-08-15** [`4ff5d102a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ff5d102a7) [#16609](https://github.com/NVIDIA/TensorRT-LLM/pull/16609)
  [TRTLLM-13579][feat] BREAKING: Support BCG in Prefill (#16609)
  _Files: `docs/source/features/torch_compile_and_piecewise_cuda_graph.md`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/custom_ops.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/module.py` _+26 more__
- **2026-08-15** [`c36bf43e80`](https://github.com/NVIDIA/TensorRT-LLM/commit/c36bf43e80) [#17233](https://github.com/NVIDIA/TensorRT-LLM/pull/17233)
  [https://nvbugs/6525008][fix] Isolate FlashInfer JIT workspaces for MPI workers (#17233)
  _Files: `docs/source/llm-api/index.md`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/test-db/l0_a100.yml` _+1 more__
- **2026-08-14** [`8d8f81ad93`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d8f81ad93) [#17675](https://github.com/NVIDIA/TensorRT-LLM/pull/17675)
  [TRTLLM-15102][test] Prune VILA family models  (#17675)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/defs/conftest.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+5 more__
- **2026-08-14** [`7550fc79c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/7550fc79c3) [#17619](https://github.com/NVIDIA/TensorRT-LLM/pull/17619)
  [None][fix] Restore DSpark disaggregated decoding accuracy (#17619)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/models/dspark/attention.py`, `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/speculative/dspark.py` _+3 more__
- **2026-08-14** [`af7d5ba3aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/af7d5ba3aa) [#17525](https://github.com/NVIDIA/TensorRT-LLM/pull/17525)
  [TRTLLM-14628][feat] Add --out-of-tree wheel builds that never write into the checkout (#17525)
  _Files: `cpp/CMakeLists.txt`, `cpp/kernels/fmha_v2/setup.py`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/CMakeLists.txt`, `docs/source/installation/build-from-source.md` _+1 more__
- **2026-08-13** [`e91b9f8717`](https://github.com/NVIDIA/TensorRT-LLM/commit/e91b9f8717) [#17557](https://github.com/NVIDIA/TensorRT-LLM/pull/17557)
  [https://nvbugs/6566891][fix] Use FlashInfer FA2 for Gemma4 on SM120 and SM121 (#17557)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-08-13** [`30cc13f244`](https://github.com/NVIDIA/TensorRT-LLM/commit/30cc13f244) [#11263](https://github.com/NVIDIA/TensorRT-LLM/pull/11263)
  [None][fix] Fix possible arithmetic overflow in FMHAv2 launcher (#11263)
  _Files: `cpp/kernels/fmha_v2/setup.py`_
- **2026-08-13** [`9bfe467c3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9bfe467c3b) [#17563](https://github.com/NVIDIA/TensorRT-LLM/pull/17563)
  [None][test] Extend the compressor BF16 tie tolerance to the remaining prefill assertions (#17563)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_compressor_kernel.py`_
- **2026-08-12** [`49d4a1aaa2`](https://github.com/NVIDIA/TensorRT-LLM/commit/49d4a1aaa2) [#17425](https://github.com/NVIDIA/TensorRT-LLM/pull/17425)
  [None][fix] Fix CuTeDSL packed QKV copy lowering (#17425)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/fmha.py`_
- **2026-08-12** [`1fb6e84996`](https://github.com/NVIDIA/TensorRT-LLM/commit/1fb6e84996) [#16620](https://github.com/NVIDIA/TensorRT-LLM/pull/16620)
  [TRTLLM-13234][feat] Complete TorchSampler beam search: length_penalty, diversity_rate, early_stopping, VBWS, and CBA performance (#16620)
  _Files: `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+16 more__
- **2026-08-12** [`0f5ba29142`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f5ba29142) [#17501](https://github.com/NVIDIA/TensorRT-LLM/pull/17501)
  [None][refactor] Remove model_path from TriAttention config and reuse the executor's pretrained config (#17501)
  _Files: `examples/kv_cache_compression/triattention.md`, `tensorrt_llm/_torch/kv_cache_compression/triattention/triattention.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/llmapi/llm_args.py` _+4 more__
- **2026-08-12** [`ce9f0a9ef4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce9f0a9ef4) [#17508](https://github.com/NVIDIA/TensorRT-LLM/pull/17508)
  [https://nvbugs/6192267] [test] unwaive test for no cache attention (#17508)
  _Files: `tests/unittest/_torch/attention/test_attention_no_cache.py`_
- **2026-08-11** [`6930568f66`](https://github.com/NVIDIA/TensorRT-LLM/commit/6930568f66) [#17090](https://github.com/NVIDIA/TensorRT-LLM/pull/17090)
  [TRTLLM-13948][feat] Clean up DeepSeek tests using CPP Transceiver v1 (#17090)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_cache_aware_balance_deepseek_v3.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_cache_reuse_deepseek_v3.yaml` _+26 more__
- **2026-08-11** [`0c1b0a8fea`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c1b0a8fea) [#17379](https://github.com/NVIDIA/TensorRT-LLM/pull/17379)
  [TRTLLM-15178][fix] Pad an empty attention-DP scheduled batch so the fleet can make forward progress (#17379)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-11** [`6b052851c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b052851c9) [#15300](https://github.com/NVIDIA/TensorRT-LLM/pull/15300)
  [None][chore] Use public flashinfer APIs (#15300)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-08-11** [`c1a8a1c397`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1a8a1c397) [#17014](https://github.com/NVIDIA/TensorRT-LLM/pull/17014)
  [https://nvbugs/6565412][fix] Size trtllm-gen and thop decode buffers for beam search (#17014)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h`, `tensorrt_llm/_torch/attention_backend/fmha/fallback.py` _+2 more__
- **2026-08-11** [`d247d1454a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d247d1454a) [#16810](https://github.com/NVIDIA/TensorRT-LLM/pull/16810)
  [None][feat] Support dense FP8 LoRA end to end (#16810)
  _Files: `cpp/include/tensorrt_llm/batch_manager/peftCacheManager.h`, `cpp/include/tensorrt_llm/runtime/loraCache.h`, `cpp/tensorrt_llm/batch_manager/peftCacheManager.cpp`, `cpp/tensorrt_llm/kernels/cuda_graph_grouped_gemm.cu` _+28 more__
- **2026-08-10** [`c745978df6`](https://github.com/NVIDIA/TensorRT-LLM/commit/c745978df6) [#13922](https://github.com/NVIDIA/TensorRT-LLM/pull/13922)
  [https://nvbugs/6159132][fix] Differentiate the two paths via extra_acc_spec="tp_attn" when attention_dp=False (#13922)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`4ec478dede`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ec478dede) [#17445](https://github.com/NVIDIA/TensorRT-LLM/pull/17445)
  [None][fix] Kimi K3 MLA: pass attn_output to MLA.forward_impl (#17445)
  _Files: `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`_

## MoE  (20 commits)

- **2026-08-17** [`bac9a5cc58`](https://github.com/NVIDIA/TensorRT-LLM/commit/bac9a5cc58) [#17612](https://github.com/NVIDIA/TensorRT-LLM/pull/17612)
  [None][fix] Drop the stale choices list on --moe-backend-for-prefill (#17612)
  _Files: `examples/layer_wise_benchmarks/run.py`_
- **2026-08-17** [`e5323835d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5323835d8) [#17621](https://github.com/NVIDIA/TensorRT-LLM/pull/17621)
  [None][fix] Fence MoE shared writes before async bulk copy (#17621)
  _Files: `cpp/tensorrt_llm/kernels/fusedMoeCommKernels.cu`_
- **2026-08-17** [`476ea087a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/476ea087a0) [#17404](https://github.com/NVIDIA/TensorRT-LLM/pull/17404)
  [None][infra] Add execution and test-runner skills for Claude Code (#17404)
  _Files: `.claude/agents/exec-local-slurm.md`, `.claude/agents/exec-remote-slurm.md`, `.claude/agents/trtllm-test-specialist.md`, `.claude/skills/exec-env-check/SKILL.md` _+78 more__
- **2026-08-16** [`43d14effe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/43d14effe3) [#17711](https://github.com/NVIDIA/TensorRT-LLM/pull/17711)
  [TRTLLM-15177][test] Wire remaining Kimi K3 MoE unit tests into L0 (Hopper) (#17711)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-08-16** [`f75a75b179`](https://github.com/NVIDIA/TensorRT-LLM/commit/f75a75b179) [#17532](https://github.com/NVIDIA/TensorRT-LLM/pull/17532)
  [TRTLLM-14956][refactor] make MoE implementation selection reproducible (#17532)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tensorrt_llm/_torch/models/modeling_laguna.py`, `tensorrt_llm/_torch/models/modeling_qwen3_moe.py` _+30 more__
- **2026-08-15** [`c639469664`](https://github.com/NVIDIA/TensorRT-LLM/commit/c639469664) [#17624](https://github.com/NVIDIA/TensorRT-LLM/pull/17624)
  [TRTLLM-15284][feat] add Kimi K3 SiTU MegaMoE support (#17624)
  _Files: `3rdparty/fetch_content.json`, `examples/kimi_k3/eval_extra_llm_options.yaml`, `scripts/attribution/data/dependency_metadata.yml`, `scripts/attribution/data/files_to_dependency.yml` _+9 more__
- **2026-08-14** [`3ef6f48d05`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ef6f48d05) [#17414](https://github.com/NVIDIA/TensorRT-LLM/pull/17414)
  [TRTLLM-15177][chore] Consolidate trtllm-gen SiTu activation slot handling (#17414)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/_torch/utils.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`7b1bb1a88e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b1bb1a88e) [#16849](https://github.com/NVIDIA/TensorRT-LLM/pull/16849)
  [None][perf] fp8 block scale quant fusion in SM90 Cutlass MoE (#16849)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_gemm.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`_
- **2026-08-13** [`f274b6ca51`](https://github.com/NVIDIA/TensorRT-LLM/commit/f274b6ca51) [#16877](https://github.com/NVIDIA/TensorRT-LLM/pull/16877)
  [TRTLLM-15293][perf] Add tiered GVR CuTe DSL top-k decode kernels (stacked on #16457) (#16877)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_direct.py` _+7 more__
- **2026-08-12** [`37b12dee6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/37b12dee6f) [#17339](https://github.com/NVIDIA/TensorRT-LLM/pull/17339)
  [TRTLLM-13696][test] Part2.4: Migrate CPU only tests - others (#17339)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+55 more__
- **2026-08-12** [`43c2386d49`](https://github.com/NVIDIA/TensorRT-LLM/commit/43c2386d49) [#17411](https://github.com/NVIDIA/TensorRT-LLM/pull/17411)
  [TRTLLM-14955][refactor] Declare MoE backend behaviour instead of comparing classes (#17411)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl_b12x.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py` _+14 more__
- **2026-08-11** [`bfc4966e4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfc4966e4c) [#16060](https://github.com/NVIDIA/TensorRT-LLM/pull/16060)
  [None][feat] Add KV cache manager V2 support for DSA (#16060)
  _Files: `cpp/tensorrt_llm/kernels/IndexerKCacheGather.h`, `cpp/tensorrt_llm/kernels/IndexerKCacheScatter.h`, `cpp/tensorrt_llm/kernels/indexerKCacheGather.cu`, `cpp/tensorrt_llm/kernels/indexerKCacheScatter.cu` _+39 more__
- **2026-08-11** [`4d7c0d4197`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d7c0d4197) [#15550](https://github.com/NVIDIA/TensorRT-LLM/pull/15550)
  [None][fix] Enable INT8 weight-only (W8A16) MoE for non-gated activations (#15550)
  _Files: `cpp/tensorrt_llm/thop/moeOp.cpp`, `tensorrt_llm/_torch/modules/fused_moe/quantization.py`, `tests/unittest/_torch/modules/moe/quantize_utils.py`, `tests/unittest/_torch/modules/moe/test_moe_backend.py`_
- **2026-08-11** [`01351eea7b`](https://github.com/NVIDIA/TensorRT-LLM/commit/01351eea7b) [#17314](https://github.com/NVIDIA/TensorRT-LLM/pull/17314)
  [TRTLLM-13696][test] Part2.3: Migrate CPU only tests - auto deploy (#17314)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/auto_deploy/unit/singlegpu/models/test_gpt_oss_modeling.py`, `tests/unittest/auto_deploy/multigpu/custom_ops/test_ad_dist_strategies.py`, `tests/unittest/auto_deploy/multigpu/transformations/library/test_tp_sharding.py` _+75 more__
- **2026-08-11** [`5f905eaf53`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f905eaf53) [#17463](https://github.com/NVIDIA/TensorRT-LLM/pull/17463)
  [None][chore] Default enable PDL for benchmoe (#17463)
  _Files: `tests/microbenchmarks/bench_moe/worker.py`_
- **2026-08-11** [`b6b8f053d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6b8f053d9) [#17294](https://github.com/NVIDIA/TensorRT-LLM/pull/17294)
  [https://nvbugs/6507110][chore] Unwaive TestQwen3_30B_A3B::test_nvfp4 dep4_latency_moe_trtllm (#17294)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`f949d3b892`](https://github.com/NVIDIA/TensorRT-LLM/commit/f949d3b892) [#17413](https://github.com/NVIDIA/TensorRT-LLM/pull/17413)
  [TRTLLM-15177][chore] Kimi K3 post-merge cleanup: config/import/test hygiene + L0 wiring (#17413)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_moe/__init__.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modeling/test_kimi_kda_fused_verify_parity.py` _+4 more__
- **2026-08-10** [`fbda11f5aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/fbda11f5aa) [#16959](https://github.com/NVIDIA/TensorRT-LLM/pull/16959)
  [https://nvbugs/6523820][fix] Waive NCCL-EP dispatch-only CUDA graph replay test (#16959)
  _Files: `tests/unittest/_torch/modules/moe/test_moe_comm.py`_
- **2026-08-10** [`0f6f2d82f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f6f2d82f3) [#17259](https://github.com/NVIDIA/TensorRT-LLM/pull/17259)
  [None][fix] Skip no-op MXFP4 weight padding (#17259)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/quantization.py`_
- **2026-08-10** [`ec044a2e1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec044a2e1a) [#17293](https://github.com/NVIDIA/TensorRT-LLM/pull/17293)
  [https://nvbugs/6434512][fix] Select Marlin for Qwen3.5 MoE on Hopper (#17293)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl_moe.py`_

## Quantization  (17 commits)

- **2026-08-16** [`0b14c6bb0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b14c6bb0d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+4 more__
- **2026-08-15** [`f3e8493b10`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3e8493b10) [#17659](https://github.com/NVIDIA/TensorRT-LLM/pull/17659)
  [https://nvbugs/6476233][fix] Cap max_seq_len on H200 DeepSeek-V3.2 blockscale test (#17659)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-15** [`cca22965fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/cca22965fd) [#15562](https://github.com/NVIDIA/TensorRT-LLM/pull/15562)
  [None][feat] Add HunyuanVideo 1.5 text-to-video support to VisualGen (#15562)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/hunyuan-t2v-fp8-1gpu.yaml`, `examples/visual_gen/models/hunyuan_t2v.py` _+13 more__
- **2026-08-14** [`38aef43a3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/38aef43a3f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+2 more__
- **2026-08-13** [`9ce30623f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ce30623f8) [#17663](https://github.com/NVIDIA/TensorRT-LLM/pull/17663)
  [None][test] Waive 3 DGX_B200 main-side CI flakes (kv-cache eviction, qwen3 fp8 lora, gemma4 e2e) (#17663)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`a611a65acf`](https://github.com/NVIDIA/TensorRT-LLM/commit/a611a65acf) [#17661](https://github.com/NVIDIA/TensorRT-LLM/pull/17661)
  [https://nvbugs/6525011][test] Waive TestLagunaXS::test_fp8 on RTXPro6000D (#17661)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`aa70f578ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa70f578ee) [#17569](https://github.com/NVIDIA/TensorRT-LLM/pull/17569)
  [https://nvbugs/6140408][chore] Unwaive DeepSeekV3Lite test_nvfp4_4gpus CUTLASS pp4 and CUTEDSL tp2pp2 (#17569)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`265a116838`](https://github.com/NVIDIA/TensorRT-LLM/commit/265a116838) [#17640](https://github.com/NVIDIA/TensorRT-LLM/pull/17640)
  [https://nvbugs/6604925][test] Waive flaky TestQwen3_6_35B_A3B::test_nvfp4[TRTLLM] (SIGSEGV on DGX_B200) (#17640)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`148f1f2290`](https://github.com/NVIDIA/TensorRT-LLM/commit/148f1f2290)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+1 more__
- **2026-08-12** [`82e27f7357`](https://github.com/NVIDIA/TensorRT-LLM/commit/82e27f7357)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+5 more__
- **2026-08-12** [`ae1465eefd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae1465eefd) [#17503](https://github.com/NVIDIA/TensorRT-LLM/pull/17503)
  [https://nvbugs/6490036][test] Isolate part1 FP8 weight-update tests (#17503)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`28e03befe6`](https://github.com/NVIDIA/TensorRT-LLM/commit/28e03befe6) [#17433](https://github.com/NVIDIA/TensorRT-LLM/pull/17433)
  [None][fix] Qwen3.5 weight mapper for FP8 rowwise checkpoints (#17433)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tests/unittest/_torch/models/checkpoints/hf/test_qwen3_5_weight_mapper.py`_
- **2026-08-11** [`921d5e35b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/921d5e35b4) [#16102](https://github.com/NVIDIA/TensorRT-LLM/pull/16102)
  [https://nvbugs/6287721][chore] Unwaive Qwen3 FP8 weight-update tests (#16102)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`26842d1f5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/26842d1f5e) [#15973](https://github.com/NVIDIA/TensorRT-LLM/pull/15973)
  [None][test] Unwaive DeepSeekV3.2 nvfp4 mtp3_fp8kv_chunked test (#15973)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-10** [`c67879c432`](https://github.com/NVIDIA/TensorRT-LLM/commit/c67879c432) [#17446](https://github.com/NVIDIA/TensorRT-LLM/pull/17446)
  [TRTLLM-15215][fix] Kimi K3: make the FP8 weight-read master switch opt-in (#17446)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tests/unittest/_torch/modeling/test_kimi_k3_fp8_weight_read_gates.py`_
- **2026-08-10** [`529d0d018e`](https://github.com/NVIDIA/TensorRT-LLM/commit/529d0d018e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+5 more__
- **2026-08-10** [`0fa708be4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fa708be4e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+1 more__

## Disaggregation / KV  (15 commits)

- **2026-08-17** [`2562a0a3d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/2562a0a3d8) [#17618](https://github.com/NVIDIA/TensorRT-LLM/pull/17618)
  [None][refactor] BREAKING remove conversation ID from disaggregated params (#17618)
  _Files: `tensorrt_llm/disaggregated_params.py`, `tensorrt_llm/serve/conversation_id.py`, `tensorrt_llm/serve/openai_disagg_service.py`, `tensorrt_llm/serve/openai_protocol.py` _+5 more__
- **2026-08-17** [`9997d3ffb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9997d3ffb0) [#17460](https://github.com/NVIDIA/TensorRT-LLM/pull/17460)
  [https://nvbugs/6435121][fix] Eliminate the trtllm-serve port reservation race with --port 0 + --report_addr (#17460)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/common.py`, `tests/integration/defs/disaggregated/disagg_test_utils.py` _+6 more__
- **2026-08-17** [`55be7e53d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/55be7e53d3) [#17480](https://github.com/NVIDIA/TensorRT-LLM/pull/17480)
  [TRTLLM-15264][fix] Reject non-Python transceiver routes for Kimi K3 disaggregated serving (#17480)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py`_
- **2026-08-15** [`f8c7f55b2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f8c7f55b2b) [#17609](https://github.com/NVIDIA/TensorRT-LLM/pull/17609)
  [None][test] Nemotron-Ultra-V3 perf-sanity cases (GB300); de-enroll DeepSeek-V3.2, Kimi-K2.5 & Llama cases (#17609)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus_perf_sanity.yml` _+19 more__
- **2026-08-14** [`3050cc00e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/3050cc00e2) [#17535](https://github.com/NVIDIA/TensorRT-LLM/pull/17535)
  [None][chore] Scope TRTLLM_DISABLE_KV_CACHE_TRANSFER_OVERLAP to the gen worker in disagg gen_only (#17535)
  _Files: `examples/disaggregated/slurm/benchmark/submit.py`, `jenkins/scripts/perf/local/submit.py`, `jenkins/scripts/perf/submit.py`_
- **2026-08-14** [`285df75de7`](https://github.com/NVIDIA/TensorRT-LLM/commit/285df75de7) [#16614](https://github.com/NVIDIA/TensorRT-LLM/pull/16614)
  [None][test] Consolidate dis-agg E2E Tests (#16614)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_deepseek_v3_lite_ucx.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_llama31_8b.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+8 more__
- **2026-08-13** [`925148af3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/925148af3e) [#16834](https://github.com/NVIDIA/TensorRT-LLM/pull/16834)
  [https://nvbugs/6487038][fix] Stop single-rank disagg errors from crashing all gen ranks (#16834)
  _Files: `tensorrt_llm/executor/worker.py`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_kimi-k25-thinking-fp4_8k1k_con4096_ctx1_dep4_gen1_dep16_eplb0_mtp0_ccb-NIXL.yaml` _+2 more__
- **2026-08-12** [`f285287b79`](https://github.com/NVIDIA/TensorRT-LLM/commit/f285287b79) [#17461](https://github.com/NVIDIA/TensorRT-LLM/pull/17461)
  [https://nvbugs/6566735][fix] recover disaggregated worker heartbeat registration (#17461)
  _Files: `tensorrt_llm/serve/disagg_auto_scaling.py`, `tests/unittest/disaggregated/test_disagg_cluster_manager_worker.py`_
- **2026-08-12** [`d4c771c7ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4c771c7ed) [#17283](https://github.com/NVIDIA/TensorRT-LLM/pull/17283)
  [None][feat] Support the masked DSA indexer k-cache pool in the Python cache transceiver (#17283)
  _Files: `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py` _+6 more__
- **2026-08-12** [`c357c9553b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c357c9553b) [#17295](https://github.com/NVIDIA/TensorRT-LLM/pull/17295)
  [None][feat] support NIXL cache transceiver with Ray (#17295)
  _Files: `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/common/envUtils.cpp`, `cpp/tensorrt_llm/common/envUtils.h`, `cpp/tensorrt_llm/executor/cache_transmission/agent_utils/connection.cpp` _+21 more__
- **2026-08-12** [`66758429f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/66758429f7) [#17427](https://github.com/NVIDIA/TensorRT-LLM/pull/17427)
  [https://nvbugs/6472256][fix] Fix disagg stress cluster flapping and DeepSeek R1 FP4 ctx OOM; add aiperf error-rate gate (#17427)
  _Files: `tests/integration/defs/disaggregated/test_aiperf_gate.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp4_gentp4_deepseek_r1_v2_fp4_tllm.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp4_gentp4_deepseek_r1_v2_fp4_tllm_mtp.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+3 more__
- **2026-08-11** [`a2f02dae36`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2f02dae36) [#16787](https://github.com/NVIDIA/TensorRT-LLM/pull/16787)
  [TRTLLM-14806][feat] Prefer Python V2 transceiver for LlamaForCausalLM and Gemma3ForCausalLM (#16787)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma3.py`, `tensorrt_llm/_torch/models/modeling_llama.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+2 more__
- **2026-08-11** [`48df89d76d`](https://github.com/NVIDIA/TensorRT-LLM/commit/48df89d76d) [#17484](https://github.com/NVIDIA/TensorRT-LLM/pull/17484)
  [TRTLLM-15264][test] Wire KDA disagg transfer tests into CI (cpu_only CPU stage + l0_b200 GPU) (#17484)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/disaggregated/test_kda_mamba_transfer.py`_
- **2026-08-11** [`bd09237dce`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd09237dce) [#17107](https://github.com/NVIDIA/TensorRT-LLM/pull/17107)
  [None][fix] Fix gen-only async kvtransfer hang (#17107)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_mamba_bs1_concurrency2.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+2 more__
- **2026-08-10** [`67dd1b7ed8`](https://github.com/NVIDIA/TensorRT-LLM/commit/67dd1b7ed8) [#16942](https://github.com/NVIDIA/TensorRT-LLM/pull/16942)
  [None][feat] Opt GPT-OSS in to KV cache manager V2 by default (#16942)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tensorrt_llm/llmapi/llm_utils.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+1 more__

## Speculative Decoding  (14 commits)

- **2026-08-17** [`2c0eca97d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c0eca97d3) [#17599](https://github.com/NVIDIA/TensorRT-LLM/pull/17599)
  [None][feat] Honor SamplingParams.seed on the one-model speculative path (#17599)
  _Files: `tensorrt_llm/_torch/speculative/eagle3_dynamic_tree.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_rng_window_counter.py`_
- **2026-08-14** [`4e95cb74e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e95cb74e9) [#17582](https://github.com/NVIDIA/TensorRT-LLM/pull/17582)
  [None][perf] Skip request_context class construction on the non-draft path (#17582)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_
- **2026-08-14** [`791588ee37`](https://github.com/NVIDIA/TensorRT-LLM/commit/791588ee37) [#17378](https://github.com/NVIDIA/TensorRT-LLM/pull/17378)
  [TRTLLM-13394][feat] Support loading MTP weights from standalone checkpoint (#17378)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/speculative/utils.py` _+3 more__
- **2026-08-13** [`e9dd5a7905`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9dd5a7905)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+1 more__
- **2026-08-13** [`20cc428d81`](https://github.com/NVIDIA/TensorRT-LLM/commit/20cc428d81) [#17594](https://github.com/NVIDIA/TensorRT-LLM/pull/17594)
  [None][doc] Add Qwen3.8 deployment guide and configs (#17594)
  _Files: `docs/source/_static/config_db.json`, `docs/source/_static/config_selector.js`, `docs/source/deployment-guide/deployment-guide-for-qwen3.5-on-trtllm.md`, `docs/source/deployment-guide/deployment-guide-for-qwen3.8-qwen3.5-on-trtllm.md` _+11 more__
- **2026-08-13** [`089a2573ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/089a2573ac) [#17544](https://github.com/NVIDIA/TensorRT-LLM/pull/17544)
  [TRTLLM-13215][perf] Skip redundant one-model sampling-param refills (#17544)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`_
- **2026-08-13** [`21d77d5953`](https://github.com/NVIDIA/TensorRT-LLM/commit/21d77d5953) [#17554](https://github.com/NVIDIA/TensorRT-LLM/pull/17554)
  [None][chore] Drop the skip_* sampling flags from one-model spec metadata (#17554)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/test_capture_override_leak.py`_
- **2026-08-13** [`8398196403`](https://github.com/NVIDIA/TensorRT-LLM/commit/8398196403) [#17597](https://github.com/NVIDIA/TensorRT-LLM/pull/17597)
  [None][fix] Remove obsolete GPT-OSS two-model Eagle3 tests (#17597)
  _Files: `tests/unittest/_torch/modeling/test_modeling_gpt_oss.py`_
- **2026-08-12** [`1e6a8cbf9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e6a8cbf9c) [#17366](https://github.com/NVIDIA/TensorRT-LLM/pull/17366)
  [TRTLLM-14388][refactor] BREAKING: Force 2 model spec dec to fall back to 1 model (#17366)
  _Files: `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_mtp.py`, `tests/unittest/_torch/speculative/test_eagle3.py`_
- **2026-08-12** [`de709952e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/de709952e1) [#17347](https://github.com/NVIDIA/TensorRT-LLM/pull/17347)
  [None][fix] Skip draft KV mirror when IndexMapper is saturated in KVCacheManagerV2 (#17347)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`_
- **2026-08-12** [`a2e0fba1bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2e0fba1bf) [#16965](https://github.com/NVIDIA/TensorRT-LLM/pull/16965)
  [None][fix] Structured Output with DSpark Speculative Drafter (#16965)
  _Files: `tensorrt_llm/_torch/speculative/dspark.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dspark_worker.py`_
- **2026-08-12** [`0ff21c085b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ff21c085b) [#16543](https://github.com/NVIDIA/TensorRT-LLM/pull/16543)
  [TRTLLM-14704][feat] Import agent-flow and modeling bringup agent into TensorRT-LLM (#16543)
  _Files: `agent-flow/.gitignore`, `agent-flow/.pre-commit-config.yaml`, `agent-flow/AGENTS.md`, `agent-flow/CLAUDE.md` _+74 more__
- **2026-08-11** [`e61a6e93c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e61a6e93c9) [#17455](https://github.com/NVIDIA/TensorRT-LLM/pull/17455)
  [TRTLLM-14814][chore] Add SA speculative-decoding eval config for Kimi K3 (#17455)
  _Files: `examples/kimi_k3/README.md`, `examples/kimi_k3/eval_extra_llm_options_sa.yaml`, `examples/kimi_k3/run_gsm8k_kimi_k3.sbatch`_
- **2026-08-10** [`fb1c287a59`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb1c287a59) [#17292](https://github.com/NVIDIA/TensorRT-LLM/pull/17292)
  [TRTLLM-15017][chore] Unify one-model speculative decoding samplers into SpecSampler (#17292)
  _Files: `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_eagle.py`, `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/pyexecutor/sampler/top_p_decay.py`, `tensorrt_llm/_torch/speculative/__init__.py` _+11 more__

## Models  (11 commits)

- **2026-08-14** [`9d951af47c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d951af47c) [#17697](https://github.com/NVIDIA/TensorRT-LLM/pull/17697)
  [TRTLLM-15402][fix] VisualGen: fix Cache-DiT stats log line (lazy %-formatting never applied) (#17697)
  _Files: `tensorrt_llm/_torch/visual_gen/models/qwen_image/pipeline_qwen_image.py`, `tensorrt_llm/_torch/visual_gen/pipeline.py`_
- **2026-08-14** [`a702ae9035`](https://github.com/NVIDIA/TensorRT-LLM/commit/a702ae9035) [#17311](https://github.com/NVIDIA/TensorRT-LLM/pull/17311)
  [None][perf] Fuse Kimi K3 KDA projections (#17311)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tests/unittest/_torch/modeling/test_kimi_kda_fused_verify_parity.py`, `tests/unittest/_torch/modeling/test_kimi_kda_verify_parity.py`_
- **2026-08-14** [`a216a8cd74`](https://github.com/NVIDIA/TensorRT-LLM/commit/a216a8cd74) [#17471](https://github.com/NVIDIA/TensorRT-LLM/pull/17471)
  [https://nvbugs/6566786][test] Unwaive fixed DeepSeek tests (#17471)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-14** [`b9eb3db6d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9eb3db6d2) [#17472](https://github.com/NVIDIA/TensorRT-LLM/pull/17472)
  [None][test] Unwaive qwen3.5 test cases (#17472)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-13** [`564dab19e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/564dab19e2) [#17584](https://github.com/NVIDIA/TensorRT-LLM/pull/17584)
  [https://nvbugs/6599150][fix] Initialize dt_bias in KDA verify-parity test (#17584)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_kimi_kda_verify_parity.py`_
- **2026-08-12** [`ec3e1a13d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec3e1a13d0) [#17577](https://github.com/NVIDIA/TensorRT-LLM/pull/17577)
  [https://nvbugs/6600098][test] Waive flaky TestKVCacheV2Llama scheduler tests on DGX_B200 (#17577)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-12** [`003a780a68`](https://github.com/NVIDIA/TensorRT-LLM/commit/003a780a68) [#17470](https://github.com/NVIDIA/TensorRT-LLM/pull/17470)
  [https://nvbugs/6529792][fix] Avoid GPT-OSS V2 cache estimation OOM (#17470)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-08-11** [`fdbe8d5d0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/fdbe8d5d0c) [#17479](https://github.com/NVIDIA/TensorRT-LLM/pull/17479)
  [TRTLLM-15264][doc] Kimi K3 disagg: stop recommending a UCX_TLS pin by default (#17479)
  _Files: `examples/kimi_k3/disagg/README.md`, `examples/kimi_k3/disagg/benchmark_kimi_k3_dep16.yaml`_
- **2026-08-10** [`ac54855177`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac54855177) [#17415](https://github.com/NVIDIA/TensorRT-LLM/pull/17415)
  [https://nvbugs/6566737][fix] Set mamba_ssm_cache_dtype="float32" in _run_qwen35_35b_update and widen… (#17415)
  _Files: `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`_
- **2026-08-10** [`48e0fae00f`](https://github.com/NVIDIA/TensorRT-LLM/commit/48e0fae00f) [#17422](https://github.com/NVIDIA/TensorRT-LLM/pull/17422)
  [None][test] Fix qwen3.5_9b avg_seq_len and restore H100 coverage for three Qwen3.5 perf cases (#17422)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-10** [`ae4520506f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae4520506f) [#17421](https://github.com/NVIDIA/TensorRT-LLM/pull/17421)
  [None][fix] Kimi K3: eager CUDA-graph buffer allocation and prebuilt fused-verify constants (#17421)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tests/unittest/_torch/modeling/test_kimi_kda_fused_verify_parity.py`_

## Torch Path (_torch)  (10 commits)

- **2026-08-17** [`99edf98239`](https://github.com/NVIDIA/TensorRT-LLM/commit/99edf98239) [#16788](https://github.com/NVIDIA/TensorRT-LLM/pull/16788)
  [https://nvbugs/6490028][fix] Bump only the cross-library `cublas_tolerance` from 1.05 to 1.10 in the test… (#16788)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-08-14** [`0946d54b8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0946d54b8d) [#17430](https://github.com/NVIDIA/TensorRT-LLM/pull/17430)
  [https://nvbugs/6272397][fix] Prevent host OOM during checkpoint prefetch (#17430)
  _Files: `tensorrt_llm/_torch/mmap_utils.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/models/checkpoints/hf/test_weight_loader.py` _+1 more__
- **2026-08-14** [`92a29f2c7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/92a29f2c7d) [#17595](https://github.com/NVIDIA/TensorRT-LLM/pull/17595)
  [TRTLLM-15093][test] Prune LLaVA-Next functional and unit tests (#17595)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/defs/conftest.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+5 more__
- **2026-08-13** [`84e05ecace`](https://github.com/NVIDIA/TensorRT-LLM/commit/84e05ecace) [#17596](https://github.com/NVIDIA/TensorRT-LLM/pull/17596)
  [None][test] Adjust timeout test cases to avoid large log (#17596)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-12** [`740c70878c`](https://github.com/NVIDIA/TensorRT-LLM/commit/740c70878c) [#17516](https://github.com/NVIDIA/TensorRT-LLM/pull/17516)
  [None][feat] Remove stale VBench test infrastructure (#17516)
  _Files: `tensorrt_llm/_torch/visual_gen/ENGINEERING_CRITERIA.md`, `tests/integration/defs/examples/visual_gen/conftest.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_ltx2.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_wan.py` _+1 more__
- **2026-08-11** [`c0e6d795c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0e6d795c8) [#16902](https://github.com/NVIDIA/TensorRT-LLM/pull/16902)
  [https://nvbugs/6262973][perf] Move AllReduce autotuner dispatch to C++ (#16902)
  _Files: `cpp/tensorrt_llm/thop/allreduceOp.cpp`, `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/compilation/patterns/ar_residual_norm.py`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+4 more__
- **2026-08-11** [`d3cfe40e75`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3cfe40e75) [#17486](https://github.com/NVIDIA/TensorRT-LLM/pull/17486)
  [None][fix] fix oom (#17486)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-08-11** [`60acc49c97`](https://github.com/NVIDIA/TensorRT-LLM/commit/60acc49c97) [#17001](https://github.com/NVIDIA/TensorRT-LLM/pull/17001)
  [TRTLLM-14555][perf] Optimize parallel VAE halo exchange path (#17001)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/parallel_vae.py`, `tensorrt_llm/_torch/visual_gen/models/wan/wan_vae.py`, `tensorrt_llm/_torch/visual_gen/modules/vae/conv.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+2 more__
- **2026-08-11** [`3da22933c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3da22933c9) [#17405](https://github.com/NVIDIA/TensorRT-LLM/pull/17405)
  [None][test] use skip_less_mpi_world_size instead of skip_less_device (#17405)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/test_e2e.py`_
- **2026-08-10** [`685a6c0d5b`](https://github.com/NVIDIA/TensorRT-LLM/commit/685a6c0d5b) [#17003](https://github.com/NVIDIA/TensorRT-LLM/pull/17003)
  [TRTLLM-14798][perf] Fuse Wan DupUp3D output mapping (#17003)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/dup_up3d.py`, `tensorrt_llm/_torch/visual_gen/models/wan/wan_vae.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/visual_gen/test_wan_dup_up3d.py`_

## Other  (9 commits)

- **2026-08-17** [`77f941f262`](https://github.com/NVIDIA/TensorRT-LLM/commit/77f941f262) [#16358](https://github.com/NVIDIA/TensorRT-LLM/pull/16358)
  [https://nvbugs/6435126][test] Attribute fatal test_unittests_v2 failures to inner tests (#16358)
  _Files: `tests/integration/defs/test_unittests.py`, `tests/unittest/tools/test_unittest_culprits.py`_
- **2026-08-13** [`7647daa14e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7647daa14e) [#17637](https://github.com/NVIDIA/TensorRT-LLM/pull/17637)
  [None][fix] Suppress mypy redundant-cast for the sampler module (#17637)
  _Files: `pyproject.toml`_
- **2026-08-13** [`1e0b9a1446`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e0b9a1446) [#17602](https://github.com/NVIDIA/TensorRT-LLM/pull/17602)
  [TRTLLM-15157][fix] scan all pages in stale PR cleanup (#17602)
  _Files: `.github/scripts/cleanup_stale_prs.test.js`, `.github/workflows/cleanup-stale-prs.yml`_
- **2026-08-12** [`6860d64c20`](https://github.com/NVIDIA/TensorRT-LLM/commit/6860d64c20) [#17571](https://github.com/NVIDIA/TensorRT-LLM/pull/17571)
  [None][fix] Update llm_function_core.txt (#17571)
- **2026-08-12** [`751a6d469f`](https://github.com/NVIDIA/TensorRT-LLM/commit/751a6d469f) [#17579](https://github.com/NVIDIA/TensorRT-LLM/pull/17579)
  [None][fix] remove duplicated test (#17579)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-08-12** [`430c0fea73`](https://github.com/NVIDIA/TensorRT-LLM/commit/430c0fea73) [#17549](https://github.com/NVIDIA/TensorRT-LLM/pull/17549)
  [None][chore] add backup owner for scaffolding (#17549)
  _Files: `.github/CODEOWNERS`_
- **2026-08-12** [`d5b1818ab9`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5b1818ab9) [#17387](https://github.com/NVIDIA/TensorRT-LLM/pull/17387)
  [None][test] Cover KVCacheManagerV2 C++ pool rebalance path (#17387)
  _Files: `cpp/tests/unit_tests/batch_manager/CMakeLists.txt`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerV2SlotAllocatorTest.cpp`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-08-11** [`02c41b7739`](https://github.com/NVIDIA/TensorRT-LLM/commit/02c41b7739) [#11562](https://github.com/NVIDIA/TensorRT-LLM/pull/11562)
  [None][fix] Update to get central version variable for trtllm-bench. (#11562)
  _Files: `tensorrt_llm/bench/benchmark/utils/general.py`_
- **2026-08-10** [`6ccdb019cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ccdb019cd) [#16850](https://github.com/NVIDIA/TensorRT-LLM/pull/16850)
  [https://nvbugs/6506990][fix] Don't treat NVLE-only as CC enabled (#16850)
  _Files: `tensorrt_llm/_utils.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/utils/test_confidential_compute.py`_

## AutoDeploy  (2 commits)

- **2026-08-13** [`86dbc1c95f`](https://github.com/NVIDIA/TensorRT-LLM/commit/86dbc1c95f) [#17653](https://github.com/NVIDIA/TensorRT-LLM/pull/17653)
  [https://nvbugs/6606123][test] Waive AutoDeploy shim SWA-eviction + mamba-cache unit tests (setup OOM) (#17653)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-11** [`4a3cbe4964`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a3cbe4964) [#15642](https://github.com/NVIDIA/TensorRT-LLM/pull/15642)
  [None][chore] Add deprecation notice for _autodeploy backend (#15642)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/unittest/api_stability/references/trtllm_serve_cli.yaml`_

## Docs / Examples  (2 commits)

- **2026-08-13** [`e3b63fe77c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3b63fe77c) [#17524](https://github.com/NVIDIA/TensorRT-LLM/pull/17524)
  [TRTLLM-14628][feat] Support out-of-tree build state via --build_root (#17524)
  _Files: `docs/source/installation/build-from-source.md`, `scripts/build_wheel.py`, `setup.py`_
- **2026-08-11** [`59e8079ab0`](https://github.com/NVIDIA/TensorRT-LLM/commit/59e8079ab0) [#17481](https://github.com/NVIDIA/TensorRT-LLM/pull/17481)
  [None][chore] Bump version to 1.3.0rc25 (#17481)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## Perf  (1 commits)

- **2026-08-15** [`584aafbe6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/584aafbe6c) [#17538](https://github.com/NVIDIA/TensorRT-LLM/pull/17538)
  [TRTLLM-14628][perf] Incremental, streamed artifact copy-back into the checkout (#17538)
  _Files: `docs/source/installation/build-from-source.md`, `scripts/build_wheel.py`, `tests/unittest/scripts/test_build_wheel_copy_back.py`_

## LoRA  (1 commits)

- **2026-08-13** [`3c68ae6ac7`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c68ae6ac7) [#17179](https://github.com/NVIDIA/TensorRT-LLM/pull/17179)
  [None][refactor] Organize SMG gRPC adapter by protocol (#17179)
  _Files: `.github/CODEOWNERS`, `docker/Dockerfile.multi`, `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_install.sh` _+13 more__

## ROCm / AMD  (1 commits)

- **2026-08-12** [`3d3d7c9192`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d3d7c9192) [#17223](https://github.com/NVIDIA/TensorRT-LLM/pull/17223)
  [https://nvbugs/6480621][fix] Preserve KV ownership in disaggregated precheck (#17223)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/README.md`, `examples/disaggregated/slurm/cache_transceiver_test/config.yaml`, `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `jenkins/scripts/perf/local/submit.py` _+13 more__

---
_Generated 2026-08-17 08:57 UTC_