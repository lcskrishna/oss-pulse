# vllm-project/vllm — Weekly Change Report
**Period:** 2026-06-29 → 2026-07-06  |  **Total commits:** 273

## ✨ New Features This Week

- **2026-07-06** [#47675](https://github.com/vllm-project/vllm/pull/47675) — [XPU][CI]Add agent tags for Basic Models Tests (Initialization) in Intel GPU CI (#47675)
- **2026-07-06** [#47024](https://github.com/vllm-project/vllm/pull/47024) — [Frontend] Support OpenAI Responses API namespace tools (#47024)
- **2026-07-06** [#45243](https://github.com/vllm-project/vllm/pull/45243) — [RISC-V] Enable BF16 on VLEN=256 hardware (#45243)
- **2026-07-06** [#44880](https://github.com/vllm-project/vllm/pull/44880) — [Feature] Support MTP speculative decoding for Bailing hybrid models (#44880)
- **2026-07-06** [#47433](https://github.com/vllm-project/vllm/pull/47433) — [Attention Backend] HPC_ATTN backend support mtp and dynamic scheduled attention (#47433)
- **2026-07-05** [#47070](https://github.com/vllm-project/vllm/pull/47070) — [Feature] Support sequence parallel without the need for DP, 1.9%~5.0% E2E Throughput Improvement (#47070)
- **2026-07-04** [#43645](https://github.com/vllm-project/vllm/pull/43645) — [XPU] Add W8A8 FP8 linear kernel with multi-granularity quant support (#43645)
- **2026-07-04** [#42890](https://github.com/vllm-project/vllm/pull/42890) — Support nvfp4 kv with kv-cache-dtype-skip-layers sliding_window (#42890)
- **2026-07-03** [#47220](https://github.com/vllm-project/vllm/pull/47220) — [AMD][EPLB] Enable EPLB for Quark OCP MXFP4 MoE (#47220)
- **2026-07-03** [#47102](https://github.com/vllm-project/vllm/pull/47102) — Add Triton Backend for Unlimited-OCR R-SWA (#47102)
- _…and 45 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-06** [`fb265fc8fb`](https://github.com/vllm-project/vllm/commit/fb265fc8fb) [#47591](https://github.com/vllm-project/vllm/pull/47591) — [ROCm][CI] Increasing parallelism in Basic Models Tests (Extra Initialization) (#47591)
- **2026-07-06** [`8f0e75e16b`](https://github.com/vllm-project/vllm/commit/8f0e75e16b) [#47481](https://github.com/vllm-project/vllm/pull/47481) — [ROCm][CI] Adding nixl multiconn (#47481)
- **2026-07-05** [`b71218107f`](https://github.com/vllm-project/vllm/commit/b71218107f) [#46944](https://github.com/vllm-project/vllm/pull/46944) — [ROCm][Test] Fix test_per_token_group_quant_fp8 tolerance for 1-ULP FP8 rounding on gfx950 (#46944)
- **2026-07-04** [`4a6bf3c77f`](https://github.com/vllm-project/vllm/commit/4a6bf3c77f) [#47519](https://github.com/vllm-project/vllm/pull/47519) — [ROCm][CI] Fix Kernels and Kernels attention test failures (#47519)
- **2026-07-04** [`f1445f6dbd`](https://github.com/vllm-project/vllm/commit/f1445f6dbd) [#47551](https://github.com/vllm-project/vllm/pull/47551) — [CI] Bump `huggingface-hub` from `v1.10.2` to `v1.22.0` (#47551)
- **2026-07-04** [`4c3c17d43b`](https://github.com/vllm-project/vllm/commit/4c3c17d43b) [#47567](https://github.com/vllm-project/vllm/pull/47567) — [ROCm] Disable persistent sparse-MLA kernel for chunked-prefill continuations (#47567)
- **2026-07-04** [`f329ce405b`](https://github.com/vllm-project/vllm/commit/f329ce405b) [#47536](https://github.com/vllm-project/vllm/pull/47536) — [ROCm][CI][Bugfix] Use VllmRunner for `voxtral_realtime` tests to avoid OOM on AMD GPU (#47536)
- **2026-07-03** [`576bf75d0e`](https://github.com/vllm-project/vllm/commit/576bf75d0e) [#47220](https://github.com/vllm-project/vllm/pull/47220) — [AMD][EPLB] Enable EPLB for Quark OCP MXFP4 MoE (#47220)
- **2026-07-03** [`f006e5a24c`](https://github.com/vllm-project/vllm/commit/f006e5a24c) [#47554](https://github.com/vllm-project/vllm/pull/47554) — [CI][AMD] Allow git operations on previously created work trees (#47554)
- **2026-07-03** [`f63dca6838`](https://github.com/vllm-project/vllm/commit/f63dca6838) [#47035](https://github.com/vllm-project/vllm/pull/47035) — [ROCm] Fix encoder-decoder cross-attention KV layout aliasing (#47035)
- **2026-07-03** [`3775d5fcab`](https://github.com/vllm-project/vllm/commit/3775d5fcab) [#47479](https://github.com/vllm-project/vllm/pull/47479) — [ROCm][CI] Adding test groups for parity with upstream (#47479)
- **2026-07-03** [`978de83353`](https://github.com/vllm-project/vllm/commit/978de83353) [#47447](https://github.com/vllm-project/vllm/pull/47447) — [Bugfix][CPU] Ship examples/ in the CPU release image (#47447)
- **2026-07-03** [`b790c84cde`](https://github.com/vllm-project/vllm/commit/b790c84cde) [#45246](https://github.com/vllm-project/vllm/pull/45246) — [CI] Enable sccache for Rust build under CUDA/ROCm (#45246)
- **2026-07-03** [`d85601c20f`](https://github.com/vllm-project/vllm/commit/d85601c20f) [#47465](https://github.com/vllm-project/vllm/pull/47465) — [CI] Pin modelscope version to fix test breakage (#47465)
- **2026-07-03** [`442ccc6098`](https://github.com/vllm-project/vllm/commit/442ccc6098) [#47482](https://github.com/vllm-project/vllm/pull/47482) — [ROCm][CI] Adding extract hs 2gpu (#47482)
- **2026-07-03** [`6768fbc76f`](https://github.com/vllm-project/vllm/commit/6768fbc76f) [#47480](https://github.com/vllm-project/vllm/pull/47480) — [ROCm][CI] Adding qwen3 dp4 eplb (#47480)
- **2026-07-03** [`407f406300`](https://github.com/vllm-project/vllm/commit/407f406300) [#47477](https://github.com/vllm-project/vllm/pull/47477) — [ROCm][CI] Adding metadata (#47477)
- **2026-07-02** [`de2a8fc042`](https://github.com/vllm-project/vllm/commit/de2a8fc042) [#47128](https://github.com/vllm-project/vllm/pull/47128) — [ROCm] [PyTorch] Move to stable abi since ROCm upgraded to torch 2.11 (#47128)
- **2026-07-02** [`09663abde0`](https://github.com/vllm-project/vllm/commit/09663abde0) [#44977](https://github.com/vllm-project/vllm/pull/44977) — [ROCm][MLA] Fuse MLA q/kv RMSNorm + FP8 per-token quant in the FP8 attention path (#44977)
- **2026-07-01** [`e91f5f8439`](https://github.com/vllm-project/vllm/commit/e91f5f8439) [#47342](https://github.com/vllm-project/vllm/pull/47342) — [CI] Remove torch_nightly mirror tags (superseded by TORCH_NIGHTLY full-nightly build) (#47342)
- **2026-07-01** [`5fd442187c`](https://github.com/vllm-project/vllm/commit/5fd442187c) [#46482](https://github.com/vllm-project/vllm/pull/46482) — [ROCm][P/D] MoRIIO toy proxy: support JSON Content-Type for OpenAI clients. (#46482)
- **2026-07-01** [`4e5ca89cfe`](https://github.com/vllm-project/vllm/commit/4e5ca89cfe) [#47269](https://github.com/vllm-project/vllm/pull/47269) — [ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing (#47269)
- **2026-07-01** [`aa8bb5562e`](https://github.com/vllm-project/vllm/commit/aa8bb5562e) [#46730](https://github.com/vllm-project/vllm/pull/46730) — [ROCm][Perf][Bugfix] DSv4 indexer: use platform FP8 dtype (fnuz) for Q-quant on gfx942 (#46730)
- **2026-07-01** [`ed41aa270a`](https://github.com/vllm-project/vllm/commit/ed41aa270a) [#43950](https://github.com/vllm-project/vllm/pull/43950) — [ROCm][DSV4] Use aiter mHC pre/post as the default ROCm path (#43950)
- **2026-07-01** [`4470ae84de`](https://github.com/vllm-project/vllm/commit/4470ae84de) [#46806](https://github.com/vllm-project/vllm/pull/46806) — Remove mantis (#46806)
- **2026-07-01** [`b446792306`](https://github.com/vllm-project/vllm/commit/b446792306) [#47209](https://github.com/vllm-project/vllm/pull/47209) — [ROCm][Bugfix] Fix Triton "out of resource: shared memory" Error In One-Shot LoRA MoE (#47209)
- **2026-07-01** [`c3b1f9e827`](https://github.com/vllm-project/vllm/commit/c3b1f9e827) [#47193](https://github.com/vllm-project/vllm/pull/47193) — [ROCm][CI] Enable LoRA TP Distributed Test Group In AMD CI (#47193)
- **2026-07-01** [`3c1396bab6`](https://github.com/vllm-project/vllm/commit/3c1396bab6) [#47222](https://github.com/vllm-project/vllm/pull/47222) — [Hardware][AMD][CI] Toggle test coredumps on ROCm debug agent (#47222)
- **2026-06-30** [`345b28ff2f`](https://github.com/vllm-project/vllm/commit/345b28ff2f) [#47195](https://github.com/vllm-project/vllm/pull/47195) — [Hardware][AMD][CI] Bump timeouts of various test groups on AMD CI (#47195)
- **2026-06-30** [`c8f9c156a5`](https://github.com/vllm-project/vllm/commit/c8f9c156a5) [#46993](https://github.com/vllm-project/vllm/pull/46993) — [ROCm][V1][MLA] Clone prefill backend state per metadata builder (#46993)
- **2026-06-30** [`f41e8ddc97`](https://github.com/vllm-project/vllm/commit/f41e8ddc97) [#47065](https://github.com/vllm-project/vllm/pull/47065) — [ROCm][CI] Move PyTorch Compilation Unit Tests to MI300(gfx942) (#47065)
- **2026-06-30** [`e840f0d3f5`](https://github.com/vllm-project/vllm/commit/e840f0d3f5) [#47140](https://github.com/vllm-project/vllm/pull/47140) — [Platform] Replace `torch.cuda.Event` with `torch.Event` (#47140)
- **2026-06-30** [`aab7af0bcb`](https://github.com/vllm-project/vllm/commit/aab7af0bcb) [#46997](https://github.com/vllm-project/vllm/pull/46997) — [Bugfix][ROCm][MLA] Pass q/kv dtypes to get_mla_metadata_v1 in FP8 decode (#46997)
- **2026-06-30** [`ba22cb6765`](https://github.com/vllm-project/vllm/commit/ba22cb6765) [#47000](https://github.com/vllm-project/vllm/pull/47000) — [ROCm][Ray][CI] Keep assigned GPU visible for weight transfer (#47000)
- **2026-06-30** [`81bcced482`](https://github.com/vllm-project/vllm/commit/81bcced482) [#46381](https://github.com/vllm-project/vllm/pull/46381) — [Bugfix][ROCm] Preserve MoE weight padding for unquantized Triton path (#46381)
- **2026-06-30** [`4236514098`](https://github.com/vllm-project/vllm/commit/4236514098) [#47004](https://github.com/vllm-project/vllm/pull/47004) — [ROCm][CI][Multimodal] Use ROCm-aware FA availability check for Unlimited-OCR (#47004)
- **2026-06-30** [`9fc0c08026`](https://github.com/vllm-project/vllm/commit/9fc0c08026) [#47085](https://github.com/vllm-project/vllm/pull/47085) — [ROCm][CI] Make tests/v1/shutdown an importable package (#47085)
- **2026-06-30** [`f2b5fabb23`](https://github.com/vllm-project/vllm/commit/f2b5fabb23) [#47094](https://github.com/vllm-project/vllm/pull/47094) — [ROCm][CI] Move LM Eval Large Models (8 GPUs) to mi300 pool (#47094)
- **2026-06-29** [`8632c884dc`](https://github.com/vllm-project/vllm/commit/8632c884dc) [#47003](https://github.com/vllm-project/vllm/pull/47003) — [ROCm][CI] Use spawn around the threaded OTLP test (#47003)
- **2026-06-29** [`c3734e8334`](https://github.com/vllm-project/vllm/commit/c3734e8334) [#47072](https://github.com/vllm-project/vllm/pull/47072) — [CI][Bugfix] Add cohere_melody to ROCm test requirements (#47072)
- **2026-06-29** [`53f7553f09`](https://github.com/vllm-project/vllm/commit/53f7553f09) [#46990](https://github.com/vllm-project/vllm/pull/46990) — [ROCm][DeepEP] Stabilize high-throughput DBO for DP+EP (#46990)
- **2026-06-29** [`4eb227992a`](https://github.com/vllm-project/vllm/commit/4eb227992a) [#45490](https://github.com/vllm-project/vllm/pull/45490) — [ROCm][CI] Make memory sampling less racy in tests and sleep mode (#45490)
- **2026-06-29** [`ebcf511ec3`](https://github.com/vllm-project/vllm/commit/ebcf511ec3) [#47067](https://github.com/vllm-project/vllm/pull/47067) — [ROCm][CI] Soft Fail `Spec Decode Ngram + Suffix` and `Entrypoints Integration (LLM)` AMD Mirrors (#47067)
- **2026-06-29** [`5316638a5e`](https://github.com/vllm-project/vllm/commit/5316638a5e) [#47015](https://github.com/vllm-project/vllm/pull/47015) — Fix transient dependency issues caused by `requirements/common.txt` (#47015)
- **2026-06-29** [`3483240b7e`](https://github.com/vllm-project/vllm/commit/3483240b7e) [#44512](https://github.com/vllm-project/vllm/pull/44512) — [Frontend] Consolidate scale out entrypoints (#44512)
- **2026-06-29** [`db28ae2d07`](https://github.com/vllm-project/vllm/commit/db28ae2d07) [#46999](https://github.com/vllm-project/vllm/pull/46999) — [ROCm][CI] Explicitly tear down multimodal offline LLMs (#46999)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#47724](https://github.com/vllm-project/vllm/issues/47724) | [Bug]: After a runtime `add_lora()`, one user's in-flight LoRA request | — | 2026-07-06 |
| [#47722](https://github.com/vllm-project/vllm/issues/47722) | RuntimeError: shape mismatch during KV cache init with EP + DP on MoE  | — | 2026-07-06 |
| [#41663](https://github.com/vllm-project/vllm/issues/41663) | [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe  | bug, intel-gpu | 2026-07-06 |
| [#47691](https://github.com/vllm-project/vllm/issues/47691) | [Bug]: `--data-parallel-start-rank 0` is silently treated as unset due | bug | 2026-07-06 |
| [#47684](https://github.com/vllm-project/vllm/issues/47684) | [RFC]: FlashInfer NVFP4 KV serving on pre-SM100 GPUs | RFC | 2026-07-06 |
| [#44008](https://github.com/vllm-project/vllm/issues/44008) | [RFC]: Offloading Metrics Redesign | RFC | 2026-07-06 |
| [#35800](https://github.com/vllm-project/vllm/issues/35800) | [Bug]: Enabling speculative coding causes malformed Tool Calls in Qwen | bug | 2026-07-06 |
| [#23497](https://github.com/vllm-project/vllm/issues/23497) | [Bug]: FP4 not leverage on RTX 6000 Pro (Blackwell) | bug, unstale | 2026-07-06 |
| [#43326](https://github.com/vllm-project/vllm/issues/43326) | [Bug]: Gemma4 26B-A4B fails because GELU_TANH is unsupported in CPU fu | bug | 2026-07-06 |
| [#40286](https://github.com/vllm-project/vllm/issues/40286) | [Bug]: v0.19.1 failed to load AWQ 4bit quantization of Gemma 4 26B-A4B | bug | 2026-07-06 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-07-06 |
| [#46856](https://github.com/vllm-project/vllm/issues/46856) | [Bug][ROCm] GLM5.1 ROCM_AITER_MLA_SPARSE corruption persists between I | bug, rocm | 2026-07-05 |
| [#42186](https://github.com/vllm-project/vllm/issues/42186) | [Bug][flashinfer 0.6.8]: worker hang on Qwen3.5-397B-A17B-NVFP4 EP=8 ( | bug | 2026-07-05 |
| [#47659](https://github.com/vllm-project/vllm/issues/47659) | [Bug]: Responses API rejects input_audio while Chat Completions accept | bug | 2026-07-05 |
| [#40002](https://github.com/vllm-project/vllm/issues/40002) | [Bug]: Inconsistent KV Cache reporting and system hang on long context | bug | 2026-07-05 |
| [#47650](https://github.com/vllm-project/vllm/issues/47650) | [Bug][XPU] --enable-lora on AutoRound int4 (INC ark_linear) crashes at | — | 2026-07-05 |
| [#42393](https://github.com/vllm-project/vllm/issues/42393) | [Installation]: RuntimeError: FlashInfer requires GPUs with sm75 or hi | installation | 2026-07-05 |
| [#47549](https://github.com/vllm-project/vllm/issues/47549) | [Bug]: REGRESSION : FP8 KV cache  FlashInfer no longer available as at | bug | 2026-07-05 |
| [#44335](https://github.com/vllm-project/vllm/issues/44335) | [Installation]: libcudart.so.13 required when torch-backend=cu129 on v | installation | 2026-07-05 |
| [#37030](https://github.com/vllm-project/vllm/issues/37030) | [Bug]: GPT-OSS-120B gpt-oss MXFP4 on SM121 (Blackwell DGX Spark): Marl | unstale | 2026-07-05 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 45 |
| Other | 38 |
| Attention | 34 |
| MoE / Expert Parallel | 25 |
| Models | 22 |
| Serving / API | 20 |
| Multimodal | 19 |
| CI / Build | 17 |
| Scheduler / Engine | 14 |
| Quantization | 11 |
| LoRA | 10 |
| Speculative Decoding | 7 |
| Disaggregation / PD | 6 |
| KV Cache / Offload | 3 |
| Docs | 1 |
| Compilation / CUDA Graph | 1 |

## ROCm / AMD  (45 commits)

- **2026-07-06** [`fb265fc8fb`](https://github.com/vllm-project/vllm/commit/fb265fc8fb) [#47591](https://github.com/vllm-project/vllm/pull/47591)
  [ROCm][CI] Increasing parallelism in Basic Models Tests (Extra Initialization) (#47591)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-07-06** [`8f0e75e16b`](https://github.com/vllm-project/vllm/commit/8f0e75e16b) [#47481](https://github.com/vllm-project/vllm/pull/47481)
  [ROCm][CI] Adding nixl multiconn (#47481)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/kv_connector/nixl_integration/run_mamba_prefix_cache_test.sh`, `tests/v1/kv_connector/nixl_integration/run_multi_connector_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/run_multi_connector_edge_case_test.sh`_
- **2026-07-05** [`b71218107f`](https://github.com/vllm-project/vllm/commit/b71218107f) [#46944](https://github.com/vllm-project/vllm/pull/46944)
  [ROCm][Test] Fix test_per_token_group_quant_fp8 tolerance for 1-ULP FP8 rounding on gfx950 (#46944)
  _Files: `tests/kernels/quantization/test_block_fp8.py`_
- **2026-07-04** [`4a6bf3c77f`](https://github.com/vllm-project/vllm/commit/4a6bf3c77f) [#47519](https://github.com/vllm-project/vllm/pull/47519)
  [ROCm][CI] Fix Kernels and Kernels attention test failures (#47519)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_decode_metadata.py`, `tests/kernels/moe/test_ocp_mx_moe.py`_
- **2026-07-04** [`f1445f6dbd`](https://github.com/vllm-project/vllm/commit/f1445f6dbd) [#47551](https://github.com/vllm-project/vllm/pull/47551)
  [CI] Bump `huggingface-hub` from `v1.10.2` to `v1.22.0` (#47551)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt` _+21 more__
- **2026-07-04** [`4c3c17d43b`](https://github.com/vllm-project/vllm/commit/4c3c17d43b) [#47567](https://github.com/vllm-project/vllm/pull/47567)
  [ROCm] Disable persistent sparse-MLA kernel for chunked-prefill continuations (#47567)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-07-04** [`f329ce405b`](https://github.com/vllm-project/vllm/commit/f329ce405b) [#47536](https://github.com/vllm-project/vllm/pull/47536)
  [ROCm][CI][Bugfix] Use VllmRunner for `voxtral_realtime` tests to avoid OOM on AMD GPU (#47536)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`_
- **2026-07-03** [`576bf75d0e`](https://github.com/vllm-project/vllm/commit/576bf75d0e) [#47220](https://github.com/vllm-project/vllm/pull/47220)
  [AMD][EPLB] Enable EPLB for Quark OCP MXFP4 MoE (#47220)
  _Files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-07-03** [`f006e5a24c`](https://github.com/vllm-project/vllm/commit/f006e5a24c) [#47554](https://github.com/vllm-project/vllm/pull/47554)
  [CI][AMD] Allow git operations on previously created work trees (#47554)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-03** [`f63dca6838`](https://github.com/vllm-project/vllm/commit/f63dca6838) [#47035](https://github.com/vllm-project/vllm/pull/47035)
  [ROCm] Fix encoder-decoder cross-attention KV layout aliasing (#47035)
  _Files: `tests/entrypoints/speech_to_text/transcription/test_transcription_validation_whisper.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-03** [`3775d5fcab`](https://github.com/vllm-project/vllm/commit/3775d5fcab) [#47479](https://github.com/vllm-project/vllm/pull/47479)
  [ROCm][CI] Adding test groups for parity with upstream (#47479)
  _Files: `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/fla/ops/chunk_delta_h.py`_
- **2026-07-03** [`978de83353`](https://github.com/vllm-project/vllm/commit/978de83353) [#47447](https://github.com/vllm-project/vllm/pull/47447)
  [Bugfix][CPU] Ship examples/ in the CPU release image (#47447)
  _Files: `docker/Dockerfile.cpu`_
- **2026-07-03** [`b790c84cde`](https://github.com/vllm-project/vllm/commit/b790c84cde) [#45246](https://github.com/vllm-project/vllm/pull/45246)
  [CI] Enable sccache for Rust build under CUDA/ROCm (#45246)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.rocm`, `docker/versions.json`_
- **2026-07-03** [`d85601c20f`](https://github.com/vllm-project/vllm/commit/d85601c20f) [#47465](https://github.com/vllm-project/vllm/pull/47465)
  [CI] Pin modelscope version to fix test breakage (#47465)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/scripts/hardware_ci/run-npu-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml` _+2 more__
- **2026-07-03** [`442ccc6098`](https://github.com/vllm-project/vllm/commit/442ccc6098) [#47482](https://github.com/vllm-project/vllm/pull/47482)
  [ROCm][CI] Adding extract hs 2gpu (#47482)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`_
- **2026-07-03** [`6768fbc76f`](https://github.com/vllm-project/vllm/commit/6768fbc76f) [#47480](https://github.com/vllm-project/vllm/pull/47480)
  [ROCm][CI] Adding qwen3 dp4 eplb (#47480)
  _Files: `.buildkite/scripts/scheduled_integration_test/qwen30b_a3b_fp8_dp4_async_eplb.sh`, `.buildkite/test-amd.yaml`_
- **2026-07-03** [`407f406300`](https://github.com/vllm-project/vllm/commit/407f406300) [#47477](https://github.com/vllm-project/vllm/pull/47477)
  [ROCm][CI] Adding metadata (#47477)
  _Files: `.buildkite/test-amd.yaml`, `docker/Dockerfile.rocm`, `tests/tools/test_docker_build_metadata_args.py`_
- **2026-07-02** [`de2a8fc042`](https://github.com/vllm-project/vllm/commit/de2a8fc042) [#47128](https://github.com/vllm-project/vllm/pull/47128)
  [ROCm] [PyTorch] Move to stable abi since ROCm upgraded to torch 2.11 (#47128)
  _Files: `CMakeLists.txt`, `csrc/cuda_view.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+2 more__
- **2026-07-02** [`09663abde0`](https://github.com/vllm-project/vllm/commit/09663abde0) [#44977](https://github.com/vllm-project/vllm/pull/44977)
  [ROCm][MLA] Fuse MLA q/kv RMSNorm + FP8 per-token quant in the FP8 attention path (#44977)
  _Files: `docs/design/fusions.md`, `tests/compile/passes/test_fuse_mla_dual_rms_norm.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`_
- **2026-07-01** [`e91f5f8439`](https://github.com/vllm-project/vllm/commit/e91f5f8439) [#47342](https://github.com/vllm-project/vllm/pull/47342)
  [CI] Remove torch_nightly mirror tags (superseded by TORCH_NIGHTLY full-nightly build) (#47342)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_language.yaml`_
- **2026-07-01** [`5fd442187c`](https://github.com/vllm-project/vllm/commit/5fd442187c) [#46482](https://github.com/vllm-project/vllm/pull/46482)
  [ROCm][P/D] MoRIIO toy proxy: support JSON Content-Type for OpenAI clients. (#46482)
  _Files: `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`_
- **2026-07-01** [`4e5ca89cfe`](https://github.com/vllm-project/vllm/commit/4e5ca89cfe) [#47269](https://github.com/vllm-project/vllm/pull/47269)
  [ROCm][MiniMax-M3] Cross-layer lightning-indexer top-k sharing (#47269)
  _Files: `vllm/models/minimax_m3/amd/model.py`_
- **2026-07-01** [`aa8bb5562e`](https://github.com/vllm-project/vllm/commit/aa8bb5562e) [#46730](https://github.com/vllm-project/vllm/pull/46730)
  [ROCm][Perf][Bugfix] DSv4 indexer: use platform FP8 dtype (fnuz) for Q-quant on gfx942 (#46730)
  _Files: `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`_
- **2026-07-01** [`ed41aa270a`](https://github.com/vllm-project/vllm/commit/ed41aa270a) [#43950](https://github.com/vllm-project/vllm/pull/43950)
  [ROCm][DSV4] Use aiter mHC pre/post as the default ROCm path (#43950)
  _Files: `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/mtp.py`_
- **2026-07-01** [`4470ae84de`](https://github.com/vllm-project/vllm/commit/4470ae84de) [#46806](https://github.com/vllm-project/vllm/pull/46806)
  Remove mantis (#46806)
  _Files: `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_multimodal.yaml`, `docs/models/supported_models.md` _+6 more__
- **2026-07-01** [`b446792306`](https://github.com/vllm-project/vllm/commit/b446792306) [#47209](https://github.com/vllm-project/vllm/pull/47209)
  [ROCm][Bugfix] Fix Triton "out of resource: shared memory" Error In One-Shot LoRA MoE (#47209)
  _Files: `vllm/lora/ops/triton_ops/fused_moe_lora_op.py`_
- **2026-07-01** [`c3b1f9e827`](https://github.com/vllm-project/vllm/commit/c3b1f9e827) [#47193](https://github.com/vllm-project/vllm/pull/47193)
  [ROCm][CI] Enable LoRA TP Distributed Test Group In AMD CI (#47193)
  _Files: `.buildkite/test-amd.yaml`, `tests/lora/test_gptoss_tp.py`_
- **2026-07-01** [`3c1396bab6`](https://github.com/vllm-project/vllm/commit/3c1396bab6) [#47222](https://github.com/vllm-project/vllm/pull/47222)
  [Hardware][AMD][CI] Toggle test coredumps on ROCm debug agent (#47222)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `tests/distributed/test_weight_transfer.py`_
- **2026-06-30** [`345b28ff2f`](https://github.com/vllm-project/vllm/commit/345b28ff2f) [#47195](https://github.com/vllm-project/vllm/pull/47195)
  [Hardware][AMD][CI] Bump timeouts of various test groups on AMD CI (#47195)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-30** [`c8f9c156a5`](https://github.com/vllm-project/vllm/commit/c8f9c156a5) [#46993](https://github.com/vllm-project/vllm/pull/46993)
  [ROCm][V1][MLA] Clone prefill backend state per metadata builder (#46993)
  _Files: `tests/v1/attention/test_mla_prefill_registry.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/prefill/base.py`_
- **2026-06-30** [`f41e8ddc97`](https://github.com/vllm-project/vllm/commit/f41e8ddc97) [#47065](https://github.com/vllm-project/vllm/pull/47065)
  [ROCm][CI] Move PyTorch Compilation Unit Tests to MI300(gfx942) (#47065)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-30** [`aab7af0bcb`](https://github.com/vllm-project/vllm/commit/aab7af0bcb) [#46997](https://github.com/vllm-project/vllm/pull/46997)
  [Bugfix][ROCm][MLA] Pass q/kv dtypes to get_mla_metadata_v1 in FP8 decode (#46997)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_decode_metadata.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-06-30** [`ba22cb6765`](https://github.com/vllm-project/vllm/commit/ba22cb6765) [#47000](https://github.com/vllm-project/vllm/pull/47000)
  [ROCm][Ray][CI] Keep assigned GPU visible for weight transfer (#47000)
  _Files: `tests/distributed/test_weight_transfer.py`_
- **2026-06-30** [`81bcced482`](https://github.com/vllm-project/vllm/commit/81bcced482) [#46381](https://github.com/vllm-project/vllm/pull/46381)
  [Bugfix][ROCm] Preserve MoE weight padding for unquantized Triton path (#46381)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-06-30** [`4236514098`](https://github.com/vllm-project/vllm/commit/4236514098) [#47004](https://github.com/vllm-project/vllm/pull/47004)
  [ROCm][CI][Multimodal] Use ROCm-aware FA availability check for Unlimited-OCR (#47004)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-06-30** [`9fc0c08026`](https://github.com/vllm-project/vllm/commit/9fc0c08026) [#47085](https://github.com/vllm-project/vllm/pull/47085)
  [ROCm][CI] Make tests/v1/shutdown an importable package (#47085)
  _Files: `tests/v1/shutdown/__init__.py`_
- **2026-06-30** [`f2b5fabb23`](https://github.com/vllm-project/vllm/commit/f2b5fabb23) [#47094](https://github.com/vllm-project/vllm/pull/47094)
  [ROCm][CI] Move LM Eval Large Models (8 GPUs) to mi300 pool (#47094)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-06-29** [`8632c884dc`](https://github.com/vllm-project/vllm/commit/8632c884dc) [#47003](https://github.com/vllm-project/vllm/pull/47003)
  [ROCm][CI] Use spawn around the threaded OTLP test (#47003)
  _Files: `tests/v1/tracing/test_tracing.py`_
- **2026-06-29** [`c3734e8334`](https://github.com/vllm-project/vllm/commit/c3734e8334) [#47072](https://github.com/vllm-project/vllm/pull/47072)
  [CI][Bugfix] Add cohere_melody to ROCm test requirements (#47072)
  _Files: `requirements/test/rocm.in`, `requirements/test/rocm.txt`_
- **2026-06-29** [`53f7553f09`](https://github.com/vllm-project/vllm/commit/53f7553f09) [#46990](https://github.com/vllm-project/vllm/pull/46990)
  [ROCm][DeepEP] Stabilize high-throughput DBO for DP+EP (#46990)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_ht.py`, `vllm/v1/worker/gpu_ubatch_wrapper.py`_
- **2026-06-29** [`4eb227992a`](https://github.com/vllm-project/vllm/commit/4eb227992a) [#45490](https://github.com/vllm-project/vllm/pull/45490)
  [ROCm][CI] Make memory sampling less racy in tests and sleep mode (#45490)
  _Files: `tests/utils.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-06-29** [`ebcf511ec3`](https://github.com/vllm-project/vllm/commit/ebcf511ec3) [#47067](https://github.com/vllm-project/vllm/pull/47067)
  [ROCm][CI] Soft Fail `Spec Decode Ngram + Suffix` and `Entrypoints Integration (LLM)` AMD Mirrors (#47067)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-06-29** [`5316638a5e`](https://github.com/vllm-project/vllm/commit/5316638a5e) [#47015](https://github.com/vllm-project/vllm/pull/47015)
  Fix transient dependency issues caused by `requirements/common.txt` (#47015)
  _Files: `docker/Dockerfile.cpu`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/rocm.in` _+4 more__
- **2026-06-29** [`3483240b7e`](https://github.com/vllm-project/vllm/commit/3483240b7e) [#44512](https://github.com/vllm-project/vllm/pull/44512)
  [Frontend] Consolidate scale out entrypoints (#44512)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docs/examples/README.md` _+41 more__
- **2026-06-29** [`db28ae2d07`](https://github.com/vllm-project/vllm/commit/db28ae2d07) [#46999](https://github.com/vllm-project/vllm/pull/46999)
  [ROCm][CI] Explicitly tear down multimodal offline LLMs (#46999)
  _Files: `tests/conftest.py`, `tests/entrypoints/multimodal/conftest.py`, `tests/entrypoints/multimodal/llm/test_chat.py`, `tests/entrypoints/multimodal/llm/test_mm_cache_external_injection.py` _+2 more__

## Other  (38 commits)

- **2026-07-06** [`26c754d847`](https://github.com/vllm-project/vllm/commit/26c754d847) [#47116](https://github.com/vllm-project/vllm/pull/47116)
  [XPU][Bugfix] Do not transpose weight_scale_inv at load time (#47116)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-07-06** [`344609ab17`](https://github.com/vllm-project/vllm/commit/344609ab17) [#47695](https://github.com/vllm-project/vllm/pull/47695)
  [CI/Build] Fix pre-commit check (#47695)
  _Files: `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-07-06** [`69715823df`](https://github.com/vllm-project/vllm/commit/69715823df) [#47406](https://github.com/vllm-project/vllm/pull/47406)
  [Test][XPU] Skip fork in kv_sharing_fast_prefill test on XPU (#47406)
  _Files: `tests/v1/e2e/general/test_kv_sharing_fast_prefill.py`_
- **2026-07-06** [`78a04c208d`](https://github.com/vllm-project/vllm/commit/78a04c208d) [#43092](https://github.com/vllm-project/vllm/pull/43092)
  [XPU] Fix CUDA API shims breaking Torch Dynamo during AOT compile (#43092)
  _Files: `tests/v1/worker/test_xpu_model_runner.py`, `vllm/v1/worker/xpu_model_runner.py`_
- **2026-07-03** [`8651f043b8`](https://github.com/vllm-project/vllm/commit/8651f043b8) [#47523](https://github.com/vllm-project/vllm/pull/47523)
  [Rust Frontend] Speed up chat roundtrip tests (#47523)
  _Files: `rust/Cargo.toml`, `rust/src/chat/tests/roundtrip.rs`_
- **2026-07-03** [`9b8e76589d`](https://github.com/vllm-project/vllm/commit/9b8e76589d) [#47289](https://github.com/vllm-project/vllm/pull/47289)
  [Rust Frontend] Recover buffered text from incomplete tool calls at EOS (#47289)
  _Files: `rust/src/chat/src/output/default/unified.rs`_
- **2026-07-03** [`1aeabec355`](https://github.com/vllm-project/vllm/commit/1aeabec355) [#44682](https://github.com/vllm-project/vllm/pull/44682)
  [Bugfix][Rust Frontend] Tolerate out-of-vocab prompt ids in detokenizer (#44682)
  _Files: `rust/src/tokenizer/src/incremental.rs`_
- **2026-07-03** [`276b837dc4`](https://github.com/vllm-project/vllm/commit/276b837dc4) [#47483](https://github.com/vllm-project/vllm/pull/47483)
  [ModelRunner V2][BugFix] Free all model refs on shutdown (#47483)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-07-02** [`e24d1b24fe`](https://github.com/vllm-project/vllm/commit/e24d1b24fe) [#47472](https://github.com/vllm-project/vllm/pull/47472)
  Fix Transformers modeling backend usage stats (#47472)
  _Files: `vllm/v1/utils.py`_
- **2026-07-02** [`258f8de91f`](https://github.com/vllm-project/vllm/commit/258f8de91f) [#47311](https://github.com/vllm-project/vllm/pull/47311)
  [Bugfix][Tool Parser] poolside_v1: accept tool calls without newline after function name (#47311)
  _Files: `tests/tool_parsers/test_poolside_v1_tool_parser.py`, `vllm/tool_parsers/poolside_v1_tool_parser.py`_
- **2026-07-02** [`a47f38f825`](https://github.com/vllm-project/vllm/commit/a47f38f825) [#47383](https://github.com/vllm-project/vllm/pull/47383)
  [Bugfix][Model Runner V2][Spec Decode] Fix int32 offset overflow in block verification kernels (#47383)
  _Files: `tests/v1/worker/test_gpu_rejection_sampler_i64.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-07-02** [`3e158ae62d`](https://github.com/vllm-project/vllm/commit/3e158ae62d) [#47428](https://github.com/vllm-project/vllm/pull/47428)
  [ModelRunner V2] Fix Mamba2 crash on non-spec-decode (#47428)
  _Files: `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-07-01** [`8cfeb84dba`](https://github.com/vllm-project/vllm/commit/8cfeb84dba) [#47308](https://github.com/vllm-project/vllm/pull/47308)
  [ModelRunner V2] Warmup cross-attn properly in encoder-decoder case (#47308)
  _Files: `vllm/v1/worker/gpu/warmup.py`_
- **2026-07-01** [`00eb7cefa3`](https://github.com/vllm-project/vllm/commit/00eb7cefa3) [#47029](https://github.com/vllm-project/vllm/pull/47029)
  [Bugfix] Prevent padding placeholders from reaching embeddings (#47029)
  _Files: `tests/v1/worker/test_gpu_input_batch.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-01** [`dee5da1dec`](https://github.com/vllm-project/vllm/commit/dee5da1dec) [#47250](https://github.com/vllm-project/vllm/pull/47250)
  [Test] Run SageMaker handler-override tests in-process via TestClient (#47250)
  _Files: `tests/entrypoints/serve/sagemaker/test_sagemaker_handler_overrides.py`_
- **2026-07-01** [`a461070d1c`](https://github.com/vllm-project/vllm/commit/a461070d1c) [#47243](https://github.com/vllm-project/vllm/pull/47243)
  [Core] Make sleep-mode backend capability flags communicator-agnostic (#47243)
  _Files: `tests/v1/worker/test_sleep_mode_backend.py`, `vllm/device_allocator/sleep_mode_backend.py`_
- **2026-07-01** [`93d8f834dd`](https://github.com/vllm-project/vllm/commit/93d8f834dd) [#44074](https://github.com/vllm-project/vllm/pull/44074)
  [Core] Pluggable sleep-mode backend abstraction (RFC #34303) (#44074)
  _Files: `tests/v1/worker/test_sleep_mode_backend.py`, `vllm/config/model.py`, `vllm/device_allocator/sleep_mode_backend.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-01** [`9a08a5118e`](https://github.com/vllm-project/vllm/commit/9a08a5118e) [#47164](https://github.com/vllm-project/vllm/pull/47164)
  fix: skip cooperative top-K on SM120 (#47164)
  _Files: `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-07-01** [`3406e8f83d`](https://github.com/vllm-project/vllm/commit/3406e8f83d) [#47062](https://github.com/vllm-project/vllm/pull/47062)
  [Bugfix][Frontend][gpt-oss] Return raw output when Harmony parser ends non-terminal (#47062)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-07-01** [`9294dd27eb`](https://github.com/vllm-project/vllm/commit/9294dd27eb) [#46255](https://github.com/vllm-project/vllm/pull/46255)
  fix(reasoning): guard rfind in ernie45 streaming </response> branch (#46255)
  _Files: `vllm/reasoning/ernie45_reasoning_parser.py`_
- **2026-06-30** [`28242824e0`](https://github.com/vllm-project/vllm/commit/28242824e0) [#45657](https://github.com/vllm-project/vllm/pull/45657)
  [Bugfix][Frontend] Normalize constrained Harmony recipients (#45657)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-06-30** [`11b26c5528`](https://github.com/vllm-project/vllm/commit/11b26c5528) [#47138](https://github.com/vllm-project/vllm/pull/47138)
  [Bugfix][Tool Parser] PoolsideV1: fix logprobs AttributeError on Responses API (#47138)
  _Files: `tests/tool_parsers/test_poolside_v1_tool_parser.py`, `vllm/tool_parsers/poolside_v1_tool_parser.py`_
- **2026-06-30** [`20434c472e`](https://github.com/vllm-project/vllm/commit/20434c472e) [#46621](https://github.com/vllm-project/vllm/pull/46621)
  [Feat] Improve Triton JIT diagnostics (#46621)
  _Files: `vllm/utils/jit_monitor.py`_
- **2026-06-30** [`9e84ec8648`](https://github.com/vllm-project/vllm/commit/9e84ec8648) [#46842](https://github.com/vllm-project/vllm/pull/46842)
  [Refactor] Remove dead minimax allreduce rms kernel (#46842)
  _Files: `csrc/libtorch_stable/minimax_reduce_rms_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `vllm/_custom_ops.py`_
- **2026-06-30** [`c231d1f290`](https://github.com/vllm-project/vllm/commit/c231d1f290) [#47007](https://github.com/vllm-project/vllm/pull/47007)
  fix(security): bound tokenizer work when explicit truncation_side is set (#47007)
  _Files: `tests/renderers/test_completions.py`, `vllm/renderers/params.py`_
- **2026-06-30** [`ded6676458`](https://github.com/vllm-project/vllm/commit/ded6676458) [#45960](https://github.com/vllm-project/vllm/pull/45960)
  [Bugfix] Seed RayExecutorV2 TCPStore port by DP rank to avoid collisions (#45960)
  _Files: `tests/distributed/test_ray_v2_executor.py`, `vllm/v1/executor/ray_executor_v2.py`_
- **2026-06-30** [`91055efd36`](https://github.com/vllm-project/vllm/commit/91055efd36) [#47134](https://github.com/vllm-project/vllm/pull/47134)
  [XPU] C++ implementation for get_memory_info (#47134)
  _Files: `vllm/platforms/xpu.py`_
- **2026-06-30** [`bdbd7278b6`](https://github.com/vllm-project/vllm/commit/bdbd7278b6) [#47110](https://github.com/vllm-project/vllm/pull/47110)
  [Rust Frontend] Extend renderer/parser roundtrip tests to support token ids (#47110)
  _Files: `rust/src/chat/src/output/harmony/tests.rs`, `rust/src/chat/tests/roundtrip.rs`_
- **2026-06-30** [`536047755e`](https://github.com/vllm-project/vllm/commit/536047755e) [#33057](https://github.com/vllm-project/vllm/pull/33057)
  Bump actions/checkout from 6.0.1 to 7.0.0 (#33057)
  _Files: `.github/workflows/macos-smoke-test.yml`, `.github/workflows/pre-commit.yml`_
- **2026-06-30** [`8e9d70fdd5`](https://github.com/vllm-project/vllm/commit/8e9d70fdd5) [#45140](https://github.com/vllm-project/vllm/pull/45140)
  [Kernel][XPU] Adjust kernel unit tests for XPU (#45140)
  _Files: `tests/kernels/mamba/test_mamba_ssm.py`_
- **2026-06-30** [`930f8dc0a1`](https://github.com/vllm-project/vllm/commit/930f8dc0a1) [#46839](https://github.com/vllm-project/vllm/pull/46839)
  [Bugfix][Rust Frontend] Reject prompt_logprobs for streaming generate (#46839)
  _Files: `rust/src/server/src/routes/inference/generate/validate.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-06-30** [`43916891b2`](https://github.com/vllm-project/vllm/commit/43916891b2) [#46346](https://github.com/vllm-project/vllm/pull/46346)
  [GDN] Improve kkt kernel of CuteDSL prefill backend (#46346)
  _Files: `vllm/cute_utils/__init__.py`, `vllm/cute_utils/_tcgen05.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/__init__.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/kernel_h.py` _+2 more__
- **2026-06-30** [`cda05ee8c4`](https://github.com/vllm-project/vllm/commit/cda05ee8c4) [#43757](https://github.com/vllm-project/vllm/pull/43757)
  [Bugfix][Reasoning] Fix thinking_token_budget not enforced on re-entry after forced end (#43757)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/v1/sample/thinking_budget_state.py`_
- **2026-06-29** [`72f639927f`](https://github.com/vllm-project/vllm/commit/72f639927f) [#46987](https://github.com/vllm-project/vllm/pull/46987)
  [XPU] [RMSNorm] revert weightless change on xpu (#46987)
  _Files: `vllm/kernels/xpu_ops.py`_
- **2026-06-29** [`8ad4a01825`](https://github.com/vllm-project/vllm/commit/8ad4a01825) [#46975](https://github.com/vllm-project/vllm/pull/46975)
  [ModelRunner V2] Simplify recent UnlimitedOCR-related changes (#46975)
  _Files: `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/default.py`, `vllm/v1/worker/gpu/model_states/encoder_decoder.py` _+1 more__
- **2026-06-29** [`49e28e8e91`](https://github.com/vllm-project/vllm/commit/49e28e8e91) [#44010](https://github.com/vllm-project/vllm/pull/44010)
  [Kernel][Helion][1/N] Add Helion kernel for fused_qk_norm_rope (#44010)
  _Files: `tests/kernels/helion/test_fused_qk_norm_rope.py`, `vllm/kernels/helion/configs/fused_qk_norm_rope/nvidia_b200.json`, `vllm/kernels/helion/configs/fused_qk_norm_rope/nvidia_h100.json`, `vllm/kernels/helion/ops/fused_qk_norm_rope.py`_
- **2026-06-29** [`a4e3cb40d0`](https://github.com/vllm-project/vllm/commit/a4e3cb40d0) [#47018](https://github.com/vllm-project/vllm/pull/47018)
  [mypy] Enable mypy for tests directory (#47018)
  _Files: `tools/pre_commit/mypy.py`_
- **2026-06-29** [`5274c1181d`](https://github.com/vllm-project/vllm/commit/5274c1181d) [#46800](https://github.com/vllm-project/vllm/pull/46800)
  [Rust Frontend] Add Harmony Renderer for GPT-OSS (#46800)
  _Files: `rust/Cargo.lock`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/lib.rs` _+23 more__

## Attention  (34 commits)

- **2026-07-06** [`736f1a5907`](https://github.com/vllm-project/vllm/commit/736f1a5907) [#47688](https://github.com/vllm-project/vllm/pull/47688)
  [XPU] Route mm_prefix models to Triton attention backend (#47688)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-06** [`16f8110935`](https://github.com/vllm-project/vllm/commit/16f8110935) [#47532](https://github.com/vllm-project/vllm/pull/47532)
  [Bugfix][CPU][RISC-V] Fix VLEN detection for RVV attention path (#47532)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_attn.cpp`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-07-06** [`95a248faed`](https://github.com/vllm-project/vllm/commit/95a248faed) [#47433](https://github.com/vllm-project/vllm/pull/47433)
  [Attention Backend] HPC_ATTN backend support mtp and dynamic scheduled attention (#47433)
  _Files: `docs/design/attention_backends.md`, `vllm/model_executor/layers/hpc/rope_norm.py`, `vllm/v1/attention/backends/hpc_attn.py`_
- **2026-07-05** [`cc1d020d01`](https://github.com/vllm-project/vllm/commit/cc1d020d01) [#46942](https://github.com/vllm-project/vllm/pull/46942)
  [MRV2] Enable mm prefix bidi attention support on MRV2 (#46942)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`, `tests/models/multimodal/generation/test_mm_prefix_lm.py`, `vllm/config/model.py`, `vllm/v1/worker/gpu/attn_utils.py` _+1 more__
- **2026-07-05** [`34b560b725`](https://github.com/vllm-project/vllm/commit/34b560b725) [#47332](https://github.com/vllm-project/vllm/pull/47332)
  [Bugfix][Gemma4] Fix FA4 mm_prefix mask: add sliding window and absolute q_idx (#47332)
  _Files: `vllm/v1/attention/backends/flash_attn.py`_
- **2026-07-04** [`26eb87204d`](https://github.com/vllm-project/vllm/commit/26eb87204d) [#45844](https://github.com/vllm-project/vllm/pull/45844)
  [Bugfix] Fix CPU split-KV scratchpad sizing (#45844)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-07-04** [`67ff0ae30f`](https://github.com/vllm-project/vllm/commit/67ff0ae30f) [#42890](https://github.com/vllm-project/vllm/pull/42890)
  Support nvfp4 kv with kv-cache-dtype-skip-layers sliding_window (#42890)
  _Files: `docs/features/quantization/quantized_kvcache.md`, `vllm/config/cache.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/platforms/interface.py` _+2 more__
- **2026-07-03** [`1f486d96a1`](https://github.com/vllm-project/vllm/commit/1f486d96a1) [#47102](https://github.com/vllm-project/vllm/pull/47102)
  Add Triton Backend for Unlimited-OCR R-SWA (#47102)
  _Files: `vllm/model_executor/models/config.py`, `vllm/model_executor/models/unlimited_ocr.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_attention_helpers.py` _+1 more__
- **2026-07-03** [`979f5511d7`](https://github.com/vllm-project/vllm/commit/979f5511d7) [#47217](https://github.com/vllm-project/vllm/pull/47217)
  [Bugfix][Gemma4] Keep image bidirectional attention within the sliding window (#47217)
  _Files: `vllm/model_executor/layers/attention/attention.py`, `vllm/model_executor/models/gemma4.py`, `vllm/model_executor/models/gemma4_mm.py`, `vllm/v1/attention/backends/flash_attn.py` _+4 more__
- **2026-07-03** [`41de1380c2`](https://github.com/vllm-project/vllm/commit/41de1380c2) [#47485](https://github.com/vllm-project/vllm/pull/47485)
  [BugFix] Derive FlashInfer Q dtype from resolved per-group builder state (#47485)
  _Files: `vllm/v1/attention/backends/flashinfer.py`_
- **2026-07-03** [`4c3c64fcf7`](https://github.com/vllm-project/vllm/commit/4c3c64fcf7) [#46853](https://github.com/vllm-project/vllm/pull/46853)
  Add Laguna XS.2.1 DFlash drafter support (#46853)
  _Files: `tests/models/registry.py`, `tests/v1/e2e/spec_decode/test_laguna_dflash.py`, `vllm/model_executor/models/laguna.py`, `vllm/model_executor/models/laguna_dflash.py` _+3 more__
- **2026-07-02** [`d29125c085`](https://github.com/vllm-project/vllm/commit/d29125c085) [#43232](https://github.com/vllm-project/vllm/pull/43232)
  Xqa decode kernels (#43232)
  _Files: `docs/design/attention_backends.md`, `tests/kernels/attention/test_use_trtllm_attention.py`, `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_trtllm_attention_integration.py` _+3 more__
- **2026-07-02** [`d715b3aa1e`](https://github.com/vllm-project/vllm/commit/d715b3aa1e) [#47361](https://github.com/vllm-project/vllm/pull/47361)
  Delete PagedAttention (#47361)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_paged_attention.py`, `csrc/libtorch_stable/attention/attention_kernels.cuh`, `csrc/libtorch_stable/attention/paged_attention_v1.cu` _+5 more__
- **2026-07-02** [`320ee285c9`](https://github.com/vllm-project/vllm/commit/320ee285c9) [#47285](https://github.com/vllm-project/vllm/pull/47285)
  [Model Runner V2][Perf] Warm up GLM-5.2 DSA indexer prefill metadata kernel (#47285)
  _Files: `vllm/model_executor/warmup/sparse_mla_triton_warmup.py`_
- **2026-07-01** [`4787f2dd1b`](https://github.com/vllm-project/vllm/commit/4787f2dd1b) [#47305](https://github.com/vllm-project/vllm/pull/47305)
  [Bugfix] Don't read KV cache past `seq_len` in triton paged attn kernels (#47305)
  _Files: `vllm/v1/attention/ops/chunked_prefill_paged_decode.py`, `vllm/v1/attention/ops/triton_attention_helpers.py`_
- **2026-07-01** [`f5a8d73377`](https://github.com/vllm-project/vllm/commit/f5a8d73377) [#46995](https://github.com/vllm-project/vllm/pull/46995)
  [Spec Decode] DSpark (#46995)
  _Files: `tests/models/registry.py`, `tests/models/test_registry.py`, `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/e2e/spec_decode/test_spec_decode.py` _+20 more__
- **2026-07-01** [`c5200d3565`](https://github.com/vllm-project/vllm/commit/c5200d3565) [#46076](https://github.com/vllm-project/vllm/pull/46076)
  [Attention][DSA] support dcp for FLASHINFER_MLA_SPARSE (#46076)
  _Files: `docs/design/attention_backends.md`, `tests/v1/attention/test_indexer_dcp_localize.py`, `vllm/model_executor/kernels/attention/__init__.py`, `vllm/model_executor/kernels/attention/dsa/__init__.py` _+8 more__
- **2026-07-01** [`9969466a59`](https://github.com/vllm-project/vllm/commit/9969466a59) [#46104](https://github.com/vllm-project/vllm/pull/46104)
  [Spec Decode] Support SWA + DFlash for MiMo (#46104)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/mimo_v2.py`, `vllm/model_executor/models/qwen3_dflash.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-07-01** [`a264e41975`](https://github.com/vllm-project/vllm/commit/a264e41975) [#47219](https://github.com/vllm-project/vllm/pull/47219)
  [Distributed] Default FlashInfer allreduce to mnnvl on single node (#47219)
  _Files: `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-07-01** [`f098ee70c7`](https://github.com/vllm-project/vllm/commit/f098ee70c7) [#47090](https://github.com/vllm-project/vllm/pull/47090)
  [GLM5] Support FlashMLA FP8 KV cache (Hopper & Blackwell) (#47090)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/nvidia/attention.py`, `vllm/models/deepseek_v32/nvidia/kernels.py`_
- **2026-06-30** [`248d1fbb71`](https://github.com/vllm-project/vllm/commit/248d1fbb71) [#46182](https://github.com/vllm-project/vllm/pull/46182)
  [Feat][1/N] CuTeDSL warmup infrastructure, FA4 MLA (#46182)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `vllm/config/kernel.py`, `vllm/model_executor/warmup/cutedsl_warmup.py`, `vllm/model_executor/warmup/fa4_cutedsl_config.py` _+5 more__
- **2026-06-30** [`3cecee40f3`](https://github.com/vllm-project/vllm/commit/3cecee40f3) [#47066](https://github.com/vllm-project/vllm/pull/47066)
  [Model Runner V2][Spec Decode] Fix stale values in idx_mapping from CG num reqs padding (#47066)
  _Files: `vllm/v1/worker/gpu/sample/gumbel.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-06-30** [`a7732537f4`](https://github.com/vllm-project/vllm/commit/a7732537f4) [#47039](https://github.com/vllm-project/vllm/pull/47039)
  [Bugfix] Restore part of bugfix #42650 after accidental deletion in #43241 (#47039)
  _Files: `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/backends/utils.py`_
- **2026-06-30** [`fcaa84efa7`](https://github.com/vllm-project/vllm/commit/fcaa84efa7) [#47050](https://github.com/vllm-project/vllm/pull/47050)
  [BugFix] Gate MRV2 mixed sparse-MLA warmup on `max_num_seqs` > 1 (#47050)
  _Files: `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/model_executor/warmup/flashinfer_sparse_mla_warmup.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-06-30** [`8cf7c4d8ad`](https://github.com/vllm-project/vllm/commit/8cf7c4d8ad) [#46020](https://github.com/vllm-project/vllm/pull/46020)
  [Attention Backend] add HPC-Ops Attention backend (#46020)
  _Files: `docs/design/attention_backends.md`, `vllm/config/compilation.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/model_executor/layers/hpc/__init__.py` _+6 more__
- **2026-06-30** [`0feca7ffa8`](https://github.com/vllm-project/vllm/commit/0feca7ffa8) [#46807](https://github.com/vllm-project/vllm/pull/46807)
  PD disagg with Mooncake Connector: GDN support (Qwen3.5) and MLA support (Deepseek-V4-Flash) (#46807)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hma.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py` _+3 more__
- **2026-06-30** [`b153dd3f28`](https://github.com/vllm-project/vllm/commit/b153dd3f28) [#47074](https://github.com/vllm-project/vllm/pull/47074)
  [Bugfix] Use larger workspace size for Flashinfer MLA LSE (#47074)
  _Files: `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-06-30** [`5b4cb69523`](https://github.com/vllm-project/vllm/commit/5b4cb69523) [#47079](https://github.com/vllm-project/vllm/pull/47079)
  [Bugfix][MLA] Fix LSE log-base mismatch in DCP + FlashInfer MLA decode (#47079)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-06-29** [`75698e60b3`](https://github.com/vllm-project/vllm/commit/75698e60b3) [#47083](https://github.com/vllm-project/vllm/pull/47083)
  [Bug] Fix sparse attention issue for GLM5.2 non-torch compile path (#47083)
  _Files: `vllm/models/deepseek_v32/nvidia/attention.py`_
- **2026-06-29** [`8fc1b2d046`](https://github.com/vllm-project/vllm/commit/8fc1b2d046) [#46659](https://github.com/vllm-project/vllm/pull/46659)
  Fix FA4 dynamic_causal for full attention layers (#46659)
  _Files: `vllm/v1/attention/backends/flash_attn.py`_
- **2026-06-29** [`a309d4fe60`](https://github.com/vllm-project/vllm/commit/a309d4fe60) [#43729](https://github.com/vllm-project/vllm/pull/43729)
  Support DCP with FlashInfer MLA (#43729)
  _Files: `docs/design/attention_backends.md`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-06-29** [`030c9523bd`](https://github.com/vllm-project/vllm/commit/030c9523bd) [#46634](https://github.com/vllm-project/vllm/pull/46634)
  [Perf][1/N] Expand Triton kernel warmup coverage, DSv4 (#46634)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/sparse_mla_triton_warmup.py`, `vllm/model_executor/warmup/v1_block_table_warmup.py`_
- **2026-06-29** [`4708292d48`](https://github.com/vllm-project/vllm/commit/4708292d48) [#46683](https://github.com/vllm-project/vllm/pull/46683)
  Bump flashinfer version to 0.6.13 (#46683)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.nightly_torch`, `docker/versions.json`, `requirements/cuda.txt` _+2 more__
- **2026-06-29** [`6149187a4c`](https://github.com/vllm-project/vllm/commit/6149187a4c) [#46819](https://github.com/vllm-project/vllm/pull/46819)
  [Kernel] Triton MLA logits workspace (#46819)
  _Files: `vllm/v1/attention/backends/mla/triton_mla.py`_

## MoE / Expert Parallel  (25 commits)

- **2026-07-06** [`98ba9b9583`](https://github.com/vllm-project/vllm/commit/98ba9b9583) [#47024](https://github.com/vllm-project/vllm/pull/47024)
  [Frontend] Support OpenAI Responses API namespace tools (#47024)
  _Files: `tests/entrypoints/openai/responses/test_namespace_tool_separator.py`, `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/protocol.py` _+4 more__
- **2026-07-06** [`f1073c050c`](https://github.com/vllm-project/vllm/commit/f1073c050c) [#46739](https://github.com/vllm-project/vllm/pull/46739)
  [CPU][BugFix] Multiple fixes to w4a8_int8 CPU MoE path (#46739)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `csrc/cpu/torch_bindings.cpp`, `csrc/moe/dynamic_4bit_int_moe_cpu.cpp`, `csrc/ops.h` _+6 more__
- **2026-07-06** [`f2aaf59151`](https://github.com/vllm-project/vllm/commit/f2aaf59151) [#44880](https://github.com/vllm-project/vllm/pull/44880)
  [Feature] Support MTP speculative decoding for Bailing hybrid models (#44880)
  _Files: `tests/config/test_bailing_mtp_config.py`, `tests/models/registry.py`, `tests/v1/attention/test_linear_attention_metadata_builder.py`, `vllm/config/speculative.py` _+7 more__
- **2026-07-05** [`b6cc46ec3b`](https://github.com/vllm-project/vllm/commit/b6cc46ec3b) [#47070](https://github.com/vllm-project/vllm/pull/47070)
  [Feature] Support sequence parallel without the need for DP, 1.9%~5.0% E2E Throughput Improvement (#47070)
  _Files: `vllm/config/parallel.py`, `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/forward_context.py`, `vllm/model_executor/layers/fused_moe/config.py` _+3 more__
- **2026-07-03** [`fbc9ba6d30`](https://github.com/vllm-project/vllm/commit/fbc9ba6d30) [#46656](https://github.com/vllm-project/vllm/pull/46656)
  New stable abi cleanup (#46656)
  _Files: `csrc/libtorch_stable/cub_helpers.h`, `csrc/libtorch_stable/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`, `csrc/libtorch_stable/cutlass_extensions/torch_utils.hpp`, `csrc/libtorch_stable/cutlass_extensions/vllm_collective_builder.cuh` _+46 more__
- **2026-07-02** [`178fd56094`](https://github.com/vllm-project/vllm/commit/178fd56094) [#47410](https://github.com/vllm-project/vllm/pull/47410)
  support GLM-5.2 gate use FP32 (#47410)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`, `vllm/model_executor/models/deepseek_v2.py`_
- **2026-07-02** [`2665ed704b`](https://github.com/vllm-project/vllm/commit/2665ed704b) [#46838](https://github.com/vllm-project/vllm/pull/46838)
  [Bugfix][Kernel] Correct FlashInfer CUTLASS MoE tuning token bound (#46838)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`_
- **2026-07-02** [`d63c8e9444`](https://github.com/vllm-project/vllm/commit/d63c8e9444) [#47238](https://github.com/vllm-project/vllm/pull/47238)
  [BugFix][Spec Decode] Compact shared topk indices buffer after first MTP draft step (#47238)
  _Files: `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-07-02** [`d0a2584773`](https://github.com/vllm-project/vllm/commit/d0a2584773) [#46984](https://github.com/vllm-project/vllm/pull/46984)
  [Misc] Use functions instead of PTX for the PDL instruction (#46984)
  _Files: `csrc/libtorch_stable/dsv3_fused_a_gemm.cu`, `csrc/libtorch_stable/fp32_router_gemm.cu`, `csrc/libtorch_stable/minimax_reduce_rms_kernel.cu`, `csrc/libtorch_stable/moe/dsv3_router_gemm_bf16_out.cu` _+3 more__
- **2026-07-01** [`fa248139a0`](https://github.com/vllm-project/vllm/commit/fa248139a0) [#45723](https://github.com/vllm-project/vllm/pull/45723)
  [MoE] Plumb gemm1_alpha/beta/clamp_limit into TRT-LLM FP8 MoE (#45723)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w8a8_mxfp8.py`, `vllm/model_executor/layers/quantization/online/mxfp8.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-07-01** [`63fcce4de1`](https://github.com/vllm-project/vllm/commit/63fcce4de1) [#47031](https://github.com/vllm-project/vllm/pull/47031)
  [Bugfix] Fix GraniteMoeShared weight loading broken by #41184 (#47031)
  _Files: `vllm/model_executor/models/granitemoeshared.py`_
- **2026-07-01** [`13c49f9845`](https://github.com/vllm-project/vllm/commit/13c49f9845) [#45368](https://github.com/vllm-project/vllm/pull/45368)
  [xpu][lora]: Align LoRA implementation with Punica GPU: fix _apply_expand rank mismatch, add_inputs hardcode, and MoE EP (#45368)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`, `vllm/lora/ops/xpu_ops/lora_ops.py`, `vllm/lora/punica_wrapper/punica_xpu.py`_
- **2026-07-01** [`e7d0fcbc09`](https://github.com/vllm-project/vllm/commit/e7d0fcbc09) [#47197](https://github.com/vllm-project/vllm/pull/47197)
  [CI] Fix various failures on `main` (#47197)
  _Files: `tests/distributed/test_weight_transfer.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/models/deepseek_v2.py` _+1 more__
- **2026-06-30** [`c8d2f3cb14`](https://github.com/vllm-project/vllm/commit/c8d2f3cb14) [#47154](https://github.com/vllm-project/vllm/pull/47154)
  [Bugfix] compressed-tensors: allow int8 grouped WNA16 MoE on Marlin (#47154)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16_marlin.py`_
- **2026-06-30** [`245888ff77`](https://github.com/vllm-project/vllm/commit/245888ff77) [#43637](https://github.com/vllm-project/vllm/pull/43637)
  [Feature] Detect all2all peer fault with fault tolerance backend and prevent corrupted output (#43637)
  _Files: `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/model_executor/layers/fused_moe/all2all_utils.py`, `vllm/v1/executor/multiproc_executor.py` _+1 more__
- **2026-06-30** [`e840f0d3f5`](https://github.com/vllm-project/vllm/commit/e840f0d3f5) [#47140](https://github.com/vllm-project/vllm/pull/47140)
  [Platform] Replace `torch.cuda.Event` with `torch.Event` (#47140)
  _Files: `benchmarks/benchmark_topk_topp.py`, `benchmarks/kernels/benchmark_moe_defaults.py`, `benchmarks/kernels/benchmark_selective_state_update.py`, `tests/v1/kv_connector/unit/test_hf3fs_connector.py` _+27 more__
- **2026-06-30** [`1ab9522935`](https://github.com/vllm-project/vllm/commit/1ab9522935) [#47058](https://github.com/vllm-project/vllm/pull/47058)
  Remove more unnecessary `load_weights` methods (#47058)
  _Files: `tests/models/multimodal/processing/test_moss_audio.py`, `vllm/lora/layers/fused_moe.py`, `vllm/lora/utils.py`, `vllm/model_executor/layers/fused_moe/layer.py` _+59 more__
- **2026-06-30** [`fb42e5219e`](https://github.com/vllm-project/vllm/commit/fb42e5219e) [#44825](https://github.com/vllm-project/vllm/pull/44825)
  [Platform] Replace `torch.cuda.mem_get_info` with `torch.accelerator.get_memory_info` (#44825)
  _Files: `tests/basic_correctness/test_mem.py`, `tests/kernels/moe/test_moe.py`, `tests/models/multimodal/generation/test_memory_leak.py`, `tests/utils_/test_mem_utils.py` _+13 more__
- **2026-06-29** [`debec6440b`](https://github.com/vllm-project/vllm/commit/debec6440b) [#46756](https://github.com/vllm-project/vllm/pull/46756)
  Add MiniMax-M3 modelopt nvfp4 support (#46756)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`_
- **2026-06-29** [`bc8481af09`](https://github.com/vllm-project/vllm/commit/bc8481af09) [#43373](https://github.com/vllm-project/vllm/pull/43373)
  [MoE Refactor] Standardize Humming MoE experts + utilities (#43373)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a4_mxfp4.py`, `vllm/model_executor/layers/quantization/fp8.py` _+4 more__
- **2026-06-29** [`e186107870`](https://github.com/vllm-project/vllm/commit/e186107870) [#45961](https://github.com/vllm-project/vllm/pull/45961)
  [Bugfix] Use native SiLU activation in CPU fused MoE (#45961)
  _Files: `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`_
- **2026-06-29** [`f6bb8682ee`](https://github.com/vllm-project/vllm/commit/f6bb8682ee) [#47009](https://github.com/vllm-project/vllm/pull/47009)
  Fix docs on main (#47009)
  _Files: `docs/design/moe_kernel_features.md`_
- **2026-06-29** [`58d6a6e60a`](https://github.com/vllm-project/vllm/commit/58d6a6e60a) [#42920](https://github.com/vllm-project/vllm/pull/42920)
  [CPU] Support cpu compressed-tensor w8a8 int8 moe (#42920)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`, `tests/quantization/test_cpu_w8a8.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py` _+2 more__
- **2026-06-29** [`a2abce646f`](https://github.com/vllm-project/vllm/commit/a2abce646f) [#38128](https://github.com/vllm-project/vllm/pull/38128)
  [EPLB] Mask padding in EPLB load recording (#38128)
  _Files: `tests/distributed/test_eplb_fused_moe_layer_dep_nvfp4.py`, `tests/kernels/moe/test_moe_layer.py`, `tests/kernels/moe/test_routing.py`, `tests/model_executor/test_routed_experts_capture.py` _+13 more__
- **2026-06-29** [`311ad689ad`](https://github.com/vllm-project/vllm/commit/311ad689ad) [#46956](https://github.com/vllm-project/vllm/pull/46956)
  Remove boilerplate missed by #46820 (#46956)
  _Files: `vllm/model_executor/models/gemma4_unified.py`, `vllm/model_executor/models/mllama4.py`, `vllm/model_executor/models/param2moe.py`, `vllm/model_executor/models/sarvam.py` _+2 more__

## Models  (22 commits)

- **2026-07-06** [`d039c17114`](https://github.com/vllm-project/vllm/commit/d039c17114) [#47448](https://github.com/vllm-project/vllm/pull/47448)
  [Bugfix] Recycle post-final-norm hidden in GLM MTP (single norm) (#47448)
  _Files: `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-07-05** [`8974ed89cd`](https://github.com/vllm-project/vllm/commit/8974ed89cd) [#44461](https://github.com/vllm-project/vllm/pull/44461)
  [Bugfix][Voxtral Realtime] Fix token feedback timeout silent hang (#44461)
  _Files: `vllm/model_executor/models/voxtral_realtime.py`_
- **2026-07-05** [`fb2faceacd`](https://github.com/vllm-project/vllm/commit/fb2faceacd) [#46037](https://github.com/vllm-project/vllm/pull/46037)
  [Bugfix][Model] Fix crash loading Mamba/Mamba2 checkpoints without an `architectures` field (#46037)
  _Files: `vllm/config/vllm.py`_
- **2026-07-05** [`91b5647300`](https://github.com/vllm-project/vllm/commit/91b5647300) [#47337](https://github.com/vllm-project/vllm/pull/47337)
  [Bugfix][Model] Allow Run:ai memory_limit sentinel values (#47337)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/test_runai_model_streamer_loader.py`, `vllm/model_executor/model_loader/runai_streamer_loader.py`_
- **2026-07-04** [`2a9113f998`](https://github.com/vllm-project/vllm/commit/2a9113f998) [#47198](https://github.com/vllm-project/vllm/pull/47198)
  [Perf] Remove redundant op for GLM 5.2 (#47198)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-07-03** [`d6d39c111e`](https://github.com/vllm-project/vllm/commit/d6d39c111e) [#47155](https://github.com/vllm-project/vllm/pull/47155)
  [GLM4V] Avoid GLM4V processor init during startup metadata reads (#47155)
  _Files: `vllm/model_executor/models/glm4_1v.py`_
- **2026-07-03** [`d7192cfccf`](https://github.com/vllm-project/vllm/commit/d7192cfccf) [#47539](https://github.com/vllm-project/vllm/pull/47539)
  [CI Bugfix] Lazily import Qwen warmup dependencies (#47539)
  _Files: `vllm/model_executor/warmup/qwen_triton_warmup.py`_
- **2026-07-03** [`bbdcbe4686`](https://github.com/vllm-project/vllm/commit/bbdcbe4686) [#47452](https://github.com/vllm-project/vllm/pull/47452)
  Move Roberta remaining nn.Embedding to VocabParallelEmbedding (#47452)
  _Files: `vllm/model_executor/models/roberta.py`_
- **2026-07-02** [`2b753ad200`](https://github.com/vllm-project/vllm/commit/2b753ad200) [#47093](https://github.com/vllm-project/vllm/pull/47093)
  [Spec Decode] DSpark speculators checkpoint support (#47093)
  _Files: `vllm/model_executor/models/qwen3_dspark.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/transformers_utils/configs/speculators/algos.py`, `vllm/v1/worker/gpu/spec_decode/dspark/speculator.py`_
- **2026-07-01** [`a78c15616f`](https://github.com/vllm-project/vllm/commit/a78c15616f) [#30966](https://github.com/vllm-project/vllm/pull/30966)
  Migrate GPTBigCode and Starcoder2 to the Transformers modeling backend (#30966)
  _Files: `docs/models/supported_models.md`, `tests/distributed/test_pipeline_parallel.py`, `vllm/model_executor/models/gpt_bigcode.py`, `vllm/model_executor/models/registry.py` _+1 more__
- **2026-07-01** [`cc56379e28`](https://github.com/vllm-project/vllm/commit/cc56379e28) [#47192](https://github.com/vllm-project/vllm/pull/47192)
  [Model] Support Hy3 token suffix and JSON Schema array types (#47192)
  _Files: `vllm/reasoning/hy_v3_reasoning_parser.py`, `vllm/tool_parsers/hy_v3_tool_parser.py`_
- **2026-07-01** [`aeb35b90f0`](https://github.com/vllm-project/vllm/commit/aeb35b90f0) [#46512](https://github.com/vllm-project/vllm/pull/46512)
  [Rust Frontend] Add error context in tool parser failures (#46512)
  _Files: `rust/src/parser/src/tool/deepseek_json/deepseek_v3.rs`, `rust/src/parser/src/tool/deepseek_json/deepseek_v31.rs`, `rust/src/parser/src/tool/json/granite4.rs`, `rust/src/parser/src/tool/json/internlm2.rs` _+8 more__
- **2026-06-30** [`7cf7cbcd95`](https://github.com/vllm-project/vllm/commit/7cf7cbcd95) [#45918](https://github.com/vllm-project/vllm/pull/45918)
  [Bugfix] MiniCPM-V 4.6: fix grid rows/cols swap in placeholder generation (#45918)
  _Files: `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-06-30** [`62c7d8009f`](https://github.com/vllm-project/vllm/commit/62c7d8009f) [#47151](https://github.com/vllm-project/vllm/pull/47151)
  Forward fix nightly errors from #44589 (#47151)
  _Files: `vllm/model_executor/models/commandr.py`, `vllm/model_executor/models/gemma3.py`, `vllm/model_executor/models/jina.py`_
- **2026-06-30** [`06fae69114`](https://github.com/vllm-project/vllm/commit/06fae69114) [#47132](https://github.com/vllm-project/vllm/pull/47132)
  [Misc] Mistral label alert (#47132)
  _Files: `.github/workflows/issue_autolabel.yml`_
- **2026-06-29** [`61ab70ec3b`](https://github.com/vllm-project/vllm/commit/61ab70ec3b) [#42406](https://github.com/vllm-project/vllm/pull/42406)
  [Model Runner V2] support mamba hybrid models align prefix cache (#42406)
  _Files: `tests/kernels/mamba/test_precopy_mamba_align.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/config/vllm.py`, `vllm/model_executor/models/diffusion_gemma.py` _+5 more__
- **2026-06-29** [`7be582697b`](https://github.com/vllm-project/vllm/commit/7be582697b) [#46986](https://github.com/vllm-project/vllm/pull/46986)
  [Bugfix] Fix DeepseekV2Model hidden_size (#46986)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-29** [`0ca39c4f1f`](https://github.com/vllm-project/vllm/commit/0ca39c4f1f) [#46973](https://github.com/vllm-project/vllm/pull/46973)
  [Bugfix] Capture final-layer aux hidden state in deepseek_v2 backbone (#46973)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-06-29** [`6185d73882`](https://github.com/vllm-project/vllm/commit/6185d73882) [#46827](https://github.com/vllm-project/vllm/pull/46827)
  [Rust Frontend] Keep literal "null" string for string-typed tool params (#46827)
  _Files: `rust/src/parser/src/tool/deepseek_dsml/deepseek_v32.rs`, `rust/src/parser/src/tool/parameters.rs`_
- **2026-06-29** [`eddfd4cf21`](https://github.com/vllm-project/vllm/commit/eddfd4cf21) [#46750](https://github.com/vllm-project/vllm/pull/46750)
  [Perf][2/N] Expand Triton kernel warmup coverage, Qwen (#46750)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/qwen_triton_warmup.py`_
- **2026-06-29** [`ab132ee98b`](https://github.com/vllm-project/vllm/commit/ab132ee98b) [#46567](https://github.com/vllm-project/vllm/pull/46567)
  Fix model info cache for package models (#46567)
  _Files: `tests/models/test_registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-06-29** [`0e207dac78`](https://github.com/vllm-project/vllm/commit/0e207dac78) [#46835](https://github.com/vllm-project/vllm/pull/46835)
  [Bugfix] Transformers backend: apply learned lm_head.bias for tied-embedding models (#46835)
  _Files: `vllm/model_executor/layers/vocab_parallel_embedding.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/causal.py`_

## Serving / API  (20 commits)

- **2026-07-06** [`394edc8108`](https://github.com/vllm-project/vllm/commit/394edc8108) [#47682](https://github.com/vllm-project/vllm/pull/47682)
  [XPU] limit max-num-seqs in test_lmeval.py for XPU (#47682)
  _Files: `tests/entrypoints/openai/correctness/test_lmeval.py`_
- **2026-07-05** [`9226613043`](https://github.com/vllm-project/vllm/commit/9226613043) [#47590](https://github.com/vllm-project/vllm/pull/47590)
  [Bugfix][Pooling] Forward instruction to Jina reranker scoring prompts (#47590)
  _Files: `examples/pooling/token_embed/jina_reranker_v3_online.py`, `tests/models/language/pooling/test_jina_reranker_v3.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-07-04** [`d2afe39647`](https://github.com/vllm-project/vllm/commit/d2afe39647) [#47597](https://github.com/vllm-project/vllm/pull/47597)
  [Bugfix][Frontend] Preserve default sampling params in batch chat (#47597)
  _Files: `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-07-04** [`0cd6f767e3`](https://github.com/vllm-project/vllm/commit/0cd6f767e3) [#47379](https://github.com/vllm-project/vllm/pull/47379)
  [Bugfix][Frontend][gpt-oss] Recover raw tail when Harmony parser ends non-terminal (#47379)
  _Files: `tests/entrypoints/unit_tests/test_context.py`, `tests/parser/test_harmony.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/parser/harmony.py`_
- **2026-07-04** [`1d354c694e`](https://github.com/vllm-project/vllm/commit/1d354c694e) [#46966](https://github.com/vllm-project/vllm/pull/46966)
  [Misc] Validate Pooling cache_salt Values (#46966)
  _Files: `vllm/entrypoints/pooling/base/protocol.py`_
- **2026-07-04** [`2f21224527`](https://github.com/vllm-project/vllm/commit/2f21224527) [#47333](https://github.com/vllm-project/vllm/pull/47333)
  [Misc] Update request-extras parity for batch chat completion (#47333)
  _Files: `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-07-04** [`fa1fa968c4`](https://github.com/vllm-project/vllm/commit/fa1fa968c4) [#46939](https://github.com/vllm-project/vllm/pull/46939)
  [Misc] Forward request-level prompt extras for cross-encoder scoring (#46939)
  _Files: `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-07-04** [`6eac8e0070`](https://github.com/vllm-project/vllm/commit/6eac8e0070) [#47082](https://github.com/vllm-project/vllm/pull/47082)
  [Misc] Preserve cross-encoder pooling extra kwargs (#47082)
  _Files: `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-07-04** [`ab3b6d97aa`](https://github.com/vllm-project/vllm/commit/ab3b6d97aa) [#47529](https://github.com/vllm-project/vllm/pull/47529)
  [Frontend] Limit `SO_REUSEPORT` to multi-worker serving (#47529)
  _Files: `vllm/entrypoints/cli/launch.py`, `vllm/entrypoints/cli/serve.py`, `vllm/entrypoints/openai/api_server.py`_
- **2026-07-03** [`18f658bb31`](https://github.com/vllm-project/vllm/commit/18f658bb31) [#47384](https://github.com/vllm-project/vllm/pull/47384)
  [Bugfix][Frontend] Fix batch chat endpoint corrupting logprobs when return_token_ids is set (#47384)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`_
- **2026-07-01** [`5c4db60f01`](https://github.com/vllm-project/vllm/commit/5c4db60f01) [#45903](https://github.com/vllm-project/vllm/pull/45903)
  docs(security): document gRPC interface as insecure for private use only (#45903)
  _Files: `docs/usage/security.md`_
- **2026-07-01** [`697c34b97b`](https://github.com/vllm-project/vllm/commit/697c34b97b) [#47126](https://github.com/vllm-project/vllm/pull/47126)
  [Bugfix] Fix beam search candidate indexing when logprobs count varies (#47126)
  _Files: `tests/samplers/test_beam_search_online.py`, `vllm/entrypoints/generate/beam_search/online.py`_
- **2026-07-01** [`5b431b905c`](https://github.com/vllm-project/vllm/commit/5b431b905c) [#47166](https://github.com/vllm-project/vllm/pull/47166)
  [Rust Frontend] Coerce completion `max_tokens: null` to default (#47166)
  _Files: `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/routes/openai/completions/types.rs`_
- **2026-06-30** [`b1190d03cc`](https://github.com/vllm-project/vllm/commit/b1190d03cc) [#47185](https://github.com/vllm-project/vllm/pull/47185)
  [Refactor][GPT-OSS] Harmony Responses API Refactor to use HarmonyParser (#47185)
  _Files: `tests/entrypoints/openai/responses/conftest.py`, `tests/entrypoints/openai/responses/test_harmony.py`, `tests/entrypoints/openai/responses/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_serving_responses.py` _+5 more__
- **2026-06-30** [`3a9784b82c`](https://github.com/vllm-project/vllm/commit/3a9784b82c) [#47076](https://github.com/vllm-project/vllm/pull/47076)
  [Feature] DP supervisor using rust frontend (#47076)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/entrypoints/openai/dp_supervisor.py`_
- **2026-06-30** [`3675bcff67`](https://github.com/vllm-project/vllm/commit/3675bcff67) [#47101](https://github.com/vllm-project/vllm/pull/47101)
  [Rust Frontend] Refactor TLS serve path with unified `MaybeTlsListener` (#47101)
  _Files: `rust/src/server/Cargo.toml`, `rust/src/server/src/grpc/mod.rs`, `rust/src/server/src/grpc/tests.rs`, `rust/src/server/src/lib.rs` _+2 more__
- **2026-06-30** [`aed541def4`](https://github.com/vllm-project/vllm/commit/aed541def4) [#46945](https://github.com/vllm-project/vllm/pull/46945)
  [Bugfix][Responses] Set completed status for Harmony function calls (#46945)
  _Files: `tests/entrypoints/openai/responses/test_harmony_utils.py`, `vllm/entrypoints/openai/responses/harmony.py`_
- **2026-06-30** [`97b5ce5c39`](https://github.com/vllm-project/vllm/commit/97b5ce5c39) [#46612](https://github.com/vllm-project/vllm/pull/46612)
  [Bugfix] Raise VLLMValidationError for non-integer logit_bias keys (#46612)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_logit_bias_validation.py`, `vllm/sampling_params.py`_
- **2026-06-30** [`fca432e60a`](https://github.com/vllm-project/vllm/commit/fca432e60a) [#35076](https://github.com/vllm-project/vllm/pull/35076)
  [Bugfix] Propagate default stop_token_ids to per-request SamplingParams (#35076)
  _Files: `tests/entrypoints/openai/test_stop_token_ids.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-06-29** [`9e86352c60`](https://github.com/vllm-project/vllm/commit/9e86352c60) [#47011](https://github.com/vllm-project/vllm/pull/47011)
  [CI Failure] Add transformers version check for openai/privacy-filter (#47011)
  _Files: `tests/models/language/pooling/test_token_classification.py`_

## Multimodal  (19 commits)

- **2026-07-06** [`40cc2e8327`](https://github.com/vllm-project/vllm/commit/40cc2e8327) [#47165](https://github.com/vllm-project/vllm/pull/47165)
  [Bugfix] Return HTTP 422 for unprocessable image URLs instead of 500 (#47165)
  _Files: `tests/multimodal/media/test_unprocessable_entity_error.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/serve/utils/error_response.py`, `vllm/exceptions.py` _+1 more__
- **2026-07-06** [`ba22152096`](https://github.com/vllm-project/vllm/commit/ba22152096) [#47259](https://github.com/vllm-project/vllm/pull/47259)
  fix(security): block request-level GPU video backend selection withou… (#47259)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/multimodal/media/video.py`, `vllm/multimodal/video.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-06** [`90ce3a09be`](https://github.com/vllm-project/vllm/commit/90ce3a09be) [#47607](https://github.com/vllm-project/vllm/pull/47607)
  [bugfix] fix MOSS-Audio deepstack_input_embeds initialization in PP (#47607)
  _Files: `vllm/model_executor/models/moss_audio.py`_
- **2026-07-03** [`379950191f`](https://github.com/vllm-project/vllm/commit/379950191f) [#47566](https://github.com/vllm-project/vllm/pull/47566)
  [Bugfix][Multimodal] Normalize direct PIL image inputs (#47566)
  _Files: `vllm/multimodal/parse.py`_
- **2026-07-03** [`400a9c386d`](https://github.com/vllm-project/vllm/commit/400a9c386d) [#47530](https://github.com/vllm-project/vllm/pull/47530)
  [Rust Frontend] Bump llm-multimodal version (#47530)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/multimodal.rs` _+2 more__
- **2026-07-03** [`4875b4456b`](https://github.com/vllm-project/vllm/commit/4875b4456b) [#47517](https://github.com/vllm-project/vllm/pull/47517)
  [Doc] Fix VLM2Vec benchmark chat template path (#47517)
  _Files: `docs/benchmarking/cli.md`_
- **2026-07-02** [`443e68cfa6`](https://github.com/vllm-project/vllm/commit/443e68cfa6) [#47437](https://github.com/vllm-project/vllm/pull/47437)
  [Bugfix] Fix pooled Whisper encoder sliding-window kernel size (#47437)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `vllm/model_executor/models/whisper_causal.py`_
- **2026-07-02** [`b0b8a286dd`](https://github.com/vllm-project/vllm/commit/b0b8a286dd) [#44785](https://github.com/vllm-project/vllm/pull/44785)
  [Model] Add LLaVA-OneVision-2 (LlavaOnevision2ForConditionalGeneration) (#44785)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llava_onevision2.py`, `tests/models/registry.py` _+2 more__
- **2026-07-01** [`c8bdcc0116`](https://github.com/vllm-project/vllm/commit/c8bdcc0116) [#47135](https://github.com/vllm-project/vllm/pull/47135)
  [Bench][BugFix] Fix empty decoder prompt for Cohere ASR in throughput benchmark (#47135)
  _Files: `tests/benchmarks/test_audio_dataset.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-07-01** [`c638f9216a`](https://github.com/vllm-project/vllm/commit/c638f9216a) [#47265](https://github.com/vllm-project/vllm/pull/47265)
  [Rust Frontend] Split engine core DTOs into separate modules (#47265)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs`, `rust/src/chat/src/multimodal/tensor.rs`, `rust/src/chat/src/output/default/structural_tag.rs` _+50 more__
- **2026-07-01** [`a22e0dfc69`](https://github.com/vllm-project/vllm/commit/a22e0dfc69) [#47263](https://github.com/vllm-project/vllm/pull/47263)
  [Model] Remove AyaVision, MusicFlamingo (#47263)
  _Files: `docs/models/supported_models.md`, `examples/generate/multimodal/audio_language_offline.py`, `examples/generate/multimodal/vision_language_multi_image_offline.py`, `examples/generate/multimodal/vision_language_offline.py` _+8 more__
- **2026-07-01** [`fa4bec9056`](https://github.com/vllm-project/vllm/commit/fa4bec9056) [#47071](https://github.com/vllm-project/vllm/pull/47071)
  [Bugfix] Fix pooled Whisper sliding-window KV sizing (#47071)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `vllm/model_executor/models/whisper_causal.py`_
- **2026-06-30** [`68294739d1`](https://github.com/vllm-project/vllm/commit/68294739d1) [#47099](https://github.com/vllm-project/vllm/pull/47099)
  [Bugfix] Align OpenCV video metadata timeline (#47099)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/assets/video.py`_
- **2026-06-30** [`7a327f0b4f`](https://github.com/vllm-project/vllm/commit/7a327f0b4f) [#47125](https://github.com/vllm-project/vllm/pull/47125)
  [Rust Frontend] Simplify unit tests with shared `TestTokenizer` (#47125)
  _Files: `rust/Cargo.lock`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/multimodal.rs` _+24 more__
- **2026-06-30** [`ab80b3dff4`](https://github.com/vllm-project/vllm/commit/ab80b3dff4) [#47139](https://github.com/vllm-project/vllm/pull/47139)
  [CI/Build] Bump PyNvVideoCodec version (#47139)
  _Files: `requirements/cuda.txt`_
- **2026-06-30** [`5dc36a4fa5`](https://github.com/vllm-project/vllm/commit/5dc36a4fa5) [#47143](https://github.com/vllm-project/vllm/pull/47143)
  [Model] Remove Tarsier, Tarsier2 (#47143)
  _Files: `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_multi_image_offline.py`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_common.py` _+8 more__
- **2026-06-30** [`364ee36af1`](https://github.com/vllm-project/vllm/commit/364ee36af1) [#47010](https://github.com/vllm-project/vllm/pull/47010)
  fix(security): prevent image decompression bomb OOM denial of service (#47010)
  _Files: `docs/usage/security.md`, `tests/multimodal/media/test_image.py`, `vllm/envs.py`, `vllm/multimodal/media/image.py` _+3 more__
- **2026-06-29** [`59575da46d`](https://github.com/vllm-project/vllm/commit/59575da46d) [#47008](https://github.com/vllm-project/vllm/pull/47008)
  [XPU] exclude unsupported models for test_tensor_sechma.py (#47008)
  _Files: `.buildkite/intel_jobs/models_multimodal_intel.yaml`, `tests/models/multimodal/processing/test_common.py`_
- **2026-06-29** [`4559c43a95`](https://github.com/vllm-project/vllm/commit/4559c43a95) [#43591](https://github.com/vllm-project/vllm/pull/43591)
  [MM][CG] Gemma3 Encoder CUDA Graph (#43591)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/gemma3_mm.py`_

## CI / Build  (17 commits)

- **2026-07-06** [`cdab28319f`](https://github.com/vllm-project/vllm/commit/cdab28319f) [#47675](https://github.com/vllm-project/vllm/pull/47675)
  [XPU][CI]Add agent tags for Basic Models Tests (Initialization) in Intel GPU CI (#47675)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-06** [`990c2a0187`](https://github.com/vllm-project/vllm/commit/990c2a0187) [#45243](https://github.com/vllm-project/vllm/pull/45243)
  [RISC-V] Enable BF16 on VLEN=256 hardware (#45243)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-07-06** [`e9cc1fd093`](https://github.com/vllm-project/vllm/commit/e9cc1fd093) [#47687](https://github.com/vllm-project/vllm/pull/47687)
  [CI/Build][CPU] Remove global extra index (#47687)
  _Files: `docker/Dockerfile.cpu`, `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.apple.inc.md`, `docs/getting_started/installation/cpu.s390x.inc.md` _+2 more__
- **2026-07-03** [`2dfaae752b`](https://github.com/vllm-project/vllm/commit/2dfaae752b) [#47510](https://github.com/vllm-project/vllm/pull/47510)
  [XPU][CI]Fix dependency typo in Intel GPU CI  (#47510)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-03** [`bd8d9021ce`](https://github.com/vllm-project/vllm/commit/bd8d9021ce) [#47467](https://github.com/vllm-project/vllm/pull/47467)
  [CPU][Build] Enable oneDNN ITT task collection by default for CPU primitive-level profiling (#47467)
  _Files: `cmake/cpu_extension.cmake`_
- **2026-07-03** [`3f0b773b30`](https://github.com/vllm-project/vllm/commit/3f0b773b30) [#47405](https://github.com/vllm-project/vllm/pull/47405)
  [XPU][CI]Mv huggingface cache to larger disk in Intel GPU CI (#47405)
  _Files: `.buildkite/ci_config_intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-test.sh`_
- **2026-07-02** [`a2f713002d`](https://github.com/vllm-project/vllm/commit/a2f713002d) [#44443](https://github.com/vllm-project/vllm/pull/44443)
  [ModelRunner V2] Enable by default for all dense models (#44443)
  _Files: `.buildkite/test_areas/model_runner_v2.yaml`, `tests/distributed/test_multiproc_executor.py`, `tests/distributed/test_ray_v2_executor.py`, `tests/test_config.py` _+2 more__
- **2026-07-02** [`84b9c2762f`](https://github.com/vllm-project/vllm/commit/84b9c2762f) [#47304](https://github.com/vllm-project/vllm/pull/47304)
  Update DeepGEMM tag to point to latest nv-dev branch for sm120 support (#47304)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-07-02** [`1360c42fe6`](https://github.com/vllm-project/vllm/commit/1360c42fe6) [#47319](https://github.com/vllm-project/vllm/pull/47319)
  [UX] Include NVTX in cuda.txt (#47319)
  _Files: `requirements/cuda.txt`_
- **2026-07-01** [`e196268bad`](https://github.com/vllm-project/vllm/commit/e196268bad) [#47338](https://github.com/vllm-project/vllm/pull/47338)
  [Docker] Remove unused Dockerfile.nightly_torch (#47338)
  _Files: `docker/Dockerfile.nightly_torch`_
- **2026-07-01** [`f1cf6b0086`](https://github.com/vllm-project/vllm/commit/f1cf6b0086) [#47299](https://github.com/vllm-project/vllm/pull/47299)
  [CI] Fix segfault in tracing test (#47299)
  _Files: `tests/v1/tracing/test_tracing.py`_
- **2026-07-01** [`89e99202f2`](https://github.com/vllm-project/vllm/commit/89e99202f2) [#44639](https://github.com/vllm-project/vllm/pull/44639)
  [CPU][Perf]Added tanh AOR for faster gelu activations. (#44639)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/activation.cpp`, `csrc/cpu/cpu_tanhf_neon.hpp`, `csrc/cpu/cpu_types_arm.hpp` _+5 more__
- **2026-06-30** [`7a341fa109`](https://github.com/vllm-project/vllm/commit/7a341fa109) [#47105](https://github.com/vllm-project/vllm/pull/47105)
  [XPU] Support ZE_AFFINITY_MASK passthrough in xpu_disagg_acc_test (#47105)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `tests/v1/kv_connector/nixl_integration/run_xpu_disagg_accuracy_test.sh`_
- **2026-06-30** [`dc148dc4d7`](https://github.com/vllm-project/vllm/commit/dc148dc4d7) [#47157](https://github.com/vllm-project/vllm/pull/47157)
  [CI][Bugfix] Fix `Hybrid SSM NixlConnector PD prefix cache test (2 GPUs)` (#47157)
  _Files: `tests/v1/kv_connector/nixl_integration/run_mamba_prefix_cache_test.sh`_
- **2026-06-30** [`ea9ddf59fc`](https://github.com/vllm-project/vllm/commit/ea9ddf59fc) [#45977](https://github.com/vllm-project/vllm/pull/45977)
  [XPU][CI] Enable shared loader test (#45977)
  _Files: `.buildkite/intel_jobs/models_distributed_intel.yaml`, `tests/model_executor/model_loader/test_sharded_state_loader.py`_
- **2026-06-30** [`14f8660a18`](https://github.com/vllm-project/vllm/commit/14f8660a18) [#47032](https://github.com/vllm-project/vllm/pull/47032)
  [CI/Build] Add CPU test dependency pre-commit hooks (#47032)
  _Files: `.pre-commit-config.yaml`, `docker/Dockerfile.cpu`, `requirements/test/cpu.txt`_
- **2026-06-29** [`c8fb2963bd`](https://github.com/vllm-project/vllm/commit/c8fb2963bd) [#46713](https://github.com/vllm-project/vllm/pull/46713)
  [FS-Offloading] Batch Lookup in C  (#46713)
  _Files: `CMakeLists.txt`, `csrc/fs_io.cpp`, `setup.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+1 more__

## Scheduler / Engine  (14 commits)

- **2026-07-06** [`2fa10566e3`](https://github.com/vllm-project/vllm/commit/2fa10566e3) [#47420](https://github.com/vllm-project/vllm/pull/47420)
  [Core][DP] Rotate load-balancer tie-break to avoid systematic engine bias (#47420)
  _Files: `vllm/v1/engine/core_client.py`_
- **2026-07-04** [`e7c9df9449`](https://github.com/vllm-project/vllm/commit/e7c9df9449) [#44297](https://github.com/vllm-project/vllm/pull/44297)
  [Bugfix][Structured Output][Spec Decode] Constrain bitmask and trim grammar advance at the reasoning boundary (#44297)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/spec_decode/test_mtp_structured_output.py`, `vllm/v1/core/sched/scheduler.py` _+2 more__
- **2026-07-03** [`6429d5f527`](https://github.com/vllm-project/vllm/commit/6429d5f527) [#46684](https://github.com/vllm-project/vllm/pull/46684)
  [Rust Frontend] add repetition_detection support to sampling params (#46684)
  _Files: `rust/src/engine-core-client/src/protocol/sampling.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/llm/src/output.rs`, `rust/src/server/src/grpc/convert.rs` _+10 more__
- **2026-07-02** [`e392bf7a68`](https://github.com/vllm-project/vllm/commit/e392bf7a68) [#46974](https://github.com/vllm-project/vllm/pull/46974)
  [BugFix][MRV2] Ensure all req slots are accounted for when scheduling (#46974)
  _Files: `tests/v1/core/test_worker_slot_overflow.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-02** [`ec0ffaacc8`](https://github.com/vllm-project/vllm/commit/ec0ffaacc8) [#47435](https://github.com/vllm-project/vllm/pull/47435)
  [Rust Frontend] Improve scheduler stats logging parity (#47435)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/llm/src/lib.rs` _+2 more__
- **2026-07-02** [`25fcb65d51`](https://github.com/vllm-project/vllm/commit/25fcb65d51) [#47283](https://github.com/vllm-project/vllm/pull/47283)
  [Rust Frontend] Use enum-backed domain types for engine outputs and structured outputs (#47283)
  _Files: `rust/src/chat/src/output/default/structural_tag.rs`, `rust/src/chat/tests/chat.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/coordinator/inproc.rs` _+12 more__
- **2026-07-02** [`08a8a4af3f`](https://github.com/vllm-project/vllm/commit/08a8a4af3f) [#46306](https://github.com/vllm-project/vllm/pull/46306)
  feat(rust): expose profiler control routes in Rust frontend (#46306)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/managed-engine/src/cli.rs` _+7 more__
- **2026-07-02** [`7fe7fa9cda`](https://github.com/vllm-project/vllm/commit/7fe7fa9cda) [#47208](https://github.com/vllm-project/vllm/pull/47208)
  [CI][Bugfix] Rerun test_engine_log_metrics_ray on Ray GCS startup timeout (#47208)
  _Files: `tests/v1/metrics/test_ray_metrics.py`_
- **2026-06-30** [`ac521f6237`](https://github.com/vllm-project/vllm/commit/ac521f6237) [#45346](https://github.com/vllm-project/vllm/pull/45346)
  [Bugfix][Structured Outputs] Reject degenerate `structured_outputs` that crash EngineCore (#45346)
  _Files: `tests/v1/structured_output/test_validation.py`, `vllm/sampling_params.py`_
- **2026-06-30** [`25671cb520`](https://github.com/vllm-project/vllm/commit/25671cb520) [#46875](https://github.com/vllm-project/vllm/pull/46875)
  [Parser][Bugfix] Ensure tool call or other special tokens don't leak in non-streaming tool parsing (#46875)
  _Files: `tests/parser/engine/conftest.py`, `tests/parser/engine/replay_harness.py`, `tests/parser/engine/test_delegating_replay.py`, `tests/parser/engine/test_gemma4_streaming_reasoning.py` _+10 more__
- **2026-06-30** [`1907d3854a`](https://github.com/vllm-project/vllm/commit/1907d3854a) [#44002](https://github.com/vllm-project/vllm/pull/44002)
  [Bugfix] Reject negative values for max_logprobs and long_prefill_token_threshold (#44002)
  _Files: `vllm/config/scheduler.py`_
- **2026-06-30** [`e45c8a9f4b`](https://github.com/vllm-project/vllm/commit/e45c8a9f4b) [#46833](https://github.com/vllm-project/vllm/pull/46833)
  [Rust Frontend] Start current wave for a stale DP FirstRequest (#46833)
  _Files: `rust/src/engine-core-client/src/coordinator/handle.rs`, `rust/src/engine-core-client/src/coordinator/inproc.rs`_
- **2026-06-30** [`af1ee8c475`](https://github.com/vllm-project/vllm/commit/af1ee8c475) [#44070](https://github.com/vllm-project/vllm/pull/44070)
  fix(config): reject negative max_logprobs (except -1) and long_prefill_token_threshold (#44070)
  _Files: `vllm/config/model.py`, `vllm/config/scheduler.py`_
- **2026-06-30** [`b8cb75b149`](https://github.com/vllm-project/vllm/commit/b8cb75b149) [#45890](https://github.com/vllm-project/vllm/pull/45890)
  [Rust Frontend] Add static HTTPS and mTLS support for HTTP and gRPC (#45890)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+12 more__

## Quantization  (11 commits)

- **2026-07-06** [`e433634c78`](https://github.com/vllm-project/vllm/commit/e433634c78) [#47538](https://github.com/vllm-project/vllm/pull/47538)
  [Performance][Hardware][RISC-V] Reduce LMUL pressure in INT4 LUT dequant (#47538)
  _Files: `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-07-06** [`d9c1767cd4`](https://github.com/vllm-project/vllm/commit/d9c1767cd4) [#46361](https://github.com/vllm-project/vllm/pull/46361)
  [INC][ARK] Direct Register Custom Op for ARK (#46361)
  _Files: `docs/features/quantization/inc.md`, `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_ark_ops.py` _+2 more__
- **2026-07-04** [`1a308c449c`](https://github.com/vllm-project/vllm/commit/1a308c449c) [#43645](https://github.com/vllm-project/vllm/pull/43645)
  [XPU] Add W8A8 FP8 linear kernel with multi-granularity quant support (#43645)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docs/features/quantization/online.md`, `vllm/config/kernel.py`, `vllm/model_executor/kernels/linear/__init__.py` _+2 more__
- **2026-07-03** [`34bf7b45a0`](https://github.com/vllm-project/vllm/commit/34bf7b45a0) [#46456](https://github.com/vllm-project/vllm/pull/46456)
  [CI] intel CI: add quantization and awq case for xpu (#46456)
  _Files: `.buildkite/intel_jobs/quantization.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-07-01** [`d3229431f9`](https://github.com/vllm-project/vllm/commit/d3229431f9) [#47229](https://github.com/vllm-project/vllm/pull/47229)
  [DSV4] Better MXFP8 quantization kernel (#47229)
  _Files: `vllm/model_executor/layers/quantization/utils/mxfp8_utils.py`_
- **2026-06-30** [`92c7fac640`](https://github.com/vllm-project/vllm/commit/92c7fac640) [#45739](https://github.com/vllm-project/vllm/pull/45739)
  [Perf] Restore zero-init of swizzled NVFP4 scale buffer to recover Blackwell decode throughput (#45739)
  _Files: `vllm/_custom_ops.py`_
- **2026-06-30** [`27d5f78b63`](https://github.com/vllm-project/vllm/commit/27d5f78b63) [#47048](https://github.com/vllm-project/vllm/pull/47048)
  [CI] Move distributed small LM eval to B200 (#47048)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DiffusionGemma-26B-A4B-it-FP8-dynamic.yaml`, `tests/evals/gsm8k/gsm8k_eval.py`, `tests/evals/gsm8k/test_gsm8k_correctness.py`_
- **2026-06-30** [`00ebf19cca`](https://github.com/vllm-project/vllm/commit/00ebf19cca) [#46230](https://github.com/vllm-project/vllm/pull/46230)
  [Bugfix][Quant] Raise actionable error instead of bare assert for group-size/TP mismatch (#46230) (#46236)
  _Files: `vllm/distributed/utils.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a8_fp8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a8_int.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py` _+2 more__
- **2026-06-30** [`ae2c4f3db7`](https://github.com/vllm-project/vllm/commit/ae2c4f3db7) [#46804](https://github.com/vllm-project/vllm/pull/46804)
  [XPU][UT]Fix xpu pass_config.fuse_norm_quant assert issue (#46804)
  _Files: `tests/test_config.py`, `vllm/config/compilation.py`_
- **2026-06-29** [`379acd4e4f`](https://github.com/vllm-project/vllm/commit/379acd4e4f) [#46860](https://github.com/vllm-project/vllm/pull/46860)
  [Bugfix][Quantization] Fix W8A8 int-quantized scheme selection regression (#46860)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`_
- **2026-06-29** [`5051698e41`](https://github.com/vllm-project/vllm/commit/5051698e41) [#44589](https://github.com/vllm-project/vllm/pull/44589)
  Remove unnecessary `load_weights` methods (#44589)
  _Files: `tests/model_executor/test_weight_utils.py`, `vllm/lora/worker_manager.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/base_config.py` _+50 more__

## LoRA  (10 commits)

- **2026-07-06** [`6569df6a3e`](https://github.com/vllm-project/vllm/commit/6569df6a3e) [#47534](https://github.com/vllm-project/vllm/pull/47534)
  [Test][LoRA] Use lightweight CPU reference and skip heavy cleanup in punica ops tests (#47534)
  _Files: `tests/lora/test_punica_ops.py`_
- **2026-07-04** [`fb5291b35b`](https://github.com/vllm-project/vllm/commit/fb5291b35b) [#45877](https://github.com/vllm-project/vllm/pull/45877)
  [Frontend] [Parser] Port DeepSeek V4 to streaming parser engine framework (#45877)
  _Files: `tests/parser/engine/test_deepseek_v32.py`, `tests/parser/engine/test_deepseek_v4.py`, `tests/parser/engine/test_replay.py`, `tests/parser/engine/trace_builder.py` _+18 more__
- **2026-07-03** [`a14f57a3ac`](https://github.com/vllm-project/vllm/commit/a14f57a3ac) [#47498](https://github.com/vllm-project/vllm/pull/47498)
  [Frontend] Refine the entrypoint class's inheritance hierarchy. (#47498)
  _Files: `tests/entrypoints/generate/generative_scoring/test_generative_scoring.py`, `tests/entrypoints/openai/responses/test_errors.py`, `tests/entrypoints/openai/test_return_tokens_as_ids.py`, `tests/entrypoints/serve/lora/test_serving_models.py` _+19 more__
- **2026-07-02** [`8357226f4f`](https://github.com/vllm-project/vllm/commit/8357226f4f) [#47376](https://github.com/vllm-project/vllm/pull/47376)
  [XPU][CI] Split test_punica_ops into separate pytest invocations for stability (#47376)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`_
- **2026-07-01** [`8f82be5705`](https://github.com/vllm-project/vllm/commit/8f82be5705) [#47242](https://github.com/vllm-project/vllm/pull/47242)
  [CI/Build]  Fix LoRA testing  (#47242)
  _Files: `tests/lora/test_default_mm_loras.py`_
- **2026-06-30** [`2bc20e8aba`](https://github.com/vllm-project/vllm/commit/2bc20e8aba) [#46610](https://github.com/vllm-project/vllm/pull/46610)
  [Frontend] Add Streaming Parser Engine and new Kimi k2.5/k2.6/k2.7 Parser (#46610)
  _Files: `tests/parser/engine/trace_builder.py`, `tests/reasoning/test_kimi_k2_reasoning_parser.py`, `vllm/parser/engine/registered_adapters.py`, `vllm/parser/kimi_k2.py` _+2 more__
- **2026-06-30** [`8cc242335d`](https://github.com/vllm-project/vllm/commit/8cc242335d) [#46433](https://github.com/vllm-project/vllm/pull/46433)
  [XPU] Optimize XPU worker shutdown logic to prevent resource leak (#46433)
  _Files: `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/lora_intel.yaml`, `tests/utils.py`, `vllm/platforms/xpu.py` _+3 more__
- **2026-06-30** [`a16dbd5b85`](https://github.com/vllm-project/vllm/commit/a16dbd5b85) [#47040](https://github.com/vllm-project/vllm/pull/47040)
  [Rust Frontend] Avoid LoRA registry scans without active LoRA requests (#47040)
  _Files: `rust/src/engine-core-client/src/client/state.rs`_
- **2026-06-30** [`b5c9e1ac33`](https://github.com/vllm-project/vllm/commit/b5c9e1ac33) [#46740](https://github.com/vllm-project/vllm/pull/46740)
  [LoRA] Add language-backbone LoRA support for MiniCPM-V 4.6 (#46740)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-06-29** [`07d33e575b`](https://github.com/vllm-project/vllm/commit/07d33e575b) [#44657](https://github.com/vllm-project/vllm/pull/44657)
  [MyPy] Fix mypy incompatible assignment errors in LRUCacheLoRAModelManager (#44657)
  _Files: `vllm/lora/model_manager.py`_

## Speculative Decoding  (7 commits)

- **2026-07-06** [`d2ec433e37`](https://github.com/vllm-project/vllm/commit/d2ec433e37) [#43957](https://github.com/vllm-project/vllm/pull/43957)
  [XPU] Fix Eagle3 initialization on XPU (#43957)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/model_executor/models/llama_eagle3.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-07-04** [`07516fda67`](https://github.com/vllm-project/vllm/commit/07516fda67) [#45953](https://github.com/vllm-project/vllm/pull/45953)
  [MRV2][SD] Make Dynamic SD comatible with Full Cuda Graphs (#45953)
  _Files: `docs/features/speculative_decoding/dynamic_speculative_decoding.md`, `tests/test_config.py`, `tests/v1/spec_decode/test_dynamic_sd_cug.py`, `vllm/config/compilation.py` _+4 more__
- **2026-07-02** [`3af8789559`](https://github.com/vllm-project/vllm/commit/3af8789559) [#38174](https://github.com/vllm-project/vllm/pull/38174)
  [Feature] Universal speculative decoding for heterogeneous vocabularies (TLI) (#38174)
  _Files: `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/draft_model.md`, `examples/features/speculative_decoding/spec_decode_offline.py`, `tests/v1/spec_decode/test_vocab_mapping.py` _+4 more__
- **2026-07-01** [`df802a87b7`](https://github.com/vllm-project/vllm/commit/df802a87b7) [#47162](https://github.com/vllm-project/vllm/pull/47162)
  [CPU] Remove speculative decoding stream overrides from CPUModelRunner (#47162)
  _Files: `vllm/v1/worker/cpu/shm.py`, `vllm/v1/worker/cpu_model_runner.py`_
- **2026-06-30** [`727971f1c1`](https://github.com/vllm-project/vllm/commit/727971f1c1) [#41396](https://github.com/vllm-project/vllm/pull/41396)
  Add Medusa speculative decoding e2e test (#41396)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/medusa.py`, `vllm/transformers_utils/config.py`_
- **2026-06-30** [`db808b3961`](https://github.com/vllm-project/vllm/commit/db808b3961) [#46781](https://github.com/vllm-project/vllm/pull/46781)
  [Model Runner V2][Spec Decode] Implement block verification for rejection sampling (#46781)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/config/speculative.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-06-29** [`0472436541`](https://github.com/vllm-project/vllm/commit/0472436541) [#46968](https://github.com/vllm-project/vllm/pull/46968)
  [Spec Decode] Avoid redundant hidden-states gather in draft prefill (#46968)
  _Files: `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`_

## Disaggregation / PD  (6 commits)

- **2026-07-01** [`024b06b0dc`](https://github.com/vllm-project/vllm/commit/024b06b0dc) [#42748](https://github.com/vllm-project/vllm/pull/42748)
  [Bugfix] Expose usage field in GenerateResponse for disaggregated serving (#42748)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-07-01** [`77a9c5ae28`](https://github.com/vllm-project/vllm/commit/77a9c5ae28) [#44353](https://github.com/vllm-project/vllm/pull/44353)
  Weight sync refactor + move sparse nccl engine (#44353)
  _Files: `docs/training/layerwise.md`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/base.md`, `docs/training/weight_transfer/ipc.md` _+28 more__
- **2026-06-30** [`953bba488d`](https://github.com/vllm-project/vllm/commit/953bba488d) [#46703](https://github.com/vllm-project/vllm/pull/46703)
  [PERF] Extend NCCL symmetric memory to AllGather and ReduceScatter (#46703)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/distributed/test_nccl_symm_mem.py`, `tests/distributed/test_nccl_symm_mem_allreduce.py`, `vllm/distributed/device_communicators/all_reduce_utils.py` _+2 more__
- **2026-06-30** [`d8f483dc30`](https://github.com/vllm-project/vllm/commit/d8f483dc30) [#46301](https://github.com/vllm-project/vllm/pull/46301)
  [Spec Decode] Fix hidden-state extraction block size for hybrid verifiers (#46301)
  _Files: `tests/v1/kv_connector/unit/test_hidden_states_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`, `vllm/model_executor/models/extract_hidden_states.py`_
- **2026-06-30** [`bec232a914`](https://github.com/vllm-project/vllm/commit/bec232a914) [#42285](https://github.com/vllm-project/vllm/pull/42285)
  Secondary tier implementation for PD disaggregation (#42285)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/p2p/__init__.py`, `tests/v1/kv_offload/tiering/p2p/p2p_connector_proxy.py`, `tests/v1/kv_offload/tiering/p2p/run_accuracy_test.sh` _+18 more__
- **2026-06-30** [`77654d080c`](https://github.com/vllm-project/vllm/commit/77654d080c) [#46777](https://github.com/vllm-project/vllm/pull/46777)
  [KVTransfer] MultiConnector: merge kv_transfer_params dicts across connectors (#46777)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py`_

## KV Cache / Offload  (3 commits)

- **2026-07-05** [`fa4321de3d`](https://github.com/vllm-project/vllm/commit/fa4321de3d) [#47609](https://github.com/vllm-project/vllm/pull/47609)
  [Bugfix][TurboQuant] Preserve KV cache dtype in backend shape (#47609)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-06-30** [`0fc2512094`](https://github.com/vllm-project/vllm/commit/0fc2512094) [#46450](https://github.com/vllm-project/vllm/pull/46450)
  [KV Offload] Pass `ScheduleEndContext` to `on_schedule_end` hook (#46450)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+7 more__
- **2026-06-29** [`36bbecd643`](https://github.com/vllm-project/vllm/commit/36bbecd643) [#46958](https://github.com/vllm-project/vllm/pull/46958)
  [BugFix] Revert "[KV Offload] Use background thread for mmap / cpu_tensors pinning" (#46958)
  _Files: `vllm/v1/kv_offload/cpu/gpu_worker.py`_

## Docs  (1 commits)

- **2026-07-06** [`3d7f357ebf`](https://github.com/vllm-project/vllm/commit/3d7f357ebf) [#47701](https://github.com/vllm-project/vllm/pull/47701)
  [Doc] docs: fix note formatting for pooling models (#47701)
  _Files: `docs/models/pooling_models/README.md`_

## Compilation / CUDA Graph  (1 commits)

- **2026-07-01** [`f651a8a9a4`](https://github.com/vllm-project/vllm/commit/f651a8a9a4) [#42486](https://github.com/vllm-project/vllm/pull/42486)
  [XPU][UT]Enable ut qk_norm_rope_fusion (#42486)
  _Files: `tests/compile/passes/test_qk_norm_rope_fusion.py`, `vllm/compilation/passes/vllm_inductor_pass.py`_

---
_Generated 2026-07-06 12:14 UTC_