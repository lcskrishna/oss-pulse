# sgl-project/sglang — Weekly Change Report
**Period:** 2026-06-01 → 2026-06-08  |  **Total commits:** 355

## ✨ New Features This Week

- **2026-06-08** [#27554](https://github.com/sgl-project/sglang/pull/27554) — [UnifiedTree]: Support hicache metrics (#27554)
- **2026-06-08** [#22786](https://github.com/sgl-project/sglang/pull/22786) — [AMD][diffusion] Add FlyDSL fused normalization kernels for ROCm diffusion models optimization (#22786)
- **2026-06-08** [#22253](https://github.com/sgl-project/sglang/pull/22253) — [EPD] Support dynamic encoder register (#22253)
- **2026-06-08** [#26850](https://github.com/sgl-project/sglang/pull/26850) — Add parallel-rank dump filenames and pipeline-global layer remapping to dumper (#26850)
- **2026-06-08** [#27394](https://github.com/sgl-project/sglang/pull/27394) — feat(agentic router): add sticky-session routing policy (#27394)
- **2026-06-08** [#10950](https://github.com/sgl-project/sglang/pull/10950) — Support encoder_decoder on cpu_graph_runner (#10950)
- **2026-06-08** [#27463](https://github.com/sgl-project/sglang/pull/27463) — Support `topk > 1` tree drafting for mamba/hybrid-linear models on spec v2 (#27463)
- **2026-06-07** [#22299](https://github.com/sgl-project/sglang/pull/22299) — [AMD] Enable Piecewise CUDA Graph for AMD GPUs (#22299)
- **2026-06-07** [#27393](https://github.com/sgl-project/sglang/pull/27393) — [diffusion] support tp for ideogram4 (#27393)
- **2026-06-07** [#27492](https://github.com/sgl-project/sglang/pull/27492) — Add all_to_all_single to GroupCoordinator (#27492)
- _…and 95 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-08** [`a26587dd4e`](https://github.com/sgl-project/sglang/commit/a26587dd4e) [#22786](https://github.com/sgl-project/sglang/pull/22786) — [AMD][diffusion] Add FlyDSL fused normalization kernels for ROCm diffusion models optimization (#22786)
- **2026-06-08** [`8ff0c9fef9`](https://github.com/sgl-project/sglang/commit/8ff0c9fef9) [#27534](https://github.com/sgl-project/sglang/pull/27534) — [PD] Downgrade propagated rank failure logs from error to debug (#27534)
- **2026-06-08** [`df6b9c2d9d`](https://github.com/sgl-project/sglang/commit/df6b9c2d9d) [#27538](https://github.com/sgl-project/sglang/pull/27538) — [AMD] ci: reinstall MoRI if Different from Dockerfile-pinned commit during install_dependency (#27538)
- **2026-06-08** [`18d728967a`](https://github.com/sgl-project/sglang/commit/18d728967a) [#26922](https://github.com/sgl-project/sglang/pull/26922) — [PD][MoRI] Drive KV transfers with a sharded synchronous worker pool (#26922)
- **2026-06-08** [`1aa5040c74`](https://github.com/sgl-project/sglang/commit/1aa5040c74) [#27530](https://github.com/sgl-project/sglang/pull/27530) — Update code owners (AMD) (#27530)
- **2026-06-08** [`1c73ff8ad3`](https://github.com/sgl-project/sglang/commit/1c73ff8ad3) [#27063](https://github.com/sgl-project/sglang/pull/27063) — [AMD] Optimize gpt-oss-120B performance (#27063)
- **2026-06-08** [`303757ccd8`](https://github.com/sgl-project/sglang/commit/303757ccd8) [#27485](https://github.com/sgl-project/sglang/pull/27485) — [Attn] Fix aiter MLA verify `kv_indices` under-alloc + shared `assert_buffer_fits` guard (#27485)
- **2026-06-07** [`10d33bd77e`](https://github.com/sgl-project/sglang/commit/10d33bd77e) [#22299](https://github.com/sgl-project/sglang/pull/22299) — [AMD] Enable Piecewise CUDA Graph for AMD GPUs (#22299)
- **2026-06-07** [`eab2e02fa0`](https://github.com/sgl-project/sglang/commit/eab2e02fa0) [#27475](https://github.com/sgl-project/sglang/pull/27475) — [spec] Dedup draft `kv_indices` sizing into `spec_utils` helpers (#27475)
- **2026-06-07** [`5e2e0d5b49`](https://github.com/sgl-project/sglang/commit/5e2e0d5b49) [#27484](https://github.com/sgl-project/sglang/pull/27484) — [spec] Make `spec_utils` module-importable: type-only imports under TYPE_CHECKING (#27484)
- **2026-06-06** [`032c9efb46`](https://github.com/sgl-project/sglang/commit/032c9efb46) [#27461](https://github.com/sgl-project/sglang/pull/27461) — Enable async-assert invariant probes by default in CI (#27461)
- **2026-06-06** [`aa55657e9e`](https://github.com/sgl-project/sglang/commit/aa55657e9e) [#27201](https://github.com/sgl-project/sglang/pull/27201) — [AMD][WA] force to use gate_mode interleaved to fix tp2/tp4/tp8 acc issue (#27201)
- **2026-06-06** [`3030119ef7`](https://github.com/sgl-project/sglang/commit/3030119ef7) [#27152](https://github.com/sgl-project/sglang/pull/27152) — [bugfix][AMD] AttributeError and warp mask bugs in DeepSeek V4 FP4 indexer (#27152)
- **2026-06-05** [`7f919edf00`](https://github.com/sgl-project/sglang/commit/7f919edf00) [#25885](https://github.com/sgl-project/sglang/pull/25885) — [AMD] Support alt stream for Qwen3.5 on AMD platform (#25885)
- **2026-06-05** [`8c8281801d`](https://github.com/sgl-project/sglang/commit/8c8281801d) [#27376](https://github.com/sgl-project/sglang/pull/27376) — [AMD] update ROCm AITER commit (#27376)
- **2026-06-05** [`66b932154f`](https://github.com/sgl-project/sglang/commit/66b932154f) [#27352](https://github.com/sgl-project/sglang/pull/27352) — [AMD] fix(ci): run partition 3 of stage-c-test-large-8-gpu-amd (#27352)
- **2026-06-05** [`bd47869ba4`](https://github.com/sgl-project/sglang/commit/bd47869ba4) [#27320](https://github.com/sgl-project/sglang/pull/27320) — [perf] parallelize create_flashmla_kv_indices over page-blocks (#27320)
- **2026-06-04** [`69623f4b11`](https://github.com/sgl-project/sglang/commit/69623f4b11) [#27247](https://github.com/sgl-project/sglang/pull/27247) — [AMD] Guard aiter greedy_sample OOB token id (fixes VLM MMMU CI) (#27247)
- **2026-06-04** [`8e836e7dc9`](https://github.com/sgl-project/sglang/commit/8e836e7dc9) [#26746](https://github.com/sgl-project/sglang/pull/26746) — Support optional kwargs in AITER fused_moe runner (#26746)
- **2026-06-04** [`7aee2ff31b`](https://github.com/sgl-project/sglang/commit/7aee2ff31b) [#26914](https://github.com/sgl-project/sglang/pull/26914) — [AMD] Remove BF16-to-FP32 elementwise cast from compressor GEMM on HIP (#26914)
- **2026-06-04** [`ff93a576e5`](https://github.com/sgl-project/sglang/commit/ff93a576e5) [#27111](https://github.com/sgl-project/sglang/pull/27111) — [AMD] Minimax M25 : FP8 block-scale GEMM dispatch for ROCm 7.0 on gfx950 (#27111)
- **2026-06-04** [`04c16fc1e5`](https://github.com/sgl-project/sglang/commit/04c16fc1e5) [#27232](https://github.com/sgl-project/sglang/pull/27232) — [AMD][CI] Remove transformers pin from GLM-5.x nightly jobs (#27232)
- **2026-06-04** [`f3acb6d4de`](https://github.com/sgl-project/sglang/commit/f3acb6d4de) [#27222](https://github.com/sgl-project/sglang/pull/27222) — [CI] Fix multimodal-gen path filter for shared trace code (#27222)
- **2026-06-04** [`e4191708c9`](https://github.com/sgl-project/sglang/commit/e4191708c9) [#26845](https://github.com/sgl-project/sglang/pull/26845) — [Qwen3.5][AMD] Fix shared-expert ×ep_size over-count under allreduce-EP (#26845)
- **2026-06-04** [`858e5a5109`](https://github.com/sgl-project/sglang/commit/858e5a5109) [#26119](https://github.com/sgl-project/sglang/pull/26119) — [diffusion] chore: disagg server args, launch helpers, and warmup utils (#26119)
- **2026-06-04** [`6dcd78a37f`](https://github.com/sgl-project/sglang/commit/6dcd78a37f) [#27126](https://github.com/sgl-project/sglang/pull/27126) — [AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X (#27126)
- **2026-06-03** [`cfb7fb4fad`](https://github.com/sgl-project/sglang/commit/cfb7fb4fad) [#27188](https://github.com/sgl-project/sglang/pull/27188) — [AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage (#27188)
- **2026-06-03** [`c9ca56da8c`](https://github.com/sgl-project/sglang/commit/c9ca56da8c) [#27091](https://github.com/sgl-project/sglang/pull/27091) — Unify full→SWA index translation in init_forward_metadata; drop pool caches (#27091)
- **2026-06-03** [`1dd9432889`](https://github.com/sgl-project/sglang/commit/1dd9432889) [#26894](https://github.com/sgl-project/sglang/pull/26894) — [AMD] Fuse compress norm+rope+hadamard into single Triton kernel (#26894)
- **2026-06-03** [`d1bc06b63b`](https://github.com/sgl-project/sglang/commit/d1bc06b63b) [#27163](https://github.com/sgl-project/sglang/pull/27163) — [AMD] Disable AITER custom all-gather in DeepSeek-R1-MXFP4 8-GPU test (#27163)
- **2026-06-03** [`293816ab14`](https://github.com/sgl-project/sglang/commit/293816ab14) [#18005](https://github.com/sgl-project/sglang/pull/18005) — [AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight (#18005)
- **2026-06-03** [`d7013b6537`](https://github.com/sgl-project/sglang/commit/d7013b6537) [#27001](https://github.com/sgl-project/sglang/pull/27001) — [AMD] [CI] Remove hardcoded model/cache paths from MI35x nightly tests (#27001)
- **2026-06-03** [`8e77af1afc`](https://github.com/sgl-project/sglang/commit/8e77af1afc) [#24762](https://github.com/sgl-project/sglang/pull/24762) — [AMD] fix(triton-mla): cap max_kv_splits at 256 on gfx942 (Kimi-K2.6 hang) (#24762)
- **2026-06-03** [`ab7c4ab6bb`](https://github.com/sgl-project/sglang/commit/ab7c4ab6bb) [#25556](https://github.com/sgl-project/sglang/pull/25556) — [AMD] Fix correctness for AITER MLA backend with `--page-size > 1` (#25556)
- **2026-06-02** [`72929c7000`](https://github.com/sgl-project/sglang/commit/72929c7000) [#25093](https://github.com/sgl-project/sglang/pull/25093) — [AMD] Enable AITER custom all-gather on ROCm (#25093)
- **2026-06-02** [`99da43b900`](https://github.com/sgl-project/sglang/commit/99da43b900) [#26735](https://github.com/sgl-project/sglang/pull/26735) — [refactor] init_forward_metadata 3-method ABC + side-channel removal + ForwardMetadata type rename (#26735)
- **2026-06-02** [`2582134a59`](https://github.com/sgl-project/sglang/commit/2582134a59) [#26677](https://github.com/sgl-project/sglang/pull/26677) — [AMD] Add amd ci mamba state scatter test (#26677)
- **2026-06-02** [`d15a2dc72c`](https://github.com/sgl-project/sglang/commit/d15a2dc72c) [#26931](https://github.com/sgl-project/sglang/pull/26931) — [AMD] dpsk-v4 swa loc cache support (#26931)
- **2026-06-02** [`4226a6f13a`](https://github.com/sgl-project/sglang/commit/4226a6f13a) [#26884](https://github.com/sgl-project/sglang/pull/26884) — [AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path (#26884)
- **2026-06-01** [`89410b380b`](https://github.com/sgl-project/sglang/commit/89410b380b) [#26879](https://github.com/sgl-project/sglang/pull/26879) — [AMD] Pin compressed-tensors==0.15.0 to fix ROCm nightly build (#26879)
- **2026-06-01** [`b14fba17d9`](https://github.com/sgl-project/sglang/commit/b14fba17d9) [#26909](https://github.com/sgl-project/sglang/pull/26909) — [AMD] make bypass-fastfail label also disable within-suite fast-fail (#26909)
- **2026-06-01** [`f60710a1d7`](https://github.com/sgl-project/sglang/commit/f60710a1d7) [#26905](https://github.com/sgl-project/sglang/pull/26905) — [AMD] Fix stage-b-test-large-8-gpu-mi35x-disaggregation-amd : switch CACHE_HOST to a fresh path to fix "No space left on device" (#26905)
- **2026-06-01** [`1d7e2f6fb8`](https://github.com/sgl-project/sglang/commit/1d7e2f6fb8) [#22972](https://github.com/sgl-project/sglang/pull/22972) — [NPU] fix normal DeepEP mode num_tokens_per_rdma_rank error caused by none (#22972)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#26890](https://github.com/sgl-project/sglang/issues/26890) | [AITER-Upgrade] AITER Scout Status | — | 2026-06-08 |
| [#27476](https://github.com/sgl-project/sglang/issues/27476) | [Bug] PD disaggregation: CPython GC causes 70s+ stalls in KV transfer  | — | 2026-06-08 |
| [#27521](https://github.com/sgl-project/sglang/issues/27521) | [AMD] PR CI new test cases to cover | amd | 2026-06-08 |
| [#23494](https://github.com/sgl-project/sglang/issues/23494) | AMD Development Roadmap (2026 Q2) | amd | 2026-06-08 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-06-08 |
| [#27519](https://github.com/sgl-project/sglang/issues/27519) | RDNA3 (gfx1101 / RX 7800 XT) runs sgl-kernel + LFM2.5 — please widen t | — | 2026-06-08 |
| [#27504](https://github.com/sgl-project/sglang/issues/27504) | [HiCache] Garbled/corrupted output when L3 cache is loaded with Moonca | — | 2026-06-08 |
| [#26751](https://github.com/sgl-project/sglang/issues/26751) | [Bug] Gemma-4 mm: single non-RGB image crashes vision tower and kills  | — | 2026-06-07 |
| [#15025](https://github.com/sgl-project/sglang/issues/15025) | [Roadmap] DeepSeek v3.2 (GLM 5) Optimization | high priority, deepseek, Good Pro Issue, good second issue, nvidia | 2026-06-07 |
| [#27462](https://github.com/sgl-project/sglang/issues/27462) | [Roadmap] Parallel Speculative Decoding Roadmap | — | 2026-06-06 |
| [#27456](https://github.com/sgl-project/sglang/issues/27456) | [Bug] CPU-only inference crashes with `AssertionError: Torch not compi | — | 2026-06-06 |
| [#27418](https://github.com/sgl-project/sglang/issues/27418) | _handle_mamba_radix_cache logic cleanup | — | 2026-06-06 |
| [#27417](https://github.com/sgl-project/sglang/issues/27417) | [ROCm Test-First CI]: Day 0 SGLang MI455X UALoE72 Helios Rack open sou | — | 2026-06-06 |
| [#27194](https://github.com/sgl-project/sglang/issues/27194) | moe_kernels.py, stage-2 reduce path: small SGLANG_MORI_NUM_MAX_DISPATC | — | 2026-06-05 |
| [#27252](https://github.com/sgl-project/sglang/issues/27252) | [Roadmap]Prefill Context Parallel Refactor | — | 2026-06-05 |
| [#27384](https://github.com/sgl-project/sglang/issues/27384) | [Bug] DeepSeek-V4-Flash flash_mla_sparse_fwd device-side assert on B30 | — | 2026-06-05 |
| [#22084](https://github.com/sgl-project/sglang/issues/22084) | [Feature] Distributed Weight Data Parallelism (DWDP) for Sparse MoE Mo | — | 2026-06-05 |
| [#27310](https://github.com/sgl-project/sglang/issues/27310) | [RFC] GPU Memory Service (GMS) integration for out-of-process GPU memo | — | 2026-06-05 |
| [#27351](https://github.com/sgl-project/sglang/issues/27351) | [Bug] NPU Out of Memory During deep_ep Dispatch (Attempted 5503 GiB) | — | 2026-06-05 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-06-05 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 61 |
| Multimodal | 56 |
| KV Cache / Memory | 42 |
| MoE / Expert Parallel | 30 |
| Prefill / Decode Disaggregation | 29 |
| Scheduler / Batching | 23 |
| Speculative Decoding | 17 |
| Models | 16 |
| Other | 15 |
| CI / Build | 13 |
| Tensor / Data Parallel | 10 |
| Triton / Kernels | 10 |
| Docs / Examples | 10 |
| ROCm / AMD | 9 |
| Quantization | 9 |
| LoRA | 2 |
| Serving / API | 2 |
| Structured Output | 1 |

## Attention / FlashInfer  (61 commits)

- **2026-06-08** [`57ea09badb`](https://github.com/sgl-project/sglang/commit/57ea09badb) [#27545](https://github.com/sgl-project/sglang/pull/27545)
  Fix NaN in triton EAGLE spec-v2 draft-extend CUDA graph at topk>1 (wrong qo_indptr stride) (#27545)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`_
- **2026-06-08** [`0d0254c9de`](https://github.com/sgl-project/sglang/commit/0d0254c9de) [#20260](https://github.com/sgl-project/sglang/pull/20260)
  Fix port overflow in DP attention path when base port is near 65535 (#20260)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/network.py`_
- **2026-06-08** [`3d2165a286`](https://github.com/sgl-project/sglang/commit/3d2165a286) [#27361](https://github.com/sgl-project/sglang/pull/27361)
  Fix dual-chunk sparse fallback index overflow (#27361)
  _Files: `python/sglang/srt/layers/attention/dual_chunk_flashattention_backend.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dual_chunk_attention.py`, `test/registered/attention/unittests/KNOWN_FAILURES.md`, `test/registered/attention/unittests/dual_chunk/README.md` _+1 more__
- **2026-06-08** [`bf7fb6b925`](https://github.com/sgl-project/sglang/commit/bf7fb6b925) [#27477](https://github.com/sgl-project/sglang/pull/27477)
  fix dflash rope config parsing for updated transformers (#27477)
  _Files: `python/sglang/srt/models/dflash.py`_
- **2026-06-08** [`1c73ff8ad3`](https://github.com/sgl-project/sglang/commit/1c73ff8ad3) [#27063](https://github.com/sgl-project/sglang/pull/27063)
  [AMD] Optimize gpt-oss-120B performance (#27063)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/aiter_utils.py`, `python/sglang/srt/layers/attention/utils.py` _+7 more__
- **2026-06-08** [`303757ccd8`](https://github.com/sgl-project/sglang/commit/303757ccd8) [#27485](https://github.com/sgl-project/sglang/pull/27485)
  [Attn] Fix aiter MLA verify `kv_indices` under-alloc + shared `assert_buffer_fits` guard (#27485)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py` _+1 more__
- **2026-06-08** [`f68c79675f`](https://github.com/sgl-project/sglang/commit/f68c79675f) [#27463](https://github.com/sgl-project/sglang/pull/27463)
  Support `topk > 1` tree drafting for mamba/hybrid-linear models on spec v2 (#27463)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py` _+4 more__
- **2026-06-07** [`a07d813ec8`](https://github.com/sgl-project/sglang/commit/a07d813ec8) [#27473](https://github.com/sgl-project/sglang/pull/27473)
  Revert "Fix TRTLLM target verify query metadata (#27473)" (#27494)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-07** [`5be0b0c8c0`](https://github.com/sgl-project/sglang/commit/5be0b0c8c0) [#27473](https://github.com/sgl-project/sglang/pull/27473)
  Fix TRTLLM target verify query metadata (#27473)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-07** [`eab2e02fa0`](https://github.com/sgl-project/sglang/commit/eab2e02fa0) [#27475](https://github.com/sgl-project/sglang/pull/27475)
  [spec] Dedup draft `kv_indices` sizing into `spec_utils` helpers (#27475)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+1 more__
- **2026-06-07** [`5e2e0d5b49`](https://github.com/sgl-project/sglang/commit/5e2e0d5b49) [#27484](https://github.com/sgl-project/sglang/pull/27484)
  [spec] Make `spec_utils` module-importable: type-only imports under TYPE_CHECKING (#27484)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-07** [`066b4a2180`](https://github.com/sgl-project/sglang/commit/066b4a2180) [#27459](https://github.com/sgl-project/sglang/pull/27459)
  [core] Probe `set_kv_buffer` / `set_mla_kv_buffer` slot ids for OOB (#27459)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-06-06** [`5160f7914e`](https://github.com/sgl-project/sglang/commit/5160f7914e) [#27460](https://github.com/sgl-project/sglang/pull/27460)
  Fix MLA EAGLE draft CUDA-graph `kv_indices` under-allocation for `topk > 1` (#27460)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`_
- **2026-06-06** [`032c9efb46`](https://github.com/sgl-project/sglang/commit/032c9efb46) [#27461](https://github.com/sgl-project/sglang/pull/27461)
  Enable async-assert invariant probes by default in CI (#27461)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/nightly-72-gpu-gb200.yml`, `.github/workflows/nightly-test-nvidia.yml`, `.github/workflows/rerun-test.yml` _+12 more__
- **2026-06-06** [`26b9053dcc`](https://github.com/sgl-project/sglang/commit/26b9053dcc) [#27360](https://github.com/sgl-project/sglang/pull/27360)
  [Spec] Fix fa3 EAGLE draft-decode expand page_table scatter OOB for topk>1 + page_size>1 (#27360)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-06-06** [`8c47b7678a`](https://github.com/sgl-project/sglang/commit/8c47b7678a) [#27403](https://github.com/sgl-project/sglang/pull/27403)
  [attn backend] clean legacy init_mha_chunk_metadata in trtllm_mla backend (#27403)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-06-06** [`38ae22e08c`](https://github.com/sgl-project/sglang/commit/38ae22e08c) [#26733](https://github.com/sgl-project/sglang/pull/26733)
  Nemotron perf changes (#26733)
  _Files: `python/sglang/jit_kernel/activation.py`, `python/sglang/jit_kernel/benchmark/bench_activation.py`, `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`, `python/sglang/jit_kernel/tests/test_activation.py` _+11 more__
- **2026-06-06** [`393d0e169e`](https://github.com/sgl-project/sglang/commit/393d0e169e) [#27114](https://github.com/sgl-project/sglang/pull/27114)
  [Bugfix] Restore overridden HF config fields and support index_skip_topk_offset for DSA topk sharing (#27114)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`, `python/sglang/srt/models/deepseek_nextn.py` _+4 more__
- **2026-06-06** [`aa55657e9e`](https://github.com/sgl-project/sglang/commit/aa55657e9e) [#27201](https://github.com/sgl-project/sglang/pull/27201)
  [AMD][WA] force to use gate_mode interleaved to fix tp2/tp4/tp8 acc issue (#27201)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py`, `test/registered/amd/accuracy/mi35x/test_gpt_oss_eval_mi35x.py`_
- **2026-06-06** [`3030119ef7`](https://github.com/sgl-project/sglang/commit/3030119ef7) [#27152](https://github.com/sgl-project/sglang/pull/27152)
  [bugfix][AMD] AttributeError and warp mask bugs in DeepSeek V4 FP4 indexer (#27152)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`_
- **2026-06-05** [`3b62286fca`](https://github.com/sgl-project/sglang/commit/3b62286fca) [#27166](https://github.com/sgl-project/sglang/pull/27166)
  Reland "Support NextN = 2/4 in DSV32" (#27166)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-06-05** [`2c2a4f243a`](https://github.com/sgl-project/sglang/commit/2c2a4f243a) [#27338](https://github.com/sgl-project/sglang/pull/27338)
  [Bug] Fix EAGLE draft CUDA-graph `kv_indices` under-allocation for `topk > 1` (#27338)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`_
- **2026-06-05** [`bd47869ba4`](https://github.com/sgl-project/sglang/commit/bd47869ba4) [#27320](https://github.com/sgl-project/sglang/pull/27320)
  [perf] parallelize create_flashmla_kv_indices over page-blocks (#27320)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/cutlass_mla_backend.py`, `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/layers/attention/triton_ops/kv_indices.py` _+2 more__
- **2026-06-05** [`2c8357f794`](https://github.com/sgl-project/sglang/commit/2c8357f794) [#23280](https://github.com/sgl-project/sglang/pull/23280)
  [XPU] Enable Gemma 4 E2B / E4B / 31B/ 26B-A4B on Intel XPU (#23280)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`, `python/sglang/srt/layers/gemma4_fused_ops.py`, `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/gemma4_causal.py` _+2 more__
- **2026-06-05** [`5af02c18ae`](https://github.com/sgl-project/sglang/commit/5af02c18ae) [#25002](https://github.com/sgl-project/sglang/pull/25002)
  [spec_v2] Enable trtllm_mha draft-extend CUDA graph with v2 semantics (#25002)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_extend_runner.py`_
- **2026-06-05** [`7dc7376697`](https://github.com/sgl-project/sglang/commit/7dc7376697) [#27316](https://github.com/sgl-project/sglang/pull/27316)
  fix(attn): delegate init_mha_chunk_metadata in HybridLinearAttnBackend (#27316)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `test/registered/attention/unittests/hybrid_linear/README.md`, `test/registered/attention/unittests/hybrid_linear/__init__.py`, `test/registered/attention/unittests/hybrid_linear/test_flashinfer_mla_chunk_metadata.py`_
- **2026-06-05** [`0aa72a9e76`](https://github.com/sgl-project/sglang/commit/0aa72a9e76) [#27193](https://github.com/sgl-project/sglang/pull/27193)
  Replace skip_attn_backend_init with a batch-carried attention plan marker (+ staleness re-plan) (#27193)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py` _+16 more__
- **2026-06-04** [`687cfe9198`](https://github.com/sgl-project/sglang/commit/687cfe9198) [#27228](https://github.com/sgl-project/sglang/pull/27228)
  Enable runtime busy memory check for speculation topk>1 (#27228)
  _Files: `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_eagle_dp_attention.py`, `test/registered/spec/eagle/test_spec_eagle.py` _+6 more__
- **2026-06-04** [`7aee2ff31b`](https://github.com/sgl-project/sglang/commit/7aee2ff31b) [#26914](https://github.com/sgl-project/sglang/pull/26914)
  [AMD] Remove BF16-to-FP32 elementwise cast from compressor GEMM on HIP (#26914)
  _Files: `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/fused_compress_triton.py`_
- **2026-06-04** [`1af53f67b2`](https://github.com/sgl-project/sglang/commit/1af53f67b2) [#26676](https://github.com/sgl-project/sglang/pull/26676)
  [mem_cache][2/N] refactor: move SWATokenToKVPoolAllocator to allocator/swa.py (#26676)
  _Files: `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/kv_canary/runner/swa_divergence.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py` _+14 more__
- **2026-06-04** [`5c8a04ac4e`](https://github.com/sgl-project/sglang/commit/5c8a04ac4e) [#27156](https://github.com/sgl-project/sglang/pull/27156)
  [XPU CI] Expand stage-a and consolidate stage-b tests into stage-a (#27156)
  _Files: `.github/workflows/pr-test-xpu.yml`, `test/registered/attention/test_chunk_gated_delta_rule.py`, `test/registered/lora/test_lora_eviction_policy.py`, `test/registered/unit/sampling/test_sampling_params.py` _+5 more__
- **2026-06-04** [`d097cd2212`](https://github.com/sgl-project/sglang/commit/d097cd2212) [#21332](https://github.com/sgl-project/sglang/pull/21332)
  [GLM-5] Apply trtllm MHA kernel for GLM-5 on Blackwell (#21332)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-06-04** [`3790173b3b`](https://github.com/sgl-project/sglang/commit/3790173b3b) [#27153](https://github.com/sgl-project/sglang/pull/27153)
  [diffusion] fix: avoid flashattention forward context lookup (#27153)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/flash_attn.py`_
- **2026-06-03** [`cfb7fb4fad`](https://github.com/sgl-project/sglang/commit/cfb7fb4fad) [#27188](https://github.com/sgl-project/sglang/pull/27188)
  [AMD] Fix TP2 DeepSeek-R1 nhead=64 MLA decode crash and add nightly coverage (#27188)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `python/sglang/srt/layers/attention/aiter_backend.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_tp2_mi35x.py` _+2 more__
- **2026-06-03** [`c9ca56da8c`](https://github.com/sgl-project/sglang/commit/c9ca56da8c) [#27091](https://github.com/sgl-project/sglang/pull/27091)
  Unify full→SWA index translation in init_forward_metadata; drop pool caches (#27091)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsa_backend.py` _+25 more__
- **2026-06-03** [`1dd9432889`](https://github.com/sgl-project/sglang/commit/1dd9432889) [#26894](https://github.com/sgl-project/sglang/pull/26894)
  [AMD] Fuse compress norm+rope+hadamard into single Triton kernel (#26894)
  _Files: `python/sglang/srt/layers/attention/dsv4/compressor.py`, `python/sglang/srt/layers/attention/dsv4/fused_compress_triton.py`_
- **2026-06-03** [`ac99794e64`](https://github.com/sgl-project/sglang/commit/ac99794e64) [#26866](https://github.com/sgl-project/sglang/pull/26866)
  Reland spec v2 tree drafting (eagle topk>1) with page_size==1 (#26866) (#26997)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+8 more__
- **2026-06-03** [`9d0e6a2df4`](https://github.com/sgl-project/sglang/commit/9d0e6a2df4) [#26882](https://github.com/sgl-project/sglang/pull/26882)
  fix(mlx): set canary_manager and materialize overlap-loop inputs on Apple Silicon (#26882)
  _Files: `python/sglang/srt/hardware_backend/mlx/model_runner_stub.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/hardware_backend/mlx/test_attention_patching.py`_
- **2026-06-03** [`33f943fbf5`](https://github.com/sgl-project/sglang/commit/33f943fbf5) [#27143](https://github.com/sgl-project/sglang/pull/27143)
  [diffusion] optimize: batch usp replicated kv prefix all-to-all (#27143)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`_
- **2026-06-03** [`d7013b6537`](https://github.com/sgl-project/sglang/commit/d7013b6537) [#27001](https://github.com/sgl-project/sglang/pull/27001)
  [AMD] [CI] Remove hardcoded model/cache paths from MI35x nightly tests (#27001)
  _Files: `test/registered/amd/accuracy/mi35x/test_deepseek_r1_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_ar_fusion_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_eval_mi35x.py`, `test/registered/amd/accuracy/mi35x/test_deepseek_r1_mxfp4_kv_fp8_eval_mi35x.py` _+23 more__
- **2026-06-03** [`73b53e7a87`](https://github.com/sgl-project/sglang/commit/73b53e7a87) [#27138](https://github.com/sgl-project/sglang/pull/27138)
  Revert "Support NextN = 2/4 in DSV32" (#27138)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-06-03** [`93173b27e8`](https://github.com/sgl-project/sglang/commit/93173b27e8) [#25418](https://github.com/sgl-project/sglang/pull/25418)
  integrate flash_mla_sparse_fwd (#25418)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/dequant_k_cache.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py` _+4 more__
- **2026-06-03** [`8e77af1afc`](https://github.com/sgl-project/sglang/commit/8e77af1afc) [#24762](https://github.com/sgl-project/sglang/pull/24762)
  [AMD] fix(triton-mla): cap max_kv_splits at 256 on gfx942 (Kimi-K2.6 hang) (#24762)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/utils/common.py` _+1 more__
- **2026-06-03** [`b5560ffc36`](https://github.com/sgl-project/sglang/commit/b5560ffc36) [#24195](https://github.com/sgl-project/sglang/pull/24195)
  Fix flashinfer autotune oom glm51 (#24195)
  _Files: `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-03** [`0ef39784ef`](https://github.com/sgl-project/sglang/commit/0ef39784ef) [#26911](https://github.com/sgl-project/sglang/pull/26911)
  [Bugfix] Gate DP-attention even-token padding to CP-enabled configs (#26911)
  _Files: `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/utils/cp_utils.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-06-03** [`ab7c4ab6bb`](https://github.com/sgl-project/sglang/commit/ab7c4ab6bb) [#25556](https://github.com/sgl-project/sglang/pull/25556)
  [AMD] Fix correctness for AITER MLA backend with `--page-size > 1` (#25556)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-06-03** [`13852d3f31`](https://github.com/sgl-project/sglang/commit/13852d3f31) [#24870](https://github.com/sgl-project/sglang/pull/24870)
  Support NextN = 2/4 in DSV32 (#24870)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa_backend.py`_
- **2026-06-02** [`a711c57a32`](https://github.com/sgl-project/sglang/commit/a711c57a32) [#26966](https://github.com/sgl-project/sglang/pull/26966)
  [Spec] Fix Gemma 4 MTP with `trtllm_mha` crash issue (#26966)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-06-02** [`99da43b900`](https://github.com/sgl-project/sglang/commit/99da43b900) [#26735](https://github.com/sgl-project/sglang/pull/26735)
  [refactor] init_forward_metadata 3-method ABC + side-channel removal + ForwardMetadata type rename (#26735)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/aiter_backend.py` _+38 more__
- **2026-06-02** [`3ea1ba5b15`](https://github.com/sgl-project/sglang/commit/3ea1ba5b15) [#26206](https://github.com/sgl-project/sglang/pull/26206)
  [GDN] Optimize prefill QKV split dispatch (#26206)
  _Files: `benchmark/bench_linear_attention/bench_gdn_qkv_split.py`, `python/sglang/jit_kernel/triton/gdn_fused_proj.py`, `python/sglang/srt/layers/attention/fla/chunk_delta_h.py`, `python/sglang/srt/layers/attention/linear/gdn_backend.py`_
- **2026-06-02** [`559581b383`](https://github.com/sgl-project/sglang/commit/559581b383) [#26000](https://github.com/sgl-project/sglang/pull/26000)
  [codex] Centralize Triton utility kernels (#26000)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/triton_ops/cache_ops.py`, `python/sglang/srt/layers/attention/triton_ops/kv_indices.py` _+25 more__
- **2026-06-02** [`8cea0473ea`](https://github.com/sgl-project/sglang/commit/8cea0473ea) [#26996](https://github.com/sgl-project/sglang/pull/26996)
  Fix dp-attention token alignment in the dumper comparator e2e test (#26996)
  _Files: `test/registered/debug_utils/test_engine_dumper_comparator_e2e.py`_
- **2026-06-02** [`301bcf0872`](https://github.com/sgl-project/sglang/commit/301bcf0872) [#26209](https://github.com/sgl-project/sglang/pull/26209)
  Add FP4 Indexer for DeepSeek V4 (#26209)
  _Files: `python/sglang/jit_kernel/benchmark/bench_dsv4_fp4_indexer.py`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/main_norm_rope.cuh`, `python/sglang/jit_kernel/dsv4/__init__.py` _+10 more__
- **2026-06-02** [`1033d835ff`](https://github.com/sgl-project/sglang/commit/1033d835ff) [#26973](https://github.com/sgl-project/sglang/pull/26973)
  [diffusion] optimize: reduce cosmos3 denoise overhead (#26973)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`_
- **2026-06-02** [`2fc548f250`](https://github.com/sgl-project/sglang/commit/2fc548f250) [#26954](https://github.com/sgl-project/sglang/pull/26954)
  [diffusion] model: support lingot-world (#26954)
  _Files: `python/pyproject.toml`, `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/__init__.py` _+64 more__
- **2026-06-02** [`08526c7fca`](https://github.com/sgl-project/sglang/commit/08526c7fca) [#25539](https://github.com/sgl-project/sglang/pull/25539)
  [Spec] `FrozenKVMTP` fold assistant seed into captured draft graph (#25539)
  _Files: `python/sglang/srt/speculative/frozen_kv_mtp_cuda_graph_runner.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_runner.py`_
- **2026-06-02** [`0574d2b8a5`](https://github.com/sgl-project/sglang/commit/0574d2b8a5) [#23273](https://github.com/sgl-project/sglang/pull/23273)
  [NVIDIA] [GDN] Enable FlashInfer MTP verify on SM100+ (Blackwell) (#23273)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py`, `test/registered/models_e2e/test_qwen35_fp4_mtp.py`_
- **2026-06-02** [`98a1b58c47`](https://github.com/sgl-project/sglang/commit/98a1b58c47) [#25813](https://github.com/sgl-project/sglang/pull/25813)
  docs(cookbook): port popular model usage guides into cookbook pages (#25813)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-OCR.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx` _+43 more__
- **2026-06-01** [`da01f2974e`](https://github.com/sgl-project/sglang/commit/da01f2974e) [#26605](https://github.com/sgl-project/sglang/pull/26605)
  [Log] include max_token_num and hidden_dim in FlashInfer workspace init log (#26605)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`_
- **2026-06-01** [`bc36231d65`](https://github.com/sgl-project/sglang/commit/bc36231d65) [#26586](https://github.com/sgl-project/sglang/pull/26586)
  [KDA] Support KDA packed decode (#26586)
  _Files: `benchmark/bench_linear_attention/bench_kda_decode.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` _+1 more__
- **2026-06-01** [`118465f5b5`](https://github.com/sgl-project/sglang/commit/118465f5b5) [#26824](https://github.com/sgl-project/sglang/pull/26824)
  [attn backend] Make spec_v2 seq_lens_cpu optional in trtllm_mla backend (#26824)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_

## Multimodal  (56 commits)

- **2026-06-08** [`a26587dd4e`](https://github.com/sgl-project/sglang/commit/a26587dd4e) [#22786](https://github.com/sgl-project/sglang/pull/22786)
  [AMD][diffusion] Add FlyDSL fused normalization kernels for ROCm diffusion models optimization (#22786)
  _Files: `python/sglang/jit_kernel/diffusion/flydsl/fused_residual_norm.py`, `python/sglang/jit_kernel/tests/diffusion/test_flydsl_fused_norm.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`_
- **2026-06-08** [`6c2770149b`](https://github.com/sgl-project/sglang/commit/6c2770149b) [#27432](https://github.com/sgl-project/sglang/pull/27432)
  [diffusion] Fix native text-encoder loading for T5/UMT5 encoder-decoder models (#27432)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/multimodal_gen/test/unit/test_text_encoder_loader.py`_
- **2026-06-08** [`acf65c1c68`](https://github.com/sgl-project/sglang/commit/acf65c1c68) [#27282](https://github.com/sgl-project/sglang/pull/27282)
  [XPU CI] Pull prebuilt nightly image instead of building per-stage (#27282)
  _Files: `.github/workflows/pr-test-xpu.yml`, `scripts/ci/xpu/xpu_ci_start_container.sh`_
- **2026-06-08** [`12d47fa78b`](https://github.com/sgl-project/sglang/commit/12d47fa78b) [#27299](https://github.com/sgl-project/sglang/pull/27299)
  ci(xpu): push latest tag and use 7-char SHA in nightly image tags (#27299)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-06-08** [`70db73afce`](https://github.com/sgl-project/sglang/commit/70db73afce) [#27512](https://github.com/sgl-project/sglang/pull/27512)
  [Spec] Clamp multimodal pad sentinels in spec-v2 draft prefill embedding (#27512)
  _Files: `python/sglang/srt/models/mimo_v2_nextn.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-06-07** [`ff8b97406d`](https://github.com/sgl-project/sglang/commit/ff8b97406d) [#27443](https://github.com/sgl-project/sglang/pull/27443)
  [diffusion] optimize: precompute ideogram4 denoising metadata (#27443)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/ideogram.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/ideogram.py`_
- **2026-06-07** [`2c3e84affe`](https://github.com/sgl-project/sglang/commit/2c3e84affe) [#27439](https://github.com/sgl-project/sglang/pull/27439)
  [Diffusion] Enable Cosmos3 denoising profiling (#27439)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`_
- **2026-06-06** [`88a7b0fd30`](https://github.com/sgl-project/sglang/commit/88a7b0fd30) [#27451](https://github.com/sgl-project/sglang/pull/27451)
  Classify malformed-multimodal rejects as invalid_request (#27451)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/multimodal/processors/base_processor.py`_
- **2026-06-06** [`bd7fea0740`](https://github.com/sgl-project/sglang/commit/bd7fea0740) [#27437](https://github.com/sgl-project/sglang/pull/27437)
  [diffusion] Fix LingBot-World crash on camera control with ulysses>1 (#27437)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`_
- **2026-06-06** [`7c6f9542c7`](https://github.com/sgl-project/sglang/commit/7c6f9542c7) [#27440](https://github.com/sgl-project/sglang/pull/27440)
  [Diffusion] Avoid GPU syncs in UniPC scheduler (#27440)
  _Files: `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_unipc_multistep.py`_
- **2026-06-06** [`4e14b50c48`](https://github.com/sgl-project/sglang/commit/4e14b50c48) [#26356](https://github.com/sgl-project/sglang/pull/26356)
  [NPU]Support torch_npu profiler patch API drift (#26356)
  _Files: `python/sglang/multimodal_gen/runtime/utils/profiler.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/utils/profile_utils.py`, `python/sglang/srt/utils/torch_npu_patch_utils.py` _+1 more__
- **2026-06-06** [`e8668508d1`](https://github.com/sgl-project/sglang/commit/e8668508d1) [#27383](https://github.com/sgl-project/sglang/pull/27383)
  [diffusion] optimize: optimize LingBot realtime sp cache path (#27383)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_lingbot_causal_denoising.py`_
- **2026-06-06** [`25d8f431d1`](https://github.com/sgl-project/sglang/commit/25d8f431d1) [#27096](https://github.com/sgl-project/sglang/pull/27096)
  [diffusion] optimize: cosmos3 fused qknorm rope (#27096)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/mrope.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/utils.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vocoder_loader.py` _+1 more__
- **2026-06-05** [`5d691a44f4`](https://github.com/sgl-project/sglang/commit/5d691a44f4) [#27341](https://github.com/sgl-project/sglang/pull/27341)
  [diffusion] fix: fix LingBot World timestep error on MUSA (#27341)
  _Files: `python/sglang/multimodal_gen/runtime/models/utils.py`_
- **2026-06-05** [`4ef081b903`](https://github.com/sgl-project/sglang/commit/4ef081b903) [#27297](https://github.com/sgl-project/sglang/pull/27297)
  [diffusion] optimize: optimize LingBot realtime transport and camera conditioning (#27297)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_output_adapter.py`, `python/sglang/multimodal_gen/runtime/entrypoints/openai/realtime/realtime_video_api.py`, `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/lingbot_world/lingbot_world_causal_denoising.py` _+3 more__
- **2026-06-05** [`46c58b5c70`](https://github.com/sgl-project/sglang/commit/46c58b5c70) [#27327](https://github.com/sgl-project/sglang/pull/27327)
  bench: fix MMMU VLM eval max_tokens for CoT prompt (#27327)
  _Files: `test/registered/eval/test_vlms_mmmu_eval.py`_
- **2026-06-04** [`07f326c184`](https://github.com/sgl-project/sglang/commit/07f326c184) [#26864](https://github.com/sgl-project/sglang/pull/26864)
  Fix multimodal synthetic benchmark prompt generation to exclude special tokens (#26864)
  _Files: `python/sglang/benchmark/datasets/common.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-06-04** [`69623f4b11`](https://github.com/sgl-project/sglang/commit/69623f4b11) [#27247](https://github.com/sgl-project/sglang/pull/27247)
  [AMD] Guard aiter greedy_sample OOB token id (fixes VLM MMMU CI) (#27247)
  _Files: `python/sglang/srt/layers/sampler.py`, `test/registered/models/test_vlm_models.py`_
- **2026-06-04** [`e4a01d5ee2`](https://github.com/sgl-project/sglang/commit/e4a01d5ee2) [#27249](https://github.com/sgl-project/sglang/pull/27249)
  [diffusion] fix: fix realtime webui recording timeline (#27249)
  _Files: `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/index.html`_
- **2026-06-04** [`9e2ad6054c`](https://github.com/sgl-project/sglang/commit/9e2ad6054c) [#27236](https://github.com/sgl-project/sglang/pull/27236)
  [diffusion] feat: speed up lossless realtime rgb transport (#27236)
  _Files: `python/sglang/multimodal_gen/runtime/utils/realtime_video.py`_
- **2026-06-04** [`f3acb6d4de`](https://github.com/sgl-project/sglang/commit/f3acb6d4de) [#27222](https://github.com/sgl-project/sglang/pull/27222)
  [CI] Fix multimodal-gen path filter for shared trace code (#27222)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-06-04** [`29d23e198f`](https://github.com/sgl-project/sglang/commit/29d23e198f) [#25308](https://github.com/sgl-project/sglang/pull/25308)
  [diffusion] fix: preserve _explicit_fields across dataclasses.replace in DiffGenerator (#25308)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/diffusion_generator.py`, `python/sglang/multimodal_gen/test/unit/test_sampling_params.py`_
- **2026-06-04** [`11605767e0`](https://github.com/sgl-project/sglang/commit/11605767e0) [#27151](https://github.com/sgl-project/sglang/pull/27151)
  [diffusion] optimize: skip unused wanvae halo send copies (#27151)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_dist_utils.py`_
- **2026-06-04** [`5dbc52c2b7`](https://github.com/sgl-project/sglang/commit/5dbc52c2b7) [#27195](https://github.com/sgl-project/sglang/pull/27195)
  [diffusion] doc: add ernie Image diffusion (#27195)
  _Files: `docs_new/cookbook/diffusion/Ernie-Image/Ernie-Image.mdx`, `docs_new/cookbook/diffusion/README.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`_
- **2026-06-03** [`c670609ac5`](https://github.com/sgl-project/sglang/commit/c670609ac5) [#24630](https://github.com/sgl-project/sglang/pull/24630)
  [NPU] Diffusion CI Ground Truth Generation (NPU) (#24630)
  _Files: `.github/CODEOWNERS`, `.github/workflows/diffusion-ci-gt-gen-npu.yml`, `.github/workflows/pr-test-npu.yml`, `python/sglang/multimodal_gen/test/run_suite.py` _+8 more__
- **2026-06-03** [`578f232e5e`](https://github.com/sgl-project/sglang/commit/578f232e5e) [#27173](https://github.com/sgl-project/sglang/pull/27173)
  Fix trace_modules gate disabling default trace contexts (#27173)
  _Files: `python/sglang/multimodal_gen/runtime/utils/trace_wrapper.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/managers/data_parallel_controller.py` _+3 more__
- **2026-06-03** [`b0f78bef97`](https://github.com/sgl-project/sglang/commit/b0f78bef97) [#27148](https://github.com/sgl-project/sglang/pull/27148)
  [diffusion] improve: improve realtime webui playback pacing (#27148)
  _Files: `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/decoder_worker.js`, `python/sglang/multimodal_gen/apps/realtime_webui/index.html`, `python/sglang/multimodal_gen/apps/realtime_webui/playback_controller.js` _+15 more__
- **2026-06-03** [`45a66f4088`](https://github.com/sgl-project/sglang/commit/45a66f4088) [#27171](https://github.com/sgl-project/sglang/pull/27171)
  [Docs] Update unified Text/Vision/Audio model cookbook: install + sgl-eval accuracy (#27171)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`_
- **2026-06-03** [`fa5c8a3101`](https://github.com/sgl-project/sglang/commit/fa5c8a3101) [#27167](https://github.com/sgl-project/sglang/pull/27167)
  [model] support encoder-free unified Text/Vision/Audio model (#27167)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`, `docs_new/src/snippets/autoregressive/gemma4-deployment.jsx`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/configs/model_config.py` _+7 more__
- **2026-06-03** [`9450696aa5`](https://github.com/sgl-project/sglang/commit/9450696aa5) [#26963](https://github.com/sgl-project/sglang/pull/26963)
  [diffusion] CI: add cosmos3 nano t2v gpu test (#26963)
  _Files: `python/sglang/multimodal_gen/test/server/consistency_threshold.json`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`_
- **2026-06-03** [`dae86f51f5`](https://github.com/sgl-project/sglang/commit/dae86f51f5) [#27068](https://github.com/sgl-project/sglang/pull/27068)
  [diffusion] chore: polish realtime webui waiting state (#27068)
  _Files: `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/index.html`, `python/sglang/multimodal_gen/apps/realtime_webui/styles.css`, `python/sglang/multimodal_gen/test/unit/realtime/test_realtime_webui.py`_
- **2026-06-03** [`3e681d7fff`](https://github.com/sgl-project/sglang/commit/3e681d7fff) [#26937](https://github.com/sgl-project/sglang/pull/26937)
  Add per-rank staggered weight loading for improved TP I/O concurrency (#26937)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/text_encoder_loader.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_loader/loader.py`, `python/sglang/srt/model_loader/weight_utils.py`_
- **2026-06-03** [`71a747cf15`](https://github.com/sgl-project/sglang/commit/71a747cf15) [#27080](https://github.com/sgl-project/sglang/pull/27080)
  [diffusion] fix: fix lingbot realtime consistency gt pin (#27080)
  _Files: `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `python/sglang/multimodal_gen/test/test_utils.py`, `python/sglang/multimodal_gen/test/unit/realtime/test_realtime_consistency_harness.py`_
- **2026-06-03** [`3d54056391`](https://github.com/sgl-project/sglang/commit/3d54056391) [#27084](https://github.com/sgl-project/sglang/pull/27084)
  [diffusion] optimize: optimize Cosmos3 i2v latent prep (#27084)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`_
- **2026-06-03** [`3715a07e87`](https://github.com/sgl-project/sglang/commit/3715a07e87) [#27086](https://github.com/sgl-project/sglang/pull/27086)
  [diffusion] improve: clamp wanvae decode output in place (#27086)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`_
- **2026-06-03** [`f0e18be0ba`](https://github.com/sgl-project/sglang/commit/f0e18be0ba) [#27081](https://github.com/sgl-project/sglang/pull/27081)
  [diffusion] improve: use conv2d width padding in wanvae (#27081)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_dist_utils.py`_
- **2026-06-03** [`2d8cb87de7`](https://github.com/sgl-project/sglang/commit/2d8cb87de7) [#27094](https://github.com/sgl-project/sglang/pull/27094)
  docs: tag new diffusion cookbooks (#27094)
  _Files: `docs_new/docs.json`_
- **2026-06-03** [`83bc776612`](https://github.com/sgl-project/sglang/commit/83bc776612) [#27077](https://github.com/sgl-project/sglang/pull/27077)
  [diffusion] optimize: preserve dtype in wanvae nearest upsample (#27077)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_common_utils.py`_
- **2026-06-02** [`22043b917b`](https://github.com/sgl-project/sglang/commit/22043b917b) [#27055](https://github.com/sgl-project/sglang/pull/27055)
  [diffusion] CI: ad lingbot case (#27055)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-02** [`64a1dec8b6`](https://github.com/sgl-project/sglang/commit/64a1dec8b6) [#27026](https://github.com/sgl-project/sglang/pull/27026)
  [diffusion] feat: add realtime webui super resolution controls (#27026)
  _Files: `python/pyproject.toml`, `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/index.html`, `python/sglang/multimodal_gen/apps/realtime_webui/styles.css` _+3 more__
- **2026-06-02** [`ce7da7397a`](https://github.com/sgl-project/sglang/commit/ce7da7397a) [#27041](https://github.com/sgl-project/sglang/pull/27041)
  [diffusion] optimize: optimize cosmos3 (#27041)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/models/vaes/wanvae.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/base.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+2 more__
- **2026-06-02** [`3394931044`](https://github.com/sgl-project/sglang/commit/3394931044) [#27023](https://github.com/sgl-project/sglang/pull/27023)
  [diffusion] optimize: optimize lingbot performance (#27023)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/lingbot_world.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/lingbot_world/lingbot_world_causal_denoising.py`, `python/sglang/multimodal_gen/runtime/realtime/causal_state.py`, `scripts/ci/utils/diffusion/diffusion_case_parser.py`_
- **2026-06-02** [`a777672939`](https://github.com/sgl-project/sglang/commit/a777672939) [#27037](https://github.com/sgl-project/sglang/pull/27037)
  [diffusion] feat: enable parallel decode for cosmos3(#27037)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/cosmos3.py`_
- **2026-06-02** [`f651b48764`](https://github.com/sgl-project/sglang/commit/f651b48764) [#26045](https://github.com/sgl-project/sglang/pull/26045)
  Apply apply_group_norm_silu to LTX-2 latent upsampler (#26045)
  _Files: `python/sglang/jit_kernel/benchmark/diffusion/bench_group_norm_silu.py`, `python/sglang/multimodal_gen/runtime/models/upsampler/latent_upsampler.py`, `python/sglang/multimodal_gen/test/unit/test_latent_upsampler_group_norm_silu.py`_
- **2026-06-02** [`547b886b3c`](https://github.com/sgl-project/sglang/commit/547b886b3c) [#26985](https://github.com/sgl-project/sglang/pull/26985)
  ci: drop redundant multimodal-server jobs from nightly (Nvidia) (#26985)
  _Files: `.github/workflows/nightly-test-nvidia.yml`_
- **2026-06-02** [`a6985e1be0`](https://github.com/sgl-project/sglang/commit/a6985e1be0) [#26958](https://github.com/sgl-project/sglang/pull/26958)
  [diffusion] doc: add cookbook for lingbot-world (#26958)
  _Files: `docs_new/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs_new/cookbook/diffusion/LingBot-World/LingBot-World.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json`_
- **2026-06-02** [`3b26644bc4`](https://github.com/sgl-project/sglang/commit/3b26644bc4) [#26959](https://github.com/sgl-project/sglang/pull/26959)
  [diffusion] misc: add realtime-webui (#26959)
  _Files: `python/pyproject.toml`, `python/sglang/multimodal_gen/apps/realtime_webui/README.md`, `python/sglang/multimodal_gen/apps/realtime_webui/app.js`, `python/sglang/multimodal_gen/apps/realtime_webui/decoder_worker.js` _+4 more__
- **2026-06-01** [`f2beb7bc76`](https://github.com/sgl-project/sglang/commit/f2beb7bc76) [#26956](https://github.com/sgl-project/sglang/pull/26956)
  [diffusion] improve: avoid cosmos3 cpu float video postprocess (#26956)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`_
- **2026-06-01** [`9a8ab2d22b`](https://github.com/sgl-project/sglang/commit/9a8ab2d22b) [#26950](https://github.com/sgl-project/sglang/pull/26950)
  [diffusion] fix: align cosmos3 text packing with official pipeline (#26950)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-06-01** [`f6a5a1b59c`](https://github.com/sgl-project/sglang/commit/f6a5a1b59c) [#26555](https://github.com/sgl-project/sglang/pull/26555)
  [RL+VLM] Avoid retokenization drift for pre-tokenized (token-id) VLM requests (#26555)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/kimi_common.py`, `test/registered/vlm/test_token_id_retokenize_e2e.py`_
- **2026-06-01** [`1988a2c9ea`](https://github.com/sgl-project/sglang/commit/1988a2c9ea) [#26926](https://github.com/sgl-project/sglang/pull/26926)
  [diffusion] feat: improve cosmos3 serve API support (#26926)
  _Files: `docs_new/cookbook/diffusion/Cosmos/Cosmos3.mdx`, `docs_new/docs.json`, `python/sglang/multimodal_gen/configs/sample/sampling_params.py`, `python/sglang/multimodal_gen/registry.py` _+15 more__
- **2026-06-01** [`ed24e3aae8`](https://github.com/sgl-project/sglang/commit/ed24e3aae8) [#26947](https://github.com/sgl-project/sglang/pull/26947)
  [diffusion] feat: speed up png image output saving (#26947)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/utils.py`, `python/sglang/multimodal_gen/test/unit/test_output_saving.py`_
- **2026-06-01** [`89feb18eb9`](https://github.com/sgl-project/sglang/commit/89feb18eb9) [#26925](https://github.com/sgl-project/sglang/pull/26925)
  [diffusion] feat: allow --dit-cpu-offload with --dit-layerwise-offload (#26925)
  _Files: `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/test/unit/test_server_args.py`_
- **2026-06-01** [`20f47cfe8e`](https://github.com/sgl-project/sglang/commit/20f47cfe8e) [#26895](https://github.com/sgl-project/sglang/pull/26895)
  fix : add sglang script as entry bin for runtime docker image (#26895)
  _Files: `docker/Dockerfile`_
- **2026-06-01** [`53b8378307`](https://github.com/sgl-project/sglang/commit/53b8378307) [#26863](https://github.com/sgl-project/sglang/pull/26863)
  Fix weights_checker checksum for 0-dim tensors and multi-GPU (#26863)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/layers/multimodal.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/mm_utils.py` _+4 more__
- **2026-06-01** [`4b0453f814`](https://github.com/sgl-project/sglang/commit/4b0453f814) [#26530](https://github.com/sgl-project/sglang/pull/26530)
  [diffusion] CI: infer diffusion test sampling params from task type (#26530)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `python/sglang/multimodal_gen/test/test_utils.py`_

## KV Cache / Memory  (42 commits)

- **2026-06-08** [`1ff7c627cd`](https://github.com/sgl-project/sglang/commit/1ff7c627cd) [#27554](https://github.com/sgl-project/sglang/pull/27554)
  [UnifiedTree]: Support hicache metrics (#27554)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-08** [`d03182cd2d`](https://github.com/sgl-project/sglang/commit/d03182cd2d) [#27489](https://github.com/sgl-project/sglang/pull/27489)
  Fix TP deadlock in unified radix cache writing_check / loading_check (#27489)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-08** [`71a0b10462`](https://github.com/sgl-project/sglang/commit/71a0b10462) [#26938](https://github.com/sgl-project/sglang/pull/26938)
  Fix the _chunked_req_scheduled_last_iter flag with a content-based stash gate (#26938)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_chunked_req_gate.py`_
- **2026-06-08** [`3197808283`](https://github.com/sgl-project/sglang/commit/3197808283) [#26547](https://github.com/sgl-project/sglang/pull/26547)
  Avoid calling filter_batch with chunked_req_to_exclude being things unrelated to chunked reqs (#26547)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-06-08** [`6365d6faee`](https://github.com/sgl-project/sglang/commit/6365d6faee) [#27486](https://github.com/sgl-project/sglang/pull/27486)
  [spec] Misc defensive guards for EAGLE draft KV indexing (#27486)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/kvcache.cuh`, `python/sglang/jit_kernel/kvcache.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker.py` _+2 more__
- **2026-06-07** [`0a190d1c97`](https://github.com/sgl-project/sglang/commit/0a190d1c97) [#27446](https://github.com/sgl-project/sglang/pull/27446)
  Fix PP is_fully_idle missing in-flight microbatches (#27446)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/test/scripted_runtime/context/queries.py`, `python/sglang/test/scripted_runtime/scheduler_hook.py`, `test/registered/chunked_prefill/test_scripted_core_4gpu.py`_
- **2026-06-07** [`a39c428d3f`](https://github.com/sgl-project/sglang/commit/a39c428d3f) [#27483](https://github.com/sgl-project/sglang/pull/27483)
  [UnifiedTree][CI]: Reduce HiCache PP KL test concurrency to avoid decode OOM (#27483)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_hicache_pp_kl.py`_
- **2026-06-07** [`0ce3db3c0a`](https://github.com/sgl-project/sglang/commit/0ce3db3c0a) [#27482](https://github.com/sgl-project/sglang/pull/27482)
  [Bug] Fix out-of-range token id crashing tp=1 `VocabParallelEmbedding` (#27482)
  _Files: `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/utils/async_probe.py`, `python/sglang/test/kits/radix_cache_server_kit.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`_
- **2026-06-07** [`52f221cce0`](https://github.com/sgl-project/sglang/commit/52f221cce0) [#26182](https://github.com/sgl-project/sglang/pull/26182)
  Fix Req array token-id concatenation (#26182)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/sampling/custom_logit_processor.py`, `test/manual/test_forward_split_prefill.py` _+4 more__
- **2026-06-07** [`fe548f36b0`](https://github.com/sgl-project/sglang/commit/fe548f36b0) [#27391](https://github.com/sgl-project/sglang/pull/27391)
  [UnifiedTree]: Fix SWA admission budget under-counts HiCache load-back consumption (#27391)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py` _+5 more__
- **2026-06-06** [`4b0f629082`](https://github.com/sgl-project/sglang/commit/4b0f629082) [#27364](https://github.com/sgl-project/sglang/pull/27364)
  [perf] reduce radix cache match overhead by changing the match algorithm (#27364)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`_
- **2026-06-06** [`1c7acba579`](https://github.com/sgl-project/sglang/commit/1c7acba579) [#27458](https://github.com/sgl-project/sglang/pull/27458)
  [spec] Consolidate the per-decode KV alloc reserve into one helper (#27458)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/utils.py`, `python/sglang/srt/mem_cache/common.py` _+2 more__
- **2026-06-06** [`42fe025280`](https://github.com/sgl-project/sglang/commit/42fe025280) [#27285](https://github.com/sgl-project/sglang/pull/27285)
  [HiCache] Fix the compatibility between PP and HiCache (L2). (#27285)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/cache_init_params.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+6 more__
- **2026-06-06** [`bf4f2ccc78`](https://github.com/sgl-project/sglang/commit/bf4f2ccc78) [#27413](https://github.com/sgl-project/sglang/pull/27413)
  Add scripted-runtime unit, core integration, and chunked-prefill tests (#27413)
  _Files: `python/sglang/test/scripted_runtime_chunked_helpers.py`, `test/registered/chunked_prefill/test_scripted_core_1gpu.py`, `test/registered/chunked_prefill/test_scripted_core_4gpu.py`, `test/registered/chunked_prefill/test_scripted_swa_1gpu.py` _+6 more__
- **2026-06-06** [`dd176387c6`](https://github.com/sgl-project/sglang/commit/dd176387c6) [#27411](https://github.com/sgl-project/sglang/pull/27411)
  Add scripted-runtime harness core and wire scheduler/IPC hooks (#27411)
  _Files: `.claude/rules/modify-component-must-read.md`, `.claude/skills/scripted-runtime-notes/SKILL.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py` _+20 more__
- **2026-06-05** [`faa6286946`](https://github.com/sgl-project/sglang/commit/faa6286946) [#27366](https://github.com/sgl-project/sglang/pull/27366)
  [BugFix]: Fix HiMamba HiCache prefetch hang after L3 sidecar transfer  (#27366)
  _Files: `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`_
- **2026-06-05** [`4df1ccdadc`](https://github.com/sgl-project/sglang/commit/4df1ccdadc) [#27330](https://github.com/sgl-project/sglang/pull/27330)
  [UnifiedTree]: Fix CP Reduce For L3 HiCache (#27330)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-05** [`631db6c757`](https://github.com/sgl-project/sglang/commit/631db6c757) [#27264](https://github.com/sgl-project/sglang/pull/27264)
  [UnifiedTree]:  Sync sidecar component hits across TP ranks and make SWA prefetch all-or-nothing (#27264)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-04** [`cd98d97037`](https://github.com/sgl-project/sglang/commit/cd98d97037) [#27303](https://github.com/sgl-project/sglang/pull/27303)
  Use level-1 (quiet) busy memory check in chunked-prefill and streaming tests (#27303)
  _Files: `python/sglang/test/server_fixtures/streaming_session_fixture.py`, `test/registered/scheduler/test_mixed_chunked_prefill.py`_
- **2026-06-04** [`efe24704b7`](https://github.com/sgl-project/sglang/commit/efe24704b7) [#26945](https://github.com/sgl-project/sglang/pull/26945)
  [HiCache] feat: truncate mamba prefetch length to available host KV size (#26945)
  _Files: `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`_
- **2026-06-04** [`133254086b`](https://github.com/sgl-project/sglang/commit/133254086b) [#26941](https://github.com/sgl-project/sglang/pull/26941)
  Plug mamba_extra_buffer ping-pong slot leaks (#26941)
  _Files: `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/session/streaming_session.py`_
- **2026-06-04** [`a10bd785be`](https://github.com/sgl-project/sglang/commit/a10bd785be) [#25000](https://github.com/sgl-project/sglang/pull/25000)
  Reduce mamba prefill allocation overhead (#25000)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-06-04** [`f6cd1a9822`](https://github.com/sgl-project/sglang/commit/f6cd1a9822) [#27174](https://github.com/sgl-project/sglang/pull/27174)
  Add num_waiting_uncached_tokens load metric (#27174)
  _Files: `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+3 more__
- **2026-06-03** [`978fb6ed1a`](https://github.com/sgl-project/sglang/commit/978fb6ed1a) [#27072](https://github.com/sgl-project/sglang/pull/27072)
  hicache kv events: publish split write-through fragments (#27072)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_hiradix_cache_unit.py` _+1 more__
- **2026-06-03** [`e0b692600f`](https://github.com/sgl-project/sglang/commit/e0b692600f) [#27118](https://github.com/sgl-project/sglang/pull/27118)
  [Mamba] extra buffer lazy support (#27118)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/mem_cache/cache_init_params.py` _+10 more__
- **2026-06-03** [`f65aae8493`](https://github.com/sgl-project/sglang/commit/f65aae8493) [#25991](https://github.com/sgl-project/sglang/pull/25991)
  [HiCache] fix: truncate prefetch key on degraded allocation (#25991)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-06-03** [`44d4a25a07`](https://github.com/sgl-project/sglang/commit/44d4a25a07) [#27071](https://github.com/sgl-project/sglang/pull/27071)
  Type hicache transfer hook kwargs in unified cache (#27071)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/full_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py`_
- **2026-06-03** [`63dc20ae6c`](https://github.com/sgl-project/sglang/commit/63dc20ae6c) [#25395](https://github.com/sgl-project/sglang/pull/25395)
  [UnifiedTree] Add CP sync (#25395)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_cp.py`_
- **2026-06-02** [`9e717cae46`](https://github.com/sgl-project/sglang/commit/9e717cae46) [#27038](https://github.com/sgl-project/sglang/pull/27038)
  [sglang] Fix Mamba COW over-releasing SWA locks (cascade-evict assert crash) (#27038)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`_
- **2026-06-02** [`28f9c1ff24`](https://github.com/sgl-project/sglang/commit/28f9c1ff24) [#27070](https://github.com/sgl-project/sglang/pull/27070)
  Relax mamba unified cache kl threshold (#27070)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`_
- **2026-06-02** [`b5e154dc73`](https://github.com/sgl-project/sglang/commit/b5e154dc73) [#27064](https://github.com/sgl-project/sglang/pull/27064)
  Fix stale import after kl_nightly rename (#27064)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_mamba.py`_
- **2026-06-02** [`38d4c9ba88`](https://github.com/sgl-project/sglang/commit/38d4c9ba88) [#26948](https://github.com/sgl-project/sglang/pull/26948)
  Improve type annotations in unified radix cache (#26948)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-06-02** [`ee4bf0a9d3`](https://github.com/sgl-project/sglang/commit/ee4bf0a9d3) [#26927](https://github.com/sgl-project/sglang/pull/26927)
  [UnifiedTree]: Add HiCache Nightly CI For GLM5 (#26927)
  _Files: `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_nightly.py`_
- **2026-06-02** [`d15a2dc72c`](https://github.com/sgl-project/sglang/commit/d15a2dc72c) [#26931](https://github.com/sgl-project/sglang/pull/26931)
  [AMD] dpsk-v4 swa loc cache support (#26931)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-02** [`f40b2ca9d3`](https://github.com/sgl-project/sglang/commit/f40b2ca9d3) [#27003](https://github.com/sgl-project/sglang/pull/27003)
  chore(CODEOWNERS): add allocator/ owners and @alphabetc1 to mem_cache (#27003)
  _Files: `.github/CODEOWNERS`_
- **2026-06-02** [`594ec6335d`](https://github.com/sgl-project/sglang/commit/594ec6335d) [#26939](https://github.com/sgl-project/sglang/pull/26939)
  [Bug Fix][HiCache] Drop @lru_cache on UnifiedTreeNode.get_prefix_hash_values (#26939)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-01** [`167272e785`](https://github.com/sgl-project/sglang/commit/167272e785) [#23179](https://github.com/sgl-project/sglang/pull/23179)
  [LoRA] add lora chunked req test and fix (#23179)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-06-01** [`dff45411da`](https://github.com/sgl-project/sglang/commit/dff45411da) [#16946](https://github.com/sgl-project/sglang/pull/16946)
  [HiCache] Prevent KV cache data loss when radix tree node is split b… (#16946)
  _Files: `python/sglang/srt/mem_cache/hiradix_cache.py`_
- **2026-06-01** [`f59bbef841`](https://github.com/sgl-project/sglang/commit/f59bbef841) [#26919](https://github.com/sgl-project/sglang/pull/26919)
  Split SWA leaf to one window on insert (#26919)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-06-01** [`d8a5a25c36`](https://github.com/sgl-project/sglang/commit/d8a5a25c36) [#25173](https://github.com/sgl-project/sglang/pull/25173)
  Refactor NIXL hicache. Add O_DIRECT support (#25173)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py` _+8 more__
- **2026-06-01** [`6965fe0eec`](https://github.com/sgl-project/sglang/commit/6965fe0eec) [#26615](https://github.com/sgl-project/sglang/pull/26615)
  [sgl] Window-aware LRU refresh for SWA prefix cache in unified cache (#26615)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/__init__.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+1 more__
- **2026-06-01** [`cdd06011a1`](https://github.com/sgl-project/sglang/commit/cdd06011a1) [#26870](https://github.com/sgl-project/sglang/pull/26870)
  Make unified tree SWA hicache tests faithful to write-through backup (#26870)
  _Files: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_

## MoE / Expert Parallel  (30 commits)

- **2026-06-08** [`1f5dc2cdca`](https://github.com/sgl-project/sglang/commit/1f5dc2cdca) [#26786](https://github.com/sgl-project/sglang/pull/26786)
  [GPTQ] Refactor CPU quantization schemes (#26786)
  _Files: `python/sglang/srt/hardware_backend/cpu/quantization/awq_kernels.py`, `python/sglang/srt/hardware_backend/cpu/quantization/gptq_kernels.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/auto_round.py` _+9 more__
- **2026-06-07** [`10d33bd77e`](https://github.com/sgl-project/sglang/commit/10d33bd77e) [#22299](https://github.com/sgl-project/sglang/pull/22299)
  [AMD] Enable Piecewise CUDA Graph for AMD GPUs (#22299)
  _Files: `python/sglang/srt/compilation/cuda_piecewise_backend.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py` _+6 more__
- **2026-06-07** [`4c8a022f38`](https://github.com/sgl-project/sglang/commit/4c8a022f38) [#27191](https://github.com/sgl-project/sglang/pull/27191)
  Fix DeepSeek V4 DP reduce scatter when use attention DP + MoE TP (#27191)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-06-06** [`f57f8a8afd`](https://github.com/sgl-project/sglang/commit/f57f8a8afd) [#26588](https://github.com/sgl-project/sglang/pull/26588)
  Optimize Gemma4 H200 MoE and extend attention (#26588)
  _Files: `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`, `python/sglang/srt/layers/gemma4_fused_ops.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=128,N=704,device_name=NVIDIA_H200.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=128,N=704,device_name=NVIDIA_H200_down.json`_
- **2026-06-06** [`9da88e32e0`](https://github.com/sgl-project/sglang/commit/9da88e32e0) [#27401](https://github.com/sgl-project/sglang/pull/27401)
  [Cohere2Moe] Enable flashinfer_trtllm NVFP4 fused-MoE via SigmoidRenorm routing (#27401)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/models/cohere2_moe.py`_
- **2026-06-05** [`29591594f5`](https://github.com/sgl-project/sglang/commit/29591594f5) [#27150](https://github.com/sgl-project/sglang/pull/27150)
  Support Waterfill with dynamic EPLB (#27150)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/unit/eplb/test_deepep_waterfill_eplb.py`_
- **2026-06-05** [`c9f582a272`](https://github.com/sgl-project/sglang/commit/c9f582a272) [#27329](https://github.com/sgl-project/sglang/pull/27329)
  [LoRA] Experimental fast LoRA path with `experimental_sgl_trtllm` MoE backend for FP8 and NVFP4 models (#27329)
  _Files: `python/sglang/jit_kernel/csrc/trtllm_lora_temp/kimi_k2_moe_fused_gate.cuh`, `python/sglang/jit_kernel/csrc/trtllm_lora_temp/moe_lora_merged_align_kernel.cu`, `python/sglang/jit_kernel/csrc/trtllm_lora_temp/topk_softmax_pack.cuh`, `python/sglang/jit_kernel/trtllm_lora_temp/SOURCE.md` _+48 more__
- **2026-06-04** [`e76d36214b`](https://github.com/sgl-project/sglang/commit/e76d36214b) [#26496](https://github.com/sgl-project/sglang/pull/26496)
  Changes for SM120 perf and usability for NVFP4 (#26496)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/layers/deep_gemm_wrapper/configurer.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_6_0/E=256,N=512,device_name=NVIDIA_RTX_PRO_6000_Blackwell_Server_Edition.json` _+6 more__
- **2026-06-04** [`4cfebbb95f`](https://github.com/sgl-project/sglang/commit/4cfebbb95f) [#25239](https://github.com/sgl-project/sglang/pull/25239)
  [FlashInfer v0.6.12] Support FlashInfer 4over6 NVFP4 (#25239)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`_
- **2026-06-04** [`8e836e7dc9`](https://github.com/sgl-project/sglang/commit/8e836e7dc9) [#26746](https://github.com/sgl-project/sglang/pull/26746)
  Support optional kwargs in AITER fused_moe runner (#26746)
  _Files: `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `test/registered/unit/layers/moe/test_aiter_runner.py`_
- **2026-06-04** [`e4191708c9`](https://github.com/sgl-project/sglang/commit/e4191708c9) [#26845](https://github.com/sgl-project/sglang/pull/26845)
  [Qwen3.5][AMD] Fix shared-expert ×ep_size over-count under allreduce-EP (#26845)
  _Files: `python/sglang/srt/models/qwen2_moe.py`_
- **2026-06-04** [`71c759ebb7`](https://github.com/sgl-project/sglang/commit/71c759ebb7) [#26861](https://github.com/sgl-project/sglang/pull/26861)
  [loader] Reduce transient allocations in NVFP4 MoE setup (#26861)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/quantization/utils.py`_
- **2026-06-04** [`3b7a258f63`](https://github.com/sgl-project/sglang/commit/3b7a258f63) [#21456](https://github.com/sgl-project/sglang/pull/21456)
  [CPU] upgrade dependent torch ver to PT2.12 (#21456)
  _Files: `.github/workflows/pr-test-xeon.yml`, `python/pyproject_cpu.toml`, `python/sglang/multimodal_gen/runtime/utils/common.py`, `python/sglang/srt/utils/common.py` _+7 more__
- **2026-06-03** [`e485ad6ac1`](https://github.com/sgl-project/sglang/commit/e485ad6ac1) [#27120](https://github.com/sgl-project/sglang/pull/27120)
  Fix hybrid linear attention dispatch by layer id with draft-worker awareness (#27120)
  _Files: `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/bailing_moe_linear.py`_
- **2026-06-03** [`293816ab14`](https://github.com/sgl-project/sglang/commit/293816ab14) [#18005](https://github.com/sgl-project/sglang/pull/18005)
  [AMD][MXFP4] Online MXFP4 quantization 1/N - dense and MOE models w. original BF16 weight (#18005)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/constants.py`, `python/sglang/srt/layers/quantization/__init__.py` _+8 more__
- **2026-06-03** [`f790674ad8`](https://github.com/sgl-project/sglang/commit/f790674ad8) [#26839](https://github.com/sgl-project/sglang/pull/26839)
  fix(moe): avoid unpacking None from masked deep_gemm without overlap when sbo enabled (#26839)
  _Files: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`_
- **2026-06-03** [`ac16dbf412`](https://github.com/sgl-project/sglang/commit/ac16dbf412) [#27049](https://github.com/sgl-project/sglang/pull/27049)
  docs: add DeepSeek-V4 EPLB Waterfill tips (#27049)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-06-03** [`202e618898`](https://github.com/sgl-project/sglang/commit/202e618898) [#27116](https://github.com/sgl-project/sglang/pull/27116)
  Revert "Fix hybrid linear attention misrouting plain-RadixAttention linear layers to the full backend (Ring-2.5-1T)" (#27116)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/bailing_moe_linear.py`_
- **2026-06-03** [`b8d7351a74`](https://github.com/sgl-project/sglang/commit/b8d7351a74) [#25655](https://github.com/sgl-project/sglang/pull/25655)
  Feat/add w4a16 moe support to nemotron (#25655)
  _Files: `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/jit_kernel/csrc/gemm/marlin/marlin_template.h`, `python/sglang/jit_kernel/tests/test_gptq_marlin.py` _+15 more__
- **2026-06-03** [`aa510bda45`](https://github.com/sgl-project/sglang/commit/aa510bda45) [#26349](https://github.com/sgl-project/sglang/pull/26349)
  Support specific pass of bias_grouped_topk for xpu (#26349)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/xpu/test_topk.py`_
- **2026-06-03** [`1ebc7438ac`](https://github.com/sgl-project/sglang/commit/1ebc7438ac) [#26106](https://github.com/sgl-project/sglang/pull/26106)
  model: support Command A plus (#26106)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/cohere2_moe.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/function_call/cohere_command4_detector.py` _+5 more__
- **2026-06-02** [`76c9899da7`](https://github.com/sgl-project/sglang/commit/76c9899da7) [#26623](https://github.com/sgl-project/sglang/pull/26623)
  Fix hybrid linear attention misrouting plain-RadixAttention linear layers to the full backend (Ring-2.5-1T) (#26623)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `test/registered/8-gpu-models/test_ling_2_6_flash.py`_
- **2026-06-02** [`b603f08c0c`](https://github.com/sgl-project/sglang/commit/b603f08c0c) [#26643](https://github.com/sgl-project/sglang/pull/26643)
  [DP] Fix FlashInfer dispatcher workspace sizing and set_dp_buffer_len (#26643)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py` _+4 more__
- **2026-06-02** [`4226a6f13a`](https://github.com/sgl-project/sglang/commit/4226a6f13a) [#26884](https://github.com/sgl-project/sglang/pull/26884)
  [AMD] Fix GPT-OSS MXFP4 accuracy on ROCm AITER path (#26884)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-06-02** [`951fa05a09`](https://github.com/sgl-project/sglang/commit/951fa05a09) [#26473](https://github.com/sgl-project/sglang/pull/26473)
  [MoE] Support BF16 standard A2A with DeepGEMM runner (#26473)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/moe/ep_moe/kernels.py` _+1 more__
- **2026-06-01** [`5700790c05`](https://github.com/sgl-project/sglang/commit/5700790c05) [#24947](https://github.com/sgl-project/sglang/pull/24947)
  DeepSeek V4: Support context parallelism with fused MoE (non-DeepEP)  (#24947)
  _Files: `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=256,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=256,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128]_down.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=256,N=256,device_name=NVIDIA_H20-3e,dtype=fp8_w8a8,block_shape=[128, 128].json` _+13 more__
- **2026-06-01** [`524ba10eda`](https://github.com/sgl-project/sglang/commit/524ba10eda) [#24692](https://github.com/sgl-project/sglang/pull/24692)
  feat: SM120 (Blackwell Desktop) support for DeepSeek-V4 inference (#24692)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`, `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/dsv4/indexer.py`, `python/sglang/srt/layers/attention/flash_mla_sm120.py` _+7 more__
- **2026-06-01** [`ff642ed936`](https://github.com/sgl-project/sglang/commit/ff642ed936) [#26303](https://github.com/sgl-project/sglang/pull/26303)
  [MoE] Extend kimi_k2_moe_fused_gate to support 256 experts (MiMo V2 Flash) (#26303)
  _Files: `sgl-kernel/csrc/moe/kimi_k2_moe_fused_gate.cu`, `sgl-kernel/tests/test_kimi_k2_moe_fused_gate.py`_
- **2026-06-01** [`1d7e2f6fb8`](https://github.com/sgl-project/sglang/commit/1d7e2f6fb8) [#22972](https://github.com/sgl-project/sglang/pull/22972)
  [NPU] fix normal DeepEP mode num_tokens_per_rdma_rank error caused by none (#22972)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`_
- **2026-06-01** [`a779791b3f`](https://github.com/sgl-project/sglang/commit/a779791b3f) [#26862](https://github.com/sgl-project/sglang/pull/26862)
  Add random-ids dataset, round-robin expert simulation, and kill_process_tree logging (#26862)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/utils/common.py`, `python/sglang/test/bench_one_batch_server_internal.py`_

## Prefill / Decode Disaggregation  (29 commits)

- **2026-06-08** [`6394a8b381`](https://github.com/sgl-project/sglang/commit/6394a8b381) [#27542](https://github.com/sgl-project/sglang/pull/27542)
  [EPD] Dynamic encoder registration cleanup (#27542)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-06-08** [`8ff0c9fef9`](https://github.com/sgl-project/sglang/commit/8ff0c9fef9) [#27534](https://github.com/sgl-project/sglang/pull/27534)
  [PD] Downgrade propagated rank failure logs from error to debug (#27534)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+2 more__
- **2026-06-08** [`13dda3b8de`](https://github.com/sgl-project/sglang/commit/13dda3b8de) [#22253](https://github.com/sgl-project/sglang/pull/22253)
  [EPD] Support dynamic encoder register (#22253)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/io_struct.py` _+2 more__
- **2026-06-08** [`18d728967a`](https://github.com/sgl-project/sglang/commit/18d728967a) [#26922](https://github.com/sgl-project/sglang/pull/26922)
  [PD][MoRI] Drive KV transfers with a sharded synchronous worker pool (#26922)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/srt/disaggregation/mori/conn.py`, `python/sglang/srt/environ.py`, `test/registered/amd/disaggregation/test_mori_transfer_engine_e2e.py`_
- **2026-06-08** [`259a2da3e0`](https://github.com/sgl-project/sglang/commit/259a2da3e0) [#26637](https://github.com/sgl-project/sglang/pull/26637)
  Refactor Req.fill_ids into full_untruncated_fill_ids + fill_len with equivalence (#26637)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/prefill.py` _+25 more__
- **2026-06-07** [`857ecb2dbc`](https://github.com/sgl-project/sglang/commit/857ecb2dbc) [#27454](https://github.com/sgl-project/sglang/pull/27454)
  [HiSparse & HiCache]Support mooncake store layer first layout (#27454)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`_
- **2026-06-07** [`e57323cae9`](https://github.com/sgl-project/sglang/commit/e57323cae9) [#27256](https://github.com/sgl-project/sglang/pull/27256)
  [mem_cache][4/N] refactor: extract MambaTokenToKVPoolAllocator into allocator/ (#27256)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+14 more__
- **2026-06-06** [`9a48bf75f5`](https://github.com/sgl-project/sglang/commit/9a48bf75f5) [#27427](https://github.com/sgl-project/sglang/pull/27427)
  Add GB300 base C CI suite (#27427)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test.yml`, `.github/workflows/rerun-test.yml`, `scripts/ci/runner_configs.yml` _+5 more__
- **2026-06-05** [`57909f731b`](https://github.com/sgl-project/sglang/commit/57909f731b) [#27372](https://github.com/sgl-project/sglang/pull/27372)
  [PD] Fix KV cache corruption on abort by notifying ongoing prefill (#27372)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`_
- **2026-06-05** [`d01cf27b7d`](https://github.com/sgl-project/sglang/commit/d01cf27b7d) [#27279](https://github.com/sgl-project/sglang/pull/27279)
  [diffusion] model: support Ideogram 4 FP8 (#27279)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/ideogram.py`, `python/sglang/multimodal_gen/configs/models/encoders/__init__.py`, `python/sglang/multimodal_gen/configs/models/encoders/ideogram.py` _+30 more__
- **2026-06-05** [`e1955bf57a`](https://github.com/sgl-project/sglang/commit/e1955bf57a) [#27374](https://github.com/sgl-project/sglang/pull/27374)
  fix(pd): clear stale bootstrap_room when freeing metadata buffer slot (#27374)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-06-05** [`00fefef16b`](https://github.com/sgl-project/sglang/commit/00fefef16b) [#24880](https://github.com/sgl-project/sglang/pull/24880)
  [PD & HiSparse] Add DeepSeek V4 support for HiSparse direct Prefill-to-Decode DRAM (#24880)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/hisparse_transfer.cuh`, `python/sglang/jit_kernel/csrc/hisparse.cuh`, `python/sglang/jit_kernel/dsv4/__init__.py`, `python/sglang/jit_kernel/dsv4/hisparse.py` _+8 more__
- **2026-06-04** [`858e5a5109`](https://github.com/sgl-project/sglang/commit/858e5a5109) [#26119](https://github.com/sgl-project/sglang/pull/26119)
  [diffusion] chore: disagg server args, launch helpers, and warmup utils (#26119)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/disaggregation/disagg_args.py`, `python/sglang/multimodal_gen/runtime/platforms/__init__.py`, `python/sglang/multimodal_gen/runtime/platforms/cpu.py` _+10 more__
- **2026-06-04** [`e541bc3881`](https://github.com/sgl-project/sglang/commit/e541bc3881) [#26576](https://github.com/sgl-project/sglang/pull/26576)
  [EPD] feat: encoder DP mode with per-rank subprocess workers (#26576)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`_
- **2026-06-04** [`736263f3dc`](https://github.com/sgl-project/sglang/commit/736263f3dc) [#26881](https://github.com/sgl-project/sglang/pull/26881)
  [UnifiedTree]: Support l3 storage for swa and deepseek v4 (#26881)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py` _+5 more__
- **2026-06-03** [`03c77dc33d`](https://github.com/sgl-project/sglang/commit/03c77dc33d) [#27085](https://github.com/sgl-project/sglang/pull/27085)
  [PD] Deduplicate PD logprob normalization (#27085)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `test/registered/disaggregation/test_disaggregation_basic.py`_
- **2026-06-03** [`e67810bea7`](https://github.com/sgl-project/sglang/commit/e67810bea7) [#23755](https://github.com/sgl-project/sglang/pull/23755)
  [SGLang Tracing] Add pd disaggregation mooncake backend tracing (#23755)
  _Files: `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/observability/mooncake_trace.py` _+5 more__
- **2026-06-03** [`52f2fe456a`](https://github.com/sgl-project/sglang/commit/52f2fe456a) [#27004](https://github.com/sgl-project/sglang/pull/27004)
  fix(disagg): correct DSA/SWA state-page transfer mismatch in PD disaggregation (#27004)
  _Files: `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/prefill.py`, `test/registered/unit/disaggregation/test_disaggregation_wire.py`_
- **2026-06-03** [`f4e7a98fe5`](https://github.com/sgl-project/sglang/commit/f4e7a98fe5) [#24984](https://github.com/sgl-project/sglang/pull/24984)
  [HiCache] feat: support draft offload for mooncake (#24984)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `python/sglang/test/hicache_spec_storage_common.py` _+2 more__
- **2026-06-03** [`c3aaafc5f2`](https://github.com/sgl-project/sglang/commit/c3aaafc5f2) [#27011](https://github.com/sgl-project/sglang/pull/27011)
  [Bugfix] Clean up failed NIXL sender state (#27011)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`, `test/registered/unit/disaggregation/test_nixl_sender_failure_cleanup.py`_
- **2026-06-02** [`6c69756fa8`](https://github.com/sgl-project/sglang/commit/6c69756fa8) [#26406](https://github.com/sgl-project/sglang/pull/26406)
  NIXL: use prep+make API to improve performance (#26406)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-06-02** [`c2eea4d7b3`](https://github.com/sgl-project/sglang/commit/c2eea4d7b3) [#27028](https://github.com/sgl-project/sglang/pull/27028)
  [Bugfix] Fix orphaned aborted prefill bootstrap requests in PP disaggregation (#27028)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-06-02** [`b55570d38e`](https://github.com/sgl-project/sglang/commit/b55570d38e) [#26780](https://github.com/sgl-project/sglang/pull/26780)
  [PD] Optimistic prefill (#26780)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py` _+7 more__
- **2026-06-02** [`3e993f6140`](https://github.com/sgl-project/sglang/commit/3e993f6140) [#26227](https://github.com/sgl-project/sglang/pull/26227)
  [PD]: Support HiCache prefetching and pd-incremental transfer on decode side (#26227)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_hicache_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/hiradix_cache.py` _+3 more__
- **2026-06-02** [`b562da0d9f`](https://github.com/sgl-project/sglang/commit/b562da0d9f) [#25521](https://github.com/sgl-project/sglang/pull/25521)
  [PD] docs: clarify disaggregation IB device formats (#25521)
  _Files: `docs_new/docs/advanced_features/pd_disaggregation.mdx`, `python/sglang/srt/server_args.py`_
- **2026-06-01** [`693adabff7`](https://github.com/sgl-project/sglang/commit/693adabff7) [#26877](https://github.com/sgl-project/sglang/pull/26877)
  Fix Mamba2Metadata dropping has_mamba_track_mask (#26877)
  _Files: `python/sglang/srt/layers/attention/mamba/mamba2_metadata.py`, `test/registered/disaggregation/test_disaggregation_hybrid_attention.py`_
- **2026-06-01** [`931765e23e`](https://github.com/sgl-project/sglang/commit/931765e23e) [#26607](https://github.com/sgl-project/sglang/pull/26607)
  Do not cap DeepSeek V4 PD prefill by SWA pool size (#26607)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-06-01** [`2394dede0e`](https://github.com/sgl-project/sglang/commit/2394dede0e) [#25669](https://github.com/sgl-project/sglang/pull/25669)
  [EPD][Perf] Async image preprocessing and cross-request ViT batching for encode_server (#25669)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`_
- **2026-06-01** [`f60710a1d7`](https://github.com/sgl-project/sglang/commit/f60710a1d7) [#26905](https://github.com/sgl-project/sglang/pull/26905)
  [AMD] Fix stage-b-test-large-8-gpu-mi35x-disaggregation-amd : switch CACHE_HOST to a fresh path to fix "No space left on device" (#26905)
  _Files: `scripts/ci/amd/amd_ci_start_container_disagg.sh`_

## Scheduler / Batching  (23 commits)

- **2026-06-08** [`f746e4a608`](https://github.com/sgl-project/sglang/commit/f746e4a608) [#26999](https://github.com/sgl-project/sglang/pull/26999)
  Fix fill_len asymmetric assignment statement in ignore-eos branch (#26999)
  _Files: `python/sglang/srt/managers/schedule_policy.py`_
- **2026-06-08** [`9034c2f9ae`](https://github.com/sgl-project/sglang/commit/9034c2f9ae) [#26659](https://github.com/sgl-project/sglang/pull/26659)
  Fix Req fill_len (fill_ids) having dual semantics by restricting to truncated/committed semantics (#26659)
  _Files: `python/sglang/srt/dllm/mixin/req.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-06-08** [`4201de11de`](https://github.com/sgl-project/sglang/commit/4201de11de) [#26548](https://github.com/sgl-project/sglang/pull/26548)
  Extract release_req and retract_all as module-level free functions (#26548)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-06-07** [`14b8f98a21`](https://github.com/sgl-project/sglang/commit/14b8f98a21) [#27445](https://github.com/sgl-project/sglang/pull/27445)
  Complete server warmup before scripted runtime scripts start (#27445)
  _Files: `python/sglang/test/scripted_runtime/http_server.py`, `python/sglang/test/scripted_runtime/scheduler_hook.py`, `python/sglang/test/scripted_runtime/tokenizer_recv_proxy.py`_
- **2026-06-06** [`5a82db85f0`](https://github.com/sgl-project/sglang/commit/5a82db85f0) [#27412](https://github.com/sgl-project/sglang/pull/27412)
  Add scripted-runtime KV-pool and lock-ref exhauster primitives (#27412)
  _Files: `python/sglang/test/scripted_runtime/context/api.py`, `python/sglang/test/scripted_runtime/context/kv_pool_exhauster.py`, `python/sglang/test/scripted_runtime/context/lock_ref_exhauster.py`, `python/sglang/test/scripted_runtime/scheduler_hook.py`_
- **2026-06-06** [`b3e4c204fd`](https://github.com/sgl-project/sglang/commit/b3e4c204fd) [#27405](https://github.com/sgl-project/sglang/pull/27405)
  Don't write crash dump on graceful exit (#27405)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-06-05** [`c06802dc16`](https://github.com/sgl-project/sglang/commit/c06802dc16) [#27205](https://github.com/sgl-project/sglang/pull/27205)
  Fix customized_info incremental streaming (#27205)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_customized_info_streaming.py`_
- **2026-06-04** [`b97a3dbb46`](https://github.com/sgl-project/sglang/commit/b97a3dbb46) [#27258](https://github.com/sgl-project/sglang/pull/27258)
  [HiSparse  PD & PP]Fix HiSparse compatibility with PP decode (#27258)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-06-04** [`8933ec8772`](https://github.com/sgl-project/sglang/commit/8933ec8772) [#26775](https://github.com/sgl-project/sglang/pull/26775)
  fix test cases failed on 5/30 in nightly pipeline (#26775)
  _Files: `python/sglang/test/ascend/test_ascend_utils.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py`, `test/registered/ascend/basic_function/parameter/test_npu_no_overlap_scheduler.py`_
- **2026-06-04** [`a5c7e9d236`](https://github.com/sgl-project/sglang/commit/a5c7e9d236) [#27046](https://github.com/sgl-project/sglang/pull/27046)
  [HiCache] fix PD L3 cache hit details from decode responses (#27046)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-06-04** [`ef170c27b6`](https://github.com/sgl-project/sglang/commit/ef170c27b6) [#27238](https://github.com/sgl-project/sglang/pull/27238)
  Add quiet mode for busy mem check (level 1: buffer + dump on leak) (#27238)
  _Files: `python/sglang/srt/managers/scheduler_components/invariant_checker.py`_
- **2026-06-04** [`e03dfa8182`](https://github.com/sgl-project/sglang/commit/e03dfa8182) [#23751](https://github.com/sgl-project/sglang/pull/23751)
  [3/N][Sync sglang-miles] TITO Support (#23751)
  _Files: `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+3 more__
- **2026-06-04** [`687baf9471`](https://github.com/sgl-project/sglang/commit/687baf9471) [#27145](https://github.com/sgl-project/sglang/pull/27145)
  fix(load-snapshot): avoid duplicate zmq bind in multi-tokenizer mode (#27145)
  _Files: `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+1 more__
- **2026-06-04** [`14ed9b448e`](https://github.com/sgl-project/sglang/commit/14ed9b448e) [#27180](https://github.com/sgl-project/sglang/pull/27180)
  Add ZMQ IPv6 support, bench_serving sampling params, and reduce routed_dp_rank log noise (#27180)
  _Files: `python/sglang/bench_serving.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/load_snapshot.py`, `python/sglang/srt/utils/network.py` _+1 more__
- **2026-06-04** [`7bb5c96685`](https://github.com/sgl-project/sglang/commit/7bb5c96685) [#26757](https://github.com/sgl-project/sglang/pull/26757)
  Trigger scheduler diagnostics on health failure (#26757)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py` _+2 more__
- **2026-06-03** [`61aa3293d3`](https://github.com/sgl-project/sglang/commit/61aa3293d3) [#27187](https://github.com/sgl-project/sglang/pull/27187)
  Revert "Fix TokenizerManager crash on top_logprobs with tensor values" (#27187)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_top_logprobs_tensor.py`_
- **2026-06-03** [`7716fa00e0`](https://github.com/sgl-project/sglang/commit/7716fa00e0) [#26825](https://github.com/sgl-project/sglang/pull/26825)
  Fix TokenizerManager crash on top_logprobs with tensor values (#26825)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_top_logprobs_tensor.py`_
- **2026-06-03** [`e5b8e3a66a`](https://github.com/sgl-project/sglang/commit/e5b8e3a66a) [#24659](https://github.com/sgl-project/sglang/pull/24659)
  Optimize streaming detokenizer updates (#24659)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`_
- **2026-06-02** [`172bd8e6b9`](https://github.com/sgl-project/sglang/commit/172bd8e6b9) [#24003](https://github.com/sgl-project/sglang/pull/24003)
  [scheduler] Zero gen_throughput and flush KV events on pause (#24003)
  _Files: `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-06-01** [`86afa21ca7`](https://github.com/sgl-project/sglang/commit/86afa21ca7) [#25300](https://github.com/sgl-project/sglang/pull/25300)
  feat: optional caller-supplied mm_hashes on GenerateReqInput (#25300)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_mm_hashes.py`_
- **2026-06-01** [`fd16e05252`](https://github.com/sgl-project/sglang/commit/fd16e05252) [#24835](https://github.com/sgl-project/sglang/pull/24835)
  [NPU] fix npu profiler (#24835)
  _Files: `python/sglang/srt/managers/scheduler_components/profiler_manager.py`_
- **2026-06-01** [`afd2d0b2f4`](https://github.com/sgl-project/sglang/commit/afd2d0b2f4) [#26883](https://github.com/sgl-project/sglang/pull/26883)
  [PP][Bugfix] Handle input_ids assignment in prepare_for_extend (#26883)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-06-01** [`11411aa49d`](https://github.com/sgl-project/sglang/commit/11411aa49d) [#24000](https://github.com/sgl-project/sglang/pull/24000)
  [tokenizer] Surface scheduler load info (num_running_reqs / num_waiting_reqs) in meta_info (#24000)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_

## Speculative Decoding  (17 commits)

- **2026-06-06** [`84ca0ffb8c`](https://github.com/sgl-project/sglang/commit/84ca0ffb8c) [#26972](https://github.com/sgl-project/sglang/pull/26972)
  Spec v2 tree drafting (topk>1) with page_size>1 (#26972)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py` _+4 more__
- **2026-06-06** [`280280ace9`](https://github.com/sgl-project/sglang/commit/280280ace9) [#27390](https://github.com/sgl-project/sglang/pull/27390)
  [SPEC] fix: import copy module for eagle sampling info clone (#27390)
  _Files: `python/sglang/srt/speculative/eagle_info.py`_
- **2026-06-06** [`aa5213abb1`](https://github.com/sgl-project/sglang/commit/aa5213abb1) [#27428](https://github.com/sgl-project/sglang/pull/27428)
  [debug] Register #27338 EAGLE draft kv_indices revert in pr_fix_toggle (#27428)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`_
- **2026-06-05** [`2e7523ddbe`](https://github.com/sgl-project/sglang/commit/2e7523ddbe) [#26726](https://github.com/sgl-project/sglang/pull/26726)
  fix(spec-dec): treat `num_nextn_predict_layers=0` the same as absent for EAGLE3 drafts (#26726)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-05** [`6b180959a8`](https://github.com/sgl-project/sglang/commit/6b180959a8) [#24055](https://github.com/sgl-project/sglang/pull/24055)
  [SPEC][5/N] feat: batchsize-aware support for adaptive speculative_num_steps (#24055)
  _Files: `docs_new/docs/advanced_features/adaptive_speculative_decoding.mdx`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/server_args.py` _+7 more__
- **2026-06-05** [`6cbc035dc9`](https://github.com/sgl-project/sglang/commit/6cbc035dc9) [#26859](https://github.com/sgl-project/sglang/pull/26859)
  FrozenKVMTPVerifyInput: add _draft_preprocess_idle call for when all requests in the verify batch finish in the same iteration (#26859)
  _Files: `python/sglang/srt/speculative/frozen_kv_mtp_worker.py`, `test/registered/unit/spec/test_frozen_kv_mtp_all_reqs_finish_in_verify.py`_
- **2026-06-04** [`448d3afb76`](https://github.com/sgl-project/sglang/commit/448d3afb76) [#27300](https://github.com/sgl-project/sglang/pull/27300)
  fix(spec): complete CustomSpecAlgo duck-typing interface and guard against drift (#27300)
  _Files: `python/sglang/srt/speculative/spec_registry.py`, `test/registered/unit/spec/test_spec_registry.py`_
- **2026-06-04** [`1a57145975`](https://github.com/sgl-project/sglang/commit/1a57145975) [#27135](https://github.com/sgl-project/sglang/pull/27135)
  [codex] Fix adaptive metrics test flake (#27135)
  _Files: `test/registered/spec/eagle/test_adaptive_speculative.py`_
- **2026-06-04** [`084c6a7e2a`](https://github.com/sgl-project/sglang/commit/084c6a7e2a) [#26768](https://github.com/sgl-project/sglang/pull/26768)
  Refactor simulated acceptance length generation (#26768)
  _Files: `python/sglang/srt/speculative/spec_utils.py`_
- **2026-06-02** [`c55548ba11`](https://github.com/sgl-project/sglang/commit/c55548ba11) [#26970](https://github.com/sgl-project/sglang/pull/26970)
  [perf] Replicate embed_tokens to drop the post-embed all-reduce (#26970)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/vocab_parallel_embedding.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/deepseek_v2.py` _+1 more__
- **2026-06-02** [`f6d0beaca8`](https://github.com/sgl-project/sglang/commit/f6d0beaca8) [#26981](https://github.com/sgl-project/sglang/pull/26981)
  Revert "Support spec v2 tree drafting (eagle topk>1) with page_size==1" (#26981)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+2 more__
- **2026-06-01** [`4151a04d1a`](https://github.com/sgl-project/sglang/commit/4151a04d1a) [#26424](https://github.com/sgl-project/sglang/pull/26424)
  [Perf][Spec Decoding] Skip cat/topk/sort/gather in draft_forward for topk=1 (#26424)
  _Files: `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/standalone_worker_v2.py`, `test/registered/unit/spec/test_eagle_worker_v2_topk1_fastpath.py`_
- **2026-06-01** [`1d4ee060c2`](https://github.com/sgl-project/sglang/commit/1d4ee060c2) [#26866](https://github.com/sgl-project/sglang/pull/26866)
  Support spec v2 tree drafting (eagle topk>1) with page_size==1 (#26866)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py` _+2 more__
- **2026-06-01** [`a0670b5ba3`](https://github.com/sgl-project/sglang/commit/a0670b5ba3) [#25940](https://github.com/sgl-project/sglang/pull/25940)
  [SPEC] feat: add adaptive speculative decoding metrics (#25940)
  _Files: `docs_new/docs/references/production_metrics.mdx`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/observability/metrics_collector.py`, `test/registered/spec/eagle/test_adaptive_speculative.py`_
- **2026-06-01** [`1f8d3c7a42`](https://github.com/sgl-project/sglang/commit/1f8d3c7a42) [#25644](https://github.com/sgl-project/sglang/pull/25644)
  [Speculative] [NPU] Adaptive-SD NPU support (#25644)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-01** [`1bff7a290f`](https://github.com/sgl-project/sglang/commit/1bff7a290f) [#26871](https://github.com/sgl-project/sglang/pull/26871)
  Refactor EAGLE infer tests: shared fixture + kits + overlap matrix (#26871)
  _Files: `python/sglang/test/kits/spec_server_kits.py`, `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_eagle_infer_a.py`, `test/registered/spec/eagle/test_eagle_infer_b.py` _+8 more__
- **2026-06-01** [`d078cb72bd`](https://github.com/sgl-project/sglang/commit/d078cb72bd) [#26903](https://github.com/sgl-project/sglang/pull/26903)
  [NPU] [DOC] clarify Ascend NPU exclusive supported values for speculative args (#26903)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_

## Models  (16 commits)

- **2026-06-08** [`d1777d1f6d`](https://github.com/sgl-project/sglang/commit/d1777d1f6d) [#26885](https://github.com/sgl-project/sglang/pull/26885)
  Cookbook renovation (#26885)
  _Files: `.claude/skills/cookbook-add-model/SKILL.md`, `.claude/skills/cookbook-add-model/references/authoring-reference.md`, `.claude/skills/cookbook-add-model/references/engine-axis.md`, `.claude/skills/cookbook-add-model/references/mintlify-authoring.md` _+12 more__
- **2026-06-08** [`2d1856bf45`](https://github.com/sgl-project/sglang/commit/2d1856bf45) [#10950](https://github.com/sgl-project/sglang/pull/10950)
  Support encoder_decoder on cpu_graph_runner (#10950)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/models/mllama.py`_
- **2026-06-06** [`163fafba51`](https://github.com/sgl-project/sglang/commit/163fafba51) [#27419](https://github.com/sgl-project/sglang/pull/27419)
  fix test_qwen3_next_models flaky (#27419)
  _Files: `test/registered/models_e2e/test_qwen3_next_models.py`_
- **2026-06-06** [`caeb449cd6`](https://github.com/sgl-project/sglang/commit/caeb449cd6) [#27248](https://github.com/sgl-project/sglang/pull/27248)
  [Doc][CPU]Update Cookbook with Xeon support info (#27248)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-OCR-2.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-OCR.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-R1.mdx`, `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V3.mdx` _+22 more__
- **2026-06-05** [`e69cc07a60`](https://github.com/sgl-project/sglang/commit/e69cc07a60) [#27404](https://github.com/sgl-project/sglang/pull/27404)
  Remove DeepSeek V4 release Docker workflow (#27404)
  _Files: `.github/workflows/release-docker-deepseek-v4.yml`_
- **2026-06-05** [`bf172c492a`](https://github.com/sgl-project/sglang/commit/bf172c492a) [#27396](https://github.com/sgl-project/sglang/pull/27396)
  Cookbook for QAT (#27396)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`, `docs_new/src/snippets/autoregressive/gemma4-deployment.jsx`_
- **2026-06-05** [`d8487bad06`](https://github.com/sgl-project/sglang/commit/d8487bad06) [#27353](https://github.com/sgl-project/sglang/pull/27353)
  Update best practice for qwen3-next-80b-a3b-instruct (#27353)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-06-05** [`aed0808e18`](https://github.com/sgl-project/sglang/commit/aed0808e18) [#27335](https://github.com/sgl-project/sglang/pull/27335)
  6-5 nightly failed test case fix (#27335)
  _Files: `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v3_2_w8a8.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_480b.py`_
- **2026-06-05** [`7425bebb6c`](https://github.com/sgl-project/sglang/commit/7425bebb6c) [#27321](https://github.com/sgl-project/sglang/pull/27321)
  docs(cookbook): restore Gemma 4 transformers commit pin (#27321)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`_
- **2026-06-04** [`0e4aa081ba`](https://github.com/sgl-project/sglang/commit/0e4aa081ba) [#27296](https://github.com/sgl-project/sglang/pull/27296)
  Add --enable-symm-mem for Qwen3.5 (#27296)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-06-04** [`75be922451`](https://github.com/sgl-project/sglang/commit/75be922451) [#27287](https://github.com/sgl-project/sglang/pull/27287)
  docs(cookbook): add Docker install option for Gemma 4 (#27287)
  _Files: `docs_new/cookbook/autoregressive/Google/Gemma4.mdx`_
- **2026-06-04** [`4167f211b1`](https://github.com/sgl-project/sglang/commit/4167f211b1) [#27027](https://github.com/sgl-project/sglang/pull/27027)
  Solving the problem of test case failures caused by timeouts (#27027)
  _Files: `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v3_2_w8a8.py`_
- **2026-06-04** [`364c2bfea8`](https://github.com/sgl-project/sglang/commit/364c2bfea8) [#26933](https://github.com/sgl-project/sglang/pull/26933)
  Test case restoration in the full test. (#26933)
  _Files: `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v3_2_w8a8.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_480b.py`, `test/registered/ascend/llm_models/test_npu_c4ai_command_r_v01.py`, `test/registered/ascend/llm_models/test_npu_exaone_3.py` _+2 more__
- **2026-06-04** [`10b6b45cad`](https://github.com/sgl-project/sglang/commit/10b6b45cad) [#27035](https://github.com/sgl-project/sglang/pull/27035)
  docs: add DeepSeek V4 FP4 indexer usage (#27035)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`_
- **2026-06-01** [`2fdae94e46`](https://github.com/sgl-project/sglang/commit/2fdae94e46) [#26968](https://github.com/sgl-project/sglang/pull/26968)
  docs: update RTX PRO 6000 deployment snippet (#26968)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-06-01** [`106092123f`](https://github.com/sgl-project/sglang/commit/106092123f) [#24435](https://github.com/sgl-project/sglang/pull/24435)
  Update Qwen3-Coder docs_new NVIDIA guidance (#24435)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3-Coder.mdx`, `docs_new/src/snippets/autoregressive/qwen3-coder-deployment.jsx`_

## Other  (15 commits)

- **2026-06-08** [`f5fdf9c5d8`](https://github.com/sgl-project/sglang/commit/f5fdf9c5d8) [#26874](https://github.com/sgl-project/sglang/pull/26874)
  Speed up dump comparator percentile computation using numpy (#26874)
  _Files: `python/sglang/srt/debug_utils/comparator/tensor_comparator/comparator.py`, `test/registered/debug_utils/comparator/tensor_comparator/test_comparator.py`_
- **2026-06-08** [`6bc3953b48`](https://github.com/sgl-project/sglang/commit/6bc3953b48) [#27394](https://github.com/sgl-project/sglang/pull/27394)
  feat(agentic router): add sticky-session routing policy (#27394)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/active_load.rs` _+22 more__
- **2026-06-07** [`80eee2d92c`](https://github.com/sgl-project/sglang/commit/80eee2d92c) [#27478](https://github.com/sgl-project/sglang/pull/27478)
  [Spec] Guard async-assert probes against `None` tensor (#27478)
  _Files: `python/sglang/srt/utils/async_probe.py`_
- **2026-06-06** [`99cf0a4399`](https://github.com/sgl-project/sglang/commit/99cf0a4399) [#27426](https://github.com/sgl-project/sglang/pull/27426)
  Fix flaky test_self_e2e_pd_perturb (#27426)
  _Files: `python/sglang/test/kv_canary/pd_fixture.py`, `test/registered/kv_canary/test_self_e2e_pd_perturb.py`_
- **2026-06-06** [`21201ef718`](https://github.com/sgl-project/sglang/commit/21201ef718) [#27410](https://github.com/sgl-project/sglang/pull/27410)
  Add kv_canary PP self-test fixture and SWA divergence coverage (#27410)
  _Files: `python/sglang/srt/kv_canary/runner/swa_divergence.py`, `python/sglang/test/kv_canary/e2e_base.py`, `python/sglang/test/kv_canary/pp_fixture.py`, `python/sglang/test/kv_canary/utils.py` _+4 more__
- **2026-06-05** [`6a3316dd1e`](https://github.com/sgl-project/sglang/commit/6a3316dd1e) [#25337](https://github.com/sgl-project/sglang/pull/25337)
  [plugin] default device detection fixes for OOT platform plugins (#25337)
  _Files: `python/sglang/srt/configs/device_config.py`, `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/platforms/__init__.py` _+3 more__
- **2026-06-05** [`6cfdc18585`](https://github.com/sgl-project/sglang/commit/6cfdc18585) [#27358](https://github.com/sgl-project/sglang/pull/27358)
  HiCache: Fix Flaky CI For 3FS Backend (#27358)
  _Files: `test/registered/hicache/test_hicache_storage_3fs_backend.py`_
- **2026-06-04** [`5bf90ad988`](https://github.com/sgl-project/sglang/commit/5bf90ad988) [#23979](https://github.com/sgl-project/sglang/pull/23979)
  Enable DeepGEMM PDL on by default (#23979)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`_
- **2026-06-04** [`ff5c4d7b57`](https://github.com/sgl-project/sglang/commit/ff5c4d7b57) [#27213](https://github.com/sgl-project/sglang/pull/27213)
  Add zx3xyy to CI_PERMISSIONS.json (#27213)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-06-03** [`eda21f6839`](https://github.com/sgl-project/sglang/commit/eda21f6839) [#25773](https://github.com/sgl-project/sglang/pull/25773)
  Add fused_rope and for xpu (#25773)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`_
- **2026-06-02** [`f531bd7ff3`](https://github.com/sgl-project/sglang/commit/f531bd7ff3) [#27014](https://github.com/sgl-project/sglang/pull/27014)
  [Bug] Fix circular import in `forward_batch_info` from runtime `cp_utils` import (#27014)
  _Files: `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-06-02** [`9fe8b72912`](https://github.com/sgl-project/sglang/commit/9fe8b72912) [#26567](https://github.com/sgl-project/sglang/pull/26567)
  Speed up DeepGEMM JIT warmup with per-PP-rank parallel compile (#26567)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-01** [`3bce192bd2`](https://github.com/sgl-project/sglang/commit/3bce192bd2) [#26965](https://github.com/sgl-project/sglang/pull/26965)
  [misc] update adaptive spec decoding code owners (#26965)
  _Files: `.github/CODEOWNERS`_
- **2026-06-01** [`dfa1af99f5`](https://github.com/sgl-project/sglang/commit/dfa1af99f5) [#26964](https://github.com/sgl-project/sglang/pull/26964)
  Fix kill_process_tree reap wait crashing on pidfd EINVAL (#26964)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-06-01** [`61cc70e8aa`](https://github.com/sgl-project/sglang/commit/61cc70e8aa) [#26481](https://github.com/sgl-project/sglang/pull/26481)
  Fixed incorrect indexing for slot 0 compatibility (#26481)
  _Files: `python/sglang/bench_one_batch.py`_

## CI / Build  (13 commits)

- **2026-06-06** [`4989d6691d`](https://github.com/sgl-project/sglang/commit/4989d6691d) [#27457](https://github.com/sgl-project/sglang/pull/27457)
  ci: show partition fit window as a date range in the step summary (#27457)
  _Files: `scripts/ci/update_est_time.py`, `scripts/ci/utils/compute_partitions.py`_
- **2026-06-06** [`9f28512737`](https://github.com/sgl-project/sglang/commit/9f28512737) [#26731](https://github.com/sgl-project/sglang/pull/26731)
  [NPU] Update documentation for software version upgrades (#26731)
  _Files: `.github/workflows/full-test-npu.yml`, `.github/workflows/nightly-test-npu.yml`, `docker/npu.Dockerfile`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx` _+2 more__
- **2026-06-05** [`d381ec7997`](https://github.com/sgl-project/sglang/commit/d381ec7997) [#27284](https://github.com/sgl-project/sglang/pull/27284)
  [CI] Fix Nemotron nightly mixed precision checkpoints test (#27284)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-06-05** [`86b9bf5812`](https://github.com/sgl-project/sglang/commit/86b9bf5812) [#27388](https://github.com/sgl-project/sglang/pull/27388)
  [CI]: Fix CI Stage for 3fs backend test (#27388)
  _Files: `test/registered/hicache/test_hicache_storage_3fs_backend.py`_
- **2026-06-05** [`088f70d0c0`](https://github.com/sgl-project/sglang/commit/088f70d0c0) [#27318](https://github.com/sgl-project/sglang/pull/27318)
  ci: open the LMSYS blog-sync PR with the repo sglang-bot (#27318)
  _Files: `.github/workflows/sync-lmsys-sglang-blogs.yml`_
- **2026-06-04** [`47377525cb`](https://github.com/sgl-project/sglang/commit/47377525cb) [#27179](https://github.com/sgl-project/sglang/pull/27179)
  ci: fix LMSYS blog sync to open a PR via gh and only run on main (#27179)
  _Files: `.github/workflows/sync-lmsys-sglang-blogs.yml`_
- **2026-06-04** [`0783813fdf`](https://github.com/sgl-project/sglang/commit/0783813fdf) [#27092](https://github.com/sgl-project/sglang/pull/27092)
  ci: cache HF hub for base-a-test-cpu to avoid Hub 429 flakes (#27092)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-06-04** [`0e0ecc11ff`](https://github.com/sgl-project/sglang/commit/0e0ecc11ff) [#27182](https://github.com/sgl-project/sglang/pull/27182)
  Add nightly Intel XPU Docker release workflow (#27182)
  _Files: `.github/workflows/release-docker-intel-xpu-nightly.yml`_
- **2026-06-03** [`b678448b8a`](https://github.com/sgl-project/sglang/commit/b678448b8a) [#26904](https://github.com/sgl-project/sglang/pull/26904)
  ci(xeon): merge 2 partitions into 1 job to reduce runner contention (#26904)
  _Files: `.github/workflows/pr-test-xeon.yml`, `docker/xeon.Dockerfile`, `docs_new/docs/hardware-platforms/xpu.mdx`, `python/sglang/bench_one_batch.py`_
- **2026-06-02** [`68caf49154`](https://github.com/sgl-project/sglang/commit/68caf49154) [#26993](https://github.com/sgl-project/sglang/pull/26993)
  Update sgl-deep-gemm to 0.1.2 (#26993)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`_
- **2026-06-02** [`54143264bf`](https://github.com/sgl-project/sglang/commit/54143264bf) [#26990](https://github.com/sgl-project/sglang/pull/26990)
  ci: disable cross-job fast-fail for run_all_tests dispatch (#26990)
  _Files: `.github/workflows/_pr-test-stage.yml`_
- **2026-06-02** [`5e63200064`](https://github.com/sgl-project/sglang/commit/5e63200064) [#26986](https://github.com/sgl-project/sglang/pull/26986)
  ci: full parallelism for run_all_tests dispatch (#26986)
  _Files: `.github/workflows/_pr-test-check-changes.yml`_
- **2026-06-01** [`1ee189831f`](https://github.com/sgl-project/sglang/commit/1ee189831f) [#26682](https://github.com/sgl-project/sglang/pull/26682)
  [CI] Bump xeon PR test unit tests timeout to 60 minutes (#26682)
  _Files: `.github/workflows/pr-test-xeon.yml`_

## Tensor / Data Parallel  (10 commits)

- **2026-06-08** [`995e649190`](https://github.com/sgl-project/sglang/commit/995e649190) [#26850](https://github.com/sgl-project/sglang/pull/26850)
  Add parallel-rank dump filenames and pipeline-global layer remapping to dumper (#26850)
  _Files: `python/sglang/srt/debug_utils/dumper.py`, `test/registered/debug_utils/test_dumper.py`_
- **2026-06-07** [`db58e76c33`](https://github.com/sgl-project/sglang/commit/db58e76c33) [#27492](https://github.com/sgl-project/sglang/pull/27492)
  Add all_to_all_single to GroupCoordinator (#27492)
  _Files: `python/sglang/srt/distributed/parallel_state.py`_
- **2026-06-05** [`e4a7388187`](https://github.com/sgl-project/sglang/commit/e4a7388187) [#26480](https://github.com/sgl-project/sglang/pull/26480)
  feat(agentic router, 1/N): Add LoadBasedPolicy (#26480)
  _Files: `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/types.rs`, `experimental/sgl-router/src/policies/factory.rs`, `experimental/sgl-router/src/policies/load_based.rs` _+2 more__
- **2026-06-04** [`6dcd78a37f`](https://github.com/sgl-project/sglang/commit/6dcd78a37f) [#27126](https://github.com/sgl-project/sglang/pull/27126)
  [AMD] Add MiniMax-M2.5 TP=4 nightly accuracy test for MI355X (#27126)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_minimax_m25_tp4_eval_mi35x.py`_
- **2026-06-03** [`90985117a5`](https://github.com/sgl-project/sglang/commit/90985117a5) [#27184](https://github.com/sgl-project/sglang/pull/27184)
  docs: fix Nemotron Super MTP deployment command (spec-v2 + B200) (#27184)
  _Files: `docs_new/src/snippets/autoregressive/nemotron3-super-deployment.jsx`_
- **2026-06-03** [`6d53615699`](https://github.com/sgl-project/sglang/commit/6d53615699) [#27101](https://github.com/sgl-project/sglang/pull/27101)
  [Gemma4] Use hard GSM8K accuracy floor for 31B MTP test (#27101)
  _Files: `test/registered/spec/test_gemma4_mtp_31b_extra.py`_
- **2026-06-02** [`72929c7000`](https://github.com/sgl-project/sglang/commit/72929c7000) [#25093](https://github.com/sgl-project/sglang/pull/25093)
  [AMD] Enable AITER custom all-gather on ROCm (#25093)
  _Files: `benchmark/kernels/all_gather/benchmark_aiter.py`, `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `test/registered/ops/test_aiter_allgather_amd.py`_
- **2026-06-02** [`22bb9a6421`](https://github.com/sgl-project/sglang/commit/22bb9a6421) [#27082](https://github.com/sgl-project/sglang/pull/27082)
  test: disable test_gemma4_mtp_26b_a4b_extra from CI (#27082)
  _Files: `test/registered/spec/test_gemma4_mtp_26b_a4b_extra.py`_
- **2026-06-01** [`cb8a103b81`](https://github.com/sgl-project/sglang/commit/cb8a103b81) [#26953](https://github.com/sgl-project/sglang/pull/26953)
  chore: add @pyc96 as codeowner for FrozenKVMTP module (#26953)
  _Files: `.github/CODEOWNERS`_
- **2026-06-01** [`3aaf8f115e`](https://github.com/sgl-project/sglang/commit/3aaf8f115e) [#26714](https://github.com/sgl-project/sglang/pull/26714)
  fix test cases failed in nightly pipeline (#26714)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `test/registered/ascend/llm_models/test_ascend_minimax_m2.py`_

## Triton / Kernels  (10 commits)

- **2026-06-06** [`9097647090`](https://github.com/sgl-project/sglang/commit/9097647090) [#27407](https://github.com/sgl-project/sglang/pull/27407)
  Route the eager forward path through the CUDA graph input-buffer registry (#27407)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/unit/batch_overlap/test_tbo_filter_batch_marker.py` _+1 more__
- **2026-06-06** [`e513c13e2e`](https://github.com/sgl-project/sglang/commit/e513c13e2e) [#24756](https://github.com/sgl-project/sglang/pull/24756)
  Optimize ngram decode token table update (#24756)
  _Files: `python/sglang/jit_kernel/benchmark/bench_ngram_update_token_table.py`, `python/sglang/jit_kernel/csrc/ngram_embedding.cuh`, `python/sglang/jit_kernel/ngram_embedding.py`, `python/sglang/jit_kernel/tests/test_ngram_embedding.py` _+1 more__
- **2026-06-06** [`58a05d3dd2`](https://github.com/sgl-project/sglang/commit/58a05d3dd2) [#27344](https://github.com/sgl-project/sglang/pull/27344)
  [CI] Isolate CUDA coredump dir per run to fix tracker mis-attribution (#27344)
  _Files: `.github/actions/upload-cuda-coredumps/action.yml`, `python/sglang/srt/debug_utils/cuda_coredump.py`, `python/sglang/srt/environ.py`_
- **2026-06-05** [`e7f94d0d40`](https://github.com/sgl-project/sglang/commit/e7f94d0d40) [#26444](https://github.com/sgl-project/sglang/pull/26444)
  [Bug Fix] Fix activation.cuh JIT compilation failure on CUDA 13 due to template type/value mismatch (#26444)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`_
- **2026-06-04** [`10ab7c919f`](https://github.com/sgl-project/sglang/commit/10ab7c919f) [#27192](https://github.com/sgl-project/sglang/pull/27192)
  [refactor] Retire DecodeInputBuffers / PrefillInputBuffers in favor of CudaGraphBufferRegistry (#27192)
  _Files: `python/sglang/srt/model_executor/breakable_cuda_graph_runner.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/input_buffers.py` _+3 more__
- **2026-06-03** [`45604a0f4a`](https://github.com/sgl-project/sglang/commit/45604a0f4a) [#26742](https://github.com/sgl-project/sglang/pull/26742)
  [refactor] Unify CUDA graph runner input buffers behind CudaGraphBufferRegistry (#26742)
  _Files: `python/sglang/srt/model_executor/breakable_cuda_graph_runner.py`, `python/sglang/srt/model_executor/cuda_graph_buffer_registry.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/input_buffers.py` _+2 more__
- **2026-06-03** [`512bfbb1e1`](https://github.com/sgl-project/sglang/commit/512bfbb1e1) [#26145](https://github.com/sgl-project/sglang/pull/26145)
  [CPU] Explicitly enable AVX512 & AMX instruction set (#26145)
  _Files: `sgl-kernel/csrc/cpu/CMakeLists.txt`_
- **2026-06-02** [`365cc2ade5`](https://github.com/sgl-project/sglang/commit/365cc2ade5) [#26994](https://github.com/sgl-project/sglang/pull/26994)
  jit_kernel tests: bump multiprocess_test timeout 90s -> 240s (cold JIT cache) (#26994)
  _Files: `python/sglang/jit_kernel/tests/utils.py`_
- **2026-06-02** [`84e1108312`](https://github.com/sgl-project/sglang/commit/84e1108312) [#24757](https://github.com/sgl-project/sglang/pull/24757)
  Optimize ngram decode id computation (#24757)
  _Files: `python/sglang/jit_kernel/benchmark/bench_ngram_compute_decode.py`, `python/sglang/jit_kernel/csrc/ngram_embedding.cuh`, `python/sglang/jit_kernel/ngram_embedding.py`, `python/sglang/jit_kernel/tests/test_ngram_embedding.py` _+1 more__
- **2026-06-02** [`5ae8d286d2`](https://github.com/sgl-project/sglang/commit/5ae8d286d2) [#26502](https://github.com/sgl-project/sglang/pull/26502)
  perf(gemma4): single-launch fused router (topk + softmax + scale) (#26502)
  _Files: `python/sglang/srt/layers/gemma4_fused_ops.py`, `python/sglang/srt/models/gemma4_causal.py`, `test/registered/kernels/test_gemma4_fused_routing.py`_

## Docs / Examples  (10 commits)

- **2026-06-05** [`632a3d480e`](https://github.com/sgl-project/sglang/commit/632a3d480e) [#27400](https://github.com/sgl-project/sglang/pull/27400)
  docs: add Tencent Hunyuan and Poolside cards to autoregressive cookbook (#27400)
  _Files: `docs_new/cards/logos/poolside.png`, `docs_new/cards/logos/tencent.png`, `docs_new/cookbook/autoregressive/intro.mdx`_
- **2026-06-05** [`4248695b07`](https://github.com/sgl-project/sglang/commit/4248695b07) [#27032](https://github.com/sgl-project/sglang/pull/27032)
  [NPU] add GLM model best practice docs (#27032)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-06-05** [`bba8de8cb4`](https://github.com/sgl-project/sglang/commit/bba8de8cb4) [#27322](https://github.com/sgl-project/sglang/pull/27322)
  docs: sync LMSYS SGLang blog cards (#27322)
  _Files: `docs_new/index.mdx`_
- **2026-06-04** [`b89686710d`](https://github.com/sgl-project/sglang/commit/b89686710d) [#27240](https://github.com/sgl-project/sglang/pull/27240)
  [Docs] re-organize nemotron cookbook (#27240)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx`, `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json`_
- **2026-06-04** [`1463e5fbdd`](https://github.com/sgl-project/sglang/commit/1463e5fbdd) [#26969](https://github.com/sgl-project/sglang/pull/26969)
  docs: add Nemotron 3 Ultra cookbook entry (#26969)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Ultra.mdx`, `docs_new/cookbook/intro copy.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/autoregressive/nemotron3-ultra-deployment.jsx`_
- **2026-06-03** [`8980eb82de`](https://github.com/sgl-project/sglang/commit/8980eb82de) [#25198](https://github.com/sgl-project/sglang/pull/25198)
  [Docs] Update Nemotron3-Nano-Omni cookbook to reflect new model paths (#25198)
  _Files: `docs_new/cookbook/autoregressive/NVIDIA/Nemotron3-Nano-Omni.mdx`, `docs_new/src/snippets/autoregressive/nemotron3-nano-omni-deployment.jsx`_
- **2026-06-02** [`7271318dc3`](https://github.com/sgl-project/sglang/commit/7271318dc3) [#27050](https://github.com/sgl-project/sglang/pull/27050)
  【docs】The remote weight download function has been adjusted to be unsupported until the PTA interface is fixed. (#27050)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-06-02** [`f27fa0da93`](https://github.com/sgl-project/sglang/commit/f27fa0da93) [#26774](https://github.com/sgl-project/sglang/pull/26774)
  [NPU][Docs] Kimi-K2.5 best practice (#26774)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_kimi_k2.5_examples.mdx`_
- **2026-06-02** [`1c0019da75`](https://github.com/sgl-project/sglang/commit/1c0019da75) [#26384](https://github.com/sgl-project/sglang/pull/26384)
  [Docs] GLM-4.7 cookbook: add NVIDIA Blackwell (B200, GB200) + NVFP4 sections (#26384)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-4.7.mdx`, `docs_new/src/snippets/autoregressive/glm-47-deployment.jsx`_
- **2026-06-01** [`4d20dc44fc`](https://github.com/sgl-project/sglang/commit/4d20dc44fc) [#26725](https://github.com/sgl-project/sglang/pull/26725)
  【NPU】add MiniMax2.5 best practice docs (#26725)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_

## ROCm / AMD  (9 commits)

- **2026-06-08** [`df6b9c2d9d`](https://github.com/sgl-project/sglang/commit/df6b9c2d9d) [#27538](https://github.com/sgl-project/sglang/pull/27538)
  [AMD] ci: reinstall MoRI if Different from Dockerfile-pinned commit during install_dependency (#27538)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-06-08** [`1aa5040c74`](https://github.com/sgl-project/sglang/commit/1aa5040c74) [#27530](https://github.com/sgl-project/sglang/pull/27530)
  Update code owners (AMD) (#27530)
  _Files: `.github/CODEOWNERS`_
- **2026-06-05** [`7f919edf00`](https://github.com/sgl-project/sglang/commit/7f919edf00) [#25885](https://github.com/sgl-project/sglang/pull/25885)
  [AMD] Support alt stream for Qwen3.5 on AMD platform (#25885)
  _Files: `python/sglang/srt/models/qwen3_5.py`_
- **2026-06-05** [`8c8281801d`](https://github.com/sgl-project/sglang/commit/8c8281801d) [#27376](https://github.com/sgl-project/sglang/pull/27376)
  [AMD] update ROCm AITER commit (#27376)
  _Files: `docker/rocm.Dockerfile`_
- **2026-06-05** [`66b932154f`](https://github.com/sgl-project/sglang/commit/66b932154f) [#27352](https://github.com/sgl-project/sglang/pull/27352)
  [AMD] fix(ci): run partition 3 of stage-c-test-large-8-gpu-amd (#27352)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-06-04** [`04c16fc1e5`](https://github.com/sgl-project/sglang/commit/04c16fc1e5) [#27232](https://github.com/sgl-project/sglang/pull/27232)
  [AMD][CI] Remove transformers pin from GLM-5.x nightly jobs (#27232)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`_
- **2026-06-02** [`2582134a59`](https://github.com/sgl-project/sglang/commit/2582134a59) [#26677](https://github.com/sgl-project/sglang/pull/26677)
  [AMD] Add amd ci mamba state scatter test (#26677)
  _Files: `test/registered/unit/layers/test_mamba_state_scatter_triton.py`_
- **2026-06-01** [`89410b380b`](https://github.com/sgl-project/sglang/commit/89410b380b) [#26879](https://github.com/sgl-project/sglang/pull/26879)
  [AMD] Pin compressed-tensors==0.15.0 to fix ROCm nightly build (#26879)
  _Files: `python/pyproject_other.toml`_
- **2026-06-01** [`b14fba17d9`](https://github.com/sgl-project/sglang/commit/b14fba17d9) [#26909](https://github.com/sgl-project/sglang/pull/26909)
  [AMD] make bypass-fastfail label also disable within-suite fast-fail (#26909)
  _Files: `.github/workflows/pr-test-amd.yml`_

## Quantization  (9 commits)

- **2026-06-08** [`5bf7dd8e4a`](https://github.com/sgl-project/sglang/commit/5bf7dd8e4a) [#27496](https://github.com/sgl-project/sglang/pull/27496)
  Update SGLang diffusion skills (#27496)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-add-model/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/references/ako-loop.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/scripts/ensure_ako4all_clean.sh` _+6 more__
- **2026-06-07** [`02be2e7189`](https://github.com/sgl-project/sglang/commit/02be2e7189) [#27393](https://github.com/sgl-project/sglang/pull/27393)
  [diffusion] support tp for ideogram4 (#27393)
  _Files: `python/sglang/multimodal_gen/configs/models/vocoder/ltx_vocoder.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/bitsandbytes.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/weight_only_fp8.py`, `python/sglang/multimodal_gen/runtime/loader/fsdp_load.py` _+7 more__
- **2026-06-07** [`52a5c01eba`](https://github.com/sgl-project/sglang/commit/52a5c01eba) [#25347](https://github.com/sgl-project/sglang/pull/25347)
  [plugin] enable OOT platforms to provide custom quant configs (#25347)
  _Files: `docs_new/docs/hardware-platforms/plugin.mdx`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/platforms/interface.py`_
- **2026-06-07** [`5da265de30`](https://github.com/sgl-project/sglang/commit/5da265de30) [#22300](https://github.com/sgl-project/sglang/pull/22300)
  [NVIDIA] Fix FP8 gemm performance with fp16 models (MInimax-M2.5) (#22300)
  _Files: `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/fp8_utils.py`, `python/sglang/srt/model_loader/utils.py`_
- **2026-06-06** [`bf66b7b6da`](https://github.com/sgl-project/sglang/commit/bf66b7b6da) [#27379](https://github.com/sgl-project/sglang/pull/27379)
  [diffusion] model: support Ideogram4 NVFP4 (#27379)
  _Files: `docs_new/cards/logos/ideogram.png`, `docs_new/cookbook/diffusion/Ideogram/Ideogram4.mdx`, `docs_new/cookbook/diffusion/intro.mdx`, `docs_new/docs.json` _+20 more__
- **2026-06-05** [`c6c1f1a29a`](https://github.com/sgl-project/sglang/commit/c6c1f1a29a) [#27308](https://github.com/sgl-project/sglang/pull/27308)
  docs: sync legacy docs/-only updates into docs_new (Mintlify) (#27308)
  _Files: `docs_new/docs.json`, `docs_new/docs/advanced_features/quantization.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/basic_usage/sampling_params.mdx` _+14 more__
- **2026-06-04** [`88a9d513e0`](https://github.com/sgl-project/sglang/commit/88a9d513e0) [#25292](https://github.com/sgl-project/sglang/pull/25292)
  [Quant] Support asymmetric weight quant in compressed-tensors WNA16 (#25292)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-06-04** [`ff93a576e5`](https://github.com/sgl-project/sglang/commit/ff93a576e5) [#27111](https://github.com/sgl-project/sglang/pull/27111)
  [AMD] Minimax M25 : FP8 block-scale GEMM dispatch for ROCm 7.0 on gfx950 (#27111)
  _Files: `python/sglang/srt/layers/quantization/fp8_utils.py`_
- **2026-06-03** [`d1bc06b63b`](https://github.com/sgl-project/sglang/commit/d1bc06b63b) [#27163](https://github.com/sgl-project/sglang/pull/27163)
  [AMD] Disable AITER custom all-gather in DeepSeek-R1-MXFP4 8-GPU test (#27163)
  _Files: `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`_

## LoRA  (2 commits)

- **2026-06-05** [`bcf89928b4`](https://github.com/sgl-project/sglang/commit/bcf89928b4) [#27073](https://github.com/sgl-project/sglang/pull/27073)
  [router] Configure experimental sgl-router via CLI flags instead of a config file (#27073)
  _Files: `experimental/sgl-router/Cargo.toml`, `experimental/sgl-router/README.md`, `experimental/sgl-router/src/config/cli.rs`, `experimental/sgl-router/src/config/mod.rs` _+39 more__
- **2026-06-04** [`cc67f922cd`](https://github.com/sgl-project/sglang/commit/cc67f922cd) [#27224](https://github.com/sgl-project/sglang/pull/27224)
  [misc] Update Codeowner for Lora  (#27224)
  _Files: `.github/CODEOWNERS`_

## Serving / API  (2 commits)

- **2026-06-03** [`7f706f4cfb`](https://github.com/sgl-project/sglang/commit/7f706f4cfb) [#26854](https://github.com/sgl-project/sglang/pull/26854)
  [Deps] Bump FI to 0.6.12 and cutedsl to 4.5.2 (#26854)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/utils/common.py`_
- **2026-06-02** [`6ba31e33e6`](https://github.com/sgl-project/sglang/commit/6ba31e33e6) [#27019](https://github.com/sgl-project/sglang/pull/27019)
  feat(api): add require_reasoning field for engine's generate api (#27019)
  _Files: `python/sglang/srt/entrypoints/engine.py`_

## Structured Output  (1 commits)

- **2026-06-06** [`e9dbbd19e9`](https://github.com/sgl-project/sglang/commit/e9dbbd19e9) [#25100](https://github.com/sgl-project/sglang/pull/25100)
  [model] Apertus Tool/Function and Reasoning parser (#25100)
  _Files: `docs_new/docs/advanced_features/separate_reasoning.ipynb`, `docs_new/docs/advanced_features/separate_reasoning.mdx`, `docs_new/docs/advanced_features/tool_parser.ipynb`, `docs_new/docs/advanced_features/tool_parser.mdx` _+8 more__

---
_Generated 2026-06-08 12:43 UTC_