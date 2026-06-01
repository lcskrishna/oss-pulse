# vllm-project/vllm — Weekly Change Report
**Period:** 2026-05-25 → 2026-06-01  |  **Total commits:** 211

## ✨ New Features This Week

- **2026-06-01** [#43481](https://github.com/vllm-project/vllm/pull/43481) — [Rust Frontend] Add InternLM2 tool parser (#43481)
- **2026-06-01** [#42730](https://github.com/vllm-project/vllm/pull/42730) — [CPU][RISC-V] Add missing RVV cpu_types helpers for WNA16 (#42730)
- **2026-05-31** [#43956](https://github.com/vllm-project/vllm/pull/43956) — [CI/Build] Enable Step3p7ForConditionalGeneration testing (#43956)
- **2026-05-30** [#44050](https://github.com/vllm-project/vllm/pull/44050) — [MRV2] Support breakable CUDA graph (#44050)
- **2026-05-30** [#44047](https://github.com/vllm-project/vllm/pull/44047) — [Governance] Add @BugenZhao as Rust frontend code owner (#44047)
- **2026-05-30** [#43817](https://github.com/vllm-project/vllm/pull/43817) — [ROCm] Add attention sink support to AITer flash attention backend (#43817)
- **2026-05-30** [#43881](https://github.com/vllm-project/vllm/pull/43881) — [ROCm] cmake: support PYTORCH_FOUND_HIP for torch 2.13 native HIP language support (#43881)
- **2026-05-29** [#43108](https://github.com/vllm-project/vllm/pull/43108) — [MoE Refactor] Remove supports_expert_map (#43108)
- **2026-05-29** [#43688](https://github.com/vllm-project/vllm/pull/43688) — [Feature] SSL support for dp supervisor (#43688)
- **2026-05-29** [#44019](https://github.com/vllm-project/vllm/pull/44019) — Add @khluu to CODEOWNERS (#44019)
- _…and 43 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-01** [`0910f7e0e1`](https://github.com/vllm-project/vllm/commit/0910f7e0e1) [#44153](https://github.com/vllm-project/vllm/pull/44153) — [Frontend] Resettle generative scoring entrypoint. (#44153)
- **2026-05-30** [`3fd9d2d357`](https://github.com/vllm-project/vllm/commit/3fd9d2d357) [#41813](https://github.com/vllm-project/vllm/pull/41813) — [CPU][Zen] Route W8A8 and W4A16 linear inference through zentorch on AMD Zen CPUs (#41813)
- **2026-05-30** [`3becc5db40`](https://github.com/vllm-project/vllm/commit/3becc5db40) [#43817](https://github.com/vllm-project/vllm/pull/43817) — [ROCm] Add attention sink support to AITer flash attention backend (#43817)
- **2026-05-30** [`e9499996df`](https://github.com/vllm-project/vllm/commit/e9499996df) [#43571](https://github.com/vllm-project/vllm/pull/43571) — [BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py (#43571)
- **2026-05-30** [`c0056b19bf`](https://github.com/vllm-project/vllm/commit/c0056b19bf) [#43881](https://github.com/vllm-project/vllm/pull/43881) — [ROCm] cmake: support PYTORCH_FOUND_HIP for torch 2.13 native HIP language support (#43881)
- **2026-05-30** [`ef8840adc7`](https://github.com/vllm-project/vllm/commit/ef8840adc7) [#44028](https://github.com/vllm-project/vllm/pull/44028) — [ROCm][CI] Fix failure in the Phi3V pooling test (#44028)
- **2026-05-29** [`7b98f498cd`](https://github.com/vllm-project/vllm/commit/7b98f498cd) [#43108](https://github.com/vllm-project/vllm/pull/43108) — [MoE Refactor] Remove supports_expert_map (#43108)
- **2026-05-29** [`6de08e8b46`](https://github.com/vllm-project/vllm/commit/6de08e8b46) [#44011](https://github.com/vllm-project/vllm/pull/44011) — [CI] Remove redundant test_chat_with_tool_reasoning.py (#44011)
- **2026-05-29** [`4aaba00f92`](https://github.com/vllm-project/vllm/commit/4aaba00f92) [#43219](https://github.com/vllm-project/vllm/pull/43219) — [EPLB] Make async EPLB default (#43219)
- **2026-05-29** [`0b56815a24`](https://github.com/vllm-project/vllm/commit/0b56815a24) [#42982](https://github.com/vllm-project/vllm/pull/42982) — [ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts) (#42982)
- **2026-05-29** [`ab12aab127`](https://github.com/vllm-project/vllm/commit/ab12aab127) [#42595](https://github.com/vllm-project/vllm/pull/42595) — [Bugfix] [ROCm] [DSV4] Fix AITER MXFP4 MoE weight loading and shuffle… (#42595)
- **2026-05-29** [`0cff0741ff`](https://github.com/vllm-project/vllm/commit/0cff0741ff) [#41394](https://github.com/vllm-project/vllm/pull/41394) — [Kernel][ROCm] Native W4A16 kernel for AMD RDNA3 (gfx1100) — fp16 + bf16 (#41394)
- **2026-05-29** [`b7fb747d8d`](https://github.com/vllm-project/vllm/commit/b7fb747d8d) [#43703](https://github.com/vllm-project/vllm/pull/43703) — [CI][ROCm] Don't skip MoRI-IO Connector tests (#43703)
- **2026-05-29** [`ff990d0d32`](https://github.com/vllm-project/vllm/commit/ff990d0d32) [#43945](https://github.com/vllm-project/vllm/pull/43945) — [ROCm][CI] Fix AITER unified attention for encoder-decoder cross-attention (#43945)
- **2026-05-29** [`ab7521d77c`](https://github.com/vllm-project/vllm/commit/ab7521d77c) [#43898](https://github.com/vllm-project/vllm/pull/43898) — [ROCm][DSv4] Remove device pipeline stall in sparse attention (#43898)
- **2026-05-29** [`22a58640b4`](https://github.com/vllm-project/vllm/commit/22a58640b4) [#43717](https://github.com/vllm-project/vllm/pull/43717) — [9/n] Migrate attention and cache kernels to torch stable ABI (continued)  (#43717)
- **2026-05-28** [`9769e2df2a`](https://github.com/vllm-project/vllm/commit/9769e2df2a) [#43120](https://github.com/vllm-project/vllm/pull/43120) — [AMD][CI][BugFix] Fix  Distributed Compile Unit Tests (2xH100-2xMI300) group (#43120)
- **2026-05-28** [`9090368b65`](https://github.com/vllm-project/vllm/commit/9090368b65) [#42083](https://github.com/vllm-project/vllm/pull/42083) — [Feat] Add support for per GPU worker RDMA NIC selection (#42083)
- **2026-05-28** [`ed7fe831da`](https://github.com/vllm-project/vllm/commit/ed7fe831da) [#43331](https://github.com/vllm-project/vllm/pull/43331) — [ROCm] Enable the aiter top-k/top-p sampler by default (#43331)
- **2026-05-28** [`5b115bb8a3`](https://github.com/vllm-project/vllm/commit/5b115bb8a3) [#43660](https://github.com/vllm-project/vllm/pull/43660) — [Attention][AMD] Standardize kv layout to blocks first for AMD (#43660)
- **2026-05-28** [`1b5437cec8`](https://github.com/vllm-project/vllm/commit/1b5437cec8) [#43136](https://github.com/vllm-project/vllm/pull/43136) — [ROCm] Bump ROCm to 7.2.3 (#43136)
- **2026-05-28** [`a9ec46d4b7`](https://github.com/vllm-project/vllm/commit/a9ec46d4b7) [#40687](https://github.com/vllm-project/vllm/pull/40687) — [ROCm][Perf] Support N=5 in wvSplitK skinny GEMM kernels for speculative decoding (#40687)
- **2026-05-28** [`552eb81918`](https://github.com/vllm-project/vllm/commit/552eb81918) [#40344](https://github.com/vllm-project/vllm/pull/40344) — [Bugfix][ROCm] Resolve MoRI connector hangs at high concurrency (#40344)
- **2026-05-28** [`9957e4d240`](https://github.com/vllm-project/vllm/commit/9957e4d240) [#43746](https://github.com/vllm-project/vllm/pull/43746) — [Model Refactoring] Remove torch compile dependency in DSv4 (#43746)
- **2026-05-28** [`a583c84e2b`](https://github.com/vllm-project/vllm/commit/a583c84e2b) [#43781](https://github.com/vllm-project/vllm/pull/43781) — [Bugfix][ROCm] Fix Accuracy Drop in Sparse Indexer on gfx950 (#43781)
- **2026-05-28** [`a9bc0ad8e4`](https://github.com/vllm-project/vllm/commit/a9bc0ad8e4) [#43824](https://github.com/vllm-project/vllm/pull/43824) — [ROCm][CI] Move workload from MI300 to MI325 (#43824)
- **2026-05-28** [`a04afd76aa`](https://github.com/vllm-project/vllm/commit/a04afd76aa) [#43829](https://github.com/vllm-project/vllm/pull/43829) — [DSV4] Remove AMD/XPU path in deepseek_v4/nvidia (#43829)
- **2026-05-28** [`0ba46d4b11`](https://github.com/vllm-project/vllm/commit/0ba46d4b11) [#43679](https://github.com/vllm-project/vllm/pull/43679) — [ROCm][DSV4] Enable Tilelang MHC replacing torch/triton mhc (#43679)
- **2026-05-28** [`33e94fc3ad`](https://github.com/vllm-project/vllm/commit/33e94fc3ad) [#43815](https://github.com/vllm-project/vllm/pull/43815) — [ROCm][CI] Stabilize Cargo cache and pre-test image checks (#43815)
- **2026-05-28** [`413ac5c070`](https://github.com/vllm-project/vllm/commit/413ac5c070) [#43664](https://github.com/vllm-project/vllm/pull/43664) — [Misc][Rocm] Remove redundant `AiterUnifiedAttentionBackend` block size log (#43664)
- **2026-05-28** [`2d2c660104`](https://github.com/vllm-project/vllm/commit/2d2c660104) [#43727](https://github.com/vllm-project/vllm/pull/43727) — [MoE] Remove inplace fused experts mechanism (#43727)
- **2026-05-27** [`05c50c721e`](https://github.com/vllm-project/vllm/commit/05c50c721e) [#41751](https://github.com/vllm-project/vllm/pull/41751) — [ROCm] mori: add InterNodeV1LL inter-node kernel selection via VLLM_MORI_INTERNODE_KERNEL (#41751)
- **2026-05-27** [`de12f5ca0b`](https://github.com/vllm-project/vllm/commit/de12f5ca0b) [#42833](https://github.com/vllm-project/vllm/pull/42833) — [ROCm][GPT-OSS] Avoid repeated compile-time `cos_sin_cache.to(bf16)` casts in rotary path (#42833)
- **2026-05-27** [`7b54690244`](https://github.com/vllm-project/vllm/commit/7b54690244) [#39177](https://github.com/vllm-project/vllm/pull/39177) — [ROCm][Perf] Expose AITER MoE sorting dispatch policy via env var (#39177)
- **2026-05-27** [`adaa5e455a`](https://github.com/vllm-project/vllm/commit/adaa5e455a) [#43710](https://github.com/vllm-project/vllm/pull/43710) — [DSv4] Refactor compressor & Fix ROCm compatibility (#43710)
- **2026-05-27** [`7e33081cee`](https://github.com/vllm-project/vllm/commit/7e33081cee) [#42095](https://github.com/vllm-project/vllm/pull/42095) — [Attention] Make FlexAttention and FlashAttention use num-blocks first layouts (#42095)
- **2026-05-27** [`5bdb181df5`](https://github.com/vllm-project/vllm/commit/5bdb181df5) [#43647](https://github.com/vllm-project/vllm/pull/43647) — [ROCm][CI] Fix ROCm multimodal Qwen2.5-VL activation compile and Phi4MM ragged image mask handling (#43647)
- **2026-05-26** [`49b4882779`](https://github.com/vllm-project/vllm/commit/49b4882779) [#43709](https://github.com/vllm-project/vllm/pull/43709) — [CI] Soft-fail AMD entrypoints mirror tests (#43709)
- **2026-05-26** [`c8414a8271`](https://github.com/vllm-project/vllm/commit/c8414a8271) [#43629](https://github.com/vllm-project/vllm/pull/43629) — [ROCm] Remove MegaMoE integration in deepseek v4 (#43629)
- **2026-05-26** [`6ab6ffb428`](https://github.com/vllm-project/vllm/commit/6ab6ffb428) [#43162](https://github.com/vllm-project/vllm/pull/43162) — [Feat][DSV4] Fuse q pad into deepseek v4 fused kernel (#43162)
- **2026-05-26** [`445ded18c1`](https://github.com/vllm-project/vllm/commit/445ded18c1) [#40990](https://github.com/vllm-project/vllm/pull/40990) — [ROCm][CI] Extend ROCm quick reduce coverage (#40990)
- **2026-05-26** [`d565357a90`](https://github.com/vllm-project/vllm/commit/d565357a90) [#43603](https://github.com/vllm-project/vllm/pull/43603) — [Docs][ROCm] MoRI-IO Connector Usage Guide (#43603)
- **2026-05-26** [`681d7dd38b`](https://github.com/vllm-project/vllm/commit/681d7dd38b) [#43303](https://github.com/vllm-project/vllm/pull/43303) — [Misc][Refactor][ROCm] Convert MoRI-related envvars to extra config args (#43303)
- **2026-05-25** [`d4004455d2`](https://github.com/vllm-project/vllm/commit/d4004455d2) [#43554](https://github.com/vllm-project/vllm/pull/43554) — [Kernel] Remove NormGateLinear (#43554)
- **2026-05-25** [`6cbe448eed`](https://github.com/vllm-project/vllm/commit/6cbe448eed) [#42373](https://github.com/vllm-project/vllm/pull/42373) — fix: MoE model using shared routed experts crashes on AMD GPUs (#42373)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#39071](https://github.com/vllm-project/vllm/issues/39071) | [Bug]: Gemma 4 31B Structured Outputs weird behaviour / character outp | bug | 2026-06-01 |
| [#43916](https://github.com/vllm-project/vllm/issues/43916) | [Parity with CUDA]: Add top 5-10 popular OSS models into mi355, mi325, | feature request, rocm | 2026-06-01 |
| [#41515](https://github.com/vllm-project/vllm/issues/41515) | [Bug]:  [kv_offload+HMA] Fails on chat subsequent request | bug | 2026-06-01 |
| [#44185](https://github.com/vllm-project/vllm/issues/44185) | [Bug]: vLLM hangs during speculative decoding with MoE draft model nea | bug | 2026-06-01 |
| [#44092](https://github.com/vllm-project/vllm/issues/44092) | AMD Development Roadmap (2026 Q2) | rocm | 2026-06-01 |
| [#44180](https://github.com/vllm-project/vllm/issues/44180) | [Bug]: v0.22.0 fails to load Qwen/Qwen3-Omni-30B-A3B-Thinking on H20:  | bug | 2026-06-01 |
| [#44100](https://github.com/vllm-project/vllm/issues/44100) | [Bug]: [LMCache] `_cleanup_request_tracker` leaks lookup state and ser | bug | 2026-06-01 |
| [#44096](https://github.com/vllm-project/vllm/issues/44096) | [Bug]:  [LMCache] `update_state_after_alloc` passes wrong `cache_salt` | bug | 2026-06-01 |
| [#44175](https://github.com/vllm-project/vllm/issues/44175) | [Bug]: Linear host RSS growth + step-up in E2E latency under sustained | bug | 2026-06-01 |
| [#33702](https://github.com/vllm-project/vllm/issues/33702) | [Roadmap]: PD Disaggregation with `NixlConnector` Roadmap | help wanted, feature request | 2026-06-01 |
| [#44091](https://github.com/vllm-project/vllm/issues/44091) | AMD Development Roadmap (2026 Q3) | rocm | 2026-06-01 |
| [#44039](https://github.com/vllm-project/vllm/issues/44039) | [Bug]: gemma4 _process_video_input not supported on CPU | bug | 2026-06-01 |
| [#41967](https://github.com/vllm-project/vllm/issues/41967) | [Bug]: Gemma4 + MTP speculative decoding drops first tool-call argumen | — | 2026-06-01 |
| [#44087](https://github.com/vllm-project/vllm/issues/44087) | [Bug]: Step-3.5/3.7-Flash MTP speculative decoding fails to load on NV | — | 2026-06-01 |
| [#35569](https://github.com/vllm-project/vllm/issues/35569) | [Bug]: [ROCm] ROCM_ATTN backend shows ~8.5% systematic score deviation | bug, rocm, stale | 2026-06-01 |
| [#43153](https://github.com/vllm-project/vllm/issues/43153) | [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regress | bug, rocm | 2026-06-01 |
| [#33014](https://github.com/vllm-project/vllm/issues/33014) | [Bug]: LoRA loading fails with Fused MoE when data parallelism (DP > 1 | bug, stale | 2026-06-01 |
| [#33783](https://github.com/vllm-project/vllm/issues/33783) | [Bug]: CutlassW4A8LinearKernel fails on DeepSeekV3.1 W4AF8 due to dime | bug, stale | 2026-06-01 |
| [#34295](https://github.com/vllm-project/vllm/issues/34295) | [Bug]: | bug, stale | 2026-06-01 |
| [#35266](https://github.com/vllm-project/vllm/issues/35266) | [Bug]: Missing opening brace for Qwen3.5 streaming tool calls | bug, stale | 2026-06-01 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 44 |
| MoE / Expert Parallel | 26 |
| Other | 26 |
| Models | 19 |
| Multimodal | 15 |
| Attention | 11 |
| Serving / API | 10 |
| Docs | 10 |
| Scheduler / Engine | 10 |
| Disaggregation / PD | 10 |
| Quantization | 9 |
| CI / Build | 9 |
| Speculative Decoding | 5 |
| KV Cache / Offload | 4 |
| Perf / Benchmark | 3 |

## ROCm / AMD  (44 commits)

- **2026-06-01** [`0910f7e0e1`](https://github.com/vllm-project/vllm/commit/0910f7e0e1) [#44153](https://github.com/vllm-project/vllm/pull/44153)
  [Frontend] Resettle generative scoring entrypoint. (#44153)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/generate/__init__.py`, `tests/entrypoints/generate/generative_scoring/__init__.py` _+9 more__
- **2026-05-30** [`3fd9d2d357`](https://github.com/vllm-project/vllm/commit/3fd9d2d357) [#41813](https://github.com/vllm-project/vllm/pull/41813)
  [CPU][Zen] Route W8A8 and W4A16 linear inference through zentorch on AMD Zen CPUs (#41813)
  _Files: `setup.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mixed_precision/__init__.py`, `vllm/model_executor/kernels/linear/mixed_precision/zentorch.py` _+3 more__
- **2026-05-30** [`3becc5db40`](https://github.com/vllm-project/vllm/commit/3becc5db40) [#43817](https://github.com/vllm-project/vllm/pull/43817)
  [ROCm] Add attention sink support to AITer flash attention backend (#43817)
  _Files: `docs/design/attention_backends.md`, `vllm/_aiter_ops.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-05-30** [`e9499996df`](https://github.com/vllm-project/vllm/commit/e9499996df) [#43571](https://github.com/vllm-project/vllm/pull/43571)
  [BugFix][Platform] Fix import vllm.platforms.rocm error on non-CUDA test_gpt_oss.py (#43571)
  _Files: `tests/models/quantization/test_gpt_oss.py`_
- **2026-05-30** [`c0056b19bf`](https://github.com/vllm-project/vllm/commit/c0056b19bf) [#43881](https://github.com/vllm-project/vllm/pull/43881)
  [ROCm] cmake: support PYTORCH_FOUND_HIP for torch 2.13 native HIP language support (#43881)
  _Files: `CMakeLists.txt`_
- **2026-05-30** [`ef8840adc7`](https://github.com/vllm-project/vllm/commit/ef8840adc7) [#44028](https://github.com/vllm-project/vllm/pull/44028)
  [ROCm][CI] Fix failure in the Phi3V pooling test (#44028)
  _Files: `tests/models/multimodal/pooling/test_phi3v.py`_
- **2026-05-29** [`7b98f498cd`](https://github.com/vllm-project/vllm/commit/7b98f498cd) [#43108](https://github.com/vllm-project/vllm/pull/43108)
  [MoE Refactor] Remove supports_expert_map (#43108)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py`, `tests/kernels/moe/test_modular_kernel_combinations.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe.py` _+23 more__
- **2026-05-29** [`6de08e8b46`](https://github.com/vllm-project/vllm/commit/6de08e8b46) [#44011](https://github.com/vllm-project/vllm/pull/44011)
  [CI] Remove redundant test_chat_with_tool_reasoning.py (#44011)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `tests/entrypoints/openai/chat_completion/test_chat_with_tool_reasoning.py`_
- **2026-05-29** [`4aaba00f92`](https://github.com/vllm-project/vllm/commit/4aaba00f92) [#43219](https://github.com/vllm-project/vllm/pull/43219)
  [EPLB] Make async EPLB default (#43219)
  _Files: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_block_ep_eplb.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/e2e_integration.yaml` _+3 more__
- **2026-05-29** [`0b56815a24`](https://github.com/vllm-project/vllm/commit/0b56815a24) [#42982](https://github.com/vllm-project/vllm/pull/42982)
  [ROCm][Perf] DSv3.2 MI355X TP4 decode-step orchestration cleanup (3 micro-opts) (#42982)
  _Files: `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-05-29** [`ab12aab127`](https://github.com/vllm-project/vllm/commit/ab12aab127) [#42595](https://github.com/vllm-project/vllm/pull/42595)
  [Bugfix] [ROCm] [DSV4] Fix AITER MXFP4 MoE weight loading and shuffle… (#42595)
  _Files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-05-29** [`0cff0741ff`](https://github.com/vllm-project/vllm/commit/0cff0741ff) [#41394](https://github.com/vllm-project/vllm/pull/41394)
  [Kernel][ROCm] Native W4A16 kernel for AMD RDNA3 (gfx1100) — fp16 + bf16 (#41394)
  _Files: `CMakeLists.txt`, `csrc/rocm/ops.h`, `csrc/rocm/q_gemm_rdna3.cu`, `csrc/rocm/q_gemm_rdna3_wmma.cu` _+9 more__
- **2026-05-29** [`b7fb747d8d`](https://github.com/vllm-project/vllm/commit/b7fb747d8d) [#43703](https://github.com/vllm-project/vllm/pull/43703)
  [CI][ROCm] Don't skip MoRI-IO Connector tests (#43703)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`_
- **2026-05-29** [`ff990d0d32`](https://github.com/vllm-project/vllm/commit/ff990d0d32) [#43945](https://github.com/vllm-project/vllm/pull/43945)
  [ROCm][CI] Fix AITER unified attention for encoder-decoder cross-attention (#43945)
  _Files: `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-05-29** [`ab7521d77c`](https://github.com/vllm-project/vllm/commit/ab7521d77c) [#43898](https://github.com/vllm-project/vllm/pull/43898)
  [ROCm][DSv4] Remove device pipeline stall in sparse attention (#43898)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-05-29** [`22a58640b4`](https://github.com/vllm-project/vllm/commit/22a58640b4) [#43717](https://github.com/vllm-project/vllm/pull/43717)
  [9/n] Migrate attention and cache kernels to torch stable ABI (continued)  (#43717)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/activation_kernels.cu`, `csrc/libtorch_stable/attention/attention_kernels.cuh`, `csrc/libtorch_stable/attention/attention_utils.cuh` _+19 more__
- **2026-05-28** [`9769e2df2a`](https://github.com/vllm-project/vllm/commit/9769e2df2a) [#43120](https://github.com/vllm-project/vllm/pull/43120)
  [AMD][CI][BugFix] Fix  Distributed Compile Unit Tests (2xH100-2xMI300) group (#43120)
  _Files: `tests/compile/fusions_e2e/common.py`, `tests/compile/fusions_e2e/conftest.py`, `tests/compile/fusions_e2e/models.py`, `tests/compile/fusions_e2e/test_tp2_ar_rms.py` _+3 more__
- **2026-05-28** [`ed7fe831da`](https://github.com/vllm-project/vllm/commit/ed7fe831da) [#43331](https://github.com/vllm-project/vllm/pull/43331)
  [ROCm] Enable the aiter top-k/top-p sampler by default (#43331)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-05-28** [`5b115bb8a3`](https://github.com/vllm-project/vllm/commit/5b115bb8a3) [#43660](https://github.com/vllm-project/vllm/pull/43660)
  [Attention][AMD] Standardize kv layout to blocks first for AMD (#43660)
  _Files: `vllm/platforms/rocm.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py` _+2 more__
- **2026-05-28** [`1b5437cec8`](https://github.com/vllm-project/vllm/commit/1b5437cec8) [#43136](https://github.com/vllm-project/vllm/pull/43136)
  [ROCm] Bump ROCm to 7.2.3 (#43136)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile.rocm_base`_
- **2026-05-28** [`a9ec46d4b7`](https://github.com/vllm-project/vllm/commit/a9ec46d4b7) [#40687](https://github.com/vllm-project/vllm/pull/40687)
  [ROCm][Perf] Support N=5 in wvSplitK skinny GEMM kernels for speculative decoding (#40687)
  _Files: `csrc/rocm/skinny_gemms.cu`, `vllm/model_executor/layers/utils.py`_
- **2026-05-28** [`552eb81918`](https://github.com/vllm-project/vllm/commit/552eb81918) [#40344](https://github.com/vllm-project/vllm/pull/40344)
  [Bugfix][ROCm] Resolve MoRI connector hangs at high concurrency (#40344)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`_
- **2026-05-28** [`9957e4d240`](https://github.com/vllm-project/vllm/commit/9957e4d240) [#43746](https://github.com/vllm-project/vllm/pull/43746)
  [Model Refactoring] Remove torch compile dependency in DSv4 (#43746)
  _Files: `vllm/config/vllm.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/common/ops/__init__.py` _+4 more__
- **2026-05-28** [`a583c84e2b`](https://github.com/vllm-project/vllm/commit/a583c84e2b) [#43781](https://github.com/vllm-project/vllm/pull/43781)
  [Bugfix][ROCm] Fix Accuracy Drop in Sparse Indexer on gfx950 (#43781)
  _Files: `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-05-28** [`a9bc0ad8e4`](https://github.com/vllm-project/vllm/commit/a9bc0ad8e4) [#43824](https://github.com/vllm-project/vllm/pull/43824)
  [ROCm][CI] Move workload from MI300 to MI325 (#43824)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/misc.yaml` _+2 more__
- **2026-05-28** [`a04afd76aa`](https://github.com/vllm-project/vllm/commit/a04afd76aa) [#43829](https://github.com/vllm-project/vllm/pull/43829)
  [DSV4] Remove AMD/XPU path in deepseek_v4/nvidia (#43829)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`_
- **2026-05-28** [`0ba46d4b11`](https://github.com/vllm-project/vllm/commit/0ba46d4b11) [#43679](https://github.com/vllm-project/vllm/pull/43679)
  [ROCm][DSV4] Enable Tilelang MHC replacing torch/triton mhc (#43679)
  _Files: `requirements/build/rocm.txt`, `requirements/rocm.txt`, `requirements/test/rocm.in`, `requirements/test/rocm.txt` _+9 more__
- **2026-05-28** [`33e94fc3ad`](https://github.com/vllm-project/vllm/commit/33e94fc3ad) [#43815](https://github.com/vllm-project/vllm/pull/43815)
  [ROCm][CI] Stabilize Cargo cache and pre-test image checks (#43815)
  _Files: `.buildkite/hardware_tests/amd.yaml`, `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `docker/Dockerfile.rocm`_
- **2026-05-28** [`413ac5c070`](https://github.com/vllm-project/vllm/commit/413ac5c070) [#43664](https://github.com/vllm-project/vllm/pull/43664)
  [Misc][Rocm] Remove redundant `AiterUnifiedAttentionBackend` block size log (#43664)
  _Files: `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-05-28** [`2d2c660104`](https://github.com/vllm-project/vllm/commit/2d2c660104) [#43727](https://github.com/vllm-project/vllm/pull/43727)
  [MoE] Remove inplace fused experts mechanism (#43727)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/test_batched_deepgemm.py`, `tests/kernels/moe/test_block_fp8.py`, `tests/kernels/moe/test_cutlass_moe.py` _+40 more__
- **2026-05-27** [`05c50c721e`](https://github.com/vllm-project/vllm/commit/05c50c721e) [#41751](https://github.com/vllm-project/vllm/pull/41751)
  [ROCm] mori: add InterNodeV1LL inter-node kernel selection via VLLM_MORI_INTERNODE_KERNEL (#41751)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py`, `tests/kernels/moe/test_moe_layer.py`, `vllm/config/parallel.py` _+3 more__
- **2026-05-27** [`de12f5ca0b`](https://github.com/vllm-project/vllm/commit/de12f5ca0b) [#42833](https://github.com/vllm-project/vllm/pull/42833)
  [ROCm][GPT-OSS] Avoid repeated compile-time `cos_sin_cache.to(bf16)` casts in rotary path (#42833)
  _Files: `vllm/model_executor/layers/rotary_embedding/base.py`_
- **2026-05-27** [`7b54690244`](https://github.com/vllm-project/vllm/commit/7b54690244) [#39177](https://github.com/vllm-project/vllm/pull/39177)
  [ROCm][Perf] Expose AITER MoE sorting dispatch policy via env var (#39177)
  _Files: `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-05-27** [`adaa5e455a`](https://github.com/vllm-project/vllm/commit/adaa5e455a) [#43710](https://github.com/vllm-project/vllm/pull/43710)
  [DSv4] Refactor compressor & Fix ROCm compatibility (#43710)
  _Files: `vllm/models/deepseek_v4/common/ops/__init__.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py` _+5 more__
- **2026-05-27** [`7e33081cee`](https://github.com/vllm-project/vllm/commit/7e33081cee) [#42095](https://github.com/vllm-project/vllm/pull/42095)
  [Attention] Make FlexAttention and FlashAttention use num-blocks first layouts (#42095)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_kv_head_stride_canonicalization.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+16 more__
- **2026-05-27** [`5bdb181df5`](https://github.com/vllm-project/vllm/commit/5bdb181df5) [#43647](https://github.com/vllm-project/vllm/pull/43647)
  [ROCm][CI] Fix ROCm multimodal Qwen2.5-VL activation compile and Phi4MM ragged image mask handling (#43647)
  _Files: `vllm/model_executor/layers/activation.py`, `vllm/model_executor/models/phi4mm.py`, `vllm/model_executor/models/qwen2_5_vl.py`_
- **2026-05-26** [`49b4882779`](https://github.com/vllm-project/vllm/commit/49b4882779) [#43709](https://github.com/vllm-project/vllm/pull/43709)
  [CI] Soft-fail AMD entrypoints mirror tests (#43709)
  _Files: `.buildkite/test_areas/entrypoints.yaml`_
- **2026-05-26** [`c8414a8271`](https://github.com/vllm-project/vllm/commit/c8414a8271) [#43629](https://github.com/vllm-project/vllm/pull/43629)
  [ROCm] Remove MegaMoE integration in deepseek v4 (#43629)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-05-26** [`6ab6ffb428`](https://github.com/vllm-project/vllm/commit/6ab6ffb428) [#43162](https://github.com/vllm-project/vllm/pull/43162)
  [Feat][DSV4] Fuse q pad into deepseek v4 fused kernel (#43162)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/ops.h`, `csrc/torch_bindings.cpp` _+7 more__
- **2026-05-26** [`445ded18c1`](https://github.com/vllm-project/vllm/commit/445ded18c1) [#40990](https://github.com/vllm-project/vllm/pull/40990)
  [ROCm][CI] Extend ROCm quick reduce coverage (#40990)
  _Files: `.buildkite/test-amd.yaml`, `tests/distributed/test_quick_all_reduce.py`, `tests/distributed/test_rocm_quick_reduce.py`, `tests/utils.py`_
- **2026-05-26** [`d565357a90`](https://github.com/vllm-project/vllm/commit/d565357a90) [#43603](https://github.com/vllm-project/vllm/pull/43603)
  [Docs][ROCm] MoRI-IO Connector Usage Guide (#43603)
  _Files: `docs/features/disagg_prefill.md`, `docs/features/moriio_connector_usage.md`_
- **2026-05-26** [`681d7dd38b`](https://github.com/vllm-project/vllm/commit/681d7dd38b) [#43303](https://github.com/vllm-project/vllm/pull/43303)
  [Misc][Refactor][ROCm] Convert MoRI-related envvars to extra config args (#43303)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py` _+1 more__
- **2026-05-25** [`d4004455d2`](https://github.com/vllm-project/vllm/commit/d4004455d2) [#43554](https://github.com/vllm-project/vllm/pull/43554)
  [Kernel] Remove NormGateLinear (#43554)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_norm_router_gemm.py`, `csrc/moe/dsv3_router_gemm_bf16_out.cu`, `csrc/moe/dsv3_router_gemm_float_out.cu` _+12 more__
- **2026-05-25** [`6cbe448eed`](https://github.com/vllm-project/vllm/commit/6cbe448eed) [#42373](https://github.com/vllm-project/vllm/pull/42373)
  fix: MoE model using shared routed experts crashes on AMD GPUs (#42373)
  _Files: `vllm/model_executor/layers/fused_moe/router/aiter_shared_routed_fused_moe_router.py`_

## MoE / Expert Parallel  (26 commits)

- **2026-06-01** [`8796838910`](https://github.com/vllm-project/vllm/commit/8796838910) [#43770](https://github.com/vllm-project/vllm/pull/43770)
  [Bugfix] fix wrong partial_rotary_factor calculation for bailing_moe model. (#43770)
  _Files: `vllm/model_executor/models/bailing_moe.py`_
- **2026-05-30** [`559d6710bf`](https://github.com/vllm-project/vllm/commit/559d6710bf) [#38445](https://github.com/vllm-project/vllm/pull/38445)
  [PERF]MiniMax-M2 gate kernel (#38445)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_router_gemm.py`, `cmake/utils.cmake`, `csrc/libtorch_stable/fp32_router_gemm.cu` _+6 more__
- **2026-05-29** [`187457a952`](https://github.com/vllm-project/vllm/commit/187457a952) [#44033](https://github.com/vllm-project/vllm/pull/44033)
  Revert "[MoE Refactor] Migrate MoeWNA16Method quantization to MK orac… (#44033)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/auto_gptq.py` _+4 more__
- **2026-05-29** [`106aa92f04`](https://github.com/vllm-project/vllm/commit/106aa92f04) [#42647](https://github.com/vllm-project/vllm/pull/42647)
  [MoE Refactor] Migrate MoeWNA16Method quantization to MK oracle (#42647)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/auto_gptq.py` _+4 more__
- **2026-05-29** [`739096a028`](https://github.com/vllm-project/vllm/commit/739096a028) [#44005](https://github.com/vllm-project/vllm/pull/44005)
  [Bug] Fix torch device issue for MOE permute (#44005)
  _Files: `vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py`_
- **2026-05-29** [`84b2a8a7e7`](https://github.com/vllm-project/vllm/commit/84b2a8a7e7) [#42553](https://github.com/vllm-project/vllm/pull/42553)
  [MoE Refactor] WNA16 MoE backend selection into oracle module (#42553)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxint4_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` _+4 more__
- **2026-05-29** [`94d3f4d205`](https://github.com/vllm-project/vllm/commit/94d3f4d205) [#43633](https://github.com/vllm-project/vllm/pull/43633)
  [CPU Backend] CPU top-k and top-p sampling kernels using Triton (#43633)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/platforms/cpu.py`, `vllm/v1/sample/ops/topk_topp_sampler.py` _+1 more__
- **2026-05-29** [`04516eabc8`](https://github.com/vllm-project/vllm/commit/04516eabc8) [#42822](https://github.com/vllm-project/vllm/pull/42822)
  [XPU] add gelu_tanh to xpu moe backend supported activations (#42822)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-05-29** [`710f077617`](https://github.com/vllm-project/vllm/commit/710f077617) [#43234](https://github.com/vllm-project/vllm/pull/43234)
  [Refactor] Remove dead code (#43234)
  _Files: `vllm/_custom_ops.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/linear.py` _+2 more__
- **2026-05-29** [`9636709372`](https://github.com/vllm-project/vllm/commit/9636709372) [#43277](https://github.com/vllm-project/vllm/pull/43277)
  [XPU] add scale transpose to prepare_fp8_moe_layer_for_xpu and bump up kernels (#43277)
  _Files: `requirements/xpu.txt`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`_
- **2026-05-29** [`b690b2bb67`](https://github.com/vllm-project/vllm/commit/b690b2bb67) [#43859](https://github.com/vllm-project/vllm/pull/43859)
  [Model]Support Step-3.7-Flash (#43859)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py` _+11 more__
- **2026-05-28** [`3207e7680e`](https://github.com/vllm-project/vllm/commit/3207e7680e) [#41426](https://github.com/vllm-project/vllm/pull/41426)
  [XPU][MoE] Add WNA16 oracle backend for GPTQ sym-int4 (xpu_fused_moe) (#41426)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`_
- **2026-05-28** [`64e1218673`](https://github.com/vllm-project/vllm/commit/64e1218673) [#43014](https://github.com/vllm-project/vllm/pull/43014)
  [Perf] Optimize moe permute by pre-allocate buffer, 9~14% kernel performance improvement (#43014)
  _Files: `benchmarks/kernels/benchmark_moe_permute_unpermute.py`, `csrc/moe/moe_ops.h`, `csrc/moe/moe_permute_unpermute_op.cu`, `csrc/moe/torch_bindings.cpp` _+4 more__
- **2026-05-28** [`6cc8577421`](https://github.com/vllm-project/vllm/commit/6cc8577421) [#40923](https://github.com/vllm-project/vllm/pull/40923)
  [Kernel] Marlin MoE: include SM 12.x in default arch list (#40923)
  _Files: `CMakeLists.txt`, `csrc/quantization/marlin/marlin.cu`_
- **2026-05-28** [`e54eff769d`](https://github.com/vllm-project/vllm/commit/e54eff769d) [#43769](https://github.com/vllm-project/vllm/pull/43769)
  [Bugfix] Pass `routed_scaling_factor` to FlashInfer TRTLLM BF16 MoE (#43769)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`_
- **2026-05-28** [`381edde1b9`](https://github.com/vllm-project/vllm/commit/381edde1b9) [#43599](https://github.com/vllm-project/vllm/pull/43599)
  [Bugfix][Kernel] TRTLLM NVFP4 MoE chunking (#43599)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`_
- **2026-05-27** [`5963c19478`](https://github.com/vllm-project/vllm/commit/5963c19478) [#43617](https://github.com/vllm-project/vllm/pull/43617)
  Fix Qwen3-VL and Qwen3-omni-thinker accuracy degradation from deepstack inputs under torch.compile (#43617)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-05-27** [`284e6f543d`](https://github.com/vllm-project/vllm/commit/284e6f543d) [#43361](https://github.com/vllm-project/vllm/pull/43361)
  [8/n] Migrate merge_attn_states, mamba, sampler to torch stable ABI (continued) (#43361)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/attention/merge_attn_states.cu`, `csrc/libtorch_stable/mamba/selective_scan.h`, `csrc/libtorch_stable/mamba/selective_scan_fwd.cu` _+9 more__
- **2026-05-27** [`396c8fee50`](https://github.com/vllm-project/vllm/commit/396c8fee50) [#43662](https://github.com/vllm-project/vllm/pull/43662)
  [Rust Frontend] Align tool parser fallback behavior between streaming & non-streaming paths (#43662)
  _Files: `rust/Cargo.lock`, `rust/src/chat/src/output/default/tool.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs` _+22 more__
- **2026-05-26** [`6e503868ca`](https://github.com/vllm-project/vllm/commit/6e503868ca) [#43410](https://github.com/vllm-project/vllm/pull/43410)
  [Kernel] Porting  fuse_minimax_qk_norm  to manual fusion (#43410)
  _Files: `docs/design/fusions.md`, `tests/kernels/core/test_minimax_reduce_rms.py`, `vllm/compilation/passes/fusion/minimax_qk_norm_fusion.py`, `vllm/compilation/passes/pass_manager.py` _+8 more__
- **2026-05-26** [`f51bbc694d`](https://github.com/vllm-project/vllm/commit/f51bbc694d) [#42789](https://github.com/vllm-project/vllm/pull/42789)
  [MoE Refactor] W4a8 int8 oracle (#42789)
  _Files: `tests/kernels/moe/test_cpu_int4_moe.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_int4_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a8_int8.py` _+1 more__
- **2026-05-26** [`b226ddacfd`](https://github.com/vllm-project/vllm/commit/b226ddacfd) [#42768](https://github.com/vllm-project/vllm/pull/42768)
  [MoE Refactor] Migrate ModelOptMxFp8FusedMoE to oracle (#42768)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/int8.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+4 more__
- **2026-05-26** [`861b97765d`](https://github.com/vllm-project/vllm/commit/861b97765d) [#43646](https://github.com/vllm-project/vllm/pull/43646)
  [XPU] Fix fused MoE LoRA kernel crash on XPU by using platform-agnos num_compute_units (#43646)
  _Files: `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-05-26** [`aa2b56ffb0`](https://github.com/vllm-project/vllm/commit/aa2b56ffb0) [#43632](https://github.com/vllm-project/vllm/pull/43632)
  [DeepSeek V4] Move MegaMoE input prep kernel to nvidia/ops (#43632)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/ops/prepare_megamoe.py`_
- **2026-05-26** [`ec5de7fa7d`](https://github.com/vllm-project/vllm/commit/ec5de7fa7d) [#42290](https://github.com/vllm-project/vllm/pull/42290)
  [LoRA] Add one shot triton kernel For MoE LoRA (#42290)
  _Files: `benchmarks/kernels/benchmark_fused_moe_lora_one_shot.py`, `tests/lora/test_fused_moe_lora_kernel.py`, `vllm/envs.py`, `vllm/lora/layers/base_linear.py` _+10 more__
- **2026-05-26** [`71d810bbf4`](https://github.com/vllm-project/vllm/commit/71d810bbf4) [#43028](https://github.com/vllm-project/vllm/pull/43028)
  [XPU] Ensure RNG offset alignment with PyTorch requirements in XPU sampler (#43028)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`_

## Other  (26 commits)

- **2026-06-01** [`29d69332aa`](https://github.com/vllm-project/vllm/commit/29d69332aa) [#44035](https://github.com/vllm-project/vllm/pull/44035)
  [BugFix] Fix `_has_module` to verify native deps via trial import (#44035)
  _Files: `tests/utils_/test_import_utils.py`, `vllm/utils/import_utils.py`_
- **2026-05-30** [`1a096d8208`](https://github.com/vllm-project/vllm/commit/1a096d8208) [#43997](https://github.com/vllm-project/vllm/pull/43997)
  [Refactor] Remove dead current_tool_name_sent assignments from tool parsers (#43997)
  _Files: `vllm/tool_parsers/ernie45_tool_parser.py`, `vllm/tool_parsers/hunyuan_a13b_tool_parser.py`, `vllm/tool_parsers/hy_v3_tool_parser.py`, `vllm/tool_parsers/phi4mini_tool_parser.py`_
- **2026-05-30** [`1e2ce5d11a`](https://github.com/vllm-project/vllm/commit/1e2ce5d11a) [#43792](https://github.com/vllm-project/vllm/pull/43792)
  offload prompt_embeds decode in render_prompts_async to avoid blocking (#43792)
  _Files: `vllm/renderers/base.py`_
- **2026-05-29** [`38b864d81d`](https://github.com/vllm-project/vllm/commit/38b864d81d) [#43346](https://github.com/vllm-project/vllm/pull/43346)
  [Metrics] Exclude KV transfer tokens from iteration_tokens_total (#43346)
  _Files: `vllm/v1/metrics/loggers.py`_
- **2026-05-29** [`acbc203340`](https://github.com/vllm-project/vllm/commit/acbc203340) [#44019](https://github.com/vllm-project/vllm/pull/44019)
  Add @khluu to CODEOWNERS (#44019)
  _Files: `.github/CODEOWNERS`_
- **2026-05-29** [`4ff865c38e`](https://github.com/vllm-project/vllm/commit/4ff865c38e) [#43616](https://github.com/vllm-project/vllm/pull/43616)
  [Bugfix] Disable allreduce_rms_fusion when pipeline_parallel_size > 1 (#43616)
  _Files: `vllm/config/vllm.py`_
- **2026-05-29** [`5502c3b52d`](https://github.com/vllm-project/vllm/commit/5502c3b52d) [#43818](https://github.com/vllm-project/vllm/pull/43818)
  [Misc] added unit tests for the core pooling methods (#43818)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`_
- **2026-05-28** [`7e53283b1c`](https://github.com/vllm-project/vllm/commit/7e53283b1c) [#43732](https://github.com/vllm-project/vllm/pull/43732)
  [Core] Cleanup KVConnector handling with PP + fix MRV2  (#43732)
  _Files: `tests/distributed/test_comm_ops.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/sequence.py` _+5 more__
- **2026-05-28** [`9090368b65`](https://github.com/vllm-project/vllm/commit/9090368b65) [#42083](https://github.com/vllm-project/vllm/pull/42083)
  [Feat] Add support for per GPU worker RDMA NIC selection (#42083)
  _Files: `tests/v1/executor/test_vllm_net_devices.py`, `vllm/envs.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py` _+3 more__
- **2026-05-28** [`be4062fd6c`](https://github.com/vllm-project/vllm/commit/be4062fd6c) [#43813](https://github.com/vllm-project/vllm/pull/43813)
  [Bug] Fix `tests/distributed/test_elastic_ep.py  - assert False` (#43813)
  _Files: `vllm/v1/utils.py`_
- **2026-05-28** [`3a282230ee`](https://github.com/vllm-project/vllm/commit/3a282230ee) [#43872](https://github.com/vllm-project/vllm/pull/43872)
  [Rust Frontend] Add `hy_v3` tool parser (#43872)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/tool-parser/src/hy_v3.rs` _+2 more__
- **2026-05-28** [`19af4e6dd4`](https://github.com/vllm-project/vllm/commit/19af4e6dd4) [#43846](https://github.com/vllm-project/vllm/pull/43846)
  Fix `OlmoHybridForCausalLM` not initialising (#43846)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-05-28** [`61288b5458`](https://github.com/vllm-project/vllm/commit/61288b5458) [#43860](https://github.com/vllm-project/vllm/pull/43860)
  [Bugfix] Fix HyperCLOVAX CI failure after upstream removed remote code (#43860)
  _Files: `tests/models/registry.py`, `vllm/transformers_utils/config.py`_
- **2026-05-28** [`2a781756a1`](https://github.com/vllm-project/vllm/commit/2a781756a1) [#43183](https://github.com/vllm-project/vllm/pull/43183)
  Restore `Literal` for `WeightTransferConfig.backend` (#43183)
  _Files: `vllm/config/weight_transfer.py`_
- **2026-05-28** [`d6b48f928f`](https://github.com/vllm-project/vllm/commit/d6b48f928f) [#43768](https://github.com/vllm-project/vllm/pull/43768)
  [BugFix] Fix hard-coded timeout for multi-API-server startup (#43768)
  _Files: `vllm/v1/utils.py`_
- **2026-05-28** [`1b16f2ddc9`](https://github.com/vllm-project/vllm/commit/1b16f2ddc9) [#43600](https://github.com/vllm-project/vllm/pull/43600)
  change name of fs_python secondary tier to fs. (#43600)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/test_fs_tier.py`, `vllm/v1/kv_offload/tiering/factory.py`, `vllm/v1/kv_offload/tiering/fs/thread_pool.py`_
- **2026-05-28** [`05eec7120e`](https://github.com/vllm-project/vllm/commit/05eec7120e) [#43464](https://github.com/vllm-project/vllm/pull/43464)
  Fix RunAI streamer tensor buffer reuse during weight loading (#43464)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/test_weight_utils.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-05-27** [`094124af15`](https://github.com/vllm-project/vllm/commit/094124af15) [#43740](https://github.com/vllm-project/vllm/pull/43740)
  Add @AndreasKaratzas to CODEOWNERS (#43740)
  _Files: `.github/CODEOWNERS`_
- **2026-05-27** [`2c2c966669`](https://github.com/vllm-project/vllm/commit/2c2c966669) [#43794](https://github.com/vllm-project/vllm/pull/43794)
  Validate against some config fields being set to 0 (#43794)
  _Files: `vllm/config/cache.py`, `vllm/config/model.py`_
- **2026-05-27** [`2272062471`](https://github.com/vllm-project/vllm/commit/2272062471) [#43731](https://github.com/vllm-project/vllm/pull/43731)
  [Kernel] Enable TritonW4A16LinearKernel as CUDA fallback for non-Marlin-aligned W4A16 shapes (#43731)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`_
- **2026-05-27** [`683033d4ba`](https://github.com/vllm-project/vllm/commit/683033d4ba) [#43175](https://github.com/vllm-project/vllm/pull/43175)
  [Frontend] Add MiniCPM5 XML tool call parser (#43175)
  _Files: `tests/tool_parsers/test_minicpm5xml_tool_parser.py`, `vllm/tool_parsers/__init__.py`, `vllm/tool_parsers/minicpm5xml_tool_parser.py`_
- **2026-05-27** [`8c94938cfb`](https://github.com/vllm-project/vllm/commit/8c94938cfb) [#43719](https://github.com/vllm-project/vllm/pull/43719)
  [MRV2][BugFix] Fix KV connector handling in spec decode case (#43719)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/v1/worker/gpu/kv_connector.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-27** [`0fa3114ae1`](https://github.com/vllm-project/vllm/commit/0fa3114ae1) [#43695](https://github.com/vllm-project/vllm/pull/43695)
  Fix test_aot_compile for torch 2.12 (#43695)
  _Files: `tests/compile/test_aot_compile.py`_
- **2026-05-27** [`0b68f21e7c`](https://github.com/vllm-project/vllm/commit/0b68f21e7c) [#43582](https://github.com/vllm-project/vllm/pull/43582)
  [Rust Frontend] Add reasoning/tool parser & renderer roundtrip tests (#43582)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/event.rs` _+7 more__
- **2026-05-26** [`771e1e48b1`](https://github.com/vllm-project/vllm/commit/771e1e48b1) [#43032](https://github.com/vllm-project/vllm/pull/43032)
  [CPU] Enable non-divisible GQA for decode workitems in mixed batches (#43032)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`_
- **2026-05-25** [`716d5294e6`](https://github.com/vllm-project/vllm/commit/716d5294e6) [#43583](https://github.com/vllm-project/vllm/pull/43583)
  [Misc] Print accuracy value for PD tests even on success  (#43583)
  _Files: `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_

## Models  (19 commits)

- **2026-06-01** [`de21863419`](https://github.com/vllm-project/vllm/commit/de21863419) [#43481](https://github.com/vllm-project/vllm/pull/43481)
  [Rust Frontend] Add InternLM2 tool parser (#43481)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/tool-parser/src/json/hermes.rs` _+6 more__
- **2026-06-01** [`1f6048abe5`](https://github.com/vllm-project/vllm/commit/1f6048abe5) [#42944](https://github.com/vllm-project/vllm/pull/42944)
  fix: glm5.1 pp model loading (#42944)
  _Files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`_
- **2026-05-30** [`e1105064b2`](https://github.com/vllm-project/vllm/commit/e1105064b2) [#43909](https://github.com/vllm-project/vllm/pull/43909)
  [Bug] Fix gemma4 MTP IMA issue when TP>1, `CUDA error: an illegal memory access was encountered` (#43909)
  _Files: `vllm/model_executor/models/gemma4_mtp.py`_
- **2026-05-29** [`60a7a2214f`](https://github.com/vllm-project/vllm/commit/60a7a2214f) [#37622](https://github.com/vllm-project/vllm/pull/37622)
  [Bugfix] Fix Step3 pipeline parallel KeyError for residual tensor (#37622)
  _Files: `vllm/model_executor/models/step3_text.py`_
- **2026-05-29** [`dfe8ba7c80`](https://github.com/vllm-project/vllm/commit/dfe8ba7c80) [#42288](https://github.com/vllm-project/vllm/pull/42288)
  Adjust design around encoder_cudagraph_forward (#42288)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py` _+4 more__
- **2026-05-29** [`7bd45da585`](https://github.com/vllm-project/vllm/commit/7bd45da585) [#43905](https://github.com/vllm-project/vllm/pull/43905)
  [DSv4] Move mHC tilelang kernels & Don't use CustomOP in dsv4/nvidia (#43905)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/kernels/mhc/tilelang.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py`, `vllm/model_executor/layers/mhc.py` _+2 more__
- **2026-05-28** [`085ac221a3`](https://github.com/vllm-project/vllm/commit/085ac221a3) [#43784](https://github.com/vllm-project/vllm/pull/43784)
  Deprecate `JAISLMHeadModel` (#43784)
  _Files: `docs/models/supported_models.md`, `tests/distributed/test_pipeline_parallel.py`, `tests/models/registry.py`, `vllm/model_executor/models/jais.py` _+4 more__
- **2026-05-28** [`9006204e90`](https://github.com/vllm-project/vllm/commit/9006204e90) [#42796](https://github.com/vllm-project/vllm/pull/42796)
  [MM][CG] Avoid over-padding Qwen2.5-VL encoder cudagraph window metadata (#42796)
  _Files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/v1/worker/encoder_cudagraph.py`, `vllm/v1/worker/encoder_cudagraph_defs.py`_
- **2026-05-28** [`61a1e30473`](https://github.com/vllm-project/vllm/commit/61a1e30473) [#43850](https://github.com/vllm-project/vllm/pull/43850)
  [Rust Frontend] Reduce Gemma4 tool parser args scan complexity (#43850)
  _Files: `rust/src/tool-parser/benches/gemma4.rs`, `rust/src/tool-parser/src/gemma4.rs`_
- **2026-05-28** [`4ec2817313`](https://github.com/vllm-project/vllm/commit/4ec2817313) [#43581](https://github.com/vllm-project/vllm/pull/43581)
  [Model][Bugfix] Rename weight_mapper to hf_to_vllm_mapper in LlamaNemotronVL pooling models (#43581)
  _Files: `vllm/model_executor/models/nemotron_vl.py`_
- **2026-05-28** [`b372ad3e90`](https://github.com/vllm-project/vllm/commit/b372ad3e90) [#42879](https://github.com/vllm-project/vllm/pull/42879)
  [Bugfix] Stream DeepSeek DSML tool-call argument deltas incrementally (#42879)
  _Files: `tests/tool_parsers/test_deepseekv32_tool_parser.py`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`, `vllm/tool_parsers/deepseekv32_tool_parser.py`_
- **2026-05-28** [`05ac829629`](https://github.com/vllm-project/vllm/commit/05ac829629) [#43243](https://github.com/vllm-project/vllm/pull/43243)
  fix: parse Qwen3 XML JSON arguments first (#43243)
  _Files: `tests/tool_parsers/test_qwen3coder_tool_parser.py`, `vllm/tool_parsers/qwen3xml_tool_parser.py`_
- **2026-05-27** [`41688e2dc7`](https://github.com/vllm-project/vllm/commit/41688e2dc7) [#43791](https://github.com/vllm-project/vllm/pull/43791)
  Fix early CUDA init (#43791)
  _Files: `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+1 more__
- **2026-05-26** [`193ce8812e`](https://github.com/vllm-project/vllm/commit/193ce8812e) [#43690](https://github.com/vllm-project/vllm/pull/43690)
  [DSv4] Drop _get_compressed_kv_buffer in DeepseekCompressor (#43690)
  _Files: `vllm/models/deepseek_v4/compressor.py`_
- **2026-05-26** [`ebd0692f80`](https://github.com/vllm-project/vllm/commit/ebd0692f80) [#38278](https://github.com/vllm-project/vllm/pull/38278)
  [Model] Use AutoWeightsLoader for InternLM2 (#38278)
  _Files: `vllm/model_executor/models/internlm2.py`_
- **2026-05-26** [`6f955986e1`](https://github.com/vllm-project/vllm/commit/6f955986e1) [#43579](https://github.com/vllm-project/vllm/pull/43579)
  [Bugfix][Model] Fix GPT2ForSequenceClassification sub-module prefix (#43579)
  _Files: `vllm/model_executor/models/gpt2.py`_
- **2026-05-26** [`f815c99954`](https://github.com/vllm-project/vllm/commit/f815c99954) [#43194](https://github.com/vllm-project/vllm/pull/43194)
  [Bugfix] fix device mismatch in MiniCPM-o-4_5 resampler (#43194)
  _Files: `vllm/model_executor/models/minicpmv.py`_
- **2026-05-25** [`5c1aec3dc0`](https://github.com/vllm-project/vllm/commit/5c1aec3dc0) [#42933](https://github.com/vllm-project/vllm/pull/42933)
  Reduce memory usage for granite_speech. (#42933)
  _Files: `vllm/model_executor/models/granite_speech.py`_
- **2026-05-25** [`b06813e872`](https://github.com/vllm-project/vllm/commit/b06813e872) [#43474](https://github.com/vllm-project/vllm/pull/43474)
  [Kernel] Add mhc_pre_big_fuse_with_norm_tilelang  (#43474)
  _Files: `vllm/_tilelang_ops.py`, `vllm/model_executor/kernels/mhc/tilelang.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+1 more__

## Multimodal  (15 commits)

- **2026-06-01** [`bd0aecdc08`](https://github.com/vllm-project/vllm/commit/bd0aecdc08) [#44146](https://github.com/vllm-project/vllm/pull/44146)
  [XPU][CI] Fix test_audio_in_video flake by using module-scoped server fixture (#44146)
  _Files: `tests/entrypoints/openai/chat_completion/test_audio_in_video.py`_
- **2026-06-01** [`1fd8bd02a4`](https://github.com/vllm-project/vllm/commit/1fd8bd02a4) [#44159](https://github.com/vllm-project/vllm/pull/44159)
  [Docs] Replace broken video url in examples (#44159)
  _Files: `docs/features/multimodal_inputs.md`, `examples/generate/multimodal/openai_chat_completion_client_for_multimodal.py`_
- **2026-05-31** [`6bdabbad5b`](https://github.com/vllm-project/vllm/commit/6bdabbad5b) [#43956](https://github.com/vllm-project/vllm/pull/43956)
  [CI/Build] Enable Step3p7ForConditionalGeneration testing (#43956)
  _Files: `tests/models/multimodal/processing/test_tensor_schema.py`, `tests/models/registry.py`_
- **2026-05-29** [`8fad266507`](https://github.com/vllm-project/vllm/commit/8fad266507) [#43974](https://github.com/vllm-project/vllm/pull/43974)
  [CI] Fix smoke test step key to bypass block gate (#43974)
  _Files: `.buildkite/image_build/image_build.yaml`_
- **2026-05-29** [`11dfa3169d`](https://github.com/vllm-project/vllm/commit/11dfa3169d) [#43857](https://github.com/vllm-project/vllm/pull/43857)
  Add vLLM library info to Hugging Face Hub requests (#43857)
  _Files: `tests/lora/test_utils.py`, `vllm/assets/video.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/lora/utils.py` _+9 more__
- **2026-05-29** [`648c3ebee6`](https://github.com/vllm-project/vllm/commit/648c3ebee6) [#43712](https://github.com/vllm-project/vllm/pull/43712)
  [CI] Separate non-root smoke tests from image build step (#43712)
  _Files: `.buildkite/image_build/image_build.yaml`_
- **2026-05-29** [`212deff2ec`](https://github.com/vllm-project/vllm/commit/212deff2ec) [#43575](https://github.com/vllm-project/vllm/pull/43575)
  [feat] add GlmgaProcessor specific logits in `glm4_1v.py` (#43575)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/multimodal/video.py`_
- **2026-05-29** [`1521173c17`](https://github.com/vllm-project/vllm/commit/1521173c17) [#43854](https://github.com/vllm-project/vllm/pull/43854)
  [Rust Frontend] Add `/version` endpoint using engine-reported value (#43854)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+13 more__
- **2026-05-28** [`69c9f19957`](https://github.com/vllm-project/vllm/commit/69c9f19957) [#41459](https://github.com/vllm-project/vllm/pull/41459)
  fix(frontend): Add multimodal placeholders to Gemma4 tool message template (#41459)
  _Files: `examples/tool_chat_template_gemma4.jinja`, `tests/renderers/test_gemma4_chat_template.py`_
- **2026-05-28** [`099024762c`](https://github.com/vllm-project/vllm/commit/099024762c) [#43670](https://github.com/vllm-project/vllm/pull/43670)
  [Rust Frontend] Optimize multimodal prompt expansion (#43670)
  _Files: `rust/src/chat/src/multimodal.rs`_
- **2026-05-28** [`9aa131f944`](https://github.com/vllm-project/vllm/commit/9aa131f944) [#43356](https://github.com/vllm-project/vllm/pull/43356)
  Add Cosmos3 Reasoner model (#43356)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_common.py`, `tests/models/multimodal/test_mapping.py`, `tests/models/registry.py` _+6 more__
- **2026-05-28** [`02606b0b09`](https://github.com/vllm-project/vllm/commit/02606b0b09) [#42965](https://github.com/vllm-project/vllm/pull/42965)
  [BUGFIX] Multimodal benchmark with MistralTokenizer (#42965)
  _Files: `vllm/benchmarks/datasets/datasets.py`_
- **2026-05-26** [`e19b9b1045`](https://github.com/vllm-project/vllm/commit/e19b9b1045) [#41303](https://github.com/vllm-project/vllm/pull/41303)
  [ci] Add arm64 ci image (#41303)
  _Files: `.buildkite/image_build/image_build.yaml`, `.buildkite/image_build/image_build_arm64.sh`, `docker/Dockerfile`, `requirements/test/cuda.in`_
- **2026-05-26** [`5d09f471f4`](https://github.com/vllm-project/vllm/commit/5d09f471f4) [#43636](https://github.com/vllm-project/vllm/pull/43636)
  [Misc] Support interleaved custom image benchmark datasets (#43636)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_custom_image_dataset.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-05-25** [`3df1c7c43e`](https://github.com/vllm-project/vllm/commit/3df1c7c43e) [#40275](https://github.com/vllm-project/vllm/pull/40275)
  [Docker] Non-root support for vllm-openai; add opt-in vllm-openai-nonroot target (#40275)
  _Files: `.buildkite/image_build/image_build.yaml`, `.pre-commit-config.yaml`, `docker/Dockerfile`, `docker/entrypoints/test_vllm_nonroot_entrypoint.sh` _+3 more__

## Attention  (11 commits)

- **2026-05-31** [`8b8546da1c`](https://github.com/vllm-project/vllm/commit/8b8546da1c) [#44118](https://github.com/vllm-project/vllm/pull/44118)
  docs: fix MLA attention docstring examples (#44118)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-05-29** [`d2889722ff`](https://github.com/vllm-project/vllm/commit/d2889722ff) [#43961](https://github.com/vllm-project/vllm/pull/43961)
  [Bugfix] Corrupted MLA + linear attention (#43961)
  _Files: `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-05-29** [`e8b5199973`](https://github.com/vllm-project/vllm/commit/e8b5199973) [#43565](https://github.com/vllm-project/vllm/pull/43565)
  [XPU] support MTP of gdn attention (#43565)
  _Files: `vllm/_xpu_ops.py`_
- **2026-05-28** [`9202ea6fda`](https://github.com/vllm-project/vllm/commit/9202ea6fda) [#43445](https://github.com/vllm-project/vllm/pull/43445)
  [Spec Decode] Allow causal DFlash (#43445)
  _Files: `vllm/v1/spec_decode/dflash.py`_
- **2026-05-28** [`69b8956dcd`](https://github.com/vllm-project/vllm/commit/69b8956dcd) [#43891](https://github.com/vllm-project/vllm/pull/43891)
  [Model Refactoring] Remove unncessary torch op registration for DSv4 (#43891)
  _Files: `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-05-28** [`53a2088675`](https://github.com/vllm-project/vllm/commit/53a2088675) [#43330](https://github.com/vllm-project/vllm/pull/43330)
  Allow native KV cache dtype in Triton cache update (#43330)
  _Files: `vllm/v1/attention/ops/triton_reshape_and_cache_flash.py`_
- **2026-05-27** [`7fb9c0197a`](https://github.com/vllm-project/vllm/commit/7fb9c0197a) [#43733](https://github.com/vllm-project/vllm/pull/43733)
  [Bugfix][DFlash]allocate the proper number of lookahead slots (#43733)
  _Files: `vllm/v1/core/sched/scheduler.py`_
- **2026-05-27** [`158289e0fc`](https://github.com/vllm-project/vllm/commit/158289e0fc) [#43697](https://github.com/vllm-project/vllm/pull/43697)
  [Docs] Fix MLA prefill backend default docs (#43697)
  _Files: `docs/design/attention_backends.md`, `tools/pre_commit/generate_attention_backend_docs.py`_
- **2026-05-27** [`aa6138169f`](https://github.com/vllm-project/vllm/commit/aa6138169f) [#43325](https://github.com/vllm-project/vllm/pull/43325)
  [MLA][Attention] Add OOT MLA prefill backend registration mechanism (#43325)
  _Files: `tests/v1/attention/test_mla_prefill_registry.py`, `vllm/v1/attention/backends/mla/prefill/__init__.py`, `vllm/v1/attention/backends/mla/prefill/registry.py`_
- **2026-05-27** [`dede691c95`](https://github.com/vllm-project/vllm/commit/dede691c95) [#43543](https://github.com/vllm-project/vllm/pull/43543)
  [Bugfix] Split attention groups by num_heads_q for spec-decode drafts (#43543)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-26** [`d56612c621`](https://github.com/vllm-project/vllm/commit/d56612c621) [#43273](https://github.com/vllm-project/vllm/pull/43273)
  [GDN] GDN Prefill kernel for SM100 (#43273)
  _Files: `tests/kernels/mamba/test_gdn_prefill_cutedsl.py`, `vllm/cute_utils/__init__.py`, `vllm/cute_utils/_tcgen05.py`, `vllm/cute_utils/cvt.py` _+9 more__

## Serving / API  (10 commits)

- **2026-06-01** [`f46e6be169`](https://github.com/vllm-project/vllm/commit/f46e6be169) [#36254](https://github.com/vllm-project/vllm/pull/36254)
  [Misc] Use VLLMValidationError consistently in chat completion and completion protocol validators (#36254)
  _Files: `tests/tool_use/test_chat_completion_request_validations.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-05-29** [`8c6daf6e2f`](https://github.com/vllm-project/vllm/commit/8c6daf6e2f) [#44023](https://github.com/vllm-project/vllm/pull/44023)
  [CI] Remove duplicate Harmony test coverage (#44023)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/chat_completion/test_serving_chat_stream_harmony.py`_
- **2026-05-29** [`46409fd2a1`](https://github.com/vllm-project/vllm/commit/46409fd2a1) [#44009](https://github.com/vllm-project/vllm/pull/44009)
  [Fronten] Clean up stop_token_ids override for Harmony (#44009)
  _Files: `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-05-29** [`5dbf1605a0`](https://github.com/vllm-project/vllm/commit/5dbf1605a0) [#43688](https://github.com/vllm-project/vllm/pull/43688)
  [Feature] SSL support for dp supervisor (#43688)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/entrypoints/openai/dp_supervisor.py`_
- **2026-05-29** [`87f12e5c7c`](https://github.com/vllm-project/vllm/commit/87f12e5c7c) [#43761](https://github.com/vllm-project/vllm/pull/43761)
  [Frontend]Responses API supports chat_template_kwargs (#43761)
  _Files: `vllm/entrypoints/openai/responses/serving.py`_
- **2026-05-28** [`d692b89c2c`](https://github.com/vllm-project/vllm/commit/d692b89c2c) [#42396](https://github.com/vllm-project/vllm/pull/42396)
  [Feature] Add structured output and effort support to Anthropic Messages API (#42396)
  _Files: `tests/entrypoints/anthropic/test_messages.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-05-28** [`7909f82a45`](https://github.com/vllm-project/vllm/commit/7909f82a45) [#42683](https://github.com/vllm-project/vllm/pull/42683)
  [Bugfix][Frontend] streaming tool-call serializer drops first args chunk when name and args share a DeltaMessage  (#42683)
  _Files: `tests/entrypoints/openai/responses/test_serving_responses.py`, `tests/entrypoints/openai/responses/test_streaming_events.py`, `vllm/entrypoints/openai/responses/serving.py`, `vllm/entrypoints/openai/responses/streaming_events.py`_
- **2026-05-27** [`52a31ccecc`](https://github.com/vllm-project/vllm/commit/52a31ccecc) [#43401](https://github.com/vllm-project/vllm/pull/43401)
  [Bugfix] Map reasoning_effort to enable_thinking in chat template kwargs (#43401)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/openai/test_reasoning_enable_thinking.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-05-26** [`739af5c7e1`](https://github.com/vllm-project/vllm/commit/739af5c7e1) [#43402](https://github.com/vllm-project/vllm/pull/43402)
  [Reasoning] [Bugfix] Reject invalid thinking_token_budget values (#43402)
  _Files: `tests/entrypoints/openai/chat_completion/test_thinking_token_budget_validation.py`, `tests/v1/logits_processors/test_correctness.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py` _+1 more__
- **2026-05-26** [`d5cf7b4a2c`](https://github.com/vllm-project/vllm/commit/d5cf7b4a2c) [#43553](https://github.com/vllm-project/vllm/pull/43553)
  [Frontend] Split the offline inference APIs and utils. (#43553)
  _Files: `tests/entrypoints/llm/test_mm_processor_kwargs.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/entrypoints/llm.py`, `vllm/entrypoints/offline_utils.py` _+1 more__

## Docs  (10 commits)

- **2026-05-30** [`50c80d7923`](https://github.com/vllm-project/vllm/commit/50c80d7923) [#44047](https://github.com/vllm-project/vllm/pull/44047)
  [Governance] Add @BugenZhao as Rust frontend code owner (#44047)
  _Files: `.github/CODEOWNERS`, `docs/governance/committers.md`_
- **2026-05-29** [`f191d5630e`](https://github.com/vllm-project/vllm/commit/f191d5630e) [#43922](https://github.com/vllm-project/vllm/pull/43922)
  docs: clarify ITL acronym in optimization docs (#43922)
  _Files: `docs/configuration/optimization.md`_
- **2026-05-29** [`0585b5ba2e`](https://github.com/vllm-project/vllm/commit/0585b5ba2e) [#43972](https://github.com/vllm-project/vllm/pull/43972)
  Skip docs build if PR doesn't affect docs (#43972)
  _Files: `.readthedocs.yaml`, `docs/pre_run_check.sh`_
- **2026-05-29** [`30c6289b8e`](https://github.com/vllm-project/vllm/commit/30c6289b8e) [#43947](https://github.com/vllm-project/vllm/pull/43947)
  [XPU] fix xpu install document triton-xpu version (#43947)
  _Files: `docs/getting_started/installation/gpu.xpu.inc.md`_
- **2026-05-27** [`49a3510266`](https://github.com/vllm-project/vllm/commit/49a3510266) [#43546](https://github.com/vllm-project/vllm/pull/43546)
  [Docs] Fix the duplicate doc icon issue (#43546)
  _Files: `docs/mkdocs/hooks/url_schemes.py`_
- **2026-05-27** [`ad464e16c0`](https://github.com/vllm-project/vllm/commit/ad464e16c0) [#43550](https://github.com/vllm-project/vllm/pull/43550)
  [Doc] Add Ascend NPU tab to the quickstart installation guide (#43550)
  _Files: `docs/getting_started/quickstart.md`, `pyproject.toml`_
- **2026-05-27** [`c02c758ea4`](https://github.com/vllm-project/vllm/commit/c02c758ea4) [#43358](https://github.com/vllm-project/vllm/pull/43358)
  [Deprecation] Deprecate functions as scheduled for v0.21.0 (#43358)
  _Files: `docs/contributing/profiling.md`, `docs/models/pooling_models/classify.md`, `vllm/config/pooler.py`, `vllm/utils/profiling.py`_
- **2026-05-26** [`3aea37d28e`](https://github.com/vllm-project/vllm/commit/3aea37d28e) [#43635](https://github.com/vllm-project/vllm/pull/43635)
  [Doc] Add line limit to AGENTS.md (#43635)
  _Files: `AGENTS.md`_
- **2026-05-25** [`0c942c69d6`](https://github.com/vllm-project/vllm/commit/0c942c69d6) [#43568](https://github.com/vllm-project/vllm/pull/43568)
  [Doc] Add section on escalating stalled contributions (#43568)
  _Files: `docs/contributing/README.md`_
- **2026-05-25** [`1b26fa361e`](https://github.com/vllm-project/vllm/commit/1b26fa361e) [#43552](https://github.com/vllm-project/vllm/pull/43552)
  [Docs] Reorganize offline inference docs.  (#43552)
  _Files: `docs/serving/offline_inference.md`_

## Scheduler / Engine  (10 commits)

- **2026-05-29** [`8b9deeec4b`](https://github.com/vllm-project/vllm/commit/8b9deeec4b) [#43998](https://github.com/vllm-project/vllm/pull/43998)
  [Bugfix] Fix Ray placement group allocation with grouped nodes (#43998)
  _Files: `vllm/v1/engine/utils.py`_
- **2026-05-29** [`bf18d7e0b4`](https://github.com/vllm-project/vllm/commit/bf18d7e0b4) [#43270](https://github.com/vllm-project/vllm/pull/43270)
  [Misc][NUMA] Auto-bind to PCT priority cores on DGX B300 + widen EngineCore across shard NUMA nodes (#43270)
  _Files: `tests/utils_/test_numa_utils.py`, `vllm/config/parallel.py`, `vllm/utils/numa_utils.py`_
- **2026-05-28** [`5d126dd155`](https://github.com/vllm-project/vllm/commit/5d126dd155) [#43864](https://github.com/vllm-project/vllm/pull/43864)
  [Bugfix] Exclude Ray DP from #42585's deferred port allocation (#43864)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `vllm/entrypoints/cli/serve.py`_
- **2026-05-28** [`577d693838`](https://github.com/vllm-project/vllm/commit/577d693838) [#43429](https://github.com/vllm-project/vllm/pull/43429)
  [rust] fix: aggregate `is_sleeping` and `reset_prefix_cache` across DP engines (#43429)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/error.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-05-28** [`c1c4db8b4b`](https://github.com/vllm-project/vllm/commit/c1c4db8b4b) [#41406](https://github.com/vllm-project/vllm/pull/41406)
  Log dummy DP step in iteration details (#41406)
  _Files: `vllm/v1/engine/core.py`_
- **2026-05-28** [`f2caefe226`](https://github.com/vllm-project/vllm/commit/f2caefe226) [#42343](https://github.com/vllm-project/vllm/pull/42343)
  [UX] Increase DP Coordinator startup timeout from 30s to 120s (#42343)
  _Files: `vllm/v1/engine/coordinator.py`_
- **2026-05-28** [`626fa9bba5`](https://github.com/vllm-project/vllm/commit/626fa9bba5) [#43808](https://github.com/vllm-project/vllm/pull/43808)
  [BugFix] Fix blocked reasoning parsing with MRV2 (#43808)
  _Files: `tests/entrypoints/openai/chat_completion/test_thinking_token_budget.py`, `vllm/config/vllm.py`, `vllm/v1/engine/input_processor.py`_
- **2026-05-28** [`c87f62ccf8`](https://github.com/vllm-project/vllm/commit/c87f62ccf8) [#43469](https://github.com/vllm-project/vllm/pull/43469)
  [Rust Frontend] Introduce mock engine for benchmark baseline (#43469)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/cmd/Cargo.toml`, `rust/src/cmd/src/main.rs` _+15 more__
- **2026-05-27** [`165460941f`](https://github.com/vllm-project/vllm/commit/165460941f) [#39155](https://github.com/vllm-project/vllm/pull/39155)
  [BugFix] HFValidationError with cloud storage URIs when HF_HUB_OFFLINE=1 (#39155)
  _Files: `tests/engine/test_arg_utils.py`, `tests/test_config.py`, `vllm/config/model.py`, `vllm/engine/arg_utils.py`_
- **2026-05-26** [`812e7e7364`](https://github.com/vllm-project/vllm/commit/812e7e7364) [#42585](https://github.com/vllm-project/vllm/pull/42585)
  [Bugfix][V1] Fix TOCTOU race causing intermittent `EADDRINUSE` on multi-API-server DP startup (#42585)
  _Files: `tests/entrypoints/test_api_server_process_manager.py`, `vllm/entrypoints/cli/serve.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/coordinator.py` _+3 more__

## Disaggregation / PD  (10 commits)

- **2026-05-29** [`d63108fb18`](https://github.com/vllm-project/vllm/commit/d63108fb18) [#43797](https://github.com/vllm-project/vllm/pull/43797)
  [kv_offload] Skip decode-phase blocks in CPU offload (#43797)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py`_
- **2026-05-28** [`864990e8d9`](https://github.com/vllm-project/vllm/commit/864990e8d9) [#39983](https://github.com/vllm-project/vllm/pull/39983)
  Add token-offset based selective offload in OffloadConnector (#39983)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-05-28** [`811d805195`](https://github.com/vllm-project/vllm/commit/811d805195) [#42423](https://github.com/vllm-project/vllm/pull/42423)
  [EC Connector] Add shutdown API to EC Connector. (#42423)
  _Files: `vllm/distributed/ec_transfer/__init__.py`, `vllm/distributed/ec_transfer/ec_connector/base.py`, `vllm/distributed/ec_transfer/ec_transfer_state.py`, `vllm/v1/core/sched/scheduler.py` _+1 more__
- **2026-05-28** [`e1814f822d`](https://github.com/vllm-project/vllm/commit/e1814f822d) [#43830](https://github.com/vllm-project/vllm/pull/43830)
  minor docs: fix incorrect example path (#43830)
  _Files: `docs/features/mooncake_connector_usage.md`_
- **2026-05-27** [`1fc2cee50a`](https://github.com/vllm-project/vllm/commit/1fc2cee50a) [#42694](https://github.com/vllm-project/vllm/pull/42694)
  [KVConnector][Mooncake] Wire reset_cache cascade end-to-end (#42694)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/protocol.py` _+4 more__
- **2026-05-26** [`d98cbf472b`](https://github.com/vllm-project/vllm/commit/d98cbf472b) [#43627](https://github.com/vllm-project/vllm/pull/43627)
  [KV Connector] MooncakeStore: drop dead discard_partial_chunks parameter (#43627)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`_
- **2026-05-26** [`755043cf3c`](https://github.com/vllm-project/vllm/commit/755043cf3c) [#41847](https://github.com/vllm-project/vllm/pull/41847)
  [KV Transfer] Enable HMA by default for connectors that support it (#41847)
  _Files: `tests/v1/kv_connector/unit/test_hma_auto_config.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py` _+3 more__
- **2026-05-26** [`c2a4005c70`](https://github.com/vllm-project/vllm/commit/c2a4005c70) [#42788](https://github.com/vllm-project/vllm/pull/42788)
  [KV Connector] Propagate MooncakeStore load failures (#42788)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-05-25** [`873758c13a`](https://github.com/vllm-project/vllm/commit/873758c13a) [#43281](https://github.com/vllm-project/vllm/pull/43281)
  [KV Connector] Handle Mooncake finish after preemption (#43281)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`_
- **2026-05-25** [`81252d4e24`](https://github.com/vllm-project/vllm/commit/81252d4e24) [#42296](https://github.com/vllm-project/vllm/pull/42296)
  [Feat][KVConnector] Support DSV4 in SimpleCPUOffloadBackend (#42296)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/manager.py`_

## Quantization  (9 commits)

- **2026-06-01** [`985c97a6a8`](https://github.com/vllm-project/vllm/commit/985c97a6a8) [#43706](https://github.com/vllm-project/vllm/pull/43706)
  [Perf] Optimize cutlass fp8 scaled mm bypassing padding, 20% kernel performance improvement (#43706)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`_
- **2026-05-30** [`124fac10cb`](https://github.com/vllm-project/vllm/commit/124fac10cb) [#42379](https://github.com/vllm-project/vllm/pull/42379)
  [Bugfix] Fix RMSNorm kernels to multiply in weight's native dtype (#42379)
  _Files: `csrc/libtorch_stable/layernorm_kernels.cu`, `csrc/libtorch_stable/layernorm_quant_kernels.cu`_
- **2026-05-28** [`20d69d100a`](https://github.com/vllm-project/vllm/commit/20d69d100a) [#43841](https://github.com/vllm-project/vllm/pull/43841)
  [CPU] Migrate cpu_awq into awq_marlin (#43841)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `vllm/config/model.py`, `vllm/model_executor/kernels/linear/mixed_precision/cpu.py`, `vllm/model_executor/layers/quantization/__init__.py` _+3 more__
- **2026-05-27** [`206b72c982`](https://github.com/vllm-project/vllm/commit/206b72c982) [#43540](https://github.com/vllm-project/vllm/pull/43540)
  [Quantization] Fix Humming RoutedExperts import (#43540)
  _Files: `vllm/model_executor/layers/quantization/utils/humming_utils.py`_
- **2026-05-27** [`d8eebe6d97`](https://github.com/vllm-project/vllm/commit/d8eebe6d97) [#43677](https://github.com/vllm-project/vllm/pull/43677)
  [Perf] Optimize Fp8BlockScaledMMLinearKernel input_scale tensor using new_empty() (#43677)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/BlockScaledMMLinearKernel.py`_
- **2026-05-26** [`6f5b533241`](https://github.com/vllm-project/vllm/commit/6f5b533241) [#42124](https://github.com/vllm-project/vllm/pull/42124)
  Add LM head quantization support for ModelOpt (#42124)
  _Files: `tests/model_executor/test_nemotron_h_quantization.py`, `tests/model_executor/test_qwen3_5_quantization.py`, `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+4 more__
- **2026-05-26** [`a970fb5a1a`](https://github.com/vllm-project/vllm/commit/a970fb5a1a) [#43530](https://github.com/vllm-project/vllm/pull/43530)
  Fix CuPy runtime deps and restore humming (#43530)
  _Files: `docker/Dockerfile`, `requirements/cuda.txt`, `requirements/kv_connectors.txt`, `setup.py` _+1 more__
- **2026-05-26** [`b3269454b1`](https://github.com/vllm-project/vllm/commit/b3269454b1) [#43045](https://github.com/vllm-project/vllm/pull/43045)
  [chores][log] change registry log from `warning` to `debug` (#43045)
  _Files: `tests/quantization/test_register_quantization_config.py`, `vllm/model_executor/layers/quantization/__init__.py`, `vllm/model_executor/models/registry.py`_
- **2026-05-26** [`a37e47100c`](https://github.com/vllm-project/vllm/commit/a37e47100c) [#43584](https://github.com/vllm-project/vllm/pull/43584)
  Add CuTe DSL sparse compressor support (#43584)
  _Files: `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/common/ops/sparse_attn_compress_cutedsl.py`, `vllm/models/deepseek_v4/compressor.py`_

## CI / Build  (9 commits)

- **2026-06-01** [`98f1279815`](https://github.com/vllm-project/vllm/commit/98f1279815) [#42730](https://github.com/vllm-project/vllm/pull/42730)
  [CPU][RISC-V] Add missing RVV cpu_types helpers for WNA16 (#42730)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_impl.hpp`, `csrc/cpu/torch_bindings.cpp`_
- **2026-05-29** [`6aabe221a5`](https://github.com/vllm-project/vllm/commit/6aabe221a5) [#43971](https://github.com/vllm-project/vllm/pull/43971)
  [CI] Make Model Executor test hangs fail fast with a traceback (#43971)
  _Files: `.buildkite/test_areas/model_executor.yaml`_
- **2026-05-29** [`3f6f508e14`](https://github.com/vllm-project/vllm/commit/3f6f508e14) [#43977](https://github.com/vllm-project/vllm/pull/43977)
  [Bugfix][CPU] Remove invalid extra deps (#43977)
  _Files: `docker/Dockerfile.cpu`, `setup.py`_
- **2026-05-29** [`7ebc0ec104`](https://github.com/vllm-project/vllm/commit/7ebc0ec104) [#43871](https://github.com/vllm-project/vllm/pull/43871)
  [CI] Nixl+SimpleCPUOffloadingConnector unit tests (#43871)
  _Files: `tests/v1/kv_connector/unit/test_nixl_simple_cpu_offload.py`_
- **2026-05-28** [`03f03f9630`](https://github.com/vllm-project/vllm/commit/03f03f9630) [#43901](https://github.com/vllm-project/vllm/pull/43901)
  Refactor output filename handling in ci-fetch-log.sh (#43901)
  _Files: `.buildkite/scripts/ci-fetch-log.sh`_
- **2026-05-28** [`8e0580f4ee`](https://github.com/vllm-project/vllm/commit/8e0580f4ee) [#43866](https://github.com/vllm-project/vllm/pull/43866)
  [CI] Auto-apply `rust` label to relevant PRs (#43866)
  _Files: `.github/mergify.yml`_
- **2026-05-27** [`2616f67faa`](https://github.com/vllm-project/vllm/commit/2616f67faa) [#43785](https://github.com/vllm-project/vllm/pull/43785)
  Remove Transformers forward/backward compatibility tests (#43785)
  _Files: `.buildkite/test_areas/models_basic.yaml`_
- **2026-05-27** [`03d9cc2fe2`](https://github.com/vllm-project/vllm/commit/03d9cc2fe2) [#43745](https://github.com/vllm-project/vllm/pull/43745)
  [misc] Bump cutedsl version to 4.5.2 (#43745)
  _Files: `requirements/cuda.txt`_
- **2026-05-26** [`e6adbd7834`](https://github.com/vllm-project/vllm/commit/e6adbd7834) [#43394](https://github.com/vllm-project/vllm/pull/43394)
  Upgrade tpu-inference to v0.20.0 (#43394)
  _Files: `requirements/tpu.txt`_

## Speculative Decoding  (5 commits)

- **2026-06-01** [`4721bb3aa4`](https://github.com/vllm-project/vllm/commit/4721bb3aa4) [#44078](https://github.com/vllm-project/vllm/pull/44078)
  [MRV2] Remove Eagle's dedicated CUDA graph pool (#44078)
  _Files: `vllm/v1/worker/gpu/spec_decode/eagle/cudagraph.py`, `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py`_
- **2026-05-30** [`27fa5aa3b9`](https://github.com/vllm-project/vllm/commit/27fa5aa3b9) [#44050](https://github.com/vllm-project/vllm/pull/44050)
  [MRV2] Support breakable CUDA graph (#44050)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py`_
- **2026-05-28** [`1223732dda`](https://github.com/vllm-project/vllm/commit/1223732dda) [#38831](https://github.com/vllm-project/vllm/pull/38831)
  [ModelRunnerV2][Hybrid model] Support kernel block size in hybrid model (#38831)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/model_runner.py` _+1 more__
- **2026-05-26** [`97e4022c6c`](https://github.com/vllm-project/vllm/commit/97e4022c6c) [#43482](https://github.com/vllm-project/vllm/pull/43482)
  [Bugfix] Apply fc_norm in Eagle3DeepseekV2 combine_hidden_states (#43482)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`_
- **2026-05-26** [`7966fc7233`](https://github.com/vllm-project/vllm/commit/7966fc7233) [#43516](https://github.com/vllm-project/vllm/pull/43516)
  [KV Connector][Bugfix] MooncakeStore: don't double-apply Eagle prune in load_mask (#43516)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`_

## KV Cache / Offload  (4 commits)

- **2026-05-29** [`d07ad0693b`](https://github.com/vllm-project/vllm/commit/d07ad0693b) [#43988](https://github.com/vllm-project/vllm/pull/43988)
  [Bugfix] Use storage_block_size in KV cache reshape for compressed specs (DeepSeek V4) (#43988)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-05-28** [`325a1ec4fb`](https://github.com/vllm-project/vllm/commit/325a1ec4fb) [#43925](https://github.com/vllm-project/vllm/pull/43925)
  [CI] Enable prefix caching in BFCL benchmark (#43925)
  _Files: `.buildkite/scripts/tool_call/run-bfcl-eval.sh`_
- **2026-05-28** [`a3ed5ab10c`](https://github.com/vllm-project/vllm/commit/a3ed5ab10c) [#43205](https://github.com/vllm-project/vllm/pull/43205)
  [KV Offload] Add per-request offloading policy via `on_new_request` lifecycle hook (#43205)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py` _+7 more__
- **2026-05-28** [`4bfa0f2b14`](https://github.com/vllm-project/vllm/commit/4bfa0f2b14) [#43870](https://github.com/vllm-project/vllm/pull/43870)
  [KV Offload] Rename `SecondaryTierManager.get_finished()` to `get_finished_jobs()` (#43870)
  _Files: `tests/v1/kv_offload/test_fs_tier.py`, `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/example/manager.py` _+2 more__

## Perf / Benchmark  (3 commits)

- **2026-05-28** [`c08ebebf30`](https://github.com/vllm-project/vllm/commit/c08ebebf30) [#43803](https://github.com/vllm-project/vllm/pull/43803)
  [Perf] Add do_not_specialize to Mamba SSD chunk kernels (#43803)
  _Files: `vllm/model_executor/layers/mamba/ops/causal_conv1d.py`, `vllm/model_executor/layers/mamba/ops/ssd_bmm.py`, `vllm/model_executor/layers/mamba/ops/ssd_chunk_scan.py`, `vllm/model_executor/layers/mamba/ops/ssd_chunk_state.py`_
- **2026-05-28** [`f3b2a819f7`](https://github.com/vllm-project/vllm/commit/f3b2a819f7) [#43667](https://github.com/vllm-project/vllm/pull/43667)
  [Perf][KDA] Fuse gate softplus, chunk-local cumsum, and RCP_LN2 scaling (#43667)
  _Files: `tests/kernels/test_kda.py`, `vllm/model_executor/layers/fla/ops/kda.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`_
- **2026-05-28** [`bfb9ebc211`](https://github.com/vllm-project/vllm/commit/bfb9ebc211) [#39795](https://github.com/vllm-project/vllm/pull/39795)
  [Feature] Add support for timed trace replay in `vllm bench serve` to replay Moonshot and Alibaba workload traces (#39795)
  _Files: `docs/benchmarking/cli.md`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/serve.py`_

---
_Generated 2026-06-01 13:47 UTC_