# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-09-14 → 2026-09-21  |  **Total commits:** 260

## ✨ New Features This Week

- **2026-09-21** [#19040](https://github.com/NVIDIA/TensorRT-LLM/pull/19040) — [TRTLLM-16564][feat] MLA-backboned standalone DSpark drafter (Inferact/Kimi-K3-DSpark) (#19040)
- **2026-09-21** [#19323](https://github.com/NVIDIA/TensorRT-LLM/pull/19323) — [None][feat] Support the MegaMoE CuteDSL MoE backend for Qwen3.8-Flash-Next (#19323)
- **2026-09-21** [#19413](https://github.com/NVIDIA/TensorRT-LLM/pull/19413) — [https://nvbugs/6759021][test] Re-enable disagg single-GPU tests for the MPI orchestrator (#19413)
- **2026-09-21** [#18397](https://github.com/NVIDIA/TensorRT-LLM/pull/18397) — [None][feat] Router Replay (R3): return per-token MoE routing to training engine in post train. (#18397)
- **2026-09-21** [#18939](https://github.com/NVIDIA/TensorRT-LLM/pull/18939) — [TRTLLM-13662][feat] transceiver enhancement (#18939)
- **2026-09-21** [#19332](https://github.com/NVIDIA/TensorRT-LLM/pull/19332) — [None][test] Add coverage for DeepseekV32ForCausalLM (#19332)
- **2026-09-21** [#19138](https://github.com/NVIDIA/TensorRT-LLM/pull/19138) — [None][feat] enable the GVR Top-K and MTP draft-loop index reuse for the QSA indexer (#19138)
- **2026-09-21** [#19256](https://github.com/NVIDIA/TensorRT-LLM/pull/19256) — [None][test] Add coverage for WhisperForConditionalGeneration (#19256)
- **2026-09-20** [#18689](https://github.com/NVIDIA/TensorRT-LLM/pull/18689) — [None][feat] Add NCCL-EP 0.2 low-latency integration (#18689)
- **2026-09-20** [#19162](https://github.com/NVIDIA/TensorRT-LLM/pull/19162) — [None][feat] FlashInfer: TRTLLM_FI_DECODE_TENSOR_CORES override; autotuner: log every candidate (#19162)
- _…and 57 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-17** [`1009588222`](https://github.com/NVIDIA/TensorRT-LLM/commit/1009588222) [#19046](https://github.com/NVIDIA/TensorRT-LLM/pull/19046) — [None][test] verify model feature matrix support (#19046)
- **2026-09-17** [`ec22079fbf`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec22079fbf) [#19198](https://github.com/NVIDIA/TensorRT-LLM/pull/19198) — [TRTLLM-16186][feat] Route native KV transfer through a shared backend contract (#19198)
- **2026-09-17** [`e76ada4478`](https://github.com/NVIDIA/TensorRT-LLM/commit/e76ada4478) [#19266](https://github.com/NVIDIA/TensorRT-LLM/pull/19266) — [TRTLLM-15716][refactor] Extract receive start/tail and admission into DisaggTransferCoordinator (#19266)
- **2026-09-16** [`6882e320e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/6882e320e8) [#19084](https://github.com/NVIDIA/TensorRT-LLM/pull/19084) — [https://nvbugs/6656598][tests] Deprecate K2 E2E test for K3 (#19084)
- **2026-09-16** [`82d667fbfb`](https://github.com/NVIDIA/TensorRT-LLM/commit/82d667fbfb) [#18743](https://github.com/NVIDIA/TensorRT-LLM/pull/18743) — [TRTLLMINF-445][infra] Upgrade public torch to 2.13.0 and triton to 3.7.1 (#18743)
- **2026-09-15** [`a494ef678a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a494ef678a) [#18461](https://github.com/NVIDIA/TensorRT-LLM/pull/18461) — [TRTLLM-16020][test] Add Kimi K3 GSM8K accuracy tests to GB300 multi-node post-merge CI (#18461)
- **2026-09-15** [`6cae275f16`](https://github.com/NVIDIA/TensorRT-LLM/commit/6cae275f16) [#19128](https://github.com/NVIDIA/TensorRT-LLM/pull/19128) — [TRTLLM-15715][refactor] Extract progress polling and error consensus into DisaggTransferCoordinator (#19128)
- **2026-09-14** [`858a360ffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/858a360ffe) [#18861](https://github.com/NVIDIA/TensorRT-LLM/pull/18861) — [None][chore] Refine QA code ownership (#18861)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-09-21 |
| [#19232](https://github.com/NVIDIA/TensorRT-LLM/issues/19232) | [RFC]: Disaggregated request preprocessing | triaged, Investigating, LLM API, Disaggregated serving, RFC, Frontend | 2026-09-16 |
| [#19242](https://github.com/NVIDIA/TensorRT-LLM/issues/19242) | [Bug]: KVCacheBlock and its radix tree LookupNode own each other with  | KV-Cache Management | 2026-09-16 |
| [#19240](https://github.com/NVIDIA/TensorRT-LLM/issues/19240) | [Bug]: mixtureOfExpertsTest crashes with SEGV when a parameter set has | Customized kernels | 2026-09-16 |
| [#19059](https://github.com/NVIDIA/TensorRT-LLM/issues/19059) | [Bug]: C++17 build cannot compile torch 2.12 headers with nvcc, but C+ | Pytorch | 2026-09-15 |
| [#19172](https://github.com/NVIDIA/TensorRT-LLM/issues/19172) | [Bug]: Async prompt-embedding H2D outlives its pooled-pinned source; t | bug, Triton backend, Inference runtime | 2026-09-14 |
| [#19067](https://github.com/NVIDIA/TensorRT-LLM/issues/19067) | [Bug]: -a 107-real is silently folded to 100, no SM107 code is generat | Infra | 2026-09-11 |
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

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 56 |
| Attention | 54 |
| MoE | 34 |
| Executor / Runtime | 27 |
| Torch Path (_torch) | 19 |
| Disaggregation / KV | 19 |
| Speculative Decoding | 11 |
| Other | 10 |
| Quantization | 9 |
| ROCm / AMD | 8 |
| Models | 5 |
| Docs / Examples | 4 |
| AutoDeploy | 2 |
| Compilation / Graph | 1 |
| Perf | 1 |

## CI / Infra  (56 commits)

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
- **2026-09-20** [`82d1cb46bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/82d1cb46bd) [#19453](https://github.com/NVIDIA/TensorRT-LLM/pull/19453)
  [None][infra] Waive 2 failed cases for main in pre-merge 61410 (#19453)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-19** [`66a447dc59`](https://github.com/NVIDIA/TensorRT-LLM/commit/66a447dc59) [#19299](https://github.com/NVIDIA/TensorRT-LLM/pull/19299)
  [TRTLLMINF-443][infra] Disable agg c1024 from BOLT profile gen (#19299)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-18** [`6db9b8cb53`](https://github.com/NVIDIA/TensorRT-LLM/commit/6db9b8cb53) [#19294](https://github.com/NVIDIA/TensorRT-LLM/pull/19294)
  [https://nvbugs/6758881][chore] unwaive bart test (#19294)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`e1b6d3a0e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1b6d3a0e2) [#19368](https://github.com/NVIDIA/TensorRT-LLM/pull/19368)
  [https://nvbugs/6782271][fix] Unwaive GLM perf sanity (#19368)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`d4a04b14c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4a04b14c0) [#19381](https://github.com/NVIDIA/TensorRT-LLM/pull/19381)
  [None][ci] waive pre-existing test failures on main (#19381)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`da7e141302`](https://github.com/NVIDIA/TensorRT-LLM/commit/da7e141302) [#19420](https://github.com/NVIDIA/TensorRT-LLM/pull/19420)
  [https://nvbugs/6627795][fix] Remove stale GB200 context-only test waiver (#19420)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`52a2538714`](https://github.com/NVIDIA/TensorRT-LLM/commit/52a2538714) [#19415](https://github.com/NVIDIA/TensorRT-LLM/pull/19415)
  [None][test] Waive 1 failed cases for main in QA CI (#19415)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`ff310b6e34`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff310b6e34) [#19414](https://github.com/NVIDIA/TensorRT-LLM/pull/19414)
  [None][test] Waive 1 failed cases for main in QA CI (#19414)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`e6f0e41e64`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6f0e41e64) [#19248](https://github.com/NVIDIA/TensorRT-LLM/pull/19248)
  [TRTLLMINF-401][infra] Derive the DLFW wheel local version from the container (#19248)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-18** [`dcc95a8bf5`](https://github.com/NVIDIA/TensorRT-LLM/commit/dcc95a8bf5) [#19408](https://github.com/NVIDIA/TensorRT-LLM/pull/19408)
  [None][test] Waive 7 failed cases for main in QA CI (#19408)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`e9e6d064bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9e6d064bb) [#19393](https://github.com/NVIDIA/TensorRT-LLM/pull/19393)
  [None][infra] Waive 1 failed cases for main in post-merge 2966 (#19393)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`fd39e00a88`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd39e00a88) [#19386](https://github.com/NVIDIA/TensorRT-LLM/pull/19386)
  [None][infra] Waive 1 failed cases for main in pre-merge 61063 (#19386)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-18** [`8c51838263`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c51838263) [#18814](https://github.com/NVIDIA/TensorRT-LLM/pull/18814)
  [None][infra] add CBTS coverage shadow-run framework (#18814)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/tools/report_cbts_decision.py`, `tests/unittest/scripts/test_cbts.py`_
- **2026-09-17** [`d9685a827d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9685a827d) [#19374](https://github.com/NVIDIA/TensorRT-LLM/pull/19374)
  [None][infra] Waive 1 failed cases for main in pre-merge 60787 (#19374)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`00f0cf086e`](https://github.com/NVIDIA/TensorRT-LLM/commit/00f0cf086e) [#19357](https://github.com/NVIDIA/TensorRT-LLM/pull/19357)
  [None][infra] Waive 2 failed cases for main in pre-merge 60901 (#19357)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`8e37c36c18`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e37c36c18) [#19356](https://github.com/NVIDIA/TensorRT-LLM/pull/19356)
  [None][infra] Waive 2 failed cases for main in pre-merge 60889 (#19356)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`d93841f8d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/d93841f8d6) [#19124](https://github.com/NVIDIA/TensorRT-LLM/pull/19124)
  [TRTLLM-16315][infra] add Python change reference analysis for CBTS (#19124)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/coverage_selection/SELECTION.md`, `jenkins/scripts/cbts/coverage_selection/qualname_map.py`, `jenkins/scripts/cbts/coverage_selection/selector.py` _+7 more__
- **2026-09-17** [`4b0d10116a`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b0d10116a) [#19343](https://github.com/NVIDIA/TensorRT-LLM/pull/19343)
  [None][infra] Waive 1 failed cases for main in pre-merge 60861 (#19343)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`9d0a78836c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d0a78836c) [#19342](https://github.com/NVIDIA/TensorRT-LLM/pull/19342)
  [None][infra] Waive 1 failed cases for main in pre-merge 60861 (#19342)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`2b03049bba`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b03049bba) [#19276](https://github.com/NVIDIA/TensorRT-LLM/pull/19276)
  [None][infra] Waive 1 failed cases for main in pre-merge 60603 (#19276)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`b941c5c15e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b941c5c15e) [#19328](https://github.com/NVIDIA/TensorRT-LLM/pull/19328)
  [None][infra] Waive 1 failed cases for main in pre-merge 60806 (#19328)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`c4168f4851`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4168f4851) [#19129](https://github.com/NVIDIA/TensorRT-LLM/pull/19129)
  [nvbugs/6770503][fix] Update perf sanity helper unit tests to match #18990 renames (#19129)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/scripts/test_perf_sanity_helpers.py`_
- **2026-09-17** [`85269b5e0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/85269b5e0e) [#19321](https://github.com/NVIDIA/TensorRT-LLM/pull/19321)
  [None][test] Waive 1 failed cases for main in QA CI (#19321)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`e2b7d18daa`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2b7d18daa) [#19215](https://github.com/NVIDIA/TensorRT-LLM/pull/19215)
  [None][infra] Add blossom-ci authorized users (#19215)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-09-17** [`176ef4acc4`](https://github.com/NVIDIA/TensorRT-LLM/commit/176ef4acc4) [#19314](https://github.com/NVIDIA/TensorRT-LLM/pull/19314)
  [None][test] Waive 3 failed cases for main in QA CI (#19314)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`15056d7ce7`](https://github.com/NVIDIA/TensorRT-LLM/commit/15056d7ce7) [#19165](https://github.com/NVIDIA/TensorRT-LLM/pull/19165)
  [None][infra] Cancel slurm job if no new log after in 2 hours (#19165)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-09-16** [`fffdfba727`](https://github.com/NVIDIA/TensorRT-LLM/commit/fffdfba727)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-09-16** [`29ae4b6dfe`](https://github.com/NVIDIA/TensorRT-LLM/commit/29ae4b6dfe) [#19271](https://github.com/NVIDIA/TensorRT-LLM/pull/19271)
  [None][infra] Waive 2 failed cases for main in pre-merge 60635 (#19271)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`58b5c92687`](https://github.com/NVIDIA/TensorRT-LLM/commit/58b5c92687) [#19263](https://github.com/NVIDIA/TensorRT-LLM/pull/19263)
  [None][infra] Waive 1 failed cases for main in post-merge 2963 (#19263)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`d1166c722a`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1166c722a) [#18951](https://github.com/NVIDIA/TensorRT-LLM/pull/18951)
  [TRTLLMINF-346][fix] add internal Git fallback for PR diffs (#18951)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-09-16** [`7659ee0fb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7659ee0fb8) [#19257](https://github.com/NVIDIA/TensorRT-LLM/pull/19257)
  [None][infra] Waive 1 failed cases for main in post-merge 2962 (#19257)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`3ebca8be84`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ebca8be84) [#19252](https://github.com/NVIDIA/TensorRT-LLM/pull/19252)
  [None][test] Waive 3 failed cases for main in QA CI (#19252)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`9fe7ae1f9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fe7ae1f9c) [#19247](https://github.com/NVIDIA/TensorRT-LLM/pull/19247)
  [None][test] Waive 2 failed cases for main in QA CI (#19247)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-15** [`57d44ddf64`](https://github.com/NVIDIA/TensorRT-LLM/commit/57d44ddf64) [#19200](https://github.com/NVIDIA/TensorRT-LLM/pull/19200)
  [TRTLLMINF-434][infra] Fix confidentiality scan argument overflow (#19200)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-09-15** [`e5bc60d08e`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5bc60d08e) [#18628](https://github.com/NVIDIA/TensorRT-LLM/pull/18628)
  [TRTLLM-10804][infra] Support DLFW wheels in release (#18628)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/repack_wheel.py`_
- **2026-09-15** [`2c19ca6d7c`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c19ca6d7c) [#19196](https://github.com/NVIDIA/TensorRT-LLM/pull/19196)
  [None][ci] waive pre-existing test failures on main (#19196)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-15** [`0beff32139`](https://github.com/NVIDIA/TensorRT-LLM/commit/0beff32139) [#18615](https://github.com/NVIDIA/TensorRT-LLM/pull/18615)
  [TRTLLMINF-336][infra] BoltProfileGen: publish the BOLTed build as canonical (default off) (#18615)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-09-15** [`924b625a05`](https://github.com/NVIDIA/TensorRT-LLM/commit/924b625a05) [#19167](https://github.com/NVIDIA/TensorRT-LLM/pull/19167)
  [https://nvbugs/5838199][infra] Waive test_cache_transceiver[8proc-nixl_kvcache-90] (#19167)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-15** [`c10d6efb70`](https://github.com/NVIDIA/TensorRT-LLM/commit/c10d6efb70)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
- **2026-09-15** [`63d217f252`](https://github.com/NVIDIA/TensorRT-LLM/commit/63d217f252) [#19116](https://github.com/NVIDIA/TensorRT-LLM/pull/19116)
  [None][test] Remove 59 closed-bug waive entries for main (#19116)
  _Files: `tests/integration/test_lists/waives.txt`_
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

## Attention  (54 commits)

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
- **2026-09-20** [`d9194e202b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9194e202b) [#19385](https://github.com/NVIDIA/TensorRT-LLM/pull/19385)
  [TRTLLM-16498][fix] Avoid full KV pool casts in Triton prefill (#19385)
  _Files: `tensorrt_llm/_torch/attention/backends/triton_prefill.py`, `tests/unittest/_torch/attention/test_triton_prefill.py`_
- **2026-09-20** [`8c891a851e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c891a851e) [#19264](https://github.com/NVIDIA/TensorRT-LLM/pull/19264)
  [TRTLLM-16464][fix] Size RocketKV KT cache using local KV heads (#19264)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/rocket/cache_manager.py`, `tests/unittest/_torch/attention/sparse/rocketkv/test_cache_manager.py`_
- **2026-09-20** [`63e64e5bdb`](https://github.com/NVIDIA/TensorRT-LLM/commit/63e64e5bdb) [#19162](https://github.com/NVIDIA/TensorRT-LLM/pull/19162)
  [None][feat] FlashInfer: TRTLLM_FI_DECODE_TENSOR_CORES override; autotuner: log every candidate (#19162)
  _Files: `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/autotuner.py`, `tests/unittest/_torch/attention/test_flashinfer_decode_tensor_cores.py`, `tests/unittest/_torch/misc/test_autotuner.py`_
- **2026-09-20** [`bfde67fce1`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfde67fce1)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+12 more__
- **2026-09-20** [`07dbde4823`](https://github.com/NVIDIA/TensorRT-LLM/commit/07dbde4823) [#19220](https://github.com/NVIDIA/TensorRT-LLM/pull/19220)
  [https://nvbugs/6672360][fix] Stabilize XQA attention sink normalization (#19220)
  _Files: `cpp/kernels/xqa/mha.cu`_
- **2026-09-19** [`c9b4c867b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9b4c867b1) [#19354](https://github.com/NVIDIA/TensorRT-LLM/pull/19354)
  [None][fix] Convert the DFlash capture tap to the buffer dtype (#19354)
  _Files: `tensorrt_llm/_torch/speculative/dflash.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dflash_capture_dtype.py`_
- **2026-09-19** [`a1c6c2b36c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1c6c2b36c) [#19372](https://github.com/NVIDIA/TensorRT-LLM/pull/19372)
  [https://nvbugs/6601633][fix] Add an SM100-family JIT target for MSA (#19372)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`, `tests/unittest/_torch/attention/sparse/msa/test_msa_backend.py`_
- **2026-09-19** [`2c1d5f183f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c1d5f183f) [#19410](https://github.com/NVIDIA/TensorRT-LLM/pull/19410)
  [None][fix] Avoid unused DFlash draft KV cache managers (#19410)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_dflash_draft_kv.py`_
- **2026-09-19** [`c6228ab50e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c6228ab50e) [#19365](https://github.com/NVIDIA/TensorRT-LLM/pull/19365)
  [https://nvbugs/6776338][fix] Run legacy fmha_v2 on the SM100 family (incl. SM107) instead of aborting (#19365)
  _Files: `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fmhaRunner.cpp`_
- **2026-09-19** [`85f5605ce8`](https://github.com/NVIDIA/TensorRT-LLM/commit/85f5605ce8) [#18329](https://github.com/NVIDIA/TensorRT-LLM/pull/18329)
  [TRTLLM-15917][feat] Integrate Sol-Attn sparse attention into VisualGen (#18329)
  _Files: `.pre-commit-config.yaml`, `3rdparty/vendor_patches/sana-sol-attn.patch`, `3rdparty/vendor_sources.lock.yaml`, `docs/source/features/visualgen-sparse-attention.md` _+36 more__
- **2026-09-19** [`5a8741084f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a8741084f) [#19024](https://github.com/NVIDIA/TensorRT-LLM/pull/19024)
  [None][feat] Enable 2:4 activation-sparsity FMHA on SM107 (#19024)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionOp.h`, `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/fused_multihead_attention_common.h`, `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp` _+9 more__
- **2026-09-18** [`c2126fdf06`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2126fdf06) [#19291](https://github.com/NVIDIA/TensorRT-LLM/pull/19291)
  [None][perf] specialize NVFP4 MLA context gather for residual layout (#19291)
  _Files: `cpp/tensorrt_llm/kernels/nvfp4MlaKvCacheGather.cu`, `tests/unittest/_torch/attention/sparse/dsa/test_cpp_custom_ops.py`_
- **2026-09-18** [`f9e3e06ee7`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9e3e06ee7) [#19284](https://github.com/NVIDIA/TensorRT-LLM/pull/19284)
  [None][chore] Clarify phased FMHA inputs and outputs (#19284)
  _Files: `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/attention/backends/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py` _+15 more__
- **2026-09-18** [`c5c839308f`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5c839308f) [#19159](https://github.com/NVIDIA/TensorRT-LLM/pull/19159)
  [TRTLLM-16403][chore] Add more dflash 2 tests (#19159)
  _Files: `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml` _+5 more__
- **2026-09-18** [`4bbe1af658`](https://github.com/NVIDIA/TensorRT-LLM/commit/4bbe1af658) [#19070](https://github.com/NVIDIA/TensorRT-LLM/pull/19070)
  [None][feat] Add FP4 MLA attention backend (#19070)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/fp4_mla.py`, `tensorrt_llm/_torch/attention/backends/fp4_mla/__init__.py`, `tensorrt_llm/_torch/attention/backends/fp4_mla/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/fp4_mla/fp4_mla_context.py` _+9 more__
- **2026-09-18** [`b069d2e4ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/b069d2e4ac) [#18205](https://github.com/NVIDIA/TensorRT-LLM/pull/18205)
  [None][perf] Fuse MiniMax-M3 QKV and index projection (#18205)
  _Files: `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedQKNormRopeOp.cpp`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/common.py` _+12 more__
- **2026-09-17** [`cc9e82b92e`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc9e82b92e) [#18147](https://github.com/NVIDIA/TensorRT-LLM/pull/18147)
  [TRTLLM-14729][feat] Support various Qwen-Image attention backends (#18147)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/qwen_image/transformer_qwen_image.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+1 more__
- **2026-09-17** [`757fcf3d3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/757fcf3d3a) [#19296](https://github.com/NVIDIA/TensorRT-LLM/pull/19296)
  [None][fix] Restore grammar state after SA, DFlash and PARD verification (#19296)
  _Files: `tensorrt_llm/_torch/pyexecutor/guided_decoder.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tensorrt_llm/_torch/speculative/pard.py` _+4 more__
- **2026-09-17** [`a9fb3f768b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9fb3f768b) [#18210](https://github.com/NVIDIA/TensorRT-LLM/pull/18210)
  [TRTLLM-14388][refactor] BREAKING: Remove eagle_choices (#18210)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `docs/source/developer-guide/telemetry.md`, `docs/source/features/sampling.md` _+23 more__
- **2026-09-17** [`363581f23d`](https://github.com/NVIDIA/TensorRT-LLM/commit/363581f23d) [#19051](https://github.com/NVIDIA/TensorRT-LLM/pull/19051)
  [TRTLLM-16465][perf] Release unused attention workspace memory (#19051)
  _Files: `cpp/tensorrt_llm/thop/attentionOp.cpp`, `docs/source/developer-guide/perf-analysis.md`, `tensorrt_llm/_torch/attention/backends/fmha/combined.py`, `tensorrt_llm/_torch/attention/backends/fmha/fallback.py` _+7 more__
- **2026-09-17** [`5eddb137b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/5eddb137b1) [#19094](https://github.com/NVIDIA/TensorRT-LLM/pull/19094)
  [TRTLLM-14329][perf] Enable fused DSA metadata by default (#19094)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/dsa/fused_metadata.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/kernels.py`, `tensorrt_llm/_torch/attention/backends/sparse/dsa/metadata.py`, `tests/unittest/_torch/attention/sparse/dsa/test_fused_metadata.py`_
- **2026-09-17** [`2c4beda854`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c4beda854) [#19034](https://github.com/NVIDIA/TensorRT-LLM/pull/19034)
  [https://nvbugs/6739553][fix] Isolate the FlashInfer cubin cache per rank (#19034)
  _Files: `docs/source/llm-api/index.md`, `tensorrt_llm/llmapi/mpi_session.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/unittest/llmapi/_run_mpi_comm_task.py` _+2 more__
- **2026-09-17** [`7353a22eab`](https://github.com/NVIDIA/TensorRT-LLM/commit/7353a22eab) [#18457](https://github.com/NVIDIA/TensorRT-LLM/pull/18457)
  [https://nvbugs/6627795][fix] stop charging retiring requests against ADP admission and capacity (#18457)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+25 more__
- **2026-09-17** [`9753ee8c5d`](https://github.com/NVIDIA/TensorRT-LLM/commit/9753ee8c5d) [#19096](https://github.com/NVIDIA/TensorRT-LLM/pull/19096)
  [https://nvbugs/6641268][perf] Use producer-zeroed V tails in PrimTS FMHA (#19096)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py`, `tests/unittest/_torch/attention/test_prims_ts_attention_backend.py`, `tests/unittest/_torch/attention/test_prims_ts_fmha.py`_
- **2026-09-17** [`1d301319b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d301319b1) [#18946](https://github.com/NVIDIA/TensorRT-LLM/pull/18946)
  [None][feat] support FP8 KV cache in PrimTS MLA decode (#18946)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/prims_ts.py`, `tests/unittest/_torch/attention/test_prims_ts_attention_backend.py`, `tests/unittest/_torch/attention/test_prims_ts_fmha.py`_
- **2026-09-17** [`3f610d644c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f610d644c) [#19224](https://github.com/NVIDIA/TensorRT-LLM/pull/19224)
  [None][fix] SM107 runtime gate fixes and test hygiene from the Rubin validation run (#19224)
  _Files: `cpp/tensorrt_llm/thop/tinygemm2.cpp`, `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_deepseek_v4_o_proj.py` _+6 more__
- **2026-09-16** [`01e73ac83c`](https://github.com/NVIDIA/TensorRT-LLM/commit/01e73ac83c) [#18556](https://github.com/NVIDIA/TensorRT-LLM/pull/18556)
  [None][perf] default NumExpr to one thread and lazy-load it (#18556)
  _Files: `docs/source/features/sparse-attention.md`, `docs/source/features/visualgen-sparse-attention.md`, `tensorrt_llm/_bootstrap.py`, `tensorrt_llm/_torch/attention/backends/sparse/skip_softmax/params.py` _+1 more__
- **2026-09-16** [`dc6d663158`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc6d663158) [#19139](https://github.com/NVIDIA/TensorRT-LLM/pull/19139)
  [None][fix] Complete DeepSeek-V4 Rubin BF16 dispatch and optimize MLA KV expansion (#19139)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention/mla.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_deepseek_v4_o_proj.py` _+1 more__
- **2026-09-16** [`3c05b248c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c05b248c2) [#19221](https://github.com/NVIDIA/TensorRT-LLM/pull/19221)
  [None][fix] Align isSM100Family() with its SM100-109 C++ namesake (#19221)
  _Files: `tests/unittest/_torch/attention/sparse/test_prims_ts_block_sparse.py`, `tests/unittest/_torch/attention/test_prims_ts_attention_backend.py`, `tests/unittest/utils/util.py`_
- **2026-09-16** [`3b4faa281a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b4faa281a) [#19025](https://github.com/NVIDIA/TensorRT-LLM/pull/19025)
  [https://nvbugs/6555619][fix] Dispatch DeepSeek-V4 FMHA epilogue-fusion kernels on SM107 (#19025)
  _Files: `cpp/tests/unit_tests/kernels/CMakeLists.txt`, `cpp/tests/unit_tests/kernels/fmhaDsv4EpilogueFusionTest.cpp`_
- **2026-09-16** [`0a4f5334f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a4f5334f1) [#18811](https://github.com/NVIDIA/TensorRT-LLM/pull/18811)
  [None][chore] Split FMHA backend policy tests (#18811)
  _Files: `tensorrt_llm/_torch/attention/ATTENTION_DEVELOPER_GUIDE.md`, `tests/unittest/_torch/attention/test_combined_fmha.py`, `tests/unittest/_torch/attention/test_flashinfer_trtllm_gen_fmha.py`, `tests/unittest/_torch/attention/test_triton_custom_mask_fmha.py`_
- **2026-09-16** [`d457278045`](https://github.com/NVIDIA/TensorRT-LLM/commit/d457278045) [#18783](https://github.com/NVIDIA/TensorRT-LLM/pull/18783)
  [None][feat] Add DeepSeek-V4 support to NVFP4 cold-page KV Cache Compression (#18783)
  _Files: `cpp/tensorrt_llm/kernels/nvfp4ColdPageKernels.cu`, `cpp/tensorrt_llm/kernels/nvfp4ColdPageKernels.h`, `cpp/tests/unit_tests/kernels/nvfp4ColdPageKernelsTest.cpp`, `tensorrt_llm/_torch/kv_cache_compression/quantization_for_cold_page/nvfp4_quantization.py` _+7 more__
- **2026-09-16** [`309c020bb2`](https://github.com/NVIDIA/TensorRT-LLM/commit/309c020bb2) [#19108](https://github.com/NVIDIA/TensorRT-LLM/pull/19108)
  [https://nvbugs/6739916][fix] Preallocate GDN prefill state workspace (#19108)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/fla/fused_state_io.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py` _+1 more__
- **2026-09-16** [`c8a88ab989`](https://github.com/NVIDIA/TensorRT-LLM/commit/c8a88ab989) [#18723](https://github.com/NVIDIA/TensorRT-LLM/pull/18723)
  [None][feat] Enable NVFP4 KV for DSV4 (#18723)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.h`, `cpp/tensorrt_llm/kernels/deepseekV4BlockTable.cu` _+25 more__
- **2026-09-15** [`9ddb2859f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ddb2859f6) [#18774](https://github.com/NVIDIA/TensorRT-LLM/pull/18774)
  [None][test] Pin the float32 precision of the attention-plugin rotary table (#18774)
  _Files: `tensorrt_llm/functional.py`_
- **2026-09-15** [`5875960a84`](https://github.com/NVIDIA/TensorRT-LLM/commit/5875960a84) [#19144](https://github.com/NVIDIA/TensorRT-LLM/pull/19144)
  [https://nvbugs/6716104][fix] Keep mixed BF16 attention on FlashInfer (#19144)
  _Files: `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-09-15** [`86669b1a3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/86669b1a3b) [#18614](https://github.com/NVIDIA/TensorRT-LLM/pull/18614)
  [None][perf] Fuse MiniMax-M3 MSA per-layer KV-cache writes into one kernel (#18614)
  _Files: `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/msa_scatter.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/kernels/msa_utils.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+1 more__
- **2026-09-15** [`0529dffce1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0529dffce1) [#19054](https://github.com/NVIDIA/TensorRT-LLM/pull/19054)
  [TRTLLM-16326][test] Fail VisualGen tests on missing checkpoints/deps (#19054)
  _Files: `tests/AGENTS.md`, `tests/CLAUDE.md`, `tests/integration/defs/examples/visual_gen/test_visual_gen_cosmos3.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_flux.py` _+66 more__
- **2026-09-15** [`64fbd92b10`](https://github.com/NVIDIA/TensorRT-LLM/commit/64fbd92b10) [#18921](https://github.com/NVIDIA/TensorRT-LLM/pull/18921)
  [None][feat] support disaggregated serving for Qwen3.8-Flash-Next (#18921)
  _Files: `docs/source/_static/config_db.json`, `docs/source/deployment-guide/deployment-guide-for-qwen3.8-flash-next-on-trtllm.md`, `docs/source/deployment-guide/index.rst`, `docs/source/models/supported-models.md` _+28 more__
- **2026-09-14** [`2ebe4e6519`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ebe4e6519) [#18988](https://github.com/NVIDIA/TensorRT-LLM/pull/18988)
  [https://nvbugs/6732123][fix] Correct V2 KV cache quota estimation (#18988)
  _Files: `examples/layer_wise_benchmarks/run.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tensorrt_llm/tools/layer_wise_benchmarks/runner.py` _+7 more__
- **2026-09-14** [`594bf14e8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/594bf14e8a) [#19078](https://github.com/NVIDIA/TensorRT-LLM/pull/19078)
  [https://nvbugs/6661846][fix] Initialize FP8 storage in MSA layout tests (#19078)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/sparse/msa/test_msa_backend.py`_
- **2026-09-14** [`8900ec7c69`](https://github.com/NVIDIA/TensorRT-LLM/commit/8900ec7c69) [#18756](https://github.com/NVIDIA/TensorRT-LLM/pull/18756)
  [None][chore] Log attention kernel failure context and add an opt-in host-side page-table check (#18756)
  _Files: `tensorrt_llm/_torch/attention/backends/flashinfer.py`, `tensorrt_llm/_torch/attention/backends/trtllm.py`, `tensorrt_llm/_torch/attention/backends/utils.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py` _+5 more__
- **2026-09-14** [`a8ac7e5bcc`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8ac7e5bcc) [#18872](https://github.com/NVIDIA/TensorRT-LLM/pull/18872)
  [TRTLLM-14093][feat] Eagle3 support for MiniMax-M3 (#18872)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/attention/backends/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention/backends/sparse/minimax_m3/msa_backend.py` _+11 more__
- **2026-09-14** [`c81f5f230d`](https://github.com/NVIDIA/TensorRT-LLM/commit/c81f5f230d) [#18155](https://github.com/NVIDIA/TensorRT-LLM/pull/18155)
  [TRTLLM-15788][feat] Add dflash 2 support (#18155)
  _Files: `docs/source/features/speculative-decoding.md`, `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tensorrt_llm/llmapi/llm_args.py` _+3 more__
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

## MoE  (34 commits)

- **2026-09-21** [`db98912686`](https://github.com/NVIDIA/TensorRT-LLM/commit/db98912686) [#19323](https://github.com/NVIDIA/TensorRT-LLM/pull/19323)
  [None][feat] Support the MegaMoE CuteDSL MoE backend for Qwen3.8-Flash-Next (#19323)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_gb300.yml` _+1 more__
- **2026-09-21** [`5982425ca8`](https://github.com/NVIDIA/TensorRT-LLM/commit/5982425ca8) [#18397](https://github.com/NVIDIA/TensorRT-LLM/pull/18397)
  [None][feat] Router Replay (R3): return per-token MoE routing to training engine in post train. (#18397)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/moe_scheduler.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+15 more__
- **2026-09-20** [`1e2619abfe`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e2619abfe) [#19380](https://github.com/NVIDIA/TensorRT-LLM/pull/19380)
  [TRTLLM-14964][TRTLLM-14965][refactor] Give Marlin and DenseGEMM canonical impl identities (#19380)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/create_moe.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_deepgemm.py`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_densegemm.py` _+17 more__
- **2026-09-20** [`61f2b09fd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/61f2b09fd7) [#18689](https://github.com/NVIDIA/TensorRT-LLM/pull/18689)
  [None][feat] Add NCCL-EP 0.2 low-latency integration (#18689)
  _Files: `.gitignore`, `3rdparty/fetch_content.json`, `cpp/CMakeLists.txt`, `cpp/tensorrt_llm/CMakeLists.txt` _+18 more__
- **2026-09-20** [`845a141822`](https://github.com/NVIDIA/TensorRT-LLM/commit/845a141822) [#19061](https://github.com/NVIDIA/TensorRT-LLM/pull/19061)
  [TRTLLM-16184][refactor] Consolidate the C++ MoE kernels, thop ops and gtests under moe/ directories (#19061)
- **2026-09-19** [`9855bc8f36`](https://github.com/NVIDIA/TensorRT-LLM/commit/9855bc8f36) [#19392](https://github.com/NVIDIA/TensorRT-LLM/pull/19392)
  [TRTLLM-14967][refactor] Give the CuteDSL MegaMoE kernel an impl identity (#19392)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/__init__.py`, `tensorrt_llm/_torch/moe/fused_moe/mega_moe/mega_moe_cute_dsl.py`, `tensorrt_llm/_torch/moe/fused_moe/moe_resolution.py` _+2 more__
- **2026-09-19** [`347f5f172f`](https://github.com/NVIDIA/TensorRT-LLM/commit/347f5f172f) [#19179](https://github.com/NVIDIA/TensorRT-LLM/pull/19179)
  [None][refactor] Clean up Kimi checkpoint FP8 attention loading (#19179)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `examples/kimi_k3/eval_extra_llm_options_nvfp4_dep16.yaml`, `examples/kimi_k3/perf_sweep/acc_sweep.sbatch`, `examples/kimi_k3/perf_sweep/perf_sweep.sbatch` _+15 more__
- **2026-09-19** [`4d5889dbe9`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d5889dbe9) [#18357](https://github.com/NVIDIA/TensorRT-LLM/pull/18357)
  [None][feat] add CuteDslFc12FusedMoE fused FC1+FC2 NVFP4 MoE backend (Rubin/SM107) (#18357)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/manual_mma_128dp.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/rubin_contiguous_grouped_blockscaled_gemm_fused_fc12.py` _+11 more__
- **2026-09-19** [`5958f7c700`](https://github.com/NVIDIA/TensorRT-LLM/commit/5958f7c700) [#19182](https://github.com/NVIDIA/TensorRT-LLM/pull/19182)
  [None][feat] Kimi K3 attention-residual RMSNorm fusion + KDA beta-cache alignment (#19182)
  _Files: `cpp/tensorrt_llm/kernels/kimiK3AttnRes/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.cu`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwd.h`, `cpp/tensorrt_llm/kernels/kimiK3AttnRes/attnResFwdPersistentFused.cu` _+20 more__
- **2026-09-19** [`96d0c509e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/96d0c509e3) [#19184](https://github.com/NVIDIA/TensorRT-LLM/pull/19184)
  [None][feat] Rubin kernels & attention: DSV4/DSA, CuteDSL GEMM (#19184)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/envUtils.h`, `cpp/tensorrt_llm/kernels/mhcKernels/fused_tf32_pmap_gemm.cuh`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcFusedHcKernel.cu` _+40 more__
- **2026-09-18** [`6d0afd070f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d0afd070f) [#19038](https://github.com/NVIDIA/TensorRT-LLM/pull/19038)
  [None][fix] Fix runtime failures for rubin test enablement (#19038)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/aarch64-linux-gnu/libTrtLlmGen.a`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/lib/aarch64-linux-gnu/libTrtLlmGenFmhaLib.a` _+4 more__
- **2026-09-18** [`a8f436b2e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8f436b2e9) [#18800](https://github.com/NVIDIA/TensorRT-LLM/pull/18800)
  [https://nvbugs/6667807][fix] Raise NVLink one-sided MoE all-to-all rank cap to 256 (#18800)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h`, `tensorrt_llm/_torch/alltoall_watchdog.py`, `tensorrt_llm/_torch/moe/fused_moe/communication/nvlink_one_sided.py`, `tensorrt_llm/_torch/moe/fused_moe/ep_group_health.py` _+2 more__
- **2026-09-18** [`bb604eb699`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb604eb699) [#19065](https://github.com/NVIDIA/TensorRT-LLM/pull/19065)
  [None][fix] Exclude aggregates from the IsSimpleAlphaBeta guard (#19065)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`_
- **2026-09-17** [`b643ef8763`](https://github.com/NVIDIA/TensorRT-LLM/commit/b643ef8763) [#17956](https://github.com/NVIDIA/TensorRT-LLM/pull/17956)
  [None][perf] update MegaMoE kernels for Blackwell and Rubin (#17956)
  _Files: `.github/CODEOWNERS`, `pyproject.toml`, `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/cute_dsl_kernels/cutedsl_megamoe/__init__.py` _+79 more__
- **2026-09-17** [`ffeb88c473`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffeb88c473) [#17015](https://github.com/NVIDIA/TensorRT-LLM/pull/17015)
  [None][perf] Add CUTEDSL FC2 N-tile tuning override (#17015)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/moe/fused_moe/test_cutedsl_fc2_tuning.py`_
- **2026-09-17** [`9314f478fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9314f478fb) [#19153](https://github.com/NVIDIA/TensorRT-LLM/pull/19153)
  [TRTLLM-14968][TRTLLM-14969][refactor] Split TRTLLMGenFusedMoE into eleven leaves with canonical identities (#19153)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/models/modeling_qwen3_moe.py` _+52 more__
- **2026-09-17** [`74f1a89fec`](https://github.com/NVIDIA/TensorRT-LLM/commit/74f1a89fec) [#19199](https://github.com/NVIDIA/TensorRT-LLM/pull/19199)
  [https://nvbugs/6776338][fix] Enable DeepGEMM FP8 block scales on SM107 (#19199)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/rubin/moe/utils.py`, `tensorrt_llm/_torch/moe/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_deepgemm.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-09-17** [`5da6818a44`](https://github.com/NVIDIA/TensorRT-LLM/commit/5da6818a44) [#19255](https://github.com/NVIDIA/TensorRT-LLM/pull/19255)
  [https://nvbugs/6758594][fix] Measure MoE LoRA adapters one request at a time (#19255)
  _Files: `tests/integration/defs/llmapi/test_llm_api_pytorch_moe_lora.py`, `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`9a08c658cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a08c658cc) [#19280](https://github.com/NVIDIA/TensorRT-LLM/pull/19280)
  [https://nvbugs/6786555][fix] [https://nvbugs/6786567] Gate SM103 graph test on SM count (#19280)
  _Files: `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_
- **2026-09-17** [`61ab7a89b9`](https://github.com/NVIDIA/TensorRT-LLM/commit/61ab7a89b9) [#19102](https://github.com/NVIDIA/TensorRT-LLM/pull/19102)
  [nvbugs/6765038][fix] unwaive test case KimiK3MoERuntime in SiTU NVFP4 test since it has been fixed (#19102)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`2d62a504b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d62a504b5) [#19148](https://github.com/NVIDIA/TensorRT-LLM/pull/19148)
  [None][feat] add powerlaw expert_pattern to bench_moe routing control (#19148)
  _Files: `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/cli.py`, `tests/microbenchmarks/bench_moe/routing/builders.py`, `tests/microbenchmarks/bench_moe/routing/materialize.py` _+1 more__
- **2026-09-16** [`e19b5e3e70`](https://github.com/NVIDIA/TensorRT-LLM/commit/e19b5e3e70) [#19298](https://github.com/NVIDIA/TensorRT-LLM/pull/19298)
  [None][fix] Align MiniMax-M3 composition test fixtures with MoE interfaces (#19298)
  _Files: `tests/unittest/_torch/models/test_minimax_m3.py`, `tests/unittest/_torch/peft/test_moe_lora_model_path.py`_
- **2026-09-16** [`c2cec526aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2cec526aa) [#16919](https://github.com/NVIDIA/TensorRT-LLM/pull/16919)
  [None][perf] Reduce DeepEP metadata overhead in CuTeDSL MoE (#16919)
  _Files: `cpp/tensorrt_llm/kernels/cuteDslKernels/moeUtils.cu`, `cpp/tensorrt_llm/kernels/cuteDslKernels/moeUtils.h`, `cpp/tensorrt_llm/thop/cuteDslMoeUtilsOp.cpp`, `tensorrt_llm/_torch/compilation/utils.py` _+12 more__
- **2026-09-16** [`65804bfced`](https://github.com/NVIDIA/TensorRT-LLM/commit/65804bfced) [#18605](https://github.com/NVIDIA/TensorRT-LLM/pull/18605)
  [None][feat] Support MiniMax-M3 in MegaMoE CuTeDSL (#18605)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/epilogue_refactor.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/kernel_fc12.py`, `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/megamoe_kernel.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+9 more__
- **2026-09-16** [`b31664498f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b31664498f) [#18974](https://github.com/NVIDIA/TensorRT-LLM/pull/18974)
  [None][fix] Restore SM107 2x-mmaK acceptance and fine-grained sync PDL path (#18974)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/BatchedGemmInterface.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/GemmOptions.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/KernelTraits.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/trtllm/gen/DtypeDecl.h` _+4 more__
- **2026-09-16** [`912187481e`](https://github.com/NVIDIA/TensorRT-LLM/commit/912187481e) [#19035](https://github.com/NVIDIA/TensorRT-LLM/pull/19035)
  [None][chore] Deprecate the TRITON MoE backend (#19035)
  _Files: `docs/source/release-notes.md`, `tensorrt_llm/_torch/moe/fused_moe/fused_moe_triton.py`_
- **2026-09-16** [`2433335e13`](https://github.com/NVIDIA/TensorRT-LLM/commit/2433335e13) [#18898](https://github.com/NVIDIA/TensorRT-LLM/pull/18898)
  [https://nvbugs/6721561][fix] Accept flashinfer W4A16 ultra-wide FC2 tile on SM120 (#18898)
  _Files: `tensorrt_llm/_torch/moe/fused_moe/fused_moe_cute_dsl_b12x.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/moe/test_cute_dsl_b12x_moe_backend.py`_
- **2026-09-16** [`1f73bc5f30`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f73bc5f30) [#17408](https://github.com/NVIDIA/TensorRT-LLM/pull/17408)
  [None][feat] support draft model MoE backend override (#17408)
  _Files: `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tensorrt_llm/_torch/models/modeling_dflash.py`, `tensorrt_llm/_torch/models/modeling_dspark.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py` _+13 more__
- **2026-09-16** [`11e4c276e4`](https://github.com/NVIDIA/TensorRT-LLM/commit/11e4c276e4) [#19076](https://github.com/NVIDIA/TensorRT-LLM/pull/19076)
  [None][perf] GVR V2 top-K: 4K<n<=8K register rungs, unified QC gate, sampled small-envelope prefill plan, SM-count-aware dispatch with B300 tuning (#19076)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling_host.py`, `tests/unittest/_torch/thop/parallel/test_gvr_selfsampling_topk.py`_
- **2026-09-16** [`645efd145b`](https://github.com/NVIDIA/TensorRT-LLM/commit/645efd145b) [#18300](https://github.com/NVIDIA/TensorRT-LLM/pull/18300)
  [TRTLLM-15938][fix] build MoE MNNVL/all-to-all workspaces without MPI under Ray (#18300)
  _Files: `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`, `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+2 more__
- **2026-09-15** [`74033770db`](https://github.com/NVIDIA/TensorRT-LLM/commit/74033770db) [#18393](https://github.com/NVIDIA/TensorRT-LLM/pull/18393)
  [TRTLLM-10657][fix] Resolve MIXED_PRECISION quant config for DeepSeek W4A8 MoE experts (#18393)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/moe/fused_moe/configurable_moe.py`, `tests/unittest/_torch/modeling/test_modeling_deepseekv3.py`_
- **2026-09-15** [`e22f1e9263`](https://github.com/NVIDIA/TensorRT-LLM/commit/e22f1e9263) [#19109](https://github.com/NVIDIA/TensorRT-LLM/pull/19109)
  [TRTLLM-16404][fix] thread LoRA params through MoE models (#19109)
  _Files: `tensorrt_llm/_torch/models/modeling_afmoe.py`, `tensorrt_llm/_torch/models/modeling_glm.py`, `tensorrt_llm/_torch/models/modeling_minimaxm2.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py` _+6 more__
- **2026-09-14** [`4b768e3313`](https://github.com/NVIDIA/TensorRT-LLM/commit/4b768e3313) [#18766](https://github.com/NVIDIA/TensorRT-LLM/pull/18766)
  [None][infra] Skip pre-merge perf gating when main has already regressed and refactor the pre-merge perf-sanity list (#18766)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/README_perf_regression_system.md`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/perf_regression_utils.py` _+6 more__
- **2026-09-14** [`43cd45f9f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/43cd45f9f9) [#18126](https://github.com/NVIDIA/TensorRT-LLM/pull/18126)
  [TRTLLMINF-397][infra] Update dependencies to NGC PyTorch 26.08 (#18126)
  _Files: `ATTRIBUTIONS-Python.md`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcKernels.cu`, `cpp/tensorrt_llm/runtime/moeLoadBalancer/hostAccessibleDeviceAllocator.cpp` _+29 more__

## Executor / Runtime  (27 commits)

- **2026-09-21** [`575f4f9fcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/575f4f9fcf) [#19454](https://github.com/NVIDIA/TensorRT-LLM/pull/19454)
  [None][fix] Responses API: treat explicit null as unset for optional fields (#19454)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/unittest/llmapi/apps/test_responses_input_preprocess.py`_
- **2026-09-21** [`e6b2e73f76`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6b2e73f76) [#18902](https://github.com/NVIDIA/TensorRT-LLM/pull/18902)
  [None][chore] BREAKING: Remove unused code from LlmRequest (#18902)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `cpp/tensorrt_llm/executor/request.cpp` _+19 more__
- **2026-09-19** [`15c59954e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/15c59954e6) [#18389](https://github.com/NVIDIA/TensorRT-LLM/pull/18389)
  [None][perf] Prefix-tokenization cache for the default input processor (#18389)
  _Files: `docs/source/features/prefix-tokenization-cache.md`, `docs/source/index.rst`, `tensorrt_llm/inputs/prefix_token_cache.py`, `tensorrt_llm/inputs/registry.py` _+6 more__
- **2026-09-19** [`b56c5c459a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b56c5c459a) [#19202](https://github.com/NVIDIA/TensorRT-LLM/pull/19202)
  [None][fix] Release V2 cache claims after failed first-context admission (#19202)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.h`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py` _+10 more__
- **2026-09-18** [`0816dd81b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/0816dd81b8) [#19360](https://github.com/NVIDIA/TensorRT-LLM/pull/19360)
  [None][refactor] Remove callable telemetry schema metadata support (#19360)
  _Files: `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/usage/llmapi_config.py`, `tests/unittest/usage/test_llmapi_config_capture.py`_
- **2026-09-18** [`ff065918c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff065918c0) [#19290](https://github.com/NVIDIA/TensorRT-LLM/pull/19290)
  [TRTLLM-15262][feat] single source of truth for mrope_dummy_seq_slot (#19290)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-09-18** [`e72f70e99d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e72f70e99d) [#19049](https://github.com/NVIDIA/TensorRT-LLM/pull/19049)
  [https://nvbugs/6751484][fix] Honor every single-token stop word on the greedy fast path (#19049)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-09-17** [`bcbcc0ea08`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcbcc0ea08) [#18560](https://github.com/NVIDIA/TensorRT-LLM/pull/18560)
  [TRTLLM-16104][test] Add MX weight manifests and widen the ModelExpress qualification probe (#18560)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py` _+12 more__
- **2026-09-17** [`64e3b82cce`](https://github.com/NVIDIA/TensorRT-LLM/commit/64e3b82cce) [#19146](https://github.com/NVIDIA/TensorRT-LLM/pull/19146)
  [None][chore] Name the Nemotron multimodal module for the family it serves instead of one of its three models (#19146)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h_multimodal.py` _+10 more__
- **2026-09-16** [`c4298a822e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4298a822e) [#18697](https://github.com/NVIDIA/TensorRT-LLM/pull/18697)
  [None][fix] Align the budget split, spec layers and pool_ratio with derived per-layer KV windows (#18697)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_budget_split.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_estimation.py`_
- **2026-09-16** [`0aede91430`](https://github.com/NVIDIA/TensorRT-LLM/commit/0aede91430) [#19203](https://github.com/NVIDIA/TensorRT-LLM/pull/19203)
  [https://nvbugs/6762589][test] Register LTX-2 VAE and executor IPC tests in CI (#19203)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-09-16** [`2cda511a00`](https://github.com/NVIDIA/TensorRT-LLM/commit/2cda511a00) [#19158](https://github.com/NVIDIA/TensorRT-LLM/pull/19158)
  [https://nvbugs/6762287][fix] Pin the measured literal `"Hello there! "` at both assertion sites, preserving… (#19158)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_llm.py`_
- **2026-09-16** [`2576928b91`](https://github.com/NVIDIA/TensorRT-LLM/commit/2576928b91) [#19103](https://github.com/NVIDIA/TensorRT-LLM/pull/19103)
  [None][fix] KVCM2: fix remaining Python/C++ parity issues and replace abort with a poison latch (#19103)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.cu`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp` _+38 more__
- **2026-09-15** [`7ec31c064b`](https://github.com/NVIDIA/TensorRT-LLM/commit/7ec31c064b) [#18207](https://github.com/NVIDIA/TensorRT-LLM/pull/18207)
  [TRTLLM-15262][feat] Test CUDA graph input buffers status before replay (#18207)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/unittest/_torch/executor/test_cuda_graph_capture_replay.py`, `tests/unittest/_torch/helpers.py`_
- **2026-09-15** [`686f0e0f72`](https://github.com/NVIDIA/TensorRT-LLM/commit/686f0e0f72) [#19130](https://github.com/NVIDIA/TensorRT-LLM/pull/19130)
  [None][feat] Make ADP new conversation routing token-aware (#19130)
  _Files: `docs/source/developer-guide/telemetry.md`, `docs/source/features/subagent-routing.md`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/llmapi/llm_args.py` _+2 more__
- **2026-09-15** [`000d3e98ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/000d3e98ca) [#19140](https://github.com/NVIDIA/TensorRT-LLM/pull/19140)
  [TRTLLM-16220][feat] Enable KVCacheManagerV2 by default for Nemotron multimodal models (#19140)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tests/unittest/_torch/executor/kv_cache/test_mamba_cache_manager.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-09-15** [`bf75b704ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/bf75b704ec) [#18680](https://github.com/NVIDIA/TensorRT-LLM/pull/18680)
  [None][fix] Route custom-tokenizer loading through one shared loader (#18680)
  _Files: `tensorrt_llm/bench/utils/data.py`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/serve/scripts/backend_request_func.py`, `tensorrt_llm/tokenizer/tokenizer.py` _+2 more__
- **2026-09-15** [`f7f596b94e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7f596b94e) [#19163](https://github.com/NVIDIA/TensorRT-LLM/pull/19163)
  [None][chore] cuda_graph_runner: name the padded-batch bound, document the tail-only padding invariant (#19163)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`_
- **2026-09-15** [`8e9790440b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e9790440b) [#19192](https://github.com/NVIDIA/TensorRT-LLM/pull/19192)
  [https://nvbugs/6708349][fix] Allocate V2 KV block scales using resolved dtype (#19192)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_mamba_cache_manager.py`_
- **2026-09-15** [`f11db85547`](https://github.com/NVIDIA/TensorRT-LLM/commit/f11db85547) [#19004](https://github.com/NVIDIA/TensorRT-LLM/pull/19004)
  [None][feat] Enable KVCacheManagerV2 by default for Llama and Llama4 (#19004)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/models/modeling_llama.py`, `tests/integration/defs/kv_cache/test_kv_cache_iteration_stats.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-09-15** [`5cb1c9500b`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cb1c9500b) [#18978](https://github.com/NVIDIA/TensorRT-LLM/pull/18978)
  [None][fix] compose telemetry capture policies (#18978)
  _Files: `docs/source/_ext/llmapi_config_telemetry.py`, `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/llmapi/llm_args.py`, `tensorrt_llm/usage/config.py` _+6 more__
- **2026-09-14** [`cf43ce5955`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf43ce5955) [#18926](https://github.com/NVIDIA/TensorRT-LLM/pull/18926)
  [https://nvbugs/6556429][fix] Fix host tier budget on integrated GPUs (#18926)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/kv_cache/test_kvv2_host_tier_sizing.py`_
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

## Torch Path (_torch)  (19 commits)

- **2026-09-21** [`2480b57f94`](https://github.com/NVIDIA/TensorRT-LLM/commit/2480b57f94) [#19476](https://github.com/NVIDIA/TensorRT-LLM/pull/19476)
  [None][chore] Remove the duplicate Rubin fused FC12 op registration (#19476)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`_
- **2026-09-21** [`25ea5ff833`](https://github.com/NVIDIA/TensorRT-LLM/commit/25ea5ff833) [#19142](https://github.com/NVIDIA/TensorRT-LLM/pull/19142)
  [None][fix] Reject unsupported SM100 sync-object factories (#19142)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/custom_pipeline.py`, `tests/unittest/_torch/cute_dsl_kernels/test_custom_pipeline.py`_
- **2026-09-21** [`79af2e7c97`](https://github.com/NVIDIA/TensorRT-LLM/commit/79af2e7c97) [#19256](https://github.com/NVIDIA/TensorRT-LLM/pull/19256)
  [None][test] Add coverage for WhisperForConditionalGeneration (#19256)
  _Files: `tests/unittest/_torch/modeling/test_modeling_whisper.py`_
- **2026-09-20** [`e1e562d3e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1e562d3e6) [#19335](https://github.com/NVIDIA/TensorRT-LLM/pull/19335)
  [https://nvbugs/6777501][fix] Fix nemotron breakable cuda graph test parity check (#19335)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_nemotron_h.py`_
- **2026-09-18** [`d4b1879b5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4b1879b5f) [#19341](https://github.com/NVIDIA/TensorRT-LLM/pull/19341)
  [TRTLLM-16217][test] Add Rubin single-node serve perf cases (#19341)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-18** [`ab769ad2a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab769ad2a4) [#19135](https://github.com/NVIDIA/TensorRT-LLM/pull/19135)
  [TRTLLM-16516][feat] Give each VisualGen server its own media directory (#19135)
  _Files: `.gitignore`, `examples/visual_gen/serve/README.md`, `tensorrt_llm/serve/openai_server.py`, `tests/unittest/_torch/visual_gen/test_trtllm_serve_endpoints.py`_
- **2026-09-18** [`07243d644d`](https://github.com/NVIDIA/TensorRT-LLM/commit/07243d644d) [#19097](https://github.com/NVIDIA/TensorRT-LLM/pull/19097)
  [NVBUG-6762388][fix] enable Cosmos3 Edge Diffusers parity (#19097)
  _Files: `tests/unittest/_torch/visual_gen/cosmos3_edge_diffusers_parity.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_edge.py`_
- **2026-09-18** [`b5011b1441`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5011b1441) [#19259](https://github.com/NVIDIA/TensorRT-LLM/pull/19259)
  [None][test] Enable Wan2.2 Rubin QA coverage and add Cosmos3 Super example (#19259)
  _Files: `tests/integration/defs/examples/visual_gen/test_visual_gen_cosmos3.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen_wan.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_b200.yml` _+4 more__
- **2026-09-17** [`e74b74043b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e74b74043b) [#19239](https://github.com/NVIDIA/TensorRT-LLM/pull/19239)
  [https://nvbugs/6693990][test] Remove flaky MTP non-greedy CUDA graph matches eager test (#19239)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`2b0421eae6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2b0421eae6) [#19246](https://github.com/NVIDIA/TensorRT-LLM/pull/19246)
  [None][test] Add coverage for Exaone4ForCausalLM (#19246)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_exaone4_5.py`_
- **2026-09-16** [`cf0f4f0126`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf0f4f0126) [#18036](https://github.com/NVIDIA/TensorRT-LLM/pull/18036)
  [TRTLLM-15740][perf] VisualGen Wan: deduplicate shared RoPE SMEM staging (#18036)
  _Files: `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`, `tests/unittest/_torch/visual_gen/kernels/parallel_hw_agnostic/test_fused_dit_qk_norm_rope.py`_
- **2026-09-16** [`845136cf04`](https://github.com/NVIDIA/TensorRT-LLM/commit/845136cf04) [#19210](https://github.com/NVIDIA/TensorRT-LLM/pull/19210)
  [None][fix] Correct the NVLink link count on GPUs below NVML's probe bound (#19210)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/test_mnnvl_utils.py`_
- **2026-09-16** [`1ebcc55651`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ebcc55651) [#18738](https://github.com/NVIDIA/TensorRT-LLM/pull/18738)
  [None][test] Add InferenceX-style GSM8K accuracy eval mode (#18738)
  _Files: `docs/source/commands/trtllm-eval.rst`, `tensorrt_llm/commands/eval.py`, `tensorrt_llm/evaluate/__init__.py`, `tensorrt_llm/evaluate/lm_eval.py` _+7 more__
- **2026-09-16** [`3a5731321c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a5731321c) [#17987](https://github.com/NVIDIA/TensorRT-LLM/pull/17987)
  [https://nvbugs/6535765][fix] bump Wan layernorm fusion math to FP32 (#17987)
  _Files: `cpp/tensorrt_llm/kernels/fusedAdaptiveLayerNormKernel.cu`, `cpp/tensorrt_llm/kernels/fusedAdaptiveLayerNormKernel.h`, `cpp/tensorrt_llm/thop/fusedAdaptiveLayerNormOp.cpp`, `tensorrt_llm/_torch/visual_gen/models/wan/transformer_wan.py` _+2 more__
- **2026-09-15** [`0f89724b8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f89724b8c) [#18909](https://github.com/NVIDIA/TensorRT-LLM/pull/18909)
  [None][fix] Preserve caller-supplied Cosmos3 prompt metadata (#18909)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_pipeline.py`_
- **2026-09-15** [`c2d8441ac3`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2d8441ac3) [#19021](https://github.com/NVIDIA/TensorRT-LLM/pull/19021)
  [None][chore] Remove TRT leftovers from perf and stress test (#19021)
  _Files: `tests/integration/defs/perf/README_release_test.md`, `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/perf/utils.py` _+2 more__
- **2026-09-14** [`3dd002db37`](https://github.com/NVIDIA/TensorRT-LLM/commit/3dd002db37) [#19017](https://github.com/NVIDIA/TensorRT-LLM/pull/19017)
  [None][test] Add coverage for BartForConditionalGeneration (#19017)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_bart.py`_
- **2026-09-14** [`eefca665ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/eefca665ca) [#18948](https://github.com/NVIDIA/TensorRT-LLM/pull/18948)
  [None][test] Add native PyTorch coverage for DeciLMForCausalLM (#18948)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nas.py`_
- **2026-09-14** [`fa9813cc4d`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa9813cc4d) [#18888](https://github.com/NVIDIA/TensorRT-LLM/pull/18888)
  [TRTLLM-15936][fix] Enable breakable prefill CUDA graphs (BCG) for Nemotron-H hybrid models (#18888)
  _Files: `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+2 more__

## Disaggregation / KV  (19 commits)

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
- **2026-09-19** [`3fafd13761`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fafd13761) [#18810](https://github.com/NVIDIA/TensorRT-LLM/pull/18810)
  [None][fix] Emit multimodal keys in KV cache v2 events (#18810)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/eventManager.h` _+17 more__
- **2026-09-18** [`3dcf5c0ea9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3dcf5c0ea9) [#19349](https://github.com/NVIDIA/TensorRT-LLM/pull/19349)
  [None][test] Trim DeepSeek-R1 and Nemotron-Ultra-V3 perf-sanity cases (#19349)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml` _+12 more__
- **2026-09-18** [`08c680196e`](https://github.com/NVIDIA/TensorRT-LLM/commit/08c680196e) [#18910](https://github.com/NVIDIA/TensorRT-LLM/pull/18910)
  [https://nvbugs/6626640][fix] Correct V2 KV cache estimation (#18910)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache/kv_cache_manager_v2.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_estimation.py` _+1 more__
- **2026-09-18** [`9f26cc3fa4`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f26cc3fa4) [#19382](https://github.com/NVIDIA/TensorRT-LLM/pull/19382)
  [None][fix] Initialize KV cache fixtures and unwaive nine cases on all platforms (#19382)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/test_kv_connector_v2_prefix.py`_
- **2026-09-18** [`ffddc5abd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffddc5abd1) [#19384](https://github.com/NVIDIA/TensorRT-LLM/pull/19384)
  [None][test] Temporarily waive nine KV cache regressions on all platforms (#19384)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-17** [`5e4bf75caa`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e4bf75caa) [#18583](https://github.com/NVIDIA/TensorRT-LLM/pull/18583)
  [#18465][feat] Track KV cache reuse hit tokens by source tier (#18583)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/AGENTS.md`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/introspection.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/introspection.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+31 more__
- **2026-09-17** [`e2be5bb529`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2be5bb529) [#18762](https://github.com/NVIDIA/TensorRT-LLM/pull/18762)
  [TRTLLM-12891][feat] Support KV cache connector for v2_kvcm and extend VSWA support (#18762)
  _Files: `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp`, `docs/source/features/kv-cache-connector.md`, `docs/source/features/kvcache.md`, `examples/llm-api/llm_kv_cache_connector.py` _+26 more__
- **2026-09-17** [`d3412a5a8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3412a5a8d) [#19219](https://github.com/NVIDIA/TensorRT-LLM/pull/19219)
  [https://nvbugs/6746175][fix] Size the agentx aiperf timeout to cover warmup and unwaive GB300 DSpark con1456 (#19219)
  _Files: `tests/integration/defs/perf/agentx_client.py`, `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v4-pro-dspark_agentx_con1156_ctx2_dep8_gen1_dep8_eplb0_dspark3_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v4-pro-dspark_agentx_con1456_ctx3_dep8_gen1_dep16_eplb0_dspark5_ccb-NIXL.yaml` _+2 more__
- **2026-09-16** [`889e574298`](https://github.com/NVIDIA/TensorRT-LLM/commit/889e574298) [#19206](https://github.com/NVIDIA/TensorRT-LLM/pull/19206)
  [None][fix] Keep strict Qwen3 LoRA checks with KV cache manager V2 (#19206)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/tests_lora_modules/test_qwen3_sanity.py`_
- **2026-09-16** [`7c79c15fa1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7c79c15fa1) [#19207](https://github.com/NVIDIA/TensorRT-LLM/pull/19207)
  [None][test] Enforce the V2 KV cache iteration stats contract (#19207)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_iteration_stats.py`, `tests/unittest/executor/test_stats_serializer.py`, `tests/unittest/metrics/test_collector.py`_
- **2026-09-16** [`4bee19ab76`](https://github.com/NVIDIA/TensorRT-LLM/commit/4bee19ab76) [#15780](https://github.com/NVIDIA/TensorRT-LLM/pull/15780)
  [TRTLLM-15344][feat] cache transceiver nixl bounce buffer (#15780)
  _Files: `cpp/CMakeLists.txt`, `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/agentBindings.cpp` _+56 more__
- **2026-09-15** [`a1f8742a84`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1f8742a84) [#18638](https://github.com/NVIDIA/TensorRT-LLM/pull/18638)
  [None][chore] Refactor support for beam search in disaggregated serving (#18638)
  _Files: `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py` _+5 more__
- **2026-09-15** [`bc013951c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc013951c9) [#19114](https://github.com/NVIDIA/TensorRT-LLM/pull/19114)
  [None][test] Prune DeepSeek-V3 and DeepSeek-V3.2 tests (#19114)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_cancel_stress_test_large.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+5 more__
- **2026-09-14** [`a1fe8aa55b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1fe8aa55b) [#19149](https://github.com/NVIDIA/TensorRT-LLM/pull/19149)
  [https://nvbugs/6758853][test] Unwaive KV cache V1/V2 parity tests (#19149)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-14** [`c776328e08`](https://github.com/NVIDIA/TensorRT-LLM/commit/c776328e08) [#19132](https://github.com/NVIDIA/TensorRT-LLM/pull/19132)
  [https://nvbugs/6758853][fix] Prewarm prefixes for KV cache parity comparisons (#19132)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`_

## Speculative Decoding  (11 commits)

- **2026-09-21** [`24c76d7a23`](https://github.com/NVIDIA/TensorRT-LLM/commit/24c76d7a23) [#18654](https://github.com/NVIDIA/TensorRT-LLM/pull/18654)
  [None][test] Prune Llama-3.1 8b model from tests (#18654)
  _Files: `tests/integration/defs/conftest.py`, `tests/integration/defs/disaggregated/test_ad_disagg.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_qwen3_8b.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+22 more__
- **2026-09-20** [`2406c60967`](https://github.com/NVIDIA/TensorRT-LLM/commit/2406c60967) [#19451](https://github.com/NVIDIA/TensorRT-LLM/pull/19451)
  [https://nvbugs/6672360][test] Unwaive GPTOSS Eagle3 no-overlap on RTX PRO 6000 (#19451)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-09-20** [`d5f7d867de`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5f7d867de) [#18515](https://github.com/NVIDIA/TensorRT-LLM/pull/18515)
  [TRTLLM-15137][feat] Add fused sampling and min-p support to AdvancedSamplingMode.FULL (#18515)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/fusedSampling/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/fusedSampling/fusedSamplingKernels.cu` _+27 more__
- **2026-09-19** [`8a26dd8f9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a26dd8f9d) [#19107](https://github.com/NVIDIA/TensorRT-LLM/pull/19107)
  [None][test] Enable gen_only_no_context mode in perf sanity system (#19107)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/aggregated/slurm_launch_draft.sh`, `jenkins/scripts/perf/benchmark_utils.py`, `jenkins/scripts/perf/local/submit.py` _+15 more__
- **2026-09-19** [`faa142a317`](https://github.com/NVIDIA/TensorRT-LLM/commit/faa142a317) [#19390](https://github.com/NVIDIA/TensorRT-LLM/pull/19390)
  [None][fix] Resolve unset temperature to 1.0 for non-greedy one-model spec decode rows (#19390)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`_
- **2026-09-17** [`33193c2b32`](https://github.com/NVIDIA/TensorRT-LLM/commit/33193c2b32) [#19204](https://github.com/NVIDIA/TensorRT-LLM/pull/19204)
  [#17495][fix] Share draft length updates with warmup (#19204)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/speculative/utils.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine_warmup.py` _+2 more__
- **2026-09-17** [`0732d9f90f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0732d9f90f) [#19018](https://github.com/NVIDIA/TensorRT-LLM/pull/19018)
  [None][fix] Fix KV cache size estimation with Qwen3.5 + EAGLE3 (#19018)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_budget_split.py`, `tests/unittest/_torch/executor/kv_cache/test_kv_cache_estimation.py`_
- **2026-09-17** [`b40c8d61fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/b40c8d61fb) [#19267](https://github.com/NVIDIA/TensorRT-LLM/pull/19267)
  [None][test] add VR200 multi-node disagg perf cases (#19267)
  _Files: `jenkins/scripts/perf/cluster_env.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/qa/llm_perf_multinode_basic.txt` _+12 more__
- **2026-09-16** [`c17b558a32`](https://github.com/NVIDIA/TensorRT-LLM/commit/c17b558a32) [#19161](https://github.com/NVIDIA/TensorRT-LLM/pull/19161)
  [None][fix] Reject sampling params unsupported by one-model speculation before the stream opens (#19161)
  _Files: `tensorrt_llm/_torch/speculative/spec_sampler_base.py`, `tensorrt_llm/llmapi/llm.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_one_model_sampling_rejection.py`_
- **2026-09-16** [`77b63b2a82`](https://github.com/NVIDIA/TensorRT-LLM/commit/77b63b2a82) [#18933](https://github.com/NVIDIA/TensorRT-LLM/pull/18933)
  [TRTLLM-15758][refactor] Extract encoder runners from model engine (#18933)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/encoder_executor.py`, `tensorrt_llm/_torch/pyexecutor/engine/cuda_graph.py`, `tensorrt_llm/_torch/pyexecutor/engine/runners/__init__.py` _+23 more__
- **2026-09-15** [`df569f4bbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/df569f4bbe) [#19168](https://github.com/NVIDIA/TensorRT-LLM/pull/19168)
  [https://nvbugs/6708111][fix] Load Nemotron-H saved by transformers>=5.13 (#19168)
  _Files: `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tensorrt_llm/_torch/speculative/utils.py`, `tensorrt_llm/tokenizer/tokenizer.py`, `tests/unittest/_torch/modeling/test_nemotron_h_layer_vocabulary.py`_

## Other  (10 commits)

- **2026-09-21** [`e1deeff3a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1deeff3a5) [#19339](https://github.com/NVIDIA/TensorRT-LLM/pull/19339)
  [None][fix] Reconfigure cmake when build_wheel.py arguments change (#19339)
  _Files: `scripts/build_wheel.py`, `tests/unittest/others/test_build_wheel_reconfigure.py`_
- **2026-09-21** [`c5e250a009`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5e250a009) [#19419](https://github.com/NVIDIA/TensorRT-LLM/pull/19419)
  [None][doc] Keep change rationale in the PR description, not code comments (#19419)
  _Files: `AGENTS.md`_
- **2026-09-17** [`e5c698cb01`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5c698cb01) [#19274](https://github.com/NVIDIA/TensorRT-LLM/pull/19274)
  [None][fix] Match vendor include patterns by path component (#19274)
  _Files: `3rdparty/vendor-sources.md`, `scripts/vendor_sources.py`, `tests/unittest/others/test_vendor_sources.py`_
- **2026-09-17** [`73c70633b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/73c70633b2)
  [None][chore] promote PrimTS source from TRT-LLM #18815
  _Files: `3rdparty/vendor_sources.lock.yaml`_
- **2026-09-16** [`66a15a1c60`](https://github.com/NVIDIA/TensorRT-LLM/commit/66a15a1c60) [#19286](https://github.com/NVIDIA/TensorRT-LLM/pull/19286)
  [None][fix] Stage all requirements files for out-of-tree wheels (#19286)
  _Files: `scripts/build_wheel.py`, `tests/unittest/scripts/test_build_wheel_staging.py`_
- **2026-09-16** [`d5a6b04227`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5a6b04227) [#19279](https://github.com/NVIDIA/TensorRT-LLM/pull/19279)
  [None][fix] Restore bounce-buffer capture policy for documentation builds (#19279)
  _Files: `tensorrt_llm/usage/llm_args_golden_manifest.json`_
- **2026-09-15** [`2dbab44d4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2dbab44d4f) [#17737](https://github.com/NVIDIA/TensorRT-LLM/pull/17737)
  [None][fix] reject empty prompt list in completions endpoint (#17737)
  _Files: `tensorrt_llm/serve/openai_server.py`_
- **2026-09-15** [`5f99da54c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f99da54c5) [#19160](https://github.com/NVIDIA/TensorRT-LLM/pull/19160)
  [None][fix] Logger: honor printf-style arguments (#19160)
  _Files: `tensorrt_llm/logger.py`, `tests/unittest/others/test_logger_percent_format.py`_
- **2026-09-15** [`a26a55aae1`](https://github.com/NVIDIA/TensorRT-LLM/commit/a26a55aae1) [#18222](https://github.com/NVIDIA/TensorRT-LLM/pull/18222)
  [None][test] Run the Blackwell 4-GPU perf cases on Rubin (#18222)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-15** [`441039154e`](https://github.com/NVIDIA/TensorRT-LLM/commit/441039154e) [#18977](https://github.com/NVIDIA/TensorRT-LLM/pull/18977)
  [None][chore] Remove unused LlmRequest methods (#18977)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/llmRequest.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/bindings.cpp`, `cpp/tests/unit_tests/batch_manager/llmRequestTest.cpp`_

## Quantization  (9 commits)

- **2026-09-21** [`dbf9ceb2a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/dbf9ceb2a5) [#19344](https://github.com/NVIDIA/TensorRT-LLM/pull/19344)
  [None][fix] Use bounded NVFP4 serving configs for MiniMax-M3 perf tests (#19344)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-18** [`55f7eca861`](https://github.com/NVIDIA/TensorRT-LLM/commit/55f7eca861) [#19340](https://github.com/NVIDIA/TensorRT-LLM/pull/19340)
  [None][test] Add nemotron_3.5_lightning_30b_nvfp4 and nemotron_3.5_lightning_30b_bf16 func and perf cases on Spark (#19340)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/examples/serve/test_configs/Nemotron35_Lightning_30B.yml`, `tests/integration/defs/examples/serve/test_serve.py`, `tests/integration/defs/perf/_model_paths.py` _+5 more__
- **2026-09-18** [`a9c9ec0e8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9c9ec0e8b) [#19317](https://github.com/NVIDIA/TensorRT-LLM/pull/19317)
  [None][doc] Document DeepSeek-V4 support in NVFP4 cold-page Compression (#19317)
  _Files: `docs/source/features/kv-cache-compression.md`, `examples/kv_cache_compression/nvfp4_cold_page.md`_
- **2026-09-18** [`6aeba5b7a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/6aeba5b7a6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+8 more__
- **2026-09-16** [`a8dca52ec6`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8dca52ec6) [#19030](https://github.com/NVIDIA/TensorRT-LLM/pull/19030)
  [https://nvbugs/6714109][fix] Remove deprecated Minimax M3 Triton MXFP8 piecewise graph test (#19030)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-09-16** [`7b1bedbbbd`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b1bedbbbd) [#19150](https://github.com/NVIDIA/TensorRT-LLM/pull/19150)
  [None][fix] Pass alpha through SM107 scaled_mm compilation (#19150)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dense_blockscaled_gemm_persistent.py`, `tensorrt_llm/_torch/cute_dsl_kernels/rubin/dense_blockscaled_gemm_persistent.py`_
- **2026-09-16** [`5af487deae`](https://github.com/NVIDIA/TensorRT-LLM/commit/5af487deae)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+8 more__
- **2026-09-15** [`108b2aaed7`](https://github.com/NVIDIA/TensorRT-LLM/commit/108b2aaed7) [#18620](https://github.com/NVIDIA/TensorRT-LLM/pull/18620)
  [None][perf] Add CuteDSL to MiniMax-M3 autotune (for MXFP8 linear GEMM+quant) (#18620)
  _Files: `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/modules/test_mxfp8_linear.py`_
- **2026-09-14** [`6e1cc953c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6e1cc953c0) [#19134](https://github.com/NVIDIA/TensorRT-LLM/pull/19134)
  [https://nvbugs/6621358][fix] Isolate DeepSeek NVFP4 LongBench MPI session (#19134)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_

## ROCm / AMD  (8 commits)

- **2026-09-17** [`1009588222`](https://github.com/NVIDIA/TensorRT-LLM/commit/1009588222) [#19046](https://github.com/NVIDIA/TensorRT-LLM/pull/19046)
  [None][test] verify model feature matrix support (#19046)
  _Files: `docs/source/features/feature-combination-matrix.md`, `docs/source/models/supported-models.md`, `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/test_glm52.py` _+2 more__
- **2026-09-17** [`ec22079fbf`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec22079fbf) [#19198](https://github.com/NVIDIA/TensorRT-LLM/pull/19198)
  [TRTLLM-16186][feat] Route native KV transfer through a shared backend contract (#19198)
  _Files: `tensorrt_llm/_torch/disaggregation/base/__init__.py`, `tensorrt_llm/_torch/disaggregation/base/backend.py`, `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/fetch.py` _+19 more__
- **2026-09-17** [`e76ada4478`](https://github.com/NVIDIA/TensorRT-LLM/commit/e76ada4478) [#19266](https://github.com/NVIDIA/TensorRT-LLM/pull/19266)
  [TRTLLM-15716][refactor] Extract receive start/tail and admission into DisaggTransferCoordinator (#19266)
  _Files: `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/disaggregation/orchestration/interfaces.py`, `tensorrt_llm/_torch/pyexecutor/disagg_adapter.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+19 more__
- **2026-09-16** [`6882e320e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/6882e320e8) [#19084](https://github.com/NVIDIA/TensorRT-LLM/pull/19084)
  [https://nvbugs/6656598][tests] Deprecate K2 E2E test for K3 (#19084)
  _Files: `tests/integration/defs/accuracy/references/gpqa_diamond.yaml`, `tests/integration/defs/accuracy/test_kimi3.py`, `tests/integration/test_lists/qa/llm_function_multinode.txt`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_node4_gpu16.yml`_
- **2026-09-16** [`82d667fbfb`](https://github.com/NVIDIA/TensorRT-LLM/commit/82d667fbfb) [#18743](https://github.com/NVIDIA/TensorRT-LLM/pull/18743)
  [TRTLLMINF-445][infra] Upgrade public torch to 2.13.0 and triton to 3.7.1 (#18743)
  _Files: `ATTRIBUTIONS-Python.md`, `docker/common/install_pytorch.sh`, `docs/source/installation/installation-guide.md`, `jenkins/L0_Test.groovy` _+49 more__
- **2026-09-15** [`a494ef678a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a494ef678a) [#18461](https://github.com/NVIDIA/TensorRT-LLM/pull/18461)
  [TRTLLM-16020][test] Add Kimi K3 GSM8K accuracy tests to GB300 multi-node post-merge CI (#18461)
  _Files: `jenkins/scripts/slurm_run.sh`, `tests/integration/defs/accuracy/test_kimi3.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_node4_gpu16.yml`_
- **2026-09-15** [`6cae275f16`](https://github.com/NVIDIA/TensorRT-LLM/commit/6cae275f16) [#19128](https://github.com/NVIDIA/TensorRT-LLM/pull/19128)
  [TRTLLM-15715][refactor] Extract progress polling and error consensus into DisaggTransferCoordinator (#19128)
  _Files: `tensorrt_llm/_torch/disaggregation/orchestration/coordinator.py`, `tensorrt_llm/_torch/disaggregation/orchestration/interfaces.py`, `tensorrt_llm/_torch/pyexecutor/disagg_adapter.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+18 more__
- **2026-09-14** [`858a360ffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/858a360ffe) [#18861](https://github.com/NVIDIA/TensorRT-LLM/pull/18861)
  [None][chore] Refine QA code ownership (#18861)
  _Files: `.github/CODEOWNERS`_

## Models  (5 commits)

- **2026-09-21** [`a7eae4beee`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7eae4beee) [#19332](https://github.com/NVIDIA/TensorRT-LLM/pull/19332)
  [None][test] Add coverage for DeepseekV32ForCausalLM (#19332)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_deepseekv32.py`_
- **2026-09-18** [`34495fa8bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/34495fa8bf) [#19277](https://github.com/NVIDIA/TensorRT-LLM/pull/19277)
  [None][fix] Make MoonViT replication helix-aware (#19277)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`, `tests/unittest/_torch/modeling/test_kimi_k3_config_routing.py`_
- **2026-09-16** [`97f84eb314`](https://github.com/NVIDIA/TensorRT-LLM/commit/97f84eb314) [#19245](https://github.com/NVIDIA/TensorRT-LLM/pull/19245)
  [None][test] Add coverage for Phi3ForCausalLM (#19245)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/modeling/test_modeling_phi3.py`_
- **2026-09-16** [`166b51894f`](https://github.com/NVIDIA/TensorRT-LLM/commit/166b51894f) [#19191](https://github.com/NVIDIA/TensorRT-LLM/pull/19191)
  [TRTLLM-16188][test] Add Kimi K3 short-context perf cases and fix stale disagg note (#19191)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-09-14** [`0aede9d2a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/0aede9d2a4) [#19022](https://github.com/NVIDIA/TensorRT-LLM/pull/19022)
  [None][chore] BREAKING: Remove TRT leftovers from serve and eval (#19022)
  _Files: `docs/source/commands/trtllm-eval.rst`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `examples/models/core/qwen/README.md`, `examples/trtllm-eval/README.md` _+3 more__

## Docs / Examples  (4 commits)

- **2026-09-20** [`7edb2b2a18`](https://github.com/NVIDIA/TensorRT-LLM/commit/7edb2b2a18) [#19426](https://github.com/NVIDIA/TensorRT-LLM/pull/19426)
  [None][doc] Remove the outdated deployment guide. (#19426)
  _Files: `docs/source/deployment-guide/index.rst`_
- **2026-09-17** [`6f6284e79f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f6284e79f) [#19346](https://github.com/NVIDIA/TensorRT-LLM/pull/19346)
  [None][chore] Bump version to 1.3.0rc28 (#19346)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-09-16** [`ccb6760b1f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccb6760b1f) [#19170](https://github.com/NVIDIA/TensorRT-LLM/pull/19170)
  [#19169][test] Balance post-merge checkpoint I/O experiment arms (#19170)
  _Files: `docs/source/features/checkpoint-loading.md`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/scripts/test_perf_sanity_helpers.py`_
- **2026-09-14** [`55e29043bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e29043bd) [#19137](https://github.com/NVIDIA/TensorRT-LLM/pull/19137)
  [None][chore] Bump version to 1.3.0rc27 (#19137)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## AutoDeploy  (2 commits)

- **2026-09-17** [`b3b6098ef6`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3b6098ef6)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-09-14** [`fc3edba4f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc3edba4f8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_

## Compilation / Graph  (1 commits)

- **2026-09-21** [`611263e2fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/611263e2fc) [#19449](https://github.com/NVIDIA/TensorRT-LLM/pull/19449)
  [https://nvbugs/6786567][chore] Remove waiver for SM103 GVR CUDA graph test (#19449)
  _Files: `tests/integration/test_lists/waives.txt`_

## Perf  (1 commits)

- **2026-09-18** [`d219a1e9f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/d219a1e9f5) [#18850](https://github.com/NVIDIA/TensorRT-LLM/pull/18850)
  [None][chore] Remove TRT leftovers from bench (#18850)
  _Files: `examples/apps/README.md`, `examples/longbench/eval_longbench_v1.py`, `tensorrt_llm/bench/benchmark/__init__.py`, `tensorrt_llm/bench/benchmark/low_latency.py` _+5 more__

---
_Generated 2026-09-21 15:12 UTC_