# vllm-project/vllm — Weekly Change Report
**Period:** 2026-06-08 → 2026-06-15  |  **Total commits:** 281

## ✨ New Features This Week

- **2026-06-15** [#43914](https://github.com/vllm-project/vllm/pull/43914) — Remove redundant Triton KV cache dtype asserts and enforce architectural support (fp8 >= sm89) (#43914)
- **2026-06-15** [#45671](https://github.com/vllm-project/vllm/pull/45671) — [ROCm][Doc] Add installation notes about python version requirement (#45671)
- **2026-06-15** [#44760](https://github.com/vllm-project/vllm/pull/44760) — [Rust Frontend] Support `parallel_tool_calls = false` (#44760)
- **2026-06-15** [#45137](https://github.com/vllm-project/vllm/pull/45137) — [Rust Frontend] Add external→internal request-id map for abort() (#45137)
- **2026-06-15** [#45458](https://github.com/vllm-project/vllm/pull/45458) — [Feature][Frontend] Report multimodal token counts in usage.prompt_tokens_details (#45458)
- **2026-06-15** [#45413](https://github.com/vllm-project/vllm/pull/45413) — [Frontend] Add Streaming Parser Engine and new Qwen3 Parser (#45413)
- **2026-06-15** [#38608](https://github.com/vllm-project/vllm/pull/38608) — [XPU] Enable sequence parallel support for XPU (#38608)
- **2026-06-15** [#45173](https://github.com/vllm-project/vllm/pull/45173) — Added real  /v1/embeddings support for messages + chat_template_kw  (#45173)
- **2026-06-14** [#45566](https://github.com/vllm-project/vllm/pull/45566) — [Perf] Use bisect for mm feature lookup in model runner v2 (#45566)
- **2026-06-14** [#44400](https://github.com/vllm-project/vllm/pull/44400) — [ROCm][Perf] Enable W4A16 FlyDSL MoE (#44400)
- _…and 50 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-15** [`25c53d1293`](https://github.com/vllm-project/vllm/commit/25c53d1293) [#45671](https://github.com/vllm-project/vllm/pull/45671) — [ROCm][Doc] Add installation notes about python version requirement (#45671)
- **2026-06-14** [`725c3bc808`](https://github.com/vllm-project/vllm/commit/725c3bc808) [#44400](https://github.com/vllm-project/vllm/pull/44400) — [ROCm][Perf] Enable W4A16 FlyDSL MoE (#44400)
- **2026-06-12** [`badddd254f`](https://github.com/vllm-project/vllm/commit/badddd254f) [#45103](https://github.com/vllm-project/vllm/pull/45103) — [ROCm][DSV4][Perf] Fuse inverse-RoPE and cache bf16 wo_a in o-projection (#45103)
- **2026-06-12** [`39cb9bf292`](https://github.com/vllm-project/vllm/commit/39cb9bf292) [#45362](https://github.com/vllm-project/vllm/pull/45362) — [ROCm] Bump Torch to 2.11 (#45362)
- **2026-06-12** [`aab639c705`](https://github.com/vllm-project/vllm/commit/aab639c705) [#43154](https://github.com/vllm-project/vllm/pull/43154) — [Core][AMD] Propagate shutdown timeout to MultiprocExecutor (#43154)
- **2026-06-12** [`6635279d8a`](https://github.com/vllm-project/vllm/commit/6635279d8a) [#39612](https://github.com/vllm-project/vllm/pull/39612) — [Migration] Migrate GGUF quantization support to plugin (#39612)
- **2026-06-12** [`2043258dec`](https://github.com/vllm-project/vllm/commit/2043258dec) [#45003](https://github.com/vllm-project/vllm/pull/45003) — [Frontend]  Support strict mode for tool calling (#45003)
- **2026-06-12** [`fe04238292`](https://github.com/vllm-project/vllm/commit/fe04238292) [#44893](https://github.com/vllm-project/vllm/pull/44893) — [ROCm][gpt-oss] Pass GateMode.INTERLEAVE for MXFP4 W4A16 fused MoE (#44893)
- **2026-06-12** [`1ce3cdc5c1`](https://github.com/vllm-project/vllm/commit/1ce3cdc5c1) [#45302](https://github.com/vllm-project/vllm/pull/45302) — [ROCm][CI] fix fp8 support for test_deepep_moe (#45302)
- **2026-06-12** [`fcf5115c45`](https://github.com/vllm-project/vllm/commit/fcf5115c45) [#44899](https://github.com/vllm-project/vllm/pull/44899) — [ROCm][DSv4][Perf] Flash-decode split-K decode attention kernel (#44899)
- **2026-06-11** [`2ec6594db9`](https://github.com/vllm-project/vllm/commit/2ec6594db9) [#36902](https://github.com/vllm-project/vllm/pull/36902) — [Kernel][Helion][1/N] Add Helion kernel for per_token_group_fp8_quant (#36902)
- **2026-06-11** [`43914dd743`](https://github.com/vllm-project/vllm/commit/43914dd743) [#44624](https://github.com/vllm-project/vllm/pull/44624) — [Rust Frontend] Add Python bridge for Rust tool parsers (#44624)
- **2026-06-10** [`16282a9c4e`](https://github.com/vllm-project/vllm/commit/16282a9c4e) [#45170](https://github.com/vllm-project/vllm/pull/45170) — [ROCm][CI] Moving MI300 tests to MI325 until cluster is stabilized (#45170)
- **2026-06-10** [`5b6b536fdc`](https://github.com/vllm-project/vllm/commit/5b6b536fdc) [#44679](https://github.com/vllm-project/vllm/pull/44679) — [ROCm][Bugfix] Make intermediate_pad TP-aware in rocm_aiter_fused_experts (#44679)
- **2026-06-10** [`bfe1001ab6`](https://github.com/vllm-project/vllm/commit/bfe1001ab6) [#45169](https://github.com/vllm-project/vllm/pull/45169) — [Bugfix] [DSV4] [ROCm] Pin apache-tvm-ffi version to `0.1.10` (#45169)
- **2026-06-10** [`4673ca1d78`](https://github.com/vllm-project/vllm/commit/4673ca1d78) [#44821](https://github.com/vllm-project/vllm/pull/44821) — fix: prefix DeepSeek V4 MTP projections (#44821)
- **2026-06-10** [`3cc9fecd58`](https://github.com/vllm-project/vllm/commit/3cc9fecd58) [#45131](https://github.com/vllm-project/vllm/pull/45131) — Deprecated 1st generation Qwen and QwenVL models (#45131)
- **2026-06-10** [`fdfb2566c0`](https://github.com/vllm-project/vllm/commit/fdfb2566c0) [#44981](https://github.com/vllm-project/vllm/pull/44981) — [Rust Frontend] [CI] Unify Rust artifact builds with setuptools-rust (#44981)
- **2026-06-10** [`32daf56b42`](https://github.com/vllm-project/vllm/commit/32daf56b42) [#45011](https://github.com/vllm-project/vllm/pull/45011) — [Refactor] Rename rocm_moe.py to rocm_moe_rdna.py (#45011)
- **2026-06-10** [`82a42234be`](https://github.com/vllm-project/vllm/commit/82a42234be) [#44823](https://github.com/vllm-project/vllm/pull/44823) — [ROCm][CI] Defer AITER sampler import and isolate server test PYTHONPATH (#44823)
- **2026-06-10** [`bb78168b21`](https://github.com/vllm-project/vllm/commit/bb78168b21) [#44804](https://github.com/vllm-project/vllm/pull/44804) — [ROCm][gpt-oss] Hybrid CDNA4 swizzle gate for A8W4 MoE (#44804)
- **2026-06-09** [`d955745d58`](https://github.com/vllm-project/vllm/commit/d955745d58) [#44678](https://github.com/vllm-project/vllm/pull/44678) — [ROCm][CI] fix test_rope_kvcache_fusion.py (#44678)
- **2026-06-09** [`c9c1540e61`](https://github.com/vllm-project/vllm/commit/c9c1540e61) [#44936](https://github.com/vllm-project/vllm/pull/44936) — [ROCm][V2] Fix failed assertion in Llama models when using EAGLE with `ROCM_AITER_FA` (#44936)
- **2026-06-09** [`c1d754d681`](https://github.com/vllm-project/vllm/commit/c1d754d681) [#43799](https://github.com/vllm-project/vllm/pull/43799) — [Mooncake] Use all HCAs on multi-NIC hosts instead of GPU-indexed RNIC selection (#43799)
- **2026-06-09** [`01d8cd92dd`](https://github.com/vllm-project/vllm/commit/01d8cd92dd) [#44945](https://github.com/vllm-project/vllm/pull/44945) — [ROCm][Perf] Use fused softplus-sqrt-topk router under AITER fused-MoE (#44945)
- **2026-06-09** [`b697119800`](https://github.com/vllm-project/vllm/commit/b697119800) [#44040](https://github.com/vllm-project/vllm/pull/44040) — [ROCm][CI] Stabilize ModernBERT token-classification parity against Hugging Face (#44040)
- **2026-06-09** [`80e2c4462d`](https://github.com/vllm-project/vllm/commit/80e2c4462d) [#42864](https://github.com/vllm-project/vllm/pull/42864) — [ROCm][Compile] Fuse AR + RMSNorm + per-group FP8 quant (+ DSv3.2 indexer fan-out) (#42864)
- **2026-06-09** [`2385e140d6`](https://github.com/vllm-project/vllm/commit/2385e140d6) [#43022](https://github.com/vllm-project/vllm/pull/43022) — [ROCm][CI] Stabilize sleep-mode memory release (#43022)
- **2026-06-09** [`996222f4bf`](https://github.com/vllm-project/vllm/commit/996222f4bf) [#44947](https://github.com/vllm-project/vllm/pull/44947) — [CI] Reorganize entrypoints CI (#44947)
- **2026-06-09** [`baacbfcebf`](https://github.com/vllm-project/vllm/commit/baacbfcebf) [#42978](https://github.com/vllm-project/vllm/pull/42978) — [ROCm][MLA][Bugfix] Reserve FP8 prefill workspace before lock for Kimi-K2.5 (#42978)
- **2026-06-08** [`05cb606cad`](https://github.com/vllm-project/vllm/commit/05cb606cad) [#44809](https://github.com/vllm-project/vllm/pull/44809) — [ROCm][CI] Re-route NixlConnector jobs (#44809)
- **2026-06-08** [`dc68bd8c41`](https://github.com/vllm-project/vllm/commit/dc68bd8c41) [#41184](https://github.com/vllm-project/vllm/pull/41184) — [MoE Refactor] FusedMoE/MoERunner inversion refactor (#41184)
- **2026-06-08** [`93ee4cd47f`](https://github.com/vllm-project/vllm/commit/93ee4cd47f) [#44819](https://github.com/vllm-project/vllm/pull/44819) — [CI] Consolidate multimodal entrypoint tests. (#44819)
- **2026-06-08** [`5add018beb`](https://github.com/vllm-project/vllm/commit/5add018beb) [#44854](https://github.com/vllm-project/vllm/pull/44854) — [Connector] Remove `P2pNcclConnector` (#44854)
- **2026-06-08** [`d9ff7e4e9a`](https://github.com/vllm-project/vllm/commit/d9ff7e4e9a) [#44761](https://github.com/vllm-project/vllm/pull/44761) — [ROCm][CI] Stabilizing teardown and timeout of flaky tests to prevent rare OOMs (#44761)
- **2026-06-08** [`967c5c3bc3`](https://github.com/vllm-project/vllm/commit/967c5c3bc3) [#42793](https://github.com/vllm-project/vllm/pull/42793) — [ROCm][CI] Stage C mirrors (#42793)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#45414](https://github.com/vllm-project/vllm/issues/45414) | [Bug]: Scheduler deadlocks without KV-cache connector | bug | 2026-06-15 |
| [#45702](https://github.com/vllm-project/vllm/issues/45702) | [RFC]: Fine-Grained Prefix Cache Hits for Hybrid Models | RFC | 2026-06-15 |
| [#45704](https://github.com/vllm-project/vllm/issues/45704) | [Bug]: SimpleCPUOffloadConnector corrupts restored KV under load → int | — | 2026-06-15 |
| [#45699](https://github.com/vllm-project/vllm/issues/45699) | [Bug]: Prefix caching on Nemotron Ultra breaks gsm8k | bug | 2026-06-15 |
| [#45698](https://github.com/vllm-project/vllm/issues/45698) | [Bug]: DeepSeek V4 TileLang MHC path produces incorrect output on gfx9 | bug, rocm | 2026-06-15 |
| [#45568](https://github.com/vllm-project/vllm/issues/45568) | [Bug]: Pre-quantized MXFP8 checkpoint (config.json quant_method: "mxfp | — | 2026-06-15 |
| [#44430](https://github.com/vllm-project/vllm/issues/44430) | [Bug]: --load-format runai_streamer retains ~the full checkpoint in ho | — | 2026-06-15 |
| [#45689](https://github.com/vllm-project/vllm/issues/45689) | [Bug]: DiffusionGemma chat logprobs can crash in batched requests | bug | 2026-06-15 |
| [#45455](https://github.com/vllm-project/vllm/issues/45455) | [Bug]: Pipeline paralelism not supported on Minimax-M3 | bug | 2026-06-15 |
| [#45670](https://github.com/vllm-project/vllm/issues/45670) | [Bug]: CUDA error: an illegal memory access was encountered when using | bug | 2026-06-15 |
| [#45669](https://github.com/vllm-project/vllm/issues/45669) | [Bug]: Draft model produces degenerate output (token_id=0) in speculat | bug | 2026-06-15 |
| [#45482](https://github.com/vllm-project/vllm/issues/45482) | [Feature]:  MXFP4 ROCm MiniMax M3 checkpoint & support | feature request, rocm | 2026-06-15 |
| [#45661](https://github.com/vllm-project/vllm/issues/45661) | [Bug]: NotImplementedError: No NvFp4 MoE backend supports the deployme | bug | 2026-06-15 |
| [#45591](https://github.com/vllm-project/vllm/issues/45591) | [Bug]: `--override-generation-config` silently drops `eos_token_id` fr | — | 2026-06-15 |
| [#45658](https://github.com/vllm-project/vllm/issues/45658) | [Bug]: AssertionError: Encoder cache miss | bug | 2026-06-15 |
| [#43226](https://github.com/vllm-project/vllm/issues/43226) | [Bug]: EngineCore crash — assert req_id in self.requests in _update_fr | — | 2026-06-15 |
| [#44522](https://github.com/vllm-project/vllm/issues/44522) | Gemma-4 tool call parser leaks raw tokens (<|" and "|>) into streaming | bug | 2026-06-15 |
| [#45597](https://github.com/vllm-project/vllm/issues/45597) | [Bug]: fastapi error '_IncludedRouter' object has no attribute 'path' | bug | 2026-06-15 |
| [#43381](https://github.com/vllm-project/vllm/issues/43381) | [Bug]: RuntimeError: UVA is not available | bug | 2026-06-15 |
| [#34118](https://github.com/vllm-project/vllm/issues/34118) | [Feature]: [ROCm]: GPTQ INT4 MoE kernel fails on non-SiLU activations  | feature request, rocm, stale | 2026-06-15 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 34 |
| Other | 33 |
| Multimodal | 29 |
| MoE / Expert Parallel | 28 |
| Serving / API | 26 |
| Attention | 25 |
| Models | 21 |
| Quantization | 16 |
| CI / Build | 14 |
| Disaggregation / PD | 14 |
| Scheduler / Engine | 13 |
| Perf / Benchmark | 6 |
| Docs | 6 |
| Speculative Decoding | 5 |
| KV Cache / Offload | 5 |
| LoRA | 3 |
| Compilation / CUDA Graph | 3 |

## ROCm / AMD  (34 commits)

- **2026-06-15** [`25c53d1293`](https://github.com/vllm-project/vllm/commit/25c53d1293) [#45671](https://github.com/vllm-project/vllm/pull/45671)
  [ROCm][Doc] Add installation notes about python version requirement (#45671)
  _Files: `docs/getting_started/installation/gpu.rocm.inc.md`_
- **2026-06-14** [`725c3bc808`](https://github.com/vllm-project/vllm/commit/725c3bc808) [#44400](https://github.com/vllm-project/vllm/pull/44400)
  [ROCm][Perf] Enable W4A16 FlyDSL MoE (#44400)
  _Files: `benchmarks/kernels/benchmark_flydsl_moe_w4a16.py`, `tests/kernels/moe/test_flydsl_moe.py`, `vllm/config/kernel.py`, `vllm/model_executor/layers/fused_moe/configs/E=384,N=256,device_name=AMD_Instinct_MI350X,dtype=int4_w4a16,backend=flydsl.json` _+11 more__
- **2026-06-12** [`badddd254f`](https://github.com/vllm-project/vllm/commit/badddd254f) [#45103](https://github.com/vllm-project/vllm/pull/45103)
  [ROCm][DSV4][Perf] Fuse inverse-RoPE and cache bf16 wo_a in o-projection (#45103)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-06-12** [`39cb9bf292`](https://github.com/vllm-project/vllm/commit/39cb9bf292) [#45362](https://github.com/vllm-project/vllm/pull/45362)
  [ROCm] Bump Torch to 2.11 (#45362)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-06-12** [`aab639c705`](https://github.com/vllm-project/vllm/commit/aab639c705) [#43154](https://github.com/vllm-project/vllm/pull/43154)
  [Core][AMD] Propagate shutdown timeout to MultiprocExecutor (#43154)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `tests/v1/executor/test_executor.py`, `vllm/envs.py`, `vllm/v1/engine/core_client.py` _+1 more__
- **2026-06-12** [`6635279d8a`](https://github.com/vllm-project/vllm/commit/6635279d8a) [#39612](https://github.com/vllm-project/vllm/pull/39612)
  [Migration] Migrate GGUF quantization support to plugin (#39612)
  _Files: `.buildkite/test_areas/plugins.yaml`, `.github/dependabot.yml`, `.pre-commit-config.yaml`, `CMakeLists.txt` _+53 more__
- **2026-06-12** [`2043258dec`](https://github.com/vllm-project/vllm/commit/2043258dec) [#45003](https://github.com/vllm-project/vllm/pull/45003)
  [Frontend]  Support strict mode for tool calling (#45003)
  _Files: `docs/features/tool_calling.md`, `requirements/common.txt`, `requirements/test/rocm.txt`, `tests/entrypoints/openai/chat_completion/test_completion_with_function_calling.py` _+25 more__
- **2026-06-12** [`fe04238292`](https://github.com/vllm-project/vllm/commit/fe04238292) [#44893](https://github.com/vllm-project/vllm/pull/44893)
  [ROCm][gpt-oss] Pass GateMode.INTERLEAVE for MXFP4 W4A16 fused MoE (#44893)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-06-12** [`1ce3cdc5c1`](https://github.com/vllm-project/vllm/commit/1ce3cdc5c1) [#45302](https://github.com/vllm-project/vllm/pull/45302)
  [ROCm][CI] fix fp8 support for test_deepep_moe (#45302)
  _Files: `tests/kernels/moe/test_deepep_moe.py`_
- **2026-06-12** [`fcf5115c45`](https://github.com/vllm-project/vllm/commit/fcf5115c45) [#44899](https://github.com/vllm-project/vllm/pull/44899)
  [ROCm][DSv4][Perf] Flash-decode split-K decode attention kernel (#44899)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-06-11** [`2ec6594db9`](https://github.com/vllm-project/vllm/commit/2ec6594db9) [#36902](https://github.com/vllm-project/vllm/pull/36902)
  [Kernel][Helion][1/N] Add Helion kernel for per_token_group_fp8_quant (#36902)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `setup.py`, `tests/kernels/helion/test_per_token_group_fp8_quant.py` _+6 more__
- **2026-06-11** [`43914dd743`](https://github.com/vllm-project/vllm/commit/43914dd743) [#44624](https://github.com/vllm-project/vllm/pull/44624)
  [Rust Frontend] Add Python bridge for Rust tool parsers (#44624)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`, `.buildkite/test_areas/misc.yaml`, `build_rust.sh`, `docker/Dockerfile` _+12 more__
- **2026-06-10** [`16282a9c4e`](https://github.com/vllm-project/vllm/commit/16282a9c4e) [#45170](https://github.com/vllm-project/vllm/pull/45170)
  [ROCm][CI] Moving MI300 tests to MI325 until cluster is stabilized (#45170)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml` _+3 more__
- **2026-06-10** [`5b6b536fdc`](https://github.com/vllm-project/vllm/commit/5b6b536fdc) [#44679](https://github.com/vllm-project/vllm/pull/44679)
  [ROCm][Bugfix] Make intermediate_pad TP-aware in rocm_aiter_fused_experts (#44679)
  _Files: `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-06-10** [`bfe1001ab6`](https://github.com/vllm-project/vllm/commit/bfe1001ab6) [#45169](https://github.com/vllm-project/vllm/pull/45169)
  [Bugfix] [DSV4] [ROCm] Pin apache-tvm-ffi version to `0.1.10` (#45169)
  _Files: `requirements/rocm.txt`, `requirements/test/rocm.txt`_
- **2026-06-10** [`4673ca1d78`](https://github.com/vllm-project/vllm/commit/4673ca1d78) [#44821](https://github.com/vllm-project/vllm/pull/44821)
  fix: prefix DeepSeek V4 MTP projections (#44821)
  _Files: `vllm/models/deepseek_v4/amd/mtp.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`_
- **2026-06-10** [`3cc9fecd58`](https://github.com/vllm-project/vllm/commit/3cc9fecd58) [#45131](https://github.com/vllm-project/vllm/pull/45131)
  Deprecated 1st generation Qwen and QwenVL models (#45131)
  _Files: `.buildkite/test-amd.yaml`, `docs/configuration/optimization.md`, `docs/contributing/model/multimodal.md`, `docs/models/supported_models.md` _+23 more__
- **2026-06-10** [`fdfb2566c0`](https://github.com/vllm-project/vllm/commit/fdfb2566c0) [#44981](https://github.com/vllm-project/vllm/pull/44981)
  [Rust Frontend] [CI] Unify Rust artifact builds with setuptools-rust (#44981)
  _Files: `MANIFEST.in`, `build_rust.sh`, `docker/Dockerfile`, `docker/Dockerfile.cpu` _+7 more__
- **2026-06-10** [`32daf56b42`](https://github.com/vllm-project/vllm/commit/32daf56b42) [#45011](https://github.com/vllm-project/vllm/pull/45011)
  [Refactor] Rename rocm_moe.py to rocm_moe_rdna.py (#45011)
  _Files: `tests/kernels/quantization/test_rdna3_compile_guards.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/rocm_moe_rdna.py`_
- **2026-06-10** [`82a42234be`](https://github.com/vllm-project/vllm/commit/82a42234be) [#44823](https://github.com/vllm-project/vllm/pull/44823)
  [ROCm][CI] Defer AITER sampler import and isolate server test PYTHONPATH (#44823)
  _Files: `tests/utils.py`, `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-06-10** [`bb78168b21`](https://github.com/vllm-project/vllm/commit/bb78168b21) [#44804](https://github.com/vllm-project/vllm/pull/44804)
  [ROCm][gpt-oss] Hybrid CDNA4 swizzle gate for A8W4 MoE (#44804)
  _Files: `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe.py`, `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`_
- **2026-06-09** [`d955745d58`](https://github.com/vllm-project/vllm/commit/d955745d58) [#44678](https://github.com/vllm-project/vllm/pull/44678)
  [ROCm][CI] fix test_rope_kvcache_fusion.py (#44678)
  _Files: `tests/compile/passes/test_rope_kvcache_fusion.py`_
- **2026-06-09** [`c9c1540e61`](https://github.com/vllm-project/vllm/commit/c9c1540e61) [#44936](https://github.com/vllm-project/vllm/pull/44936)
  [ROCm][V2] Fix failed assertion in Llama models when using EAGLE with `ROCM_AITER_FA` (#44936)
  _Files: `vllm/v1/attention/backends/utils.py`_
- **2026-06-09** [`01d8cd92dd`](https://github.com/vllm-project/vllm/commit/01d8cd92dd) [#44945](https://github.com/vllm-project/vllm/pull/44945)
  [ROCm][Perf] Use fused softplus-sqrt-topk router under AITER fused-MoE (#44945)
  _Files: `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-06-09** [`b697119800`](https://github.com/vllm-project/vllm/commit/b697119800) [#44040](https://github.com/vllm-project/vllm/pull/44040)
  [ROCm][CI] Stabilize ModernBERT token-classification parity against Hugging Face (#44040)
  _Files: `vllm/model_executor/models/modernbert.py`_
- **2026-06-09** [`80e2c4462d`](https://github.com/vllm-project/vllm/commit/80e2c4462d) [#42864](https://github.com/vllm-project/vllm/pull/42864)
  [ROCm][Compile] Fuse AR + RMSNorm + per-group FP8 quant (+ DSv3.2 indexer fan-out) (#42864)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-06-09** [`2385e140d6`](https://github.com/vllm-project/vllm/commit/2385e140d6) [#43022](https://github.com/vllm-project/vllm/pull/43022)
  [ROCm][CI] Stabilize sleep-mode memory release (#43022)
  _Files: `csrc/cumem_allocator.cpp`_
- **2026-06-09** [`996222f4bf`](https://github.com/vllm-project/vllm/commit/996222f4bf) [#44947](https://github.com/vllm-project/vllm/pull/44947)
  [CI] Reorganize entrypoints CI (#44947)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/plugins.yaml`, `tests/distributed/test_distributed_oot.py` _+16 more__
- **2026-06-09** [`baacbfcebf`](https://github.com/vllm-project/vllm/commit/baacbfcebf) [#42978](https://github.com/vllm-project/vllm/pull/42978)
  [ROCm][MLA][Bugfix] Reserve FP8 prefill workspace before lock for Kimi-K2.5 (#42978)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-06-08** [`05cb606cad`](https://github.com/vllm-project/vllm/commit/05cb606cad) [#44809](https://github.com/vllm-project/vllm/pull/44809)
  [ROCm][CI] Re-route NixlConnector jobs (#44809)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`_
- **2026-06-08** [`dc68bd8c41`](https://github.com/vllm-project/vllm/commit/dc68bd8c41) [#41184](https://github.com/vllm-project/vllm/pull/41184)
  [MoE Refactor] FusedMoE/MoERunner inversion refactor (#41184)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `docs/design/moe_kernel_features.md`, `tests/distributed/test_eplb_fused_moe_layer.py`, `tests/distributed/test_eplb_fused_moe_layer_dep_nvfp4.py` _+86 more__
- **2026-06-08** [`93ee4cd47f`](https://github.com/vllm-project/vllm/commit/93ee4cd47f) [#44819](https://github.com/vllm-project/vllm/pull/44819)
  [CI] Consolidate multimodal entrypoint tests. (#44819)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/llm/test_chat.py`, `tests/entrypoints/multimodal/__init__.py` _+20 more__
- **2026-06-08** [`d9ff7e4e9a`](https://github.com/vllm-project/vllm/commit/d9ff7e4e9a) [#44761](https://github.com/vllm-project/vllm/pull/44761)
  [ROCm][CI] Stabilizing teardown and timeout of flaky tests to prevent rare OOMs (#44761)
  _Files: `tests/conftest.py`, `tests/models/language/generation/test_hybrid.py`, `tests/models/language/pooling/test_colbert.py`, `tests/utils.py`_
- **2026-06-08** [`967c5c3bc3`](https://github.com/vllm-project/vllm/commit/967c5c3bc3) [#42793](https://github.com/vllm-project/vllm/pull/42793)
  [ROCm][CI] Stage C mirrors (#42793)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/engine.yaml` _+7 more__

## Other  (33 commits)

- **2026-06-15** [`c17e2f7c84`](https://github.com/vllm-project/vllm/commit/c17e2f7c84) [#45465](https://github.com/vllm-project/vllm/pull/45465)
  [Bugfix][Rust Frontend] Make metrics respect --served-model-name (#45465)
  _Files: `rust/src/server/src/lib.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-15** [`ebb0a71ad0`](https://github.com/vllm-project/vllm/commit/ebb0a71ad0) [#44965](https://github.com/vllm-project/vllm/pull/44965)
  [Bugfix] Reject out-of-range temperature values in SamplingParams (#44965)
  _Files: `vllm/sampling_params.py`_
- **2026-06-14** [`cf027b86af`](https://github.com/vllm-project/vllm/commit/cf027b86af) [#45442](https://github.com/vllm-project/vllm/pull/45442)
  [Core] Simplify MRV2 async output handling (#45442)
  _Files: `vllm/v1/executor/multiproc_executor.py`, `vllm/v1/executor/uniproc_executor.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-06-13** [`521b88c29e`](https://github.com/vllm-project/vllm/commit/521b88c29e) [#45468](https://github.com/vllm-project/vllm/pull/45468)
  [Bugfix] Reject structured outputs for diffusion decoders with a clear error (#45468)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/sampling_params.py`_
- **2026-06-13** [`470229c37e`](https://github.com/vllm-project/vllm/commit/470229c37e) [#45252](https://github.com/vllm-project/vllm/pull/45252)
  [Security] Fix DoS via prompt_embeds on M-RoPE models (#45252)
  _Files: `tests/v1/worker/test_mrope_prompt_embeds.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-13** [`2b3006076c`](https://github.com/vllm-project/vllm/commit/2b3006076c) [#45118](https://github.com/vllm-project/vllm/pull/45118)
  [Security] Add timeout guard for regex compilation in structured outp… (#45118)
  _Files: `tests/v1/structured_output/test_regex_compilation_timeout.py`, `vllm/envs.py`, `vllm/v1/structured_output/backend_outlines.py`, `vllm/v1/structured_output/backend_xgrammar.py` _+1 more__
- **2026-06-13** [`5b2943f5a6`](https://github.com/vllm-project/vllm/commit/5b2943f5a6) [#45460](https://github.com/vllm-project/vllm/pull/45460)
  [Bugfix] Return the tokenizer from maybe_make_thread_pool so it survives pickling (#45460)
  _Files: `tests/tokenizers_/test_hf.py`, `vllm/tokenizers/hf.py`_
- **2026-06-12** [`5af4aec141`](https://github.com/vllm-project/vllm/commit/5af4aec141) [#45216](https://github.com/vllm-project/vllm/pull/45216)
  [Rust Frontend] Add standalone `granite4` tool parser (#45216)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/tool-parser/src/json/granite4.rs` _+2 more__
- **2026-06-12** [`fbc3a1907a`](https://github.com/vllm-project/vllm/commit/fbc3a1907a) [#42759](https://github.com/vllm-project/vllm/pull/42759)
  [Bug] Migrate Reset cache for both v2 and v1 model runner (#42759)
  _Files: `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-12** [`8af550b399`](https://github.com/vllm-project/vllm/commit/8af550b399) [#45394](https://github.com/vllm-project/vllm/pull/45394)
  [BUGFIX][XPU] Update fa interface for compatibility (#45394)
  _Files: `vllm/_xpu_ops.py`_
- **2026-06-11** [`79f8c5bd8c`](https://github.com/vllm-project/vllm/commit/79f8c5bd8c) [#42331](https://github.com/vllm-project/vllm/pull/42331)
  [Metrics] Scope unregister_vllm_metrics() to strictly "vllm:" metrics (#42331)
  _Files: `vllm/v1/metrics/prometheus.py`_
- **2026-06-11** [`5edf7ff489`](https://github.com/vllm-project/vllm/commit/5edf7ff489) [#45179](https://github.com/vllm-project/vllm/pull/45179)
  [Core] Release cached device memory under pressure on UMA GPUs during weight loading (#45179)
  _Files: `vllm/model_executor/model_loader/utils.py`, `vllm/utils/mem_utils.py`_
- **2026-06-11** [`b78fc47f05`](https://github.com/vllm-project/vllm/commit/b78fc47f05) [#45218](https://github.com/vllm-project/vllm/pull/45218)
  [Docs] Add redirect for moved lmcache examples page (#45218)
  _Files: `mkdocs.yaml`_
- **2026-06-11** [`e62d00ab73`](https://github.com/vllm-project/vllm/commit/e62d00ab73) [#45253](https://github.com/vllm-project/vllm/pull/45253)
  docs: add fix disclosure policy to SECURITY.md (#45253)
  _Files: `SECURITY.md`_
- **2026-06-11** [`d598d23973`](https://github.com/vllm-project/vllm/commit/d598d23973) [#45116](https://github.com/vllm-project/vllm/pull/45116)
  [Security] Reject non-finite temperature and repetition_penalty values (#45116)
  _Files: `tests/samplers/test_non_finite_params.py`, `vllm/sampling_params.py`_
- **2026-06-11** [`0b995f8609`](https://github.com/vllm-project/vllm/commit/0b995f8609) [#45089](https://github.com/vllm-project/vllm/pull/45089)
  Use std::bit_cast for type punning in CPU kernels (#45089)
  _Files: `csrc/cpu/cpu_types_riscv_impl.hpp`, `csrc/cpu/cpu_types_vxe.hpp`, `csrc/cpu/float_convert.hpp`_
- **2026-06-11** [`86111c00c7`](https://github.com/vllm-project/vllm/commit/86111c00c7) [#45191](https://github.com/vllm-project/vllm/pull/45191)
  [Chore] Add Github notification for MRv2 for @yewentao256 (#45191)
  _Files: `.github/CODEOWNERS`_
- **2026-06-10** [`d1bcb4b44c`](https://github.com/vllm-project/vllm/commit/d1bcb4b44c) [#45147](https://github.com/vllm-project/vllm/pull/45147)
  [Bugfix] Fix tool parsing crash with non-function tool types (e.g. WebSearchTool) (#45147)
  _Files: `tests/tool_use/test_tool_choice_required.py`, `vllm/tool_parsers/utils.py`_
- **2026-06-10** [`2ba68d9bf7`](https://github.com/vllm-project/vllm/commit/2ba68d9bf7) [#44946](https://github.com/vllm-project/vllm/pull/44946)
  [Test] Fix one-sided MNNVL alltoall test workspace under-reservation (#44946)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`_
- **2026-06-10** [`de900fa7e5`](https://github.com/vllm-project/vllm/commit/de900fa7e5) [#45059](https://github.com/vllm-project/vllm/pull/45059)
  fix: AOT compile cache collision for dataclass-based HF configs (#45059)
  _Files: `vllm/config/utils.py`_
- **2026-06-10** [`166d14e9bf`](https://github.com/vllm-project/vllm/commit/166d14e9bf) [#45072](https://github.com/vllm-project/vllm/pull/45072)
  [bugfix] skip conch kernel for g_idx reordering (#45072)
  _Files: `vllm/model_executor/kernels/linear/mixed_precision/conch.py`_
- **2026-06-10** [`af65e08fc5`](https://github.com/vllm-project/vllm/commit/af65e08fc5) [#44193](https://github.com/vllm-project/vllm/pull/44193)
  KV-Cache multi-tier offloading async batched lookup (#44193)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/async_lookup.py` _+2 more__
- **2026-06-10** [`c9e5bf8135`](https://github.com/vllm-project/vllm/commit/c9e5bf8135) [#44814](https://github.com/vllm-project/vllm/pull/44814)
  [Bugfix] Fix layerwise reload dropping params after a composed weight loader (#44814)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/meta.py`_
- **2026-06-10** [`4882fd7632`](https://github.com/vllm-project/vllm/commit/4882fd7632) [#39091](https://github.com/vllm-project/vllm/pull/39091)
  [Bugfix][Reasoning] Nemotron V3: surface reasoning as content when thinking is unterminated (#39091)
  _Files: `tests/reasoning/test_nemotron_v3_reasoning_parser.py`, `vllm/parser/abstract_parser.py`, `vllm/reasoning/nemotron_v3_reasoning_parser.py`_
- **2026-06-10** [`8a5cf1ccd6`](https://github.com/vllm-project/vllm/commit/8a5cf1ccd6) [#44744](https://github.com/vllm-project/vllm/pull/44744)
  [Security] Fix remote DoS via invalid recovered token reinjection (#44744)
  _Files: `tests/v1/sample/test_rejection_sampler.py`, `vllm/v1/sample/rejection_sampler.py`_
- **2026-06-10** [`e9b728de8a`](https://github.com/vllm-project/vllm/commit/e9b728de8a) [#45058](https://github.com/vllm-project/vllm/pull/45058)
  Change from owning configs to owning config utils (#45058)
  _Files: `.github/CODEOWNERS`_
- **2026-06-10** [`7a74f31d2e`](https://github.com/vllm-project/vllm/commit/7a74f31d2e) [#44552](https://github.com/vllm-project/vllm/pull/44552)
  [Rust Frontend] Add seed_oss and step3p5 reasoning parsers (#44552)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/reasoning/tests.rs`, `rust/src/chat/tests/roundtrip.rs` _+5 more__
- **2026-06-09** [`dc10e467a9`](https://github.com/vllm-project/vllm/commit/dc10e467a9) [#44983](https://github.com/vllm-project/vllm/pull/44983)
  [Bugfix] Fix minimax_qk_norm_fusion (#44983)
  _Files: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`_
- **2026-06-09** [`1c23c42030`](https://github.com/vllm-project/vllm/commit/1c23c42030) [#44901](https://github.com/vllm-project/vllm/pull/44901)
  [Rust Frontend] Support Kimi K2 tool call IDs (#44901)
  _Files: `rust/src/chat/src/output/default/tool.rs`, `rust/src/chat/src/output/mod.rs`, `rust/src/chat/tests/roundtrip.rs`, `rust/src/tool-parser/src/kimi_k2.rs` _+1 more__
- **2026-06-09** [`7c2aa3108a`](https://github.com/vllm-project/vllm/commit/7c2aa3108a) [#43595](https://github.com/vllm-project/vllm/pull/43595)
  fix: prevent MM cache hang from stale LRU order keys (#43595)
  _Files: `vllm/utils/cache.py`_
- **2026-06-08** [`303916e93d`](https://github.com/vllm-project/vllm/commit/303916e93d) [#39562](https://github.com/vllm-project/vllm/pull/39562)
  [Bugfix]: Fix assertion in MambaManager.allocate_slots() (#39562)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-08** [`5633405964`](https://github.com/vllm-project/vllm/commit/5633405964) [#44805](https://github.com/vllm-project/vllm/pull/44805)
  Added extra_repr() to pooler classes to improve debuggability (#44805)
  _Files: `vllm/model_executor/layers/pooler/activations.py`, `vllm/model_executor/layers/pooler/seqwise/heads.py`, `vllm/model_executor/layers/pooler/seqwise/poolers.py`, `vllm/model_executor/layers/pooler/special.py` _+3 more__
- **2026-06-08** [`2ed0a9627b`](https://github.com/vllm-project/vllm/commit/2ed0a9627b) [#42736](https://github.com/vllm-project/vllm/pull/42736)
  [Kernel][Test] Make kernel tests for mamba dual-HW (CUDA + XPU) (#42736)
  _Files: `tests/kernels/mamba/test_causal_conv1d.py`, `tests/kernels/mamba/test_mamba_ssm.py`, `tests/kernels/mamba/test_mamba_ssm_ssd.py`_

## Multimodal  (29 commits)

- **2026-06-15** [`b997071ec4`](https://github.com/vllm-project/vllm/commit/b997071ec4) [#45510](https://github.com/vllm-project/vllm/pull/45510)
  (security) Enforce audio upload size limit before full file materialization (#45510)
  _Files: `tests/entrypoints/speech_to_text/test_upload_size_limit.py`, `vllm/entrypoints/speech_to_text/base/utils.py`, `vllm/entrypoints/speech_to_text/transcription/api_router.py`, `vllm/entrypoints/speech_to_text/translation/api_router.py`_
- **2026-06-15** [`48df95c43e`](https://github.com/vllm-project/vllm/commit/48df95c43e) [#45458](https://github.com/vllm-project/vllm/pull/45458)
  [Feature][Frontend] Report multimodal token counts in usage.prompt_tokens_details (#45458)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/engine/protocol.py`_
- **2026-06-14** [`c621af1690`](https://github.com/vllm-project/vllm/commit/c621af1690) [#45383](https://github.com/vllm-project/vllm/pull/45383)
  [BugFix] Fix prompt_embeds for multimodal models (#45383)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-14** [`54bbf51668`](https://github.com/vllm-project/vllm/commit/54bbf51668) [#44795](https://github.com/vllm-project/vllm/pull/44795)
  [Bugfix] nightly Docker images crash with ImportError: AnthropicOutputConfig since May 28 (#44795)
  _Files: `docker/Dockerfile`, `tests/entrypoints/anthropic/test_protocol_exports.py`_
- **2026-06-13** [`96fa5cdd9e`](https://github.com/vllm-project/vllm/commit/96fa5cdd9e) [#45478](https://github.com/vllm-project/vllm/pull/45478)
  [CI Bug] Fix `ValueError: There is no module or parameter named 'model.vision_tower.vision_model'` (#45478)
  _Files: `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/utils.py`_
- **2026-06-13** [`ff5a30cfac`](https://github.com/vllm-project/vllm/commit/ff5a30cfac) [#42700](https://github.com/vllm-project/vllm/pull/42700)
  [Bugfix] Replace deprecated Qwen2VLImageProcessorFast with Qwen2VLImageProcessor (#42700)
  _Files: `vllm/model_executor/models/qwen3_vl.py`_
- **2026-06-12** [`e3e31e54b0`](https://github.com/vllm-project/vllm/commit/e3e31e54b0) [#45401](https://github.com/vllm-project/vllm/pull/45401)
  [Bugfix][CPU] Don't build triton-cpu on arm64 release image (#45401)
  _Files: `docker/Dockerfile.cpu`_
- **2026-06-12** [`f1e13f7df9`](https://github.com/vllm-project/vllm/commit/f1e13f7df9) [#45129](https://github.com/vllm-project/vllm/pull/45129)
  [Model] Remove Mono-InternVL (InternLM2VEForCausalLM) (#45129)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_common.py`, `tests/models/registry.py`, `vllm/model_executor/models/h2ovl.py` _+5 more__
- **2026-06-12** [`f715f25f29`](https://github.com/vllm-project/vllm/commit/f715f25f29) [#45113](https://github.com/vllm-project/vllm/pull/45113)
  Fix misleading error for audio duration limit rejection (#45113)
  _Files: `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/multimodal/media/audio.py`_
- **2026-06-12** [`39dee1114a`](https://github.com/vllm-project/vllm/commit/39dee1114a) [#40660](https://github.com/vllm-project/vllm/pull/40660)
  [MM][Perf][CG] Support ViT full cudagraphs for mllama4 (#40660)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/models/utils.py` _+1 more__
- **2026-06-12** [`226ba9fc9e`](https://github.com/vllm-project/vllm/commit/226ba9fc9e) [#44587](https://github.com/vllm-project/vllm/pull/44587)
  [ASR] Add Long Audio benchmark and correctness test (#44587)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_audio_dataset.py`, `tests/entrypoints/speech_to_text/correctness/test_transcription_api_correctness.py`, `vllm/benchmarks/datasets/datasets.py` _+1 more__
- **2026-06-11** [`ab3a1fd2e6`](https://github.com/vllm-project/vllm/commit/ab3a1fd2e6) [#45244](https://github.com/vllm-project/vllm/pull/45244)
  minicpmv4_6: fix ImageSize (W,H) order for placeholder token calculation (#45244)
  _Files: `vllm/model_executor/models/minicpmv.py`, `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-06-11** [`1c3a72b8b2`](https://github.com/vllm-project/vllm/commit/1c3a72b8b2) [#45180](https://github.com/vllm-project/vllm/pull/45180)
  [Bugfix] Add fetch_images to MistralCommonImageProcessor (#45180)
  _Files: `tests/transformers_utils/processors/test_pixtral.py`, `vllm/transformers_utils/processors/pixtral.py`_
- **2026-06-11** [`2f2c5cf4f1`](https://github.com/vllm-project/vllm/commit/2f2c5cf4f1) [#45236](https://github.com/vllm-project/vllm/pull/45236)
  [release] Always block release images to dockerhub (#45236)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-06-10** [`12f3f19c19`](https://github.com/vllm-project/vllm/commit/12f3f19c19) [#35415](https://github.com/vllm-project/vllm/pull/35415)
  feat(qwen3-asr): support prompt parameter in v1/audio/transcriptions (#35415)
  _Files: `examples/speech_to_text/openai/openai_transcription_client.py`, `tests/entrypoints/speech_to_text/transcription/test_qwen3_asr_sanitize_prompt.py`, `vllm/model_executor/models/qwen3_asr.py`_
- **2026-06-10** [`ccc05de038`](https://github.com/vllm-project/vllm/commit/ccc05de038) [#45073](https://github.com/vllm-project/vllm/pull/45073)
  [Bugfix] Fix missing sequence_lengths in EXAONE-4.5 vision encoder (#45073)
  _Files: `vllm/model_executor/models/exaone4_5.py`_
- **2026-06-10** [`9ad08c4d15`](https://github.com/vllm-project/vllm/commit/9ad08c4d15) [#44683](https://github.com/vllm-project/vllm/pull/44683)
  [Bugfix][Rust Frontend] Fix missing added tokens in hf/fastokens tokenizer (#44683)
  _Files: `rust/src/chat/src/multimodal.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/tokenizer/src/hf.rs`, `rust/src/tokenizer/src/hf/added_tokens.rs`_
- **2026-06-10** [`af9f583344`](https://github.com/vllm-project/vllm/commit/af9f583344) [#45029](https://github.com/vllm-project/vllm/pull/45029)
  Revert "[Bugfix][CI] Gemma3 Transformers multimodal encoder profiling and build prompt-embedding fixtures" (#45029)
  _Files: `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-06-10** [`47930b59ca`](https://github.com/vllm-project/vllm/commit/47930b59ca) [#45057](https://github.com/vllm-project/vllm/pull/45057)
  [Bugfix] Handle HWC images in ImageProcessorItems.get_image_size (#45057)
  _Files: `tests/multimodal/test_parse.py`, `vllm/multimodal/parse.py`_
- **2026-06-09** [`cf1c906724`](https://github.com/vllm-project/vllm/commit/cf1c906724) [#44974](https://github.com/vllm-project/vllm/pull/44974)
  [Security] Fix image EXIF orientation and tRNS transparency handling (#44974)
  _Files: `tests/multimodal/test_image.py`, `vllm/multimodal/image.py`, `vllm/multimodal/media/image.py`_
- **2026-06-09** [`1b1359c332`](https://github.com/vllm-project/vllm/commit/1b1359c332) [#44970](https://github.com/vllm-project/vllm/pull/44970)
  [Security] Fix DoS via audio decompression bomb in speech-to-text endpoint (#44970)
  _Files: `tests/multimodal/media/test_audio.py`, `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/envs.py`, `vllm/multimodal/media/audio.py`_
- **2026-06-09** [`2ee5106372`](https://github.com/vllm-project/vllm/commit/2ee5106372) [#39425](https://github.com/vllm-project/vllm/pull/39425)
  Remove `raw_inputs` from transformers backend (#39425)
  _Files: `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-06-09** [`b12e42d132`](https://github.com/vllm-project/vllm/commit/b12e42d132) [#44481](https://github.com/vllm-project/vllm/pull/44481)
  [XPU][CI] Refine docker image build and pull/create lock mechanism in Intel GPU CI (#44481)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-test.sh`, `docker/Dockerfile.xpu`_
- **2026-06-09** [`f843ac1a1c`](https://github.com/vllm-project/vllm/commit/f843ac1a1c) [#44952](https://github.com/vllm-project/vllm/pull/44952)
  [Bugfix][CI] Gemma3 Transformers multimodal encoder profiling and build prompt-embedding fixtures (#44952)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_completion_with_prompt_embeds.py`, `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-06-09** [`d8218b1ee7`](https://github.com/vllm-project/vllm/commit/d8218b1ee7) [#44750](https://github.com/vllm-project/vllm/pull/44750)
  [Bugfix] Propagate ImportError from load_audio_pyav when vllm[audio] … (#44750)
  _Files: `vllm/multimodal/media/audio.py`_
- **2026-06-09** [`9f153aa781`](https://github.com/vllm-project/vllm/commit/9f153aa781) [#40576](https://github.com/vllm-project/vllm/pull/40576)
  [MM][Perf][CG] Support ViT full CUDA graph for glm4_1v image and video inference  (#40576)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/glm4_1v.py`_
- **2026-06-08** [`980796cd07`](https://github.com/vllm-project/vllm/commit/980796cd07) [#44852](https://github.com/vllm-project/vllm/pull/44852)
  [CI/Build][CPU] Fix flaky CI image build failure and unexpected warnings (#44852)
  _Files: `docker/Dockerfile.cpu`, `vllm/_custom_ops.py`_
- **2026-06-08** [`469f3dcf1d`](https://github.com/vllm-project/vllm/commit/469f3dcf1d) [#44828](https://github.com/vllm-project/vllm/pull/44828)
  [BugFix] Use served model name in gemma4 audio-tower error message (#44828)
  _Files: `vllm/model_executor/models/gemma4_mm.py`_
- **2026-06-08** [`94fcdd007f`](https://github.com/vllm-project/vllm/commit/94fcdd007f) [#43663](https://github.com/vllm-project/vllm/pull/43663)
  [XPU][CI] Add more test cases in Intel GPU CI (#43663)
  _Files: `.buildkite/intel_jobs/expert_parallelism_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-test.sh`_

## MoE / Expert Parallel  (28 commits)

- **2026-06-15** [`5ed15f42b9`](https://github.com/vllm-project/vllm/commit/5ed15f42b9) [#43557](https://github.com/vllm-project/vllm/pull/43557)
  Fix the E8M0 scale computation in the MXFP4 (W4A4) MOE CUTLASS kernel (#43557)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_utils.cuh`, `tests/kernels/moe/test_mxfp4_moe.py`, `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`_
- **2026-06-14** [`9548a1887f`](https://github.com/vllm-project/vllm/commit/9548a1887f) [#45136](https://github.com/vllm-project/vllm/pull/45136)
  [XPU] Support int4 group_size=32 W4A16 MoE (#45136)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-06-14** [`78e7293bb1`](https://github.com/vllm-project/vllm/commit/78e7293bb1) [#45277](https://github.com/vllm-project/vllm/pull/45277)
  [Build] Fix CUDA arch build coverage gaps (#45277)
  _Files: `.buildkite/release-pipeline.yaml`, `.github/workflows/scripts/build.sh`, `CMakeLists.txt`, `cmake/external_projects/qutlass.cmake` _+10 more__
- **2026-06-13** [`b3f0a0a0df`](https://github.com/vllm-project/vllm/commit/b3f0a0a0df) [#45536](https://github.com/vllm-project/vllm/pull/45536)
  Fix docs build on `main` (#45536)
  _Files: `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`, `vllm/model_executor/layers/fusion/__init__.py`_
- **2026-06-12** [`78739c1946`](https://github.com/vllm-project/vllm/commit/78739c1946) [#42667](https://github.com/vllm-project/vllm/pull/42667)
  [Model Runner v2] Migration from v1 to v2, with Qwen and DSv2 MOE models [3/N] (#42667)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-06-12** [`0cd9b7af25`](https://github.com/vllm-project/vllm/commit/0cd9b7af25) [#43409](https://github.com/vllm-project/vllm/pull/43409)
  [CPU] Support CPU W4A16 INT4 MoE (#43409)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`, `tests/quantization/test_cpu_wna16.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py` _+4 more__
- **2026-06-12** [`eb28452b10`](https://github.com/vllm-project/vllm/commit/eb28452b10) [#45163](https://github.com/vllm-project/vllm/pull/45163)
  [Model] Add DiffusionGemma Support (#45163)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `cmake/external_projects/vllm_flash_attn.cmake`, `docs/design/attention_backends.md`, `tests/kernels/attention/test_mixed_causal_attn.py` _+48 more__
- **2026-06-12** [`7021be66e8`](https://github.com/vllm-project/vllm/commit/7021be66e8) [#45176](https://github.com/vllm-project/vllm/pull/45176)
  [11a/n]  Migrate Marlin kernels to torch stable ABI (#45176)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/moe/marlin_moe_wna16/kernel.h`, `csrc/libtorch_stable/moe/marlin_moe_wna16/marlin_template.h`, `csrc/libtorch_stable/quantization/gptq_allspark/allspark_utils.cuh` _+15 more__
- **2026-06-11** [`c9340e6f35`](https://github.com/vllm-project/vllm/commit/c9340e6f35) [#45128](https://github.com/vllm-project/vllm/pull/45128)
  [Model] Remove InternLMForCausalLM registry alias (#45128)
  _Files: `docs/models/supported_models.md`, `tests/distributed/test_pipeline_parallel.py`, `tests/models/registry.py`, `vllm/model_executor/models/apertus.py` _+10 more__
- **2026-06-11** [`03878d1c22`](https://github.com/vllm-project/vllm/commit/03878d1c22) [#44992](https://github.com/vllm-project/vllm/pull/44992)
  Deprecations for v0.23 and v0.24 (#44992)
  _Files: `.buildkite/lm-eval-harness/configs/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8.yaml`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `docs/design/moe_kernel_features.md`, `docs/models/pooling_models/reward.md` _+31 more__
- **2026-06-11** [`3508cb78d4`](https://github.com/vllm-project/vllm/commit/3508cb78d4) [#43300](https://github.com/vllm-project/vllm/pull/43300)
  [Bugfix] Fix broken profile_modular_kernel.py (#43300)
  _Files: `tests/kernels/moe/modular_kernel_tools/profile_modular_kernel.py`, `tests/kernels/moe/test_profile_modular_kernel.py`_
- **2026-06-11** [`6e64c1bab1`](https://github.com/vllm-project/vllm/commit/6e64c1bab1) [#44565](https://github.com/vllm-project/vllm/pull/44565)
  [10c/n] Migrate MoE kernels to torch stable ABI  (#44565)
  _Files: `.gitignore`, `.pre-commit-config.yaml`, `CMakeLists.txt`, `csrc/libtorch_stable/dispatch_utils.h` _+30 more__
- **2026-06-11** [`18d87a87dc`](https://github.com/vllm-project/vllm/commit/18d87a87dc) [#45161](https://github.com/vllm-project/vllm/pull/45161)
  Deprecate Transformers v4 support (#45161)
  _Files: `requirements/common.txt`, `vllm/config/vllm.py`, `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/gemma3n_mm.py` _+15 more__
- **2026-06-11** [`7920ccb97c`](https://github.com/vllm-project/vllm/commit/7920ccb97c) [#45067](https://github.com/vllm-project/vllm/pull/45067)
  [Bugfix]: Fix Quark gpt-oss weight loading broken by FusedMoe refactor (#45067)
  _Files: `vllm/model_executor/models/gpt_oss.py`_
- **2026-06-10** [`6471ec75bd`](https://github.com/vllm-project/vllm/commit/6471ec75bd) [#44978](https://github.com/vllm-project/vllm/pull/44978)
  [EPLB] Reject NCCL-based EPLB communicators with async EPLB (#44978)
  _Files: `tests/distributed/test_elastic_ep.py`, `tests/distributed/test_eplb_execute.py`, `tests/kernels/moe/test_moe_layer.py`, `vllm/config/parallel.py` _+4 more__
- **2026-06-10** [`fa8c868a3c`](https://github.com/vllm-project/vllm/commit/fa8c868a3c) [#45047](https://github.com/vllm-project/vllm/pull/45047)
  [Bugfix] Fix Llama4 weight loading (#45047)
  _Files: `vllm/model_executor/model_loader/weight_utils.py`, `vllm/model_executor/models/lfm2_moe.py`, `vllm/model_executor/models/llama4.py`, `vllm/model_executor/models/mllama4.py`_
- **2026-06-10** [`29026682cb`](https://github.com/vllm-project/vllm/commit/29026682cb) [#45037](https://github.com/vllm-project/vllm/pull/45037)
  [Bugfix] Fix nemotron accuracy drop introduced by #41184 (#45037)
  _Files: `vllm/model_executor/layers/fused_moe/layer.py`_
- **2026-06-10** [`6850839c6f`](https://github.com/vllm-project/vllm/commit/6850839c6f) [#44217](https://github.com/vllm-project/vllm/pull/44217)
  [Perf] Fix dsv3_router_gemm heuristic (#44217)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-06-10** [`87c15d46e3`](https://github.com/vllm-project/vllm/commit/87c15d46e3) [#44921](https://github.com/vllm-project/vllm/pull/44921)
  [Bugfix] Lazily import the humming quantization backend (#44921)
  _Files: `vllm/model_executor/kernels/linear/mixed_precision/humming.py`, `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/quantization/humming.py`, `vllm/model_executor/layers/quantization/utils/humming_utils.py` _+1 more__
- **2026-06-10** [`f4966f8b3d`](https://github.com/vllm-project/vllm/commit/f4966f8b3d) [#45054](https://github.com/vllm-project/vllm/pull/45054)
  [Bugfix] Fix weight loading issues caused by #41184 (#45054)
  _Files: `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/qwen3_vl_moe.py`, `vllm/model_executor/models/step3_text.py`, `vllm/model_executor/models/step3p5.py` _+1 more__
- **2026-06-09** [`ee4d7df2b5`](https://github.com/vllm-project/vllm/commit/ee4d7df2b5) [#44907](https://github.com/vllm-project/vllm/pull/44907)
  [Cohere] Cohere2 moe parser fix (#44907)
  _Files: `vllm/tool_parsers/cohere_command_tool_parser.py`_
- **2026-06-09** [`3e8afdf785`](https://github.com/vllm-project/vllm/commit/3e8afdf785) [#44747](https://github.com/vllm-project/vllm/pull/44747)
  [Cohere] Fix Cohere2MoE weight loading when using Transformers ≥5.10 (#44747)
  _Files: `vllm/model_executor/models/cohere2_moe.py`_
- **2026-06-09** [`59401ac9f1`](https://github.com/vllm-project/vllm/commit/59401ac9f1) [#44830](https://github.com/vllm-project/vllm/pull/44830)
  [Kernel][Perf] Tune fused_moe FP8 config for Qwen3-Next-80B tp=4 on H100 (+25% at batch 96-512) (#44830)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=512,N=128,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json`_
- **2026-06-09** [`540aaf2140`](https://github.com/vllm-project/vllm/commit/540aaf2140) [#44264](https://github.com/vllm-project/vllm/pull/44264)
  [Bugfix][Model] Qwen3-Omni: move cu_seqlens to GPU before VIT attention (#44264)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-06-09** [`e2f993dc41`](https://github.com/vllm-project/vllm/commit/e2f993dc41) [#41183](https://github.com/vllm-project/vllm/pull/41183)
  [WideEP] Integrate DeepEP v2 (#41183)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/distributed/test_mnnvl_alltoall.py`, `tests/kernels/moe/modular_kernel_tools/common.py`, `tests/kernels/moe/modular_kernel_tools/mk_objects.py` _+18 more__
- **2026-06-08** [`823a0ab754`](https://github.com/vllm-project/vllm/commit/823a0ab754) [#44897](https://github.com/vllm-project/vllm/pull/44897)
  [Bugfix][MoE] Fix fused MoE expert mapping helper call sites (#44897)
  _Files: `vllm/lora/model_manager.py`, `vllm/model_executor/models/cohere2_moe.py`, `vllm/model_executor/models/hy_v3.py`, `vllm/model_executor/models/hy_v3_mtp.py` _+2 more__
- **2026-06-08** [`fa662b1a8b`](https://github.com/vllm-project/vllm/commit/fa662b1a8b) [#44470](https://github.com/vllm-project/vllm/pull/44470)
  [XPU] Cap topk/topp Triton BLOCK_SIZE to 4096 to fix Top-p mask difference failures (#44470)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-06-08** [`54c660c3a6`](https://github.com/vllm-project/vllm/commit/54c660c3a6) [#44771](https://github.com/vllm-project/vllm/pull/44771)
  [XPU][Minor] format moe kernel name and add in kernel list (#44771)
  _Files: `vllm/model_executor/layers/fused_moe/__init__.py`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+1 more__

## Serving / API  (26 commits)

- **2026-06-15** [`1d88c4dadd`](https://github.com/vllm-project/vllm/commit/1d88c4dadd) [#45676](https://github.com/vllm-project/vllm/pull/45676)
  [Docs] Update the online serving docs. (#45676)
  _Files: `docs/models/pooling_models/README.md`, `docs/models/pooling_models/scoring.md`, `docs/serving/online_serving/README.md`, `docs/serving/online_serving/openai_compatible_server.md`_
- **2026-06-15** [`40eac9a9d9`](https://github.com/vllm-project/vllm/commit/40eac9a9d9) [#44760](https://github.com/vllm-project/vllm/pull/44760)
  [Rust Frontend] Support `parallel_tool_calls = false` (#44760)
  _Files: `rust/src/chat/src/output/default/mod.rs`, `rust/src/chat/src/output/default/tool.rs`, `rust/src/chat/src/output/harmony/mod.rs`, `rust/src/chat/src/output/structured.rs` _+4 more__
- **2026-06-15** [`e8d3e22c88`](https://github.com/vllm-project/vllm/commit/e8d3e22c88) [#45629](https://github.com/vllm-project/vllm/pull/45629)
  Fix included router missing path for `FastAPI >=0.137` (#45629)
  _Files: `vllm/entrypoints/serve/instrumentator/metrics.py`_
- **2026-06-15** [`2c764c089a`](https://github.com/vllm-project/vllm/commit/2c764c089a) [#45173](https://github.com/vllm-project/vllm/pull/45173)
  Added real  /v1/embeddings support for messages + chat_template_kw  (#45173)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/entrypoints/pooling/base/protocol.py`, `vllm/entrypoints/pooling/embed/io_processor.py`, `vllm/entrypoints/pooling/embed/protocol.py` _+1 more__
- **2026-06-13** [`9261dbbc55`](https://github.com/vllm-project/vllm/commit/9261dbbc55) [#45491](https://github.com/vllm-project/vllm/pull/45491)
  Treat null completion max_tokens like the default (#45491)
  _Files: `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-06-13** [`2ecf7d0eb4`](https://github.com/vllm-project/vllm/commit/2ecf7d0eb4) [#45467](https://github.com/vllm-project/vllm/pull/45467)
  [Model Runner V2] Fix `openai.InternalServerError: Error code: 500 - 'list index out of range'` (#45467)
  _Files: `vllm/v1/worker/gpu/sample/states.py`_
- **2026-06-13** [`17ee5b1ac5`](https://github.com/vllm-project/vllm/commit/17ee5b1ac5) [#45376](https://github.com/vllm-project/vllm/pull/45376)
  [Bugfix] Set type/role explicitly in streaming message_start event (#45376)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-12** [`6e4a547176`](https://github.com/vllm-project/vllm/commit/6e4a547176) [#45431](https://github.com/vllm-project/vllm/pull/45431)
  [Refactor] Deprecate ResponsesParser wrapper, inline parsing into ParsableContext (#45431)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context_unit.py`, `vllm/entrypoints/mcp/tool.py`, `vllm/entrypoints/openai/parser/responses_parser.py`, `vllm/entrypoints/openai/responses/context.py` _+1 more__
- **2026-06-12** [`3b8fc3fe6d`](https://github.com/vllm-project/vllm/commit/3b8fc3fe6d) [#45396](https://github.com/vllm-project/vllm/pull/45396)
  [Frontend] Support strict mode for tool calling with ResponsesAPI (#45396)
  _Files: `tests/entrypoints/openai/responses/conftest.py`, `vllm/parser/abstract_parser.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/tool_parsers/abstract_tool_parser.py` _+1 more__
- **2026-06-12** [`c7aa3d2630`](https://github.com/vllm-project/vllm/commit/c7aa3d2630) [#35022](https://github.com/vllm-project/vllm/pull/35022)
  [Core] Support structured outputs for beam search (#35022)
  _Files: `tests/samplers/test_beam_search.py`, `vllm/entrypoints/generate/beam_search/offline.py`, `vllm/sampling_params.py`_
- **2026-06-12** [`1ae1051b4b`](https://github.com/vllm-project/vllm/commit/1ae1051b4b) [#45286](https://github.com/vllm-project/vllm/pull/45286)
  [Bugfix][Rust Frontend] Return 400 for prompt-validation submit errors (#45286)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/completions.rs`_
- **2026-06-12** [`e0b9fb1290`](https://github.com/vllm-project/vllm/commit/e0b9fb1290) [#44612](https://github.com/vllm-project/vllm/pull/44612)
  [ASR] Optimize CPU preproc to get 2.5x RTFx via multi-threading (#44612)
  _Files: `vllm/entrypoints/serve/utils/server_utils.py`, `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/envs.py`, `vllm/utils/async_utils.py`_
- **2026-06-12** [`42ae5e7ac6`](https://github.com/vllm-project/vllm/commit/42ae5e7ac6) [#44383](https://github.com/vllm-project/vllm/pull/44383)
  [Bugfix] Fix --enable-prompt-tokens-details omitting zero cached tokens (#44383)
  _Files: `tests/entrypoints/openai/completion/test_completion.py`, `tests/entrypoints/serve/disagg/test_generate_stream.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/completion/serving.py` _+1 more__
- **2026-06-12** [`e0871ad225`](https://github.com/vllm-project/vllm/commit/e0871ad225) [#45104](https://github.com/vllm-project/vllm/pull/45104)
  [Refactor] Chat Completions Streaming Harmony Refactor and Bugfixes (#45104)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat_stream_harmony.py`, `tests/parser/test_harmony.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/chat_completion/stream_harmony.py` _+1 more__
- **2026-06-11** [`235b63c004`](https://github.com/vllm-project/vllm/commit/235b63c004) [#45287](https://github.com/vllm-project/vllm/pull/45287)
  [Bugfix] Fix Anthropic tool_use content handling dropping args (#45287)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-11** [`3b03a2cf47`](https://github.com/vllm-project/vllm/commit/3b03a2cf47) [#43965](https://github.com/vllm-project/vllm/pull/43965)
  [Rust Frontend] Support continuous_usage_stats stream option (#43965)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions.rs` _+5 more__
- **2026-06-11** [`1f9dd7900d`](https://github.com/vllm-project/vllm/commit/1f9dd7900d) [#44680](https://github.com/vllm-project/vllm/pull/44680)
  [Bugfix][Rust Frontend] Validate out-of-vocab token ids in request params (#44680)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions.rs` _+12 more__
- **2026-06-11** [`9492362972`](https://github.com/vllm-project/vllm/commit/9492362972) [#45119](https://github.com/vllm-project/vllm/pull/45119)
  [Security] Apply sanitize_message to Anthropic and STT error paths (#45119)
  _Files: `tests/entrypoints/serve/utils/test_error_sanitization.py`, `vllm/entrypoints/anthropic/api_router.py`, `vllm/entrypoints/anthropic/serving.py`, `vllm/entrypoints/speech_to_text/realtime/connection.py`_
- **2026-06-11** [`3a04061701`](https://github.com/vllm-project/vllm/commit/3a04061701) [#45190](https://github.com/vllm-project/vllm/pull/45190)
  [Refactor][Parser] Unify Response API to use parser.parse() like Chat Completion API (#45190)
  _Files: `tests/entrypoints/openai/test_responses_parser_unified.py`, `tests/entrypoints/openai/test_tool_choice_content_none.py`, `vllm/entrypoints/openai/parser/responses_parser.py`, `vllm/entrypoints/openai/responses/serving.py` _+2 more__
- **2026-06-11** [`248e33c40d`](https://github.com/vllm-project/vllm/commit/248e33c40d) [#44608](https://github.com/vllm-project/vllm/pull/44608)
  [Bugfix][Responses API] Set id on function_call item in streaming done event (#44608)
  _Files: `vllm/entrypoints/openai/responses/streaming_events.py`_
- **2026-06-10** [`6ec7dcd641`](https://github.com/vllm-project/vllm/commit/6ec7dcd641) [#44448](https://github.com/vllm-project/vllm/pull/44448)
  [Frontend][Metrics] Add `vllm:tool_call_parser_invocations_total` Prometheus metric (#44448)
  _Files: `vllm/entrypoints/openai/api_server.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/metrics.py`_
- **2026-06-10** [`5828a205ef`](https://github.com/vllm-project/vllm/commit/5828a205ef) [#44686](https://github.com/vllm-project/vllm/pull/44686)
  Fix Harmony tool descriptions for optional fields (#44686)
  _Files: `tests/entrypoints/openai/parser/test_harmony_utils.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`_
- **2026-06-10** [`6aec99f030`](https://github.com/vllm-project/vllm/commit/6aec99f030) [#45081](https://github.com/vllm-project/vllm/pull/45081)
  [Refactor] Remove dead states from chat completion serving (#45081)
  _Files: `vllm/entrypoints/openai/chat_completion/serving.py`_
- **2026-06-10** [`2c9c07c85e`](https://github.com/vllm-project/vllm/commit/2c9c07c85e) [#45085](https://github.com/vllm-project/vllm/pull/45085)
  [Bugfix][CI/Build] Fix Rust frontend build after chat conversion refactor (#45085)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`_
- **2026-06-10** [`dac9e9a640`](https://github.com/vllm-project/vllm/commit/dac9e9a640) [#44884](https://github.com/vllm-project/vllm/pull/44884)
  [Rust Frontend] Extract shared options in route helper params (#44884)
  _Files: `rust/src/server/src/lib.rs`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/openai/chat_completions.rs` _+5 more__
- **2026-06-09** [`69fdaffbcd`](https://github.com/vllm-project/vllm/commit/69fdaffbcd) [#44222](https://github.com/vllm-project/vllm/pull/44222)
  [Rust Frontend] Add /tokenize and /detokenize endpoints (#44222)
  _Files: `rust/src/chat/src/error.rs`, `rust/src/chat/src/lib.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs` _+5 more__

## Attention  (25 commits)

- **2026-06-15** [`fa63bb9db6`](https://github.com/vllm-project/vllm/commit/fa63bb9db6) [#43914](https://github.com/vllm-project/vllm/pull/43914)
  Remove redundant Triton KV cache dtype asserts and enforce architectural support (fp8 >= sm89) (#43914)
  _Files: `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_reshape_and_cache_flash.py`_
- **2026-06-15** [`b8336c3c7c`](https://github.com/vllm-project/vllm/commit/b8336c3c7c) [#45564](https://github.com/vllm-project/vllm/pull/45564)
  [Bugfix][V1] Split V2 model-runner attention groups on num_heads_q (#45564)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-06-15** [`8760f972ca`](https://github.com/vllm-project/vllm/commit/8760f972ca) [#45391](https://github.com/vllm-project/vllm/pull/45391)
  [CPU] Refine CPU attention frontend (#45391)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `csrc/cpu/generate_cpu_attn_dispatch.py`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-06-14** [`9fd737badc`](https://github.com/vllm-project/vllm/commit/9fd737badc) [#45487](https://github.com/vllm-project/vllm/pull/45487)
  [Bugfix][DCP] Fix illegal memory access in DCP a2a decode under full CUDA graphs (#45487)
  _Files: `vllm/v1/attention/ops/dcp_alltoall.py`_
- **2026-06-12** [`c90650088d`](https://github.com/vllm-project/vllm/commit/c90650088d) [#44260](https://github.com/vllm-project/vllm/pull/44260)
  Add the QuantizedActivation linear-kernel contract (#44260)
  _Files: `.buildkite/test_areas/quantization.yaml`, `tests/fusion/__init__.py`, `tests/fusion/test_quant_activation_contract.py`, `vllm/model_executor/kernels/linear/base.py` _+9 more__
- **2026-06-12** [`cf567cbc71`](https://github.com/vllm-project/vllm/commit/cf567cbc71) [#39336](https://github.com/vllm-project/vllm/pull/39336)
  [Attention] Improve attention benchmarks: configs and profiling (#39336)
  _Files: `benchmarks/attention_benchmarks/README.md`, `benchmarks/attention_benchmarks/benchmark.py`, `benchmarks/attention_benchmarks/common.py`, `benchmarks/attention_benchmarks/configs/mla_decode.yaml` _+11 more__
- **2026-06-12** [`efe7adb5e1`](https://github.com/vllm-project/vllm/commit/efe7adb5e1) [#45322](https://github.com/vllm-project/vllm/pull/45322)
  [Perf] Use native DSA indexer decode path for next_n > 2 on SM100 (#45322)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-06-12** [`d6fd7ce8da`](https://github.com/vllm-project/vllm/commit/d6fd7ce8da) [#45319](https://github.com/vllm-project/vllm/pull/45319)
  [Model][Dflash] Enable Dflash support for Qwen3NextForCausalLM targets (#45319)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-06-12** [`4171ae406c`](https://github.com/vllm-project/vllm/commit/4171ae406c) [#39457](https://github.com/vllm-project/vllm/pull/39457)
  [V1][Metrics] Add MLA attention metrics for DeepSeek MFU estimation (#39457)
  _Files: `tests/v1/metrics/test_perf_metrics.py`, `vllm/v1/metrics/perf.py`_
- **2026-06-12** [`6fbfdd1831`](https://github.com/vllm-project/vllm/commit/6fbfdd1831) [#44583](https://github.com/vllm-project/vllm/pull/44583)
  [NIXL] Per-region KV transfer classification for mixed full-attn + MLA groups (#44583)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py`_
- **2026-06-11** [`5a6c7b7ab5`](https://github.com/vllm-project/vllm/commit/5a6c7b7ab5) [#45052](https://github.com/vllm-project/vllm/pull/45052)
  [Bug] Fix test flashmla for DSv4 (#45052)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`_
- **2026-06-11** [`b8142294b7`](https://github.com/vllm-project/vllm/commit/b8142294b7) [#45251](https://github.com/vllm-project/vllm/pull/45251)
  [Bugfix] Restrict FlashInfer cuDNN FP8 ViT attention gate to Blackwell (SM 100) (#45251)
  _Files: `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/utils/flashinfer.py`_
- **2026-06-11** [`f81daf8880`](https://github.com/vllm-project/vllm/commit/f81daf8880) [#41797](https://github.com/vllm-project/vllm/pull/41797)
  [Attention] add triton diff-kv backend for mimo (#41797)
  _Files: `.buildkite/test_areas/kernels.yaml`, `docs/design/attention_backends.md`, `tests/kernels/attention/test_triton_unified_attention_diffkv.py`, `vllm/model_executor/models/mimo_v2.py` _+4 more__
- **2026-06-11** [`c2b4cd39ac`](https://github.com/vllm-project/vllm/commit/c2b4cd39ac) [#37047](https://github.com/vllm-project/vllm/pull/37047)
  [Doc][Attention] Fix MLA top-of-file comments (#37047)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-06-11** [`c3662b36ea`](https://github.com/vllm-project/vllm/commit/c3662b36ea) [#44733](https://github.com/vllm-project/vllm/pull/44733)
  [KV offload] Parallel-agnostic fs-tier cache for single full-attention group (#44733)
  _Files: `tests/v1/kv_offload/test_file_mapper.py`, `vllm/v1/kv_offload/file_mapper.py`, `vllm/v1/kv_offload/tiering/fs/manager.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-06-11** [`1f60771c74`](https://github.com/vllm-project/vllm/commit/1f60771c74) [#42679](https://github.com/vllm-project/vllm/pull/42679)
  fix: guard flash-attn rotary import (#42679)
  _Files: `vllm/model_executor/layers/rotary_embedding/common.py`_
- **2026-06-11** [`f272dfdce1`](https://github.com/vllm-project/vllm/commit/f272dfdce1) [#44774](https://github.com/vllm-project/vllm/pull/44774)
  [KV Connector] Mooncake store: prefix-cache retention interval for sparse attention (#44774)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-10** [`e2db0222e9`](https://github.com/vllm-project/vllm/commit/e2db0222e9) [#45074](https://github.com/vllm-project/vllm/pull/45074)
  [Perf][Attention] Pin MLA chunked-context metadata tensors so H2D copies are truly non-blocking (#45074)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-06-10** [`82d6b59f04`](https://github.com/vllm-project/vllm/commit/82d6b59f04) [#44687](https://github.com/vllm-project/vllm/pull/44687)
  [CI/Build] Skip test_use_trtllm_attention on non-CUDA platforms (#44687)
  _Files: `tests/kernels/attention/test_use_trtllm_attention.py`_
- **2026-06-10** [`0bae1d3848`](https://github.com/vllm-project/vllm/commit/0bae1d3848) [#44586](https://github.com/vllm-project/vllm/pull/44586)
  [MRV2][Spec Decode] DFlash (#44586)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/model_runner.py` _+10 more__
- **2026-06-10** [`fe1d923afc`](https://github.com/vllm-project/vllm/commit/fe1d923afc) [#45110](https://github.com/vllm-project/vllm/pull/45110)
  [BUGFIX][XPU] fix xpu `flash_attn_varlen_func` interface (#45110)
  _Files: `vllm/_xpu_ops.py`_
- **2026-06-10** [`6deb05e0e4`](https://github.com/vllm-project/vllm/commit/6deb05e0e4) [#42175](https://github.com/vllm-project/vllm/pull/42175)
  [Core][Model] Gemma4: Unified FA4 for all layers + FlashAttention mm_prefix support (#42175)
  _Files: `vllm/model_executor/models/config.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/backends/flex_attention.py` _+10 more__
- **2026-06-09** [`766ce2bb6b`](https://github.com/vllm-project/vllm/commit/766ce2bb6b) [#44408](https://github.com/vllm-project/vllm/pull/44408)
  Fix MiDashengLM TP>1 crash in audio encoder attention (#44408)
  _Files: `vllm/model_executor/models/midashenglm.py`_
- **2026-06-08** [`ba94a3b998`](https://github.com/vllm-project/vllm/commit/ba94a3b998) [#40470](https://github.com/vllm-project/vllm/pull/40470)
  [Attention] Extract KV-cache update from CPU attention backend (#40470)
  _Files: `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-06-08** [`eebce65756`](https://github.com/vllm-project/vllm/commit/eebce65756) [#42953](https://github.com/vllm-project/vllm/pull/42953)
  [XPU]feat: add DeepSeek-V4 XPU attention decode path (#42953)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/compressor.py` _+7 more__

## Models  (21 commits)

- **2026-06-15** [`6c5872efc5`](https://github.com/vllm-project/vllm/commit/6c5872efc5) [#45417](https://github.com/vllm-project/vllm/pull/45417)
  [Bugfix] Unset HF's default max_new_tokens for DiffusionGemma (#45417)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-06-15** [`7df4fe1bd7`](https://github.com/vllm-project/vllm/commit/7df4fe1bd7) [#45638](https://github.com/vllm-project/vllm/pull/45638)
  [Model] Remove XverseForCausalLM (#45638)
  _Files: `docs/models/supported_models.md`, `tests/distributed/test_pipeline_parallel.py`, `tests/models/registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-06-15** [`1801fad0ba`](https://github.com/vllm-project/vllm/commit/1801fad0ba) [#44645](https://github.com/vllm-project/vllm/pull/44645)
  [Bugfix] Stream Llama4 weight loading to avoid host-OOM with copy-returning loaders (#44645)
  _Files: `vllm/model_executor/models/llama4.py`, `vllm/model_executor/models/mllama4.py`_
- **2026-06-15** [`3d6ce816f0`](https://github.com/vllm-project/vllm/commit/3d6ce816f0) [#45291](https://github.com/vllm-project/vllm/pull/45291)
  [Bugfix][Model] Validate runai_streamer model_loader_extra_config (#45291)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_loader.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py`_
- **2026-06-12** [`04cec9e4d8`](https://github.com/vllm-project/vllm/commit/04cec9e4d8) [#45240](https://github.com/vllm-project/vllm/pull/45240)
  [XPU][DeepSeek-V4] Fix MTP: sync with upstream fixes #44821 and #43746 (#45240)
  _Files: `vllm/models/deepseek_v4/xpu/mtp.py`_
- **2026-06-11** [`9bbf42be26`](https://github.com/vllm-project/vllm/commit/9bbf42be26) [#45305](https://github.com/vllm-project/vllm/pull/45305)
  Make mistral_common optional by deferring MistralToolCall import (#45305)
  _Files: `vllm/tool_parsers/streaming.py`_
- **2026-06-11** [`f712fd0d7d`](https://github.com/vllm-project/vllm/commit/f712fd0d7d) [#45171](https://github.com/vllm-project/vllm/pull/45171)
  [Refactor] Chat Completions Harmony Refactor, non-streaming path. (#45171)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/parser/test_harmony.py`, `tests/tool_parsers/test_openai_tool_parser.py` _+12 more__
- **2026-06-11** [`0d657e44dc`](https://github.com/vllm-project/vllm/commit/0d657e44dc) [#45155](https://github.com/vllm-project/vllm/pull/45155)
  [Rust Frontend] Fix DeepSeek V3.2 continue_final_message rendering (#45155)
  _Files: `rust/src/chat/src/renderer/deepseek_v32/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v32/tests.rs`_
- **2026-06-11** [`aa1df36c53`](https://github.com/vllm-project/vllm/commit/aa1df36c53) [#44980](https://github.com/vllm-project/vllm/pull/44980)
  Fix/minicpmv46 missing version (#44980)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`, `vllm/transformers_utils/processors/minicpmo.py`, `vllm/transformers_utils/processors/minicpmv.py`_
- **2026-06-11** [`85a0ffae42`](https://github.com/vllm-project/vllm/commit/85a0ffae42) [#45194](https://github.com/vllm-project/vllm/pull/45194)
  [CI Bug] Remove qwen test `ValueError: No example model defined for Qwen/Qwen-7B-Chat` (#45194)
  _Files: `tests/distributed/test_pipeline_parallel.py`, `tests/models/language/generation/test_common.py`_
- **2026-06-11** [`2d481f8a94`](https://github.com/vllm-project/vllm/commit/2d481f8a94) [#45025](https://github.com/vllm-project/vllm/pull/45025)
  [Bugfix][Rust Frontend] Stop unescaping XML-style tool-call parameter values (#45025)
  _Files: `rust/src/tool-parser/src/deepseek_dsml/deepseek_v32.rs`, `rust/src/tool-parser/src/deepseek_dsml/mod.rs`, `rust/src/tool-parser/src/glm_xml/mod.rs`, `rust/src/tool-parser/src/minimax_m2.rs` _+2 more__
- **2026-06-10** [`ffce72c041`](https://github.com/vllm-project/vllm/commit/ffce72c041) [#44568](https://github.com/vllm-project/vllm/pull/44568)
  [Model Runner V2] Fix v2 `AttributeError: 'CohereASRDecoder' object has no attribute 'embed_input_ids'` (#44568)
  _Files: `vllm/v1/worker/gpu/model_states/__init__.py`_
- **2026-06-10** [`2131b597b1`](https://github.com/vllm-project/vllm/commit/2131b597b1) [#45153](https://github.com/vllm-project/vllm/pull/45153)
  [CI] Ping Mistral team for ministral/voxtral/mixtral/pixtral changes (#45153)
  _Files: `.github/mergify.yml`_
- **2026-06-10** [`77f42d9725`](https://github.com/vllm-project/vllm/commit/77f42d9725) [#45127](https://github.com/vllm-project/vllm/pull/45127)
  [Model] Remove obsolete ERNIE models (#45127)
  _Files: `docs/models/pooling_models/classify.md`, `docs/models/pooling_models/embed.md`, `docs/models/pooling_models/token_classify.md`, `tests/models/language/pooling/test_classification.py` _+5 more__
- **2026-06-10** [`7fdfa6441d`](https://github.com/vllm-project/vllm/commit/7fdfa6441d) [#44999](https://github.com/vllm-project/vllm/pull/44999)
  Model/colbert autoweightsloader (#44999)
  _Files: `vllm/model_executor/models/colbert.py`_
- **2026-06-10** [`d82ac00923`](https://github.com/vllm-project/vllm/commit/d82ac00923) [#44596](https://github.com/vllm-project/vllm/pull/44596)
  [Refactor][Mistral] Extract parsing logic into MistralParser (#44596)
  _Files: `tests/tool_parsers/test_mistral_tool_parser.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/mistral.py` _+3 more__
- **2026-06-09** [`ca4cfd8731`](https://github.com/vllm-project/vllm/commit/ca4cfd8731) [#45002](https://github.com/vllm-project/vllm/pull/45002)
  [Bugfix] fix qwen3.5 ep weight loading (#45002)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_5_mtp.py`_
- **2026-06-09** [`7a89b72564`](https://github.com/vllm-project/vllm/commit/7a89b72564) [#44176](https://github.com/vllm-project/vllm/pull/44176)
  [Perf] fuse qk rmsnorm rope gate for qwen3.5 (#44176)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_fused_qk_norm_rope_gate.py`, `vllm/model_executor/layers/fused_qk_norm_rope.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-06-09** [`70db1488c5`](https://github.com/vllm-project/vllm/commit/70db1488c5) [#44144](https://github.com/vllm-project/vllm/pull/44144)
  [DSV4][XPU] Add MHC fused_post_pre support (#44144)
  _Files: `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/xpu/model.py`_
- **2026-06-09** [`e6fc848d4f`](https://github.com/vllm-project/vllm/commit/e6fc848d4f) [#43844](https://github.com/vllm-project/vllm/pull/43844)
  [Bugfix][MiniCPM-o] Fix cuda/cpu device mismatch in Resampler2_5 pos_embed (#43844)
  _Files: `vllm/model_executor/models/minicpmv.py`_
- **2026-06-08** [`6124a98a9b`](https://github.com/vllm-project/vllm/commit/6124a98a9b) [#44215](https://github.com/vllm-project/vllm/pull/44215)
  [Bugfix] Fix FunASR-Nano crash during initialization (#44215)
  _Files: `vllm/model_executor/models/funasr.py`_

## Quantization  (16 commits)

- **2026-06-15** [`b5adb027ad`](https://github.com/vllm-project/vllm/commit/b5adb027ad) [#45200](https://github.com/vllm-project/vllm/pull/45200)
  [Models] Fix MiMo v2.x QKV TP sharding + FP4 support (#45200)
  _Files: `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/models/mimo_v2.py`_
- **2026-06-13** [`71b961dd35`](https://github.com/vllm-project/vllm/commit/71b961dd35) [#44572](https://github.com/vllm-project/vllm/pull/44572)
  [Perf] SM90 cutlass fp8 mm supports odd M by swap_ab, 180~290% kernel performance improvement (#44572)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`, `tests/kernels/quantization/test_cutlass_scaled_mm.py`, `vllm/model_executor/kernels/linear/scaled_mm/cutlass.py`_
- **2026-06-12** [`9eaacb23ec`](https://github.com/vllm-project/vllm/commit/9eaacb23ec) [#45295](https://github.com/vllm-project/vllm/pull/45295)
  [Kernel] Consolidate Marlin thread-tile padding across all dense Marlin paths (#45295)
  _Files: `tests/kernels/quantization/test_marlin_tile_padding.py`, `vllm/model_executor/kernels/linear/mixed_precision/marlin.py`, `vllm/model_executor/layers/quantization/awq_marlin.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+3 more__
- **2026-06-12** [`272c16953e`](https://github.com/vllm-project/vllm/commit/272c16953e) [#33790](https://github.com/vllm-project/vllm/pull/33790)
  [Kernel][Helion][1/N] Add Helion kernel for dynamic_per_token_scaled_fp8_quant (#33790)
  _Files: `tests/kernels/helion/test_dynamic_per_token_scaled_fp8_quant.py`, `vllm/kernels/helion/configs/dynamic_per_token_scaled_fp8_quant/nvidia_b200.json`, `vllm/kernels/helion/configs/dynamic_per_token_scaled_fp8_quant/nvidia_h100.json`, `vllm/kernels/helion/ops/dynamic_per_token_scaled_fp8_quant.py`_
- **2026-06-12** [`a014dddbaa`](https://github.com/vllm-project/vllm/commit/a014dddbaa) [#45304](https://github.com/vllm-project/vllm/pull/45304)
  [11b/n] Migrate Machete kernels to torch stable ABI (#45304)
  _Files: `CMakeLists.txt`, `csrc/cutlass_extensions/vllm_cutlass_library_extension.py`, `csrc/libtorch_stable/quantization/machete/Readme.md`, `csrc/libtorch_stable/quantization/machete/generate.py` _+13 more__
- **2026-06-12** [`c1076839c9`](https://github.com/vllm-project/vllm/commit/c1076839c9) [#45308](https://github.com/vllm-project/vllm/pull/45308)
  [Bugfix][Model] Pass revision by name in Run:ai and bitsandbytes index downloads (#45308)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_loader.py`, `tests/models/quantization/test_bitsandbytes.py`, `vllm/model_executor/model_loader/bitsandbytes_loader.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py`_
- **2026-06-11** [`f1d8d99717`](https://github.com/vllm-project/vllm/commit/f1d8d99717) [#43495](https://github.com/vllm-project/vllm/pull/43495)
  [Bugfix] CohereModel.load_weights: skip modelopt _quantizer.* keys (#43495)
  _Files: `vllm/model_executor/models/commandr.py`_
- **2026-06-11** [`f06aefb4e3`](https://github.com/vllm-project/vllm/commit/f06aefb4e3) [#44523](https://github.com/vllm-project/vllm/pull/44523)
  [CPU] Add missing scalar fallback for CPU W4A8 INT4 GEMM (#44523)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/gemm_int4.cpp`, `csrc/cpu/sgl-kernels/vec.h`, `csrc/cpu/torch_bindings.cpp`_
- **2026-06-11** [`f219788f91`](https://github.com/vllm-project/vllm/commit/f219788f91) [#44971](https://github.com/vllm-project/vllm/pull/44971)
  [Security] Fix info disclosure via int32 truncation in GGUF dequantize kernels (#44971)
  _Files: `csrc/libtorch_stable/quantization/gguf/dequantize.cuh`, `csrc/libtorch_stable/quantization/gguf/ggml-common.h`, `csrc/libtorch_stable/quantization/gguf/gguf_kernel.cu`_
- **2026-06-11** [`f31bc2ea60`](https://github.com/vllm-project/vllm/commit/f31bc2ea60) [#44478](https://github.com/vllm-project/vllm/pull/44478)
  [CPU][RISC-V] Enable oneDNN W8A8 INT8 to run on RISC-V (#44478)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_defs.hpp`, `csrc/cpu/cpu_types_riscv_impl.hpp`, `csrc/cpu/torch_bindings.cpp`_
- **2026-06-10** [`a1ec011a83`](https://github.com/vllm-project/vllm/commit/a1ec011a83) [#39498](https://github.com/vllm-project/vllm/pull/39498)
  [Bugfix] Add deepseek_v32 to Quark dynamic MXFP4 model type check (#39498)
  _Files: `vllm/model_executor/layers/quantization/quark/quark.py`_
- **2026-06-09** [`d7607ad273`](https://github.com/vllm-project/vllm/commit/d7607ad273) [#44914](https://github.com/vllm-project/vllm/pull/44914)
  [Bug] Fix deepseek v4 OOM issue (#44914)
  _Files: `vllm/models/deepseek_v4/quant_config.py`_
- **2026-06-09** [`e1ed89dbee`](https://github.com/vllm-project/vllm/commit/e1ed89dbee) [#45066](https://github.com/vllm-project/vllm/pull/45066)
  Revert "[Kernel] Speed up silu_and_mul_per_block_quant with warp-shuf… (#45066)
  _Files: `csrc/libtorch_stable/quantization/fused_kernels/fused_silu_mul_block_quant.cu`_
- **2026-06-09** [`a4b14b98c6`](https://github.com/vllm-project/vllm/commit/a4b14b98c6) [#44173](https://github.com/vllm-project/vllm/pull/44173)
  [Kernel] Speed up silu_and_mul_per_block_quant with warp-shuffle reduction + vectorized I/O (#44173)
  _Files: `csrc/libtorch_stable/quantization/fused_kernels/fused_silu_mul_block_quant.cu`_
- **2026-06-08** [`6afa25000c`](https://github.com/vllm-project/vllm/commit/6afa25000c) [#44735](https://github.com/vllm-project/vllm/pull/44735)
  [Bugfix] Canonicalize FP8 weight layout to (K, N) at the source (#44735)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/marlin.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a16_fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`_
- **2026-06-08** [`753e9d55e6`](https://github.com/vllm-project/vllm/commit/753e9d55e6) [#44132](https://github.com/vllm-project/vllm/pull/44132)
  [Quantization] add online fp8 ptpc (#44132)
  _Files: `tests/models/quantization/test_fp8_per_channel.py`, `tests/quantization/test_fp8_per_channel.py`, `vllm/config/quantization.py`, `vllm/model_executor/layers/quantization/__init__.py` _+2 more__

## CI / Build  (14 commits)

- **2026-06-15** [`e3e3cd5458`](https://github.com/vllm-project/vllm/commit/e3e3cd5458) [#45602](https://github.com/vllm-project/vllm/pull/45602)
  [Bugfix][CI] Update Dockerfile dependency graph PNG (#45602)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`_
- **2026-06-13** [`1033ffac2e`](https://github.com/vllm-project/vllm/commit/1033ffac2e) [#45489](https://github.com/vllm-project/vllm/pull/45489)
  [CI] Wait for SSL cert refresher events in the test (#45489)
  _Files: `tests/entrypoints/serve/utils/test_ssl_cert_refresher.py`_
- **2026-06-12** [`462ef83d58`](https://github.com/vllm-project/vllm/commit/462ef83d58) [#45294](https://github.com/vllm-project/vllm/pull/45294)
  Update hidden states extraction integration test triggers (#45294)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-06-12** [`bd59c913bc`](https://github.com/vllm-project/vllm/commit/bd59c913bc) [#45274](https://github.com/vllm-project/vllm/pull/45274)
  [CI] ci-fetch-log.sh: fetch all failed jobs from a build URL or PR number (#45274)
  _Files: `.buildkite/scripts/ci-clean-log.sh`, `.buildkite/scripts/ci-fetch-log.sh`, `AGENTS.md`, `docs/contributing/ci/failures.md`_
- **2026-06-12** [`a2c72d4388`](https://github.com/vllm-project/vllm/commit/a2c72d4388) [#45374](https://github.com/vllm-project/vllm/pull/45374)
  [Bugfix] Fix Dockerfile dependency graph pre-commit error (#45374)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`_
- **2026-06-12** [`2263f8a3de`](https://github.com/vllm-project/vllm/commit/2263f8a3de) [#45345](https://github.com/vllm-project/vllm/pull/45345)
  [CI][BugFix] Fix broken `test_mamba_prefix_cache.py` due to stale mock (#45345)
  _Files: `tests/v1/e2e/general/test_mamba_prefix_cache.py`_
- **2026-06-11** [`05d9848267`](https://github.com/vllm-project/vllm/commit/05d9848267) [#44923](https://github.com/vllm-project/vllm/pull/44923)
  [Build] Upgrade CUDA Dockerfiles from GCC 10 to GCC 12 for C++20 compatibility (#44923)
  _Files: `CMakeLists.txt`, `docker/Dockerfile`, `docker/Dockerfile.nightly_torch`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-06-11** [`ef67071b21`](https://github.com/vllm-project/vllm/commit/ef67071b21) [#44783](https://github.com/vllm-project/vllm/pull/44783)
  [Build] Skip spinloop extension on Python < 3.11 (#44783)
  _Files: `CMakeLists.txt`, `setup.py`_
- **2026-06-11** [`40e065e86a`](https://github.com/vllm-project/vllm/commit/40e065e86a) [#45204](https://github.com/vllm-project/vllm/pull/45204)
  [Docker] Fix CUTLASS DSL cu13 install order in Dockerfile (#45204)
  _Files: `docker/Dockerfile`_
- **2026-06-11** [`3501324957`](https://github.com/vllm-project/vllm/commit/3501324957) [#44942](https://github.com/vllm-project/vllm/pull/44942)
  [Build] fix self-contradictory precompiled-flag orthogonality test (#44942)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/test_envs.py`_
- **2026-06-11** [`b038a2f73b`](https://github.com/vllm-project/vllm/commit/b038a2f73b) [#45209](https://github.com/vllm-project/vllm/pull/45209)
  [CI][Bugfix] Update Dockerfile dependency graph PNG (#45209)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`_
- **2026-06-09** [`b4c6dc6454`](https://github.com/vllm-project/vllm/commit/b4c6dc6454) [#42262](https://github.com/vllm-project/vllm/pull/42262)
  [WIP][XPU] upgrade torch-xpu to 2.12 (#42262)
  _Files: `docker/Dockerfile.xpu`, `docs/getting_started/installation/gpu.xpu.inc.md`, `requirements/test/xpu.in`, `requirements/test/xpu.txt` _+1 more__
- **2026-06-09** [`dab60fc658`](https://github.com/vllm-project/vllm/commit/dab60fc658) [#44903](https://github.com/vllm-project/vllm/pull/44903)
  [Bugfix][CI] Fix `test_offloading_connector.py::test_fs_tiering_offloading` (#44903)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`_
- **2026-06-09** [`d3de61502f`](https://github.com/vllm-project/vllm/commit/d3de61502f) [#44940](https://github.com/vllm-project/vllm/pull/44940)
  [XPU][CI] fix test case path (#44940)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_

## Disaggregation / PD  (14 commits)

- **2026-06-13** [`43f0e024bc`](https://github.com/vllm-project/vllm/commit/43f0e024bc) [#43606](https://github.com/vllm-project/vllm/pull/43606)
  [Render] Add `/derender` endpoints for disaggregated postprocessing (#43606)
  _Files: `tests/entrypoints/serve/render/test_derender.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/completion/serving.py`, `vllm/entrypoints/openai/engine/serving.py` _+3 more__
- **2026-06-12** [`88ed636218`](https://github.com/vllm-project/vllm/commit/88ed636218) [#35264](https://github.com/vllm-project/vllm/pull/35264)
  [KV Connector]: Support KV push from Prefill to Decode node using Nixl KV Connector (#35264)
  _Files: `docs/design/nixl_kv_push_connector.md`, `examples/disaggregated/disaggregated_serving/disagg_proxy_pushconnector_demo.py`, `tests/v1/kv_connector/unit/test_bidirectional_kv_transfer.py`, `tests/v1/kv_connector/unit/test_multi_connector.py` _+22 more__
- **2026-06-12** [`b927004c44`](https://github.com/vllm-project/vllm/commit/b927004c44) [#44599](https://github.com/vllm-project/vllm/pull/44599)
  [Bugfix] Mamba CPU Offloading (#44599)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-06-12** [`4bc83323f2`](https://github.com/vllm-project/vllm/commit/4bc83323f2) [#44592](https://github.com/vllm-project/vllm/pull/44592)
  [Bugfix] OffloadingConnector: respect skip_reading_prefix_cache flag (#44592)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-06-11** [`8a91228dbe`](https://github.com/vllm-project/vllm/commit/8a91228dbe) [#45206](https://github.com/vllm-project/vllm/pull/45206)
  [Bugfix][KVConnector][Mooncake] Close MooncakeDistributedStore on connector teardown (#45206)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-11** [`23eb7c8fbb`](https://github.com/vllm-project/vllm/commit/23eb7c8fbb) [#44422](https://github.com/vllm-project/vllm/pull/44422)
  [Bugfix] Fix NixlEPAll2AllManager's dependency on --enable-elastic-ep to function (#44422)
  _Files: `vllm/distributed/device_communicators/all2all.py`_
- **2026-06-11** [`750aab5b8e`](https://github.com/vllm-project/vllm/commit/750aab5b8e) [#44424](https://github.com/vllm-project/vllm/pull/44424)
  [Bugfix] Fix CPU memory leak related to not cleaning up old remotes data (#44424)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py`_
- **2026-06-11** [`55911db580`](https://github.com/vllm-project/vllm/commit/55911db580) [#44243](https://github.com/vllm-project/vllm/pull/44243)
  [PD][Core] Fix Mamba prefix cache hit rate in PD disaggregation (#44243)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/run_mamba_prefix_cache_test.sh`, `tests/v1/kv_connector/nixl_integration/test_mamba_prefix_cache.py`, `vllm/v1/core/kv_cache_coordinator.py` _+1 more__
- **2026-06-10** [`9dfc313bdc`](https://github.com/vllm-project/vllm/commit/9dfc313bdc) [#35669](https://github.com/vllm-project/vllm/pull/35669)
  Feature/offloading manager stats (#35669)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker_metadata.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/cpu/test_manager.py` _+10 more__
- **2026-06-10** [`320c52b134`](https://github.com/vllm-project/vllm/commit/320c52b134) [#43756](https://github.com/vllm-project/vllm/pull/43756)
  [Bench] benchmark_serving_multi_turn: make non-standard conversation_id payload opt-in (#43756)
  _Files: `benchmarks/multi_turn/benchmark_serving_multi_turn.py`, `docs/features/nixl_connector_usage.md`, `examples/disaggregated/disaggregated_serving/disagg_proxy_multiturn.py`_
- **2026-06-09** [`c1d754d681`](https://github.com/vllm-project/vllm/commit/c1d754d681) [#43799](https://github.com/vllm-project/vllm/pull/43799)
  [Mooncake] Use all HCAs on multi-NIC hosts instead of GPU-indexed RNIC selection (#43799)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/rdma_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-09** [`5b3807e862`](https://github.com/vllm-project/vllm/commit/5b3807e862) [#42892](https://github.com/vllm-project/vllm/pull/42892)
  [KV Events] Switch event structs from array to map encoding (#42892)
  _Files: `examples/features/kv_events/kv_events_subscriber.py`, `vllm/distributed/kv_events.py`_
- **2026-06-09** [`4128605ad4`](https://github.com/vllm-project/vllm/commit/4128605ad4) [#44929](https://github.com/vllm-project/vllm/pull/44929)
  [Docs] Remove broken link to deleted disaggregated_prefill.sh (#44929)
  _Files: `docs/features/disagg_prefill.md`_
- **2026-06-08** [`5add018beb`](https://github.com/vllm-project/vllm/commit/5add018beb) [#44854](https://github.com/vllm-project/vllm/pull/44854)
  [Connector] Remove `P2pNcclConnector` (#44854)
  _Files: `benchmarks/disagg_benchmarks/disagg_overhead_benchmark.sh`, `benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh`, `benchmarks/disagg_benchmarks/disagg_prefill_proxy_server.py`, `benchmarks/disagg_benchmarks/round_robin_proxy.py` _+14 more__

## Scheduler / Engine  (13 commits)

- **2026-06-15** [`64833f8158`](https://github.com/vllm-project/vllm/commit/64833f8158) [#45137](https://github.com/vllm-project/vllm/pull/45137)
  [Rust Frontend] Add external→internal request-id map for abort() (#45137)
  _Files: `rust/Cargo.lock`, `rust/src/chat/src/lib.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+9 more__
- **2026-06-15** [`ddad5dbda2`](https://github.com/vllm-project/vllm/commit/ddad5dbda2) [#45557](https://github.com/vllm-project/vllm/pull/45557)
  [Bugfix][Rust] Sync EngineCoreReadyResponse with the Python dataclass (#45557)
  _Files: `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`_
- **2026-06-12** [`1a369783e9`](https://github.com/vllm-project/vllm/commit/1a369783e9) [#45347](https://github.com/vllm-project/vllm/pull/45347)
  [BugFix] Avoid prematurely freeing cached mm encoder outputs (#45347)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-12** [`9ff278b1d2`](https://github.com/vllm-project/vllm/commit/9ff278b1d2) [#43877](https://github.com/vllm-project/vllm/pull/43877)
  [Core][KV Connector] fix scheduler KV connector stats aggregation (#43877)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-12** [`87b98d6d6c`](https://github.com/vllm-project/vllm/commit/87b98d6d6c) [#45300](https://github.com/vllm-project/vllm/pull/45300)
  [Rust Frontend][Bugfix] Forward --shutdown-timeout and --disable-log-stats to the managed Python engine (#45300)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/managed-engine/src/cli.rs`_
- **2026-06-11** [`7852e50e4d`](https://github.com/vllm-project/vllm/commit/7852e50e4d) [#43724](https://github.com/vllm-project/vllm/pull/43724)
  [docs] Document --scheduler-cls base class requirement (extend AsyncScheduler, not Scheduler) (#43724)
  _Files: `vllm/config/scheduler.py`_
- **2026-06-11** [`5d5591d99b`](https://github.com/vllm-project/vllm/commit/5d5591d99b) [#44887](https://github.com/vllm-project/vllm/pull/44887)
  [Rust Frontend] Populate `cached_token_count` in responses (#44887)
  _Files: `rust/src/chat/examples/external_engine_chat_qwen.rs`, `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/reasoning.rs`, `rust/src/chat/src/output/default/tool.rs` _+30 more__
- **2026-06-10** [`dc66e01a70`](https://github.com/vllm-project/vllm/commit/dc66e01a70) [#37898](https://github.com/vllm-project/vllm/pull/37898)
  [Hybrid] Marconi-style admission policy for hybrid cache (#37898)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-09** [`d841386d27`](https://github.com/vllm-project/vllm/commit/d841386d27) [#44321](https://github.com/vllm-project/vllm/pull/44321)
  [Rust Frontend] Support API key authentication (#44321)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+10 more__
- **2026-06-09** [`ebf53ba373`](https://github.com/vllm-project/vllm/commit/ebf53ba373) [#44729](https://github.com/vllm-project/vllm/pull/44729)
  [Bugfix][Rust Frontend] Set a structured-output backend so requests do not 500 (#44729)
  _Files: `rust/src/engine-core-client/src/protocol/mod.rs`_
- **2026-06-08** [`3f627ebef7`](https://github.com/vllm-project/vllm/commit/3f627ebef7) [#44595](https://github.com/vllm-project/vllm/pull/44595)
  [Misc] usage_stats: report more engine, spec-decode, and EP config (#44595)
  _Files: `vllm/v1/utils.py`_
- **2026-06-08** [`bc941f375d`](https://github.com/vllm-project/vllm/commit/bc941f375d) [#44856](https://github.com/vllm-project/vllm/pull/44856)
  [Rust Frontend] [Refactor] Refine utility call interfaces (#44856)
  _Files: `rust/src/engine-core-client/examples/external_engine_utility_call.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/protocol/utility.rs`, `rust/src/server/src/routes/pause.rs` _+1 more__
- **2026-06-08** [`3c0b4432be`](https://github.com/vllm-project/vllm/commit/3c0b4432be) [#44499](https://github.com/vllm-project/vllm/pull/44499)
  [Rust Frontend] Add /pause, /resume, /is_paused endpoints (#44499)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/pause.rs`, `rust/src/server/src/routes/tests.rs`_

## Perf / Benchmark  (6 commits)

- **2026-06-14** [`e2bf2b3d84`](https://github.com/vllm-project/vllm/commit/e2bf2b3d84) [#45566](https://github.com/vllm-project/vllm/pull/45566)
  [Perf] Use bisect for mm feature lookup in model runner v2 (#45566)
  _Files: `vllm/v1/worker/gpu/mm/encoder_runner.py`_
- **2026-06-10** [`89c6a41001`](https://github.com/vllm-project/vllm/commit/89c6a41001) [#42457](https://github.com/vllm-project/vllm/pull/42457)
  [Bench] Add BFCL dataset for vllm bench serve tool-calling workloads (#42457)
  _Files: `docs/benchmarking/cli.md`, `docs/features/tool_calling.md`, `tests/benchmarks/test_bfcl_dataset.py`, `vllm/benchmarks/datasets/__init__.py` _+3 more__
- **2026-06-09** [`1c2ffc6f88`](https://github.com/vllm-project/vllm/commit/1c2ffc6f88) [#44516](https://github.com/vllm-project/vllm/pull/44516)
  feat(multi-turn-bench): add api_key and custom headers for multi turn benchmark (#44516)
  _Files: `benchmarks/multi_turn/benchmark_serving_multi_turn.py`_
- **2026-06-09** [`cad4ca12b8`](https://github.com/vllm-project/vllm/commit/cad4ca12b8) [#44663](https://github.com/vllm-project/vllm/pull/44663)
  [Bugfix] Add X-Session-ID from conversation_id in multi-turn benchmark (#44663)
  _Files: `benchmarks/multi_turn/benchmark_serving_multi_turn.py`_
- **2026-06-08** [`ac3409d162`](https://github.com/vllm-project/vllm/commit/ac3409d162) [#44708](https://github.com/vllm-project/vllm/pull/44708)
  [Benchmark] Auto-detect and correct client/server tokenizer mismatch for random dataset (#44708)
  _Files: `vllm/benchmarks/serve.py`_
- **2026-06-08** [`d5fe994e79`](https://github.com/vllm-project/vllm/commit/d5fe994e79) [#44419](https://github.com/vllm-project/vllm/pull/44419)
  [CPU][Spec Decode] Warn about throughput loss when libiomp5 is not preloaded (#44419)
  _Files: `vllm/v1/worker/cpu_worker.py`_

## Docs  (6 commits)

- **2026-06-13** [`0d29612292`](https://github.com/vllm-project/vllm/commit/0d29612292) [#45412](https://github.com/vllm-project/vllm/pull/45412)
  [Doc] Fix uv dependency resolution failure for setuptools during CPU source builds (x86 & ARM) (#45412)
  _Files: `docs/getting_started/installation/cpu.arm.inc.md`, `docs/getting_started/installation/cpu.x86.inc.md`_
- **2026-06-12** [`a30addc754`](https://github.com/vllm-project/vllm/commit/a30addc754) [#44055](https://github.com/vllm-project/vllm/pull/44055)
  [Docs][KV Connector][NIXL] document KV Transfer stat logging and Prometheus metrics (#44055)
  _Files: `docs/features/nixl_connector_usage.md`_
- **2026-06-12** [`a37b4a940e`](https://github.com/vllm-project/vllm/commit/a37b4a940e) [#45301](https://github.com/vllm-project/vllm/pull/45301)
  [Doc] AGENTS.md: add section about coding style (#45301)
  _Files: `AGENTS.md`_
- **2026-06-11** [`432905d5d6`](https://github.com/vllm-project/vllm/commit/432905d5d6) [#45262](https://github.com/vllm-project/vllm/pull/45262)
  Only enable PR docs builds manually (#45262)
  _Files: `docs/pre_run_check.sh`_
- **2026-06-10** [`3d300aecb1`](https://github.com/vllm-project/vllm/commit/3d300aecb1) [#39400](https://github.com/vllm-project/vllm/pull/39400)
  [Doc] Switch K8S examples to default MP mode (#39400)
  _Files: `docs/deployment/frameworks/lws.md`, `docs/deployment/integrations/kthena.md`, `examples/ray_serving/multi-node-serving.sh`_
- **2026-06-09** [`fff9210b2a`](https://github.com/vllm-project/vllm/commit/fff9210b2a) [#44918](https://github.com/vllm-project/vllm/pull/44918)
  [CI/Docs] Remove stale disagg prefill links (#44918)
  _Files: `docs/features/disagg_prefill.md`_

## Speculative Decoding  (5 commits)

- **2026-06-15** [`9872921c5f`](https://github.com/vllm-project/vllm/commit/9872921c5f) [#44423](https://github.com/vllm-project/vllm/pull/44423)
  [XPU] skip UT test_with_ngram_gpu_spec_decoding (#44423)
  _Files: `tests/v1/e2e/general/test_async_scheduling.py`_
- **2026-06-14** [`4ef4492e9b`](https://github.com/vllm-project/vllm/commit/4ef4492e9b) [#32374](https://github.com/vllm-project/vllm/pull/32374)
  [V1][Spec Decode] Add Dynamic SD (#32374)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/dynamic_speculative_decoding.md`, `tests/v1/spec_decode/test_dynamic_sd.py`, `tests/v1/spec_decode/test_eagle.py` _+19 more__
- **2026-06-12** [`6f573f486b`](https://github.com/vllm-project/vllm/commit/6f573f486b) [#45217](https://github.com/vllm-project/vllm/pull/45217)
  [Bugfix] Initialize missing attributes in mistral eagle (#45217)
  _Files: `tests/model_executor/test_mistral_large_3_eagle.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`_
- **2026-06-11** [`ebc6ef971a`](https://github.com/vllm-project/vllm/commit/ebc6ef971a) [#43805](https://github.com/vllm-project/vllm/pull/43805)
  Hidden states extraction improvements (#43805)
  _Files: `benchmarks/benchmark_hidden_state_extraction.py`, `docs/features/speculative_decoding/extract_hidden_states.md`, `examples/features/speculative_decoding/extract_hidden_states_offline.py`, `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py` _+3 more__
- **2026-06-10** [`bd2d83ff31`](https://github.com/vllm-project/vllm/commit/bd2d83ff31) [#39419](https://github.com/vllm-project/vllm/pull/39419)
  [SpecDecode] Reduce TP communication for large-vocab draft models speculative decoding (#39419)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llama.py`, `vllm/model_executor/models/llama4_eagle.py` _+3 more__

## KV Cache / Offload  (5 commits)

- **2026-06-15** [`b675cb7d0f`](https://github.com/vllm-project/vllm/commit/b675cb7d0f) [#45086](https://github.com/vllm-project/vllm/pull/45086)
  [Bugfix][CPU] Honor cgroup memory limit when computing KV cache size (#45086)
  _Files: `vllm/utils/cpu_resource_utils.py`_
- **2026-06-12** [`b7f9b6ab27`](https://github.com/vllm-project/vllm/commit/b7f9b6ab27) [#42206](https://github.com/vllm-project/vllm/pull/42206)
  [Metrics] Add group-aware KV cache capacity to vllm:cache_config_info (#42206)
  _Files: `tests/entrypoints/serve/instrumentator/test_metrics.py`, `tests/v1/core/test_kv_cache_utils.py`, `vllm/config/cache.py`, `vllm/v1/core/kv_cache_utils.py` _+3 more__
- **2026-06-11** [`4085ff7cb4`](https://github.com/vllm-project/vllm/commit/4085ff7cb4) [#44594](https://github.com/vllm-project/vllm/pull/44594)
  [Core] Add kvcache watermark to reduce preemptions (#44594)
  _Files: `benchmarks/kv_cache_watermark.sh`, `tests/v1/core/test_scheduler.py`, `tests/v1/core/utils.py`, `vllm/config/scheduler.py` _+3 more__
- **2026-06-09** [`3d119f78f7`](https://github.com/vllm-project/vllm/commit/3d119f78f7) [#44415](https://github.com/vllm-project/vllm/pull/44415)
  [Docs] Add KV offloading usage guide (single- and multi-tier) (#44415)
  _Files: `docs/features/disagg_prefill.md`, `docs/features/kv_offloading_usage.md`_
- **2026-06-09** [`6690a0c4de`](https://github.com/vllm-project/vllm/commit/6690a0c4de) [#44629](https://github.com/vllm-project/vllm/pull/44629)
  [PD][Bugfix] Fix KV Cache sharing with HMA (#44629)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py`_

## LoRA  (3 commits)

- **2026-06-15** [`c4a3f9d137`](https://github.com/vllm-project/vllm/commit/c4a3f9d137) [#45413](https://github.com/vllm-project/vllm/pull/45413)
  [Frontend] Add Streaming Parser Engine and new Qwen3 Parser (#45413)
  _Files: `tests/parser/engine/__init__.py`, `tests/parser/engine/conftest.py`, `tests/parser/engine/replay_harness.py`, `tests/parser/engine/streaming_helpers.py` _+29 more__
- **2026-06-11** [`cc640ee8bc`](https://github.com/vllm-project/vllm/commit/cc640ee8bc) [#45030](https://github.com/vllm-project/vllm/pull/45030)
  [Rust Frontend][Metrics] Export `vllm:lora_requests_info` from frontend (#45030)
  _Files: `rust/Cargo.lock`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/client/state.rs` _+4 more__
- **2026-06-08** [`2c27c294c0`](https://github.com/vllm-project/vllm/commit/2c27c294c0) [#44450](https://github.com/vllm-project/vllm/pull/44450)
  [Model Runner V2] Fix mrv2 mm lora issue (#44450)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/worker/gpu/mm/lora.py`, `vllm/v1/worker/gpu/model_runner.py`_

## Compilation / CUDA Graph  (3 commits)

- **2026-06-15** [`2725c84aae`](https://github.com/vllm-project/vllm/commit/2725c84aae) [#38608](https://github.com/vllm-project/vllm/pull/38608)
  [XPU] Enable sequence parallel support for XPU (#38608)
  _Files: `tests/compile/conftest.py`, `tests/compile/test_sequence_parallelism_threshold.py`, `vllm/compilation/passes/fusion/sequence_parallelism.py`, `vllm/compilation/passes/pass_manager.py` _+1 more__
- **2026-06-12** [`053e7daa79`](https://github.com/vllm-project/vllm/commit/053e7daa79) [#44930](https://github.com/vllm-project/vllm/pull/44930)
  [Model] Add encoder CUDA graph support to Lfm2VL (#44930)
  _Files: `vllm/model_executor/models/lfm2_vl.py`_
- **2026-06-08** [`8fb0274415`](https://github.com/vllm-project/vllm/commit/8fb0274415) [#44484](https://github.com/vllm-project/vllm/pull/44484)
  [MM][CG] Simplify ViT CUDA graph interfaces (#44484)
  _Files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/step3_vl.py`_

---
_Generated 2026-06-15 14:35 UTC_