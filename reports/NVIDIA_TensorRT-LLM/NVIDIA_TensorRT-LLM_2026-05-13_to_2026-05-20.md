# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-05-13 → 2026-05-20  |  **Total commits:** 161

## ✨ New Features This Week

- **2026-05-19** [#13401](https://github.com/NVIDIA/TensorRT-LLM/pull/13401) — [TRTLLM-11127][feat] add W4A8_MXFP4_FP8 MoE unit test support (#13401)
- **2026-05-19** [#14134](https://github.com/NVIDIA/TensorRT-LLM/pull/14134) — [None][feat] Add chunked prefill support for Gemma4 (text + vision multimodal) (#14134)
- **2026-05-19** [#13917](https://github.com/NVIDIA/TensorRT-LLM/pull/13917) — [None][doc] Add guide for integrating custom kernels in PyTorch backend (#13917)
- **2026-05-18** [#14195](https://github.com/NVIDIA/TensorRT-LLM/pull/14195) — [None][doc] Update spec dec support matrices (#14195)
- **2026-05-18** [#14144](https://github.com/NVIDIA/TensorRT-LLM/pull/14144) — [#8542][feat] AutoDeploy: add DeepSeek-R1 FP8 perf test on 8x B200 post merge, remove super perf test from premerge (#14144)
- **2026-05-18** [#14140](https://github.com/NVIDIA/TensorRT-LLM/pull/14140) — [None][chore] Refactor salting support for KVCacheManagerV2 (#14140)
- **2026-05-18** [#13882](https://github.com/NVIDIA/TensorRT-LLM/pull/13882) — [None][test] Add DSR1 B200 DISAGG to CI Perf Test (#13882)
- **2026-05-18** [#14178](https://github.com/NVIDIA/TensorRT-LLM/pull/14178) — [None][test] add metric for trtllm-bench (#14178)
- **2026-05-18** [#11741](https://github.com/NVIDIA/TensorRT-LLM/pull/11741) — [TRTLLM-10851][feat] Further doc and utility features for host profiler. (#11741)
- **2026-05-18** [#13689](https://github.com/NVIDIA/TensorRT-LLM/pull/13689) — [None][feat] Add bf16 trtllm moe through flashinfer. (#13689)
- _…and 30 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
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
| CI / Infra | 43 |
| Executor / Runtime | 22 |
| MoE | 22 |
| Attention | 17 |
| Quantization | 12 |
| Torch Path (_torch) | 9 |
| Disaggregation / KV | 9 |
| Other | 7 |
| AutoDeploy | 7 |
| Models | 4 |
| Docs / Examples | 4 |
| Speculative Decoding | 3 |
| Perf | 2 |

## CI / Infra  (43 commits)

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
- **2026-05-16** [`9555305f59`](https://github.com/NVIDIA/TensorRT-LLM/commit/9555305f59) [#14204](https://github.com/NVIDIA/TensorRT-LLM/pull/14204)
  [None][infra] Waive 1 failed cases for main in pre-merge 38428 (#14204)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`7ba0e300b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/7ba0e300b4) [#14192](https://github.com/NVIDIA/TensorRT-LLM/pull/14192)
  [None][infra] Waive 1 failed cases for main in pre-merge 38383 (#14192)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`9018d6034d`](https://github.com/NVIDIA/TensorRT-LLM/commit/9018d6034d) [#14163](https://github.com/NVIDIA/TensorRT-LLM/pull/14163)
  [None][test] Waive 1 failed cases for main in QA CI (#14163)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`ae8956fba2`](https://github.com/NVIDIA/TensorRT-LLM/commit/ae8956fba2) [#14136](https://github.com/NVIDIA/TensorRT-LLM/pull/14136)
  [None][test] Waive 1 failed cases for main in QA CI (#14136)
  _Files: `tests/integration/test_lists/qa/llm_function_rtx6k.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`40a4223ff6`](https://github.com/NVIDIA/TensorRT-LLM/commit/40a4223ff6) [#13641](https://github.com/NVIDIA/TensorRT-LLM/pull/13641)
  [https://nvbugs/6084825][fix] Unwaive testcase (#13641)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`dd43540d37`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd43540d37) [#14132](https://github.com/NVIDIA/TensorRT-LLM/pull/14132)
  [None][infra] Add mingyangHao to blossom-ci allowlist (#14132)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-05-15** [`f403d00565`](https://github.com/NVIDIA/TensorRT-LLM/commit/f403d00565) [#14147](https://github.com/NVIDIA/TensorRT-LLM/pull/14147)
  [TRTLLMINF-54][feat] Delete legacy classifyInfraFailure + four pattern lists (#14147)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-15** [`d989ff5bcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/d989ff5bcd) [#13899](https://github.com/NVIDIA/TensorRT-LLM/pull/13899)
  [TRTLLM-12152][infra] change based testing rules on tests (#13899)
  _Files: `jenkins/scripts/cbts/README.md`, `jenkins/scripts/cbts/blocks.py`, `jenkins/scripts/cbts/main.py`, `jenkins/scripts/cbts/rules/README.md` _+6 more__
- **2026-05-14** [`7021547b20`](https://github.com/NVIDIA/TensorRT-LLM/commit/7021547b20) [#13809](https://github.com/NVIDIA/TensorRT-LLM/pull/13809)
  [TRTLLMINF-54][feat] SlurmConfig boundary throws typed InfraFailure (#13809)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-14** [`740ae3b002`](https://github.com/NVIDIA/TensorRT-LLM/commit/740ae3b002) [#13877](https://github.com/NVIDIA/TensorRT-LLM/pull/13877)
  [https://nvbugs/6095421][chore] Unwaive 1 failed test (#13877)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`ed89fb69ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/ed89fb69ab) [#14002](https://github.com/NVIDIA/TensorRT-LLM/pull/14002)
  [None][fix] Reuse prior-attempt passes when infra retry fires (#14002)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/test_rerun.py`_
- **2026-05-14** [`b9e1945a26`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9e1945a26) [#14139](https://github.com/NVIDIA/TensorRT-LLM/pull/14139)
  [None][test] Unwaive K25 Disagg DEP Case  (#14139)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`f3fe93056a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f3fe93056a) [#14131](https://github.com/NVIDIA/TensorRT-LLM/pull/14131)
  [None][infra] Waive 1 failed cases for main in post-merge 2718 (#14131)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`50590a3b08`](https://github.com/NVIDIA/TensorRT-LLM/commit/50590a3b08) [#14119](https://github.com/NVIDIA/TensorRT-LLM/pull/14119)
  [None][infra] Waive 3 failed cases for main in post-merge 2717 (#14119)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`5882e37278`](https://github.com/NVIDIA/TensorRT-LLM/commit/5882e37278) [#14022](https://github.com/NVIDIA/TensorRT-LLM/pull/14022)
  [TRTLLM-12627][ci] Narrow tensorrt_llm/serve/ MGPU trigger to disagg-only files (#14022)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-05-14** [`27fdd55890`](https://github.com/NVIDIA/TensorRT-LLM/commit/27fdd55890) [#14114](https://github.com/NVIDIA/TensorRT-LLM/pull/14114)
  [None][chore] Remove the waiver (#14114)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`3c4386b26c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3c4386b26c) [#14093](https://github.com/NVIDIA/TensorRT-LLM/pull/14093)
  [None][test] Waive 1 failed cases for main in QA CI (#14093)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`4364d087a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4364d087a6) [#14086](https://github.com/NVIDIA/TensorRT-LLM/pull/14086)
  [None][test] Waive 2 failed cases for main in QA CI (#14086)
  _Files: `tests/integration/defs/.test_durations`, `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`fc6028192e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc6028192e) [#12635](https://github.com/NVIDIA/TensorRT-LLM/pull/12635)
  [TRTLLM-10804][infra] add LLM_SBSA_WHEEL_DOCKER_IMAGE (#12635)
  _Files: `docker/Makefile`, `docs/source/installation/installation-guide.md`, `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy` _+3 more__
- **2026-05-13** [`f03cb1ce6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/f03cb1ce6b) [#14058](https://github.com/NVIDIA/TensorRT-LLM/pull/14058)
  [https://nvbugs/6078431][fix] Unwaive the test_llm_disagg_streaming_gen_cancelled test. (#14058)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`07770d9160`](https://github.com/NVIDIA/TensorRT-LLM/commit/07770d9160) [#14094](https://github.com/NVIDIA/TensorRT-LLM/pull/14094)
  [None][infra] Waive 1 failed cases for main in pre-merge 37998 (#14094)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`e8b3433b78`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8b3433b78) [#13405](https://github.com/NVIDIA/TensorRT-LLM/pull/13405)
  [https://nvbugs/6102381][fix] serve /metrics from tee buffer to avoid racing iter stats collector (#13405)
  _Files: `tensorrt_llm/serve/openai_server.py`_
- **2026-05-13** [`a21f7945ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/a21f7945ab) [#14083](https://github.com/NVIDIA/TensorRT-LLM/pull/14083)
  [TRTLLM-12659][ci] move 3 python_scheduler chunked_prefill cases to post merge (#14083)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`_
- **2026-05-13** [`111b747a57`](https://github.com/NVIDIA/TensorRT-LLM/commit/111b747a57) [#14062](https://github.com/NVIDIA/TensorRT-LLM/pull/14062)
  [None][test] Waive 1 failed cases for main in QA CI (#14062)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`28da135e5e`](https://github.com/NVIDIA/TensorRT-LLM/commit/28da135e5e) [#12406](https://github.com/NVIDIA/TensorRT-LLM/pull/12406)
  [TRTLLM-9651][infra] Enhance test rerun logic with unfinished and not-run test handling (#12406)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/test_rerun.py`_
- **2026-05-13** [`ff6e1d9ef7`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff6e1d9ef7) [#13242](https://github.com/NVIDIA/TensorRT-LLM/pull/13242)
  [https://nvbugs/6050483][fix] pin diffusers version (#13242)
  _Files: `examples/visual_gen/README.md`, `examples/visual_gen/serve/README.md`, `examples/visual_gen/serve/benchmark_visual_gen.sh`, `requirements.txt` _+1 more__
- **2026-05-13** [`9d12d1e1bb`](https://github.com/NVIDIA/TensorRT-LLM/commit/9d12d1e1bb) [#13169](https://github.com/NVIDIA/TensorRT-LLM/pull/13169)
  [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion (#13169)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/allReduceFusionKernels.cu`, `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (22 commits)

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
- **2026-05-16** [`3309769235`](https://github.com/NVIDIA/TensorRT-LLM/commit/3309769235) [#14010](https://github.com/NVIDIA/TensorRT-LLM/pull/14010)
  [TRTLLM-12533][refactor] Move Media IO modality loading into MediaIO Interfaces (#14010)
  _Files: `tensorrt_llm/grpc/grpc_servicer.py`, `tensorrt_llm/inputs/media_io.py`, `tensorrt_llm/inputs/utils.py`, `tensorrt_llm/serve/chat_utils.py` _+6 more__
- **2026-05-15** [`731eb9bd9e`](https://github.com/NVIDIA/TensorRT-LLM/commit/731eb9bd9e) [#13918](https://github.com/NVIDIA/TensorRT-LLM/pull/13918)
  [None][fix] Make SleepConfig picklable by replacing closure lambda in defaultdict (#13918)
  _Files: `tensorrt_llm/llmapi/llm_args.py`, `tests/unittest/llmapi/test_llm_args.py`_
- **2026-05-15** [`55659c580b`](https://github.com/NVIDIA/TensorRT-LLM/commit/55659c580b) [#13520](https://github.com/NVIDIA/TensorRT-LLM/pull/13520)
  [https://nvbugs/5944731][fix] BREAKING: Limit sampling requested logprobs (#13520)
  _Files: `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tensorrt_llm/sampling_params.py`, `tensorrt_llm/serve/openai_protocol.py`, `tests/unittest/llmapi/test_sampling_params.py`_
- **2026-05-15** [`a530424b33`](https://github.com/NVIDIA/TensorRT-LLM/commit/a530424b33) [#13519](https://github.com/NVIDIA/TensorRT-LLM/pull/13519)
  [https://nvbugs/5923456][fix] GRPC bound request payloads (#13519)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/grpc/grpc_request_manager.py`, `tensorrt_llm/grpc/grpc_servicer.py`, `tests/unittest/llmapi/test_grpc.py`_
- **2026-05-15** [`8a11da8bff`](https://github.com/NVIDIA/TensorRT-LLM/commit/8a11da8bff) [#13758](https://github.com/NVIDIA/TensorRT-LLM/pull/13758)
  [https://nvbugs/5805494][fix] Limit maximum warmup token count to prevent crash in autotuner (#13758)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tests/unittest/_torch/executor/test_pytorch_model_engine.py`_
- **2026-05-15** [`6042b4cf82`](https://github.com/NVIDIA/TensorRT-LLM/commit/6042b4cf82) [#13592](https://github.com/NVIDIA/TensorRT-LLM/pull/13592)
  [None][fix] Clear stale Scheduler V2 request state (#13592)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`, `tests/unittest/_torch/executor/test_kv_cache_v2_scheduler.py`_
- **2026-05-14** [`18479bda83`](https://github.com/NVIDIA/TensorRT-LLM/commit/18479bda83) [#13784](https://github.com/NVIDIA/TensorRT-LLM/pull/13784)
  [None][fix] Move drain inside pause_generation() for async RL (#13784)
  _Files: `tensorrt_llm/_torch/async_llm.py`, `tensorrt_llm/llmapi/rlhf_utils.py`_
- **2026-05-14** [`a227373939`](https://github.com/NVIDIA/TensorRT-LLM/commit/a227373939) [#12788](https://github.com/NVIDIA/TensorRT-LLM/pull/12788)
  [TRTLLM-11375][feat] Add Kimi K2.5 multimodal vision support (#12788)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_kimi_k25.py` _+8 more__
- **2026-05-14** [`54c5c4b468`](https://github.com/NVIDIA/TensorRT-LLM/commit/54c5c4b468) [#13132](https://github.com/NVIDIA/TensorRT-LLM/pull/13132)
  [https://nvbugs/6076767][fix] Add barrier before warmup to prevent PP hang with guided decoding (#13132)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-05-13** [`8cc5b61f8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cc5b61f8e) [#13933](https://github.com/NVIDIA/TensorRT-LLM/pull/13933)
  [None][test] Add checkpoint_format / load_format keys to test_features_contract (#13933)
  _Files: `tests/unittest/llmapi/test_features_contract.py`_
- **2026-05-13** [`7b49db39e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b49db39e0) [#14064](https://github.com/NVIDIA/TensorRT-LLM/pull/14064)
  [None][infra] Add explicit llmapi-compatibility label gh check when api touched (#14064)
  _Files: `.github/pull_request_template.md`, `.github/workflows/llm-api-compatibility.yml`, `CONTRIBUTING.md`, `docs/source/developer-guide/api-change.md`_
- **2026-05-13** [`7ced42ad99`](https://github.com/NVIDIA/TensorRT-LLM/commit/7ced42ad99) [#14050](https://github.com/NVIDIA/TensorRT-LLM/pull/14050)
  [None][fix] AutoDeploy: Cleanup CUDA graph memory in shutdown (#14050)
  _Files: `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`_
- **2026-05-13** [`550de9fb38`](https://github.com/NVIDIA/TensorRT-LLM/commit/550de9fb38) [#13251](https://github.com/NVIDIA/TensorRT-LLM/pull/13251)
  [None][fix] Fix GIL management for guided decoding host func (#13251)
  _Files: `cpp/tensorrt_llm/nanobind/runtime/hostfunc.cpp`_

## MoE  (22 commits)

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
- **2026-05-17** [`06cff70502`](https://github.com/NVIDIA/TensorRT-LLM/commit/06cff70502) [#14069](https://github.com/NVIDIA/TensorRT-LLM/pull/14069)
  [https://nvbugs/6152892][fix] Fix Triton MOE memory free when no swizzling enabled (#14069)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/defs/conftest.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-17** [`4d20ed133b`](https://github.com/NVIDIA/TensorRT-LLM/commit/4d20ed133b) [#14215](https://github.com/NVIDIA/TensorRT-LLM/pull/14215)
  [https://nvbugs/6184143][chore] AutoDeploy Waive DeciLM and GraniteMoEHybrid failures (#14215)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-16** [`65a5b3471d`](https://github.com/NVIDIA/TensorRT-LLM/commit/65a5b3471d) [#13787](https://github.com/NVIDIA/TensorRT-LLM/pull/13787)
  [#13446][feat] AutoDeploy: Add Remaining Models From Model Onboarding Sprint Part 1 (03/19) (#13787)
  _Files: `.claude/agents/ad-onboard-reviewer.md`, `.claude/skills/ad-model-onboard/SKILL.md`, `docs/source/models/supported-models.md`, `examples/auto_deploy/model_registry/configs/aya_vision_8b.yaml` _+71 more__
- **2026-05-15** [`3ae0b70604`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ae0b70604) [#14054](https://github.com/NVIDIA/TensorRT-LLM/pull/14054)
  [https://nvbugs/6162323][fix] Make mxfp4 H20 swizzle WAR more robust (#14054)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`da9ce58116`](https://github.com/NVIDIA/TensorRT-LLM/commit/da9ce58116) [#13994](https://github.com/NVIDIA/TensorRT-LLM/pull/13994)
  [None][feat] Upgrade transformers dependency to 5.5.3 (#13994)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/torch_quant.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_eagle.py` _+18 more__
- **2026-05-15** [`849bb4d710`](https://github.com/NVIDIA/TensorRT-LLM/commit/849bb4d710) [#14171](https://github.com/NVIDIA/TensorRT-LLM/pull/14171)
  [None] [docs] rename blog23_MoE_as_Dense_GEMM to blog24_MoE_as_Dense_GEMM (#14171)
  _Files: `docs/source/blogs/tech_blog/blog24_MoE_as_Dense_GEMM.md`_
- **2026-05-15** [`e5456dad23`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5456dad23) [#13834](https://github.com/NVIDIA/TensorRT-LLM/pull/13834)
  [None][doc] Add tech blog23: MoE as Dense GEMM on Blackwell (#13834)
  _Files: `docs/source/blogs/media/tech_blog23_Picture1.png`, `docs/source/blogs/media/tech_blog23_Picture2.png`, `docs/source/blogs/tech_blog/blog23_MoE_as_Dense_GEMM.md`_
- **2026-05-15** [`a3e0f56068`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3e0f56068)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+48 more__
- **2026-05-14** [`e6ccf9772d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6ccf9772d) [#14004](https://github.com/NVIDIA/TensorRT-LLM/pull/14004)
  [None][feat] AutoDeploy re-onboard GPT_OSS (#14004)
  _Files: `docs/source/models/supported-models.md`, `examples/auto_deploy/cookbooks/gpt_oss_trtllm_cookbook.ipynb`, `examples/auto_deploy/model_registry/configs/gpt_oss_120b.yaml`, `examples/auto_deploy/model_registry/configs/gpt_oss_20b.yaml` _+11 more__
- **2026-05-14** [`553b8dea22`](https://github.com/NVIDIA/TensorRT-LLM/commit/553b8dea22)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+50 more__
- **2026-05-14** [`fca29e8116`](https://github.com/NVIDIA/TensorRT-LLM/commit/fca29e8116) [#13964](https://github.com/NVIDIA/TensorRT-LLM/pull/13964)
  [None][test] promote DeepSeek-V4-Flash to MoE CI config subset (#13964)
  _Files: `tests/unittest/_torch/modules/moe/moe_test_utils.py`, `tests/unittest/_torch/modules/moe/test_moe_module.py`_
- **2026-05-13** [`2fd65a5fa1`](https://github.com/NVIDIA/TensorRT-LLM/commit/2fd65a5fa1) [#13997](https://github.com/NVIDIA/TensorRT-LLM/pull/13997)
  [None][feat] enable TRTLLM-Gen internal routing (#13997)
  _Files: `examples/auto_deploy/model_registry/configs/super_v3.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/multi_stream_moe.py` _+1 more__
- **2026-05-13** [`c3dce701ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3dce701ac)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+51 more__

## Attention  (17 commits)

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
- **2026-05-16** [`566fd230a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/566fd230a6) [#13996](https://github.com/NVIDIA/TensorRT-LLM/pull/13996)
  [TRTLLM-11228][feat] Perf optimizations for DFlash (#13996)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/speculative/dflash.py` _+1 more__
- **2026-05-14** [`b9c17305a5`](https://github.com/NVIDIA/TensorRT-LLM/commit/b9c17305a5) [#13929](https://github.com/NVIDIA/TensorRT-LLM/pull/13929)
  [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel (#13929)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/__init__.py`, `tensorrt_llm/_torch/cute_dsl_kernels/blackwell/paged_mqa_logits/fp4_paged_mqa_logits.py` _+10 more__
- **2026-05-14** [`f5b0bdea06`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5b0bdea06) [#13166](https://github.com/NVIDIA/TensorRT-LLM/pull/13166)
  [None][fix] Raise clear error when GPT-OSS is used with non-TRTLLM attention backend (#13166)
  _Files: `tensorrt_llm/_torch/models/modeling_gpt_oss.py`, `tensorrt_llm/_torch/modules/attention.py`_
- **2026-05-14** [`b19e6a611e`](https://github.com/NVIDIA/TensorRT-LLM/commit/b19e6a611e) [#14076](https://github.com/NVIDIA/TensorRT-LLM/pull/14076)
  [None][chore] Update flashinfer-python from 0.6.11 to 0.6.11.post1 (#14076)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-05-14** [`58e7572c08`](https://github.com/NVIDIA/TensorRT-LLM/commit/58e7572c08) [#13873](https://github.com/NVIDIA/TensorRT-LLM/pull/13873)
  [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing (#13873)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/configs/wan2.2-t2v-fp4-1gpu.yaml`, `examples/visual_gen/configs/wan2.2-t2v-fp4-4gpu.yaml` _+21 more__
- **2026-05-13** [`23cd0c3eae`](https://github.com/NVIDIA/TensorRT-LLM/commit/23cd0c3eae) [#13649](https://github.com/NVIDIA/TensorRT-LLM/pull/13649)
  [None][feat] Emit per-rank Attention-DP iteration stats (#13649)
  _Files: `tensorrt_llm/_torch/pyexecutor/adp_iter_stats.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/scheduler/adp_router.py`, `tensorrt_llm/executor/base_worker.py` _+3 more__
- **2026-05-13** [`f7fadf1b84`](https://github.com/NVIDIA/TensorRT-LLM/commit/f7fadf1b84) [#13052](https://github.com/NVIDIA/TensorRT-LLM/pull/13052)
  [#12716][feat] Fused cross-head QK Norm + RoPE kernel for WAN (#13052)
  _Files: `benchmarks/bench_fused_dit_cross_head_qk_norm_rope.py`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.h`, `cpp/tensorrt_llm/thop/fusedDiTQKNormRopeOp.cpp` _+4 more__
- **2026-05-13** [`6232f76fa9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6232f76fa9) [#14077](https://github.com/NVIDIA/TensorRT-LLM/pull/14077)
  [None][chore] Make poetry.lock update opt-in in flashinfer-upgrade skill (#14077)
  _Files: `.claude/skills/flashinfer-upgrade/SKILL.md`_
- **2026-05-13** [`b19ac7bc5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/b19ac7bc5a) [#14067](https://github.com/NVIDIA/TensorRT-LLM/pull/14067)
  [https://nvbugs/6084568][fix] Fix attention workspace error when running qwen3 CI (#14067)
  _Files: `tests/integration/test_lists/test-db/l0_gb200_multi_nodes.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`609557c145`](https://github.com/NVIDIA/TensorRT-LLM/commit/609557c145) [#14038](https://github.com/NVIDIA/TensorRT-LLM/pull/14038)
  [https://nvbugs/6160248][fix] AutoDeploy: fixed broken pattern matching of fuse_rope_into_trtllm_attention transform (#14038)
  _Files: `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rope_into_trtllm_attention.py`_
- **2026-05-13** [`1a8f5ab795`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a8f5ab795) [#13992](https://github.com/NVIDIA/TensorRT-LLM/pull/13992)
  [None][chore] Update flashinfer-python from 0.6.10 to 0.6.11 (#13992)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-05-13** [`f0d926c874`](https://github.com/NVIDIA/TensorRT-LLM/commit/f0d926c874) [#13808](https://github.com/NVIDIA/TensorRT-LLM/pull/13808)
  [None][feat] Update FMHA cubins for head_dim 80 (#13808)
  _Files: `cpp/tensorrt_llm/kernels/fmhaDispatcher.cpp`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/kernelMetaInfo.h`, `tests/unittest/trt/attention/test_gpt_attention.py`, `tests/unittest/utils/util.py`_

## Quantization  (12 commits)

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
- **2026-05-17** [`667bec046e`](https://github.com/NVIDIA/TensorRT-LLM/commit/667bec046e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+47 more__
- **2026-05-16** [`aa52b40e80`](https://github.com/NVIDIA/TensorRT-LLM/commit/aa52b40e80)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+57 more__
- **2026-05-15** [`b0b0052d18`](https://github.com/NVIDIA/TensorRT-LLM/commit/b0b0052d18) [#14118](https://github.com/NVIDIA/TensorRT-LLM/pull/14118)
  [https://nvbugs/6168136][fix] Unwaive GPT-OSS test_w4_4gpus dp4-trtllm-fp8 (#14118)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`c3ba00714b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c3ba00714b) [#12823](https://github.com/NVIDIA/TensorRT-LLM/pull/12823)
  [None][fix] Fix DeepSeekV32 test_fp8_blockscale[baseline_mtp1] OOM on Blackwell (#12823)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-05-14** [`c5e405618e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c5e405618e) [#13846](https://github.com/NVIDIA/TensorRT-LLM/pull/13846)
  [https://nvbugs/6143811][fix] AutoDeploy gate quantization tests (#13846)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`da55b34d2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/da55b34d2e) [#14039](https://github.com/NVIDIA/TensorRT-LLM/pull/14039)
  [#8542][feat] AutoDeploy: add Llama-3.1-8B FP8 perf-sanity test on H100 (#14039)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/test-db/l0_h100.yml`, `tests/scripts/perf-sanity/aggregated/llama3_1_8b_fp8_ad_hopper.yaml`_
- **2026-05-13** [`7b39eb1a19`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b39eb1a19) [#13837](https://github.com/NVIDIA/TensorRT-LLM/pull/13837)
  [None][test] Add func and perf case of nemotron-3-Nano-Omni model on DGX-Spark (#13837)
  _Files: `tests/integration/defs/examples/serve/test_configs/Nemotron3_Nano_Omni_30B_NVFP4.yml`, `tests/integration/defs/examples/serve/test_configs/Nemotron3_Super_120B_NVFP4.yml`, `tests/integration/defs/examples/serve/test_serve.py`, `tests/integration/defs/perf/pytorch_model_config.py` _+4 more__

## Torch Path (_torch)  (9 commits)

- **2026-05-19** [`989671bea2`](https://github.com/NVIDIA/TensorRT-LLM/commit/989671bea2) [#14185](https://github.com/NVIDIA/TensorRT-LLM/pull/14185)
  [https://nvbugs/6162128][tests] Skip nano v3 E2E tests entirely on G/B300 (#14185)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`_
- **2026-05-19** [`55b6973eb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/55b6973eb4) [#13917](https://github.com/NVIDIA/TensorRT-LLM/pull/13917)
  [None][doc] Add guide for integrating custom kernels in PyTorch backend (#13917)
  _Files: `docs/source/torch/adding_custom_kernels.md`_
- **2026-05-18** [`ccd98c3cd1`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccd98c3cd1) [#14178](https://github.com/NVIDIA/TensorRT-LLM/pull/14178)
  [None][test] add metric for trtllm-bench (#14178)
  _Files: `tests/integration/defs/perf/README_release_test.md`, `tests/integration/defs/perf/base_perf.csv`, `tests/integration/defs/perf/base_perf_pytorch.csv`, `tests/integration/defs/perf/test_perf.py` _+1 more__
- **2026-05-16** [`3a354dcc73`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a354dcc73) [#13977](https://github.com/NVIDIA/TensorRT-LLM/pull/13977)
  [None][perf] Enable in-flight batching for Nemotron3 Nano Omni multimodal encoder (#13977)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tests/unittest/_torch/modeling/test_modeling_nemotron_nano_v2_vl.py`, `tests/unittest/_torch/modeling/test_nemotron_nano_preprocessing.py`_
- **2026-05-15** [`159a2f5fb9`](https://github.com/NVIDIA/TensorRT-LLM/commit/159a2f5fb9) [#14031](https://github.com/NVIDIA/TensorRT-LLM/pull/14031)
  [TRTLLM-11950][perf] Audio feature extractor optimizations (#14031)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_nano.py`, `tensorrt_llm/_torch/models/modeling_parakeet.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/unittest/_torch/modeling/test_modeling_parakeet.py` _+1 more__
- **2026-05-15** [`472face04f`](https://github.com/NVIDIA/TensorRT-LLM/commit/472face04f) [#14101](https://github.com/NVIDIA/TensorRT-LLM/pull/14101)
  [None][tests] Speed up EPD disagg tests (#14101)
  _Files: `tests/unittest/_torch/multimodal/test_mm_encoder_standalone.py`_
- **2026-05-14** [`7d2bed7820`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d2bed7820) [#13740](https://github.com/NVIDIA/TensorRT-LLM/pull/13740)
  [https://nvbugs/6108841][fix] add hidden_dim=6144 router GEMM instantiation for GLM-5 (#13740)
  _Files: `cpp/tensorrt_llm/kernels/dsv3MinLatencyKernels/dsv3RouterGemm.cu`, `cpp/tensorrt_llm/thop/dsv3RouterGemmOp.cpp`, `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py`_
- **2026-05-13** [`0a861da1d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a861da1d7) [#13285](https://github.com/NVIDIA/TensorRT-LLM/pull/13285)
  [TRTLLM-11767][feat] LTX2 pipeline refactor part1 (#13285)
  _Files: `examples/visual_gen/visual_gen_ltx2.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2.py`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_
- **2026-05-13** [`2225b7fe3a`](https://github.com/NVIDIA/TensorRT-LLM/commit/2225b7fe3a) [#14036](https://github.com/NVIDIA/TensorRT-LLM/pull/14036)
  [https://nvbugs/6162128] Remove nano v3 E2E test (#14036)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_

## Disaggregation / KV  (9 commits)

- **2026-05-18** [`f819383a44`](https://github.com/NVIDIA/TensorRT-LLM/commit/f819383a44) [#13882](https://github.com/NVIDIA/TensorRT-LLM/pull/13882)
  [None][test] Add DSR1 B200 DISAGG to CI Perf Test (#13882)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/disaggregated/submit.py`, `jenkins/scripts/perf/local/submit.py`, `tests/integration/test_lists/test-db/l0_b200_multi_nodes_perf_sanity_node2_gpu16.yml` _+2 more__
- **2026-05-18** [`1109e1cc65`](https://github.com/NVIDIA/TensorRT-LLM/commit/1109e1cc65) [#14168](https://github.com/NVIDIA/TensorRT-LLM/pull/14168)
  [https://nvbugs/6094100][fix] set UCX_TLS  for gb300 to enable disagg test (#14168)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-15** [`9afe4549dd`](https://github.com/NVIDIA/TensorRT-LLM/commit/9afe4549dd) [#14063](https://github.com/NVIDIA/TensorRT-LLM/pull/14063)
  [https://nvbugs/5981122][fix] Lower KV cache fraction for python_scheduler MTP combo on H100 (#14063)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-14** [`7a890ac018`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a890ac018) [#13422](https://github.com/NVIDIA/TensorRT-LLM/pull/13422)
  [https://nvbugs/6109719][fix] Update all broken URLs to their new locations and remove the expired event entry (#13422)
  _Files: `README.md`, `docker/develop.md`, `docs/source/blogs/Best_perf_practice_on_DeepSeek-R1_in_TensorRT-LLM.md`, `docs/source/blogs/tech_blog/blog05_Disaggregated_Serving_in_TensorRT-LLM.md` _+11 more__
- **2026-05-13** [`44d0b01543`](https://github.com/NVIDIA/TensorRT-LLM/commit/44d0b01543) [#13807](https://github.com/NVIDIA/TensorRT-LLM/pull/13807)
  [https://nvbugs/6141806][test] unwaive disaggregated overlap gen-first tests (#13807)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`e60f9107e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/e60f9107e7) [#13075](https://github.com/NVIDIA/TensorRT-LLM/pull/13075)
  [None][feat] use multi thread for kv transfer (#13075)
  _Files: `tensorrt_llm/_torch/disaggregation/native/transfer.py`, `tests/unittest/disaggregated/test_kv_transfer.py`, `tests/unittest/disaggregated/test_kv_transfer_mp.py`_
- **2026-05-13** [`f9ae14b948`](https://github.com/NVIDIA/TensorRT-LLM/commit/f9ae14b948) [#13594](https://github.com/NVIDIA/TensorRT-LLM/pull/13594)
  [None][test] Add GB300 DISAGG NIXL CI Perf Test Back (#13594)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/perf/disaggregated/submit.py`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_ctx1_node1_gpu4_gen1_node1_gpu4.yml`, `tests/integration/test_lists/test-db/l0_gb300_multi_nodes_perf_sanity_ctx1_node1_gpu4_gen1_node2_gpu8.yml` _+3 more__
- **2026-05-13** [`4baeec385d`](https://github.com/NVIDIA/TensorRT-LLM/commit/4baeec385d) [#13793](https://github.com/NVIDIA/TensorRT-LLM/pull/13793)
  [None][feat] Support cache_salt_id in KV cache v2 manager (#13793)
  _Files: `examples/llm-api/llm_kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/connectors/kv_cache_connector.py`, `tensorrt_llm/_torch/pyexecutor/resource_manager.py`, `tensorrt_llm/runtime/kv_cache_manager_v2/__init__.pyi` _+4 more__
- **2026-05-13** [`2318adbad0`](https://github.com/NVIDIA/TensorRT-LLM/commit/2318adbad0) [#14041](https://github.com/NVIDIA/TensorRT-LLM/pull/14041)
  [None][fix] fix warm up number in disagg benchmark (#14041)
  _Files: `examples/disaggregated/slurm/benchmark/submit.py`_

## Other  (7 commits)

- **2026-05-20** [`9871cbea12`](https://github.com/NVIDIA/TensorRT-LLM/commit/9871cbea12) [#14122](https://github.com/NVIDIA/TensorRT-LLM/pull/14122)
  [None][chore] Remove trailing spaces from module name in logger output (#14122)
  _Files: `cpp/include/tensorrt_llm/common/logger.h`, `cpp/tests/unit_tests/common/loggerTest.cpp`, `tensorrt_llm/logger.py`, `tests/unittest/utils/test_logger.py`_
- **2026-05-19** [`ba685046cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba685046cc) [#14285](https://github.com/NVIDIA/TensorRT-LLM/pull/14285)
  [None][chore] Enforce Claude Code skill and agent naming convention via pre-commit (#14285)
  _Files: `.pre-commit-config.yaml`, `scripts/check_skill_naming_convention.py`_
- **2026-05-18** [`2ad0060dee`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ad0060dee) [#14211](https://github.com/NVIDIA/TensorRT-LLM/pull/14211)
  [None][chore] gitignore NFS system temporary files (#14211)
  _Files: `.gitignore`_
- **2026-05-14** [`d75df195c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/d75df195c5) [#14106](https://github.com/NVIDIA/TensorRT-LLM/pull/14106)
  [None][fix] Add SPDX Apache-2.0 headers and fix license compliance for llm-c standalone repo (#14106)
- **2026-05-14** [`9a9d73d6df`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a9d73d6df) [#14068](https://github.com/NVIDIA/TensorRT-LLM/pull/14068)
  [https://nvbugs/6058251][fix] Resolve top-level model_type for composite HF configs (#14068)
  _Files: `tensorrt_llm/serve/chat_utils.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/responses_utils.py`_
- **2026-05-14** [`21dd6987d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/21dd6987d9) [#14030](https://github.com/NVIDIA/TensorRT-LLM/pull/14030)
  [None][fix] skip tokenizer in kvcache router when there is only one server (#14030)
  _Files: `tensorrt_llm/serve/router.py`_
- **2026-05-14** [`8fdce1c221`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fdce1c221) [#13970](https://github.com/NVIDIA/TensorRT-LLM/pull/13970)
  [None][fix] Fix misleading skills that use the -ccache option (#13970)
  _Files: `.claude/skills/exec-local-compile/SKILL.md`, `.claude/skills/exec-slurm-compile/SKILL.md`_

## AutoDeploy  (7 commits)

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
- **2026-05-15** [`c38f0d2484`](https://github.com/NVIDIA/TensorRT-LLM/commit/c38f0d2484) [#13396](https://github.com/NVIDIA/TensorRT-LLM/pull/13396)
  [#13321][fix] disable multi_stream on piecewise path instead of persistent buffer (#13396)
  _Files: `examples/auto_deploy/model_registry/configs/deepseek-r1.yaml`, `examples/auto_deploy/model_registry/configs/nano_v3.yaml`, `tensorrt_llm/_torch/auto_deploy/compile/backends/torch_cudagraph.py`, `tensorrt_llm/_torch/auto_deploy/compile/piecewise_runner.py` _+7 more__
- **2026-05-14** [`579a10f912`](https://github.com/NVIDIA/TensorRT-LLM/commit/579a10f912) [#14103](https://github.com/NVIDIA/TensorRT-LLM/pull/14103)
  [https://nvbugs/6080024][fix] autodeploy unwaive test (#14103)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-13** [`be4f57ecef`](https://github.com/NVIDIA/TensorRT-LLM/commit/be4f57ecef) [#14081](https://github.com/NVIDIA/TensorRT-LLM/pull/14081)
  [https://nvbugs/6160248][fix] AutoDeploy: unwaived test_fuse_qkv_passthrough_with_rope (#14081)
  _Files: `tests/integration/test_lists/waives.txt`_

## Models  (4 commits)

- **2026-05-19** [`95ad97ea69`](https://github.com/NVIDIA/TensorRT-LLM/commit/95ad97ea69) [#14293](https://github.com/NVIDIA/TensorRT-LLM/pull/14293)
  [https://nvbugs/6185234][fix] register deepseek_v32 / kimi_k2 with transformers AutoConfig (#14293)
  _Files: `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/models/__init__.py`, `tests/unittest/_torch/test_custom_config_registration.py`_
- **2026-05-19** [`04357222e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/04357222e3) [#13895](https://github.com/NVIDIA/TensorRT-LLM/pull/13895)
  [https://nvbugs/6069543][fix] Lower accuracy threshold for H20 qwen3.5 test (#13895)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_
- **2026-05-19** [`2af9ba9b84`](https://github.com/NVIDIA/TensorRT-LLM/commit/2af9ba9b84) [#14261](https://github.com/NVIDIA/TensorRT-LLM/pull/14261)
  [https://nvbugs/6185234][fix] DeepSeek-V3.2 tokenizer load on transformers 5.x (#14261)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`_
- **2026-05-14** [`95204b7802`](https://github.com/NVIDIA/TensorRT-LLM/commit/95204b7802) [#14082](https://github.com/NVIDIA/TensorRT-LLM/pull/14082)
  [None][fix] Gemma4 CUDA-graph test KV pre-alloc + L0 registration (#14082)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/modeling/test_modeling_gemma4.py`_

## Docs / Examples  (4 commits)

- **2026-05-18** [`e4c9a7cf4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4c9a7cf4a) [#14195](https://github.com/NVIDIA/TensorRT-LLM/pull/14195)
  [None][doc] Update spec dec support matrices (#14195)
  _Files: `docs/source/features/feature-combination-matrix.md`, `docs/source/models/supported-models.md`_
- **2026-05-15** [`d5ecfd3518`](https://github.com/NVIDIA/TensorRT-LLM/commit/d5ecfd3518) [#11841](https://github.com/NVIDIA/TensorRT-LLM/pull/11841)
  [None][doc] scaffolding tech blog part two (#11841)
  _Files: `README.md`, `docs/source/blogs/media/tech_blog23_open_deep_research_workflow.png`, `docs/source/blogs/media/tech_blog23_queuing_delays.png`, `docs/source/blogs/tech_blog/blog23_Joint_Optimization_of_Agent_Applications_and_TensorRT-LLM.md`_
- **2026-05-13** [`acba2516eb`](https://github.com/NVIDIA/TensorRT-LLM/commit/acba2516eb) [#13942](https://github.com/NVIDIA/TensorRT-LLM/pull/13942)
  [None][feat] Add --use-3rdparty-cache to accelerate cmake configuration of clean build (#13942)
  _Files: `.gitignore`, `3rdparty/CMakeLists.txt`, `3rdparty/README.md`, `3rdparty/fetch-cache.md` _+5 more__
- **2026-05-13** [`8bee59eb6f`](https://github.com/NVIDIA/TensorRT-LLM/commit/8bee59eb6f) [#13979](https://github.com/NVIDIA/TensorRT-LLM/pull/13979)
  [None][doc] Fix replay iter flag names in layer-wise benchmarks docs (#13979)
  _Files: `examples/layer_wise_benchmarks/README.md`, `examples/layer_wise_benchmarks/sample_performance_alignment.sh`_

## Speculative Decoding  (3 commits)

- **2026-05-18** [`371c12662e`](https://github.com/NVIDIA/TensorRT-LLM/commit/371c12662e) [#13799](https://github.com/NVIDIA/TensorRT-LLM/pull/13799)
  [https://nvbugs/5615248][fix] Beam history copies only on terminal steps (#13799)
  _Files: `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tensorrt_llm/_torch/speculative/mtp.py`, `tensorrt_llm/_torch/speculative/spec_sampler_base.py` _+5 more__
- **2026-05-15** [`acc41c1d27`](https://github.com/NVIDIA/TensorRT-LLM/commit/acc41c1d27) [#12588](https://github.com/NVIDIA/TensorRT-LLM/pull/12588)
  [TRTLLM-11540][feat] Support rejection sampling in EAGLE3 dynamic tree (#12588)
  _Files: `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.cu`, `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.h`, `cpp/tensorrt_llm/thop/dynamicTreeOp.cpp`, `docs/source/features/speculative-decoding.md` _+14 more__
- **2026-05-14** [`54b2279d50`](https://github.com/NVIDIA/TensorRT-LLM/commit/54b2279d50) [#13532](https://github.com/NVIDIA/TensorRT-LLM/pull/13532)
  [#13534][chore] AutoDeploy: Remove Two Model Speculative Decoding Support (#13532)
  _Files: `tensorrt_llm/_torch/auto_deploy/llm_args.py`, `tensorrt_llm/_torch/auto_deploy/shim/ad_executor.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/hidden_states.py`, `tensorrt_llm/_torch/auto_deploy/utils/_graph.py` _+6 more__

## Perf  (2 commits)

- **2026-05-15** [`f4abee975d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4abee975d) [#14070](https://github.com/NVIDIA/TensorRT-LLM/pull/14070)
  [None][perf] Speed up model init: cache support_nvlink() (#14070)
  _Files: `cpp/tensorrt_llm/thop/allreduceOp.cpp`, `tensorrt_llm/_mnnvl_utils.py`_
- **2026-05-14** [`6ccb07a2b0`](https://github.com/NVIDIA/TensorRT-LLM/commit/6ccb07a2b0) [#13638](https://github.com/NVIDIA/TensorRT-LLM/pull/13638)
  [None][feat] add batch-full benchmark throughput metric (#13638)
  _Files: `tensorrt_llm/bench/dataclasses/reporting.py`, `tensorrt_llm/bench/dataclasses/statistics.py`_

---
_Generated 2026-05-20 04:15 UTC_