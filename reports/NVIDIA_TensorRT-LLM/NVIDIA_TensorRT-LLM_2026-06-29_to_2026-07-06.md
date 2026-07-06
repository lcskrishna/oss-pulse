# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-06-29 → 2026-07-06  |  **Total commits:** 183

## ✨ New Features This Week

- **2026-07-06** [#15555](https://github.com/NVIDIA/TensorRT-LLM/pull/15555) — [TRTLLM-13584][feat] add Wan VAE backend (#15555)
- **2026-07-06** [#14990](https://github.com/NVIDIA/TensorRT-LLM/pull/14990) — [None][test] Add gpt-oss-120b eagle3 accuracy test (#14990)
- **2026-07-06** [#14810](https://github.com/NVIDIA/TensorRT-LLM/pull/14810) — [#14588][feat] AutoDeploy: DeepSeek-R1 optimization for low concurrency (#14810)
- **2026-07-05** [#15637](https://github.com/NVIDIA/TensorRT-LLM/pull/15637) — [TRTLLM-13176][feat] Enables CUDA graph execution for PyTorch encoder-decoder models (#15637)
- **2026-07-04** [#12262](https://github.com/NVIDIA/TensorRT-LLM/pull/12262) — [TRTLLM-11556][feat] Expand dynamic speculation to all spec decode algorithms (#12262)
- **2026-07-04** [#15768](https://github.com/NVIDIA/TensorRT-LLM/pull/15768) — [None][feat] Add Gemma 4 12B Unified (encoder-free multimodal) support (#15768)
- **2026-07-03** [#15857](https://github.com/NVIDIA/TensorRT-LLM/pull/15857) — [TRTLLM-13458][feat] Support Minimax M3 NVFP4 checkpoint (#15857)
- **2026-07-03** [#15470](https://github.com/NVIDIA/TensorRT-LLM/pull/15470) — [None][feat] Qwen-Image: load pre-quantized ModelOpt NVFP4/FP8 checkpoints (#15470)
- **2026-07-03** [#15633](https://github.com/NVIDIA/TensorRT-LLM/pull/15633) — [None][feat] DSv4 follow-up: runtime KV and cache foundations (#15633)
- **2026-07-03** [#15714](https://github.com/NVIDIA/TensorRT-LLM/pull/15714) — [TRTLLM-13581][test] Add moe fp4 gpu dequant and unpack optimization (#15714)
- _…and 34 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#15634](https://github.com/NVIDIA/TensorRT-LLM/issues/15634) | [Bug] Qwen3-Next (Gated-DeltaNet) fails at warmup on consumer Blackwel | Customized kernels | 2026-06-25 |
| [#10241](https://github.com/NVIDIA/TensorRT-LLM/issues/10241) | [Feature]: Add NVFP4 KV cache support for SM120 in trtllm-gen | feature request, KV-Cache Management | 2026-06-19 |
| [#15339](https://github.com/NVIDIA/TensorRT-LLM/issues/15339) | [Feature]: Add TRTLLM-gen FMHA Dense paged GQA generation cubins for P | feature request, Customized kernels | 2026-06-13 |
| [#15328](https://github.com/NVIDIA/TensorRT-LLM/issues/15328) | [Parity with vLLM, SGLang, ATOM]: Public Nightly NGC docker images too | feature request | 2026-06-12 |
| [#14826](https://github.com/NVIDIA/TensorRT-LLM/issues/14826) | [Bug]: Using the official tensorrt llm whisper conversion script does  | bug, Triton backend | 2026-06-10 |
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
| CI / Infra | 57 |
| MoE | 25 |
| Attention | 21 |
| Executor / Runtime | 19 |
| Quantization | 11 |
| Models | 11 |
| Torch Path (_torch) | 10 |
| Disaggregation / KV | 8 |
| Other | 7 |
| Speculative Decoding | 6 |
| Docs / Examples | 3 |
| AutoDeploy | 3 |
| Perf | 1 |
| LoRA | 1 |

## CI / Infra  (57 commits)

- **2026-07-06** [`ef6ebc2f2c`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef6ebc2f2c) [#15977](https://github.com/NVIDIA/TensorRT-LLM/pull/15977)
  [None][test] Waive 1 failed cases for main in QA CI (#15977)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`0044d5b5c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0044d5b5c9) [#15658](https://github.com/NVIDIA/TensorRT-LLM/pull/15658)
  [TRTLLMINF-126][infra] Generate timeout result when the tests all pass in the rerun step (#15658)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-06** [`4f1881d838`](https://github.com/NVIDIA/TensorRT-LLM/commit/4f1881d838) [#15968](https://github.com/NVIDIA/TensorRT-LLM/pull/15968)
  [None][infra] Waive 5 failed cases for main in post-merge 2823 (#15968)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`9727b20ff8`](https://github.com/NVIDIA/TensorRT-LLM/commit/9727b20ff8) [#15874](https://github.com/NVIDIA/TensorRT-LLM/pull/15874)
  [None][infra] Coerce null CBTS PR diffs to empty string (#15874)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/scripts/cbts/main.py`_
- **2026-07-06** [`a4ed524c2e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a4ed524c2e) [#15967](https://github.com/NVIDIA/TensorRT-LLM/pull/15967)
  [None][infra] Waive 50 failed cases for main in post-merge 2822 (#15967)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`3b5ce7cdf9`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b5ce7cdf9) [#15962](https://github.com/NVIDIA/TensorRT-LLM/pull/15962)
  [None][test] Waive 1 failed cases for main in QA CI (#15962)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`1728261f91`](https://github.com/NVIDIA/TensorRT-LLM/commit/1728261f91) [#15960](https://github.com/NVIDIA/TensorRT-LLM/pull/15960)
  [None][infra] Waive 11 failed cases for main in post-merge 2822 (#15960)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`90f90bea91`](https://github.com/NVIDIA/TensorRT-LLM/commit/90f90bea91) [#15770](https://github.com/NVIDIA/TensorRT-LLM/pull/15770)
  [None][infra] Fix KeyError for test names with spaces in generate_rerun_tests_list (#15770)
  _Files: `jenkins/scripts/test_rerun.py`_
- **2026-07-06** [`56aca69ecf`](https://github.com/NVIDIA/TensorRT-LLM/commit/56aca69ecf) [#15959](https://github.com/NVIDIA/TensorRT-LLM/pull/15959)
  [None][test] Remove 72 closed-bug waive entries for main (#15959)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`1ef55adad9`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ef55adad9)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`_
- **2026-07-06** [`16430fd3e7`](https://github.com/NVIDIA/TensorRT-LLM/commit/16430fd3e7) [#15946](https://github.com/NVIDIA/TensorRT-LLM/pull/15946)
  [None][infra] Waive 1 failed cases for main in pre-merge 46289 (#15946)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-05** [`7974a3e14d`](https://github.com/NVIDIA/TensorRT-LLM/commit/7974a3e14d) [#15949](https://github.com/NVIDIA/TensorRT-LLM/pull/15949)
  [None][infra] Waive 1 failed cases for main in pre-merge 46352 (#15949)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-05** [`844cc890f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/844cc890f0) [#15854](https://github.com/NVIDIA/TensorRT-LLM/pull/15854)
  [https://nvbugs/6401921][fix] Stabilize single-GPU Wan2.2 LPIPS test (#15854)
  _Files: `tensorrt_llm/media/encoding.py`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/ltx2_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/visual_gen_lpips_golden_media.zip`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/wan21_t2v_lpips_golden_video.json` _+3 more__
- **2026-07-05** [`5992258818`](https://github.com/NVIDIA/TensorRT-LLM/commit/5992258818) [#15948](https://github.com/NVIDIA/TensorRT-LLM/pull/15948)
  [None][ci] Use x86 image for daemon host in Slurm jobs everywhere (#15948)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-05** [`fbf102348a`](https://github.com/NVIDIA/TensorRT-LLM/commit/fbf102348a) [#15943](https://github.com/NVIDIA/TensorRT-LLM/pull/15943)
  [None][infra] Ensure Slurm cleanup runs after interruptions (#15943)
  _Files: `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy`, `jenkins/L0_Test.groovy`_
- **2026-07-05** [`5adff5530c`](https://github.com/NVIDIA/TensorRT-LLM/commit/5adff5530c) [#15942](https://github.com/NVIDIA/TensorRT-LLM/pull/15942)
  [None][ci] Use x86 daemon host in Slurm jobs everywhere (#15942)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-07-04** [`086af6f1d7`](https://github.com/NVIDIA/TensorRT-LLM/commit/086af6f1d7) [#15930](https://github.com/NVIDIA/TensorRT-LLM/pull/15930)
  [None][test] Waive 1 failed cases for main in QA CI (#15930)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`1abcc63892`](https://github.com/NVIDIA/TensorRT-LLM/commit/1abcc63892) [#15914](https://github.com/NVIDIA/TensorRT-LLM/pull/15914)
  [None][infra] Waive 12 failed cases for main in post-merge 2816 (#15914)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`ca9c439cde`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca9c439cde) [#15814](https://github.com/NVIDIA/TensorRT-LLM/pull/15814)
  [TRTLLM-13947][test] Retire Triton backend TRT workflow QA tests (#15814)
  _Files: `tests/integration/defs/triton_server/build_engines.py`, `tests/integration/defs/triton_server/rcca/bug_4323566/inflight_batcher_llm_client_with_end_id.py`, `tests/integration/defs/triton_server/test_triton_llm.py`, `tests/integration/defs/triton_server/test_triton_memleak.py` _+5 more__
- **2026-07-03** [`7f2804ea47`](https://github.com/NVIDIA/TensorRT-LLM/commit/7f2804ea47) [#15904](https://github.com/NVIDIA/TensorRT-LLM/pull/15904)
  [https://nvbugs/6410963][chore] Waive a failed test in Pre-merge (#15904)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`8888dc3c14`](https://github.com/NVIDIA/TensorRT-LLM/commit/8888dc3c14) [#15901](https://github.com/NVIDIA/TensorRT-LLM/pull/15901)
  [None][infra] Waive 2 failed cases for main in pre-merge 45969 (#15901)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`8ced0a3bee`](https://github.com/NVIDIA/TensorRT-LLM/commit/8ced0a3bee) [#15902](https://github.com/NVIDIA/TensorRT-LLM/pull/15902)
  [None][test] Waive 4 failed cases for main in QA CI (#15902)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`a6e0a5d00e`](https://github.com/NVIDIA/TensorRT-LLM/commit/a6e0a5d00e) [#15898](https://github.com/NVIDIA/TensorRT-LLM/pull/15898)
  [None][infra] Waive 2 failed cases for main in pre-merge 45992 (#15898)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`c186721ecf`](https://github.com/NVIDIA/TensorRT-LLM/commit/c186721ecf) [#15894](https://github.com/NVIDIA/TensorRT-LLM/pull/15894)
  [None][infra] Waive 1 failed cases for main in pre-merge 45992 (#15894)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`f4a359fe40`](https://github.com/NVIDIA/TensorRT-LLM/commit/f4a359fe40) [#15891](https://github.com/NVIDIA/TensorRT-LLM/pull/15891)
  [None][infra] Waive 1 failed cases for main in pre-merge 45955 (#15891)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`4605402110`](https://github.com/NVIDIA/TensorRT-LLM/commit/4605402110) [#15870](https://github.com/NVIDIA/TensorRT-LLM/pull/15870)
  [None][infra] Waive 2 failed cases for main in post-merge 2815 (#15870)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`dc02d584e9`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc02d584e9) [#15867](https://github.com/NVIDIA/TensorRT-LLM/pull/15867)
  [None][test] Waive 9 failed cases for main in QA CI (#15867)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`b155a51615`](https://github.com/NVIDIA/TensorRT-LLM/commit/b155a51615) [#15749](https://github.com/NVIDIA/TensorRT-LLM/pull/15749)
  [TRTLLMINF-152][infra] Waive tests that have too many logs in system-out (#15749)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`ccf319fa25`](https://github.com/NVIDIA/TensorRT-LLM/commit/ccf319fa25)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-07-02** [`41d2200fe3`](https://github.com/NVIDIA/TensorRT-LLM/commit/41d2200fe3) [#15396](https://github.com/NVIDIA/TensorRT-LLM/pull/15396)
  [TRTLLM-12823][ci] Drop duplicate test (#15396)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml`, `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-07-02** [`db2c8a0d34`](https://github.com/NVIDIA/TensorRT-LLM/commit/db2c8a0d34) [#15827](https://github.com/NVIDIA/TensorRT-LLM/pull/15827)
  [https://nvbugs/6342840][infra] Un-waive 37 mtp perf-sanity cases (18 fixed by #15797 + 19 for CI recheck) (#15827)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`3d78a6acca`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d78a6acca) [#15862](https://github.com/NVIDIA/TensorRT-LLM/pull/15862)
  [None][infra] Waive 1 failed cases for main in pre-merge 45748 (#15862)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`920a50a2ac`](https://github.com/NVIDIA/TensorRT-LLM/commit/920a50a2ac) [#15850](https://github.com/NVIDIA/TensorRT-LLM/pull/15850)
  [None][chore] Waive failing allreduce tests (#15850)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`35b981db8f`](https://github.com/NVIDIA/TensorRT-LLM/commit/35b981db8f) [#15847](https://github.com/NVIDIA/TensorRT-LLM/pull/15847)
  [None][infra] Waive 1 failed cases for main in pre-merge 45709 (#15847)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`3b3716aab8`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b3716aab8) [#15845](https://github.com/NVIDIA/TensorRT-LLM/pull/15845)
  [None][infra] Waive 1 failed cases for main in pre-merge 45709 (#15845)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`f691a9eee9`](https://github.com/NVIDIA/TensorRT-LLM/commit/f691a9eee9) [#15843](https://github.com/NVIDIA/TensorRT-LLM/pull/15843)
  [None][infra] Waive 1 failed cases for main in pre-merge 45709 (#15843)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`d567f924b7`](https://github.com/NVIDIA/TensorRT-LLM/commit/d567f924b7) [#15694](https://github.com/NVIDIA/TensorRT-LLM/pull/15694)
  [None][infra] Upgrade NIXL to v1.3.0 (#15694)
  _Files: `docker/common/install_nixl.sh`, `jenkins/current_image_tags.properties`, `requirements-dev.txt`_
- **2026-07-01** [`3e5a7f99d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e5a7f99d8) [#15825](https://github.com/NVIDIA/TensorRT-LLM/pull/15825)
  [None][infra] Waive 10 failed cases for main in post-merge 2814 (#15825)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`e63e783fcb`](https://github.com/NVIDIA/TensorRT-LLM/commit/e63e783fcb) [#15643](https://github.com/NVIDIA/TensorRT-LLM/pull/15643)
  [None][feat] add CI-enforced stability gate for trtllm-serve CLI options (#15643)
  _Files: `tensorrt_llm/commands/_serve_stability.py`, `tensorrt_llm/commands/serve.py`, `tests/unittest/api_stability/references/trtllm_serve_cli.yaml`, `tests/unittest/api_stability/test_serve_cli.py` _+1 more__
- **2026-07-01** [`c026619ad2`](https://github.com/NVIDIA/TensorRT-LLM/commit/c026619ad2) [#15811](https://github.com/NVIDIA/TensorRT-LLM/pull/15811)
  [None][test] Waive 1 failed cases for main in post-merge (#15811)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`9a26938784`](https://github.com/NVIDIA/TensorRT-LLM/commit/9a26938784) [#15769](https://github.com/NVIDIA/TensorRT-LLM/pull/15769)
  [https://nvbugs/6196614][infra] Upgrade aiperf to 0.8.0 (#15769)
  _Files: `requirements-dev.txt`_
- **2026-06-30** [`3f3362022f`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f3362022f) [#15778](https://github.com/NVIDIA/TensorRT-LLM/pull/15778)
  [None][test] waive tests (#15778)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`539ee226c4`](https://github.com/NVIDIA/TensorRT-LLM/commit/539ee226c4) [#15779](https://github.com/NVIDIA/TensorRT-LLM/pull/15779)
  [None][infra] Waive 5 failed cases for main in pre-merge 45198 (#15779)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`a811318a59`](https://github.com/NVIDIA/TensorRT-LLM/commit/a811318a59) [#15774](https://github.com/NVIDIA/TensorRT-LLM/pull/15774)
  [None][test] Waive 8 failed cases for main in post-merge (#15774)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`3689eb2c9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3689eb2c9c) [#15701](https://github.com/NVIDIA/TensorRT-LLM/pull/15701)
  [None][test] remove two model tests from test list (#15701)
  _Files: `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/qa/llm_function_rtx6k.txt`, `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`9390bf85ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/9390bf85ec) [#15764](https://github.com/NVIDIA/TensorRT-LLM/pull/15764)
  [None][test] Waive hang issues (#15764)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`2ed55d88cc`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ed55d88cc) [#15733](https://github.com/NVIDIA/TensorRT-LLM/pull/15733)
  [None][test] Waive 8 failed cases for main in QA CI (#15733)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`833ddd2a59`](https://github.com/NVIDIA/TensorRT-LLM/commit/833ddd2a59) [#15713](https://github.com/NVIDIA/TensorRT-LLM/pull/15713)
  [None][ci] Disable home mount for sbatch L0 tests (#15713)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-06-29** [`b326ce011b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b326ce011b) [#15719](https://github.com/NVIDIA/TensorRT-LLM/pull/15719)
  [None][test] Waive 1 failed cases for main in QA CI (#15719)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`fdbb8108f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/fdbb8108f3) [#15721](https://github.com/NVIDIA/TensorRT-LLM/pull/15721)
  [None][test] Waive 4 failed cases for main in post-merge (#15721)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`fde8e0aab8`](https://github.com/NVIDIA/TensorRT-LLM/commit/fde8e0aab8) [#15644](https://github.com/NVIDIA/TensorRT-LLM/pull/15644)
  [None][feat] add CI-enforced stability gate for trtllm-serve HTTP schema (#15644)
  _Files: `tests/unittest/api_stability/references/trtllm_serve_api.yaml`, `tests/unittest/api_stability/test_serve_api.py`_
- **2026-06-29** [`0bba015066`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bba015066) [#15705](https://github.com/NVIDIA/TensorRT-LLM/pull/15705)
  [None][infra] Waive 5 failed cases for main in post-merge 2811 (#15705)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`47333fa193`](https://github.com/NVIDIA/TensorRT-LLM/commit/47333fa193) [#15686](https://github.com/NVIDIA/TensorRT-LLM/pull/15686)
  [None][test] Waive 4 failed cases for main in QA CI (#15686)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`33c7717a9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/33c7717a9c) [#15667](https://github.com/NVIDIA/TensorRT-LLM/pull/15667)
  [None][test] Waive 2 failed cases for main in QA CI (#15667)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`f5002e93f4`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5002e93f4) [#15700](https://github.com/NVIDIA/TensorRT-LLM/pull/15700)
  [None][infra] Waive 9 failed cases for main in post-merge 2810 (#15700)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`f1789c1417`](https://github.com/NVIDIA/TensorRT-LLM/commit/f1789c1417) [#15688](https://github.com/NVIDIA/TensorRT-LLM/pull/15688)
  [None][test] Waive 1 failed cases for main in QA CI (#15688)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`267b2596ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/267b2596ab) [#15678](https://github.com/NVIDIA/TensorRT-LLM/pull/15678)
  [None][test] Waive 1 failed cases for main in QA CI (#15678)
  _Files: `tests/integration/test_lists/waives.txt`_

## MoE  (25 commits)

- **2026-07-06** [`02715db02f`](https://github.com/NVIDIA/TensorRT-LLM/commit/02715db02f) [#15594](https://github.com/NVIDIA/TensorRT-LLM/pull/15594)
  [https://nvbugs/6299530][fix] Capture Qwen3.5 GDN for piecewise CUDA … (#15594)
  _Files: `tensorrt_llm/_torch/compilation/piecewise_optimizer.py`, `tensorrt_llm/_torch/compilation/utils.py`, `tensorrt_llm/_torch/modules/fla/chunk.py`, `tensorrt_llm/_torch/modules/fla/chunk_o.py` _+8 more__
- **2026-07-06** [`0bfc38926c`](https://github.com/NVIDIA/TensorRT-LLM/commit/0bfc38926c) [#15451](https://github.com/NVIDIA/TensorRT-LLM/pull/15451)
  [TRTLLM-13334][fix] Add EP assertion to DenseGEMMFusedMoE (#15451)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/fused_moe_densegemm.py`_
- **2026-07-06** [`f5a1f54ec1`](https://github.com/NVIDIA/TensorRT-LLM/commit/f5a1f54ec1) [#15662](https://github.com/NVIDIA/TensorRT-LLM/pull/15662)
  [TRTLLM-13628][test] Optimize MoE comm test execution (#15662)
  _Files: `tests/unittest/_torch/modules/moe/test_moe_comm.py`_
- **2026-07-06** [`496acab85c`](https://github.com/NVIDIA/TensorRT-LLM/commit/496acab85c) [#15717](https://github.com/NVIDIA/TensorRT-LLM/pull/15717)
  [None][perf] DSv4 follow-up: sparse attention and model defaults (#15717)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.cu`, `cpp/tensorrt_llm/kernels/compressorKernels/compressorKernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/fp8_blockscale_quant_packed.cu` _+40 more__
- **2026-07-06** [`45fae3eb9f`](https://github.com/NVIDIA/TensorRT-LLM/commit/45fae3eb9f) [#14810](https://github.com/NVIDIA/TensorRT-LLM/pull/14810)
  [#14588][feat] AutoDeploy: DeepSeek-R1 optimization for low concurrency (#14810)
  _Files: `examples/auto_deploy/model_registry/configs/deepseek-r1.yaml`, `examples/auto_deploy/model_registry/configs/gemma3n_e2b_it.yaml`, `examples/auto_deploy/model_registry/models.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/__init__.py` _+20 more__
- **2026-07-04** [`21260bbc0b`](https://github.com/NVIDIA/TensorRT-LLM/commit/21260bbc0b) [#14599](https://github.com/NVIDIA/TensorRT-LLM/pull/14599)
  [TRTLLM-12500][feat] Add support for Qwen3.5 VL MoE (with the MTP fixes) (#14599)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/models/__init__.py`, `tensorrt_llm/_torch/models/checkpoints/hf/qwen3_5_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_qwen3_5.py` _+12 more__
- **2026-07-04** [`e4aba85f1b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e4aba85f1b) [#15865](https://github.com/NVIDIA/TensorRT-LLM/pull/15865)
  [https://nvbugs/6402048][test] Skip MXFP8 CUTLASS MoE with non-128-aligned per-shard intermediate (#15865)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/modules/moe/moe_test_utils.py`_
- **2026-07-04** [`5c7ef768ed`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c7ef768ed)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+18 more__
- **2026-07-03** [`a0e65c6e00`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0e65c6e00) [#15857](https://github.com/NVIDIA/TensorRT-LLM/pull/15857)
  [TRTLLM-13458][feat] Support Minimax M3 NVFP4 checkpoint (#15857)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/_torch/models/modeling_minimaxm3.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`, `tests/integration/defs/accuracy/references/gsm8k.yaml` _+3 more__
- **2026-07-03** [`e8e1ade1c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8e1ade1c6) [#15632](https://github.com/NVIDIA/TensorRT-LLM/pull/15632)
  [TRTLLM-12950][perf] DSv4 follow-up: DeepGEMM and MegaMoE (#15632)
  _Files: `cpp/tensorrt_llm/kernels/megaMoePrepareKernel.cu`, `cpp/tensorrt_llm/kernels/megaMoePrepareKernel.h`, `cpp/tensorrt_llm/thop/CMakeLists.txt`, `cpp/tensorrt_llm/thop/allreduceOp.cpp` _+22 more__
- **2026-07-03** [`0e9c8fb7cb`](https://github.com/NVIDIA/TensorRT-LLM/commit/0e9c8fb7cb) [#15714](https://github.com/NVIDIA/TensorRT-LLM/pull/15714)
  [TRTLLM-13581][test] Add moe fp4 gpu dequant and unpack optimization (#15714)
  _Files: `cpp/tensorrt_llm/kernels/quantization.cu`, `cpp/tensorrt_llm/kernels/quantization.h`, `cpp/tensorrt_llm/thop/weightOnlyQuantOp.cpp`, `tests/unittest/_torch/modules/moe/quantize_utils.py` _+1 more__
- **2026-07-03** [`dd064e7cba`](https://github.com/NVIDIA/TensorRT-LLM/commit/dd064e7cba) [#15868](https://github.com/NVIDIA/TensorRT-LLM/pull/15868)
  [None][test] reuse conftest mpi_pool_executor in MoE routing multi-GPU test (#15868)
  _Files: `tests/unittest/_torch/modules/test_moe_routing.py`_
- **2026-07-03** [`a853451e08`](https://github.com/NVIDIA/TensorRT-LLM/commit/a853451e08)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/cpp/kernels/fmha_v2/poetry.lock`, `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock` _+83 more__
- **2026-07-02** [`f12c08f550`](https://github.com/NVIDIA/TensorRT-LLM/commit/f12c08f550) [#15063](https://github.com/NVIDIA/TensorRT-LLM/pull/15063)
  [#14225][perf] AutoDeploy MTP + ADP enablement and MoE all-to-all optimization (#15063)
  _Files: `examples/auto_deploy/model_registry/configs/super_v3_mtp.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/attention_interface.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/torch_moe.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py` _+13 more__
- **2026-07-01** [`9900e122e0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9900e122e0) [#15330](https://github.com/NVIDIA/TensorRT-LLM/pull/15330)
  [None][chore] Simplify MoE lora (#15330)
  _Files: `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_kernels.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/include/moe_lora_grouped_gemm.h`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_kernels.cu`, `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_lora_pointer_expand.cu` _+19 more__
- **2026-07-01** [`9de2850422`](https://github.com/NVIDIA/TensorRT-LLM/commit/9de2850422) [#15687](https://github.com/NVIDIA/TensorRT-LLM/pull/15687)
  [TRTLLM-13458][feat] Support Minimax M3 MXFP8 checkpoint (#15687)
  _Files: `docs/source/_static/config_db.json`, `docs/source/deployment-guide/deployment-guide-for-minimax-m3-on-trtllm.md`, `examples/configs/curated/lookup.yaml`, `examples/configs/curated/minimax-m3-throughput.yaml` _+5 more__
- **2026-07-01** [`78f21d9957`](https://github.com/NVIDIA/TensorRT-LLM/commit/78f21d9957) [#15744](https://github.com/NVIDIA/TensorRT-LLM/pull/15744)
  [TRTLLM-13630][test] Reuse MPIPoolExecutor across MoE multi-GPU test cases (#15744)
  _Files: `tests/unittest/_torch/modules/moe/test_moe_module.py`_
- **2026-07-01** [`75630ee286`](https://github.com/NVIDIA/TensorRT-LLM/commit/75630ee286) [#15748](https://github.com/NVIDIA/TensorRT-LLM/pull/15748)
  [https://nvbugs/6162506][test] AutoDeploy: fix NVFP4 MoE fp4 weight scale in test + unwaives (#15748)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/auto_deploy/singlegpu/custom_ops/moe/test_trtllm_moe.py`_
- **2026-06-30** [`ef07729eac`](https://github.com/NVIDIA/TensorRT-LLM/commit/ef07729eac) [#15528](https://github.com/NVIDIA/TensorRT-LLM/pull/15528)
  [None][chore] Allow fp8 per-tensor base weights for MoE LoRA (#15528)
  _Files: `cpp/tensorrt_llm/thop/moeOp.cpp`, `tensorrt_llm/_torch/models/modeling_mixtral.py`, `tensorrt_llm/_torch/peft/lora/validation.py`, `tests/integration/defs/llmapi/test_llm_api_pytorch_moe_lora.py` _+7 more__
- **2026-06-30** [`80bca100f1`](https://github.com/NVIDIA/TensorRT-LLM/commit/80bca100f1) [#13404](https://github.com/NVIDIA/TensorRT-LLM/pull/13404)
  [TRTLLM-12200][feat] WideEP FT: add active_rank_mask to NVLink AlltoAll kernels (1a.2) (#13404)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h`, `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+2 more__
- **2026-06-30** [`7d3b2907d8`](https://github.com/NVIDIA/TensorRT-LLM/commit/7d3b2907d8) [#14786](https://github.com/NVIDIA/TensorRT-LLM/pull/14786)
  [None][feat] Sharding IR default (auto-detect) + Eagle/MTP draft sharding + qwen3_next (#14786)
  _Files: `.claude/skills/ad-sharding-ir-port/SKILL.md`, `docs/source/features/auto_deploy/advanced/expert_configurations.md`, `examples/auto_deploy/README.md`, `examples/auto_deploy/model_registry/configs/enable_legacy_sharding.yaml` _+30 more__
- **2026-06-30** [`92147d6e01`](https://github.com/NVIDIA/TensorRT-LLM/commit/92147d6e01)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock` _+49 more__
- **2026-06-30** [`96416f1abb`](https://github.com/NVIDIA/TensorRT-LLM/commit/96416f1abb) [#15525](https://github.com/NVIDIA/TensorRT-LLM/pull/15525)
  [TRTLLM-13543][feat] WideEP FT: add EPLB mask-only reconfigure (1b.1) (#15525)
  _Files: `cpp/tensorrt_llm/nanobind/runtime/moeBindings.cpp`, `cpp/tensorrt_llm/runtime/moeLoadBalancer/moeLoadBalancer.cpp`, `cpp/tensorrt_llm/runtime/moeLoadBalancer/moeLoadBalancer.h`, `cpp/tests/unit_tests/runtime/moeLoadBalancerTest.cpp` _+2 more__
- **2026-06-29** [`552f462864`](https://github.com/NVIDIA/TensorRT-LLM/commit/552f462864) [#15656](https://github.com/NVIDIA/TensorRT-LLM/pull/15656)
  [None][feat] Optimize trtllmgen moe routing (#15656)
  _Files: `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustom.cu`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingCustomPolicy.cuh`, `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/routing/RoutingKernelTopK.cuh`_
- **2026-06-29** [`28acbad14b`](https://github.com/NVIDIA/TensorRT-LLM/commit/28acbad14b)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+47 more__

## Attention  (21 commits)

- **2026-07-06** [`c45f75fcca`](https://github.com/NVIDIA/TensorRT-LLM/commit/c45f75fcca) [#15869](https://github.com/NVIDIA/TensorRT-LLM/pull/15869)
  [None][chore] Update flashinfer-python from 0.6.12 to 0.6.14 (#15869)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-07-05** [`3b08b1952e`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b08b1952e) [#15637](https://github.com/NVIDIA/TensorRT-LLM/pull/15637)
  [TRTLLM-13176][feat] Enables CUDA graph execution for PyTorch encoder-decoder models (#15637)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/fallback.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/sparse/rocket.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+12 more__
- **2026-07-04** [`98688c66fc`](https://github.com/NVIDIA/TensorRT-LLM/commit/98688c66fc) [#12262](https://github.com/NVIDIA/TensorRT-LLM/pull/12262)
  [TRTLLM-11556][feat] Expand dynamic speculation to all spec decode algorithms (#12262)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/pyexecutor/cuda_graph_runner.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py` _+12 more__
- **2026-07-04** [`1c4344c7d0`](https://github.com/NVIDIA/TensorRT-LLM/commit/1c4344c7d0) [#15754](https://github.com/NVIDIA/TensorRT-LLM/pull/15754)
  [None][perf] overlap LTX-2 v2a cross-attn comm with compute via async-Ulysses (#15754)
  _Files: `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.cu`, `cpp/tensorrt_llm/kernels/ulyssesPostUnscatterKernel.h`, `cpp/tensorrt_llm/thop/ulyssesPostUnscatterOp.cpp`, `tensorrt_llm/_torch/custom_ops/cpp_custom_ops.py` _+3 more__
- **2026-07-03** [`0b65e4fd52`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b65e4fd52) [#15633](https://github.com/NVIDIA/TensorRT-LLM/pull/15633)
  [None][feat] DSv4 follow-up: runtime KV and cache foundations (#15633)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/executor/cacheTransceiverConfig.cpp`, `cpp/tensorrt_llm/executor/executorConfig.cpp` _+69 more__
- **2026-07-03** [`0ccc7ece13`](https://github.com/NVIDIA/TensorRT-LLM/commit/0ccc7ece13) [#15746](https://github.com/NVIDIA/TensorRT-LLM/pull/15746)
  [TRTLLM-13445][test] Add SageAttention backend-routing and SAGE recip… (#15746)
  _Files: `tests/unittest/_torch/visual_gen/test_attention_integration.py`, `tests/unittest/_torch/visual_gen/test_visual_gen_args.py`_
- **2026-07-03** [`695dd1d0ea`](https://github.com/NVIDIA/TensorRT-LLM/commit/695dd1d0ea) [#15251](https://github.com/NVIDIA/TensorRT-LLM/pull/15251)
  [https://nvbugs/6095851][fix] Refresh FlashMLA metadata for draft KV cache (#15251)
  _Files: `tensorrt_llm/_torch/speculative/interface.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-03** [`fb0d68be9c`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb0d68be9c) [#15368](https://github.com/NVIDIA/TensorRT-LLM/pull/15368)
  [None][infra] Improve unit test CI coverage (#15368)
  _Files: `.pre-commit-config.yaml`, `jenkins/scripts/cbts/blocks.py`, `legacy-files.txt`, `pyproject.toml` _+31 more__
- **2026-07-03** [`0effabbd6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0effabbd6b) [#14396](https://github.com/NVIDIA/TensorRT-LLM/pull/14396)
  [None][perf] Cascade attention impl faster than MMHA 4.6x (#14396)
  _Files: `cpp/tensorrt_llm/common/attentionOp.cpp`, `cpp/tensorrt_llm/common/attentionWorkspace.h`, `cpp/tensorrt_llm/common/envUtils.cpp`, `cpp/tensorrt_llm/common/envUtils.h` _+9 more__
- **2026-07-02** [`93ad56623b`](https://github.com/NVIDIA/TensorRT-LLM/commit/93ad56623b) [#15648](https://github.com/NVIDIA/TensorRT-LLM/pull/15648)
  [TRTLLM-13685][chore] Move MLA module to separate file (#15648)
  _Files: `AGENTS.md`, `tensorrt_llm/_torch/custom_ops/__init__.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_deepseekv4.py` _+12 more__
- **2026-07-02** [`e1ea04901d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e1ea04901d) [#15625](https://github.com/NVIDIA/TensorRT-LLM/pull/15625)
  [None][perf] DSv4 follow-up: disagg routing improvements (#15625)
  _Files: `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/executor/request.cpp`, `cpp/tensorrt_llm/executor/requestImpl.h`, `cpp/tensorrt_llm/nanobind/executor/request.cpp` _+51 more__
- **2026-07-01** [`b8219bf370`](https://github.com/NVIDIA/TensorRT-LLM/commit/b8219bf370) [#15420](https://github.com/NVIDIA/TensorRT-LLM/pull/15420)
  [None][doc] add VisualGen MGMN NVL72 tech blog (#15420)
  _Files: `docs/source/blogs/media/tech_blog25_a2d_vs_ring.png`, `docs/source/blogs/media/tech_blog25_async_ulysses.png`, `docs/source/blogs/media/tech_blog25_attention2d.png`, `docs/source/blogs/media/tech_blog25_cosmos3_highlight.png` _+8 more__
- **2026-07-01** [`fb03f97e0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/fb03f97e0e) [#15786](https://github.com/NVIDIA/TensorRT-LLM/pull/15786)
  [TRTLLM-12955][fix] use get_free_port_in_ci to avoid binding to a port in use (#15786)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/visual_gen/multi_gpu/_visual_gen_dist_utils.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_attn2d_attention.py`, `tests/unittest/_torch/visual_gen/multi_gpu/test_cosmos3_transformer_parallel.py` _+19 more__
- **2026-07-01** [`790c8660c0`](https://github.com/NVIDIA/TensorRT-LLM/commit/790c8660c0) [#15574](https://github.com/NVIDIA/TensorRT-LLM/pull/15574)
  [None][feat] Support DSA cross-layer indexer top-k sharing (e.g. GLM-5.2) (#15574)
  _Files: `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`, `tensorrt_llm/_torch/modules/attention.py`, `tensorrt_llm/_torch/pyexecutor/config_utils.py`, `tensorrt_llm/llmapi/llm_args.py` _+7 more__
- **2026-07-01** [`0d10ebe25b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d10ebe25b) [#13503](https://github.com/NVIDIA/TensorRT-LLM/pull/13503)
  [TRTLLM-8997][feat] Add encoder_max_batch_size & encoder_max_num_tokens and deterministic dummy sizing (#13503)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/models/modeling_clip.py` _+30 more__
- **2026-06-30** [`a721a0861d`](https://github.com/NVIDIA/TensorRT-LLM/commit/a721a0861d) [#15383](https://github.com/NVIDIA/TensorRT-LLM/pull/15383)
  [None][feat] Handle empty-block ranks with Helix CP (#15383)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/include/tensorrt_llm/batch_manager/llmRequest.h`, `cpp/tensorrt_llm/batch_manager/cacheFormatter.cpp`, `cpp/tensorrt_llm/batch_manager/dataTransceiver.cpp` _+10 more__
- **2026-06-30** [`81290eb64d`](https://github.com/NVIDIA/TensorRT-LLM/commit/81290eb64d) [#15761](https://github.com/NVIDIA/TensorRT-LLM/pull/15761)
  [https://nvbugs/6331421][fix] Fix TRTLLM-GEN backend multiCtasKv counter clear (#15761)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`55e3bfc291`](https://github.com/NVIDIA/TensorRT-LLM/commit/55e3bfc291) [#15739](https://github.com/NVIDIA/TensorRT-LLM/pull/15739)
  [https://nvbugs/6250439][fix] Correct speculative XQA attention sinks (#15739)
  _Files: `cpp/kernels/xqa/mha.cu`, `cpp/kernels/xqa/test/refAttention.cpp`, `cpp/kernels/xqa/test/refAttention.h`, `cpp/kernels/xqa/test/test.cpp`_
- **2026-06-30** [`3a6c777d84`](https://github.com/NVIDIA/TensorRT-LLM/commit/3a6c777d84) [#15536](https://github.com/NVIDIA/TensorRT-LLM/pull/15536)
  [TRTLLM-13580][test] Add model-derived PyTorch attention backend test suite (#15536)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/attention_backend/interface.py`, `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tensorrt_llm/_torch/attention_backend/utils.py` _+8 more__
- **2026-06-30** [`c61a704900`](https://github.com/NVIDIA/TensorRT-LLM/commit/c61a704900) [#15496](https://github.com/NVIDIA/TensorRT-LLM/pull/15496)
  [https://nvbugs/6316980][fix] Added a runtime guard in FlashInferTrtllmGenAttention.is_supported using the… (#15496)
  _Files: `tensorrt_llm/_torch/attention_backend/fmha/flashinfer_trtllm_gen.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/attention_backend/test_fmha_page_index.py`_
- **2026-06-30** [`a9f5fc75b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9f5fc75b4) [#15230](https://github.com/NVIDIA/TensorRT-LLM/pull/15230)
  [https://nvbugs/6273845][fix] Fix FMHA kernels are not found for GPTOSS + SM120 (#15230)
  _Files: `cpp/kernels/fmha_v2/setup.py`, `tests/integration/test_lists/waives.txt`_

## Executor / Runtime  (19 commits)

- **2026-07-06** [`605dd00734`](https://github.com/NVIDIA/TensorRT-LLM/commit/605dd00734) [#15099](https://github.com/NVIDIA/TensorRT-LLM/pull/15099)
  [https://nvbugs/6248837][fix] Free worker GPU memory on executor shutdown (#15099)
  _Files: `tensorrt_llm/executor/worker.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`ad9866882d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ad9866882d) [#15882](https://github.com/NVIDIA/TensorRT-LLM/pull/15882)
  [https://nvbugs/6396420][fix] Restore single-node NVLS over POSIX-FD (#15882)
  _Files: `cpp/include/tensorrt_llm/runtime/ipcNvlsMemory.h`, `cpp/tensorrt_llm/common/opUtils.cpp`, `cpp/tensorrt_llm/runtime/ipcNvlsMemory.cu`, `cpp/tensorrt_llm/runtime/ncclCommunicator.cpp` _+3 more__
- **2026-07-06** [`96b73ddb8e`](https://github.com/NVIDIA/TensorRT-LLM/commit/96b73ddb8e) [#15927](https://github.com/NVIDIA/TensorRT-LLM/pull/15927)
  [https://nvbugs/6337231][fix] Unskip and fix iter-stats unit tests' fake-self predicate (#15927)
  _Files: `tests/unittest/_torch/executor/test_iter_stats_populate.py`_
- **2026-07-06** [`6c22551583`](https://github.com/NVIDIA/TensorRT-LLM/commit/6c22551583) [#15732](https://github.com/NVIDIA/TensorRT-LLM/pull/15732)
  [https://nvbugs/6384951][fix] Fix incorrect error reporting (#15732)
  _Files: `tensorrt_llm/serve/chat_utils.py`, `tests/unittest/llmapi/apps/test_chat_utils.py`_
- **2026-07-06** [`b48661b190`](https://github.com/NVIDIA/TensorRT-LLM/commit/b48661b190) [#15655](https://github.com/NVIDIA/TensorRT-LLM/pull/15655)
  [https://nvbugs/6344107][fix] Enable disagg partial reuse store for PP>1 (#15655)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_py_executor.py`_
- **2026-07-04** [`13f334619b`](https://github.com/NVIDIA/TensorRT-LLM/commit/13f334619b) [#15860](https://github.com/NVIDIA/TensorRT-LLM/pull/15860)
  [https://nvbugs/6398200][fix] Remove fixture-level params on mpi_pool_executor to avoid duplicate parametrization (#15860)
  _Files: `tests/unittest/conftest.py`_
- **2026-07-04** [`bfb048ff64`](https://github.com/NVIDIA/TensorRT-LLM/commit/bfb048ff64) [#15834](https://github.com/NVIDIA/TensorRT-LLM/pull/15834)
  [TRTLLM-14040][perf] VisualGen: Eliminate worker-server decoded media IPC by using shared-tensor handle (#15834)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/_torch/visual_gen/output.py`, `tests/unittest/visual_gen/test_executor_shared_tensor_ipc.py`_
- **2026-07-03** [`bf2ef86f9a`](https://github.com/NVIDIA/TensorRT-LLM/commit/bf2ef86f9a) [#15819](https://github.com/NVIDIA/TensorRT-LLM/pull/15819)
  [None][chore] Upgrade ray version to 2.55.1 (#15819)
  _Files: `jenkins/L0_Test.groovy`, `jenkins/scripts/slurm_install.sh`, `tensorrt_llm/executor/ray_executor.py`, `tests/integration/defs/ray_orchestrator/RL/run_rl_perf_reproduce.py` _+3 more__
- **2026-07-03** [`48fc7537ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/48fc7537ba) [#15654](https://github.com/NVIDIA/TensorRT-LLM/pull/15654)
  [https://nvbugs/6208457][fix] Pass IPC HMAC key through file descriptor (#15654)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/ipc.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/executor/worker.py` _+3 more__
- **2026-07-02** [`08d505f75d`](https://github.com/NVIDIA/TensorRT-LLM/commit/08d505f75d) [#15677](https://github.com/NVIDIA/TensorRT-LLM/pull/15677)
  [TRTLLM-13546][feat] Add error classification patterns (1c.1) (#15677)
  _Files: `tensorrt_llm/_torch/pyexecutor/error_classification.py`, `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/pyexecutor/test_error_classification.py`_
- **2026-07-02** [`d9ca6f1c3e`](https://github.com/NVIDIA/TensorRT-LLM/commit/d9ca6f1c3e) [#15750](https://github.com/NVIDIA/TensorRT-LLM/pull/15750)
  [https://nvbugs/6376948][fix] Reduce per-request attribute overhead in model_engine hot path (#15750)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`_
- **2026-07-02** [`cd2f9b02aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd2f9b02aa) [#15649](https://github.com/NVIDIA/TensorRT-LLM/pull/15649)
  [None][fix] report NCCL init timeout (#15649)
  _Files: `cpp/tensorrt_llm/runtime/ncclCommunicator.cpp`_
- **2026-07-01** [`cd66b84a04`](https://github.com/NVIDIA/TensorRT-LLM/commit/cd66b84a04) [#14384](https://github.com/NVIDIA/TensorRT-LLM/pull/14384)
  [None][perf] Eliminate torch.where host sync in multimodal fuse_input_embeds path (#14384)
  _Files: `tensorrt_llm/_torch/models/modeling_gemma3vl.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_hyperclovax.py`, `tensorrt_llm/_torch/models/modeling_kimi_k25.py` _+14 more__
- **2026-07-01** [`1927ff6bd4`](https://github.com/NVIDIA/TensorRT-LLM/commit/1927ff6bd4) [#15612](https://github.com/NVIDIA/TensorRT-LLM/pull/15612)
  [TRTLLM-13409][feat] hard-exit on HangDetector fire + cross-rank propagation (#15612)
  _Files: `tensorrt_llm/_torch/pyexecutor/hang_detector.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/integration/test_lists/test-db/l0_sanity_check.yml`, `tests/unittest/_torch/pyexecutor/test_hang_detector_kill.py`_
- **2026-06-30** [`046d16931a`](https://github.com/NVIDIA/TensorRT-LLM/commit/046d16931a) [#15526](https://github.com/NVIDIA/TensorRT-LLM/pull/15526)
  [None][feat] Add prefix-aware scheduling config flag to support opt-out (#15526)
  _Files: `cpp/include/tensorrt_llm/batch_manager/capacityScheduler.h`, `cpp/include/tensorrt_llm/executor/executor.h`, `cpp/tensorrt_llm/batch_manager/capacityScheduler.cpp`, `cpp/tensorrt_llm/batch_manager/trtEncoderModel.cpp` _+21 more__
- **2026-06-30** [`e53e2e867a`](https://github.com/NVIDIA/TensorRT-LLM/commit/e53e2e867a) [#15631](https://github.com/NVIDIA/TensorRT-LLM/pull/15631)
  [TRTLLM-12622][feat] Reland: Add native post-processing hook to trtllm-serve (#15631)
  _Files: `docs/source/features/post-processor-hook.md`, `docs/source/index.rst`, `tensorrt_llm/_torch/auto_deploy/llm.py`, `tensorrt_llm/commands/serve.py` _+16 more__
- **2026-06-30** [`287465ac88`](https://github.com/NVIDIA/TensorRT-LLM/commit/287465ac88) [#15117](https://github.com/NVIDIA/TensorRT-LLM/pull/15117)
  [None][feat] Cosmos3 reasoner only support (#15117)
  _Files: `.github/CODEOWNERS`, `docs/source/commands/trtllm-serve/trtllm-serve.rst`, `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/configs/__init__.py` _+15 more__
- **2026-06-29** [`cc3e41ef38`](https://github.com/NVIDIA/TensorRT-LLM/commit/cc3e41ef38) [#13590](https://github.com/NVIDIA/TensorRT-LLM/pull/13590)
  [None][feat] Bind NUMA-aware CPU affinity in visual_gen workers (#13590)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/executor/base_worker.py`, `tensorrt_llm/executor/ray_gpu_worker.py`, `tensorrt_llm/llmapi/utils.py`_
- **2026-06-29** [`d913524adf`](https://github.com/NVIDIA/TensorRT-LLM/commit/d913524adf) [#14246](https://github.com/NVIDIA/TensorRT-LLM/pull/14246)
  [TRTLLM-12751][feat] visual-gen /metrics iteration stats producer (#14246)
  _Files: `tensorrt_llm/_torch/visual_gen/executor.py`, `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/visual_gen/visual_gen.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+2 more__

## Quantization  (11 commits)

- **2026-07-06** [`398e3e75ef`](https://github.com/NVIDIA/TensorRT-LLM/commit/398e3e75ef) [#15970](https://github.com/NVIDIA/TensorRT-LLM/pull/15970)
  [None][test] Increase timeout for Kimi-K2.5 disaggregated nvfp4 test (#15970)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-07-06** [`b52f6073df`](https://github.com/NVIDIA/TensorRT-LLM/commit/b52f6073df) [#15660](https://github.com/NVIDIA/TensorRT-LLM/pull/15660)
  [None][fix] Fix marlin_nvfp4_template.h compilation error (#15660)
  _Files: `cpp/tensorrt_llm/kernels/marlin/marlin_nvfp4_template.h`_
- **2026-07-05** [`995b23a50d`](https://github.com/NVIDIA/TensorRT-LLM/commit/995b23a50d)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/chatglm-6b/poetry.lock`, `security_scanning/examples/models/contrib/chatglm2-6b/poetry.lock` _+16 more__
- **2026-07-03** [`b1ea26ce3b`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1ea26ce3b) [#15470](https://github.com/NVIDIA/TensorRT-LLM/pull/15470)
  [None][feat] Qwen-Image: load pre-quantized ModelOpt NVFP4/FP8 checkpoints (#15470)
  _Files: `docs/source/models/visual-generation.md`, `tensorrt_llm/_torch/visual_gen/models/qwen_image/transformer_qwen_image.py`, `tests/unittest/_torch/visual_gen/test_qwen_image_registry.py`_
- **2026-07-02** [`9ff00c869a`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ff00c869a) [#15718](https://github.com/NVIDIA/TensorRT-LLM/pull/15718)
  [None][fix] handle rank-3 Fp4 and non-contiguous Ulysses shard in LTX-2 NVFP4 fused paths (#15718)
  _Files: `tensorrt_llm/_torch/modules/gated_mlp.py`, `tensorrt_llm/_torch/modules/mlp.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py`, `tensorrt_llm/_torch/visual_gen/utils.py` _+2 more__
- **2026-07-02** [`281acfdf7a`](https://github.com/NVIDIA/TensorRT-LLM/commit/281acfdf7a) [#15767](https://github.com/NVIDIA/TensorRT-LLM/pull/15767)
  [TRTLLM-13782][doc] Remove legacy TensorRT docs and add migration guide (#15767)
  _Files: `docs/source/commands/trtllm-build.rst`, `docs/source/conf.py`, `docs/source/index.rst`, `docs/source/legacy/advanced/gpt-runtime.md` _+27 more__
- **2026-07-01** [`8252540fb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/8252540fb4)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/docs/pyproject.toml`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+48 more__
- **2026-07-01** [`d41d09103f`](https://github.com/NVIDIA/TensorRT-LLM/commit/d41d09103f) [#15415](https://github.com/NVIDIA/TensorRT-LLM/pull/15415)
  [None][fix] compressed-tensors fp8: resolve config group by name and flatten per-channel weight_scale (#15415)
  _Files: `tensorrt_llm/_torch/modules/linear.py`, `tensorrt_llm/models/quant_config_utils.py`, `tests/unittest/models/test_quant_config_utils.py`_
- **2026-06-30** [`63e3dcf800`](https://github.com/NVIDIA/TensorRT-LLM/commit/63e3dcf800) [#15561](https://github.com/NVIDIA/TensorRT-LLM/pull/15561)
  [https://nvbugs/6336747][ci] Unwaive nemotron nvfp4 E2E test (#15561)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`6656400198`](https://github.com/NVIDIA/TensorRT-LLM/commit/6656400198) [#15599](https://github.com/NVIDIA/TensorRT-LLM/pull/15599)
  [None][fix] Honor Qwen Image quant ignore list (#15599)
  _Files: `tensorrt_llm/_torch/visual_gen/models/qwen_image/transformer_qwen_image.py`, `tests/unittest/_torch/visual_gen/test_qwen_image_registry.py`_
- **2026-06-29** [`70c5e430c8`](https://github.com/NVIDIA/TensorRT-LLM/commit/70c5e430c8) [#15659](https://github.com/NVIDIA/TensorRT-LLM/pull/15659)
  [None][fix] GLM-5.1 NVFP4 fallback to AR-Norm fusion for unquantized dense layers (#15659)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`_

## Models  (11 commits)

- **2026-07-06** [`ca708a1f71`](https://github.com/NVIDIA/TensorRT-LLM/commit/ca708a1f71) [#15957](https://github.com/NVIDIA/TensorRT-LLM/pull/15957)
  [https://nvbugs/6401925][fix] Unwaive DeepSeek V4 compressor corner-case test (#15957)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-06** [`b420e72266`](https://github.com/NVIDIA/TensorRT-LLM/commit/b420e72266) [#15547](https://github.com/NVIDIA/TensorRT-LLM/pull/15547)
  [None][fix] Pass dtype to AllReduce ctor to enable MNNVL all-reduce fo… (#15547)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_next.py`_
- **2026-07-04** [`c50ac2a0f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/c50ac2a0f7) [#15768](https://github.com/NVIDIA/TensorRT-LLM/pull/15768)
  [None][feat] Add Gemma 4 12B Unified (encoder-free multimodal) support (#15768)
  _Files: `docs/source/models/supported-models.md`, `tensorrt_llm/_torch/configs/__init__.py`, `tensorrt_llm/_torch/configs/gemma4_unified.py`, `tensorrt_llm/_torch/models/__init__.py` _+6 more__
- **2026-07-03** [`3b23a9f188`](https://github.com/NVIDIA/TensorRT-LLM/commit/3b23a9f188) [#15783](https://github.com/NVIDIA/TensorRT-LLM/pull/15783)
  [NVBUG-6280721][fix] Unwaive DeepSeek-V3.2 FP4 MTP perf-sanity test (#15783)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`98d9d18582`](https://github.com/NVIDIA/TensorRT-LLM/commit/98d9d18582) [#15826](https://github.com/NVIDIA/TensorRT-LLM/pull/15826)
  [https://nvbugs/5955773][test] Unwaive test_no_kv_cache_reuse for DeepSeekV3Lite (#15826)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`f397bb0026`](https://github.com/NVIDIA/TensorRT-LLM/commit/f397bb0026) [#15573](https://github.com/NVIDIA/TensorRT-LLM/pull/15573)
  [None][feat] Support update weight for nemotron-h (#15573)
  _Files: `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_h_weight_mapper.py`, `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py` _+2 more__
- **2026-07-01** [`066a201eee`](https://github.com/NVIDIA/TensorRT-LLM/commit/066a201eee)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/grok/poetry.lock`, `security_scanning/examples/models/core/gemma/poetry.lock`, `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json` _+1 more__
- **2026-06-30** [`7b1ddcca42`](https://github.com/NVIDIA/TensorRT-LLM/commit/7b1ddcca42) [#15751](https://github.com/NVIDIA/TensorRT-LLM/pull/15751)
  [None][feat] Add 'kimi_k2.5_fp4' to TRUST_REMOTE_CODE_MODELS in performance tests (#15751)
  _Files: `tests/integration/defs/perf/test_perf.py`_
- **2026-06-29** [`e9016273e8`](https://github.com/NVIDIA/TensorRT-LLM/commit/e9016273e8) [#15600](https://github.com/NVIDIA/TensorRT-LLM/pull/15600)
  [https://nvbugs/6287834][chore] Unwaive GPT-OSS disagg perf sanity case (#15600)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-29** [`863bc4ede9`](https://github.com/NVIDIA/TensorRT-LLM/commit/863bc4ede9) [#15564](https://github.com/NVIDIA/TensorRT-LLM/pull/15564)
  [None][test] Enable single-GPU LPIPS CI protection for VisualGen models (#15564)
  _Files: `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_t2i_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/cosmos3_nano_t2v_lpips_golden_video.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/flux1_lpips_golden.json`, `tests/integration/defs/examples/visual_gen/golden/visual_gen_lpips/flux2_lpips_golden.json` _+8 more__
- **2026-06-29** [`798989ab79`](https://github.com/NVIDIA/TensorRT-LLM/commit/798989ab79) [#15646](https://github.com/NVIDIA/TensorRT-LLM/pull/15646)
  [None][chore] Decrease the qwen3.5 ci test time (#15646)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`_

## Torch Path (_torch)  (10 commits)

- **2026-07-06** [`7023aeac4a`](https://github.com/NVIDIA/TensorRT-LLM/commit/7023aeac4a) [#15555](https://github.com/NVIDIA/TensorRT-LLM/pull/15555)
  [TRTLLM-13584][feat] add Wan VAE backend (#15555)
  _Files: `tensorrt_llm/_torch/visual_gen/models/wan/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan.py`, `tensorrt_llm/_torch/visual_gen/models/wan/pipeline_wan_i2v.py`, `tensorrt_llm/_torch/visual_gen/models/wan/vae_loader.py` _+3 more__
- **2026-07-06** [`1ae65a64ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/1ae65a64ab) [#15937](https://github.com/NVIDIA/TensorRT-LLM/pull/15937)
  [TRTLLM-13973][fix] Restrict MiniMax M3 dense SDPA backends (#15937)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm3.py`_
- **2026-07-03** [`8fc918bf0e`](https://github.com/NVIDIA/TensorRT-LLM/commit/8fc918bf0e) [#15745](https://github.com/NVIDIA/TensorRT-LLM/pull/15745)
  [TRTLLM-13446][test] Add FLUX infer() num_images_per_prompt forwardin… (#15745)
  _Files: `tests/integration/test_lists/test-db/l0_a10.yml`, `tests/unittest/_torch/visual_gen/test_flux_infer.py`_
- **2026-07-02** [`f50ca53dae`](https://github.com/NVIDIA/TensorRT-LLM/commit/f50ca53dae) [#14827](https://github.com/NVIDIA/TensorRT-LLM/pull/14827)
  [TRTLLM-13120][feat] Cosmos3 Audio Output Support (#14827)
  _Files: `examples/visual_gen/configs/cosmos3-nano-1gpu.yaml`, `examples/visual_gen/configs/cosmos3-super-4gpu.yaml`, `examples/visual_gen/models/cosmos3/README.md`, `examples/visual_gen/models/cosmos3/cosmos3.py` _+17 more__
- **2026-07-02** [`2ffab8d0ec`](https://github.com/NVIDIA/TensorRT-LLM/commit/2ffab8d0ec) [#15220](https://github.com/NVIDIA/TensorRT-LLM/pull/15220)
  [NVBUG-6266259][fix] Fix userbuffers prologue patterns (#15220)
  _Files: `tensorrt_llm/_torch/compilation/patterns/ar_residual_norm.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`23c835d3aa`](https://github.com/NVIDIA/TensorRT-LLM/commit/23c835d3aa) [#15603](https://github.com/NVIDIA/TensorRT-LLM/pull/15603)
  [None][feat] VisualGen: enable CUDA graph capture with torch.compile (#15603)
  _Files: `tensorrt_llm/_torch/visual_gen/pipeline.py`, `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`70b09920f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/70b09920f3) [#15225](https://github.com/NVIDIA/TensorRT-LLM/pull/15225)
  [None][docs] Add VisualGen engineering criteria (#15225)
  _Files: `AGENTS.md`, `tensorrt_llm/_torch/visual_gen/ENGINEERING_CRITERIA.md`_
- **2026-06-29** [`c4b9fcb772`](https://github.com/NVIDIA/TensorRT-LLM/commit/c4b9fcb772) [#15615](https://github.com/NVIDIA/TensorRT-LLM/pull/15615)
  [TRTLLM-13613][test] Trim duplicated and dead multimodal accuracy tests from pre-merge CI (#15615)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_l40s.yml`_
- **2026-06-29** [`f2160af48d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f2160af48d) [#15670](https://github.com/NVIDIA/TensorRT-LLM/pull/15670)
  [None][chore] split unittest/_torch/visual_gen (#15670)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-06-29** [`b02b6b4642`](https://github.com/NVIDIA/TensorRT-LLM/commit/b02b6b4642) [#15626](https://github.com/NVIDIA/TensorRT-LLM/pull/15626)
  [None][perf] DSv4 follow-up: autotuner updates (#15626)
  _Files: `tensorrt_llm/_torch/autotuner.py`, `tensorrt_llm/_torch/custom_ops/torch_custom_ops.py`, `tensorrt_llm/_torch/modules/mhc/mhc_cuda.py`, `tests/unittest/_torch/misc/test_autotuner.py` _+1 more__

## Disaggregation / KV  (8 commits)

- **2026-07-06** [`ceae332fe6`](https://github.com/NVIDIA/TensorRT-LLM/commit/ceae332fe6) [#15879](https://github.com/NVIDIA/TensorRT-LLM/pull/15879)
  [https://nvbugs/6384622][fix] increase free_mem_frac for failed perf test (#15879)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb200_deepseek-r1-fp4_128k8k_con128_ctx1_pp8_gen1_dep16_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-07-06** [`0071389094`](https://github.com/NVIDIA/TensorRT-LLM/commit/0071389094) [#15917](https://github.com/NVIDIA/TensorRT-LLM/pull/15917)
  [https://nvbugs/6405665][test] Disable block reuse for KV cache comparison (#15917)
  _Files: `tests/integration/defs/kv_cache/test_kv_cache_v2_scheduler.py`, `tests/integration/test_lists/waives.txt`_
- **2026-07-02** [`507411240c`](https://github.com/NVIDIA/TensorRT-LLM/commit/507411240c) [#15617](https://github.com/NVIDIA/TensorRT-LLM/pull/15617)
  [None][test] Add Kimi-K2.5 disaggregated GSM8K accuracy test (#15617)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`, `tests/integration/defs/accuracy/test_disaggregated_serving.py`, `tests/integration/test_lists/qa/llm_function_core.txt`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`_
- **2026-07-01** [`50ea42affc`](https://github.com/NVIDIA/TensorRT-LLM/commit/50ea42affc) [#15800](https://github.com/NVIDIA/TensorRT-LLM/pull/15800)
  [https://nvbugs/6266302][test] Unwaive test_disaggregated_llama_context_capacity (#15800)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-07-01** [`3196872e2a`](https://github.com/NVIDIA/TensorRT-LLM/commit/3196872e2a) [#14933](https://github.com/NVIDIA/TensorRT-LLM/pull/14933)
  [TRTLLM-13168][feat] test best ucx env for cache transceiver (#14933)
  _Files: `examples/disaggregated/slurm/cache_transceiver_test/README.md`, `examples/disaggregated/slurm/cache_transceiver_test/config.yaml`, `examples/disaggregated/slurm/cache_transceiver_test/launch.slurm`, `examples/disaggregated/slurm/cache_transceiver_test/report.py` _+5 more__
- **2026-06-30** [`7a0db61dcd`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a0db61dcd) [#13511](https://github.com/NVIDIA/TensorRT-LLM/pull/13511)
  [None][perf] set ncclConfig graphUsageMode=1 on communicator init (#13511)
  _Files: `cpp/tensorrt_llm/common/opUtils.cpp`, `docs/source/features/disagg-serving.md`, `docs/source/legacy/advanced/disaggregated-service.md`_
- **2026-06-30** [`e6046df86b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6046df86b) [#12490](https://github.com/NVIDIA/TensorRT-LLM/pull/12490)
  [None][feat] kv cache manager v1 use fabric memory to enable mnnvl transfer for kv cache transfer in disaggregated serving (#12490)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/baseTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.h` _+8 more__
- **2026-06-29** [`c9b6518c8a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c9b6518c8a) [#15431](https://github.com/NVIDIA/TensorRT-LLM/pull/15431)
  [None][feat] Parallelize host KV cache pool prefault and add THP control (#15431)
  _Files: `tensorrt_llm/runtime/kv_cache_manager_v2/_utils.py`_

## Other  (7 commits)

- **2026-07-06** [`2c6116012e`](https://github.com/NVIDIA/TensorRT-LLM/commit/2c6116012e) [#15925](https://github.com/NVIDIA/TensorRT-LLM/pull/15925)
  [https://nvbugs/6341070][fix] Fix scaffolding MajorityVoteController output handling (#15925)
  _Files: `tensorrt_llm/scaffolding/controller.py`, `tests/unittest/scaffolding/test_scaffolding.py`, `tests/unittest/scaffolding/test_worker.py`_
- **2026-07-06** [`7340eac7f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/7340eac7f7) [#15954](https://github.com/NVIDIA/TensorRT-LLM/pull/15954)
  [None][fix] Ignore valid Faroese code in codespell (#15954)
  _Files: `triton_backend/all_models/whisper/whisper_bls/1/tokenizer.py`_
- **2026-07-06** [`1519f7f341`](https://github.com/NVIDIA/TensorRT-LLM/commit/1519f7f341) [#15781](https://github.com/NVIDIA/TensorRT-LLM/pull/15781)
  [https://nvbugs/6385256][fix] Guard at both layers — add len>0 checks in get_request_num_tokens, return []… (#15781)
  _Files: `tensorrt_llm/serve/openai_disagg_service.py`, `tensorrt_llm/serve/router.py`_
- **2026-07-02** [`0d433e0bc6`](https://github.com/NVIDIA/TensorRT-LLM/commit/0d433e0bc6) [#15812](https://github.com/NVIDIA/TensorRT-LLM/pull/15812)
  [https://nvbugs/6385283][fix] Add empty/absent-content guard in the "message" and "reasoning" branches that… (#15812)
  _Files: `tensorrt_llm/serve/responses_utils.py`_
- **2026-07-02** [`7704d30143`](https://github.com/NVIDIA/TensorRT-LLM/commit/7704d30143) [#15813](https://github.com/NVIDIA/TensorRT-LLM/pull/15813)
  [https://nvbugs/6385673][fix] Add `isinstance` guards for `parameters`, `properties`, and the per-parameter… (#15813)
  _Files: `tensorrt_llm/serve/tool_parser/minimax_m2_parser.py`, `tensorrt_llm/serve/tool_parser/minimax_m3_parser.py`_
- **2026-06-30** [`93fa1e0483`](https://github.com/NVIDIA/TensorRT-LLM/commit/93fa1e0483) [#15534](https://github.com/NVIDIA/TensorRT-LLM/pull/15534)
  [https://nvbugs/6150288][fix] Use persistent per-stream workspace in cublas_mm for CUDA-graph safety (#15534)
  _Files: `cpp/tensorrt_llm/thop/cublasScaledMM.cpp`_
- **2026-06-29** [`20e0e915e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/20e0e915e1) [#15663](https://github.com/NVIDIA/TensorRT-LLM/pull/15663)
  [None][test] record per-case hostname in perf result CSV (#15663)
  _Files: `tests/integration/defs/perf/utils.py`_

## Speculative Decoding  (6 commits)

- **2026-07-06** [`4c5f3b06d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/4c5f3b06d2) [#14990](https://github.com/NVIDIA/TensorRT-LLM/pull/14990)
  [None][test] Add gpt-oss-120b eagle3 accuracy test (#14990)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_spark_func.yml`_
- **2026-07-06** [`c960dd1e4e`](https://github.com/NVIDIA/TensorRT-LLM/commit/c960dd1e4e) [#15722](https://github.com/NVIDIA/TensorRT-LLM/pull/15722)
  [None][fix] Remove unreachable model path from MTPDraftModel (#15722)
  _Files: `tensorrt_llm/_torch/models/modeling_speculative.py`_
- **2026-07-05** [`973c497483`](https://github.com/NVIDIA/TensorRT-LLM/commit/973c497483) [#15796](https://github.com/NVIDIA/TensorRT-LLM/pull/15796)
  [https://nvbugs/6378901][fix] Defer speculative D2H sync-check hooks until after LLM warmup (#15796)
  _Files: `tensorrt_llm/_utils.py`, `tensorrt_llm/commands/serve.py`, `tests/integration/defs/common.py`, `tests/integration/test_lists/waives.txt` _+1 more__
- **2026-07-03** [`edf63e8185`](https://github.com/NVIDIA/TensorRT-LLM/commit/edf63e8185) [#15842](https://github.com/NVIDIA/TensorRT-LLM/pull/15842)
  [https://nvbugs/6394425][fix] Added _is_effective_dynamic_tree() helper in utils.py that returns True only… (#15842)
  _Files: `tensorrt_llm/_torch/speculative/utils.py`_
- **2026-07-01** [`dc1b4fdd72`](https://github.com/NVIDIA/TensorRT-LLM/commit/dc1b4fdd72) [#15797](https://github.com/NVIDIA/TensorRT-LLM/pull/15797)
  [https://nvbugs/6342840][fix] Add spec_metadata=None kwarg to SpecWorkerBase._apply_force_accepted_tokens… (#15797)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`, `tensorrt_llm/_torch/speculative/eagle3_dynamic_tree.py`, `tensorrt_llm/_torch/speculative/interface.py`, `tensorrt_llm/_torch/speculative/mtp.py`_
- **2026-06-29** [`e31bcf9dab`](https://github.com/NVIDIA/TensorRT-LLM/commit/e31bcf9dab) [#15098](https://github.com/NVIDIA/TensorRT-LLM/pull/15098)
  [TRTLLM-13319][fix] fix output distribution correctness for Eagle3 dynamic-tree rejection sampling (#15098)
  _Files: `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.cu`, `cpp/tensorrt_llm/kernels/speculativeDecoding/dynamicTreeKernels.h`, `cpp/tensorrt_llm/thop/dynamicTreeOp.cpp`, `tensorrt_llm/_torch/compilation/utils.py` _+5 more__

## Docs / Examples  (3 commits)

- **2026-07-02** [`e5a05b25be`](https://github.com/NVIDIA/TensorRT-LLM/commit/e5a05b25be) [#15763](https://github.com/NVIDIA/TensorRT-LLM/pull/15763)
  [TRTLLM-13781][chore] Remove legacy TensorRT examples (#15763)
- **2026-07-02** [`c81fa33915`](https://github.com/NVIDIA/TensorRT-LLM/commit/c81fa33915) [#15858](https://github.com/NVIDIA/TensorRT-LLM/pull/15858)
  [None][doc] add NVL72 video generation blog to README (#15858)
  _Files: `README.md`_
- **2026-06-30** [`19b674e091`](https://github.com/NVIDIA/TensorRT-LLM/commit/19b674e091) [#15742](https://github.com/NVIDIA/TensorRT-LLM/pull/15742)
  [None][chore] Bump version to 1.3.0rc21 (#15742)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_

## AutoDeploy  (3 commits)

- **2026-07-01** [`4cfcc64dad`](https://github.com/NVIDIA/TensorRT-LLM/commit/4cfcc64dad) [#15418](https://github.com/NVIDIA/TensorRT-LLM/pull/15418)
  [None][fix] Add AutoDeploy post-merge stages (#15418)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/waives.txt`_
- **2026-06-30** [`ff387a754f`](https://github.com/NVIDIA/TensorRT-LLM/commit/ff387a754f) [#15530](https://github.com/NVIDIA/TensorRT-LLM/pull/15530)
  [None][chore] Autodeploy disable the pipeline cache by default (#15530)
  _Files: `tensorrt_llm/_torch/auto_deploy/config/default.yaml`_
- **2026-06-29** [`a3026c9596`](https://github.com/NVIDIA/TensorRT-LLM/commit/a3026c9596) [#15675](https://github.com/NVIDIA/TensorRT-LLM/pull/15675)
  [None][test] AutoDeploy: Fix standalone linear simple on B200 (#15675)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/linear/linear.py`, `tests/unittest/auto_deploy/standalone/test_standalone_package.py`_

## Perf  (1 commits)

- **2026-06-30** [`2a3e2fd96b`](https://github.com/NVIDIA/TensorRT-LLM/commit/2a3e2fd96b) [#15558](https://github.com/NVIDIA/TensorRT-LLM/pull/15558)
  [https://nvbugs/6266306][fix] Fix testing harness (#15558)
  _Files: `tests/integration/defs/kv_cache/test_prefix_aware_scheduling.py`, `tests/integration/test_lists/waives.txt`_

## LoRA  (1 commits)

- **2026-06-29** [`8d9c890e50`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d9c890e50) [#14984](https://github.com/NVIDIA/TensorRT-LLM/pull/14984)
  [None][feat] Cache LTX2 merged LoRA weight (#14984)
  _Files: `tensorrt_llm/_torch/visual_gen/models/ltx2/pipeline_ltx2_two_stages.py`, `tests/integration/defs/examples/visual_gen/test_visual_gen.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/unittest/_torch/visual_gen/test_ltx2_pipeline.py`_

---
_Generated 2026-07-06 12:15 UTC_