# vllm-project/vllm — Weekly Change Report
**Period:** 2026-06-15 → 2026-06-22  |  **Total commits:** 270

## ✨ New Features This Week

- **2026-06-22** [#44324](https://github.com/vllm-project/vllm/pull/44324) — [CPU][RISC-V] Add RVV micro GEMM for WNA16 (#44324)
- **2026-06-22** [#46137](https://github.com/vllm-project/vllm/pull/46137) — [Rust Frontend] Support thinking_token_budget for chat and completions (#46137)
- **2026-06-22** [#43468](https://github.com/vllm-project/vllm/pull/43468) — [feature][kv_offload] Self-describing KV events for OffloadingConnector (#43468)
- **2026-06-22** [#43081](https://github.com/vllm-project/vllm/pull/43081) — [SpecDecode] Support DFlash with FlashInfer  (#43081)
- **2026-06-22** [#45768](https://github.com/vllm-project/vllm/pull/45768) — [XPU][CI] Add agent_tags for Intel GPU CI (#45768)
- **2026-06-22** [#45955](https://github.com/vllm-project/vllm/pull/45955) — [ROCm][CI] Enable kv_connector unit tests on ROCm (#45955)
- **2026-06-21** [#43132](https://github.com/vllm-project/vllm/pull/43132) — [Spec Decode] Add Qwen3 architecture support for EAGLE3 (#43132)
- **2026-06-21** [#45555](https://github.com/vllm-project/vllm/pull/45555) — [Multimodal] Add Qwen2-VL/Qwen2.5-VL processor-mapped video loader (#45555)
- **2026-06-21** [#45957](https://github.com/vllm-project/vllm/pull/45957) — [KV Offloading] Add labeled metrics support (#45957)
- **2026-06-21** [#45181](https://github.com/vllm-project/vllm/pull/45181) — [Spec Decode] Support mixed KV page sizes for DFlash (#45181)
- _…and 60 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-22** [`89accad2cc`](https://github.com/vllm-project/vllm/commit/89accad2cc) [#45931](https://github.com/vllm-project/vllm/pull/45931) — [ROCm][DSV4] Disable TileLang MHC dispatch on gfx942 (#45931)
- **2026-06-22** [`f3df7a7231`](https://github.com/vllm-project/vllm/commit/f3df7a7231) [#45955](https://github.com/vllm-project/vllm/pull/45955) — [ROCm][CI] Enable kv_connector unit tests on ROCm (#45955)
- **2026-06-21** [`a19ff2218a`](https://github.com/vllm-project/vllm/commit/a19ff2218a) [#46018](https://github.com/vllm-project/vllm/pull/46018) — [Hardware][AMD][CI] Fix Spec Decode Eagle test group (#46018)
- **2026-06-21** [`4f0d0049a0`](https://github.com/vllm-project/vllm/commit/4f0d0049a0) [#46080](https://github.com/vllm-project/vllm/pull/46080) — [Hardware][AMD][CI] Fix Kernels Attention test groups (#46080)
- **2026-06-21** [`13b83d77ad`](https://github.com/vllm-project/vllm/commit/13b83d77ad) [#45967](https://github.com/vllm-project/vllm/pull/45967) — [ROCm][CI] skip test_double_aiter_rms_quant_fusion (#45967)
- **2026-06-21** [`50241602fd`](https://github.com/vllm-project/vllm/commit/50241602fd) [#46298](https://github.com/vllm-project/vllm/pull/46298) — [Hardware][AMD][CI] Fix gfx942 Kernels MoE test group (#46298)
- **2026-06-21** [`b91b7726e0`](https://github.com/vllm-project/vllm/commit/b91b7726e0) [#46039](https://github.com/vllm-project/vllm/pull/46039) — [ROCm][P/D] Support MiniMax-M3 mixed KV layouts in MoRIIO READ mode (#46039)
- **2026-06-20** [`1bdf9810aa`](https://github.com/vllm-project/vllm/commit/1bdf9810aa) [#46222](https://github.com/vllm-project/vllm/pull/46222) — [ROCm] [Bugfix] Bugfix ROCm Sparse Indexer (#46222)
- **2026-06-20** [`dced290769`](https://github.com/vllm-project/vllm/commit/dced290769) [#46024](https://github.com/vllm-project/vllm/pull/46024) — [Hardware][AMD][CI] Fix e2e core test group (#46024)
- **2026-06-19** [`0fbf42af84`](https://github.com/vllm-project/vllm/commit/0fbf42af84) [#46046](https://github.com/vllm-project/vllm/pull/46046) — [ROCm] Fix VRAM not freed in test_phi3v (#46046)
- **2026-06-19** [`e6cd8913dd`](https://github.com/vllm-project/vllm/commit/e6cd8913dd) [#46109](https://github.com/vllm-project/vllm/pull/46109) — [ROCm][CI] Skip Qwen3.5-35B-A3B-MXFP4-AITER-TP2 for non gfx950 (#46109)
- **2026-06-19** [`4a083cc858`](https://github.com/vllm-project/vllm/commit/4a083cc858) [#46180](https://github.com/vllm-project/vllm/pull/46180) — [ROCm][CI] Pin `test_rocm_compressed_tensors_w8a8` to TRITON_ATTN (#46180)
- **2026-06-19** [`dec860fb19`](https://github.com/vllm-project/vllm/commit/dec860fb19) [#46176](https://github.com/vllm-project/vllm/pull/46176) — [ROCm] Use vLLM's fp8 quant max in AITER hipBLASLt accuracy test (#46176)
- **2026-06-19** [`4a8abf37c7`](https://github.com/vllm-project/vllm/commit/4a8abf37c7) [#46173](https://github.com/vllm-project/vllm/pull/46173) — [Test] Migrate test_openai_schema.py to schemathesis 4.x (#46173)
- **2026-06-19** [`ecf9d83520`](https://github.com/vllm-project/vllm/commit/ecf9d83520) [#45509](https://github.com/vllm-project/vllm/pull/45509) — [AMD][CI] Fix Language Models Test (Extended Generation) failures (#45509)
- **2026-06-19** [`ab66606993`](https://github.com/vllm-project/vllm/commit/ab66606993) [#45895](https://github.com/vllm-project/vllm/pull/45895) — [bugfix]Indexer init skip and MTP TopK share for iteration (#45895)
- **2026-06-18** [`f6ba720963`](https://github.com/vllm-project/vllm/commit/f6ba720963) [#45675](https://github.com/vllm-project/vllm/pull/45675) — (security) Upgrade Starlette to >= 1.0.1 to fix CVE-2026-48710 (#45675)
- **2026-06-18** [`e2352c2974`](https://github.com/vllm-project/vllm/commit/e2352c2974) [#45706](https://github.com/vllm-project/vllm/pull/45706) — [ROCm][Spec Decode] Fix probabilistic draft probs test attention backend (#45706)
- **2026-06-18** [`25faa1f4cc`](https://github.com/vllm-project/vllm/commit/25faa1f4cc) [#43802](https://github.com/vllm-project/vllm/pull/43802) — [CI]Enable mxfp4 lora test for ROCm platform (#43802)
- **2026-06-18** [`21da47dabe`](https://github.com/vllm-project/vllm/commit/21da47dabe) [#45970](https://github.com/vllm-project/vllm/pull/45970) — [ROCm][CI] move lora%N test to mi300 and gate (#45970)
- **2026-06-18** [`5099474633`](https://github.com/vllm-project/vllm/commit/5099474633) [#45747](https://github.com/vllm-project/vllm/pull/45747) — [Bugfix][ROCm] Fix rocm_aiter_per_tensor_quant custom op aliasing (#45747)
- **2026-06-18** [`afdcbd5d39`](https://github.com/vllm-project/vllm/commit/afdcbd5d39) [#45681](https://github.com/vllm-project/vllm/pull/45681) — [ROCm][DSv4] Functional fixes for DeepSeek V4 on MI300X/MI325X (#45681)
- **2026-06-18** [`8d4f54966c`](https://github.com/vllm-project/vllm/commit/8d4f54966c) [#42727](https://github.com/vllm-project/vllm/pull/42727) — fix(quantization): Fix AWQ dequantize on Intel XPU and refactor AutoAWQ config (#42727)
- **2026-06-17** [`091386a99b`](https://github.com/vllm-project/vllm/commit/091386a99b) [#45794](https://github.com/vllm-project/vllm/pull/45794) — [Bugfix] MiniMax-M3 (AMD): add packed_modules_mapping and pass swiglu… (#45794)
- **2026-06-17** [`d112eb1ac7`](https://github.com/vllm-project/vllm/commit/d112eb1ac7) [#45896](https://github.com/vllm-project/vllm/pull/45896) — [feature] MiniMax-M3-MXFP4 support added (#45896)
- **2026-06-17** [`0b131b16c9`](https://github.com/vllm-project/vllm/commit/0b131b16c9) [#44626](https://github.com/vllm-project/vllm/pull/44626) — [ROCm][AITER][Quark] Tag per-channel FP8 weights as PER_CHANNEL so AITER pre-shuffled GEMM is selected (#44626)
- **2026-06-17** [`e28e8c8782`](https://github.com/vllm-project/vllm/commit/e28e8c8782) [#45854](https://github.com/vllm-project/vllm/pull/45854) — [ROCm][Quant] Minimax-M3:  Enable fp8_per_channel for bf16 weights on mi300x (#45854)
- **2026-06-17** [`d537122398`](https://github.com/vllm-project/vllm/commit/d537122398) [#45782](https://github.com/vllm-project/vllm/pull/45782) — [ROCm][Bugfix]: Fallback GFX942 sparse MLA ops to Triton (#45782)
- **2026-06-17** [`4c62663315`](https://github.com/vllm-project/vllm/commit/4c62663315) [#45744](https://github.com/vllm-project/vllm/pull/45744) — [M3] Enable FP8 sparse GQA (#45744)
- **2026-06-17** [`2785a5e0e6`](https://github.com/vllm-project/vllm/commit/2785a5e0e6) [#44912](https://github.com/vllm-project/vllm/pull/44912) — [Bugfix][ROCm] Fix FP8 per-tensor scale rank mismatch causing Inductor assertion failure (#44912)
- **2026-06-17** [`efd15e192a`](https://github.com/vllm-project/vllm/commit/efd15e192a) [#45720](https://github.com/vllm-project/vllm/pull/45720) — [Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype (#45720)
- **2026-06-16** [`4fadf9c92c`](https://github.com/vllm-project/vllm/commit/4fadf9c92c) [#45858](https://github.com/vllm-project/vllm/pull/45858) — [ROCm][CI] fix multimodel run cmds (#45858)
- **2026-06-16** [`f2beaa80c8`](https://github.com/vllm-project/vllm/commit/f2beaa80c8) [#45725](https://github.com/vllm-project/vllm/pull/45725) — [ROCm][Quant] mxfp8 moe/linear gfx950 tuning for MiniMax-M3 (#45725)
- **2026-06-16** [`188c68798e`](https://github.com/vllm-project/vllm/commit/188c68798e) [#45488](https://github.com/vllm-project/vllm/pull/45488) — [KVConnector][MoRIIO] Allow overriding the advertised host IP (#45488)
- **2026-06-16** [`6f612fbedf`](https://github.com/vllm-project/vllm/commit/6f612fbedf) [#45722](https://github.com/vllm-project/vllm/pull/45722) — [ROCm][CI] Patch conftest to resolve occasional OOMs (#45722)
- **2026-06-16** [`3d34f8cbdc`](https://github.com/vllm-project/vllm/commit/3d34f8cbdc) [#44178](https://github.com/vllm-project/vllm/pull/44178) — [ROCm][Cleanup] Remove stale AITER FA hybrid KV-cache TODO (#44178)
- **2026-06-16** [`eb04c769d3`](https://github.com/vllm-project/vllm/commit/eb04c769d3) [#43050](https://github.com/vllm-project/vllm/pull/43050) — feat: MLA prefill enable FA4 fp8 output (#43050)
- **2026-06-16** [`040df8f2ea`](https://github.com/vllm-project/vllm/commit/040df8f2ea) [#45728](https://github.com/vllm-project/vllm/pull/45728) — [CI] Fix attention benchmark smoke test (#45728)
- **2026-06-16** [`7e179e4bc0`](https://github.com/vllm-project/vllm/commit/7e179e4bc0) [#41532](https://github.com/vllm-project/vllm/pull/41532) — [ROCm][CI] Gate incompatible HF references on Transformers v5 (#41532)
- **2026-06-16** [`b00e76ff72`](https://github.com/vllm-project/vllm/commit/b00e76ff72) [#45210](https://github.com/vllm-project/vllm/pull/45210) — [Misc][Model] add io processor for query/document embeddings from ColBERT (jinaai/jina-colbert-v2) (#45210)
- **2026-06-15** [`a3195fab7b`](https://github.com/vllm-project/vllm/commit/a3195fab7b) [#43981](https://github.com/vllm-project/vllm/pull/43981) — [AMD][Bugfix][Quantization] Honor fused-name match in is_layer_skipped (#43981)
- **2026-06-15** [`25c53d1293`](https://github.com/vllm-project/vllm/commit/25c53d1293) [#45671](https://github.com/vllm-project/vllm/pull/45671) — [ROCm][Doc] Add installation notes about python version requirement (#45671)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#40604](https://github.com/vllm-project/vllm/issues/40604) | [Bug]: DeepSeek-R1 hang on 8xB200 after NCCL Initialization | bug | 2026-06-22 |
| [#46253](https://github.com/vllm-project/vllm/issues/46253) | [Bug]: Cross-node CUDA graph capture fails (illegal memory access at c | — | 2026-06-22 |
| [#45702](https://github.com/vllm-project/vllm/issues/45702) | [RFC]: Fine-Grained Prefix Cache Hits for Hybrid Models | RFC | 2026-06-22 |
| [#46367](https://github.com/vllm-project/vllm/issues/46367) | [Bug]: Weird outputs for GLM-5.2-FP8 on 8xB200 | bug | 2026-06-22 |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | [Feature]: Batch Invariant Feature and Performance Optimization | good first issue, feature request | 2026-06-22 |
| [#46358](https://github.com/vllm-project/vllm/issues/46358) | [RFC]: Unify Context Parallelism in vLLM (PCP ⊥ DCP) | RFC | 2026-06-22 |
| [#45658](https://github.com/vllm-project/vllm/issues/45658) | [Bug]: AssertionError: Encoder cache miss | bug | 2026-06-22 |
| [#41789](https://github.com/vllm-project/vllm/issues/41789) | [Bug]: gemma4 31B MTP Avg Draft acceptance rate: 0.2% | bug | 2026-06-22 |
| [#42545](https://github.com/vllm-project/vllm/issues/42545) | [RFC]: Tensor descriptor (TD) adoption strategy for vLLM Triton kernel | — | 2026-06-22 |
| [#46354](https://github.com/vllm-project/vllm/issues/46354) | [Bug]: AssertionError: Expected a cached item for mm_hash | usage | 2026-06-22 |
| [#46347](https://github.com/vllm-project/vllm/issues/46347) | [Bug]: Changing VLLM_CPU_KVCACHE_SPACE drops Qwen 3.5 accuracy on AMD  | bug, rocm | 2026-06-22 |
| [#46249](https://github.com/vllm-project/vllm/issues/46249) | [Bug]: [Regression] Qwen3.6-27B tool calls fail on Responses API when  | bug | 2026-06-22 |
| [#40076](https://github.com/vllm-project/vllm/issues/40076) | [Feature]: Per-request timing metrics in response body | feature request | 2026-06-22 |
| [#40696](https://github.com/vllm-project/vllm/issues/40696) | [Feature]: Prefix caching completely ineffective for Mamba-hybrid mode | feature request | 2026-06-22 |
| [#14365](https://github.com/vllm-project/vllm/issues/14365) | [Bug]: API Connection Error after concurrent API calls | bug, stale | 2026-06-22 |
| [#21231](https://github.com/vllm-project/vllm/issues/21231) | [Bug]: 100% cpu usage on 3 cores on every node when using ray distribu | bug, ray, stale | 2026-06-22 |
| [#25021](https://github.com/vllm-project/vllm/issues/25021) | [Feature]: Ship some basic html UI with vllm for most basic testing (n | feature request, stale | 2026-06-22 |
| [#25771](https://github.com/vllm-project/vllm/issues/25771) | [Bug]: Too many values to unpack in dispatch_cpu_unquantized_gemm [Liq | bug, stale, cpu | 2026-06-22 |
| [#31394](https://github.com/vllm-project/vllm/issues/31394) | [Bug]: accuracy issue with VLLM_USE_FLASHINFER_MOE_FP8=1 for Qwen3-Cod | bug, stale | 2026-06-22 |
| [#43367](https://github.com/vllm-project/vllm/issues/43367) | [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel afte | bug | 2026-06-22 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 41 |
| Other | 36 |
| Attention | 26 |
| Scheduler / Engine | 26 |
| Models | 20 |
| MoE / Expert Parallel | 19 |
| Quantization | 16 |
| Serving / API | 15 |
| CI / Build | 14 |
| Disaggregation / PD | 14 |
| Multimodal | 13 |
| KV Cache / Offload | 10 |
| LoRA | 7 |
| Compilation / CUDA Graph | 4 |
| Docs | 3 |
| Speculative Decoding | 3 |
| Perf / Benchmark | 3 |

## ROCm / AMD  (41 commits)

- **2026-06-22** [`89accad2cc`](https://github.com/vllm-project/vllm/commit/89accad2cc) [#45931](https://github.com/vllm-project/vllm/pull/45931)
  [ROCm][DSV4] Disable TileLang MHC dispatch on gfx942 (#45931)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-06-22** [`f3df7a7231`](https://github.com/vllm-project/vllm/commit/f3df7a7231) [#45955](https://github.com/vllm-project/vllm/pull/45955)
  [ROCm][CI] Enable kv_connector unit tests on ROCm (#45955)
  _Files: `.buildkite/scripts/install-kv-connectors.sh`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_offloading_connector.py`_
- **2026-06-21** [`a19ff2218a`](https://github.com/vllm-project/vllm/commit/a19ff2218a) [#46018](https://github.com/vllm-project/vllm/pull/46018)
  [Hardware][AMD][CI] Fix Spec Decode Eagle test group (#46018)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/test_spec_decode.py`_
- **2026-06-21** [`4f0d0049a0`](https://github.com/vllm-project/vllm/commit/4f0d0049a0) [#46080](https://github.com/vllm-project/vllm/pull/46080)
  [Hardware][AMD][CI] Fix Kernels Attention test groups (#46080)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_prefix_prefill.py` _+2 more__
- **2026-06-21** [`13b83d77ad`](https://github.com/vllm-project/vllm/commit/13b83d77ad) [#45967](https://github.com/vllm-project/vllm/pull/45967)
  [ROCm][CI] skip test_double_aiter_rms_quant_fusion (#45967)
  _Files: `.buildkite/test_areas/pytorch.yaml`, `tests/compile/passes/test_double_aiter_rms_quant_fusion.py`_
- **2026-06-21** [`50241602fd`](https://github.com/vllm-project/vllm/commit/50241602fd) [#46298](https://github.com/vllm-project/vllm/pull/46298)
  [Hardware][AMD][CI] Fix gfx942 Kernels MoE test group (#46298)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_ocp_mx_moe.py`_
- **2026-06-21** [`b91b7726e0`](https://github.com/vllm-project/vllm/commit/b91b7726e0) [#46039](https://github.com/vllm-project/vllm/pull/46039)
  [ROCm][P/D] Support MiniMax-M3 mixed KV layouts in MoRIIO READ mode (#46039)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`_
- **2026-06-20** [`1bdf9810aa`](https://github.com/vllm-project/vllm/commit/1bdf9810aa) [#46222](https://github.com/vllm-project/vllm/pull/46222)
  [ROCm] [Bugfix] Bugfix ROCm Sparse Indexer (#46222)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-06-20** [`dced290769`](https://github.com/vllm-project/vllm/commit/dced290769) [#46024](https://github.com/vllm-project/vllm/pull/46024)
  [Hardware][AMD][CI] Fix e2e core test group (#46024)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `tests/v1/e2e/general/test_cascade_attention.py`_
- **2026-06-19** [`0fbf42af84`](https://github.com/vllm-project/vllm/commit/0fbf42af84) [#46046](https://github.com/vllm-project/vllm/pull/46046)
  [ROCm] Fix VRAM not freed in test_phi3v (#46046)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`, `tests/models/multimodal/pooling/test_phi3v.py`_
- **2026-06-19** [`e6cd8913dd`](https://github.com/vllm-project/vllm/commit/e6cd8913dd) [#46109](https://github.com/vllm-project/vllm/pull/46109)
  [ROCm][CI] Skip Qwen3.5-35B-A3B-MXFP4-AITER-TP2 for non gfx950 (#46109)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/test_gsm8k_correctness.py`_
- **2026-06-19** [`4a083cc858`](https://github.com/vllm-project/vllm/commit/4a083cc858) [#46180](https://github.com/vllm-project/vllm/pull/46180)
  [ROCm][CI] Pin `test_rocm_compressed_tensors_w8a8` to TRITON_ATTN (#46180)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/quantization/test_triton_scaled_mm.py`_
- **2026-06-19** [`dec860fb19`](https://github.com/vllm-project/vllm/commit/dec860fb19) [#46176](https://github.com/vllm-project/vllm/pull/46176)
  [ROCm] Use vLLM's fp8 quant max in AITER hipBLASLt accuracy test (#46176)
  _Files: `tests/rocm/aiter/test_aiter_hipb_mm_linear_kernel.py`_
- **2026-06-19** [`4a8abf37c7`](https://github.com/vllm-project/vllm/commit/4a8abf37c7) [#46173](https://github.com/vllm-project/vllm/pull/46173)
  [Test] Migrate test_openai_schema.py to schemathesis 4.x (#46173)
  _Files: `requirements/test/cuda.in`, `requirements/test/nightly-torch.txt`, `requirements/test/rocm.in`, `tests/entrypoints/openai/test_openai_schema.py`_
- **2026-06-19** [`ecf9d83520`](https://github.com/vllm-project/vllm/commit/ecf9d83520) [#45509](https://github.com/vllm-project/vllm/pull/45509)
  [AMD][CI] Fix Language Models Test (Extended Generation) failures (#45509)
  _Files: `tests/models/language/generation/test_common.py`_
- **2026-06-19** [`ab66606993`](https://github.com/vllm-project/vllm/commit/ab66606993) [#45895](https://github.com/vllm-project/vllm/pull/45895)
  [bugfix]Indexer init skip and MTP TopK share for iteration (#45895)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/mla.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/models/deepseek_v2.py` _+5 more__
- **2026-06-18** [`f6ba720963`](https://github.com/vllm-project/vllm/commit/f6ba720963) [#45675](https://github.com/vllm-project/vllm/pull/45675)
  (security) Upgrade Starlette to >= 1.0.1 to fix CVE-2026-48710 (#45675)
  _Files: `requirements/common.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt`_
- **2026-06-18** [`e2352c2974`](https://github.com/vllm-project/vllm/commit/e2352c2974) [#45706](https://github.com/vllm-project/vllm/pull/45706)
  [ROCm][Spec Decode] Fix probabilistic draft probs test attention backend (#45706)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/spec_decode/test_eagle.py`_
- **2026-06-18** [`25faa1f4cc`](https://github.com/vllm-project/vllm/commit/25faa1f4cc) [#43802](https://github.com/vllm-project/vllm/pull/43802)
  [CI]Enable mxfp4 lora test for ROCm platform (#43802)
  _Files: `tests/lora/test_gptoss_tp.py`_
- **2026-06-18** [`21da47dabe`](https://github.com/vllm-project/vllm/commit/21da47dabe) [#45970](https://github.com/vllm-project/vllm/pull/45970)
  [ROCm][CI] move lora%N test to mi300 and gate (#45970)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/lora.yaml`_
- **2026-06-18** [`5099474633`](https://github.com/vllm-project/vllm/commit/5099474633) [#45747](https://github.com/vllm-project/vllm/pull/45747)
  [Bugfix][ROCm] Fix rocm_aiter_per_tensor_quant custom op aliasing (#45747)
  _Files: `tests/rocm/aiter/test_quant_op_schema.py`, `vllm/_aiter_ops.py`_
- **2026-06-18** [`afdcbd5d39`](https://github.com/vllm-project/vllm/commit/afdcbd5d39) [#45681](https://github.com/vllm-project/vllm/pull/45681)
  [ROCm][DSv4] Functional fixes for DeepSeek V4 on MI300X/MI325X (#45681)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`, `vllm/models/deepseek_v4/amd/rocm.py` _+4 more__
- **2026-06-18** [`8d4f54966c`](https://github.com/vllm-project/vllm/commit/8d4f54966c) [#42727](https://github.com/vllm-project/vllm/pull/42727)
  fix(quantization): Fix AWQ dequantize on Intel XPU and refactor AutoAWQ config (#42727)
  _Files: `docs/features/quantization/auto_awq.md`, `tests/quantization/test_auto_awq.py`, `tests/quantization/test_auto_round.py`, `tests/quantization/test_configs.py` _+16 more__
- **2026-06-17** [`091386a99b`](https://github.com/vllm-project/vllm/commit/091386a99b) [#45794](https://github.com/vllm-project/vllm/pull/45794)
  [Bugfix] MiniMax-M3 (AMD): add packed_modules_mapping and pass swiglu… (#45794)
- **2026-06-17** [`d112eb1ac7`](https://github.com/vllm-project/vllm/commit/d112eb1ac7) [#45896](https://github.com/vllm-project/vllm/pull/45896)
  [feature] MiniMax-M3-MXFP4 support added (#45896)
  _Files: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/models/minimax_m3/amd/model.py`_
- **2026-06-17** [`0b131b16c9`](https://github.com/vllm-project/vllm/commit/0b131b16c9) [#44626](https://github.com/vllm-project/vllm/pull/44626)
  [ROCm][AITER][Quark] Tag per-channel FP8 weights as PER_CHANNEL so AITER pre-shuffled GEMM is selected (#44626)
  _Files: `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_fp8.py`_
- **2026-06-17** [`e28e8c8782`](https://github.com/vllm-project/vllm/commit/e28e8c8782) [#45854](https://github.com/vllm-project/vllm/pull/45854)
  [ROCm][Quant] Minimax-M3:  Enable fp8_per_channel for bf16 weights on mi300x (#45854)
  _Files: `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/online/fp8.py` _+1 more__
- **2026-06-17** [`d537122398`](https://github.com/vllm-project/vllm/commit/d537122398) [#45782](https://github.com/vllm-project/vllm/pull/45782)
  [ROCm][Bugfix]: Fallback GFX942 sparse MLA ops to Triton (#45782)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-06-17** [`4c62663315`](https://github.com/vllm-project/vllm/commit/4c62663315) [#45744](https://github.com/vllm-project/vllm/pull/45744)
  [M3] Enable FP8 sparse GQA (#45744)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+6 more__
- **2026-06-17** [`2785a5e0e6`](https://github.com/vllm-project/vllm/commit/2785a5e0e6) [#44912](https://github.com/vllm-project/vllm/pull/44912)
  [Bugfix][ROCm] Fix FP8 per-tensor scale rank mismatch causing Inductor assertion failure (#44912)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py`_
- **2026-06-17** [`efd15e192a`](https://github.com/vllm-project/vllm/commit/efd15e192a) [#45720](https://github.com/vllm-project/vllm/pull/45720)
  [Bugfix][ROCm] Fix MiniMax-M3 FP8 KV cache dtype (#45720)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/ops/sparse_attn.py`, `vllm/models/minimax_m3/common/sparse_attention.py`_
- **2026-06-16** [`4fadf9c92c`](https://github.com/vllm-project/vllm/commit/4fadf9c92c) [#45858](https://github.com/vllm-project/vllm/pull/45858)
  [ROCm][CI] fix multimodel run cmds (#45858)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-16** [`f2beaa80c8`](https://github.com/vllm-project/vllm/commit/f2beaa80c8) [#45725](https://github.com/vllm-project/vllm/pull/45725)
  [ROCm][Quant] mxfp8 moe/linear gfx950 tuning for MiniMax-M3 (#45725)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`, `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`_
- **2026-06-16** [`6f612fbedf`](https://github.com/vllm-project/vllm/commit/6f612fbedf) [#45722](https://github.com/vllm-project/vllm/pull/45722)
  [ROCm][CI] Patch conftest to resolve occasional OOMs (#45722)
  _Files: `tests/conftest.py`_
- **2026-06-16** [`3d34f8cbdc`](https://github.com/vllm-project/vllm/commit/3d34f8cbdc) [#44178](https://github.com/vllm-project/vllm/pull/44178)
  [ROCm][Cleanup] Remove stale AITER FA hybrid KV-cache TODO (#44178)
  _Files: `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-06-16** [`eb04c769d3`](https://github.com/vllm-project/vllm/commit/eb04c769d3) [#43050](https://github.com/vllm-project/vllm/pull/43050)
  feat: MLA prefill enable FA4 fp8 output (#43050)
  _Files: `benchmarks/attention_benchmarks/benchmark.py`, `benchmarks/attention_benchmarks/configs/mla_fa4_fp8_output.yaml`, `benchmarks/attention_benchmarks/mla_runner.py`, `tests/v1/attention/test_mla_prefill_quant_output.py` _+9 more__
- **2026-06-16** [`040df8f2ea`](https://github.com/vllm-project/vllm/commit/040df8f2ea) [#45728](https://github.com/vllm-project/vllm/pull/45728)
  [CI] Fix attention benchmark smoke test (#45728)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/benchmarks.yaml`_
- **2026-06-16** [`7e179e4bc0`](https://github.com/vllm-project/vllm/commit/7e179e4bc0) [#41532](https://github.com/vllm-project/vllm/pull/41532)
  [ROCm][CI] Gate incompatible HF references on Transformers v5 (#41532)
  _Files: `setup.py`, `tests/models/language/generation/test_common.py`, `tests/models/multimodal/generation/test_musicflamingo.py`, `tests/models/multimodal/processing/test_audioflamingo3.py` _+6 more__
- **2026-06-16** [`b00e76ff72`](https://github.com/vllm-project/vllm/commit/b00e76ff72) [#45210](https://github.com/vllm-project/vllm/pull/45210)
  [Misc][Model] add io processor for query/document embeddings from ColBERT (jinaai/jina-colbert-v2) (#45210)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/plugins.yaml`, `tests/plugins/colbert_query_plugin/colbert_query_processor/__init__.py`, `tests/plugins/colbert_query_plugin/colbert_query_processor/query_embedding_processor.py` _+3 more__
- **2026-06-15** [`a3195fab7b`](https://github.com/vllm-project/vllm/commit/a3195fab7b) [#43981](https://github.com/vllm-project/vllm/pull/43981)
  [AMD][Bugfix][Quantization] Honor fused-name match in is_layer_skipped (#43981)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/utils/quant_utils.py`_
- **2026-06-15** [`25c53d1293`](https://github.com/vllm-project/vllm/commit/25c53d1293) [#45671](https://github.com/vllm-project/vllm/pull/45671)
  [ROCm][Doc] Add installation notes about python version requirement (#45671)
  _Files: `docs/getting_started/installation/gpu.rocm.inc.md`_

## Other  (36 commits)

- **2026-06-22** [`a4610da0c6`](https://github.com/vllm-project/vllm/commit/a4610da0c6) [#46373](https://github.com/vllm-project/vllm/pull/46373)
  [docs] link security docs from AGENTS (#46373)
  _Files: `AGENTS.md`_
- **2026-06-22** [`d2c671c29b`](https://github.com/vllm-project/vllm/commit/d2c671c29b) [#44324](https://github.com/vllm-project/vllm/pull/44324)
  [CPU][RISC-V] Add RVV micro GEMM for WNA16 (#44324)
  _Files: `csrc/cpu/cpu_wna16.cpp`, `csrc/cpu/micro_gemm/cpu_micro_gemm_rvv.hpp`, `csrc/cpu/utils.hpp`, `vllm/model_executor/kernels/linear/mixed_precision/cpu.py`_
- **2026-06-22** [`78739e3bda`](https://github.com/vllm-project/vllm/commit/78739e3bda) [#46313](https://github.com/vllm-project/vllm/pull/46313)
  [Bugfix] Reject matryoshka embedding dimensions above hidden size (#46313)
  _Files: `tests/test_pooling_params.py`, `vllm/pooling_params.py`_
- **2026-06-22** [`1c4b51b990`](https://github.com/vllm-project/vllm/commit/1c4b51b990) [#46352](https://github.com/vllm-project/vllm/pull/46352)
  Temporarily skip M3 on CI (#46352)
  _Files: `tests/models/registry.py`_
- **2026-06-22** [`68567ef2df`](https://github.com/vllm-project/vllm/commit/68567ef2df) [#46216](https://github.com/vllm-project/vllm/pull/46216)
  [CPUOffloadingManager] Maintain evictable list in LRUCachePolicy (#46216)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/policies/base.py` _+1 more__
- **2026-06-22** [`6bc6f2d86d`](https://github.com/vllm-project/vllm/commit/6bc6f2d86d) [#45939](https://github.com/vllm-project/vllm/pull/45939)
  [1/N][Core] add partial prefix cache primitives (#45939)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/block_pool.py` _+1 more__
- **2026-06-22** [`31124749d1`](https://github.com/vllm-project/vllm/commit/31124749d1) [#46113](https://github.com/vllm-project/vllm/pull/46113)
  [Bugfix] [Rust Frontend] Fix stop string truncation with repeated matches (#46113)
  _Files: `rust/src/text/src/output/decoded.rs`_
- **2026-06-21** [`b5495cc5f9`](https://github.com/vllm-project/vllm/commit/b5495cc5f9) [#44665](https://github.com/vllm-project/vllm/pull/44665)
  Fix memory pointer overflow in Mamba state buffers (#44665)
  _Files: `vllm/v1/worker/mamba_utils.py`_
- **2026-06-21** [`183a430c13`](https://github.com/vllm-project/vllm/commit/183a430c13) [#46243](https://github.com/vllm-project/vllm/pull/46243)
  [Bugfix][Model Runner V2] Fix min_tokens off-by-one in the V2 GPU sampler (#46243)
  _Files: `vllm/v1/worker/gpu/sample/logit_bias.py`_
- **2026-06-20** [`8dd1b702f2`](https://github.com/vllm-project/vllm/commit/8dd1b702f2) [#35530](https://github.com/vllm-project/vllm/pull/35530)
  [Misc] Fix stale doc URL and docstring module path (#35530)
  _Files: `vllm/envs.py`, `vllm/tool_parsers/__init__.py`_
- **2026-06-20** [`3b4a76b63f`](https://github.com/vllm-project/vllm/commit/3b4a76b63f) [#45737](https://github.com/vllm-project/vllm/pull/45737)
  [KV-Offloading] : Expose CPU cache usage metric  (#45737)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/common.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-06-18** [`16908e132e`](https://github.com/vllm-project/vllm/commit/16908e132e) [#45996](https://github.com/vllm-project/vllm/pull/45996)
  [MRV2] Make FP32 Gumbel sampling more accurate (#45996)
  _Files: `tests/v1/worker/test_gpu_gumbel_sample.py`, `vllm/v1/worker/gpu/sample/gumbel.py`_
- **2026-06-18** [`ea6078fe6a`](https://github.com/vllm-project/vllm/commit/ea6078fe6a) [#46044](https://github.com/vllm-project/vllm/pull/46044)
  [KV Connector][Offloading] Disable parallel-agnostic fs-tier cache on V2 model runner (#46044)
  _Files: `tests/v1/kv_offload/test_file_mapper.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/file_mapper.py`_
- **2026-06-18** [`837db7605e`](https://github.com/vllm-project/vllm/commit/837db7605e) [#43984](https://github.com/vllm-project/vllm/pull/43984)
  [Bugfix][Tool Parser] Handle non-finite numbers in coerce_to_schema_type (#43984)
  _Files: `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/utils.py`_
- **2026-06-18** [`bf2a393034`](https://github.com/vllm-project/vllm/commit/bf2a393034) [#46053](https://github.com/vllm-project/vllm/pull/46053)
  Temporarily remove @markmc from CODEOWNERS (#46053)
  _Files: `.github/CODEOWNERS`_
- **2026-06-18** [`351c72d6e5`](https://github.com/vllm-project/vllm/commit/351c72d6e5) [#44991](https://github.com/vllm-project/vllm/pull/44991)
  [CPU] Skip Triton kernel monkey-patches when Triton-CPU is available (#44991)
  _Files: `vllm/v1/sample/rejection_sampler.py`, `vllm/v1/spec_decode/utils.py`, `vllm/v1/worker/cpu_model_runner.py`_
- **2026-06-18** [`ed938ad7db`](https://github.com/vllm-project/vllm/commit/ed938ad7db) [#45757](https://github.com/vllm-project/vllm/pull/45757)
  [CPUOffloading] Guard CPU eviction check (#45757)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py`_
- **2026-06-18** [`731fb3323d`](https://github.com/vllm-project/vllm/commit/731fb3323d) [#45876](https://github.com/vllm-project/vllm/pull/45876)
  [Rust Frontend] Validate tokenized bad_words vocabulary range (#45876)
  _Files: `rust/src/text/src/lower.rs`, `rust/src/text/src/lower/token_ids.rs`_
- **2026-06-17** [`f694d43b33`](https://github.com/vllm-project/vllm/commit/f694d43b33) [#45913](https://github.com/vllm-project/vllm/pull/45913)
  [Bugfix][test] Use Salesforce/wikitext for ppl tests (#45913)
  _Files: `tests/models/language/generation_ppl_test/ppl_utils.py`_
- **2026-06-17** [`93bbe94d3a`](https://github.com/vllm-project/vllm/commit/93bbe94d3a) [#41430](https://github.com/vllm-project/vllm/pull/41430)
  [Kernel] Add weightless RMSNorm CUDA kernels for has_weight=False (#41430) (#44109)
  _Files: `csrc/cpu/layernorm.cpp`, `csrc/cpu/torch_bindings.cpp`, `csrc/libtorch_stable/layernorm_kernels.cu`, `csrc/libtorch_stable/ops.h` _+7 more__
- **2026-06-17** [`295232a26a`](https://github.com/vllm-project/vllm/commit/295232a26a) [#44382](https://github.com/vllm-project/vllm/pull/44382)
  [Rust Frontend] Add /abort_requests endpoint (#44382)
  _Files: `rust/src/server/src/routes.rs`, `rust/src/server/src/routes/abort_requests.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-17** [`14b438a98b`](https://github.com/vllm-project/vllm/commit/14b438a98b) [#45868](https://github.com/vllm-project/vllm/pull/45868)
  [ModelRunnerV2] Various model/config compatibility fixes (#45868)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu/mm/encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/whisper.py`_
- **2026-06-16** [`4bf699d310`](https://github.com/vllm-project/vllm/commit/4bf699d310) [#45473](https://github.com/vllm-project/vllm/pull/45473)
  [Kernel] Support DS Mamba tail copy for MTP align mode (#45473)
  _Files: `tests/v1/worker/test_mamba_utils.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-06-16** [`520828789c`](https://github.com/vllm-project/vllm/commit/520828789c) [#42656](https://github.com/vllm-project/vllm/pull/42656)
  Apply LRU policy only to proper cache entries (#42656)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/block_pool.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-16** [`475a6ad18a`](https://github.com/vllm-project/vllm/commit/475a6ad18a) [#45853](https://github.com/vllm-project/vllm/pull/45853)
  [Misc] Update Mergify tool-calling label  (#45853)
  _Files: `.github/mergify.yml`_
- **2026-06-16** [`c45f681932`](https://github.com/vllm-project/vllm/commit/c45f681932) [#45438](https://github.com/vllm-project/vllm/pull/45438)
  [Bugfix][Core] Fall back when numactl --membind is blocked in constrained containers (#45438)
  _Files: `tests/utils_/test_numa_utils.py`, `vllm/utils/numa_utils.py`_
- **2026-06-16** [`3f1ff1ff14`](https://github.com/vllm-project/vllm/commit/3f1ff1ff14) [#45792](https://github.com/vllm-project/vllm/pull/45792)
  [Misc]Clean up useless test (#45792)
  _Files: `tests/test_seed_behavior.py`_
- **2026-06-16** [`c4fd9794e9`](https://github.com/vllm-project/vllm/commit/c4fd9794e9) [#45759](https://github.com/vllm-project/vllm/pull/45759)
  [Frontend] Remove AsyncMicrobatchTokenizer. (#45759)
  _Files: `vllm/renderers/base.py`, `vllm/utils/async_utils.py`_
- **2026-06-16** [`9096659edb`](https://github.com/vllm-project/vllm/commit/9096659edb) [#45777](https://github.com/vllm-project/vllm/pull/45777)
  [Cleanup] Remove dead env (#45777)
  _Files: `vllm/envs.py`_
- **2026-06-16** [`a9a8a32dcd`](https://github.com/vllm-project/vllm/commit/a9a8a32dcd) [#40299](https://github.com/vllm-project/vllm/pull/40299)
  Register parsed config classes before tokenizer init (#40299)
  _Files: `tests/tokenizers_/test_registry.py`, `vllm/tokenizers/registry.py`, `vllm/transformers_utils/config.py`_
- **2026-06-16** [`9d808e2309`](https://github.com/vllm-project/vllm/commit/9d808e2309) [#40183](https://github.com/vllm-project/vllm/pull/40183)
  [Core] Use fastsafetensors ParallelLoader for weight loading (#40183)
  _Files: `tests/model_executor/model_loader/fastsafetensors_loader/test_weight_utils.py`, `vllm/envs.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-06-16** [`259ff891be`](https://github.com/vllm-project/vllm/commit/259ff891be) [#45696](https://github.com/vllm-project/vllm/pull/45696)
  [Rust Frontend] Require `ModelConfig.vocab_size` to be present (#45696)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/text/src/backend/hf/config.rs`, `rust/src/text/src/backend/hf/mod.rs`, `rust/src/text/src/backend/mod.rs` _+4 more__
- **2026-06-15** [`3afe659b6b`](https://github.com/vllm-project/vllm/commit/3afe659b6b) [#45275](https://github.com/vllm-project/vllm/pull/45275)
  [EP] Enable DBO with NIXL EP (#45275)
  _Files: `vllm/config/compilation.py`, `vllm/config/vllm.py`_
- **2026-06-15** [`588db18362`](https://github.com/vllm-project/vllm/commit/588db18362) [#44409](https://github.com/vllm-project/vllm/pull/44409)
  [Bugfix] Two-phase KV allocation for cross-group prefix cache hits (supersedes #33775) (#44409)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-15** [`c17e2f7c84`](https://github.com/vllm-project/vllm/commit/c17e2f7c84) [#45465](https://github.com/vllm-project/vllm/pull/45465)
  [Bugfix][Rust Frontend] Make metrics respect --served-model-name (#45465)
  _Files: `rust/src/server/src/lib.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-15** [`ebb0a71ad0`](https://github.com/vllm-project/vllm/commit/ebb0a71ad0) [#44965](https://github.com/vllm-project/vllm/pull/44965)
  [Bugfix] Reject out-of-range temperature values in SamplingParams (#44965)
  _Files: `vllm/sampling_params.py`_

## Attention  (26 commits)

- **2026-06-22** [`3c8e49596c`](https://github.com/vllm-project/vllm/commit/3c8e49596c) [#46108](https://github.com/vllm-project/vllm/pull/46108)
  [Model] ColQwen3.5: fix retrieval correctness (bias + bidirectional) (#46108)
  _Files: `docs/models/pooling_models/token_embed.md`, `examples/pooling/score/colqwen3_5_rerank_online.py`, `tests/models/multimodal/pooling/test_colqwen3_5.py`, `vllm/model_executor/layers/attention/attention.py` _+3 more__
- **2026-06-22** [`cec2ec1176`](https://github.com/vllm-project/vllm/commit/cec2ec1176) [#45100](https://github.com/vllm-project/vllm/pull/45100)
  [Bugfix] Avoid racy accepted counts in async spec decode (#45100)
  _Files: `tests/v1/attention/test_gdn_metadata_builder.py`, `vllm/v1/attention/backends/gdn_attn.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-22** [`d14e551a53`](https://github.com/vllm-project/vllm/commit/d14e551a53) [#45993](https://github.com/vllm-project/vllm/pull/45993)
  [Model] Remove MiniMaxText01, MiniMaxVL01, MiniMaxForCausalLM (#45993)
  _Files: `docs/contributing/model/basic.md`, `docs/features/tool_calling.md`, `docs/models/supported_models.md`, `docs/usage/v1_guide.md` _+16 more__
- **2026-06-22** [`db32b53e30`](https://github.com/vllm-project/vllm/commit/db32b53e30) [#43081](https://github.com/vllm-project/vllm/pull/43081)
  [SpecDecode] Support DFlash with FlashInfer  (#43081)
  _Files: `docs/design/attention_backends.md`, `tests/kernels/attention/test_attention_selector.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-06-21** [`9c450b1027`](https://github.com/vllm-project/vllm/commit/9c450b1027) [#45361](https://github.com/vllm-project/vllm/pull/45361)
  [Kernel][Bugfix] Fix INT8 per-token-head KV cache rounding in Triton reshape-and-cache (#45361)
  _Files: `tests/quantization/test_per_token_kv_cache.py`, `vllm/v1/attention/ops/triton_reshape_and_cache_flash.py`_
- **2026-06-21** [`2cac89f9da`](https://github.com/vllm-project/vllm/commit/2cac89f9da) [#45181](https://github.com/vllm-project/vllm/pull/45181)
  [Spec Decode] Support mixed KV page sizes for DFlash (#45181)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/worker/test_attn_utils.py`, `vllm/v1/attention/backend.py`, `vllm/v1/core/kv_cache_utils.py` _+4 more__
- **2026-06-21** [`7df3d7dada`](https://github.com/vllm-project/vllm/commit/7df3d7dada) [#45424](https://github.com/vllm-project/vllm/pull/45424)
  [Core] Ensure memory is pinned prior to async h2d copy (#45424)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `tests/v1/streaming_input/test_gpu_model_runner_streaming.py`, `tests/v1/worker/test_gpu_input_batch.py`, `tests/v1/worker/test_gpu_model_runner.py` _+45 more__
- **2026-06-20** [`ebfbcfe46a`](https://github.com/vllm-project/vllm/commit/ebfbcfe46a) [#45026](https://github.com/vllm-project/vllm/pull/45026)
  Stop setting CUDA_VISIBLE_DEVICES internally in vLLM, add device_ids arg (#45026)
  _Files: `csrc/libtorch_stable/attention/mla/sm100_cutlass_mla_kernel.cu`, `tests/engine/test_arg_utils.py`, `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/config/parallel.py` _+20 more__
- **2026-06-18** [`79ca54d221`](https://github.com/vllm-project/vllm/commit/79ca54d221) [#45040](https://github.com/vllm-project/vllm/pull/45040)
  [Bugfix][Quantization] Don't reject fp8_e5m2 KV cache for non-fp8 quantized checkpoints (#45040)
  _Files: `vllm/model_executor/layers/attention/attention.py`_
- **2026-06-18** [`4583630b56`](https://github.com/vllm-project/vllm/commit/4583630b56) [#45466](https://github.com/vllm-project/vllm/pull/45466)
  [Bugfix][Kernel] Check output alignment in vectorize_with_alignment (fixes misaligned-address crash for non-multiple-of-8 head sizes) (#45466)
  _Files: `csrc/libtorch_stable/quantization/vectorization_utils.cuh`, `tests/kernels/attention/test_cache.py`_
- **2026-06-18** [`021cdf72bc`](https://github.com/vllm-project/vllm/commit/021cdf72bc) [#43179](https://github.com/vllm-project/vllm/pull/43179)
  Fix _riscv_supports_rvv_vlen128() to detect RVV on hardware without zvl flags (#43179)
  _Files: `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/torch_bindings.cpp`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-06-18** [`1797576237`](https://github.com/vllm-project/vllm/commit/1797576237) [#45309](https://github.com/vllm-project/vllm/pull/45309)
  Revert "[DSV4 Perf] Optimize dsv4 cudagraph by reducing `eager_break_during_capture`" (#45309) (#45972)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-06-17** [`5fd21eb0b2`](https://github.com/vllm-project/vllm/commit/5fd21eb0b2) [#45849](https://github.com/vllm-project/vllm/pull/45849)
  [BUG] fix hidden states nan for hybrid attention models (#45849)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-06-17** [`2a47a9ff0f`](https://github.com/vllm-project/vllm/commit/2a47a9ff0f) [#45309](https://github.com/vllm-project/vllm/pull/45309)
  [DSV4 Perf] Optimize dsv4 cudagraph by reducing `eager_break_during_capture`, 26.8% ~ 27.9% E2E TTFT improvement (#45309)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-06-17** [`5e27b2baf4`](https://github.com/vllm-project/vllm/commit/5e27b2baf4) [#45917](https://github.com/vllm-project/vllm/pull/45917)
  [Bugfix] Pass TP group to FlashInfer all-reduce fusion (#45917)
  _Files: `vllm/config/vllm.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-06-17** [`0a7bacdcac`](https://github.com/vllm-project/vllm/commit/0a7bacdcac) [#45863](https://github.com/vllm-project/vllm/pull/45863)
  [DSv4 Perf] DSv4 flashinfer sparse index cache for metadata, 2%~4% TTFT improvement (#45863)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-06-17** [`20a5f8b43b`](https://github.com/vllm-project/vllm/commit/20a5f8b43b) [#45232](https://github.com/vllm-project/vllm/pull/45232)
  [FlexAttention] make custom mask mods fully cudagraphable (#45232)
  _Files: `tests/kernels/test_flex_attention.py`, `vllm/v1/attention/backends/flex_attention.py`_
- **2026-06-17** [`556b063e45`](https://github.com/vllm-project/vllm/commit/556b063e45) [#44468](https://github.com/vllm-project/vllm/pull/44468)
  [XPU] Fix test_spec_decode_logprobs: use FLASH_ATTN for XPU in GPU_DETERMINISM_KWARGS (#44468)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `tests/v1/sample/test_logprobs.py`_
- **2026-06-16** [`9d4dc4ca2f`](https://github.com/vllm-project/vllm/commit/9d4dc4ca2f) [#43525](https://github.com/vllm-project/vllm/pull/43525)
  [Kernel] Support GLM-5 dimensions for TRT-LLM ragged MLA prefill (#43525)
  _Files: `docs/design/attention_backends.md`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_mla_prefill_registry.py`, `tests/v1/attention/test_mla_prefill_selector.py` _+6 more__
- **2026-06-16** [`a52205bccf`](https://github.com/vllm-project/vllm/commit/a52205bccf) [#43098](https://github.com/vllm-project/vllm/pull/43098)
  [Model] Add HrmTextForCausalLM (Hierarchical Reasoning Model — Text) (#43098)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/layers/attention/__init__.py`, `vllm/model_executor/layers/attention/prefill_prefix_lm_attention.py` _+4 more__
- **2026-06-16** [`b8bd773fe4`](https://github.com/vllm-project/vllm/commit/b8bd773fe4) [#45758](https://github.com/vllm-project/vllm/pull/45758)
  [XPU] Fix Triton attn fp8/bf16 check failing (#45758)
  _Files: `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_reshape_and_cache_flash.py`_
- **2026-06-16** [`f4359a70f9`](https://github.com/vllm-project/vllm/commit/f4359a70f9) [#44892](https://github.com/vllm-project/vllm/pull/44892)
  [DSV4][Minor] Fix supported KV cache dtypes (#44892)
  _Files: `docs/design/attention_backends.md`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`, `vllm/models/deepseek_v4/sparse_mla.py`_
- **2026-06-15** [`e18fe932ca`](https://github.com/vllm-project/vllm/commit/e18fe932ca) [#45061](https://github.com/vllm-project/vllm/pull/45061)
  [Perf] Optimize DSv4 prefill chunk planning, 4.0% E2E Throughput Improvement (#45061)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/nvidia/flashmla.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-06-15** [`fa63bb9db6`](https://github.com/vllm-project/vllm/commit/fa63bb9db6) [#43914](https://github.com/vllm-project/vllm/pull/43914)
  Remove redundant Triton KV cache dtype asserts and enforce architectural support (fp8 >= sm89) (#43914)
  _Files: `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_reshape_and_cache_flash.py`_
- **2026-06-15** [`b8336c3c7c`](https://github.com/vllm-project/vllm/commit/b8336c3c7c) [#45564](https://github.com/vllm-project/vllm/pull/45564)
  [Bugfix][V1] Split V2 model-runner attention groups on num_heads_q (#45564)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-06-15** [`8760f972ca`](https://github.com/vllm-project/vllm/commit/8760f972ca) [#45391](https://github.com/vllm-project/vllm/pull/45391)
  [CPU] Refine CPU attention frontend (#45391)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `csrc/cpu/generate_cpu_attn_dispatch.py`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`_

## Scheduler / Engine  (26 commits)

- **2026-06-22** [`80abe0de7d`](https://github.com/vllm-project/vllm/commit/80abe0de7d) [#46137](https://github.com/vllm-project/vllm/pull/46137)
  [Rust Frontend] Support thinking_token_budget for chat and completions (#46137)
  _Files: `rust/src/engine-core-client/src/protocol/mod.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`, `rust/src/server/src/error.rs` _+9 more__
- **2026-06-22** [`1eb2cc961e`](https://github.com/vllm-project/vllm/commit/1eb2cc961e) [#46022](https://github.com/vllm-project/vllm/pull/46022)
  [Frontend] Refactor ServingTokenization entrypoint. (#46022)
  _Files: `tests/entrypoints/serve/tokenize/test_serving_tokenization.py`, `vllm/entrypoints/anthropic/api_router.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/engine/serving.py` _+11 more__
- **2026-06-20** [`6e919960af`](https://github.com/vllm-project/vllm/commit/6e919960af) [#45840](https://github.com/vllm-project/vllm/pull/45840)
  [Perf] Skip/shrink all_token_ids copy in scheduler for non-async and V2 runner (#45840)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/output.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-06-20** [`c88d3d4775`](https://github.com/vllm-project/vllm/commit/c88d3d4775) [#39831](https://github.com/vllm-project/vllm/pull/39831)
  [SimpleCPUOffloadConnector] PCP + DCP support (#39831)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-06-20** [`7ff7f5c8eb`](https://github.com/vllm-project/vllm/commit/7ff7f5c8eb) [#46125](https://github.com/vllm-project/vllm/pull/46125)
  Revert "Fix Stale Encoder Cache After Weight Update" (#46125)
  _Files: `vllm/entrypoints/llm.py`, `vllm/v1/engine/async_llm.py`_
- **2026-06-19** [`859e4d436b`](https://github.com/vllm-project/vllm/commit/859e4d436b) [#46159](https://github.com/vllm-project/vllm/pull/46159)
  [Bugfix][Parser] Fix U+FFFD leak at reasoning-to-content transition in engine parsers (#46159)
  _Files: `tests/parser/engine/replay_harness.py`, `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_ufffd_reasoning_transition.py`, `vllm/parser/abstract_parser.py` _+1 more__
- **2026-06-18** [`7f616c327d`](https://github.com/vllm-project/vllm/commit/7f616c327d) [#46091](https://github.com/vllm-project/vllm/pull/46091)
  [Bugfix] [Parser] Fix empty tool block silently dropping subsequent content (#46091)
  _Files: `tests/parser/engine/trace_builder.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/gemma4.py`, `vllm/parser/qwen3.py`_
- **2026-06-18** [`09f3cd5c10`](https://github.com/vllm-project/vllm/commit/09f3cd5c10) [#46047](https://github.com/vllm-project/vllm/pull/46047)
  [Bugfix] [Parser] Fix Qwen3 latent bug in partial params dropping values containing `<` (#46047)
  _Files: `tests/parser/engine/test_qwen3.py`, `vllm/parser/qwen3.py`_
- **2026-06-18** [`4cb5e746b6`](https://github.com/vllm-project/vllm/commit/4cb5e746b6) [#44801](https://github.com/vllm-project/vllm/pull/44801)
  [Rust Frontend]: Add `/get_world_size` route with static parallel size (#44801)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/test_utils.rs` _+7 more__
- **2026-06-18** [`08985351f3`](https://github.com/vllm-project/vllm/commit/08985351f3) [#45093](https://github.com/vllm-project/vllm/pull/45093)
  Fix Stale Encoder Cache After Weight Update (#45093)
  _Files: `vllm/entrypoints/llm.py`, `vllm/v1/engine/async_llm.py`_
- **2026-06-18** [`554352a311`](https://github.com/vllm-project/vllm/commit/554352a311) [#45679](https://github.com/vllm-project/vllm/pull/45679)
  [Test][KV Connector] Add request_finished fence population tests for offloading scheduler (#45679)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`_
- **2026-06-17** [`9d4b87f4f0`](https://github.com/vllm-project/vllm/commit/9d4b87f4f0) [#45196](https://github.com/vllm-project/vllm/pull/45196)
  [Bugfix][Model] Validate DefaultModelLoader / LoadConfig and fail with clear errors (#45196)
  _Files: `tests/model_executor/model_loader/test_registry.py`, `tests/test_config.py`, `vllm/config/load.py`, `vllm/engine/arg_utils.py` _+1 more__
- **2026-06-17** [`e2c58570ea`](https://github.com/vllm-project/vllm/commit/e2c58570ea) [#45805](https://github.com/vllm-project/vllm/pull/45805)
  [Rust Frontend] Support hybrid/external DP LB in Python supervised bootstrap (#45805)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/engine-core-client/src/client.rs` _+4 more__
- **2026-06-17** [`17bc144556`](https://github.com/vllm-project/vllm/commit/17bc144556) [#45848](https://github.com/vllm-project/vllm/pull/45848)
  [Rust Frontend] Add serde defaults for omit_defaults fields in `EngineCoreSamplingParams` (#45848)
  _Files: `rust/src/engine-core-client/src/protocol/mod.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`_
- **2026-06-17** [`e9993a52aa`](https://github.com/vllm-project/vllm/commit/e9993a52aa) [#45897](https://github.com/vllm-project/vllm/pull/45897)
  [BugFix][CI] Fix scheduler plugin test (#45897)
  _Files: `tests/plugins_tests/test_scheduler_plugins.py`_
- **2026-06-17** [`7b5d60cc37`](https://github.com/vllm-project/vllm/commit/7b5d60cc37) [#45195](https://github.com/vllm-project/vllm/pull/45195)
  [Bugfix][V1] Clean up compiled-model bytecode hooks on VllmRunner exit (#45195)
  _Files: `tests/conftest.py`, `tests/v1/shutdown/test_delete.py`, `vllm/compilation/wrapper.py`, `vllm/v1/engine/llm_engine.py`_
- **2026-06-16** [`b9684d99e9`](https://github.com/vllm-project/vllm/commit/b9684d99e9) [#45795](https://github.com/vllm-project/vllm/pull/45795)
  [Bugfix] Gemma4: skip forced JSON for required/named tool choice (#45795)
  _Files: `tests/tool_use/test_gemma4_responses_adjust_request.py`, `vllm/tool_parsers/gemma4_engine_tool_parser.py`_
- **2026-06-16** [`d8d95998dc`](https://github.com/vllm-project/vllm/commit/d8d95998dc) [#44558](https://github.com/vllm-project/vllm/pull/44558)
  [Core] Add prefill step cadence for better non-PD DP balancing (#44558)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/distributed/test_async_llm_dp.py`, `vllm/config/scheduler.py`, `vllm/engine/arg_utils.py` _+3 more__
- **2026-06-16** [`7d567172fc`](https://github.com/vllm-project/vllm/commit/7d567172fc) [#45763](https://github.com/vllm-project/vllm/pull/45763)
  [Bugfix] Fix Qwen3 prompt tool-call reasoning false positive (#45763)
  _Files: `tests/parser/engine/test_qwen3_reasoning.py`, `vllm/parser/qwen3.py`_
- **2026-06-16** [`cca3365b73`](https://github.com/vllm-project/vllm/commit/cca3365b73) [#45753](https://github.com/vllm-project/vllm/pull/45753)
  [Rust Frontend] Add CORS support (#45753)
  _Files: `rust/Cargo.toml`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs` _+8 more__
- **2026-06-16** [`b2cfae777d`](https://github.com/vllm-project/vllm/commit/b2cfae777d) [#45631](https://github.com/vllm-project/vllm/pull/45631)
  Add Triton recompile detection (#45631)
  _Files: `tests/engine/test_arg_utils.py`, `tests/test_jit_monitor.py`, `vllm/config/observability.py`, `vllm/engine/arg_utils.py` _+2 more__
- **2026-06-16** [`3f65e21e32`](https://github.com/vllm-project/vllm/commit/3f65e21e32) [#45674](https://github.com/vllm-project/vllm/pull/45674)
  [Rust Frontend] Support `max_logprobs` validation (#45674)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/managed-engine/src/cli.rs` _+11 more__
- **2026-06-15** [`d467a2a7f2`](https://github.com/vllm-project/vllm/commit/d467a2a7f2) [#45357](https://github.com/vllm-project/vllm/pull/45357)
  [Bugfix] Defer block freeing until in-flight steps finish under async scheduling + PD KV consumer (#45357)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_deferred_block_free.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` _+5 more__
- **2026-06-15** [`cd9078fe59`](https://github.com/vllm-project/vllm/commit/cd9078fe59) [#45600](https://github.com/vllm-project/vllm/pull/45600)
  [Frontend] Skip structural tags for auto tool_choice without strict mode (#45600)
  _Files: `docs/features/tool_calling.md`, `tests/tool_parsers/test_deepseekv4_tool_parser.py`, `tests/tool_parsers/test_qwen3coder_tool_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py` _+4 more__
- **2026-06-15** [`64833f8158`](https://github.com/vllm-project/vllm/commit/64833f8158) [#45137](https://github.com/vllm-project/vllm/pull/45137)
  [Rust Frontend] Add external→internal request-id map for abort() (#45137)
  _Files: `rust/Cargo.lock`, `rust/src/chat/src/lib.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+9 more__
- **2026-06-15** [`ddad5dbda2`](https://github.com/vllm-project/vllm/commit/ddad5dbda2) [#45557](https://github.com/vllm-project/vllm/pull/45557)
  [Bugfix][Rust] Sync EngineCoreReadyResponse with the Python dataclass (#45557)
  _Files: `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`_

## Models  (20 commits)

- **2026-06-22** [`435f82d61a`](https://github.com/vllm-project/vllm/commit/435f82d61a) [#46341](https://github.com/vllm-project/vllm/pull/46341)
  [Bugfix] Fix Llama4ForCausalLM initialization test failure (#46341)
  _Files: `tests/models/utils.py`_
- **2026-06-21** [`745bba5ea8`](https://github.com/vllm-project/vllm/commit/745bba5ea8) [#45935](https://github.com/vllm-project/vllm/pull/45935)
  [Model]Fix MiniMaxM2ForCausalLM perf  regression (#45935)
  _Files: `tests/kernels/core/test_minimax_reduce_rms.py`, `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`_
- **2026-06-20** [`77148992cf`](https://github.com/vllm-project/vllm/commit/77148992cf) [#46199](https://github.com/vllm-project/vllm/pull/46199)
  [Bugfix] Move extract_layer_index back inside is_v32 guard (#46199)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-19** [`560fb8b867`](https://github.com/vllm-project/vllm/commit/560fb8b867) [#46099](https://github.com/vllm-project/vllm/pull/46099)
  [Cohere] Remove dead prepare_structured_tag override in Cohere parser  (#46099)
  _Files: `vllm/reasoning/cohere_command_reasoning_parser.py`_
- **2026-06-18** [`c3c6d723fd`](https://github.com/vllm-project/vllm/commit/c3c6d723fd) [#45988](https://github.com/vllm-project/vllm/pull/45988)
  [Perf] Remove unused loggers in `reasoning/` (#45988)
  _Files: `vllm/reasoning/deepseek_v3_reasoning_parser.py`, `vllm/reasoning/ernie45_reasoning_parser.py`, `vllm/reasoning/granite_reasoning_parser.py`, `vllm/reasoning/hunyuan_a13b_reasoning_parser.py` _+5 more__
- **2026-06-18** [`a0df04e477`](https://github.com/vllm-project/vllm/commit/a0df04e477) [#45708](https://github.com/vllm-project/vllm/pull/45708)
  [Tests] Add Qwen3 streaming parser delta boundary cases (#45708)
  _Files: `tests/tool_parsers/test_qwen3coder_tool_parser.py`_
- **2026-06-18** [`d682968aa9`](https://github.com/vllm-project/vllm/commit/d682968aa9) [#45990](https://github.com/vllm-project/vllm/pull/45990)
  [Model] Remove BambaForCausalLM (#45990)
  _Files: `docs/models/supported_models.md`, `tests/models/language/generation/test_hybrid.py`, `tests/models/registry.py`, `vllm/model_executor/models/bamba.py` _+1 more__
- **2026-06-18** [`e1a5fc406b`](https://github.com/vllm-project/vllm/commit/e1a5fc406b) [#45826](https://github.com/vllm-project/vllm/pull/45826)
  [Rust Frontend][Perf] O(n) argument scan in tool parser (#45826)
  _Files: `rust/src/tool-parser/benches/qwen3_coder.rs`, `rust/src/tool-parser/src/deepseek_dsml/mod.rs`, `rust/src/tool-parser/src/glm_xml/mod.rs`, `rust/src/tool-parser/src/hy_v3.rs` _+4 more__
- **2026-06-17** [`58b2e89642`](https://github.com/vllm-project/vllm/commit/58b2e89642) [#45867](https://github.com/vllm-project/vllm/pull/45867)
  [Bugfix][Gemma4] Render reasoning on assistant turns without tool_calls (#45867)
  _Files: `examples/tool_chat_template_gemma4.jinja`_
- **2026-06-17** [`68ff30d40e`](https://github.com/vllm-project/vllm/commit/68ff30d40e) [#42332](https://github.com/vllm-project/vllm/pull/42332)
  [Bugfix] Fixes MiniCPM-O resampler device placement to avoid tensor device mismatch (#42332)
  _Files: `vllm/model_executor/models/minicpmo.py`_
- **2026-06-17** [`43fa24e832`](https://github.com/vllm-project/vllm/commit/43fa24e832) [#45873](https://github.com/vllm-project/vllm/pull/45873)
  [Misc] Validate Cohere Embed Mixed Content Payloads (#45873)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/entrypoints/pooling/embed/protocol.py`_
- **2026-06-17** [`b831374cf1`](https://github.com/vllm-project/vllm/commit/b831374cf1) [#45832](https://github.com/vllm-project/vllm/pull/45832)
  [Bugfix][Gemma4] Fix parsing when thinking is disabled (#45832)
  _Files: `tests/tool_use/test_gemma4_responses_adjust_request.py`, `vllm/parser/gemma4.py`_
- **2026-06-16** [`89e8645a9e`](https://github.com/vllm-project/vllm/commit/89e8645a9e) [#45637](https://github.com/vllm-project/vllm/pull/45637)
  [Model] Remove Dots1ForCausalLM (#45637)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/dots1.py`, `vllm/model_executor/models/registry.py`_
- **2026-06-16** [`81d8f4ebac`](https://github.com/vllm-project/vllm/commit/81d8f4ebac) [#45640](https://github.com/vllm-project/vllm/pull/45640)
  [Misc] Added validation for Cohere /v2/embed input field exclusivity (#45640)
  _Files: `tests/entrypoints/pooling/embed/test_io_processor.py`, `vllm/entrypoints/pooling/embed/protocol.py`_
- **2026-06-16** [`6607a80dab`](https://github.com/vllm-project/vllm/commit/6607a80dab) [#45553](https://github.com/vllm-project/vllm/pull/45553)
  [Bugfix][Gemma4] Fix offline parser truncation, adjust_request token leak, and chat template sync (#45553)
  _Files: `examples/tool_chat_template_gemma4.jinja`, `tests/reasoning/test_gemma4_reasoning_parser.py`, `tests/renderers/test_gemma4_chat_template.py`, `vllm/parser/gemma4.py` _+1 more__
- **2026-06-15** [`0a1c5034f5`](https://github.com/vllm-project/vllm/commit/0a1c5034f5) [#45381](https://github.com/vllm-project/vllm/pull/45381)
  [Model] Add MiniMax M3 support (#45381)
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

## MoE / Expert Parallel  (19 commits)

- **2026-06-22** [`9037498c22`](https://github.com/vllm-project/vllm/commit/9037498c22) [#44517](https://github.com/vllm-project/vllm/pull/44517)
  [DSV4][XPU] Pass gemm1_clamp_limit to XpuFusedMoe (#44517)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-06-22** [`485bbe1c6f`](https://github.com/vllm-project/vllm/commit/485bbe1c6f) [#46163](https://github.com/vllm-project/vllm/pull/46163)
  [CI] Fix missing `tp_size` attribute on `RoutedExperts` (#46163)
  _Files: `vllm/model_executor/layers/quantization/moe_wna16.py`_
- **2026-06-21** [`a346d589f5`](https://github.com/vllm-project/vllm/commit/a346d589f5) [#46254](https://github.com/vllm-project/vllm/pull/46254)
  [Bugfix] Fix NVFP4/OCP MX MoE emulation (#46254)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+1 more__
- **2026-06-19** [`b9a7cd464c`](https://github.com/vllm-project/vllm/commit/b9a7cd464c) [#45415](https://github.com/vllm-project/vllm/pull/45415)
  [12/n]  final _C library kernel migration (#45415)
  _Files: `CMakeLists.txt`, `cmake/external_projects/qutlass.cmake`, `csrc/libtorch_stable/core/math.hpp`, `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu` _+13 more__
- **2026-06-19** [`9ea3a4015b`](https://github.com/vllm-project/vllm/commit/9ea3a4015b) [#42120](https://github.com/vllm-project/vllm/pull/42120)
  [Bugfix] Fix corrupt outputs in MoE FP8 LoRA responses and MoE base model responses when LoRAs are loaded (#42120)
  _Files: `tests/lora/test_punica_ops.py`, `vllm/lora/punica_wrapper/punica_gpu.py`, `vllm/model_executor/layers/fused_moe/experts/lora_context.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+1 more__
- **2026-06-18** [`6c379b9e54`](https://github.com/vllm-project/vllm/commit/6c379b9e54) [#45915](https://github.com/vllm-project/vllm/pull/45915)
  [Frontend] Add Streaming Parser Engine and new GLM4.7/GLM5.1/GLM5.2 Parser (#45915)
  _Files: `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_glm4_moe_reasoning_parser.py`, `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `tests/tool_parsers/test_glm4_moe_tool_parser.py` _+7 more__
- **2026-06-18** [`058cc0a8b6`](https://github.com/vllm-project/vllm/commit/058cc0a8b6) [#45656](https://github.com/vllm-project/vllm/pull/45656)
  [Bugfix] Restore is_sym guard for zp in GPTQ/CT MoE to fix symmetric quant regression (#45656)
  _Files: `vllm/model_executor/layers/quantization/auto_gptq.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16_marlin.py`_
- **2026-06-18** [`b4c80ec0fd`](https://github.com/vllm-project/vllm/commit/b4c80ec0fd) [#44681](https://github.com/vllm-project/vllm/pull/44681)
  [Refactor] Remove dead cutlass mxfp8 code (#44681)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/moe/mxfp8_moe/cutlass_mxfp8_grouped_mm.cu`, `csrc/libtorch_stable/moe/mxfp8_moe/cutlass_mxfp8_grouped_mm_functor.cuh`, `csrc/libtorch_stable/moe/mxfp8_moe/cutlass_mxfp8_grouped_mm_launcher.cuh` _+6 more__
- **2026-06-17** [`9c7c74bf10`](https://github.com/vllm-project/vllm/commit/9c7c74bf10) [#45857](https://github.com/vllm-project/vllm/pull/45857)
  [Log] Update deepgemm log (#45857)
  _Files: `tests/kernels/moe/modular_kernel_tools/common.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/utils/deep_gemm.py`_
- **2026-06-17** [`8b2b566ea7`](https://github.com/vllm-project/vllm/commit/8b2b566ea7) [#43853](https://github.com/vllm-project/vllm/pull/43853)
  Feature: Enable Flashinfer non-gated MoE bf16 (#43853)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-06-17** [`5bdc01bcc3`](https://github.com/vllm-project/vllm/commit/5bdc01bcc3) [#45743](https://github.com/vllm-project/vllm/pull/45743)
  [M3] Tune Triton indexer score decode for spec-decode (#45743)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/index_topk.py`_
- **2026-06-17** [`71bc19dbdd`](https://github.com/vllm-project/vllm/commit/71bc19dbdd) [#45589](https://github.com/vllm-project/vllm/pull/45589)
  [Bugfix] Fix MoE model load OOM in FlashInfer_TRTLLM  backend with sleep mode (#45589)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-06-16** [`88a9cdd439`](https://github.com/vllm-project/vllm/commit/88a9cdd439) [#45461](https://github.com/vllm-project/vllm/pull/45461)
  [Model Runner V2] Enable GraniteMOE for MRv2 by default (#45461)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-06-16** [`bf5149b516`](https://github.com/vllm-project/vllm/commit/bf5149b516) [#36616](https://github.com/vllm-project/vllm/pull/36616)
  [Bugfix] Fix FlashMLA sparse accuracy with topk_length and zero-init padding (#36616)
  _Files: `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-06-16** [`c5e5c33fcd`](https://github.com/vllm-project/vllm/commit/c5e5c33fcd) [#45707](https://github.com/vllm-project/vllm/pull/45707)
  [Bugfix][MoE] Restore routed output unpadding before shared expert add (#45707)
  _Files: `tests/quantization/test_blackwell_moe.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`_
- **2026-06-16** [`a7fdfeef72`](https://github.com/vllm-project/vllm/commit/a7fdfeef72) [#45690](https://github.com/vllm-project/vllm/pull/45690)
  [CPU] Support Gemma Diffusion (#45690)
  _Files: `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/cpu_attn_impl.hpp`, `csrc/cpu/cpu_fused_moe.cpp`, `csrc/cpu/torch_bindings.cpp` _+3 more__
- **2026-06-15** [`16e91176cf`](https://github.com/vllm-project/vllm/commit/16e91176cf) [#45298](https://github.com/vllm-project/vllm/pull/45298)
  [EP] Query NIXL EP top-k index dtype (#45298)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/nixl_ep.py`_
- **2026-06-15** [`ab8b0fe338`](https://github.com/vllm-project/vllm/commit/ab8b0fe338) [#45606](https://github.com/vllm-project/vllm/pull/45606)
  nixl_ep: Skip post-receive quantization for NVFP4 (#45606)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/nixl_ep.py`_
- **2026-06-15** [`5ed15f42b9`](https://github.com/vllm-project/vllm/commit/5ed15f42b9) [#43557](https://github.com/vllm-project/vllm/pull/43557)
  Fix the E8M0 scale computation in the MXFP4 (W4A4) MOE CUTLASS kernel (#43557)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_utils.cuh`, `tests/kernels/moe/test_mxfp4_moe.py`, `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`_

## Quantization  (16 commits)

- **2026-06-20** [`93bad11912`](https://github.com/vllm-project/vllm/commit/93bad11912) [#45255](https://github.com/vllm-project/vllm/pull/45255)
  [Bugfix] Fix gridDim.y overflow for large row counts (#45255)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `tests/kernels/quantization/test_per_token_group_quant.py`_
- **2026-06-19** [`2a6c6b9429`](https://github.com/vllm-project/vllm/commit/2a6c6b9429) [#46001](https://github.com/vllm-project/vllm/pull/46001)
  [DeepSeek-V4] Support TEP=16 for the block-FP8 shared expert (#46001)
  _Files: `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-06-18** [`225936a1dd`](https://github.com/vllm-project/vllm/commit/225936a1dd) [#46070](https://github.com/vllm-project/vllm/pull/46070)
  [CI Bug] Revert #42379 to fix CI `Multi-Modal Models (Extended Generation 1)` (#46070)
  _Files: `csrc/libtorch_stable/layernorm_kernels.cu`, `csrc/libtorch_stable/layernorm_quant_kernels.cu`_
- **2026-06-18** [`b53b1c7ffe`](https://github.com/vllm-project/vllm/commit/b53b1c7ffe) [#44446](https://github.com/vllm-project/vllm/pull/44446)
  [Model Runner V2] Migration to support quantized model by default [5/N] (#44446)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-06-18** [`22cc891108`](https://github.com/vllm-project/vllm/commit/22cc891108) [#46006](https://github.com/vllm-project/vllm/pull/46006)
  [Kernel] Add PDL support for DeepGEMM kernel (#46006)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/utils/deep_gemm.py`_
- **2026-06-18** [`e945169207`](https://github.com/vllm-project/vllm/commit/e945169207) [#45999](https://github.com/vllm-project/vllm/pull/45999)
  Revert "[Kernel] Add PDL support for DeepGEMM kernel" (#45999)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/utils/deep_gemm.py`_
- **2026-06-18** [`4403af8fb5`](https://github.com/vllm-project/vllm/commit/4403af8fb5) [#42996](https://github.com/vllm-project/vllm/pull/42996)
  [Kernel] Add PDL support for DeepGEMM kernel (#42996)
  _Files: `csrc/libtorch_stable/quantization/w8a8/fp8/per_token_group_quant.cu`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/utils/deep_gemm.py`_
- **2026-06-18** [`8dd8b6ed78`](https://github.com/vllm-project/vllm/commit/8dd8b6ed78) [#43958](https://github.com/vllm-project/vllm/pull/43958)
  [XPU] Fix FP8 block-scaled scheme selection on non-CUDA platforms (#43958)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-06-17** [`2659f60a1a`](https://github.com/vllm-project/vllm/commit/2659f60a1a) [#45454](https://github.com/vllm-project/vllm/pull/45454)
  [Refactor] Remove dead quantization code and tests (#45454)
  _Files: `tests/kernels/quantization/test_awq.py`, `tests/quantization/fp_quant.py`, `tests/quantization/test_fp8.py`, `vllm/model_executor/layers/quantization/__init__.py` _+1 more__
- **2026-06-17** [`46f74e144b`](https://github.com/vllm-project/vllm/commit/46f74e144b) [#34432](https://github.com/vllm-project/vllm/pull/34432)
  [Kernel][Helion][1/N] Add Helion kernel for rms_norm_dynamic_per_token_quant (#34432)
  _Files: `tests/kernels/helion/test_rms_norm_dynamic_per_token_quant.py`, `vllm/kernels/helion/configs/rms_norm_dynamic_per_token_quant/nvidia_b200.json`, `vllm/kernels/helion/configs/rms_norm_dynamic_per_token_quant/nvidia_h100.json`, `vllm/kernels/helion/ops/rms_norm_dynamic_per_token_quant.py`_
- **2026-06-17** [`bcb518ad7a`](https://github.com/vllm-project/vllm/commit/bcb518ad7a) [#40601](https://github.com/vllm-project/vllm/pull/40601)
  [quant][autoround]Refactor INC quantization into package with INCScheme orchestrator (#40601)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc.py` _+9 more__
- **2026-06-16** [`ce3ef17bec`](https://github.com/vllm-project/vllm/commit/ce3ef17bec) [#36895](https://github.com/vllm-project/vllm/pull/36895)
  [Kernel][Helion][1/N] Add Helion kernel for rms_norm_per_block_quant (#36895)
  _Files: `tests/kernels/helion/test_rms_norm_per_block_quant.py`, `vllm/kernels/helion/configs/rms_norm_per_block_quant/nvidia_b200.json`, `vllm/kernels/helion/configs/rms_norm_per_block_quant/nvidia_h100.json`, `vllm/kernels/helion/ops/rms_norm_per_block_quant.py` _+1 more__
- **2026-06-16** [`a8c86eeb16`](https://github.com/vllm-project/vllm/commit/a8c86eeb16) [#45306](https://github.com/vllm-project/vllm/pull/45306)
  [Quant] Support modelopt_mixed on Ampere (SM80/SM86) (#45306)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-06-16** [`405c7cf283`](https://github.com/vllm-project/vllm/commit/405c7cf283) [#42726](https://github.com/vllm-project/vllm/pull/42726)
  [ZenCPU] Add zencpu Platform Runtime Logging and Docs (#42726)
  _Files: `docs/getting_started/installation/cpu.md`, `docs/getting_started/installation/cpu.x86.inc.md`, `docs/models/hardware_supported_models/cpu.md`, `tests/model_executor/test_cpu_unquantized_gemm_dispatch.py` _+2 more__
- **2026-06-16** [`3f53e2138f`](https://github.com/vllm-project/vllm/commit/3f53e2138f) [#45463](https://github.com/vllm-project/vllm/pull/45463)
  [Refactor] Remove `Fp8OnlineLinearMethod` as scheduled (#45463)
  _Files: `docs/training/layerwise.md`, `tests/quantization/test_fp8.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/online/fp8.py` _+1 more__
- **2026-06-15** [`b5adb027ad`](https://github.com/vllm-project/vllm/commit/b5adb027ad) [#45200](https://github.com/vllm-project/vllm/pull/45200)
  [Models] Fix MiMo v2.x QKV TP sharding + FP4 support (#45200)
  _Files: `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/models/mimo_v2.py`_

## Serving / API  (15 commits)

- **2026-06-21** [`3e6e33526d`](https://github.com/vllm-project/vllm/commit/3e6e33526d) [#44638](https://github.com/vllm-project/vllm/pull/44638)
  [Disagg] return routed_experts on streaming generate responses (#44638)
  _Files: `vllm/entrypoints/serve/disagg/protocol.py`, `vllm/entrypoints/serve/disagg/serving.py`_
- **2026-06-20** [`f57ac274b2`](https://github.com/vllm-project/vllm/commit/f57ac274b2) [#45919](https://github.com/vllm-project/vllm/pull/45919)
  [Render] Add reasoning/tool parsing to /derender + fix byte-fallback FFFD (#45919)
  _Files: `tests/entrypoints/serve/render/test_derender.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/serve/disagg/protocol.py`, `vllm/entrypoints/serve/render/serving.py`_
- **2026-06-20** [`891cc4b9c5`](https://github.com/vllm-project/vllm/commit/891cc4b9c5) [#40912](https://github.com/vllm-project/vllm/pull/40912)
  [Frontend] Report cache usage in Anthropic /v1/messages API (#40912)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-19** [`69bdd34542`](https://github.com/vllm-project/vllm/commit/69bdd34542) [#46038](https://github.com/vllm-project/vllm/pull/46038)
  [Bugfix] Fall back to Pydantic loc for param in validation errors (#46038)
  _Files: `tests/entrypoints/serve/utils/test_server_utils.py`, `vllm/entrypoints/serve/utils/server_utils.py`_
- **2026-06-18** [`4ce2d01453`](https://github.com/vllm-project/vllm/commit/4ce2d01453) [#46025](https://github.com/vllm-project/vllm/pull/46025)
  fix(anthropic): auto-detect template support for mid-conversation system messages (#46025)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-18** [`702214146c`](https://github.com/vllm-project/vllm/commit/702214146c) [#44725](https://github.com/vllm-project/vllm/pull/44725)
  [Bugfix][Frontend] Fix Anthropic count_tokens decorator order driving server load negative (#44725)
  _Files: `vllm/entrypoints/anthropic/api_router.py`_
- **2026-06-17** [`56e4345226`](https://github.com/vllm-project/vllm/commit/56e4345226) [#44938](https://github.com/vllm-project/vllm/pull/44938)
  [Rust Frontend] Support prompt-only completions (#44938)
  _Files: `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/openai/completions/validate.rs`_
- **2026-06-16** [`f99260d2aa`](https://github.com/vllm-project/vllm/commit/f99260d2aa) [#45685](https://github.com/vllm-project/vllm/pull/45685)
  [Rust Frontend] Lower out-of-vocab validation to `text` layer (#45685)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs`, `rust/src/server/src/routes/openai/completions.rs` _+10 more__
- **2026-06-15** [`25ee659db0`](https://github.com/vllm-project/vllm/commit/25ee659db0) [#44955](https://github.com/vllm-project/vllm/pull/44955)
  Fix parallel_tool_calls: null treated as false instead of default true (#44955)
  _Files: `vllm/entrypoints/serve/utils/tool_calls_utils.py`_
- **2026-06-15** [`51ec5cf08f`](https://github.com/vllm-project/vllm/commit/51ec5cf08f) [#45464](https://github.com/vllm-project/vllm/pull/45464)
  [Bugfix] Chat Completions Harmony Refactor Clean up (#45464)
  _Files: `tests/parser/test_harmony.py`, `vllm/entrypoints/serve/render/serving.py`, `vllm/parser/harmony.py`_
- **2026-06-15** [`0d80979644`](https://github.com/vllm-project/vllm/commit/0d80979644) [#45548](https://github.com/vllm-project/vllm/pull/45548)
  [Chore] Consolidate reasoning/tool parser attributes into unified Parser in chat serving (#45548)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/chat_completion/serving.py`_
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

## CI / Build  (14 commits)

- **2026-06-22** [`09cdcf34aa`](https://github.com/vllm-project/vllm/commit/09cdcf34aa) [#46327](https://github.com/vllm-project/vllm/pull/46327)
  [XPU] update nixl to v1.2.0 (#46327)
  _Files: `docker/Dockerfile.xpu`_
- **2026-06-22** [`b5a2adec4b`](https://github.com/vllm-project/vllm/commit/b5a2adec4b) [#46356](https://github.com/vllm-project/vllm/pull/46356)
  [XPU][CI]Skip v1/spec_decode/test_speculators_correctness.py in intel GPU nightly (#46356)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-06-21** [`b80ce9dd2f`](https://github.com/vllm-project/vllm/commit/b80ce9dd2f) [#46241](https://github.com/vllm-project/vllm/pull/46241)
  [CI][test] Replace InternVL2-1B with InternVL3-1B in test_pipeline_parallel.py (#46241)
  _Files: `tests/distributed/test_pipeline_parallel.py`_
- **2026-06-19** [`ca7e1f2c43`](https://github.com/vllm-project/vllm/commit/ca7e1f2c43) [#45975](https://github.com/vllm-project/vllm/pull/45975)
  Move CI failure diagnosis docs into ci-fails-buildkite skill (#45975)
  _Files: `.claude/skills/ci-fails-buildkite/SKILL.md`, `.github/CODEOWNERS`, `.gitignore`, `AGENTS.md`_
- **2026-06-19** [`ec67d7ae61`](https://github.com/vllm-project/vllm/commit/ec67d7ae61) [#40367](https://github.com/vllm-project/vllm/pull/40367)
  [xpu] bump up vllm-xpu-kernels v0.1.10 and upgrade 2618 umd (#40367)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docker/Dockerfile.xpu`, `docs/getting_started/installation/gpu.xpu.inc.md`, `requirements/xpu.txt`_
- **2026-06-18** [`a331589394`](https://github.com/vllm-project/vllm/commit/a331589394) [#40287](https://github.com/vllm-project/vllm/pull/40287)
  [XPU] Update nixl to v0.10.1 in Dockerfile (#40287)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docker/Dockerfile.xpu`_
- **2026-06-18** [`2959a9273a`](https://github.com/vllm-project/vllm/commit/2959a9273a) [#44650](https://github.com/vllm-project/vllm/pull/44650)
  [XPU][CI] add model runner v2 into CI (#44650)
  _Files: `.buildkite/intel_jobs/model_runner_v2_intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-test.sh`_
- **2026-06-17** [`06e1e0885c`](https://github.com/vllm-project/vllm/commit/06e1e0885c) [#44469](https://github.com/vllm-project/vllm/pull/44469)
  [XPU] Fix test_logprobs_e2e import error: pin lm-eval[api]>=0.4.12 (#44469)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `requirements/test/xpu.in`, `requirements/test/xpu.txt`_
- **2026-06-17** [`d78650cf97`](https://github.com/vllm-project/vllm/commit/d78650cf97) [#45843](https://github.com/vllm-project/vllm/pull/45843)
  [CI][NIXL] Pin NIXL to 1.2.0 (#45843)
  _Files: `requirements/kv_connectors.txt`_
- **2026-06-17** [`aa0ac8a661`](https://github.com/vllm-project/vllm/commit/aa0ac8a661) [#45865](https://github.com/vllm-project/vllm/pull/45865)
  [CI] Run pre-commit on self-hosted vllm-runners (#45865)
  _Files: `.github/actionlint.yaml`, `.github/workflows/pre-commit.yml`_
- **2026-06-17** [`ef2c40dc00`](https://github.com/vllm-project/vllm/commit/ef2c40dc00) [#45870](https://github.com/vllm-project/vllm/pull/45870)
  [XPU][CI] fix server test file path (#45870)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-06-16** [`506ec6d656`](https://github.com/vllm-project/vllm/commit/506ec6d656) [#45793](https://github.com/vllm-project/vllm/pull/45793)
  Upgrade tpu-inference to v0.22.1 (#45793)
  _Files: `requirements/tpu.txt`_
- **2026-06-16** [`c69c73418a`](https://github.com/vllm-project/vllm/commit/c69c73418a) [#44372](https://github.com/vllm-project/vllm/pull/44372)
  [XPU][CI] add intel xpu cases for nightly CI (#44372)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-06-15** [`e3e3cd5458`](https://github.com/vllm-project/vllm/commit/e3e3cd5458) [#45602](https://github.com/vllm-project/vllm/pull/45602)
  [Bugfix][CI] Update Dockerfile dependency graph PNG (#45602)
  _Files: `docs/assets/contributing/dockerfile-stages-dependency.png`_

## Disaggregation / PD  (14 commits)

- **2026-06-22** [`a9f7b2d41c`](https://github.com/vllm-project/vllm/commit/a9f7b2d41c) [#43468](https://github.com/vllm-project/vllm/pull/43468)
  [feature][kv_offload] Self-describing KV events for OffloadingConnector (#43468)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+5 more__
- **2026-06-21** [`d3ad8e8bcd`](https://github.com/vllm-project/vllm/commit/d3ad8e8bcd) [#46231](https://github.com/vllm-project/vllm/pull/46231)
  [Bugfix] Defer offload reads while transfers are pending (#46231)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-06-20** [`ab7fcbdd5d`](https://github.com/vllm-project/vllm/commit/ab7fcbdd5d) [#45969](https://github.com/vllm-project/vllm/pull/45969)
  [Perf][KVConnector][Mooncake] Compact chunk-hash keys and zero-copy lookup wire format (#45969)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py` _+3 more__
- **2026-06-19** [`c9135db27c`](https://github.com/vllm-project/vllm/commit/c9135db27c) [#45762](https://github.com/vllm-project/vllm/pull/45762)
  [Docs] Update stale LMCache examples (#45762)
  _Files: `docs/deployment/integrations/production-stack.md`, `docs/features/disagg_prefill.md`, `examples/disaggregated/lmcache/README.md`, `examples/disaggregated/lmcache/cpu_offload_lmcache.py` _+4 more__
- **2026-06-18** [`41dcf49ca5`](https://github.com/vllm-project/vllm/commit/41dcf49ca5) [#45371](https://github.com/vllm-project/vllm/pull/45371)
  [Bugfix][KV Connector] Disable Mooncake TP put-striding when DCP > 1 (#45371)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-18** [`35e4dd4a69`](https://github.com/vllm-project/vllm/commit/35e4dd4a69) [#45659](https://github.com/vllm-project/vllm/pull/45659)
  [KV Connector][Mooncake] Async lookup to reduce scheduler overhead (#45659)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+2 more__
- **2026-06-18** [`5fd3b276f8`](https://github.com/vllm-project/vllm/commit/5fd3b276f8) [#45444](https://github.com/vllm-project/vllm/pull/45444)
  [Mooncake] Skip KV lookup for non-reachable SWA blocks (#45444)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-18** [`d57888efa4`](https://github.com/vllm-project/vllm/commit/d57888efa4) [#39726](https://github.com/vllm-project/vllm/pull/39726)
  [SimpleCPUOffloadConnector]: Add support for reset_cache() (#39726)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-06-17** [`0d339cf135`](https://github.com/vllm-project/vllm/commit/0d339cf135) [#45879](https://github.com/vllm-project/vllm/pull/45879)
  [Bugfix] Fix NixlConnector handshake block_len validation for GQA-replicated KV heads (#45879)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-06-17** [`eb0fdeb1e8`](https://github.com/vllm-project/vllm/commit/eb0fdeb1e8) [#45831](https://github.com/vllm-project/vllm/pull/45831)
  [Bugfix][PD] Fix DSV4 disaggregated serving (#45831)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-06-17** [`6d8fff5698`](https://github.com/vllm-project/vllm/commit/6d8fff5698) [#45595](https://github.com/vllm-project/vllm/pull/45595)
  [KV Connector][Offloading] Avoid blocking the engine to flush offloads on idle (#45595)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`, `vllm/v1/kv_offload/base.py` _+2 more__
- **2026-06-16** [`44b2512767`](https://github.com/vllm-project/vllm/commit/44b2512767) [#45767](https://github.com/vllm-project/vllm/pull/45767)
  [KV Connector][Mooncake] Add cache_prefix to namespace store keys (#45767)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-06-16** [`188c68798e`](https://github.com/vllm-project/vllm/commit/188c68798e) [#45488](https://github.com/vllm-project/vllm/pull/45488)
  [KVConnector][MoRIIO] Allow overriding the advertised host IP (#45488)
  _Files: `tests/v1/kv_connector/unit/test_moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-06-16** [`d53f4593ce`](https://github.com/vllm-project/vllm/commit/d53f4593ce) [#44528](https://github.com/vllm-project/vllm/pull/44528)
  [KV Connector][Mooncake] Pipeline-parallel support for PD-disaggregated serving with Mooncake connector (#44528)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`, `vllm/distributed/kv_transfer/kv_transfer_state.py`_

## Multimodal  (13 commits)

- **2026-06-22** [`b529bfd6c5`](https://github.com/vllm-project/vllm/commit/b529bfd6c5) [#45768](https://github.com/vllm-project/vllm/pull/45768)
  [XPU][CI] Add agent_tags for Intel GPU CI (#45768)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/expert_parallelism_intel.yaml` _+6 more__
- **2026-06-21** [`12fe2a9aac`](https://github.com/vllm-project/vllm/commit/12fe2a9aac) [#46305](https://github.com/vllm-project/vllm/pull/46305)
  [Bugfix][Qwen3-VL] Fix multi-video crash with list-valued fps/num_frames (#46305)
  _Files: `tests/models/multimodal/processing/test_qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-06-21** [`635c38338a`](https://github.com/vllm-project/vllm/commit/635c38338a) [#45555](https://github.com/vllm-project/vllm/pull/45555)
  [Multimodal] Add Qwen2-VL/Qwen2.5-VL processor-mapped video loader (#45555)
  _Files: `tests/entrypoints/pooling/classify/test_online_vision.py`, `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`, `vllm/transformers_utils/processor.py`_
- **2026-06-20** [`d272418f45`](https://github.com/vllm-project/vllm/commit/d272418f45) [#46026](https://github.com/vllm-project/vllm/pull/46026)
  [Perf] Optimize Qwen3-VL multi-video prompt processing (#46026)
  _Files: `tests/models/multimodal/processing/test_qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-06-19** [`675cd5d228`](https://github.com/vllm-project/vllm/commit/675cd5d228) [#46095](https://github.com/vllm-project/vllm/pull/46095)
  [Model Runner V2] Fix MRv2 memory leak test (#46095)
  _Files: `tests/models/multimodal/generation/test_memory_leak.py`_
- **2026-06-17** [`1a59078c87`](https://github.com/vllm-project/vllm/commit/1a59078c87) [#45654](https://github.com/vllm-project/vllm/pull/45654)
  [CI/Build] Avoid duplicate ViT CG test introduced by accident (#45654)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-06-17** [`fa85ead2f3`](https://github.com/vllm-project/vllm/commit/fa85ead2f3) [#41992](https://github.com/vllm-project/vllm/pull/41992)
  [MM][Perf][CG] Support ViT full CUDA graph for Kimi-VL (#41992)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/kimi_vl.py` _+1 more__
- **2026-06-17** [`3d20275bb4`](https://github.com/vllm-project/vllm/commit/3d20275bb4) [#45908](https://github.com/vllm-project/vllm/pull/45908)
  fix(security): enforce audio decode duration limit in chat completions path (#45908)
  _Files: `vllm/multimodal/media/audio.py`_
- **2026-06-16** [`ad32608e24`](https://github.com/vllm-project/vllm/commit/ad32608e24) [#43586](https://github.com/vllm-project/vllm/pull/43586)
  [MM][Perf][CG] Support dual-path ViT full CUDA graph for DeepSeek-OCR (#43586)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py` _+12 more__
- **2026-06-16** [`2addbb9cc9`](https://github.com/vllm-project/vllm/commit/2addbb9cc9) [#45673](https://github.com/vllm-project/vllm/pull/45673)
  [BugFix] Support async scheduling with prompt embeds for multimodal models (#45673)
  _Files: `vllm/config/vllm.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-06-16** [`e3cfea2e1b`](https://github.com/vllm-project/vllm/commit/e3cfea2e1b) [#44412](https://github.com/vllm-project/vllm/pull/44412)
  [Multimodal] Add Qwen3-VL video loader (#44412)
  _Files: `tests/multimodal/test_video.py`, `tests/multimodal/utils.py`, `vllm/multimodal/video.py`_
- **2026-06-15** [`b997071ec4`](https://github.com/vllm-project/vllm/commit/b997071ec4) [#45510](https://github.com/vllm-project/vllm/pull/45510)
  (security) Enforce audio upload size limit before full file materialization (#45510)
  _Files: `tests/entrypoints/speech_to_text/test_upload_size_limit.py`, `vllm/entrypoints/speech_to_text/base/utils.py`, `vllm/entrypoints/speech_to_text/transcription/api_router.py`, `vllm/entrypoints/speech_to_text/translation/api_router.py`_
- **2026-06-15** [`48df95c43e`](https://github.com/vllm-project/vllm/commit/48df95c43e) [#45458](https://github.com/vllm-project/vllm/pull/45458)
  [Feature][Frontend] Report multimodal token counts in usage.prompt_tokens_details (#45458)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/entrypoints/openai/chat_completion/serving.py`, `vllm/entrypoints/openai/engine/protocol.py`_

## KV Cache / Offload  (10 commits)

- **2026-06-21** [`c441ad1c07`](https://github.com/vllm-project/vllm/commit/c441ad1c07) [#45957](https://github.com/vllm-project/vllm/pull/45957)
  [KV Offloading] Add labeled metrics support (#45957)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`, `vllm/v1/kv_offload/base.py`_
- **2026-06-20** [`cc22621b51`](https://github.com/vllm-project/vllm/commit/cc22621b51) [#46205](https://github.com/vllm-project/vllm/pull/46205)
  [KV Offload] Support packed HMA KV cache layout (#46205)
  _Files: `tests/v1/core/test_contiguous_kv_packing.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`, `vllm/envs.py`, `vllm/v1/core/kv_cache_utils.py` _+2 more__
- **2026-06-19** [`01192139bf`](https://github.com/vllm-project/vllm/commit/01192139bf) [#44577](https://github.com/vllm-project/vllm/pull/44577)
  [DSv4] Pack KV caches into contiguous per-block allocations for DeepSeek V4 (#44577)
  _Files: `tests/v1/core/test_contiguous_kv_packing.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`, `vllm/v1/core/kv_cache_utils.py` _+3 more__
- **2026-06-18** [`1e9f04da14`](https://github.com/vllm-project/vllm/commit/1e9f04da14) [#44602](https://github.com/vllm-project/vllm/pull/44602)
  fix(anthropic): preserve inline system message position for prefix caching (#44602)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-06-18** [`421c1ec448`](https://github.com/vllm-project/vllm/commit/421c1ec448) [#45905](https://github.com/vllm-project/vllm/pull/45905)
  [KV Offloading] Remove dummy worker-side stats from OffloadingConnector (#45905)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`_
- **2026-06-18** [`f428718ffe`](https://github.com/vllm-project/vllm/commit/f428718ffe) [#45823](https://github.com/vllm-project/vllm/pull/45823)
  [Fix][KV offload] Defer `on_request_finished` until in-flight transfers drain (#45823)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py`, `vllm/v1/kv_offload/tiering/base.py`_
- **2026-06-17** [`a46abb7ae6`](https://github.com/vllm-project/vllm/commit/a46abb7ae6) [#45312](https://github.com/vllm-project/vllm/pull/45312)
  [Bugfix][Quantization] Reject unsupported compressed tensors KV cache schemes (#45312)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-06-16** [`7ad894c86a`](https://github.com/vllm-project/vllm/commit/7ad894c86a) [#44784](https://github.com/vllm-project/vllm/pull/44784)
  [Bugfix] Prevent cuMemcpyBatchAsync segfault with MTP and KV offloading (#44784)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-06-15** [`7e612a0f06`](https://github.com/vllm-project/vllm/commit/7e612a0f06) [#44541](https://github.com/vllm-project/vllm/pull/44541)
  [KV Offloading] Implement `reset_cache` for `TieringOffloadingManager` (#44541)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+6 more__
- **2026-06-15** [`b675cb7d0f`](https://github.com/vllm-project/vllm/commit/b675cb7d0f) [#45086](https://github.com/vllm-project/vllm/pull/45086)
  [Bugfix][CPU] Honor cgroup memory limit when computing KV cache size (#45086)
  _Files: `vllm/utils/cpu_resource_utils.py`_

## LoRA  (7 commits)

- **2026-06-18** [`7299e6509e`](https://github.com/vllm-project/vllm/commit/7299e6509e) [#45950](https://github.com/vllm-project/vllm/pull/45950)
  [Rust Frontend] Return model metadata fields in /v1/models (#45950)
  _Files: `rust/Cargo.lock`, `rust/src/server/Cargo.toml`, `rust/src/server/src/lib.rs`, `rust/src/server/src/lora.rs` _+4 more__
- **2026-06-17** [`3c6084bb0d`](https://github.com/vllm-project/vllm/commit/3c6084bb0d) [#45852](https://github.com/vllm-project/vllm/pull/45852)
  [Bugfix][Gemma4] Pre-initialise streaming reasoning state when prompt ends inside an open `<|channel>` (fixes #45834) (#45852)
  _Files: `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/engine/adapters.py`, `vllm/parser/engine/parser_engine.py` _+2 more__
- **2026-06-16** [`f00e163f35`](https://github.com/vllm-project/vllm/commit/f00e163f35) [#45701](https://github.com/vllm-project/vllm/pull/45701)
  [Frontend] Add Streaming Parser Engine and new MinimaxM2 Parser (#45701)
  _Files: `tests/parser/engine/test_minimax_m2.py`, `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_minimax_m2_reasoning_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py` _+8 more__
- **2026-06-16** [`f3858d5422`](https://github.com/vllm-project/vllm/commit/f3858d5422) [#45755](https://github.com/vllm-project/vllm/pull/45755)
  [Frontend] [Parser] Migrate Nemotron V3 to streaming parser engine  (#45755)
  _Files: `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_nemotron_v3.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py` _+8 more__
- **2026-06-15** [`76a373eff4`](https://github.com/vllm-project/vllm/commit/76a373eff4) [#45588](https://github.com/vllm-project/vllm/pull/45588)
  [Frontend] Replace legacy Gemma4 parsers with engine-based implementation (#45588)
  _Files: `tests/parser/engine/replay_harness.py`, `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `tests/parser/engine/test_parser_engine.py` _+16 more__
- **2026-06-15** [`eacff17c8d`](https://github.com/vllm-project/vllm/commit/eacff17c8d) [#35536](https://github.com/vllm-project/vllm/pull/35536)
  [Model Runner V2][Bugfix] Fix MRV2 LoRA warmup (#35536)
  _Files: `tests/lora/test_qwen3_with_multi_loras.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/dp_utils.py`, `vllm/v1/worker/gpu/lora_utils.py` _+1 more__
- **2026-06-15** [`c4a3f9d137`](https://github.com/vllm-project/vllm/commit/c4a3f9d137) [#45413](https://github.com/vllm-project/vllm/pull/45413)
  [Frontend] Add Streaming Parser Engine and new Qwen3 Parser (#45413)
  _Files: `tests/parser/engine/__init__.py`, `tests/parser/engine/conftest.py`, `tests/parser/engine/replay_harness.py`, `tests/parser/engine/streaming_helpers.py` _+29 more__

## Compilation / CUDA Graph  (4 commits)

- **2026-06-20** [`e9de72fe6c`](https://github.com/vllm-project/vllm/commit/e9de72fe6c) [#46198](https://github.com/vllm-project/vllm/pull/46198)
  [Bugfix] Guard model_config access in _log_compilation_config (#46198)
  _Files: `vllm/compilation/backends.py`_
- **2026-06-18** [`b4092176b9`](https://github.com/vllm-project/vllm/commit/b4092176b9) [#45448](https://github.com/vllm-project/vllm/pull/45448)
  [Bugfix] Complete one-shot fused all-reduce PDL at end to avoid NaN (#45448)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-06-16** [`ebf3a6d705`](https://github.com/vllm-project/vllm/commit/ebf3a6d705) [#45307](https://github.com/vllm-project/vllm/pull/45307)
  [Bugfix] Fix trtllm fused allreduce+rms_norm for transformers backend (#45307)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-06-15** [`2725c84aae`](https://github.com/vllm-project/vllm/commit/2725c84aae) [#38608](https://github.com/vllm-project/vllm/pull/38608)
  [XPU] Enable sequence parallel support for XPU (#38608)
  _Files: `tests/compile/conftest.py`, `tests/compile/test_sequence_parallelism_threshold.py`, `vllm/compilation/passes/fusion/sequence_parallelism.py`, `vllm/compilation/passes/pass_manager.py` _+1 more__

## Docs  (3 commits)

- **2026-06-22** [`2e2c47928b`](https://github.com/vllm-project/vllm/commit/2e2c47928b) [#45940](https://github.com/vllm-project/vllm/pull/45940)
  [Doc] Update MiniMax-M3  (#45940)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-06-19** [`0a49fb2b13`](https://github.com/vllm-project/vllm/commit/0a49fb2b13) [#46181](https://github.com/vllm-project/vllm/pull/46181)
  Fix dead link in docs (#46181)
  _Files: `docs/contributing/model/basic.md`_
- **2026-06-17** [`ee0fd6984a`](https://github.com/vllm-project/vllm/commit/ee0fd6984a) [#45279](https://github.com/vllm-project/vllm/pull/45279)
  docs, kv_offloading: add docs for selective offload (#45279)
  _Files: `docs/features/kv_offloading_usage.md`_

## Speculative Decoding  (3 commits)

- **2026-06-21** [`89bd2c14d3`](https://github.com/vllm-project/vllm/commit/89bd2c14d3) [#43132](https://github.com/vllm-project/vllm/pull/43132)
  [Spec Decode] Add Qwen3 architecture support for EAGLE3 (#43132)
  _Files: `tests/models/registry.py`, `tests/v1/spec_decode/test_speculators_correctness.py`, `vllm/model_executor/models/qwen3_eagle3.py`, `vllm/model_executor/models/registry.py` _+2 more__
- **2026-06-18** [`ebbb2d55ac`](https://github.com/vllm-project/vllm/commit/ebbb2d55ac) [#45941](https://github.com/vllm-project/vllm/pull/45941)
  [CI/Build][Bugfix] Fix SD LoRA  (#45941)
  _Files: `vllm/v1/worker/gpu/spec_decode/eagle/utils.py`_
- **2026-06-15** [`9872921c5f`](https://github.com/vllm-project/vllm/commit/9872921c5f) [#44423](https://github.com/vllm-project/vllm/pull/44423)
  [XPU] skip UT test_with_ngram_gpu_spec_decoding (#44423)
  _Files: `tests/v1/e2e/general/test_async_scheduling.py`_

## Perf / Benchmark  (3 commits)

- **2026-06-16** [`8e27a9c215`](https://github.com/vllm-project/vllm/commit/8e27a9c215) [#44944](https://github.com/vllm-project/vllm/pull/44944)
  [PERF] Fuse multi-group block table staged writes (#44944)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/buffer_utils.py`_
- **2026-06-16** [`ced32bb474`](https://github.com/vllm-project/vllm/commit/ced32bb474) [#42425](https://github.com/vllm-project/vllm/pull/42425)
  [Perf] Add VLLM_TRITON_FORCE_FIRST_CONFIG to skip Triton autotuning (#42425)
  _Files: `tests/test_force_first_config.py`, `vllm/env_override.py`, `vllm/envs.py`, `vllm/triton_utils/force_first_config.py`_
- **2026-06-16** [`8bf374955f`](https://github.com/vllm-project/vllm/commit/8bf374955f) [#41496](https://github.com/vllm-project/vllm/pull/41496)
  [Bug Fix] Allow pinned memory for WSL2 (#41496)
  _Files: `benchmarks/benchmark_pin_memory.py`, `vllm/envs.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`_

---
_Generated 2026-06-22 13:46 UTC_