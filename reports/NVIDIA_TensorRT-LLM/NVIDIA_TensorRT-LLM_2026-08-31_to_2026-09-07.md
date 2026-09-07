# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-08-31 → 2026-09-07  |  **Total commits:** 259

## ✨ New Features This Week

- **2026-09-07** [#18749](https://github.com/NVIDIA/TensorRT-LLM/pull/18749) — [None][feat] Add opt-in GPU keepalive to the benchmark fill gate (#18749)
- **2026-09-07** [#18294](https://github.com/NVIDIA/TensorRT-LLM/pull/18294) — [None][feat] support Kimi K3 KDA replay with KV cache manager V2 (#18294)
- **2026-09-07** [#18699](https://github.com/NVIDIA/TensorRT-LLM/pull/18699) — [None][test] add Kimi K3 feature matrix coverage (#18699)
- **2026-09-07** [#18587](https://github.com/NVIDIA/TensorRT-LLM/pull/18587) — [None][docs] Add KV cache compression documentation and examples (#18587)
- **2026-09-07** [#18655](https://github.com/NVIDIA/TensorRT-LLM/pull/18655) — [None][test] Add func and perf cases for Qwen3.6-35B-A3B and gemma4 on Spark (#18655)
- **2026-09-07** [#18751](https://github.com/NVIDIA/TensorRT-LLM/pull/18751) — [None][feat] lm_eval: let the CLI override a task's stop strings (#18751)
- **2026-09-07** [#18586](https://github.com/NVIDIA/TensorRT-LLM/pull/18586) — [None][test] Enable strict checks for declarative extra import path (#18586)
- **2026-09-06** [#17399](https://github.com/NVIDIA/TensorRT-LLM/pull/17399) — [None][feat] integrate PrimTS FMHA kernels (#17399)
- **2026-09-06** [#18174](https://github.com/NVIDIA/TensorRT-LLM/pull/18174) — [None][feat] Add FlashInfer VisualGen attention backend (#18174)
- **2026-09-05** [#18463](https://github.com/NVIDIA/TensorRT-LLM/pull/18463) — [None][feat] Add Cosmos3 Edge Policy DROID support (#18463)
- _…and 55 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-07** [`5fa39642b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa39642b9) [#18699](https://github.com/NVIDIA/TensorRT-LLM/pull/18699) — [None][test] add Kimi K3 feature matrix coverage (#18699)
- **2026-09-03** [`fd79a3db6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd79a3db6e) [#17720](https://github.com/NVIDIA/TensorRT-LLM/pull/17720) — [None][fix] Guard Python KV receive ownership and publication (#17720)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
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
| [#17436](https://github.com/NVIDIA/TensorRT-LLM/issues/17436) | [Performance] OpenAI server logit_bias causes ~2x decode throughput lo | OpenAI API | 2026-08-09 |
| [#17437](https://github.com/NVIDIA/TensorRT-LLM/issues/17437) | [Bug]: Interior control-token rejection can split a tool-call prelude  | Speculative Decoding | 2026-08-08 |
| [#17016](https://github.com/NVIDIA/TensorRT-LLM/issues/17016) | [RFC]: Add openengine gRPC server support to trtllm-serve | RFC | 2026-08-03 |
| [#17021](https://github.com/NVIDIA/TensorRT-LLM/issues/17021) | DeepSeek-V4: OpenAI `tools` field reorders the system prompt after the | — | 2026-07-29 |
| [#17020](https://github.com/NVIDIA/TensorRT-LLM/issues/17020) | `trtllm-eval aime25`/`aime26` silently disable thinking on DeepSeek-V4 | — | 2026-07-29 |
| [#17013](https://github.com/NVIDIA/TensorRT-LLM/issues/17013) | [RFC]: Reduce overhead in KV cache event publishing | RFC | 2026-07-29 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-07-25 |
| [#16459](https://github.com/NVIDIA/TensorRT-LLM/issues/16459) | [Bug]: Preserve per-item processed metadata when computing multimodal  | Multimodal | 2026-07-21 |
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 63 |
| Attention | 44 |
| Executor / Runtime | 24 |
| Disaggregation / KV | 22 |
| MoE | 22 |
| Quantization | 19 |
| Torch Path (_torch) | 15 |
| Other | 14 |
| Models | 12 |
| Docs / Examples | 10 |
| Speculative Decoding | 8 |
| ROCm / AMD | 2 |
| LoRA | 2 |
| AutoDeploy | 2 |

## CI / Infra  (63 commits)

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
- **2026-09-06** [`ee7525c0cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee7525c0cd) [#18385](https://github.com/NVIDIA/TensorRT-LLM/pull/18385)
  [TRTLLMINF-357][infra] Consolidate runBranchesWithInfraDefer into shared lib (#18385)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`_
- **2026-09-05** [`fc8969ec59`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc8969ec59) [#18744](https://github.com/NVIDIA/TensorRT-LLM/pull/18744)
  [None][infra] Waive 1 failed cases for main in pre-merge 58732 (#18744)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-04** [`17803f6c0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/17803f6c0c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-09-04** [`f5e2fbf539`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5e2fbf539) [#17630](https://github.com/NVIDIA/TensorRT-LLM/pull/17630)
  [https://nvbugs/6593378][baseline] Overwrite partial Slurm artifact retries (#17630)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/bash_utils.sh`, `jenkins/scripts/slurm_install.sh`, `tests/unittest/scripts/test_slurm_install.py`_
- **2026-09-04** [`220545da63`](https://github.com/NVIDIA/TensorRT-LLM/commit/220545da63) [#18707](https://github.com/NVIDIA/TensorRT-LLM/pull/18707)
  [None][infra] Waive 4 failed cases for main in post-merge 2947 (#18707)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-04** [`8af89fffda`](https://github.com/NVIDIA/TensorRT-LLM/commit/8af89fffda) [#18708](https://github.com/NVIDIA/TensorRT-LLM/pull/18708)
  [None][infra] Add blossom-ci authorized users (#18708)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-09-04** [`75ae1d4061`](https://github.com/NVIDIA/TensorRT-LLM/commit/75ae1d4061) [#18692](https://github.com/NVIDIA/TensorRT-LLM/pull/18692)
  [None][infra] Waive 1 failed cases for main in pre-merge 58485 (#18692)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-03** [`3503e3f9bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/3503e3f9bb) [#18685](https://github.com/NVIDIA/TensorRT-LLM/pull/18685)
  [None][infra] Waive 1 failed cases for main in pre-merge 58439 (#18685)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-03** [`01dc618130`](https://github.com/NVIDIA/TensorRT-LLM/commit/01dc618130) [#18622](https://github.com/NVIDIA/TensorRT-LLM/pull/18622)
  [TRTLLMINF-336][infra] enable BOLT premerge consume scaffolding (default off) (#18622)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-09-03** [`116fe875c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/116fe875c5) [#17843](https://github.com/NVIDIA/TensorRT-LLM/pull/17843)
  [None][ci] Add focused CBTS coverage for OpenEngine (#17843)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/README.md` _+4 more__
- **2026-09-03** [`26581002bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/26581002bd) [#18603](https://github.com/NVIDIA/TensorRT-LLM/pull/18603)
  [https://nvbugs/6602094][chore] Unwaive RocketKV test_model tests (#18603)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-03** [`f047b8076c`](https://github.com/NVIDIA/TensorRT-LLM/commit/f047b8076c) [#18355](https://github.com/NVIDIA/TensorRT-LLM/pull/18355)
  [TRTLLMINF-356][infra] Upload results at the end of stage no matter whether the peridic uplo… (#18355)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-03** [`2e522c5f30`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e522c5f30) [#18573](https://github.com/NVIDIA/TensorRT-LLM/pull/18573)
  [None][infra] Avoid false CBTS follow-up for test lists (#18573)
  _Files: `.coderabbit.yaml`_
- **2026-09-03** [`949716a175`](https://github.com/NVIDIA/TensorRT-LLM/commit/949716a175) [#17686](https://github.com/NVIDIA/TensorRT-LLM/pull/17686)
  [TRTLLMINF-316][infra] Use authenticated token for GitHub fetch in build and test jobs (#17686)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_install.sh`, `jenkins/scripts/slurm_run.sh`_
- **2026-09-03** [`9e722517e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e722517e3) [#18462](https://github.com/NVIDIA/TensorRT-LLM/pull/18462)
  [TRTLLMINF-365][infra] BoltProfileGen: run the merge job on the CPU partition (#18462)
  _Files: `jenkins/BoltProfileGen.groovy`, `scripts/bolt/internal/slurm_merge.sh`_
- **2026-09-03** [`f04b7d044d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f04b7d044d) [#18469](https://github.com/NVIDIA/TensorRT-LLM/pull/18469)
  [TRTLLMINF-376][infra] default BoltProfileGen aarch64 platform to gb300-flex-oci-jhb (#18469)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-02** [`6d3c6891e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d3c6891e0) [#18460](https://github.com/NVIDIA/TensorRT-LLM/pull/18460)
  [None][ci] waive pre-existing test failures on main (#18460)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-02** [`449d5eec83`](https://github.com/NVIDIA/TensorRT-LLM/commit/449d5eec83) [#18426](https://github.com/NVIDIA/TensorRT-LLM/pull/18426)
  [TRTLLMINF-374][infra] BoltProfileGen: log SLURM queue-vs-run timing (#18426)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-02** [`2d80f64967`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d80f64967) [#18425](https://github.com/NVIDIA/TensorRT-LLM/pull/18425)
  [TRTLLMINF-373][infra] BoltProfileGen: persistent version-keyed llvm-bolt cache (#18425)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-02** [`acc5633df9`](https://github.com/NVIDIA/TensorRT-LLM/commit/acc5633df9) [#18073](https://github.com/NVIDIA/TensorRT-LLM/pull/18073)
  [TRTLLMINF-160][infra] Support CBTS test result reuse (#18073)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/open_search_query.py`_
- **2026-09-02** [`5098fbe89d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5098fbe89d) [#18543](https://github.com/NVIDIA/TensorRT-LLM/pull/18543)
  [None][infra] Tighten CBTS testdef anchors for deletion-only test diffs (#18543)
  _Files: `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/_helpers.py`, `jenkins/scripts/cbts/rules/tests_def_rule.py`, `tests/unittest/scripts/test_cbts_tests_def_rule.py`_
- **2026-09-02** [`35b90c165a`](https://github.com/NVIDIA/TensorRT-LLM/commit/35b90c165a) [#18508](https://github.com/NVIDIA/TensorRT-LLM/pull/18508)
  [TRTLLMINF-353][infra] add maintenance stage config (#18508)
  _Files: `.github/CODEOWNERS`, `jenkins/config/maintenance_stages.txt`_
- **2026-09-02** [`6d10c672bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d10c672bd) [#18305](https://github.com/NVIDIA/TensorRT-LLM/pull/18305)
  [None][fix] Fix INFRA-DEFER stage status and multi-GPU blocking (#18305)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`_
- **2026-09-02** [`b387759178`](https://github.com/NVIDIA/TensorRT-LLM/commit/b387759178)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-09-02** [`f8aa81a370`](https://github.com/NVIDIA/TensorRT-LLM/commit/f8aa81a370) [#18536](https://github.com/NVIDIA/TensorRT-LLM/pull/18536)
  [https://nvbugs/6698723][fix] Unwaive tests after model config fix (#18536)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-02** [`55b383050a`](https://github.com/NVIDIA/TensorRT-LLM/commit/55b383050a) [#18442](https://github.com/NVIDIA/TensorRT-LLM/pull/18442)
  [None][infra] Expand CBTS Tier 2 pilot to QA team (#18442)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-09-02** [`f221314f60`](https://github.com/NVIDIA/TensorRT-LLM/commit/f221314f60) [#18567](https://github.com/NVIDIA/TensorRT-LLM/pull/18567)
  [None][infra] Waive 1 failed cases for main in pre-merge 57819 (#18567)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-02** [`fa8a3c8f50`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa8a3c8f50) [#18562](https://github.com/NVIDIA/TensorRT-LLM/pull/18562)
  [None][infra] Waive 1 failed cases for main in pre-merge 57886 (#18562)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`fcc84548ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/fcc84548ee) [#18424](https://github.com/NVIDIA/TensorRT-LLM/pull/18424)
  [TRTLLMINF-372][infra] BoltProfileGen: parallel chunked artifact downloads (#18424)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-01** [`efcf8e9fb7`](https://github.com/NVIDIA/TensorRT-LLM/commit/efcf8e9fb7) [#18530](https://github.com/NVIDIA/TensorRT-LLM/pull/18530)
  [None][infra] Waive 1 failed cases for main in pre-merge 57863 (#18530)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`a43418424f`](https://github.com/NVIDIA/TensorRT-LLM/commit/a43418424f) [#18529](https://github.com/NVIDIA/TensorRT-LLM/pull/18529)
  [None][infra] Waive 1 failed cases for main in pre-merge 57863 (#18529)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`90789525f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/90789525f3) [#18522](https://github.com/NVIDIA/TensorRT-LLM/pull/18522)
  [None][infra] Waive 1 failed cases for main in pre-merge 57818 (#18522)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`e6f2e3fa39`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6f2e3fa39) [#18512](https://github.com/NVIDIA/TensorRT-LLM/pull/18512)
  [None][infra] Waive 8 failed cases for main in post-merge 2942 (#18512)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`f04859d04d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f04859d04d) [#18499](https://github.com/NVIDIA/TensorRT-LLM/pull/18499)
  [None][infra] Waive 1 failed cases for main in pre-merge 57755 (#18499)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`39d915cac1`](https://github.com/NVIDIA/TensorRT-LLM/commit/39d915cac1) [#18495](https://github.com/NVIDIA/TensorRT-LLM/pull/18495)
  [None][infra] Waive 1 failed cases for main in pre-merge 57684 (#18495)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`418b9709a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/418b9709a6) [#18494](https://github.com/NVIDIA/TensorRT-LLM/pull/18494)
  [None][infra] Waive 1 failed cases for main in pre-merge 57744 (#18494)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`f3359bed21`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3359bed21) [#18480](https://github.com/NVIDIA/TensorRT-LLM/pull/18480)
  [None][infra] Lower GB300 16-GPU accuracy test timeout to 90 minutes (#18480)
  _Files: `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_node4_gpu16.yml`_
- **2026-09-01** [`b53be97789`](https://github.com/NVIDIA/TensorRT-LLM/commit/b53be97789) [#18481](https://github.com/NVIDIA/TensorRT-LLM/pull/18481)
  [None][test] Waive 2 failed cases for main in QA CI (#18481)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`b6fc74fdce`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6fc74fdce) [#18192](https://github.com/NVIDIA/TensorRT-LLM/pull/18192)
  [https://nvbugs/6644487][fix] Unwaive one case which might be fixed (#18192)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`69889e1f66`](https://github.com/NVIDIA/TensorRT-LLM/commit/69889e1f66) [#18475](https://github.com/NVIDIA/TensorRT-LLM/pull/18475)
  [None][test] Waive 2 failed cases for main in QA CI (#18475)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`c1d013411c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c1d013411c) [#18473](https://github.com/NVIDIA/TensorRT-LLM/pull/18473)
  [None][infra] Waive 6 failed cases for main in post-merge 2941 (#18473)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`ca0b685d66`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca0b685d66) [#18472](https://github.com/NVIDIA/TensorRT-LLM/pull/18472)
  [None][test] Waive 2 failed cases for main in QA CI (#18472)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`b621454edd`](https://github.com/NVIDIA/TensorRT-LLM/commit/b621454edd) [#18467](https://github.com/NVIDIA/TensorRT-LLM/pull/18467)
  [None][infra] Waive 1 failed cases for main in pre-merge 57672 (#18467)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`5c5a5d8b20`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c5a5d8b20) [#18468](https://github.com/NVIDIA/TensorRT-LLM/pull/18468)
  [None][infra] Waive 1 failed cases for main in pre-merge 57472 (#18468)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`2ca8aae8e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ca8aae8e0) [#18430](https://github.com/NVIDIA/TensorRT-LLM/pull/18430)
  [https://nvbugs/6633929][fix] Fix XGrammar structural tag doc links and pin the source link (#18430)
  _Files: `docs/source/features/guided-decoding.md`, `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`20fe04a8ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/20fe04a8ac) [#18452](https://github.com/NVIDIA/TensorRT-LLM/pull/18452)
  [None][infra] Waive 1 failed cases for main in pre-merge 57535 (#18452)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`f21fb00efa`](https://github.com/NVIDIA/TensorRT-LLM/commit/f21fb00efa) [#18453](https://github.com/NVIDIA/TensorRT-LLM/pull/18453)
  [None][test] Waive 2 failed cases for main in QA CI (#18453)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`1151605704`](https://github.com/NVIDIA/TensorRT-LLM/commit/1151605704) [#18451](https://github.com/NVIDIA/TensorRT-LLM/pull/18451)
  [None][test] Waive 1 failed cases for main in QA CI (#18451)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`5fa3078ced`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa3078ced) [#18441](https://github.com/NVIDIA/TensorRT-LLM/pull/18441)
  [TRTLLMINF-371][infra] Run pre-commits checks on all files if there are more than 3000 changed files (#18441)
  _Files: `.github/workflows/precommit-check.yml`, `jenkins/L0_MergeRequest.groovy`_
- **2026-08-31** [`879603afff`](https://github.com/NVIDIA/TensorRT-LLM/commit/879603afff) [#18439](https://github.com/NVIDIA/TensorRT-LLM/pull/18439)
  [None][test] Waive 1 failed cases for main in QA CI (#18439)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`23e8905722`](https://github.com/NVIDIA/TensorRT-LLM/commit/23e8905722) [#18438](https://github.com/NVIDIA/TensorRT-LLM/pull/18438)
  [None][test] Waive 11 failed cases for main in QA CI (#18438)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`1b191b610b`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b191b610b) [#18435](https://github.com/NVIDIA/TensorRT-LLM/pull/18435)
  [None][test] Waive 1 failed cases for main in QA CI (#18435)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`66f684b249`](https://github.com/NVIDIA/TensorRT-LLM/commit/66f684b249) [#18279](https://github.com/NVIDIA/TensorRT-LLM/pull/18279)
  [TRTLLMINF-339][infra] enable BOLT profile overlay on published container images (#18279)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-31** [`ea8f861e18`](https://github.com/NVIDIA/TensorRT-LLM/commit/ea8f861e18) [#18423](https://github.com/NVIDIA/TensorRT-LLM/pull/18423)
  [None][test] Waive 3 failed cases for main in QA CI (#18423)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`2e041d1e18`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e041d1e18) [#18420](https://github.com/NVIDIA/TensorRT-LLM/pull/18420)
  [None][infra] Waive 7 failed cases for main in post-merge 2938 (#18420)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`5b09f87de2`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b09f87de2) [#18286](https://github.com/NVIDIA/TensorRT-LLM/pull/18286)
  [https://nvbugs/6384625][fix] Unwaive testcase (#18286)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`73ee6b0b19`](https://github.com/NVIDIA/TensorRT-LLM/commit/73ee6b0b19) [#18419](https://github.com/NVIDIA/TensorRT-LLM/pull/18419)
  [None][test] Waive 2 failed cases for main in QA CI (#18419)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`8b1f34531c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b1f34531c) [#18418](https://github.com/NVIDIA/TensorRT-LLM/pull/18418)
  [None][test] Waive 6 failed cases for main in QA CI (#18418)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`c0503c2b0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0503c2b0a) [#18415](https://github.com/NVIDIA/TensorRT-LLM/pull/18415)
  [None][infra] Waive 1 failed cases for main in post-merge 2938 (#18415)
  _Files: `tests/integration/test_lists/waives.txt`_

## Attention  (44 commits)

- **2026-09-07** [`0bbca8333f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bbca8333f) [#18093](https://github.com/NVIDIA/TensorRT-LLM/pull/18093)
  [https://nvbugs/6621358][fix] Enable one-model draft KV reuse in cache manager V2 (#18093)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/config.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+36 more__
- **2026-09-07** [`e473b03a6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e473b03a6c) [#18587](https://github.com/NVIDIA/TensorRT-LLM/pull/18587)
  [None][docs] Add KV cache compression documentation and examples (#18587)
  _Files: `docs/source/developer-guide/kv-cache-cold-page-codec.md`, `docs/source/developer-guide/kv-cache-compression-development.md`, `docs/source/features/kv-cache-compression.md`, `docs/source/features/kvcache.md` _+8 more__
- **2026-09-06** [`75f521ddac`](https://github.com/NVIDIA/TensorRT-LLM/commit/75f521ddac) [#18771](https://github.com/NVIDIA/TensorRT-LLM/pull/18771)
  [None][fix] Update stale attention and KV-cache import paths that break main (#18771)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/phased.py`, `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py`, `tensorrt_llm/_torch/attention/backends/fmha/utils.py`, `tensorrt_llm/_torch/pyexecutor/engine/lora.py` _+6 more__
- **2026-09-06** [`b6dd8afd5d`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6dd8afd5d) [#17399](https://github.com/NVIDIA/TensorRT-LLM/pull/17399)
  [None][feat] integrate PrimTS FMHA kernels (#17399)
- **2026-09-06** [`26092ade9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/26092ade9d) [#18174](https://github.com/NVIDIA/TensorRT-LLM/pull/18174)
  [None][feat] Add FlashInfer VisualGen attention backend (#18174)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/utils.py` _+10 more__
- **2026-09-06** [`06ce7bf24e`](https://github.com/NVIDIA/TensorRT-LLM/commit/06ce7bf24e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+11 more__
- **2026-09-05** [`a56ec20396`](https://github.com/NVIDIA/TensorRT-LLM/commit/a56ec20396) [#17968](https://github.com/NVIDIA/TensorRT-LLM/pull/17968)
  [TRTLLM-14558][chore] Consolidate the Attention domain: modules, backends and unit tests (#17968)
- **2026-09-04** [`c7da76e4ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7da76e4ce) [#18518](https://github.com/NVIDIA/TensorRT-LLM/pull/18518)
  [None][feat] Enable Rubin (SM107) trtllm-gen FMHA features (#18518)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/kernels/multiHeadAttentionCommon.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h` _+8 more__
- **2026-09-04** [`7635b57b0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7635b57b0d) [#18000](https://github.com/NVIDIA/TensorRT-LLM/pull/18000)
  [TRTLLM-15011][infra] Unwaive TestDeepSeekV4Flash::test_auto_dtype (#18000)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-04** [`efdd087558`](https://github.com/NVIDIA/TensorRT-LLM/commit/efdd087558) [#17466](https://github.com/NVIDIA/TensorRT-LLM/pull/17466)
  [None][fix] Fix window vector layer indexing (#17466)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py` _+9 more__
- **2026-09-04** [`cbf859251e`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbf859251e) [#18639](https://github.com/NVIDIA/TensorRT-LLM/pull/18639)
  [None][perf] Use single-op int64 exchanges for per-iteration attention-DP host collectives (#18639)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+6 more__
- **2026-09-04** [`6bb72faadc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bb72faadc) [#18710](https://github.com/NVIDIA/TensorRT-LLM/pull/18710)
  [None][doc] Document FMHA availability contract (#18710)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/interface.py`_
- **2026-09-04** [`f295bd001a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f295bd001a) [#18548](https://github.com/NVIDIA/TensorRT-LLM/pull/18548)
  [None][chore] Extract FMHA manager from TrtllmAttention (#18548)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/interface.py`, `tensorrt_llm/_torch/attention_backend/fmha/manager.py`, `tensorrt_llm/_torch/attention_backend/fmha/msa_sparse_gqa.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_utils.py` _+7 more__
- **2026-09-04** [`8da2ed1961`](https://github.com/NVIDIA/TensorRT-LLM/commit/8da2ed1961) [#17374](https://github.com/NVIDIA/TensorRT-LLM/pull/17374)
  [None][fix] Use HND mapping for MiniMax-M3 MSA KV cache (#17374)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/disaggregation/resource/page.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/unittest/disaggregated/test_minimax_m3_kv_transfer.py` _+1 more__
- **2026-09-04** [`98c176f042`](https://github.com/NVIDIA/TensorRT-LLM/commit/98c176f042) [#18157](https://github.com/NVIDIA/TensorRT-LLM/pull/18157)
  [None][fix] Handle refused attention DP pad dummy on legacy ranks (#18157)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-04** [`f30e0f2df4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f30e0f2df4) [#18596](https://github.com/NVIDIA/TensorRT-LLM/pull/18596)
  [https://nvbugs/6692197][perf] Reuse FlashInfer plans for single-token decode (#18596)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tests/unittest/_torch/attention/test_flashinfer_attention.py`_
- **2026-09-03** [`1bd5e4328c`](https://github.com/NVIDIA/TensorRT-LLM/commit/1bd5e4328c) [#18278](https://github.com/NVIDIA/TensorRT-LLM/pull/18278)
  [https://nvbugs/6655987][fix] Isolate FlashInfer JIT workspaces across MPI processes (#18278)
  _Files: `docs/source/llm-api/index.md`, `tensorrt_llm/llmapi/mpi_session.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+6 more__
- **2026-09-03** [`e5b67d53c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5b67d53c2) [#18646](https://github.com/NVIDIA/TensorRT-LLM/pull/18646)
  [None][perf] Seed the GVR prior from device-side prefill lengths (#18646)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/modules/top_k.py`, `tests/unittest/_torch/modules/test_top_k.py`_
- **2026-09-03** [`5a8b284fb2`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a8b284fb2) [#18545](https://github.com/NVIDIA/TensorRT-LLM/pull/18545)
  [https://nvbugs/6698606][fix] Keep quantized KV context on TRTLLM-Gen FMHA (#18545)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-09-03** [`38b8c559b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/38b8c559b9) [#17681](https://github.com/NVIDIA/TensorRT-LLM/pull/17681)
  [None][feat] Add NVFP4 KV cache support for DSA (#17681)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/mlaKernels.cu`, `cpp/tensorrt_llm/kernels/mlaKernels.h` _+26 more__
- **2026-09-03** [`4b63205f49`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b63205f49) [#18476](https://github.com/NVIDIA/TensorRT-LLM/pull/18476)
  [TRTLLM-14645][fix] VisualGen: allow sm_107a in CuTe DSL FMHA and guard unsupported SAGE SM (#18476)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/fmha.py`, `tensorrt_llm/visual_gen/args.py`, `tests/unittest/_torch/visual_gen/test_visual_gen_args.py`_
- **2026-09-03** [`e0b3772035`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0b3772035) [#18264](https://github.com/NVIDIA/TensorRT-LLM/pull/18264)
  [TRTLLM-14575][perf] Add env-gated BF16 DSA indexer projection (#18264)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-09-03** [`31779d6e65`](https://github.com/NVIDIA/TensorRT-LLM/commit/31779d6e65) [#18428](https://github.com/NVIDIA/TensorRT-LLM/pull/18428)
  [None][chore] Update flashinfer-python from 0.6.16 to 0.6.18 (#18428)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-09-03** [`cb796e849f`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb796e849f) [#16506](https://github.com/NVIDIA/TensorRT-LLM/pull/16506)
  [None][doc] Add video generation optimization blog (#16506)
  _Files: `.gitattributes`, `README.md`, `docs/source/blogs/media/tech_blog28_bf16_time_breakdown.png`, `docs/source/blogs/media/tech_blog28_latency_step_down.png` _+17 more__
- **2026-09-03** [`f00b2be4f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/f00b2be4f1) [#18375](https://github.com/NVIDIA/TensorRT-LLM/pull/18375)
  [TRTLLM-15160][feat] Add post-attention o_proj gate hook to shared MLA base and make trtllm::kda_decode inplace-only (#18375)
  _Files: `cpp/tensorrt_llm/thop/kdaDecodeOp.cpp`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py` _+7 more__
- **2026-09-03** [`beb0a09ebd`](https://github.com/NVIDIA/TensorRT-LLM/commit/beb0a09ebd) [#18544](https://github.com/NVIDIA/TensorRT-LLM/pull/18544)
  [https://nvbugs/6700260][fix] Fix Gemma4 TRTLLM FMHA fallback selection (#18544)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention_backend/fmha/triton_custom_mask.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-09-03** [`9362a5613d`](https://github.com/NVIDIA/TensorRT-LLM/commit/9362a5613d) [#18118](https://github.com/NVIDIA/TensorRT-LLM/pull/18118)
  [None][perf] Enable configurable MLA skip correction for TRT-LLM Gen FMHA (#18118)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp` _+22 more__
- **2026-09-02** [`42903f9a94`](https://github.com/NVIDIA/TensorRT-LLM/commit/42903f9a94) [#18064](https://github.com/NVIDIA/TensorRT-LLM/pull/18064)
  [TRTLLM-15498][perf] prepare Kimi K3 prefill metadata (#18064)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/models/modeling_kimi_k3_vl.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_k3_mamba_metadata.py` _+4 more__
- **2026-09-02** [`f848ecb24f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f848ecb24f) [#18593](https://github.com/NVIDIA/TensorRT-LLM/pull/18593)
  [https://nvbugs/6602094][fix] Avoid MPI bootstrap in RocketKV unit test (#18593)
  _Files: `tests/unittest/_torch/attention/sparse/rocketkv/test_rocketkv.py`_
- **2026-09-02** [`d7d79c3c24`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7d79c3c24) [#18265](https://github.com/NVIDIA/TensorRT-LLM/pull/18265)
  [TRTLLM-14575][perf] Enable fused-A GEMM for the GLM MLA A-projection (#18265)
  _Files: `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3FusedAGemm.cu`, `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3FusedAGemm.h`, `cpp/tensorrt_llm/thop/dsv3FusedAGemmOp.cpp`, `tests/unittest/_torch/thop/parallel/test_dsv3_fused_a_gemm.py`_
- **2026-09-02** [`c74f8cf244`](https://github.com/NVIDIA/TensorRT-LLM/commit/c74f8cf244) [#18268](https://github.com/NVIDIA/TensorRT-LLM/pull/18268)
  [TRTLLM-14575][perf] Fuse DSA decode metadata into a single Triton kernel (#18268)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/fused_metadata.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py`, `tests/unittest/_torch/attention/sparse/dsa/test_fused_metadata.py`_
- **2026-09-02** [`1ed2928d3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ed2928d3d) [#17858](https://github.com/NVIDIA/TensorRT-LLM/pull/17858)
  [TRTLLM-15040][test] Prune legacy Llama and Nemotron tests (#17858)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/.test_durations_aws_dfw`, `tests/integration/defs/accuracy/references/SlimPajama-6B.yaml`, `tests/integration/defs/accuracy/references/cnn_dailymail.yaml` _+58 more__
- **2026-09-02** [`5a1ae8f772`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a1ae8f772) [#18308](https://github.com/NVIDIA/TensorRT-LLM/pull/18308)
  [None][fix] Minimize and account for attention-DP dummy tokens (#18308)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-02** [`870d460cdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/870d460cdf) [#18474](https://github.com/NVIDIA/TensorRT-LLM/pull/18474)
  [None][perf] Widen MiniMax-M3 decode q in-register instead of in a copy (#18474)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/triton_sparse_decode.py`, `tests/unittest/_torch/attention/sparse/test_minimax_m3_sparse_attn_decode.py`_
- **2026-09-01** [`f77d1a2b2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f77d1a2b2b) [#18091](https://github.com/NVIDIA/TensorRT-LLM/pull/18091)
  [None][feat] Add NVFP4 as a cold-page KV Cache Compression Method (#18091)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_compression/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_compression/nativeColdPageCodec.cpp` _+39 more__
- **2026-09-01** [`5c03a515e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c03a515e7) [#18350](https://github.com/NVIDIA/TensorRT-LLM/pull/18350)
  [None][perf] Cache FMHA library selection in TrtllmAttention (#18350)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-09-01** [`8c0d0cbfef`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c0d0cbfef) [#18293](https://github.com/NVIDIA/TensorRT-LLM/pull/18293)
  [None][perf] Merge per-iteration attention-DP host allgathers in input prep (#18293)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+2 more__
- **2026-09-01** [`f152eb29af`](https://github.com/NVIDIA/TensorRT-LLM/commit/f152eb29af) [#18504](https://github.com/NVIDIA/TensorRT-LLM/pull/18504)
  [https://nvbugs/6697142][fix] Wire the stub the way `TrtllmAttention.forward` does and parametrize over both… (#18504)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-09-01** [`109f211d1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/109f211d1c) [#18383](https://github.com/NVIDIA/TensorRT-LLM/pull/18383)
  [TRTLLM-14575][perf] Use native next_n for DSA paged-MQA on Blackwell (#18383)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-09-01** [`d62fc67895`](https://github.com/NVIDIA/TensorRT-LLM/commit/d62fc67895) [#18061](https://github.com/NVIDIA/TensorRT-LLM/pull/18061)
  [None][perf] optimize DSpark attention (#18061)
  _Files: `tensorrt_llm/_torch/custom_ops/dspark_attention_custom_op.py`, `tensorrt_llm/_torch/custom_ops/dspark_rmsnorm_rope_custom_op.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dspark/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dspark/attention.py` _+8 more__
- **2026-08-31** [`3d466dba8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d466dba8d) [#18164](https://github.com/NVIDIA/TensorRT-LLM/pull/18164)
  [TRTLLM-14705][fix] Kimi K3 B200 enablement: MLA decode dispatch fix, L0 wiring, docs (#18164)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `docs/source/models/supported-models.md`, `examples/kimi_k3/README.md`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py` _+3 more__
- **2026-08-31** [`4593e50d78`](https://github.com/NVIDIA/TensorRT-LLM/commit/4593e50d78) [#18391](https://github.com/NVIDIA/TensorRT-LLM/pull/18391)
  [TRTLLM-14575][perf] Batch DSA cross-layer index remap into one kernel launch per indexer group (#18391)
  _Files: `cpp/tensorrt_llm/kernels/convertReqIndexToGlobal.cu`, `cpp/tensorrt_llm/kernels/convertReqIndexToGlobal.h`, `cpp/tensorrt_llm/thop/convertReqIndexToGlobalOp.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/backend.py` _+5 more__
- **2026-08-31** [`ad66327e17`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad66327e17) [#16214](https://github.com/NVIDIA/TensorRT-LLM/pull/16214)
  [None][feat] Support custom masks in TRTLLM attention (#16214)
  _Files: `cpp/tensorrt_llm/kernels/unfusedAttentionKernels.h`, `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h`, `cpp/tensorrt_llm/thop/trtllmGenQKVProcessOp.cpp`, `tensorrt_llm/_torch/attention_backend/fmha/__init__.py` _+19 more__
- **2026-08-31** [`775015b6c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/775015b6c0) [#18417](https://github.com/NVIDIA/TensorRT-LLM/pull/18417)
  [None][chore] Apply clang-format to FMHA kernel header (#18417)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_

## Executor / Runtime  (24 commits)

- **2026-09-07** [`65b244dcd3`](https://github.com/NVIDIA/TensorRT-LLM/commit/65b244dcd3) [#18749](https://github.com/NVIDIA/TensorRT-LLM/pull/18749)
  [None][feat] Add opt-in GPU keepalive to the benchmark fill gate (#18749)
  _Files: `docs/source/features/disagg-serving.md`, `tensorrt_llm/_torch/pyexecutor/gpu_keepalive.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_gpu_keepalive.py` _+1 more__
- **2026-09-07** [`288ad73745`](https://github.com/NVIDIA/TensorRT-LLM/commit/288ad73745) [#18135](https://github.com/NVIDIA/TensorRT-LLM/pull/18135)
  [https://nvbugs/6428069][fix] Drain only the due PP relay send before forward and unwaive the disagg PP tests (#18135)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-06** [`e8c3fcaccd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8c3fcaccd) [#18686](https://github.com/NVIDIA/TensorRT-LLM/pull/18686)
  [https://nvbugs/6720250][fix] Use adjusted clock for VisualGen timing (#18686)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/openai_video_routes.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/test_trtllm_serve_endpoints.py` _+1 more__
- **2026-09-04** [`c4422cea5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4422cea5a) [#18736](https://github.com/NVIDIA/TensorRT-LLM/pull/18736)
  [None][fix] Revert #18445 (#18736)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/README.md`, `jenkins/scripts/perf/local/README.md`, `jenkins/scripts/perf/local/configs/example.conf` _+23 more__
- **2026-09-04** [`b660b4b1e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b660b4b1e8) [#18613](https://github.com/NVIDIA/TensorRT-LLM/pull/18613)
  [https://nvbugs/6683840][fix] Join the encoder launch before the decoder forward (#18613)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-04** [`737af472c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/737af472c3) [#18445](https://github.com/NVIDIA/TensorRT-LLM/pull/18445)
  [None][feat] perf-sanity: upload per-request disagg lifecycle spans to OpenSearch (#18445)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/README.md`, `jenkins/scripts/perf/local/README.md`, `jenkins/scripts/perf/local/configs/example.conf` _+23 more__
- **2026-09-04** [`962c74c1f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/962c74c1f8) [#16635](https://github.com/NVIDIA/TensorRT-LLM/pull/16635)
  [TRTLLM-14715][feat] preserve MNNVL all-reduce graph VAs across restore (#16635)
  _Files: `cpp/tensorrt_llm/nanobind/runtime/bindings.cpp`, `cpp/tensorrt_llm/runtime/mcastDeviceMemory.cpp`, `cpp/tensorrt_llm/runtime/mcastDeviceMemory.h`, `cpp/tensorrt_llm/runtime/mcastGPUBuffer.h` _+5 more__
- **2026-09-03** [`45400eb827`](https://github.com/NVIDIA/TensorRT-LLM/commit/45400eb827) [#18558](https://github.com/NVIDIA/TensorRT-LLM/pull/18558)
  [TRTLLM-14881][feat] qualify Mistral dense for MX (#18558)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py` _+5 more__
- **2026-09-03** [`c2023c9d99`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2023c9d99) [#18513](https://github.com/NVIDIA/TensorRT-LLM/pull/18513)
  [https://nvbugs/6693991][fix] Restore verl rollout after sampler_type removal (#18513)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/defs/verl/verl_config.yml` _+1 more__
- **2026-09-03** [`40ac40773e`](https://github.com/NVIDIA/TensorRT-LLM/commit/40ac40773e) [#18524](https://github.com/NVIDIA/TensorRT-LLM/pull/18524)
  [TRTLLM-15751][refactor] Extract the MM-encoder item-scheduling facet into engine/multimodal.py (#18524)
  _Files: `.github/CODEOWNERS`, `tensorrt_llm/_torch/pyexecutor/engine/__init__.py`, `tensorrt_llm/_torch/pyexecutor/engine/multimodal.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+8 more__
- **2026-09-03** [`6c3235a24a`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c3235a24a) [#18456](https://github.com/NVIDIA/TensorRT-LLM/pull/18456)
  [TRTLLM-13409][fix] Count async KV completions as benchmark fill progress (#18456)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-09-03** [`68b2b97b79`](https://github.com/NVIDIA/TensorRT-LLM/commit/68b2b97b79) [#17493](https://github.com/NVIDIA/TensorRT-LLM/pull/17493)
  [TRTLLM-15277][feat] BREAKING: Redesign VisualGen reference inputs and server-to-worker IPC (#17493)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `examples/visual_gen/models/flux2.py`, `examples/visual_gen/models/qwen_image_edit.py` _+40 more__
- **2026-09-02** [`777a2c7fea`](https://github.com/NVIDIA/TensorRT-LLM/commit/777a2c7fea) [#18509](https://github.com/NVIDIA/TensorRT-LLM/pull/18509)
  [https://nvbugs/6693989][fix] Apply the K3 prompt-token offset only when a prompt count is actually known… (#18509)
  _Files: `tensorrt_llm/serve/postprocess_handlers.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-09-02** [`395985c025`](https://github.com/NVIDIA/TensorRT-LLM/commit/395985c025) [#17393](https://github.com/NVIDIA/TensorRT-LLM/pull/17393)
  [TRTLLM-15448][perf] Implement rank-striped checkpoint read-ahead (#17393)
  _Files: `docs/source/developer-guide/perf-benchmarking.md`, `docs/source/features/checkpoint-loading.md`, `docs/source/llm-api/index.md`, `tensorrt_llm/_torch/models/checkpoints/base_checkpoint_loader.py` _+14 more__
- **2026-09-02** [`e34e02f012`](https://github.com/NVIDIA/TensorRT-LLM/commit/e34e02f012) [#18236](https://github.com/NVIDIA/TensorRT-LLM/pull/18236)
  [TRTLLM-15888][fix] Proper lazy import for post transform profile matching (#18236)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py`, `tests/unittest/_torch/executor/test_model_loader_mx.py`_
- **2026-09-02** [`24a5c6425c`](https://github.com/NVIDIA/TensorRT-LLM/commit/24a5c6425c) [#18284](https://github.com/NVIDIA/TensorRT-LLM/pull/18284)
  [TRTLLM-15889][fix] Proper lazy import for MPI worker submit (#18284)
  _Files: `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/worker.py`, `tests/unittest/others/test_lazy_model_zoo.py`_
- **2026-09-01** [`c2467bc046`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2467bc046) [#18317](https://github.com/NVIDIA/TensorRT-LLM/pull/18317)
  [None][feat] Add locality domain Python layer (#18317)
  _Files: `tensorrt_llm/_torch/cute_dsl_utils.py`, `tensorrt_llm/_torch/locality_domain/__init__.py`, `tensorrt_llm/_torch/locality_domain/autotune.py`, `tensorrt_llm/_torch/locality_domain/layout.py` _+5 more__
- **2026-09-01** [`d105e6a76f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d105e6a76f) [#18326](https://github.com/NVIDIA/TensorRT-LLM/pull/18326)
  [https://nvbugs/6608382][test] Mitigate disagg cancellation test hangs (#18326)
  _Files: `tests/unittest/llmapi/test_llm_pytorch.py`_
- **2026-09-01** [`a1ad3edf92`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1ad3edf92) [#18202](https://github.com/NVIDIA/TensorRT-LLM/pull/18202)
  [None][fix] register beneficial-to-skip contributions only after scheduling (#18202)
  _Files: `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp`, `cpp/tests/unit_tests/batch_manager/capacitySchedulerTest.cpp`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler.py`, `tests/unittest/_torch/executor/test_py_scheduler.py`_
- **2026-08-31** [`6f6f069415`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f6f069415) [#17142](https://github.com/NVIDIA/TensorRT-LLM/pull/17142)
  [TRTLLM-14880][feat] qualify Qwen3 dense for MX (#17142)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py` _+4 more__
- **2026-08-31** [`19356d5ee0`](https://github.com/NVIDIA/TensorRT-LLM/commit/19356d5ee0) [#17030](https://github.com/NVIDIA/TensorRT-LLM/pull/17030)
  [TRTLLM-14778][perf] Add feature-mode encoder CUDA graphs for fixed-shape encoders (Whisper) (#17030)
  _Files: `docs/source/models/encoder-decoder.md`, `tensorrt_llm/_torch/models/modeling_whisper.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+9 more__
- **2026-08-31** [`03eb1a34eb`](https://github.com/NVIDIA/TensorRT-LLM/commit/03eb1a34eb) [#17377](https://github.com/NVIDIA/TensorRT-LLM/pull/17377)
  [TRTLLM-12680][feat] add exit code telemetry (#17377)
  _Files: `README.md`, `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/commands/_telemetry.py`, `tensorrt_llm/commands/bench.py` _+28 more__
- **2026-08-31** [`33d1a3cf9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/33d1a3cf9d) [#14095](https://github.com/NVIDIA/TensorRT-LLM/pull/14095)
  [TRTLLM-11412][feat] Add offloading support for visual_gen (#14095)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/executor.py` _+21 more__
- **2026-08-31** [`cfd7cf1d56`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfd7cf1d56) [#16710](https://github.com/NVIDIA/TensorRT-LLM/pull/16710)
  [None][feat] KVCacheManagerV2: suspend/resume observability stat + coverage (#16710)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.h`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp` _+11 more__

## Disaggregation / KV  (22 commits)

- **2026-09-07** [`ebf619a22a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ebf619a22a) [#18538](https://github.com/NVIDIA/TensorRT-LLM/pull/18538)
  [None][chore] Cleanup kv cache manager (#18538)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`_
- **2026-09-07** [`4b9f3ae3de`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b9f3ae3de) [#18294](https://github.com/NVIDIA/TensorRT-LLM/pull/18294)
  [None][feat] support Kimi K3 KDA replay with KV cache manager V2 (#18294)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_kda_mtp_ops.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_k3_mamba_metadata.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+5 more__
- **2026-09-07** [`564c73dd4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/564c73dd4a) [#18649](https://github.com/NVIDIA/TensorRT-LLM/pull/18649)
  [https://nvbugs/6594241][fix] increase timeout for test_disaggregated_gpt_oss_120b_harmony (#18649)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-06** [`70feda6395`](https://github.com/NVIDIA/TensorRT-LLM/commit/70feda6395) [#18554](https://github.com/NVIDIA/TensorRT-LLM/pull/18554)
  [https://nvbugs/6676406][fix] Fix DSV4 disagg MTP accuracy (#18554)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tests/unittest/disaggregated/test_cache_reuse_adapter.py`_
- **2026-09-05** [`c3c207a190`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3c207a190) [#17899](https://github.com/NVIDIA/TensorRT-LLM/pull/17899)
  [TRTLLM-14846][chore] Group KV Cache managers and reunite the Disaggregation transceiver halves (#17899)
- **2026-09-04** [`8e7ba24125`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e7ba24125) [#18695](https://github.com/NVIDIA/TensorRT-LLM/pull/18695)
  [NVBUG-6689820][test] unwaive Llama disaggregated serving test (#18695)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-04** [`f7b7f221d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7b7f221d5) [#18694](https://github.com/NVIDIA/TensorRT-LLM/pull/18694)
  [https://nvbugs/6674826][fix] Drop overlap hint from KV cache page-index upload (#18694)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/coldPageCopy.cu`, `tests/integration/test_lists/waives.txt`_
- **2026-09-04** [`56be13f4fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/56be13f4fc) [#18403](https://github.com/NVIDIA/TensorRT-LLM/pull/18403)
  [https://nvbugs/6686534][fix] Keep disagg worker liveness within its TTL window (#18403)
  _Files: `tensorrt_llm/serve/disagg_auto_scaling.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/disaggregated/test_disagg_cluster_manager_worker.py`_
- **2026-09-03** [`3901bca583`](https://github.com/NVIDIA/TensorRT-LLM/commit/3901bca583) [#18595](https://github.com/NVIDIA/TensorRT-LLM/pull/18595)
  [None][refactor] Add DisaggTransferCoordinator skeleton and loop transcript tests (#18595)
  _Files: `tensorrt_llm/_torch/disaggregation/executor/coordinator.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_disagg_coordinator.py`, `tests/unittest/_torch/executor/test_disagg_loop_transcript.py` _+1 more__
- **2026-09-03** [`e11905f5c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/e11905f5c6) [#17491](https://github.com/NVIDIA/TensorRT-LLM/pull/17491)
  [None][fix] Normalize perf metrics clocks across frontend processes (#17491)
  _Files: `tensorrt_llm/_utils.py`, `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/perf_metrics.py` _+2 more__
- **2026-09-03** [`c8c1feceee`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8c1feceee) [#18301](https://github.com/NVIDIA/TensorRT-LLM/pull/18301)
  [https://nvbugs/6670614][fix] Set UCX_TLS for Ray disaggregated serving tests (#18301)
  _Files: `tests/integration/defs/examples/test_ray.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-03** [`316c11354f`](https://github.com/NVIDIA/TensorRT-LLM/commit/316c11354f) [#18272](https://github.com/NVIDIA/TensorRT-LLM/pull/18272)
  [TRTLLM-15701][feat] Add branch-point Mamba state snapshots for hybrid KV cache prefix reuse (#18272)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.h` _+14 more__
- **2026-09-02** [`e34a4ff974`](https://github.com/NVIDIA/TensorRT-LLM/commit/e34a4ff974) [#15727](https://github.com/NVIDIA/TensorRT-LLM/pull/15727)
  [TRTLLM-12499][feat] Pipelined KVCache transfer for disaggregated serving in Python Cache Transceiver (#15727)
  _Files: `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py` _+18 more__
- **2026-09-02** [`cbd3dcb729`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbd3dcb729) [#18374](https://github.com/NVIDIA/TensorRT-LLM/pull/18374)
  [https://nvbugs/6668807][fix] Remove invalid GLM KV cache assertion (#18374)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`b7c58623d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7c58623d5) [#18372](https://github.com/NVIDIA/TensorRT-LLM/pull/18372)
  [https://nvbugs/6681216][fix] Raise disagg nixl readiness timeout on Blackwell (#18372)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`131cd15a1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/131cd15a1d) [#18373](https://github.com/NVIDIA/TensorRT-LLM/pull/18373)
  [https://nvbugs/6657468][fix] Set UCX_TLS for GB300 in disagg logprobs test (#18373)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`24ab1fab23`](https://github.com/NVIDIA/TensorRT-LLM/commit/24ab1fab23) [#18348](https://github.com/NVIDIA/TensorRT-LLM/pull/18348)
  [https://nvbugs/6649386][chore] Unwaive disaggregated deepseek_r1_v2_fp4_mtp_stress on B200 (#18348)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`6e6f506077`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e6f506077) [#18388](https://github.com/NVIDIA/TensorRT-LLM/pull/18388)
  [None][doc] Update GLM-5 docs for GLM-5.3 and disaggregated serving (#18388)
  _Files: `docs/source/deployment-guide/deployment-guide-for-glm-5-on-trtllm.md`, `docs/source/models/supported-models.md`_
- **2026-08-31** [`4c2ba54551`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c2ba54551) [#18178](https://github.com/NVIDIA/TensorRT-LLM/pull/18178)
  [None][refactor] Harden the KvCacheTransceiver contract and add a conformance fake (#18178)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_transceiver.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/fake_kv_cache_transceiver.py` _+4 more__
- **2026-08-31** [`e052d14bb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/e052d14bb4) [#18347](https://github.com/NVIDIA/TensorRT-LLM/pull/18347)
  [None][feat] Prefer POSIX FD handle type for KV cache V2 VMM allocations (#18347)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/cudaVirtMem.cpp`, `tensorrt_llm/runtime/kv_cache_manager_v2/_cuda_virt_mem.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_ad_disagg.py` _+6 more__
- **2026-08-31** [`be3fecb424`](https://github.com/NVIDIA/TensorRT-LLM/commit/be3fecb424) [#18298](https://github.com/NVIDIA/TensorRT-LLM/pull/18298)
  [None][test] Add AgentX DeepSeek-V4-Pro-DSpark perf-sanity lanes on GB300 (#18298)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/local/README.md`, `tests/integration/defs/.test_durations`, `tests/integration/defs/perf/README_test_perf_sanity.md` _+9 more__
- **2026-08-31** [`f787e8a1b6`](https://github.com/NVIDIA/TensorRT-LLM/commit/f787e8a1b6) [#18175](https://github.com/NVIDIA/TensorRT-LLM/pull/18175)
  [https://nvbugs/6647405][fix] Do not sleep out the KV transfer poll interval with no in-flight session (#18175)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tests/unittest/disaggregated/test_transceiver_bounded_polling.py`_

## MoE  (22 commits)

- **2026-09-07** [`058fade908`](https://github.com/NVIDIA/TensorRT-LLM/commit/058fade908) [#18785](https://github.com/NVIDIA/TensorRT-LLM/pull/18785)
  [None][fix] bench_moe: prune MNNVL comm methods that cannot span nodes (#18785)
  _Files: `tests/microbenchmarks/bench_moe/search.py`_
- **2026-09-07** [`e0ee12a55c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e0ee12a55c) [#18683](https://github.com/NVIDIA/TensorRT-LLM/pull/18683)
  [None][fix] Self-sampling top-k host: physical row-width envelope and exact-row warmup population (#18683)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_
- **2026-09-06** [`f7454b6bd2`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7454b6bd2) [#18612](https://github.com/NVIDIA/TensorRT-LLM/pull/18612)
  [TRTLLM-15316][fix] SM107 FP8 GEMM routing and runtime guards (follow-up to #17485) (#18612)
  _Files: `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/kernelLauncher.h`, `tensorrt_llm/_torch/attention/backends/sparse/rocket/kernels.py`, `tensorrt_llm/_torch/custom_ops/cuda_tile_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py` _+7 more__
- **2026-09-04** [`ba753a6f91`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba753a6f91) [#18498](https://github.com/NVIDIA/TensorRT-LLM/pull/18498)
  [None][feat] Add SM107 NVFP4 CuTe DSL fused MoE kernels and integration (#18498)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_finalize_fusion.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/inline_ptx.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_gather_grouped_blockscaled_gemm_act_fusion.py` _+16 more__
- **2026-09-04** [`c295dd9fca`](https://github.com/NVIDIA/TensorRT-LLM/commit/c295dd9fca) [#18675](https://github.com/NVIDIA/TensorRT-LLM/pull/18675)
  [https://nvbugs/6193837][fix] Include FINALIZE-fusion workspace for SM>=90 in the MoE autotuner (#18675)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`_
- **2026-09-04** [`02746c52d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/02746c52d0) [#18585](https://github.com/NVIDIA/TensorRT-LLM/pull/18585)
  [None][feat] add Qwen3.8-Flash-Next support (#18585)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/attention_backend/sparse/hooks.py`, `tensorrt_llm/_torch/attention_backend/sparse/qsa/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/qsa/backend.py` _+58 more__
- **2026-09-04** [`d773557c75`](https://github.com/NVIDIA/TensorRT-LLM/commit/d773557c75) [#17816](https://github.com/NVIDIA/TensorRT-LLM/pull/17816)
  [None][feat] Kimi k3 Support bcg (#17816)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+6 more__
- **2026-09-04** [`73a702ecf0`](https://github.com/NVIDIA/TensorRT-LLM/commit/73a702ecf0) [#17984](https://github.com/NVIDIA/TensorRT-LLM/pull/17984)
  [None][feat] Patch DeepEP Commit To Support TopK 16 (#17984)
  _Files: `3rdparty/fetch_content.json`, `tensorrt_llm/_torch/moe/fused_moe/communication/deep_ep_low_latency.py`, `tests/unittest/_torch/moe/test_moe_comm.py`_
- **2026-09-03** [`625a4727cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/625a4727cc) [#18625](https://github.com/NVIDIA/TensorRT-LLM/pull/18625)
  [None][fix] Self-sampling top-k drops +inf from the top-k (register family) (#18625)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_
- **2026-09-03** [`a6616d6f8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6616d6f8a) [#18520](https://github.com/NVIDIA/TensorRT-LLM/pull/18520)
  [https://nvbugs/5859751][fix] Reject NVFP4 MoE layers with unaligned gated FC1 (#18520)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/moe/fused_moe/impl_contract.py`, `tensorrt_llm/_torch/moe/fused_moe/moe_resolution.py` _+1 more__
- **2026-09-03** [`d13567c8fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/d13567c8fa) [#18410](https://github.com/NVIDIA/TensorRT-LLM/pull/18410)
  [None][feat] GVR V2 decode top-k goes hint-free by default: the bracket comes from the current row (#18410)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tensorrt_llm/_torch/modules/top_k.py` _+2 more__
- **2026-09-02** [`05b0324813`](https://github.com/NVIDIA/TensorRT-LLM/commit/05b0324813) [#18409](https://github.com/NVIDIA/TensorRT-LLM/pull/18409)
  [TRTLLM-14959][refactor] declare MoE backend capabilities instead of checking exact classes (#18409)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py` _+34 more__
- **2026-09-02** [`e5f853f5d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5f853f5d4) [#18369](https://github.com/NVIDIA/TensorRT-LLM/pull/18369)
  [None][feat] Add Rubin SM107 CuTe DSL foundation and BF16 kernels (#18369)
  _Files: `cpp/tensorrt_llm/thop/cuteDslMoeUtilsOp.cpp`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/custom_pipeline.py` _+19 more__
- **2026-09-02** [`ca38e9ee81`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca38e9ee81) [#16632](https://github.com/NVIDIA/TensorRT-LLM/pull/16632)
  [TRTLLM-14715][feat] preserve native MoE A2A graph VAs across restore (#16632)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/mnnvl_alltoall_workspace.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/communication/__init__.py` _+19 more__
- **2026-09-02** [`16354eefc3`](https://github.com/NVIDIA/TensorRT-LLM/commit/16354eefc3) [#16953](https://github.com/NVIDIA/TensorRT-LLM/pull/16953)
  [None][perf] Emission-assisted GVR top-K decode for the DeepSeek V4 indexer (#16953)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_emission.py` _+10 more__
- **2026-09-02** [`08cc1002cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/08cc1002cd) [#18501](https://github.com/NVIDIA/TensorRT-LLM/pull/18501)
  [None][fix] Enforce the count-crossing invariant in the self-sampling top-k register family (#18501)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py`, `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_
- **2026-09-02** [`84a59d6f17`](https://github.com/NVIDIA/TensorRT-LLM/commit/84a59d6f17) [#18322](https://github.com/NVIDIA/TensorRT-LLM/pull/18322)
  [https://nvbugs/6633931][fix] Chunk the MoE workspace on the SM90 branch of TestDeepSeekV32::test_fp8_blockscale (#18322)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-02** [`181f726d10`](https://github.com/NVIDIA/TensorRT-LLM/commit/181f726d10) [#17707](https://github.com/NVIDIA/TensorRT-LLM/pull/17707)
  [TRTLLM-15316][feat] Rubin trtllmgen batchedGemm MoE (#17707)
- **2026-09-01** [`e9376f8a9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9376f8a9b) [#18323](https://github.com/NVIDIA/TensorRT-LLM/pull/18323)
  [https://nvbugs/6633931][fix] Size the SM90 fp8 block-scale MoE workspace for the buffers it actually uses (#18323)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`_
- **2026-09-01** [`d70260a14b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d70260a14b) [#18285](https://github.com/NVIDIA/TensorRT-LLM/pull/18285)
  [TRTLLM-15800][feat] bench_moe: hybrid MoE TP x EP parallel modes (#18285)
  _Files: `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/case_runner.py`, `tests/microbenchmarks/bench_moe/cli.py`, `tests/microbenchmarks/bench_moe/mapping.py` _+4 more__
- **2026-08-31** [`f9d11b281a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9d11b281a) [#18344](https://github.com/NVIDIA/TensorRT-LLM/pull/18344)
  [https://nvbugs/6402009][test] unwaive Qwen3-235B NVFP4 TRTLLM MoE test (#18344)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`9332a81ce2`](https://github.com/NVIDIA/TensorRT-LLM/commit/9332a81ce2) [#18339](https://github.com/NVIDIA/TensorRT-LLM/pull/18339)
  [#18338][fix] Fix barrier-divergence races in the Blackwell CuTe DSL GVR top-k decode kernel (#18339)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_

## Quantization  (19 commits)

- **2026-09-07** [`6e8fe90078`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e8fe90078)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+2 more__
- **2026-09-07** [`774cfbbfcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/774cfbbfcf) [#18260](https://github.com/NVIDIA/TensorRT-LLM/pull/18260)
  [None][fix] validate the layer-wise replay request against the calibration before it runs (#18260)
  _Files: `examples/layer_wise_benchmarks/run.py`, `tensorrt_llm/tools/layer_wise_benchmarks/calibrator.py`, `tests/unittest/tools/test_layer_wise_benchmarks_calibrator.py`_
- **2026-09-05** [`4656c4b519`](https://github.com/NVIDIA/TensorRT-LLM/commit/4656c4b519) [#18674](https://github.com/NVIDIA/TensorRT-LLM/pull/18674)
  [https://nvbugs/6480110][fix] Fall back to FP8 KV cache when NVFP4 KV cache is requested on SM107 (#18674)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tests/unittest/_torch/test_model_config.py`_
- **2026-09-05** [`9964d34d67`](https://github.com/NVIDIA/TensorRT-LLM/commit/9964d34d67) [#18633](https://github.com/NVIDIA/TensorRT-LLM/pull/18633)
  [None][test] Add the 40-GPU AgentX DeepSeek-V4-Pro-DSpark case to post-merge and switch both cases to the NVFP4 checkpoint (#18633)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/test_lists/qa/llm_perf_multinode.txt` _+5 more__
- **2026-09-05** [`270e73cf9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/270e73cf9f) [#18546](https://github.com/NVIDIA/TensorRT-LLM/pull/18546)
  [None][feat] Add SM107 quantized dense and DSV4 CuTe DSL kernels (#18546)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.h`, `cpp/tensorrt_llm/thop/fp8Quantize.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+15 more__
- **2026-09-04** [`7b55291e55`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b55291e55)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock` _+7 more__
- **2026-09-03** [`4f5cc659b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f5cc659b4) [#18550](https://github.com/NVIDIA/TensorRT-LLM/pull/18550)
  [https://nvbugs/6655359][test] Shrink the Cosmos3-Nano T2V LPIPS gate to 9 frames, relax T2V/V2V thresholds, and unwaive (#18550)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_i2v_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_t2i_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_t2v_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_fp8_blockwise_lpips_golden.json` _+7 more__
- **2026-09-03** [`999acb64e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/999acb64e4) [#16847](https://github.com/NVIDIA/TensorRT-LLM/pull/16847)
  [TRTLLM-14616][feat] add VisualGen fp8 row-wise quant + autotuner (#16847)
  _Files: `cpp/tensorrt_llm/kernels/fp8PerTokenQuant/fp8_per_token_quant.cu`, `cpp/tensorrt_llm/kernels/fp8PerTokenQuant/fp8_per_token_quant.cuh`, `cpp/tensorrt_llm/kernels/fp8PerTokenQuant/vectorization.cuh`, `cpp/tensorrt_llm/kernels/fp8PerTokenQuant/vectorized_cub_helpers.h` _+20 more__
- **2026-09-03** [`f329d949c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/f329d949c3) [#18607](https://github.com/NVIDIA/TensorRT-LLM/pull/18607)
  [https://nvbugs/6563482][fix] Always exclude mamba conv1d from quantization (#18607)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`_
- **2026-09-03** [`4f14207271`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f14207271) [#18319](https://github.com/NVIDIA/TensorRT-LLM/pull/18319)
  [https://nvbugs/6566734][test] Unwaive test_disaggregated_qwen3_32b_fp8 and accept both greedy completions (#18319)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-03** [`7f2715520d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f2715520d) [#18526](https://github.com/NVIDIA/TensorRT-LLM/pull/18526)
  [TRTLLM-15821][feat] Enable Nemotron Super 3.5 VL NVFP4 variants (#18526)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/_torch/models/modeling_radio.py`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nano_v2_vl.py`_
- **2026-09-03** [`e3dd622744`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3dd622744)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+10 more__
- **2026-09-02** [`ef567dd9b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef567dd9b8) [#18387](https://github.com/NVIDIA/TensorRT-LLM/pull/18387)
  [None][fix] Fix Qwen3.8-27B NVFP4 checkpoint loading (#18387)
  _Files: `docs/source/deployment-guide/deployment-guide-for-qwen3.8-qwen3.5-on-trtllm.md`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/models/modeling_qwen_image_bench.py`, `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl.py` _+1 more__
- **2026-09-01** [`d147336b7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d147336b7a) [#17238](https://github.com/NVIDIA/TensorRT-LLM/pull/17238)
  [None][perf] Optimize MiniMax-M3 MXFP8 GEMMs (#17238)
  _Files: `cpp/tensorrt_llm/thop/mxfp8Gemm.cpp`, `docs/source/deployment-guide/deployment-guide-for-minimax-m3-on-trtllm.md`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+7 more__
- **2026-09-01** [`d717506e45`](https://github.com/NVIDIA/TensorRT-LLM/commit/d717506e45)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-08-31** [`b6cb3d6450`](https://github.com/NVIDIA/TensorRT-LLM/commit/b6cb3d6450) [#18363](https://github.com/NVIDIA/TensorRT-LLM/pull/18363)
  [None][infra] Add GB300 multi-node post-merge stages for Qwen3.8-2.4T-A95B NVFP4 accuracy (#18363)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_node2_gpu8.yml` _+1 more__
- **2026-08-31** [`acf1dad0bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/acf1dad0bb)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/longbench/poetry.lock`, `security_scanning/examples/longbench/pyproject.toml`, `security_scanning/examples/ngram/poetry.lock` _+8 more__
- **2026-08-31** [`0d4cf39e99`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d4cf39e99) [#18121](https://github.com/NVIDIA/TensorRT-LLM/pull/18121)
  [https://nvbugs/6633928][test] Unwaive Gemma3 FP8 accuracy test on H100 (#18121)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`c77f3196f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c77f3196f0) [#18304](https://github.com/NVIDIA/TensorRT-LLM/pull/18304)
  [https://nvbugs/6650388][chore] Unwaive TestDeepSeekV32 nvfp4 chunked_prefill and piecewise_cuda_graph on B200 (#18304)
  _Files: `tests/integration/test_lists/waives.txt`_

## Torch Path (_torch)  (15 commits)

- **2026-09-07** [`374df3c3c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/374df3c3c1) [#18715](https://github.com/NVIDIA/TensorRT-LLM/pull/18715)
  [https://nvbugs/6682352][fix] rebuild MNNVL communicator on layout change (#18715)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/test_mnnvl_memory_lifecycle.py`_
- **2026-09-05** [`515b984dc9`](https://github.com/NVIDIA/TensorRT-LLM/commit/515b984dc9) [#18463](https://github.com/NVIDIA/TensorRT-LLM/pull/18463)
  [None][feat] Add Cosmos3 Edge Policy DROID support (#18463)
  _Files: `.codex/skills/visual-gen-component-test/SKILL.md`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `examples/visual_gen/models/cosmos3/prompts/action_edge_policy_droid.json` _+19 more__
- **2026-09-04** [`12680fc00b`](https://github.com/NVIDIA/TensorRT-LLM/commit/12680fc00b) [#18681](https://github.com/NVIDIA/TensorRT-LLM/pull/18681)
  [None][refactor] Table-drive the lazy-safetensors model-type check in HfWeightLoader (#18681)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tests/unittest/_torch/models/checkpoints/hf/test_weight_loader.py`_
- **2026-09-04** [`b916389638`](https://github.com/NVIDIA/TensorRT-LLM/commit/b916389638) [#18642](https://github.com/NVIDIA/TensorRT-LLM/pull/18642)
  [https://nvbugs/6581049][fix] Slightly lower accuracy threshold (#18642)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`_
- **2026-09-04** [`eeaaf59f38`](https://github.com/NVIDIA/TensorRT-LLM/commit/eeaaf59f38) [#18470](https://github.com/NVIDIA/TensorRT-LLM/pull/18470)
  [None][test] validate GLM-5.2 feature support matrix (#18470)
  _Files: `docs/source/models/supported-models.md`, `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/test_glm52.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+3 more__
- **2026-09-03** [`a06c550a9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a06c550a9c) [#17788](https://github.com/NVIDIA/TensorRT-LLM/pull/17788)
  [TRTLLMINF-316][infra] Use authenticated token for GitHub fetch in docker image build (#17788)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `docker/common/github_auth.sh`, `docker/common/install_mooncake.sh` _+5 more__
- **2026-09-03** [`53bb31fdcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/53bb31fdcf) [#18635](https://github.com/NVIDIA/TensorRT-LLM/pull/18635)
  [None][fix] reject incompatible cached low-M GEMM tactics (#18635)
  _Files: `tensorrt_llm/_torch/modules/low_m_gemm.py`, `tests/unittest/_torch/modules/test_low_m_gemm.py`_
- **2026-09-03** [`6c7a90628e`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c7a90628e) [#18444](https://github.com/NVIDIA/TensorRT-LLM/pull/18444)
  [None][feat] Support response_format='path' on /v1/images/edits and report Server-Timing total (#18444)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/openai_video_routes.py`, `tests/unittest/_torch/visual_gen/test_trtllm_serve_endpoints.py`_
- **2026-09-02** [`30316da103`](https://github.com/NVIDIA/TensorRT-LLM/commit/30316da103) [#18331](https://github.com/NVIDIA/TensorRT-LLM/pull/18331)
  [TRTLLM-15316][feat] Fix fused mHC Phase-4 coherence and support uneven split-K (#18331)
  _Files: `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcFusedHcKernel.cu`, `tensorrt_llm/_torch/modules/mhc/mhc_cuda.py`, `tests/unittest/_torch/modules/test_mhc.py`_
- **2026-09-01** [`8cbfd0e7f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cbfd0e7f3) [#18209](https://github.com/NVIDIA/TensorRT-LLM/pull/18209)
  [https://nvbugs/6661914][fix] restore Wan 5B per-token AdaLN with TeaCache (#18209)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/transformer_wan.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/test_wan_timestep_routing.py`_
- **2026-09-01** [`5fb68830c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fb68830c9) [#18464](https://github.com/NVIDIA/TensorRT-LLM/pull/18464)
  [https://nvbugs/6699646][fix] Preserve prepared Cosmos3 video frames (#18464)
  _Files: `tensorrt_llm/_torch/models/modeling_cosmos3.py`, `tests/unittest/_torch/modeling/test_modeling_cosmos3.py`_
- **2026-09-01** [`6507185b02`](https://github.com/NVIDIA/TensorRT-LLM/commit/6507185b02) [#18466](https://github.com/NVIDIA/TensorRT-LLM/pull/18466)
  [None][fix] Support MiniMax-M3 vision meta init (#18466)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3_vl.py`, `tests/unittest/_torch/models/test_minimax_m3_vl.py`_
- **2026-09-01** [`12ec47588a`](https://github.com/NVIDIA/TensorRT-LLM/commit/12ec47588a) [#18370](https://github.com/NVIDIA/TensorRT-LLM/pull/18370)
  [TRTLLM-15820][feat] Enable Nemotron Super 3.5 VL video input (#18370)
  _Files: `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/_torch/models/modeling_radio.py`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nano_v2_vl.py`_
- **2026-09-01** [`07c5f2145a`](https://github.com/NVIDIA/TensorRT-LLM/commit/07c5f2145a) [#18081](https://github.com/NVIDIA/TensorRT-LLM/pull/18081)
  [None][perf] Convolve the Mamba2 prefill on a channel-last projection (#18081)
  _Files: `cpp/tensorrt_llm/kernels/causalConv1d/causalConv1d.cu`, `cpp/tensorrt_llm/kernels/causalConv1d/causalConv1d.h`, `cpp/tensorrt_llm/thop/causalConv1dOp.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+3 more__
- **2026-08-31** [`05bf7b4e8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/05bf7b4e8d) [#18328](https://github.com/NVIDIA/TensorRT-LLM/pull/18328)
  [https://nvbugs/6626445][fix] Narrow Wan2.2 I2V test fixture scope to reduce peak GPU memory (#18328)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/test_wan22_i2v_pipeline.py`_

## Other  (14 commits)

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
- **2026-09-04** [`23e5ff15f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/23e5ff15f7) [#18532](https://github.com/NVIDIA/TensorRT-LLM/pull/18532)
  [TRTLLM-15947][refactor] BREAKING: Remove C++ state left dead by the TRTLLMSampler removal (#18532)
- **2026-09-04** [`cf45d3ce8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf45d3ce8b) [#17884](https://github.com/NVIDIA/TensorRT-LLM/pull/17884)
  [None][test] Declarative extra import path for test sources (#17884)
- **2026-09-03** [`21fe7817a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/21fe7817a7) [#18591](https://github.com/NVIDIA/TensorRT-LLM/pull/18591)
  [None][test] check GitHub links in documentation (#18591)
  _Files: `tests/integration/defs/test_doc.py`_
- **2026-09-02** [`0699c4bedb`](https://github.com/NVIDIA/TensorRT-LLM/commit/0699c4bedb) [#17650](https://github.com/NVIDIA/TensorRT-LLM/pull/17650)
  [https://nvbugs/6467691][fix] Raise Starlette security floor (#17650)
  _Files: `constraints.txt`, `requirements.txt`, `tests/unittest/others/test_web_dependency_security.py`_
- **2026-09-02** [`9291052b4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/9291052b4f) [#18432](https://github.com/NVIDIA/TensorRT-LLM/pull/18432)
  [None][test] Enable warmup request for disagg e2e and ctx_only perf sanity lanes (#18432)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/tools/test_perf_sanity_matching.py`_
- **2026-09-01** [`f88f83b8ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/f88f83b8ba) [#18454](https://github.com/NVIDIA/TensorRT-LLM/pull/18454)
  [TRTLLM-12680][fix] stabilize telemetry lifecycle follow-ups (#18454)
  _Files: `tensorrt_llm/usage/__init__.py`, `tensorrt_llm/usage/schema.py`, `tensorrt_llm/usage/usage_lib.py`, `tests/unittest/usage/test_cli_telemetry.py` _+2 more__
- **2026-09-01** [`8355ecf7ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/8355ecf7ee) [#18233](https://github.com/NVIDIA/TensorRT-LLM/pull/18233)
  [TRTLLM-15405][refactor] Remove the C++ decoder stack behind TRTLLMSampler (#18233)

## Models  (12 commits)

- **2026-09-07** [`634a3ec273`](https://github.com/NVIDIA/TensorRT-LLM/commit/634a3ec273) [#18655](https://github.com/NVIDIA/TensorRT-LLM/pull/18655)
  [None][test] Add func and perf cases for Qwen3.6-35B-A3B and gemma4 on Spark (#18655)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py` _+4 more__
- **2026-09-05** [`709dd417f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/709dd417f1) [#18682](https://github.com/NVIDIA/TensorRT-LLM/pull/18682)
  [https://nvbugs/6707518][fix] Fix Kimi K3 spec dec test (#18682)
  _Files: `tests/integration/defs/kimi_k3_sa_harness.py`, `tests/integration/defs/test_kimi_k3_specdec.py`_
- **2026-09-04** [`dec2efcf06`](https://github.com/NVIDIA/TensorRT-LLM/commit/dec2efcf06) [#18643](https://github.com/NVIDIA/TensorRT-LLM/pull/18643)
  [None][perf] Give the K3 KDA prefill conv input its layout without a repack (#18643)
  _Files: `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`_
- **2026-09-03** [`b2cb0cdc04`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2cb0cdc04) [#18606](https://github.com/NVIDIA/TensorRT-LLM/pull/18606)
  [https://nvbugs/6693811][test] Unwaive DeepSeek V3 Lite guided decoding (#18606)
- **2026-09-03** [`cd5d04759f`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd5d04759f) [#18503](https://github.com/NVIDIA/TensorRT-LLM/pull/18503)
  [https://nvbugs/6693811][test] Unwaive DeepSeekV3Lite disagg guided_decoding mtp test (#18503)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-02** [`0c30590bbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c30590bbd) [#18491](https://github.com/NVIDIA/TensorRT-LLM/pull/18491)
  [None][test] Add coverage for KimiLinearForCausalLM._setup_helix_mappings and related paths (#18491)
  _Files: `tests/unittest/_torch/modeling/test_kimi_linear_helix_mappings.py`_
- **2026-09-02** [`16881d4fa8`](https://github.com/NVIDIA/TensorRT-LLM/commit/16881d4fa8) [#18251](https://github.com/NVIDIA/TensorRT-LLM/pull/18251)
  [TRTLLM-15498][perf] optimize Kimi KDA decode data flow (#18251)
  _Files: `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.cu`, `cpp/tensorrt_llm/kernels/kdaDecode/kdaDecode.h`, `cpp/tensorrt_llm/thop/kdaDecodeOp.cpp`, `tensorrt_llm/_torch/modules/kimi_kda/_kda_decode.py` _+4 more__
- **2026-09-02** [`f03e77196e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f03e77196e) [#18511](https://github.com/NVIDIA/TensorRT-LLM/pull/18511)
  [None][test] Unwaive qwen3.5 test cases (#18511)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`1c7d1c0a31`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c7d1c0a31) [#18549](https://github.com/NVIDIA/TensorRT-LLM/pull/18549)
  [https://nvbugs/6705034][test] waive Kimi KDA empty prefill test on B200 (#18549)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-01** [`75593a2f98`](https://github.com/NVIDIA/TensorRT-LLM/commit/75593a2f98) [#18199](https://github.com/NVIDIA/TensorRT-LLM/pull/18199)
  [TRTLLM-11446][feat] trtllm-eval visual-gen generation evaluation pipeline (#18199)
  _Files: `tensorrt_llm/commands/eval.py`, `tensorrt_llm/evaluate/__init__.py`, `tensorrt_llm/evaluate/image_generation_eval.py`, `tensorrt_llm/evaluate/visual_gen/__init__.py` _+11 more__
- **2026-09-01** [`99395c5fb2`](https://github.com/NVIDIA/TensorRT-LLM/commit/99395c5fb2) [#18324](https://github.com/NVIDIA/TensorRT-LLM/pull/18324)
  [https://nvbugs/6384357][test] Unwaive DeepSeek-V3.2 DSA host cache offload mtp params (#18324)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`5b32a5f785`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b32a5f785) [#18458](https://github.com/NVIDIA/TensorRT-LLM/pull/18458)
  [https://nvbugs/6698722][test] Waive Gemma3 1B disagg KV-cache-v2 NIXL flaky test (#18458)
  _Files: `tests/integration/test_lists/waives.txt`_

## Docs / Examples  (10 commits)

- **2026-09-06** [`15580f8ddd`](https://github.com/NVIDIA/TensorRT-LLM/commit/15580f8ddd) [#18500](https://github.com/NVIDIA/TensorRT-LLM/pull/18500)
  [https://nvbugs/6676352][doc] Fix missing backslash in prepare-dataset command block (#18500)
  _Files: `docs/source/developer-guide/perf-benchmarking.md`, `examples/llm-api/out_of_tree_example/readme.md`_
- **2026-09-03** [`6b1b4cd3cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b1b4cd3cd) [#18626](https://github.com/NVIDIA/TensorRT-LLM/pull/18626)
  [None][doc] Fix stale Wide-EP EPLB documentation (#18626)
  _Files: `examples/wide_ep/README.md`, `examples/wide_ep/ep_load_balancer/README.md`, `examples/wide_ep/slurm_scripts/README.md`_
- **2026-09-03** [`61a6ca83f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/61a6ca83f3) [#18179](https://github.com/NVIDIA/TensorRT-LLM/pull/18179)
  [https://nvbugs/6646568][chore] Make DeepGEMM in-kernel barrier timeout configurable (#18179)
  _Files: `3rdparty/fetch_content.json`, `3rdparty/patches/deepgemm_configurable_barrier_timeout.patch`, `docs/source/developer-guide/overview.md`_
- **2026-09-02** [`5313446ac6`](https://github.com/NVIDIA/TensorRT-LLM/commit/5313446ac6) [#18440](https://github.com/NVIDIA/TensorRT-LLM/pull/18440)
  [None][doc] Split LLM API reference into smaller searchable pages (#18440)
  _Files: `docs/source/conf.py`, `docs/source/helper.py`_
- **2026-09-01** [`de57b1eaf6`](https://github.com/NVIDIA/TensorRT-LLM/commit/de57b1eaf6) [#18434](https://github.com/NVIDIA/TensorRT-LLM/pull/18434)
  [None][feat] Add perf-analyze and perf-optimize skills to agent-flow (#18434)
  _Files: `agent-flow/.claude/skills/perf-analyze/SKILL.md`, `agent-flow/.claude/skills/perf-optimize/SKILL.md`, `agent-flow/agent_flow/workflows/perf_optimize/README.md`_
- **2026-08-31** [`aada22672b`](https://github.com/NVIDIA/TensorRT-LLM/commit/aada22672b) [#18429](https://github.com/NVIDIA/TensorRT-LLM/pull/18429)
  [https://nvbugs/6676066][doc] Clone examples/llm-api before running the multimodal quick start (#18429)
  _Files: `docs/source/features/multi-modality.md`_
- **2026-08-31** [`c28bd30d40`](https://github.com/NVIDIA/TensorRT-LLM/commit/c28bd30d40) [#18431](https://github.com/NVIDIA/TensorRT-LLM/pull/18431)
  [https://nvbugs/6676032][doc] Give a runnable lm_eval install command in the trtllm-eval guide (#18431)
  _Files: `docs/source/commands/trtllm-eval.rst`_
- **2026-08-31** [`5d979ef817`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d979ef817) [#18427](https://github.com/NVIDIA/TensorRT-LLM/pull/18427)
  [None][doc] Remove invalid html_inline entry from myst_enable_extensions (#18427)
  _Files: `docs/source/conf.py`_
- **2026-08-31** [`12f5545729`](https://github.com/NVIDIA/TensorRT-LLM/commit/12f5545729) [#18402](https://github.com/NVIDIA/TensorRT-LLM/pull/18402)
  [None][chore] Bump version to 1.3.0rc26 (#18402)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-08-31** [`3d2b26e570`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d2b26e570) [#18408](https://github.com/NVIDIA/TensorRT-LLM/pull/18408)
  [None][test] key perf-sanity case identity on test case name (#18408)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/perf_regression_utils.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/test_common/perf_sanity_matching.py` _+2 more__

## Speculative Decoding  (8 commits)

- **2026-09-04** [`22b7fdf351`](https://github.com/NVIDIA/TensorRT-LLM/commit/22b7fdf351) [#18647](https://github.com/NVIDIA/TensorRT-LLM/pull/18647)
  [TRTLLM-15822][feat] Forward speculative-decoding state through the Nemotron VL wrapper (#18647)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nano_v2_vl.py`_
- **2026-09-03** [`5418d2205d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5418d2205d) [#16873](https://github.com/NVIDIA/TensorRT-LLM/pull/16873)
  [None][perf] serve: always use msgspec msgpack for disagg orchestrator->worker body (#16873)
  _Files: `docs/source/blogs/tech_blog/blog26_DeepSeek_V4_on_NVIDIA_Blackwell_Model_Specific_and_Agentic_Workload_Optimizations_in_TensorRT-LLM.md`, `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_server.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+6 more__
- **2026-09-03** [`75ca0821c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/75ca0821c0) [#18459](https://github.com/NVIDIA/TensorRT-LLM/pull/18459)
  [None][fix] Support fixed-only draft KV cache budgets (#18459)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/unittest/_torch/executor/test_kv_cache_budget_split.py` _+1 more__
- **2026-09-03** [`90893b87a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/90893b87a5) [#18533](https://github.com/NVIDIA/TensorRT-LLM/pull/18533)
  [None][chore] Remove unused KV cache draft-token rewind helpers (#18533)
  _Files: `cpp/tensorrt_llm/kernels/speculativeDecoding/kvCacheUpdateKernels.cu`, `cpp/tensorrt_llm/kernels/speculativeDecoding/kvCacheUpdateKernels.h`_
- **2026-09-01** [`e00d95fa4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e00d95fa4c) [#18295](https://github.com/NVIDIA/TensorRT-LLM/pull/18295)
  [None][fix] use prompt lookahead for MTP Eagle chunked prefill (#18295)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tensorrt_llm/_torch/speculative/mtp_dynamic_tree.py` _+3 more__
- **2026-09-01** [`0f94be2600`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f94be2600) [#17921](https://github.com/NVIDIA/TensorRT-LLM/pull/17921)
  [TRTLLM-15035][test] Wire Kimi K3 spec-dec and suffix-automaton tests into L0 CI (#17921)
  _Files: `tests/integration/defs/kimi_k3_disagg_parity.py`, `tests/integration/defs/test_kimi_k3_specdec.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+2 more__
- **2026-09-01** [`22e4cbc3bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/22e4cbc3bf) [#18401](https://github.com/NVIDIA/TensorRT-LLM/pull/18401)
  [https://nvbugs/6676511][fix] Reject unsupported speculative outputs (#18401)
  _Files: `tensorrt_llm/_torch/speculative/spec_sampler_base.py`, `tests/unittest/llmapi/test_sampling_params.py`_
- **2026-08-31** [`36808bd812`](https://github.com/NVIDIA/TensorRT-LLM/commit/36808bd812) [#18416](https://github.com/NVIDIA/TensorRT-LLM/pull/18416)
  [None][test] Add MiniMax-M3 disaggregated perf recipes to QA multi-node list (#18416)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep16_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep8_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tep2_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml` _+1 more__

## ROCm / AMD  (2 commits)

- **2026-09-07** [`5fa39642b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/5fa39642b9) [#18699](https://github.com/NVIDIA/TensorRT-LLM/pull/18699)
  [None][test] add Kimi K3 feature matrix coverage (#18699)
  _Files: `docs/source/models/supported-models.md`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/test_glm52.py`, `tests/integration/defs/accuracy/test_kimi3.py` _+2 more__
- **2026-09-03** [`fd79a3db6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd79a3db6e) [#17720](https://github.com/NVIDIA/TensorRT-LLM/pull/17720)
  [None][fix] Guard Python KV receive ownership and publication (#17720)
  _Files: `tensorrt_llm/_torch/disaggregation/native/bounce/core.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py` _+4 more__

## LoRA  (2 commits)

- **2026-09-06** [`a5f8680e41`](https://github.com/NVIDIA/TensorRT-LLM/commit/a5f8680e41) [#18652](https://github.com/NVIDIA/TensorRT-LLM/pull/18652)
  [TRTLLM-15752][refactor] Extract LoRA parameter construction into engine/lora.py (#18652)
  _Files: `tensorrt_llm/_torch/pyexecutor/engine/lora.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/engine/__init__.py`, `tests/unittest/_torch/executor/engine/test_lora.py`_
- **2026-09-02** [`d0bb5cee94`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0bb5cee94) [#17315](https://github.com/NVIDIA/TensorRT-LLM/pull/17315)
  [TRTLLM-14867][feat] Auto-tuning for split-K in LoRA grouped GEMM (#17315)
  _Files: `tensorrt_llm/_torch/peft/lora/layer.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/peft/test_lora_autotuner.py`_

## AutoDeploy  (2 commits)

- **2026-09-02** [`08ebfb8dd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/08ebfb8dd9) [#18572](https://github.com/NVIDIA/TensorRT-LLM/pull/18572)
  [None][chore] Remove AutoDeploy (ad-) skills and agents (#18572)
  _Files: `.claude/README.md`, `.claude/agents/ad-conf-check-update.md`, `.claude/agents/ad-debug-agent.md`, `.claude/agents/ad-onboard-reviewer.md` _+18 more__
- **2026-08-31** [`db1ce32d0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/db1ce32d0d) [#18422](https://github.com/NVIDIA/TensorRT-LLM/pull/18422)
  [TRTLLM-15883][infra] clarify CBTS fallback diagnostics (#18422)
  _Files: `jenkins/scripts/cbts/coverage_selection/artifact.py`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/_helpers.py`, `jenkins/scripts/cbts/rules/auto_deploy_rule.py` _+5 more__

---
_Generated 2026-09-07 14:16 UTC_