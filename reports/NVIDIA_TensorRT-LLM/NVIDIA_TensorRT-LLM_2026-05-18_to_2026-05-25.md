# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-05-18 → 2026-05-25  |  **Total commits:** 186

## ✨ New Features This Week

- **2026-05-25** [#13478](https://github.com/NVIDIA/TensorRT-LLM/pull/13478) — [TRTLLM-13429][feat] Switch DeepSeek/NemotronH/Qwen3/Qwen3.5-MoE to sharding-IR canonical models (#13478)
- **2026-05-25** [#14507](https://github.com/NVIDIA/TensorRT-LLM/pull/14507) — [TRTLLM-12635][feat] add bench_moe microbenchmark (#14507)
- **2026-05-25** [#12947](https://github.com/NVIDIA/TensorRT-LLM/pull/12947) — [None][feat] Add SkipSoftmax sparse attention support for visual generation (#12947)
- **2026-05-25** [#13428](https://github.com/NVIDIA/TensorRT-LLM/pull/13428) — [None][feat] Add FlashInfer MLA attention backend support (#13428)
- **2026-05-25** [#14060](https://github.com/NVIDIA/TensorRT-LLM/pull/14060) — [TRTLLM-12027][feat] Disagg serving support with block reuse ON for hybrid models (#14060)
- **2026-05-24** [#14412](https://github.com/NVIDIA/TensorRT-LLM/pull/14412) — [None][feat] support SWA scratch reuse rewind (#14412)
- **2026-05-23** [#14462](https://github.com/NVIDIA/TensorRT-LLM/pull/14462) — [None][feat] Update cubins to resolve FMHA PDL issue (#14462)
- **2026-05-23** [#14471](https://github.com/NVIDIA/TensorRT-LLM/pull/14471) — [None][feat] Disable mamba replay by default (#14471)
- **2026-05-22** [#14463](https://github.com/NVIDIA/TensorRT-LLM/pull/14463) — [None][doc] Update Gemma 4 entries in supported-models.md (#14463)
- **2026-05-22** [#12525](https://github.com/NVIDIA/TensorRT-LLM/pull/12525) — [None][feat] Disable shared paged index in flashinfer trtllm-gen fmha kernel and unify kv cache buffer calculation with thop.attention (#12525)
- _…and 31 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-24 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |
| [#14100](https://github.com/NVIDIA/TensorRT-LLM/issues/14100) | [Bug] trtllm-serve /v1/chat/completions: audio_url with data: URI base | bug, Multimodal | 2026-05-14 |
| [#10663](https://github.com/NVIDIA/TensorRT-LLM/issues/10663) | [Bug]: Exceptions in PyTorch workflow worker processes lead to hanging | bug, Investigating, Speculative Decoding, Pytorch | 2026-05-13 |
| [#13318](https://github.com/NVIDIA/TensorRT-LLM/issues/13318) | [Bug]: Scheduler deadlock on main + #12976 + #13029: AssertionError to | bug, KV-Cache Management, Pytorch | 2026-04-22 |
| [#4910](https://github.com/NVIDIA/TensorRT-LLM/issues/4910) | CUDA error CUBLAS_STATUS_EXECUTION_FAILED when launching Qwen2.5-VL-72 | bug, triaged, Scale-out, Model optimization, Multimodal | 2026-03-30 |
| [#12183](https://github.com/NVIDIA/TensorRT-LLM/issues/12183) | [Bug]: AutoDeploy: nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 gene | bug, Triton backend | 2026-03-13 |
| [#5783](https://github.com/NVIDIA/TensorRT-LLM/issues/5783) | Performance Issue: TensorRT-LLM (v0.20.0/v25.06) Significantly Slower  | bug, triaged, Performance, Investigating, Model optimization, General perf | 2026-02-03 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-01-27 |
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
| CI / Infra | 44 |
| MoE | 25 |
| Executor / Runtime | 21 |
| Attention | 20 |
| Models | 16 |
| Other | 14 |
| Disaggregation / KV | 11 |
| Quantization | 9 |
| AutoDeploy | 8 |
| Torch Path (_torch) | 8 |
| Speculative Decoding | 6 |
| Docs / Examples | 2 |
| LoRA | 1 |
| Perf | 1 |

## CI / Infra  (44 commits)

- **2026-05-25** [`4517988cb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/4517988cb3) [#14515](https://github.com/NVIDIA/TensorRT-LLM/pull/14515)
  [None][infra] Waive 9 failed cases for main in post-merge (#14515)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`66b6fb0fce`](https://github.com/NVIDIA/TensorRT-LLM/commit/66b6fb0fce) [#14525](https://github.com/NVIDIA/TensorRT-LLM/pull/14525)
  [TRTLLM-12942][ci] Dedup misc unit tests on B200 (#14525)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-05-25** [`2e3a75c223`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e3a75c223) [#14516](https://github.com/NVIDIA/TensorRT-LLM/pull/14516)
  [None][infra] Waive 5 failed cases for main in post-merge 2733 (#14516)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`e6d4f9f2f9`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6d4f9f2f9) [#14514](https://github.com/NVIDIA/TensorRT-LLM/pull/14514)
  [None][infra] Waive 10 failed cases for main in post-merge 2733 (#14514)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`ce788e0208`](https://github.com/NVIDIA/TensorRT-LLM/commit/ce788e0208) [#14503](https://github.com/NVIDIA/TensorRT-LLM/pull/14503)
  [None][test] Waive 1 failed cases for main in QA CI (#14503)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`8e691e89b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/8e691e89b7) [#14504](https://github.com/NVIDIA/TensorRT-LLM/pull/14504)
  [None][test] Waive 7 failed cases for main in QA CI (#14504)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`5712b9a35d`](https://github.com/NVIDIA/TensorRT-LLM/commit/5712b9a35d) [#14461](https://github.com/NVIDIA/TensorRT-LLM/pull/14461)
  [https://nvbugs/6185248][test] Unwaive K2.5 thinking MTP3 perf sanity test (#14461)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-23** [`c5b0372aa4`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5b0372aa4) [#14485](https://github.com/NVIDIA/TensorRT-LLM/pull/14485)
  [None][infra] Waive 1 failed cases for main in pre-merge 39582 (#14485)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-22** [`827d0c1c8d`](https://github.com/NVIDIA/TensorRT-LLM/commit/827d0c1c8d) [#14372](https://github.com/NVIDIA/TensorRT-LLM/pull/14372)
  [https://nvbugs/6185192][fix] raise Wan 2.2 VBench threshold (#14372)
  _Files: `tests/integration/defs/examples/test_visual_gen.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-22** [`fac947c01f`](https://github.com/NVIDIA/TensorRT-LLM/commit/fac947c01f) [#14430](https://github.com/NVIDIA/TensorRT-LLM/pull/14430)
  [None][infra] Fix container scanning according to security teams latest update (#14430)
  _Files: `jenkins/TensorRT_LLM_PLC.groovy`_
- **2026-05-22** [`25f7ca8b73`](https://github.com/NVIDIA/TensorRT-LLM/commit/25f7ca8b73) [#14415](https://github.com/NVIDIA/TensorRT-LLM/pull/14415)
  [None][fix] Cap infra-retry budget at 2 attempts total (#14415)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-22** [`30b87fcd90`](https://github.com/NVIDIA/TensorRT-LLM/commit/30b87fcd90) [#14450](https://github.com/NVIDIA/TensorRT-LLM/pull/14450)
  [None][infra] Waive 2 failed cases for main in post-merge (#14450)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-22** [`d1c587ebda`](https://github.com/NVIDIA/TensorRT-LLM/commit/d1c587ebda) [#14455](https://github.com/NVIDIA/TensorRT-LLM/pull/14455)
  [None][infra] Waive 1 failed cases for main in pre-merge 39395 (#14455)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-22** [`6b69a8bd57`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b69a8bd57) [#14387](https://github.com/NVIDIA/TensorRT-LLM/pull/14387)
  [https://nvbugs/6112497][test] Unwaive passing test (#14387)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`24b68fc1d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/24b68fc1d0) [#14323](https://github.com/NVIDIA/TensorRT-LLM/pull/14323)
  [TRTLLMINF-89][feat] Make L0 retries timeout-budget aware (#14323)
  _Files: `jenkins/Build.groovy`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`_
- **2026-05-21** [`736d580f80`](https://github.com/NVIDIA/TensorRT-LLM/commit/736d580f80) [#14405](https://github.com/NVIDIA/TensorRT-LLM/pull/14405)
  [None][infra] Waive 6 failed cases for main in post-merge 2726 (#14405)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`97f2dda6dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/97f2dda6dd) [#14402](https://github.com/NVIDIA/TensorRT-LLM/pull/14402)
  [None][test] Update bug ID for test_all_optimizations_combined waiver (#14402)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`285e1047db`](https://github.com/NVIDIA/TensorRT-LLM/commit/285e1047db) [#14284](https://github.com/NVIDIA/TensorRT-LLM/pull/14284)
  [https://nvbugs/6153638][fix] unwaive tests for testing the flaky issue (#14284)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`31d68b2dd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/31d68b2dd0) [#14383](https://github.com/NVIDIA/TensorRT-LLM/pull/14383)
  [https://nvbugs/6027594][fix] Unwaive testcase (#14383)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`c7d609bd0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7d609bd0e) [#14367](https://github.com/NVIDIA/TensorRT-LLM/pull/14367)
  [None][infra] Handle sacct error when checking slurm job status (#14367)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-21** [`6a4a2a8911`](https://github.com/NVIDIA/TensorRT-LLM/commit/6a4a2a8911) [#14337](https://github.com/NVIDIA/TensorRT-LLM/pull/14337)
  [nvbug6185190][doc] fix invalid links in doc (#14337)
  _Files: `docs/source/features/guided-decoding.md`, `tests/integration/defs/test_doc.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`462793077d`](https://github.com/NVIDIA/TensorRT-LLM/commit/462793077d) [#14037](https://github.com/NVIDIA/TensorRT-LLM/pull/14037)
  [None][test] Split verl tests into 19 fine-grained per-case wrappers (#14037)
  _Files: `tests/integration/defs/verl/test_verl_cases.py`, `tests/integration/defs/verl/verl_config.yml`, `tests/integration/test_lists/test-db/l0_verl.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`b8f78a12a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8f78a12a5) [#14350](https://github.com/NVIDIA/TensorRT-LLM/pull/14350)
  [None][infra] Waive 1 failed cases for main in pre-merge 38987 (#14350)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`67fad12f98`](https://github.com/NVIDIA/TensorRT-LLM/commit/67fad12f98) [#14357](https://github.com/NVIDIA/TensorRT-LLM/pull/14357)
  [None][infra] Waive 2 failed cases for main in post-merge 2725 (#14357)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`c71655e7a7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c71655e7a7) [#14349](https://github.com/NVIDIA/TensorRT-LLM/pull/14349)
  [None][infra] Revert Mingyang back to mingyangHao in allowlist (#14349)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-05-20** [`9e3dbaa1b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/9e3dbaa1b5) [#14346](https://github.com/NVIDIA/TensorRT-LLM/pull/14346)
  [None][infra] Waive 1 failed cases for main in pre-merge 38925 (#14346)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`c72d43d896`](https://github.com/NVIDIA/TensorRT-LLM/commit/c72d43d896) [#14332](https://github.com/NVIDIA/TensorRT-LLM/pull/14332)
  [None][test] Waive 1 failed cases for main in QA CI (#14332)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`fb06a2f161`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb06a2f161) [#14158](https://github.com/NVIDIA/TensorRT-LLM/pull/14158)
  [https://nvbugs/6162624][test] Unwaive passing test (#14158)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`6de1482874`](https://github.com/NVIDIA/TensorRT-LLM/commit/6de1482874) [#14309](https://github.com/NVIDIA/TensorRT-LLM/pull/14309)
  [None][test] Waive 8 failed cases for main in QA CI (#14309)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`9f9036108a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9f9036108a) [#14304](https://github.com/NVIDIA/TensorRT-LLM/pull/14304)
  [None][infra] Update blossom-ci allowlist: fix jdebache (#14304)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-05-19** [`c681fdf383`](https://github.com/NVIDIA/TensorRT-LLM/commit/c681fdf383) [#14324](https://github.com/NVIDIA/TensorRT-LLM/pull/14324)
  [None][infra] Waive 3 failed cases for main in pre-merge 38724 (#14324)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`f35948636f`](https://github.com/NVIDIA/TensorRT-LLM/commit/f35948636f) [#14319](https://github.com/NVIDIA/TensorRT-LLM/pull/14319)
  [https://nvbugs/6189918][chore] Waive test_auto_dtype_with_helix[fifo-cudagraph:with_padding-pp1tp1cp4] (#14319)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`b2a5070e2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b2a5070e2c) [#14316](https://github.com/NVIDIA/TensorRT-LLM/pull/14316)
  [None][infra] Waive 1 failed cases for main in pre-merge 38844 (#14316)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`a7f72297f5`](https://github.com/NVIDIA/TensorRT-LLM/commit/a7f72297f5) [#14313](https://github.com/NVIDIA/TensorRT-LLM/pull/14313)
  [https://nvbugs/6168859][chore] Waive test_openai_chat_guided_decoding on all GPUs (#14313)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`eb477a13aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb477a13aa) [#14269](https://github.com/NVIDIA/TensorRT-LLM/pull/14269)
  [None][fix] Prevent SLURM dispatcher retry duplicate-upload error (#14269)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-19** [`22bafe4ba1`](https://github.com/NVIDIA/TensorRT-LLM/commit/22bafe4ba1) [#14283](https://github.com/NVIDIA/TensorRT-LLM/pull/14283)
  [None][infra] Waive 5 failed cases for main in post-merge (#14283)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`13413e9900`](https://github.com/NVIDIA/TensorRT-LLM/commit/13413e9900) [#14259](https://github.com/NVIDIA/TensorRT-LLM/pull/14259)
  [None][infra] Waive 1 failed cases for main in post-merge (#14259)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`fa8aaff31b`](https://github.com/NVIDIA/TensorRT-LLM/commit/fa8aaff31b) [#14260](https://github.com/NVIDIA/TensorRT-LLM/pull/14260)
  [None][test] Waive 2 failed cases for main in QA CI (#14260)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`e2b8d97056`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2b8d97056) [#14295](https://github.com/NVIDIA/TensorRT-LLM/pull/14295)
  [None][infra] Update blossom-ci allowlist: fix Mingyang, add brnguyen2 and yongzhiz (#14295)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-05-19** [`869bb24b80`](https://github.com/NVIDIA/TensorRT-LLM/commit/869bb24b80) [#14294](https://github.com/NVIDIA/TensorRT-LLM/pull/14294)
  [None][infra] Waive 2 failed cases for main in post-merge 2723 (#14294)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-19** [`e483bf8ac5`](https://github.com/NVIDIA/TensorRT-LLM/commit/e483bf8ac5) [#14233](https://github.com/NVIDIA/TensorRT-LLM/pull/14233)
  [None][test] Waive 4 failed cases for main in QA test list (#14233)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-18** [`a6fc155178`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6fc155178) [#14221](https://github.com/NVIDIA/TensorRT-LLM/pull/14221)
  [None][test] Waive 1 failed cases for main in QA CI (#14221)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-18** [`aba19ef906`](https://github.com/NVIDIA/TensorRT-LLM/commit/aba19ef906) [#14235](https://github.com/NVIDIA/TensorRT-LLM/pull/14235)
  [None][infra] Waive 13 failed cases for main in post-merge 2722 (#14235)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-18** [`13bbeb9741`](https://github.com/NVIDIA/TensorRT-LLM/commit/13bbeb9741) [#14169](https://github.com/NVIDIA/TensorRT-LLM/pull/14169)
  [https://nvbugs/6163030][fix] Unwaive testcase (#14169)
  _Files: `tests/integration/test_lists/waives.txt`_

## MoE  (25 commits)

- **2026-05-25** [`92c5030ff4`](https://github.com/NVIDIA/TensorRT-LLM/commit/92c5030ff4) [#13478](https://github.com/NVIDIA/TensorRT-LLM/pull/13478)
  [TRTLLM-13429][feat] Switch DeepSeek/NemotronH/Qwen3/Qwen3.5-MoE to sharding-IR canonical models (#13478)
  _Files: `.claude/skills/ad-model-onboard/SKILL.md`, `.claude/skills/ad-sharding-ir-port/SKILL.md`, `examples/auto_deploy/.gitignore`, `examples/auto_deploy/model_registry/configs/enable_sharder_ir.yaml` _+11 more__
- **2026-05-25** [`8c8765d69c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c8765d69c) [#14507](https://github.com/NVIDIA/TensorRT-LLM/pull/14507)
  [TRTLLM-12635][feat] add bench_moe microbenchmark (#14507)
  _Files: `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/__init__.py`, `tests/microbenchmarks/bench_moe/__main__.py`, `tests/microbenchmarks/bench_moe/backend.py` _+21 more__
- **2026-05-23** [`751be5d9b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/751be5d9b5) [#14164](https://github.com/NVIDIA/TensorRT-LLM/pull/14164)
  [None][feat] Revert Add support for Qwen3.5 VL MoE (#14164) (#14465)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+10 more__
- **2026-05-22** [`c044e96280`](https://github.com/NVIDIA/TensorRT-LLM/commit/c044e96280) [#14273](https://github.com/NVIDIA/TensorRT-LLM/pull/14273)
  [https://nvbugs/6184143][fix] AutoDeploy: Fix newly added unit tests for Transformers 5.5.3 (#14273)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/singlegpu/models/test_decilm_modeling.py`, `tests/unittest/auto_deploy/singlegpu/models/test_granite_moe_hybrid_modeling.py`_
- **2026-05-22** [`e26fa16392`](https://github.com/NVIDIA/TensorRT-LLM/commit/e26fa16392) [#14354](https://github.com/NVIDIA/TensorRT-LLM/pull/14354)
  [None][chore] Use CUDA 13 CUTLASS DSL package (#14354)
  _Files: `requirements.txt`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_gather_grouped_gemm_act_fusion.py` _+17 more__
- **2026-05-22** [`8791347a06`](https://github.com/NVIDIA/TensorRT-LLM/commit/8791347a06) [#14401](https://github.com/NVIDIA/TensorRT-LLM/pull/14401)
  [https://nvbugs/6185212][fix] Fix B300 MoE test list ids (#14401)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b300.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-22** [`ef408260b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef408260b2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+51 more__
- **2026-05-21** [`1b1053113b`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b1053113b) [#14362](https://github.com/NVIDIA/TensorRT-LLM/pull/14362)
  [https://nvbugs/6175060][fix] Fix B300 MegaMoE test selection (#14362)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/mega_moe/mega_moe_deepgemm.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`f15af81e88`](https://github.com/NVIDIA/TensorRT-LLM/commit/f15af81e88) [#11962](https://github.com/NVIDIA/TensorRT-LLM/pull/11962)
  [None][fix] Reduce host memory usage during EPLB config model loading. (#11962)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/quantization.py`_
- **2026-05-21** [`1921ef1742`](https://github.com/NVIDIA/TensorRT-LLM/commit/1921ef1742) [#13559](https://github.com/NVIDIA/TensorRT-LLM/pull/13559)
  [None][feat] Add Laguna model support (Poolside Laguna-XS.2) (#13559)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/laguna.py`, `tensorrt_llm/_torch/model_config.py` _+19 more__
- **2026-05-21** [`96a4a0937e`](https://github.com/NVIDIA/TensorRT-LLM/commit/96a4a0937e) [#14164](https://github.com/NVIDIA/TensorRT-LLM/pull/14164)
  [TRTLLM-12500][feat] Add support for Qwen3.5 VL MoE (#14164)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+10 more__
- **2026-05-21** [`7279d6322d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7279d6322d) [#12873](https://github.com/NVIDIA/TensorRT-LLM/pull/12873)
  [None][feat] EXAONE-4.5 Support (#12873)
  _Files: `docs/source/models/supported-models.md`, `examples/models/core/exaone/README.md`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/__init__.py` _+14 more__
- **2026-05-21** [`47255f405f`](https://github.com/NVIDIA/TensorRT-LLM/commit/47255f405f) [#14331](https://github.com/NVIDIA/TensorRT-LLM/pull/14331)
  [None][chore] Remove unnecessary buffer to save memory during refit (#14331)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/quantization.py`_
- **2026-05-21** [`57060a7706`](https://github.com/NVIDIA/TensorRT-LLM/commit/57060a7706)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+50 more__
- **2026-05-20** [`bb57a837dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb57a837dd) [#14306](https://github.com/NVIDIA/TensorRT-LLM/pull/14306)
  [None][perf] Fuse sigmoid+mul+add shared-expert combine into one Trit… (#14306)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/modules/fused_shared_expert.py`, `tests/unittest/_torch/modules/test_fused_shared_expert.py`_
- **2026-05-20** [`f7fb5f4bfb`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7fb5f4bfb) [#14344](https://github.com/NVIDIA/TensorRT-LLM/pull/14344)
  [None][chore] Update Claude Code agents and skills (#14344)
  _Files: `.claude/agents/ad-onboard-reviewer.md`, `.claude/agents/perf-test-sync.md`, `.claude/skills/ad-accuracy-debug/SKILL.md`, `.claude/skills/ad-add-fusion-transformation/SKILL.md` _+33 more__
- **2026-05-20** [`d724c6862d`](https://github.com/NVIDIA/TensorRT-LLM/commit/d724c6862d) [#13349](https://github.com/NVIDIA/TensorRT-LLM/pull/13349)
  [https://nvbugs/6094108][fix] Fix Qwen3-30B-A3B NVFP4 tep4 CUTLASS MoE test OOM on B300 (#13349)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-05-20** [`fd54508854`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd54508854) [#14282](https://github.com/NVIDIA/TensorRT-LLM/pull/14282)
  [https://nvbugs/6095421][fix] Update resolve_moe_backend (#14282)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`77db08daf8`](https://github.com/NVIDIA/TensorRT-LLM/commit/77db08daf8) [#11561](https://github.com/NVIDIA/TensorRT-LLM/pull/11561)
  [None][fix] Fix int4 awq for sm120/121 (#11561)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/quantization/functional.py` _+4 more__
- **2026-05-19** [`c087a58108`](https://github.com/NVIDIA/TensorRT-LLM/commit/c087a58108) [#14281](https://github.com/NVIDIA/TensorRT-LLM/pull/14281)
  [None][fix] Update the OSS headers in derived FLA ops and AD modeling code (#14281)
  _Files: `examples/auto_deploy/llmc/_license_data.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/chunk.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/fused_recurrent.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/utils.py` _+48 more__
- **2026-05-19** [`de3afb3c0f`](https://github.com/NVIDIA/TensorRT-LLM/commit/de3afb3c0f) [#13401](https://github.com/NVIDIA/TensorRT-LLM/pull/13401)
  [TRTLLM-11127][feat] add W4A8_MXFP4_FP8 MoE unit test support (#13401)
  _Files: `tests/unittest/_torch/modules/moe/moe_test_utils.py`, `tests/unittest/_torch/modules/moe/quantize_utils.py`, `tests/unittest/_torch/modules/moe/test_moe_backend.py`, `tests/unittest/_torch/modules/moe/test_moe_module.py`_
- **2026-05-18** [`f830224e49`](https://github.com/NVIDIA/TensorRT-LLM/commit/f830224e49) [#14193](https://github.com/NVIDIA/TensorRT-LLM/pull/14193)
  [None][fix] Add SPDX Apache-2.0 headers to auto_deploy test files (#14193)
  _Files: `tensorrt_llm/_torch/auto_deploy/config/default.yaml`, `tensorrt_llm/_torch/auto_deploy/config/transformers.yaml`, `tests/unittest/auto_deploy/_utils_test/_custom_op_utils.py`, `tests/unittest/auto_deploy/_utils_test/_dist_test_utils.py` _+93 more__
- **2026-05-18** [`5e2597705c`](https://github.com/NVIDIA/TensorRT-LLM/commit/5e2597705c) [#13833](https://github.com/NVIDIA/TensorRT-LLM/pull/13833)
  [None][perf] FC2 DenseGEMM autotune: split-K, swap_ab, fine-grained tuning buckets (#13833)
  _Files: `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/moe_as_dense_gemm/fc2.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/utils.py`, `tests/scripts/cute_dsl_kernels/moe_as_dense_gemm/run_moe_as_dense_gemm_fc2.py`_
- **2026-05-18** [`a1acbce524`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1acbce524) [#13689](https://github.com/NVIDIA/TensorRT-LLM/pull/13689)
  [None][feat] Add bf16 trtllm moe through flashinfer. (#13689)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tensorrt_llm/_torch/modules/fused_moe/moe_op_backend.py` _+11 more__
- **2026-05-18** [`0886d6a03c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0886d6a03c) [#14179](https://github.com/NVIDIA/TensorRT-LLM/pull/14179)
  [https://nvbugs/6163147][fix] swap layer.mlp in place for Mixtral modelopt export (#14179)
  _Files: `tensorrt_llm/quantization/quantize_by_modelopt.py`_

## Executor / Runtime  (21 commits)

- **2026-05-24** [`9ba6744e8c`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ba6744e8c) [#14412](https://github.com/NVIDIA/TensorRT-LLM/pull/14412)
  [None][feat] support SWA scratch reuse rewind (#14412)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_config.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py` _+4 more__
- **2026-05-23** [`d741a661cf`](https://github.com/NVIDIA/TensorRT-LLM/commit/d741a661cf) [#14471](https://github.com/NVIDIA/TensorRT-LLM/pull/14471)
  [None][feat] Disable mamba replay by default (#14471)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tensorrt_llm/_torch/modules/mamba/selective_state_update.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`_
- **2026-05-22** [`e796f16c81`](https://github.com/NVIDIA/TensorRT-LLM/commit/e796f16c81) [#14307](https://github.com/NVIDIA/TensorRT-LLM/pull/14307)
  [None][fix] cold-start warmup for KV-aware ADP router (#14307)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/_torch/executor/test_kvcache_aware_router.py`_
- **2026-05-22** [`5de99b66c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/5de99b66c4) [#14410](https://github.com/NVIDIA/TensorRT-LLM/pull/14410)
  [https://nvbugs/6185234][fix] route load_hf_model_config via AutoConfig (#14410)
  _Files: `tensorrt_llm/llmapi/llm_utils.py`, `tests/unittest/_torch/test_custom_config_registration.py`_
- **2026-05-22** [`79ede08f31`](https://github.com/NVIDIA/TensorRT-LLM/commit/79ede08f31) [#14003](https://github.com/NVIDIA/TensorRT-LLM/pull/14003)
  [None][fix] Fix CppMambaHybridCacheManager functional and perf issues (#14003)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheTransferManager.cpp` _+6 more__
- **2026-05-22** [`44fb9a7b38`](https://github.com/NVIDIA/TensorRT-LLM/commit/44fb9a7b38) [#13577](https://github.com/NVIDIA/TensorRT-LLM/pull/13577)
  [None][fix] Reject incompatible KV connector configurations at construction time (#13577)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/defs/llmapi/test_llm_api_connector.py`, `tests/integration/test_lists/test-db/l0_a10.yml`_
- **2026-05-21** [`57a1b84a22`](https://github.com/NVIDIA/TensorRT-LLM/commit/57a1b84a22) [#14170](https://github.com/NVIDIA/TensorRT-LLM/pull/14170)
  [None][feature] Add env variables to help debugging mamba modules. (#14170)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tensorrt_llm/_torch/pyexecutor/py_executor_creator.py`_
- **2026-05-21** [`e64c92ba29`](https://github.com/NVIDIA/TensorRT-LLM/commit/e64c92ba29) [#14267](https://github.com/NVIDIA/TensorRT-LLM/pull/14267)
  [None][fix] ADP router crashes on serve when scheduling_params.attent… (#14267)
  _Files: `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tests/unittest/_torch/executor/test_adp_router.py`_
- **2026-05-20** [`ef160ad0f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef160ad0f2) [#13347](https://github.com/NVIDIA/TensorRT-LLM/pull/13347)
  [https://nvbugs/6093911][fix] Fix disagg gen-only benchmark hang under ADP router imbalance (#13347)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tests/integration/defs/perf/disagg/test_configs/wideep/perf/kimi-k2-thinking-fp4_8k1k_ctx8_gen1_dep32_bs256_eplb416_mtp0_ccb-NIXL.yaml`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-05-20** [`8ba76f48a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ba76f48a6) [#14052](https://github.com/NVIDIA/TensorRT-LLM/pull/14052)
  [None][feat] add single-rank MPI sleep/wakeup and rank-0 collective_rpc shim (#14052)
  _Files: `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/proxy.py`, `tensorrt_llm/executor/rpc_proxy.py`, `tests/unittest/executor/test_sleep_collective_rpc_guards.py`_
- **2026-05-20** [`f278c4f170`](https://github.com/NVIDIA/TensorRT-LLM/commit/f278c4f170) [#12637](https://github.com/NVIDIA/TensorRT-LLM/pull/12637)
  [None][feat] opentelemetry metrics for num_postproc_workers > 0 disagg (#12637)
  _Files: `ruff-legacy-baseline.json`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/postproc_worker.py`, `tensorrt_llm/executor/result.py` _+2 more__
- **2026-05-20** [`7acaf1ef02`](https://github.com/NVIDIA/TensorRT-LLM/commit/7acaf1ef02) [#13815](https://github.com/NVIDIA/TensorRT-LLM/pull/13815)
  [None][feat] Exact multimodal KV blockhashing (#13815)
  _Files: `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/blockKey.cpp`, `cpp/tensorrt_llm/executor/multimodalInput.cpp` _+19 more__
- **2026-05-20** [`4a58dc3581`](https://github.com/NVIDIA/TensorRT-LLM/commit/4a58dc3581) [#13843](https://github.com/NVIDIA/TensorRT-LLM/pull/13843)
  [TRTLLM-12520][perf] Reduce host overhead during scheduling and sampling (#13843)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py` _+1 more__
- **2026-05-20** [`cf87a8beaa`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf87a8beaa) [#14061](https://github.com/NVIDIA/TensorRT-LLM/pull/14061)
  [https://nvbugs/5615248][perf] Early emission of first token with overlap scheduling (#14061)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/llmapi/llm_args.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py` _+4 more__
- **2026-05-19** [`1c2c5c3fff`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c2c5c3fff) [#14218](https://github.com/NVIDIA/TensorRT-LLM/pull/14218)
  [#13561][fix] AutoDeploy: forward garbage_collection_gen0_threshold to PyExecutor (#14218)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tests/unittest/auto_deploy/singlegpu/shim/test_create_ad_executor.py`_
- **2026-05-18** [`1f1e9aab9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f1e9aab9e) [#12993](https://github.com/NVIDIA/TensorRT-LLM/pull/12993)
  [#13076][fix] Destroy torch distributed process groups on PyExecutor shutdown (#12993)
  _Files: `tensorrt_llm/executor/worker.py`_
- **2026-05-18** [`d42ec3df56`](https://github.com/NVIDIA/TensorRT-LLM/commit/d42ec3df56) [#14252](https://github.com/NVIDIA/TensorRT-LLM/pull/14252)
  [https://nvbugs/6185713][fix] Revert PR13758's code changes on Limiting maximum warmup token count (#14252)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`_
- **2026-05-18** [`70951837cd`](https://github.com/NVIDIA/TensorRT-LLM/commit/70951837cd) [#13968](https://github.com/NVIDIA/TensorRT-LLM/pull/13968)
  [None][fix] Fix bugs related with nemotron-nas model (#13968)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheTransferManager.cpp`, `tensorrt_llm/_torch/models/checkpoints/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_nas_weight_mapper.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-05-18** [`61a64e6c98`](https://github.com/NVIDIA/TensorRT-LLM/commit/61a64e6c98) [#14140](https://github.com/NVIDIA/TensorRT-LLM/pull/14140)
  [None][chore] Refactor salting support for KVCacheManagerV2 (#14140)
  _Files: `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py` _+6 more__
- **2026-05-18** [`d0638a0ac2`](https://github.com/NVIDIA/TensorRT-LLM/commit/d0638a0ac2) [#14172](https://github.com/NVIDIA/TensorRT-LLM/pull/14172)
  [https://nvbugs/6025177][test] rcca tests using kimi k2.5 fp4 (#14172)
  _Files: `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/unittest/llmapi/apps/_test_openai_kv_cache_contamination.py`_
- **2026-05-18** [`f1c5013b39`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1c5013b39) [#11741](https://github.com/NVIDIA/TensorRT-LLM/pull/11741)
  [TRTLLM-10851][feat] Further doc and utility features for host profiler. (#11741)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/tools/profiler/host_profile_tools/README.md`, `tensorrt_llm/tools/profiler/host_profile_tools/__init__.py`, `tensorrt_llm/tools/profiler/host_profile_tools/host_profiler.py` _+1 more__

## Attention  (20 commits)

- **2026-05-25** [`fd8ae36bbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd8ae36bbe) [#12947](https://github.com/NVIDIA/TensorRT-LLM/pull/12947)
  [None][feat] Add SkipSoftmax sparse attention support for visual generation (#12947)
  _Files: `docs/source/features/sparse-attention.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py` _+6 more__
- **2026-05-25** [`e45a8e3156`](https://github.com/NVIDIA/TensorRT-LLM/commit/e45a8e3156) [#13428](https://github.com/NVIDIA/TensorRT-LLM/pull/13428)
  [None][feat] Add FlashInfer MLA attention backend support (#13428)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/modules/attention.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+3 more__
- **2026-05-25** [`f49ac5689d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f49ac5689d) [#14275](https://github.com/NVIDIA/TensorRT-LLM/pull/14275)
  [None][chore] Drop sink_token_length from PyTorch attention surface (#14275)
  _Files: `cpp/tensorrt_llm/kernels/gptKernels.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h` _+17 more__
- **2026-05-24** [`763408bdd4`](https://github.com/NVIDIA/TensorRT-LLM/commit/763408bdd4) [#13426](https://github.com/NVIDIA/TensorRT-LLM/pull/13426)
  [None][perf] EAGLE3 dynamic tree kernel optimizations (#13426)
  _Files: `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.cu`, `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.h`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/prepareCustomMask.cu`, `cpp/tensorrt_llm/thop/dynamicTreeOp.cpp` _+15 more__
- **2026-05-24** [`77f87f9276`](https://github.com/NVIDIA/TensorRT-LLM/commit/77f87f9276) [#13985](https://github.com/NVIDIA/TensorRT-LLM/pull/13985)
  [TRTLLM-12580][perf] ltx2: fused RMSNorm+RoPE across all attention paths + PE pre-shard (#13985)
  _Files: `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.h`, `cpp/tensorrt_llm/kernels/fusedDiTSplitNormKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTSplitNormKernel.h` _+17 more__
- **2026-05-23** [`4addc5ecbc`](https://github.com/NVIDIA/TensorRT-LLM/commit/4addc5ecbc) [#14462](https://github.com/NVIDIA/TensorRT-LLM/pull/14462)
  [None][feat] Update cubins to resolve FMHA PDL issue (#14462)
- **2026-05-22** [`f02cc223db`](https://github.com/NVIDIA/TensorRT-LLM/commit/f02cc223db) [#14175](https://github.com/NVIDIA/TensorRT-LLM/pull/14175)
  [TRTLLM-11320][refactor] Refactor VisualGenArgs API and registry (#14175)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/configs/wan2.2-t2v-fp4-1gpu.yaml`, `examples/visual_gen/configs/wan2.2-t2v-fp4-4gpu.yaml`, `examples/visual_gen/configs/wan2.2-t2v-fp8-8gpu.yaml` _+76 more__
- **2026-05-22** [`e091460b29`](https://github.com/NVIDIA/TensorRT-LLM/commit/e091460b29) [#12525](https://github.com/NVIDIA/TensorRT-LLM/pull/12525)
  [None][feat] Disable shared paged index in flashinfer trtllm-gen fmha kernel and unify kv cache buffer calculation with thop.attention (#12525)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionWorkspace.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp` _+9 more__
- **2026-05-22** [`043ae94661`](https://github.com/NVIDIA/TensorRT-LLM/commit/043ae94661) [#14411](https://github.com/NVIDIA/TensorRT-LLM/pull/14411)
  [https://nvbugs/6185182][fix] Adjust H20 accuracy for Qwen3.5-4B DFlash (#14411)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-05-22** [`25e5a99a9b`](https://github.com/NVIDIA/TensorRT-LLM/commit/25e5a99a9b) [#14133](https://github.com/NVIDIA/TensorRT-LLM/pull/14133)
  [TRTLLM-35237][feat] Tune cute dsl paged MQA logits decode kernel (#14133)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp8_paged_mqa_logits.py` _+4 more__
- **2026-05-21** [`30845bda9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/30845bda9e) [#13711](https://github.com/NVIDIA/TensorRT-LLM/pull/13711)
  [#12359][feat] AutoDeploy: MTP performance: Integrate FI kernel for extend path (#13711)
  _Files: `examples/auto_deploy/model_registry/configs/super_v3_mtp.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/flashinfer_backend_mamba.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_autodeploy.py` _+4 more__
- **2026-05-21** [`66988254ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/66988254ed) [#14148](https://github.com/NVIDIA/TensorRT-LLM/pull/14148)
  [https://nvbugs/6110638][fix] Mark AutoDeploy attention DP world sizes by GPU count (#14148)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`_
- **2026-05-21** [`3b8387c44b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b8387c44b) [#13821](https://github.com/NVIDIA/TensorRT-LLM/pull/13821)
  [TRTLLM-12342][feat] Ring Attention, Unified Context Parallel for VisualGen (#13821)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/visual_gen_wan_i2v.py`, `examples/visual_gen/visual_gen_wan_t2v.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/__init__.py` _+16 more__
- **2026-05-20** [`a173761069`](https://github.com/NVIDIA/TensorRT-LLM/commit/a173761069) [#14291](https://github.com/NVIDIA/TensorRT-LLM/pull/14291)
  [None][feat] Update the logic of FMHA JIT path (#14291)
- **2026-05-20** [`3cf9a5b068`](https://github.com/NVIDIA/TensorRT-LLM/commit/3cf9a5b068) [#14244](https://github.com/NVIDIA/TensorRT-LLM/pull/14244)
  [None][refactor] clean up AttentionForwardArgs (#14244)
  _Files: `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/models/modeling_qwen.py` _+2 more__
- **2026-05-20** [`3de344d384`](https://github.com/NVIDIA/TensorRT-LLM/commit/3de344d384) [#14276](https://github.com/NVIDIA/TensorRT-LLM/pull/14276)
  [None][fix] Handle unset attention_dp_relax in ADP routers (#14276)
  _Files: `tensorrt_llm/scheduling_params.py`, `tests/unittest/_torch/executor/test_adp_router.py`_
- **2026-05-19** [`b892451afc`](https://github.com/NVIDIA/TensorRT-LLM/commit/b892451afc) [#13630](https://github.com/NVIDIA/TensorRT-LLM/pull/13630)
  [#13580][fix] AutoDeploy: Support Gemma3n/4 E2B variants (#13630)
  _Files: `examples/auto_deploy/model_registry/configs/gemma3n_e2b_it.yaml`, `examples/auto_deploy/model_registry/configs/gemma4_e2b.yaml`, `examples/auto_deploy/model_registry/models.yaml`, `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py` _+22 more__
- **2026-05-19** [`501a58034e`](https://github.com/NVIDIA/TensorRT-LLM/commit/501a58034e) [#14008](https://github.com/NVIDIA/TensorRT-LLM/pull/14008)
  [https://nvbugs/6117814][fix] AutoDeploy: Fix Eagle cu_seqlen data race (#14008)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/singlegpu/custom_ops/test_switch_to_generate_inplace.py`_
- **2026-05-19** [`025086fc1a`](https://github.com/NVIDIA/TensorRT-LLM/commit/025086fc1a) [#14134](https://github.com/NVIDIA/TensorRT-LLM/pull/14134)
  [None][feat] Add chunked prefill support for Gemma4 (text + vision multimodal) (#14134)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/triton_prefill.py`, `tensorrt_llm/_torch/models/modeling_gemma4.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py` _+3 more__
- **2026-05-18** [`ca0aad2c1e`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca0aad2c1e) [#14234](https://github.com/NVIDIA/TensorRT-LLM/pull/14234)
  [None][chore] Rename .claude skills with trtllm- prefix and drop ci-failure-retrieval (#14234)
  _Files: `.claude/README.md`, `.claude/skills/ci-failure-retrieval/SKILL.md`, `.claude/skills/trtllm-flashinfer-upgrade/SKILL.md`, `.claude/skills/trtllm-serve-config-guide/SKILL.md` _+2 more__

## Models  (16 commits)

- **2026-05-25** [`546a5b0912`](https://github.com/NVIDIA/TensorRT-LLM/commit/546a5b0912) [#14392](https://github.com/NVIDIA/TensorRT-LLM/pull/14392)
  [https://nvbugs/6182617][fix] Restore K2.5 multimodal dep8 accuracy test on transformers 5.5.x (#14392)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`01c9a34d53`](https://github.com/NVIDIA/TensorRT-LLM/commit/01c9a34d53) [#14522](https://github.com/NVIDIA/TensorRT-LLM/pull/14522)
  [https://nvbugs/6215684][fix] Fix invalid links in deployment guide (#14522)
  _Files: `docs/source/deployment-guide/deployment-guide-for-deepseek-r1-on-trtllm.md`, `docs/source/deployment-guide/deployment-guide-for-glm-5-on-trtllm.md`, `docs/source/deployment-guide/deployment-guide-for-gpt-oss-on-trtllm.md`, `docs/source/deployment-guide/deployment-guide-for-llama3.3-70b-on-trtllm.md` _+3 more__
- **2026-05-25** [`5cb6d2d4ad`](https://github.com/NVIDIA/TensorRT-LLM/commit/5cb6d2d4ad) [#14511](https://github.com/NVIDIA/TensorRT-LLM/pull/14511)
  [None][fix] Unwaive Qwen3.5 bf16 mtp on case (#14511)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`10dd9d4dd0`](https://github.com/NVIDIA/TensorRT-LLM/commit/10dd9d4dd0)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json` _+2 more__
- **2026-05-24** [`dcf1cd83c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/dcf1cd83c2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/qwen/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-05-22** [`8cc40d302a`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cc40d302a) [#14463](https://github.com/NVIDIA/TensorRT-LLM/pull/14463)
  [None][doc] Update Gemma 4 entries in supported-models.md (#14463)
  _Files: `docs/source/models/supported-models.md`_
- **2026-05-22** [`6dfaf281d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6dfaf281d7) [#13832](https://github.com/NVIDIA/TensorRT-LLM/pull/13832)
  [https://nvbugs/6141606][fix] Move the `layer_types` derivation into `Qwen3HybridConfig.from_hf` (where `pretr (#13832)
  _Files: `tensorrt_llm/bench/build/dataclasses.py`_
- **2026-05-22** [`eb6ee930be`](https://github.com/NVIDIA/TensorRT-LLM/commit/eb6ee930be) [#14379](https://github.com/NVIDIA/TensorRT-LLM/pull/14379)
  [None][chore] Fix Kimi_k25 with spec dec (#14379)
  _Files: `tensorrt_llm/_torch/models/modeling_kimi_k25.py`_
- **2026-05-21** [`4c5500ea44`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c5500ea44) [#14300](https://github.com/NVIDIA/TensorRT-LLM/pull/14300)
  [None][feat] Gemma4 MM: native vision + audio towers (#14300)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma4_audio.py`, `tensorrt_llm/_torch/models/modeling_gemma4_vision.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tests/integration/test_lists/test-db/l0_b200.yml` _+2 more__
- **2026-05-21** [`09f6885bcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/09f6885bcd) [#14055](https://github.com/NVIDIA/TensorRT-LLM/pull/14055)
  [https://nvbugs/6141803][fix] Skip Qwen3.5-4B tests pre-hopper (#14055)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`3024ec6941`](https://github.com/NVIDIA/TensorRT-LLM/commit/3024ec6941) [#14232](https://github.com/NVIDIA/TensorRT-LLM/pull/14232)
  [https://nvbugs/6143599][fix] DeepSeek-V3 OOM and artifacts path (#14232)
  _Files: `tests/integration/defs/stress_test/stress_test.py`_
- **2026-05-20** [`23dc213486`](https://github.com/NVIDIA/TensorRT-LLM/commit/23dc213486) [#14271](https://github.com/NVIDIA/TensorRT-LLM/pull/14271)
  [None][cleanup] MistralSmall related cleanups (#14271)
  _Files: `tensorrt_llm/_torch/models/modeling_mistral.py`, `tensorrt_llm/_torch/models/modeling_multimodal_mixin.py`, `tests/unittest/_torch/modeling/test_modeling_mistral.py`_
- **2026-05-20** [`aac0d658ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/aac0d658ea) [#14303](https://github.com/NVIDIA/TensorRT-LLM/pull/14303)
  [None][doc] Gemma 4: usage examples (#14303)
  _Files: `examples/models/core/gemma/README.md`_
- **2026-05-19** [`95ad97ea69`](https://github.com/NVIDIA/TensorRT-LLM/commit/95ad97ea69) [#14293](https://github.com/NVIDIA/TensorRT-LLM/pull/14293)
  [https://nvbugs/6185234][fix] register deepseek_v32 / kimi_k2 with transformers AutoConfig (#14293)
  _Files: `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/models/__init__.py`, `tests/unittest/_torch/test_custom_config_registration.py`_
- **2026-05-19** [`04357222e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/04357222e3) [#13895](https://github.com/NVIDIA/TensorRT-LLM/pull/13895)
  [https://nvbugs/6069543][fix] Lower accuracy threshold for H20 qwen3.5 test (#13895)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-05-19** [`2af9ba9b84`](https://github.com/NVIDIA/TensorRT-LLM/commit/2af9ba9b84) [#14261](https://github.com/NVIDIA/TensorRT-LLM/pull/14261)
  [https://nvbugs/6185234][fix] DeepSeek-V3.2 tokenizer load on transformers 5.x (#14261)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`_

## Other  (14 commits)

- **2026-05-25** [`5f4946e912`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f4946e912) [#14226](https://github.com/NVIDIA/TensorRT-LLM/pull/14226)
  [https://nvbugs/6094070][fix] Skip ray-marked integration tests when --run-ray is not set (#14226)
  _Files: `tests/integration/defs/conftest.py`_
- **2026-05-25** [`72bc8ed5f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/72bc8ed5f0) [#14078](https://github.com/NVIDIA/TensorRT-LLM/pull/14078)
  [https://nvbugs/6157131][fix] lower the GSM8K accuracy grade for Nano V3 (#14078)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`_
- **2026-05-24** [`c02475efa0`](https://github.com/NVIDIA/TensorRT-LLM/commit/c02475efa0) [#13618](https://github.com/NVIDIA/TensorRT-LLM/pull/13618)
  [https://nvbugs/6079901][fix] Avoid divide-by-zero in KVCacheTransfer… (#13618)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheTransferManager.cpp`_
- **2026-05-23** [`ad7c20680b`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad7c20680b) [#13518](https://github.com/NVIDIA/TensorRT-LLM/pull/13518)
  [https://nvbugs/5914391][fix] Add OpenAI chat logit bias validation (#13518)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tensorrt_llm/serve/openai_server.py`_
- **2026-05-23** [`c05a32251c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c05a32251c) [#14456](https://github.com/NVIDIA/TensorRT-LLM/pull/14456)
  [None][chore] bump transformers to 5.5.4 (#14456)
  _Files: `requirements.txt`, `triton_backend/requirements.txt`_
- **2026-05-22** [`2bbb945d72`](https://github.com/NVIDIA/TensorRT-LLM/commit/2bbb945d72) [#14380](https://github.com/NVIDIA/TensorRT-LLM/pull/14380)
  [None][test] Remove the testcases for spark (#14380)
  _Files: `tests/integration/test_lists/qa/llm_spark_func.yml`, `tests/integration/test_lists/qa/llm_spark_perf.yml`_
- **2026-05-22** [`501b2dc1f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/501b2dc1f1) [#14289](https://github.com/NVIDIA/TensorRT-LLM/pull/14289)
  [https://nvbugs/6115562][fix] defer worker registration until HTTP server is accepting (#14289)
  _Files: `tensorrt_llm/serve/openai_server.py`_
- **2026-05-21** [`ac0be47748`](https://github.com/NVIDIA/TensorRT-LLM/commit/ac0be47748) [#14347](https://github.com/NVIDIA/TensorRT-LLM/pull/14347)
  [None][test] Disable ignore-eos when Spec Decoding in Perf Test (#14347)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-05-21** [`67b0654541`](https://github.com/NVIDIA/TensorRT-LLM/commit/67b0654541) [#13842](https://github.com/NVIDIA/TensorRT-LLM/pull/13842)
  [None][doc] Add Claude skill for multimodal model onboarding (#13842)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`_
- **2026-05-20** [`b5d64e2e26`](https://github.com/NVIDIA/TensorRT-LLM/commit/b5d64e2e26) [#14340](https://github.com/NVIDIA/TensorRT-LLM/pull/14340)
  [None][chore] Clean test_durations file by removing outdated items. (#14340)
  _Files: `tests/integration/defs/.test_durations`_
- **2026-05-20** [`8923e38b8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/8923e38b8b) [#12364](https://github.com/NVIDIA/TensorRT-LLM/pull/12364)
  [TRTLLM-10362][fix] Fix trtllm-bench for Nemotron models (#12364)
  _Files: `tensorrt_llm/bench/build/dataclasses.py`_
- **2026-05-20** [`9871cbea12`](https://github.com/NVIDIA/TensorRT-LLM/commit/9871cbea12) [#14122](https://github.com/NVIDIA/TensorRT-LLM/pull/14122)
  [None][chore] Remove trailing spaces from module name in logger output (#14122)
  _Files: `cpp/include/tensorrt_llm/common/logger.h`, `cpp/tests/unit_tests/common/loggerTest.cpp`, `tensorrt_llm/logger.py`, `tests/unittest/utils/test_logger.py`_
- **2026-05-19** [`ba685046cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba685046cc) [#14285](https://github.com/NVIDIA/TensorRT-LLM/pull/14285)
  [None][chore] Enforce Claude Code skill and agent naming convention via pre-commit (#14285)
  _Files: `.pre-commit-config.yaml`, `scripts/check_skill_naming_convention.py`_
- **2026-05-18** [`2ad0060dee`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ad0060dee) [#14211](https://github.com/NVIDIA/TensorRT-LLM/pull/14211)
  [None][chore] gitignore NFS system temporary files (#14211)
  _Files: `.gitignore`_

## Disaggregation / KV  (11 commits)

- **2026-05-25** [`140d24bcf1`](https://github.com/NVIDIA/TensorRT-LLM/commit/140d24bcf1) [#14510](https://github.com/NVIDIA/TensorRT-LLM/pull/14510)
  [None][fix] fix typo (#14510)
  _Files: `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`_
- **2026-05-25** [`bdc8b6420a`](https://github.com/NVIDIA/TensorRT-LLM/commit/bdc8b6420a) [#14442](https://github.com/NVIDIA/TensorRT-LLM/pull/14442)
  [None][fix] Fix KV cache grain slot refinement (#14442)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_storage/_core.py`, `tests/unittest/kv_cache_manager_v2_tests/test_kv_cache_manager_v2.py`_
- **2026-05-25** [`90694fec72`](https://github.com/NVIDIA/TensorRT-LLM/commit/90694fec72) [#14460](https://github.com/NVIDIA/TensorRT-LLM/pull/14460)
  [https://nvbugs/6190759][fix] set env on some gb300 cluster (#14460)
  _Files: `tests/integration/defs/disaggregated/test_auto_scaling.py`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/llmapi/apps/_test_disagg_serving_multi_nodes.py`_
- **2026-05-25** [`ab08ffd03c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ab08ffd03c) [#14060](https://github.com/NVIDIA/TensorRT-LLM/pull/14060)
  [TRTLLM-12027][feat] Disagg serving support with block reuse ON for hybrid models (#14060)
  _Files: `cpp/include/tensorrt_llm/batch_manager/cacheTransceiver.h`, `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/batch_manager/rnnCacheFormatter.h`, `cpp/include/tensorrt_llm/executor/dataTransceiverState.h` _+22 more__
- **2026-05-22** [`ad38289d0c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad38289d0c) [#14177](https://github.com/NVIDIA/TensorRT-LLM/pull/14177)
  [https://nvbugs/6156492][fix] Fix disaggregated usage propagation (#14177)
  _Files: `tensorrt_llm/_torch/disaggregation/native/auxiliary.py`, `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tensorrt_llm/disaggregated_params.py`, `tensorrt_llm/executor/postproc_worker.py` _+9 more__
- **2026-05-22** [`d21a9ed875`](https://github.com/NVIDIA/TensorRT-LLM/commit/d21a9ed875) [#12928](https://github.com/NVIDIA/TensorRT-LLM/pull/12928)
  [None][feat] KV cache manager v2 + python transceiver bug fix (#12928)
  _Files: `cpp/include/tensorrt_llm/executor/transferAgent.h`, `cpp/tensorrt_llm/batch_manager/kvCacheManagerV2Utils.h`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/CMakeLists.txt`, `cpp/tensorrt_llm/executor/cache_transmission/nixl_utils/agentBindings.cpp` _+20 more__
- **2026-05-21** [`075933ac66`](https://github.com/NVIDIA/TensorRT-LLM/commit/075933ac66) [#14333](https://github.com/NVIDIA/TensorRT-LLM/pull/14333)
  [None][feat] add KV cache reuse probe (#14333)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi`, `tensorrt_llm/runtime/kv_cache_manager_v2/_block_radix_tree.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/_core/_kv_cache_manager.py` _+2 more__
- **2026-05-21** [`b3fcf083e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/b3fcf083e9) [#14335](https://github.com/NVIDIA/TensorRT-LLM/pull/14335)
  [https://nvbugs/6114141][test] Remove deprecated disagg trtllm_sampler test (#14335)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/disaggregated/test_configs/disagg_config_trtllm_sampler.yaml`, `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+2 more__
- **2026-05-20** [`7e2359738a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7e2359738a) [#14191](https://github.com/NVIDIA/TensorRT-LLM/pull/14191)
  [https://nvbugs/6133201][fix] Bump GEN max_num_tokens in disagg perf YAMLs (#14191)
  _Files: `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_1k1k_con2048_ctx2_dep4_gen1_dep16_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_1k1k_con2048_ctx2_dep4_gen1_dep16_eplb288_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_1k1k_con2048_ctx2_dep4_gen1_dep16_eplb0_mtp3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_qwen3-235b-fp4_1k1k_ctx2_gen1_dep16_bs128_eplb0_mtp3_con2048_ccb-NIXL.yaml` _+1 more__
- **2026-05-18** [`f819383a44`](https://github.com/NVIDIA/TensorRT-LLM/commit/f819383a44) [#13882](https://github.com/NVIDIA/TensorRT-LLM/pull/13882)
  [None][test] Add DSR1 B200 DISAGG to CI Perf Test (#13882)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/disaggregated/submit.py`, `jenkins/scripts/perf/local/submit.py`, `tests/integration/test_lists/test-db/l0_b200_multi_nodes_perf_sanity_node2_gpu16.yml` _+2 more__
- **2026-05-18** [`1109e1cc65`](https://github.com/NVIDIA/TensorRT-LLM/commit/1109e1cc65) [#14168](https://github.com/NVIDIA/TensorRT-LLM/pull/14168)
  [https://nvbugs/6094100][fix] set UCX_TLS  for gb300 to enable disagg test (#14168)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_

## Quantization  (9 commits)

- **2026-05-22** [`fe03942702`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe03942702) [#14359](https://github.com/NVIDIA/TensorRT-LLM/pull/14359)
  [https://nvbugs/6106659][fix] Add Qwen3.6-27B-FP8 support. (#14359)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+1 more__
- **2026-05-22** [`a6a5f28117`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6a5f28117)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+47 more__
- **2026-05-21** [`6bf1701393`](https://github.com/NVIDIA/TensorRT-LLM/commit/6bf1701393) [#14406](https://github.com/NVIDIA/TensorRT-LLM/pull/14406)
  [https://nvbugs/6004530][fix] Unwaive Qwen3.5 35B A3B FP8 test case (#14406)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`c0b73b0e77`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0b73b0e77) [#14088](https://github.com/NVIDIA/TensorRT-LLM/pull/14088)
  [None][feat] Refactor to support legacy and 1.x modelopt quant config format (#14088)
  _Files: `tensorrt_llm/_torch/auto_deploy/models/quant_config_reader.py`, `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/llmapi/llm_utils.py`, `tensorrt_llm/quantization/modelopt_config.py` _+1 more__
- **2026-05-20** [`8b23219726`](https://github.com/NVIDIA/TensorRT-LLM/commit/8b23219726)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+49 more__
- **2026-05-19** [`89e1410d6c`](https://github.com/NVIDIA/TensorRT-LLM/commit/89e1410d6c)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+40 more__
- **2026-05-18** [`355ba940a2`](https://github.com/NVIDIA/TensorRT-LLM/commit/355ba940a2) [#14165](https://github.com/NVIDIA/TensorRT-LLM/pull/14165)
  [TRTLLM-12462][fix] Fix FP8 block scaling GEMM autotuner cache growth (#14165)
  _Files: `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`_
- **2026-05-18** [`c681127da9`](https://github.com/NVIDIA/TensorRT-LLM/commit/c681127da9) [#14144](https://github.com/NVIDIA/TensorRT-LLM/pull/14144)
  [#8542][feat] AutoDeploy: add DeepSeek-R1 FP8 perf test on 8x B200 post merge, remove super perf test from premerge (#14144)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/scripts/perf-sanity/aggregated/deepseek_r1_fp8_ad_blackwell.yaml`_
- **2026-05-18** [`0620bf4c91`](https://github.com/NVIDIA/TensorRT-LLM/commit/0620bf4c91) [#12530](https://github.com/NVIDIA/TensorRT-LLM/pull/12530)
  [https://nvbugs/5879577][fix] Fix KeyError in DeepSeekV3Lite FP8 MTP weight loading (#12530)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tests/integration/test_lists/waives.txt`_

## AutoDeploy  (8 commits)

- **2026-05-25** [`998f41855d`](https://github.com/NVIDIA/TensorRT-LLM/commit/998f41855d) [#13566](https://github.com/NVIDIA/TensorRT-LLM/pull/13566)
  [https://nvbugs/6120981][fix] Switch to cu_seqlens_to_chunk_indices_offsets_triton with total_seqlens/extra_ch (#13566)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/mamba_backend_common.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-24** [`a8cd4fffb3`](https://github.com/NVIDIA/TensorRT-LLM/commit/a8cd4fffb3) [#14352](https://github.com/NVIDIA/TensorRT-LLM/pull/14352)
  [#14173][tests] move autodeploy accuracy tests to post merge and use model registry (#14352)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml` _+1 more__
- **2026-05-23** [`9ec3c84ddb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ec3c84ddb)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock`, `security_scanning/examples/models/core/whisper/poetry.lock` _+7 more__
- **2026-05-21** [`00f3335bf4`](https://github.com/NVIDIA/TensorRT-LLM/commit/00f3335bf4) [#14266](https://github.com/NVIDIA/TensorRT-LLM/pull/14266)
  [TRTLLM-12719][cbts] Add core code related rule (#14266)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/README.md`, `jenkins/scripts/cbts/rules/auto_deploy_rule.py` _+3 more__
- **2026-05-18** [`98359d8f54`](https://github.com/NVIDIA/TensorRT-LLM/commit/98359d8f54) [#14228](https://github.com/NVIDIA/TensorRT-LLM/pull/14228)
  [https://nvbugs/6059036][fix] Unwaive test_autodeploy_from_registry[google_gemma-3-1b] and test_encode_matches_huggingface[gemma-3-1b] (#14228)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-18** [`4abc1fd0a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4abc1fd0a6) [#14243](https://github.com/NVIDIA/TensorRT-LLM/pull/14243)
  [https://nvbugs/6094208][fix] AutoDeploy: skip bf16 Nemotron-Nano-V3 accuracy test on <80GB GPUs (#14243)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`_
- **2026-05-18** [`bd54511046`](https://github.com/NVIDIA/TensorRT-LLM/commit/bd54511046) [#14220](https://github.com/NVIDIA/TensorRT-LLM/pull/14220)
  [#14173][chore] AutoDeploy: Removed perf tests from L0 (#14220)
  _Files: `tests/integration/test_lists/test-db/l0_perf.yml`_
- **2026-05-18** [`50aacccd86`](https://github.com/NVIDIA/TensorRT-LLM/commit/50aacccd86)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock`, `security_scanning/examples/models/core/whisper/poetry.lock`, `security_scanning/metadata.json` _+2 more__

## Torch Path (_torch)  (8 commits)

- **2026-05-22** [`9c1b5c4583`](https://github.com/NVIDIA/TensorRT-LLM/commit/9c1b5c4583) [#13469](https://github.com/NVIDIA/TensorRT-LLM/pull/13469)
  [https://nvbugs/6110074][fix] Add torch.cuda.synchronize() wrapped in try/except in the _profile_runners excep (#13469)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`709e9c8541`](https://github.com/NVIDIA/TensorRT-LLM/commit/709e9c8541) [#14342](https://github.com/NVIDIA/TensorRT-LLM/pull/14342)
  [None][fix] Isolate ray tests to avoid GCS timeout in one pytest session (#14342)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_llm_update_weights_multi_gpu.py`, `tests/unittest/_torch/ray_orchestrator/multi_gpu/test_ops.py`_
- **2026-05-21** [`b7c23030de`](https://github.com/NVIDIA/TensorRT-LLM/commit/b7c23030de) [#14152](https://github.com/NVIDIA/TensorRT-LLM/pull/14152)
  [https://nvbugs/6171743][fix] Set `PYTORCH_ALLOC_CONF=expandable_segments:True` on MPI workers via `patch_mpi_ (#14152)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-20** [`234c9e4add`](https://github.com/NVIDIA/TensorRT-LLM/commit/234c9e4add) [#14217](https://github.com/NVIDIA/TensorRT-LLM/pull/14217)
  [None][chore] Remove closed bugs (#14217)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/qa/llm_function_rtx6k.txt`, `tests/integration/test_lists/test-db/l0_b200.yml` _+2 more__
- **2026-05-20** [`f406f6e3e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/f406f6e3e5) [#13567](https://github.com/NVIDIA/TensorRT-LLM/pull/13567)
  [TRTLLM-12385][feat] Use LPIPS score for visual gen model regression test (#13567)
  _Files: `.gitattributes`, `requirements-dev.txt`, `scripts/visualgen_eval/visual_gen_lpips_score_eval.py`, `tests/integration/defs/examples/golden/visual_gen_lpips/flux1_lpips_golden.json` _+8 more__
- **2026-05-19** [`989671bea2`](https://github.com/NVIDIA/TensorRT-LLM/commit/989671bea2) [#14185](https://github.com/NVIDIA/TensorRT-LLM/pull/14185)
  [https://nvbugs/6162128][tests] Skip nano v3 E2E tests entirely on G/B300 (#14185)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`_
- **2026-05-19** [`55b6973eb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/55b6973eb4) [#13917](https://github.com/NVIDIA/TensorRT-LLM/pull/13917)
  [None][doc] Add guide for integrating custom kernels in PyTorch backend (#13917)
  _Files: `docs/source/torch/adding_custom_kernels.md`_
- **2026-05-18** [`ccd98c3cd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccd98c3cd1) [#14178](https://github.com/NVIDIA/TensorRT-LLM/pull/14178)
  [None][test] add metric for trtllm-bench (#14178)
  _Files: `tests/integration/defs/perf/README_release_test.md`, `tests/integration/defs/perf/base_perf.csv`, `tests/integration/defs/perf/base_perf_pytorch.csv`, `tests/integration/defs/perf/test_perf.py` _+1 more__

## Speculative Decoding  (6 commits)

- **2026-05-22** [`c68ccf334c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c68ccf334c) [#14391](https://github.com/NVIDIA/TensorRT-LLM/pull/14391)
  [None][fix] Add MTP speculative_config to wideep dep48 mtp3 disagg yaml (#14391)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_deepseek-r1-fp4_128k8k_ctx1_pp4_gen8_pp4_bs2_eplb0_mtp0_con2-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_deepseek-r1-fp4_1k1k_ctx2_gen1_dep48_bs16_eplb288_mtp3_con12288_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_deepseek-v32-fp4_1k1k_ctx2_gen1_dep48_bs16_eplb288_mtp3_con12288_ccb-NIXL.yaml`_
- **2026-05-21** [`a1ec8dafb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a1ec8dafb9) [#14341](https://github.com/NVIDIA/TensorRT-LLM/pull/14341)
  [https://nvbugs/6079440][test] Unwaive MTP speculative decoding test (#14341)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-21** [`6b95463ff6`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b95463ff6) [#14390](https://github.com/NVIDIA/TensorRT-LLM/pull/14390)
  [None][test] Add new stress cases (#14390)
  _Files: `tests/integration/test_lists/qa/llm_perf_multinode.txt`, `tests/scripts/perf/disaggregated/gb200_stress-gpt-oss-120b-fp4_8k1k_ctx1_tp1_gen1_tp4_eplb0_eagle3_ccb-NIXL.yaml`, `tests/scripts/perf/disaggregated/gb200_wideep_stress-deepseek-r1-fp4_8k1k_ctx2_gen1_dep32_bs128_eplb288_mtp3_ccb-NIXL.yaml`_
- **2026-05-21** [`5d19712ae7`](https://github.com/NVIDIA/TensorRT-LLM/commit/5d19712ae7) [#12646](https://github.com/NVIDIA/TensorRT-LLM/pull/12646)
  [TRTLLM-11547][feat] Add Qwen3.5 MTP support. (#12646)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_5.py`, `tensorrt_llm/_torch/models/modeling_qwen3_next.py`, `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py` _+6 more__
- **2026-05-21** [`df951f0b3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/df951f0b3b) [#14366](https://github.com/NVIDIA/TensorRT-LLM/pull/14366)
  [None][fix] Import missing get_draft_token_length in py_executor (#14366)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-05-18** [`371c12662e`](https://github.com/NVIDIA/TensorRT-LLM/commit/371c12662e) [#13799](https://github.com/NVIDIA/TensorRT-LLM/pull/13799)
  [https://nvbugs/5615248][fix] Beam history copies only on terminal steps (#13799)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tensorrt_llm/_torch/speculative/mtp.py`, `tensorrt_llm/_torch/speculative/spec_sampler_base.py` _+5 more__

## Docs / Examples  (2 commits)

- **2026-05-21** [`d5a97c9a6e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5a97c9a6e) [#14422](https://github.com/NVIDIA/TensorRT-LLM/pull/14422)
  [None][chore] Bump version to 1.3.0rc16 (#14422)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-05-18** [`e4c9a7cf4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4c9a7cf4a) [#14195](https://github.com/NVIDIA/TensorRT-LLM/pull/14195)
  [None][doc] Update spec dec support matrices (#14195)
  _Files: `docs/source/features/feature-combination-matrix.md`, `docs/source/models/supported-models.md`_

## LoRA  (1 commits)

- **2026-05-21** [`19cba37e8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/19cba37e8e) [#13517](https://github.com/NVIDIA/TensorRT-LLM/pull/13517)
  [https://nvbugs/5911709][fix] Wrap lora load failures (#13517)
  _Files: `tensorrt_llm/executor/base_worker.py`, `tests/unittest/executor/test_base_worker.py`_

## Perf  (1 commits)

- **2026-05-21** [`8c52f217b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c52f217b7) [#14197](https://github.com/NVIDIA/TensorRT-LLM/pull/14197)
  [TRTLLM-12706][perf] Optimize beam search candidate reconstruction by skipping prompt-prefix copies (#14197)
  _Files: `cpp/tensorrt_llm/kernels/beamSearchKernels/beamSearchKernelsTemplate.h`, `cpp/tensorrt_llm/kernels/decodingKernels.cu`, `cpp/tests/unit_tests/kernels/decodingKernelTest.cpp`_

---
_Generated 2026-05-25 12:03 UTC_