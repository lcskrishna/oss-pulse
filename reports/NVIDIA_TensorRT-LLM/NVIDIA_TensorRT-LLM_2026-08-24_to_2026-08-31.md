# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-08-24 → 2026-08-31  |  **Total commits:** 270

## ✨ New Features This Week

- **2026-08-31** [#18178](https://github.com/NVIDIA/TensorRT-LLM/pull/18178) — [None][refactor] Harden the KvCacheTransceiver contract and add a conformance fake (#18178)
- **2026-08-31** [#17377](https://github.com/NVIDIA/TensorRT-LLM/pull/17377) — [TRTLLM-12680][feat] add exit code telemetry (#17377)
- **2026-08-31** [#14095](https://github.com/NVIDIA/TensorRT-LLM/pull/14095) — [TRTLLM-11412][feat] Add offloading support for visual_gen (#14095)
- **2026-08-31** [#18363](https://github.com/NVIDIA/TensorRT-LLM/pull/18363) — [None][infra] Add GB300 multi-node post-merge stages for Qwen3.8-2.4T-A95B NVFP4 accuracy (#18363)
- **2026-08-31** [#18347](https://github.com/NVIDIA/TensorRT-LLM/pull/18347) — [None][feat] Prefer POSIX FD handle type for KV cache V2 VMM allocations (#18347)
- **2026-08-31** [#18298](https://github.com/NVIDIA/TensorRT-LLM/pull/18298) — [None][test] Add AgentX DeepSeek-V4-Pro-DSpark perf-sanity lanes on GB300 (#18298)
- **2026-08-31** [#16710](https://github.com/NVIDIA/TensorRT-LLM/pull/16710) — [None][feat] KVCacheManagerV2: suspend/resume observability stat + coverage (#16710)
- **2026-08-31** [#18279](https://github.com/NVIDIA/TensorRT-LLM/pull/18279) — [TRTLLMINF-339][infra] enable BOLT profile overlay on published container images (#18279)
- **2026-08-31** [#18416](https://github.com/NVIDIA/TensorRT-LLM/pull/18416) — [None][test] Add MiniMax-M3 disaggregated perf recipes to QA multi-node list (#18416)
- **2026-08-31** [#16214](https://github.com/NVIDIA/TensorRT-LLM/pull/16214) — [None][feat] Support custom masks in TRTLLM attention (#16214)
- _…and 43 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#18407](https://github.com/NVIDIA/TensorRT-LLM/issues/18407) | [Bug]: KVCacheV2Scheduler retains active PEFT adapters after KV suspen | KV-Cache Management, Lora/P-tuning, Pytorch | 2026-08-30 |
| [#18297](https://github.com/NVIDIA/TensorRT-LLM/issues/18297) | [Bug] trtllm-bench hangs forever at shutdown when --iteration_log poin | Customized kernels | 2026-08-27 |
| [#18156](https://github.com/NVIDIA/TensorRT-LLM/issues/18156) | KV-cache-aware router never matches LoRA or salted requests: lora_id i | Disaggregated serving | 2026-08-24 |
| [#18153](https://github.com/NVIDIA/TensorRT-LLM/issues/18153) | [RFC]: Versioned KV Hints Protocol for TRT-LLM | RFC | 2026-08-24 |
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-08-22 |
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
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 78 |
| Attention | 35 |
| Executor / Runtime | 31 |
| MoE | 28 |
| Disaggregation / KV | 19 |
| Quantization | 18 |
| Models | 14 |
| Torch Path (_torch) | 13 |
| LoRA | 8 |
| Other | 8 |
| Docs / Examples | 7 |
| Speculative Decoding | 7 |
| AutoDeploy | 4 |

## CI / Infra  (78 commits)

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
- **2026-08-29** [`2e5dbe0a52`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e5dbe0a52) [#18394](https://github.com/NVIDIA/TensorRT-LLM/pull/18394)
  [https://nvbugs/6581049][ci] Unwaive test (#18394)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`5a9700462f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a9700462f) [#17799](https://github.com/NVIDIA/TensorRT-LLM/pull/17799)
  [TRTLLMINF-324][infra] Extend infra-scoped fail-fast to the build→consumer edge (#17799)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-08-28** [`a662631a31`](https://github.com/NVIDIA/TensorRT-LLM/commit/a662631a31) [#17084](https://github.com/NVIDIA/TensorRT-LLM/pull/17084)
  [#17016][feat] Add selectable OpenEngine gRPC server (#17084)
  _Files: `.github/CODEOWNERS`, `docker/Dockerfile.multi`, `jenkins/current_image_tags.properties`, `requirements-openengine.txt` _+6 more__
- **2026-08-28** [`7110513dd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7110513dd8) [#18033](https://github.com/NVIDIA/TensorRT-LLM/pull/18033)
  [None][infra] Declare and pin CI-imported deps to prevent transitive drops (#18033)
  _Files: `.github/workflows/label_community_pr.yml`, `.github/workflows/label_component_pr.yml`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_Test.groovy` _+4 more__
- **2026-08-28** [`390f92d763`](https://github.com/NVIDIA/TensorRT-LLM/commit/390f92d763) [#18361](https://github.com/NVIDIA/TensorRT-LLM/pull/18361)
  [None][infra] Waive 7 failed cases for main in post-merge 2934 (#18361)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`bd675a5e72`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd675a5e72) [#17586](https://github.com/NVIDIA/TensorRT-LLM/pull/17586)
  [None][infra] Retry SLURM agent online timeouts (#17586)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-28** [`4fa30d2bd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/4fa30d2bd1) [#18283](https://github.com/NVIDIA/TensorRT-LLM/pull/18283)
  [None][infra] Waive failed cases for main in pre-merge 56812 (#18283)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`54478a0d14`](https://github.com/NVIDIA/TensorRT-LLM/commit/54478a0d14) [#18340](https://github.com/NVIDIA/TensorRT-LLM/pull/18340)
  [None][infra] Waive 5 failed cases for main in post-merge 2932 (#18340)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`b08deaaa34`](https://github.com/NVIDIA/TensorRT-LLM/commit/b08deaaa34) [#18309](https://github.com/NVIDIA/TensorRT-LLM/pull/18309)
  [None][infra] Cache merge request file changes for CBTS (#18309)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-28** [`fef337286c`](https://github.com/NVIDIA/TensorRT-LLM/commit/fef337286c) [#18332](https://github.com/NVIDIA/TensorRT-LLM/pull/18332)
  [None][test] Update GB300 MiniMax-M3 waive (#18332)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`85ae713eb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/85ae713eb5) [#18315](https://github.com/NVIDIA/TensorRT-LLM/pull/18315)
  [None][chore] Update blossom-ci allowlist (#18315)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-08-27** [`507f2a5086`](https://github.com/NVIDIA/TensorRT-LLM/commit/507f2a5086) [#18291](https://github.com/NVIDIA/TensorRT-LLM/pull/18291)
  [TRTLLMINF-339][infra] Declare BoltProfileGen's SCM pass-through params (#18291)
  _Files: `jenkins/BoltProfileGen.groovy`_
- **2026-08-27** [`43ba505710`](https://github.com/NVIDIA/TensorRT-LLM/commit/43ba505710) [#18221](https://github.com/NVIDIA/TensorRT-LLM/pull/18221)
  [https://nvbugs/6337224][test] Unwaive test_config_database_tests_sync (#18221)
  _Files: `tests/unittest/tools/test_config_database_sync.py`_
- **2026-08-27** [`d6ed25c636`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6ed25c636) [#18282](https://github.com/NVIDIA/TensorRT-LLM/pull/18282)
  [TRTLLMINF-345][doc] clarify nightly release installation (#18282)
  _Files: `docker/Dockerfile.multi`, `docs/source/installation/installation-guide.md`_
- **2026-08-27** [`7cae26e987`](https://github.com/NVIDIA/TensorRT-LLM/commit/7cae26e987) [#18303](https://github.com/NVIDIA/TensorRT-LLM/pull/18303)
  [None][infra] Waive 1 failed cases for main in pre-merge 56942 (#18303)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`6589a4eccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/6589a4eccf) [#18237](https://github.com/NVIDIA/TensorRT-LLM/pull/18237)
  [None][infra] Upload build info during pipeline setup (#18237)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-27** [`8e1655195f`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e1655195f) [#18217](https://github.com/NVIDIA/TensorRT-LLM/pull/18217)
  [TRTLLMINF-263][infra] pass nSpect release entitlement (#18217)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-08-27** [`34847b86be`](https://github.com/NVIDIA/TensorRT-LLM/commit/34847b86be) [#18058](https://github.com/NVIDIA/TensorRT-LLM/pull/18058)
  [None][infra] CBTS coverage arch combine v2 (#18058)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/coverage_selection/SELECTION.md`, `jenkins/scripts/cbts/coverage_selection/artifact.py` _+4 more__
- **2026-08-27** [`6a44fe7d08`](https://github.com/NVIDIA/TensorRT-LLM/commit/6a44fe7d08) [#18240](https://github.com/NVIDIA/TensorRT-LLM/pull/18240)
  [TRTLLMINF-187][fix] Drain S3 test logs from rank zero (#18240)
  _Files: `jenkins/scripts/slurm_run.sh`, `tests/test_common/s3_output.py`_
- **2026-08-27** [`d55090633b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d55090633b) [#14138](https://github.com/NVIDIA/TensorRT-LLM/pull/14138)
  [TRTLLM-9905][infra] Upload results periodically (#14138)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/progress_upload_snapshot.sh`, `jenkins/scripts/progress_upload_watcher.sh`_
- **2026-08-27** [`6eb66fa8b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6eb66fa8b7) [#18281](https://github.com/NVIDIA/TensorRT-LLM/pull/18281)
  [None][infra] Waive 1 failed cases for main in pre-merge 56772 (#18281)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`c2f5f31912`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2f5f31912) [#18212](https://github.com/NVIDIA/TensorRT-LLM/pull/18212)
  [TRTLLMINF-339][infra] Enable BOLT profile-gen producer (job + cadence + promote) (#18212)
  _Files: `jenkins/BoltProfileGen.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-08-26** [`ddd62066bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/ddd62066bf) [#18208](https://github.com/NVIDIA/TensorRT-LLM/pull/18208)
  [None][infra] Set --platform when retagging CI image (#18208)
  _Files: `scripts/rename_docker_images.py`_
- **2026-08-26** [`fa77839718`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa77839718) [#18191](https://github.com/NVIDIA/TensorRT-LLM/pull/18191)
  [None][ci] waive pre-existing test failures on main (#18191)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`574bd601d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/574bd601d8) [#18258](https://github.com/NVIDIA/TensorRT-LLM/pull/18258)
  [None][infra] Waive 1 failed cases for main in pre-merge 56793 (#18258)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`8bde010504`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bde010504) [#17947](https://github.com/NVIDIA/TensorRT-LLM/pull/17947)
  [https://nvbugs/6422432][fix] Unwaive testcase (#17947)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`7e192541a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e192541a4) [#18241](https://github.com/NVIDIA/TensorRT-LLM/pull/18241)
  [https://nvbugs/6669902][test] Waive minimax_m3 tests broken by the build_kv_page_indices signature (#18241)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`f4449ae8f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4449ae8f1) [#18245](https://github.com/NVIDIA/TensorRT-LLM/pull/18245)
  [None][infra] Waive 1 failed cases for main in pre-merge 56702 (#18245)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`6d9fbeae70`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d9fbeae70) [#16467](https://github.com/NVIDIA/TensorRT-LLM/pull/16467)
  [None][infra] Fix CBTS skip-rate calculation method (#16467)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/tools/report_cbts_decision.py`, `tests/unittest/scripts/test_report_cbts_decision.py`_
- **2026-08-26** [`e3b0e2b32c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e3b0e2b32c) [#17372](https://github.com/NVIDIA/TensorRT-LLM/pull/17372)
  [https://nvbugs/6561778][fix] Fence all ranks before pytest launch in multi-node slurm_run.sh (#17372)
  _Files: `jenkins/scripts/slurm_run.sh`, `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`d2ad4c0110`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2ad4c0110) [#18224](https://github.com/NVIDIA/TensorRT-LLM/pull/18224)
  [None][infra] Waive 1 failed cases for main in pre-merge 56631 (#18224)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`6d09ecbaab`](https://github.com/NVIDIA/TensorRT-LLM/commit/6d09ecbaab) [#18230](https://github.com/NVIDIA/TensorRT-LLM/pull/18230)
  [None][infra] Waive 7 failed cases for main in post-merge 2927 (#18230)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`67b9201e30`](https://github.com/NVIDIA/TensorRT-LLM/commit/67b9201e30) [#18229](https://github.com/NVIDIA/TensorRT-LLM/pull/18229)
  [None][infra] Waive 1 failed cases for main in pre-merge 56649 (#18229)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`59825e3a0b`](https://github.com/NVIDIA/TensorRT-LLM/commit/59825e3a0b) [#18227](https://github.com/NVIDIA/TensorRT-LLM/pull/18227)
  [None][infra] Waive 1 failed cases for main in pre-merge 56614 (#18227)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`500cd3c1de`](https://github.com/NVIDIA/TensorRT-LLM/commit/500cd3c1de) [#18216](https://github.com/NVIDIA/TensorRT-LLM/pull/18216)
  [https://nvbugs/6661846][test] Waive MSA paged HND unaligned outer stride test (#18216)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`6beb4b2b39`](https://github.com/NVIDIA/TensorRT-LLM/commit/6beb4b2b39)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-08-25** [`909dbfd50e`](https://github.com/NVIDIA/TensorRT-LLM/commit/909dbfd50e) [#18198](https://github.com/NVIDIA/TensorRT-LLM/pull/18198)
  [None][infra] Waive 1 failed cases for main in pre-merge 56476 (#18198)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`cfc93d4755`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfc93d4755) [#18127](https://github.com/NVIDIA/TensorRT-LLM/pull/18127)
  [None][infra] Set perf-sanity s_branch from the pipeline branch, not the Jenkins folder (#18127)
  _Files: `jenkins/L0_MergeRequest.groovy`, `tests/integration/defs/perf/README_perf_regression_system.md`, `tests/integration/defs/perf/perf_regression_utils.py`, `tests/unittest/others/test_perf_regression_branch.py`_
- **2026-08-25** [`c9878386ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9878386ce) [#18187](https://github.com/NVIDIA/TensorRT-LLM/pull/18187)
  [None][test] Waive 6 failed cases for main in QA CI (#18187)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`ce5307ca16`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce5307ca16) [#17813](https://github.com/NVIDIA/TensorRT-LLM/pull/17813)
  [TRTLLMINF-161][infra] Add simplified infrastructure dry-run pipeline (#17813)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_run.sh`, `tests/integration/defs/test_infra_dry_run_benchmark.py` _+3 more__
- **2026-08-25** [`5eb413dcdf`](https://github.com/NVIDIA/TensorRT-LLM/commit/5eb413dcdf) [#17370](https://github.com/NVIDIA/TensorRT-LLM/pull/17370)
  [https://nvbugs/6561777][fix] Add slurm_wait_all_ranks(), a job+step-keyed marker barrier counting… (#17370)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`c850fb4cd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/c850fb4cd9) [#18177](https://github.com/NVIDIA/TensorRT-LLM/pull/18177)
  [None][test] Waive 5 failed cases for main in QA CI (#18177)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`410ec5dd79`](https://github.com/NVIDIA/TensorRT-LLM/commit/410ec5dd79) [#18173](https://github.com/NVIDIA/TensorRT-LLM/pull/18173)
  [None][infra] Waive 5 failed cases for main in post-merge 2925 (#18173)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`cd51d92f07`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd51d92f07) [#18171](https://github.com/NVIDIA/TensorRT-LLM/pull/18171)
  [https://nvbugs/6661914][test] Waive Wan2.2 TI2V-5B T2V per-token AdaLN unittests (#18171)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`a265c6cc02`](https://github.com/NVIDIA/TensorRT-LLM/commit/a265c6cc02) [#18172](https://github.com/NVIDIA/TensorRT-LLM/pull/18172)
  [None][test] Waive 3 failed cases for main in QA CI (#18172)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`1e63f30568`](https://github.com/NVIDIA/TensorRT-LLM/commit/1e63f30568) [#18168](https://github.com/NVIDIA/TensorRT-LLM/pull/18168)
  [None][test] Waive 4 failed cases for main in QA CI (#18168)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`11b4d9ed8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/11b4d9ed8c) [#18167](https://github.com/NVIDIA/TensorRT-LLM/pull/18167)
  [None][test] Waive 9 failed cases for main in QA CI (#18167)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`ac7d6089a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac7d6089a7) [#17803](https://github.com/NVIDIA/TensorRT-LLM/pull/17803)
  [None][infra] CBTS compact coverage data (#17803)
  _Files: `.github/CODEOWNERS`, `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/coverage_pilot.py`, `jenkins/scripts/cbts/coverage_selection/SELECTION.md` _+10 more__
- **2026-08-25** [`6be4f23c7b`](https://github.com/NVIDIA/TensorRT-LLM/commit/6be4f23c7b) [#18105](https://github.com/NVIDIA/TensorRT-LLM/pull/18105)
  [None][test] Remove 54 closed-bug waive entries for main (#18105)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`b4eb01dd0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4eb01dd0e) [#18119](https://github.com/NVIDIA/TensorRT-LLM/pull/18119)
  [TRTLLMINF-263][infra] unify nSpect version organization (#18119)
  _Files: `jenkins/BuildDockerImage.groovy`, `jenkins/L0_MergeRequest.groovy`_
- **2026-08-25** [`8644826e6a`](https://github.com/NVIDIA/TensorRT-LLM/commit/8644826e6a) [#17313](https://github.com/NVIDIA/TensorRT-LLM/pull/17313)
  [https://nvbugs/6546909][fix] Make the handle's lifetime match its graphs — lazy… (#17313)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`896a766d14`](https://github.com/NVIDIA/TensorRT-LLM/commit/896a766d14) [#17419](https://github.com/NVIDIA/TensorRT-LLM/pull/17419)
  [None][infra] PLC pipeline display fix (#17419)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`, `jenkins/scripts/pulse_in_pipeline_scanning/main.py`, `jenkins/scripts/pulse_in_pipeline_scanning/submit_report.py`, `jenkins/scripts/pulse_in_pipeline_scanning/utils/triage.py` _+2 more__
- **2026-08-24** [`7a33f79196`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a33f79196) [#16132](https://github.com/NVIDIA/TensorRT-LLM/pull/16132)
  [https://nvbugs/6428091][fix] Move `use_host_stop_criteria` from `SampleStateTorch` into… (#16132)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`4259477efb`](https://github.com/NVIDIA/TensorRT-LLM/commit/4259477efb) [#18125](https://github.com/NVIDIA/TensorRT-LLM/pull/18125)
  [None][infra] Reduce resource requested by CPU stages (#18125)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-24** [`13b1eaf379`](https://github.com/NVIDIA/TensorRT-LLM/commit/13b1eaf379) [#18137](https://github.com/NVIDIA/TensorRT-LLM/pull/18137)
  [None][test] Waive 6 failed cases for main in QA CI (#18137)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`2221eba9fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/2221eba9fe) [#18132](https://github.com/NVIDIA/TensorRT-LLM/pull/18132)
  [None][test] Waive 1 failed cases for main in QA CI (#18132)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`18b272ec16`](https://github.com/NVIDIA/TensorRT-LLM/commit/18b272ec16) [#18129](https://github.com/NVIDIA/TensorRT-LLM/pull/18129)
  [None][test] Waive 3 failed cases for main in QA CI (#18129)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`5b7a888c41`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b7a888c41) [#18110](https://github.com/NVIDIA/TensorRT-LLM/pull/18110)
  [https://nvbugs/6561777][fix] Unwaive bug 6561775 since the fix from 6541343 is merged (#18110)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`0beecdac62`](https://github.com/NVIDIA/TensorRT-LLM/commit/0beecdac62) [#18123](https://github.com/NVIDIA/TensorRT-LLM/pull/18123)
  [None][infra] Waive 6 failed cases for main in post-merge 2924 (#18123)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`ba0b9b4b9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba0b9b4b9e) [#17852](https://github.com/NVIDIA/TensorRT-LLM/pull/17852)
  [https://nvbugs/6561559][test] Unwaive test_overlap_scheduler_consist… (#17852)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`3497d9f006`](https://github.com/NVIDIA/TensorRT-LLM/commit/3497d9f006) [#17543](https://github.com/NVIDIA/TensorRT-LLM/pull/17543)
  [None][infra] Disable RTXPro6000D multi gpu stages due to some nodes are offline (#17543)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-24** [`74fc10a3f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/74fc10a3f6) [#18112](https://github.com/NVIDIA/TensorRT-LLM/pull/18112)
  [None][infra] Waive 6 failed cases for main in post-merge 2923 (#18112)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`2d974a7155`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d974a7155)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-24** [`add5e32849`](https://github.com/NVIDIA/TensorRT-LLM/commit/add5e32849) [#17367](https://github.com/NVIDIA/TensorRT-LLM/pull/17367)
  [https://nvbugs/6541343][fix] Add `slurm_wait_all_ranks()` — a job+step-keyed marker barrier on the shared… (#17367)
  _Files: `jenkins/scripts/slurm_run.sh`_

## Attention  (35 commits)

- **2026-08-31** [`4593e50d78`](https://github.com/NVIDIA/TensorRT-LLM/commit/4593e50d78) [#18391](https://github.com/NVIDIA/TensorRT-LLM/pull/18391)
  [TRTLLM-14575][perf] Batch DSA cross-layer index remap into one kernel launch per indexer group (#18391)
  _Files: `cpp/tensorrt_llm/kernels/convertReqIndexToGlobal.cu`, `cpp/tensorrt_llm/kernels/convertReqIndexToGlobal.h`, `cpp/tensorrt_llm/thop/convertReqIndexToGlobalOp.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/backend.py` _+5 more__
- **2026-08-31** [`ad66327e17`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad66327e17) [#16214](https://github.com/NVIDIA/TensorRT-LLM/pull/16214)
  [None][feat] Support custom masks in TRTLLM attention (#16214)
  _Files: `cpp/tensorrt_llm/kernels/unfusedAttentionKernels.h`, `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h`, `cpp/tensorrt_llm/thop/trtllmGenQKVProcessOp.cpp`, `tensorrt_llm/_torch/attention_backend/fmha/__init__.py` _+19 more__
- **2026-08-31** [`775015b6c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/775015b6c0) [#18417](https://github.com/NVIDIA/TensorRT-LLM/pull/18417)
  [None][chore] Apply clang-format to FMHA kernel header (#18417)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-08-30** [`6c1ce33e7f`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c1ce33e7f) [#18183](https://github.com/NVIDIA/TensorRT-LLM/pull/18183)
  [None][chore] Update trtllm-gen FMHA kernels and cubins (#18183)
- **2026-08-30** [`e53a70c0e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/e53a70c0e3) [#18145](https://github.com/NVIDIA/TensorRT-LLM/pull/18145)
  [https://nvbugs/6640776][fix] Bump CUTLASS DSL to 4.6.2 to unblock FA4 split-KV (#18145)
  _Files: `ATTRIBUTIONS-Python.md`, `constraints.txt`, `docker/Dockerfile.multi`, `jenkins/L0_MergeRequest.groovy` _+5 more__
- **2026-08-30** [`26c1c12f17`](https://github.com/NVIDIA/TensorRT-LLM/commit/26c1c12f17)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+11 more__
- **2026-08-29** [`77cc145384`](https://github.com/NVIDIA/TensorRT-LLM/commit/77cc145384) [#18232](https://github.com/NVIDIA/TensorRT-LLM/pull/18232)
  [TRTLLM-15405][refactor] BREAKING: Remove TRTLLMSampler and sampler_type (#18232)
  _Files: `.pre-commit-config.yaml`, `docs/source/blogs/tech_blog/blog11_GPT_OSS_Eagle3.md`, `docs/source/developer-guide/telemetry.md`, `docs/source/features/sampling.md` _+44 more__
- **2026-08-29** [`57db9f4bb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/57db9f4bb5) [#18354](https://github.com/NVIDIA/TensorRT-LLM/pull/18354)
  [https://nvbugs/6641268][fix] Use fallback FMHA for SM103 context attention (#18354)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/test_combined_fmha.py`_
- **2026-08-28** [`f077d4a467`](https://github.com/NVIDIA/TensorRT-LLM/commit/f077d4a467) [#17781](https://github.com/NVIDIA/TensorRT-LLM/pull/17781)
  [TRTLLM-15585][feat] Wire SkipSoftmax sparse attention into the CuTeDSL backend (#17781)
  _Files: `docs/source/visual-gen/features/sparse-attention.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/cute_dsl/fmha.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/utils.py`, `tensorrt_llm/_torch/visual_gen/models/modeling.py` _+6 more__
- **2026-08-28** [`891b483174`](https://github.com/NVIDIA/TensorRT-LLM/commit/891b483174) [#18043](https://github.com/NVIDIA/TensorRT-LLM/pull/18043)
  [None][feat] Consolidate the DSpark draft paths and support standalone drafters (#18043)
  _Files: `tensorrt_llm/_torch/models/_arch_index.py`, `tensorrt_llm/_torch/models/dspark/__init__.py`, `tensorrt_llm/_torch/models/dspark/attention.py`, `tensorrt_llm/_torch/models/dspark/draft.py` _+29 more__
- **2026-08-28** [`e68f58149b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e68f58149b) [#16940](https://github.com/NVIDIA/TensorRT-LLM/pull/16940)
  [TRTLLM-14116][feat] Add DeepSeek-V4 Hopper support (#16940)
  _Files: `3rdparty/fetch_content.json`, `cpp/tensorrt_llm/flash_mla/CMakeLists.txt`, `examples/models/core/deepseek_v4/README.md`, `scripts/attribution/data/dependency_metadata.yml` _+13 more__
- **2026-08-28** [`ec411dcedb`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec411dcedb) [#18131](https://github.com/NVIDIA/TensorRT-LLM/pull/18131)
  [None][feat] Enable CuTe DSL MLA with Helix (#18131)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp16.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/attention/mla/mla_decode_fp8.py` _+2 more__
- **2026-08-28** [`6f7a13c739`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f7a13c739) [#17976](https://github.com/NVIDIA/TensorRT-LLM/pull/17976)
  [None][perf] SM120 optimizations for Qwen3.6-35B-A3B-NVFP4 (#17976)
  _Files: `cpp/kernels/fmha_v2/setup.py`, `cpp/kernels/xqa/mha.cu`, `cpp/tensorrt_llm/common/attentionOp.cpp`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+3 more__
- **2026-08-28** [`bd03d5ff32`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd03d5ff32) [#18226](https://github.com/NVIDIA/TensorRT-LLM/pull/18226)
  [None][fix] Keep CuTe-DSL MLA decode for Kimi K3 H=96 speculative-verify batches (#18226)
  _Files: `tensorrt_llm/_torch/modules/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`, `tests/unittest/_torch/modules/test_kimi_k3_mla_backend.py`_
- **2026-08-27** [`682fa40d27`](https://github.com/NVIDIA/TensorRT-LLM/commit/682fa40d27) [#18154](https://github.com/NVIDIA/TensorRT-LLM/pull/18154)
  [None][perf] Histogram top-k for MiniMax-M3 block selector (#18154)
  _Files: `cpp/tensorrt_llm/kernels/minimaxM3SelectBlocks.cu`, `tests/unittest/_torch/attention/sparse/test_minimax_m3_msa_selector.py`_
- **2026-08-27** [`710fd258cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/710fd258cb) [#17936](https://github.com/NVIDIA/TensorRT-LLM/pull/17936)
  [TRTLLM-14874][feat] Refactor advanced-sampling CUDA graph capture (#17936)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/rocket/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+13 more__
- **2026-08-27** [`9fc603baa0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fc603baa0) [#17792](https://github.com/NVIDIA/TensorRT-LLM/pull/17792)
  [TRTLLM-15030][fix] CuteDSL MLA decode follow-ups: bucket AutoTuner fallback, autotune + disagg tests (#17792)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/unittest/_torch/attention/test_attention_mla.py`_
- **2026-08-26** [`ca939b7bae`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca939b7bae) [#18196](https://github.com/NVIDIA/TensorRT-LLM/pull/18196)
  [https://nvbugs/6579626][perf] Fallback small BF16 context batches (#18196)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-08-26** [`3e2749fccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e2749fccf) [#17961](https://github.com/NVIDIA/TensorRT-LLM/pull/17961)
  [https://nvbugs/6596590][fix] Densify warmup mesh for sparse fmha kernel (#17961)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`_
- **2026-08-26** [`1b19a8197f`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b19a8197f) [#18002](https://github.com/NVIDIA/TensorRT-LLM/pull/18002)
  [None][fix] Stabilize Gemma4 FA2 CUDA Graph decode on Hopper (#18002)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-08-26** [`0a373efd9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a373efd9f) [#17842](https://github.com/NVIDIA/TensorRT-LLM/pull/17842)
  [None][feat] Add the ported MiniMax-M3 decode kernels ahead of their wiring (#17842)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_indexer.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/triton_sparse_decode.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/trtllm_gen_dense_decode.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+6 more__
- **2026-08-26** [`a2888334f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2888334f9) [#17986](https://github.com/NVIDIA/TensorRT-LLM/pull/17986)
  [None][perf] Address inter-idle times and decode-first assumption in MSA (#17986)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/common.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_backend.py` _+3 more__
- **2026-08-25** [`7e106301df`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e106301df) [#18211](https://github.com/NVIDIA/TensorRT-LLM/pull/18211)
  [None][test] Unwaive Qwen3.5-4B DFlash tests (#18211)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`c2539ac93c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2539ac93c) [#17935](https://github.com/NVIDIA/TensorRT-LLM/pull/17935)
  [None][perf] Optimize DFlash draft forward (#17935)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+1 more__
- **2026-08-25** [`f12bf33370`](https://github.com/NVIDIA/TensorRT-LLM/commit/f12bf33370) [#18044](https://github.com/NVIDIA/TensorRT-LLM/pull/18044)
  [None][refactor] add Vanilla sparse attention primitives (#18044)
  _Files: `tensorrt_llm/_torch/attention_backend/vanilla.py`, `tests/unittest/_torch/attention/test_vanilla_attention.py`_
- **2026-08-25** [`491f11a691`](https://github.com/NVIDIA/TensorRT-LLM/commit/491f11a691) [#17562](https://github.com/NVIDIA/TensorRT-LLM/pull/17562)
  [TRTLLM-14388][refactor] Remove 2 model spec dec drafting loops (#17562)
  _Files: `.pre-commit-config.yaml`, `legacy-files.txt`, `pyproject.toml`, `ruff-legacy.toml` _+21 more__
- **2026-08-25** [`c32f1d4cb8`](https://github.com/NVIDIA/TensorRT-LLM/commit/c32f1d4cb8) [#17691](https://github.com/NVIDIA/TensorRT-LLM/pull/17691)
  [TRTLLM-15349][feat] Mamba page table enhancements (#17691)
  _Files: `tensorrt_llm/_torch/disaggregation/base/transfer.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py`, `tensorrt_llm/_torch/disaggregation/native/mixers/attention/peer.py`, `tensorrt_llm/_torch/disaggregation/native/mixers/ssm/peer.py` _+13 more__
- **2026-08-25** [`b057f77b62`](https://github.com/NVIDIA/TensorRT-LLM/commit/b057f77b62) [#18054](https://github.com/NVIDIA/TensorRT-LLM/pull/18054)
  [https://nvbugs/6617948][fix] Restore trtllm-gen MLA decode perf gate dropped by #15300 (#18054)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tests/unittest/_torch/attention/test_fmha_page_index.py`_
- **2026-08-25** [`ef2f31df20`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef2f31df20) [#18026](https://github.com/NVIDIA/TensorRT-LLM/pull/18026)
  [None][refactor] Compose phased FMHA implementations (#18026)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/__init__.py`, `tensorrt_llm/_torch/attention_backend/fmha/combined.py`, `tensorrt_llm/_torch/attention_backend/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py` _+5 more__
- **2026-08-25** [`f1f9f00b08`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1f9f00b08) [#17796](https://github.com/NVIDIA/TensorRT-LLM/pull/17796)
  [None][feat] Kimi K3: KDA-TP + MLA-DCP (helix) wiring (#17796)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`_
- **2026-08-24** [`55548ee861`](https://github.com/NVIDIA/TensorRT-LLM/commit/55548ee861) [#18025](https://github.com/NVIDIA/TensorRT-LLM/pull/18025)
  [TRTLLM-15655][chore] BREAKING: remove star attention (#18025)
  _Files: `.pre-commit-config.yaml`, `docs/source/developer-guide/telemetry.md`, `docs/source/helper.py`, `examples/llm-api/quickstart_advanced.py` _+31 more__
- **2026-08-24** [`2f22de218d`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f22de218d) [#16224](https://github.com/NVIDIA/TensorRT-LLM/pull/16224)
  [None][feat] Enable DeepSeek-V4 and DSA (DeepSeek-V3.2/GLM) serving on SM120 via FlashInfer sparse-MLA (#16224)
  _Files: `cpp/tensorrt_llm/common/attentionOp.h`, `tensorrt_llm/_torch/attention_backend/fmha/__init__.py`, `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_sparse_mla.py` _+34 more__
- **2026-08-24** [`f3a13711a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3a13711a3) [#16951](https://github.com/NVIDIA/TensorRT-LLM/pull/16951)
  [TRTLLM-14692][feat] Overlap LoRA and base model computations (#16951)
  _Files: `tensorrt_llm/_torch/modules/attention.py`, `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/modules/mlp.py` _+6 more__
- **2026-08-24** [`f5080d7923`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5080d7923) [#18013](https://github.com/NVIDIA/TensorRT-LLM/pull/18013)
  [TRTLLM-15120][test] Prune Step-3.7-Flash functional tests (#18013)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py` _+2 more__
- **2026-08-24** [`5ee95a1037`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ee95a1037) [#17318](https://github.com/NVIDIA/TensorRT-LLM/pull/17318)
  [None][perf] Use FP8 MiniMax-M3 MSA indexer QK (#17318)
  _Files: `cpp/tensorrt_llm/kernels/minimaxM3Fp8IndexerKernel.cu`, `cpp/tensorrt_llm/kernels/minimaxM3Fp8IndexerKernel.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/minimaxM3Fp8IndexerOp.cpp` _+13 more__

## Executor / Runtime  (31 commits)

- **2026-08-31** [`03eb1a34eb`](https://github.com/NVIDIA/TensorRT-LLM/commit/03eb1a34eb) [#17377](https://github.com/NVIDIA/TensorRT-LLM/pull/17377)
  [TRTLLM-12680][feat] add exit code telemetry (#17377)
  _Files: `README.md`, `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/commands/_telemetry.py`, `tensorrt_llm/commands/bench.py` _+28 more__
- **2026-08-31** [`33d1a3cf9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/33d1a3cf9d) [#14095](https://github.com/NVIDIA/TensorRT-LLM/pull/14095)
  [TRTLLM-11412][feat] Add offloading support for visual_gen (#14095)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/executor.py` _+21 more__
- **2026-08-31** [`cfd7cf1d56`](https://github.com/NVIDIA/TensorRT-LLM/commit/cfd7cf1d56) [#16710](https://github.com/NVIDIA/TensorRT-LLM/pull/16710)
  [None][feat] KVCacheManagerV2: suspend/resume observability stat + coverage (#16710)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.h`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManagerV2.cpp` _+11 more__
- **2026-08-29** [`2bc0a99b81`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bc0a99b81) [#18395](https://github.com/NVIDIA/TensorRT-LLM/pull/18395)
  [TRTLLMINF-336][infra] BOLT profile merge: skip runtime tensorrt import gate (libs-only) (#18395)
  _Files: `scripts/bolt/internal/slurm_merge.sh`, `scripts/bolt/setup_env.sh`_
- **2026-08-28** [`c3fd8caac7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3fd8caac7) [#18318](https://github.com/NVIDIA/TensorRT-LLM/pull/18318)
  [None][chore] Refine runtime CODEOWNERs (#18318)
  _Files: `.github/CODEOWNERS`_
- **2026-08-28** [`15040dd6d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/15040dd6d7) [#18203](https://github.com/NVIDIA/TensorRT-LLM/pull/18203)
  [None][test] Unwaive test_trtllm_bench_llmapi_launch for nvbugs/6568058 (#18203)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`6c344c3860`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c344c3860) [#18186](https://github.com/NVIDIA/TensorRT-LLM/pull/18186)
  [None][refactor] Split connector KV save out of _send_kv_async (#18186)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_disagg_index_mapper_early_release.py`, `tests/unittest/_torch/executor/test_send_kv_async_split.py`_
- **2026-08-27** [`732cd83e94`](https://github.com/NVIDIA/TensorRT-LLM/commit/732cd83e94) [#17667](https://github.com/NVIDIA/TensorRT-LLM/pull/17667)
  [https://nvbugs/6384357][fix] Fail stop distributed warmup errors (#17667)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_distributed_warmup_oom.py`_
- **2026-08-27** [`6bfd454657`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bfd454657) [#18086](https://github.com/NVIDIA/TensorRT-LLM/pull/18086)
  [https://nvbugs/6572838][fix] Fix LLM-only behavior for Mistral large (#18086)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_mistral.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+6 more__
- **2026-08-27** [`4679927575`](https://github.com/NVIDIA/TensorRT-LLM/commit/4679927575) [#18130](https://github.com/NVIDIA/TensorRT-LLM/pull/18130)
  [TRTLLM-15894][feat] Responses API: complete the /v1/responses surface for agent CLIs (#18130)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/postprocess_handlers.py`, `tensorrt_llm/serve/responses_utils.py` _+9 more__
- **2026-08-27** [`88f79692f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/88f79692f9) [#17741](https://github.com/NVIDIA/TensorRT-LLM/pull/17741)
  [None][feat] k3 weight pipeline opt (#17741)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tests/unittest/_torch/modeling/test_kimi_linear_checkpoint.py` _+2 more__
- **2026-08-27** [`785c948197`](https://github.com/NVIDIA/TensorRT-LLM/commit/785c948197) [#18190](https://github.com/NVIDIA/TensorRT-LLM/pull/18190)
  [https://nvbugs/6645731][fix] align logprobs with token_ids when stopwords are trimmed (#18190)
  _Files: `tensorrt_llm/executor/result.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/executor/test_stop_word_side_output_trim.py`_
- **2026-08-27** [`9769ff1378`](https://github.com/NVIDIA/TensorRT-LLM/commit/9769ff1378) [#14290](https://github.com/NVIDIA/TensorRT-LLM/pull/14290)
  [TRTLLM-12758][feat] honor named function in tool_choice for non-harmony models (#14290)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/postprocess_handlers.py`, `tests/unittest/llmapi/apps/_test_openai_tool_call.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-08-27** [`2e70be3245`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e70be3245) [#17662](https://github.com/NVIDIA/TensorRT-LLM/pull/17662)
  [None][feat] Add locality domain runtime and bindings for Rubin (#17662)
  _Files: `cpp/tensorrt_llm/nanobind/runtime/bindings.cpp`, `cpp/tensorrt_llm/runtime/CMakeLists.txt`, `cpp/tensorrt_llm/runtime/locality_domain/localityDomainResourceConfig.h`, `cpp/tensorrt_llm/runtime/locality_domain/locality_domain_utils.cpp` _+6 more__
- **2026-08-26** [`767af6f285`](https://github.com/NVIDIA/TensorRT-LLM/commit/767af6f285) [#17531](https://github.com/NVIDIA/TensorRT-LLM/pull/17531)
  [None][perf] Cut per-iteration executor bookkeeping in the hang detector and profiler (#17531)
  _Files: `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_hang_detector_kill.py`_
- **2026-08-26** [`599448db1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/599448db1d) [#18263](https://github.com/NVIDIA/TensorRT-LLM/pull/18263)
  [None][fix] Drop the unbound is_idle guard left in the idle disagg CTX reap (#18263)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-26** [`428839007a`](https://github.com/NVIDIA/TensorRT-LLM/commit/428839007a) [#18053](https://github.com/NVIDIA/TensorRT-LLM/pull/18053)
  [None][perf] Compute response GPU timings once per batch (#18053)
  _Files: `tensorrt_llm/_torch/pyexecutor/perf_metrics_manager.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_perf_metrics_manager.py`_
- **2026-08-26** [`16260e5044`](https://github.com/NVIDIA/TensorRT-LLM/commit/16260e5044) [#18065](https://github.com/NVIDIA/TensorRT-LLM/pull/18065)
  [https://nvbugs/6525010][fix] Isolate torch compile test sessions (#18065)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`, `tests/test_common/grouped_test_utils.py`, `tests/test_common/session_reuse.py` _+2 more__
- **2026-08-26** [`46f0b7ee82`](https://github.com/NVIDIA/TensorRT-LLM/commit/46f0b7ee82) [#17575](https://github.com/NVIDIA/TensorRT-LLM/pull/17575)
  [#17574][fix] Complete zero-argument tool calls in the streaming tool parser (#17575)
  _Files: `tensorrt_llm/serve/tool_parser/base_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-08-25** [`ecbdb27e54`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecbdb27e54) [#16204](https://github.com/NVIDIA/TensorRT-LLM/pull/16204)
  [TRTLLMINF-95][infra] Add LLVM BOLT profile-generation engine and pipeline (#16204)
  _Files: `docker/Dockerfile.bolt`, `docker/Makefile`, `docker/README.md`, `jenkins/BoltProfileGen.groovy` _+19 more__
- **2026-08-25** [`c7006ffe83`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7006ffe83) [#17564](https://github.com/NVIDIA/TensorRT-LLM/pull/17564)
  [https://nvbugs/6590664][fix] Reap idle single-rank CTX transfers (#17564)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-25** [`a1b3eb6489`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1b3eb6489) [#16751](https://github.com/NVIDIA/TensorRT-LLM/pull/16751)
  [https://nvbugs/6425321][fix] remove unnecessary VSA + Ulysses NCCL flag (#16751)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_wan_vsa_ulysses.py`_
- **2026-08-25** [`29980b03a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/29980b03a1) [#17817](https://github.com/NVIDIA/TensorRT-LLM/pull/17817)
  [https://nvbugs/6581066][fix] Abort the wedged worker world when a rank dies during init (#17817)
  _Files: `tensorrt_llm/executor/proxy.py`, `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-08-25** [`0a4861dcab`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a4861dcab) [#17980](https://github.com/NVIDIA/TensorRT-LLM/pull/17980)
  [TRTLLM-15176][fix] Harden Kimi K3 tool-call parsing (#17980)
  _Files: `tensorrt_llm/serve/postprocess_handlers.py`, `tensorrt_llm/serve/tool_parser/base_tool_parser.py`, `tensorrt_llm/serve/tool_parser/kimi_k3_tool_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-08-24** [`1a1e50968d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a1e50968d) [#18116](https://github.com/NVIDIA/TensorRT-LLM/pull/18116)
  [None][fix] propagate max token limits to hybrid cache managers (#18116)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py`_
- **2026-08-24** [`9d396def3c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d396def3c) [#17642](https://github.com/NVIDIA/TensorRT-LLM/pull/17642)
  [TRTLLM-15302][fix] Reject dead prefetched MPI pools (#17642)
  _Files: `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/test_common/session_prefetcher.py`, `tests/unittest/llmapi/test_session_prefetcher.py`_
- **2026-08-24** [`127320d5dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/127320d5dd) [#17492](https://github.com/NVIDIA/TensorRT-LLM/pull/17492)
  [None][fix] fix CppMambaHybridCacheManager (#17492)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-24** [`091b560f83`](https://github.com/NVIDIA/TensorRT-LLM/commit/091b560f83) [#17202](https://github.com/NVIDIA/TensorRT-LLM/pull/17202)
  [TRTLLM-13409][fix] give the benchmark-disagg fill gate's retry loop a deadline (#17202)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`, `tests/unittest/_torch/executor/test_disagg_fill_gate_stall_bound.py`_
- **2026-08-24** [`ecd69d56f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecd69d56f0) [#17644](https://github.com/NVIDIA/TensorRT-LLM/pull/17644)
  [https://nvbugs/6581065][fix] Reap wedged workers during session drain (#17644)
  _Files: `tests/test_common/session_reuse.py`, `tests/unittest/llmapi/test_session_reuse.py`_
- **2026-08-24** [`8c1e685228`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c1e685228) [#17866](https://github.com/NVIDIA/TensorRT-LLM/pull/17866)
  [None][feat] KVCacheManagerV2: helix decode-CP via a global super-block ledger (#17866)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py` _+7 more__
- **2026-08-24** [`0db09f5b50`](https://github.com/NVIDIA/TensorRT-LLM/commit/0db09f5b50) [#18038](https://github.com/NVIDIA/TensorRT-LLM/pull/18038)
  [https://nvbugs/6627197][fix] Unwaive KV pool rebalance PP loop tests (#18038)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_kv_pool_rebalance.py`_

## MoE  (28 commits)

- **2026-08-31** [`f9d11b281a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9d11b281a) [#18344](https://github.com/NVIDIA/TensorRT-LLM/pull/18344)
  [https://nvbugs/6402009][test] unwaive Qwen3-235B NVFP4 TRTLLM MoE test (#18344)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-31** [`9332a81ce2`](https://github.com/NVIDIA/TensorRT-LLM/commit/9332a81ce2) [#18339](https://github.com/NVIDIA/TensorRT-LLM/pull/18339)
  [#18338][fix] Fix barrier-divergence races in the Blackwell CuTe DSL GVR top-k decode kernel (#18339)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-08-30** [`c5c985c4a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5c985c4a1) [#17952](https://github.com/NVIDIA/TensorRT-LLM/pull/17952)
  [TRTLLM-14843][chore] Establish _torch/moe/ and relocate MoE modules, custom ops, and communication (#17952)
- **2026-08-28** [`61aa99a968`](https://github.com/NVIDIA/TensorRT-LLM/commit/61aa99a968) [#18142](https://github.com/NVIDIA/TensorRT-LLM/pull/18142)
  [https://nvbugs/6644644][fix] Replay both verified orphan payloads onto current origin/main as a single… (#18142)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`, `tests/unittest/_torch/thop/parallel/test_cute_dsl_moe.py`_
- **2026-08-27** [`d210366ce6`](https://github.com/NVIDIA/TensorRT-LLM/commit/d210366ce6) [#18257](https://github.com/NVIDIA/TensorRT-LLM/pull/18257)
  [https://nvbugs/6650463][fix] Let CutlassFusedMoE serve MXFP8 under MiniMax SwiGLU (#18257)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`68e97d91a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/68e97d91a1) [#18144](https://github.com/NVIDIA/TensorRT-LLM/pull/18144)
  [https://nvbugs/6644468][fix] Defer the four runner imports to their sole `isinstance` use site (reached… (#18144)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`d094b51ef9`](https://github.com/NVIDIA/TensorRT-LLM/commit/d094b51ef9) [#18256](https://github.com/NVIDIA/TensorRT-LLM/pull/18256)
  [https://nvbugs/6660905][fix] Gate TritonFusedMoE on the SwiGLU family, not the gpt-oss flavour (#18256)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`c110d1dc2b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c110d1dc2b) [#17918](https://github.com/NVIDIA/TensorRT-LLM/pull/17918)
  [None][feat] laguna: config-driven sqrt-softplus router scoring (#17918)
  _Files: `tensorrt_llm/_torch/models/modeling_laguna.py`, `tensorrt_llm/_torch/modules/fused_moe/__init__.py`, `tensorrt_llm/_torch/modules/fused_moe/routing.py`_
- **2026-08-27** [`8e7a8ff719`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e7a8ff719) [#18288](https://github.com/NVIDIA/TensorRT-LLM/pull/18288)
  [https://nvbugs/6663062][fix] remove Mistral moe tests (#18288)
  _Files: `tests/integration/defs/llmapi/test_llm_api_pytorch_moe_lora.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-08-27** [`64ca8adacf`](https://github.com/NVIDIA/TensorRT-LLM/commit/64ca8adacf) [#17827](https://github.com/NVIDIA/TensorRT-LLM/pull/17827)
  [TRTLLM-15108][test] clean obsolete qwen tests (#17827)
  _Files: `tensorrt_llm/inputs/multimodal.py`, `tests/integration/defs/.test_durations`, `tests/integration/defs/.test_durations_aws_dfw`, `tests/integration/defs/accuracy/references/cnn_dailymail.yaml` _+75 more__
- **2026-08-26** [`0c68b4f69b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c68b4f69b) [#18140](https://github.com/NVIDIA/TensorRT-LLM/pull/18140)
  [https://nvbugs/6652876][fix] Add correct autotuner constraint for sm120 fp8 block scale moe (#18140)
  _Files: `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`ed94d4cfbf`](https://github.com/NVIDIA/TensorRT-LLM/commit/ed94d4cfbf) [#17821](https://github.com/NVIDIA/TensorRT-LLM/pull/17821)
  [TRTLLM-15293][perf] Add self-sampling (GVR V2) top-K decode kernels (#17821)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode_self_sampling.py` _+4 more__
- **2026-08-26** [`38c824b98e`](https://github.com/NVIDIA/TensorRT-LLM/commit/38c824b98e) [#17940](https://github.com/NVIDIA/TensorRT-LLM/pull/17940)
  [None][feat] Add nvfp4 situ moe cubins (#17940)
- **2026-08-26** [`15f92dc176`](https://github.com/NVIDIA/TensorRT-LLM/commit/15f92dc176) [#18181](https://github.com/NVIDIA/TensorRT-LLM/pull/18181)
  [TRTLLM-15748][chore] Remove dead code and de-reflect lazy attributes for ModelEngine (#18181)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_multimodal_scheduler.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine_warmup.py` _+1 more__
- **2026-08-26** [`b5875ec96c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5875ec96c) [#18136](https://github.com/NVIDIA/TensorRT-LLM/pull/18136)
  [https://nvbugs/6644448][test] Remove fixed CuTeDSL MoE waivers (#18136)
- **2026-08-25** [`14f683645a`](https://github.com/NVIDIA/TensorRT-LLM/commit/14f683645a) [#17893](https://github.com/NVIDIA/TensorRT-LLM/pull/17893)
  [None][perf] split routing kernels to reduce compile time (#17893)
  _Files: `cpp/tensorrt_llm/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomBlock.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomCluster.cu` _+4 more__
- **2026-08-25** [`59abd31d04`](https://github.com/NVIDIA/TensorRT-LLM/commit/59abd31d04) [#18068](https://github.com/NVIDIA/TensorRT-LLM/pull/18068)
  [https://nvbugs/6644448][fix] unwaive MegaMoE CuTe DSL tests (#18068)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`244c6ea70a`](https://github.com/NVIDIA/TensorRT-LLM/commit/244c6ea70a) [#18018](https://github.com/NVIDIA/TensorRT-LLM/pull/18018)
  [TRTLLM-14958][refactor] separate MoE execution units from complete layers (#18018)
  _Files: `tensorrt_llm/_torch/models/modeling_hunyuan_moe.py`, `tensorrt_llm/_torch/models/modeling_laguna.py`, `tensorrt_llm/_torch/models/modeling_llama_min_latency.py`, `tensorrt_llm/_torch/models/modeling_qwen3_moe.py` _+20 more__
- **2026-08-25** [`6c5119411d`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c5119411d) [#18133](https://github.com/NVIDIA/TensorRT-LLM/pull/18133)
  [https://nvbugs/6525059][fix] 128KiB-align TMA-OOB MoE workspace buffers on Blackwell (#18133)
  _Files: `cpp/tensorrt_llm/thop/fp8BlockScaleMoe.cpp`, `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`36b424ec35`](https://github.com/NVIDIA/TensorRT-LLM/commit/36b424ec35) [#15712](https://github.com/NVIDIA/TensorRT-LLM/pull/15712)
  [https://nvbugs/6384747][fix] Add input_ids=None to MiniMaxM3MoeRoutingMethod.apply signature and forward to… (#15712)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`cf375ce358`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf375ce358) [#17959](https://github.com/NVIDIA/TensorRT-LLM/pull/17959)
  [None][feat] Add qwen3_8 / kimi_k3 bench_moe presets and activation plumbing (#17959)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_deepgemm.py`, `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/build.py`, `tests/microbenchmarks/bench_moe/case_runner.py` _+4 more__
- **2026-08-25** [`496a002efe`](https://github.com/NVIDIA/TensorRT-LLM/commit/496a002efe) [#18094](https://github.com/NVIDIA/TensorRT-LLM/pull/18094)
  [None][fix] CuTe DSL GVR top-K decode: repair the non-converged threshold search (#18094)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-08-25** [`453308d6f6`](https://github.com/NVIDIA/TensorRT-LLM/commit/453308d6f6) [#17550](https://github.com/NVIDIA/TensorRT-LLM/pull/17550)
  [None][fix] GVR indexer top-K: repair the non-converged threshold search (#17550)
  _Files: `cpp/tensorrt_llm/kernels/heuristic_topk.cuh`, `tests/unittest/_torch/thop/parallel/test_indexer_topk.py`_
- **2026-08-25** [`3d4e91920b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d4e91920b) [#18059](https://github.com/NVIDIA/TensorRT-LLM/pull/18059)
  [None][fix] Kimi K3: bound MegaMoE expert-weight memory at EP8; drop the MoE TP/EP env overrides (#18059)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/fused_moe/quantization.py`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/unittest/_torch/modules/moe/test_kimi_k3_situ_moe.py`_
- **2026-08-25** [`0f34c8aca5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f34c8aca5) [#17951](https://github.com/NVIDIA/TensorRT-LLM/pull/17951)
  [https://nvbugs/6464169][fix] Pad trtllm-gen MoE route map to cover kernel over-read (#17951)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h`, `cpp/tensorrt_llm/thop/fp4BlockScaleMoe.cpp`, `cpp/tensorrt_llm/thop/fp8BlockScaleMoe.cpp`, `cpp/tensorrt_llm/thop/fp8PerTensorScaleMoe.cpp` _+2 more__
- **2026-08-24** [`2fa5093e8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fa5093e8f) [#17647](https://github.com/NVIDIA/TensorRT-LLM/pull/17647)
  [None][feat] Add CFT counted-write path to MoE all-to-all (#17647)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllCftManager.h`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllCftSupport.h`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h` _+7 more__
- **2026-08-24** [`27e461c171`](https://github.com/NVIDIA/TensorRT-LLM/commit/27e461c171) [#17598](https://github.com/NVIDIA/TensorRT-LLM/pull/17598)
  [TRTLLM-15099][test] Prune Mistral functional and unit tests (#17598)
  _Files: `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_cli_flow.py` _+21 more__
- **2026-08-24** [`2bb2e1c4e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bb2e1c4e6) [#17831](https://github.com/NVIDIA/TensorRT-LLM/pull/17831)
  [https://nvbugs/6601578][fix] Avoid MoE multi-GPU rendezvous port race (#17831)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/dynamic_mainloop.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/moe/test_moe_module.py`_

## Disaggregation / KV  (19 commits)

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
- **2026-08-28** [`61083f4af3`](https://github.com/NVIDIA/TensorRT-LLM/commit/61083f4af3) [#17434](https://github.com/NVIDIA/TensorRT-LLM/pull/17434)
  [TRTLLM-14604][fix] add auth for RL endpoints (#17434)
  _Files: `tensorrt_llm/serve/disagg_auth.py`, `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/rl_control_auth.py` _+3 more__
- **2026-08-28** [`3c4dc51f93`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c4dc51f93) [#17137](https://github.com/NVIDIA/TensorRT-LLM/pull/17137)
  [https://nvbugs/6480621][test] Revert to 60-second KV transfer timeout for GB300 DeepSeek V4 Pro disaggregated perf-sanity (#17137)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-v4-pro-fp4_8k1k_con180_ctx3_dep4_gen1_dep32_eplb384_mtp3_ccb-NIXL.yaml`_
- **2026-08-27** [`3035d47286`](https://github.com/NVIDIA/TensorRT-LLM/commit/3035d47286) [#17891](https://github.com/NVIDIA/TensorRT-LLM/pull/17891)
  [None][infra] Upgrade NIXL to v1.4.0 and UCX to v1.22.x (#17891)
  _Files: `docker/common/install_nixl.sh`, `docker/common/install_ucx.sh`, `examples/disaggregated/slurm/cache_transceiver_test/report.py`, `jenkins/L0_Test.groovy` _+2 more__
- **2026-08-27** [`141260367a`](https://github.com/NVIDIA/TensorRT-LLM/commit/141260367a) [#18248](https://github.com/NVIDIA/TensorRT-LLM/pull/18248)
  [None][doc] Point the dis-agg docs at transceiver v2 (#18248)
  _Files: `docs/source/developer-guide/kv-transfer.md`, `docs/source/features/disagg-serving.md`, `examples/disaggregated/README.md`, `examples/models/core/deepseek_v3/README.md` _+1 more__
- **2026-08-27** [`c170995b61`](https://github.com/NVIDIA/TensorRT-LLM/commit/c170995b61) [#17680](https://github.com/NVIDIA/TensorRT-LLM/pull/17680)
  [None][test] Consolidate ssm dis-agg E2E Tests (#17680)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`5ae89d64ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ae89d64ea) [#17324](https://github.com/NVIDIA/TensorRT-LLM/pull/17324)
  [None][fix] Simplify idle disagg KV transfer progress check (#17324)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-26** [`45f2b13263`](https://github.com/NVIDIA/TensorRT-LLM/commit/45f2b13263) [#17988](https://github.com/NVIDIA/TensorRT-LLM/pull/17988)
  [https://nvbugs/6327718][fix] Drain EPD thread pool before proxy shutdown (#17988)
  _Files: `tests/integration/defs/accuracy/test_epd_disagg_multimodal.py`_
- **2026-08-26** [`a6f6eedff2`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6f6eedff2) [#18225](https://github.com/NVIDIA/TensorRT-LLM/pull/18225)
  [None][test] Remove deepseek v32 test cases on the qa side for disagg multinode perf testing (#18225)
  _Files: `.gitignore`, `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-v32-fp4_32k4k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml` _+15 more__
- **2026-08-26** [`c2badbee8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c2badbee8e) [#18092](https://github.com/NVIDIA/TensorRT-LLM/pull/18092)
  [None][fix] Synchronize KV cache V2 host fallback across ranks (#18092)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/unittest/_torch/executor/test_kv_cache_manager_v2.py`_
- **2026-08-25** [`675e17d3d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/675e17d3d9) [#16802](https://github.com/NVIDIA/TensorRT-LLM/pull/16802)
  [https://nvbugs/5977180][fix] size KV cache and admit requests per beam width (#16802)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+3 more__
- **2026-08-24** [`88b0944dd9`](https://github.com/NVIDIA/TensorRT-LLM/commit/88b0944dd9) [#17815](https://github.com/NVIDIA/TensorRT-LLM/pull/17815)
  [None][fix] Report request-level KV cache metrics with KVCM V2 (#17815)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCacheManager.h` _+11 more__
- **2026-08-24** [`bae4fc52ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/bae4fc52ac) [#18143](https://github.com/NVIDIA/TensorRT-LLM/pull/18143)
  [None][fix] Restore CpType import for HELIX KV cache (#18143)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`_
- **2026-08-24** [`958d651b18`](https://github.com/NVIDIA/TensorRT-LLM/commit/958d651b18) [#18012](https://github.com/NVIDIA/TensorRT-LLM/pull/18012)
  [https://nvbugs/6632606][fix] Pass server_start_timeout to Ray disagg (#18012)
  _Files: `examples/ray_orchestrator/disaggregated/disagg_serving_local.sh`, `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`0f2c3a95f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f2c3a95f9) [#18090](https://github.com/NVIDIA/TensorRT-LLM/pull/18090)
  [None][fix] preserve streaming SSE event boundaries (#18090)
  _Files: `tensorrt_llm/serve/openai_client.py`, `tests/unittest/disaggregated/test_disagg_openai_client.py`_
- **2026-08-24** [`33df8c1e81`](https://github.com/NVIDIA/TensorRT-LLM/commit/33df8c1e81) [#17966](https://github.com/NVIDIA/TensorRT-LLM/pull/17966)
  [None][refactor] Move disagg transfer helpers from py_executor into disaggregation/executor (#17966)
  _Files: `tensorrt_llm/_torch/disaggregation/executor/__init__.py`, `tensorrt_llm/_torch/disaggregation/executor/admission.py`, `tensorrt_llm/_torch/disaggregation/executor/pp_termination.py`, `tensorrt_llm/_torch/disaggregation/executor/transfer_manager.py` _+5 more__

## Quantization  (18 commits)

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
- **2026-08-30** [`ffdffe8ed4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffdffe8ed4) [#18400](https://github.com/NVIDIA/TensorRT-LLM/pull/18400)
  [None][test] Unwaive GB300 MiniMax M3 NVFP4 test (#18400)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-29** [`c44de1a6cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/c44de1a6cd) [#17485](https://github.com/NVIDIA/TensorRT-LLM/pull/17485)
  [TRTLLM-15316][feat] sm107 gemm + quant (#17485)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/CMakeLists.txt`, `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`, `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_preprocessors.cpp`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp4_gemm/fp4_gemm_template.h` _+13 more__
- **2026-08-29** [`1acd695759`](https://github.com/NVIDIA/TensorRT-LLM/commit/1acd695759)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+8 more__
- **2026-08-28** [`2dddac6481`](https://github.com/NVIDIA/TensorRT-LLM/commit/2dddac6481) [#17870](https://github.com/NVIDIA/TensorRT-LLM/pull/17870)
  [TRTLLM-15498][perf] optimize Kimi KDA prefill convolution data flow (#17870)
  _Files: `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+11 more__
- **2026-08-28** [`e8d76729f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8d76729f7) [#17502](https://github.com/NVIDIA/TensorRT-LLM/pull/17502)
  [https://nvbugs/6581071][fix] Pass the SM explicitly as `is_nvfp4_marlin_supported_sm(get_sm_version())` so… (#17502)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/test_w4a16_nvfp4_linear.py`_
- **2026-08-28** [`c845c18abf`](https://github.com/NVIDIA/TensorRT-LLM/commit/c845c18abf)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+6 more__
- **2026-08-28** [`4107854ff3`](https://github.com/NVIDIA/TensorRT-LLM/commit/4107854ff3) [#18134](https://github.com/NVIDIA/TensorRT-LLM/pull/18134)
  [None][feat] Make the Python KV-cache transceiver the default runtime (#18134)
  _Files: `examples/disaggregated/slurm/service_discovery_example/launch.slurm`, `examples/disaggregated/slurm/simple_example/ctx_extra-llm-api-config.yaml`, `examples/disaggregated/slurm/simple_example/gen_extra-llm-api-config.yaml`, `examples/dwdp/reproduce.py` _+16 more__
- **2026-08-27** [`f946837a50`](https://github.com/NVIDIA/TensorRT-LLM/commit/f946837a50)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+8 more__
- **2026-08-26** [`0cb928b72e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0cb928b72e) [#18219](https://github.com/NVIDIA/TensorRT-LLM/pull/18219)
  [https://nvbugs/6647310][chore] Unwaive TestLagunaXS::test_nvfp4 (#18219)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-26** [`6c69da71e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c69da71e0) [#18139](https://github.com/NVIDIA/TensorRT-LLM/pull/18139)
  [https://nvbugs/6428063][chore] Unwaive the DeepSeekV3Lite nvfp4 pp4 test (#18139)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`ec8cf6b832`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec8cf6b832) [#18180](https://github.com/NVIDIA/TensorRT-LLM/pull/18180)
  [None][test] Add Nemotron-3.5-Lightning NVFP4 Marlin MTP3 accuracy test (#18180)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+1 more__
- **2026-08-25** [`eb71774e94`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb71774e94) [#17819](https://github.com/NVIDIA/TensorRT-LLM/pull/17819)
  [https://nvbugs/5961814][unwaive] Unwaive DeepSeek V3 Lite NVFP4 test (#17819)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`be69541924`](https://github.com/NVIDIA/TensorRT-LLM/commit/be69541924) [#18056](https://github.com/NVIDIA/TensorRT-LLM/pull/18056)
  [https://nvbugs/6633928][fix] Limit Gemma3 FP8 accuracy test sequence length (#18056)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-08-24** [`c564f4925b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c564f4925b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+5 more__

## Models  (14 commits)

- **2026-08-29** [`cb511b53d6`](https://github.com/NVIDIA/TensorRT-LLM/commit/cb511b53d6) [#18218](https://github.com/NVIDIA/TensorRT-LLM/pull/18218)
  [TRTLLM-15376][test] expand Gemma 4 MTP QA coverage (#18218)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/qa/llm_function_core.txt`_
- **2026-08-29** [`7b60a569a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b60a569a9) [#18274](https://github.com/NVIDIA/TensorRT-LLM/pull/18274)
  [None][fix] Fix Gemma4 video token counting (#18274)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tests/unittest/_torch/modeling/test_gemma4_multimodal.py`_
- **2026-08-28** [`ef3124d198`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef3124d198) [#18390](https://github.com/NVIDIA/TensorRT-LLM/pull/18390)
  [None][ci] Waive flaky TestGemma3_1BInstruct::test_auto_dtype[False] disagg test (#18390)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`32655aba8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/32655aba8b) [#18371](https://github.com/NVIDIA/TensorRT-LLM/pull/18371)
  [https://nvbugs/6669206][test] Unwaive test_kimi_k3_gen_dep[1] fixed by #18226 (#18371)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`5767bed025`](https://github.com/NVIDIA/TensorRT-LLM/commit/5767bed025) [#18189](https://github.com/NVIDIA/TensorRT-LLM/pull/18189)
  [https://nvbugs/6571418][test] Unwaive DeepSeek-V4-Pro GSM8K accuracy (#18189)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-28** [`40b9cbc2f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/40b9cbc2f4) [#18306](https://github.com/NVIDIA/TensorRT-LLM/pull/18306)
  [https://nvbugs/6670227][fix] Drop redundant min_tokens from DSv4-Pro token-boundary smoke (#18306)
  _Files: `tests/integration/defs/examples/test_deepseek_v4_pro.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`3fde2c5a64`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fde2c5a64) [#18325](https://github.com/NVIDIA/TensorRT-LLM/pull/18325)
  [https://nvbugs/6681216][infra] Waive DeepSeek V3 Lite NIXL on B200 and B300 (#18325)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-27** [`8d6bf992e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d6bf992e0) [#17922](https://github.com/NVIDIA/TensorRT-LLM/pull/17922)
  [TRTLLM-15036][test] Add Kimi K3 GSM8K/MMMU accuracy tests and register them in QA's weekly multinode list (#17922)
  _Files: `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+2 more__
- **2026-08-27** [`d0d0173fd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0d0173fd8) [#18089](https://github.com/NVIDIA/TensorRT-LLM/pull/18089)
  [https://nvbugs/6571410][fix] Move Gemma4 perf test to post-merge (#18089)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_b200_perf_sanity.yml`_
- **2026-08-27** [`b460237a9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b460237a9c) [#17862](https://github.com/NVIDIA/TensorRT-LLM/pull/17862)
  [TRTLLM-15498][perf] fuse KDA beta preprocessing and isolate FLA fallbacks (#17862)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/kimi_k3_kda/fused_k123.py`, `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py` _+4 more__
- **2026-08-27** [`e8fd8c078c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8fd8c078c) [#17887](https://github.com/NVIDIA/TensorRT-LLM/pull/17887)
  [TRTLLM-15498][perf] eliminate KDA recurrent-state and metadata copies (#17887)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_kimi_k3_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/kimi_k3_kda/k4_persistent.py`, `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py` _+11 more__
- **2026-08-27** [`36138a2c8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/36138a2c8e) [#18185](https://github.com/NVIDIA/TensorRT-LLM/pull/18185)
  [https://nvbugs/6644226][fix] Reduce DeepSeek V4 EPLB loading memory (#18185)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_deepseekv4.py`_
- **2026-08-25** [`c86582b75a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c86582b75a) [#18071](https://github.com/NVIDIA/TensorRT-LLM/pull/18071)
  [TRTLLM-15719][test] add Qwen3.8-2.4T-A95B accuracy guards (#18071)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/conftest.py`, `tests/integration/test_lists/qa/llm_function_multinode.txt`_
- **2026-08-24** [`ec3ff2e7f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec3ff2e7f5) [#18062](https://github.com/NVIDIA/TensorRT-LLM/pull/18062)
  [None][test] Set Llama4 QA max sequence length (#18062)
  _Files: `tests/integration/defs/test_e2e.py`_

## Torch Path (_torch)  (13 commits)

- **2026-08-28** [`2938adaf3c`](https://github.com/NVIDIA/TensorRT-LLM/commit/2938adaf3c) [#17325](https://github.com/NVIDIA/TensorRT-LLM/pull/17325)
  [None][feat] Cosmos3 action generation (#17325)
  _Files: `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `examples/visual_gen/models/cosmos3/prompts/action_forward_dynamics.json`, `examples/visual_gen/models/cosmos3/prompts/action_inverse_dynamics.json` _+25 more__
- **2026-08-28** [`648e717723`](https://github.com/NVIDIA/TensorRT-LLM/commit/648e717723) [#18082](https://github.com/NVIDIA/TensorRT-LLM/pull/18082)
  [None][perf] Fuse relu2 into a single elementwise kernel (#18082)
  _Files: `tensorrt_llm/_torch/fused_relu2_triton.py`, `tensorrt_llm/_torch/utils.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/test_fused_relu2.py`_
- **2026-08-27** [`0a41020f6d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a41020f6d) [#17505](https://github.com/NVIDIA/TensorRT-LLM/pull/17505)
  [https://nvbugs/6581067][fix] Request the unbiased GEMM in fp32 and add `bias.float()` before a single cast… (#17505)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/thop/parallel/test_fp4_linear.py`_
- **2026-08-26** [`590c2fda80`](https://github.com/NVIDIA/TensorRT-LLM/commit/590c2fda80) [#18162](https://github.com/NVIDIA/TensorRT-LLM/pull/18162)
  [None][fix] Multimodal Mixin Guided Decoder Delegation (#18162)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`_
- **2026-08-26** [`f4fbe29b8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4fbe29b8b) [#17555](https://github.com/NVIDIA/TensorRT-LLM/pull/17555)
  [None][perf] use native Wan VAE for Cosmos3 (#17555)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/models/wan/parallel_vae.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_parallel_vae.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_pipeline.py` _+1 more__
- **2026-08-25** [`1d4a71f750`](https://github.com/NVIDIA/TensorRT-LLM/commit/1d4a71f750) [#17623](https://github.com/NVIDIA/TensorRT-LLM/pull/17623)
  [None][chore] Unwaive flaky accuracy tests (#17623)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-25** [`e8eb6908a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8eb6908a9) [#17490](https://github.com/NVIDIA/TensorRT-LLM/pull/17490)
  [TRTLLM-13143][feat] BREAKING: VisualGen serving API: response_format support path and modify async job status (#17490)
  _Files: `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/models/visual-generation.md`, `docs/source/release-notes.md`, `examples/visual_gen/serve/README.md` _+11 more__
- **2026-08-25** [`d928429083`](https://github.com/NVIDIA/TensorRT-LLM/commit/d928429083) [#17539](https://github.com/NVIDIA/TensorRT-LLM/pull/17539)
  [#17522][fix] Restore conv_state ordering barriers in the Triton conv kernels (#17539)
  _Files: `tensorrt_llm/_torch/modules/mamba/causal_conv1d_triton.py`_
- **2026-08-25** [`7e6c0b205e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e6c0b205e) [#17946](https://github.com/NVIDIA/TensorRT-LLM/pull/17946)
  [https://nvbugs/6619882][test] Unwaive unittest/_torch/sampler on DGX_B200 (#17946)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`6da64ef1ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/6da64ef1ad) [#17949](https://github.com/NVIDIA/TensorRT-LLM/pull/17949)
  [https://nvbugs/6631019][fix] Add a `torch_compiling(enable)` contextmanager to `_torch/utils.py` and lower… (#17949)
  _Files: `tensorrt_llm/_torch/models/modeling_radio.py`, `tensorrt_llm/_torch/models/multimodal_encoder_graph.py`, `tensorrt_llm/_torch/utils.py`, `tests/integration/test_lists/test-db/l0_cpu.yml` _+4 more__
- **2026-08-24** [`a7b3276701`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7b3276701) [#17696](https://github.com/NVIDIA/TensorRT-LLM/pull/17696)
  [TRTLLM-15401][fix] VisualGen Wan: collapse uniform per-patch timesteps — unlock TeaCache on Wan2.2-TI2V-5B (#17696)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`_
- **2026-08-24** [`46fa03d533`](https://github.com/NVIDIA/TensorRT-LLM/commit/46fa03d533) [#18063](https://github.com/NVIDIA/TensorRT-LLM/pull/18063)
  [TRTLLM-14851][chore] Relocate VisualGen kernel tests (#18063)
  _Files: `.github/CODEOWNERS`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_b300.yml`, `tests/integration/test_lists/test-db/l0_gb300.yml` _+7 more__
- **2026-08-24** [`4baa757f97`](https://github.com/NVIDIA/TensorRT-LLM/commit/4baa757f97) [#17695](https://github.com/NVIDIA/TensorRT-LLM/pull/17695)
  [TRTLLM-15400][perf] fuse per-token AdaLN for VisualGen Wan 2.2 5B (#17695)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/pertoken_adaln.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/reduce.py`, `tensorrt_llm/_torch/visual_gen/models/wan/transformer_wan.py` _+4 more__

## LoRA  (8 commits)

- **2026-08-28** [`11d8ef198c`](https://github.com/NVIDIA/TensorRT-LLM/commit/11d8ef198c) [#17845](https://github.com/NVIDIA/TensorRT-LLM/pull/17845)
  [TRTLLM-14764][feat] trtllm-serve: Kimi K3 API compliance for the Kimi Vendor Verifier (KVV) (#17845)
  _Files: `docs/source/deployment-guide/deployment-guide-for-kimi-k3-on-trtllm.md`, `tensorrt_llm/_torch/models/modeling_kimi_k3_vl.py`, `tensorrt_llm/executor/postproc_worker.py`, `tensorrt_llm/inputs/utils.py` _+10 more__
- **2026-08-28** [`ad84866c81`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad84866c81) [#18200](https://github.com/NVIDIA/TensorRT-LLM/pull/18200)
  [TRTLLM-15314][fix] recalculate PEFT cache capacity for adapter dtype (#18200)
  _Files: `cpp/include/tensorrt_llm/batch_manager/peftCacheManager.h`, `cpp/include/tensorrt_llm/runtime/loraCache.h`, `cpp/tensorrt_llm/batch_manager/peftCacheManager.cpp`, `cpp/tensorrt_llm/runtime/loraCache.cpp` _+1 more__
- **2026-08-26** [`7fbfd3e2a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7fbfd3e2a1) [#16707](https://github.com/NVIDIA/TensorRT-LLM/pull/16707)
  [https://nvbugs/6459792][fix] Teach bench ModelConfig about kv_lora_rank/qk_rope_head_dim (with… (#16707)
  _Files: `tensorrt_llm/bench/tuning/dataclasses.py`, `tensorrt_llm/bench/tuning/heuristics.py`_
- **2026-08-25** [`16c32cce57`](https://github.com/NVIDIA/TensorRT-LLM/commit/16c32cce57) [#17412](https://github.com/NVIDIA/TensorRT-LLM/pull/17412)
  [TRTLLM-15192][feat] Specialize CUDA graphs for LoRA (#17412)
  _Files: `tensorrt_llm/_torch/peft/lora/config.py`, `tensorrt_llm/_torch/peft/lora/cuda_graph_lora_manager.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+5 more__
- **2026-08-25** [`87f9ba2235`](https://github.com/NVIDIA/TensorRT-LLM/commit/87f9ba2235) [#18184](https://github.com/NVIDIA/TensorRT-LLM/pull/18184)
  [https://nvbugs/6566707][fix] Isolate LoRA peft-cache-override test from MPI session reuse (#18184)
  _Files: `tests/unittest/llmapi/test_llm_pytorch.py`_
- **2026-08-24** [`95af10a8f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/95af10a8f1) [#18114](https://github.com/NVIDIA/TensorRT-LLM/pull/18114)
  [TRTLLM-15314][test] Add LoRA manager tests to H100 L0 (#18114)
  _Files: `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-08-24** [`d03aebec63`](https://github.com/NVIDIA/TensorRT-LLM/commit/d03aebec63) [#17435](https://github.com/NVIDIA/TensorRT-LLM/pull/17435)
  [TRTLLM-14622][feat] Add VisualGen dynamic LoRA support (#17435)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/pipeline.py`, `tensorrt_llm/_torch/visual_gen/pipeline_loader.py` _+7 more__
- **2026-08-24** [`57212666fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/57212666fa) [#17464](https://github.com/NVIDIA/TensorRT-LLM/pull/17464)
  [https://nvbugs/6456085][fix] Harmony: stop discarding malformed tool-call messages silently (#17464)
  _Files: `tensorrt_llm/serve/harmony_adapter.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/apps/test_harmony_parsing.py`_

## Other  (8 commits)

- **2026-08-28** [`7b4f74070a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b4f74070a) [#15497](https://github.com/NVIDIA/TensorRT-LLM/pull/15497)
  [https://nvbugs/6337228][fix] In tests/unittest/tools/test_layer_wise_benchmarks.py, replace check_call with… (#15497)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/tools/test_layer_wise_benchmarks.py`_
- **2026-08-28** [`263921face`](https://github.com/NVIDIA/TensorRT-LLM/commit/263921face) [#18346](https://github.com/NVIDIA/TensorRT-LLM/pull/18346)
  [None][test] Don't force disable_overlap_scheduler for perf-sanity ctx_only tests (#18346)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-08-27** [`528a5308a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/528a5308a9) [#18197](https://github.com/NVIDIA/TensorRT-LLM/pull/18197)
  [TRTLLM-15316][feat] Rubin sm107 trtllm-gen gemms (#18197)
- **2026-08-27** [`52b4279b8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/52b4279b8b) [#18235](https://github.com/NVIDIA/TensorRT-LLM/pull/18235)
  [None][chore] Make disagg test paths sole-owned by disagg-devs (#18235)
  _Files: `.github/CODEOWNERS`_
- **2026-08-27** [`aaa62b293c`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaa62b293c) [#18287](https://github.com/NVIDIA/TensorRT-LLM/pull/18287)
  [None][test] Remove unused performance test utilities and clean up test list configurations in llm_perf_core.yml. (#18287)
  _Files: `tests/integration/defs/perf/test_utils.py`, `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-08-26** [`1c3d13b1c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c3d13b1c5) [#18246](https://github.com/NVIDIA/TensorRT-LLM/pull/18246)
  [None][chore] Add Top-K code owners (#18246)
  _Files: `.github/CODEOWNERS`_
- **2026-08-24** [`d9329fb8d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9329fb8d3) [#18095](https://github.com/NVIDIA/TensorRT-LLM/pull/18095)
  [https://nvbugs/6625710][fix] Re-attach radix-tree blocks detached under a live request (#18095)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/exceptions.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp` _+4 more__
- **2026-08-24** [`ce6306bb4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce6306bb4a) [#15487](https://github.com/NVIDIA/TensorRT-LLM/pull/15487)
  [https://nvbugs/6337226][fix] Count profiled calls with min() of positive line hits (#15487)
  _Files: `tests/unittest/tools/test_host_profiler.py`_

## Docs / Examples  (7 commits)

- **2026-08-31** [`12f5545729`](https://github.com/NVIDIA/TensorRT-LLM/commit/12f5545729) [#18402](https://github.com/NVIDIA/TensorRT-LLM/pull/18402)
  [None][chore] Bump version to 1.3.0rc26 (#18402)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-08-31** [`3d2b26e570`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d2b26e570) [#18408](https://github.com/NVIDIA/TensorRT-LLM/pull/18408)
  [None][test] key perf-sanity case identity on test case name (#18408)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/perf_regression_utils.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/test_common/perf_sanity_matching.py` _+2 more__
- **2026-08-28** [`c7b8ec26fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7b8ec26fa) [#18358](https://github.com/NVIDIA/TensorRT-LLM/pull/18358)
  [None][doc] Add human-in-the-loop section to modeling-bringup README (#18358)
  _Files: `agent-flow/agent_flow/workflows/modeling_bringup/README.md`, `agent-flow/agent_flow/workflows/modeling_bringup/docs/human-in-the-loop.svg`_
- **2026-08-28** [`96c8d567bd`](https://github.com/NVIDIA/TensorRT-LLM/commit/96c8d567bd) [#18330](https://github.com/NVIDIA/TensorRT-LLM/pull/18330)
  [None][feat] Add perf-analyze and perf-optimize workflows to agent-flow (#18330)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/backends/base.py`, `agent-flow/agent_flow/backends/claude_code.py`, `agent-flow/agent_flow/backends/codex.py` _+65 more__
- **2026-08-26** [`9a200a571b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a200a571b) [#18201](https://github.com/NVIDIA/TensorRT-LLM/pull/18201)
  [https://nvbugs/6647349][fix] Replace FuzzyWuzzy with RapidFuzz (#18201)
  _Files: `examples/longbench/eval_longbench_v1.py`, `examples/longbench/requirements.txt`, `requirements-dev.txt`, `security_scanning/examples/longbench/poetry.lock` _+2 more__
- **2026-08-25** [`6ac5bde845`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ac5bde845) [#18011](https://github.com/NVIDIA/TensorRT-LLM/pull/18011)
  [None][test] Revert the gen_only warmup probe and fix the per-iter device step time metric (#18011)
  _Files: `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/unittest/scripts/test_perf_sanity_helpers.py`_
- **2026-08-24** [`97e94e1796`](https://github.com/NVIDIA/TensorRT-LLM/commit/97e94e1796) [#18108](https://github.com/NVIDIA/TensorRT-LLM/pull/18108)
  [None][doc] Fix some typos of modeling agent (#18108)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/workflows/modeling_bringup/quick_start.md`_

## Speculative Decoding  (7 commits)

- **2026-08-31** [`36808bd812`](https://github.com/NVIDIA/TensorRT-LLM/commit/36808bd812) [#18416](https://github.com/NVIDIA/TensorRT-LLM/pull/18416)
  [None][test] Add MiniMax-M3 disaggregated perf recipes to QA multi-node list (#18416)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep16_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con256_ctx4_tp4_gen1_dep8_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb300_minimax-m3-fp4_8k1k_con30_ctx1_tep2_gen2_tp4_eplb0_eagle3_ccb-NIXL.yaml` _+1 more__
- **2026-08-25** [`5b1a27357a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b1a27357a) [#17955](https://github.com/NVIDIA/TensorRT-LLM/pull/17955)
  [TRTLLM-15621][fix] Reject sampling params the one-model speculative path cannot honor (#17955)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler_common.py`, `tensorrt_llm/_torch/speculative/spec_sampler_base.py`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-08-25** [`7299f8c600`](https://github.com/NVIDIA/TensorRT-LLM/commit/7299f8c600) [#18170](https://github.com/NVIDIA/TensorRT-LLM/pull/18170)
  [https://nvbugs/6627979][fix] Apply chat template in test_eagle3_output_repetition_4gpus (#18170)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-24** [`fa787a8c27`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa787a8c27) [#18069](https://github.com/NVIDIA/TensorRT-LLM/pull/18069)
  [None][feat] Optimize human trigger replan for modeling agent (#18069)
  _Files: `agent-flow/agent_flow/workflows/agent_team/progress.py`, `agent-flow/agent_flow/workflows/agent_team/state.py`, `agent-flow/agent_flow/workflows/agent_team/workflow.py`, `agent-flow/agent_flow/workflows/modeling_bringup/prompts/coder_extra.py` _+6 more__
- **2026-08-24** [`38c25ce315`](https://github.com/NVIDIA/TensorRT-LLM/commit/38c25ce315) [#17890](https://github.com/NVIDIA/TensorRT-LLM/pull/17890)
  [None][chore] Split TorchSampler feature code out of sampler.py (#17890)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/pyexecutor/sampler/__init__.py`, `tensorrt_llm/_torch/pyexecutor/sampler/beam_search.py`, `tensorrt_llm/_torch/pyexecutor/sampler/logprobs.py` _+10 more__
- **2026-08-24** [`c82fabff54`](https://github.com/NVIDIA/TensorRT-LLM/commit/c82fabff54) [#17710](https://github.com/NVIDIA/TensorRT-LLM/pull/17710)
  [None][fix] Refresh group greedy state per iteration (#17710)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/test_group_all_greedy_sync.py`_
- **2026-08-24** [`df437526a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/df437526a2) [#17998](https://github.com/NVIDIA/TensorRT-LLM/pull/17998)
  [https://nvbugs/6550099][fix] Raise no-top-k equivalence tolerance (#17998)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/speculative/hw_agnostic/test_advanced_sampling_mode.py`_

## AutoDeploy  (4 commits)

- **2026-08-31** [`db1ce32d0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/db1ce32d0d) [#18422](https://github.com/NVIDIA/TensorRT-LLM/pull/18422)
  [TRTLLM-15883][infra] clarify CBTS fallback diagnostics (#18422)
  _Files: `jenkins/scripts/cbts/coverage_selection/artifact.py`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/_helpers.py`, `jenkins/scripts/cbts/rules/auto_deploy_rule.py` _+5 more__
- **2026-08-26** [`cd508a1ccf`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd508a1ccf) [#18107](https://github.com/NVIDIA/TensorRT-LLM/pull/18107)
  [None][ci] disable autodeploy test stages (#18107)
  _Files: `AGENTS.md`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/test_lists/qa/llm_function_core.txt` _+9 more__
- **2026-08-26** [`249bad43ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/249bad43ce)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-08-25** [`f9938a1053`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9938a1053)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock` _+4 more__

---
_Generated 2026-08-31 16:10 UTC_