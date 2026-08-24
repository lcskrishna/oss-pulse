# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-08-17 → 2026-08-24  |  **Total commits:** 232

## ✨ New Features This Week

- **2026-08-24** [#17435](https://github.com/NVIDIA/TensorRT-LLM/pull/17435) — [TRTLLM-14622][feat] Add VisualGen dynamic LoRA support (#17435)
- **2026-08-24** [#17866](https://github.com/NVIDIA/TensorRT-LLM/pull/17866) — [None][feat] KVCacheManagerV2: helix decode-CP via a global super-block ledger (#17866)
- **2026-08-23** [#17521](https://github.com/NVIDIA/TensorRT-LLM/pull/17521) — [TRTLLM-15314][feat] Add FP8 LoRA support for B200 (#17521)
- **2026-08-22** [#17800](https://github.com/NVIDIA/TensorRT-LLM/pull/17800) — [TRTLLM-15033][feat] Upstream Kimi K3 MLA decode backend selection to main (#17800)
- **2026-08-22** [#16394](https://github.com/NVIDIA/TensorRT-LLM/pull/16394) — [TRTLLM-14268][feat] Cosmos3 Transfer (control-video conditioning) (#16394)
- **2026-08-21** [#17512](https://github.com/NVIDIA/TensorRT-LLM/pull/17512) — [None][feat] Add cold-page codec support to KVCM2 (#17512)
- **2026-08-21** [#17889](https://github.com/NVIDIA/TensorRT-LLM/pull/17889) — [TRTLLM-15304][perf] add low-M BF16 GEMM dispatcher for SM10x decode (#17889)
- **2026-08-21** [#18057](https://github.com/NVIDIA/TensorRT-LLM/pull/18057) — [None][infra] Add blossom-ci authorized users (#18057)
- **2026-08-21** [#17865](https://github.com/NVIDIA/TensorRT-LLM/pull/17865) — [None][feat] bring up Kimi K3 NVFP4 with CUTLASS and cuteDSL MegaMoE SiTU (#17865)
- **2026-08-20** [#16230](https://github.com/NVIDIA/TensorRT-LLM/pull/16230) — [None][doc] Add tech blog: Evaluating Agentic Serving with Trace Replay and Job-Level Metrics (#16230)
- _…and 23 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-19** [`8e48971814`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e48971814) [#17657](https://github.com/NVIDIA/TensorRT-LLM/pull/17657) — [None][chore] Extend OpenEngine ownership to dynamo dev (#17657)
- **2026-08-17** [`b539ad220b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b539ad220b) [#16303](https://github.com/NVIDIA/TensorRT-LLM/pull/16303) — [https://nvbugs/6445494][infra] Upgrade Triton to 3.7.0 for Torch 2.12.0 compatibility (#16303)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#17665](https://github.com/NVIDIA/TensorRT-LLM/issues/17665) | [Bug]: NIXL cache-transceiver hangs forever if a single completion not | Disaggregated serving | 2026-08-22 |
| [#18085](https://github.com/NVIDIA/TensorRT-LLM/issues/18085) | [RFC] DFlash2 for Qwen3.8 on consumer Blackwell: integration boundary  | Speculative Decoding | 2026-08-21 |
| [#17522](https://github.com/NVIDIA/TensorRT-LLM/issues/17522) | [Bug]: causal_conv1d_triton overwrites conv_state while the convolutio | bug, Triton backend | 2026-08-19 |
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
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-26 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 68 |
| Executor / Runtime | 27 |
| MoE | 24 |
| Attention | 23 |
| Disaggregation / KV | 19 |
| Quantization | 17 |
| Torch Path (_torch) | 14 |
| Models | 10 |
| Speculative Decoding | 7 |
| Other | 6 |
| Docs / Examples | 6 |
| LoRA | 5 |
| Perf | 2 |
| ROCm / AMD | 2 |
| AutoDeploy | 1 |
| Compilation / Graph | 1 |

## CI / Infra  (68 commits)

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
- **2026-08-23** [`6281c5b009`](https://github.com/NVIDIA/TensorRT-LLM/commit/6281c5b009)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-08-23** [`056ea3d639`](https://github.com/NVIDIA/TensorRT-LLM/commit/056ea3d639)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/ray_orchestrator/pyproject.toml`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
- **2026-08-21** [`e523b6aef9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e523b6aef9) [#18027](https://github.com/NVIDIA/TensorRT-LLM/pull/18027)
  [None][test] Unwaive tests for NVBug 6507113 (#18027)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`828e765a78`](https://github.com/NVIDIA/TensorRT-LLM/commit/828e765a78) [#17989](https://github.com/NVIDIA/TensorRT-LLM/pull/17989)
  [https://nvbugs/6618102][chore] Unwaive multi gpu pp tests (#17989)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`4153606091`](https://github.com/NVIDIA/TensorRT-LLM/commit/4153606091) [#18076](https://github.com/NVIDIA/TensorRT-LLM/pull/18076)
  [None][fix] test_cbts_coverage_pilot: use capfd to avoid autouse-fixture clash (#18076)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/scripts/test_cbts_coverage_pilot.py`_
- **2026-08-21** [`8cfa341332`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cfa341332) [#18080](https://github.com/NVIDIA/TensorRT-LLM/pull/18080)
  [None][infra] Waive 1 failed cases for main in pre-merge 55687 (#18080)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`d32c27c7ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/d32c27c7ce) [#17967](https://github.com/NVIDIA/TensorRT-LLM/pull/17967)
  [None][test] Unwaive 17 recovered perf-sanity test_e2e cases (#17967)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`f6d7404652`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6d7404652) [#18006](https://github.com/NVIDIA/TensorRT-LLM/pull/18006)
  [https://nvbugs/6329155][fix] Raise glm5 tep8 8k1k max_num_tokens to 8192 to fit isl=8192 prefill (#18006)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/aggregated/glm5_fp4_blackwell.yaml`_
- **2026-08-21** [`d40b8bc15d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d40b8bc15d) [#18077](https://github.com/NVIDIA/TensorRT-LLM/pull/18077)
  [None][infra] Waive 1 failed cases for main in pre-merge 55595 (#18077)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`a1245d4605`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1245d4605) [#17975](https://github.com/NVIDIA/TensorRT-LLM/pull/17975)
  [TRTLLMINF-136][infra] Strengthen check_test_list.py param-ID validation and gate on validate<->collection parity (#17975)
  _Files: `.github/workflows/precommit-check.yml`, `jenkins/L0_Test.groovy`, `scripts/check_test_list.py`, `tests/integration/defs/sysinfo/get_sysinfo.py` _+2 more__
- **2026-08-21** [`b024d1dbd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/b024d1dbd8) [#17996](https://github.com/NVIDIA/TensorRT-LLM/pull/17996)
  [None][infra] cbts-v2 coverage pilot allowlist (#17996)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/coverage_pilot.py`, `tests/unittest/scripts/test_cbts_coverage_pilot.py`_
- **2026-08-21** [`ddd65b8e63`](https://github.com/NVIDIA/TensorRT-LLM/commit/ddd65b8e63) [#18057](https://github.com/NVIDIA/TensorRT-LLM/pull/18057)
  [None][infra] Add blossom-ci authorized users (#18057)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-08-21** [`8780bb000c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8780bb000c) [#18047](https://github.com/NVIDIA/TensorRT-LLM/pull/18047)
  [None][infra] Cap diffusers<0.40 to avoid deps conflicts (#18047)
  _Files: `requirements.txt`_
- **2026-08-21** [`1612e17b43`](https://github.com/NVIDIA/TensorRT-LLM/commit/1612e17b43) [#18048](https://github.com/NVIDIA/TensorRT-LLM/pull/18048)
  [None][infra] Waive 15 failed cases for main in post-merge 2920 (#18048)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`d556198fd2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d556198fd2) [#18010](https://github.com/NVIDIA/TensorRT-LLM/pull/18010)
  [https://nvbugs/6602094][test] Unwaive RocketKV model tests (#18010)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`5c6d743488`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c6d743488) [#18040](https://github.com/NVIDIA/TensorRT-LLM/pull/18040)
  [None][ci] waive pre-existing test failures on main (#18040)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-21** [`9656c9c0fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9656c9c0fb) [#16531](https://github.com/NVIDIA/TensorRT-LLM/pull/16531)
  [https://nvbugs/6467684][fix] Bump the golang image tag to `1.23`  (#16531)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-20** [`e189237f0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/e189237f0c) [#15552](https://github.com/NVIDIA/TensorRT-LLM/pull/15552)
  [None][infra] Trigger PLC source code scannning pipeline in pre-merge (#15552)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-08-20** [`0fdc9169fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fdc9169fa) [#18029](https://github.com/NVIDIA/TensorRT-LLM/pull/18029)
  [https://nvbugs/6608387][ci] Waive flaky test_overlap_scheduler_block_reuse_cache_hit[TorchSampler] (#18029)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`4bb38b2b39`](https://github.com/NVIDIA/TensorRT-LLM/commit/4bb38b2b39) [#17993](https://github.com/NVIDIA/TensorRT-LLM/pull/17993)
  [None][fix] Keep sysinfo distro probe working without the distro module; fail empty test-list renders loudly (#17993)
  _Files: `jenkins/L0_Test.groovy`, `requirements-dev.txt`, `tests/integration/defs/sysinfo/get_sysinfo.py`_
- **2026-08-20** [`b0597ac320`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0597ac320) [#18007](https://github.com/NVIDIA/TensorRT-LLM/pull/18007)
  [None][infra] Waive 1 failed cases for main in post-merge 2917 (#18007)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`c30f71365c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c30f71365c) [#18017](https://github.com/NVIDIA/TensorRT-LLM/pull/18017)
  [None][ci] waive pre-existing test failures on main (#18017)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`88c3f045a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/88c3f045a9) [#18004](https://github.com/NVIDIA/TensorRT-LLM/pull/18004)
  [None][fix] Pin distro for CI sysinfo detection (#18004)
  _Files: `requirements-dev.txt`_
- **2026-08-20** [`22eccabc24`](https://github.com/NVIDIA/TensorRT-LLM/commit/22eccabc24) [#17995](https://github.com/NVIDIA/TensorRT-LLM/pull/17995)
  [None][infra] Waive 12 failed cases for main in post-merge 2918 (#17995)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`c05cbe2810`](https://github.com/NVIDIA/TensorRT-LLM/commit/c05cbe2810) [#17938](https://github.com/NVIDIA/TensorRT-LLM/pull/17938)
  [TRTLLMINF-320][infra] Extend infra-scoped fail-fast deferral to SLURM-scoped aborts (#17938)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-19** [`d0bb6ac13b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0bb6ac13b) [#17645](https://github.com/NVIDIA/TensorRT-LLM/pull/17645)
  [None][fix] Don't infra-retry deterministic SLURM test failures (#17645)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-19** [`7a63a33f97`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a63a33f97) [#17941](https://github.com/NVIDIA/TensorRT-LLM/pull/17941)
  [None][ci] waive pre-existing test failures on main (#17941)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`bb53037536`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb53037536) [#16776](https://github.com/NVIDIA/TensorRT-LLM/pull/16776)
  [TRTLLM-12838][infra] CBTS: coverage-based test selection (#16776)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/blocks.py` _+13 more__
- **2026-08-19** [`14ef94ccae`](https://github.com/NVIDIA/TensorRT-LLM/commit/14ef94ccae) [#17963](https://github.com/NVIDIA/TensorRT-LLM/pull/17963)
  [https://nvbugs/6578853][test] Unwaive layer-wise benchmarks performance alignment test (#17963)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`470d6038b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/470d6038b2) [#17958](https://github.com/NVIDIA/TensorRT-LLM/pull/17958)
  [None][test] Waive 2 failed cases for main in QA CI (#17958)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`d431758482`](https://github.com/NVIDIA/TensorRT-LLM/commit/d431758482) [#17868](https://github.com/NVIDIA/TensorRT-LLM/pull/17868)
  [https://nvbugs/6567057][infra] Unwaive disagg helix test after port reservation race fix (#17868)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`70e2be2cef`](https://github.com/NVIDIA/TensorRT-LLM/commit/70e2be2cef) [#17673](https://github.com/NVIDIA/TensorRT-LLM/pull/17673)
  [https://nvbugs/6607481][fix] Isolate stateful KV-cache comparison (#17673)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`, `tests/integration/test_lists/waives.txt`, `tests/test_common/session_reuse_hooks.py`_
- **2026-08-19** [`256056a642`](https://github.com/NVIDIA/TensorRT-LLM/commit/256056a642) [#17944](https://github.com/NVIDIA/TensorRT-LLM/pull/17944)
  [None][test] Waive 5 failed cases for main in QA CI (#17944)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`d83401c164`](https://github.com/NVIDIA/TensorRT-LLM/commit/d83401c164) [#17943](https://github.com/NVIDIA/TensorRT-LLM/pull/17943)
  [None][test] Waive 7 failed cases for main in QA CI (#17943)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`51c73d0ba6`](https://github.com/NVIDIA/TensorRT-LLM/commit/51c73d0ba6) [#16839](https://github.com/NVIDIA/TensorRT-LLM/pull/16839)
  [https://nvbugs/6507080][fix] Override `TokenizerBase.__repr__` to return `f"{self.__class__.__name__}()"`… (#16839)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`2419a0fb42`](https://github.com/NVIDIA/TensorRT-LLM/commit/2419a0fb42) [#17834](https://github.com/NVIDIA/TensorRT-LLM/pull/17834)
  [TRTLLM-14727][test] Clean up MX qualification follow-ups (#17834)
  _Files: `docs/source/features/model-express.md`, `jenkins/L0_Test.groovy`_
- **2026-08-18** [`b9c6870adc`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9c6870adc) [#17925](https://github.com/NVIDIA/TensorRT-LLM/pull/17925)
  [None][infra] Waive 1 failed cases for main in pre-merge 54650 (#17925)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`963850b5cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/963850b5cc) [#17709](https://github.com/NVIDIA/TensorRT-LLM/pull/17709)
  [TRTLLMINF-40][fix] Fold sbatch submit stderr into the SLURM failure classifier (+ standby backoff) (#17709)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-18** [`b417fc5454`](https://github.com/NVIDIA/TensorRT-LLM/commit/b417fc5454) [#17886](https://github.com/NVIDIA/TensorRT-LLM/pull/17886)
  [None][test] Waive 2 failed cases for main in QA CI (#17886)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`e89659c01d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e89659c01d) [#17885](https://github.com/NVIDIA/TensorRT-LLM/pull/17885)
  [None][test] Waive 15 failed cases for main in QA CI (#17885)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`f65ec3b1d4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f65ec3b1d4) [#17689](https://github.com/NVIDIA/TensorRT-LLM/pull/17689)
  [None][infra] Fix UpdateTestDurations.groovy concurrent-update conflict (#17689)
  _Files: `jenkins/UpdateTestDurations.groovy`_
- **2026-08-18** [`912f44be1c`](https://github.com/NVIDIA/TensorRT-LLM/commit/912f44be1c)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-08-18** [`877fbc22db`](https://github.com/NVIDIA/TensorRT-LLM/commit/877fbc22db) [#17883](https://github.com/NVIDIA/TensorRT-LLM/pull/17883)
  [None][test] Waive 6 failed cases for main in QA CI (#17883)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`e817f5462e`](https://github.com/NVIDIA/TensorRT-LLM/commit/e817f5462e) [#17880](https://github.com/NVIDIA/TensorRT-LLM/pull/17880)
  [None][test] Waive 1 failed cases for main in QA CI (#17880)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`5ca827ccf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ca827ccf2) [#17864](https://github.com/NVIDIA/TensorRT-LLM/pull/17864)
  [None][infra] Waive 4 failed cases for main in pre-merge 54498 (#17864)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`aaa2fb4bcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaa2fb4bcd) [#17863](https://github.com/NVIDIA/TensorRT-LLM/pull/17863)
  [None][test] Waive 2 failed cases for main in QA CI (#17863)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`0969ee6835`](https://github.com/NVIDIA/TensorRT-LLM/commit/0969ee6835) [#17830](https://github.com/NVIDIA/TensorRT-LLM/pull/17830)
  [https://nvbugs/6581048][test] Unwaive TorchSampler beam-search e2e case (#17830)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`2254b6fb07`](https://github.com/NVIDIA/TensorRT-LLM/commit/2254b6fb07) [#17632](https://github.com/NVIDIA/TensorRT-LLM/pull/17632)
  [https://nvbugs/6601574][fix] Clean up leftover disagg server processes between Ray tests (#17632)
  _Files: `tests/integration/defs/examples/test_ray.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`102134fe8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/102134fe8d) [#17856](https://github.com/NVIDIA/TensorRT-LLM/pull/17856)
  [None][test] Waive 5 failed cases for main in QA CI (#17856)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`f11855b9bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/f11855b9bc) [#17854](https://github.com/NVIDIA/TensorRT-LLM/pull/17854)
  [None][test] Waive 4 failed cases for main in QA CI (#17854)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`f0e9623dba`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0e9623dba) [#17853](https://github.com/NVIDIA/TensorRT-LLM/pull/17853)
  [None][test] Waive 3 failed cases for main in QA CI (#17853)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`fa84a9ee35`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa84a9ee35) [#17851](https://github.com/NVIDIA/TensorRT-LLM/pull/17851)
  [None][ci] Waive six pre-existing main-side flaky tests (split from #17792) (#17851)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`215b7e4d98`](https://github.com/NVIDIA/TensorRT-LLM/commit/215b7e4d98) [#17706](https://github.com/NVIDIA/TensorRT-LLM/pull/17706)
  [TRTLLMINF-40][chore] Dedupe COMMON_SSH_OPTIONS to reference bloom's DEFAULT_CUSTOM_SSH_OPTIONS (#17706)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-08-17** [`38c5c49ebd`](https://github.com/NVIDIA/TensorRT-LLM/commit/38c5c49ebd) [#17812](https://github.com/NVIDIA/TensorRT-LLM/pull/17812)
  [None][test] Waive 3 failed cases for main in QA CI (#17812)
  _Files: `tests/integration/test_lists/waives.txt`_
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

## Executor / Runtime  (27 commits)

- **2026-08-24** [`ecd69d56f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecd69d56f0) [#17644](https://github.com/NVIDIA/TensorRT-LLM/pull/17644)
  [https://nvbugs/6581065][fix] Reap wedged workers during session drain (#17644)
  _Files: `tests/test_common/session_reuse.py`, `tests/unittest/llmapi/test_session_reuse.py`_
- **2026-08-24** [`8c1e685228`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c1e685228) [#17866](https://github.com/NVIDIA/TensorRT-LLM/pull/17866)
  [None][feat] KVCacheManagerV2: helix decode-CP via a global super-block ledger (#17866)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py` _+7 more__
- **2026-08-24** [`0db09f5b50`](https://github.com/NVIDIA/TensorRT-LLM/commit/0db09f5b50) [#18038](https://github.com/NVIDIA/TensorRT-LLM/pull/18038)
  [https://nvbugs/6627197][fix] Unwaive KV pool rebalance PP loop tests (#18038)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_kv_pool_rebalance.py`_
- **2026-08-21** [`0e00a9481e`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e00a9481e) [#17512](https://github.com/NVIDIA/TensorRT-LLM/pull/17512)
  [None][feat] Add cold-page codec support to KVCM2 (#17512)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/CMakeLists.txt`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/coldPageCodec.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/coldPageCodec.h` _+59 more__
- **2026-08-21** [`e433070b09`](https://github.com/NVIDIA/TensorRT-LLM/commit/e433070b09) [#17889](https://github.com/NVIDIA/TensorRT-LLM/pull/17889)
  [TRTLLM-15304][perf] add low-M BF16 GEMM dispatcher for SM10x decode (#17889)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/low_m_bf16_direct.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/low_m_bf16_splitk.py`, `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/modules/low_m_gemm.py` _+4 more__
- **2026-08-21** [`e7e6cf646d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e7e6cf646d) [#17534](https://github.com/NVIDIA/TensorRT-LLM/pull/17534)
  [None][fix] Clamp conversation-affinity ADP routing to per-rank slot (#17534)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tests/unittest/_torch/executor/test_adp_router.py`_
- **2026-08-21** [`b3116d676e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3116d676e) [#8855](https://github.com/NVIDIA/TensorRT-LLM/pull/8855)
  [None][fix] Use class-qualified access for clarity (#8855)
  _Files: `cpp/include/tensorrt_llm/runtime/iTensor.h`_
- **2026-08-20** [`e4cbeed3f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4cbeed3f1) [#17824](https://github.com/NVIDIA/TensorRT-LLM/pull/17824)
  [https://nvbugs/6525011][fix] Release eager outputs before CUDA graph capture (#17824)
  _Files: `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`b4ee1b4935`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4ee1b4935) [#16974](https://github.com/NVIDIA/TensorRT-LLM/pull/16974)
  [TRTLLM-14879][feat] qualify Qwen2 dense for MX (#16974)
  _Files: `docs/source/features/model-express.md`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py` _+4 more__
- **2026-08-19** [`8873151667`](https://github.com/NVIDIA/TensorRT-LLM/commit/8873151667) [#17903](https://github.com/NVIDIA/TensorRT-LLM/pull/17903)
  [#17580][fix] Stream the text that precedes a tool call in DeepSeek parsers (#17903)
  _Files: `tensorrt_llm/serve/tool_parser/deepseekv31_parser.py`, `tensorrt_llm/serve/tool_parser/deepseekv32_parser.py`, `tensorrt_llm/serve/tool_parser/deepseekv3_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-08-19** [`968a6706a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/968a6706a0) [#17790](https://github.com/NVIDIA/TensorRT-LLM/pull/17790)
  [TRTLLM-15179][test] Add multi-rank test for KVCM v2 host-tier quota sync (#17790)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_kvv2_host_tier_sizing.py`_
- **2026-08-19** [`849c9eb375`](https://github.com/NVIDIA/TensorRT-LLM/commit/849c9eb375) [#17583](https://github.com/NVIDIA/TensorRT-LLM/pull/17583)
  [TRTLLM-14778][perf] Cache the Whisper suppress-token index as a device tensor (#17583)
  _Files: `tensorrt_llm/llmapi/llm.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/test_whisper_suppress_tokens_processor.py`_
- **2026-08-18** [`b36faf1d82`](https://github.com/NVIDIA/TensorRT-LLM/commit/b36faf1d82) [#17828](https://github.com/NVIDIA/TensorRT-LLM/pull/17828)
  [https://nvbugs/6618106][fix] Carry single_step_greedy on SampleStateTensorsHostTorch (#17828)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler_strategy.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/sampler/test_torch_sampler.py`_
- **2026-08-18** [`b54e444c9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/b54e444c9d) [#17829](https://github.com/NVIDIA/TensorRT-LLM/pull/17829)
  [None][infra] Fix DIND networking/runtime compatibility and release wheel context (#17829)
  _Files: `docker/Dockerfile.multi`, `jenkins/BuildDockerImage.groovy`, `jenkins/docker/Dockerfile.dind`, `jenkins/docker/dind_mtu.sh` _+1 more__
- **2026-08-18** [`61c11a0ed4`](https://github.com/NVIDIA/TensorRT-LLM/commit/61c11a0ed4) [#16987](https://github.com/NVIDIA/TensorRT-LLM/pull/16987)
  [TRTLLM-14730][feat] Add image edit serving endpoint for visual generation models (#16987)
  _Files: `docs/source/models/supported-models.md`, `docs/source/models/visual-generation.md`, `examples/visual_gen/models/qwen_image_layered.py`, `tensorrt_llm/_torch/visual_gen/executor.py` _+10 more__
- **2026-08-18** [`bbfeecf82c`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbfeecf82c) [#17573](https://github.com/NVIDIA/TensorRT-LLM/pull/17573)
  [#17572][fix] Emit the withheld buffer in DeepSeek streaming tool parsers (#17573)
  _Files: `tensorrt_llm/serve/tool_parser/deepseekv31_parser.py`, `tensorrt_llm/serve/tool_parser/deepseekv32_parser.py`, `tensorrt_llm/serve/tool_parser/deepseekv3_parser.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-08-18** [`5dfe080491`](https://github.com/NVIDIA/TensorRT-LLM/commit/5dfe080491) [#17874](https://github.com/NVIDIA/TensorRT-LLM/pull/17874)
  [https://nvbugs/6627248][fix] Initialize multimodal flag in PP loop fixture (#17874)
  _Files: `tests/unittest/_torch/executor/test_kv_pool_rebalance.py`_
- **2026-08-18** [`cd572e118f`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd572e118f) [#17578](https://github.com/NVIDIA/TensorRT-LLM/pull/17578)
  [https://nvbugs/6590666][fix] Detect worker death during initialization (#17578)
  _Files: `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/worker.py`, `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-08-18** [`92c0b91ad7`](https://github.com/NVIDIA/TensorRT-LLM/commit/92c0b91ad7) [#17396](https://github.com/NVIDIA/TensorRT-LLM/pull/17396)
  [None][feat] Enable KVCacheManagerV2 by default for Gemma3 and Gemma4 (#17396)
  _Files: `docs/source/features/kvcache.md`, `tensorrt_llm/_torch/models/modeling_deepseekv4.py`, `tensorrt_llm/_torch/models/modeling_gemma3.py`, `tensorrt_llm/_torch/models/modeling_gemma3vl.py` _+4 more__
- **2026-08-17** [`59a7d2cabb`](https://github.com/NVIDIA/TensorRT-LLM/commit/59a7d2cabb) [#17568](https://github.com/NVIDIA/TensorRT-LLM/pull/17568)
  [None][fix] PostprocWorker: skip load_hf_tokenizer when tokenizer_dir is `None` (#17568)
  _Files: `tensorrt_llm/executor/postproc_worker.py`_
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

## MoE  (24 commits)

- **2026-08-24** [`27e461c171`](https://github.com/NVIDIA/TensorRT-LLM/commit/27e461c171) [#17598](https://github.com/NVIDIA/TensorRT-LLM/pull/17598)
  [TRTLLM-15099][test] Prune Mistral functional and unit tests (#17598)
  _Files: `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/test_cli_flow.py` _+21 more__
- **2026-08-24** [`2bb2e1c4e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bb2e1c4e6) [#17831](https://github.com/NVIDIA/TensorRT-LLM/pull/17831)
  [https://nvbugs/6601578][fix] Avoid MoE multi-GPU rendezvous port race (#17831)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/mega_moe_nvfp4/dynamic_mainloop.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/moe/test_moe_module.py`_
- **2026-08-23** [`88592cda9d`](https://github.com/NVIDIA/TensorRT-LLM/commit/88592cda9d) [#17822](https://github.com/NVIDIA/TensorRT-LLM/pull/17822)
  [TRTLLM-15498][refactor] consolidate Kimi KDA production frontend (#17822)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_kda/__init__.py`, `tensorrt_llm/_torch/modules/kimi_kda/_kda_kernels.py`, `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py` _+12 more__
- **2026-08-22** [`4f13faf713`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f13faf713) [#17622](https://github.com/NVIDIA/TensorRT-LLM/pull/17622)
  [None][refactor] Modularize sparse Top-K selection (#17622)
  _Files: `cpp/tensorrt_llm/thop/IndexerTopKOp.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/__init__.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py` _+4 more__
- **2026-08-21** [`19573c81f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/19573c81f3) [#17865](https://github.com/NVIDIA/TensorRT-LLM/pull/17865)
  [None][feat] bring up Kimi K3 NVFP4 with CUTLASS and cuteDSL MegaMoE SiTU (#17865)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/common.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_gemm_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu` _+27 more__
- **2026-08-21** [`2f17320eb2`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f17320eb2) [#17700](https://github.com/NVIDIA/TensorRT-LLM/pull/17700)
  [None][perf] Qwen3.5/3.8 wave-2: MoE, attention-DP, GDN replay, weight loading (#17700)
  _Files: `cpp/tensorrt_llm/thop/moeUtilOp.cpp`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/checkpoints/base_weight_loader.py`, `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py` _+11 more__
- **2026-08-20** [`9f5f711539`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f5f711539) [#17546](https://github.com/NVIDIA/TensorRT-LLM/pull/17546)
  [None][test] Replace disaggregated DWDP accuracy tests with aggregated coverage (#17546)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/integration/defs/accuracy/test_dwdp_aggregated.py`, `tests/integration/defs/accuracy/test_dwdp_disaggregated_serving.py` _+2 more__
- **2026-08-20** [`e223b00565`](https://github.com/NVIDIA/TensorRT-LLM/commit/e223b00565) [#16666](https://github.com/NVIDIA/TensorRT-LLM/pull/16666)
  [None][perf] Overlap DSA heuristic prev_topk write-back on the aux stream (#16666)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/module.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/indexer.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/module.py`_
- **2026-08-20** [`668cde6948`](https://github.com/NVIDIA/TensorRT-LLM/commit/668cde6948) [#17274](https://github.com/NVIDIA/TensorRT-LLM/pull/17274)
  [TRTLLM-13767][chore] upgrade CUTLASS DSL stack to 4.6.1 (#17274)
  _Files: `.claude/skills/kernel-cute-writing/references/api-core.md`, `.claude/skills/kernel-cute-writing/references/concepts-tensors.md`, `constraints.txt`, `docker/Dockerfile.multi` _+28 more__
- **2026-08-19** [`e6caf6f09b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6caf6f09b) [#15993](https://github.com/NVIDIA/TensorRT-LLM/pull/15993)
  [TRTLLM-11901][feat] Add trtllm weight loading metrics (#15993)
  _Files: `docs/source/developer-guide/perf-benchmarking.md`, `docs/source/llm-api/index.md`, `tensorrt_llm/_torch/models/checkpoints/base_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py` _+22 more__
- **2026-08-19** [`2c1be7d52f`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c1be7d52f) [#17801](https://github.com/NVIDIA/TensorRT-LLM/pull/17801)
  [https://nvbugs/6567554][fix] Make DeepSeek-V4 layer-wise benchmarks run, and derive module perf cases from the trace (#17801)
  _Files: `examples/layer_wise_benchmarks/run.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/tools/layer_wise_benchmarks/mark_utils.py`, `tensorrt_llm/tools/layer_wise_benchmarks/runner.py` _+4 more__
- **2026-08-19** [`b2fc34b5d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2fc34b5d5) [#17797](https://github.com/NVIDIA/TensorRT-LLM/pull/17797)
  [TRTLLM-15433][chore] Remove all WIDEEP files (#17797)
  _Files: `.pre-commit-config.yaml`, `examples/layer_wise_benchmarks/run.py`, `legacy-files.txt`, `pyproject.toml` _+19 more__
- **2026-08-19** [`e1a984e049`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1a984e049) [#17059](https://github.com/NVIDIA/TensorRT-LLM/pull/17059)
  [None][perf] fuse Kimi K3 routing and MXFP8 quantization (#17059)
  _Files: `cpp/tensorrt_llm/kernels/noAuxTcKernels.cu`, `cpp/tensorrt_llm/kernels/noAuxTcKernels.h`, `cpp/tensorrt_llm/thop/noAuxTcOp.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+6 more__
- **2026-08-19** [`36ae3f0f08`](https://github.com/NVIDIA/TensorRT-LLM/commit/36ae3f0f08) [#17878](https://github.com/NVIDIA/TensorRT-LLM/pull/17878)
  [None][test] GVR top-K decode UT: compile-signature-aware parametrization (27m31s -> 13m34s) (#17878)
  _Files: `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-08-19** [`18b0eafe6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/18b0eafe6e) [#17791](https://github.com/NVIDIA/TensorRT-LLM/pull/17791)
  [None][feat] bench_moe: group-aware routing support (#17791)
  _Files: `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/case_runner.py`, `tests/microbenchmarks/bench_moe/routing/materialize.py`, `tests/microbenchmarks/bench_moe/routing/native_logits.py` _+1 more__
- **2026-08-19** [`d918e325a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/d918e325a3) [#17806](https://github.com/NVIDIA/TensorRT-LLM/pull/17806)
  [TRTLLM-14839][chore] Relocate root PEFT modules into _torch/peft/ (#17806)
  _Files: `.github/CODEOWNERS`, `.pre-commit-config.yaml`, `cpp/tensorrt_llm/thop/moeOp.cpp`, `docs/source/features/lora.md` _+48 more__
- **2026-08-18** [`754323eca2`](https://github.com/NVIDIA/TensorRT-LLM/commit/754323eca2) [#17641](https://github.com/NVIDIA/TensorRT-LLM/pull/17641)
  [https://nvbugs/6566765][fix] Release Qwen MoE CUDA memory between tests (#17641)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modeling/test_modeling_qwen_moe.py`_
- **2026-08-18** [`0c667398b1`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c667398b1) [#17777](https://github.com/NVIDIA/TensorRT-LLM/pull/17777)
  [TRTLLM-14957][refactor] split the MoE base class by responsibility and converge the loader owner gate (#17777)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/afmoe_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/exaone_moe_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen2_moe_weight_mapper.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py` _+12 more__
- **2026-08-18** [`bef843ef97`](https://github.com/NVIDIA/TensorRT-LLM/commit/bef843ef97) [#17312](https://github.com/NVIDIA/TensorRT-LLM/pull/17312)
  [None][refactor] Refactor Kimi K3 MLP (#17312)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_moe/__init__.py`, `tensorrt_llm/_torch/modules/kimi_k3_moe/_mlp.py`, `tensorrt_llm/_torch/modules/kimi_k3_moe/kimi_k3_moe_gate.py` _+10 more__
- **2026-08-18** [`3c5cc959fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c5cc959fb) [#17635](https://github.com/NVIDIA/TensorRT-LLM/pull/17635)
  [TRTLLM-15304][fix] MoE and MTP fixes for large hybrid-attention FP8 serving (#17635)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomPolicy.cuh`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomSelection.h` _+8 more__
- **2026-08-17** [`7d55b873fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d55b873fe) [#17497](https://github.com/NVIDIA/TensorRT-LLM/pull/17497)
  [https://nvbugs/6572835][fix] Use HashStore for single-rank MegaMoE tests (#17497)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/microbenchmarks/bench_moe/utils.py`, `tests/unittest/_torch/modules/moe/test_moe_backend.py`, `tests/unittest/_torch/modules/moe/test_moe_module.py`_
- **2026-08-17** [`bac9a5cc58`](https://github.com/NVIDIA/TensorRT-LLM/commit/bac9a5cc58) [#17612](https://github.com/NVIDIA/TensorRT-LLM/pull/17612)
  [None][fix] Drop the stale choices list on --moe-backend-for-prefill (#17612)
  _Files: `examples/layer_wise_benchmarks/run.py`_
- **2026-08-17** [`e5323835d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5323835d8) [#17621](https://github.com/NVIDIA/TensorRT-LLM/pull/17621)
  [None][fix] Fence MoE shared writes before async bulk copy (#17621)
  _Files: `cpp/tensorrt_llm/kernels/fusedMoeCommKernels.cu`_
- **2026-08-17** [`476ea087a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/476ea087a0) [#17404](https://github.com/NVIDIA/TensorRT-LLM/pull/17404)
  [None][infra] Add execution and test-runner skills for Claude Code (#17404)
  _Files: `.claude/agents/exec-local-slurm.md`, `.claude/agents/exec-remote-slurm.md`, `.claude/agents/trtllm-test-specialist.md`, `.claude/skills/exec-env-check/SKILL.md` _+78 more__

## Attention  (23 commits)

- **2026-08-24** [`f5080d7923`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5080d7923) [#18013](https://github.com/NVIDIA/TensorRT-LLM/pull/18013)
  [TRTLLM-15120][test] Prune Step-3.7-Flash functional tests (#18013)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py` _+2 more__
- **2026-08-24** [`5ee95a1037`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ee95a1037) [#17318](https://github.com/NVIDIA/TensorRT-LLM/pull/17318)
  [None][perf] Use FP8 MiniMax-M3 MSA indexer QK (#17318)
  _Files: `cpp/tensorrt_llm/kernels/minimaxM3Fp8IndexerKernel.cu`, `cpp/tensorrt_llm/kernels/minimaxM3Fp8IndexerKernel.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/minimaxM3Fp8IndexerOp.cpp` _+13 more__
- **2026-08-23** [`ca728f8562`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca728f8562) [#17236](https://github.com/NVIDIA/TensorRT-LLM/pull/17236)
  [None][perf] Optimize MiniMax-M3 MSA block selection (#17236)
  _Files: `cpp/tensorrt_llm/kernels/minimaxM3SelectBlocks.cu`, `cpp/tensorrt_llm/kernels/minimaxM3SelectBlocks.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/minimaxM3SelectBlocksOp.cpp` _+6 more__
- **2026-08-22** [`f51e32335a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f51e32335a) [#17800](https://github.com/NVIDIA/TensorRT-LLM/pull/17800)
  [TRTLLM-15033][feat] Upstream Kimi K3 MLA decode backend selection to main (#17800)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tensorrt_llm/_torch/attention_backend/fmha/interface.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py` _+9 more__
- **2026-08-22** [`f148307f6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/f148307f6c) [#17794](https://github.com/NVIDIA/TensorRT-LLM/pull/17794)
  [None][fix] PYTHON transceiver: decode-CP transfer support and concurrency corruption fixes (#17794)
  _Files: `tensorrt_llm/_torch/disaggregation/native/mixers/attention/peer.py`, `tensorrt_llm/_torch/disaggregation/native/mixers/ssm/peer.py`, `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py` _+2 more__
- **2026-08-21** [`5264ed52f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/5264ed52f8) [#17264](https://github.com/NVIDIA/TensorRT-LLM/pull/17264)
  [None][fix] Fix FlashInfer shared-KV speculative decode (#17264)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/metadata.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+4 more__
- **2026-08-21** [`d4b7b61e92`](https://github.com/NVIDIA/TensorRT-LLM/commit/d4b7b61e92) [#17846](https://github.com/NVIDIA/TensorRT-LLM/pull/17846)
  [TRTLLM-14818][test] Port Kimi K3 DFlash/DSpark eval helpers and KDA FP8 prefill test to main (#17846)
  _Files: `examples/kimi_k3/eval_extra_llm_options_dflash.yaml`, `examples/kimi_k3/make_synthetic_dflash_drafter.py`, `examples/kimi_k3/measure_dspark_acceptance.py`, `examples/kimi_k3/run_dspark_acceptance.sbatch` _+2 more__
- **2026-08-20** [`664c386ee4`](https://github.com/NVIDIA/TensorRT-LLM/commit/664c386ee4) [#18019](https://github.com/NVIDIA/TensorRT-LLM/pull/18019)
  [None][ci] Waive B300 flake test_attention_backend[qwen2_0_5b_gqa_hd64-ctx-bf16-HND-p32-v1] (nvbugs/6641268) (#18019)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`1a95c93699`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a95c93699) [#16887](https://github.com/NVIDIA/TensorRT-LLM/pull/16887)
  [https://nvbugs/6463967][fix] DeepSeek-V4 one-model MTP separate draft kv cache (TEP) (#16887)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/metadata.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa/metadata.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+6 more__
- **2026-08-19** [`8fc097f0db`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fc097f0db) [#17698](https://github.com/NVIDIA/TensorRT-LLM/pull/17698)
  [TRTLLM-15403][fix] VisualGen: warn when a requested attention backend silently falls back to VANILLA (#17698)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/transformer_cosmos3.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py`_
- **2026-08-19** [`4815338556`](https://github.com/NVIDIA/TensorRT-LLM/commit/4815338556) [#17684](https://github.com/NVIDIA/TensorRT-LLM/pull/17684)
  [None][feat] Remove padding in Kimi K3 MLA module (#17684)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/cute_dsl_mla.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/modules/kimi_k3_mla/kimi_k3_mla_attention.py`_
- **2026-08-19** [`018c56ebd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/018c56ebd0) [#17879](https://github.com/NVIDIA/TensorRT-LLM/pull/17879)
  [https://nvbugs/6610548][test] Unwaive B300 qwen2_0_5b_gqa_hd64 ctx attention backend test (#17879)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`6a532224cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/6a532224cf) [#17840](https://github.com/NVIDIA/TensorRT-LLM/pull/17840)
  [None][perf] Remove spurious sync in sparse fmha forward (#17840)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_backend.py`, `tensorrt_llm/_torch/attention_backend/sparse/minimax_m3/msa_utils.py`_
- **2026-08-18** [`e59fbf2bfd`](https://github.com/NVIDIA/TensorRT-LLM/commit/e59fbf2bfd) [#17053](https://github.com/NVIDIA/TensorRT-LLM/pull/17053)
  [None][perf] Preallocate Kimi attention residual snapshots (#17053)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`_
- **2026-08-18** [`0eeda343df`](https://github.com/NVIDIA/TensorRT-LLM/commit/0eeda343df) [#17273](https://github.com/NVIDIA/TensorRT-LLM/pull/17273)
  [TRTLLM-14597][perf] Fuse the DSv4 MLA prologue: kv_a_layernorm, q_nope FP8 quant and Q RoPE (#17273)
  _Files: `cpp/tensorrt_llm/kernels/deepseekV4QNormKernel.cu`, `cpp/tensorrt_llm/kernels/deepseekV4QNormKernel.h`, `cpp/tensorrt_llm/kernels/mlaKernels.cu`, `cpp/tensorrt_llm/kernels/mlaKernels.h` _+15 more__
- **2026-08-18** [`1093273ab5`](https://github.com/NVIDIA/TensorRT-LLM/commit/1093273ab5) [#17026](https://github.com/NVIDIA/TensorRT-LLM/pull/17026)
  [https://nvbugs/6571220][fix] Correct unfused attention context workspace sizing (#17026)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_t5.py` _+2 more__
- **2026-08-18** [`b4b92c9f5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4b92c9f5f) [#17648](https://github.com/NVIDIA/TensorRT-LLM/pull/17648)
  [https://nvbugs/6198760][fix] Refresh FMHA cubins to fix SageAttention when KV-sequence is not a multiple of 128 (#17648)
- **2026-08-17** [`c763b04de2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c763b04de2) [#17448](https://github.com/NVIDIA/TensorRT-LLM/pull/17448)
  [TRTLLM-15218][chore] KVCacheManagerV2: report the prefix attention alone supports (#17448)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/blockRadixTree.h`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.h` _+4 more__
- **2026-08-17** [`718608b098`](https://github.com/NVIDIA/TensorRT-LLM/commit/718608b098) [#17391](https://github.com/NVIDIA/TensorRT-LLM/pull/17391)
  [TRTLLM-13308][feat] Make the KVCacheManagerV2 KV pool rebalance safe under TP, CP, PP and attention DP (#17391)
  _Files: `cpp/tensorrt_llm/batch_manager/kv_cache_manager_v2/kvCache.cpp`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py`, `tests/integration/defs/accuracy/test_kv_pool_rebalance_accuracy.py` _+4 more__
- **2026-08-17** [`be2732912b`](https://github.com/NVIDIA/TensorRT-LLM/commit/be2732912b) [#17307](https://github.com/NVIDIA/TensorRT-LLM/pull/17307)
  [None][perf] fuse DSpark attention and RMSNorm RoPE (#17307)
  _Files: `tensorrt_llm/_torch/custom_ops/dspark_attention_custom_op.py`, `tensorrt_llm/_torch/custom_ops/dspark_rmsnorm_rope_custom_op.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dspark_attention.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/dspark_rmsnorm_rope.py` _+5 more__
- **2026-08-17** [`3d311e377e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d311e377e) [#16432](https://github.com/NVIDIA/TensorRT-LLM/pull/16432)
  [None][fix] Declare attention runtime-workspace bytes/token as a backend contract (#16432)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/modules/ATTENTION_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+3 more__
- **2026-08-17** [`afee78d207`](https://github.com/NVIDIA/TensorRT-LLM/commit/afee78d207) [#17674](https://github.com/NVIDIA/TensorRT-LLM/pull/17674)
  [TRTLLM-15115][test] Prune Starcoder2-3B functional and unit tests (#17674)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/humaneval.yaml`, `tests/integration/defs/accuracy/test_cli_flow.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_encode.py` _+7 more__
- **2026-08-17** [`2d9e78c96e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2d9e78c96e) [#16914](https://github.com/NVIDIA/TensorRT-LLM/pull/16914)
  [None][feat] Support DFlash RoPE, sliding-window configuration, and TRTLLM-gen attention backend (#16914)
  _Files: `docs/source/features/speculative-decoding.md`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py` _+16 more__

## Disaggregation / KV  (19 commits)

- **2026-08-24** [`0f2c3a95f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f2c3a95f9) [#18090](https://github.com/NVIDIA/TensorRT-LLM/pull/18090)
  [None][fix] preserve streaming SSE event boundaries (#18090)
  _Files: `tensorrt_llm/serve/openai_client.py`, `tests/unittest/disaggregated/test_disagg_openai_client.py`_
- **2026-08-24** [`33df8c1e81`](https://github.com/NVIDIA/TensorRT-LLM/commit/33df8c1e81) [#17966](https://github.com/NVIDIA/TensorRT-LLM/pull/17966)
  [None][refactor] Move disagg transfer helpers from py_executor into disaggregation/executor (#17966)
  _Files: `tensorrt_llm/_torch/disaggregation/executor/__init__.py`, `tensorrt_llm/_torch/disaggregation/executor/admission.py`, `tensorrt_llm/_torch/disaggregation/executor/pp_termination.py`, `tensorrt_llm/_torch/disaggregation/executor/transfer_manager.py` _+5 more__
- **2026-08-23** [`5450c0536e`](https://github.com/NVIDIA/TensorRT-LLM/commit/5450c0536e) [#17850](https://github.com/NVIDIA/TensorRT-LLM/pull/17850)
  [None][fix] Stop KV cache estimation probes from pinning the full host tier (#17850)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/unittest/_torch/executor/test_kv_cache_budget_split.py`_
- **2026-08-22** [`181c827eb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/181c827eb5) [#17962](https://github.com/NVIDIA/TensorRT-LLM/pull/17962)
  [https://nvbugs/6602927][test] Unwaive fixed KV cache V2 deadlock case (#17962)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-22** [`afe626dd5c`](https://github.com/NVIDIA/TensorRT-LLM/commit/afe626dd5c) [#17483](https://github.com/NVIDIA/TensorRT-LLM/pull/17483)
  [TRTLLM-15264][test] Kimi K3 disagg review fixups: KDA test geometry, gate docs, example cleanup (#17483)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/configs/kda_payload_kimi_k3.yaml`, `examples/kimi_k3/disagg/README.md`, `examples/kimi_k3/disagg/ctx_config.yaml`, `tensorrt_llm/_torch/disaggregation/native/bounce/config.py` _+4 more__
- **2026-08-20** [`e97f3f382a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e97f3f382a) [#17873](https://github.com/NVIDIA/TensorRT-LLM/pull/17873)
  [None][test] Increase KV transfer timeout for PP4-to-TP4 disaggregated test (#17873)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxpp4_gentp4.yaml`_
- **2026-08-20** [`96a143e41a`](https://github.com/NVIDIA/TensorRT-LLM/commit/96a143e41a) [#17823](https://github.com/NVIDIA/TensorRT-LLM/pull/17823)
  [https://nvbugs/6600098][test] Stabilize KV cache V2 scheduler tests (#17823)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`d0e8baa03b`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0e8baa03b) [#17121](https://github.com/NVIDIA/TensorRT-LLM/pull/17121)
  [https://nvbugs/6541356][fix] Align the transceiver precheck with the serving KV cache setup (#17121)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/run_cache_transceiver_test.py`, `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/cluster_env.py`, `jenkins/scripts/perf/disaggregated/slurm_ct_precheck_gate.sh` _+14 more__
- **2026-08-19** [`6afe08dcdb`](https://github.com/NVIDIA/TensorRT-LLM/commit/6afe08dcdb) [#15252](https://github.com/NVIDIA/TensorRT-LLM/pull/15252)
  [None][fix] Add KV cache V2 recompute pause path (#15252)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+11 more__
- **2026-08-19** [`f601fca69e`](https://github.com/NVIDIA/TensorRT-LLM/commit/f601fca69e) [#17848](https://github.com/NVIDIA/TensorRT-LLM/pull/17848)
  [TRTLLM-14575][perf] Avoid quadratic copy in KV cache block reuse (#17848)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`_
- **2026-08-19** [`d689652b7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d689652b7d) [#17811](https://github.com/NVIDIA/TensorRT-LLM/pull/17811)
  [None][fix] helix: compensate position_id for the overlap scheduler (#17811)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+1 more__
- **2026-08-18** [`5cf3e94f57`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cf3e94f57) [#17881](https://github.com/NVIDIA/TensorRT-LLM/pull/17881)
  [None][fix] Make disaggregated benchmark server health timeout configurable (#17881)
  _Files: `examples/disaggregated/slurm/benchmark/README.md`, `examples/disaggregated/slurm/benchmark/config.yaml`, `examples/disaggregated/slurm/benchmark/submit.py`, `examples/disaggregated/slurm/benchmark/submit_dwdp.py` _+1 more__
- **2026-08-18** [`5a8462aef7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a8462aef7) [#17861](https://github.com/NVIDIA/TensorRT-LLM/pull/17861)
  [None][test] Add back kimi k25 and deepseek v32 cases from qa side (#17861)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-v32-fp4_32k4k_con1_ctx1_dep4_gen1_tep8_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-v32-fp4_32k4k_con256_ctx1_dep4_gen1_dep32_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-v32-fp4_32k4k_con256_ctx1_dep8_gen1_dep8_eplb0_mtp0_ccb-NIXL.yaml` _+8 more__
- **2026-08-18** [`aede3825b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/aede3825b7) [#17802](https://github.com/NVIDIA/TensorRT-LLM/pull/17802)
  [None][test] Add kimi k3 cases for multi-node disagg (#17802)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb300_kimi-k3-fp4_8k1k_con512_ctx1_dep16_gen1_dep16_eplb0_mtp0_ccb-NIXL.yaml`_
- **2026-08-18** [`0258940e38`](https://github.com/NVIDIA/TensorRT-LLM/commit/0258940e38) [#17300](https://github.com/NVIDIA/TensorRT-LLM/pull/17300)
  [None][test] Allow IB transport in disaggregated tests on Hopper (#17300)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_ad_disagg.py`, `tests/integration/defs/disaggregated/test_auto_scaling.py`, `tests/integration/defs/disaggregated/test_disaggregated.py` _+3 more__
- **2026-08-18** [`03ddc2463d`](https://github.com/NVIDIA/TensorRT-LLM/commit/03ddc2463d) [#17482](https://github.com/NVIDIA/TensorRT-LLM/pull/17482)
  [TRTLLM-15264][fix] Fail only the affected requests on disagg peer-layout mismatch (#17482)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_kv_transfer.py`_
- **2026-08-17** [`2562a0a3d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/2562a0a3d8) [#17618](https://github.com/NVIDIA/TensorRT-LLM/pull/17618)
  [None][refactor] BREAKING remove conversation ID from disaggregated params (#17618)
  _Files: `tensorrt_llm/disaggregated_params.py`, `tensorrt_llm/serve/conversation_id.py`, `tensorrt_llm/serve/openai_disagg_service.py`, `tensorrt_llm/serve/openai_protocol.py` _+5 more__
- **2026-08-17** [`9997d3ffb0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9997d3ffb0) [#17460](https://github.com/NVIDIA/TensorRT-LLM/pull/17460)
  [https://nvbugs/6435121][fix] Eliminate the trtllm-serve port reservation race with --port 0 + --report_addr (#17460)
  _Files: `tensorrt_llm/commands/serve.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/common.py`, `tests/integration/defs/disaggregated/disagg_test_utils.py` _+6 more__
- **2026-08-17** [`55be7e53d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/55be7e53d3) [#17480](https://github.com/NVIDIA/TensorRT-LLM/pull/17480)
  [TRTLLM-15264][fix] Reject non-Python transceiver routes for Kimi K3 disaggregated serving (#17480)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py`_

## Quantization  (17 commits)

- **2026-08-24** [`be69541924`](https://github.com/NVIDIA/TensorRT-LLM/commit/be69541924) [#18056](https://github.com/NVIDIA/TensorRT-LLM/pull/18056)
  [https://nvbugs/6633928][fix] Limit Gemma3 FP8 accuracy test sequence length (#18056)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-08-24** [`c564f4925b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c564f4925b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/ngram/poetry.lock`, `security_scanning/examples/quantization/poetry.lock` _+5 more__
- **2026-08-23** [`aaaf65998b`](https://github.com/NVIDIA/TensorRT-LLM/commit/aaaf65998b) [#17521](https://github.com/NVIDIA/TensorRT-LLM/pull/17521)
  [TRTLLM-15314][feat] Add FP8 LoRA support for B200 (#17521)
  _Files: `cpp/tensorrt_llm/kernels/cuda_graph_grouped_gemm.cu`, `cpp/tensorrt_llm/kernels/fp8GroupedGemmConfig.h`, `cpp/tensorrt_llm/kernels/groupGemm.cu`, `cpp/tensorrt_llm/kernels/groupGemm.h` _+8 more__
- **2026-08-23** [`11e1b99925`](https://github.com/NVIDIA/TensorRT-LLM/commit/11e1b99925) [#18099](https://github.com/NVIDIA/TensorRT-LLM/pull/18099)
  [https://nvbugs/6652876][fix] Fix release checks and waive Laguna XS FP8 (#18099)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/lora_test_utils.py`_
- **2026-08-23** [`da38c1d2e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/da38c1d2e0) [#17693](https://github.com/NVIDIA/TensorRT-LLM/pull/17693)
  [TRTLLM-15398][perf] VisualGen MLP: cublasLt GELU-tanh epilogue for the unquantized bf16 path (#17693)
  _Files: `tensorrt_llm/_torch/modules/mlp.py`, `tests/unittest/_torch/thop/parallel/test_dense_gemm_act_fusion.py`_
- **2026-08-21** [`bc12697eaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/bc12697eaf) [#17780](https://github.com/NVIDIA/TensorRT-LLM/pull/17780)
  [https://nvbugs/6418815][test] Pin fp32-matmul precision in VisualGen LPIPS tests and re-baseline Cosmos3 goldens (#17780)
  _Files: `scripts/visualgen_eval/visual_gen_lpips_score_eval.py`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_i2v_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_t2i_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_edge_t2v_lpips_golden_video.json` _+8 more__
- **2026-08-21** [`fe4aebfe0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe4aebfe0f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock` _+9 more__
- **2026-08-21** [`eaf6dc558c`](https://github.com/NVIDIA/TensorRT-LLM/commit/eaf6dc558c) [#17786](https://github.com/NVIDIA/TensorRT-LLM/pull/17786)
  [None][fix] normalize Qwen3.8 27B FP8 VLM quantization config (#17786)
  _Files: `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tests/unittest/_torch/modeling/test_qwen_image_bench_modeling.py`_
- **2026-08-20** [`b70aed32f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/b70aed32f3) [#17699](https://github.com/NVIDIA/TensorRT-LLM/pull/17699)
  [TRTLLM-15404][fix] VisualGen: refuse static quant recipes against unquantized checkpoints (silent weight corruption) (#17699)
  _Files: `tensorrt_llm/_torch/visual_gen/quantization/loader.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/_torch/visual_gen/test_quant_static_guard.py`_
- **2026-08-20** [`0fbac8ce0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fbac8ce0d) [#17610](https://github.com/NVIDIA/TensorRT-LLM/pull/17610)
  [None][feat] Enable FA4 + parallel VAE in LTX-2 examples (#17610)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/configs/ltx2-1gpu.yaml`, `examples/visual_gen/configs/ltx2-4gpu.yaml`, `examples/visual_gen/configs/ltx2-fp4-1gpu.yaml` _+3 more__
- **2026-08-19** [`586d84cdce`](https://github.com/NVIDIA/TensorRT-LLM/commit/586d84cdce) [#16018](https://github.com/NVIDIA/TensorRT-LLM/pull/16018)
  [None][feat] Add GlmImage text-to-image pipeline support to VisualGen (#16018)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/models/glm_image.py`, `tensorrt_llm/_torch/visual_gen/models/__init__.py` _+12 more__
- **2026-08-19** [`bd90276f6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd90276f6b) [#17855](https://github.com/NVIDIA/TensorRT-LLM/pull/17855)
  [https://nvbugs/6478723][fix] Unwaive TestNemotronV3Super::test_nvfp4_4gpus_hopper_w4a16 after the MTPEagleDynamicTreeWorker fix (#17855)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`daa75397d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/daa75397d8) [#17923](https://github.com/NVIDIA/TensorRT-LLM/pull/17923)
  [https://nvbugs/6631019][test] waive Nemotron Nano FP8 CUDA graph test on DGX B200 (#17923)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`9ab8a9d40b`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ab8a9d40b) [#17660](https://github.com/NVIDIA/TensorRT-LLM/pull/17660)
  [https://nvbugs/6604925][fix] Swap the grid axes so N maps to the unbounded `grid.x` and M to `grid.y`… (#17660)
  _Files: `cpp/tensorrt_llm/kernels/weightOnlyBatchedGemv/cudaCoreGemmNVFP4.cu`, `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`29e92245a1`](https://github.com/NVIDIA/TensorRT-LLM/commit/29e92245a1) [#17833](https://github.com/NVIDIA/TensorRT-LLM/pull/17833)
  [https://nvbugs/6624972][test] Waive Nemotron-Nano-9B-v2-NVFP4 quickstart on l0_b200 (#17833)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`bec64faf3f`](https://github.com/NVIDIA/TensorRT-LLM/commit/bec64faf3f) [#17847](https://github.com/NVIDIA/TensorRT-LLM/pull/17847)
  [None][ci] Waive two pre-existing main-side flaky tests (Qwen3.5 fp8 block-reuse, Nemotron Nano V2 VL video batch) (#17847)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-17** [`8efd46efb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/8efd46efb5) [#17789](https://github.com/NVIDIA/TensorRT-LLM/pull/17789)
  [None][test] Unwaive DeepSeek nvfp4 tests (nvbugs 6481323, 6245394) (#17789)
  _Files: `tests/integration/test_lists/waives.txt`_

## Torch Path (_torch)  (14 commits)

- **2026-08-24** [`4baa757f97`](https://github.com/NVIDIA/TensorRT-LLM/commit/4baa757f97) [#17695](https://github.com/NVIDIA/TensorRT-LLM/pull/17695)
  [TRTLLM-15400][perf] fuse per-token AdaLN for VisualGen Wan 2.2 5B (#17695)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/pertoken_adaln.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/pertoken_adaln/reduce.py`, `tensorrt_llm/_torch/visual_gen/models/wan/transformer_wan.py` _+4 more__
- **2026-08-23** [`7784c413d1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7784c413d1) [#17825](https://github.com/NVIDIA/TensorRT-LLM/pull/17825)
  [https://nvbugs/6590418][perf] Infer avg sequence length for fixed perf datasets (#17825)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`, `tests/integration/defs/perf/test_perf.py`, `tests/unittest/others/test_perf_fixed_sequence_length.py`, `tests/unittest/others/test_sysinfo.py`_
- **2026-08-22** [`cbc3784a27`](https://github.com/NVIDIA/TensorRT-LLM/commit/cbc3784a27) [#16394](https://github.com/NVIDIA/TensorRT-LLM/pull/16394)
  [TRTLLM-14268][feat] Cosmos3 Transfer (control-video conditioning) (#16394)
  _Files: `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py`, `examples/visual_gen/models/cosmos3/generate_bouncing_ball_control.py`, `examples/visual_gen/serve/README.md` _+19 more__
- **2026-08-19** [`9c895034b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c895034b4) [#17523](https://github.com/NVIDIA/TensorRT-LLM/pull/17523)
  [None][fix] Reword Cosmos3 negative prompt terms that trip the guardrail blocklist (#17523)
  _Files: `examples/visual_gen/models/cosmos3/cosmos3_negative_prompt.json`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/negative_prompt.py`_
- **2026-08-19** [`83aa576925`](https://github.com/NVIDIA/TensorRT-LLM/commit/83aa576925) [#17510](https://github.com/NVIDIA/TensorRT-LLM/pull/17510)
  [None][fix] Fix Cosmos3 CUDA event crash when text guardrail blocks prompt (#17510)
  _Files: `tensorrt_llm/_torch/visual_gen/models/cosmos3/pipeline_cosmos3.py`, `tests/unittest/_torch/visual_gen/test_cosmos3_pipeline.py`_
- **2026-08-19** [`cf4619cc38`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf4619cc38) [#17708](https://github.com/NVIDIA/TensorRT-LLM/pull/17708)
  [https://nvbugs/6602928][fix] Serialize HF remote-code loading when building input processors (#17708)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/inputs/registry.py`_
- **2026-08-18** [`24be2c11b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/24be2c11b8) [#17565](https://github.com/NVIDIA/TensorRT-LLM/pull/17565)
  [https://nvbugs/6373561][fix] Fix minimax M3 E2E test (#17565)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/models/test_minimax_m3.py`_
- **2026-08-18** [`6822e3fa6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/6822e3fa6c) [#17507](https://github.com/NVIDIA/TensorRT-LLM/pull/17507)
  [https://nvbugs/5573856][fix] Re-enable NCCL symmetric shape-growth test (#17507)
  _Files: `tests/unittest/_torch/multi_gpu/test_mnnvl_allreduce.py`_
- **2026-08-18** [`b9c51d956e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9c51d956e) [#17719](https://github.com/NVIDIA/TensorRT-LLM/pull/17719)
  [https://nvbugs/6581049][ci] Mark flaky test as xfail instead of skipping (#17719)
  _Files: `requirements-dev.txt`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`8986c2275c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8986c2275c) [#17474](https://github.com/NVIDIA/TensorRT-LLM/pull/17474)
  [TRTLLM-14719][infra] Add spec-dec acceptance-length regression baselines and remove PARD CnnDailymail coverage (#17474)
  _Files: `tests/integration/defs/accuracy/accuracy_core.py`, `tests/integration/defs/accuracy/references/acceptance_length.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-08-18** [`80770160e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/80770160e9) [#16712](https://github.com/NVIDIA/TensorRT-LLM/pull/16712)
  [https://nvbugs/6437410][fix] fix nemotron weight update test (#16712)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_install.sh`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py` _+1 more__
- **2026-08-17** [`013d8d1f82`](https://github.com/NVIDIA/TensorRT-LLM/commit/013d8d1f82) [#16764](https://github.com/NVIDIA/TensorRT-LLM/pull/16764)
  [None][refactor] Mixed Modality Support for Nemotron Nano Omni V3 (#16764)
  _Files: `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`, `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/inputs/registry.py` _+5 more__
- **2026-08-17** [`ad1202d084`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad1202d084) [#17222](https://github.com/NVIDIA/TensorRT-LLM/pull/17222)
  [TRTLLM-14727][test] Create MX donor-receiver qualification test harness (#17222)
  _Files: `docs/source/features/model-express.md`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py` _+4 more__
- **2026-08-17** [`99edf98239`](https://github.com/NVIDIA/TensorRT-LLM/commit/99edf98239) [#16788](https://github.com/NVIDIA/TensorRT-LLM/pull/16788)
  [https://nvbugs/6490028][fix] Bump only the cross-library `cublas_tolerance` from 1.05 to 1.10 in the test… (#16788)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/misc/test_autotuner.py`_

## Models  (10 commits)

- **2026-08-24** [`ec3ff2e7f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec3ff2e7f5) [#18062](https://github.com/NVIDIA/TensorRT-LLM/pull/18062)
  [None][test] Set Llama4 QA max sequence length (#18062)
  _Files: `tests/integration/defs/test_e2e.py`_
- **2026-08-22** [`75b023cd12`](https://github.com/NVIDIA/TensorRT-LLM/commit/75b023cd12) [#17999](https://github.com/NVIDIA/TensorRT-LLM/pull/17999)
  [None][fix] release Kimi K3 checkpoint mappings after loading (#17999)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`_
- **2026-08-21** [`b4c5450f5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b4c5450f5e) [#18028](https://github.com/NVIDIA/TensorRT-LLM/pull/18028)
  [https://nvbugs/6631848][fix] Size Mistral encoder budget for MMMU (#18028)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-08-20** [`32dbd5b41c`](https://github.com/NVIDIA/TensorRT-LLM/commit/32dbd5b41c) [#17804](https://github.com/NVIDIA/TensorRT-LLM/pull/17804)
  [None][feat] Add Kimi K3 to layer-wise benchmarks (#17804)
  _Files: `examples/layer_wise_benchmarks/README.md`, `examples/layer_wise_benchmarks/run.py`, `tensorrt_llm/_torch/models/modeling_kimi_linear.py`, `tensorrt_llm/tools/layer_wise_benchmarks/mark_utils.py` _+3 more__
- **2026-08-20** [`ab26d98eb1`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab26d98eb1) [#17649](https://github.com/NVIDIA/TensorRT-LLM/pull/17649)
  [https://nvbugs/6535779][fix] Remove stale Qwen3.5 and DeepSeekV32 waivers (#17649)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`8d0e9adb36`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d0e9adb36) [#17364](https://github.com/NVIDIA/TensorRT-LLM/pull/17364)
  [https://nvbugs/6517844][test] Unwaive DeepSeek V3 Lite RTX Pro 6000D test (#17364)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`bbc40d820b`](https://github.com/NVIDIA/TensorRT-LLM/commit/bbc40d820b) [#17957](https://github.com/NVIDIA/TensorRT-LLM/pull/17957)
  [https://nvbugs/6633268][test] waive DeepSeekV3Lite bfloat16 mtp_nextn=2 v2_kv_cache test on DGX B200 (#17957)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-19** [`ee197dcad9`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee197dcad9) [#17945](https://github.com/NVIDIA/TensorRT-LLM/pull/17945)
  [https://nvbugs/6626655][test] Align QA test-list timeout for multimodal Kimi-K2.5 dep8 with pre-merge (#17945)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`3253b64043`](https://github.com/NVIDIA/TensorRT-LLM/commit/3253b64043) [#17809](https://github.com/NVIDIA/TensorRT-LLM/pull/17809)
  [https://nvbugs/6422343][test] Unwaive DeepSeek V3 Lite BF16 test (#17809)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-08-18** [`29d774315c`](https://github.com/NVIDIA/TensorRT-LLM/commit/29d774315c) [#17793](https://github.com/NVIDIA/TensorRT-LLM/pull/17793)
  [TRTLLM-15204][fix] Initialize KDA dt_bias and re-enable the prefill parity suite on B200 (#17793)
  _Files: `tensorrt_llm/_torch/modules/kimi_kda/kimi_kda_mixer.py`, `tests/integration/test_lists/test-db/l0_b200.yml`_

## Speculative Decoding  (7 commits)

- **2026-08-24** [`df437526a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/df437526a2) [#17998](https://github.com/NVIDIA/TensorRT-LLM/pull/17998)
  [https://nvbugs/6550099][fix] Raise no-top-k equivalence tolerance (#17998)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/speculative/hw_agnostic/test_advanced_sampling_mode.py`_
- **2026-08-19** [`8325542983`](https://github.com/NVIDIA/TensorRT-LLM/commit/8325542983) [#17939](https://github.com/NVIDIA/TensorRT-LLM/pull/17939)
  [TRTLLM-15465][feat] Support SA speculative decoding under disaggregated serving for Kimi K3 (#17939)
  _Files: `examples/kimi_k3/README.md`, `examples/kimi_k3/disagg/README.md`, `examples/kimi_k3/disagg/gen_config.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_sa.yaml` _+4 more__
- **2026-08-19** [`03964bf306`](https://github.com/NVIDIA/TensorRT-LLM/commit/03964bf306) [#17701](https://github.com/NVIDIA/TensorRT-LLM/pull/17701)
  [TRTLLM-15406][feat] Support occurrence penalties in one-model speculative decoding (#17701)
  _Files: `docs/source/features/sampling.md`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/vanilla.py`, `tensorrt_llm/_torch/pyexecutor/sampler/penalties.py`, `tensorrt_llm/_torch/speculative/interface.py` _+4 more__
- **2026-08-19** [`e9b0b08a26`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9b0b08a26) [#17837](https://github.com/NVIDIA/TensorRT-LLM/pull/17837)
  [None][fix] Restore Gemma4 shared-KV draft loading (#17837)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/models/modeling_speculative.py` _+7 more__
- **2026-08-18** [`dff59cd5c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/dff59cd5c7) [#17836](https://github.com/NVIDIA/TensorRT-LLM/pull/17836)
  [None][fix] Synchronize one-model MTP scheduler draft tokens (#17836)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-08-17** [`01c7ae3d9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/01c7ae3d9c) [#16733](https://github.com/NVIDIA/TensorRT-LLM/pull/16733)
  [https://nvbugs/6478723][fix] Rename forward -> _forward_impl AND stash the extra dynamic-tree state on… (#16733)
  _Files: `tensorrt_llm/_torch/speculative/mtp_dynamic_tree.py`_
- **2026-08-17** [`2c0eca97d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c0eca97d3) [#17599](https://github.com/NVIDIA/TensorRT-LLM/pull/17599)
  [None][feat] Honor SamplingParams.seed on the one-model speculative path (#17599)
  _Files: `tensorrt_llm/_torch/speculative/eagle3_dynamic_tree.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tests/unittest/_torch/speculative/hw_agnostic/test_rng_window_counter.py`_

## Other  (6 commits)

- **2026-08-24** [`ce6306bb4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce6306bb4a) [#15487](https://github.com/NVIDIA/TensorRT-LLM/pull/15487)
  [https://nvbugs/6337226][fix] Count profiled calls with min() of positive line hits (#15487)
  _Files: `tests/unittest/tools/test_host_profiler.py`_
- **2026-08-22** [`0adaf0182a`](https://github.com/NVIDIA/TensorRT-LLM/commit/0adaf0182a) [#18045](https://github.com/NVIDIA/TensorRT-LLM/pull/18045)
  [None][fix] bound CLI dependency minimums (#18045)
  _Files: `requirements.txt`_
- **2026-08-19** [`89ed0c8f61`](https://github.com/NVIDIA/TensorRT-LLM/commit/89ed0c8f61) [#17919](https://github.com/NVIDIA/TensorRT-LLM/pull/17919)
  [TRTLLM-14628][fix] Do not trust just-written mtimes in sync_tree copy-back (#17919)
  _Files: `scripts/build_wheel.py`, `tests/unittest/scripts/test_build_wheel_copy_back.py`_
- **2026-08-19** [`17175d295d`](https://github.com/NVIDIA/TensorRT-LLM/commit/17175d295d) [#17506](https://github.com/NVIDIA/TensorRT-LLM/pull/17506)
  [https://nvbugs/6581121][fix] Keep the single CSV row (parallel_factor 16 → min(16,8) = 8 workers, matching… (#17506)
  _Files: `tests/integration/defs/agg_unit_mem_df.csv`_
- **2026-08-18** [`36d7d80165`](https://github.com/NVIDIA/TensorRT-LLM/commit/36d7d80165) [#17651](https://github.com/NVIDIA/TensorRT-LLM/pull/17651)
  [https://nvbugs/5547275][test] Scope stage mapping checks to live stages (#17651)
  _Files: `tests/unittest/tools/test_test_to_stage_mapping.py`_
- **2026-08-17** [`77f941f262`](https://github.com/NVIDIA/TensorRT-LLM/commit/77f941f262) [#16358](https://github.com/NVIDIA/TensorRT-LLM/pull/16358)
  [https://nvbugs/6435126][test] Attribute fatal test_unittests_v2 failures to inner tests (#16358)
  _Files: `tests/integration/defs/test_unittests.py`, `tests/unittest/tools/test_unittest_culprits.py`_

## Docs / Examples  (6 commits)

- **2026-08-24** [`97e94e1796`](https://github.com/NVIDIA/TensorRT-LLM/commit/97e94e1796) [#18108](https://github.com/NVIDIA/TensorRT-LLM/pull/18108)
  [None][doc] Fix some typos of modeling agent (#18108)
  _Files: `agent-flow/README.md`, `agent-flow/agent_flow/workflows/modeling_bringup/quick_start.md`_
- **2026-08-20** [`0af651b793`](https://github.com/NVIDIA/TensorRT-LLM/commit/0af651b793) [#16230](https://github.com/NVIDIA/TensorRT-LLM/pull/16230)
  [None][doc] Add tech blog: Evaluating Agentic Serving with Trace Replay and Job-Level Metrics (#16230)
  _Files: `docs/source/blogs/media/tech_blog27_batch_size_sweep_fixed_concurrency.png`, `docs/source/blogs/media/tech_blog27_coder_bc_frontier.png`, `docs/source/blogs/media/tech_blog27_hit_rate_eviction_cliff.png`, `docs/source/blogs/media/tech_blog27_host_offloading.png` _+10 more__
- **2026-08-19** [`da0aecf97d`](https://github.com/NVIDIA/TensorRT-LLM/commit/da0aecf97d) [#17629](https://github.com/NVIDIA/TensorRT-LLM/pull/17629)
  [TRTLLM-14777][doc] Correct LMCache example output guidance (#17629)
  _Files: `examples/llm-api/llm_lmcache_connector.py`_
- **2026-08-19** [`52c62f174b`](https://github.com/NVIDIA/TensorRT-LLM/commit/52c62f174b) [#17869](https://github.com/NVIDIA/TensorRT-LLM/pull/17869)
  [None][chore] Sync vendored agent-flow with upstream (#17869)
  _Files: `.github/CODEOWNERS`, `agent-flow/.gitignore`, `agent-flow/agent_flow/backends/base.py`, `agent-flow/agent_flow/backends/claude_code.py` _+8 more__
- **2026-08-18** [`2894d691f8`](https://github.com/NVIDIA/TensorRT-LLM/commit/2894d691f8) [#17628](https://github.com/NVIDIA/TensorRT-LLM/pull/17628)
  [TRTLLM-14775][doc] Document Helix source test prerequisites (#17628)
  _Files: `docs/source/features/helix.md`_
- **2026-08-18** [`67ceedb137`](https://github.com/NVIDIA/TensorRT-LLM/commit/67ceedb137) [#17716](https://github.com/NVIDIA/TensorRT-LLM/pull/17716)
  [None][fix] Update ModelExpress dependency version (#17716)
  _Files: `docs/source/features/model-express.md`, `setup.py`_

## LoRA  (5 commits)

- **2026-08-24** [`d03aebec63`](https://github.com/NVIDIA/TensorRT-LLM/commit/d03aebec63) [#17435](https://github.com/NVIDIA/TensorRT-LLM/pull/17435)
  [TRTLLM-14622][feat] Add VisualGen dynamic LoRA support (#17435)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/pipeline.py`, `tensorrt_llm/_torch/visual_gen/pipeline_loader.py` _+7 more__
- **2026-08-24** [`57212666fa`](https://github.com/NVIDIA/TensorRT-LLM/commit/57212666fa) [#17464](https://github.com/NVIDIA/TensorRT-LLM/pull/17464)
  [https://nvbugs/6456085][fix] Harmony: stop discarding malformed tool-call messages silently (#17464)
  _Files: `tensorrt_llm/serve/harmony_adapter.py`, `tests/integration/test_lists/test-db/l0_cpu.yml`, `tests/unittest/llmapi/apps/test_harmony_parsing.py`_
- **2026-08-19** [`ab6fdcf86a`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab6fdcf86a) [#17857](https://github.com/NVIDIA/TensorRT-LLM/pull/17857)
  [TRTLLM-14839][chore] Add shim files for root PEFT module relocation (#17857)
  _Files: `.github/CODEOWNERS`, `tensorrt_llm/llmapi/serialization.py`, `tensorrt_llm/lora_helper.py`, `tensorrt_llm/lora_manager.py` _+2 more__
- **2026-08-18** [`6f393c4dcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f393c4dcd) [#17600](https://github.com/NVIDIA/TensorRT-LLM/pull/17600)
  [TRTLLM-15103][test] clean retired phi tests (#17600)
  _Files: `tests/integration/defs/accuracy/references/cnn_dailymail.yaml`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/references/mmlu.yaml`, `tests/integration/defs/accuracy/references/mmmu.yaml` _+28 more__
- **2026-08-18** [`e05a90e351`](https://github.com/NVIDIA/TensorRT-LLM/commit/e05a90e351) [#17678](https://github.com/NVIDIA/TensorRT-LLM/pull/17678)
  [https://nvbugs/6607487][fix] fix LoRA host/device cache dtype reconfiguration race (#17678)
  _Files: `cpp/include/tensorrt_llm/runtime/loraCache.h`, `cpp/tensorrt_llm/batch_manager/peftCacheManager.cpp`, `cpp/tensorrt_llm/runtime/loraCache.cpp`, `tests/integration/test_lists/waives.txt`_

## Perf  (2 commits)

- **2026-08-19** [`a2d234deef`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2d234deef) [#17841](https://github.com/NVIDIA/TensorRT-LLM/pull/17841)
  [None][perf] Address D2D copies in mixed batches (#17841)
  _Files: `3rdparty/patches/msa_strided_paged_kv.patch`_
- **2026-08-19** [`f42674a5db`](https://github.com/NVIDIA/TensorRT-LLM/commit/f42674a5db) [#17905](https://github.com/NVIDIA/TensorRT-LLM/pull/17905)
  [None][doc] Correct per-GPU throughput in ADP Balance blog figure (#17905)
  _Files: `docs/source/blogs/media/tech_blog10_tps_ttft_pareto_curve.png`_

## ROCm / AMD  (2 commits)

- **2026-08-19** [`8e48971814`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e48971814) [#17657](https://github.com/NVIDIA/TensorRT-LLM/pull/17657)
  [None][chore] Extend OpenEngine ownership to dynamo dev (#17657)
  _Files: `.github/CODEOWNERS`_
- **2026-08-17** [`b539ad220b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b539ad220b) [#16303](https://github.com/NVIDIA/TensorRT-LLM/pull/16303)
  [https://nvbugs/6445494][infra] Upgrade Triton to 3.7.0 for Torch 2.12.0 compatibility (#16303)
  _Files: `ATTRIBUTIONS-Python.md`, `README.md`, `docker/common/install_pytorch.sh`, `docs/source/installation/installation-guide.md` _+64 more__

## AutoDeploy  (1 commits)

- **2026-08-22** [`6fc38605c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6fc38605c7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/trtllm-eval/poetry.lock` _+1 more__

## Compilation / Graph  (1 commits)

- **2026-08-17** [`fd913be253`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd913be253) [#17713](https://github.com/NVIDIA/TensorRT-LLM/pull/17713)
  [https://nvbugs/6463822][fix] Remove LTX2 CUDA graph test waiver (#17713)
  _Files: `tests/integration/test_lists/waives.txt`_

---
_Generated 2026-08-24 09:01 UTC_