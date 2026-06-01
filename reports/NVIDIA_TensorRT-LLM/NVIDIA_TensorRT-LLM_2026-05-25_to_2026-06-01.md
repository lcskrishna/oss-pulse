# NVIDIA/TensorRT-LLM — Weekly Change Report
**Period:** 2026-05-25 → 2026-06-01  |  **Total commits:** 170

## ✨ New Features This Week

- **2026-06-01** [#14453](https://github.com/NVIDIA/TensorRT-LLM/pull/14453) — [None][feat] Refactor DWDP from CUDA IPC to CUDA VMM + MNNVL composite VA (#14453)
- **2026-06-01** [#14436](https://github.com/NVIDIA/TensorRT-LLM/pull/14436) — [None][feat] Upgrade NIXL to v1.0.1 and UCX to 1.21 (#14436)
- **2026-06-01** [#13972](https://github.com/NVIDIA/TensorRT-LLM/pull/13972) — [TRTLLM-12596][feat] Support simple logprob format (#13972)
- **2026-06-01** [#14775](https://github.com/NVIDIA/TensorRT-LLM/pull/14775) — [TRTLLM-12288][feat] Support Nemotron-H nvfp4 ckpt on Hopper (#14775)
- **2026-06-01** [#14730](https://github.com/NVIDIA/TensorRT-LLM/pull/14730) — [None][feat] Tune mamba config by env variables (#14730)
- **2026-06-01** [#14632](https://github.com/NVIDIA/TensorRT-LLM/pull/14632) — [TRTLLM-13015][feat] drop complex visual_gen CLI example scripts (#14632)
- **2026-06-01** [#14661](https://github.com/NVIDIA/TensorRT-LLM/pull/14661) — [None][infra] Update new .test_durations (#14661)
- **2026-05-31** [#14438](https://github.com/NVIDIA/TensorRT-LLM/pull/14438) — [None][test] Add TLLM_SPEC_DECODE_FORCE_NUM_ACCEPTED_TOKENS in Spec Decoding Perf Test (#14438)
- **2026-05-30** [#13614](https://github.com/NVIDIA/TensorRT-LLM/pull/13614) — [TRTLLM-11408][feat] Add VisualGen TP Support (#13614)
- **2026-05-30** [#13926](https://github.com/NVIDIA/TensorRT-LLM/pull/13926) — [TRTLLM-12440][feat] Add GMS-only weight sharing support (#13926)
- _…and 30 more_

## 🔴 ROCm / AMD Spotlight

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#14663](https://github.com/NVIDIA/TensorRT-LLM/issues/14663) | Consider using pre-built Flash Attention kernels via `kernels` | Customized kernels | 2026-05-28 |
| [#14502](https://github.com/NVIDIA/TensorRT-LLM/issues/14502) | [llmapi] NemotronV3ReasoningParser returns empty content when enable_t | LLM API, Pytorch | 2026-05-26 |
| [#13777](https://github.com/NVIDIA/TensorRT-LLM/issues/13777) | [Bug]: Memory leak: Qwen3 30B A3B pytorch backend | bug, Memory, Pytorch | 2026-05-14 |
| [#14100](https://github.com/NVIDIA/TensorRT-LLM/issues/14100) | [Bug] trtllm-serve /v1/chat/completions: audio_url with data: URI base | bug, Multimodal | 2026-05-14 |
| [#10663](https://github.com/NVIDIA/TensorRT-LLM/issues/10663) | [Bug]: Exceptions in PyTorch workflow worker processes lead to hanging | bug, Investigating, Speculative Decoding, Pytorch | 2026-05-13 |
| [#13318](https://github.com/NVIDIA/TensorRT-LLM/issues/13318) | [Bug]: Scheduler deadlock on main + #12976 + #13029: AssertionError to | bug, KV-Cache Management, Pytorch | 2026-04-22 |
| [#4910](https://github.com/NVIDIA/TensorRT-LLM/issues/4910) | CUDA error CUBLAS_STATUS_EXECUTION_FAILED when launching Qwen2.5-VL-72 | bug, triaged, Scale-out, Model optimization, Multimodal | 2026-03-30 |
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
| CI / Infra | 41 |
| Attention | 27 |
| MoE | 21 |
| Executor / Runtime | 21 |
| Disaggregation / KV | 11 |
| Torch Path (_torch) | 9 |
| Quantization | 9 |
| Models | 9 |
| Other | 7 |
| AutoDeploy | 7 |
| Docs / Examples | 5 |
| Speculative Decoding | 2 |
| LoRA | 1 |

## CI / Infra  (41 commits)

- **2026-06-01** [`d2fd17b03c`](https://github.com/NVIDIA/TensorRT-LLM/commit/d2fd17b03c) [#14559](https://github.com/NVIDIA/TensorRT-LLM/pull/14559)
  [TRTLLM-12971][infra] Fix parse classname logic in timeout result (#14559)
  _Files: `jenkins/scripts/generate_timeout_xml.py`_
- **2026-06-01** [`0b96e3a3b4`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b96e3a3b4) [#14802](https://github.com/NVIDIA/TensorRT-LLM/pull/14802)
  [None][infra] Waive 12 failed cases for main in post-merge 2749 (#14802)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-06-01** [`35cce74734`](https://github.com/NVIDIA/TensorRT-LLM/commit/35cce74734) [#14809](https://github.com/NVIDIA/TensorRT-LLM/pull/14809)
  [None][test] Update precision of previous device step time (#14809)
  _Files: `tests/integration/defs/perf/test_perf_sanity.py`_
- **2026-06-01** [`6b36b0e9f7`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b36b0e9f7)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/ray_orchestrator/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`, `security_scanning/pyproject.toml`_
- **2026-06-01** [`9ed1669593`](https://github.com/NVIDIA/TensorRT-LLM/commit/9ed1669593) [#14661](https://github.com/NVIDIA/TensorRT-LLM/pull/14661)
  [None][infra] Update new .test_durations (#14661)
  _Files: `jenkins/L0_Test.groovy`, `tests/integration/defs/.test_durations`_
- **2026-05-31** [`0fb9a36d3d`](https://github.com/NVIDIA/TensorRT-LLM/commit/0fb9a36d3d) [#14756](https://github.com/NVIDIA/TensorRT-LLM/pull/14756)
  [https://nvbugs/6165866][infra] Waive 1 failed cases for main in pre-merge 40081 - Fix prefix (#14756)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-31** [`46bbdf540e`](https://github.com/NVIDIA/TensorRT-LLM/commit/46bbdf540e)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/contrib/grok/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock`_
- **2026-05-30** [`255a54bb8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/255a54bb8b) [#14788](https://github.com/NVIDIA/TensorRT-LLM/pull/14788)
  [None][chore] Waive failing multi-gpu test (#14788)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-30** [`c27da7553c`](https://github.com/NVIDIA/TensorRT-LLM/commit/c27da7553c) [#14776](https://github.com/NVIDIA/TensorRT-LLM/pull/14776)
  [None][infra] Waive 1 failed cases for main in pre-merge 40562 (#14776)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-30** [`15bb7915c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/15bb7915c5) [#14737](https://github.com/NVIDIA/TensorRT-LLM/pull/14737)
  [None][infra] Waive 2 failed cases for main in post-merge 2741 (#14737)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-29** [`74d7c3acbb`](https://github.com/NVIDIA/TensorRT-LLM/commit/74d7c3acbb) [#14757](https://github.com/NVIDIA/TensorRT-LLM/pull/14757)
  [None][infra] revert #13607 (#14757)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy` _+3 more__
- **2026-05-29** [`cf3c1d96a9`](https://github.com/NVIDIA/TensorRT-LLM/commit/cf3c1d96a9) [#14718](https://github.com/NVIDIA/TensorRT-LLM/pull/14718)
  [None][infra] Fix cbts tokenmacro b64 (#14718)
  _Files: `jenkins/L0_MergeRequest.groovy`, `jenkins/L0_Test.groovy`, `jenkins/scripts/cbts/README.md`_
- **2026-05-29** [`fed47f1fb1`](https://github.com/NVIDIA/TensorRT-LLM/commit/fed47f1fb1) [#13607](https://github.com/NVIDIA/TensorRT-LLM/pull/13607)
  [None][infra] Generate json with cmake fetched contents in build stage (#13607)
  _Files: `docker/Dockerfile.multi`, `docker/Makefile`, `jenkins/Build.groovy`, `jenkins/BuildDockerImage.groovy` _+3 more__
- **2026-05-29** [`e35f0f492b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e35f0f492b) [#12885](https://github.com/NVIDIA/TensorRT-LLM/pull/12885)
  [None][test] Enable test for kv_cache_manager_v2 for A10 (#12885)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`da9db3a952`](https://github.com/NVIDIA/TensorRT-LLM/commit/da9db3a952) [#14653](https://github.com/NVIDIA/TensorRT-LLM/pull/14653)
  [https://nvbugs/6165866][infra] Waive 1 failed cases for main in pre-merge 40081 (#14653)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`776bebcd58`](https://github.com/NVIDIA/TensorRT-LLM/commit/776bebcd58) [#14587](https://github.com/NVIDIA/TensorRT-LLM/pull/14587)
  [TRTLLMINF-67][infra] use pre-configured idle GPU exemption (#14587)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-28** [`e173446942`](https://github.com/NVIDIA/TensorRT-LLM/commit/e173446942) [#14594](https://github.com/NVIDIA/TensorRT-LLM/pull/14594)
  [None][fix] Exclude post-merge stages from CBTS force-keep filters (#14594)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-28** [`89bcd802bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/89bcd802bf) [#14688](https://github.com/NVIDIA/TensorRT-LLM/pull/14688)
  [None][infra] Waive 1 failed cases for main in post-merge 2740 (#14688)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`e73d06808d`](https://github.com/NVIDIA/TensorRT-LLM/commit/e73d06808d) [#14116](https://github.com/NVIDIA/TensorRT-LLM/pull/14116)
  [https://nvbugs/6160085][fix] At `tensorrt_llm/tokenizer/tokenizer.py` import time, re-export `bytes_to_unicod (#14116)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`f391155e5a`](https://github.com/NVIDIA/TensorRT-LLM/commit/f391155e5a) [#14087](https://github.com/NVIDIA/TensorRT-LLM/pull/14087)
  [None][chore] Add test lists with multi-gpu test to CI multi-gpu test trigger files (#14087)
  _Files: `jenkins/L0_MergeRequest.groovy`_
- **2026-05-28** [`1b8c739efc`](https://github.com/NVIDIA/TensorRT-LLM/commit/1b8c739efc) [#14662](https://github.com/NVIDIA/TensorRT-LLM/pull/14662)
  [None][infra] Update blossom-ci allowlist: add nv-anants, guqiqi, jonghyunchoe, belgarten-nv (#14662)
  _Files: `.github/workflows/blossom-ci.yml`_
- **2026-05-28** [`fd5fa6169d`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd5fa6169d) [#14625](https://github.com/NVIDIA/TensorRT-LLM/pull/14625)
  [None][infra] Fix hang when generating report (#14625)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-27** [`09f59589f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/09f59589f2) [#14498](https://github.com/NVIDIA/TensorRT-LLM/pull/14498)
  [None][test] Waive 7 failed cases for main in QA CI (#14498)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`a0cdb8ce6a`](https://github.com/NVIDIA/TensorRT-LLM/commit/a0cdb8ce6a) [#14615](https://github.com/NVIDIA/TensorRT-LLM/pull/14615)
  [None][infra] Waive 8 failed cases for main in post-merge 2738 (#14615)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`28718e5ba7`](https://github.com/NVIDIA/TensorRT-LLM/commit/28718e5ba7) [#14581](https://github.com/NVIDIA/TensorRT-LLM/pull/14581)
  [TRTLLMINF-106][infra] Use B300 frontend platforms (#14581)
  _Files: `jenkins/L0_Test.groovy`_
- **2026-05-26** [`a23207f9ba`](https://github.com/NVIDIA/TensorRT-LLM/commit/a23207f9ba) [#14328](https://github.com/NVIDIA/TensorRT-LLM/pull/14328)
  [None][chore] Unwaive `test_cp_tp_broadcast_object` (#14328)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`ba25b6afae`](https://github.com/NVIDIA/TensorRT-LLM/commit/ba25b6afae) [#14537](https://github.com/NVIDIA/TensorRT-LLM/pull/14537)
  [https://nvbugs/6168859][fix] move tinygemm PDL release after reduction (#14537)
  _Files: `cpp/tensorrt_llm/kernels/tinygemm2/tinygemm2_kernel.cuh`, `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`0c44d2dafe`](https://github.com/NVIDIA/TensorRT-LLM/commit/0c44d2dafe) [#14393](https://github.com/NVIDIA/TensorRT-LLM/pull/14393)
  [None][refactor] Update model path definitions in test_perf.py and clean up waives.txt (#14393)
  _Files: `tests/integration/defs/perf/_model_paths.py`, `tests/integration/defs/perf/test_perf.py`, `tests/integration/defs/perf/test_perf_sanity.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`17cf970f2f`](https://github.com/NVIDIA/TensorRT-LLM/commit/17cf970f2f) [#14557](https://github.com/NVIDIA/TensorRT-LLM/pull/14557)
  [None][chore] Add disagg local one-step run script for CI submit (#14557)
  _Files: `.gitignore`, `jenkins/scripts/perf/README.md`, `jenkins/scripts/perf/local/configs/example.conf`, `jenkins/scripts/perf/local/run_disagg.sh`_
- **2026-05-26** [`526d7ee675`](https://github.com/NVIDIA/TensorRT-LLM/commit/526d7ee675) [#14542](https://github.com/NVIDIA/TensorRT-LLM/pull/14542)
  [None][infra] Waive 1 failed cases for main in post-merge 2735 (#14542)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`b1d23c7435`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1d23c7435) [#14526](https://github.com/NVIDIA/TensorRT-LLM/pull/14526)
  [None][infra] Waive 2 failed cases for main in post-merge 2734 (#14526)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`68d3db1423`](https://github.com/NVIDIA/TensorRT-LLM/commit/68d3db1423) [#14523](https://github.com/NVIDIA/TensorRT-LLM/pull/14523)
  [https://nvbugs/6184914][test] Unwaive related tests (#14523)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`e2497f0253`](https://github.com/NVIDIA/TensorRT-LLM/commit/e2497f0253) [#14440](https://github.com/NVIDIA/TensorRT-LLM/pull/14440)
  [https://nvbugs/6114610][test] unwaive disagg tests fixed by UCX_TLS setter (#14440)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`31826c1296`](https://github.com/NVIDIA/TensorRT-LLM/commit/31826c1296) [#14090](https://github.com/NVIDIA/TensorRT-LLM/pull/14090)
  [https://nvbugs/6162328][fix] Add a tiny compat shim in `load_hf_tokenizer` that, when `bytes_to_unicode` is m (#14090)
  _Files: `tensorrt_llm/tokenizer/tokenizer.py`, `tests/integration/test_lists/waives.txt`_
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

## Attention  (27 commits)

- **2026-06-01** [`f402178281`](https://github.com/NVIDIA/TensorRT-LLM/commit/f402178281) [#14459](https://github.com/NVIDIA/TensorRT-LLM/pull/14459)
  [https://nvbugs/6117811][fix] Fix XQA IMA for invalid pages with sliding window (#14459)
  _Files: `3rdparty/fetch_content.json`, `cpp/kernels/xqa/CMakeLists.txt`, `cpp/kernels/xqa/ldgsts.cuh`, `cpp/kernels/xqa/mha.cu` _+4 more__
- **2026-05-30** [`5f106dfabd`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f106dfabd) [#13614](https://github.com/NVIDIA/TensorRT-LLM/pull/13614)
  [TRTLLM-11408][feat] Add VisualGen TP Support (#13614)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/visual_gen_flux.py`, `examples/visual_gen/visual_gen_ltx2.py` _+19 more__
- **2026-05-29** [`6f2055f7c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6f2055f7c2) [#13719](https://github.com/NVIDIA/TensorRT-LLM/pull/13719)
  [https://nvbugs/6136737][fix] Propagate external SWA window to FMHA kernel in V2 KV cache (#13719)
  _Files: `tensorrt_llm/_torch/attention_backend/trtllm.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-29** [`59de15d21a`](https://github.com/NVIDIA/TensorRT-LLM/commit/59de15d21a) [#12544](https://github.com/NVIDIA/TensorRT-LLM/pull/12544)
  [None][feat] Enable NVFP4 KV cache support in trtllm-gen attention (#12544)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h`, `cpp/tensorrt_llm/thop/trtllmGenFusedOps.h` _+3 more__
- **2026-05-29** [`29971b4c1d`](https://github.com/NVIDIA/TensorRT-LLM/commit/29971b4c1d) [#14481](https://github.com/NVIDIA/TensorRT-LLM/pull/14481)
  [TRTLLM-12901][fix] cap per-rank max_num_active_requests by max_num_tokens under attention DP (#14481)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/_torch/pyexecutor/request_utils.py`, `tests/unittest/_torch/executor/test_request_utils.py`_
- **2026-05-29** [`27b4e565db`](https://github.com/NVIDIA/TensorRT-LLM/commit/27b4e565db) [#14713](https://github.com/NVIDIA/TensorRT-LLM/pull/14713)
  [https://nvbugs/6156233][test] unwaive GPT-OSS dflash test since bug has been closed as fix unknown (#14713)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-29** [`208ed9b5df`](https://github.com/NVIDIA/TensorRT-LLM/commit/208ed9b5df) [#14634](https://github.com/NVIDIA/TensorRT-LLM/pull/14634)
  [TRTLLM-12982][perf] remove sync after FlashInfer attention plan() (#14634)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`_
- **2026-05-29** [`0a192053d9`](https://github.com/NVIDIA/TensorRT-LLM/commit/0a192053d9) [#14569](https://github.com/NVIDIA/TensorRT-LLM/pull/14569)
  [None][refactor] Flatten thop.attention sequence kwargs + rename rotary_embedding_* to rope_* (#14569)
  _Files: `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h`, `tensorrt_llm/_torch/attention_backend/trtllm.py` _+4 more__
- **2026-05-29** [`b1dfd3094c`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1dfd3094c) [#14044](https://github.com/NVIDIA/TensorRT-LLM/pull/14044)
  [TRTLLM-12653][feat] LTX-2 Ulysses cross-attention for v2a with audio padding (#14044)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/flash_attn4.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/vanilla.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/ltx2_core/transformer_args.py`, `tensorrt_llm/_torch/visual_gen/models/ltx2/transformer_ltx2.py` _+5 more__
- **2026-05-29** [`1bb1a0206b`](https://github.com/NVIDIA/TensorRT-LLM/commit/1bb1a0206b) [#13721](https://github.com/NVIDIA/TensorRT-LLM/pull/13721)
  [TRTLLM-12436][feat] visual_gen: add CuTe DSL attention via exported binaries (#13721)
  _Files: `.gitattributes`, `.gitignore`, `docs/source/models/visual-generation.md`, `setup.py` _+78 more__
- **2026-05-28** [`f6ba936179`](https://github.com/NVIDIA/TensorRT-LLM/commit/f6ba936179) [#14635](https://github.com/NVIDIA/TensorRT-LLM/pull/14635)
  [TRTLLM-12982][feat] improve attention backend selection (#14635)
  _Files: `tensorrt_llm/_torch/attention_backend/utils.py`_
- **2026-05-28** [`7443f1d05f`](https://github.com/NVIDIA/TensorRT-LLM/commit/7443f1d05f) [#13498](https://github.com/NVIDIA/TensorRT-LLM/pull/13498)
  [https://nvbugs/6115036][fix] Fix NVFP4 engine size estimation and attention DP batch size in trtllm-bench (#13498)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/bench/benchmark/utils/general.py`, `tensorrt_llm/bench/build/build.py`, `tensorrt_llm/bench/build/dataclasses.py` _+1 more__
- **2026-05-28** [`5c896cd13b`](https://github.com/NVIDIA/TensorRT-LLM/commit/5c896cd13b) [#14012](https://github.com/NVIDIA/TensorRT-LLM/pull/14012)
  [TRTLLM-11410][feat] MoT World Model Support (#14012)
  _Files: `tensorrt_llm/_torch/visual_gen/attention_backend/vanilla.py`, `tensorrt_llm/_torch/visual_gen/models/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/__init__.py`, `tensorrt_llm/_torch/visual_gen/models/cosmos3/defaults.py` _+7 more__
- **2026-05-28** [`13ca44a117`](https://github.com/NVIDIA/TensorRT-LLM/commit/13ca44a117) [#13745](https://github.com/NVIDIA/TensorRT-LLM/pull/13745)
  [None][feat] Support Gemma4 multi-head_dim pools and host-side slicing to provide local view to Triton kernels for SWA (#13745)
  _Files: `cpp/include/tensorrt_llm/batch_manager/kvCacheManager.h`, `cpp/tensorrt_llm/batch_manager/cacheFormatter.cpp`, `cpp/tensorrt_llm/batch_manager/cacheTransBuffer.cpp`, `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp` _+22 more__
- **2026-05-28** [`09bad734e1`](https://github.com/NVIDIA/TensorRT-LLM/commit/09bad734e1) [#14279](https://github.com/NVIDIA/TensorRT-LLM/pull/14279)
  [None][refactor] Add derived properties for the thop.attention call site (#14279)
  _Files: `cpp/kernels/xqa/mla_sm120.cu`, `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/decoderMaskedMultiheadAttentionTemplate.h`, `cpp/tensorrt_llm/kernels/flashMLA/flash_fwd_mla_kernel.h`, `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/unfusedAttentionKernels_2_template.h` _+11 more__
- **2026-05-28** [`89c90eb603`](https://github.com/NVIDIA/TensorRT-LLM/commit/89c90eb603) [#14670](https://github.com/NVIDIA/TensorRT-LLM/pull/14670)
  [None][fix] Fix OSRB source header and provenance issues in AutoDeploy modeling code (#14670)
  _Files: `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gpt_oss.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_minimax_m2.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_nemotron_flash.py`, `tests/unittest/auto_deploy/singlegpu/models/test_minimax_m2_modeling.py`_
- **2026-05-27** [`9fa13581ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/9fa13581ab) [#13788](https://github.com/NVIDIA/TensorRT-LLM/pull/13788)
  [None][fix] make FA4 proper pip dependency (#13788)
  _Files: `requirements.txt`, `tensorrt_llm/_torch/visual_gen/attention_backend/flash_attn4.py`, `tensorrt_llm/_torch/visual_gen/attention_backend/parallel.py`, `tensorrt_llm/_torch/visual_gen/jit_kernels/__init__.py` _+39 more__
- **2026-05-27** [`86c1b0ccaf`](https://github.com/NVIDIA/TensorRT-LLM/commit/86c1b0ccaf) [#14535](https://github.com/NVIDIA/TensorRT-LLM/pull/14535)
  [https://nvbugs/6215690][fix] AutoDeploy: FlashInfer 128-byte alignment for Mamba inputs (also addresses nvbugs/6162114) (#14535)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/flashinfer_backend_mamba.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`0b16ef9d8b`](https://github.com/NVIDIA/TensorRT-LLM/commit/0b16ef9d8b) [#14607](https://github.com/NVIDIA/TensorRT-LLM/pull/14607)
  [None][chore] Update flashinfer-python from 0.6.12rc1 to 0.6.12rc2 (#14607)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-05-27** [`bb16882939`](https://github.com/NVIDIA/TensorRT-LLM/commit/bb16882939) [#14600](https://github.com/NVIDIA/TensorRT-LLM/pull/14600)
  [None][fix] Bypass FlashInfer SSD prefill to fix state dtype precision (#14600)
  _Files: `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`_
- **2026-05-27** [`6481d4caa9`](https://github.com/NVIDIA/TensorRT-LLM/commit/6481d4caa9) [#14548](https://github.com/NVIDIA/TensorRT-LLM/pull/14548)
  [None][perf] Fuse FlashInfer GDN prefill state I/O into Triton kernels (#14548)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/fla/fused_state_io.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_fused_state_io.py`_
- **2026-05-26** [`1f8312d5bf`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f8312d5bf) [#14529](https://github.com/NVIDIA/TensorRT-LLM/pull/14529)
  [TRTLLM-12949][refactor] visual_gen: unify fused QK-norm+rope dispatch (#14529)
  _Files: `benchmarks/bench_fused_dit_cross_head_qk_norm_rope.py`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.cu`, `cpp/tensorrt_llm/kernels/fusedDiTQKNormRopeKernel.h`, `cpp/tensorrt_llm/kernels/fusedDiTSplitNormKernel.cu` _+9 more__
- **2026-05-26** [`acd224175c`](https://github.com/NVIDIA/TensorRT-LLM/commit/acd224175c) [#14512](https://github.com/NVIDIA/TensorRT-LLM/pull/14512)
  [None][chore] Update flashinfer-python from 0.6.11.post1 to 0.6.12rc1 (#14512)
  _Files: `ATTRIBUTIONS-Python.md`, `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-05-26** [`28abcad55a`](https://github.com/NVIDIA/TensorRT-LLM/commit/28abcad55a) [#13644](https://github.com/NVIDIA/TensorRT-LLM/pull/13644)
  [None][perf] Integrate the flashinfer gdn prefill kernel for qwen3.5 (#13644)
  _Files: `tensorrt_llm/_torch/modules/fla/flashinfer_chunk.py`, `tensorrt_llm/_torch/modules/mamba/gdn_mixer.py`, `tests/unittest/_torch/modules/mamba/test_flashinfer_chunk_gdn.py`_
- **2026-05-25** [`fd8ae36bbe`](https://github.com/NVIDIA/TensorRT-LLM/commit/fd8ae36bbe) [#12947](https://github.com/NVIDIA/TensorRT-LLM/pull/12947)
  [None][feat] Add SkipSoftmax sparse attention support for visual generation (#12947)
  _Files: `docs/source/features/sparse-attention.md`, `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`, `tensorrt_llm/_torch/visual_gen/config.py`, `tensorrt_llm/_torch/visual_gen/modules/attention.py` _+6 more__
- **2026-05-25** [`e45a8e3156`](https://github.com/NVIDIA/TensorRT-LLM/commit/e45a8e3156) [#13428](https://github.com/NVIDIA/TensorRT-LLM/pull/13428)
  [None][feat] Add FlashInfer MLA attention backend support (#13428)
  _Files: `tensorrt_llm/_torch/attention_backend/flashinfer.py`, `tensorrt_llm/_torch/modules/attention.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+3 more__
- **2026-05-25** [`f49ac5689d`](https://github.com/NVIDIA/TensorRT-LLM/commit/f49ac5689d) [#14275](https://github.com/NVIDIA/TensorRT-LLM/pull/14275)
  [None][chore] Drop sink_token_length from PyTorch attention surface (#14275)
  _Files: `cpp/tensorrt_llm/kernels/gptKernels.h`, `cpp/tensorrt_llm/nanobind/thop/bindings.cpp`, `cpp/tensorrt_llm/thop/attentionOp.cpp`, `cpp/tensorrt_llm/thop/attentionOp.h` _+17 more__

## MoE  (21 commits)

- **2026-06-01** [`441eaae20d`](https://github.com/NVIDIA/TensorRT-LLM/commit/441eaae20d) [#14453](https://github.com/NVIDIA/TensorRT-LLM/pull/14453)
  [None][feat] Refactor DWDP from CUDA IPC to CUDA VMM + MNNVL composite VA (#14453)
  _Files: `examples/disaggregated/slurm/benchmark/disaggr_torch_dwdp.slurm`, `examples/disaggregated/slurm/benchmark/start_worker_dwdp.sh`, `examples/disaggregated/slurm/benchmark/submit_dwdp.py`, `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py` _+30 more__
- **2026-06-01** [`71a188ccd8`](https://github.com/NVIDIA/TensorRT-LLM/commit/71a188ccd8) [#14775](https://github.com/NVIDIA/TensorRT-LLM/pull/14775)
  [TRTLLM-12288][feat] Support Nemotron-H nvfp4 ckpt on Hopper (#14775)
  _Files: `tensorrt_llm/_torch/models/modeling_nemotron_h.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`, `tensorrt_llm/_torch/modules/fused_moe/quantization.py`, `tensorrt_llm/_torch/modules/fused_moe/triton_dequant_nvfp4.py` _+3 more__
- **2026-06-01** [`cde996386b`](https://github.com/NVIDIA/TensorRT-LLM/commit/cde996386b) [#14803](https://github.com/NVIDIA/TensorRT-LLM/pull/14803)
  [None][test] Update moe backend for ctx and acceptance length env (#14803)
  _Files: `tests/scripts/perf-sanity/aggregated/config_database_b200_nvl.yaml`, `tests/scripts/perf-sanity/aggregated/config_database_h200_sxm.yaml`, `tests/scripts/perf-sanity/aggregated/deepseek_r1_fp4_v2_2_nodes_blackwell.yaml`, `tests/scripts/perf-sanity/aggregated/deepseek_r1_fp4_v2_2_nodes_grace_blackwell.yaml` _+44 more__
- **2026-05-30** [`097dab1496`](https://github.com/NVIDIA/TensorRT-LLM/commit/097dab1496)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock` _+11 more__
- **2026-05-29** [`4504fd724f`](https://github.com/NVIDIA/TensorRT-LLM/commit/4504fd724f) [#14554](https://github.com/NVIDIA/TensorRT-LLM/pull/14554)
  [#13561][feat] AutoDeploy: enable MLIR elementwise fusion and trtllm_gen MoE on Nano NVFP4 (#14554)
  _Files: `examples/auto_deploy/model_registry/configs/nano_v3.yaml`, `tensorrt_llm/_torch/auto_deploy/mlir/dialect.py`_
- **2026-05-29** [`4826f6a4b5`](https://github.com/NVIDIA/TensorRT-LLM/commit/4826f6a4b5) [#13310](https://github.com/NVIDIA/TensorRT-LLM/pull/13310)
  [https://nvbugs/6084447][fix] Fix MoE DeepGEMM workspace size with attention_dp (#13310)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/moe_scheduler.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-29** [`dedd826651`](https://github.com/NVIDIA/TensorRT-LLM/commit/dedd826651)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/docs/poetry.lock`, `security_scanning/examples/apps/poetry.lock`, `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock` _+49 more__
- **2026-05-28** [`56be62529c`](https://github.com/NVIDIA/TensorRT-LLM/commit/56be62529c) [#14361](https://github.com/NVIDIA/TensorRT-LLM/pull/14361)
  [None][perf] Add AutoDeploy NVFP4 RMSNorm quant fusion (#14361)
  _Files: `tensorrt_llm/_torch/auto_deploy/config/default.yaml`, `tensorrt_llm/_torch/auto_deploy/custom_ops/distributed/trtllm_dist.py`, `tensorrt_llm/_torch/auto_deploy/custom_ops/normalization/rms_norm.py`, `tensorrt_llm/_torch/auto_deploy/transform/library/fuse_rmsnorm_quant_fp8.py` _+5 more__
- **2026-05-28** [`c0a64cf466`](https://github.com/NVIDIA/TensorRT-LLM/commit/c0a64cf466)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock`, `security_scanning/examples/models/contrib/hyperclovax/poetry.lock`, `security_scanning/examples/models/contrib/stdit/poetry.lock` _+10 more__
- **2026-05-28** [`db347a9484`](https://github.com/NVIDIA/TensorRT-LLM/commit/db347a9484) [#13888](https://github.com/NVIDIA/TensorRT-LLM/pull/13888)
  [None][feat] support non-divisible EP in MoE alltoall and slurm benchmark (#13888)
  _Files: `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/thop/moeAlltoAllOp.cpp`, `examples/disaggregated/slurm/benchmark/README.md`, `examples/disaggregated/slurm/benchmark/config.yaml` _+10 more__
- **2026-05-27** [`af74e004c9`](https://github.com/NVIDIA/TensorRT-LLM/commit/af74e004c9) [#13668](https://github.com/NVIDIA/TensorRT-LLM/pull/13668)
  [https://nvbugs/6114464][fix] Add kv_cache_config to TestQwen3VL_MOE::test_auto_dtype (#13668)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`ec067d755d`](https://github.com/NVIDIA/TensorRT-LLM/commit/ec067d755d) [#14424](https://github.com/NVIDIA/TensorRT-LLM/pull/14424)
  [https://nvbugs/6099723][fix] Gate supports_mnnvl() False on SM120/121 in _mnnvl_utils.py and add the same Mnn (#14424)
  _Files: `tensorrt_llm/_mnnvl_utils.py`, `tensorrt_llm/_torch/modules/fused_moe/communication/deep_ep_low_latency.py`_
- **2026-05-27** [`11dbd9deb4`](https://github.com/NVIDIA/TensorRT-LLM/commit/11dbd9deb4) [#14550](https://github.com/NVIDIA/TensorRT-LLM/pull/14550)
  [None][chore] Remove one-warp-per-token policy from MoE A2A kernels (#14550)
  _Files: `cpp/tensorrt_llm/common/envUtils.cpp`, `cpp/tensorrt_llm/common/envUtils.h`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.cu`, `cpp/tensorrt_llm/kernels/communicationKernels/moeAlltoAllKernels.h` _+1 more__
- **2026-05-27** [`c61705ec6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/c61705ec6b) [#14612](https://github.com/NVIDIA/TensorRT-LLM/pull/14612)
  [https://nvbugs/6175923][test] Revert gpt_oss_20b perf MoE-backend pin (#14612)
  _Files: `tests/integration/defs/perf/pytorch_model_config.py`_
- **2026-05-27** [`276ccd64f2`](https://github.com/NVIDIA/TensorRT-LLM/commit/276ccd64f2)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/auto_deploy/poetry.lock`, `security_scanning/examples/draft_target_model/poetry.lock`, `security_scanning/examples/eagle/poetry.lock`, `security_scanning/examples/llm-eval/lm-eval-harness/poetry.lock` _+46 more__
- **2026-05-27** [`5dd96d6c5f`](https://github.com/NVIDIA/TensorRT-LLM/commit/5dd96d6c5f) [#13859](https://github.com/NVIDIA/TensorRT-LLM/pull/13859)
  [None][feat] AutoDeploy push the rope buffer to later stage (#13859)
  _Files: `tensorrt_llm/_torch/auto_deploy/config/default.yaml`, `tensorrt_llm/_torch/auto_deploy/mlir/fusion/subgraph_replace.py`, `tensorrt_llm/_torch/auto_deploy/mlir/mlir_to_fx.py`, `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_deepseek.py` _+19 more__
- **2026-05-26** [`8f052f4fa9`](https://github.com/NVIDIA/TensorRT-LLM/commit/8f052f4fa9) [#13409](https://github.com/NVIDIA/TensorRT-LLM/pull/13409)
  [None][chore] Include layer_idx in MoE backend fallback warnings (#13409)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`_
- **2026-05-26** [`983541534f`](https://github.com/NVIDIA/TensorRT-LLM/commit/983541534f) [#14404](https://github.com/NVIDIA/TensorRT-LLM/pull/14404)
  [https://nvbugs/6186880][fix] In deep_ep.py, fall back to the pre-quant dispatch path when hidden_states_sf is (#14404)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/communication/deep_ep.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`63b1d8d9b2`](https://github.com/NVIDIA/TensorRT-LLM/commit/63b1d8d9b2) [#13773](https://github.com/NVIDIA/TensorRT-LLM/pull/13773)
  [None][feat] FlashInfer NVFP4 MoE backend (SM120/SM121) for Nemotron … (#13773)
  _Files: `tensorrt_llm/_torch/modules/fused_moe/MOE_DEVELOPER_GUIDE.md`, `tensorrt_llm/_torch/modules/fused_moe/__init__.py`, `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`, `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl_b12x.py` _+6 more__
- **2026-05-25** [`92c5030ff4`](https://github.com/NVIDIA/TensorRT-LLM/commit/92c5030ff4) [#13478](https://github.com/NVIDIA/TensorRT-LLM/pull/13478)
  [TRTLLM-13429][feat] Switch DeepSeek/NemotronH/Qwen3/Qwen3.5-MoE to sharding-IR canonical models (#13478)
  _Files: `.claude/skills/ad-model-onboard/SKILL.md`, `.claude/skills/ad-sharding-ir-port/SKILL.md`, `examples/auto_deploy/.gitignore`, `examples/auto_deploy/model_registry/configs/enable_sharder_ir.yaml` _+11 more__
- **2026-05-25** [`8c8765d69c`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c8765d69c) [#14507](https://github.com/NVIDIA/TensorRT-LLM/pull/14507)
  [TRTLLM-12635][feat] add bench_moe microbenchmark (#14507)
  _Files: `tests/microbenchmarks/bench_moe/BENCH_MOE_USER_GUIDE.md`, `tests/microbenchmarks/bench_moe/__init__.py`, `tests/microbenchmarks/bench_moe/__main__.py`, `tests/microbenchmarks/bench_moe/backend.py` _+21 more__

## Executor / Runtime  (21 commits)

- **2026-06-01** [`2e6f602ece`](https://github.com/NVIDIA/TensorRT-LLM/commit/2e6f602ece) [#14509](https://github.com/NVIDIA/TensorRT-LLM/pull/14509)
  [None][fix] Stabilize Mamba replay state update (#14509)
  _Files: `tensorrt_llm/_torch/modules/mamba/mamba2_mixer.py`, `tensorrt_llm/_torch/modules/mamba/replay_selective_state_update.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`, `tensorrt_llm/_torch/pyexecutor/mamba_cache_manager.py` _+1 more__
- **2026-06-01** [`3ec9e9b04c`](https://github.com/NVIDIA/TensorRT-LLM/commit/3ec9e9b04c) [#12735](https://github.com/NVIDIA/TensorRT-LLM/pull/12735)
  [https://nvbugs/6038228][fix] Propagate event loop errors to await_responses callers (#12735)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tests/unittest/_torch/executor/test_py_executor.py`, `tests/unittest/executor/test_event_loop_error_broadcast.py`_
- **2026-06-01** [`7a9c1865de`](https://github.com/NVIDIA/TensorRT-LLM/commit/7a9c1865de) [#14730](https://github.com/NVIDIA/TensorRT-LLM/pull/14730)
  [None][feat] Tune mamba config by env variables (#14730)
  _Files: `tensorrt_llm/_torch/modules/mamba/ssd_combined.py`, `tensorrt_llm/_torch/pyexecutor/_util.py`_
- **2026-06-01** [`a422420db9`](https://github.com/NVIDIA/TensorRT-LLM/commit/a422420db9) [#14782](https://github.com/NVIDIA/TensorRT-LLM/pull/14782)
  [https://nvbugs/6244695][fix] Revert Pass IPC HMAC key through file descriptor (#14782)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/unittest/executor/test_launcher_envs.py`_
- **2026-05-31** [`54259ed5d2`](https://github.com/NVIDIA/TensorRT-LLM/commit/54259ed5d2) [#14719](https://github.com/NVIDIA/TensorRT-LLM/pull/14719)
  [https://nvbugs/6196391][fix] Carryover disagg TTFT improvements (#14719)
  _Files: `cpp/tensorrt_llm/batch_manager/kvCacheManager.cpp`, `tensorrt_llm/serve/openai_server.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_core.txt` _+3 more__
- **2026-05-30** [`f20858cc05`](https://github.com/NVIDIA/TensorRT-LLM/commit/f20858cc05) [#14475](https://github.com/NVIDIA/TensorRT-LLM/pull/14475)
  [https://nvbugs/6204488][fix] Replace fixed disagg fill throttle with slow-start ramp (#14475)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tests/unittest/_torch/executor/test_benchmark_disagg.py`_
- **2026-05-30** [`4ec2942c7c`](https://github.com/NVIDIA/TensorRT-LLM/commit/4ec2942c7c) [#13926](https://github.com/NVIDIA/TensorRT-LLM/pull/13926)
  [TRTLLM-12440][feat] Add GMS-only weight sharing support (#13926)
  _Files: `tensorrt_llm/_torch/memory/__init__.py`, `tensorrt_llm/_torch/memory/gpu_memory_backend.py`, `tensorrt_llm/_torch/models/checkpoints/mx/checkpoint_loader.py`, `tensorrt_llm/_torch/pyexecutor/model_engine.py` _+8 more__
- **2026-05-30** [`1f02e96aa4`](https://github.com/NVIDIA/TensorRT-LLM/commit/1f02e96aa4) [#14370](https://github.com/NVIDIA/TensorRT-LLM/pull/14370)
  [TRTLLM-12535][chore] Refactor fast path (token ID space) preprocessing logic out to the input preprocessor methods only (#14370)
  _Files: `.claude/skills/trtllm-model-onboard-multimodal/SKILL.md`, `tensorrt_llm/_torch/models/modeling_gemma3vl.py`, `tensorrt_llm/_torch/models/modeling_gemma4mm.py`, `tensorrt_llm/_torch/models/modeling_hyperclovax.py` _+12 more__
- **2026-05-29** [`ebbbec419e`](https://github.com/NVIDIA/TensorRT-LLM/commit/ebbbec419e) [#12985](https://github.com/NVIDIA/TensorRT-LLM/pull/12985)
  [None][fix] Resolve NVML device index mismatch in get_numa_aware_cpu_affinity when CUDA_VISIBLE_DEVICES is set (#12985)
  _Files: `tensorrt_llm/llmapi/utils.py`_
- **2026-05-29** [`562d6837e6`](https://github.com/NVIDIA/TensorRT-LLM/commit/562d6837e6) [#13525](https://github.com/NVIDIA/TensorRT-LLM/pull/13525)
  [https://nvbugs/5979710][fix] Bound transfer destinations (#13525)
  _Files: `cpp/tensorrt_llm/executor/cache_transmission/agent_utils/connection.cpp`, `cpp/tensorrt_llm/executor/cache_transmission/agent_utils/connection.h`_
- **2026-05-29** [`91371ddc6b`](https://github.com/NVIDIA/TensorRT-LLM/commit/91371ddc6b) [#13527](https://github.com/NVIDIA/TensorRT-LLM/pull/13527)
  [https://nvbugs/5996024][fix] Enforce trust_remote_code flag (#13527)
  _Files: `tensorrt_llm/_torch/pyexecutor/model_engine.py`, `tensorrt_llm/_torch/pyexecutor/model_loader.py`, `tensorrt_llm/inputs/registry.py`, `tensorrt_llm/inputs/utils.py` _+6 more__
- **2026-05-29** [`c7683f2f0a`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7683f2f0a) [#14638](https://github.com/NVIDIA/TensorRT-LLM/pull/14638)
  [None][feat] add Poolside Laguna tool parser (#14638)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/serve/tool_parser/poolside_v1_parser.py`, `tensorrt_llm/serve/tool_parser/tool_parser_factory.py`, `tests/unittest/llmapi/apps/test_tool_parsers.py`_
- **2026-05-29** [`3e80e33655`](https://github.com/NVIDIA/TensorRT-LLM/commit/3e80e33655) [#14689](https://github.com/NVIDIA/TensorRT-LLM/pull/14689)
  [https://nvbugs/6045177][fix] resolve mypy error (#14689)
  _Files: `pyproject.toml`, `tensorrt_llm/_torch/pyexecutor/sampler.py`_
- **2026-05-29** [`5421ef9c11`](https://github.com/NVIDIA/TensorRT-LLM/commit/5421ef9c11) [#14665](https://github.com/NVIDIA/TensorRT-LLM/pull/14665)
  [None][feature] Add thinking token budget control (#14665)
  _Files: `tensorrt_llm/llmapi/__init__.py`, `tensorrt_llm/llmapi/llm.py`, `tensorrt_llm/llmapi/thinking_budget.py`, `tensorrt_llm/sampling_params.py` _+5 more__
- **2026-05-29** [`8c830c90f3`](https://github.com/NVIDIA/TensorRT-LLM/commit/8c830c90f3) [#14624](https://github.com/NVIDIA/TensorRT-LLM/pull/14624)
  [https://nvbugs/6221841][fix] Detect via the raw config_dict whether the user actually set a top-level rope_th (#14624)
  _Files: `tensorrt_llm/_torch/pyexecutor/config_utils.py`_
- **2026-05-29** [`a471435b35`](https://github.com/NVIDIA/TensorRT-LLM/commit/a471435b35) [#14659](https://github.com/NVIDIA/TensorRT-LLM/pull/14659)
  [https://nvbugs/6229221][fix] Add a reasoning parser for qwen3_5 (#14659)
  _Files: `tensorrt_llm/llmapi/reasoning_parser.py`_
- **2026-05-28** [`50ca49f8c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/50ca49f8c5) [#14378](https://github.com/NVIDIA/TensorRT-LLM/pull/14378)
  [https://nvbugs/5972776][fix] Pass IPC HMAC key through file descriptor (#14378)
  _Files: `tensorrt_llm/commands/serve.py`, `tensorrt_llm/executor/utils.py`, `tensorrt_llm/llmapi/trtllm-llmapi-launch`, `tests/unittest/executor/test_launcher_envs.py`_
- **2026-05-28** [`0432a81ccb`](https://github.com/NVIDIA/TensorRT-LLM/commit/0432a81ccb) [#14648](https://github.com/NVIDIA/TensorRT-LLM/pull/14648)
  [https://nvbugs/6043248][fix] Validate tensor payload size on deserialization (#14648)
  _Files: `cpp/tensorrt_llm/executor/serialization.cpp`_
- **2026-05-28** [`fe079575de`](https://github.com/NVIDIA/TensorRT-LLM/commit/fe079575de) [#14127](https://github.com/NVIDIA/TensorRT-LLM/pull/14127)
  [None][feat] Expose host/GPU per-iter time and clarify iter labeling in /metrics (#14127)
  _Files: `tensorrt_llm/_torch/pyexecutor/adp_iter_stats.py`, `tensorrt_llm/_torch/pyexecutor/py_executor.py`, `tensorrt_llm/executor/base_worker.py`, `tests/unittest/executor/test_stats_serializer.py` _+1 more__
- **2026-05-26** [`6130b2a30e`](https://github.com/NVIDIA/TensorRT-LLM/commit/6130b2a30e) [#14368](https://github.com/NVIDIA/TensorRT-LLM/pull/14368)
  [https://nvbugs/6143579][fix] Allow content: null in CustomChatCompletionMessageParam (#14368)
  _Files: `tensorrt_llm/serve/openai_protocol.py`, `tests/unittest/llmapi/apps/test_chat_utils.py`_
- **2026-05-26** [`a9c35f3c47`](https://github.com/NVIDIA/TensorRT-LLM/commit/a9c35f3c47) [#14556](https://github.com/NVIDIA/TensorRT-LLM/pull/14556)
  [TRTLLM-12968][ci] Dedup executor unit tests on H100/B200 (#14556)
  _Files: `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/test-db/l0_h100.yml`_

## Disaggregation / KV  (11 commits)

- **2026-06-01** [`2f9b85a4df`](https://github.com/NVIDIA/TensorRT-LLM/commit/2f9b85a4df) [#14436](https://github.com/NVIDIA/TensorRT-LLM/pull/14436)
  [None][feat] Upgrade NIXL to v1.0.1 and UCX to 1.21 (#14436)
  _Files: `docker/common/install_nixl.sh`, `docker/common/install_ucx.sh`, `jenkins/L0_Test.groovy`, `jenkins/current_image_tags.properties` _+3 more__
- **2026-06-01** [`70ab8fb512`](https://github.com/NVIDIA/TensorRT-LLM/commit/70ab8fb512) [#13972](https://github.com/NVIDIA/TensorRT-LLM/pull/13972)
  [TRTLLM-12596][feat] Support simple logprob format (#13972)
  _Files: `tensorrt_llm/_torch/pyexecutor/llm_request.py`, `tensorrt_llm/_torch/pyexecutor/sampler.py`, `tensorrt_llm/disaggregated_params.py`, `tensorrt_llm/executor/base_worker.py` _+10 more__
- **2026-05-30** [`32eda52a44`](https://github.com/NVIDIA/TensorRT-LLM/commit/32eda52a44) [#14664](https://github.com/NVIDIA/TensorRT-LLM/pull/14664)
  [None][test] Unwaive some Perf Tests (#14664)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/disaggregated/gb300_deepseek-r1-fp4_128k8k_con256_ctx1_pp4_gen1_dep8_eplb0_mtp1_ccb-NIXL.yaml`_
- **2026-05-28** [`e8a42a1f69`](https://github.com/NVIDIA/TensorRT-LLM/commit/e8a42a1f69) [#14161](https://github.com/NVIDIA/TensorRT-LLM/pull/14161)
  [https://nvbugs/5911594][fix] Restrict HTTP cluster storage to loopback (#14161)
  _Files: `tensorrt_llm/serve/cluster_storage.py`, `tensorrt_llm/serve/openai_disagg_server.py`, `tests/integration/defs/test_e2e.py`, `tests/integration/test_lists/qa/llm_function_multinode.txt` _+4 more__
- **2026-05-28** [`c90fe19ebc`](https://github.com/NVIDIA/TensorRT-LLM/commit/c90fe19ebc) [#14626](https://github.com/NVIDIA/TensorRT-LLM/pull/14626)
  [https://nvbugs/6094100][fix] add ucx tls env in disagg related tests (#14626)
  _Files: `tests/integration/defs/disaggregated/test_disaggregated_etcd.py`, `tests/integration/defs/disaggregated/test_disaggregated_single_gpu.py`, `tests/integration/defs/disaggregated/test_workers.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`46532472e3`](https://github.com/NVIDIA/TensorRT-LLM/commit/46532472e3) [#14206](https://github.com/NVIDIA/TensorRT-LLM/pull/14206)
  [None][chore] log KV cache utilization and context tokens per iter (#14206)
  _Files: `tensorrt_llm/_torch/pyexecutor/py_executor.py`_
- **2026-05-26** [`7142d07702`](https://github.com/NVIDIA/TensorRT-LLM/commit/7142d07702) [#14452](https://github.com/NVIDIA/TensorRT-LLM/pull/14452)
  [None][fix] Route trtllm-bench and trtllm-serve tokenizer load through TransformersTokenizer (#14452)
  _Files: `tensorrt_llm/bench/utils/data.py`, `tensorrt_llm/serve/router.py`, `tests/unittest/disaggregated/test_router.py`, `tests/unittest/others/test_bench_data.py`_
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

## Torch Path (_torch)  (9 commits)

- **2026-05-29** [`3d56a4e399`](https://github.com/NVIDIA/TensorRT-LLM/commit/3d56a4e399) [#14472](https://github.com/NVIDIA/TensorRT-LLM/pull/14472)
  [TRTLLM-10004][chore] Enable NCCL symmetric zero-copy by default (#14472)
  _Files: `tensorrt_llm/_torch/distributed/ops.py`_
- **2026-05-29** [`3f21a4828b`](https://github.com/NVIDIA/TensorRT-LLM/commit/3f21a4828b) [#14176](https://github.com/NVIDIA/TensorRT-LLM/pull/14176)
  [https://nvbugs/6162857][fix] Use generation metrics for VisualGen perf sanity (#14176)
  _Files: `tensorrt_llm/serve/openai_server.py`, `tensorrt_llm/serve/openai_video_routes.py`, `tensorrt_llm/serve/scripts/benchmark_visual_gen.py`, `tensorrt_llm/serve/visual_gen_metrics.py` _+5 more__
- **2026-05-29** [`6b126caaf2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6b126caaf2) [#14652](https://github.com/NVIDIA/TensorRT-LLM/pull/14652)
  [https://nvbugs/6194552][fix] stabilize Triton Mamba softplus (#14652)
  _Files: `tensorrt_llm/_torch/modules/mamba/softplus.py`_
- **2026-05-29** [`7bdd8357c1`](https://github.com/NVIDIA/TensorRT-LLM/commit/7bdd8357c1) [#14474](https://github.com/NVIDIA/TensorRT-LLM/pull/14474)
  [None][perf] Replace Parakeet audio encoder with native trtllm layers (#14474)
  _Files: `tensorrt_llm/_torch/models/modeling_parakeet.py`_
- **2026-05-28** [`82679b58ab`](https://github.com/NVIDIA/TensorRT-LLM/commit/82679b58ab) [#14314](https://github.com/NVIDIA/TensorRT-LLM/pull/14314)
  [TRTLLM-12762][fix] Enable multi-node TP for MiniMax-M2 (#14314)
  _Files: `tensorrt_llm/_torch/models/modeling_minimaxm2.py`_
- **2026-05-28** [`59d4369369`](https://github.com/NVIDIA/TensorRT-LLM/commit/59d4369369) [#11960](https://github.com/NVIDIA/TensorRT-LLM/pull/11960)
  [https://nvbugs/6115560][fix] catch OSError in config_file_lock for NFS compatibility (#11960)
  _Files: `tensorrt_llm/_torch/model_config.py`_
- **2026-05-27** [`8cd28ed022`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cd28ed022) [#14109](https://github.com/NVIDIA/TensorRT-LLM/pull/14109)
  [https://nvbugs/6162860][fix] Set free_gpu_memory_fraction=0.6 only when torch_compile=True for test_bfloat16_ (#14109)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`272c10148e`](https://github.com/NVIDIA/TensorRT-LLM/commit/272c10148e) [#14486](https://github.com/NVIDIA/TensorRT-LLM/pull/14486)
  [https://nvbugs/6164924][fix] Lower free_gpu_memory_fraction for Exaone tests (#14486)
  _Files: `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`92e601cd76`](https://github.com/NVIDIA/TensorRT-LLM/commit/92e601cd76) [#14580](https://github.com/NVIDIA/TensorRT-LLM/pull/14580)
  [https://nvbugs/6211185][fix] Fix failed GSM8K accuracy tests for LagunaXS on B200/GB200/B300 (#14580)
  _Files: `tensorrt_llm/_torch/models/modeling_laguna.py`, `tests/integration/test_lists/test-db/l0_b200.yml`, `tests/integration/test_lists/waives.txt`_

## Quantization  (9 commits)

- **2026-05-29** [`566c226d00`](https://github.com/NVIDIA/TensorRT-LLM/commit/566c226d00) [#14622](https://github.com/NVIDIA/TensorRT-LLM/pull/14622)
  [#14619][perf] AutoDeploy: tune Llama-3.1-8B-Instruct-FP8 TP=2/4 config and handle CG max bs when it is unset in the yaml (#14622)
  _Files: `examples/auto_deploy/model_registry/configs/llama3_1_8b.yaml`, `tensorrt_llm/_torch/auto_deploy/llm_args.py`_
- **2026-05-29** [`018c432718`](https://github.com/NVIDIA/TensorRT-LLM/commit/018c432718) [#14484](https://github.com/NVIDIA/TensorRT-LLM/pull/14484)
  [https://nvbugs/6189416][fix] Add a Blackwell-specific reference entry (extra_acc_spec=sm100_fp8, accuracy=46. (#14484)
  _Files: `tests/integration/defs/accuracy/references/mmmu.yaml`, `tests/integration/defs/accuracy/test_llm_api_pytorch_multimodal.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`e6784d834b`](https://github.com/NVIDIA/TensorRT-LLM/commit/e6784d834b) [#14691](https://github.com/NVIDIA/TensorRT-LLM/pull/14691)
  [https://nvbugs/6192201][fix] AutoDeploy: unwaive llama perf test and increase its concurrency to 256 (#14691)
  _Files: `tests/integration/test_lists/waives.txt`, `tests/scripts/perf-sanity/aggregated/llama3_1_8b_fp8_ad_hopper.yaml`_
- **2026-05-28** [`9feaa76ba0`](https://github.com/NVIDIA/TensorRT-LLM/commit/9feaa76ba0) [#14666](https://github.com/NVIDIA/TensorRT-LLM/pull/14666)
  [None][test] Unwaive fp8 blockscale baseline mtp1 (#14666)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`d636ba02c5`](https://github.com/NVIDIA/TensorRT-LLM/commit/d636ba02c5) [#14454](https://github.com/NVIDIA/TensorRT-LLM/pull/14454)
  [None][test] Update stress tests (#14454)
  _Files: `.coderabbit.yaml`, `tests/integration/defs/disaggregated/disagg_test_utils.py`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp1_gentp1_qwen3_5_4b_fp8_tllm.yaml`, `tests/integration/defs/disaggregated/test_configs/disagg_config_ctxtp2_gentp2_gptoss_tllm.yaml` _+9 more__
- **2026-05-27** [`5a5d093131`](https://github.com/NVIDIA/TensorRT-LLM/commit/5a5d093131) [#12851](https://github.com/NVIDIA/TensorRT-LLM/pull/12851)
  [None][fix] Exclude Qwen3 VL vision model from quantization (#12851)
  _Files: `tensorrt_llm/_torch/models/modeling_qwen3vl.py`_
- **2026-05-27** [`46bf87cfec`](https://github.com/NVIDIA/TensorRT-LLM/commit/46bf87cfec) [#14033](https://github.com/NVIDIA/TensorRT-LLM/pull/14033)
  [https://nvbugs/6163033][fix] Guard `q_a_proj.weight` dict access behind `nvfp4_fused_a`; update test to `chec (#14033)
  _Files: `tensorrt_llm/_torch/models/modeling_deepseekv3.py`, `tensorrt_llm/_torch/models/modeling_mistral.py`, `tests/integration/defs/accuracy/test_llm_api_pytorch.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`37079f69e5`](https://github.com/NVIDIA/TensorRT-LLM/commit/37079f69e5) [#14541](https://github.com/NVIDIA/TensorRT-LLM/pull/14541)
  [https://nvbugs/6215736][infra] Unwaive test_fp8_blockscale[throughput_mtp] (#14541)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-26** [`c7e7fc5cdc`](https://github.com/NVIDIA/TensorRT-LLM/commit/c7e7fc5cdc) [#14468](https://github.com/NVIDIA/TensorRT-LLM/pull/14468)
  [None] [refactor] Unify compressed-tensors quant config parsing (#14468)
  _Files: `tensorrt_llm/_torch/model_config.py`, `tensorrt_llm/llmapi/llm_utils.py`, `tensorrt_llm/models/quant_config_utils.py`, `tests/integration/test_lists/test-db/l0_a10.yml` _+2 more__

## Models  (9 commits)

- **2026-05-28** [`83ec591f08`](https://github.com/NVIDIA/TensorRT-LLM/commit/83ec591f08) [#14248](https://github.com/NVIDIA/TensorRT-LLM/pull/14248)
  [https://nvbugs/5800725][fix] Restore Mistral Large 3 text-only processor (#14248)
  _Files: `tensorrt_llm/_torch/models/checkpoints/mistral/config_loader.py`, `tensorrt_llm/_torch/models/modeling_mistral.py`, `tests/integration/test_lists/waives.txt`, `tests/unittest/_torch/models/checkpoints/mistral/test_config_loader.py`_
- **2026-05-28** [`1a5292091d`](https://github.com/NVIDIA/TensorRT-LLM/commit/1a5292091d) [#14375](https://github.com/NVIDIA/TensorRT-LLM/pull/14375)
  [TRTLLM-12648][test] add disagg cancellation stress-test harness skeleton (#14375)
  _Files: `tests/integration/defs/stress_test/disagg_cancel/README.md`, `tests/integration/defs/stress_test/disagg_cancel/__init__.py`, `tests/integration/defs/stress_test/disagg_cancel/configs/README.md`, `tests/integration/defs/stress_test/disagg_cancel/configs/marathon_cpp_v1_deepseek.yaml` _+4 more__
- **2026-05-27** [`80a22f733b`](https://github.com/NVIDIA/TensorRT-LLM/commit/80a22f733b) [#14596](https://github.com/NVIDIA/TensorRT-LLM/pull/14596)
  [https://nvbugs/6109750][test] Unwaive passing GPTOSS tests (#14596)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-27** [`da0359b27b`](https://github.com/NVIDIA/TensorRT-LLM/commit/da0359b27b) [#14570](https://github.com/NVIDIA/TensorRT-LLM/pull/14570)
  [https://nvbugs/6221621][test] Update trust_remote to nemotron and phi4 models (#14570)
  _Files: `tests/integration/defs/perf/test_perf.py`_
- **2026-05-26** [`13778e15d5`](https://github.com/NVIDIA/TensorRT-LLM/commit/13778e15d5)
  [None][infra] Check in most recent lock file from nightly pipeline
  _Files: `security_scanning/examples/models/core/mllama/poetry.lock`, `security_scanning/examples/serve/poetry.lock`, `security_scanning/metadata.json`, `security_scanning/poetry.lock` _+1 more__
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

## Other  (7 commits)

- **2026-06-01** [`5f5b77239a`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f5b77239a) [#14671](https://github.com/NVIDIA/TensorRT-LLM/pull/14671)
  [None][test] Update datasets path (#14671)
  _Files: `tests/integration/defs/perf/test_perf.py`_
- **2026-05-31** [`26c099f52d`](https://github.com/NVIDIA/TensorRT-LLM/commit/26c099f52d) [#14438](https://github.com/NVIDIA/TensorRT-LLM/pull/14438)
  [None][test] Add TLLM_SPEC_DECODE_FORCE_NUM_ACCEPTED_TOKENS in Spec Decoding Perf Test (#14438)
- **2026-05-29** [`8d8a259229`](https://github.com/NVIDIA/TensorRT-LLM/commit/8d8a259229) [#14732](https://github.com/NVIDIA/TensorRT-LLM/pull/14732)
  [TRTLLM-13043][chroe] add VisualGen context to AGENTS.md (#14732)
  _Files: `AGENTS.md`_
- **2026-05-28** [`e96b710f97`](https://github.com/NVIDIA/TensorRT-LLM/commit/e96b710f97) [#14577](https://github.com/NVIDIA/TensorRT-LLM/pull/14577)
  [https://nvbugs/6207749][fix] Replace the spec with `onnx>=1.21.0` in `requirements.txt`; mirror in `security_ (#14577)
  _Files: `requirements.txt`, `security_scanning/pyproject.toml`_
- **2026-05-27** [`4db70515a6`](https://github.com/NVIDIA/TensorRT-LLM/commit/4db70515a6) [#14530](https://github.com/NVIDIA/TensorRT-LLM/pull/14530)
  [None][chore] update VisualGen codeowner settings (#14530)
  _Files: `.github/CODEOWNERS`_
- **2026-05-25** [`5f4946e912`](https://github.com/NVIDIA/TensorRT-LLM/commit/5f4946e912) [#14226](https://github.com/NVIDIA/TensorRT-LLM/pull/14226)
  [https://nvbugs/6094070][fix] Skip ray-marked integration tests when --run-ray is not set (#14226)
  _Files: `tests/integration/defs/conftest.py`_
- **2026-05-25** [`72bc8ed5f0`](https://github.com/NVIDIA/TensorRT-LLM/commit/72bc8ed5f0) [#14078](https://github.com/NVIDIA/TensorRT-LLM/pull/14078)
  [https://nvbugs/6157131][fix] lower the GSM8K accuracy grade for Nano V3 (#14078)
  _Files: `tests/integration/defs/accuracy/references/gsm8k.yaml`_

## AutoDeploy  (7 commits)

- **2026-05-29** [`027eb72d85`](https://github.com/NVIDIA/TensorRT-LLM/commit/027eb72d85) [#14716](https://github.com/NVIDIA/TensorRT-LLM/pull/14716)
  [https://nvbugs/6185480][fix] autodeploy unwaive the test (#14716)
  _Files: `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`56df2009c6`](https://github.com/NVIDIA/TensorRT-LLM/commit/56df2009c6) [#14584](https://github.com/NVIDIA/TensorRT-LLM/pull/14584)
  [https://nvbugs/6187185][fix] Apply the existing `low_memory_overrides()` helper in `TestNemotronV2.test_auto_ (#14584)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`_
- **2026-05-28** [`22c79563fb`](https://github.com/NVIDIA/TensorRT-LLM/commit/22c79563fb) [#14656](https://github.com/NVIDIA/TensorRT-LLM/pull/14656)
  [https://nvbugs/6185480][fix] Autodeploy skip the GLM accuracy test for pre-hopper (#14656)
  _Files: `tests/integration/defs/accuracy/test_llm_api_autodeploy.py`_
- **2026-05-28** [`0715e15aa8`](https://github.com/NVIDIA/TensorRT-LLM/commit/0715e15aa8) [#13963](https://github.com/NVIDIA/TensorRT-LLM/pull/13963)
  [TRTLLM-13960][test] Offline equivalence test for sharding IR (#13963)
  _Files: `.claude/skills/ad-sharding-ir-port/SKILL.md`, `tests/unittest/auto_deploy/_utils_test/_sharding_ir_helpers.py`, `tests/unittest/auto_deploy/multigpu/transformations/library/conftest.py`, `tests/unittest/auto_deploy/multigpu/transformations/library/test_sharding_ir_equivalence.py`_
- **2026-05-28** [`6484b713c2`](https://github.com/NVIDIA/TensorRT-LLM/commit/6484b713c2) [#14640](https://github.com/NVIDIA/TensorRT-LLM/pull/14640)
  [https://nvbugs/6221483][fix] Revert auto_deploy _mamba_ssm_prepare_metadata to pre-#13566 state (#14640)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/mamba_backend_common.py`, `tests/integration/test_lists/waives.txt`_
- **2026-05-28** [`fc3b69e524`](https://github.com/NVIDIA/TensorRT-LLM/commit/fc3b69e524) [#14448](https://github.com/NVIDIA/TensorRT-LLM/pull/14448)
  [https://nvbugs/6185173][fix] Set mamba ssm cache to fp32 for NemotronV2 (#14448)
  _Files: `examples/auto_deploy/model_registry/configs/nemotron-nano-9b-v2.yaml`, `tests/integration/test_lists/waives.txt`_
- **2026-05-25** [`998f41855d`](https://github.com/NVIDIA/TensorRT-LLM/commit/998f41855d) [#13566](https://github.com/NVIDIA/TensorRT-LLM/pull/13566)
  [https://nvbugs/6120981][fix] Switch to cu_seqlens_to_chunk_indices_offsets_triton with total_seqlens/extra_ch (#13566)
  _Files: `tensorrt_llm/_torch/auto_deploy/custom_ops/mamba/mamba_backend_common.py`, `tensorrt_llm/_torch/modules/mamba/mamba2_metadata.py`, `tests/integration/test_lists/waives.txt`_

## Docs / Examples  (5 commits)

- **2026-06-01** [`4e12ff7b75`](https://github.com/NVIDIA/TensorRT-LLM/commit/4e12ff7b75) [#14632](https://github.com/NVIDIA/TensorRT-LLM/pull/14632)
  [TRTLLM-13015][feat] drop complex visual_gen CLI example scripts (#14632)
  _Files: `docs/source/models/visual-generation.md`, `examples/visual_gen/README.md`, `examples/visual_gen/models/wan_t2v.py`, `examples/visual_gen/visual_gen_flux.py` _+5 more__
- **2026-05-28** [`82f69a0e94`](https://github.com/NVIDIA/TensorRT-LLM/commit/82f69a0e94) [#14487](https://github.com/NVIDIA/TensorRT-LLM/pull/14487)
  [None][docs] fix incorrect auto sampler behavior description for beam search (#14487)
  _Files: `docs/source/features/sampling.md`_
- **2026-05-28** [`757f1e7320`](https://github.com/NVIDIA/TensorRT-LLM/commit/757f1e7320) [#14657](https://github.com/NVIDIA/TensorRT-LLM/pull/14657)
  [None][chore] Bump version to 1.3.0rc17 (#14657)
  _Files: `README.md`, `examples/constraints.txt`, `tensorrt_llm/version.py`_
- **2026-05-27** [`b1eb703635`](https://github.com/NVIDIA/TensorRT-LLM/commit/b1eb703635) [#14495](https://github.com/NVIDIA/TensorRT-LLM/pull/14495)
  [None][docs] Add deprecation notice to legacy support-matrix.md (#14495)
  _Files: `docs/source/legacy/reference/support-matrix.md`_
- **2026-05-27** [`021e4d8039`](https://github.com/NVIDIA/TensorRT-LLM/commit/021e4d8039) [#14621](https://github.com/NVIDIA/TensorRT-LLM/pull/14621)
  [None][doc] Add CUTLASS DSL uninstall step to installation guide (#14621)
  _Files: `docs/source/installation/installation-guide.md`_

## Speculative Decoding  (2 commits)

- **2026-05-29** [`ecb1b44992`](https://github.com/NVIDIA/TensorRT-LLM/commit/ecb1b44992) [#14735](https://github.com/NVIDIA/TensorRT-LLM/pull/14735)
  [TRTLLM-13050][test] Remove two-model eagle3 spec-decoding tests (#14735)
  _Files: `tests/integration/test_lists/test-db/l0_dgx_b200.yml`, `tests/integration/test_lists/test-db/l0_dgx_h100.yml`, `tests/integration/test_lists/test-db/l0_gb200_multi_gpus.yml`, `tests/integration/test_lists/test-db/l0_h100.yml`_
- **2026-05-29** [`8cdde83c16`](https://github.com/NVIDIA/TensorRT-LLM/commit/8cdde83c16) [#14381](https://github.com/NVIDIA/TensorRT-LLM/pull/14381)
  [None][fix] Reuse batch_indices_cuda across CUDA graph captures in EAGLE3 (#14381)
  _Files: `tensorrt_llm/_torch/speculative/eagle3.py`_

## LoRA  (1 commits)

- **2026-05-26** [`92ac6fc6ee`](https://github.com/NVIDIA/TensorRT-LLM/commit/92ac6fc6ee) [#14079](https://github.com/NVIDIA/TensorRT-LLM/pull/14079)
  [#11257][feat] Add LoRA support to llmapi triton backend (#14079)
  _Files: `ruff-legacy-baseline.json`, `tests/integration/defs/triton_server/common.py`, `tests/integration/defs/triton_server/conftest.py`, `tests/integration/defs/triton_server/test_triton_llm.py` _+7 more__

---
_Generated 2026-06-01 13:49 UTC_