# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-09-07 → 2026-09-14  |  **Total commits:** 227

## ✨ New Features This Week

- **2026-09-14** [#19012](https://github.com/NVIDIA/TensorRT-LLM/pull/19012) — [None][test] Add Qwen 3.8 MAX and Flash-next performance coverage (#19012)
- **2026-09-14** [#18853](https://github.com/NVIDIA/TensorRT-LLM/pull/18853) — [None][test] Add single-node disagg DEP4 DSpark GSM8K test for DeepSeek-V4-Flash NVFP4 (#18853)
- **2026-09-14** [#19017](https://github.com/NVIDIA/TensorRT-LLM/pull/19017) — [None][test] Add coverage for BartForConditionalGeneration (#19017)
- **2026-09-14** [#18765](https://github.com/NVIDIA/TensorRT-LLM/pull/18765) — [None][feat] Add SM107 CuTe DSL quantized dense GEMM/BMM custom ops and dispatch (#18765)
- **2026-09-14** [#18399](https://github.com/NVIDIA/TensorRT-LLM/pull/18399) — [None][feat] Support num_postprocess_workers > 0 under the Ray Orchestration (#18399)
- **2026-09-14** [#18948](https://github.com/NVIDIA/TensorRT-LLM/pull/18948) — [None][test] Add native PyTorch coverage for DeciLMForCausalLM (#18948)
- **2026-09-13** [#18754](https://github.com/NVIDIA/TensorRT-LLM/pull/18754) — [None][feat] Add opt-in KV guard page and fresh-page fill diagnostics (#18754)
- **2026-09-13** [#18632](https://github.com/NVIDIA/TensorRT-LLM/pull/18632) — [TRTLLM-16122][feat] Refine VisualGen serve benching (#18632)
- **2026-09-12** [#18733](https://github.com/NVIDIA/TensorRT-LLM/pull/18733) — [TRTLLM-16194][feat] Add MiniMax H3 support (#18733)
- **2026-09-12** [#18761](https://github.com/NVIDIA/TensorRT-LLM/pull/18761) — [None][feat] Add SM107 CuTe DSL BF16 dense GEMM/BMM custom ops and dispatch (#18761)
- _…and 48 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-14** [`858a360ffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/858a360ffe) [#18861](https://github.com/NVIDIA/TensorRT-LLM/pull/18861) — [None][chore] Refine QA code ownership (#18861)
- **2026-09-11** [`0628a73388`](https://github.com/NVIDIA/TensorRT-LLM/commit/0628a73388) [#18908](https://github.com/NVIDIA/TensorRT-LLM/pull/18908) — [None][test] add guided decoding architecture coverage (#18908)
- **2026-09-10** [`05838cebf4`](https://github.com/NVIDIA/TensorRT-LLM/commit/05838cebf4) [#18827](https://github.com/NVIDIA/TensorRT-LLM/pull/18827) — [TRTLLM-15714][refactor] Move disagg send/reap/timeout/cancel orchestration into DisaggTransferCoordinator (#18827)
- **2026-09-10** [`bccc86ad59`](https://github.com/NVIDIA/TensorRT-LLM/commit/bccc86ad59) [#18041](https://github.com/NVIDIA/TensorRT-LLM/pull/18041) — [None][fix] bridge FP4 MLA disaggregated KV ownership (#18041)
- **2026-09-09** [`5f7e4cc68a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f7e4cc68a) [#18905](https://github.com/NVIDIA/TensorRT-LLM/pull/18905) — [None][test] expand speculative decoding model coverage (#18905)
- **2026-09-08** [`9dfa2e21e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/9dfa2e21e1) [#18343](https://github.com/NVIDIA/TensorRT-LLM/pull/18343) — [None][feat] Page the DSpark drafter context through the draft KV cache manager (#18343)
- **2026-09-07** [`5fa39642b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa39642b9) [#18699](https://github.com/NVIDIA/TensorRT-LLM/pull/18699) — [None][test] add Kimi K3 feature matrix coverage (#18699)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#19067](https://github.com/NVIDIA/TensorRT-LLM/issues/19067) | [Bug]: -a 107-real is silently folded to 100, no SM107 code is generat | Infra | 2026-09-11 |
| [#19059](https://github.com/NVIDIA/TensorRT-LLM/issues/19059) | [Bug]: C++17 build cannot compile torch 2.12 headers with nvcc, but C+ | Pytorch | 2026-09-11 |
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-09-09 |
| [#18847](https://github.com/NVIDIA/TensorRT-LLM/issues/18847) | [Bug] Worker CPU affinity is applied process-wide in shared-process de | Inference runtime | 2026-09-07 |
| [#18660](https://github.com/NVIDIA/TensorRT-LLM/issues/18660) | [Bug]: KVCacheManagerV2 + DSA: indexer (draft) cache pool is not part  | KV-Cache Management | 2026-09-04 |
| [#18687](https://github.com/NVIDIA/TensorRT-LLM/issues/18687) | [Bug]: Cosmos3 sequence-parallel path attends zero-padded text K/V whe | bug, VisualGen | 2026-09-03 |
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-09-02 |
| [#18407](https://github.com/NVIDIA/TensorRT-LLM/issues/18407) | [Bug]: KVCacheV2Scheduler retains active PEFT adapters after KV suspen | KV-Cache Management, Lora/P-tuning, Pytorch | 2026-08-30 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-08-27 |
| [#18156](https://github.com/NVIDIA/TensorRT-LLM/issues/18156) | KV-cache-aware router never matches LoRA or salted requests: lora_id i | Disaggregated serving | 2026-08-24 |
| [#18153](https://github.com/NVIDIA/TensorRT-LLM/issues/18153) | [RFC]: Versioned KV Hints Protocol for TRT-LLM | RFC | 2026-08-24 |
| [#18085](https://github.com/NVIDIA/TensorRT-LLM/issues/18085) | [RFC] DFlash2 for Qwen3.8 on consumer Blackwell: integration boundary  | Speculative Decoding | 2026-08-21 |
| [#17714](https://github.com/NVIDIA/TensorRT-LLM/issues/17714) | [Feature] NcclEP backend hardcodes LOW_LATENCY + RANK_MAJOR; algorithm | Scale-out | 2026-08-14 |
| [#10014](https://github.com/NVIDIA/TensorRT-LLM/issues/10014) | [Documentation] AWS EFA/LIBFABRIC deployment guide for disaggregated i | Doc, Disaggregated serving | 2026-08-12 |
| [#16827](https://github.com/NVIDIA/TensorRT-LLM/issues/16827) | [Performance]: MAX_UTILIZATION causes a 40.6% output-throughput drop a | KV-Cache Management, Pytorch, General perf | 2026-08-09 |
| [#17437](https://github.com/NVIDIA/TensorRT-LLM/issues/17437) | [Bug]: Interior control-token rejection can split a tool-call prelude  | Speculative Decoding | 2026-08-08 |
| [#17016](https://github.com/NVIDIA/TensorRT-LLM/issues/17016) | [RFC]: Add openengine gRPC server support to trtllm-serve | RFC | 2026-08-03 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-07-29 |
| [#17020](https://github.com/NVIDIA/TensorRT-LLM/issues/17020) | `trtllm-eval aime25`/`aime26` silently disable thinking on DeepSeek-V4 | — | 2026-07-29 |
| [#17013](https://github.com/NVIDIA/TensorRT-LLM/issues/17013) | [RFC]: Reduce overhead in KV cache event publishing | RFC | 2026-07-29 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 45 |
| Attention | 39 |
| Executor / Runtime | 28 |
| MoE | 26 |
| Other | 19 |
| Disaggregation / KV | 16 |
| Quantization | 12 |
| Docs / Examples | 10 |
| Torch Path (_torch) | 8 |
| ROCm / AMD | 7 |
| Speculative Decoding | 6 |
| Models | 6 |
| LoRA | 3 |
| AutoDeploy | 2 |

## CI / Infra  (45 commits)

- **2026-09-14** [`0941472b13`](https://github.com/NVIDIA/TensorRT-LLM/commit/0941472b13) [#19121](https://github.com/NVIDIA/TensorRT-LLM/pull/19121)
  [None][test] Waive 4 failed cases for main in QA CI (#19121)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`a0a81ddeb7`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0a81ddeb7) [#19141](https://github.com/NVIDIA/TensorRT-LLM/pull/19141)
  [None][infra] Correct an NvBug ID in the waive list (#19141)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`35687ce585`](https://github.com/NVIDIA/TensorRT-LLM/commit/35687ce585) [#19123](https://github.com/NVIDIA/TensorRT-LLM/pull/19123)
  [None][infra] Waive 5 failed cases for main in pre-merge 60083 (#19123)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`bb69dbcfbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb69dbcfbe) [#19133](https://github.com/NVIDIA/TensorRT-LLM/pull/19133)
  [None][test] Waive 5 failed cases for main in QA CI (#19133)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`e62069ac75`](https://github.com/NVIDIA/TensorRT-LLM/commit/e62069ac75) [#19127](https://github.com/NVIDIA/TensorRT-LLM/pull/19127)
  [None][test] Waive 6 failed cases for main in QA CI (#19127)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`575bac25a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/575bac25a0) [#19131](https://github.com/NVIDIA/TensorRT-LLM/pull/19131)
  [None][infra] Waive 1 failed cases for main in pre-merge 60095 (#19131)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`df3195fe0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/df3195fe0f) [#19125](https://github.com/NVIDIA/TensorRT-LLM/pull/19125)
  [None][test] Waive 3 failed cases for main in QA CI (#19125)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`a18abf94f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a18abf94f3)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-09-13** [`3f43bb0fb7`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f43bb0fb7) [#18049](https://github.com/NVIDIA/TensorRT-LLM/pull/18049)
  [None][infra] Classify SLURM resource-cleanup failures as typed infra (#18049)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-12** [`918d242520`](https://github.com/NVIDIA/TensorRT-LLM/commit/918d242520) [#19104](https://github.com/NVIDIA/TensorRT-LLM/pull/19104)
  [None][infra] Waive 1 failed cases for main in pre-merge 60005 (#19104)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-12** [`f42378a63c`](https://github.com/NVIDIA/TensorRT-LLM/commit/f42378a63c) [#19074](https://github.com/NVIDIA/TensorRT-LLM/pull/19074)
  [None][ci] Switch GB300 perf sanity stages to auto:gb300-flex (#19074)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-11** [`bdedf3fd51`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdedf3fd51) [#19079](https://github.com/NVIDIA/TensorRT-LLM/pull/19079)
  [https://nvbugs/6662724][fix] Remove validated H100 waivers (#19079)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`3364553683`](https://github.com/NVIDIA/TensorRT-LLM/commit/3364553683) [#19066](https://github.com/NVIDIA/TensorRT-LLM/pull/19066)
  [https://nvbugs/6608387][test] Unwaive test_overlap_scheduler cases tracked by 6608387 (#19066)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`09ec9ecf42`](https://github.com/NVIDIA/TensorRT-LLM/commit/09ec9ecf42) [#19073](https://github.com/NVIDIA/TensorRT-LLM/pull/19073)
  [None][infra] Waive 4 failed cases for main in post-merge 2959 (#19073)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`31b47b67eb`](https://github.com/NVIDIA/TensorRT-LLM/commit/31b47b67eb) [#19052](https://github.com/NVIDIA/TensorRT-LLM/pull/19052)
  [None][test] consolidate CBTS unit tests in CPU stage (#19052)
  _Files: `tests/unittest/scripts/test_cbts.py`, `tests/unittest/scripts/test_cbts_coverage_artifact.py`, `tests/unittest/scripts/test_cbts_coverage_pilot.py`, `tests/unittest/scripts/test_cbts_tests_def_rule.py` _+1 more__
- **2026-09-11** [`460d437a9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/460d437a9d) [#19062](https://github.com/NVIDIA/TensorRT-LLM/pull/19062)
  [None][infra] Add blossom-ci authorized users (#19062)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-09-11** [`e13e487195`](https://github.com/NVIDIA/TensorRT-LLM/commit/e13e487195) [#18880](https://github.com/NVIDIA/TensorRT-LLM/pull/18880)
  [None][fix] Narrow CBTS perf helper selection (#18880)
  _Files: `jenkins/scripts/cbts/rules/tests_def_rule.py`, `tests/unittest/scripts/test_cbts_tests_def_rule.py`_
- **2026-09-11** [`7535668a3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7535668a3d) [#18928](https://github.com/NVIDIA/TensorRT-LLM/pull/18928)
  [https://nvbugs/6644465][test] Unwaive WAN pipeline parallel test (#18928)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`74ebe72e44`](https://github.com/NVIDIA/TensorRT-LLM/commit/74ebe72e44) [#19042](https://github.com/NVIDIA/TensorRT-LLM/pull/19042)
  [None][infra] Waive 3 failed cases for main in post-merge 2958 (#19042)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`a738a2767c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a738a2767c) [#19039](https://github.com/NVIDIA/TensorRT-LLM/pull/19039)
  [None][test] Waive 5 failed cases for A100 (#19039)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-10** [`6366555682`](https://github.com/NVIDIA/TensorRT-LLM/commit/6366555682) [#19027](https://github.com/NVIDIA/TensorRT-LLM/pull/19027)
  [None][infra] Waive 1 failed cases for main in pre-merge 59731 (#19027)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-10** [`c31bfcc2e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/c31bfcc2e4) [#19010](https://github.com/NVIDIA/TensorRT-LLM/pull/19010)
  [None][infra] Waive 2 failed cases for main in post-merge 2957 (#19010)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-10** [`8a931f6196`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a931f6196) [#18982](https://github.com/NVIDIA/TensorRT-LLM/pull/18982)
  [TRTLLMINF-368][infra] update cluster config for OCI-JHB (#18982)
  _Files: `jenkins/scripts/perf/cluster_env.py`, `tests/unittest/scripts/test_cluster_env.py`_
- **2026-09-10** [`d77225c96f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d77225c96f) [#18980](https://github.com/NVIDIA/TensorRT-LLM/pull/18980)
  [https://nvbugs/6670516][fix] Call build_kv_page_indices with current signature (#18980)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/microbenchmarks/minimax_m3_index_decode_score.py`_
- **2026-09-09** [`e76ae7849e`](https://github.com/NVIDIA/TensorRT-LLM/commit/e76ae7849e) [#18981](https://github.com/NVIDIA/TensorRT-LLM/pull/18981)
  [None][infra] Waive 1 failed cases for main in pre-merge 59492 (#18981)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`bca6761ab8`](https://github.com/NVIDIA/TensorRT-LLM/commit/bca6761ab8) [#17069](https://github.com/NVIDIA/TensorRT-LLM/pull/17069)
  [https://nvbugs/6530090][fix] autoinstall media deps within test framework (#17069)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/local/slurm_install.sh`, `jenkins/scripts/perf/local/slurm_run.sh`, `jenkins/scripts/slurm_install.sh` _+3 more__
- **2026-09-09** [`dbf6b27a3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbf6b27a3b) [#18958](https://github.com/NVIDIA/TensorRT-LLM/pull/18958)
  [None][infra] Waive 4 failed cases for main in post-merge 2956 (#18958)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`26e8c99a4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/26e8c99a4a) [#18386](https://github.com/NVIDIA/TensorRT-LLM/pull/18386)
  [https://nvbugs/6655990][test] Gate WAN multi-GPU LPIPS against a within-build reference and unwaive (#18386)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_multi_gpu.py`, `tests/integration/defs/examples/visual_gen/visual_gen_test_utils.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`e3b22d6804`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3b22d6804) [#18918](https://github.com/NVIDIA/TensorRT-LLM/pull/18918)
  [None][test] Waive 2 failed cases for main in QA CI (#18918)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`f248c9a2fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/f248c9a2fd) [#18916](https://github.com/NVIDIA/TensorRT-LLM/pull/18916)
  [None][infra] Waive 1 failed cases for main in pre-merge 59274 (#18916)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`f143c5b7a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f143c5b7a4) [#18384](https://github.com/NVIDIA/TensorRT-LLM/pull/18384)
  [https://nvbugs/6655986][test] Raise LTX-2 LPIPS golden thresholds to 0.15 and unwaive (#18384)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_ltx2.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`baa8809352`](https://github.com/NVIDIA/TensorRT-LLM/commit/baa8809352) [#18911](https://github.com/NVIDIA/TensorRT-LLM/pull/18911)
  [https://nvbugs/6572838][ci] Unwaive fixed test (#18911)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`c495ad18f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/c495ad18f3) [#18732](https://github.com/NVIDIA/TensorRT-LLM/pull/18732)
  [https://nvbugs/6676844][test] Unwaive test_wan_t2v_example after CI checkpoint storage fix (#18732)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`d48c0d0aac`](https://github.com/NVIDIA/TensorRT-LLM/commit/d48c0d0aac) [#18889](https://github.com/NVIDIA/TensorRT-LLM/pull/18889)
  [None][infra] Waive 2 failed cases for main in post-merge 2955 (#18889)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`1a28b08b26`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a28b08b26) [#18859](https://github.com/NVIDIA/TensorRT-LLM/pull/18859)
  [https://nvbugs/6682113][fix] give gb300 v4-pro con4301 ctx_only perf-sanity the 120min budget its workload already carries (#18859)
  _Files: `tests/integration/test_lists/test-db/l0_gb300_multi_gpus_perf_sanity.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`55761d7dcc`](https://github.com/NVIDIA/TensorRT-LLM/commit/55761d7dcc) [#18729](https://github.com/NVIDIA/TensorRT-LLM/pull/18729)
  [TRTLLMINF-396][ci] Auto-label fully approved pre-merge PRs (#18729)
  _Files: `.github/workflows/full-premerge-approval-signal.yml`, `.github/workflows/full-premerge-approval.yml`_
- **2026-09-08** [`3810f4ee50`](https://github.com/NVIDIA/TensorRT-LLM/commit/3810f4ee50) [#18829](https://github.com/NVIDIA/TensorRT-LLM/pull/18829)
  [https://nvbugs/6621358][test] Unwaive tests tracked by NVBug 6621358 (#18829)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`b6d67a8fa1`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6d67a8fa1) [#18590](https://github.com/NVIDIA/TensorRT-LLM/pull/18590)
  [TRTLLMINF-334][infra] Report FAILURE for unrerun test failures skipped due to duration/no-signature match (#18590)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/test_rerun.py`, `tests/integration/defs/conftest.py`, `tests/integration/defs/utils/periodic_junit.py`_
- **2026-09-08** [`d7ae24756e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7ae24756e) [#18860](https://github.com/NVIDIA/TensorRT-LLM/pull/18860)
  [None][infra] Waive 8 failed cases for main in post-merge 2954 (#18860)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`5e4dc03d72`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e4dc03d72) [#18490](https://github.com/NVIDIA/TensorRT-LLM/pull/18490)
  [None][test] Cleanup/multinode test list (#18490)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_multinode.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`3811a8157d`](https://github.com/NVIDIA/TensorRT-LLM/commit/3811a8157d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-09-07** [`3a3871d8b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a3871d8b1) [#18791](https://github.com/NVIDIA/TensorRT-LLM/pull/18791)
  [TRTLLMINF-250][infra] Migrate BoltProfileGen JNLP image to Artifactory (#18791)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-07** [`3c9d1f910c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c9d1f910c) [#18796](https://github.com/NVIDIA/TensorRT-LLM/pull/18796)
  [None][test] Waive 1 failed cases for main in QA CI (#18796)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-07** [`42347b8be9`](https://github.com/NVIDIA/TensorRT-LLM/commit/42347b8be9) [#18795](https://github.com/NVIDIA/TensorRT-LLM/pull/18795)
  [None][test] Waive 15 failed cases for main in QA CI (#18795)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-07** [`c21a90820a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c21a90820a)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_

## Attention  (39 commits)

- **2026-09-14** [`3fdcef6f22`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fdcef6f22) [#19012](https://github.com/NVIDIA/TensorRT-LLM/pull/19012)
  [None][test] Add Qwen 3.8 MAX and Flash-next performance coverage (#19012)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-14** [`dd6759a435`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd6759a435) [#18853](https://github.com/NVIDIA/TensorRT-LLM/pull/18853)
  [None][test] Add single-node disagg DEP4 DSpark GSM8K test for DeepSeek-V4-Flash NVFP4 (#18853)
  _Files: `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_disaggregated_serving.py` _+1 more__
- **2026-09-14** [`357c02e4f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/357c02e4f3) [#18765](https://github.com/NVIDIA/TensorRT-LLM/pull/18765)
  [None][feat] Add SM107 CuTe DSL quantized dense GEMM/BMM custom ops and dispatch (#18765)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+4 more__
- **2026-09-14** [`8f99f59c10`](https://github.com/NVIDIA/TensorRT-LLM/commit/8f99f59c10) [#19119](https://github.com/NVIDIA/TensorRT-LLM/pull/19119)
  [None][ci] Waive TestQwen3_8_Flash_Next::test_fp8_adp4_mtp3_trtllm_ple_offload on main (#19119)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-13** [`63f271cc17`](https://github.com/NVIDIA/TensorRT-LLM/commit/63f271cc17) [#18754](https://github.com/NVIDIA/TensorRT-LLM/pull/18754)
  [None][feat] Add opt-in KV guard page and fresh-page fill diagnostics (#18754)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py` _+2 more__
- **2026-09-12** [`63cff55d85`](https://github.com/NVIDIA/TensorRT-LLM/commit/63cff55d85) [#18824](https://github.com/NVIDIA/TensorRT-LLM/pull/18824)
  [None][fix] Filter zero-size buffers in KVCM V2 runtime wrapper (#18824)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/storage/core.cpp`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_storage/_core.py` _+5 more__
- **2026-09-12** [`9364a2a210`](https://github.com/NVIDIA/TensorRT-LLM/commit/9364a2a210) [#18761](https://github.com/NVIDIA/TensorRT-LLM/pull/18761)
  [None][feat] Add SM107 CuTe DSL BF16 dense GEMM/BMM custom ops and dispatch (#18761)
  _Files: `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py` _+2 more__
- **2026-09-12** [`78107e2a20`](https://github.com/NVIDIA/TensorRT-LLM/commit/78107e2a20) [#18553](https://github.com/NVIDIA/TensorRT-LLM/pull/18553)
  [None][perf] DFlash draft latency for Qwen3.5-4B (#18553)
  _Files: `docs/source/features/speculative-decoding.md`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_utils.py`, `tensorrt_llm/_torch/models/modeling_dflash.py` _+12 more__
- **2026-09-12** [`a76e0b2b40`](https://github.com/NVIDIA/TensorRT-LLM/commit/a76e0b2b40) [#18769](https://github.com/NVIDIA/TensorRT-LLM/pull/18769)
  [None][fix] Re-plan FlashInfer decode schedule on page-table changes under CUDA graphs (#18769)
  _Files: `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tests/unittest/_torch/attention/test_flashinfer_attention.py`_
- **2026-09-12** [`b7681d7f96`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7681d7f96) [#18611](https://github.com/NVIDIA/TensorRT-LLM/pull/18611)
  [None][perf] Wire in custom decode kernels for MinimaxM3 (#18611)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/__init__.py`, `tensorrt_llm/_torch/attention/backends/fmha/msa_decode.py`, `tensorrt_llm/_torch/attention/backends/fmha/msa_prefill.py` _+21 more__
- **2026-09-11** [`a85c26c624`](https://github.com/NVIDIA/TensorRT-LLM/commit/a85c26c624) [#18758](https://github.com/NVIDIA/TensorRT-LLM/pull/18758)
  [None][fix] Map SM107 to the sm_100f NVRTC target in the trtllm-gen FMHA kernel loader (#18758)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-09-11** [`c6f98058c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/c6f98058c8) [#18815](https://github.com/NVIDIA/TensorRT-LLM/pull/18815)
  [None][feat] add generic PrimTS block-sparse FMHA and unify sparse attention runtime inputs (#18815)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `docs/source/developer-guide/sparse-attention-development-guide.md`, `docs/source/features/sparse-attention.md` _+42 more__
- **2026-09-11** [`7351c9c882`](https://github.com/NVIDIA/TensorRT-LLM/commit/7351c9c882) [#18812](https://github.com/NVIDIA/TensorRT-LLM/pull/18812)
  [None][test] Add timeouts to test subprocesses (#18812)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_disaggregated_etcd.py`, `tests/integration/defs/examples/visual_gen/visual_gen_test_utils.py`, `tests/integration/defs/kimi_k3_disagg_parity.py` _+31 more__
- **2026-09-11** [`cdb12988b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/cdb12988b2) [#18767](https://github.com/NVIDIA/TensorRT-LLM/pull/18767)
  [None][feat] Derive per-layer KV cache windows from layer_types (#18767)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/unittest/_torch/executor/test_layer_type_attention_windows.py`_
- **2026-09-11** [`e4fbe98f95`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4fbe98f95) [#17685](https://github.com/NVIDIA/TensorRT-LLM/pull/17685)
  [None][perf] Enable FlashInfer add-RMSNorm for NVFP4 Marlin (#17685)
  _Files: `tensorrt_llm/_torch/modules/rms_norm.py`_
- **2026-09-11** [`e7e301714f`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7e301714f) [#18945](https://github.com/NVIDIA/TensorRT-LLM/pull/18945)
  [https://nvbugs/6737351][fix] Remove CGA smem-reduction clamp from trtllm-gen FMHA kernel selection (#18945)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-09-11** [`81485db3d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/81485db3d1) [#18996](https://github.com/NVIDIA/TensorRT-LLM/pull/18996)
  [None][fix] Update vendored PrimTS with FlashInfer #4829 follow-ups (#18996)
  _Files: `3rdparty/vendor_patches/flashinfer-prims-ts.patch`, `3rdparty/vendor_sources.lock.yaml`, `tensorrt_llm/_torch/attention/backends/prims_ts/context.py`, `tensorrt_llm/_torch/attention/backends/prims_ts/decode.py` _+5 more__
- **2026-09-11** [`7619b86925`](https://github.com/NVIDIA/TensorRT-LLM/commit/7619b86925) [#19008](https://github.com/NVIDIA/TensorRT-LLM/pull/19008)
  [None][refactor] Centralize FMHA availability and support capability checks (#19008)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_sparse_mla.py` _+9 more__
- **2026-09-10** [`74f97c0387`](https://github.com/NVIDIA/TensorRT-LLM/commit/74f97c0387) [#18075](https://github.com/NVIDIA/TensorRT-LLM/pull/18075)
  [None][feat] Add cuDNN attention backend (#18075)
  _Files: `docs/source/features/visualgen-quantized-attention.md`, `docs/source/models/visual-generation.md`, `requirements.txt`, `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py` _+7 more__
- **2026-09-10** [`fbac78bd2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/fbac78bd2a) [#17365](https://github.com/NVIDIA/TensorRT-LLM/pull/17365)
  [None][perf] optimize qwen3.5 perf by removing gather and scatter op (#17365)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py`_
- **2026-09-10** [`26b57136ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/26b57136ee) [#18141](https://github.com/NVIDIA/TensorRT-LLM/pull/18141)
  [https://nvbugs/6530268][fix] Fix XQA race condition and attn sink numerical accuracy (#18141)
  _Files: `cpp/kernels/xqa/mha.cu`_
- **2026-09-10** [`f5fabd47d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5fabd47d5) [#18883](https://github.com/NVIDIA/TensorRT-LLM/pull/18883)
  [None][perf] fuse decode kernel seams for Qwen3.8-Flash-Next and de-vendor the low-M GEMMs (#18883)
  _Files: `tensorrt_llm/_torch/attention/attention.py`, `tensorrt_llm/_torch/attention/backends/sparse/hooks.py`, `tensorrt_llm/_torch/attention/backends/sparse/qsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/qsa/kernels.py` _+14 more__
- **2026-09-10** [`4bc68db85d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4bc68db85d) [#18792](https://github.com/NVIDIA/TensorRT-LLM/pull/18792)
  [TRTLLM-11484][doc] VisualGen separate out quantized-attention.md (#18792)
  _Files: `docs/source/blogs/tech_blog/blog28_Accelerating_Video_Generation_with_GEMM_Quantization_Attention_Quantization_and_Skip_Softmax_Attention_in_TensorRT-LLM.md`, `docs/source/features/visualgen-cuda-graph.md`, `docs/source/features/visualgen-quantized-attention.md`, `docs/source/features/visualgen-sparse-attention.md` _+2 more__
- **2026-09-10** [`ff667d791d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff667d791d) [#18984](https://github.com/NVIDIA/TensorRT-LLM/pull/18984)
  [None][doc] Fix broken images in tech blogs 27 and 28 (#18984)
  _Files: `docs/source/blogs/tech_blog/blog27_Evaluating_Agentic_Serving_with_Trace_Replay_and_Job_Level_Metrics.md`, `docs/source/blogs/tech_blog/blog28_Accelerating_Video_Generation_with_GEMM_Quantization_Attention_Quantization_and_Skip_Softmax_Attention_in_TensorRT-LLM.md`_
- **2026-09-10** [`8e2c261286`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e2c261286) [#18869](https://github.com/NVIDIA/TensorRT-LLM/pull/18869)
  [None][perf] Optimize HCA compressor decode (#18869)
  _Files: `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.h`, `cpp/tensorrt_llm/thop/compressorOp.cpp`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_compressor_kernel.py`_
- **2026-09-09** [`e8e3afc0d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8e3afc0d3) [#18925](https://github.com/NVIDIA/TensorRT-LLM/pull/18925)
  [https://nvbugs/6641268][fix] Zero paged V-cache tails during context preprocessing (#18925)
  _Files: `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-09-09** [`9c766dcd58`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c766dcd58) [#18678](https://github.com/NVIDIA/TensorRT-LLM/pull/18678)
  [https://nvbugs/6695563][fix] Densify the bmm LHS with `a.contiguous()` gated on get_sm_version() in (120… (#18678)
  _Files: `tensorrt_llm/_torch/attention/mla.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`a3e6cc1535`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3e6cc1535) [#18557](https://github.com/NVIDIA/TensorRT-LLM/pull/18557)
  [https://nvbugs/6689016][fix] Limit eager FlashInfer plan cache growth (#18557)
  _Files: `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/test_flashinfer_attention.py`_
- **2026-09-09** [`7e397a06ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e397a06ed) [#17643](https://github.com/NVIDIA/TensorRT-LLM/pull/17643)
  [None][fix] Fix handling of hybrid FlashInfer page tables with KV cache V2 (#17643)
  _Files: `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/attention/test_flashinfer_attention.py`_
- **2026-09-09** [`40d3bc2159`](https://github.com/NVIDIA/TensorRT-LLM/commit/40d3bc2159) [#18901](https://github.com/NVIDIA/TensorRT-LLM/pull/18901)
  [None][docs] fix --config kv_cache_dtype samples and trtllm-serve positional model path (#18901)
  _Files: `AGENTS.md`, `docs/source/blogs/Best_perf_practice_on_DeepSeek-R1_in_TensorRT-LLM.md`, `docs/source/commands/trtllm-serve/run-benchmark-with-trtllm-serve.md`, `docs/source/legacy/performance/perf-benchmarking.md` _+3 more__
- **2026-09-09** [`e1e6bcca3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1e6bcca3b) [#18823](https://github.com/NVIDIA/TensorRT-LLM/pull/18823)
  [TRTLLM-16182][fix] load the mixed-precision Qwen3.8-Flash-Next NVFP4 checkpoint (#18823)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen4_exp.py`, `tensorrt_llm/_torch/modules/qwen4_exp/ple.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml` _+7 more__
- **2026-09-08** [`cca440c776`](https://github.com/NVIDIA/TensorRT-LLM/commit/cca440c776) [#18106](https://github.com/NVIDIA/TensorRT-LLM/pull/18106)
  [None][test] Add sparse MQA/GQA coverage and support documentation (#18106)
  _Files: `docs/source/developer-guide/sparse-attention-development-guide.md`, `docs/source/features/sparse-attention.md`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py` _+26 more__
- **2026-09-08** [`12da5f270c`](https://github.com/NVIDIA/TensorRT-LLM/commit/12da5f270c) [#18750](https://github.com/NVIDIA/TensorRT-LLM/pull/18750)
  [TRTLLM-11484][fix] Address Quantization Regressions for VisualGen CuTeDSL FMHA (#18750)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/fmha.py`, `tensorrt_llm/_torch/visual_gen/cute_dsl_kernels/blackwell/attention/fmha.py`, `tensorrt_llm/_torch/visual_gen/cute_dsl_kernels/blackwell/attention/fmha_blockscaled.py`, `tests/unittest/_torch/visual_gen/test_attention_cute_dsl.py`_
- **2026-09-08** [`d321907619`](https://github.com/NVIDIA/TensorRT-LLM/commit/d321907619) [#18653](https://github.com/NVIDIA/TensorRT-LLM/pull/18653)
  [TRTLLM-15033][fix] Revert #17800 FlashInfer CuTeDSL MLA dispatch (#18653)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `examples/kimi_k3/README.md`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py` _+12 more__
- **2026-09-08** [`adedc0680e`](https://github.com/NVIDIA/TensorRT-LLM/commit/adedc0680e) [#18437](https://github.com/NVIDIA/TensorRT-LLM/pull/18437)
  [TRTLLM-15621][feat] Support in-graph sampling for temperature/top-k/top-p batches (#18437)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py` _+11 more__
- **2026-09-08** [`00ebdeb9d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/00ebdeb9d7) [#18840](https://github.com/NVIDIA/TensorRT-LLM/pull/18840)
  [None][chore] add attention team to vendor lock owners (#18840)
  _Files: `.github/CODEOWNERS`_
- **2026-09-08** [`8533131fac`](https://github.com/NVIDIA/TensorRT-LLM/commit/8533131fac) [#17969](https://github.com/NVIDIA/TensorRT-LLM/pull/17969)
  [TRTLLM-14558][chore] Add the forwarding modules for the retired Attention paths (#17969)
  _Files: `tensorrt_llm/_torch/attention/backends/__init__.py`, `tensorrt_llm/_torch/attention_backend/__init__.py`, `tensorrt_llm/_torch/modules/attention.py`, `tests/unittest/_torch/attention/test_backends_importable.py`_
- **2026-09-07** [`0bbca8333f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bbca8333f) [#18093](https://github.com/NVIDIA/TensorRT-LLM/pull/18093)
  [https://nvbugs/6621358][fix] Enable one-model draft KV reuse in cache manager V2 (#18093)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+36 more__
- **2026-09-07** [`e473b03a6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e473b03a6c) [#18587](https://github.com/NVIDIA/TensorRT-LLM/pull/18587)
  [None][docs] Add KV cache compression documentation and examples (#18587)
  _Files: `docs/source/developer-guide/kv-cache-cold-page-codec.md`, `docs/source/developer-guide/kv-cache-compression-development.md`, `docs/source/features/kv-cache-compression.md`, `docs/source/features/kvcache.md` _+8 more__

## Executor / Runtime  (28 commits)

- **2026-09-14** [`12c5de87ff`](https://github.com/NVIDIA/TensorRT-LLM/commit/12c5de87ff) [#19005](https://github.com/NVIDIA/TensorRT-LLM/pull/19005)
  [https://nvbugs/6727262][test] Bound batch size in default-backend smoke tests (#19005)
  _Files: `tests/integration/defs/llmapi/_run_llmapi_llm.py`, `tests/integration/defs/llmapi/test_llm_api_qa.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`9cd401aa2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/9cd401aa2f) [#18886](https://github.com/NVIDIA/TensorRT-LLM/pull/18886)
  [None][fix] Stop the generation worker from re-expanding media placeholders under disagg (#18886)
  _Files: `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/chat_utils.py`, `tensorrt_llm/serve/openai_server.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+1 more__
- **2026-09-14** [`a6a75a1198`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6a75a1198) [#18856](https://github.com/NVIDIA/TensorRT-LLM/pull/18856)
  [#13949][test] Cover /v1/responses in per-request perf metrics tests (#18856)
  _Files: `tests/unittest/llmapi/apps/_test_openai_perf_metrics.py`_
- **2026-09-14** [`d9280633c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9280633c3) [#18865](https://github.com/NVIDIA/TensorRT-LLM/pull/18865)
  [#17917][fix] Warn when a tool parser detects markup but extracts no tool calls (#18865)
  _Files: `tensorrt_llm/serve/postprocess_handlers.py`, `tensorrt_llm/serve/responses_utils.py`, `tensorrt_llm/serve/tool_parser/base_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-09-14** [`566bfa150a`](https://github.com/NVIDIA/TensorRT-LLM/commit/566bfa150a) [#18399](https://github.com/NVIDIA/TensorRT-LLM/pull/18399)
  [None][feat] Support num_postprocess_workers > 0 under the Ray Orchestration (#18399)
  _Files: `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/ray/executor.py`, `tensorrt_llm/executor/ray/gpu_worker.py`, `tensorrt_llm/executor/result.py` _+4 more__
- **2026-09-12** [`8fff903d8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fff903d8a) [#18990](https://github.com/NVIDIA/TensorRT-LLM/pull/18990)
  [None][feat] perf-sanity: upload per-request disagg lifecycle spans to OpenSearch (#18990)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/README.md`, `jenkins/scripts/perf/local/README.md`, `jenkins/scripts/perf/local/configs/example.conf` _+18 more__
- **2026-09-12** [`64707941c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/64707941c0) [#18807](https://github.com/NVIDIA/TensorRT-LLM/pull/18807)
  [None][fix] Shut down resources before GC assertions (#18807)
  _Files: `tests/unittest/gc_utils.py`, `tests/unittest/llmapi/test_gc_utils.py`_
- **2026-09-11** [`84da514b15`](https://github.com/NVIDIA/TensorRT-LLM/commit/84da514b15) [#18737](https://github.com/NVIDIA/TensorRT-LLM/pull/18737)
  [TRTLLM-15448][refactor] Add checkpoint catalog and shadow load planning (#18737)
  _Files: `tensorrt_llm/_torch/models/checkpoints/base_checkpoint_loader.py`, `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/checkpoint_catalog.py`, `tensorrt_llm/_torch/models/checkpoints/hf/checkpoint_catalog.py` _+7 more__
- **2026-09-11** [`273c342ade`](https://github.com/NVIDIA/TensorRT-LLM/commit/273c342ade) [#18541](https://github.com/NVIDIA/TensorRT-LLM/pull/18541)
  [None][perf] Speed up burst KVCM2 resize for very long sequences (#18541)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batchedPageCopy.cu`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/batchedPageCopy.h` _+35 more__
- **2026-09-11** [`8697c5dc61`](https://github.com/NVIDIA/TensorRT-LLM/commit/8697c5dc61) [#18957](https://github.com/NVIDIA/TensorRT-LLM/pull/18957)
  [https://nvbugs/6739081][fix] Preserve per-layer KV page addressing for mixed head sizes (#18957)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_v2_extra_buffers.py`, `tests/unittest/_torch/executor/test_per_layer_head_dim.py`_
- **2026-09-10** [`7bbf99e5a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/7bbf99e5a7) [#18994](https://github.com/NVIDIA/TensorRT-LLM/pull/18994)
  [TRTLLM-16179][test] Port detokenization stop-word tests to Qwen3-0.6B (#18994)
  _Files: `tests/unittest/llmapi/test_llm.py`_
- **2026-09-10** [`d740e1957f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d740e1957f) [#18608](https://github.com/NVIDIA/TensorRT-LLM/pull/18608)
  [TRTLLM-15448][perf] Add checkpoint I/O experiment and startup telemetry (#18608)
  _Files: `docs/source/features/checkpoint-loading.md`, `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+8 more__
- **2026-09-10** [`5fe6523ebe`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fe6523ebe) [#18381](https://github.com/NVIDIA/TensorRT-LLM/pull/18381)
  [None][feat] Support image input in the Triton llmapi backend (#18381)
  _Files: `tensorrt_llm/inputs/__init__.py`, `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/chat_utils.py`, `triton_backend/all_models/llmapi/tensorrt_llm/1/model.py` _+3 more__
- **2026-09-10** [`430f24fdb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/430f24fdb4) [#18701](https://github.com/NVIDIA/TensorRT-LLM/pull/18701)
  [None][perf] Apply NUMA-aware CPU affinity beyond the main thread (#18701)
  _Files: `docs/source/deployment-guide/configuring-cpu-affinity.md`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/llmapi/utils.py`, `tests/unittest/llmapi/test_utils.py`_
- **2026-09-10** [`d094c55e8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d094c55e8e) [#18195](https://github.com/NVIDIA/TensorRT-LLM/pull/18195)
  [TRTLLM-15520][feat] Admit one context per uncached prefix instead of letting every duplicate recompute it (#18195)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_dual_pool_kv_cache.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_v2_first_new_block_probe.py` _+2 more__
- **2026-09-10** [`05293ce32e`](https://github.com/NVIDIA/TensorRT-LLM/commit/05293ce32e) [#17023](https://github.com/NVIDIA/TensorRT-LLM/pull/17023)
  [TRTLLM-15331][feat] Improve KV event publish performance via StreamingEvent (#17023)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_events.py` _+7 more__
- **2026-09-09** [`16872f42e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/16872f42e4) [#18267](https://github.com/NVIDIA/TensorRT-LLM/pull/18267)
  [None][chore] Clean up disagg transfer idle progress (#18267)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-09** [`5da0285cd6`](https://github.com/NVIDIA/TensorRT-LLM/commit/5da0285cd6) [#18768](https://github.com/NVIDIA/TensorRT-LLM/pull/18768)
  [None][fix] Make llm_args use the canonical custom-tokenizer alias table (#18768)
  _Files: `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_tokenizer_aliases.py`_
- **2026-09-09** [`94330e9d5c`](https://github.com/NVIDIA/TensorRT-LLM/commit/94330e9d5c) [#18784](https://github.com/NVIDIA/TensorRT-LLM/pull/18784)
  [TRTLLM-15757][refactor] Land the ModelRunner contract with the no-KVCache families (#18784)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`, `tensorrt_llm/_torch/models/modeling_llama.py`, `tensorrt_llm/_torch/models/modeling_llava_next.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+20 more__
- **2026-09-09** [`07a58bd9ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/07a58bd9ec) [#18804](https://github.com/NVIDIA/TensorRT-LLM/pull/18804)
  [TRTLLM-16163][feat] Enable Nemotron 3.5 Super VL serving paths (#18804)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/llmapi/reasoning_parser.py`, `tensorrt_llm/serve/tool_parser/tool_parser_factory.py`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nano_v2_vl.py` _+2 more__
- **2026-09-09** [`eca1022782`](https://github.com/NVIDIA/TensorRT-LLM/commit/eca1022782) [#18896](https://github.com/NVIDIA/TensorRT-LLM/pull/18896)
  [https://nvbugs/6625851][fix] Fail guided-decoding requests reaching a dead-end grammar state (#18896)
  _Files: `tensorrt_llm/_torch/pyexecutor/guided_decoder.py`, `tests/unittest/_torch/misc/test_guided_decoder_bitmask.py`_
- **2026-09-09** [`7db313ce7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7db313ce7a) [#18894](https://github.com/NVIDIA/TensorRT-LLM/pull/18894)
  [None][fix] match the sampler's scratch slot row in the fused finish-reason guard (#18894)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/finish_reasons.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/unittest/_torch/sampler/test_finish_reasons_fused.py`_
- **2026-09-08** [`cbe8bec77c`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbe8bec77c) [#17029](https://github.com/NVIDIA/TensorRT-LLM/pull/17029)
  [MX-299][feat] Delegate MX loading to ModelExpress strategies (#17029)
  _Files: `docs/source/features/model-express.md`, `jenkins/L0_Test.groovy`, `setup.py`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py` _+12 more__
- **2026-09-08** [`35f4e60ef6`](https://github.com/NVIDIA/TensorRT-LLM/commit/35f4e60ef6) [#18540](https://github.com/NVIDIA/TensorRT-LLM/pull/18540)
  [None][chore] Cleanup unused C++ algorithms (#18540)
  _Files: `.github/CODEOWNERS`, `cpp/include/tensorrt_llm/batch_manager/allocateKvCache.h`, `cpp/include/tensorrt_llm/batch_manager/assignReqSeqSlots.h`, `cpp/include/tensorrt_llm/batch_manager/pauseRequests.h` _+14 more__
- **2026-09-07** [`a67ede16f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/a67ede16f6) [#18030](https://github.com/NVIDIA/TensorRT-LLM/pull/18030)
  [https://nvbugs/6642522][fix] Prevent orphaned VisualGen workers (#18030)
  _Files: `cpp/tensorrt_llm/nanobind/CMakeLists.txt`, `cpp/tensorrt_llm/nanobind/bindings.cpp`, `cpp/tensorrt_llm/nanobind/visual_gen/coordinatorWatchdog.cpp`, `cpp/tensorrt_llm/nanobind/visual_gen/coordinatorWatchdog.h` _+16 more__
- **2026-09-07** [`41e6c8fc74`](https://github.com/NVIDIA/TensorRT-LLM/commit/41e6c8fc74) [#18724](https://github.com/NVIDIA/TensorRT-LLM/pull/18724)
  [None][fix] Preserve configured Mamba snapshot placement (#18724)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/mamba_cache_manager.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/executor/kv_cache/test_mamba_cache_manager.py`_
- **2026-09-07** [`65b244dcd3`](https://github.com/NVIDIA/TensorRT-LLM/commit/65b244dcd3) [#18749](https://github.com/NVIDIA/TensorRT-LLM/pull/18749)
  [None][feat] Add opt-in GPU keepalive to the benchmark fill gate (#18749)
  _Files: `docs/source/features/disagg-serving.md`, `tensorrt_llm/_torch/pyexecutor/gpu_keepalive.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_gpu_keepalive.py` _+1 more__
- **2026-09-07** [`288ad73745`](https://github.com/NVIDIA/TensorRT-LLM/commit/288ad73745) [#18135](https://github.com/NVIDIA/TensorRT-LLM/pull/18135)
  [https://nvbugs/6428069][fix] Drain only the due PP relay send before forward and unwaive the disagg PP tests (#18135)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_py_executor.py`_

## MoE  (26 commits)

- **2026-09-14** [`4b768e3313`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b768e3313) [#18766](https://github.com/NVIDIA/TensorRT-LLM/pull/18766)
  [None][infra] Skip pre-merge perf gating when main has already regressed and refactor the pre-merge perf-sanity list (#18766)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/README_perf_regression_system.md`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/perf_regression_utils.py` _+6 more__
- **2026-09-14** [`43cd45f9f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/43cd45f9f9) [#18126](https://github.com/NVIDIA/TensorRT-LLM/pull/18126)
  [TRTLLMINF-397][infra] Update dependencies to NGC PyTorch 26.08 (#18126)
  _Files: `ATTRIBUTIONS-Python.md`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcKernels.cu`, `cpp/tensorrt_llm/runtime/moeLoadBalancer/hostAccessibleDeviceAllocator.cpp` _+29 more__
- **2026-09-13** [`a3848cc0d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3848cc0d8) [#19088](https://github.com/NVIDIA/TensorRT-LLM/pull/19088)
  [None][test] Supply auxiliary streams in Kimi K3 NVFP4 regression (#19088)
  _Files: `tests/unittest/_torch/moe/test_kimi_k3_situ_moe.py`_
- **2026-09-12** [`e6ca0c7bc2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6ca0c7bc2) [#18972](https://github.com/NVIDIA/TensorRT-LLM/pull/18972)
  [None][fix] Stabilize MoE LoRA CUDA graph scratch (#18972)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_grouped_gemm.h`, `cpp/tensorrt_llm/thop/moeOp.cpp`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/peft/lora/cuda_graph_lora_manager.py` _+4 more__
- **2026-09-12** [`c1aa940196`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1aa940196) [#19092](https://github.com/NVIDIA/TensorRT-LLM/pull/19092)
  [None][ci] Waive test_kimi_k3_trtllm_accepts_nvfp4_routed_experts (#19092)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`8a9c66ce08`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a9c66ce08) [#19050](https://github.com/NVIDIA/TensorRT-LLM/pull/19050)
  [None][doc] Reduce Sphinx build warnings from 1229 to 258 (#19050)
  _Files: `docs/source/_includes/note_sections.rst`, `docs/source/blogs/Best_perf_practice_on_DeepSeek-R1_in_TensorRT-LLM.md`, `docs/source/blogs/Falcon180B-H200.md`, `docs/source/blogs/H200launch.md` _+57 more__
- **2026-09-11** [`6dad5c91ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dad5c91ef) [#18870](https://github.com/NVIDIA/TensorRT-LLM/pull/18870)
  [https://nvbugs/6537568][fix] Support MXFP4/NVFP4 MoE TP shard padding (#18870)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/unittest/_torch/moe/test_kimi_k3_situ_moe.py`, `tests/unittest/_torch/moe/test_moe_backend.py`_
- **2026-09-10** [`5a53818055`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a53818055) [#18644](https://github.com/NVIDIA/TensorRT-LLM/pull/18644)
  [None][fix] Harden VMM-backed DWDP lifecycle (#18644)
  _Files: `tensorrt_llm/_torch/modules/dwdp/__init__.py`, `tensorrt_llm/_torch/modules/dwdp/setup.py`, `tensorrt_llm/_torch/modules/dwdp/weight_manager.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md` _+7 more__
- **2026-09-10** [`3668a5ac53`](https://github.com/NVIDIA/TensorRT-LLM/commit/3668a5ac53) [#18770](https://github.com/NVIDIA/TensorRT-LLM/pull/18770)
  [None][fix] Re-resolve the MoE op provider once the per-layer quant config is known (#18770)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_trtllm_gen.py`, `tests/unittest/_torch/moe/test_moe_op_provider_resync.py`_
- **2026-09-10** [`b509ae936c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b509ae936c) [#18624](https://github.com/NVIDIA/TensorRT-LLM/pull/18624)
  [https://nvbugs/6676312][fix] Restore DSA CUDA TopK workspace lifecycle (#18624)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/modules/top_k.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py` _+1 more__
- **2026-09-10** [`9ac90888b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ac90888b9) [#18992](https://github.com/NVIDIA/TensorRT-LLM/pull/18992)
  [https://nvbugs/6709495][doc] Fix dead links flagged by test_http_url_validity (#18992)
  _Files: `docs/source/blogs/tech_blog/blog01_Pushing_Latency_Boundaries_Optimizing_DeepSeek-R1_Performance_on_NVIDIA_B200_GPUs.md`, `docs/source/blogs/tech_blog/blog04_Scaling_Expert_Parallelism_in_TensorRT-LLM.md`, `docs/source/blogs/tech_blog/blog05_Disaggregated_Serving_in_TensorRT-LLM.md`, `docs/source/blogs/tech_blog/blog08_Scaling_Expert_Parallelism_in_TensorRT-LLM_part2.md` _+15 more__
- **2026-09-10** [`173e3da059`](https://github.com/NVIDIA/TensorRT-LLM/commit/173e3da059) [#18808](https://github.com/NVIDIA/TensorRT-LLM/pull/18808)
  [None][chore] Update cutedsl to 4.8.0 dev (#18808)
  _Files: `3rdparty/vendor_sources.lock.yaml`, `ATTRIBUTIONS-Python.md`, `constraints.txt`, `docker/Dockerfile.multi` _+5 more__
- **2026-09-10** [`140e1a208a`](https://github.com/NVIDIA/TensorRT-LLM/commit/140e1a208a) [#18885](https://github.com/NVIDIA/TensorRT-LLM/pull/18885)
  [None][fix] Resolve vocab_size through config within v2_KVCM instead of propagating depending on model family (#18885)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_v2_vocab_size.py`_
- **2026-09-09** [`9504a60060`](https://github.com/NVIDIA/TensorRT-LLM/commit/9504a60060) [#18182](https://github.com/NVIDIA/TensorRT-LLM/pull/18182)
  [https://nvbugs/6581063][fix] Release MegaMoE symm buffers on executor teardown (#18182)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_deepgemm.py`, `tensorrt_llm/executor/worker.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`eabb0c8a15`](https://github.com/NVIDIA/TensorRT-LLM/commit/eabb0c8a15) [#18728](https://github.com/NVIDIA/TensorRT-LLM/pull/18728)
  [None][fix] share Kimi auxiliary streams (#18728)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`, `tests/unittest/_torch/modeling/test_kimi_linear_modeling.py`, `tests/unittest/_torch/moe/test_kimi_k3_mlp.py`_
- **2026-09-09** [`5601be60b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5601be60b7) [#18527](https://github.com/NVIDIA/TensorRT-LLM/pull/18527)
  [https://nvbugs/6683837][fix] Thread `lora_params` to `self.experts()`; cache a per-(layer,module) rank… (#18527)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_moe.py`, `tensorrt_llm/_torch/peft/lora/cuda_graph_lora_params.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_moe_lora.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-09-09** [`3992241b73`](https://github.com/NVIDIA/TensorRT-LLM/commit/3992241b73) [#18709](https://github.com/NVIDIA/TensorRT-LLM/pull/18709)
  [None][fix] Kimi K3: admit every trtllm-gen SiTu quant format, not just MXFP4 (#18709)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_trtllm_gen.py`, `tests/unittest/_torch/moe/test_kimi_k3_situ_moe.py`_
- **2026-09-09** [`688bcfbb40`](https://github.com/NVIDIA/TensorRT-LLM/commit/688bcfbb40) [#18702](https://github.com/NVIDIA/TensorRT-LLM/pull/18702)
  [None][feat] Self-sampling GVR V2 prefill indexer top-K (#18702)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py` _+8 more__
- **2026-09-09** [`dfff67a09d`](https://github.com/NVIDIA/TensorRT-LLM/commit/dfff67a09d) [#18772](https://github.com/NVIDIA/TensorRT-LLM/pull/18772)
  [None][fix] MoE: keep separate NVFP4 gate/up global scales where supported (#18772)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/quantization.py`, `tests/unittest/_torch/moe/test_moe_nvfp4_gate_up_scale2.py`_
- **2026-09-08** [`7810d5f522`](https://github.com/NVIDIA/TensorRT-LLM/commit/7810d5f522) [#18799](https://github.com/NVIDIA/TensorRT-LLM/pull/18799)
  [https://nvbugs/6667807][fix] Support more than 128 EP ranks in MoE two-sided prepare cumsum (#18799)
  _Files: `cpp/tensorrt_llm/kernels/moePrepareKernels.cu`_
- **2026-09-08** [`3933f62170`](https://github.com/NVIDIA/TensorRT-LLM/commit/3933f62170) [#18714](https://github.com/NVIDIA/TensorRT-LLM/pull/18714)
  [None][perf] speed up the block-scale MoE, GDN and sampler decode paths for Qwen3.8-flash-next (#18714)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomKernels.cuh`, `cpp/tests/unit_tests/kernels/CMakeLists.txt` _+10 more__
- **2026-09-08** [`ba32790910`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba32790910) [#18748](https://github.com/NVIDIA/TensorRT-LLM/pull/18748)
  [TRTLLM-14963][TRTLLM-14966][refactor] Give the DeepGEMM MoE implementations canonical identities and add an impl_id pin (#18748)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/create_moe.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_deepgemm.py`, `tensorrt_llm/_torch/moe/fused_moe/impl_identity.py` _+7 more__
- **2026-09-08** [`392ce14cae`](https://github.com/NVIDIA/TensorRT-LLM/commit/392ce14cae) [#18832](https://github.com/NVIDIA/TensorRT-LLM/pull/18832)
  [https://nvbugs/6644226][fix] page out MoE safetensors during weight load regardless of EPLB (#18832)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`85d9871b35`](https://github.com/NVIDIA/TensorRT-LLM/commit/85d9871b35) [#18446](https://github.com/NVIDIA/TensorRT-LLM/pull/18446)
  [None][feat] Two-level GVR decode top-K dispatch; remove the CUDA heuristic and temporal-only prior state (#18446)
  _Files: `cpp/tensorrt_llm/kernels/IndexerTopK.h`, `cpp/tensorrt_llm/kernels/heuristicTopKDecode.cu`, `cpp/tensorrt_llm/kernels/heuristicTopKDecode.h`, `cpp/tensorrt_llm/kernels/heuristic_topk.cuh` _+14 more__
- **2026-09-07** [`058fade908`](https://github.com/NVIDIA/TensorRT-LLM/commit/058fade908) [#18785](https://github.com/NVIDIA/TensorRT-LLM/pull/18785)
  [None][fix] bench_moe: prune MNNVL comm methods that cannot span nodes (#18785)
  _Files: `tests/microbenchmarks/bench_moe/search.py`_
- **2026-09-07** [`e0ee12a55c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0ee12a55c) [#18683](https://github.com/NVIDIA/TensorRT-LLM/pull/18683)
  [None][fix] Self-sampling top-k host: physical row-width envelope and exact-row warmup population (#18683)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_

## Other  (19 commits)

- **2026-09-11** [`0528172f47`](https://github.com/NVIDIA/TensorRT-LLM/commit/0528172f47)
  [None][chore] promote PrimTS source from TRT-LLM #18996
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-09-11** [`3bd8e8b129`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bd8e8b129) [#18037](https://github.com/NVIDIA/TensorRT-LLM/pull/18037)
  [https://nvbugs/6608795][fix] Fall back when UserBuffers multicast mapping fails (#18037)
  _Files: `cpp/tensorrt_llm/kernels/userbuffers/userbuffers-host.cpp`_
- **2026-09-11** [`795805fffc`](https://github.com/NVIDIA/TensorRT-LLM/commit/795805fffc) [#17730](https://github.com/NVIDIA/TensorRT-LLM/pull/17730)
  [None][fix] catch KeyError when parsing --server_role into ServerRole (#17730)
  _Files: `tensorrt_llm/commands/serve.py`_
- **2026-09-10** [`09503b92ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/09503b92ef) [#18703](https://github.com/NVIDIA/TensorRT-LLM/pull/18703)
  [None][fix] Raise SetupError instead of NameError when the precompiled wheel is missing (#18703)
  _Files: `setup.py`_
- **2026-09-10** [`0ee0893ee5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ee0893ee5)
  [None][chore] promote PrimTS source from TRT-LLM #18808
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-09-09** [`36a4fd4bab`](https://github.com/NVIDIA/TensorRT-LLM/commit/36a4fd4bab) [#18884](https://github.com/NVIDIA/TensorRT-LLM/pull/18884)
  [None][chore] Clean up unused code in C++ test files (#18884)
  _Files: `tests/integration/defs/cpp/conftest.py`, `tests/integration/defs/cpp/cpp_common.py`, `tests/integration/defs/cpp/test_multi_gpu.py`_
- **2026-09-09** [`96a25c48b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/96a25c48b2) [#18942](https://github.com/NVIDIA/TensorRT-LLM/pull/18942)
  [None][test] update qa test list (#18942)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-09-09** [`2ece8d97d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ece8d97d2) [#18930](https://github.com/NVIDIA/TensorRT-LLM/pull/18930)
  [https://nvbugs/6737123][fix] Preserve PATH in vendor source offline checks (#18930)
  _Files: `tests/unittest/others/test_vendor_sources.py`_
- **2026-09-08** [`f3a2757d38`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3a2757d38) [#18857](https://github.com/NVIDIA/TensorRT-LLM/pull/18857)
  [None][test] update Coderabbit review (#18857)
  _Files: `.coderabbit.yaml`_
- **2026-09-08** [`22f4305bbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/22f4305bbe) [#18574](https://github.com/NVIDIA/TensorRT-LLM/pull/18574)
  [None][fix] Let the kernel ledger record comm kernels and partial ncu captures without hiding the gaps (#18574)
  _Files: `agent-flow/agent_flow/workflows/perf_optimize/kernel_ledger.py`, `agent-flow/agent_flow/workflows/perf_optimize/prompts/_common.py`, `agent-flow/tests/workflows/perf_optimize/test_kernel_ledger.py`, `agent-flow/tests/workflows/perf_optimize/test_prompts.py`_
- **2026-09-08** [`383e50ecda`](https://github.com/NVIDIA/TensorRT-LLM/commit/383e50ecda) [#15952](https://github.com/NVIDIA/TensorRT-LLM/pull/15952)
  [None][chore] Reuse datas in datasets to build test prompts with number larger than origin dataset (#15952)
  _Files: `tensorrt_llm/serve/scripts/benchmark_dataset.py`_
- **2026-09-07** [`c426264bc4`](https://github.com/NVIDIA/TensorRT-LLM/commit/c426264bc4) [#18790](https://github.com/NVIDIA/TensorRT-LLM/pull/18790)
  [None][feat] Add --trtllm-custom-output-len to override OSL for the trtllm_custom dataset (#18790)
  _Files: `tensorrt_llm/serve/scripts/benchmark_dataset.py`, `tensorrt_llm/serve/scripts/benchmark_serving.py`_
- **2026-09-07** [`99e819538b`](https://github.com/NVIDIA/TensorRT-LLM/commit/99e819538b) [#18773](https://github.com/NVIDIA/TensorRT-LLM/pull/18773)
  [None][fix] Install with the venv interpreter, not sys.executable (#18773)
  _Files: `scripts/build_wheel.py`, `tests/unittest/others/test_build_wheel_install_interpreter.py`_
- **2026-09-07** [`bbf9b65090`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbf9b65090) [#18833](https://github.com/NVIDIA/TensorRT-LLM/pull/18833)
  [None][chore] point PrimTS vendor source to dev branch (#18833)
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-09-07** [`cd484cdee5`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd484cdee5) [#18718](https://github.com/NVIDIA/TensorRT-LLM/pull/18718)
  [None][test] check relative links in documentation (#18718)
  _Files: `tests/integration/defs/test_doc.py`, `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-09-07** [`6202f0302d`](https://github.com/NVIDIA/TensorRT-LLM/commit/6202f0302d) [#18648](https://github.com/NVIDIA/TensorRT-LLM/pull/18648)
  [None][test] Remove H20 in QA perf test (#18648)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-07** [`9154df1ff4`](https://github.com/NVIDIA/TensorRT-LLM/commit/9154df1ff4) [#18604](https://github.com/NVIDIA/TensorRT-LLM/pull/18604)
  [None][test] Fix layerwise replay bugs (#18604)
  _Files: `tensorrt_llm/tools/layer_wise_benchmarks/runner.py`_
- **2026-09-07** [`e8654268e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8654268e9) [#18751](https://github.com/NVIDIA/TensorRT-LLM/pull/18751)
  [None][feat] lm_eval: let the CLI override a task's stop strings (#18751)
  _Files: `tensorrt_llm/evaluate/lm_eval.py`, `tests/unittest/others/test_lm_eval.py`_
- **2026-09-07** [`f033c0713e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f033c0713e) [#18586](https://github.com/NVIDIA/TensorRT-LLM/pull/18586)
  [None][test] Enable strict checks for declarative extra import path (#18586)
  _Files: `tests/test_common/magic_import_hooks.py`, `tests/unittest/others/test_magic_import.py`_

## Disaggregation / KV  (16 commits)

- **2026-09-14** [`a1fe8aa55b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1fe8aa55b) [#19149](https://github.com/NVIDIA/TensorRT-LLM/pull/19149)
  [https://nvbugs/6758853][test] Unwaive KV cache V1/V2 parity tests (#19149)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`c776328e08`](https://github.com/NVIDIA/TensorRT-LLM/commit/c776328e08) [#19132](https://github.com/NVIDIA/TensorRT-LLM/pull/19132)
  [https://nvbugs/6758853][fix] Prewarm prefixes for KV cache parity comparisons (#19132)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`_
- **2026-09-12** [`14863f0c23`](https://github.com/NVIDIA/TensorRT-LLM/commit/14863f0c23) [#18941](https://github.com/NVIDIA/TensorRT-LLM/pull/18941)
  [TRTLLM-16203][test] Restore disaggregated-serving coverage on Hopper (#18941)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml`, `tests/integration/test_lists/test-db/l0_dgx_h200.yml`_
- **2026-09-12** [`e3c1b9e8ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3c1b9e8ce) [#18684](https://github.com/NVIDIA/TensorRT-LLM/pull/18684)
  [TRTLLM-16022][feat] Add sub-agent conversation affinity for disaggregated serving (#18684)
  _Files: `docs/source/features/disagg-serving.md`, `docs/source/features/subagent-routing.md`, `docs/source/index.rst`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py` _+13 more__
- **2026-09-11** [`80d9e15328`](https://github.com/NVIDIA/TensorRT-LLM/commit/80d9e15328) [#19031](https://github.com/NVIDIA/TensorRT-LLM/pull/19031)
  [https://nvbugs/6756996][fix] use llama_model_root fixture evaluation (#19031)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`8bbaf66bd5`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bbaf66bd5) [#17992](https://github.com/NVIDIA/TensorRT-LLM/pull/17992)
  [None][feat] OpenEngine gRPC: wire Generate RPC to the engine with disaggregated serving (#17992)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/rules/README.md`, `tensorrt_llm/commands/serve.py` _+19 more__
- **2026-09-11** [`d26f734d63`](https://github.com/NVIDIA/TensorRT-LLM/commit/d26f734d63) [#13872](https://github.com/NVIDIA/TensorRT-LLM/pull/13872)
  [TRTLLM-12670][feat] add /start_profile and /stop_profile endpoints to trtllm… (#13872)
  _Files: `docs/source/commands/trtllm-serve/run-benchmark-with-trtllm-serve.md`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `tensorrt_llm/_torch/pyexecutor/executor_request_queue.py`, `tensorrt_llm/_torch/pyexecutor/profiling.py` _+23 more__
- **2026-09-11** [`c1ab38e14a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1ab38e14a) [#18809](https://github.com/NVIDIA/TensorRT-LLM/pull/18809)
  [None][test] clean Llama-3.1-8B accuracy test coverage (#18809)
  _Files: `tests/README.md`, `tests/integration/defs/accuracy/README.md`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml` _+25 more__
- **2026-09-11** [`153cab509c`](https://github.com/NVIDIA/TensorRT-LLM/commit/153cab509c) [#19007](https://github.com/NVIDIA/TensorRT-LLM/pull/19007)
  [https://nvbugs/6731971][doc] Fix broken relative paths flagged by test_relative_path_validity (#19007)
  _Files: `.claude/skills/trtllm-code-contribution/SKILL.md`, `cpp/tests/README.md`, `docs/source/legacy/advanced/disaggregated-service.md`, `docs/source/legacy/architecture/model-weights-loader.md` _+11 more__
- **2026-09-09** [`f3b867dab4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3b867dab4) [#18580](https://github.com/NVIDIA/TensorRT-LLM/pull/18580)
  [None][test] retire Gemma 3 checkpoint tests (#18580)
  _Files: `examples/auto_deploy/model_registry/models.yaml`, `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/json_mode_eval.yaml` _+22 more__
- **2026-09-08** [`3718d3f4fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/3718d3f4fa) [#18150](https://github.com/NVIDIA/TensorRT-LLM/pull/18150)
  [None][perf] Bypass static transfer admission for async Python PP1 (#18150)
  _Files: `tensorrt_llm/_torch/disaggregation/kv_cache_transceiver.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/disaggregation/test_disagg_inflight_cancel_gate.py` _+1 more__
- **2026-09-08** [`3fed8e7103`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fed8e7103) [#18828](https://github.com/NVIDIA/TensorRT-LLM/pull/18828)
  [None][test] align perf disagg cases to the PYTHON transceiver runtime (#18828)
  _Files: `tests/scripts/perf/disaggregated/gb200_glm-5-fp4_8k1k_con1024_ctx1_dep4_gen1_dep8_eplb256_mtp1_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_glm-5-fp4_8k1k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_glm-5-fp4_8k1k_con512_ctx1_dep4_gen1_dep32_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_qwen3-235b-fp4_8k1k_con1024_ctx1_tp1_gen1_dep8_eplb0_mtp0_ccb-NIXL.yaml` _+7 more__
- **2026-09-08** [`40bee2a808`](https://github.com/NVIDIA/TensorRT-LLM/commit/40bee2a808) [#18404](https://github.com/NVIDIA/TensorRT-LLM/pull/18404)
  [None][test] add a basic disaggregated multi-node tier (#18404)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode_basic.txt`_
- **2026-09-07** [`ebf619a22a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ebf619a22a) [#18538](https://github.com/NVIDIA/TensorRT-LLM/pull/18538)
  [None][chore] Cleanup kv cache manager (#18538)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`_
- **2026-09-07** [`4b9f3ae3de`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b9f3ae3de) [#18294](https://github.com/NVIDIA/TensorRT-LLM/pull/18294)
  [None][feat] support Kimi K3 KDA replay with KV cache manager V2 (#18294)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_kda_mtp_ops.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_k3_mamba_metadata.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+5 more__
- **2026-09-07** [`564c73dd4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/564c73dd4a) [#18649](https://github.com/NVIDIA/TensorRT-LLM/pull/18649)
  [https://nvbugs/6594241][fix] increase timeout for test_disaggregated_gpt_oss_120b_harmony (#18649)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_

## Quantization  (12 commits)

- **2026-09-14** [`6e1cc953c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e1cc953c0) [#19134](https://github.com/NVIDIA/TensorRT-LLM/pull/19134)
  [https://nvbugs/6621358][fix] Isolate DeepSeek NVFP4 LongBench MPI session (#19134)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-09-13** [`5154ec9b42`](https://github.com/NVIDIA/TensorRT-LLM/commit/5154ec9b42)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+4 more__
- **2026-09-12** [`61154e9f3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/61154e9f3f) [#18733](https://github.com/NVIDIA/TensorRT-LLM/pull/18733)
  [TRTLLM-16194][feat] Add MiniMax H3 support (#18733)
  _Files: `LICENSE`, `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md` _+24 more__
- **2026-09-12** [`01f80868c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/01f80868c2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+4 more__
- **2026-09-11** [`09c7f9b72d`](https://github.com/NVIDIA/TensorRT-LLM/commit/09c7f9b72d) [#18875](https://github.com/NVIDIA/TensorRT-LLM/pull/18875)
  [None][test] Add DeepSeek V4 Pro-Base and NVFP4 DSpark B300 perf tests (#18875)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-11** [`ca2305b6b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca2305b6b6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-09-10** [`a4b6741b7c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4b6741b7c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+8 more__
- **2026-09-10** [`31504068f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/31504068f2) [#18979](https://github.com/NVIDIA/TensorRT-LLM/pull/18979)
  [https://nvbugs/5836830][test] Remove DeepSeek-R1 W4AFP8 8-GPU quickstart test from QA list (#18979)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`d8d7d383b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d8d7d383b7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-09-08** [`6c42edd0d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c42edd0d6) [#17262](https://github.com/NVIDIA/TensorRT-LLM/pull/17262)
  [TRTLLM-13767][feat] integrate FP4 Conv3d into parallel Wan VAE (#17262)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/conv/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/conv/dense_blockscaled_implicit_gemm_fprop.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/conv/dense_gemm_persistent_dynamic.py` _+22 more__
- **2026-09-07** [`6e8fe90078`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e8fe90078)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+2 more__
- **2026-09-07** [`774cfbbfcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/774cfbbfcf) [#18260](https://github.com/NVIDIA/TensorRT-LLM/pull/18260)
  [None][fix] validate the layer-wise replay request against the calibration before it runs (#18260)
  _Files: `examples/layer_wise_benchmarks/run.py`, `tensorrt_llm/tools/layer_wise_benchmarks/calibrator.py`, `tests/unittest/tools/test_layer_wise_benchmarks_calibrator.py`_

## Docs / Examples  (10 commits)

- **2026-09-14** [`55e29043bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e29043bd) [#19137](https://github.com/NVIDIA/TensorRT-LLM/pull/19137)
  [None][chore] Bump version to 1.3.0rc27 (#19137)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-09-11** [`4476ee3eac`](https://github.com/NVIDIA/TensorRT-LLM/commit/4476ee3eac) [#19023](https://github.com/NVIDIA/TensorRT-LLM/pull/19023)
  [None][doc] Group VisualGen feature guides under one navigation entry (#19023)
  _Files: `docs/source/conf.py`, `docs/source/features/visual-generation.md`, `docs/source/index.rst`_
- **2026-09-11** [`a43b672bf1`](https://github.com/NVIDIA/TensorRT-LLM/commit/a43b672bf1) [#19009](https://github.com/NVIDIA/TensorRT-LLM/pull/19009)
  [https://nvbugs/6676352][doc] Fix two copy-paste-broken doc snippets (#19009)
  _Files: `docs/source/deployment-guide/deployment-guide-for-glm-5-on-trtllm.md`, `docs/source/legacy/advanced/kv-cache-reuse.md`_
- **2026-09-09** [`fcd4636560`](https://github.com/NVIDIA/TensorRT-LLM/commit/fcd4636560) [#18213](https://github.com/NVIDIA/TensorRT-LLM/pull/18213)
  [None][doc] Document the three generation-side time breakdown segments (#18213)
  _Files: `tensorrt_llm/serve/scripts/time_breakdown/README.md`_
- **2026-09-09** [`72104b5fe9`](https://github.com/NVIDIA/TensorRT-LLM/commit/72104b5fe9) [#18752](https://github.com/NVIDIA/TensorRT-LLM/pull/18752)
  [None][feat] Add a link mode to the precompiled editable-install path (#18752)
  _Files: `docs/source/installation/build-from-source.md`, `setup.py`, `tests/unittest/others/test_precompiled_link_mode.py`_
- **2026-09-08** [`d348bc26ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/d348bc26ec) [#18455](https://github.com/NVIDIA/TensorRT-LLM/pull/18455)
  [TRTLLM-16103][feat] protect private model architecture names (#18455)
  _Files: `AGENTS.md`, `README.md`, `tensorrt_llm/usage/architecture_allowlist.py`, `tensorrt_llm/usage/schemas/README.md` _+4 more__
- **2026-09-08** [`d6bd9eaf6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6bd9eaf6e) [#18825](https://github.com/NVIDIA/TensorRT-LLM/pull/18825)
  [None][feat] perf-optimize: add elimination and overlap questions to the per-kernel coverage contract (#18825)
  _Files: `agent-flow/.claude/skills/perf-optimize/SKILL.md`, `agent-flow/agent_flow/workflows/perf_optimize/README.md`, `agent-flow/agent_flow/workflows/perf_optimize/cli.py`, `agent-flow/agent_flow/workflows/perf_optimize/kernel_ledger.py` _+8 more__
- **2026-09-08** [`8488761e76`](https://github.com/NVIDIA/TensorRT-LLM/commit/8488761e76) [#18805](https://github.com/NVIDIA/TensorRT-LLM/pull/18805)
  [None][feat] Decompose the nsys timeline in the perf-analyze/optimize workflows (#18805)
  _Files: `agent-flow/.claude/skills/perf-analyze/SKILL.md`, `agent-flow/.claude/skills/perf-optimize/SKILL.md`, `agent-flow/README.md`, `agent-flow/agent_flow/workflows/perf_analyze/README.md` _+35 more__
- **2026-09-08** [`58b4bc6639`](https://github.com/NVIDIA/TensorRT-LLM/commit/58b4bc6639) [#18789](https://github.com/NVIDIA/TensorRT-LLM/pull/18789)
  [None][feat] Add lightweight remote execution to performance workflows (#18789)
  _Files: `agent-flow/agent_flow/workflows/perf_analyze/README.md`, `agent-flow/agent_flow/workflows/perf_analyze/cli.py`, `agent-flow/agent_flow/workflows/perf_analyze/prompts/__init__.py`, `agent-flow/agent_flow/workflows/perf_analyze/prompts/_common.py` _+16 more__
- **2026-09-08** [`7fb64ae8a8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fb64ae8a8) [#18568](https://github.com/NVIDIA/TensorRT-LLM/pull/18568)
  [None][feat] add parallel feature for perf-optimize in agent flow (#18568)
  _Files: `agent-flow/.claude/skills/perf-optimize/SKILL.md`, `agent-flow/agent_flow/workflows/perf_optimize/README.md`, `agent-flow/agent_flow/workflows/perf_optimize/__init__.py`, `agent-flow/agent_flow/workflows/perf_optimize/cli.py` _+18 more__

## Torch Path (_torch)  (8 commits)

- **2026-09-14** [`3dd002db37`](https://github.com/NVIDIA/TensorRT-LLM/commit/3dd002db37) [#19017](https://github.com/NVIDIA/TensorRT-LLM/pull/19017)
  [None][test] Add coverage for BartForConditionalGeneration (#19017)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_bart.py`_
- **2026-09-14** [`eefca665ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/eefca665ca) [#18948](https://github.com/NVIDIA/TensorRT-LLM/pull/18948)
  [None][test] Add native PyTorch coverage for DeciLMForCausalLM (#18948)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nas.py`_
- **2026-09-14** [`fa9813cc4d`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa9813cc4d) [#18888](https://github.com/NVIDIA/TensorRT-LLM/pull/18888)
  [TRTLLM-15936][fix] Enable breakable prefill CUDA graphs (BCG) for Nemotron-H hybrid models (#18888)
  _Files: `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+2 more__
- **2026-09-13** [`5dc504668e`](https://github.com/NVIDIA/TensorRT-LLM/commit/5dc504668e) [#18632](https://github.com/NVIDIA/TensorRT-LLM/pull/18632)
  [TRTLLM-16122][feat] Refine VisualGen serve benching (#18632)
  _Files: `examples/visual_gen/models/cosmos3/prompts/action_inverse_dynamics.json`, `examples/visual_gen/serve/README.md`, `examples/visual_gen/serve/benchmark_visual_gen.sh`, `examples/visual_gen/serve/benchmark_visual_gen_mgmn_distributed.sh` _+10 more__
- **2026-09-11** [`1374e96c89`](https://github.com/NVIDIA/TensorRT-LLM/commit/1374e96c89) [#18820](https://github.com/NVIDIA/TensorRT-LLM/pull/18820)
  [None][perf] Build GDN verify-path intermediate state indices once per step (#18820)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_gdn_kernel_optimizations.py`_
- **2026-09-10** [`5c89e7aa67`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c89e7aa67) [#18352](https://github.com/NVIDIA/TensorRT-LLM/pull/18352)
  [None][fix] Add Linux EBADHANDLE error handling (#18352)
  _Files: `tensorrt_llm/_torch/model_config.py`_
- **2026-09-10** [`b2ec2c1c7c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2ec2c1c7c) [#18845](https://github.com/NVIDIA/TensorRT-LLM/pull/18845)
  [None][perf] Use indexed in-place state I/O for GDN prefill in verify batches (#18845)
  _Files: `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`_
- **2026-09-07** [`374df3c3c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/374df3c3c1) [#18715](https://github.com/NVIDIA/TensorRT-LLM/pull/18715)
  [https://nvbugs/6682352][fix] rebuild MNNVL communicator on layout change (#18715)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/test_mnnvl_memory_lifecycle.py`_

## ROCm / AMD  (7 commits)

- **2026-09-14** [`858a360ffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/858a360ffe) [#18861](https://github.com/NVIDIA/TensorRT-LLM/pull/18861)
  [None][chore] Refine QA code ownership (#18861)
  _Files: `.github/CODEOWNERS`_
- **2026-09-11** [`0628a73388`](https://github.com/NVIDIA/TensorRT-LLM/commit/0628a73388) [#18908](https://github.com/NVIDIA/TensorRT-LLM/pull/18908)
  [None][test] add guided decoding architecture coverage (#18908)
  _Files: `docs/source/models/supported-models.md`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/test_kimi3.py`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` _+3 more__
- **2026-09-10** [`05838cebf4`](https://github.com/NVIDIA/TensorRT-LLM/commit/05838cebf4) [#18827](https://github.com/NVIDIA/TensorRT-LLM/pull/18827)
  [TRTLLM-15714][refactor] Move disagg send/reap/timeout/cancel orchestration into DisaggTransferCoordinator (#18827)
  _Files: `.github/CODEOWNERS`, `tensorrt_llm/_torch/disaggregation/executor/coordinator.py`, `tensorrt_llm/_torch/disaggregation/orchestration/__init__.py`, `tensorrt_llm/_torch/disaggregation/orchestration/admission.py` _+22 more__
- **2026-09-10** [`bccc86ad59`](https://github.com/NVIDIA/TensorRT-LLM/commit/bccc86ad59) [#18041](https://github.com/NVIDIA/TensorRT-LLM/pull/18041)
  [None][fix] bridge FP4 MLA disaggregated KV ownership (#18041)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/serve/openai_client.py` _+2 more__
- **2026-09-09** [`5f7e4cc68a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f7e4cc68a) [#18905](https://github.com/NVIDIA/TensorRT-LLM/pull/18905)
  [None][test] expand speculative decoding model coverage (#18905)
  _Files: `docs/source/models/supported-models.md`, `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml` _+9 more__
- **2026-09-08** [`9dfa2e21e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/9dfa2e21e1) [#18343](https://github.com/NVIDIA/TensorRT-LLM/pull/18343)
  [None][feat] Page the DSpark drafter context through the draft KV cache manager (#18343)
  _Files: `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+6 more__
- **2026-09-07** [`5fa39642b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa39642b9) [#18699](https://github.com/NVIDIA/TensorRT-LLM/pull/18699)
  [None][test] add Kimi K3 feature matrix coverage (#18699)
  _Files: `docs/source/models/supported-models.md`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/test_glm52.py`, `tests/integration/defs/accuracy/test_kimi3.py` _+2 more__

## Speculative Decoding  (6 commits)

- **2026-09-13** [`21dc97fbc8`](https://github.com/NVIDIA/TensorRT-LLM/commit/21dc97fbc8) [#18721](https://github.com/NVIDIA/TensorRT-LLM/pull/18721)
  [None][refactor] BREAKING: Remove the two-model speculative decoding path and dead C++ spec-dec code (#18721)
- **2026-09-12** [`b349408280`](https://github.com/NVIDIA/TensorRT-LLM/commit/b349408280) [#18651](https://github.com/NVIDIA/TensorRT-LLM/pull/18651)
  [None][feat] Add no mcp flag for modeling agent (#18651)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/workflows/agent_team/README.md`, `agent-flow/agent_flow/workflows/agent_team/cli.py`, `agent-flow/agent_flow/workflows/agent_team/mcpless.py` _+20 more__
- **2026-09-10** [`c814fcffde`](https://github.com/NVIDIA/TensorRT-LLM/commit/c814fcffde) [#18629](https://github.com/NVIDIA/TensorRT-LLM/pull/18629)
  [https://nvbugs/6707519][fix] Re-land attempt 1 verbatim on the current tip — add… (#18629)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/draft_target.py`, `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/interface.py` _+2 more__
- **2026-09-10** [`3e05ad9778`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e05ad9778) [#18986](https://github.com/NVIDIA/TensorRT-LLM/pull/18986)
  [https://nvbugs/6626640][test] Bound Eagle VSWA test batch capacity (#18986)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`0369d450eb`](https://github.com/NVIDIA/TensorRT-LLM/commit/0369d450eb) [#18564](https://github.com/NVIDIA/TensorRT-LLM/pull/18564)
  [https://nvbugs/6702267][fix] Stage `kv_block_ids_per_seq` unrotated so the block table matches… (#18564)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`_
- **2026-09-08** [`20333a9831`](https://github.com/NVIDIA/TensorRT-LLM/commit/20333a9831) [#18858](https://github.com/NVIDIA/TensorRT-LLM/pull/18858)
  [None][fix] Make LlmRequest.is_generation_only_request a property to match the C++ binding (#18858)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/perf_metrics_manager.py` _+12 more__

## Models  (6 commits)

- **2026-09-12** [`d674bf6ff4`](https://github.com/NVIDIA/TensorRT-LLM/commit/d674bf6ff4) [#19089](https://github.com/NVIDIA/TensorRT-LLM/pull/19089)
  [None][infra] Waive failing GPT-OSS 4-GPU test case (#19089)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-11** [`efd828a848`](https://github.com/NVIDIA/TensorRT-LLM/commit/efd828a848) [#19026](https://github.com/NVIDIA/TensorRT-LLM/pull/19026)
  [https://nvbugs/6718910][chore] Unwaive deepseek perf sanity test (#19026)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-09** [`adfc41e28a`](https://github.com/NVIDIA/TensorRT-LLM/commit/adfc41e28a) [#18477](https://github.com/NVIDIA/TensorRT-LLM/pull/18477)
  [TRTLLM-14645][fix] VisualGen: cross-hardware CPU RNG for pipeline noise (#18477)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux.py`, `tensorrt_llm/_torch/visual_gen/models/flux/pipeline_flux2.py`, `tensorrt_llm/_torch/visual_gen/models/glm_image/pipeline_glm_image.py` _+12 more__
- **2026-09-08** [`d01b961de2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d01b961de2) [#18745](https://github.com/NVIDIA/TensorRT-LLM/pull/18745)
  [https://nvbugs/6721560][fix] Read the conditioning image in the three stale callers… (#18745)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_cosmos3.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_qwen_image.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`4e54eb20b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e54eb20b9) [#18806](https://github.com/NVIDIA/TensorRT-LLM/pull/18806)
  [None][test] Add Kimi K3 TEP8 performance coverage (#18806)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-07** [`634a3ec273`](https://github.com/NVIDIA/TensorRT-LLM/commit/634a3ec273) [#18655](https://github.com/NVIDIA/TensorRT-LLM/pull/18655)
  [None][test] Add func and perf cases for Qwen3.6-35B-A3B and gemma4 on Spark (#18655)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py` _+4 more__

## LoRA  (3 commits)

- **2026-09-10** [`74c69c7fdb`](https://github.com/NVIDIA/TensorRT-LLM/commit/74c69c7fdb) [#18846](https://github.com/NVIDIA/TensorRT-LLM/pull/18846)
  [None][chore] BREAKING: Remove unused C++ code (#18846)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/rnnStateManager.h`, `cpp/include/tensorrt_llm/runtime/gptJsonConfig.h`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt` _+20 more__
- **2026-09-09** [`52bc8e7bb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/52bc8e7bb8) [#18949](https://github.com/NVIDIA/TensorRT-LLM/pull/18949)
  [https://nvbugs/6640875][test] Stabilize LoRA KV scheduler tests and re-enable seven cases (#18949)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-08** [`2334357ec1`](https://github.com/NVIDIA/TensorRT-LLM/commit/2334357ec1) [#18289](https://github.com/NVIDIA/TensorRT-LLM/pull/18289)
  [TRTLLM-15892][feat] Add Anthropic Messages API support to trtllm-serve (#18289)
  _Files: `examples/serve/anthropic_compatibility/README.md`, `examples/serve/anthropic_compatibility/deployments/gateway_users.txt`, `examples/serve/anthropic_compatibility/gateway.py`, `examples/serve/anthropic_compatibility/serve.sh` _+16 more__

## AutoDeploy  (2 commits)

- **2026-09-14** [`fc3edba4f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc3edba4f8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-09-11** [`5d43ae17fd`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d43ae17fd) [#19001](https://github.com/NVIDIA/TensorRT-LLM/pull/19001)
  [TRTLLM-15097][test] Prune MiniMax-M2 and MiniMax-M2.5 tests (#19001)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` _+4 more__

---
_Generated 2026-09-14 15:07 UTC_