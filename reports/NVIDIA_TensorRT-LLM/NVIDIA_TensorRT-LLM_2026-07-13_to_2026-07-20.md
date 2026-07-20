# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-07-13 → 2026-07-20  |  **Total commits:** 208

## ✨ New Features This Week

- **2026-07-20** [#15697](https://github.com/NVIDIA/TensorRT-LLM/pull/15697) — [None][feat] Add TensorRT-LLM runtime integration for KV cache compression (#15697)
- **2026-07-20** [#16464](https://github.com/NVIDIA/TensorRT-LLM/pull/16464) — [TRTLLM-14345][feat] Support GDN MTP Replay (#16464)
- **2026-07-20** [#16540](https://github.com/NVIDIA/TensorRT-LLM/pull/16540) — [None][test] Add DeepSeek-V4-Pro perf sanity cases on GB300 (#16540)
- **2026-07-20** [#15908](https://github.com/NVIDIA/TensorRT-LLM/pull/15908) — [None][test] Add opt-in background prefetch of test MPI sessions and model page cache (#15908)
- **2026-07-20** [#16052](https://github.com/NVIDIA/TensorRT-LLM/pull/16052) — [TRTLLM-13235][feat] Support bad_words in TorchSampler (#16052)
- **2026-07-19** [#16369](https://github.com/NVIDIA/TensorRT-LLM/pull/16369) — [TRTLLM-14026][feat] BREAKING: Remove C++ modules for legacy TRT backend (#16369)
- **2026-07-18** [#16395](https://github.com/NVIDIA/TensorRT-LLM/pull/16395) — [None][feat] Append git commit hash to version for editable installs (#16395)
- **2026-07-18** [#15905](https://github.com/NVIDIA/TensorRT-LLM/pull/15905) — [None][feat] Disagg coordinator + multi-process orchestrator fleet (#15905)
- **2026-07-18** [#15641](https://github.com/NVIDIA/TensorRT-LLM/pull/15641) — [TRTLLM-12352][feat] integrate ModelExpress checkpoint loading (#15641)
- **2026-07-18** [#15808](https://github.com/NVIDIA/TensorRT-LLM/pull/15808) — [None][feat] Add DeepSeek DSpark speculative decoding (#15808)
- _…and 27 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-15** [`e322472c64`](https://github.com/NVIDIA/TensorRT-LLM/commit/e322472c64) [#16372](https://github.com/NVIDIA/TensorRT-LLM/pull/16372) — [None][infra] Assign KV cache manager v2 test ownership (#16372)
- **2026-07-14** [`602718366c`](https://github.com/NVIDIA/TensorRT-LLM/commit/602718366c) [#16385](https://github.com/NVIDIA/TensorRT-LLM/pull/16385) — [None][chore] Remove disagg-devs co-ownership of mla.py in CODEOWNERS (#16385)
- **2026-07-13** [`6c43b3eddc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c43b3eddc) [#16053](https://github.com/NVIDIA/TensorRT-LLM/pull/16053) — [None][feat] Support externally provided MPI sessions with explicit ownership (#16053)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-07-17 |
| [#16459](https://github.com/NVIDIA/TensorRT-LLM/issues/16459) | [Bug]: Preserve per-item processed metadata when computing multimodal  | Multimodal | 2026-07-15 |
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
| [#10014](https://github.com/NVIDIA/TensorRT-LLM/issues/10014) | [Documentation] AWS EFA/LIBFABRIC deployment guide for disaggregated i | Doc, Disaggregated serving | 2025-12-15 |
| [#3125](https://github.com/NVIDIA/TensorRT-LLM/issues/3125) | Model built with ReDrafter produces substantially lower quality output | bug, triaged, Investigating, Speculative Decoding, Model customization | 2025-09-09 |
| [#2864](https://github.com/NVIDIA/TensorRT-LLM/issues/2864) | Could not run on a machine with dual RTX 5090s, using WSL2 and Docker | bug, triaged, Investigating, Scale-out, Testing | 2025-09-09 |
| [#7080](https://github.com/NVIDIA/TensorRT-LLM/issues/7080) | [Performance]: Can Scaffolding give more information about kvcache-reu | Performance, KV-Cache Management, Scaffolding | 2025-08-22 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| CI / Infra | 67 |
| Attention | 26 |
| Executor / Runtime | 24 |
| Disaggregation / KV | 19 |
| MoE | 15 |
| Other | 12 |
| Models | 11 |
| Quantization | 8 |
| Torch Path (_torch) | 7 |
| AutoDeploy | 7 |
| Speculative Decoding | 6 |
| Perf | 3 |
| ROCm / AMD | 3 |

## CI / Infra  (67 commits)

- **2026-07-20** [`8bb0c50236`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bb0c50236) [#16591](https://github.com/NVIDIA/TensorRT-LLM/pull/16591)
  [https://nvbugs/6305365][chore] Unwaive piecewise cudagraph related tests (#16591)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`24ae9f4659`](https://github.com/NVIDIA/TensorRT-LLM/commit/24ae9f4659) [#16615](https://github.com/NVIDIA/TensorRT-LLM/pull/16615)
  [None][infra] Waive 1 failed cases for main in pre-merge 48660 (#16615)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`b8604c46ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8604c46ce)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-20** [`a857096693`](https://github.com/NVIDIA/TensorRT-LLM/commit/a857096693) [#16606](https://github.com/NVIDIA/TensorRT-LLM/pull/16606)
  [TRTQA-3278][test] Waive 6 failed cases for main in QA CI (#16606)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`910426f950`](https://github.com/NVIDIA/TensorRT-LLM/commit/910426f950) [#16607](https://github.com/NVIDIA/TensorRT-LLM/pull/16607)
  [TRTQA-3276][test] Waive 3 failed cases for main in QA CI (#16607)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`32110a8544`](https://github.com/NVIDIA/TensorRT-LLM/commit/32110a8544) [#16600](https://github.com/NVIDIA/TensorRT-LLM/pull/16600)
  [None][test] Waive 3 failed cases for main in QA CI (#16600)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`9955555c6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/9955555c6e) [#16604](https://github.com/NVIDIA/TensorRT-LLM/pull/16604)
  [TRTQA-3279][test] Waive 8 failed cases for main in QA CI (#16604)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`af4aff4220`](https://github.com/NVIDIA/TensorRT-LLM/commit/af4aff4220) [#16605](https://github.com/NVIDIA/TensorRT-LLM/pull/16605)
  [None][test] Waive 7 failed cases for main in QA CI (#16605)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`454fed35cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/454fed35cc) [#16480](https://github.com/NVIDIA/TensorRT-LLM/pull/16480)
  [TRTLLMINF-216][infra] use main as default target branch in L0_MergeRequest_PR (#16480)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-07-20** [`5ebcda8c76`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ebcda8c76) [#16602](https://github.com/NVIDIA/TensorRT-LLM/pull/16602)
  [None][test] Waive 7 failed cases for main in QA CI (#16602)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`d42e391e0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d42e391e0c) [#16599](https://github.com/NVIDIA/TensorRT-LLM/pull/16599)
  [None][test] Waive 1 failed cases for main in QA CI (#16599)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`447a628c30`](https://github.com/NVIDIA/TensorRT-LLM/commit/447a628c30) [#16576](https://github.com/NVIDIA/TensorRT-LLM/pull/16576)
  [None][test] Remove 33 closed-bug waive entries for main (#16576)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`826922f147`](https://github.com/NVIDIA/TensorRT-LLM/commit/826922f147) [#16593](https://github.com/NVIDIA/TensorRT-LLM/pull/16593)
  [None][test] Waive 2 failed cases for main in QA CI (#16593)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`3fe4ceb9bc`](https://github.com/NVIDIA/TensorRT-LLM/commit/3fe4ceb9bc) [#16587](https://github.com/NVIDIA/TensorRT-LLM/pull/16587)
  [None][infra] Waive 5 failed cases for main in post-merge 2844 (#16587)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`3ab71753fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ab71753fe) [#16584](https://github.com/NVIDIA/TensorRT-LLM/pull/16584)
  [None][test] Waive 4 failed cases for main in QA CI (#16584)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`7941475e7e`](https://github.com/NVIDIA/TensorRT-LLM/commit/7941475e7e) [#16585](https://github.com/NVIDIA/TensorRT-LLM/pull/16585)
  [None][test] Waive 3 failed cases for main in QA CI (#16585)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`fd4548572f`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd4548572f) [#16582](https://github.com/NVIDIA/TensorRT-LLM/pull/16582)
  [None][infra] Waive 1 failed cases for main in pre-merge 48569 (#16582)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`c253e57976`](https://github.com/NVIDIA/TensorRT-LLM/commit/c253e57976)
  [None][infra] Auto-update test durations from OpenSearch (last 7 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-20** [`cf4973d70e`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf4973d70e)
  [None][infra] Auto-update test durations from OpenSearch (last 3 days)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-07-19** [`1dcde1f917`](https://github.com/NVIDIA/TensorRT-LLM/commit/1dcde1f917) [#13804](https://github.com/NVIDIA/TensorRT-LLM/pull/13804)
  [TRTLLM-5311][infra] Periodically query OpenSearch for test duration and push to main automatically (#13804)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/UpdateTestDurations.groovy`, `jenkins/scripts/generate_duration.py`, `scripts/generate_duration.py` _+1 more__
- **2026-07-19** [`3124bb3525`](https://github.com/NVIDIA/TensorRT-LLM/commit/3124bb3525) [#16318](https://github.com/NVIDIA/TensorRT-LLM/pull/16318)
  [TRTLLMINF-188][infra] Require approval for broad post-merge bot runs (#16318)
  _Files: `.github/workflows/bot-command.yml`, `.github/workflows/post-merge-approval.yml`, `docs/source/developer-guide/ci-overview.md`_
- **2026-07-18** [`0e1c2629e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e1c2629e5) [#16547](https://github.com/NVIDIA/TensorRT-LLM/pull/16547)
  [None][chore] update allowlist 2026-07-17 (#16547)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-17** [`3e1d6e7429`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e1d6e7429) [#15730](https://github.com/NVIDIA/TensorRT-LLM/pull/15730)
  [https://nvbugs/6272644][fix] Stabilize and unwaive multi-GPU VisualGen LPIPS tests (#15730)
  _Files: `requirements-dev.txt`, `tests/integration/defs/examples/visual_gen/conftest.py`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media.zip`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/wan22_t2v_fa4_fully_eager_lpips_golden_video.json` _+4 more__
- **2026-07-17** [`334aaa8fb5`](https://github.com/NVIDIA/TensorRT-LLM/commit/334aaa8fb5) [#16535](https://github.com/NVIDIA/TensorRT-LLM/pull/16535)
  [None][test] Remove all 1k1k perf-sanity cases from CI (#16535)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_b200_multi_gpus_perf_sanity.yml`, `tests/integration/test_lists/test-db/l0_b200_multi_nodes_perf_sanity_ctx1_node1_gpu4_gen1_node1_gpu8.yml` _+18 more__
- **2026-07-17** [`3eefb000c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3eefb000c9) [#16351](https://github.com/NVIDIA/TensorRT-LLM/pull/16351)
  [None][test] Promote disagg perf sanity tests to pre-merge for functional verification (#16351)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/perf/README_test_perf_sanity.md`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/test-db/l0_b200_multi_nodes_perf_sanity_ctx1_node1_gpu4_gen1_node1_gpu8.yml` _+3 more__
- **2026-07-17** [`01f34634e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/01f34634e6) [#16541](https://github.com/NVIDIA/TensorRT-LLM/pull/16541)
  [None][infra] Add blossom-ci authorized users (#16541)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-07-17** [`c963514656`](https://github.com/NVIDIA/TensorRT-LLM/commit/c963514656) [#16519](https://github.com/NVIDIA/TensorRT-LLM/pull/16519)
  [None][infra] Waive 1 failed cases for main in pre-merge 48139 (#16519)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-17** [`09e0d3f7cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/09e0d3f7cb) [#16474](https://github.com/NVIDIA/TensorRT-LLM/pull/16474)
  [https://nvbugs/6422339][fix] unwaive disagg tests (#16474)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`a2595c099c`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2595c099c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-07-16** [`107e972d61`](https://github.com/NVIDIA/TensorRT-LLM/commit/107e972d61) [#16503](https://github.com/NVIDIA/TensorRT-LLM/pull/16503)
  [None][infra] Handle SBSA image tags for x86 CI agents (#16503)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_Test.groovy`_
- **2026-07-16** [`21c6d5bcf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/21c6d5bcf2) [#15674](https://github.com/NVIDIA/TensorRT-LLM/pull/15674)
  [TRTLLMINF-99][infra] Add SLURM frontend failover to L0 (#15674)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-16** [`b602fa6f91`](https://github.com/NVIDIA/TensorRT-LLM/commit/b602fa6f91) [#16495](https://github.com/NVIDIA/TensorRT-LLM/pull/16495)
  [None][infra] Waive 3 failed cases for main in pre-merge 48086 (#16495)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`274043a75a`](https://github.com/NVIDIA/TensorRT-LLM/commit/274043a75a) [#16194](https://github.com/NVIDIA/TensorRT-LLM/pull/16194)
  [None][infra] Upgrade NIXL to v1.3.1 (#16194)
  _Files: `docker/common/install_nixl.sh`, `jenkins/current_image_tags.properties`, `requirements-dev.txt`_
- **2026-07-16** [`51457cc661`](https://github.com/NVIDIA/TensorRT-LLM/commit/51457cc661) [#16367](https://github.com/NVIDIA/TensorRT-LLM/pull/16367)
  [https://nvbugs/6327143][chore] Unwaive test cases (#16367)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`5f377be2e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f377be2e7) [#16368](https://github.com/NVIDIA/TensorRT-LLM/pull/16368)
  [None][infra] Auto-label PRs by component from CODEOWNERS (#16368)
  _Files: `.github/scripts/label_component.py`, `.github/workflows/label_component_pr.yml`_
- **2026-07-16** [`5006f4ebdc`](https://github.com/NVIDIA/TensorRT-LLM/commit/5006f4ebdc) [#16470](https://github.com/NVIDIA/TensorRT-LLM/pull/16470)
  [None][infra] Waive 1 failed cases for main in pre-merge 48013 (#16470)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`6013944d1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/6013944d1e) [#16465](https://github.com/NVIDIA/TensorRT-LLM/pull/16465)
  [None][infra] Waive 14 failed cases for main in post-merge 2839 (#16465)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`659dee9326`](https://github.com/NVIDIA/TensorRT-LLM/commit/659dee9326) [#16414](https://github.com/NVIDIA/TensorRT-LLM/pull/16414)
  [None][fix] Skip commented-out lines in Groovy stage parsing (#16414)
  _Files: `jenkins/scripts/cbts/blocks.py`_
- **2026-07-16** [`02c2c01470`](https://github.com/NVIDIA/TensorRT-LLM/commit/02c2c01470) [#16461](https://github.com/NVIDIA/TensorRT-LLM/pull/16461)
  [None][chore] Waive failing torch-compile test (#16461)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`d3301ba5ae`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3301ba5ae) [#16452](https://github.com/NVIDIA/TensorRT-LLM/pull/16452)
  [None][infra] Waive 1 failed cases for main in pre-merge 47930 (#16452)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`2dbbd170a3`](https://github.com/NVIDIA/TensorRT-LLM/commit/2dbbd170a3) [#16450](https://github.com/NVIDIA/TensorRT-LLM/pull/16450)
  [None][infra] Waive 1 failed cases for main in pre-merge 47953 (#16450)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`7b6c17dffe`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b6c17dffe) [#16442](https://github.com/NVIDIA/TensorRT-LLM/pull/16442)
  [None][infra] Waive 1 failed cases for main in pre-merge 47847 (#16442)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`495611cda2`](https://github.com/NVIDIA/TensorRT-LLM/commit/495611cda2) [#16443](https://github.com/NVIDIA/TensorRT-LLM/pull/16443)
  [None][infra] Waive 1 failed cases for main in pre-merge 47847 (#16443)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`862306bd73`](https://github.com/NVIDIA/TensorRT-LLM/commit/862306bd73) [#16361](https://github.com/NVIDIA/TensorRT-LLM/pull/16361)
  [None][infra] Waive 1 failed cases for main in pre-merge 47597 (#16361)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`5722cf0799`](https://github.com/NVIDIA/TensorRT-LLM/commit/5722cf0799) [#15455](https://github.com/NVIDIA/TensorRT-LLM/pull/15455)
  [None][infra] Tail Slurm job logs when job is no longer active. (#15455)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-15** [`5344a0ad72`](https://github.com/NVIDIA/TensorRT-LLM/commit/5344a0ad72) [#16316](https://github.com/NVIDIA/TensorRT-LLM/pull/16316)
  [https://nvbugs/6445332][test] Remove test waivers for nvbug 6445332 (code fix merged in #16326) (#16316)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`07af1dea34`](https://github.com/NVIDIA/TensorRT-LLM/commit/07af1dea34) [#16423](https://github.com/NVIDIA/TensorRT-LLM/pull/16423)
  [None][infra] Waive 2 failed cases for main in pre-merge 47854 (#16423)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`e54fe5565d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e54fe5565d) [#15121](https://github.com/NVIDIA/TensorRT-LLM/pull/15121)
  [https://nvbugs/6260897][fix] Relax line-589 assertion to accept either IN_PROGRESS or SUCCESS (FAILURE… (#15121)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/bindings/test_transfer_agent_bindings.py`_
- **2026-07-15** [`baa7279e86`](https://github.com/NVIDIA/TensorRT-LLM/commit/baa7279e86) [#16412](https://github.com/NVIDIA/TensorRT-LLM/pull/16412)
  [None][test] Waive 1 failed cases for main in QA CI (#16412)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`7d002f6863`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d002f6863) [#16328](https://github.com/NVIDIA/TensorRT-LLM/pull/16328)
  [None][test] Refine CBTS logic for handling `-Perf-` stages (#16328)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`_
- **2026-07-15** [`71d829199f`](https://github.com/NVIDIA/TensorRT-LLM/commit/71d829199f)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-07-14** [`544199a47b`](https://github.com/NVIDIA/TensorRT-LLM/commit/544199a47b) [#16359](https://github.com/NVIDIA/TensorRT-LLM/pull/16359)
  [None][infra] Enable B300 stages (#16359)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-14** [`671bfec14a`](https://github.com/NVIDIA/TensorRT-LLM/commit/671bfec14a) [#16042](https://github.com/NVIDIA/TensorRT-LLM/pull/16042)
  [None][test] Waive 7 failed cases for main in QA CI (#16042)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`3865c655ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/3865c655ce) [#16061](https://github.com/NVIDIA/TensorRT-LLM/pull/16061)
  [None][test] Waive 8 failed cases for main in QA CI (#16061)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`017ccee1ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/017ccee1ce) [#16366](https://github.com/NVIDIA/TensorRT-LLM/pull/16366)
  [None][infra] Waive 1 failed cases for main in pre-merge 47605 (#16366)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`d9fcebc653`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9fcebc653) [#16243](https://github.com/NVIDIA/TensorRT-LLM/pull/16243)
  [None][test] Waive 1 failed cases for main in QA CI (#16243)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`9274258131`](https://github.com/NVIDIA/TensorRT-LLM/commit/9274258131) [#16356](https://github.com/NVIDIA/TensorRT-LLM/pull/16356)
  [None][infra] Waive 3 failed cases for main in post-merge 2836 (#16356)
  _Files: `.github/CODEOWNERS`, `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`e9f101b138`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9f101b138) [#16310](https://github.com/NVIDIA/TensorRT-LLM/pull/16310)
  [https://nvbugs/6445322][fix] Restore the pre-#16108 baseline `- accuracy: 56.667` alongside the existing… (#16310)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`da3830473a`](https://github.com/NVIDIA/TensorRT-LLM/commit/da3830473a)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`_
- **2026-07-13** [`1225445ceb`](https://github.com/NVIDIA/TensorRT-LLM/commit/1225445ceb) [#16334](https://github.com/NVIDIA/TensorRT-LLM/pull/16334)
  [None][ci] Disable B300 stages during aws-pdx cluster maintenance (#16334)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-13** [`01291f9466`](https://github.com/NVIDIA/TensorRT-LLM/commit/01291f9466) [#16180](https://github.com/NVIDIA/TensorRT-LLM/pull/16180)
  [https://nvbugs/6379333] [chore] Unwaive test cases (#16180)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`53d2bde62f`](https://github.com/NVIDIA/TensorRT-LLM/commit/53d2bde62f) [#16308](https://github.com/NVIDIA/TensorRT-LLM/pull/16308)
  [https://nvbugs/6437410][chore] Waive a failed test in pre-merge CI (#16308)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`6bd6bb888d`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bd6bb888d) [#16283](https://github.com/NVIDIA/TensorRT-LLM/pull/16283)
  [None][test] Waive 1 failed cases for main in QA CI (#16283)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`75e80082d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/75e80082d3) [#16296](https://github.com/NVIDIA/TensorRT-LLM/pull/16296)
  [None][test] Waive 4 failed cases for main in QA CI (#16296)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`ffe313d5c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffe313d5c3) [#16295](https://github.com/NVIDIA/TensorRT-LLM/pull/16295)
  [None][test] Waive 6 failed cases for main in QA CI (#16295)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`29bda273bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/29bda273bf) [#16271](https://github.com/NVIDIA/TensorRT-LLM/pull/16271)
  [None][test] Waive 9 failed cases for main in QA CI (#16271)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-13** [`770ebc5db5`](https://github.com/NVIDIA/TensorRT-LLM/commit/770ebc5db5) [#16292](https://github.com/NVIDIA/TensorRT-LLM/pull/16292)
  [None][infra] Waive 7 failed cases for main in post-merge 2835 (#16292)
  _Files: `tests/integration/test_lists/waives.txt`_

## Attention  (26 commits)

- **2026-07-20** [`d94540b429`](https://github.com/NVIDIA/TensorRT-LLM/commit/d94540b429) [#16466](https://github.com/NVIDIA/TensorRT-LLM/pull/16466)
  [None][fix] Fix DeepSeek V4 KV cache warmup handling and serveral other issues (#16466)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+3 more__
- **2026-07-20** [`52ae70934f`](https://github.com/NVIDIA/TensorRT-LLM/commit/52ae70934f) [#16052](https://github.com/NVIDIA/TensorRT-LLM/pull/16052)
  [TRTLLM-13235][feat] Support bad_words in TorchSampler (#16052)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler/ops/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampler.py`, `tensorrt_llm/_torch/pyexecutor/sampler/sampling_utils.py` _+3 more__
- **2026-07-19** [`d97397437f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d97397437f) [#16382](https://github.com/NVIDIA/TensorRT-LLM/pull/16382)
  [https://nvbugs/6442074][fix] Make one-model spec-dec attn-metadata save/restore exception-safe (#16382)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/speculative/dflash.py`, `tensorrt_llm/_torch/speculative/draft_target.py`, `tensorrt_llm/_torch/speculative/eagle3.py` _+7 more__
- **2026-07-18** [`147404864d`](https://github.com/NVIDIA/TensorRT-LLM/commit/147404864d) [#15808](https://github.com/NVIDIA/TensorRT-LLM/pull/15808)
  [None][feat] Add DeepSeek DSpark speculative decoding (#15808)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/dspark/__init__.py`, `tensorrt_llm/_torch/models/dspark/attention.py` _+26 more__
- **2026-07-17** [`66f76b607d`](https://github.com/NVIDIA/TensorRT-LLM/commit/66f76b607d) [#16509](https://github.com/NVIDIA/TensorRT-LLM/pull/16509)
  [None][perf] Various Gemma4 related perf fixes (#16509)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/models/modeling_gemma4_vision.py`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_
- **2026-07-17** [`5b6548439a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5b6548439a) [#15434](https://github.com/NVIDIA/TensorRT-LLM/pull/15434)
  [#15344][fix] Add SM121 MLA cache reuse support (#15434)
  _Files: `docs/source/models/supported-models.md`, `examples/models/core/deepseek_v3/README.md`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`, `tests/unittest/_torch/executor/test_py_executor_creator_mla_cache_reuse_sync.py`_
- **2026-07-17** [`a2ab5934ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/a2ab5934ca) [#16307](https://github.com/NVIDIA/TensorRT-LLM/pull/16307)
  [None][fix] DSA CuteDSL paged-MQA-logits: persistent output buffer (CUDA-graph stale-pointer IMA) (#16307)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-07-17** [`f4df481dbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4df481dbb) [#16313](https://github.com/NVIDIA/TensorRT-LLM/pull/16313)
  [TRTLLM-14054][perf] Reduce per-step host preparation overhead in the PyTorch executor decode path (#16313)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py` _+5 more__
- **2026-07-16** [`4277d156cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/4277d156cd) [#15775](https://github.com/NVIDIA/TensorRT-LLM/pull/15775)
  [TRTLLM-13321][feat] Extend rejection sampling to one-model speculative decoding (MTP/DRAFT_TARGET/PARD/DFLASH) (#15775)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py` _+18 more__
- **2026-07-15** [`0846183218`](https://github.com/NVIDIA/TensorRT-LLM/commit/0846183218) [#16218](https://github.com/NVIDIA/TensorRT-LLM/pull/16218)
  [None][chore] KVCacheManagerV2: Python and test preparation for a C++ backend (#16218)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/disaggregation/resource/kv_extractor.py`, `tensorrt_llm/_torch/disaggregation/resource/utils.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py` _+29 more__
- **2026-07-15** [`46bf21b1bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/46bf21b1bf) [#16365](https://github.com/NVIDIA/TensorRT-LLM/pull/16365)
  [TRTLLM-13212][refactor] Unify sampler ops and clean up dead code in TorchSampler (#16365)
  _Files: `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.cu`, `cpp/tensorrt_llm/thop/dynamicTreeOp.cpp`, `tensorrt_llm/_torch/auto_deploy/shim/demollm.py`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+6 more__
- **2026-07-15** [`9115e48391`](https://github.com/NVIDIA/TensorRT-LLM/commit/9115e48391) [#16099](https://github.com/NVIDIA/TensorRT-LLM/pull/16099)
  [None][fix] Fix Gemma4 illegal memory access when max_seq_len is at most the sliding window size (#16099)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modeling/test_gemma4_e2e_dummy.py`_
- **2026-07-15** [`d3436a0d0d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d3436a0d0d) [#16400](https://github.com/NVIDIA/TensorRT-LLM/pull/16400)
  [https://nvbugs/6403909][test] Remove attention backend test waiver (#16400)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`eac54d1d9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/eac54d1d9e) [#16376](https://github.com/NVIDIA/TensorRT-LLM/pull/16376)
  [https://nvbugs/6426860][fix] Stabilize compressor BF16 tolerance (#16376)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_compressor_kernel.py`_
- **2026-07-15** [`501777ac89`](https://github.com/NVIDIA/TensorRT-LLM/commit/501777ac89) [#14848](https://github.com/NVIDIA/TensorRT-LLM/pull/14848)
  [TRTLLM-12373][feat] RMSNorm nvfp4 quant fusion for DS V3.2 / Kimi-K2.5 (#14848)
  _Files: `cpp/tensorrt_llm/kernels/rmsNormFp4QuantKernels.cu`, `cpp/tensorrt_llm/kernels/rmsNormFp4QuantKernels.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/rmsNormFp4Quant.cpp` _+12 more__
- **2026-07-14** [`58d8964d13`](https://github.com/NVIDIA/TensorRT-LLM/commit/58d8964d13) [#15238](https://github.com/NVIDIA/TensorRT-LLM/pull/15238)
  [TRTLLM-12721][fix] Add gated C++ NIXL in-flight cancellation and safe cleanup (#15238)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.h` _+23 more__
- **2026-07-14** [`f665e59a7d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f665e59a7d) [#15666](https://github.com/NVIDIA/TensorRT-LLM/pull/15666)
  [None][feat] Add Laguna DFlash drafter support (#15666)
  _Files: `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/decoderXQAImplJIT/compileEngine.cpp`, `tensorrt_llm/_torch/models/modeling_laguna.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/speculative/dflash.py` _+6 more__
- **2026-07-14** [`3249f03688`](https://github.com/NVIDIA/TensorRT-LLM/commit/3249f03688) [#16185](https://github.com/NVIDIA/TensorRT-LLM/pull/16185)
  [None][feat] Integrate KVCMv2 `commit_min_snapshot` in runtime (#16185)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tests/unittest/_torch/attention/sparse/deepseek_v4/test_deepseek_v4_cache_manager.py`, `tests/unittest/_torch/executor/test_kv_cache_manager_v2.py` _+2 more__
- **2026-07-14** [`771d3857ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/771d3857ef) [#16311](https://github.com/NVIDIA/TensorRT-LLM/pull/16311)
  [https://nvbugs/6438658][fix] Fix MLA KV cache estimation sizing (#16311)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_kv_cache_estimation.py`_
- **2026-07-14** [`f41cfeb11d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f41cfeb11d) [#14374](https://github.com/NVIDIA/TensorRT-LLM/pull/14374)
  [https://nvbugs/6115271][fix] Fix LTX-2 Attention Metadata issue (#14374)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+1 more__
- **2026-07-14** [`13f8716205`](https://github.com/NVIDIA/TensorRT-LLM/commit/13f8716205) [#15815](https://github.com/NVIDIA/TensorRT-LLM/pull/15815)
  [TRTLLM-13696][test] Part1: Add CPU only CI stage (#15815)
  _Files: `jenkins/L0_Test.groovy`, `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tensorrt_llm/_torch/cuda_tile_utils.py` _+13 more__
- **2026-07-13** [`e4a8dda776`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4a8dda776) [#16221](https://github.com/NVIDIA/TensorRT-LLM/pull/16221)
  [None][fix] Fix fused mHC output reuse and extend compressor next_n (#16221)
  _Files: `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/mhcKernels/mhcFusedHcKernel.cu`, `cpp/tensorrt_llm/thop/compressorOp.cpp`, `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py` _+4 more__
- **2026-07-13** [`4a86ff538d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a86ff538d) [#16073](https://github.com/NVIDIA/TensorRT-LLM/pull/16073)
  [TRTLLM-14138][perf] Make FlashInfer decode plans sync-free with host-built page tables (#16073)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_
- **2026-07-13** [`c47715a2b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c47715a2b2) [#16236](https://github.com/NVIDIA/TensorRT-LLM/pull/16236)
  [None][fix] source DSA metadata from sparse params (#16236)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/deepseek_v4.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-07-13** [`9fe5d0f735`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fe5d0f735) [#16167](https://github.com/NVIDIA/TensorRT-LLM/pull/16167)
  [https://nvbugs/6430674][fix] Surgical revert of PR #15838's dispatch guard removal: re-add… (#16167)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`_
- **2026-07-13** [`5a5cba0743`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a5cba0743) [#16225](https://github.com/NVIDIA/TensorRT-LLM/pull/16225)
  [None][fix] Correct RocketKV KT cache byte accounting for FP8 KV cache (#16225)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/rocket.py`, `tests/unittest/_torch/attention/sparse/rocketkv/test_rocketkv.py`_

## Executor / Runtime  (24 commits)

- **2026-07-20** [`ee241d25f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/ee241d25f4) [#16464](https://github.com/NVIDIA/TensorRT-LLM/pull/16464)
  [TRTLLM-14345][feat] Support GDN MTP Replay (#16464)
  _Files: `tensorrt_llm/_torch/modules/fla/cached_replay.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+7 more__
- **2026-07-20** [`a72b6469c3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a72b6469c3) [#16226](https://github.com/NVIDIA/TensorRT-LLM/pull/16226)
  [https://nvbugs/6426852][fix] Fix intermittent cuda mapping error (#16226)
  _Files: `tensorrt_llm/executor/ray_executor.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`, `tests/unittest/_torch/ray_orchestrator/single_gpu/test_llm_update_weights.py`_
- **2026-07-20** [`5a4d258798`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a4d258798) [#16312](https://github.com/NVIDIA/TensorRT-LLM/pull/16312)
  [TRTLLM-13409][fix] make proxy shutdown non-blocking when the engine is dead (#16312)
  _Files: `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/llmapi/mpi_session.py`, `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-07-18** [`6967d0eaf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6967d0eaf2) [#15641](https://github.com/NVIDIA/TensorRT-LLM/pull/15641)
  [TRTLLM-12352][feat] integrate ModelExpress checkpoint loading (#15641)
  _Files: `docker/Dockerfile.multi`, `docs/source/features/checkpoint-loading.md`, `docs/source/features/model-express.md`, `docs/source/index.rst` _+6 more__
- **2026-07-17** [`e2874ec8a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2874ec8a7) [#15852](https://github.com/NVIDIA/TensorRT-LLM/pull/15852)
  [None][feat] Qwen3-VL: support mixed image+video modality requests (#15852)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+15 more__
- **2026-07-17** [`8dba04bebf`](https://github.com/NVIDIA/TensorRT-LLM/commit/8dba04bebf) [#16178](https://github.com/NVIDIA/TensorRT-LLM/pull/16178)
  [None][perf] Prewarm DeepGEMM paged_mqa_logits_metadata JIT buckets (#16178)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-17** [`fd74257413`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd74257413) [#16453](https://github.com/NVIDIA/TensorRT-LLM/pull/16453)
  [https://nvbugs/6336747][fix] Honor GenerationResult timeout (#16453)
  _Files: `tensorrt_llm/executor/result.py`, `tensorrt_llm/llmapi/utils.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/test_executor.py`_
- **2026-07-17** [`459839cc27`](https://github.com/NVIDIA/TensorRT-LLM/commit/459839cc27) [#16256](https://github.com/NVIDIA/TensorRT-LLM/pull/16256)
  [https://nvbugs/6404567][fix] Clamp piecewise cudagraph captures to the reachable ceiling instead of force-appending it (#16256)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-07-16** [`e15883702b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e15883702b) [#16444](https://github.com/NVIDIA/TensorRT-LLM/pull/16444)
  [https://nvbugs/6435642][fix] handle session reuse worker registration (#16444)
  _Files: `tensorrt_llm/executor/proxy.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/executor/test_proxy_fast_death.py`_
- **2026-07-16** [`abe4b17136`](https://github.com/NVIDIA/TensorRT-LLM/commit/abe4b17136) [#15734](https://github.com/NVIDIA/TensorRT-LLM/pull/15734)
  [TRTLLM-6905][feat] MM encoder cache (#15734)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/modeling_mistral.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+12 more__
- **2026-07-16** [`8b5d9ea5fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b5d9ea5fc) [#16164](https://github.com/NVIDIA/TensorRT-LLM/pull/16164)
  [None][feat] BREAKING: add per-model transceiver runtime auto selection (#16164)
  _Files: `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/_torch/models/modeling_utils.py`, `tensorrt_llm/_torch/pyexecutor/kv_cache_transceiver.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py` _+5 more__
- **2026-07-15** [`573bd5f0b8`](https://github.com/NVIDIA/TensorRT-LLM/commit/573bd5f0b8) [#16250](https://github.com/NVIDIA/TensorRT-LLM/pull/16250)
  [https://nvbugs/6405760][fix] Do not load the multimodal encoder for text-only trtllm-bench runs (#16250)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/models/modeling_qwen3vl.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+6 more__
- **2026-07-15** [`a1302a5c76`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1302a5c76) [#16238](https://github.com/NVIDIA/TensorRT-LLM/pull/16238)
  [TRTLLM-12352][feat] add post-transform capability profiles (#16238)
  _Files: `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/weight_sharing/__init__.py`, `tensorrt_llm/_torch/weight_sharing/post_transform_profiles.py` _+5 more__
- **2026-07-15** [`287c12a364`](https://github.com/NVIDIA/TensorRT-LLM/commit/287c12a364) [#16249](https://github.com/NVIDIA/TensorRT-LLM/pull/16249)
  [https://nvbugs/6269388][fix] Raise error to enforce HMAC encryption in IPC (#16249)
  _Files: `tensorrt_llm/executor/ipc.py`_
- **2026-07-15** [`bcf5a20e05`](https://github.com/NVIDIA/TensorRT-LLM/commit/bcf5a20e05) [#16401](https://github.com/NVIDIA/TensorRT-LLM/pull/16401)
  [None][fix] fix missing torch_dtype_to_binding (#16401)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`_
- **2026-07-15** [`e05790a1ca`](https://github.com/NVIDIA/TensorRT-LLM/commit/e05790a1ca) [#16338](https://github.com/NVIDIA/TensorRT-LLM/pull/16338)
  [https://nvbugs/6435642][fix] detect killed MPI executor workers (#16338)
  _Files: `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/worker.py`, `tensorrt_llm/executor/worker_process_monitor.py`, `tests/unittest/executor/test_fatal_error_health_check.py`_
- **2026-07-14** [`5ee89c045d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ee89c045d) [#16212](https://github.com/NVIDIA/TensorRT-LLM/pull/16212)
  [https://nvbugs/6127669][fix] Fix layer-wise benchmarks performance alignment test (#16212)
  _Files: `examples/layer_wise_benchmarks/README.md`, `examples/layer_wise_benchmarks/parse.py`, `examples/layer_wise_benchmarks/parse_e2e.py`, `examples/layer_wise_benchmarks/parser_utils.py` _+4 more__
- **2026-07-14** [`42e0e703ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/42e0e703ce) [#16232](https://github.com/NVIDIA/TensorRT-LLM/pull/16232)
  [None][perf] Memoize multimodal run metadata and drop identity block-offset gather (#16232)
  _Files: `tensorrt_llm/_torch/pyexecutor/kv_cache_manager_v2.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_
- **2026-07-14** [`67e8dc9ba3`](https://github.com/NVIDIA/TensorRT-LLM/commit/67e8dc9ba3) [#16326](https://github.com/NVIDIA/TensorRT-LLM/pull/16326)
  [TRTLLM-14040][fix] Fix multi-GPU VisualGen response IPC: REBUILD_LOCAL handle crossed a process boundary (#16326)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tests/unittest/visual_gen/test_executor_shared_tensor_ipc.py`_
- **2026-07-13** [`f81b9d2787`](https://github.com/NVIDIA/TensorRT-LLM/commit/f81b9d2787) [#16233](https://github.com/NVIDIA/TensorRT-LLM/pull/16233)
  [None][fix] Fix VSWA gate in KVCacheManager window-size resolution (#16233)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/test_resource_manager.py`_
- **2026-07-13** [`17190cf7bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/17190cf7bb) [#15752](https://github.com/NVIDIA/TensorRT-LLM/pull/15752)
  [None][feat] add commit min snapshot for SSM reuse (#15752)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_config.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py` _+4 more__
- **2026-07-13** [`52fc8f465b`](https://github.com/NVIDIA/TensorRT-LLM/commit/52fc8f465b) [#15588](https://github.com/NVIDIA/TensorRT-LLM/pull/15588)
  [https://nvbugs/6330273][fix] Reserve worst-case SWA slots to avoid single-request deadlock (#15588)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_life_cycle_registry.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_storage_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_event_manager.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-07-13** [`d6e9bf3355`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6e9bf3355) [#16248](https://github.com/NVIDIA/TensorRT-LLM/pull/16248)
  [https://nvbugs/6438658][fix] Avoid false disagg benchmark KV exhaustion (#16248)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-07-13** [`696904a6d3`](https://github.com/NVIDIA/TensorRT-LLM/commit/696904a6d3) [#16197](https://github.com/NVIDIA/TensorRT-LLM/pull/16197)
  [None][fix] Fix indexer-k-cache transfer for disagg (#16197)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`_

## Disaggregation / KV  (19 commits)

- **2026-07-20** [`d6add927fe`](https://github.com/NVIDIA/TensorRT-LLM/commit/d6add927fe) [#15697](https://github.com/NVIDIA/TensorRT-LLM/pull/15697)
  [None][feat] Add TensorRT-LLM runtime integration for KV cache compression (#15697)
  _Files: `tensorrt_llm/_torch/kv_cache_compression/__init__.py`, `tensorrt_llm/_torch/kv_cache_compression/interface.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/pyexecutor/_util.py` _+9 more__
- **2026-07-20** [`fc88aea0e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc88aea0e8) [#16481](https://github.com/NVIDIA/TensorRT-LLM/pull/16481)
  [https://nvbugs/6314696] [fix] update disaggregated GB200 test configs (#16481)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/test-db/l0_gb200_multi_nodes_perf_sanity_ctx1_node2_gpu8_gen1_node8_gpu32.yml` _+3 more__
- **2026-07-20** [`d1eda80491`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1eda80491) [#16586](https://github.com/NVIDIA/TensorRT-LLM/pull/16586)
  [None][chore] Remove all 1k1k cases from QA's disagg side (#16586)
  _Files: `tests/integration/test_lists/qa/llm_perf_disagg.yml`, `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/integration/test_lists/qa/llm_perf_multinode.yml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con1024_ctx1_dep4_gen1_dep32_eplb0_mtp0_ccb-NIXL.yaml` _+58 more__
- **2026-07-19** [`176041ba15`](https://github.com/NVIDIA/TensorRT-LLM/commit/176041ba15) [#16445](https://github.com/NVIDIA/TensorRT-LLM/pull/16445)
  [nvbugs/6440089][fix][test] Guard KvCacheAwareRouter against server-list churn; replace accuracy=0.0 stopgap with incomplete_rate metric (#16445)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/test-db/l0_dgx_h200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-07-19** [`f4c5c935aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4c5c935aa) [#16570](https://github.com/NVIDIA/TensorRT-LLM/pull/16570)
  [None][test] Consolidate test coverage for helix (#16570)
  _Files: `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml` _+1 more__
- **2026-07-18** [`682c38d7cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/682c38d7cd) [#16429](https://github.com/NVIDIA/TensorRT-LLM/pull/16429)
  [None][fix] disagg: derive KV transfer layer offset from physical slot order (#16429)
  _Files: `tensorrt_llm/_torch/disaggregation/native/peer.py`, `tests/unittest/disaggregated/test_peer.py`_
- **2026-07-18** [`29bd1034c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/29bd1034c9) [#15905](https://github.com/NVIDIA/TensorRT-LLM/pull/15905)
  [None][feat] Disagg coordinator + multi-process orchestrator fleet (#15905)
  _Files: `docs/source/features/disagg-serving.md`, `tensorrt_llm/commands/serve.py`, `tensorrt_llm/llmapi/disagg_utils.py`, `tensorrt_llm/serve/conversation_id.py` _+22 more__
- **2026-07-17** [`74739166e2`](https://github.com/NVIDIA/TensorRT-LLM/commit/74739166e2) [#16528](https://github.com/NVIDIA/TensorRT-LLM/pull/16528)
  [https://nvbugs/6329052][fix] Change the config for DSV3 disagg conditional test (#16528)
  _Files: `tests/integration/defs/disaggregated/test_configs/disagg_config_cache_reuse_deepseek_v3.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`b5321af204`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5321af204) [#16456](https://github.com/NVIDIA/TensorRT-LLM/pull/16456)
  [None][test] disagg startup: detect and fail fast on worker OOM/crash (#16456)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/integration/defs/conftest.py`, `tests/integration/defs/disaggregated/disagg_test_utils.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`_
- **2026-07-16** [`4188dbe330`](https://github.com/NVIDIA/TensorRT-LLM/commit/4188dbe330) [#15966](https://github.com/NVIDIA/TensorRT-LLM/pull/15966)
  [TRTLLM-13639][perf] Migrate Kimi perf-sanity tests to Transceiver v2 (#15966)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb200_kimi-k25-thinking-fp4_1k1k_con2048_ctx1_dep4_gen1_dep32_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_kimi-k25-thinking-fp4_1k1k_con4096_ctx1_dep4_gen1_dep8_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_kimi-k25-thinking-fp4_1k1k_con4_ctx1_dep4_gen1_tep4_eplb0_mtp0_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_kimi-k25-thinking-fp4_8k1k_con1024_ctx1_dep4_gen1_dep32_eplb416_mtp3_ccb-NIXL.yaml` _+8 more__
- **2026-07-16** [`4a682fd246`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a682fd246) [#16116](https://github.com/NVIDIA/TensorRT-LLM/pull/16116)
  [None][fix] Enhance the dis-agg bounce buffer workflow (#16116)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/agentBindings.cpp`, `tensorrt_llm/_torch/disaggregation/native/bounce/config.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/core.py`, `tensorrt_llm/_torch/disaggregation/native/bounce/impl.py` _+8 more__
- **2026-07-16** [`a914fe4cd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/a914fe4cd8) [#15999](https://github.com/NVIDIA/TensorRT-LLM/pull/15999)
  [https://nvbugs/6414762][fix] Minor fixes for helix tests (#15999)
  _Files: `cpp/tensorrt_llm/executor/requestImpl.h`, `cpp/tests/unit_tests/multi_gpu/cacheTransceiverTest.cpp`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`3b330ca063`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b330ca063) [#16415](https://github.com/NVIDIA/TensorRT-LLM/pull/16415)
  [None][chore] add disagg-devs as code owner for disaggregated tests (#16415)
  _Files: `.github/CODEOWNERS`_
- **2026-07-15** [`f84b6dac8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f84b6dac8b) [#15245](https://github.com/NVIDIA/TensorRT-LLM/pull/15245)
  [None][feat] Python transceiver support cpp cache manager + offload (#15245)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tensorrt_llm/nanobind/batch_manager/kvCacheManager.cpp`, `tensorrt_llm/_torch/disaggregation/resource/cache_reuse.py` _+5 more__
- **2026-07-15** [`ad440e3fdd`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad440e3fdd) [#15824](https://github.com/NVIDIA/TensorRT-LLM/pull/15824)
  [None][fix] align KV slice token_range.end with transferred block count (#15824)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tests/unittest/disaggregated/test_cache_reuse_adapter.py`_
- **2026-07-15** [`999618ee2d`](https://github.com/NVIDIA/TensorRT-LLM/commit/999618ee2d) [#16304](https://github.com/NVIDIA/TensorRT-LLM/pull/16304)
  [https://nvbugs/6374873][fix] Allow fp4 KV Cache + non-FP4 Mamba State (#16304)
  _Files: `cpp/tests/unit_tests/batch_manager/kvCacheManagerTest.cpp`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tests/unittest/_torch/executor/test_mamba_cache_manager.py` _+1 more__
- **2026-07-13** [`e8321d2097`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8321d2097) [#16083](https://github.com/NVIDIA/TensorRT-LLM/pull/16083)
  [None][chore] Remove unused token_range and is_last_slice parameters from _create_kv_slice (#16083)
  _Files: `tensorrt_llm/_torch/disaggregation/transceiver.py`, `tests/unittest/disaggregated/test_cache_reuse_adapter.py`_
- **2026-07-13** [`5088a4dbde`](https://github.com/NVIDIA/TensorRT-LLM/commit/5088a4dbde) [#15533](https://github.com/NVIDIA/TensorRT-LLM/pull/15533)
  [None][chore] Clean deprecated CppMambaCacheManager (#15533)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/rnnCacheFormatter.h`, `cpp/tensorrt_llm/batch_manager/cacheTransceiver.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransferLayer.cpp` _+19 more__
- **2026-07-13** [`c883622b6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c883622b6b) [#15823](https://github.com/NVIDIA/TensorRT-LLM/pull/15823)
  [None][feat] add per-model KV cache manager v2 auto selection (#15823)
  _Files: `examples/llm-api/quickstart_advanced.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/llmapi/llm_args.py` _+4 more__

## MoE  (15 commits)

- **2026-07-20** [`8bd00e4e3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bd00e4e3e) [#16540](https://github.com/NVIDIA/TensorRT-LLM/pull/16540)
  [None][test] Add DeepSeek-V4-Pro perf sanity cases on GB300 (#16540)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/local/submit.py`, `jenkins/scripts/perf/submit.py`, `tests/integration/defs/perf/_model_paths.py` _+19 more__
- **2026-07-20** [`0b03361010`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b03361010) [#15908](https://github.com/NVIDIA/TensorRT-LLM/pull/15908)
  [None][test] Add opt-in background prefetch of test MPI sessions and model page cache (#15908)
  _Files: `tensorrt_llm/llmapi/mpi_session.py`, `tests/conftest.py`, `tests/integration/defs/conftest.py`, `tests/integration/defs/pytest.ini` _+12 more__
- **2026-07-19** [`d470e919ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/d470e919ee)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+22 more__
- **2026-07-18** [`14f8138269`](https://github.com/NVIDIA/TensorRT-LLM/commit/14f8138269)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+20 more__
- **2026-07-17** [`d541ae5680`](https://github.com/NVIDIA/TensorRT-LLM/commit/d541ae5680) [#16539](https://github.com/NVIDIA/TensorRT-LLM/pull/16539)
  [None][doc] Add DeepSeek-V4 optimization tech blog (#16539)
  _Files: `.gitattributes`, `README.md`, `docs/source/blogs/media/tech_blog26_agentperf_closed_loop_workflow.svg`, `docs/source/blogs/media/tech_blog26_deepseek_v4_hybrid_attention.png` _+5 more__
- **2026-07-17** [`1228fed15d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1228fed15d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+20 more__
- **2026-07-16** [`a273f0f3c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/a273f0f3c8)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+18 more__
- **2026-07-16** [`adc8c4d619`](https://github.com/NVIDIA/TensorRT-LLM/commit/adc8c4d619) [#16286](https://github.com/NVIDIA/TensorRT-LLM/pull/16286)
  [https://nvbugs/6412108][fix] AutoDeploy:Shard shared Qwen3.5 experts (#16286)
  _Files: `examples/auto_deploy/model_registry/configs/qwen3.5_moe_400b.yaml`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_qwen3_5_moe.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`803f5cae1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/803f5cae1e) [#16299](https://github.com/NVIDIA/TensorRT-LLM/pull/16299)
  [None][perf] fuse gdn post-conv split, QK norm and gating and  RMSNorm with FP8 quantization (#16299)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/_torch/modules/mamba/fuse_elementwise_ops.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/modules/mamba/layernorm_gated.py` _+2 more__
- **2026-07-15** [`95f9f92a76`](https://github.com/NVIDIA/TensorRT-LLM/commit/95f9f92a76) [#16068](https://github.com/NVIDIA/TensorRT-LLM/pull/16068)
  [None][test] Split test_moe_backend TRTLLM by quant=None to avoid in-process IMA cascade (#16068)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/moe/moe_test_utils.py`_
- **2026-07-14** [`5053c2bdda`](https://github.com/NVIDIA/TensorRT-LLM/commit/5053c2bdda) [#15410](https://github.com/NVIDIA/TensorRT-LLM/pull/15410)
  [https://nvbugs/6245862][fix] Fix MoE EP divisibility check for EPLB configurations (#15410)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/interface.py`_
- **2026-07-14** [`9aae1b8a44`](https://github.com/NVIDIA/TensorRT-LLM/commit/9aae1b8a44) [#16200](https://github.com/NVIDIA/TensorRT-LLM/pull/16200)
  [https://nvbugs/6430702][perf] Restore NVLink one-sided A2A fast path (#16200)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h`, `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`, `tensorrt_llm/_torch/alltoall_watchdog.py` _+6 more__
- **2026-07-14** [`046952a60f`](https://github.com/NVIDIA/TensorRT-LLM/commit/046952a60f) [#15835](https://github.com/NVIDIA/TensorRT-LLM/pull/15835)
  [None][perf] Cute DSL GVR Top-K: short-row remove cluster sync in run_one_row (#15835)
  _Files: `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/top_k/gvr_topk_decode.py`, `tests/unittest/_torch/attention/sparse/test_cute_dsl_gvr_topk_decode.py`_
- **2026-07-13** [`0c2952efcf`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c2952efcf) [#16290](https://github.com/NVIDIA/TensorRT-LLM/pull/16290)
  [None][fix] DSA indexer: persistent topk-output buffer to avoid CUDA-graph stale-pointer IMA (#16290)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tests/unittest/_torch/attention/sparse/dsa/test_dsa_indexer.py`_
- **2026-07-13** [`44c3adf9e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/44c3adf9e6) [#16293](https://github.com/NVIDIA/TensorRT-LLM/pull/16293)
  [https://nvbugs/6428113][fix] Fix TEP token-count handling in MoE Test (#16293)
  _Files: `tests/unittest/_torch/modules/test_moe_routing.py`_

## Other  (12 commits)

- **2026-07-19** [`c77bc6ed6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c77bc6ed6b) [#16369](https://github.com/NVIDIA/TensorRT-LLM/pull/16369)
  [TRTLLM-14026][feat] BREAKING: Remove C++ modules for legacy TRT backend (#16369)
- **2026-07-18** [`f1434b7781`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1434b7781) [#16395](https://github.com/NVIDIA/TensorRT-LLM/pull/16395)
  [None][feat] Append git commit hash to version for editable installs (#16395)
  _Files: `setup.py`_
- **2026-07-17** [`9fdfd10c17`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fdfd10c17) [#16538](https://github.com/NVIDIA/TensorRT-LLM/pull/16538)
  [None][test] Update LLM performance test cases to use increased input/output lengths (#16538)
  _Files: `tests/integration/test_lists/qa/llm_perf_core.yml`_
- **2026-07-17** [`8e1f6ea0c7`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e1f6ea0c7) [#16451](https://github.com/NVIDIA/TensorRT-LLM/pull/16451)
  [None][test] add --keep-workspace pytest option to skip workspace cleanup (#16451)
  _Files: `tests/integration/defs/conftest.py`_
- **2026-07-16** [`d7cefb6de9`](https://github.com/NVIDIA/TensorRT-LLM/commit/d7cefb6de9) [#16512](https://github.com/NVIDIA/TensorRT-LLM/pull/16512)
  [None][chore] Update API update missed in Dynamo test (#16512)
  _Files: `tests/unittest/dynamo/test_imports.py`_
- **2026-07-15** [`97e387da49`](https://github.com/NVIDIA/TensorRT-LLM/commit/97e387da49) [#16209](https://github.com/NVIDIA/TensorRT-LLM/pull/16209)
  [None][test] Fix the multinode test case on DGX-Spark(perf skipped and func hang) (#16209)
  _Files: `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/test_e2e.py`_
- **2026-07-14** [`b20691b71d`](https://github.com/NVIDIA/TensorRT-LLM/commit/b20691b71d) [#16373](https://github.com/NVIDIA/TensorRT-LLM/pull/16373)
  [None][chore] Remove deprecated rules (#16373)
  _Files: `.github/CODEOWNERS`_
- **2026-07-14** [`5ec6f56e2d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5ec6f56e2d) [#14397](https://github.com/NVIDIA/TensorRT-LLM/pull/14397)
  [None][feat] Enable agent serving evaluation via trace-replay on Scaffolding (#14397)
- **2026-07-14** [`7e833f7220`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e833f7220) [#15918](https://github.com/NVIDIA/TensorRT-LLM/pull/15918)
  [TRTLLM-14022][feat] BREAKING: Remove python modules and tests for legacy TensorRT backend (#15918)
- **2026-07-14** [`b432db32cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/b432db32cb) [#16321](https://github.com/NVIDIA/TensorRT-LLM/pull/16321)
  [None][chore] Code review group (#16321)
  _Files: `.github/CODEOWNERS`_
- **2026-07-13** [`11a880f4fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/11a880f4fb) [#16298](https://github.com/NVIDIA/TensorRT-LLM/pull/16298)
  [None][test] Restrict gen-worker per-iter mean to steady-state iterations (#16298)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-07-13** [`3bff181f8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3bff181f8a) [#16172](https://github.com/NVIDIA/TensorRT-LLM/pull/16172)
  [https://nvbugs/6323074][fix] fix flaky hang issue for disagg gen-onl… (#16172)

## Models  (11 commits)

- **2026-07-20** [`56c3734511`](https://github.com/NVIDIA/TensorRT-LLM/commit/56c3734511) [#16588](https://github.com/NVIDIA/TensorRT-LLM/pull/16588)
  [None][infra] Waive B300 Nemotron SuperV3 MTP and Mistral Large3 timeout cases (#16588)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-20** [`699e2277a4`](https://github.com/NVIDIA/TensorRT-LLM/commit/699e2277a4) [#16534](https://github.com/NVIDIA/TensorRT-LLM/pull/16534)
  [https://nvbugs/6316983][chore] Unwaive TestQwen2_5_VL_7B::test_auto_dtype (#16534)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-19** [`f6bd3e2b78`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6bd3e2b78) [#16573](https://github.com/NVIDIA/TensorRT-LLM/pull/16573)
  [https://nvbugs/6476233][test] waive DeepSeek V3.2 tests on DGX H200 (#16573)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-17** [`29f4552bfc`](https://github.com/NVIDIA/TensorRT-LLM/commit/29f4552bfc) [#16378](https://github.com/NVIDIA/TensorRT-LLM/pull/16378)
  [None][fix] Fix unfused RoPE for yarn models: double rotation and GPT-OSS pairing (#16378)
  _Files: `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tensorrt_llm/functional.py`, `tests/unittest/_torch/modules/test_rotary_embedding.py`_
- **2026-07-16** [`a0545b7446`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0545b7446) [#16391](https://github.com/NVIDIA/TensorRT-LLM/pull/16391)
  [None][fix] Fix Qwen image CUDA graph with CFG (#16391)
  _Files: `tensorrt_llm/_torch/visual_gen/models/qwen_image/pipeline_qwen_image.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-07-16** [`44f05214ce`](https://github.com/NVIDIA/TensorRT-LLM/commit/44f05214ce) [#15919](https://github.com/NVIDIA/TensorRT-LLM/pull/15919)
  [None][feat] Add DeepSeek-V4-Pro curated configs (#15919)
  _Files: `examples/configs/curated/deepseek-v4-pro-latency.yaml`, `examples/configs/curated/deepseek-v4-pro-throughput.yaml`, `examples/configs/curated/lookup.yaml`_
- **2026-07-15** [`0623958120`](https://github.com/NVIDIA/TensorRT-LLM/commit/0623958120) [#16392](https://github.com/NVIDIA/TensorRT-LLM/pull/16392)
  [https://nvbugs/6283537][fix] Unwaive TestQwen3_5_4B::test_bf16 (#16392)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`725d9a1aaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/725d9a1aaf) [#16267](https://github.com/NVIDIA/TensorRT-LLM/pull/16267)
  [https://nvbugs/6428144][test] Unwaive GB300 DeepSeek-R1 gen-only disagg PerfSanity (#16267)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`924978f7a0`](https://github.com/NVIDIA/TensorRT-LLM/commit/924978f7a0) [#16353](https://github.com/NVIDIA/TensorRT-LLM/pull/16353)
  [TRTLLM-14054][perf] Qwen3.5-VL: pass the inner LM's normalized model_config to the weight mapper (#16353)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`_
- **2026-07-14** [`0f05df4f4c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0f05df4f4c) [#16314](https://github.com/NVIDIA/TensorRT-LLM/pull/16314)
  [TRTLLM-14054][perf] Load Qwen3-Next GDN in_proj in dense layout and add a multi-row gated RMSNorm (#16314)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_next_weight_mapper.py`, `tensorrt_llm/_torch/modules/mamba/fuse_elementwise_ops.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/modules/mamba/layernorm_gated.py` _+1 more__
- **2026-07-14** [`7d7c364ae9`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d7c364ae9) [#16264](https://github.com/NVIDIA/TensorRT-LLM/pull/16264)
  [None][fix] Align dense Qwen3.5-VL SSM cache dtype test with #16065 semantics (#16264)
  _Files: `tests/unittest/_torch/modeling/test_modeling_qwen3_5_vl.py`_

## Quantization  (8 commits)

- **2026-07-20** [`26e476a4df`](https://github.com/NVIDIA/TensorRT-LLM/commit/26e476a4df) [#16245](https://github.com/NVIDIA/TensorRT-LLM/pull/16245)
  [None][fix] remove unsupported INT8 from trtllm-bench --quantization choices (#16245)
  _Files: `tensorrt_llm/bench/utils/__init__.py`, `tests/unittest/others/test_bench.py`, `tests/unittest/others/test_bench_data.py`_
- **2026-07-20** [`79c62c2276`](https://github.com/NVIDIA/TensorRT-LLM/commit/79c62c2276)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+17 more__
- **2026-07-17** [`ed1a0b9bfa`](https://github.com/NVIDIA/TensorRT-LLM/commit/ed1a0b9bfa) [#16398](https://github.com/NVIDIA/TensorRT-LLM/pull/16398)
  [https://nvbugs/6272673][chore] Unwaive DeepSeek V3 Lite NVFP4 test (#16398)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-16** [`4cf830a894`](https://github.com/NVIDIA/TensorRT-LLM/commit/4cf830a894)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/core/qwen2audio/poetry.lock`, `security_scanning/examples/models/core/qwenvl/poetry.lock` _+8 more__
- **2026-07-15** [`d17ba0e4dc`](https://github.com/NVIDIA/TensorRT-LLM/commit/d17ba0e4dc) [#15909](https://github.com/NVIDIA/TensorRT-LLM/pull/15909)
  [TRTLLM-14024][feat] Prune CuTe DSL NVFP4 GEMM autotuner tactics with nvMatmulHeuristics (#15909)
  _Files: `docs/source/torch/adding_custom_kernels.md`, `requirements.txt`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/custom_ops/cutedsl_matmul_heuristics.py` _+3 more__
- **2026-07-14** [`5e16fdb55c`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e16fdb55c) [#16352](https://github.com/NVIDIA/TensorRT-LLM/pull/16352)
  [TRTLLM-14054][fix] LMHead: pass true full dims to Linear for quantized TP>1 (#16352)
  _Files: `tensorrt_llm/_torch/modules/embedding.py`_
- **2026-07-14** [`4919218934`](https://github.com/NVIDIA/TensorRT-LLM/commit/4919218934) [#16357](https://github.com/NVIDIA/TensorRT-LLM/pull/16357)
  [None][test] Skip test_disaggregated_llama_context_capacity fp8 on hopper (#16357)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated_single_gpu.py`_
- **2026-07-13** [`9a2f5389e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a2f5389e7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock` _+21 more__

## Torch Path (_torch)  (7 commits)

- **2026-07-20** [`f354b77834`](https://github.com/NVIDIA/TensorRT-LLM/commit/f354b77834) [#16521](https://github.com/NVIDIA/TensorRT-LLM/pull/16521)
  [None][test] Assert MTP acceptance length in ADP + LM-head-TP accuracy tests (#16521)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-07-16** [`ef90708ed2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef90708ed2) [#16066](https://github.com/NVIDIA/TensorRT-LLM/pull/16066)
  [TRTLLM-14123][feat] add ParallelVAE_TrtllmWan for native Wan VAE (#16066)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/parallel_vae.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan_i2v.py`, `tensorrt_llm/_torch/visual_gen/models/wan/vae_loader.py` _+5 more__
- **2026-07-14** [`02cedf6e4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/02cedf6e4e) [#15087](https://github.com/NVIDIA/TensorRT-LLM/pull/15087)
  [TRTLLMINF-127][infra] Upgrade dependencies for NGC PyTorch 26.05 stack (#15087)
  _Files: `docker/Dockerfile.multi`, `docker/common/install_pytorch.sh`, `docker/common/install_tensorrt.sh`, `docs/source/installation/installation-guide.md` _+5 more__
- **2026-07-14** [`cc9eb09cfe`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc9eb09cfe) [#16228](https://github.com/NVIDIA/TensorRT-LLM/pull/16228)
  [TRTLLM-14234][perf] LTX-2: replicate audio stream across Ulysses ranks by default (#16228)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`_
- **2026-07-14** [`3e9932c1e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e9932c1e9) [#16199](https://github.com/NVIDIA/TensorRT-LLM/pull/16199)
  [https://nvbugs/6434572][fix] Add a new `pytorch_model_config.py` pattern block covering the six 4-GPU… (#16199)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`_
- **2026-07-13** [`50142a98bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/50142a98bf) [#15213](https://github.com/NVIDIA/TensorRT-LLM/pull/15213)
  [None][chore] Fix lock_infra_error (#15213)
  _Files: `tensorrt_llm/_torch/model_config.py`_
- **2026-07-13** [`e9b8e91dba`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9b8e91dba) [#16054](https://github.com/NVIDIA/TensorRT-LLM/pull/16054)
  [None][feat] Add an opt-in raw-weight cache to the HF weight loader (#16054)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/weight_loader.py`, `tests/unittest/_torch/models/checkpoints/hf/test_weight_loader.py`_

## AutoDeploy  (7 commits)

- **2026-07-18** [`634abb850f`](https://github.com/NVIDIA/TensorRT-LLM/commit/634abb850f) [#16408](https://github.com/NVIDIA/TensorRT-LLM/pull/16408)
  [None][fix] Copy all AutoDeploy tests to Paragraf (#16408)
  _Files: `examples/auto_deploy/paragraf/README.md`, `examples/auto_deploy/paragraf/create_standalone_package.py`, `tests/unittest/auto_deploy/standalone/test_standalone_package.py`, `tests/unittest/auto_deploy/standalone/test_standalone_test_export.py`_
- **2026-07-16** [`d0483a3ae2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0483a3ae2) [#16389](https://github.com/NVIDIA/TensorRT-LLM/pull/16389)
  [https://nvbugs/6403920][fix] Move allreduce strategy test to smoke, use full-warp hidden_size (#16389)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/multigpu/custom_ops/test_ad_dist_strategies.py`, `tests/unittest/auto_deploy/multigpu/smoke/test_ad_allreduce_strategies.py`_
- **2026-07-16** [`f033c65203`](https://github.com/NVIDIA/TensorRT-LLM/commit/f033c65203) [#16229](https://github.com/NVIDIA/TensorRT-LLM/pull/16229)
  [TRTLLM-12838][infra] enhance function-level code coverage for catching subprocess data (#16229)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/blocks.py`, `jenkins/scripts/cbts/coverage_utils/README.md` _+19 more__
- **2026-07-15** [`a8c9e208ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8c9e208ee) [#16383](https://github.com/NVIDIA/TensorRT-LLM/pull/16383)
  [https://nvbugs/6396422][fix] Disable kv-cache reuse for MiniMax-M2 (#16383)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-15** [`5977a19fe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/5977a19fe3) [#16324](https://github.com/NVIDIA/TensorRT-LLM/pull/16324)
  [None][chore] Rename AutoDeploy standalone package to Paragraf (#16324)
  _Files: `examples/auto_deploy/README.md`, `examples/auto_deploy/llmc/create_standalone_package.py`, `examples/auto_deploy/paragraf/CONTRIBUTING.md`, `examples/auto_deploy/paragraf/README.md` _+11 more__
- **2026-07-13** [`43dfc81ffd`](https://github.com/NVIDIA/TensorRT-LLM/commit/43dfc81ffd)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/examples/serve/poetry.lock` _+3 more__
- **2026-07-13** [`56033086de`](https://github.com/NVIDIA/TensorRT-LLM/commit/56033086de) [#16285](https://github.com/NVIDIA/TensorRT-LLM/pull/16285)
  [https://nvbugs/6367792][fix] unwaive Nano AutoDeploy tests (#16285)
  _Files: `tests/integration/test_lists/waives.txt`_

## Speculative Decoding  (6 commits)

- **2026-07-20** [`fa54a19df5`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa54a19df5) [#16579](https://github.com/NVIDIA/TensorRT-LLM/pull/16579)
  [https://nvbugs/6442074][fix] Unbreak main: DSparkWorker forward rename + test stub _forward_impl (#16579)
  _Files: `tensorrt_llm/_torch/speculative/dspark.py`, `tests/unittest/_torch/speculative/test_rejection_buffers_guard.py`_
- **2026-07-17** [`28be4aebd7`](https://github.com/NVIDIA/TensorRT-LLM/commit/28be4aebd7) [#16440](https://github.com/NVIDIA/TensorRT-LLM/pull/16440)
  [https://nvbugs/6460072][fix] Split the caller — for `use_lm_head_tp_in_adp and is_all_greedy_sample`, keep… (#16440)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/interface.py`_
- **2026-07-14** [`1662a877f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/1662a877f3) [#16279](https://github.com/NVIDIA/TensorRT-LLM/pull/16279)
  [None][fix] Seq-slot pool overlap headroom with consistent slot-indexed buffer sizing (#16279)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py` _+7 more__
- **2026-07-14** [`890e108942`](https://github.com/NVIDIA/TensorRT-LLM/commit/890e108942) [#16121](https://github.com/NVIDIA/TensorRT-LLM/pull/16121)
  [https://nvbugs/6422334][fix] In PyExecutor._prepare_draft_requests, gate the py_last_draft_tokens snapshot… (#16121)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-14** [`ffa5396be8`](https://github.com/NVIDIA/TensorRT-LLM/commit/ffa5396be8) [#15777](https://github.com/NVIDIA/TensorRT-LLM/pull/15777)
  [None][test] Optimize LLM test startup overhead (#15777)
  _Files: `tests/conftest.py`, `tests/integration/defs/pytest.ini`, `tests/test_common/grouped_test_utils.py`, `tests/test_common/session_reuse.py` _+4 more__
- **2026-07-13** [`54d484fd3c`](https://github.com/NVIDIA/TensorRT-LLM/commit/54d484fd3c) [#12905](https://github.com/NVIDIA/TensorRT-LLM/pull/12905)
  [TRTLLM-11558][feat] BREAKING: Acceptance rate based speculation off in one model path (#12905)
  _Files: `docs/source/developer-guide/telemetry.md`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/speculative/speculation_gate.py`, `tensorrt_llm/llmapi/llm_args.py` _+3 more__

## Perf  (3 commits)

- **2026-07-15** [`47ded3ff4f`](https://github.com/NVIDIA/TensorRT-LLM/commit/47ded3ff4f) [#16340](https://github.com/NVIDIA/TensorRT-LLM/pull/16340)
  [None][perf] Optimize Video Hashing Speed (#16340)
  _Files: `tensorrt_llm/inputs/media_io.py`, `tensorrt_llm/inputs/multimodal_data.py`, `tests/unittest/inputs/test_video_data_hashing.py`_
- **2026-07-13** [`a201a43a16`](https://github.com/NVIDIA/TensorRT-LLM/commit/a201a43a16) [#15284](https://github.com/NVIDIA/TensorRT-LLM/pull/15284)
  [None][perf] offload chat template rendering into async (#15284)
  _Files: `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/resource_governor.py`, `tensorrt_llm/serve/responses_utils.py` _+1 more__
- **2026-07-13** [`c7d2498bda`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7d2498bda) [#16126](https://github.com/NVIDIA/TensorRT-LLM/pull/16126)
  [None][perf] serve: opt-in msgspec msgpack transport for disagg orchestrator->worker request body (#16126)
  _Files: `requirements.txt`, `tensorrt_llm/serve/openai_client.py`, `tensorrt_llm/serve/openai_server.py`_

## ROCm / AMD  (3 commits)

- **2026-07-15** [`e322472c64`](https://github.com/NVIDIA/TensorRT-LLM/commit/e322472c64) [#16372](https://github.com/NVIDIA/TensorRT-LLM/pull/16372)
  [None][infra] Assign KV cache manager v2 test ownership (#16372)
  _Files: `.github/CODEOWNERS`_
- **2026-07-14** [`602718366c`](https://github.com/NVIDIA/TensorRT-LLM/commit/602718366c) [#16385](https://github.com/NVIDIA/TensorRT-LLM/pull/16385)
  [None][chore] Remove disagg-devs co-ownership of mla.py in CODEOWNERS (#16385)
  _Files: `.github/CODEOWNERS`_
- **2026-07-13** [`6c43b3eddc`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c43b3eddc) [#16053](https://github.com/NVIDIA/TensorRT-LLM/pull/16053)
  [None][feat] Support externally provided MPI sessions with explicit ownership (#16053)
  _Files: `tensorrt_llm/_torch/distributed/communicator.py`, `tensorrt_llm/executor/executor.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/rpc_proxy.py` _+2 more__

---
_Generated 2026-07-20 11:12 UTC_