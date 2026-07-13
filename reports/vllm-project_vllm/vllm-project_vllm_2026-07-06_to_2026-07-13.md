# vllm-project/vllm — Weekly Change Report
**Period:** 2026-07-06 → 2026-07-13  |  **Total commits:** 274

## ✨ New Features This Week

- **2026-07-13** [#48472](https://github.com/vllm-project/vllm/pull/48472) — [CI] Add SPDX license header to Rust/Protobuf sources (#48472)
- **2026-07-13** [#48390](https://github.com/vllm-project/vllm/pull/48390) — [Core] Support fp32 lm_head for generation models via head_dtype (RFC #48305 §3.6) (#48390)
- **2026-07-13** [#48011](https://github.com/vllm-project/vllm/pull/48011) — [Attention] Make sliding-window support an explicit backend capability (#48011)
- **2026-07-13** [#48064](https://github.com/vllm-project/vllm/pull/48064) — [Distributed][Perf] Enable FlashInfer MNNVL allreduce RMS quant fusion (#48064)
- **2026-07-13** [#46090](https://github.com/vllm-project/vllm/pull/46090) — [CPU][Spec Decode] Support DFlash speculative decoding for GDN models on CPU (#46090)
- **2026-07-13** [#47287](https://github.com/vllm-project/vllm/pull/47287) — [ROCm][MiniMax-M3] Add AITER sparse paged attention (#47287)
- **2026-07-13** [#39058](https://github.com/vllm-project/vllm/pull/39058) — [Kernel] Implement CUDA kernel for ReLUSquaredActivation (relu^2) (#39058)
- **2026-07-12** [#42433](https://github.com/vllm-project/vllm/pull/42433) — [EC Connector] Add EC Transfer Params (#42433)
- **2026-07-12** [#47173](https://github.com/vllm-project/vllm/pull/47173) — [Frontend] Add /abort_requests to the RLHF dev API router (#47173)
- **2026-07-11** [#48268](https://github.com/vllm-project/vllm/pull/48268) — Add VLLM_FLASHINFER_AUTOTUNE_SKIP_OPS and skip CuTeDSL fp4_gemm autotuning by default (#48268)
- _…and 44 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-13** [`bea70c7cfc`](https://github.com/vllm-project/vllm/commit/bea70c7cfc) [#48011](https://github.com/vllm-project/vllm/pull/48011) — [Attention] Make sliding-window support an explicit backend capability (#48011)
- **2026-07-13** [`b7b58d1eba`](https://github.com/vllm-project/vllm/commit/b7b58d1eba) [#46527](https://github.com/vllm-project/vllm/pull/46527) — [ROCm][CI] Cache Rust builds by source inputs (#46527)
- **2026-07-13** [`d973cce3ca`](https://github.com/vllm-project/vllm/commit/d973cce3ca) [#48440](https://github.com/vllm-project/vllm/pull/48440) — Re-disable CUDA graph memory profiling on ROCm (#48440)
- **2026-07-13** [`775c1589ea`](https://github.com/vllm-project/vllm/commit/775c1589ea) [#48446](https://github.com/vllm-project/vllm/pull/48446) — [Bugfix][ROCm] Keep TP all_gather on base-class collective (#48446)
- **2026-07-13** [`ee5a89f4d7`](https://github.com/vllm-project/vllm/commit/ee5a89f4d7) [#47287](https://github.com/vllm-project/vllm/pull/47287) — [ROCm][MiniMax-M3] Add AITER sparse paged attention (#47287)
- **2026-07-11** [`51878e5b6e`](https://github.com/vllm-project/vllm/commit/51878e5b6e) [#44455](https://github.com/vllm-project/vllm/pull/44455) — [2/N][KV-Cache Layout Refactor] Pack K/V into the content dim across attention backends (#44455)
- **2026-07-11** [`1bd8f80a64`](https://github.com/vllm-project/vllm/commit/1bd8f80a64) [#48328](https://github.com/vllm-project/vllm/pull/48328) — [CI] Point CI at Transformers release rather than release branch (#48328)
- **2026-07-11** [`4a6440acef`](https://github.com/vllm-project/vllm/commit/4a6440acef) [#47867](https://github.com/vllm-project/vllm/pull/47867) — Bump Transformers version to 5.13.0 (#47867)
- **2026-07-10** [`c227aaa3f8`](https://github.com/vllm-project/vllm/commit/c227aaa3f8) [#47419](https://github.com/vllm-project/vllm/pull/47419) — [ROCm] Enable DeepSeek-V4 DSpark speculative decoding on AMD (MI350X / MI355X, gfx950) (#47419)
- **2026-07-10** [`e257faf87d`](https://github.com/vllm-project/vllm/commit/e257faf87d) [#48158](https://github.com/vllm-project/vllm/pull/48158) — [Refactor] Remove unused rocm kernel `combine_topk_swa_indices_ragged` (#48158)
- **2026-07-10** [`88e5e2c57b`](https://github.com/vllm-project/vllm/commit/88e5e2c57b) [#47366](https://github.com/vllm-project/vllm/pull/47366) — [CI/Build][AMD] Fix ROCm OOM in eagle_correctness_heavy by reserving CUDA graph memory (#47366)
- **2026-07-10** [`a0f6d767e4`](https://github.com/vllm-project/vllm/commit/a0f6d767e4) [#48169](https://github.com/vllm-project/vllm/pull/48169) — [ROCm][CI] Move remaining engine/samplers AMD steps to mi325_1 (#48169)
- **2026-07-09** [`766469a4c4`](https://github.com/vllm-project/vllm/commit/766469a4c4) [#48154](https://github.com/vllm-project/vllm/pull/48154) — [ROCm] Revert Part of `[ROCm] Fix pooling startup workspace lock` #47912 (#48154)
- **2026-07-09** [`bbb0f945ff`](https://github.com/vllm-project/vllm/commit/bbb0f945ff) [#47404](https://github.com/vllm-project/vllm/pull/47404) — [ROCm] Synchronize sparse MLA metadata before graph replay (#47404)
- **2026-07-09** [`b0dec2a11b`](https://github.com/vllm-project/vllm/commit/b0dec2a11b) [#45149](https://github.com/vllm-project/vllm/pull/45149) — [ROCM][DSV32][Perf][MTP] Enable UNIFORM_BATCH CG mode in rocm_aiter_mla_sparse (#45149)
- **2026-07-09** [`2285cfca46`](https://github.com/vllm-project/vllm/commit/2285cfca46) [#46865](https://github.com/vllm-project/vllm/pull/46865) — [KVConnector] MultiConnector: give every sub-connector the request's real blocks in `update_state_after_alloc` (#46865)
- **2026-07-09** [`67e7ea8977`](https://github.com/vllm-project/vllm/commit/67e7ea8977) [#48146](https://github.com/vllm-project/vllm/pull/48146) — [ROCm][CI] Set all timeout_in_minutes to 180 (#48146)
- **2026-07-09** [`2c17d33f42`](https://github.com/vllm-project/vllm/commit/2c17d33f42) [#47144](https://github.com/vllm-project/vllm/pull/47144) — [Bugfix][ROCm] Change AttentionCGSuppoort in TritonMLA to UNIFORM_SINGLE_TOKEN_DECODE (#47144)
- **2026-07-08** [`bc44f9feb7`](https://github.com/vllm-project/vllm/commit/bc44f9feb7) [#47874](https://github.com/vllm-project/vllm/pull/47874) — [ROCm][CI][MoE] Fix double-transpose of fused w3 expert weights (#47874)
- **2026-07-08** [`26831949b4`](https://github.com/vllm-project/vllm/commit/26831949b4) [#47912](https://github.com/vllm-project/vllm/pull/47912) — [ROCm] Fix pooling startup workspace lock (#47912)
- **2026-07-08** [`49abadaedb`](https://github.com/vllm-project/vllm/commit/49abadaedb) [#47894](https://github.com/vllm-project/vllm/pull/47894) — [ROCm][Bugfix] Fix empty-tensor .max() crash in AITER FA (#47894)
- **2026-07-08** [`2cae98dfa5`](https://github.com/vllm-project/vllm/commit/2cae98dfa5) [#47844](https://github.com/vllm-project/vllm/pull/47844) — [Rust Frontend] Handle `continue_final_message` with renderer sentinel (#47844)
- **2026-07-08** [`db39d60010`](https://github.com/vllm-project/vllm/commit/db39d60010) [#47943](https://github.com/vllm-project/vllm/pull/47943) — Add tuned selective_state_update float32 config for AMD Instinct MI355 (#47943)
- **2026-07-08** [`eeaf23107f`](https://github.com/vllm-project/vllm/commit/eeaf23107f) [#47947](https://github.com/vllm-project/vllm/pull/47947) — [ROCm] Add tuned selective_state_update float32 config for AMD Instinct MI300X (#47947)
- **2026-07-08** [`1f4ad059d1`](https://github.com/vllm-project/vllm/commit/1f4ad059d1) [#47945](https://github.com/vllm-project/vllm/pull/47945) — [ROCm] Add tuned selective_state_update float16 config for AMD Instinct MI300X (#47945)
- **2026-07-08** [`2c64b4c1cc`](https://github.com/vllm-project/vllm/commit/2c64b4c1cc) [#47158](https://github.com/vllm-project/vllm/pull/47158) — [ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8 (#47158)
- **2026-07-08** [`d9e57ea82e`](https://github.com/vllm-project/vllm/commit/d9e57ea82e) [#46117](https://github.com/vllm-project/vllm/pull/46117) — [ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3 (#46117)
- **2026-07-08** [`f7fc0ca993`](https://github.com/vllm-project/vllm/commit/f7fc0ca993) [#47454](https://github.com/vllm-project/vllm/pull/47454) — [Frontend] Add endpoint plugins framework (#47454)
- **2026-07-08** [`4aceabf8c1`](https://github.com/vllm-project/vllm/commit/4aceabf8c1) [#47766](https://github.com/vllm-project/vllm/pull/47766) — [ROCm][Bugfix] Key sparse-MLA persistent metadata on per-request context lengths (#47766)
- **2026-07-08** [`6e35c5e5af`](https://github.com/vllm-project/vllm/commit/6e35c5e5af) [#47731](https://github.com/vllm-project/vllm/pull/47731) — [ROCm][CI] Minimize comment in RocmAttention q_scale check (#47731)
- **2026-07-07** [`c8c2f838e7`](https://github.com/vllm-project/vllm/commit/c8c2f838e7) [#47767](https://github.com/vllm-project/vllm/pull/47767) — Add tuned selective_state_update config for AMD Instinct MI355 (#47767)
- **2026-07-07** [`dd94484577`](https://github.com/vllm-project/vllm/commit/dd94484577) [#41359](https://github.com/vllm-project/vllm/pull/41359) — Bump Transformers version to 5.10.4 (#41359)
- **2026-07-07** [`ed051fab54`](https://github.com/vllm-project/vllm/commit/ed051fab54) [#45418](https://github.com/vllm-project/vllm/pull/45418) — [Bugfix] Reject sampling params unsupported by diffusion models (#45418)
- **2026-07-07** [`cbb5f045be`](https://github.com/vllm-project/vllm/commit/cbb5f045be) [#46904](https://github.com/vllm-project/vllm/pull/46904) — [ROCm][CI] Refresh ROCm base images when docker rocm_base changes (#46904)
- **2026-07-07** [`e55cc59e52`](https://github.com/vllm-project/vllm/commit/e55cc59e52) [#47735](https://github.com/vllm-project/vllm/pull/47735) — [Rust Frontend][CI] Unblock more end-to-end test cases (#47735)
- **2026-07-07** [`dd5c299fbe`](https://github.com/vllm-project/vllm/commit/dd5c299fbe) [#47201](https://github.com/vllm-project/vllm/pull/47201) — [ROCm][Bugfix] Convert ModelOpt FP8 per-channel weights to e4m3fnuz on MI300/MI325 (#47201)
- **2026-07-07** [`2f71b2bd9f`](https://github.com/vllm-project/vllm/commit/2f71b2bd9f) [#47685](https://github.com/vllm-project/vllm/pull/47685) — [ROCm] Align mixed encoder-decoder KV cache views in V2 runner (#47685)
- **2026-07-06** [`5769a7382c`](https://github.com/vllm-project/vllm/commit/5769a7382c) [#47550](https://github.com/vllm-project/vllm/pull/47550) — [ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers) (#47550)
- **2026-07-06** [`8484ca5d45`](https://github.com/vllm-project/vllm/commit/8484ca5d45) [#47478](https://github.com/vllm-project/vllm/pull/47478) — [ROCm][CI] Adding Rust parity (#47478)
- **2026-07-06** [`482e5524fe`](https://github.com/vllm-project/vllm/commit/482e5524fe) [#47276](https://github.com/vllm-project/vllm/pull/47276) — [Bugfix][ROCm] Fix memory access fault in AITER MLA backend for DPA+FP8 KV  (#47276)
- **2026-07-06** [`5bce653e09`](https://github.com/vllm-project/vllm/commit/5bce653e09) [#47187](https://github.com/vllm-project/vllm/pull/47187) — Make the Transformers modeling backend as fast as native vLLM (#47187)
- **2026-07-06** [`07f9baf756`](https://github.com/vllm-project/vllm/commit/07f9baf756) [#47140](https://github.com/vllm-project/vllm/pull/47140) — Revert "[Platform] Replace `torch.cuda.Event` with `torch.Event` (#47140)" (#47668)
- **2026-07-06** [`f676808ba0`](https://github.com/vllm-project/vllm/commit/f676808ba0) [#47730](https://github.com/vllm-project/vllm/pull/47730) — [CI] Use TTY for AMD CI tests for colored buildkite logs (#47730)
- **2026-07-06** [`740f379fae`](https://github.com/vllm-project/vllm/commit/740f379fae) [#46065](https://github.com/vllm-project/vllm/pull/46065) — [ROCm][AITER] Directly Implement AITER Custom All-reduce in CudaCommunicator (#46065)
- **2026-07-06** [`fb265fc8fb`](https://github.com/vllm-project/vllm/commit/fb265fc8fb) [#47591](https://github.com/vllm-project/vllm/pull/47591) — [ROCm][CI] Increasing parallelism in Basic Models Tests (Extra Initialization) (#47591)
- **2026-07-06** [`8f0e75e16b`](https://github.com/vllm-project/vllm/commit/8f0e75e16b) [#47481](https://github.com/vllm-project/vllm/pull/47481) — [ROCm][CI] Adding nixl multiconn (#47481)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#48486](https://github.com/vllm-project/vllm/issues/48486) | [Bug]: Hang in CUDA Graph replay with PyTorch symmetric-memory all-red | bug | 2026-07-13 |
| [#48480](https://github.com/vllm-project/vllm/issues/48480) | [RFC]: Make Triton kernel unit tests hardware-agnostic and cover untes | — | 2026-07-13 |
| [#48478](https://github.com/vllm-project/vllm/issues/48478) | [RFC] Fail-Closed Graph Storage Contract for Weight Reload | rocm, RFC | 2026-07-13 |
| [#48312](https://github.com/vllm-project/vllm/issues/48312) | [RFC] Weight Reload Correctness for RL | rocm, RFC | 2026-07-13 |
| [#41663](https://github.com/vllm-project/vllm/issues/41663) | [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe  | bug, intel-gpu | 2026-07-13 |
| [#43559](https://github.com/vllm-project/vllm/issues/43559) | [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used toge | bug | 2026-07-13 |
| [#42363](https://github.com/vllm-project/vllm/issues/42363) | [Bug]: EngineDeadError with Kimi-K2.6 model using vLLM 0.20.2 | bug | 2026-07-13 |
| [#42659](https://github.com/vllm-project/vllm/issues/42659) | [RFC]: Per-Layer Parallelism Policy | feature request | 2026-07-13 |
| [#48453](https://github.com/vllm-project/vllm/issues/48453) | [Performance]: [ROCm][Perf] ~17-20% decode throughput regression from  | performance, rocm | 2026-07-13 |
| [#34303](https://github.com/vllm-project/vllm/issues/34303) | [RFC]: CUDA Checkpoint/Restore for Near-Zero Cold Starts | RFC | 2026-07-13 |
| [#47761](https://github.com/vllm-project/vllm/issues/47761) | [Bug]: vllm 0.23.0 and 0.24.0 - Qwen3.6-35B-A3B-FP8 - Fails generating | bug | 2026-07-13 |
| [#36315](https://github.com/vllm-project/vllm/issues/36315) | [Bug]: AttributeError: 'Qwen3_5TextConfig' object has no attribute 'ma | bug, stale | 2026-07-13 |
| [#39589](https://github.com/vllm-project/vllm/issues/39589) | [Bug]: KV Cache Read/Write Index Corruption Under Concurrent Prefill o | bug, stale | 2026-07-13 |
| [#39663](https://github.com/vllm-project/vllm/issues/39663) | [Bug]: Online FP8 quantization drops bias weights, which breaks Qwen2  | bug, stale | 2026-07-13 |
| [#39687](https://github.com/vllm-project/vllm/issues/39687) | [Bug]: vllm(g0e39202ca) vllm serve: error: argument --limit-mm-per-pro | bug, stale | 2026-07-13 |
| [#39722](https://github.com/vllm-project/vllm/issues/39722) | Gibberish with flashinfer_nvlink_two_sided on GB200/arm64 | stale | 2026-07-13 |
| [#37729](https://github.com/vllm-project/vllm/issues/37729) | [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix ca | bug | 2026-07-13 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-07-13 |
| [#48441](https://github.com/vllm-project/vllm/issues/48441) | [Bug]: Local PP Rank0 stalls in legacy non-SPMD Ray AsyncLLMEngine und | bug | 2026-07-12 |
| [#48229](https://github.com/vllm-project/vllm/issues/48229) | V1 multiprocess engine: sporadic 0.7-2s frozen engine step once per ge | — | 2026-07-12 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 44 |
| Other | 36 |
| Attention | 31 |
| MoE / Expert Parallel | 26 |
| Multimodal | 25 |
| Models | 19 |
| CI / Build | 15 |
| Scheduler / Engine | 13 |
| Serving / API | 13 |
| Quantization | 12 |
| Disaggregation / PD | 9 |
| Speculative Decoding | 8 |
| KV Cache / Offload | 7 |
| LoRA | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 3 |
| Perf / Benchmark | 2 |

## ROCm / AMD  (44 commits)

- **2026-07-13** [`bea70c7cfc`](https://github.com/vllm-project/vllm/commit/bea70c7cfc) [#48011](https://github.com/vllm-project/vllm/pull/48011)
  [Attention] Make sliding-window support an explicit backend capability (#48011)
  _Files: `vllm/model_executor/layers/attention/attention.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/cpu_attn.py`, `vllm/v1/attention/backends/flash_attn.py` _+6 more__
- **2026-07-13** [`b7b58d1eba`](https://github.com/vllm-project/vllm/commit/b7b58d1eba) [#46527](https://github.com/vllm-project/vllm/pull/46527)
  [ROCm][CI] Cache Rust builds by source inputs (#46527)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`, `docker/ci-rocm.hcl`_
- **2026-07-13** [`d973cce3ca`](https://github.com/vllm-project/vllm/commit/d973cce3ca) [#48440](https://github.com/vllm-project/vllm/pull/48440)
  Re-disable CUDA graph memory profiling on ROCm (#48440)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-07-13** [`775c1589ea`](https://github.com/vllm-project/vllm/commit/775c1589ea) [#48446](https://github.com/vllm-project/vllm/pull/48446)
  [Bugfix][ROCm] Keep TP all_gather on base-class collective (#48446)
  _Files: `vllm/distributed/device_communicators/cuda_communicator.py`_
- **2026-07-13** [`ee5a89f4d7`](https://github.com/vllm-project/vllm/commit/ee5a89f4d7) [#47287](https://github.com/vllm-project/vllm/pull/47287)
  [ROCm][MiniMax-M3] Add AITER sparse paged attention (#47287)
  _Files: `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/attention/test_minimax_m3.py` _+11 more__
- **2026-07-11** [`51878e5b6e`](https://github.com/vllm-project/vllm/commit/51878e5b6e) [#44455](https://github.com/vllm-project/vllm/pull/44455)
  [2/N][KV-Cache Layout Refactor] Pack K/V into the content dim across attention backends (#44455)
  _Files: `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `tests/compile/passes/test_fusion_attn.py`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_flashinfer_trtllm_attention.py` _+27 more__
- **2026-07-11** [`1bd8f80a64`](https://github.com/vllm-project/vllm/commit/1bd8f80a64) [#48328](https://github.com/vllm-project/vllm/pull/48328)
  [CI] Point CI at Transformers release rather than release branch (#48328)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+4 more__
- **2026-07-11** [`4a6440acef`](https://github.com/vllm-project/vllm/commit/4a6440acef) [#47867](https://github.com/vllm-project/vllm/pull/47867)
  Bump Transformers version to 5.13.0 (#47867)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+8 more__
- **2026-07-10** [`c227aaa3f8`](https://github.com/vllm-project/vllm/commit/c227aaa3f8) [#47419](https://github.com/vllm-project/vllm/pull/47419)
  [ROCm] Enable DeepSeek-V4 DSpark speculative decoding on AMD (MI350X / MI355X, gfx950) (#47419)
  _Files: `tests/models/test_registry.py`, `vllm/config/speculative.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/amd/dspark.py` _+2 more__
- **2026-07-10** [`e257faf87d`](https://github.com/vllm-project/vllm/commit/e257faf87d) [#48158](https://github.com/vllm-project/vllm/pull/48158)
  [Refactor] Remove unused rocm kernel `combine_topk_swa_indices_ragged` (#48158)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-07-10** [`88e5e2c57b`](https://github.com/vllm-project/vllm/commit/88e5e2c57b) [#47366](https://github.com/vllm-project/vllm/pull/47366)
  [CI/Build][AMD] Fix ROCm OOM in eagle_correctness_heavy by reserving CUDA graph memory (#47366)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-10** [`a0f6d767e4`](https://github.com/vllm-project/vllm/commit/a0f6d767e4) [#48169](https://github.com/vllm-project/vllm/pull/48169)
  [ROCm][CI] Move remaining engine/samplers AMD steps to mi325_1 (#48169)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/samplers.yaml`_
- **2026-07-09** [`766469a4c4`](https://github.com/vllm-project/vllm/commit/766469a4c4) [#48154](https://github.com/vllm-project/vllm/pull/48154)
  [ROCm] Revert Part of `[ROCm] Fix pooling startup workspace lock` #47912 (#48154)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-07-09** [`bbb0f945ff`](https://github.com/vllm-project/vllm/commit/bbb0f945ff) [#47404](https://github.com/vllm-project/vllm/pull/47404)
  [ROCm] Synchronize sparse MLA metadata before graph replay (#47404)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-07-09** [`b0dec2a11b`](https://github.com/vllm-project/vllm/commit/b0dec2a11b) [#45149](https://github.com/vllm-project/vllm/pull/45149)
  [ROCM][DSV32][Perf][MTP] Enable UNIFORM_BATCH CG mode in rocm_aiter_mla_sparse (#45149)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-07-09** [`67e7ea8977`](https://github.com/vllm-project/vllm/commit/67e7ea8977) [#48146](https://github.com/vllm-project/vllm/pull/48146)
  [ROCm][CI] Set all timeout_in_minutes to 180 (#48146)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-07-09** [`2c17d33f42`](https://github.com/vllm-project/vllm/commit/2c17d33f42) [#47144](https://github.com/vllm-project/vllm/pull/47144)
  [Bugfix][ROCm] Change AttentionCGSuppoort in TritonMLA to UNIFORM_SINGLE_TOKEN_DECODE (#47144)
  _Files: `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-07-08** [`bc44f9feb7`](https://github.com/vllm-project/vllm/commit/bc44f9feb7) [#47874](https://github.com/vllm-project/vllm/pull/47874)
  [ROCm][CI][MoE] Fix double-transpose of fused w3 expert weights (#47874)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-07-08** [`26831949b4`](https://github.com/vllm-project/vllm/commit/26831949b4) [#47912](https://github.com/vllm-project/vllm/pull/47912)
  [ROCm] Fix pooling startup workspace lock (#47912)
  _Files: `vllm/v1/attention/backends/rocm_attn.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_prefill_attention.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-08** [`49abadaedb`](https://github.com/vllm-project/vllm/commit/49abadaedb) [#47894](https://github.com/vllm-project/vllm/pull/47894)
  [ROCm][Bugfix] Fix empty-tensor .max() crash in AITER FA (#47894)
  _Files: `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-07-08** [`2cae98dfa5`](https://github.com/vllm-project/vllm/commit/2cae98dfa5) [#47844](https://github.com/vllm-project/vllm/pull/47844)
  [Rust Frontend] Handle `continue_final_message` with renderer sentinel (#47844)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-07-08** [`db39d60010`](https://github.com/vllm-project/vllm/commit/db39d60010) [#47943](https://github.com/vllm-project/vllm/pull/47943)
  Add tuned selective_state_update float32 config for AMD Instinct MI355 (#47943)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI355_OAM,cache_dtype=float32.json`_
- **2026-07-08** [`eeaf23107f`](https://github.com/vllm-project/vllm/commit/eeaf23107f) [#47947](https://github.com/vllm-project/vllm/pull/47947)
  [ROCm] Add tuned selective_state_update float32 config for AMD Instinct MI300X (#47947)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI300X,cache_dtype=float32.json`_
- **2026-07-08** [`1f4ad059d1`](https://github.com/vllm-project/vllm/commit/1f4ad059d1) [#47945](https://github.com/vllm-project/vllm/pull/47945)
  [ROCm] Add tuned selective_state_update float16 config for AMD Instinct MI300X (#47945)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI300X,cache_dtype=float16.json`_
- **2026-07-08** [`2c64b4c1cc`](https://github.com/vllm-project/vllm/commit/2c64b4c1cc) [#47158](https://github.com/vllm-project/vllm/pull/47158)
  [ROCm] fixed aiter master flag and expert parallelism compatibility on minimax-m3-mxfp8 (#47158)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`_
- **2026-07-08** [`d9e57ea82e`](https://github.com/vllm-project/vllm/commit/d9e57ea82e) [#46117](https://github.com/vllm-project/vllm/pull/46117)
  [ROCm][Perf] MXFP8 dense-linear + grouped-MoE GEMM optimizations for MiniMax-M3 (#46117)
  _Files: `tests/kernels/test_minimax_m3_amd_ops.py`, `vllm/model_executor/kernels/linear/mxfp8/rocm_native.py`, `vllm/model_executor/layers/fused_moe/experts/mxfp8_native_moe.py`_
- **2026-07-08** [`f7fc0ca993`](https://github.com/vllm-project/vllm/commit/f7fc0ca993) [#47454](https://github.com/vllm-project/vllm/pull/47454)
  [Frontend] Add endpoint plugins framework (#47454)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/plugins.yaml`, `docs/design/endpoint_plugins.md`, `docs/design/plugin_system.md` _+8 more__
- **2026-07-08** [`4aceabf8c1`](https://github.com/vllm-project/vllm/commit/4aceabf8c1) [#47766](https://github.com/vllm-project/vllm/pull/47766)
  [ROCm][Bugfix] Key sparse-MLA persistent metadata on per-request context lengths (#47766)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-07-08** [`6e35c5e5af`](https://github.com/vllm-project/vllm/commit/6e35c5e5af) [#47731](https://github.com/vllm-project/vllm/pull/47731)
  [ROCm][CI] Minimize comment in RocmAttention q_scale check (#47731)
  _Files: `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-07-07** [`c8c2f838e7`](https://github.com/vllm-project/vllm/commit/c8c2f838e7) [#47767](https://github.com/vllm-project/vllm/pull/47767)
  Add tuned selective_state_update config for AMD Instinct MI355 (#47767)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI355_OAM,cache_dtype=float16.json`_
- **2026-07-07** [`dd94484577`](https://github.com/vllm-project/vllm/commit/dd94484577) [#41359](https://github.com/vllm-project/vllm/pull/41359)
  Bump Transformers version to 5.10.4 (#41359)
  _Files: `benchmarks/backend_request_func.py`, `docs/features/reasoning_outputs.md`, `examples/features/prompt_embed/prompt_embed_offline.py`, `requirements/test/cpu.txt` _+47 more__
- **2026-07-07** [`ed051fab54`](https://github.com/vllm-project/vllm/commit/ed051fab54) [#45418](https://github.com/vllm-project/vllm/pull/45418)
  [Bugfix] Reject sampling params unsupported by diffusion models (#45418)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/test_sampling_params.py`, `tests/v1/sample/test_logprobs.py` _+1 more__
- **2026-07-07** [`cbb5f045be`](https://github.com/vllm-project/vllm/commit/cbb5f045be) [#46904](https://github.com/vllm-project/vllm/pull/46904)
  [ROCm][CI] Refresh ROCm base images when docker rocm_base changes (#46904)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/hardware_tests/amd.yaml`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh` _+10 more__
- **2026-07-07** [`e55cc59e52`](https://github.com/vllm-project/vllm/commit/e55cc59e52) [#47735](https://github.com/vllm-project/vllm/pull/47735)
  [Rust Frontend][CI] Unblock more end-to-end test cases (#47735)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/server/src/routes/inference/generate/types.rs` _+10 more__
- **2026-07-07** [`dd5c299fbe`](https://github.com/vllm-project/vllm/commit/dd5c299fbe) [#47201](https://github.com/vllm-project/vllm/pull/47201)
  [ROCm][Bugfix] Convert ModelOpt FP8 per-channel weights to e4m3fnuz on MI300/MI325 (#47201)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-07-07** [`2f71b2bd9f`](https://github.com/vllm-project/vllm/commit/2f71b2bd9f) [#47685](https://github.com/vllm-project/vllm/pull/47685)
  [ROCm] Align mixed encoder-decoder KV cache views in V2 runner (#47685)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-07-06** [`5769a7382c`](https://github.com/vllm-project/vllm/commit/5769a7382c) [#47550](https://github.com/vllm-project/vllm/pull/47550)
  [ROCm][CI][Bugfix] Fix flaky parallel tool-call streaming (test assertion + Mistral/Granite parsers) (#47550)
  _Files: `tests/entrypoints/openai/chat_completion/test_thinking_token_budget.py`, `tests/tool_parsers/test_granite_tool_parser.py`, `tests/tool_parsers/test_mistral_tool_parser.py`, `tests/tool_use/test_parallel_tool_calls.py` _+2 more__
- **2026-07-06** [`8484ca5d45`](https://github.com/vllm-project/vllm/commit/8484ca5d45) [#47478](https://github.com/vllm-project/vllm/pull/47478)
  [ROCm][CI] Adding Rust parity (#47478)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`, `.buildkite/test-amd.yaml`, `docker/Dockerfile.rocm`_
- **2026-07-06** [`482e5524fe`](https://github.com/vllm-project/vllm/commit/482e5524fe) [#47276](https://github.com/vllm-project/vllm/pull/47276)
  [Bugfix][ROCm] Fix memory access fault in AITER MLA backend for DPA+FP8 KV  (#47276)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-07-06** [`5bce653e09`](https://github.com/vllm-project/vllm/commit/5bce653e09) [#47187](https://github.com/vllm-project/vllm/pull/47187)
  Make the Transformers modeling backend as fast as native vLLM (#47187)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_distributed.yaml`, `.github/CODEOWNERS` _+19 more__
- **2026-07-06** [`f676808ba0`](https://github.com/vllm-project/vllm/commit/f676808ba0) [#47730](https://github.com/vllm-project/vllm/pull/47730)
  [CI] Use TTY for AMD CI tests for colored buildkite logs (#47730)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/scripts/run-multi-node-test.sh`_
- **2026-07-06** [`740f379fae`](https://github.com/vllm-project/vllm/commit/740f379fae) [#46065](https://github.com/vllm-project/vllm/pull/46065)
  [ROCm][AITER] Directly Implement AITER Custom All-reduce in CudaCommunicator (#46065)
  _Files: `.buildkite/test-amd.yaml`, `tests/compile/fusions_e2e/conftest.py`, `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `tests/distributed/test_rocm_aiter_custom_ar.py` _+8 more__
- **2026-07-06** [`fb265fc8fb`](https://github.com/vllm-project/vllm/commit/fb265fc8fb) [#47591](https://github.com/vllm-project/vllm/pull/47591)
  [ROCm][CI] Increasing parallelism in Basic Models Tests (Extra Initialization) (#47591)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-07-06** [`8f0e75e16b`](https://github.com/vllm-project/vllm/commit/8f0e75e16b) [#47481](https://github.com/vllm-project/vllm/pull/47481)
  [ROCm][CI] Adding nixl multiconn (#47481)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/kv_connector/nixl_integration/run_mamba_prefix_cache_test.sh`, `tests/v1/kv_connector/nixl_integration/run_multi_connector_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/run_multi_connector_edge_case_test.sh`_

## Other  (36 commits)

- **2026-07-12** [`5c0c987c03`](https://github.com/vllm-project/vllm/commit/5c0c987c03) [#47987](https://github.com/vllm-project/vllm/pull/47987)
  Make tiering offload region DP-replica aware (#47987)
  _Files: `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-07-11** [`54503ecec0`](https://github.com/vllm-project/vllm/commit/54503ecec0) [#43117](https://github.com/vllm-project/vllm/pull/43117)
  fix(processor): route MiMo-V2-Omni media fetch through MediaConnector (#43117)
  _Files: `vllm/transformers_utils/processors/mimo_v2_omni.py`_
- **2026-07-11** [`76fedaa2a5`](https://github.com/vllm-project/vllm/commit/76fedaa2a5) [#48232](https://github.com/vllm-project/vllm/pull/48232)
  [XPU][UT]Fix InternS1ProForConditionalGeneration AssertionError (#48232)
  _Files: `tests/models/utils.py`_
- **2026-07-10** [`ed908cf0a0`](https://github.com/vllm-project/vllm/commit/ed908cf0a0) [#45984](https://github.com/vllm-project/vllm/pull/45984)
  [Bugfix] Fix thinking_token_budget not enforced after natural </think> re-entry (#45984)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/v1/sample/thinking_budget_state.py`, `vllm/v1/worker/gpu_input_batch.py`_
- **2026-07-10** [`85c09e9885`](https://github.com/vllm-project/vllm/commit/85c09e9885) [#41811](https://github.com/vllm-project/vllm/pull/41811)
  fix: correct load_weights track logic and enable weight integrity for… (#41811)
  _Files: `tests/model_executor/model_loader/test_filter_duplicate_safetensors.py`, `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-07-10** [`c241c7a2b0`](https://github.com/vllm-project/vllm/commit/c241c7a2b0) [#47883](https://github.com/vllm-project/vllm/pull/47883)
  [Rust Frontend] Add roundtrip fixtures for more chat parsers (#47883)
  _Files: `rust/src/chat/tests/roundtrip.rs`_
- **2026-07-10** [`e5588e49bc`](https://github.com/vllm-project/vllm/commit/e5588e49bc) [#45261](https://github.com/vllm-project/vllm/pull/45261)
  [Core][KV events] Report prefix-cache-reused blocks in full report mode (#45261)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/block_pool.py`, `vllm/v1/core/kv_cache_manager.py`, `vllm/v1/core/kv_cache_utils.py` _+1 more__
- **2026-07-10** [`feb384ada2`](https://github.com/vllm-project/vllm/commit/feb384ada2) [#48112](https://github.com/vllm-project/vllm/pull/48112)
  [bugfix] bge-m3-sparse-plugin mismatch requests (#48112)
  _Files: `tests/plugins/bge_m3_sparse_plugin/bge_m3_sparse_processor/sparse_embeddings_processor.py`_
- **2026-07-09** [`ff8d3488f2`](https://github.com/vllm-project/vllm/commit/ff8d3488f2) [#48132](https://github.com/vllm-project/vllm/pull/48132)
  [Bugfix][MRV2] Reset num_accepted_tokens on add_request in all modes (#48132)
  _Files: `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-07-09** [`1cd75b3dd4`](https://github.com/vllm-project/vllm/commit/1cd75b3dd4) [#48085](https://github.com/vllm-project/vllm/pull/48085)
  [Bugfix] Fix race condition in KVBlockZeroer (#48085)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/utils.py`_
- **2026-07-08** [`5f85975624`](https://github.com/vllm-project/vllm/commit/5f85975624) [#46718](https://github.com/vllm-project/vllm/pull/46718)
  [Feat] Add runtime monitor for post-warmup TileLang compilation (#46718)
  _Files: `tests/test_jit_monitor.py`, `vllm/utils/jit_monitor.py`_
- **2026-07-08** [`a5d19cbb95`](https://github.com/vllm-project/vllm/commit/a5d19cbb95) [#48014](https://github.com/vllm-project/vllm/pull/48014)
  [Core] Move MRV1 `late_interaction_runner.py` out of MRV2 subtree (#48014)
  _Files: `tests/v1/worker/test_late_interaction_runner.py`, `vllm/v1/pool/late_interaction_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-08** [`68b4a1d582`](https://github.com/vllm-project/vllm/commit/68b4a1d582) [#47892](https://github.com/vllm-project/vllm/pull/47892)
  Fix NVML capability lookup for visible devices (#47892)
  _Files: `tests/cuda/test_cuda_context.py`, `vllm/platforms/cuda.py`, `vllm/platforms/interface.py`_
- **2026-07-08** [`d79855eaac`](https://github.com/vllm-project/vllm/commit/d79855eaac) [#47044](https://github.com/vllm-project/vllm/pull/47044)
  [Docs] `kv_sharing_fast_prefill` correction (#47044)
  _Files: `vllm/config/cache.py`_
- **2026-07-08** [`0ca6eee743`](https://github.com/vllm-project/vllm/commit/0ca6eee743) [#47744](https://github.com/vllm-project/vllm/pull/47744)
  [Core] Pass request context to CPU offload cache policy touch (#47744)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/policies/arc.py`, `vllm/v1/kv_offload/cpu/policies/base.py` _+1 more__
- **2026-07-08** [`f7efab58ec`](https://github.com/vllm-project/vllm/commit/f7efab58ec) [#47848](https://github.com/vllm-project/vllm/pull/47848)
  [CPU][Bugfix] Fix flaky ShortConv prefill test on ARM (uninitialized weights) (#47848)
  _Files: `tests/kernels/mamba/test_cpu_short_conv.py`_
- **2026-07-08** [`e97c3cb303`](https://github.com/vllm-project/vllm/commit/e97c3cb303) [#47388](https://github.com/vllm-project/vllm/pull/47388)
  [Core] Persist and reuse the memory-profiling result across boots (opt-in) (#47388)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/envs.py`, `vllm/v1/worker/gpu_worker.py`, `vllm/v1/worker/startup_plan.py`_
- **2026-07-07** [`aad0fb741b`](https://github.com/vllm-project/vllm/commit/aad0fb741b) [#47897](https://github.com/vllm-project/vllm/pull/47897)
  [CI/Build] Accept ready-run-all-tests label in pre-commit gate (#47897)
  _Files: `.github/workflows/pre-commit.yml`_
- **2026-07-07** [`55da232db6`](https://github.com/vllm-project/vllm/commit/55da232db6) [#45207](https://github.com/vllm-project/vllm/pull/45207)
  [Bugfix] Pad Mamba page size instead of scaling block_size in unify_kv_cache_spec_page_size (#45207)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-07** [`3f99883d97`](https://github.com/vllm-project/vllm/commit/3f99883d97) [#47902](https://github.com/vllm-project/vllm/pull/47902)
  [CI Bug Fix] Temp fix for v3.2 accuracy (#47902)
  _Files: `vllm/config/parallel.py`_
- **2026-07-07** [`d6875196ad`](https://github.com/vllm-project/vllm/commit/d6875196ad) [#47356](https://github.com/vllm-project/vllm/pull/47356)
  [Bugfix] Exclude kv_cache_memory_bytes from CacheConfig.compute_hash (#47356)
  _Files: `tests/config/test_config_utils.py`, `vllm/config/cache.py`_
- **2026-07-07** [`bdc6f3bfa1`](https://github.com/vllm-project/vllm/commit/bdc6f3bfa1) [#47755](https://github.com/vllm-project/vllm/pull/47755)
  [Bug] Fix tmp directory for `lm_eval` (#47755)
  _Files: `tests/evals/gsm8k/gsm8k_eval.py`_
- **2026-07-07** [`21b396abe1`](https://github.com/vllm-project/vllm/commit/21b396abe1) [#47784](https://github.com/vllm-project/vllm/pull/47784)
  AGENTS MD: Add suggestion on how to incorporate tests (#47784)
  _Files: `AGENTS.md`_
- **2026-07-07** [`bdaf27519f`](https://github.com/vllm-project/vllm/commit/bdaf27519f) [#47868](https://github.com/vllm-project/vllm/pull/47868)
  [XPU] Fix Event init failure w/ blocking (#47868)
  _Files: `vllm/v1/worker/xpu_model_runner.py`_
- **2026-07-07** [`beb4327c46`](https://github.com/vllm-project/vllm/commit/beb4327c46) [#47745](https://github.com/vllm-project/vllm/pull/47745)
  Enable causal masking for SWA in vllm-project/speculators models (#47745)
  _Files: `vllm/transformers_utils/configs/speculators/algos.py`_
- **2026-07-07** [`65a7b46284`](https://github.com/vllm-project/vllm/commit/65a7b46284) [#47063](https://github.com/vllm-project/vllm/pull/47063)
  [KV-Offloading] Support workload identity for objectstore secondary tier (#47063)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/config.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-07-07** [`920469974a`](https://github.com/vllm-project/vllm/commit/920469974a) [#38641](https://github.com/vllm-project/vllm/pull/38641)
  [UX] Log worker exit code when process dies unexpectedly (#38641)
  _Files: `vllm/v1/executor/multiproc_executor.py`_
- **2026-07-07** [`8b91cd5b20`](https://github.com/vllm-project/vllm/commit/8b91cd5b20) [#44726](https://github.com/vllm-project/vllm/pull/44726)
  [Bugfix][Core] Close underlying iterator in merge_async_iterators single-iterator fast path (#44726)
  _Files: `tests/utils_/test_async_utils.py`, `vllm/utils/async_utils.py`_
- **2026-07-07** [`c85d72076a`](https://github.com/vllm-project/vllm/commit/c85d72076a) [#47321](https://github.com/vllm-project/vllm/pull/47321)
  [HARDWARE][POWER]  optimize math functions of VSX power (#47321)
  _Files: `csrc/cpu/cpu_attn_vsx.hpp`, `csrc/cpu/cpu_types.hpp`, `csrc/cpu/cpu_types_vsx.hpp`, `csrc/cpu/utils.hpp` _+1 more__
- **2026-07-07** [`ba50b9763f`](https://github.com/vllm-project/vllm/commit/ba50b9763f) [#47586](https://github.com/vllm-project/vllm/pull/47586)
  [Bugfix] Match the mapped filename in find_loaded_library (#47586)
  _Files: `vllm/utils/system_utils.py`_
- **2026-07-07** [`69f3150981`](https://github.com/vllm-project/vllm/commit/69f3150981) [#47253](https://github.com/vllm-project/vllm/pull/47253)
  [XPU] Fix PP accuracy on XPU device (#47253)
  _Files: `vllm/v1/worker/gpu/pp_utils.py`_
- **2026-07-06** [`567a78432d`](https://github.com/vllm-project/vllm/commit/567a78432d) [#40589](https://github.com/vllm-project/vllm/pull/40589)
  [Bugfix] Fix dp mtp hang (#40589)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
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

## Attention  (31 commits)

- **2026-07-13** [`56a357ed33`](https://github.com/vllm-project/vllm/commit/56a357ed33) [#48256](https://github.com/vllm-project/vllm/pull/48256)
  [Bugfix][KV Cache] Don't route uniform-page-size MLA+SWA models into DeepseekV4 packing (#48256)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-13** [`75fe92a316`](https://github.com/vllm-project/vllm/commit/75fe92a316) [#48064](https://github.com/vllm-project/vllm/pull/48064)
  [Distributed][Perf] Enable FlashInfer MNNVL allreduce RMS quant fusion (#48064)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-07-13** [`05fa8183a6`](https://github.com/vllm-project/vllm/commit/05fa8183a6) [#46090](https://github.com/vllm-project/vllm/pull/46090)
  [CPU][Spec Decode] Support DFlash speculative decoding for GDN models on CPU (#46090)
  _Files: `csrc/cpu/sgl-kernels/fla.cpp`, `csrc/cpu/torch_bindings.cpp`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py` _+1 more__
- **2026-07-12** [`370b678a02`](https://github.com/vllm-project/vllm/commit/370b678a02) [#48394](https://github.com/vllm-project/vllm/pull/48394)
  [CI][2/N] reduce CI time (#48394)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/kernels.yaml`_
- **2026-07-11** [`bec0a4ede6`](https://github.com/vllm-project/vllm/commit/bec0a4ede6) [#48269](https://github.com/vllm-project/vllm/pull/48269)
  [Revert] [Build] Update vllm ...builds FA3 with torch stable API (#48269)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-07-11** [`9c18e90f6c`](https://github.com/vllm-project/vllm/commit/9c18e90f6c) [#47314](https://github.com/vllm-project/vllm/pull/47314)
  [BugFix] Fix packed HND KV cache reshape for FlashAttention (#47314)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-07-11** [`29fd688892`](https://github.com/vllm-project/vllm/commit/29fd688892) [#48268](https://github.com/vllm-project/vllm/pull/48268)
  Add VLLM_FLASHINFER_AUTOTUNE_SKIP_OPS and skip CuTeDSL fp4_gemm autotuning by default (#48268)
  _Files: `vllm/envs.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-07-10** [`735def4fcf`](https://github.com/vllm-project/vllm/commit/735def4fcf) [#48045](https://github.com/vllm-project/vllm/pull/48045)
  [Bugfix] Fix FlashMLA dense fp8 metadata crash (num_sm_parts clamp) (#48045)
  _Files: `cmake/external_projects/flashmla.cmake`_
- **2026-07-10** [`08dfd68610`](https://github.com/vllm-project/vllm/commit/08dfd68610) [#47857](https://github.com/vllm-project/vllm/pull/47857)
  [Model] Add LongCat-Flash-Lite (n-gram embedding) (#47857)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/ngram_embedding_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+12 more__
- **2026-07-10** [`b12cca6a23`](https://github.com/vllm-project/vllm/commit/b12cca6a23) [#39988](https://github.com/vllm-project/vllm/pull/39988)
  [Bugfix] Fix turboquant FP8 cast failure for BF16 models on Ampere GPUs (#39988)
  _Files: `vllm/v1/attention/ops/triton_turboquant_store.py`_
- **2026-07-10** [`7614b88ebd`](https://github.com/vllm-project/vllm/commit/7614b88ebd) [#48113](https://github.com/vllm-project/vllm/pull/48113)
  [Bugfix][Spec Decode] Fix DFlash draft/target layer-count mismatch (#48113)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-07-10** [`433f291195`](https://github.com/vllm-project/vllm/commit/433f291195) [#48186](https://github.com/vllm-project/vllm/pull/48186)
  [CI] Right-size test-area timeouts from nightly durations (#48186)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/compile.yaml` _+26 more__
- **2026-07-10** [`95ed0feaa5`](https://github.com/vllm-project/vllm/commit/95ed0feaa5) [#40996](https://github.com/vllm-project/vllm/pull/40996)
  DCP supports hybrid attention (#40996)
  _Files: `tests/distributed/test_context_parallel.py`, `tests/distributed/test_pynccl.py`, `tests/models/language/generation/test_hybrid.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py` _+22 more__
- **2026-07-09** [`e08a915146`](https://github.com/vllm-project/vllm/commit/e08a915146) [#48135](https://github.com/vllm-project/vllm/pull/48135)
  [Bugfix] Preserve tensor causal metadata for grouped attention (#48135)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-07-08** [`95d6d6f4bb`](https://github.com/vllm-project/vllm/commit/95d6d6f4bb) [#48046](https://github.com/vllm-project/vllm/pull/48046)
  [Bugfix] Use int8 workspace for FlashInfer MLA decode (#48046)
  _Files: `tests/kernels/attention/test_flashinfer_mla_decode.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`_
- **2026-07-08** [`8347c6e6e1`](https://github.com/vllm-project/vllm/commit/8347c6e6e1) [#47995](https://github.com/vllm-project/vllm/pull/47995)
  updated flash_attn GIT_TAG to point to torch Stable ABI FA3 commit (#47995)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-07-08** [`f05603fa28`](https://github.com/vllm-project/vllm/commit/f05603fa28) [#47801](https://github.com/vllm-project/vllm/pull/47801)
  [Bugfix][DCP] Cast LSE to fp32 in a2a combine to fix bf16 bitcast crash (#47801)
  _Files: `vllm/v1/attention/ops/dcp_alltoall.py`_
- **2026-07-08** [`c2ecd0f888`](https://github.com/vllm-project/vllm/commit/c2ecd0f888) [#42642](https://github.com/vllm-project/vllm/pull/42642)
  Fix FlashAttention MLA prefill V unpadding (#42642)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/mla/prefill/flash_attn.py`, `vllm/v1/attention/ops/merge_attn_states.py`_
- **2026-07-08** [`0d12618e98`](https://github.com/vllm-project/vllm/commit/0d12618e98) [#47914](https://github.com/vllm-project/vllm/pull/47914)
  [Spec Decode] Support hybrid (SWA + full attention) DFlash drafters (#47914)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/models/qwen3_dflash.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/spec_decode/dflash/cudagraph.py` _+5 more__
- **2026-07-08** [`440002552e`](https://github.com/vllm-project/vllm/commit/440002552e) [#47962](https://github.com/vllm-project/vllm/pull/47962)
  [XPU] [Fusion passes] Disable fuse_rope_kvcache_cat_mla & qk_norm_rope_ fusion on XPU (#47962)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-08** [`80eb01e93d`](https://github.com/vllm-project/vllm/commit/80eb01e93d) [#47493](https://github.com/vllm-project/vllm/pull/47493)
  [Bugfix] DSV4 TP16 garbage output (#47493)
  _Files: `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py` _+1 more__
- **2026-07-07** [`3dd910da42`](https://github.com/vllm-project/vllm/commit/3dd910da42) [#47908](https://github.com/vllm-project/vllm/pull/47908)
  [Bugfix] Allow non-contiguous query in FlashInfer FP8 query quantization (#47908)
  _Files: `vllm/v1/attention/backends/flashinfer.py`_
- **2026-07-07** [`7bd154375d`](https://github.com/vllm-project/vllm/commit/7bd154375d) [#47698](https://github.com/vllm-project/vllm/pull/47698)
  [Bugfix] Fix mamba+dflash for MRV2 (#47698)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-07-06** [`04adc8843b`](https://github.com/vllm-project/vllm/commit/04adc8843b) [#47716](https://github.com/vllm-project/vllm/pull/47716)
  [Bugfix]Fix DeepSeek-V4 fp8_ds_mla KV cache reshape (#47716)
  _Files: `vllm/models/deepseek_v4/attention.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-06** [`f70caef48b`](https://github.com/vllm-project/vllm/commit/f70caef48b) [#47474](https://github.com/vllm-project/vllm/pull/47474)
  [Perf] Cache `token_to_req_indices` for dsv4, 5x~6x kernel performance improvement (#47474)
  _Files: `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/sparse_mla.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/mla/sparse_swa.py`_
- **2026-07-06** [`b1c6dba558`](https://github.com/vllm-project/vllm/commit/b1c6dba558) [#47329](https://github.com/vllm-project/vllm/pull/47329)
  [Refactor] Remove multiple dead code (#47329)
  _Files: `CMakeLists.txt`, `vllm/kernels/helion/config_manager.py`, `vllm/model_executor/layers/fla/ops/layernorm_guard.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py` _+3 more__
- **2026-07-06** [`095adf1fdc`](https://github.com/vllm-project/vllm/commit/095adf1fdc) [#47671](https://github.com/vllm-project/vllm/pull/47671)
  [Bugfix] Fix int32 overflow in triton_decode_attention page offsets (#47671)
  _Files: `vllm/v1/attention/ops/triton_decode_attention.py`_
- **2026-07-06** [`8b79971bb9`](https://github.com/vllm-project/vllm/commit/8b79971bb9) [#43597](https://github.com/vllm-project/vllm/pull/43597)
  attention: pass None for unused args in unified attention TD path (#43597)
  _Files: `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-07-06** [`736f1a5907`](https://github.com/vllm-project/vllm/commit/736f1a5907) [#47688](https://github.com/vllm-project/vllm/pull/47688)
  [XPU] Route mm_prefix models to Triton attention backend (#47688)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-06** [`16f8110935`](https://github.com/vllm-project/vllm/commit/16f8110935) [#47532](https://github.com/vllm-project/vllm/pull/47532)
  [Bugfix][CPU][RISC-V] Fix VLEN detection for RVV attention path (#47532)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_attn.cpp`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-07-06** [`95a248faed`](https://github.com/vllm-project/vllm/commit/95a248faed) [#47433](https://github.com/vllm-project/vllm/pull/47433)
  [Attention Backend] HPC_ATTN backend support mtp and dynamic scheduled attention (#47433)
  _Files: `docs/design/attention_backends.md`, `vllm/model_executor/layers/hpc/rope_norm.py`, `vllm/v1/attention/backends/hpc_attn.py`_

## MoE / Expert Parallel  (26 commits)

- **2026-07-13** [`36484e464a`](https://github.com/vllm-project/vllm/commit/36484e464a) [#48429](https://github.com/vllm-project/vllm/pull/48429)
  [BugFix] Restore full tokens for Qwen MTP When MoE SP (#48429)
  _Files: `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`_
- **2026-07-13** [`2595d5cebc`](https://github.com/vllm-project/vllm/commit/2595d5cebc) [#48350](https://github.com/vllm-project/vllm/pull/48350)
  [Model] Optimize Qwen3.5 on H20 (#48350)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=256,device_name=NVIDIA_H20.json`_
- **2026-07-12** [`a02984ed47`](https://github.com/vllm-project/vllm/commit/a02984ed47) [#47006](https://github.com/vllm-project/vllm/pull/47006)
  [Perf][Qwen] Replace MOE all-reduce with reduce-scatter (#47006)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-07-11** [`19069bcbd5`](https://github.com/vllm-project/vllm/commit/19069bcbd5) [#48335](https://github.com/vllm-project/vllm/pull/48335)
  FP32 router GEMV optimization (#48335)
  _Files: `csrc/libtorch_stable/fp32_router_gemm.cu`, `csrc/libtorch_stable/fp32_router_gemm_entry.cu`, `tests/kernels/test_fp32_router_gemm.py`, `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-07-11** [`0b6636cbcb`](https://github.com/vllm-project/vllm/commit/0b6636cbcb) [#48079](https://github.com/vllm-project/vllm/pull/48079)
  [XPU]remove is_xxx from moe class and bump up kernels (#48079)
  _Files: `requirements/xpu.txt`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`_
- **2026-07-11** [`092387963c`](https://github.com/vllm-project/vllm/commit/092387963c) [#46276](https://github.com/vllm-project/vllm/pull/46276)
  [BugFix] weights processing peak memory reduction for nvfp4 MoE layers (#46276)
  _Files: `tests/kernels/moe/test_flashinfer_b12x_moe.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_
- **2026-07-11** [`1bf3997eae`](https://github.com/vllm-project/vllm/commit/1bf3997eae) [#47851](https://github.com/vllm-project/vllm/pull/47851)
  [Quantization] Bound peak memory when repacking FP4 MoE weights for Marlin (#47851)
  _Files: `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`_
- **2026-07-10** [`f378f79b7c`](https://github.com/vllm-project/vllm/commit/f378f79b7c) [#47785](https://github.com/vllm-project/vllm/pull/47785)
  handle topk_ids padding in align sum kernel (#47785)
  _Files: `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `tests/kernels/moe/test_moe_align_block_size.py`_
- **2026-07-09** [`f1a5adddb8`](https://github.com/vllm-project/vllm/commit/f1a5adddb8) [#48144](https://github.com/vllm-project/vllm/pull/48144)
  update marlin M size for EP (#48144)
  _Files: `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`_
- **2026-07-08** [`6cf7b26bd4`](https://github.com/vllm-project/vllm/commit/6cf7b26bd4) [#48008](https://github.com/vllm-project/vllm/pull/48008)
  [docs] Fix the docs build (#48008)
  _Files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/v1/kv_offload/tiering/p2p/manager.py`_
- **2026-07-08** [`0d2f4e7c9c`](https://github.com/vllm-project/vllm/commit/0d2f4e7c9c) [#46661](https://github.com/vllm-project/vllm/pull/46661)
  Allow FlashInfer A2A backends for TRTLLM FP8 MoE Modular (#46661)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`_
- **2026-07-08** [`089e412878`](https://github.com/vllm-project/vllm/commit/089e412878) [#45182](https://github.com/vllm-project/vllm/pull/45182)
  [Perf] Integrate TRTLLM BF16 MoE Modular Kernel  (#45182)
  _Files: `tests/kernels/moe/test_trtllm_bf16_moe.py`, `tests/kernels/moe/test_unquantized_backend_selection.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/base.py` _+1 more__
- **2026-07-08** [`572b25b03e`](https://github.com/vllm-project/vllm/commit/572b25b03e) [#47884](https://github.com/vllm-project/vllm/pull/47884)
  [Bug] Fix Batched DeepGEMM (#47884)
  _Files: `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`_
- **2026-07-08** [`934eeaecfb`](https://github.com/vllm-project/vllm/commit/934eeaecfb) [#47781](https://github.com/vllm-project/vllm/pull/47781)
  [CI/Build][BugFix][The Rock] Fix get_ssm_device_name to return sanitized, usable filename (#47781)
  _Files: `benchmarks/kernels/benchmark_flydsl_moe_w4a16.py`, `benchmarks/kernels/benchmark_w8a8_block_fp8.py`, `vllm/model_executor/layers/fused_moe/fused_flydsl_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py` _+4 more__
- **2026-07-08** [`99a85617bf`](https://github.com/vllm-project/vllm/commit/99a85617bf) [#47946](https://github.com/vllm-project/vllm/pull/47946)
  [Test] Skip DeepEP MoE layer tests without P2P access (#47946)
  _Files: `tests/kernels/moe/test_moe_layer.py`_
- **2026-07-08** [`2afa3f7e95`](https://github.com/vllm-project/vllm/commit/2afa3f7e95) [#47631](https://github.com/vllm-project/vllm/pull/47631)
  [Perf] Minimax M3 - Support cross-layer allreduce-norm fusion (#47631)
  _Files: `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/models/deepseek_v32/nvidia/model.py` _+3 more__
- **2026-07-08** [`9021589498`](https://github.com/vllm-project/vllm/commit/9021589498) [#47502](https://github.com/vllm-project/vllm/pull/47502)
  [Minimax-M3] Using tok_sparse_select from MSA instead of triton kernels (#47502)
  _Files: `cmake/external_projects/fmha_sm100.cmake`, `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/indexer.py`, `vllm/models/minimax_m3/common/ops/__init__.py` _+5 more__
- **2026-07-07** [`b93cbd7416`](https://github.com/vllm-project/vllm/commit/b93cbd7416) [#47858](https://github.com/vllm-project/vllm/pull/47858)
  [XPU] Fix topk_sigmoid arg mismatch on XPU (#47858)
  _Files: `vllm/_custom_ops.py`_
- **2026-07-07** [`066f02ae94`](https://github.com/vllm-project/vllm/commit/066f02ae94) [#47427](https://github.com/vllm-project/vllm/pull/47427)
  [MoE] FI autotuning: max bucket = max token count [e.g. `DP_size*MNBT`] (#47427)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-07-07** [`5d23ca47ab`](https://github.com/vllm-project/vllm/commit/5d23ca47ab) [#47408](https://github.com/vllm-project/vllm/pull/47408)
  [Kernel]  Applies routed_scaling_factor internally (#47408)
  _Files: `csrc/libtorch_stable/moe/moe_ops.h`, `csrc/libtorch_stable/moe/topk_softmax_kernels.cu`, `csrc/libtorch_stable/moe/torch_bindings.cpp`, `vllm/_custom_ops.py` _+4 more__
- **2026-07-06** [`d891b9bd51`](https://github.com/vllm-project/vllm/commit/d891b9bd51) [#41652](https://github.com/vllm-project/vllm/pull/41652)
  [Quantization] add humming moe backend to all dense/moe oracles (#41652)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `requirements/cuda.txt`, `tests/evals/gsm8k/configs/humming/Qwen2-1.5B-Instruct-FP8W8-humming-act-fp8.yaml`, `tests/evals/gsm8k/configs/humming/Qwen2-1.5B-Instruct-FP8W8-humming.yaml` _+69 more__
- **2026-07-06** [`b1384f5ec6`](https://github.com/vllm-project/vllm/commit/b1384f5ec6) [#43328](https://github.com/vllm-project/vllm/pull/43328)
  Enable B12x backend for non-gated MoEs (like Nemotron)  (#43328)
  _Files: `tests/kernels/moe/test_flashinfer_b12x_moe.py`, `tests/kernels/moe/utils.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_b12x_moe.py`_
- **2026-07-06** [`07f9baf756`](https://github.com/vllm-project/vllm/commit/07f9baf756) [#47140](https://github.com/vllm-project/vllm/pull/47140)
  Revert "[Platform] Replace `torch.cuda.Event` with `torch.Event` (#47140)" (#47668)
  _Files: `benchmarks/benchmark_topk_topp.py`, `benchmarks/kernels/benchmark_moe_defaults.py`, `benchmarks/kernels/benchmark_selective_state_update.py`, `tests/v1/kv_connector/unit/test_hf3fs_connector.py` _+27 more__
- **2026-07-06** [`98ba9b9583`](https://github.com/vllm-project/vllm/commit/98ba9b9583) [#47024](https://github.com/vllm-project/vllm/pull/47024)
  [Frontend] Support OpenAI Responses API namespace tools (#47024)
  _Files: `tests/entrypoints/openai/responses/test_namespace_tool_separator.py`, `tests/tool_parsers/test_glm47_moe_tool_parser.py`, `vllm/entrypoints/openai/responses/context.py`, `vllm/entrypoints/openai/responses/protocol.py` _+4 more__
- **2026-07-06** [`f1073c050c`](https://github.com/vllm-project/vllm/commit/f1073c050c) [#46739](https://github.com/vllm-project/vllm/pull/46739)
  [CPU][BugFix] Multiple fixes to w4a8_int8 CPU MoE path (#46739)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `csrc/cpu/torch_bindings.cpp`, `csrc/moe/dynamic_4bit_int_moe_cpu.cpp`, `csrc/ops.h` _+6 more__
- **2026-07-06** [`f2aaf59151`](https://github.com/vllm-project/vllm/commit/f2aaf59151) [#44880](https://github.com/vllm-project/vllm/pull/44880)
  [Feature] Support MTP speculative decoding for Bailing hybrid models (#44880)
  _Files: `tests/config/test_bailing_mtp_config.py`, `tests/models/registry.py`, `tests/v1/attention/test_linear_attention_metadata_builder.py`, `vllm/config/speculative.py` _+7 more__

## Multimodal  (25 commits)

- **2026-07-12** [`8e981630c9`](https://github.com/vllm-project/vllm/commit/8e981630c9) [#48072](https://github.com/vllm-project/vllm/pull/48072)
  [CI][CPU] Add Qwen2-VL multimodal tests for CPU backend and fix incompatibilities (#48072)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/models/multimodal/generation/test_qwen2_5_vl.py`_
- **2026-07-11** [`1ef1c7ebba`](https://github.com/vllm-project/vllm/commit/1ef1c7ebba) [#48219](https://github.com/vllm-project/vllm/pull/48219)
  [CI] split tests to reduce CI time (#48219)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `.buildkite/test_areas/models_multimodal.yaml`_
- **2026-07-10** [`978a6dfa3f`](https://github.com/vllm-project/vllm/commit/978a6dfa3f) [#48041](https://github.com/vllm-project/vllm/pull/48041)
  [Build/CI] Build arm64 PR and postmerge image builds for Blackwell SM10x and SM110 (#48041)
  _Files: `.buildkite/image_build/image_build_arm64.sh`_
- **2026-07-10** [`68ea76e780`](https://github.com/vllm-project/vllm/commit/68ea76e780) [#48220](https://github.com/vllm-project/vllm/pull/48220)
  [Misc] Remove dead code in ViT functionality test (#48220)
  _Files: `tests/models/multimodal/generation/test_vit_backend_functionality.py`_
- **2026-07-10** [`e23b19309b`](https://github.com/vllm-project/vllm/commit/e23b19309b) [#42424](https://github.com/vllm-project/vllm/pull/42424)
  Deepstream video backend (#42424)
  _Files: `docs/features/multimodal_inputs.md`, `setup.py`, `vllm/multimodal/video.py`_
- **2026-07-10** [`f36284a8d2`](https://github.com/vllm-project/vllm/commit/f36284a8d2) [#47180](https://github.com/vllm-project/vllm/pull/47180)
  [CI] Add TORCH_NIGHTLY=1 build mode (run full suite on torch nightly) (#47180)
  _Files: `.buildkite/image_build/image_build.sh`, `.buildkite/scripts/check-ray-compatibility.sh`, `.buildkite/scripts/trigger-ci-build.sh`, `CMakeLists.txt` _+1 more__
- **2026-07-10** [`424df4f65d`](https://github.com/vllm-project/vllm/commit/424df4f65d) [#48211](https://github.com/vllm-project/vllm/pull/48211)
  [Model][CI/Build] Cosmos3: enable registry tests and register Cosmos3-Super (#48211)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/generation/test_common.py`, `tests/models/registry.py`_
- **2026-07-10** [`074bdd0d99`](https://github.com/vllm-project/vllm/commit/074bdd0d99) [#47959](https://github.com/vllm-project/vllm/pull/47959)
  [Rust Frontend] Integrate MM video support (#47959)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/backend/hf.rs` _+12 more__
- **2026-07-10** [`216ee58780`](https://github.com/vllm-project/vllm/commit/216ee58780) [#48126](https://github.com/vllm-project/vllm/pull/48126)
  Add XPU nightly and release image publishing to DockerHub (#48126)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/publish-release-images.sh`, `.buildkite/scripts/xpu/push-nightly-builds-xpu.sh`_
- **2026-07-09** [`753c5039f0`](https://github.com/vllm-project/vllm/commit/753c5039f0) [#48056](https://github.com/vllm-project/vllm/pull/48056)
  Pin PyNvVideoCodec to tested 2.0.4 wheel (#48056)
  _Files: `requirements/cuda.txt`_
- **2026-07-09** [`299d2b5655`](https://github.com/vllm-project/vllm/commit/299d2b5655) [#48101](https://github.com/vllm-project/vllm/pull/48101)
  [CI] Annotate built Docker image tags on the Buildkite build page (#48101)
  _Files: `.buildkite/image_build/image_build.sh`, `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/image_build/image_build_cpu.sh`, `.buildkite/image_build/image_build_cpu_arm64.sh` _+4 more__
- **2026-07-09** [`412414d8e0`](https://github.com/vllm-project/vllm/commit/412414d8e0) [#48096](https://github.com/vllm-project/vllm/pull/48096)
  Remove PersimmonForCausalLM and FuyuForCausalLM model architectures (#48096)
  _Files: `docs/configuration/conserving_memory.md`, `docs/contributing/model/multimodal.md`, `docs/models/supported_models.md`, `examples/generate/multimodal/vision_language_offline.py` _+10 more__
- **2026-07-08** [`d1f1d86797`](https://github.com/vllm-project/vllm/commit/d1f1d86797) [#47033](https://github.com/vllm-project/vllm/pull/47033)
  [Bugfix] Re-enable benchmarking of librispeech dataset. (#47033)
  _Files: `tests/benchmarks/test_audio_dataset.py`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-07-08** [`9f2b3b093c`](https://github.com/vllm-project/vllm/commit/9f2b3b093c) [#46017](https://github.com/vllm-project/vllm/pull/46017)
  Improvement of Docker image build for IBM Power using prebuilt wheels from IBM published devpi index (#46017)
  _Files: `build_vllm_ppc64le.sh`, `docker/Dockerfile.ppc64le`_
- **2026-07-08** [`cd0de48d08`](https://github.com/vllm-project/vllm/commit/cd0de48d08) [#47728](https://github.com/vllm-project/vllm/pull/47728)
  [Bugfix][V1] Free out-of-window blocks on the processed-token basis under async scheduling (#47728)
  _Files: `tests/models/multimodal/generation/test_voxtral_realtime.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `tests/v1/core/test_swa_inflight_window_free.py` _+10 more__
- **2026-07-08** [`51e5372f3d`](https://github.com/vllm-project/vllm/commit/51e5372f3d) [#47872](https://github.com/vllm-project/vllm/pull/47872)
  [Model][HunyuanVL] Use native transformers processor and adapt to transformers 5.13 (#47872)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/hunyuan_vision.py`, `vllm/transformers_utils/processors/hunyuan_vl.py`, `vllm/transformers_utils/processors/hunyuan_vl_image.py`_
- **2026-07-08** [`c0e8e1f12a`](https://github.com/vllm-project/vllm/commit/c0e8e1f12a) [#45313](https://github.com/vllm-project/vllm/pull/45313)
  [Bugfix] Register VLLM_BUILD_* and VLLM_IMAGE_TAG provenance env vars (#45313)
  _Files: `vllm/envs.py`_
- **2026-07-08** [`5e975eae1a`](https://github.com/vllm-project/vllm/commit/5e975eae1a) [#47888](https://github.com/vllm-project/vllm/pull/47888)
  [Bugfix] Avoid blocking model launching when no system ffmpeg available for TorchCodec (#47888)
  _Files: `vllm/multimodal/video.py`, `vllm/utils/import_utils.py`_
- **2026-07-07** [`6db31c8e76`](https://github.com/vllm-project/vllm/commit/6db31c8e76) [#47758](https://github.com/vllm-project/vllm/pull/47758)
  [XPU][CI]Adjust memory request for tests in Intel GPU CI (#47758)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/models_distributed_intel.yaml`, `.buildkite/intel_jobs/models_multimodal_intel.yaml` _+1 more__
- **2026-07-07** [`39a1d32b59`](https://github.com/vllm-project/vllm/commit/39a1d32b59) [#47581](https://github.com/vllm-project/vllm/pull/47581)
  [Rust Frontend] Avoid extra copies for multimodal tensors (#47581)
  _Files: `rust/src/engine-core-client/src/protocol/tensor.rs`, `rust/src/text/src/lower.rs`_
- **2026-07-07** [`700e882eab`](https://github.com/vllm-project/vllm/commit/700e882eab) [#46609](https://github.com/vllm-project/vllm/pull/46609)
  Add TorchCodec as a video decoding backend (#46609)
  _Files: `docs/features/multimodal_inputs.md`, `requirements/cpu.txt`, `requirements/cuda.txt`, `requirements/test/cpu.txt` _+5 more__
- **2026-07-06** [`5ad11172b7`](https://github.com/vllm-project/vllm/commit/5ad11172b7) [#47416](https://github.com/vllm-project/vllm/pull/47416)
  [perf]Add fused Kimi image preprocessing (#47416)
  _Files: `vllm/model_executor/models/kimi_k25.py`, `vllm/transformers_utils/processor.py`, `vllm/transformers_utils/processors/kimi_k25_vision_fused.py`, `vllm/utils/import_utils.py` _+1 more__
- **2026-07-06** [`40cc2e8327`](https://github.com/vllm-project/vllm/commit/40cc2e8327) [#47165](https://github.com/vllm-project/vllm/pull/47165)
  [Bugfix] Return HTTP 422 for unprocessable image URLs instead of 500 (#47165)
  _Files: `tests/multimodal/media/test_unprocessable_entity_error.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/serve/utils/error_response.py`, `vllm/exceptions.py` _+1 more__
- **2026-07-06** [`ba22152096`](https://github.com/vllm-project/vllm/commit/ba22152096) [#47259](https://github.com/vllm-project/vllm/pull/47259)
  fix(security): block request-level GPU video backend selection withou… (#47259)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/multimodal/media/video.py`, `vllm/multimodal/video.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-06** [`90ce3a09be`](https://github.com/vllm-project/vllm/commit/90ce3a09be) [#47607](https://github.com/vllm-project/vllm/pull/47607)
  [bugfix] fix MOSS-Audio deepstack_input_embeds initialization in PP (#47607)
  _Files: `vllm/model_executor/models/moss_audio.py`_

## Models  (19 commits)

- **2026-07-10** [`26ff616bbf`](https://github.com/vllm-project/vllm/commit/26ff616bbf) [#48276](https://github.com/vllm-project/vllm/pull/48276)
  [Bugfix][Test] Register Qwen/Qwen3.5-4B example model (#48276)
  _Files: `tests/models/registry.py`_
- **2026-07-10** [`300e33797f`](https://github.com/vllm-project/vllm/commit/300e33797f) [#46998](https://github.com/vllm-project/vllm/pull/46998)
  [Perf] fuse more rmsnorm and all-reduce in qwen3.5 (#46998)
  _Files: `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-07-09** [`cac3e70cd4`](https://github.com/vllm-project/vllm/commit/cac3e70cd4) [#43896](https://github.com/vllm-project/vllm/pull/43896)
  Correct model layer aliasing for Bert style models (#43896)
  _Files: `vllm/model_executor/models/modernbert.py`, `vllm/model_executor/warmup/deep_gemm_warmup.py`_
- **2026-07-09** [`85b3a7264b`](https://github.com/vllm-project/vllm/commit/85b3a7264b) [#47381](https://github.com/vllm-project/vllm/pull/47381)
  [Bugfix][Model Runner V2] Order uniform decodes first so spec decodes aren't misclassified as prefills (#47381)
  _Files: `tests/v1/worker/test_gpu_batch_ordering.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-07-09** [`b83be00cdd`](https://github.com/vllm-project/vllm/commit/b83be00cdd) [#48100](https://github.com/vllm-project/vllm/pull/48100)
  Migrate Olmo and Olmo2 to the Transformers modeling backend (#48100)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/olmo.py`, `vllm/model_executor/models/olmo3.py`, `vllm/model_executor/models/registry.py`_
- **2026-07-09** [`ab7961a14a`](https://github.com/vllm-project/vllm/commit/ab7961a14a) [#47989](https://github.com/vllm-project/vllm/pull/47989)
  Remove TeleChatForCausalLM  (#47989)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-07-09** [`a07765c6bd`](https://github.com/vllm-project/vllm/commit/a07765c6bd) [#42478](https://github.com/vllm-project/vllm/pull/42478)
  [Bugfix] Fix Qwen3-ASR transcription streaming postprocessing (#42478)
  _Files: `tests/entrypoints/speech_to_text/transcription/test_transcription_inter_chunk_spacing.py`, `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/qwen3_asr.py`_
- **2026-07-09** [`1171467e91`](https://github.com/vllm-project/vllm/commit/1171467e91) [#48073](https://github.com/vllm-project/vllm/pull/48073)
  [CPU] Fix Qwen-Next SSM type for AMX GDN (#48073)
  _Files: `vllm/platforms/cpu.py`_
- **2026-07-08** [`a1ab51afb6`](https://github.com/vllm-project/vllm/commit/a1ab51afb6) [#47797](https://github.com/vllm-project/vllm/pull/47797)
  [Bugfix] Allocate HY V3 expert_bias in float32 to prevent silent downcasting (#47797)
  _Files: `vllm/model_executor/models/hy_v3.py`_
- **2026-07-08** [`e7b3853bac`](https://github.com/vllm-project/vllm/commit/e7b3853bac) [#47970](https://github.com/vllm-project/vllm/pull/47970)
  Remove router weight upcast for DSv2-related models (#47970)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-07-08** [`285c08c036`](https://github.com/vllm-project/vllm/commit/285c08c036) [#47729](https://github.com/vllm-project/vllm/pull/47729)
  [Model] Support MOSS-Transcribe-Diarize (#47729)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/moss_transcribe_diarize.py`, `vllm/model_executor/models/registry.py` _+3 more__
- **2026-07-08** [`7c67da967f`](https://github.com/vllm-project/vllm/commit/7c67da967f) [#47969](https://github.com/vllm-project/vllm/pull/47969)
  Remove unused _get_kv_cache_config_deepseek_v4 alias (#47969)
  _Files: `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-07** [`c3284c31f5`](https://github.com/vllm-project/vllm/commit/c3284c31f5) [#47546](https://github.com/vllm-project/vllm/pull/47546)
  [Perf][3/N] Expand Triton kernel warmup coverage, Qwen (#47546)
  _Files: `vllm/model_executor/warmup/qwen_triton_warmup.py`_
- **2026-07-07** [`65dcde1695`](https://github.com/vllm-project/vllm/commit/65dcde1695) [#47466](https://github.com/vllm-project/vllm/pull/47466)
  [Bugfix] Fix PD disagg + MTP correctness for Qwen3.5(GDN) (#47466)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py` _+2 more__
- **2026-07-07** [`7ff656cc8b`](https://github.com/vllm-project/vllm/commit/7ff656cc8b) [#47440](https://github.com/vllm-project/vllm/pull/47440)
  fix: ensure no double load of lm head in nemotron mtp (#47440)
  _Files: `vllm/model_executor/models/nemotron_h_mtp.py`_
- **2026-07-07** [`c64c356990`](https://github.com/vllm-project/vllm/commit/c64c356990) [#45672](https://github.com/vllm-project/vllm/pull/45672)
  [Perf] Bound DiffusionGemma sampler transient via request-tiled logits (#45672)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-07-07** [`a46c9329e5`](https://github.com/vllm-project/vllm/commit/a46c9329e5) [#47619](https://github.com/vllm-project/vllm/pull/47619)
  [Rust Frontend] Add DeepSeek V3.2 roundtrip fixture (#47619)
  _Files: `rust/src/chat/tests/roundtrip.rs`_
- **2026-07-06** [`b136cc2c2c`](https://github.com/vllm-project/vllm/commit/b136cc2c2c) [#45965](https://github.com/vllm-project/vllm/pull/45965)
  [Bugfix][Model] Add stability window to DiffusionGemma to match HF stability_threshold semantics (#45965)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-07-06** [`d039c17114`](https://github.com/vllm-project/vllm/commit/d039c17114) [#47448](https://github.com/vllm-project/vllm/pull/47448)
  [Bugfix] Recycle post-final-norm hidden in GLM MTP (single norm) (#47448)
  _Files: `vllm/models/deepseek_v32/nvidia/mtp.py`_

## CI / Build  (15 commits)

- **2026-07-13** [`487dfb3418`](https://github.com/vllm-project/vllm/commit/487dfb3418) [#48472](https://github.com/vllm-project/vllm/pull/48472)
  [CI] Add SPDX license header to Rust/Protobuf sources (#48472)
- **2026-07-12** [`27c3e579f0`](https://github.com/vllm-project/vllm/commit/27c3e579f0) [#48222](https://github.com/vllm-project/vllm/pull/48222)
  [CI][Rust Frontend] Pin cargo tool versions (#48222)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`_
- **2026-07-10** [`28eaf05d56`](https://github.com/vllm-project/vllm/commit/28eaf05d56) [#44472](https://github.com/vllm-project/vllm/pull/44472)
  [XPU] Enable v1/sample tests on XPU CI (#44472)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-09** [`e12b91b032`](https://github.com/vllm-project/vllm/commit/e12b91b032) [#48170](https://github.com/vllm-project/vllm/pull/48170)
  [CI] Fix cargo-deny config flag ordering (#48170)
  _Files: `.buildkite/scripts/run-rust-frontend-cargo-ci.sh`_
- **2026-07-09** [`ea0fa34f49`](https://github.com/vllm-project/vllm/commit/ea0fa34f49) [#48161](https://github.com/vllm-project/vllm/pull/48161)
  [CI] Increase extract hidden states TP2 timeout (#48161)
  _Files: `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`_
- **2026-07-09** [`0206f10871`](https://github.com/vllm-project/vllm/commit/0206f10871) [#47880](https://github.com/vllm-project/vllm/pull/47880)
  Add Intel XPU Docker release pipeline (#47880)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/xpu/create-xpu-ecr-manifest.sh`_
- **2026-07-07** [`47c40bfe8a`](https://github.com/vllm-project/vllm/commit/47c40bfe8a) [#47913](https://github.com/vllm-project/vllm/pull/47913)
  [Doc] Fix manylinux tag in installation guide (#47913)
  _Files: `docs/contributing/ci/nightly_builds.md`, `docs/getting_started/installation/cpu.arm.inc.md`, `docs/getting_started/installation/cpu.x86.inc.md`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-07-07** [`abe41f28de`](https://github.com/vllm-project/vllm/commit/abe41f28de) [#47835](https://github.com/vllm-project/vllm/pull/47835)
  Upgrade tpu-inference to v0.24.0 (#47835)
  _Files: `requirements/tpu.txt`_
- **2026-07-07** [`9dd2465896`](https://github.com/vllm-project/vllm/commit/9dd2465896) [#35059](https://github.com/vllm-project/vllm/pull/35059)
  feat(cpu): add CPU support for Mamba ShortConv (#35059)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `tests/kernels/mamba/test_cpu_short_conv.py`, `vllm/model_executor/layers/mamba/short_conv.py`_
- **2026-07-06** [`ae098abe3f`](https://github.com/vllm-project/vllm/commit/ae098abe3f) [#47726](https://github.com/vllm-project/vllm/pull/47726)
  [CI] Fix some errors on `main` (#47726)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-07-06** [`3ee9eea928`](https://github.com/vllm-project/vllm/commit/3ee9eea928) [#47457](https://github.com/vllm-project/vllm/pull/47457)
  [macOS][CPU][Installation] Fix the broken installation of vllm 0.24.0 in macos + cpu (#47457)
  _Files: `requirements/cuda.txt`_
- **2026-07-06** [`51ee564e56`](https://github.com/vllm-project/vllm/commit/51ee564e56) [#47748](https://github.com/vllm-project/vllm/pull/47748)
  [CI] Skip test for checkpoint that was deleted (#47748)
  _Files: `tests/models/registry.py`_
- **2026-07-06** [`cdab28319f`](https://github.com/vllm-project/vllm/commit/cdab28319f) [#47675](https://github.com/vllm-project/vllm/pull/47675)
  [XPU][CI]Add agent tags for Basic Models Tests (Initialization) in Intel GPU CI (#47675)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-06** [`990c2a0187`](https://github.com/vllm-project/vllm/commit/990c2a0187) [#45243](https://github.com/vllm-project/vllm/pull/45243)
  [RISC-V] Enable BF16 on VLEN=256 hardware (#45243)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-07-06** [`e9cc1fd093`](https://github.com/vllm-project/vllm/commit/e9cc1fd093) [#47687](https://github.com/vllm-project/vllm/pull/47687)
  [CI/Build][CPU] Remove global extra index (#47687)
  _Files: `docker/Dockerfile.cpu`, `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.apple.inc.md`, `docs/getting_started/installation/cpu.s390x.inc.md` _+2 more__

## Scheduler / Engine  (13 commits)

- **2026-07-12** [`8df14cfc8c`](https://github.com/vllm-project/vllm/commit/8df14cfc8c) [#42433](https://github.com/vllm-project/vllm/pull/42433)
  [EC Connector] Add EC Transfer Params (#42433)
  _Files: `.buildkite/test_areas/misc.yaml`, `rust/proto/vllm_grpc.proto`, `rust/src/chat/src/event.rs`, `rust/src/chat/src/output/default/unified.rs` _+51 more__
- **2026-07-10** [`5715fde12c`](https://github.com/vllm-project/vllm/commit/5715fde12c) [#44301](https://github.com/vllm-project/vllm/pull/44301)
  [Feature][Parser] Support include_reasoning param for non-Harmony models (#44301)
  _Files: `docs/features/reasoning_outputs.md`, `tests/entrypoints/openai/chat_completion/test_include_reasoning.py`, `tests/parser/engine/conftest.py`, `tests/parser/engine/test_nemotron_v3.py` _+9 more__
- **2026-07-09** [`ae6170f874`](https://github.com/vllm-project/vllm/commit/ae6170f874) [#46694](https://github.com/vllm-project/vllm/pull/46694)
  [P/D][Bugfix] Fix PD async KV load lookahead handling for MTP spec decode (#46694)
  _Files: `vllm/v1/core/kv_cache_manager.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-08** [`bd3bb4eb26`](https://github.com/vllm-project/vllm/commit/bd3bb4eb26) [#47608](https://github.com/vllm-project/vllm/pull/47608)
  [Misc][Docs]  Add human-readable integer support for more cli-args (#47608)
  _Files: `docs/cli/README.md`, `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`_
- **2026-07-08** [`dd127d82ed`](https://github.com/vllm-project/vllm/commit/dd127d82ed) [#47053](https://github.com/vllm-project/vllm/pull/47053)
  [Core][Engine] only materialize tokens when thinking budget is in req (#47053)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-07** [`675f4295cd`](https://github.com/vllm-project/vllm/commit/675f4295cd) [#47845](https://github.com/vllm-project/vllm/pull/47845)
  fix(security): bound completion prompt list to prevent unbounded engine fan-out (#47845)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/envs.py`_
- **2026-07-07** [`c5b66233b2`](https://github.com/vllm-project/vllm/commit/c5b66233b2) [#47464](https://github.com/vllm-project/vllm/pull/47464)
  [Bugfix][Spec Decode] Skip uniform spec-decode padding for diffusion models (#47464)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-07** [`b4cfbc24d3`](https://github.com/vllm-project/vllm/commit/b4cfbc24d3) [#44490](https://github.com/vllm-project/vllm/pull/44490)
  [Bugfix][Core] Fix host memory leak from undrained new_block_ids (#44490)
  _Files: `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-07-07** [`32ab064621`](https://github.com/vllm-project/vllm/commit/32ab064621) [#47148](https://github.com/vllm-project/vllm/pull/47148)
  [UX] Add `model_class_overrides` for  development and debugging (#47148)
  _Files: `tests/test_config.py`, `vllm/config/model.py`, `vllm/engine/arg_utils.py`_
- **2026-07-07** [`86db6c3070`](https://github.com/vllm-project/vllm/commit/86db6c3070) [#46768](https://github.com/vllm-project/vllm/pull/46768)
  [Frontend] add per-request timing `metrics` field to response body of Chat/Completions APIs (#46768)
  _Files: `docs/features/per_request_metrics.md`, `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `tests/entrypoints/openai/test_cli_args.py` _+8 more__
- **2026-07-06** [`373eb314af`](https://github.com/vllm-project/vllm/commit/373eb314af) [#46066](https://github.com/vllm-project/vllm/pull/46066)
  [Bugfix][Core] Fix num_output_placeholders underflow with async scheduling + spec decode (#46066)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-06** [`8f4c69b222`](https://github.com/vllm-project/vllm/commit/8f4c69b222) [#47444](https://github.com/vllm-project/vllm/pull/47444)
  [Rust Frontend] Cache metric handles for scheduler & request stats (#47444)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/client/stream.rs`, `rust/src/engine-core-client/src/metrics.rs` _+5 more__
- **2026-07-06** [`2fa10566e3`](https://github.com/vllm-project/vllm/commit/2fa10566e3) [#47420](https://github.com/vllm-project/vllm/pull/47420)
  [Core][DP] Rotate load-balancer tie-break to avoid systematic engine bias (#47420)
  _Files: `vllm/v1/engine/core_client.py`_

## Serving / API  (13 commits)

- **2026-07-12** [`83762b77b0`](https://github.com/vllm-project/vllm/commit/83762b77b0) [#47173](https://github.com/vllm-project/vllm/pull/47173)
  [Frontend] Add /abort_requests to the RLHF dev API router (#47173)
  _Files: `docs/serving/online_serving/README.md`, `docs/training/async_rl.md`, `docs/usage/security.md`, `rust/src/llm/src/inflight.rs` _+4 more__
- **2026-07-11** [`0067311536`](https://github.com/vllm-project/vllm/commit/0067311536) [#48333](https://github.com/vllm-project/vllm/pull/48333)
  fix(entrypoints): stop resolve_items leaking in-flight media fetch tasks on partial failure (#48333)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-07-11** [`3d99b0499a`](https://github.com/vllm-project/vllm/commit/3d99b0499a) [#48278](https://github.com/vllm-project/vllm/pull/48278)
  [Logs] DP Supervisor Log Improvement (#48278)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/entrypoints/openai/dp_supervisor.py`_
- **2026-07-09** [`e87521626f`](https://github.com/vllm-project/vllm/commit/e87521626f) [#46415](https://github.com/vllm-project/vllm/pull/46415)
  Sanitize server file paths from validation error responses (#46415)
  _Files: `tests/entrypoints/serve/utils/test_api_utils.py`, `tests/entrypoints/serve/utils/test_server_utils.py`, `vllm/entrypoints/serve/utils/api_utils.py`, `vllm/entrypoints/serve/utils/server_utils.py`_
- **2026-07-08** [`04a703e397`](https://github.com/vllm-project/vllm/commit/04a703e397) [#46793](https://github.com/vllm-project/vllm/pull/46793)
  [Frontend] Support bad_words in the /v1/completions endpoint (#46793)
  _Files: `tests/entrypoints/openai/completion/test_completion.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-07-08** [`d35eba302f`](https://github.com/vllm-project/vllm/commit/d35eba302f) [#47028](https://github.com/vllm-project/vllm/pull/47028)
  [Bugfix] Avoid leaking Pydantic repr in tool_choice error message (#47028)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/renderers/online_renderer.py`_
- **2026-07-08** [`5d5fab0061`](https://github.com/vllm-project/vllm/commit/5d5fab0061) [#44303](https://github.com/vllm-project/vllm/pull/44303)
  [Bugfix][Frontend] Fix http_requests_total metric recording some 4xx errors as 5xx (#44303)
  _Files: `tests/entrypoints/serve/instrumentator/test_http_status_metrics.py`, `vllm/entrypoints/openai/api_server.py`_
- **2026-07-08** [`0303f37a54`](https://github.com/vllm-project/vllm/commit/0303f37a54) [#47772](https://github.com/vllm-project/vllm/pull/47772)
  [Bugfix][Pooling] Align CrossEncoder token type ids after truncation (#47772)
  _Files: `tests/entrypoints/pooling/scoring/test_cross_encoder_offline.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_
- **2026-07-07** [`b3e85be663`](https://github.com/vllm-project/vllm/commit/b3e85be663) [#47834](https://github.com/vllm-project/vllm/pull/47834)
  fix: use configured max_logprobs instead of hardcoded 20 in derender validation (#47834)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/entrypoints/scale_out/derender/serving.py`_
- **2026-07-07** [`8e61b646e2`](https://github.com/vllm-project/vllm/commit/8e61b646e2) [#47260](https://github.com/vllm-project/vllm/pull/47260)
  fix(security): add resource bounds validation to derender endpoints (#47260)
  _Files: `tests/entrypoints/scale_out/derender/test_derender.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-07-07** [`34e6dfced8`](https://github.com/vllm-project/vllm/commit/34e6dfced8) [#47787](https://github.com/vllm-project/vllm/pull/47787)
  [Rust Frontend] Stamp `arrival_time` at the frontend entry (#47787)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/llm/src/lib.rs`, `rust/src/llm/src/request.rs`, `rust/src/llm/src/request_metrics.rs` _+6 more__
- **2026-07-06** [`98e4726a14`](https://github.com/vllm-project/vllm/commit/98e4726a14) [#47697](https://github.com/vllm-project/vllm/pull/47697)
  [fix][run_batch]: respect proxy env vars when downloading media URLs (#47697)
  _Files: `vllm/entrypoints/openai/run_batch.py`_
- **2026-07-06** [`394edc8108`](https://github.com/vllm-project/vllm/commit/394edc8108) [#47682](https://github.com/vllm-project/vllm/pull/47682)
  [XPU] limit max-num-seqs in test_lmeval.py for XPU (#47682)
  _Files: `tests/entrypoints/openai/correctness/test_lmeval.py`_

## Quantization  (12 commits)

- **2026-07-12** [`5f8e73cb8b`](https://github.com/vllm-project/vllm/commit/5f8e73cb8b) [#48330](https://github.com/vllm-project/vllm/pull/48330)
  [Bugfix] Guard mixed-dtype allreduce RMSNorm quant fusions (#48330)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-07-09** [`429f405748`](https://github.com/vllm-project/vllm/commit/429f405748) [#47296](https://github.com/vllm-project/vllm/pull/47296)
  [Bugfix] Guard CUDA-only rms_norm_per_block_quant in FUSED_OPS for non-CUDA builds (#47296)
  _Files: `vllm/compilation/passes/fusion/rms_quant_fusion.py`_
- **2026-07-08** [`b2cf70ea3a`](https://github.com/vllm-project/vllm/commit/b2cf70ea3a) [#47980](https://github.com/vllm-project/vllm/pull/47980)
  [CI] BugFix Eval Small Models Distributed test for DiffusionGemma (#47980)
  _Files: `tests/evals/gsm8k/configs/DiffusionGemma-26B-A4B-it-FP8-dynamic.yaml`, `tests/evals/gsm8k/test_gsm8k_correctness.py`_
- **2026-07-07** [`7d2ce5750e`](https://github.com/vllm-project/vllm/commit/7d2ce5750e) [#47910](https://github.com/vllm-project/vllm/pull/47910)
  [Bugfix] Patch Hopper MXFP4 OOB scales reads leading to NaN (#47910)
  _Files: `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`_
- **2026-07-07** [`d99adcebdc`](https://github.com/vllm-project/vllm/commit/d99adcebdc) [#47445](https://github.com/vllm-project/vllm/pull/47445)
  [BugFix] Fix ModelOpt quantization inference for fused siblings (#47445)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-07-07** [`0a2965b1b3`](https://github.com/vllm-project/vllm/commit/0a2965b1b3) [#47318](https://github.com/vllm-project/vllm/pull/47318)
  [BugFix] Fix ModelOpt mixed-precision quantization for sparse `quantized_layers` configs. (#47318)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-07-07** [`445321fab4`](https://github.com/vllm-project/vllm/commit/445321fab4) [#47780](https://github.com/vllm-project/vllm/pull/47780)
  [Bugfix] [Quantization] Fix loading for CT DSV2 (#47780)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-07-06** [`9fde043f54`](https://github.com/vllm-project/vllm/commit/9fde043f54) [#43994](https://github.com/vllm-project/vllm/pull/43994)
  [Kernel][Helion][1/N] Add Helion kernel for silu_and_mul_per_block_quant (#43994)
  _Files: `tests/kernels/helion/test_silu_and_mul_per_block_quant.py`, `vllm/kernels/helion/configs/silu_and_mul_per_block_quant/nvidia_b200.json`, `vllm/kernels/helion/configs/silu_and_mul_per_block_quant/nvidia_h100.json`, `vllm/kernels/helion/ops/silu_and_mul_per_block_quant.py`_
- **2026-07-06** [`24dd2aec81`](https://github.com/vllm-project/vllm/commit/24dd2aec81) [#46168](https://github.com/vllm-project/vllm/pull/46168)
  [Bugfix] Preserve FP8 indexer WK pairs across incremental load_weights (#46168)
  _Files: `vllm/model_executor/models/deepseek_v2.py`_
- **2026-07-06** [`7a90eb98ab`](https://github.com/vllm-project/vllm/commit/7a90eb98ab) [#47091](https://github.com/vllm-project/vllm/pull/47091)
  [Bugfix] [Gemma4] Fix Gemma4 MTP draft model layers ignoring quant_config (#47091)
  _Files: `vllm/model_executor/models/gemma4_mtp.py`_
- **2026-07-06** [`e433634c78`](https://github.com/vllm-project/vllm/commit/e433634c78) [#47538](https://github.com/vllm-project/vllm/pull/47538)
  [Performance][Hardware][RISC-V] Reduce LMUL pressure in INT4 LUT dequant (#47538)
  _Files: `csrc/cpu/cpu_types_riscv_impl.hpp`_
- **2026-07-06** [`d9c1767cd4`](https://github.com/vllm-project/vllm/commit/d9c1767cd4) [#46361](https://github.com/vllm-project/vllm/pull/46361)
  [INC][ARK] Direct Register Custom Op for ARK (#46361)
  _Files: `docs/features/quantization/inc.md`, `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_ark_ops.py` _+2 more__

## Disaggregation / PD  (9 commits)

- **2026-07-13** [`9e57de7197`](https://github.com/vllm-project/vllm/commit/9e57de7197) [#40714](https://github.com/vllm-project/vllm/pull/40714)
  [CPU] Create Proper Numa topology for s390x (#40714)
  _Files: `docker/Dockerfile.s390x`, `requirements/common.txt`, `vllm/distributed/device_communicators/cpu_communicator.py`, `vllm/platforms/cpu.py` _+3 more__
- **2026-07-12** [`481e481be7`](https://github.com/vllm-project/vllm/commit/481e481be7) [#46384](https://github.com/vllm-project/vllm/pull/46384)
  [2/N][Core] support partial prefix cache hit for hybrid model (#46384)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_deferred_block_free.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py` _+17 more__
- **2026-07-10** [`2d814a0082`](https://github.com/vllm-project/vllm/commit/2d814a0082) [#47923](https://github.com/vllm-project/vllm/pull/47923)
  [kv_offload] Emit tier-owned BlockStored events from FS/OBJ secondary tiers (#47923)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/distributed/kv_events.py` _+2 more__
- **2026-07-09** [`2ded1b24e7`](https://github.com/vllm-project/vllm/commit/2ded1b24e7) [#47317](https://github.com/vllm-project/vllm/pull/47317)
  [KV Connector][Mooncake] Apply SWA lookup mask before hashing/key build (#47317)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-07-09** [`2285cfca46`](https://github.com/vllm-project/vllm/commit/2285cfca46) [#46865](https://github.com/vllm-project/vllm/pull/46865)
  [KVConnector] MultiConnector: give every sub-connector the request's real blocks in `update_state_after_alloc` (#46865)
  _Files: `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py`_
- **2026-07-08** [`7802c20c4e`](https://github.com/vllm-project/vllm/commit/7802c20c4e) [#45880](https://github.com/vllm-project/vllm/pull/45880)
  [KVConnector][NIXL] Support pipeline-parallel prefill in push mode (#45880)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `examples/disaggregated/disaggregated_serving/disagg_proxy_pushconnector_demo.py`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/nixl_side_channel_probe.py` _+11 more__
- **2026-07-07** [`2f3f441f84`](https://github.com/vllm-project/vllm/commit/2f3f441f84) [#45177](https://github.com/vllm-project/vllm/pull/45177)
  fix: include topic frame in KV events replay response (#45177)
  _Files: `examples/features/kv_events/kv_events_subscriber.py`, `tests/distributed/conftest.py`, `tests/distributed/test_events.py`, `vllm/distributed/kv_events.py`_
- **2026-07-07** [`c46ced1ee3`](https://github.com/vllm-project/vllm/commit/c46ced1ee3) [#46544](https://github.com/vllm-project/vllm/pull/46544)
  [kv_offload] Establish tier-owned KV event handling (#46544)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+7 more__
- **2026-07-07** [`a4f019fa25`](https://github.com/vllm-project/vllm/commit/a4f019fa25) [#45159](https://github.com/vllm-project/vllm/pull/45159)
  fix(distributed): propagate distributed_timeout_seconds to NCCL device groups (#45159)
  _Files: `vllm/distributed/parallel_state.py`, `vllm/distributed/utils.py`_

## Speculative Decoding  (8 commits)

- **2026-07-13** [`8c5dafcd09`](https://github.com/vllm-project/vllm/commit/8c5dafcd09) [#48452](https://github.com/vllm-project/vllm/pull/48452)
  [Bugfix][UT]Fix EagleMiniCPMForCausalLM meet TypeError (#48452)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/minicpm_eagle.py`_
- **2026-07-12** [`fc1c548093`](https://github.com/vllm-project/vllm/commit/fc1c548093) [#46725](https://github.com/vllm-project/vllm/pull/46725)
  Runtime Draft Weight Update for Speculative Decoding (#46725)
  _Files: `docs/training/weight_transfer/base.md`, `tests/entrypoints/openai/test_openai_schema.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/distributed/weight_transfer/base.py` _+8 more__
- **2026-07-10** [`fabec87f63`](https://github.com/vllm-project/vllm/commit/fabec87f63) [#48153](https://github.com/vllm-project/vllm/pull/48153)
  [Model] Migrate MistralLarge3ForCausalLM to AutoWeightsLoader (#48153)
  _Files: `vllm/model_executor/models/mistral_large_3.py`, `vllm/model_executor/models/mistral_large_3_eagle.py`_
- **2026-07-08** [`7cc2e8e74f`](https://github.com/vllm-project/vllm/commit/7cc2e8e74f) [#47911](https://github.com/vllm-project/vllm/pull/47911)
  fix: hash speculative draft model config (#47911)
  _Files: `vllm/config/speculative.py`_
- **2026-07-07** [`93e2ab7111`](https://github.com/vllm-project/vllm/commit/93e2ab7111) [#45963](https://github.com/vllm-project/vllm/pull/45963)
  Disable dynamic speculative decoding when DP is enabled (#45963)
  _Files: `docs/features/speculative_decoding/dynamic_speculative_decoding.md`, `tests/v1/core/utils.py`, `tests/v1/spec_decode/test_dynamic_sd.py`, `vllm/config/vllm.py`_
- **2026-07-07** [`cbe9c40f99`](https://github.com/vllm-project/vllm/commit/cbe9c40f99) [#45352](https://github.com/vllm-project/vllm/pull/45352)
  [Bugfix] Forward callable hf_overrides to the draft model config (#45352)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `tests/models/registry.py`, `vllm/config/speculative.py`_
- **2026-07-06** [`8d8ec38361`](https://github.com/vllm-project/vllm/commit/8d8ec38361) [#47429](https://github.com/vllm-project/vllm/pull/47429)
  [Bugfix][Spec Decode] Add missing draft_id_to_target_id to DSparkDeepseekV4ForCausalLM (#47429)
  _Files: `vllm/models/deepseek_v4/nvidia/dspark.py`_
- **2026-07-06** [`d2ec433e37`](https://github.com/vllm-project/vllm/commit/d2ec433e37) [#43957](https://github.com/vllm-project/vllm/pull/43957)
  [XPU] Fix Eagle3 initialization on XPU (#43957)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/model_executor/models/llama_eagle3.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_

## KV Cache / Offload  (7 commits)

- **2026-07-12** [`4c81772e8b`](https://github.com/vllm-project/vllm/commit/4c81772e8b) [#48102](https://github.com/vllm-project/vllm/pull/48102)
  [Bugfix][KV Offloading] Fix stale transfer_jobs after reset_cache + harden job completion (#48102)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-11** [`04d553f390`](https://github.com/vllm-project/vllm/commit/04d553f390) [#47316](https://github.com/vllm-project/vllm/pull/47316)
  [Misc] Use meta tensor for KV cache stride calculation (#47316)
  _Files: `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-07-09** [`529af88842`](https://github.com/vllm-project/vllm/commit/529af88842) [#47849](https://github.com/vllm-project/vllm/pull/47849)
  [KV Offloading] Add free block iterator for CPU offload scheduling (#47849)
  _Files: `vllm/v1/core/kv_cache_utils.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-07-08** [`dcdd756d75`](https://github.com/vllm-project/vllm/commit/dcdd756d75) [#46893](https://github.com/vllm-project/vllm/pull/46893)
  [CI] GSM8K eval integration test for KV offloading (#46893)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `rust/src/server/src/routes/cache.rs`, `rust/src/server/src/routes/tests.rs`, `tests/evals/gsm8k/test_gsm8k_offloading.py` _+1 more__
- **2026-07-07** [`48fcfc926c`](https://github.com/vllm-project/vllm/commit/48fcfc926c) [#47274](https://github.com/vllm-project/vllm/pull/47274)
  [KV Offload] Add `ParentManager` ABC for secondary tier callbacks (#47274)
  _Files: `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/manager.py`_
- **2026-07-07** [`3354dba381`](https://github.com/vllm-project/vllm/commit/3354dba381) [#46972](https://github.com/vllm-project/vllm/pull/46972)
  [Bugfix][KV offload] Store interior chunk-boundary blocks under MTP/Eagle (#46972)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-07-07** [`e040899a00`](https://github.com/vllm-project/vllm/commit/e040899a00) [#45958](https://github.com/vllm-project/vllm/pull/45958)
  [KV Offloading] Add basic offloading metrics (#45958)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/cpu/test_manager.py` _+6 more__

## LoRA  (6 commits)

- **2026-07-13** [`107a03ba63`](https://github.com/vllm-project/vllm/commit/107a03ba63) [#48390](https://github.com/vllm-project/vllm/pull/48390)
  [Core] Support fp32 lm_head for generation models via head_dtype (RFC #48305 §3.6) (#48390)
  _Files: `tests/models/language/generation_ppl_test/ppl_utils.py`, `tests/models/language/generation_ppl_test/test_gpt.py`, `tests/v1/sample/test_head_dtype.py`, `vllm/config/model.py` _+2 more__
- **2026-07-12** [`9a48eef89a`](https://github.com/vllm-project/vllm/commit/9a48eef89a) [#47690](https://github.com/vllm-project/vllm/pull/47690)
  [Bugfix][LoRA] Support ark_linear base layer in _get_lora_device (#47690)
  _Files: `tests/lora/test_layers_utils.py`, `vllm/lora/layers/utils.py`_
- **2026-07-09** [`b8c7c86533`](https://github.com/vllm-project/vllm/commit/b8c7c86533) [#47944](https://github.com/vllm-project/vllm/pull/47944)
  [XPU][LoRA] Fix torch.compile DEVICE_LOST by avoiding view-mutation in LoRA shrink (#47944)
  _Files: `vllm/lora/punica_wrapper/punica_xpu.py`_
- **2026-07-07** [`392d1b4d2e`](https://github.com/vllm-project/vllm/commit/392d1b4d2e) [#47725](https://github.com/vllm-project/vllm/pull/47725)
  [BugFix][LoRA] Refresh punica metadata when LoRA slots are reassigned under an unchanged mapping (#47725)
  _Files: `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`_
- **2026-07-07** [`0ed05b6f82`](https://github.com/vllm-project/vllm/commit/0ed05b6f82) [#47832](https://github.com/vllm-project/vllm/pull/47832)
  [CI] Fix Transformers modeling backend LoRA test (#47832)
  _Files: `tests/models/transformers/fusers/test_linear.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/models/transformers/fusers/qkv.py`_
- **2026-07-06** [`6569df6a3e`](https://github.com/vllm-project/vllm/commit/6569df6a3e) [#47534](https://github.com/vllm-project/vllm/pull/47534)
  [Test][LoRA] Use lightweight CPU reference and skip heavy cleanup in punica ops tests (#47534)
  _Files: `tests/lora/test_punica_ops.py`_

## Docs  (5 commits)

- **2026-07-07** [`dd0d74cd92`](https://github.com/vllm-project/vllm/commit/dd0d74cd92) [#47374](https://github.com/vllm-project/vllm/pull/47374)
  [Doc] Surface the --kv-cache-memory suggestion at INFO and document fast-startup knobs (#47374)
  _Files: `docs/configuration/optimization.md`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-07** [`c74e751824`](https://github.com/vllm-project/vllm/commit/c74e751824) [#36715](https://github.com/vllm-project/vllm/pull/36715)
  [Doc] Fix grammatically incorrect error message in gpu_worker and xpu_worker (#36715)
  _Files: `vllm/v1/worker/gpu_worker.py`, `vllm/v1/worker/xpu_worker.py`_
- **2026-07-07** [`1e823dc01d`](https://github.com/vllm-project/vllm/commit/1e823dc01d) [#47830](https://github.com/vllm-project/vllm/pull/47830)
  [docs update] Update usage of `hf` cli for cache list and removal (#47830)
  _Files: `docs/models/supported_models.md`_
- **2026-07-06** [`641cb59592`](https://github.com/vllm-project/vllm/commit/641cb59592) [#45813](https://github.com/vllm-project/vllm/pull/45813)
  [Doc] Clarify fastokens availability (#45813)
  _Files: `docs/configuration/optimization.md`_
- **2026-07-06** [`3d7f357ebf`](https://github.com/vllm-project/vllm/commit/3d7f357ebf) [#47701](https://github.com/vllm-project/vllm/pull/47701)
  [Doc] docs: fix note formatting for pooling models (#47701)
  _Files: `docs/models/pooling_models/README.md`_

## Compilation / CUDA Graph  (3 commits)

- **2026-07-08** [`56da398dac`](https://github.com/vllm-project/vllm/commit/56da398dac) [#48010](https://github.com/vllm-project/vllm/pull/48010)
  Fix embed scaling + CUDA graphs in Transformers modelling backend (#48010)
  _Files: `vllm/model_executor/models/transformers/base.py`_
- **2026-07-07** [`8b745527cd`](https://github.com/vllm-project/vllm/commit/8b745527cd) [#43161](https://github.com/vllm-project/vllm/pull/43161)
  [Bugfix] Fix UBatchWrapper CUDA graph key to sum all ubatches, not just first two (#43161)
  _Files: `vllm/v1/worker/gpu_ubatch_wrapper.py`_
- **2026-07-06** [`598d51153a`](https://github.com/vllm-project/vllm/commit/598d51153a) [#47589](https://github.com/vllm-project/vllm/pull/47589)
  [Bugfix][Distributed] Delegate MNNVL allreduce one-shot selection (#47589)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_

## Perf / Benchmark  (2 commits)

- **2026-07-13** [`e26264f3ef`](https://github.com/vllm-project/vllm/commit/e26264f3ef) [#39058](https://github.com/vllm-project/vllm/pull/39058)
  [Kernel] Implement CUDA kernel for ReLUSquaredActivation (relu^2) (#39058)
  _Files: `benchmarks/kernels/benchmark_relu_squared.py`, `csrc/libtorch_stable/activation_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+3 more__
- **2026-07-07** [`d3e69fd671`](https://github.com/vllm-project/vllm/commit/d3e69fd671) [#47081](https://github.com/vllm-project/vllm/pull/47081)
  [Perf] Use blocking CUDA events to avoid busy polling cuda driver lock (#47081)
  _Files: `vllm/v1/worker/gpu/async_utils.py`, `vllm/v1/worker/gpu/spec_decode/utils.py`, `vllm/v1/worker/gpu_model_runner.py`_

---
_Generated 2026-07-13 11:25 UTC_