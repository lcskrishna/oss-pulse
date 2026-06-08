# vllm-project/vllm — Weekly Change Report
**Period:** 2026-06-01 → 2026-06-08  |  **Total commits:** 248

## ✨ New Features This Week

- **2026-06-08** [#44499](https://github.com/vllm-project/vllm/pull/44499) — [Rust Frontend] Add /pause, /resume, /is_paused endpoints (#44499)
- **2026-06-08** [#43663](https://github.com/vllm-project/vllm/pull/43663) — [XPU][CI] Add more test cases in Intel GPU CI (#43663)
- **2026-06-08** [#44771](https://github.com/vllm-project/vllm/pull/44771) — [XPU][Minor] format moe kernel name and add in kernel list (#44771)
- **2026-06-08** [#42953](https://github.com/vllm-project/vllm/pull/42953) — [XPU]feat: add DeepSeek-V4 XPU attention decode path (#42953)
- **2026-06-07** [#44674](https://github.com/vllm-project/vllm/pull/44674) — [ROCm][Kernel] Enable permute_cols for ROCm (#44674)
- **2026-06-07** [#44417](https://github.com/vllm-project/vllm/pull/44417) — [videoloader] implement glm46v video loader (#44417)
- **2026-06-07** [#44707](https://github.com/vllm-project/vllm/pull/44707) — [Cohere] Enable Cohere Mini Code model and update Command A-plus test registry (#44707)
- **2026-06-07** [#44420](https://github.com/vllm-project/vllm/pull/44420) — [feature] add index share feature for DSA MTP (#44420)
- **2026-06-07** [#44540](https://github.com/vllm-project/vllm/pull/44540) — [XPU] add xpu branch in compressed_tensors_moe_w4a4_mxfp4 (#44540)
- **2026-06-07** [#37149](https://github.com/vllm-project/vllm/pull/37149) — [XPU][Feature] transparent sleep mode support for XPU platform (#37149)
- _…and 51 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-08** [`93ee4cd47f`](https://github.com/vllm-project/vllm/commit/93ee4cd47f) [#44819](https://github.com/vllm-project/vllm/pull/44819) — [CI] Consolidate multimodal entrypoint tests. (#44819)
- **2026-06-08** [`5add018beb`](https://github.com/vllm-project/vllm/commit/5add018beb) [#44854](https://github.com/vllm-project/vllm/pull/44854) — [Connector] Remove `P2pNcclConnector` (#44854)
- **2026-06-08** [`d9ff7e4e9a`](https://github.com/vllm-project/vllm/commit/d9ff7e4e9a) [#44761](https://github.com/vllm-project/vllm/pull/44761) — [ROCm][CI] Stabilizing teardown and timeout of flaky tests to prevent rare OOMs (#44761)
- **2026-06-08** [`967c5c3bc3`](https://github.com/vllm-project/vllm/commit/967c5c3bc3) [#42793](https://github.com/vllm-project/vllm/pull/42793) — [ROCm][CI] Stage C mirrors (#42793)
- **2026-06-07** [`228bcc436b`](https://github.com/vllm-project/vllm/commit/228bcc436b) [#44674](https://github.com/vllm-project/vllm/pull/44674) — [ROCm][Kernel] Enable permute_cols for ROCm (#44674)
- **2026-06-07** [`3bb46975bd`](https://github.com/vllm-project/vllm/commit/3bb46975bd) [#37149](https://github.com/vllm-project/vllm/pull/37149) — [XPU][Feature] transparent sleep mode support for XPU platform (#37149)
- **2026-06-07** [`2a983c79ac`](https://github.com/vllm-project/vllm/commit/2a983c79ac) [#44699](https://github.com/vllm-project/vllm/pull/44699) — [DSV4] Decouple DS V4 Sparse MLA Metadata from DS V3.2 (#44699)
- **2026-06-06** [`bc5745a00f`](https://github.com/vllm-project/vllm/commit/bc5745a00f) [#42838](https://github.com/vllm-project/vllm/pull/42838) — [ROCm][MLA] Replace torch.cat in sparse-MLA forward_mqa with fused concat_mla_q (#42838)
- **2026-06-06** [`062b05ff3a`](https://github.com/vllm-project/vllm/commit/062b05ff3a) [#44075](https://github.com/vllm-project/vllm/pull/44075) — [ROCm][Perf] Fused MoE W4A16 HIP kernel for AMD RDNA3 (gfx1100) (#44075)
- **2026-06-06** [`00d1fb7747`](https://github.com/vllm-project/vllm/commit/00d1fb7747) [#43684](https://github.com/vllm-project/vllm/pull/43684) — [Bugfix][ROCm] `ApplyRotaryEmb`: fall back to native when flash_attn rotary grid would exceed the HIP per-dim limit (#43684)
- **2026-06-05** [`4200f62147`](https://github.com/vllm-project/vllm/commit/4200f62147) [#42832](https://github.com/vllm-project/vllm/pull/42832) — [ROCm][GPT-OSS] Fuse RoPE + static Q FP8 quant on fused RoPE+KV path (#42832)
- **2026-06-05** [`aa6fb8a329`](https://github.com/vllm-project/vllm/commit/aa6fb8a329) [#44648](https://github.com/vllm-project/vllm/pull/44648) — [Bugfix] [ROCm] [Critical] fallback to regular abi for ROCm (#44648)
- **2026-06-05** [`c66b19800b`](https://github.com/vllm-project/vllm/commit/c66b19800b) [#44649](https://github.com/vllm-project/vllm/pull/44649) — [CI] Bump mistral-common (#44649)
- **2026-06-05** [`b4a6f26c90`](https://github.com/vllm-project/vllm/commit/b4a6f26c90) [#41002](https://github.com/vllm-project/vllm/pull/41002) — [ROCm][perf] Use workspace manager for sparse indexer allocations (#41002)
- **2026-06-05** [`165b7864d0`](https://github.com/vllm-project/vllm/commit/165b7864d0) [#40426](https://github.com/vllm-project/vllm/pull/40426) — [ROCM] [FEAT] Integrate Aiter hipBLASLt GEMM online tuning (#40426)
- **2026-06-05** [`4efd6ffde0`](https://github.com/vllm-project/vllm/commit/4efd6ffde0) [#44569](https://github.com/vllm-project/vllm/pull/44569) — [DSV4] Refactor DeepseekV4Attention (#44569)
- **2026-06-04** [`06f94633e7`](https://github.com/vllm-project/vllm/commit/06f94633e7) [#44436](https://github.com/vllm-project/vllm/pull/44436) — [ROCm][CI] Add test for Aiter unified attn kernel (#44436)
- **2026-06-04** [`06ee2d8433`](https://github.com/vllm-project/vllm/commit/06ee2d8433) [#44340](https://github.com/vllm-project/vllm/pull/44340) — [Quant] Support compressed-tensors WNA8O8Int linears and WNInt embeddings (#44340)
- **2026-06-04** [`b5235fca2e`](https://github.com/vllm-project/vllm/commit/b5235fca2e) [#43827](https://github.com/vllm-project/vllm/pull/43827) — [DSv4] Adding TRTLLM gen attention kernel (#43827)
- **2026-06-04** [`3e77036768`](https://github.com/vllm-project/vllm/commit/3e77036768) [#44255](https://github.com/vllm-project/vllm/pull/44255) — [ROCm][CI] Specifying time outs for the lm eval models (#44255)
- **2026-06-04** [`6f68ca3e91`](https://github.com/vllm-project/vllm/commit/6f68ca3e91) [#44046](https://github.com/vllm-project/vllm/pull/44046) — [ROCm][CI] Stabilize memory-release in the Hybrid model generation tests (#44046)
- **2026-06-04** [`0c96dd64fb`](https://github.com/vllm-project/vllm/commit/0c96dd64fb) [#43625](https://github.com/vllm-project/vllm/pull/43625) — [ROCm] Bump fastsafetensors to v0.3.2 from PyPI, remove git source build (#43625)
- **2026-06-04** [`22c2e87555`](https://github.com/vllm-project/vllm/commit/22c2e87555) [#44497](https://github.com/vllm-project/vllm/pull/44497) — [CI] Reverted gitignore changes (#44497)
- **2026-06-04** [`d01d0b4646`](https://github.com/vllm-project/vllm/commit/d01d0b4646) [#44479](https://github.com/vllm-project/vllm/pull/44479) — [Frontend] Consolidate online serving utils. (#44479)
- **2026-06-04** [`b4b4aaa70e`](https://github.com/vllm-project/vllm/commit/b4b4aaa70e) [#42129](https://github.com/vllm-project/vllm/pull/42129) — [Inductor] Fast-path Inductor fallback for vllm::*/vllm_aiter::* custom ops (#42129)
- **2026-06-04** [`5e2af28838`](https://github.com/vllm-project/vllm/commit/5e2af28838) [#44463](https://github.com/vllm-project/vllm/pull/44463) — [CI] Resolve release V2 docker build after ROCm CI wheels change (#44463)
- **2026-06-03** [`5b2a2beade`](https://github.com/vllm-project/vllm/commit/5b2a2beade) [#44370](https://github.com/vllm-project/vllm/pull/44370) — [ROCm][CI] Move Model Executor test step from MI250 to MI300 (gfx942) (#44370)
- **2026-06-03** [`87954eb50e`](https://github.com/vllm-project/vllm/commit/87954eb50e) [#36949](https://github.com/vllm-project/vllm/pull/36949) — [ROCm][CI] Optimize ROCm Docker build: registry cache, DeepEP, and ci-bake script (#36949)
- **2026-06-03** [`71df063c49`](https://github.com/vllm-project/vllm/commit/71df063c49) [#42758](https://github.com/vllm-project/vllm/pull/42758) — Enable perf_token_group_quant/_C_stable_libtorch for ROCm (#42758)
- **2026-06-03** [`7b476c8f14`](https://github.com/vllm-project/vllm/commit/7b476c8f14) [#44369](https://github.com/vllm-project/vllm/pull/44369) — [ROCm][CI] Skip fp8 reload tests on gfx90a (MI250) (#44369)
- **2026-06-03** [`4454a18695`](https://github.com/vllm-project/vllm/commit/4454a18695) [#44368](https://github.com/vllm-project/vllm/pull/44368) — [ROCm][CI] Fix stale wvSplitK GEMM fallback test for N=5 (#44368)
- **2026-06-02** [`88f172188b`](https://github.com/vllm-project/vllm/commit/88f172188b) [#44308](https://github.com/vllm-project/vllm/pull/44308) — [ROCm] Fix AITER RMSNormQuantFusion for Kimi-Linear (#44308)
- **2026-06-02** [`b623f7ea95`](https://github.com/vllm-project/vllm/commit/b623f7ea95) [#44170](https://github.com/vllm-project/vllm/pull/44170) — [Frontend] Consolidate dev entrypoints. (#44170)
- **2026-06-02** [`2588ec4f0a`](https://github.com/vllm-project/vllm/commit/2588ec4f0a) [#44265](https://github.com/vllm-project/vllm/pull/44265) — [ROCm] Upgrade AITER to v0.1.13.post1 (#44265)
- **2026-06-02** [`517e74a964`](https://github.com/vllm-project/vllm/commit/517e74a964) [#44262](https://github.com/vllm-project/vllm/pull/44262) — [DSV4] Refactor RoPE initialization (#44262)
- **2026-06-02** [`48c0d13e65`](https://github.com/vllm-project/vllm/commit/48c0d13e65) [#44256](https://github.com/vllm-project/vllm/pull/44256) — [ROCm][CI] Skip unbacked dynamic shapes tests on PyTorch < 2.11 (#44256)
- **2026-06-01** [`8c3cc98cff`](https://github.com/vllm-project/vllm/commit/8c3cc98cff) [#44246](https://github.com/vllm-project/vllm/pull/44246) — [DSV4] Remove unncessary classes & functions (#44246)
- **2026-06-01** [`fd9e91d7e4`](https://github.com/vllm-project/vllm/commit/fd9e91d7e4) [#41294](https://github.com/vllm-project/vllm/pull/41294) — [ROCm][CI] Fix and stabilize EAGLE3 acceptance tests (#41294)
- **2026-06-01** [`0910f7e0e1`](https://github.com/vllm-project/vllm/commit/0910f7e0e1) [#44153](https://github.com/vllm-project/vllm/pull/44153) — [Frontend] Resettle generative scoring entrypoint. (#44153)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#44878](https://github.com/vllm-project/vllm/issues/44878) | [Bug]: vllm serve hangs permanently with data_parallel_size > 1 on mul | bug | 2026-06-08 |
| [#42932](https://github.com/vllm-project/vllm/issues/42932) | [Bug]: vLLM wheel version mismatch  | bug | 2026-06-08 |
| [#44841](https://github.com/vllm-project/vllm/issues/44841) | [BUG]: Garbled/Corrupted output when serving deepseek-ai/DeepSeek-R1-0 | usage | 2026-06-08 |
| [#41663](https://github.com/vllm-project/vllm/issues/41663) | [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe  | bug, intel-gpu | 2026-06-08 |
| [#43428](https://github.com/vllm-project/vllm/issues/43428) | [Bug]: Endless '!' output when a long context request is sent on qwen3 | bug, intel-gpu | 2026-06-08 |
| [#44842](https://github.com/vllm-project/vllm/issues/44842) | [Bug]: Setting prompt_embeds does not work for vision-language models | bug | 2026-06-08 |
| [#44249](https://github.com/vllm-project/vllm/issues/44249) | [Bug]: lmcache_connector.start_load_kv asserts on degraded LMCache ins | bug | 2026-06-08 |
| [#33689](https://github.com/vllm-project/vllm/issues/33689) | [RFC]: KV Offloading Roadmap | RFC, keep-open | 2026-06-08 |
| [#44827](https://github.com/vllm-project/vllm/issues/44827) | [Bug]: Inference-time probabilistic error: pre-allocated buffer size m | bug | 2026-06-08 |
| [#44826](https://github.com/vllm-project/vllm/issues/44826) | [RFC]: MTP Routing for Qwen3.5 Series Multi-LoRA Deployments | RFC | 2026-06-08 |
| [#42082](https://github.com/vllm-project/vllm/issues/42082) | [RFC]: Standardize KV-cache Layouts | RFC | 2026-06-08 |
| [#25623](https://github.com/vllm-project/vllm/issues/25623) | [Bug]: torch.compile padding causes IMA on Hopper + DBO | bug, help wanted, torch.compile, stale | 2026-06-08 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-06-07 |
| [#35288](https://github.com/vllm-project/vllm/issues/35288) | [Bug]: MTP speculative decoding produces corrupted output at concurren | bug | 2026-06-07 |
| [#40994](https://github.com/vllm-project/vllm/issues/40994) | [Bug]: vllm does not expose /v1/audio/transcriptions for google/gemma- | bug | 2026-06-07 |
| [#44759](https://github.com/vllm-project/vllm/issues/44759) | [Bug] nightly Docker images crash with ImportError: AnthropicOutputCon | bug | 2026-06-07 |
| [#38474](https://github.com/vllm-project/vllm/issues/38474) | [RFC]: Add Mooncake Store Connector for Shared KV Cache Reuse | RFC | 2026-06-07 |
| [#44688](https://github.com/vllm-project/vllm/issues/44688) | [Performance]: Qwen3.6-35B-A3B-FP8 on RTX PRO 6000 Blackwell has very  | — | 2026-06-07 |
| [#44788](https://github.com/vllm-project/vllm/issues/44788) | [Bug] ValueError: Following weights were not initialized from checkpoi | — | 2026-06-07 |
| [#44780](https://github.com/vllm-project/vllm/issues/44780) | [Bug]: vllm server crashed when use "--kv-offloading-backend native  - | bug | 2026-06-07 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 38 |
| Other | 36 |
| MoE / Expert Parallel | 33 |
| Multimodal | 21 |
| Models | 17 |
| Disaggregation / PD | 14 |
| Attention | 14 |
| Scheduler / Engine | 12 |
| Quantization | 12 |
| KV Cache / Offload | 11 |
| CI / Build | 10 |
| Serving / API | 10 |
| Speculative Decoding | 5 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Docs | 3 |

## ROCm / AMD  (38 commits)

- **2026-06-08** [`93ee4cd47f`](https://github.com/vllm-project/vllm/commit/93ee4cd47f) [#44819](https://github.com/vllm-project/vllm/pull/44819)
  [CI] Consolidate multimodal entrypoint tests. (#44819)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/llm/test_chat.py`, `tests/entrypoints/multimodal/__init__.py` _+20 more__
- **2026-06-08** [`d9ff7e4e9a`](https://github.com/vllm-project/vllm/commit/d9ff7e4e9a) [#44761](https://github.com/vllm-project/vllm/pull/44761)
  [ROCm][CI] Stabilizing teardown and timeout of flaky tests to prevent rare OOMs (#44761)
  _Files: `tests/conftest.py`, `tests/models/language/generation/test_hybrid.py`, `tests/models/language/pooling/test_colbert.py`, `tests/utils.py`_
- **2026-06-08** [`967c5c3bc3`](https://github.com/vllm-project/vllm/commit/967c5c3bc3) [#42793](https://github.com/vllm-project/vllm/pull/42793)
  [ROCm][CI] Stage C mirrors (#42793)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/engine.yaml` _+7 more__
- **2026-06-07** [`228bcc436b`](https://github.com/vllm-project/vllm/commit/228bcc436b) [#44674](https://github.com/vllm-project/vllm/pull/44674)
  [ROCm][Kernel] Enable permute_cols for ROCm (#44674)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`_
- **2026-06-07** [`3bb46975bd`](https://github.com/vllm-project/vllm/commit/3bb46975bd) [#37149](https://github.com/vllm-project/vllm/pull/37149)
  [XPU][Feature] transparent sleep mode support for XPU platform (#37149)
  _Files: `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `tests/basic_correctness/test_mem.py` _+6 more__
- **2026-06-07** [`2a983c79ac`](https://github.com/vllm-project/vllm/commit/2a983c79ac) [#44699](https://github.com/vllm-project/vllm/pull/44699)
  [DSV4] Decouple DS V4 Sparse MLA Metadata from DS V3.2 (#44699)
  _Files: `docs/design/attention_backends.md`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/nvidia/flashmla.py` _+3 more__
- **2026-06-06** [`bc5745a00f`](https://github.com/vllm-project/vllm/commit/bc5745a00f) [#42838](https://github.com/vllm-project/vllm/pull/42838)
  [ROCm][MLA] Replace torch.cat in sparse-MLA forward_mqa with fused concat_mla_q (#42838)
  _Files: `csrc/libtorch_stable/concat_mla_q.cuh`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-06-06** [`062b05ff3a`](https://github.com/vllm-project/vllm/commit/062b05ff3a) [#44075](https://github.com/vllm-project/vllm/pull/44075)
  [ROCm][Perf] Fused MoE W4A16 HIP kernel for AMD RDNA3 (gfx1100) (#44075)
  _Files: `CMakeLists.txt`, `csrc/rocm/moe_q_gemm_rdna3.cu`, `csrc/rocm/ops.h`, `csrc/rocm/torch_bindings.cpp` _+7 more__
- **2026-06-06** [`00d1fb7747`](https://github.com/vllm-project/vllm/commit/00d1fb7747) [#43684](https://github.com/vllm-project/vllm/pull/43684)
  [Bugfix][ROCm] `ApplyRotaryEmb`: fall back to native when flash_attn rotary grid would exceed the HIP per-dim limit (#43684)
  _Files: `vllm/model_executor/layers/rotary_embedding/common.py`_
- **2026-06-05** [`4200f62147`](https://github.com/vllm-project/vllm/commit/4200f62147) [#42832](https://github.com/vllm-project/vllm/pull/42832)
  [ROCm][GPT-OSS] Fuse RoPE + static Q FP8 quant on fused RoPE+KV path (#42832)
  _Files: `tests/compile/passes/test_rope_kvcache_fusion.py`, `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`_
- **2026-06-05** [`aa6fb8a329`](https://github.com/vllm-project/vllm/commit/aa6fb8a329) [#44648](https://github.com/vllm-project/vllm/pull/44648)
  [Bugfix] [ROCm] [Critical] fallback to regular abi for ROCm (#44648)
  _Files: `CMakeLists.txt`, `csrc/cuda_view.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+2 more__
- **2026-06-05** [`c66b19800b`](https://github.com/vllm-project/vllm/commit/c66b19800b) [#44649](https://github.com/vllm-project/vllm/pull/44649)
  [CI] Bump mistral-common (#44649)
  _Files: `requirements/common.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+3 more__
- **2026-06-05** [`b4a6f26c90`](https://github.com/vllm-project/vllm/commit/b4a6f26c90) [#41002](https://github.com/vllm-project/vllm/pull/41002)
  [ROCm][perf] Use workspace manager for sparse indexer allocations (#41002)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-06-05** [`165b7864d0`](https://github.com/vllm-project/vllm/commit/165b7864d0) [#40426](https://github.com/vllm-project/vllm/pull/40426)
  [ROCM] [FEAT] Integrate Aiter hipBLASLt GEMM online tuning (#40426)
  _Files: `tests/rocm/aiter/test_aiter_hipb_mm_linear_kernel.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/__init__.py` _+2 more__
- **2026-06-05** [`4efd6ffde0`](https://github.com/vllm-project/vllm/commit/4efd6ffde0) [#44569](https://github.com/vllm-project/vllm/pull/44569)
  [DSV4] Refactor DeepseekV4Attention (#44569)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` _+4 more__
- **2026-06-04** [`06f94633e7`](https://github.com/vllm-project/vllm/commit/06f94633e7) [#44436](https://github.com/vllm-project/vllm/pull/44436)
  [ROCm][CI] Add test for Aiter unified attn kernel (#44436)
  _Files: `tests/kernels/attention/test_rocm_aiter_unified_attn.py`_
- **2026-06-04** [`06ee2d8433`](https://github.com/vllm-project/vllm/commit/06ee2d8433) [#44340](https://github.com/vllm-project/vllm/pull/44340)
  [Quant] Support compressed-tensors WNA8O8Int linears and WNInt embeddings (#44340)
  _Files: `requirements/common.txt`, `requirements/cuda.txt`, `requirements/test/rocm.txt`, `tests/kernels/quantization/test_quantized_embedding.py` _+10 more__
- **2026-06-04** [`b5235fca2e`](https://github.com/vllm-project/vllm/commit/b5235fca2e) [#43827](https://github.com/vllm-project/vllm/pull/43827)
  [DSv4] Adding TRTLLM gen attention kernel (#43827)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `csrc/torch_bindings.cpp` _+16 more__
- **2026-06-04** [`3e77036768`](https://github.com/vllm-project/vllm/commit/3e77036768) [#44255](https://github.com/vllm-project/vllm/pull/44255)
  [ROCm][CI] Specifying time outs for the lm eval models (#44255)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-V2-Lite-Instruct-FP8.yaml`, `tests/evals/gsm8k/configs/Qwen1.5-MoE-W4A16-CT.yaml`, `tests/evals/gsm8k/gsm8k_eval.py`, `tests/evals/gsm8k/test_gsm8k_correctness.py`_
- **2026-06-04** [`6f68ca3e91`](https://github.com/vllm-project/vllm/commit/6f68ca3e91) [#44046](https://github.com/vllm-project/vllm/pull/44046)
  [ROCm][CI] Stabilize memory-release in the Hybrid model generation tests (#44046)
  _Files: `tests/models/language/generation/test_hybrid.py`_
- **2026-06-04** [`0c96dd64fb`](https://github.com/vllm-project/vllm/commit/0c96dd64fb) [#43625](https://github.com/vllm-project/vllm/pull/43625)
  [ROCm] Bump fastsafetensors to v0.3.2 from PyPI, remove git source build (#43625)
  _Files: `requirements/cuda.txt`, `requirements/rocm.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+4 more__
- **2026-06-04** [`22c2e87555`](https://github.com/vllm-project/vllm/commit/22c2e87555) [#44497](https://github.com/vllm-project/vllm/pull/44497)
  [CI] Reverted gitignore changes (#44497)
  _Files: `.dockerignore`, `docker/Dockerfile.rocm`, `tools/check_repo.sh`_
- **2026-06-04** [`d01d0b4646`](https://github.com/vllm-project/vllm/commit/d01d0b4646) [#44479](https://github.com/vllm-project/vllm/pull/44479)
  [Frontend] Consolidate online serving utils. (#44479)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.github/CODEOWNERS`, `tests/entrypoints/llm/offline_mode/__init__.py` _+77 more__
- **2026-06-04** [`b4b4aaa70e`](https://github.com/vllm-project/vllm/commit/b4b4aaa70e) [#42129](https://github.com/vllm-project/vllm/pull/42129)
  [Inductor] Fast-path Inductor fallback for vllm::*/vllm_aiter::* custom ops (#42129)
  _Files: `tests/compile/test_inductor_fallback_allow_list_patch.py`, `vllm/env_override.py`_
- **2026-06-04** [`5e2af28838`](https://github.com/vllm-project/vllm/commit/5e2af28838) [#44463](https://github.com/vllm-project/vllm/pull/44463)
  [CI] Resolve release V2 docker build after ROCm CI wheels change (#44463)
  _Files: `.dockerignore`, `tools/check_repo.sh`_
- **2026-06-03** [`5b2a2beade`](https://github.com/vllm-project/vllm/commit/5b2a2beade) [#44370](https://github.com/vllm-project/vllm/pull/44370)
  [ROCm][CI] Move Model Executor test step from MI250 to MI300 (gfx942) (#44370)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-03** [`87954eb50e`](https://github.com/vllm-project/vllm/commit/87954eb50e) [#36949](https://github.com/vllm-project/vllm/pull/36949)
  [ROCm][CI] Optimize ROCm Docker build: registry cache, DeepEP, and ci-bake script (#36949)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/hardware_tests/amd.yaml`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh` _+6 more__
- **2026-06-03** [`71df063c49`](https://github.com/vllm-project/vllm/commit/71df063c49) [#42758](https://github.com/vllm-project/vllm/pull/42758)
  Enable perf_token_group_quant/_C_stable_libtorch for ROCm (#42758)
  _Files: `CMakeLists.txt`, `cmake/hipify.py`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu` _+8 more__
- **2026-06-03** [`7b476c8f14`](https://github.com/vllm-project/vllm/commit/7b476c8f14) [#44369](https://github.com/vllm-project/vllm/pull/44369)
  [ROCm][CI] Skip fp8 reload tests on gfx90a (MI250) (#44369)
  _Files: `tests/model_executor/model_loader/test_reload.py`_
- **2026-06-03** [`4454a18695`](https://github.com/vllm-project/vllm/commit/4454a18695) [#44368](https://github.com/vllm-project/vllm/pull/44368)
  [ROCm][CI] Fix stale wvSplitK GEMM fallback test for N=5 (#44368)
  _Files: `tests/model_executor/layers/test_rocm_unquantized_gemm.py`_
- **2026-06-02** [`88f172188b`](https://github.com/vllm-project/vllm/commit/88f172188b) [#44308](https://github.com/vllm-project/vllm/pull/44308)
  [ROCm] Fix AITER RMSNormQuantFusion for Kimi-Linear (#44308)
  _Files: `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`_
- **2026-06-02** [`b623f7ea95`](https://github.com/vllm-project/vllm/commit/b623f7ea95) [#44170](https://github.com/vllm-project/vllm/pull/44170)
  [Frontend] Consolidate dev entrypoints. (#44170)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docs/serving/online_serving/README.md` _+18 more__
- **2026-06-02** [`2588ec4f0a`](https://github.com/vllm-project/vllm/commit/2588ec4f0a) [#44265](https://github.com/vllm-project/vllm/pull/44265)
  [ROCm] Upgrade AITER to v0.1.13.post1 (#44265)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-06-02** [`517e74a964`](https://github.com/vllm-project/vllm/commit/517e74a964) [#44262](https://github.com/vllm-project/vllm/pull/44262)
  [DSV4] Refactor RoPE initialization (#44262)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/common/rope.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-06-02** [`48c0d13e65`](https://github.com/vllm-project/vllm/commit/48c0d13e65) [#44256](https://github.com/vllm-project/vllm/pull/44256)
  [ROCm][CI] Skip unbacked dynamic shapes tests on PyTorch < 2.11 (#44256)
  _Files: `tests/compile/test_dynamic_shapes_compilation.py`_
- **2026-06-01** [`8c3cc98cff`](https://github.com/vllm-project/vllm/commit/8c3cc98cff) [#44246](https://github.com/vllm-project/vllm/pull/44246)
  [DSV4] Remove unncessary classes & functions (#44246)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-06-01** [`fd9e91d7e4`](https://github.com/vllm-project/vllm/commit/fd9e91d7e4) [#41294](https://github.com/vllm-project/vllm/pull/41294)
  [ROCm][CI] Fix and stabilize EAGLE3 acceptance tests (#41294)
  _Files: `tests/v1/spec_decode/test_acceptance_length.py`_
- **2026-06-01** [`0910f7e0e1`](https://github.com/vllm-project/vllm/commit/0910f7e0e1) [#44153](https://github.com/vllm-project/vllm/pull/44153)
  [Frontend] Resettle generative scoring entrypoint. (#44153)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/generate/__init__.py`, `tests/entrypoints/generate/generative_scoring/__init__.py` _+9 more__

## Other  (36 commits)

- **2026-06-08** [`303916e93d`](https://github.com/vllm-project/vllm/commit/303916e93d) [#39562](https://github.com/vllm-project/vllm/pull/39562)
  [Bugfix]: Fix assertion in MambaManager.allocate_slots() (#39562)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-08** [`5633405964`](https://github.com/vllm-project/vllm/commit/5633405964) [#44805](https://github.com/vllm-project/vllm/pull/44805)
  Added extra_repr() to pooler classes to improve debuggability (#44805)
  _Files: `vllm/model_executor/layers/pooler/activations.py`, `vllm/model_executor/layers/pooler/seqwise/heads.py`, `vllm/model_executor/layers/pooler/seqwise/poolers.py`, `vllm/model_executor/layers/pooler/special.py` _+3 more__
- **2026-06-08** [`2ed0a9627b`](https://github.com/vllm-project/vllm/commit/2ed0a9627b) [#42736](https://github.com/vllm-project/vllm/pull/42736)
  [Kernel][Test] Make kernel tests for mamba dual-HW (CUDA + XPU) (#42736)
  _Files: `tests/kernels/mamba/test_causal_conv1d.py`, `tests/kernels/mamba/test_mamba_ssm.py`, `tests/kernels/mamba/test_mamba_ssm_ssd.py`_
- **2026-06-06** [`eafbb06331`](https://github.com/vllm-project/vllm/commit/eafbb06331) [#44593](https://github.com/vllm-project/vllm/pull/44593)
  [Misc] Replaced asserts with proper exceptions to improve UX for pooling (#44593)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`, `vllm/config/pooler.py`, `vllm/model_executor/layers/pooler/seqwise/heads.py`, `vllm/model_executor/layers/pooler/seqwise/methods.py` _+3 more__
- **2026-06-06** [`ec0a31d4aa`](https://github.com/vllm-project/vllm/commit/ec0a31d4aa) [#44692](https://github.com/vllm-project/vllm/pull/44692)
  [Bugfix][Kernel] Fix mHC fused-RMSNorm big-fuse miscompile for hidden_size != 4096 (#44692)
  _Files: `vllm/model_executor/kernels/mhc/tilelang_kernels.py`_
- **2026-06-06** [`c8beda4cc3`](https://github.com/vllm-project/vllm/commit/c8beda4cc3) [#44213](https://github.com/vllm-project/vllm/pull/44213)
  [Rust Frontend] Add Phi-4 mini JSON tool parser (#44213)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/tool-parser/src/json/mod.rs` _+2 more__
- **2026-06-05** [`e28e369f78`](https://github.com/vllm-project/vllm/commit/e28e369f78) [#44666](https://github.com/vllm-project/vllm/pull/44666)
  Male Mergify comment less spammy (#44666)
  _Files: `.github/mergify.yml`_
- **2026-06-05** [`91e17d4315`](https://github.com/vllm-project/vllm/commit/91e17d4315) [#38804](https://github.com/vllm-project/vllm/pull/38804)
  Fix sarvam forward compatibility with transformers v5 (#38804)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-06-05** [`7f003a1285`](https://github.com/vllm-project/vllm/commit/7f003a1285) [#44609](https://github.com/vllm-project/vllm/pull/44609)
  Support MiniCPMV batched preprocessing (#44609)
  _Files: `vllm/transformers_utils/processors/minicpmv.py`_
- **2026-06-05** [`d2f70da116`](https://github.com/vllm-project/vllm/commit/d2f70da116) [#44603](https://github.com/vllm-project/vllm/pull/44603)
  fix: pad dummy run query_start_loc (#44603)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-05** [`ca73293fa6`](https://github.com/vllm-project/vllm/commit/ca73293fa6) [#44620](https://github.com/vllm-project/vllm/pull/44620)
  [Bugfix][Rust Frontend] Fix UTF-8 char-boundary panic in incremental detokenizer (#44620)
  _Files: `rust/src/tokenizer/src/incremental.rs`_
- **2026-06-04** [`8d9536a775`](https://github.com/vllm-project/vllm/commit/8d9536a775) [#44471](https://github.com/vllm-project/vllm/pull/44471)
  [Misc] Add unit tests for pooler head classes (#44471)
  _Files: `tests/model_executor/layers/test_pooler_heads.py`_
- **2026-06-04** [`99ef652907`](https://github.com/vllm-project/vllm/commit/99ef652907) [#44057](https://github.com/vllm-project/vllm/pull/44057)
  [Bugfix] Reject non-positive values for ParallelConfig int knobs (#44057)
  _Files: `vllm/config/parallel.py`_
- **2026-06-04** [`4cc78c9d5d`](https://github.com/vllm-project/vllm/commit/4cc78c9d5d) [#44363](https://github.com/vllm-project/vllm/pull/44363)
  [Core] Freeze garbage collector in workers after model initialization (#44363)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-06-04** [`b58e082d95`](https://github.com/vllm-project/vllm/commit/b58e082d95) [#42865](https://github.com/vllm-project/vllm/pull/42865)
  [KV Connector] Update lmcache kv_offloading_backend to use LMCacheMPConnector (#42865)
  _Files: `tests/v1/kv_connector/unit/test_config.py`, `vllm/config/vllm.py`_
- **2026-06-04** [`0414d75410`](https://github.com/vllm-project/vllm/commit/0414d75410) [#44289](https://github.com/vllm-project/vllm/pull/44289)
  [XPU] skip unapplied UT in test_gpu_model_runner.py (#44289)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`_
- **2026-06-03** [`bdbf08fc02`](https://github.com/vllm-project/vllm/commit/bdbf08fc02) [#35078](https://github.com/vllm-project/vllm/pull/35078)
  Bump actions/stale from 10.1.1 to 10.2.0 (#35078)
  _Files: `.github/workflows/stale.yml`_
- **2026-06-03** [`2b237c7a41`](https://github.com/vllm-project/vllm/commit/2b237c7a41) [#42752](https://github.com/vllm-project/vllm/pull/42752)
  [Bugfix] Honor tool_choice="none" in Chat Completions streaming (#42752)
  _Files: `tests/parser/test_streaming.py`, `vllm/parser/abstract_parser.py`_
- **2026-06-03** [`dad95e34d8`](https://github.com/vllm-project/vllm/commit/dad95e34d8) [#42453](https://github.com/vllm-project/vllm/pull/42453)
  [Feature] Support batch invariant rms norm with residual (#42453)
  _Files: `tests/v1/determinism/test_rms_norm_batch_invariant.py`, `vllm/model_executor/layers/batch_invariant.py`, `vllm/model_executor/layers/layernorm.py`_
- **2026-06-03** [`27f1d34a23`](https://github.com/vllm-project/vllm/commit/27f1d34a23) [#43590](https://github.com/vllm-project/vllm/pull/43590)
  [Frontend][Responses API] Move developer-to-system conversion into HF renderer (#43590)
  _Files: `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-06-03** [`3d76f395e3`](https://github.com/vllm-project/vllm/commit/3d76f395e3) [#43689](https://github.com/vllm-project/vllm/pull/43689)
  [SharedOffloadRegion] Align blocks to page-size   (#43689)
  _Files: `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py` _+2 more__
- **2026-06-03** [`02564b4de0`](https://github.com/vllm-project/vllm/commit/02564b4de0) [#43759](https://github.com/vllm-project/vllm/pull/43759)
  [XPU]fallback to TRITON_ATTN for vit attn on xpu when use float32 dtype (#43759)
  _Files: `vllm/platforms/xpu.py`_
- **2026-06-03** [`449be4f934`](https://github.com/vllm-project/vllm/commit/449be4f934) [#44311](https://github.com/vllm-project/vllm/pull/44311)
  [Rust Frontend] Fix several hf chat template rendering issues (#44311)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/renderer/hf/mod.rs` _+5 more__
- **2026-06-03** [`4aaed4ca22`](https://github.com/vllm-project/vllm/commit/4aaed4ca22) [#43774](https://github.com/vllm-project/vllm/pull/43774)
  [Rust Frontend] Add server router extension hook (#43774)
  _Files: `rust/src/server/src/lib.rs`_
- **2026-06-03** [`02a01496fc`](https://github.com/vllm-project/vllm/commit/02a01496fc) [#43838](https://github.com/vllm-project/vllm/pull/43838)
  [Platform] Add is_cumem_allocator_available (#43838)
  _Files: `vllm/config/model.py`, `vllm/platforms/interface.py`_
- **2026-06-02** [`557781131a`](https://github.com/vllm-project/vllm/commit/557781131a) [#44350](https://github.com/vllm-project/vllm/pull/44350)
  [Misc] Remove stray empty file (#44350)
  _Files: `=4.5.1`_
- **2026-06-02** [`e4a2e584e5`](https://github.com/vllm-project/vllm/commit/e4a2e584e5) [#44338](https://github.com/vllm-project/vllm/pull/44338)
  [MRV2] Remove assignment of graph_pool in cudagraph_utils (#44338)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-06-02** [`b8b49e2395`](https://github.com/vllm-project/vllm/commit/b8b49e2395) [#39667](https://github.com/vllm-project/vllm/pull/39667)
  Bump actions/github-script from 8.0.0 to 9.0.0 (#39667)
  _Files: `.github/workflows/add_label_automerge.yml`, `.github/workflows/issue_autolabel.yml`, `.github/workflows/new_pr_bot.yml`, `.github/workflows/pre-commit.yml`_
- **2026-06-02** [`478b49ddec`](https://github.com/vllm-project/vllm/commit/478b49ddec) [#44279](https://github.com/vllm-project/vllm/pull/44279)
  [Refactor] Remove dead code from parser infrastructure (#44279)
  _Files: `tests/parser/test_streaming.py`, `vllm/parser/__init__.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/minimax_m2_parser.py` _+1 more__
- **2026-06-02** [`586201ebdc`](https://github.com/vllm-project/vllm/commit/586201ebdc) [#44320](https://github.com/vllm-project/vllm/pull/44320)
  [Rust Frontend] Cover different thinking modes in roundtrip tests (#44320)
  _Files: `rust/src/chat/tests/roundtrip.rs`_
- **2026-06-02** [`6314de8bad`](https://github.com/vllm-project/vllm/commit/6314de8bad) [#44168](https://github.com/vllm-project/vllm/pull/44168)
  [XPU] [Bug] remove xpuw4a16 output size check (#44168)
  _Files: `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`_
- **2026-06-02** [`f69ede495b`](https://github.com/vllm-project/vllm/commit/f69ede495b) [#43421](https://github.com/vllm-project/vllm/pull/43421)
  [XPU][Mamba] Triton-based selective scan forward op for XPU (#43421)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/layers/mamba/ops/mamba_ssm.py`_
- **2026-06-02** [`93da882e73`](https://github.com/vllm-project/vllm/commit/93da882e73) [#44177](https://github.com/vllm-project/vllm/pull/44177)
  [kv_offload] Add `@override` decorators to subclass method implementations (#44177)
  _Files: `vllm/v1/kv_offload/base.py`, `vllm/v1/kv_offload/cpu/common.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`, `vllm/v1/kv_offload/cpu/manager.py` _+6 more__
- **2026-06-01** [`e4cbc4385d`](https://github.com/vllm-project/vllm/commit/e4cbc4385d) [#44234](https://github.com/vllm-project/vllm/pull/44234)
  [Test][BugFix] Fix double-BOS in PD+specdec acceptance test (#44234)
  _Files: `tests/v1/kv_connector/nixl_integration/test_spec_decode_acceptance.py`_
- **2026-06-01** [`182c67daf1`](https://github.com/vllm-project/vllm/commit/182c67daf1) [#43779](https://github.com/vllm-project/vllm/pull/43779)
  [Rust Frontend] Support streaming `generate` endpoint (#43779)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/inference/generate/validate.rs` _+1 more__
- **2026-06-01** [`29d69332aa`](https://github.com/vllm-project/vllm/commit/29d69332aa) [#44035](https://github.com/vllm-project/vllm/pull/44035)
  [BugFix] Fix `_has_module` to verify native deps via trial import (#44035)
  _Files: `tests/utils_/test_import_utils.py`, `vllm/utils/import_utils.py`_

## MoE / Expert Parallel  (33 commits)

- **2026-06-08** [`fa662b1a8b`](https://github.com/vllm-project/vllm/commit/fa662b1a8b) [#44470](https://github.com/vllm-project/vllm/pull/44470)
  [XPU] Cap topk/topp Triton BLOCK_SIZE to 4096 to fix Top-p mask difference failures (#44470)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-06-08** [`54c660c3a6`](https://github.com/vllm-project/vllm/commit/54c660c3a6) [#44771](https://github.com/vllm-project/vllm/pull/44771)
  [XPU][Minor] format moe kernel name and add in kernel list (#44771)
  _Files: `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+1 more__
- **2026-06-07** [`9c7f7741d4`](https://github.com/vllm-project/vllm/commit/9c7f7741d4) [#44041](https://github.com/vllm-project/vllm/pull/44041)
  [Bugfix] Fix benchmark_moe.py after inplace mechanism removal (#44041)
  _Files: `benchmarks/kernels/benchmark_moe.py`_
- **2026-06-07** [`6181e80fe0`](https://github.com/vllm-project/vllm/commit/6181e80fe0) [#44540](https://github.com/vllm-project/vllm/pull/44540)
  [XPU] add xpu branch in compressed_tensors_moe_w4a4_mxfp4 (#44540)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a4_mxfp4.py`_
- **2026-06-06** [`f87df1df9e`](https://github.com/vllm-project/vllm/commit/f87df1df9e) [#44613](https://github.com/vllm-project/vllm/pull/44613)
  [Bugfix][MoE] Snapshot max_cudagraph_capture_size into FusedMoEConfig (#44613)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/layers/fused_moe/layer.py` _+1 more__
- **2026-06-05** [`a50e675b0d`](https://github.com/vllm-project/vllm/commit/a50e675b0d) [#44021](https://github.com/vllm-project/vllm/pull/44021)
  [Cohere] fix RoutingMethodType (#44021)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/router/custom_routing_router.py`_
- **2026-06-05** [`ef0df7dbd6`](https://github.com/vllm-project/vllm/commit/ef0df7dbd6) [#44647](https://github.com/vllm-project/vllm/pull/44647)
  [CI] Bump mypy version `1.19.1` -> `1.20.2` (#44647)
  _Files: `.github/mergify.yml`, `.pre-commit-config.yaml`, `AGENTS.md`, `docs/contributing/README.md` _+5 more__
- **2026-06-05** [`a80af24356`](https://github.com/vllm-project/vllm/commit/a80af24356) [#44635](https://github.com/vllm-project/vllm/pull/44635)
  Speed up docs build (#44635)
  _Files: `AGENTS.md`, `docs/features/speculative_decoding/README.md`, `mkdocs.yaml`, `vllm/_custom_ops.py` _+28 more__
- **2026-06-05** [`62215e72c6`](https://github.com/vllm-project/vllm/commit/62215e72c6) [#43167](https://github.com/vllm-project/vllm/pull/43167)
  Remove KV cache scale boilerplate from model weight loading methods (#43167)
  _Files: `tests/model_executor/test_eagle_quantization.py`, `vllm/model_executor/layers/quantization/base_config.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/kv_cache.py` _+52 more__
- **2026-06-05** [`7fe7800fa4`](https://github.com/vllm-project/vllm/commit/7fe7800fa4) [#43150](https://github.com/vllm-project/vllm/pull/43150)
  [BUG] Fix FP64 Gumbel precision coverage (#43150)
  _Files: `tests/v1/sample/test_rejection_sampler.py`, `tests/v1/sample/test_topk_topp_sampler.py`, `tests/v1/spec_decode/test_eagle.py`, `tests/v1/spec_decode/test_llm_base_proposer_sampling.py` _+7 more__
- **2026-06-05** [`56aff0dd15`](https://github.com/vllm-project/vllm/commit/56aff0dd15) [#44334](https://github.com/vllm-project/vllm/pull/44334)
  [10/n] Migrate cuda_view and silu_and_mul_per_block_quant kernels to torch stale ABI. (#44334)
  _Files: `CMakeLists.txt`, `csrc/cuda_view.cu`, `csrc/libtorch_stable/cuda_utils_kernels.cu`, `csrc/libtorch_stable/cuda_view.cu` _+21 more__
- **2026-06-05** [`063ce98fb7`](https://github.com/vllm-project/vllm/commit/063ce98fb7) [#42139](https://github.com/vllm-project/vllm/pull/42139)
  [XPU][MoE] support block_fp8_moe on xpu (#42139)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`_
- **2026-06-04** [`38fd2405f3`](https://github.com/vllm-project/vllm/commit/38fd2405f3) [#41980](https://github.com/vllm-project/vllm/pull/41980)
  use split_group for pytorch process group creation (#41980)
  _Files: `tests/distributed/test_dcp_a2a.py`, `tests/distributed/test_pynccl.py`, `tests/distributed/test_quick_all_reduce.py`, `tests/distributed/test_split_group.py` _+7 more__
- **2026-06-04** [`439203d32c`](https://github.com/vllm-project/vllm/commit/439203d32c) [#44380](https://github.com/vllm-project/vllm/pull/44380)
  [Bugfix] Fix test_cutlass_moe.py (#44380)
  _Files: `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/utils.py`, `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`_
- **2026-06-04** [`90619351e3`](https://github.com/vllm-project/vllm/commit/90619351e3) [#43556](https://github.com/vllm-project/vllm/pull/43556)
  [Attention] Mamba attention module refactor - LINEAR (#43556)
  _Files: `tests/v1/attention/test_attention_backends_selection.py`, `vllm/model_executor/layers/mamba/linear/__init__.py`, `vllm/model_executor/layers/mamba/linear/bailing_linear_attn.py`, `vllm/model_executor/layers/mamba/linear/base.py` _+3 more__
- **2026-06-04** [`4f423bd5bc`](https://github.com/vllm-project/vllm/commit/4f423bd5bc) [#41633](https://github.com/vllm-project/vllm/pull/41633)
  [EPLB] Nixl communicator optimization. Zero-copy transfers (#41633)
  _Files: `tests/distributed/test_eplb_execute.py`, `tests/distributed/test_eplb_fused_moe_layer.py`, `tests/distributed/test_eplb_fused_moe_layer_dep_nvfp4.py`, `tests/kernels/moe/test_moe_layer.py` _+8 more__
- **2026-06-03** [`6bad553f4e`](https://github.com/vllm-project/vllm/commit/6bad553f4e) [#44442](https://github.com/vllm-project/vllm/pull/44442)
  [Minor] Remove FlashInfer version check in topk_topp_sampler (#44442)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-06-03** [`59d0236193`](https://github.com/vllm-project/vllm/commit/59d0236193) [#44365](https://github.com/vllm-project/vllm/pull/44365)
  [10b/n] Migrate custom all-reduce, DeepSeek V4 fused MLA, MiniMax reduce-RMS, and MXFP8 MoE to libtorch stable ABI (#44365)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/custom_all_reduce.cu`, `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/minimax_reduce_rms_kernel.cu` _+14 more__
- **2026-06-03** [`ec8d60bea8`](https://github.com/vllm-project/vllm/commit/ec8d60bea8) [#42472](https://github.com/vllm-project/vllm/pull/42472)
  [Model Runner V2] Use FlashInfer sampler (#42472)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/worker/gpu/sample/sampler.py`, `vllm/v1/worker/gpu/sample/states.py`_
- **2026-06-03** [`e3e132d2dd`](https://github.com/vllm-project/vllm/commit/e3e132d2dd) [#44346](https://github.com/vllm-project/vllm/pull/44346)
  [Refactor] Suppress SyntaxWarning from ast.literal_eval in tool parsers (#44346)
  _Files: `vllm/tool_parsers/glm4_moe_tool_parser.py`, `vllm/tool_parsers/hy_v3_tool_parser.py`, `vllm/tool_parsers/minicpm5xml_tool_parser.py`, `vllm/tool_parsers/poolside_v1_tool_parser.py` _+3 more__
- **2026-06-03** [`ace95c9cf8`](https://github.com/vllm-project/vllm/commit/ace95c9cf8) [#44347](https://github.com/vllm-project/vllm/pull/44347)
  [Bugfix] Update TrtLLM MoE routing methods (#44347)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py` _+2 more__
- **2026-06-03** [`969aec4bc8`](https://github.com/vllm-project/vllm/commit/969aec4bc8) [#44356](https://github.com/vllm-project/vllm/pull/44356)
  [Bugfix] Fix Deepseek v4 non-mega-moe model init error (#44356)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-06-03** [`ca17b6b17d`](https://github.com/vllm-project/vllm/commit/ca17b6b17d) [#42191](https://github.com/vllm-project/vllm/pull/42191)
  [Perf] Apply single-pass min_larger finding and binary search in Triton Top-p path. (#42191)
  _Files: `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-06-03** [`b254e0456c`](https://github.com/vllm-project/vllm/commit/b254e0456c) [#44367](https://github.com/vllm-project/vllm/pull/44367)
  [DSV4] Minor cleanup for DeepseekV4MegaMoEExperts (#44367)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-06-02** [`a4ac746405`](https://github.com/vllm-project/vllm/commit/a4ac746405) [#43332](https://github.com/vllm-project/vllm/pull/43332)
  [MoE/b12x] Accept W4A16 (kNvfp4Static, None) in FlashInferB12xExperts supports check (#43332)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_b12x_moe.py`_
- **2026-06-02** [`3099de3617`](https://github.com/vllm-project/vllm/commit/3099de3617) [#42027](https://github.com/vllm-project/vllm/pull/42027)
  [Kernel][MoE] Add GELU_TANH to CPU, CUTLASS, and WNA16 MoE backends (#42027)
  _Files: `csrc/cpu/cpu_fused_moe.cpp`, `tests/kernels/moe/test_cpu_fused_moe.py`, `tests/kernels/moe/test_cutlass_moe.py`, `tests/quantization/test_moe_wna16.py` _+3 more__
- **2026-06-02** [`2427094152`](https://github.com/vllm-project/vllm/commit/2427094152) [#43339](https://github.com/vllm-project/vllm/pull/43339)
  [Feature] Support EPLB for DeepSeek v4 Mega Moe (#43339)
  _Files: `vllm/distributed/eplb/eplb_utils.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/utils/deep_gemm.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-06-02** [`afcb580715`](https://github.com/vllm-project/vllm/commit/afcb580715) [#43100](https://github.com/vllm-project/vllm/pull/43100)
  [BugFix] Fix Humming MoE deploy error (#43100)
  _Files: `vllm/model_executor/layers/quantization/humming.py`_
- **2026-06-02** [`774e552397`](https://github.com/vllm-project/vllm/commit/774e552397) [#44025](https://github.com/vllm-project/vllm/pull/44025)
  [compressed-tensors] Asymmetric support for MoE WNA16 marlin (#44025)
  _Files: `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16_marlin.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils.py` _+1 more__
- **2026-06-02** [`4d93bc35c9`](https://github.com/vllm-project/vllm/commit/4d93bc35c9) [#44013](https://github.com/vllm-project/vllm/pull/44013)
  Migrate header files to torch stable abi (#44013)
  _Files: `.pre-commit-config.yaml`, `csrc/libtorch_stable/async_util.cuh`, `csrc/libtorch_stable/cutlass_extensions/epilogue/broadcast_load_epilogue_c2x.hpp`, `csrc/libtorch_stable/cutlass_extensions/epilogue/scaled_mm_epilogues_c2x.hpp` _+14 more__
- **2026-06-02** [`0cbc48c4f9`](https://github.com/vllm-project/vllm/commit/0cbc48c4f9) [#42958](https://github.com/vllm-project/vllm/pull/42958)
  Support ModelOpt MXFP8 non-gated MoE (#42958)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`_
- **2026-06-02** [`dcdfe66bfa`](https://github.com/vllm-project/vllm/commit/dcdfe66bfa) [#44220](https://github.com/vllm-project/vllm/pull/44220)
  [Perf] use triton moe backend on hopper by default (#44220)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-06-01** [`8796838910`](https://github.com/vllm-project/vllm/commit/8796838910) [#43770](https://github.com/vllm-project/vllm/pull/43770)
  [Bugfix] fix wrong partial_rotary_factor calculation for bailing_moe model. (#43770)
  _Files: `vllm/model_executor/models/bailing_moe.py`_

## Multimodal  (21 commits)

- **2026-06-08** [`980796cd07`](https://github.com/vllm-project/vllm/commit/980796cd07) [#44852](https://github.com/vllm-project/vllm/pull/44852)
  [CI/Build][CPU] Fix flaky CI image build failure and unexpected warnings (#44852)
  _Files: `docker/Dockerfile.cpu`, `vllm/_custom_ops.py`_
- **2026-06-08** [`469f3dcf1d`](https://github.com/vllm-project/vllm/commit/469f3dcf1d) [#44828](https://github.com/vllm-project/vllm/pull/44828)
  [BugFix] Use served model name in gemma4 audio-tower error message (#44828)
  _Files: `vllm/model_executor/models/gemma4_mm.py`_
- **2026-06-08** [`94fcdd007f`](https://github.com/vllm-project/vllm/commit/94fcdd007f) [#43663](https://github.com/vllm-project/vllm/pull/43663)
  [XPU][CI] Add more test cases in Intel GPU CI (#43663)
  _Files: `.buildkite/intel_jobs/expert_parallelism_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-test.sh`_
- **2026-06-07** [`f0f6805d8a`](https://github.com/vllm-project/vllm/commit/f0f6805d8a) [#44051](https://github.com/vllm-project/vllm/pull/44051)
  [CI] Stabilize the multi-audio OpenAI server path (#44051)
  _Files: `vllm/entrypoints/chat_utils.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/multimodal/processing/context.py`_
- **2026-06-07** [`15652a6b70`](https://github.com/vllm-project/vllm/commit/15652a6b70) [#44378](https://github.com/vllm-project/vllm/pull/44378)
  [Doc] Fix multimodal torch.compile troubleshooting to not use removed VLLM_TORCH_COMPILE_LEVEL (#44378)
  _Files: `docs/design/torch_compile_multimodal.md`_
- **2026-06-07** [`6ac69203e8`](https://github.com/vllm-project/vllm/commit/6ac69203e8) [#44417](https://github.com/vllm-project/vllm/pull/44417)
  [videoloader] implement glm46v video loader (#44417)
  _Files: `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-06-06** [`c9b4b184b4`](https://github.com/vllm-project/vllm/commit/c9b4b184b4) [#44559](https://github.com/vllm-project/vllm/pull/44559)
  [Bugfix][Voxtral] Add fetch_audio to MistralCommonFeatureExtractor (transformers>=5.10 compat) (#44559)
  _Files: `tests/transformers_utils/processors/__init__.py`, `tests/transformers_utils/processors/test_voxtral.py`, `vllm/transformers_utils/processors/voxtral.py`_
- **2026-06-05** [`62d6f06e3d`](https://github.com/vllm-project/vllm/commit/62d6f06e3d) [#44500](https://github.com/vllm-project/vllm/pull/44500)
  [Rust Frontend] Skip loading multimodal processor if `--language-model-only` is specified (#44500)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+4 more__
- **2026-06-04** [`3dbb4e0ace`](https://github.com/vllm-project/vllm/commit/3dbb4e0ace) [#44509](https://github.com/vllm-project/vllm/pull/44509)
  [Bugfix] MiniCPM-V-4.6 video inference crash: placeholder count mismatches visual embedding count (#44509)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`, `vllm/multimodal/parse.py`_
- **2026-06-04** [`b21443e23c`](https://github.com/vllm-project/vllm/commit/b21443e23c) [#43519](https://github.com/vllm-project/vllm/pull/43519)
  Add model support for granite speech plus (#43519)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_granite_speech.py`, `tests/models/registry.py`, `vllm/model_executor/models/granite_speech.py` _+2 more__
- **2026-06-04** [`f25952e59b`](https://github.com/vllm-project/vllm/commit/f25952e59b) [#41759](https://github.com/vllm-project/vllm/pull/41759)
  [MM][Perf][CG] Support ViT full CUDA graph for InternVL (#41759)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/internvl.py`_
- **2026-06-03** [`95b1615ec9`](https://github.com/vllm-project/vllm/commit/95b1615ec9) [#44212](https://github.com/vllm-project/vllm/pull/44212)
  [Perf] Improve multimodal item handling from O(n) to O(log n) per step (#44212)
  _Files: `tests/v1/core/test_encoder_cache_manager.py`, `vllm/multimodal/utils.py`, `vllm/transformers_utils/processors/voxtral.py`, `vllm/v1/core/encoder_cache_manager.py` _+2 more__
- **2026-06-03** [`0e2b13103b`](https://github.com/vllm-project/vllm/commit/0e2b13103b) [#44388](https://github.com/vllm-project/vllm/pull/44388)
  [Doc] Update ViT CUDA graph interfaces (#44388)
  _Files: `docs/design/cuda_graphs_multimodal.md`_
- **2026-06-02** [`53fa09d085`](https://github.com/vllm-project/vllm/commit/53fa09d085) [#43843](https://github.com/vllm-project/vllm/pull/43843)
  [Misc] Support local image encoding in benchmarks (#43843)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_custom_image_dataset.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-06-02** [`c91a87f01a`](https://github.com/vllm-project/vllm/commit/c91a87f01a) [#43978](https://github.com/vllm-project/vllm/pull/43978)
  [BugFix] [GDN] Read linear_key_head_dim from hf_text_config for multimodal models (#43978)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_
- **2026-06-02** [`0bdfd5eb84`](https://github.com/vllm-project/vllm/commit/0bdfd5eb84) [#44282](https://github.com/vllm-project/vllm/pull/44282)
  [Bugfix] Vendor MiniCPMV/MiniCPMO processors to unblock Transformers v5  (#44282)
  _Files: `tests/lora/test_minicpmv_tp.py`, `tests/models/multimodal/generation/test_common.py`, `vllm/model_executor/models/minicpmo.py`, `vllm/model_executor/models/minicpmv.py` _+3 more__
- **2026-06-02** [`2fd0e52252`](https://github.com/vllm-project/vllm/commit/2fd0e52252) [#44232](https://github.com/vllm-project/vllm/pull/44232)
  [Bugfix] Fix Gemma4 startup crash with recent transformers multimodal processor (#44232)
  _Files: `vllm/model_executor/models/gemma4_mm.py`_
- **2026-06-02** [`f8e9c56d15`](https://github.com/vllm-project/vllm/commit/f8e9c56d15) [#44126](https://github.com/vllm-project/vllm/pull/44126)
  [Multimodal] Automatically select registered video loader for VLM (#44126)
  _Files: `tests/multimodal/test_video.py`, `vllm/entrypoints/chat_utils.py`, `vllm/multimodal/media/connector.py`, `vllm/multimodal/video.py` _+1 more__
- **2026-06-02** [`279d25f5cb`](https://github.com/vllm-project/vllm/commit/279d25f5cb) [#38053](https://github.com/vllm-project/vllm/pull/38053)
  [BugFix] Fix TypeError in MiniCPM-O audio feature unpadding (#38053)
  _Files: `vllm/model_executor/models/minicpmo.py`_
- **2026-06-01** [`bd0aecdc08`](https://github.com/vllm-project/vllm/commit/bd0aecdc08) [#44146](https://github.com/vllm-project/vllm/pull/44146)
  [XPU][CI] Fix test_audio_in_video flake by using module-scoped server fixture (#44146)
  _Files: `tests/entrypoints/openai/chat_completion/test_audio_in_video.py`_
- **2026-06-01** [`1fd8bd02a4`](https://github.com/vllm-project/vllm/commit/1fd8bd02a4) [#44159](https://github.com/vllm-project/vllm/pull/44159)
  [Docs] Replace broken video url in examples (#44159)
  _Files: `docs/features/multimodal_inputs.md`, `examples/generate/multimodal/openai_chat_completion_client_for_multimodal.py`_

## Models  (17 commits)

- **2026-06-08** [`6124a98a9b`](https://github.com/vllm-project/vllm/commit/6124a98a9b) [#44215](https://github.com/vllm-project/vllm/pull/44215)
  [Bugfix] Fix FunASR-Nano crash during initialization (#44215)
  _Files: `vllm/model_executor/models/funasr.py`_
- **2026-06-07** [`1505b3d8a1`](https://github.com/vllm-project/vllm/commit/1505b3d8a1) [#44707](https://github.com/vllm-project/vllm/pull/44707)
  [Cohere] Enable Cohere Mini Code model and update Command A-plus test registry (#44707)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-06-05** [`4765f0f189`](https://github.com/vllm-project/vllm/commit/4765f0f189) [#44130](https://github.com/vllm-project/vllm/pull/44130)
  [Bugfix] Fix `sequence_parallel_chunk_impl` custom op aliasing its input (#44130)
  _Files: `vllm/model_executor/models/utils.py`_
- **2026-06-05** [`f6a708ab2b`](https://github.com/vllm-project/vllm/commit/f6a708ab2b) [#44435](https://github.com/vllm-project/vllm/pull/44435)
  [Doc] Add Llama-3.2-3B-Instruct to batch-invariance tested models (#44435)
  _Files: `docs/features/batch_invariance.md`_
- **2026-06-05** [`6a11d72df7`](https://github.com/vllm-project/vllm/commit/6a11d72df7) [#44588](https://github.com/vllm-project/vllm/pull/44588)
  [Reasoning][Structured Outputs] Add Command A plus tags for structural tags (#44588)
  _Files: `vllm/reasoning/cohere_command_reasoning_parser.py`_
- **2026-06-05** [`bbb6c274c8`](https://github.com/vllm-project/vllm/commit/bbb6c274c8) [#44615](https://github.com/vllm-project/vllm/pull/44615)
  [Bugfix] Fix gemma4 crash on CPU: guard mem_get_info call (#44615)
  _Files: `vllm/platforms/cpu.py`_
- **2026-06-05** [`d61d8566ec`](https://github.com/vllm-project/vllm/commit/d61d8566ec) [#44622](https://github.com/vllm-project/vllm/pull/44622)
  [Bugfix] Update mistral tokenizer test for continue_final_message fix (#44622)
  _Files: `tests/tokenizers_/test_mistral.py`_
- **2026-06-04** [`b7c5baf63d`](https://github.com/vllm-project/vllm/commit/b7c5baf63d) [#43926](https://github.com/vllm-project/vllm/pull/43926)
  fix: keep DeepSeek V4 RoPE cache on inv_freq device (#43926)
  _Files: `vllm/model_executor/layers/rotary_embedding/deepseek_scaling_rope.py`_
- **2026-06-04** [`a55fccfc7c`](https://github.com/vllm-project/vllm/commit/a55fccfc7c) [#44539](https://github.com/vllm-project/vllm/pull/44539)
  [mamba] unify KDA conv states into one cache to match 2-state SSM layout (#44539)
  _Files: `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/kimi_linear.py`_
- **2026-06-04** [`4b87b3e845`](https://github.com/vllm-project/vllm/commit/4b87b3e845) [#44205](https://github.com/vllm-project/vllm/pull/44205)
  [Bugfix] fix EVS for qwen3-vl (#44205)
  _Files: `vllm/model_executor/models/qwen3_vl.py`_
- **2026-06-04** [`f0cd590d62`](https://github.com/vllm-project/vllm/commit/f0cd590d62) [#44230](https://github.com/vllm-project/vllm/pull/44230)
  optimize the compressor 128 split cutedsl kernel  (#44230)
  _Files: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`_
- **2026-06-04** [`128adabfe0`](https://github.com/vllm-project/vllm/commit/128adabfe0) [#43982](https://github.com/vllm-project/vllm/pull/43982)
  [Bugfix] Fix Gemma4 MTP block_table batch_size mismatch under concurrent load (#43982)
  _Files: `vllm/v1/spec_decode/gemma4.py`_
- **2026-06-03** [`597bc15936`](https://github.com/vllm-project/vllm/commit/597bc15936) [#44236](https://github.com/vllm-project/vllm/pull/44236)
  fix: resolve CUTLASS fmin compatibility for DeepSeek-V4 init (#44236)
  _Files: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`_
- **2026-06-02** [`880fc032f4`](https://github.com/vllm-project/vllm/commit/880fc032f4) [#44299](https://github.com/vllm-project/vllm/pull/44299)
  [Rust Frontend] Support recursive tool parameter conversion (#44299)
  _Files: `rust/src/tool-parser/src/deepseek_dsml/mod.rs`, `rust/src/tool-parser/src/parameters.rs`_
- **2026-06-01** [`023808c23d`](https://github.com/vllm-project/vllm/commit/023808c23d) [#43992](https://github.com/vllm-project/vllm/pull/43992)
  [Feature] Add support for JetBrains' Mellum v2 code generation model (#43992)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/mellum.py`, `vllm/model_executor/models/registry.py` _+3 more__
- **2026-06-01** [`de21863419`](https://github.com/vllm-project/vllm/commit/de21863419) [#43481](https://github.com/vllm-project/vllm/pull/43481)
  [Rust Frontend] Add InternLM2 tool parser (#43481)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/tool-parser/src/json/hermes.rs` _+6 more__
- **2026-06-01** [`1f6048abe5`](https://github.com/vllm-project/vllm/commit/1f6048abe5) [#42944](https://github.com/vllm-project/vllm/pull/42944)
  fix: glm5.1 pp model loading (#42944)
  _Files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`_

## Disaggregation / PD  (14 commits)

- **2026-06-08** [`5add018beb`](https://github.com/vllm-project/vllm/commit/5add018beb) [#44854](https://github.com/vllm-project/vllm/pull/44854)
  [Connector] Remove `P2pNcclConnector` (#44854)
  _Files: `benchmarks/disagg_benchmarks/disagg_overhead_benchmark.sh`, `benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh`, `benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py`, `benchmarks/disagg_benchmarks/round_robin_proxy.py` _+14 more__
- **2026-06-07** [`51ef688831`](https://github.com/vllm-project/vllm/commit/51ef688831) [#44103](https://github.com/vllm-project/vllm/pull/44103)
  [Bugfix][Mooncake] Fix per-group block_size/block_hash and group_idx in MooncakeStoreConnector KV events (#44103)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py` _+1 more__
- **2026-06-05** [`d98b8f371c`](https://github.com/vllm-project/vllm/commit/d98b8f371c) [#43874](https://github.com/vllm-project/vllm/pull/43874)
  [NixlConnector] Initiate deprecation cycle for `kv_both` role  (#43874)
  _Files: `docs/design/nixl_kv_cache_lease.md`, `docs/features/nixl_connector_usage.md`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/spec_decode_acceptance_test.sh` _+6 more__
- **2026-06-05** [`96229fa99e`](https://github.com/vllm-project/vllm/commit/96229fa99e) [#43720](https://github.com/vllm-project/vllm/pull/43720)
  [KVConnector][1/N] PP-aware handshake aggregation and intermediate-PP output plumbing (#43720)
  _Files: `tests/v1/kv_connector/unit/test_handshake_pp_aggregation.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_transfer_topology_sharded.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py` _+5 more__
- **2026-06-04** [`41a4829f22`](https://github.com/vllm-project/vllm/commit/41a4829f22) [#43707](https://github.com/vllm-project/vllm/pull/43707)
  [Logs Refactor] Optimize shutdown logs, easier to follow and consistent (#43707)
  _Files: `vllm/distributed/parallel_state.py`, `vllm/entrypoints/launcher.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/core.py` _+3 more__
- **2026-06-04** [`e6018c644a`](https://github.com/vllm-project/vllm/commit/e6018c644a) [#41471](https://github.com/vllm-project/vllm/pull/41471)
  [Refactor] Remove dead code in tests and parallel_state (#41471)
  _Files: `tests/v1/kv_connector/unit/test_bidirectional_kv_transfer.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py`, `vllm/distributed/parallel_state.py`_
- **2026-06-03** [`0a5cbf633e`](https://github.com/vllm-project/vllm/commit/0a5cbf633e) [#43659](https://github.com/vllm-project/vllm/pull/43659)
  Handle spinloop ext load failure gracefully (#43659)
  _Files: `CMakeLists.txt`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-06-02** [`e15f20258b`](https://github.com/vllm-project/vllm/commit/e15f20258b) [#42187](https://github.com/vllm-project/vllm/pull/42187)
  [ModelRunnerV2] Avoid pipeline parallel bubbles (#42187)
  _Files: `.buildkite/test_areas/model_runner_v2.yaml`, `tests/v1/distributed/test_pp_dp_v2.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/config/vllm.py` _+15 more__
- **2026-06-02** [`689b0eeb9e`](https://github.com/vllm-project/vllm/commit/689b0eeb9e) [#43754](https://github.com/vllm-project/vllm/pull/43754)
  [HARDWARE][POWER] Enable SHM communicator support for PowerPC (#43754)
  _Files: `=4.5.1`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vsx.hpp`, `csrc/cpu/shm.cpp` _+2 more__
- **2026-06-02** [`d247a9dc13`](https://github.com/vllm-project/vllm/commit/d247a9dc13) [#41627](https://github.com/vllm-project/vllm/pull/41627)
  [EC Connector] Non blocking EC Connector lookup (#41627)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/distributed/ec_transfer/ec_connector/base.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-02** [`480fadab1b`](https://github.com/vllm-project/vllm/commit/480fadab1b) [#42959](https://github.com/vllm-project/vllm/pull/42959)
  [BugFix][kv_offload]: Prevent offloading stale sliding window blocks (#42959)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-06-02** [`816cc73a9b`](https://github.com/vllm-project/vllm/commit/816cc73a9b) [#44266](https://github.com/vllm-project/vllm/pull/44266)
  [Bugfix][CI] Normalize NIXL connector CUDA wheel installs (#44266)
  _Files: `.buildkite/scripts/install-kv-connectors.sh`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/misc.yaml`_
- **2026-06-02** [`d68f0b220e`](https://github.com/vllm-project/vllm/commit/d68f0b220e) [#43742](https://github.com/vllm-project/vllm/pull/43742)
  [Bugfix][Mooncake] Release GPU pin on failed store in MooncakeStoreConnector (#43742)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-01** [`266b9d9c64`](https://github.com/vllm-project/vllm/commit/266b9d9c64) [#40096](https://github.com/vllm-project/vllm/pull/40096)
  [Frontend][Core] Add sparse NCCL weight transfer support for in-place updates (#40096)
  _Files: `docs/training/weight_transfer/nccl.md`, `examples/rl/rlhf_sparse_nccl.py`, `tests/distributed/test_weight_transfer.py`, `tests/entrypoints/weight_transfer/test_weight_transfer_llm.py` _+8 more__

## Attention  (14 commits)

- **2026-06-08** [`eebce65756`](https://github.com/vllm-project/vllm/commit/eebce65756) [#42953](https://github.com/vllm-project/vllm/pull/42953)
  [XPU]feat: add DeepSeek-V4 XPU attention decode path (#42953)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/compressor.py` _+7 more__
- **2026-06-06** [`fa27d4e9cf`](https://github.com/vllm-project/vllm/commit/fa27d4e9cf) [#44700](https://github.com/vllm-project/vllm/pull/44700)
  [PERF] [Qwen3.5] Split mixed prefill+decode batches: route decodes to the recurrent kernel (#44700)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`, `tests/evals/gsm8k/configs/models-qwen35-blackwell.txt`, `tests/kernels/mamba/test_gdn_forward_core_split.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py` _+1 more__
- **2026-06-05** [`02d2da0748`](https://github.com/vllm-project/vllm/commit/02d2da0748) [#44561](https://github.com/vllm-project/vllm/pull/44561)
  [DSV4] Move more ops out of eager breakpoint (#44561)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-06-04** [`a947f7a420`](https://github.com/vllm-project/vllm/commit/a947f7a420) [#43307](https://github.com/vllm-project/vllm/pull/43307)
  [Kernel][Test] Extend lightning_attn and awq_triton kernel tests to XPU (#43307)
  _Files: `tests/kernels/attention/test_lightning_attn.py`, `tests/kernels/quantization/test_awq_triton.py`, `vllm/model_executor/layers/lightning_attn.py`_
- **2026-06-04** [`1bdc60ed53`](https://github.com/vllm-project/vllm/commit/1bdc60ed53) [#44493](https://github.com/vllm-project/vllm/pull/44493)
  Fix Kimi-K2.5 FlashInfer ViT metadata (#44493)
  _Files: `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-06-04** [`ceb0111a90`](https://github.com/vllm-project/vllm/commit/ceb0111a90) [#43241](https://github.com/vllm-project/vllm/pull/43241)
  [Model Runner V2][Spec Decode] Add Gemma4 MTP support (#43241)
  _Files: `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/backends/utils.py`, `vllm/v1/worker/gpu/model_runner.py` _+10 more__
- **2026-06-03** [`91945b6e4a`](https://github.com/vllm-project/vllm/commit/91945b6e4a) [#44253](https://github.com/vllm-project/vllm/pull/44253)
  [Bug Fix][Model Runner V2][Spec Decode] Warmup & capture with different attention states for speculator prefill (#44253)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/eagle/cudagraph.py`, `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py`_
- **2026-06-03** [`823d271c0d`](https://github.com/vllm-project/vllm/commit/823d271c0d) [#44393](https://github.com/vllm-project/vllm/pull/44393)
  [Attention][CPU] Standardize kv layout to blocks first (#44393)
  _Files: `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-06-03** [`27a93cd426`](https://github.com/vllm-project/vllm/commit/27a93cd426) [#44366](https://github.com/vllm-project/vllm/pull/44366)
  [docker] Stop using extra-index-url for flashinfer-jit-cache (#44366)
  _Files: `docker/Dockerfile`_
- **2026-06-02** [`8b3b71ee9d`](https://github.com/vllm-project/vllm/commit/8b3b71ee9d) [#44036](https://github.com/vllm-project/vllm/pull/44036)
  [CI/Build] Bump flashinfer to v0.6.12 (#44036)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.nightly_torch`, `docker/versions.json`, `requirements/cuda.txt`_
- **2026-06-02** [`fe32e7830b`](https://github.com/vllm-project/vllm/commit/fe32e7830b) [#43669](https://github.com/vllm-project/vllm/pull/43669)
  [Bugfix] flashinfer: fail fast when --kv-cache-dtype nvfp4 used on unsupported arch (#43669)
  _Files: `vllm/v1/attention/backends/flashinfer.py`_
- **2026-06-02** [`ea0d045a05`](https://github.com/vllm-project/vllm/commit/ea0d045a05) [#44065](https://github.com/vllm-project/vllm/pull/44065)
  [FlashAttention] Sync FA with upstream (#44065)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-06-02** [`0eeba5eec1`](https://github.com/vllm-project/vllm/commit/0eeba5eec1) [#42971](https://github.com/vllm-project/vllm/pull/42971)
  Fix DFlash prefix cache corruption due to missing lookahead block (#42971)
  _Files: `tests/v1/spec_decode/test_dflash_lookahead.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-02** [`0b25cf4419`](https://github.com/vllm-project/vllm/commit/0b25cf4419) [#43534](https://github.com/vllm-project/vllm/pull/43534)
  [CPU][Perf] Enable fused kernels for GDN's gated delta rules (#43534)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/blas_gemm.h` _+7 more__

## Scheduler / Engine  (12 commits)

- **2026-06-08** [`3c0b4432be`](https://github.com/vllm-project/vllm/commit/3c0b4432be) [#44499](https://github.com/vllm-project/vllm/pull/44499)
  [Rust Frontend] Add /pause, /resume, /is_paused endpoints (#44499)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/pause.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-06** [`3b3d5287fa`](https://github.com/vllm-project/vllm/commit/3b3d5287fa) [#44560](https://github.com/vllm-project/vllm/pull/44560)
  [BugFix] Resolve multiple async kv load deadlock (#44560)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `tests/v1/kv_connector/unit/test_remote_prefill_lifecycle.py`, `tests/v1/kv_connector/unit/utils.py` _+2 more__
- **2026-06-05** [`c73b0d0db9`](https://github.com/vllm-project/vllm/commit/c73b0d0db9) [#44669](https://github.com/vllm-project/vllm/pull/44669)
  [Core][Engine] allow DP ray placement groups to be set on specific nodes (#44669)
  _Files: `tests/v1/engine/test_dp_placement_node_allowlist.py`, `vllm/envs.py`, `vllm/v1/engine/utils.py`_
- **2026-06-05** [`8a83e6f2d7`](https://github.com/vllm-project/vllm/commit/8a83e6f2d7) [#44591](https://github.com/vllm-project/vllm/pull/44591)
  [Rust Frontend] Batch auto-abort requests by engine (#44591)
  _Files: `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-06-03** [`51e0c579b0`](https://github.com/vllm-project/vllm/commit/51e0c579b0) [#44207](https://github.com/vllm-project/vllm/pull/44207)
  fix(config): validate max_num_scheduled_tokens >= 0 on all paths (#44207)
  _Files: `vllm/config/scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-03** [`309385a359`](https://github.com/vllm-project/vllm/commit/309385a359) [#43942](https://github.com/vllm-project/vllm/pull/43942)
  [Rust Frontend] Add /server_info to Rust frontend (#43942)
  _Files: `rust/src/chat/src/parser/mod.rs`, `rust/src/chat/src/renderer/hf/format.rs`, `rust/src/chat/src/renderer/selection.rs`, `rust/src/engine-core-client/src/client.rs` _+7 more__
- **2026-06-02** [`da107a59e5`](https://github.com/vllm-project/vllm/commit/da107a59e5) [#43458](https://github.com/vllm-project/vllm/pull/43458)
  [MRV2] Also enable MRV2 for Llama and Mistral dense models  (#43458)
  _Files: `tests/test_config.py`, `tests/v1/engine/test_abort_final_step.py`, `tests/v1/shutdown/test_forward_error.py`, `vllm/config/vllm.py` _+1 more__
- **2026-06-02** [`cab5c9a2a9`](https://github.com/vllm-project/vllm/commit/cab5c9a2a9) [#44274](https://github.com/vllm-project/vllm/pull/44274)
  [Core] Move `max_concurrent_batches` to `VllmConfig` (#44274)
  _Files: `tests/distributed/test_multiproc_executor.py`, `tests/distributed/test_ray_v2_executor.py`, `tests/model_executor/model_loader/tensorizer_loader/conftest.py`, `tests/v1/engine/test_engine_core.py` _+7 more__
- **2026-06-02** [`654bd2bca4`](https://github.com/vllm-project/vllm/commit/654bd2bca4) [#42967](https://github.com/vllm-project/vllm/pull/42967)
  [Bugfix] Sync block_size from EngineCore to frontend for hybrid Mamba… (#42967)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/engine/__init__.py`, `vllm/v1/engine/core.py`, `vllm/v1/engine/core_client.py`_
- **2026-06-02** [`b817b23f7b`](https://github.com/vllm-project/vllm/commit/b817b23f7b) [#43883](https://github.com/vllm-project/vllm/pull/43883)
  [Rust Frontend] add  --enable-request-id-headers flag support. (#43883)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/examples/external_engine_openai_qwen.rs` _+7 more__
- **2026-06-02** [`68dafcca75`](https://github.com/vllm-project/vllm/commit/68dafcca75) [#44267](https://github.com/vllm-project/vllm/pull/44267)
  [Refactor] Unify reasoning + tool-call parsing behind Parser.parse() (#44267)
  _Files: `tests/entrypoints/openai/test_tool_choice_content_none.py`, `tests/parser/test_parse.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/engine/serving.py` _+1 more__
- **2026-06-02** [`54d0c36fff`](https://github.com/vllm-project/vllm/commit/54d0c36fff) [#44131](https://github.com/vllm-project/vllm/pull/44131)
  [CI] Stabilize OpenAI schema fuzzing for malformed structural tags (#44131)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+2 more__

## Quantization  (12 commits)

- **2026-06-06** [`67d3792d99`](https://github.com/vllm-project/vllm/commit/67d3792d99) [#44694](https://github.com/vllm-project/vllm/pull/44694)
  [Bugfix] Fix Qwen3.5-FP8 nightly fail. Guard fused_add_rms_norm input/weight dtype mismatch in RMSNorm + quant fusion (#44694)
  _Files: `vllm/compilation/passes/fusion/rms_quant_fusion.py`_
- **2026-06-05** [`da1daf40bf`](https://github.com/vllm-project/vllm/commit/da1daf40bf) [#44571](https://github.com/vllm-project/vllm/pull/44571)
  [Bugfix] Exclude vision embedder from quantization in Gemma4 Unified (#44571)
  _Files: `vllm/model_executor/models/gemma4_unified.py`_
- **2026-06-04** [`3da29aa4a5`](https://github.com/vllm-project/vllm/commit/3da29aa4a5) [#34894](https://github.com/vllm-project/vllm/pull/34894)
  [DOC] Add INT8 W4A8 docs and Arm's supported quantization schemes (#34894)
  _Files: `docs/features/quantization/README.md`, `docs/features/quantization/llm_compressor/README.md`, `docs/features/quantization/llm_compressor/fp8.md`, `docs/features/quantization/llm_compressor/int4.md` _+3 more__
- **2026-06-04** [`9354fb1ba5`](https://github.com/vllm-project/vllm/commit/9354fb1ba5) [#44476](https://github.com/vllm-project/vllm/pull/44476)
  [Bugfix][Compile] Guard per_token_group_fp8_quant lookup on non-CUDA platforms (#44476)
  _Files: `vllm/compilation/passes/fusion/matcher_utils.py`, `vllm/compilation/passes/fusion/rms_quant_fusion.py`_
- **2026-06-04** [`e68988a248`](https://github.com/vllm-project/vllm/commit/e68988a248) [#42443](https://github.com/vllm-project/vllm/pull/42443)
  Refactor CT NVFP4 linear to use a single class (#42443)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/__init__.py` _+2 more__
- **2026-06-03** [`2b91012650`](https://github.com/vllm-project/vllm/commit/2b91012650) [#44122](https://github.com/vllm-project/vllm/pull/44122)
  [Refactor] Remove dead code fp quant (#44122)
  _Files: `vllm/model_executor/layers/quantization/fp_quant.py`_
- **2026-06-03** [`e5232679a3`](https://github.com/vllm-project/vllm/commit/e5232679a3) [#39968](https://github.com/vllm-project/vllm/pull/39968)
  [XPU] Add XPU block-scaled W8A8 fp8 path (#39968)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/triton.py`, `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-06-02** [`3f3e2702c2`](https://github.com/vllm-project/vllm/commit/3f3e2702c2) [#43963](https://github.com/vllm-project/vllm/pull/43963)
  [XPU] Enable rms_norm/act quant fusions (#43963)
  _Files: `vllm/compilation/passes/fusion/act_quant_fusion.py`, `vllm/compilation/passes/fusion/rms_quant_fusion.py`, `vllm/compilation/passes/pass_manager.py`, `vllm/platforms/xpu.py`_
- **2026-06-02** [`f91fb2fcf3`](https://github.com/vllm-project/vllm/commit/f91fb2fcf3) [#43798](https://github.com/vllm-project/vllm/pull/43798)
  [Bugfix] Convert Gemma4-MM ViT linear layers to vllm native impl (#43798)
  _Files: `vllm/model_executor/layers/quantization/bitsandbytes.py`, `vllm/model_executor/model_loader/bitsandbytes_loader.py`, `vllm/model_executor/models/gemma4_mm.py`, `vllm/model_executor/models/transformers/utils.py`_
- **2026-06-02** [`a3a5a5ece5`](https://github.com/vllm-project/vllm/commit/a3a5a5ece5) [#43930](https://github.com/vllm-project/vllm/pull/43930)
  [XPU][Bugfix] Fix per_token_group_fp8_quant missing dummy args on XPU (#43930)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`_
- **2026-06-01** [`035733515f`](https://github.com/vllm-project/vllm/commit/035733515f) [#44161](https://github.com/vllm-project/vllm/pull/44161)
  [Kernel][DSv4] Optimize sparse FP8 compressor kernels (#44161)
  _Files: `vllm/models/deepseek_v4/nvidia/ops/sparse_attn_compress_cutedsl.py`_
- **2026-06-01** [`985c97a6a8`](https://github.com/vllm-project/vllm/commit/985c97a6a8) [#43706](https://github.com/vllm-project/vllm/pull/43706)
  [Perf] Optimize cutlass fp8 scaled mm bypassing padding, 20% kernel performance improvement (#43706)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`_

## KV Cache / Offload  (11 commits)

- **2026-06-07** [`4dcd10eb0d`](https://github.com/vllm-project/vllm/commit/4dcd10eb0d) [#44454](https://github.com/vllm-project/vllm/pull/44454)
  [1/N][KV-Cache Layout Refactor] Refactor DSV4 KV cache config construction (#44454)
  _Files: `vllm/v1/core/kv_cache_utils.py`_
- **2026-06-07** [`810966453a`](https://github.com/vllm-project/vllm/commit/810966453a) [#36423](https://github.com/vllm-project/vllm/pull/36423)
  [XPU] Support  cpu kv offloading and tiering offloading on XPU platform (#36423)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/_custom_ops.py` _+3 more__
- **2026-06-05** [`6a894574bf`](https://github.com/vllm-project/vllm/commit/6a894574bf) [#41968](https://github.com/vllm-project/vllm/pull/41968)
  Add objectstore as a secondary tier to multi-tier kv cache offloading (#41968)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/factory.py`, `vllm/v1/kv_offload/tiering/obj/__init__.py`, `vllm/v1/kv_offload/tiering/obj/config.py` _+2 more__
- **2026-06-04** [`68f5e565c9`](https://github.com/vllm-project/vllm/commit/68f5e565c9) [#42554](https://github.com/vllm-project/vllm/pull/42554)
  [PD][Nixl] Mamba prefix caching mode support  (#42554)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-04** [`a6183563b6`](https://github.com/vllm-project/vllm/commit/a6183563b6) [#43447](https://github.com/vllm-project/vllm/pull/43447)
  [Prefix Caching] DeepSeekv4 - Support selective prefix-cache retention for sliding-window KV cache (#43447)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/envs.py`, `vllm/v1/core/block_pool.py` _+3 more__
- **2026-06-03** [`0c6631f02a`](https://github.com/vllm-project/vllm/commit/0c6631f02a) [#37505](https://github.com/vllm-project/vllm/pull/37505)
  [KVCache] Support Pluggable KVCacheSpec (#37505)
  _Files: `tests/v1/core/utils.py`, `tests/v1/simple_kv_offload/test_scheduler.py`, `tests/v1/test_kv_cache_spec_registry.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py` _+7 more__
- **2026-06-03** [`7268457999`](https://github.com/vllm-project/vllm/commit/7268457999) [#44287](https://github.com/vllm-project/vllm/pull/44287)
  [KV Offloading] Enable HMA models for Tiering Offloading (#44287)
  _Files: `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-06-03** [`3f0a91bb96`](https://github.com/vllm-project/vllm/commit/3f0a91bb96) [#44293](https://github.com/vllm-project/vllm/pull/44293)
  Nit Changes in Tiered KV Offload (#44293)
  _Files: `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/fs/manager.py`_
- **2026-06-02** [`2a2b5ca791`](https://github.com/vllm-project/vllm/commit/2a2b5ca791) [#44206](https://github.com/vllm-project/vllm/pull/44206)
  [KV Offload] Add `on_schedule_end()` hook to separate step lifecycle from event draining (#44206)
  _Files: `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py`, `vllm/v1/kv_offload/tiering/base.py` _+1 more__
- **2026-06-02** [`7c37096620`](https://github.com/vllm-project/vllm/commit/7c37096620) [#44165](https://github.com/vllm-project/vllm/pull/44165)
  [Core][Refactor]: thread `scheduler_block_size` into KVCacheManager and KVCacheCoordinator (#44165)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+5 more__
- **2026-06-02** [`8a9eb40808`](https://github.com/vllm-project/vllm/commit/8a9eb40808) [#43990](https://github.com/vllm-project/vllm/pull/43990)
  [Model Runner V2] Support zeroing freshly allocated KV blocks for hybrid + fp8 KVCache (#43990)
  _Files: `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/utils.py`_

## CI / Build  (10 commits)

- **2026-06-07** [`3d3ba460a2`](https://github.com/vllm-project/vllm/commit/3d3ba460a2) [#43087](https://github.com/vllm-project/vllm/pull/43087)
  Modify torch dependency in xpu.txt (#43087)
  _Files: `requirements/xpu.txt`_
- **2026-06-07** [`66ecfd0568`](https://github.com/vllm-project/vllm/commit/66ecfd0568) [#42599](https://github.com/vllm-project/vllm/pull/42599)
  [Dependency] Remove stale cuDNN frontend upper bound (#42599)
  _Files: `requirements/cuda.txt`_
- **2026-06-05** [`b593396c7a`](https://github.com/vllm-project/vllm/commit/b593396c7a) [#44621](https://github.com/vllm-project/vllm/pull/44621)
  Upgrade tpu-inference to v0.21.0 (#44621)
  _Files: `requirements/tpu.txt`_
- **2026-06-05** [`c505cd93ef`](https://github.com/vllm-project/vllm/commit/c505cd93ef) [#44605](https://github.com/vllm-project/vllm/pull/44605)
  [CI/Build] Disable CPU-Compatibility Tests (#44605)
  _Files: `.buildkite/hardware_tests/cpu.yaml`_
- **2026-06-03** [`df7252c343`](https://github.com/vllm-project/vllm/commit/df7252c343) [#44174](https://github.com/vllm-project/vllm/pull/44174)
  [CI] Align PD tests to HMA on by default (#44174)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/config_sweep_spec_decode_test.sh`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/spec_decode_acceptance_test.sh` _+1 more__
- **2026-06-03** [`e67063826b`](https://github.com/vllm-project/vllm/commit/e67063826b) [#44352](https://github.com/vllm-project/vllm/pull/44352)
  [CI] Add missing vllm/parser/ CI trigger and fix test_parse.py  (#44352)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/parser/test_parse.py`_
- **2026-06-03** [`53b88d1dfc`](https://github.com/vllm-project/vllm/commit/53b88d1dfc) [#44042](https://github.com/vllm-project/vllm/pull/44042)
  [CI] Reject out-of-vocabulary  before they reach the GPU logprob path (#44042)
  _Files: `tests/v1/sample/test_logprobs.py`, `vllm/sampling_params.py`, `vllm/v1/sample/thinking_budget_state.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-03** [`bd98e97557`](https://github.com/vllm-project/vllm/commit/bd98e97557) [#44128](https://github.com/vllm-project/vllm/pull/44128)
  [Misc] Remove dead VLLM_RPC_TIMEOUT env var and fix profiling doc that references it (#44128)
  _Files: `.buildkite/performance-benchmarks/tests/latency-tests-arm64-cpu.json`, `.buildkite/performance-benchmarks/tests/latency-tests-cpu.json`, `.buildkite/performance-benchmarks/tests/serving-tests-arm64-cpu.json`, `.buildkite/performance-benchmarks/tests/serving-tests-cpu-asr.json` _+7 more__
- **2026-06-01** [`6f8b40a23f`](https://github.com/vllm-project/vllm/commit/6f8b40a23f) [#44248](https://github.com/vllm-project/vllm/pull/44248)
  [BugFix][CI] Fix added `_has_module` tests (#44248)
  _Files: `tests/utils_/test_import_utils.py`_
- **2026-06-01** [`98f1279815`](https://github.com/vllm-project/vllm/commit/98f1279815) [#42730](https://github.com/vllm-project/vllm/pull/42730)
  [CPU][RISC-V] Add missing RVV cpu_types helpers for WNA16 (#42730)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_impl.hpp`, `csrc/cpu/torch_bindings.cpp`_

## Serving / API  (10 commits)

- **2026-06-05** [`703fb17b13`](https://github.com/vllm-project/vllm/commit/703fb17b13) [#44330](https://github.com/vllm-project/vllm/pull/44330)
  [Bugfix] GPT-OSS instruction rendering (#44330)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/parser/test_harmony_render_parity.py`, `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_response_input_to_harmony.py` _+5 more__
- **2026-06-05** [`e64237ae82`](https://github.com/vllm-project/vllm/commit/e64237ae82) [#44391](https://github.com/vllm-project/vllm/pull/44391)
  [Rust Frontend] Support include_reasoning=false (#44391)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-05** [`6542d48964`](https://github.com/vllm-project/vllm/commit/6542d48964) [#44618](https://github.com/vllm-project/vllm/pull/44618)
  [Bugfix] Fix test_invocations flaky failure with newer openai SDK (#44618)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat.py`_
- **2026-06-05** [`ef3af56a97`](https://github.com/vllm-project/vllm/commit/ef3af56a97) [#44617](https://github.com/vllm-project/vllm/pull/44617)
  Fix `LLM.wait_for_completion` output type docstring (#44617)
  _Files: `vllm/entrypoints/llm.py`_
- **2026-06-03** [`209709a8c1`](https://github.com/vllm-project/vllm/commit/209709a8c1) [#44348](https://github.com/vllm-project/vllm/pull/44348)
  [Bugfix] Fix unstreamed tool call args dropped in Responses API streaming (#44348)
  _Files: `tests/parser/test_streaming.py`, `vllm/entrypoints/openai/responses/serving.py`, `vllm/parser/abstract_parser.py`_
- **2026-06-03** [`f0204358d9`](https://github.com/vllm-project/vllm/commit/f0204358d9) [#43862](https://github.com/vllm-project/vllm/pull/43862)
  [Bugfix] fix crash in postprocess for null tool args  (#43862)
  _Files: `tests/entrypoints/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-06-02** [`ed9a7526b6`](https://github.com/vllm-project/vllm/commit/ed9a7526b6) [#44283](https://github.com/vllm-project/vllm/pull/44283)
  [Anthropic] Support system role messages inside messages array (#44283)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-02** [`e30313220c`](https://github.com/vllm-project/vllm/commit/e30313220c) [#42977](https://github.com/vllm-project/vllm/pull/42977)
  [Parser] Migrate `ResponsesParser` to unified `Parser` interface (#42977)
  _Files: `tests/entrypoints/openai/test_responses_parser_unified.py`, `vllm/entrypoints/openai/parser/responses_parser.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/serving.py`_
- **2026-06-02** [`9affc17a05`](https://github.com/vllm-project/vllm/commit/9affc17a05) [#44017](https://github.com/vllm-project/vllm/pull/44017)
  [Refactor] Move unstreamed tool-arg flush from serving layer to parser (#44017)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/parser/test_streaming.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/parser/abstract_parser.py` _+1 more__
- **2026-06-01** [`f46e6be169`](https://github.com/vllm-project/vllm/commit/f46e6be169) [#36254](https://github.com/vllm-project/vllm/pull/36254)
  [Misc] Use VLLMValidationError consistently in chat completion and completion protocol validators (#36254)
  _Files: `tests/tool_use/test_chat_completion_request_validations.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`_

## Speculative Decoding  (5 commits)

- **2026-06-07** [`32f34d3935`](https://github.com/vllm-project/vllm/commit/32f34d3935) [#44420](https://github.com/vllm-project/vllm/pull/44420)
  [feature] add index share feature for DSA MTP (#44420)
  _Files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/transformers_utils/model_arch_config_convertor.py`, `vllm/v1/spec_decode/llm_base_proposer.py` _+1 more__
- **2026-06-03** [`a248b45d05`](https://github.com/vllm-project/vllm/commit/a248b45d05) [#44429](https://github.com/vllm-project/vllm/pull/44429)
  [Model] Add Gemma4 Unified (encoder-free)  support (#44429)
  _Files: `docs/features/speculative_decoding/mtp.md`, `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_gemma4_unified.py`, `tests/models/registry.py` _+10 more__
- **2026-06-02** [`e9e08c49b9`](https://github.com/vllm-project/vllm/commit/e9e08c49b9) [#44082](https://github.com/vllm-project/vllm/pull/44082)
  [Bugfix] Cache the EAGLE/MTP lookahead block in the SWA prefix-cache mask (#44082)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`, `vllm/v1/core/kv_cache_coordinator.py` _+1 more__
- **2026-06-02** [`1edfd09ffd`](https://github.com/vllm-project/vllm/commit/1edfd09ffd) [#43991](https://github.com/vllm-project/vllm/pull/43991)
  [Model Runner V2] Use actual batch max_seq_len for attn metadata (#43991)
  _Files: `vllm/v1/worker/gpu/model_states/default.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`, `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py`_
- **2026-06-01** [`4721bb3aa4`](https://github.com/vllm-project/vllm/commit/4721bb3aa4) [#44078](https://github.com/vllm-project/vllm/pull/44078)
  [MRV2] Remove Eagle's dedicated CUDA graph pool (#44078)
  _Files: `vllm/v1/worker/gpu/spec_decode/eagle/cudagraph.py`, `vllm/v1/worker/gpu/spec_decode/eagle/speculator.py`_

## Perf / Benchmark  (4 commits)

- **2026-06-08** [`d5fe994e79`](https://github.com/vllm-project/vllm/commit/d5fe994e79) [#44419](https://github.com/vllm-project/vllm/pull/44419)
  [CPU][Spec Decode] Warn about throughput loss when libiomp5 is not preloaded (#44419)
  _Files: `vllm/v1/worker/cpu_worker.py`_
- **2026-06-03** [`1fa9ea09f6`](https://github.com/vllm-project/vllm/commit/1fa9ea09f6) [#42212](https://github.com/vllm-project/vllm/pull/42212)
  [Perf] Triton fast path for small CPU→GPU `swap_blocks_batch` in the offloading connector (#42212)
  _Files: `tests/v1/kv_offload/cpu/test_swap_blocks_triton.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`, `vllm/v1/kv_offload/cpu/swap_blocks_triton.py`_
- **2026-06-03** [`9af53a3c13`](https://github.com/vllm-project/vllm/commit/9af53a3c13) [#44251](https://github.com/vllm-project/vllm/pull/44251)
  [Perf] Add tuned selective_state_update configs for H200 and RTX PRO … (#44251)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=NVIDIA_H200,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=NVIDIA_H200,cache_dtype=float32.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Server_Edition,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Server_Edition,cache_dtype=float32.json`_
- **2026-06-03** [`e0081ef8cf`](https://github.com/vllm-project/vllm/commit/e0081ef8cf) [#44244](https://github.com/vllm-project/vllm/pull/44244)
  [Benchmark] Enable reasoning-model (thinking) benchmarking via `--chat-template-kwargs` for client-rendered datasets (#44244)
  _Files: `tests/benchmarks/test_custom_dataset_chat_template_kwargs.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/serve.py`_

## Compilation / CUDA Graph  (4 commits)

- **2026-06-08** [`8fb0274415`](https://github.com/vllm-project/vllm/commit/8fb0274415) [#44484](https://github.com/vllm-project/vllm/pull/44484)
  [MM][CG] Simplify ViT CUDA graph interfaces (#44484)
  _Files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/step3_vl.py`_
- **2026-06-06** [`2f27c9a150`](https://github.com/vllm-project/vllm/commit/2f27c9a150) [#44574](https://github.com/vllm-project/vllm/pull/44574)
  Preserve layout-changing clones (#44574)
  _Files: `tests/compile/passes/ir/test_clone_cleanup.py`, `vllm/compilation/passes/ir/clone_elimination.py`_
- **2026-06-04** [`d0975a4b50`](https://github.com/vllm-project/vllm/commit/d0975a4b50) [#42646](https://github.com/vllm-project/vllm/pull/42646)
  [perf] Add gemma RMS AR fusion (#42646)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/model_executor/layers/layernorm.py`_
- **2026-06-02** [`a045c7425f`](https://github.com/vllm-project/vllm/commit/a045c7425f) [#41714](https://github.com/vllm-project/vllm/pull/41714)
  [MM][CG] Profile encoder CUDA graph pool memory (#41714)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/utils/import_utils.py`, `vllm/v1/worker/encoder_cudagraph.py`, `vllm/v1/worker/gpu_model_runner.py`_

## LoRA  (4 commits)

- **2026-06-04** [`0c1e6f63f5`](https://github.com/vllm-project/vllm/commit/0c1e6f63f5) [#44410](https://github.com/vllm-project/vllm/pull/44410)
  [Bugfix] Fix VLLMNotFoundError when using LoRA adapter name in poolin… (#44410)
  _Files: `tests/entrypoints/serve/lora/test_serving_models.py`, `vllm/entrypoints/pooling/base/serving.py`_
- **2026-06-03** [`271328e256`](https://github.com/vllm-project/vllm/commit/271328e256) [#44413](https://github.com/vllm-project/vllm/pull/44413)
  [LoRA] Fix dedup for post-replacement module aliases (#44413)
  _Files: `vllm/lora/model_manager.py`_
- **2026-06-03** [`4d1fd13613`](https://github.com/vllm-project/vllm/commit/4d1fd13613) [#44425](https://github.com/vllm-project/vllm/pull/44425)
  [CI/Build] Fix LoRA testing (#44425)
  _Files: `vllm/entrypoints/openai/models/serving.py`_
- **2026-06-03** [`6550ff12f2`](https://github.com/vllm-project/vllm/commit/6550ff12f2) [#43778](https://github.com/vllm-project/vllm/pull/43778)
  [Rust Frontend] Add dynamic LoRA endpoints (#43778)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/request.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs` _+20 more__

## Docs  (3 commits)

- **2026-06-05** [`efc347f1b2`](https://github.com/vllm-project/vllm/commit/efc347f1b2) [#44066](https://github.com/vllm-project/vllm/pull/44066)
  docs: fix tokenizer optimization typo (#44066)
  _Files: `docs/configuration/optimization.md`_
- **2026-06-04** [`f35b557239`](https://github.com/vllm-project/vllm/commit/f35b557239) [#44534](https://github.com/vllm-project/vllm/pull/44534)
  Add GH token to docs build pre run check (#44534)
  _Files: `docs/pre_run_check.sh`_
- **2026-06-02** [`0917a009d3`](https://github.com/vllm-project/vllm/commit/0917a009d3) [#44345](https://github.com/vllm-project/vllm/pull/44345)
  Fix sparse NCCL weight transfer test construction (#44345)
  _Files: `docs/training/weight_transfer/base.md`, `tests/distributed/test_weight_transfer.py`_

---
_Generated 2026-06-08 12:46 UTC_