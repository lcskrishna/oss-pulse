# sgl-project/sglang — Weekly Change Report
**Period:** 2026-05-25 → 2026-06-01  |  **Total commits:** 303

## ✨ New Features This Week

- **2026-06-01** [#25644](https://github.com/sgl-project/sglang/pull/25644) — [Speculative] [NPU] Adaptive-SD NPU support (#25644)
- **2026-06-01** [#26586](https://github.com/sgl-project/sglang/pull/26586) — [KDA] Support KDA packed decode (#26586)
- **2026-06-01** [#26903](https://github.com/sgl-project/sglang/pull/26903) — [NPU] [DOC] clarify Ascend NPU exclusive supported values for speculative args (#26903)
- **2026-06-01** [#26303](https://github.com/sgl-project/sglang/pull/26303) — [MoE] Extend kimi_k2_moe_fused_gate to support 256 experts (MiMo V2 Flash) (#26303)
- **2026-06-01** [#26862](https://github.com/sgl-project/sglang/pull/26862) — Add random-ids dataset, round-robin expert simulation, and kill_process_tree logging (#26862)
- **2026-06-01** [#26725](https://github.com/sgl-project/sglang/pull/26725) — 【NPU】add MiniMax2.5 best practice docs (#26725)
- **2026-05-31** [#26797](https://github.com/sgl-project/sglang/pull/26797) — [core] Compute token_type_ids in ForwardBatch.init_new (#26797)
- **2026-05-31** [#26821](https://github.com/sgl-project/sglang/pull/26821) — Add periodic KV-canary stats logging and kernel-run-counter health check (#26821)
- **2026-05-31** [#26820](https://github.com/sgl-project/sglang/pull/26820) — Add a sliding-window-attention divergence reporter for the KV-canary (#26820)
- **2026-05-31** [#26819](https://github.com/sgl-project/sglang/pull/26819) — Add the KV-canary perturb modes and PD-disaggregation e2e tests (#26819)
- _…and 79 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-06-01** [`89410b380b`](https://github.com/sgl-project/sglang/commit/89410b380b) [#26879](https://github.com/sgl-project/sglang/pull/26879) — [AMD] Pin compressed-tensors==0.15.0 to fix ROCm nightly build (#26879)
- **2026-06-01** [`b14fba17d9`](https://github.com/sgl-project/sglang/commit/b14fba17d9) [#26909](https://github.com/sgl-project/sglang/pull/26909) — [AMD] make bypass-fastfail label also disable within-suite fast-fail (#26909)
- **2026-06-01** [`f60710a1d7`](https://github.com/sgl-project/sglang/commit/f60710a1d7) [#26905](https://github.com/sgl-project/sglang/pull/26905) — [AMD] Fix stage-b-test-large-8-gpu-mi35x-disaggregation-amd : switch CACHE_HOST to a fresh path to fix "No space left on device" (#26905)
- **2026-06-01** [`1d7e2f6fb8`](https://github.com/sgl-project/sglang/commit/1d7e2f6fb8) [#22972](https://github.com/sgl-project/sglang/pull/22972) — [NPU] fix normal DeepEP mode num_tokens_per_rdma_rank error caused by none (#22972)
- **2026-05-29** [`ff8ed7a302`](https://github.com/sgl-project/sglang/commit/ff8ed7a302) [#26665](https://github.com/sgl-project/sglang/pull/26665) — [refactor] unify cuda-graph capture/replay across attention backends (#26665)
- **2026-05-29** [`9062f583db`](https://github.com/sgl-project/sglang/commit/9062f583db) [#25463](https://github.com/sgl-project/sglang/pull/25463) — [ROCm] Eliminate redundant contiguous copy in MLA attention on ROCm MXFP4 (#25463)
- **2026-05-29** [`4d1163e6a9`](https://github.com/sgl-project/sglang/commit/4d1163e6a9) [#26539](https://github.com/sgl-project/sglang/pull/26539) — [PD][MoRI] Align hybrid state transfer with per-component schema (#26539)
- **2026-05-29** [`ace730db48`](https://github.com/sgl-project/sglang/commit/ace730db48) [#26672](https://github.com/sgl-project/sglang/pull/26672) — [AMD] Work around HIP TPOT regression from Event.wait() in MTP seq lens resolution (#26672)
- **2026-05-29** [`6e9bd82714`](https://github.com/sgl-project/sglang/commit/6e9bd82714) [#26662](https://github.com/sgl-project/sglang/pull/26662) — [AMD][CI] Update v4 CI setting and move the task to main branch (#26662)
- **2026-05-29** [`79c844527c`](https://github.com/sgl-project/sglang/commit/79c844527c) [#25676](https://github.com/sgl-project/sglang/pull/25676) — Upgrade xgrammar to 0.2.1 (#25676)
- **2026-05-29** [`272066566f`](https://github.com/sgl-project/sglang/commit/272066566f) [#26591](https://github.com/sgl-project/sglang/pull/26591) — [AMD] Pin compressed-tensors<0.16.0 for srt_hip (fixes ROCm 7.2 nightly build) (#26591)
- **2026-05-29** [`569ee93357`](https://github.com/sgl-project/sglang/commit/569ee93357) [#26642](https://github.com/sgl-project/sglang/pull/26642) — [AMD] ci: switch CACHE_HOST to a fresh path to fix "No space left on device" (#26642)
- **2026-05-28** [`be32df33b9`](https://github.com/sgl-project/sglang/commit/be32df33b9) [#26437](https://github.com/sgl-project/sglang/pull/26437) — [MUSA] Fix startup with patched torchada (#26437)
- **2026-05-28** [`bdfd5da53e`](https://github.com/sgl-project/sglang/commit/bdfd5da53e) [#26562](https://github.com/sgl-project/sglang/pull/26562) — [AMD] AITER Upgrade (#26562)
- **2026-05-28** [`6f85957ff2`](https://github.com/sgl-project/sglang/commit/6f85957ff2) [#26544](https://github.com/sgl-project/sglang/pull/26544) — [AMD] Fix aiter checkout (rocm dockerfile) (#26544)
- **2026-05-28** [`505f37a63d`](https://github.com/sgl-project/sglang/commit/505f37a63d) [#26535](https://github.com/sgl-project/sglang/pull/26535) — [AMD] force AITER checkout to bypass CSV CRLF/LF smudge dirty state (#26535)
- **2026-05-28** [`81663cb5f1`](https://github.com/sgl-project/sglang/commit/81663cb5f1) [#26478](https://github.com/sgl-project/sglang/pull/26478) — [AMD] [CI] Register MI35x GSM8K nightly tests (#26478)
- **2026-05-27** [`deaba74745`](https://github.com/sgl-project/sglang/commit/deaba74745) [#26383](https://github.com/sgl-project/sglang/pull/26383) — [AMD][DSV4] DSV4 MTP graph + sparse triton attn optimizations (#26383)
- **2026-05-27** [`e06058ed62`](https://github.com/sgl-project/sglang/commit/e06058ed62) [#26499](https://github.com/sgl-project/sglang/pull/26499) — [Kernel] Import flash_mla kernels from sglang kernel for deepseek v4 (#26499)
- **2026-05-27** [`d44584e8d8`](https://github.com/sgl-project/sglang/commit/d44584e8d8) [#26396](https://github.com/sgl-project/sglang/pull/26396) — [AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate (#26396)
- **2026-05-27** [`bf5bc23431`](https://github.com/sgl-project/sglang/commit/bf5bc23431) [#26395](https://github.com/sgl-project/sglang/pull/26395) — [AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x (#26395)
- **2026-05-27** [`f32ca1e0e5`](https://github.com/sgl-project/sglang/commit/f32ca1e0e5) [#26443](https://github.com/sgl-project/sglang/pull/26443) — [AMD] AＭD CI - temporarily change to mi325 (#26443)
- **2026-05-26** [`0753182b50`](https://github.com/sgl-project/sglang/commit/0753182b50) [#26414](https://github.com/sgl-project/sglang/pull/26414) — chore: bump sgl-kernel version to 0.4.3 (#26414)
- **2026-05-26** [`d25a220fdb`](https://github.com/sgl-project/sglang/commit/d25a220fdb) [#26392](https://github.com/sgl-project/sglang/pull/26392) — [AMD] Relaxing timeout for AMD CI (#26392)
- **2026-05-26** [`3f5e2c7688`](https://github.com/sgl-project/sglang/commit/3f5e2c7688) [#26208](https://github.com/sgl-project/sglang/pull/26208) — [AMD] Dsv4/pr2 compressor opt (#26208)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#26438](https://github.com/sgl-project/sglang/issues/26438) | [RFC] In-Tree Support for Cambricon MLU Backend | — | 2026-06-01 |
| [#26087](https://github.com/sgl-project/sglang/issues/26087) | [Question] Does SGLang GLM-5 support NVIDIA SM120 GPUs? | — | 2026-06-01 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-06-01 |
| [#26890](https://github.com/sgl-project/sglang/issues/26890) | [AITER-Upgrade] AITER Scout Status | — | 2026-06-01 |
| [#26889](https://github.com/sgl-project/sglang/issues/26889) | [RFC] SGLang IR A Functional Intermediate Representation for SGLang Op | — | 2026-06-01 |
| [#26196](https://github.com/sgl-project/sglang/issues/26196) | DeepEP Buffer initialization fails with 'invalid resource handle' on G | — | 2026-05-31 |
| [#26796](https://github.com/sgl-project/sglang/issues/26796) | [Bug] MambaRadixCache.sanity_check() O(N) heap-walk runs on every idle | — | 2026-05-31 |
| [#21443](https://github.com/sgl-project/sglang/issues/21443) | [Feature][MPS] Better memory management for Apple Silicon Macs | inactive | 2026-05-30 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-05-30 |
| [#26751](https://github.com/sgl-project/sglang/issues/26751) | [Bug] Gemma-4 mm: single non-RGB image crashes vision tower and kills  | — | 2026-05-30 |
| [#20069](https://github.com/sgl-project/sglang/issues/20069) | [Tracking] Qwen3.5 bugs | high priority, nvidia | 2026-05-30 |
| [#8715](https://github.com/sgl-project/sglang/issues/8715) | [Roadmap] MoE Refactor | high priority, collaboration | 2026-05-29 |
| [#26345](https://github.com/sgl-project/sglang/issues/26345) | [Feature][AMD] Enhance Wheel Support for ROCm Platform | — | 2026-05-29 |
| [#26702](https://github.com/sgl-project/sglang/issues/26702) | [RFC] TensorCast KV backend integration | — | 2026-05-29 |
| [#26650](https://github.com/sgl-project/sglang/issues/26650) | [Bug] `get_processor()` TokenizersBackend replacement branch regresses | — | 2026-05-29 |
| [#26647](https://github.com/sgl-project/sglang/issues/26647) | [Bug] Mooncake HiCache fails to start with DeepSeek-V4-Flash hybrid ca | — | 2026-05-29 |
| [#24784](https://github.com/sgl-project/sglang/issues/24784) | [Bug] Qwen3.6 awq doesn't work with offloading | — | 2026-05-29 |
| [#26620](https://github.com/sgl-project/sglang/issues/26620) | Anthropic /v1/messages drops the `thinking` field, breaks default-off  | — | 2026-05-28 |
| [#26611](https://github.com/sgl-project/sglang/issues/26611) | DP-attention: add prefix_match load balance for in-instance cache-awar | — | 2026-05-28 |
| [#24656](https://github.com/sgl-project/sglang/issues/24656) | [RFC] Agent-Aware KV Cache Phase 1 for Agentic Workloads | — | 2026-05-28 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention / FlashInfer | 60 |
| Prefill / Decode Disaggregation | 35 |
| MoE / Expert Parallel | 31 |
| Multimodal | 22 |
| KV Cache / Memory | 19 |
| Speculative Decoding | 18 |
| Scheduler / Batching | 18 |
| Other | 17 |
| Triton / Kernels | 16 |
| Models | 13 |
| CI / Build | 12 |
| Tensor / Data Parallel | 11 |
| ROCm / AMD | 10 |
| Quantization | 7 |
| Docs / Examples | 6 |
| Structured Output | 5 |
| LoRA | 3 |

## Attention / FlashInfer  (60 commits)

- **2026-06-01** [`bc36231d65`](https://github.com/sgl-project/sglang/commit/bc36231d65) [#26586](https://github.com/sgl-project/sglang/pull/26586)
  [KDA] Support KDA packed decode (#26586)
  _Files: `benchmark/bench_linear_attention/bench_kda_decode.py`, `python/sglang/srt/layers/attention/fla/fused_recurrent.py`, `python/sglang/srt/layers/attention/linear/kda_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/kda_triton.py` _+1 more__
- **2026-06-01** [`118465f5b5`](https://github.com/sgl-project/sglang/commit/118465f5b5) [#26824](https://github.com/sgl-project/sglang/pull/26824)
  [attn backend] Make spec_v2 seq_lens_cpu optional in trtllm_mla backend (#26824)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-05-31** [`376635c1e3`](https://github.com/sgl-project/sglang/commit/376635c1e3) [#26123](https://github.com/sgl-project/sglang/pull/26123)
  Fix routed-experts device buffer overflow under DP attention (#26123)
  _Files: `python/sglang/srt/state_capturer/routed_experts.py`_
- **2026-05-31** [`7dd19ae3d8`](https://github.com/sgl-project/sglang/commit/7dd19ae3d8) [#26820](https://github.com/sgl-project/sglang/pull/26820)
  Add a sliding-window-attention divergence reporter for the KV-canary (#26820)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/kv_canary/runner/swa_divergence.py` _+9 more__
- **2026-05-31** [`0ca610a6df`](https://github.com/sgl-project/sglang/commit/0ca610a6df) [#26817](https://github.com/sgl-project/sglang/pull/26817)
  Add real-data KV verification to the KV-canary (#26817)
  _Files: `python/sglang/jit_kernel/benchmark/kv_canary/bench_verify.py`, `python/sglang/jit_kernel/benchmark/kv_canary/bench_write.py`, `python/sglang/jit_kernel/benchmark/kv_canary/utils.py`, `python/sglang/jit_kernel/csrc/kv_canary/canary_common.cuh` _+41 more__
- **2026-05-31** [`9ecf314970`](https://github.com/sgl-project/sglang/commit/9ecf314970) [#26809](https://github.com/sgl-project/sglang/pull/26809)
  Add the KV-canary install API and forward-path wiring (#26809)
  _Files: `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py` _+11 more__
- **2026-05-31** [`11391b2a1c`](https://github.com/sgl-project/sglang/commit/11391b2a1c) [#26808](https://github.com/sgl-project/sglang/pull/26808)
  Add the KV-canary core: data layer, MHA KV-pool patcher, and per-forward runner (#26808)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/__init__.py`, `python/sglang/srt/kv_canary/buffer_group.py`, `python/sglang/srt/kv_canary/capacities.py` _+42 more__
- **2026-05-30** [`a952e9174f`](https://github.com/sgl-project/sglang/commit/a952e9174f) [#25754](https://github.com/sgl-project/sglang/pull/25754)
  [MLX] Support Qwen3.5 (dense) Model (#25754)
  _Files: `.isort.cfg`, `python/pyproject_other.toml`, `python/sglang/bench_one_batch.py`, `python/sglang/srt/entrypoints/http_server.py` _+19 more__
- **2026-05-30** [`02aeed5387`](https://github.com/sgl-project/sglang/commit/02aeed5387) [#23122](https://github.com/sgl-project/sglang/pull/23122)
  [NPU] DFlash Speculative Decoding Support NPU (#23122)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/models/dflash.py`, `python/sglang/srt/speculative/dflash_worker.py`_
- **2026-05-30** [`fe4b29d391`](https://github.com/sgl-project/sglang/commit/fe4b29d391) [#26705](https://github.com/sgl-project/sglang/pull/26705)
  [Bugfix] Fix Ascend NPU CP attention for batch size > 1 (#26705)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`_
- **2026-05-30** [`1f850e67f2`](https://github.com/sgl-project/sglang/commit/1f850e67f2) [#26738](https://github.com/sgl-project/sglang/pull/26738)
  [core] Fix crashes on the `gpu_only` spec_v2 path (#26738)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/test/kits/fwd_occupancy_kit.py` _+1 more__
- **2026-05-29** [`a5e6a8887a`](https://github.com/sgl-project/sglang/commit/a5e6a8887a) [#23993](https://github.com/sgl-project/sglang/pull/23993)
  [attention] Fallback to Triton merge_state when FlashInfer hits CUDA thread limit (#23993)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`_
- **2026-05-29** [`6b5f0d0ccb`](https://github.com/sgl-project/sglang/commit/6b5f0d0ccb) [#26128](https://github.com/sgl-project/sglang/pull/26128)
  [core] Make spec_v2 `seq_lens_cpu` optional via backend `needs_cpu_seq_lens`; Triton opts out (#26128)
  _Files: `python/sglang/srt/layers/attention/base_attn_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py` _+10 more__
- **2026-05-29** [`ff8ed7a302`](https://github.com/sgl-project/sglang/commit/ff8ed7a302) [#26665](https://github.com/sgl-project/sglang/pull/26665)
  [refactor] unify cuda-graph capture/replay across attention backends (#26665)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/layers/attention/aiter_backend.py`, `python/sglang/srt/layers/attention/cutlass_mla_backend.py` _+15 more__
- **2026-05-29** [`ec075d8bc5`](https://github.com/sgl-project/sglang/commit/ec075d8bc5) [#26651](https://github.com/sgl-project/sglang/pull/26651)
  Fix DRAFT_EXTEND_V2 CG metadata: align test fixture and Triton with production seq_lens convention (#26651)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_extend_runner.py`, `test/registered/attention/unittests/KNOWN_FAILURES.md`, `test/registered/attention/unittests/dense/README.md` _+2 more__
- **2026-05-29** [`9062f583db`](https://github.com/sgl-project/sglang/commit/9062f583db) [#25463](https://github.com/sgl-project/sglang/pull/25463)
  [ROCm] Eliminate redundant contiguous copy in MLA attention on ROCm MXFP4 (#25463)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-05-29** [`6e9bd82714`](https://github.com/sgl-project/sglang/commit/6e9bd82714) [#26662](https://github.com/sgl-project/sglang/pull/26662)
  [AMD][CI] Update v4 CI setting and move the task to main branch (#26662)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `test/registered/amd/test_deepseek_v4_flash_fp4.py`, `test/registered/amd/test_deepseek_v4_flash_fp8.py`, `test/registered/amd/test_deepseek_v4_pro_fp4.py` _+1 more__
- **2026-05-29** [`b2eed9e16d`](https://github.com/sgl-project/sglang/commit/b2eed9e16d) [#22868](https://github.com/sgl-project/sglang/pull/22868)
  [Apple Silicon] Add custom Metal RoPE kernel with fused KV cache store (#22868)
  _Files: `docs_new/docs/hardware-platforms/apple_metal.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/mlx/aot.py`, `python/sglang/srt/hardware_backend/mlx/kv_cache/attention_wrapper.py` _+8 more__
- **2026-05-29** [`0fb0ea7aac`](https://github.com/sgl-project/sglang/commit/0fb0ea7aac) [#26669](https://github.com/sgl-project/sglang/pull/26669)
  test: add trtllm_mha EAGLE-draft CG runner coverage (chain) (#26669)
  _Files: `test/registered/attention/unittests/KNOWN_FAILURES.md`, `test/registered/attention/unittests/dense/README.md`, `test/registered/attention/unittests/dense/test_trtllm_mha.py`_
- **2026-05-29** [`2dfbc3d781`](https://github.com/sgl-project/sglang/commit/2dfbc3d781) [#26658](https://github.com/sgl-project/sglang/pull/26658)
  test: strengthen CG-replay coverage with prod-fill padding, metadata invariants, and pad-ratio sweep (#26658)
  _Files: `python/sglang/test/kits/attention_unittest/runner_modes/cuda_graph_decode_runner.py`, `python/sglang/test/kits/attention_unittest/runner_modes/metadata_invariants.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_cuda_graph_runner.py`, `python/sglang/test/kits/attention_unittest/runner_modes/speculative_draft_extend_runner.py` _+4 more__
- **2026-05-29** [`f16816f043`](https://github.com/sgl-project/sglang/commit/f16816f043) [#26521](https://github.com/sgl-project/sglang/pull/26521)
  fix: copy seq_lens in TRTLLM MHA draft decode cuda graph capture (#26521)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-05-29** [`40f91e6697`](https://github.com/sgl-project/sglang/commit/40f91e6697) [#24654](https://github.com/sgl-project/sglang/pull/24654)
  [Bugfix] [DSA] [Hisparse] Broadcast TP Rank 0 Topk Indexes to other TPs (#24654)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-05-29** [`84698b21e7`](https://github.com/sgl-project/sglang/commit/84698b21e7) [#26654](https://github.com/sgl-project/sglang/pull/26654)
  rename unittest as unittests (#26654)
  _Files: `test/registered/attention/unittests/KNOWN_FAILURES.md`, `test/registered/attention/unittests/__init__.py`, `test/registered/attention/unittests/conftest.py`, `test/registered/attention/unittests/dense/README.md` _+46 more__
- **2026-05-29** [`dc4e7bc479`](https://github.com/sgl-project/sglang/commit/dc4e7bc479) [#26655](https://github.com/sgl-project/sglang/pull/26655)
  Fix TRTLLM MHA draft decode cache seqlens replay (#26655)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-05-29** [`b1173c8c14`](https://github.com/sgl-project/sglang/commit/b1173c8c14) [#24582](https://github.com/sgl-project/sglang/pull/24582)
  [NPU] Enhance accuracy for model Step3_5 from 0 to 88% (#24582)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`, `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-05-29** [`e381312664`](https://github.com/sgl-project/sglang/commit/e381312664) [#26628](https://github.com/sgl-project/sglang/pull/26628)
  Revert "Fix FA DRAFT_EXTEND_V2 cache extent" (#26628)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `test/registered/attention/unittest/KNOWN_FAILURES.md`, `test/registered/attention/unittest/dense/README.md`, `test/registered/attention/unittest/dense/test_fa3.py` _+1 more__
- **2026-05-29** [`6258947039`](https://github.com/sgl-project/sglang/commit/6258947039) [#26353](https://github.com/sgl-project/sglang/pull/26353)
  NPU Nightly Pipeline Skip Test Case Adaptation and Recovery Testing (#26353)
  _Files: `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py`, `test/registered/ascend/basic_function/memory_and_scheduling/test_npu_no_chunked_prefill.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py` _+13 more__
- **2026-05-29** [`a8cfae0b30`](https://github.com/sgl-project/sglang/commit/a8cfae0b30) [#26625](https://github.com/sgl-project/sglang/pull/26625)
  doc: update step-3.7-flash docker image tag (#26625)
  _Files: `docs_new/cookbook/autoregressive/StepFun/Step-3.7-Flash.mdx`_
- **2026-05-29** [`f66f56c6bd`](https://github.com/sgl-project/sglang/commit/f66f56c6bd) [#26517](https://github.com/sgl-project/sglang/pull/26517)
  Add attention-backend unit-test suite under test/registered/attention/unittest (#26517)
  _Files: `python/sglang/test/kits/attention_unittest/__init__.py`, `python/sglang/test/kits/attention_unittest/attention_methods/__init__.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dense_attention.py`, `python/sglang/test/kits/attention_unittest/attention_methods/dsa_attention.py` _+65 more__
- **2026-05-28** [`ec78fa6518`](https://github.com/sgl-project/sglang/commit/ec78fa6518) [#26610](https://github.com/sgl-project/sglang/pull/26610)
  test/registered: cleanup pure model e2e tests (moves, splits, dedup, kit) (#26610)
  _Files: `python/sglang/test/kits/unified_radix_cache_kit.py`, `test/manual/core/test_dsv4_hicache_swa_translation_cache.py`, `test/registered/4-gpu-models/test_qwen35_models.py`, `test/registered/8-gpu-models/test_deepseek_v3_mtp.py` _+22 more__
- **2026-05-28** [`93445e6359`](https://github.com/sgl-project/sglang/commit/93445e6359) [#26506](https://github.com/sgl-project/sglang/pull/26506)
  [spec decoding] support kimi-k2.6-eagle3.1-mla draft (#26506)
  _Files: `python/sglang/srt/models/kimi_k25_eagle3.py`_
- **2026-05-28** [`690d4cdd94`](https://github.com/sgl-project/sglang/commit/690d4cdd94) [#26532](https://github.com/sgl-project/sglang/pull/26532)
  Revert "[CI] FA3: ascending cuda-graph capture to avoid varlen workspace IMA (#26532) (#26550)" (#26600)
  _Files: `python/sglang/srt/model_executor/cuda_graph_runner.py`_
- **2026-05-28** [`d616b8edad`](https://github.com/sgl-project/sglang/commit/d616b8edad) [#26318](https://github.com/sgl-project/sglang/pull/26318)
  [diffusion][jit_kernel] perf: varlen FA fast path for USPAttention masked branch (#26318)
  _Files: `python/sglang/jit_kernel/diffusion/triton/varlen_pack_pad.py`, `python/sglang/jit_kernel/tests/diffusion/test_varlen_pack_pad.py`, `python/sglang/jit_kernel/tests/diffusion/test_varlen_uspattn_equivalence.py`, `python/sglang/multimodal_gen/runtime/layers/attention/__init__.py` _+2 more__
- **2026-05-28** [`12e28bdf0c`](https://github.com/sgl-project/sglang/commit/12e28bdf0c) [#26513](https://github.com/sgl-project/sglang/pull/26513)
  Fix FlashInfer SWA EXTEND-with-prefix correctness in merge_state path (#26513)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`_
- **2026-05-28** [`00cd6fb3d9`](https://github.com/sgl-project/sglang/commit/00cd6fb3d9) [#26516](https://github.com/sgl-project/sglang/pull/26516)
  Add sliding-window mask support to TorchNativeAttnBackend (#26516)
  _Files: `python/sglang/srt/layers/attention/torch_native_backend.py`_
- **2026-05-28** [`8ca09a30f1`](https://github.com/sgl-project/sglang/commit/8ca09a30f1) [#26515](https://github.com/sgl-project/sglang/pull/26515)
  Allow Optional key/value in unified_attention_with_output split-op (MLA absorb fix) (#26515)
  _Files: `python/sglang/srt/layers/radix_attention.py`_
- **2026-05-28** [`b429a30428`](https://github.com/sgl-project/sglang/commit/b429a30428) [#26514](https://github.com/sgl-project/sglang/pull/26514)
  Expose Flex attention causal/decode masks as static methods (#26514)
  _Files: `python/sglang/srt/layers/attention/torch_flex_backend.py`_
- **2026-05-28** [`e5f5d84780`](https://github.com/sgl-project/sglang/commit/e5f5d84780) [#26512](https://github.com/sgl-project/sglang/pull/26512)
  Fix FA DRAFT_EXTEND_V2 cache extent (#26512)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-05-28** [`770c51b127`](https://github.com/sgl-project/sglang/commit/770c51b127) [#26412](https://github.com/sgl-project/sglang/pull/26412)
  [Bug] Forward fixed_split_size in SWA / cross-attention paths of FlashInfer backend (#26412)
  _Files: `python/sglang/srt/layers/attention/flashinfer_backend.py`_
- **2026-05-28** [`8dca6291c7`](https://github.com/sgl-project/sglang/commit/8dca6291c7) [#26532](https://github.com/sgl-project/sglang/pull/26532)
  [CI] FA3: ascending cuda-graph capture to avoid varlen workspace IMA (#26532) (#26550)
  _Files: `python/sglang/srt/model_executor/cuda_graph_runner.py`_
- **2026-05-28** [`50e0b3b77f`](https://github.com/sgl-project/sglang/commit/50e0b3b77f) [#24737](https://github.com/sgl-project/sglang/pull/24737)
  Support Flashinfer Cute-DSL MLA attention (#24737)
  _Files: `docs_new/docs/advanced_features/attention_backend.mdx`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/model_executor/model_runner.py` _+4 more__
- **2026-05-28** [`e31ea50df8`](https://github.com/sgl-project/sglang/commit/e31ea50df8) [#26494](https://github.com/sgl-project/sglang/pull/26494)
  Remove DeepGEMM for indexer GEMM in piecewise NSA path (#26494)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-05-28** [`97dd6aad60`](https://github.com/sgl-project/sglang/commit/97dd6aad60) [#26193](https://github.com/sgl-project/sglang/pull/26193)
  Add a little env var for disabling Flashinfer autotune cache (#26193)
  _Files: `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-28** [`421bda6d85`](https://github.com/sgl-project/sglang/commit/421bda6d85) [#26470](https://github.com/sgl-project/sglang/pull/26470)
  [Bug Fix] Remove H20 device check for FlashInfer AllReduce Fusion (#26470)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-05-27** [`deaba74745`](https://github.com/sgl-project/sglang/commit/deaba74745) [#26383](https://github.com/sgl-project/sglang/pull/26383)
  [AMD][DSV4] DSV4 MTP graph + sparse triton attn optimizations (#26383)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_fused.py`, `python/sglang/srt/layers/attention/nsa/triton_decode/triton_mla_kernels_decode_optimized.py` _+6 more__
- **2026-05-27** [`e06058ed62`](https://github.com/sgl-project/sglang/commit/e06058ed62) [#26499](https://github.com/sgl-project/sglang/pull/26499)
  [Kernel] Import flash_mla kernels from sglang kernel for deepseek v4 (#26499)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/hip_flash_mla.py`_
- **2026-05-27** [`ddf0627254`](https://github.com/sgl-project/sglang/commit/ddf0627254) [#22921](https://github.com/sgl-project/sglang/pull/22921)
  [NVIDIA] [GDN] Add FlashInfer prefill support for SM100+ (Blackwell) (#22921)
  _Files: `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/server_args.py`, `test/manual/4-gpu-models/test_qwen35_fp4_triton.py`, `test/registered/4-gpu-models/test_qwen35_fp4_flashinfer.py`_
- **2026-05-27** [`737c6cd6d1`](https://github.com/sgl-project/sglang/commit/737c6cd6d1) [#25405](https://github.com/sgl-project/sglang/pull/25405)
  [XPU] Add registry mechanism for XPU CI tests (#25405)
  _Files: `.github/workflows/pr-test-xpu.yml`, `python/sglang/test/ci/ci_register.py`, `test/registered/attention/test_chunk_gated_delta_rule.py`, `test/registered/xpu/test_deepseek_ocr.py` _+5 more__
- **2026-05-27** [`c317beda99`](https://github.com/sgl-project/sglang/commit/c317beda99) [#24994](https://github.com/sgl-project/sglang/pull/24994)
  [diffusion] model: support a new model (#24994)
  _Files: `docs/diffusion/compatibility_matrix.md`, `docs/diffusion/index.md`, `python/sglang/multimodal_gen/configs/models/dits/__init__.py`, `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py` _+15 more__
- **2026-05-26** [`b66f8e0b96`](https://github.com/sgl-project/sglang/commit/b66f8e0b96) [#26132](https://github.com/sgl-project/sglang/pull/26132)
  Sgl flashmla (#26132)
  _Files: `sgl-kernel/cmake/flashmla.cmake`, `sgl-kernel/csrc/flashmla_extension.cc`, `sgl-kernel/include/sgl_kernel_ops.h`, `sgl-kernel/python/sgl_kernel/flash_mla.py`_
- **2026-05-26** [`ec6f8d61f7`](https://github.com/sgl-project/sglang/commit/ec6f8d61f7) [#26335](https://github.com/sgl-project/sglang/pull/26335)
  [Spec] Async-assert probes across EAGLE/MTP; zero `tgt_cache_loc` (#26335)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/sampler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/server_args.py` _+19 more__
- **2026-05-26** [`d34d4d9f5f`](https://github.com/sgl-project/sglang/commit/d34d4d9f5f) [#26200](https://github.com/sgl-project/sglang/pull/26200)
  [GDN] Support SM100 CuTeDSL GDN Prefill Kernel (#26200)
  _Files: `benchmark/bench_linear_attention/bench_gdn_prefill_cutedsl.py`, `python/sglang/srt/layers/attention/cute_utils/__init__.py`, `python/sglang/srt/layers/attention/cute_utils/_tcgen05.py`, `python/sglang/srt/layers/attention/cute_utils/cvt.py` _+7 more__
- **2026-05-26** [`7c0fbc8c2e`](https://github.com/sgl-project/sglang/commit/7c0fbc8c2e) [#25045](https://github.com/sgl-project/sglang/pull/25045)
  fix: fix fa3 cross-attention batched-decode for per-request varlen encoder (#25045)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`_
- **2026-05-26** [`156d1af23a`](https://github.com/sgl-project/sglang/commit/156d1af23a) [#23757](https://github.com/sgl-project/sglang/pull/23757)
  [Intel GPU] Fix incorrect KV-cache page table for local attention when page_size > 1 (#23757)
  _Files: `python/sglang/srt/layers/attention/xpu_backend.py`_
- **2026-05-25** [`2b9dd9c8b3`](https://github.com/sgl-project/sglang/commit/2b9dd9c8b3) [#22851](https://github.com/sgl-project/sglang/pull/22851)
  [FlashInfer v0.6.10] [RL] [DSv32] [GLM-5] Add `--dsa-topk-backend` and integrate FlashInfer and pytorch topk (#22851)
  _Files: `docs/advanced_features/server_arguments.md`, `docs/references/environment_variables.md`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/references/environment_variables.mdx` _+5 more__
- **2026-05-25** [`533ef41112`](https://github.com/sgl-project/sglang/commit/533ef41112) [#25523](https://github.com/sgl-project/sglang/pull/25523)
  [Diffusion] Default NVFP4 backend to FlashInfer TRTLLM (#25523)
  _Files: `docs/diffusion/environment_variables.md`, `docs/diffusion/quantization.md`, `docs_new/docs/sglang-diffusion/environment_variables.mdx`, `docs_new/docs/sglang-diffusion/quantization.mdx` _+7 more__
- **2026-05-25** [`c05756da7a`](https://github.com/sgl-project/sglang/commit/c05756da7a) [#26197](https://github.com/sgl-project/sglang/pull/26197)
  [SRT] fix flashInfer allreduce fusion not used on blackwell (#26197)
  _Files: `python/sglang/srt/layers/flashinfer_comm_fusion.py`_
- **2026-05-25** [`2bd3ac0b5d`](https://github.com/sgl-project/sglang/commit/2bd3ac0b5d) [#26065](https://github.com/sgl-project/sglang/pull/26065)
  [XPU] fix correctness issue of GDN triton kernel for XPU (#26065)
  _Files: `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_delta_h.py`, `python/sglang/srt/hardware_backend/xpu/kernels/fla/chunk_fwd.py`, `test/registered/attention/test_chunk_gated_delta_rule.py`_
- **2026-05-25** [`ec6fcb93cb`](https://github.com/sgl-project/sglang/commit/ec6fcb93cb) [#26241](https://github.com/sgl-project/sglang/pull/26241)
  [perf][spec decoding] Skip common_template in TRTLLMMLAMultiStepDraftBackend init (#26241)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-05-25** [`ed179bf9b2`](https://github.com/sgl-project/sglang/commit/ed179bf9b2) [#26239](https://github.com/sgl-project/sglang/pull/26239)
  [dsv4] fix multi-step draft on non-cuda-graph path (#26239)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_

## Prefill / Decode Disaggregation  (35 commits)

- **2026-06-01** [`931765e23e`](https://github.com/sgl-project/sglang/commit/931765e23e) [#26607](https://github.com/sgl-project/sglang/pull/26607)
  Do not cap DeepSeek V4 PD prefill by SWA pool size (#26607)
  _Files: `python/sglang/srt/disaggregation/prefill.py`_
- **2026-06-01** [`2394dede0e`](https://github.com/sgl-project/sglang/commit/2394dede0e) [#25669](https://github.com/sgl-project/sglang/pull/25669)
  [EPD][Perf] Async image preprocessing and cross-request ViT batching for encode_server (#25669)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`_
- **2026-06-01** [`f60710a1d7`](https://github.com/sgl-project/sglang/commit/f60710a1d7) [#26905](https://github.com/sgl-project/sglang/pull/26905)
  [AMD] Fix stage-b-test-large-8-gpu-mi35x-disaggregation-amd : switch CACHE_HOST to a fresh path to fix "No space left on device" (#26905)
  _Files: `scripts/ci/amd/amd_ci_start_container_disagg.sh`_
- **2026-05-31** [`373cadc92e`](https://github.com/sgl-project/sglang/commit/373cadc92e) [#26569](https://github.com/sgl-project/sglang/pull/26569)
  [bugfix] mooncake store double-tag bug fix (#26569)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`_
- **2026-05-31** [`972fbf7711`](https://github.com/sgl-project/sglang/commit/972fbf7711) [#26838](https://github.com/sgl-project/sglang/pull/26838)
  Skip flaky mamba extra_buffer disagg test (#26838)
  _Files: `test/registered/disaggregation/test_disaggregation_hybrid_attention.py`_
- **2026-05-31** [`ae9db7ff4b`](https://github.com/sgl-project/sglang/commit/ae9db7ff4b) [#26819](https://github.com/sgl-project/sglang/pull/26819)
  Add the KV-canary perturb modes and PD-disaggregation e2e tests (#26819)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/perturb/config.py`, `python/sglang/srt/kv_canary/perturb/manager.py`, `python/sglang/srt/kv_canary/perturb/real_kv_post_forward.py` _+16 more__
- **2026-05-31** [`27eb139ef7`](https://github.com/sgl-project/sglang/commit/27eb139ef7) [#26811](https://github.com/sgl-project/sglang/pull/26811)
  Add the KV-canary mock-model end-to-end test harness (#26811)
  _Files: `python/sglang/test/mock_model/__init__.py`, `python/sglang/test/mock_model/perturb_e2e_base.py`, `python/sglang/test/mock_model/utils.py`, `python/sglang/test/server_fixtures/disaggregation_fixture.py` _+3 more__
- **2026-05-30** [`282c46133f`](https://github.com/sgl-project/sglang/commit/282c46133f) [#25945](https://github.com/sgl-project/sglang/pull/25945)
  [Scheduler] Defer prefill input_ids H2D to forward stream, unify resolve via future_map (#25945)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-05-30** [`3b61a1f935`](https://github.com/sgl-project/sglang/commit/3b61a1f935) [#26707](https://github.com/sgl-project/sglang/pull/26707)
  [Bugfix] Optimize metadata allocation and transfer for mooncake intraNode NVLink (#26707)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/utils.py`_
- **2026-05-29** [`544f3039d5`](https://github.com/sgl-project/sglang/commit/544f3039d5) [#26114](https://github.com/sgl-project/sglang/pull/26114)
  [PD] Fix IB device validation for JSON mappings (#26114)
  _Files: `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`, `test/registered/cpu/test_server_args_backend.py`_
- **2026-05-29** [`5601b7139d`](https://github.com/sgl-project/sglang/commit/5601b7139d) [#26646](https://github.com/sgl-project/sglang/pull/26646)
  [core] Make overlap-schedule WAR barrier CUDA-only (#26646)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-05-29** [`4d1163e6a9`](https://github.com/sgl-project/sglang/commit/4d1163e6a9) [#26539](https://github.com/sgl-project/sglang/pull/26539)
  [PD][MoRI] Align hybrid state transfer with per-component schema (#26539)
  _Files: `python/sglang/srt/disaggregation/mori/conn.py`, `test/registered/amd/disaggregation/test_mori_transfer_engine_e2e.py`_
- **2026-05-29** [`a42a7654a2`](https://github.com/sgl-project/sglang/commit/a42a7654a2) [#25880](https://github.com/sgl-project/sglang/pull/25880)
  Update MooncakeStore batch tests to use v1 APIs (#25880)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/test_mooncake_store.py`_
- **2026-05-29** [`5850aa14c3`](https://github.com/sgl-project/sglang/commit/5850aa14c3) [#25083](https://github.com/sgl-project/sglang/pull/25083)
  fix(mooncake): honour MOONCAKE_PROTOCOL so EFA hardware can select efa transport (#25083)
  _Files: `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-29** [`73c99e3361`](https://github.com/sgl-project/sglang/commit/73c99e3361) [#25959](https://github.com/sgl-project/sglang/pull/25959)
  Ensure multi-node MM embedding cache consistency in insert_batch (#25959)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/embedding_cache_controller.py`_
- **2026-05-29** [`36d0a6e08e`](https://github.com/sgl-project/sglang/commit/36d0a6e08e) [#22587](https://github.com/sgl-project/sglang/pull/22587)
  [EPD] Optimize the Mooncake backend (#22587)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/io_struct.py` _+7 more__
- **2026-05-28** [`407106300e`](https://github.com/sgl-project/sglang/commit/407106300e) [#26617](https://github.com/sgl-project/sglang/pull/26617)
  test/disaggregation: dp-attention keeps total_tokens e2e, simpler LB algos -> unit tests (#26617)
  _Files: `test/registered/disaggregation/test_disaggregation_dp_attention.py`, `test/registered/unit/managers/test_data_parallel_controller.py`, `test/registered/unit/managers/test_dp_budget.py`_
- **2026-05-28** [`435c4ffb30`](https://github.com/sgl-project/sglang/commit/435c4ffb30) [#26609](https://github.com/sgl-project/sglang/pull/26609)
  [CI] Clean DeepSeek V4 tests and installation scripts (#26609)
  _Files: `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`, `docker/Dockerfile`, `scripts/ci/cuda/ci_install_deepep.sh` _+9 more__
- **2026-05-28** [`8ff66b707f`](https://github.com/sgl-project/sglang/commit/8ff66b707f) [#26487](https://github.com/sgl-project/sglang/pull/26487)
  feat: convert mm_hashes to str in encode_server for Mooncake key compat (#26487)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`_
- **2026-05-28** [`b437a0d066`](https://github.com/sgl-project/sglang/commit/b437a0d066) [#25973](https://github.com/sgl-project/sglang/pull/25973)
  Fix PD decode radix cache double-counting cached_tokens (#25973)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/test/kits/cache_hit_kit.py`_
- **2026-05-27** [`d6e1692410`](https://github.com/sgl-project/sglang/commit/d6e1692410) [#26195](https://github.com/sgl-project/sglang/pull/26195)
  Allow custom speculative algorithm to support disaggregation (#26195)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/speculative/eagle_disaggregation.py`, `python/sglang/srt/speculative/spec_info.py`, `python/sglang/srt/speculative/spec_registry.py`_
- **2026-05-27** [`163b970127`](https://github.com/sgl-project/sglang/commit/163b970127) [#26380](https://github.com/sgl-project/sglang/pull/26380)
  [core] WAR barrier for overlap schedule buffer writes, without fwd occupancy cost (#26380)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py` _+1 more__
- **2026-05-27** [`d45ee3f6c5`](https://github.com/sgl-project/sglang/commit/d45ee3f6c5) [#25278](https://github.com/sgl-project/sglang/pull/25278)
  [HiCache] fix: Mooncake Dummy Client mode for hybrid Mamba models (#25278)
  _Files: `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`, `test/registered/unit/mem_cache/test_mooncake_standalone_dummy_mamba.py`_
- **2026-05-27** [`1051a8456f`](https://github.com/sgl-project/sglang/commit/1051a8456f) [#26425](https://github.com/sgl-project/sglang/pull/26425)
  [core] Maintain `req_pool_indices_cpu` host mirror (like `seq_lens_cpu`) (#26425)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/hisparse_coordinator.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/common.py`_
- **2026-05-27** [`6076066e38`](https://github.com/sgl-project/sglang/commit/6076066e38) [#26346](https://github.com/sgl-project/sglang/pull/26346)
  Add mooncake_tcp transfer backend (mooncake over TCP) (#26346)
  _Files: `python/sglang/srt/arg_groups/pd_disaggregation_hook.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/server_args.py`_
- **2026-05-26** [`c47f0e7cdd`](https://github.com/sgl-project/sglang/commit/c47f0e7cdd) [#26299](https://github.com/sgl-project/sglang/pull/26299)
  [PD] Fix top logprobs crash in prefill path (#26299)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `test/registered/disaggregation/test_disaggregation_basic.py`_
- **2026-05-26** [`c8c1aed5e9`](https://github.com/sgl-project/sglang/commit/c8c1aed5e9) [#26394](https://github.com/sgl-project/sglang/pull/26394)
  [PD] Fix cross-rank queue divergence by gating metadata readiness before all-reduce (#26394)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/utils.py`_
- **2026-05-26** [`e958f4561f`](https://github.com/sgl-project/sglang/commit/e958f4561f) [#15829](https://github.com/sgl-project/sglang/pull/15829)
  [feat] Support `extra_buffer` in Mamba2-based models (#15829)
  _Files: `docs/advanced_features/server_arguments.md`, `python/sglang/srt/arg_groups/nemotron_h_hook.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/mamba/mamba.py` _+13 more__
- **2026-05-26** [`dabdd91ef3`](https://github.com/sgl-project/sglang/commit/dabdd91ef3) [#25964](https://github.com/sgl-project/sglang/pull/25964)
  [EPD] Cross-request batching for image/audio encoder (#25964)
  _Files: `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`_
- **2026-05-25** [`8805f4cf16`](https://github.com/sgl-project/sglang/commit/8805f4cf16) [#26298](https://github.com/sgl-project/sglang/pull/26298)
  Fail-fast on PD subprocess exit and scheduler exception (#26298)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/test/server_fixtures/disaggregation_fixture.py`, `python/sglang/test/test_utils.py`_
- **2026-05-25** [`2aa6995308`](https://github.com/sgl-project/sglang/commit/2aa6995308) [#26281](https://github.com/sgl-project/sglang/pull/26281)
  [CI] Enable EPD CI for EPD architecture enhancements (#26281)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `test/registered/disaggregation/test_epd_disaggregation.py`_
- **2026-05-25** [`0801cc05ed`](https://github.com/sgl-project/sglang/commit/0801cc05ed) [#25895](https://github.com/sgl-project/sglang/pull/25895)
  [Diffusion][NPU] Disaggregation diffusion stages support for NPU (#25895)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/diffusion/disaggregation.mdx`, `python/sglang/multimodal_gen/runtime/disaggregation/scheduler_mixin.py`, `python/sglang/multimodal_gen/runtime/disaggregation/transport/buffer.py`, `python/sglang/multimodal_gen/runtime/disaggregation/transport/codec.py` _+1 more__
- **2026-05-25** [`bc8d64bf36`](https://github.com/sgl-project/sglang/commit/bc8d64bf36) [#26268](https://github.com/sgl-project/sglang/pull/26268)
  [CI] Align score threshold in dsv4 disaggregation test (#26268)
  _Files: `test/registered/disaggregation/test_disaggregation_dsv4.py`_
- **2026-05-25** [`7f2829af39`](https://github.com/sgl-project/sglang/commit/7f2829af39) [#25989](https://github.com/sgl-project/sglang/pull/25989)
  chore: bump mooncake version to 0.3.11.post1 (#25989)
  _Files: `docker/Dockerfile`, `python/sglang/srt/elastic_ep/elastic_ep.py`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-05-25** [`d7e3e54148`](https://github.com/sgl-project/sglang/commit/d7e3e54148) [#26240](https://github.com/sgl-project/sglang/pull/26240)
  [Test] split test/registered/distributed/ into topic folders (#26240)
  _Files: `test/registered/backends/test_flashinfer_fusion_preflight.py`, `test/registered/disaggregation/test_disaggregation_aarch64.py`, `test/registered/disaggregation/test_disaggregation_decode_radix_cache.py`, `test/registered/disaggregation/test_disaggregation_different_tp.py` _+12 more__

## MoE / Expert Parallel  (31 commits)

- **2026-06-01** [`ff642ed936`](https://github.com/sgl-project/sglang/commit/ff642ed936) [#26303](https://github.com/sgl-project/sglang/pull/26303)
  [MoE] Extend kimi_k2_moe_fused_gate to support 256 experts (MiMo V2 Flash) (#26303)
  _Files: `sgl-kernel/csrc/moe/kimi_k2_moe_fused_gate.cu`, `sgl-kernel/tests/test_kimi_k2_moe_fused_gate.py`_
- **2026-06-01** [`1d7e2f6fb8`](https://github.com/sgl-project/sglang/commit/1d7e2f6fb8) [#22972](https://github.com/sgl-project/sglang/pull/22972)
  [NPU] fix normal DeepEP mode num_tokens_per_rdma_rank error caused by none (#22972)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`_
- **2026-06-01** [`a779791b3f`](https://github.com/sgl-project/sglang/commit/a779791b3f) [#26862](https://github.com/sgl-project/sglang/pull/26862)
  Add random-ids dataset, round-robin expert simulation, and kill_process_tree logging (#26862)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/utils/common.py`, `python/sglang/test/bench_one_batch_server_internal.py`_
- **2026-05-30** [`b421e60eed`](https://github.com/sgl-project/sglang/commit/b421e60eed) [#26389](https://github.com/sgl-project/sglang/pull/26389)
  【NPU】【bugfix】fix server error when mtp unquant (#26389)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`, `python/sglang/srt/models/deepseek_nextn.py`, `python/sglang/srt/models/qwen3_5_mtp.py`, `python/sglang/srt/models/qwen3_next_mtp.py` _+1 more__
- **2026-05-30** [`714bcd84e2`](https://github.com/sgl-project/sglang/commit/714bcd84e2) [#23996](https://github.com/sgl-project/sglang/pull/23996)
  [parallel] Support moe_dense_tp_size == attn_tp_size to share the attention TP group (#23996)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py`_
- **2026-05-30** [`0d9a2a9de3`](https://github.com/sgl-project/sglang/commit/0d9a2a9de3) [#26489](https://github.com/sgl-project/sglang/pull/26489)
  [MoE Refactor] Migrate SM90 Cutlass W4A16 to MoeRunner (#26489)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_mxfp4.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/layers/quantization/mxfp4_flashinfer_cutlass_moe.py` _+1 more__
- **2026-05-30** [`c93a559e5a`](https://github.com/sgl-project/sglang/commit/c93a559e5a) [#26710](https://github.com/sgl-project/sglang/pull/26710)
  Fix MoE LoRA wrapper exposing moe_runner_config (#26710)
  _Files: `python/sglang/srt/lora/layers.py`_
- **2026-05-30** [`716e670d3d`](https://github.com/sgl-project/sglang/commit/716e670d3d) [#26696](https://github.com/sgl-project/sglang/pull/26696)
  [bugfix]: size CuteDSL MoE allgather buffers for the worst-case forward (#26696)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/server_args/test_server_args.py`_
- **2026-05-29** [`cf66693b35`](https://github.com/sgl-project/sglang/commit/cf66693b35) [#26468](https://github.com/sgl-project/sglang/pull/26468)
  [Model] Add Qwen3-MoE MTP (#26468)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/models/qwen3_moe.py`, `python/sglang/srt/models/qwen3_moe_mtp.py`, `python/sglang/srt/speculative/eagle_worker.py` _+1 more__
- **2026-05-29** [`4585f8eb95`](https://github.com/sgl-project/sglang/commit/4585f8eb95) [#26673](https://github.com/sgl-project/sglang/pull/26673)
  [refactor] remove unused op_mlp (#26673)
  _Files: `python/sglang/srt/models/deepseek_v2.py`, `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/mimo_v2.py` _+2 more__
- **2026-05-29** [`3ecf2c76ad`](https://github.com/sgl-project/sglang/commit/3ecf2c76ad) [#16775](https://github.com/sgl-project/sglang/pull/16775)
  [CPU] Add GPT-OSS model optimization for CPU (#16775)
  _Files: `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/quantization/__init__.py` _+31 more__
- **2026-05-29** [`08ec19872c`](https://github.com/sgl-project/sglang/commit/08ec19872c) [#26474](https://github.com/sgl-project/sglang/pull/26474)
  [HotFix][Ling 2.6] Fix HybridLinearAttn dispatcher for Ling-2.6 (#26474)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/models/bailing_moe_linear.py`, `test/registered/8-gpu-models/test_ling_2_6_flash.py`_
- **2026-05-29** [`54b06f199c`](https://github.com/sgl-project/sglang/commit/54b06f199c) [#24160](https://github.com/sgl-project/sglang/pull/24160)
  [lora] Share MoE LoRA Info (#24160)
  _Files: `python/sglang/srt/lora/backend/ascend_backend.py`, `python/sglang/srt/lora/backend/base_backend.py`, `python/sglang/srt/lora/backend/chunked_backend.py`, `python/sglang/srt/lora/backend/torch_backend.py` _+5 more__
- **2026-05-29** [`3bdea78ad1`](https://github.com/sgl-project/sglang/commit/3bdea78ad1) [#26565](https://github.com/sgl-project/sglang/pull/26565)
  model: support Step-3.7-Flash (#26565)
  _Files: `docs_new/cookbook/autoregressive/StepFun/Step-3.7-Flash.mdx`, `docs_new/cookbook/autoregressive/StepFun/Step3.5.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/autoregressive/step-37-flash-deployment.jsx` _+13 more__
- **2026-05-28** [`e33bbbb467`](https://github.com/sgl-project/sglang/commit/e33bbbb467) [#26402](https://github.com/sgl-project/sglang/pull/26402)
  [5/N] Quantization Refactor: GPTQ schemes and kernel split (#26402)
  _Files: `python/sglang/srt/hardware_backend/gpu/quantization/gptq_kernels.py`, `python/sglang/srt/hardware_backend/npu/quantization/gptq_kernels.py`, `python/sglang/srt/layers/quantization/__init__.py`, `python/sglang/srt/layers/quantization/auto_round.py` _+8 more__
- **2026-05-28** [`b4808d44da`](https://github.com/sgl-project/sglang/commit/b4808d44da) [#25486](https://github.com/sgl-project/sglang/pull/25486)
  Use Cute-DSL MXFP8 quantize kernels (#25486)
  _Files: `python/sglang/srt/layers/quantization/mxfp4_flashinfer_trtllm_moe.py`_
- **2026-05-28** [`714fdd9723`](https://github.com/sgl-project/sglang/commit/714fdd9723) [#25061](https://github.com/sgl-project/sglang/pull/25061)
  Fix MiniMax-M2.7 on CPU (#25061)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/models/minimax_m2.py`, `sgl-kernel/csrc/cpu/moe.cpp`_
- **2026-05-27** [`19663aafcd`](https://github.com/sgl-project/sglang/commit/19663aafcd) [#23269](https://github.com/sgl-project/sglang/pull/23269)
  Support batch size > 1 when enable CP (#23269)
  _Files: `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`, `python/sglang/srt/layers/attention/dsa/utils.py`, `python/sglang/srt/layers/utils/cp_utils.py`, `python/sglang/srt/managers/schedule_policy.py` _+9 more__
- **2026-05-27** [`d9d719b270`](https://github.com/sgl-project/sglang/commit/d9d719b270) [#26309](https://github.com/sgl-project/sglang/pull/26309)
  [npu] [bugfix] Add contiguous operation during quantized weight loading. (#26309)
  _Files: `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`_
- **2026-05-27** [`51840ca459`](https://github.com/sgl-project/sglang/commit/51840ca459) [#26479](https://github.com/sgl-project/sglang/pull/26479)
  Add xutizhou as code owner for eplb directory (#26479)
  _Files: `.github/CODEOWNERS`_
- **2026-05-27** [`dea85c30f4`](https://github.com/sgl-project/sglang/commit/dea85c30f4) [#23837](https://github.com/sgl-project/sglang/pull/23837)
  Add Ling_2_6 (#23837)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/layers/attention/linear/lightning_backend.py`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=256,N=512,device_name=NVIDIA_H20-3e.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=256,N=512,device_name=NVIDIA_H20-3e_down.json` _+8 more__
- **2026-05-27** [`87c3171aaa`](https://github.com/sgl-project/sglang/commit/87c3171aaa) [#12662](https://github.com/sgl-project/sglang/pull/12662)
  [CPU] Add support for Qwen3-vl and Qwen3-omni (#12662)
  _Files: `python/sglang/srt/layers/amx_utils.py`, `python/sglang/srt/layers/attention/vision.py`, `python/sglang/srt/layers/conv.py`, `python/sglang/srt/layers/logits_processor.py` _+4 more__
- **2026-05-26** [`468c565168`](https://github.com/sgl-project/sglang/commit/468c565168) [#26187](https://github.com/sgl-project/sglang/pull/26187)
  Wire YARN rope_parameters through LFM2 and LFM2-MoE attention (#26187)
  _Files: `python/sglang/srt/models/lfm2.py`, `python/sglang/srt/models/lfm2_moe.py`_
- **2026-05-26** [`2b1e53c98d`](https://github.com/sgl-project/sglang/commit/2b1e53c98d) [#26287](https://github.com/sgl-project/sglang/pull/26287)
  [RL] Fix FP8 skip matching for trailing-dot prefixes (#26287)
  _Files: `python/sglang/srt/layers/quantization/utils.py`, `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`, `test/registered/quant/test_is_layer_skipped.py`_
- **2026-05-26** [`6c8128650e`](https://github.com/sgl-project/sglang/commit/6c8128650e) [#22627](https://github.com/sgl-project/sglang/pull/22627)
  [Bugfix] Fix flashinfer_cutlass MoE crash when intermediate_size_per_partition is not 16-aligned (#22627)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-05-26** [`137168539a`](https://github.com/sgl-project/sglang/commit/137168539a) [#19493](https://github.com/sgl-project/sglang/pull/19493)
  [Perf][Moe]improve cutlass_moe_fp4 performance by using apply_router_weight_on_i… (#19493)
  _Files: `python/sglang/srt/layers/moe/cutlass_moe.py`_
- **2026-05-26** [`3f5e2c7688`](https://github.com/sgl-project/sglang/commit/3f5e2c7688) [#26208](https://github.com/sgl-project/sglang/pull/26208)
  [AMD] Dsv4/pr2 compressor opt (#26208)
  _Files: `docs/diffusion/compatibility_matrix.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/activation.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+27 more__
- **2026-05-26** [`63a89bf1a9`](https://github.com/sgl-project/sglang/commit/63a89bf1a9) [#26112](https://github.com/sgl-project/sglang/pull/26112)
  [kernel] reuse wna16 marlin moe workspace (#26112)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`_
- **2026-05-26** [`7ef06bfc06`](https://github.com/sgl-project/sglang/commit/7ef06bfc06) [#26088](https://github.com/sgl-project/sglang/pull/26088)
  GLM-4.7-Flash: standalone MLA impl and MLA NextN/MTP (#26088)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/model_loader/weight_utils.py`, `python/sglang/srt/models/glm4_moe_lite.py`, `python/sglang/srt/models/glm4_moe_lite_nextn.py`_
- **2026-05-26** [`59cad671e2`](https://github.com/sgl-project/sglang/commit/59cad671e2) [#25391](https://github.com/sgl-project/sglang/pull/25391)
  Support DeepSeek V4 DeepEP Waterfill (#25391)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-25** [`e27d4fb70f`](https://github.com/sgl-project/sglang/commit/e27d4fb70f) [#25775](https://github.com/sgl-project/sglang/pull/25775)
  [Perf][Qwen3.5] Add case 512 to topkGatingSoftmaxKernelLauncher, (#25775)
  _Files: `sgl-kernel/benchmark/bench_moe_topk_softmax.py`, `sgl-kernel/csrc/moe/moe_topk_softmax_kernels.cu`, `sgl-kernel/tests/test_moe_topk_softmax.py`_

## Multimodal  (22 commits)

- **2026-06-01** [`20f47cfe8e`](https://github.com/sgl-project/sglang/commit/20f47cfe8e) [#26895](https://github.com/sgl-project/sglang/pull/26895)
  fix : add sglang script as entry bin for runtime docker image (#26895)
  _Files: `docker/Dockerfile`_
- **2026-06-01** [`53b8378307`](https://github.com/sgl-project/sglang/commit/53b8378307) [#26863](https://github.com/sgl-project/sglang/pull/26863)
  Fix weights_checker checksum for 0-dim tensors and multi-GPU (#26863)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/layers/multimodal.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/managers/mm_utils.py` _+4 more__
- **2026-06-01** [`4b0453f814`](https://github.com/sgl-project/sglang/commit/4b0453f814) [#26530](https://github.com/sgl-project/sglang/pull/26530)
  [diffusion] CI: infer diffusion test sampling params from task type (#26530)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-05-30** [`90eb894564`](https://github.com/sgl-project/sglang/commit/90eb894564) [#26573](https://github.com/sgl-project/sglang/pull/26573)
  [NPU] fix model llava-onevision-qwen2-7b-ov torch compiles error in npu case (#26573)
  _Files: `python/sglang/srt/sampling/penaltylib/repetition_penalty.py`_
- **2026-05-30** [`edfe8d34e8`](https://github.com/sgl-project/sglang/commit/edfe8d34e8) [#26619](https://github.com/sgl-project/sglang/pull/26619)
  [CI] ci-coverage-overview: schedule + manual only, include XPU/MUSA/multimodal_gen (#26619)
  _Files: `.github/workflows/ci-coverage-overview.yml`, `python/sglang/test/ci/ci_register.py`, `scripts/ci/utils/ci_coverage_report.py`_
- **2026-05-29** [`f113ece5cc`](https://github.com/sgl-project/sglang/commit/f113ece5cc) [#25910](https://github.com/sgl-project/sglang/pull/25910)
  Revert "improve: combine vit calls for images from different reqs from one batch (#25910)" (#26442)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-29** [`3e8d8736c8`](https://github.com/sgl-project/sglang/commit/3e8d8736c8) [#26698](https://github.com/sgl-project/sglang/pull/26698)
  fix stage-b-test-2-npu-a2 image (#26698)
  _Files: `.github/workflows/pr-test-npu.yml`_
- **2026-05-29** [`3ea9607d1c`](https://github.com/sgl-project/sglang/commit/3ea9607d1c) [#26492](https://github.com/sgl-project/sglang/pull/26492)
  [diffusion] model: update to new model format (#26492)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/models/dits/cosmos3video.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/cosmos3_guardrails.py`, `python/sglang/multimodal_gen/test/unit/test_cosmos3.py`_
- **2026-05-29** [`0f8104ef15`](https://github.com/sgl-project/sglang/commit/0f8104ef15) [#26257](https://github.com/sgl-project/sglang/pull/26257)
  [XPU] Fix Device Assignment (#26257)
  _Files: `python/sglang/srt/layers/rotary_embedding/base.py`, `python/sglang/srt/models/kimi_vl_moonvit.py`, `python/sglang/srt/models/minicpmo.py`, `python/sglang/srt/models/minicpmv.py` _+2 more__
- **2026-05-28** [`c397a21167`](https://github.com/sgl-project/sglang/commit/c397a21167) [#26146](https://github.com/sgl-project/sglang/pull/26146)
  [Ascend NPU] Enable GLM-4.6V series models inference (#26146)
  _Files: `python/sglang/srt/hardware_backend/npu/modules/glm46v_processor.py`, `python/sglang/srt/multimodal/processors/base_processor.py`_
- **2026-05-28** [`794fdd39ef`](https://github.com/sgl-project/sglang/commit/794fdd39ef) [#25829](https://github.com/sgl-project/sglang/pull/25829)
  fix: adapt dots_vlm for transformers v5 (#25829)
  _Files: `python/sglang/srt/multimodal/processors/dots_vlm.py`_
- **2026-05-27** [`24bcb37efb`](https://github.com/sgl-project/sglang/commit/24bcb37efb) [#26327](https://github.com/sgl-project/sglang/pull/26327)
  [diffusion] fix: fix diffusion LoRA consistency cases (#26327)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/lora_pipeline.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/test_server_common.py` _+2 more__
- **2026-05-27** [`a95b4e2e09`](https://github.com/sgl-project/sglang/commit/a95b4e2e09) [#22848](https://github.com/sgl-project/sglang/pull/22848)
  [Feature] WebSocket streaming audio input for ASR (#22848)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/realtime/__init__.py`, `python/sglang/srt/entrypoints/openai/realtime/handler.py`, `python/sglang/srt/entrypoints/openai/realtime/protocol.py` _+7 more__
- **2026-05-27** [`3afc80d781`](https://github.com/sgl-project/sglang/commit/3afc80d781) [#26311](https://github.com/sgl-project/sglang/pull/26311)
  [diffusion] Fix multi image input for GLM-Image (#26311)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/glm_image.py`_
- **2026-05-27** [`f70e604101`](https://github.com/sgl-project/sglang/commit/f70e604101) [#26247](https://github.com/sgl-project/sglang/pull/26247)
  [diffusion] fix: fix diffusion serve warmup defaults (#26247)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux_finetuned.py`, `python/sglang/multimodal_gen/runtime/entrypoints/cli/serve.py`, `python/sglang/multimodal_gen/runtime/entrypoints/http_server.py` _+12 more__
- **2026-05-26** [`6afebc278a`](https://github.com/sgl-project/sglang/commit/6afebc278a) [#26413](https://github.com/sgl-project/sglang/pull/26413)
  [docs] DeepSeek-V4 cookbook: note cu129 image for GB200 Pro DeepEP backend (#26413)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-25** [`121cc09405`](https://github.com/sgl-project/sglang/commit/121cc09405) [#25848](https://github.com/sgl-project/sglang/pull/25848)
  [diffusion] Add CFG gating for denoising (#25848)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`, `python/sglang/multimodal_gen/test/unit/test_cfg_gating.py`_
- **2026-05-25** [`85f9522e36`](https://github.com/sgl-project/sglang/commit/85f9522e36) [#25847](https://github.com/sgl-project/sglang/pull/25847)
  [diffusion] Cache fp32 layernorm params (#25847)
  _Files: `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/test/unit/test_fp32_layernorm.py`_
- **2026-05-25** [`0942011665`](https://github.com/sgl-project/sglang/commit/0942011665) [#26267](https://github.com/sgl-project/sglang/pull/26267)
  [NPU] Add torchaudio dependency for NPU platform (#26267)
  _Files: `docker/npu.Dockerfile`, `python/pyproject_npu.toml`_
- **2026-05-25** [`e1463bb2c2`](https://github.com/sgl-project/sglang/commit/e1463bb2c2) [#26097](https://github.com/sgl-project/sglang/pull/26097)
  [VLM] try to reuse precomputed padded input ids in scheduler instead of padding (#26097)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-25** [`64e2b54a8f`](https://github.com/sgl-project/sglang/commit/64e2b54a8f) [#26149](https://github.com/sgl-project/sglang/pull/26149)
  [VLM] feat: accept grid_thws from preprocessed metadata for kimi (#26149)
  _Files: `python/sglang/srt/models/kimi_k25.py`_
- **2026-05-25** [`72c1582d4e`](https://github.com/sgl-project/sglang/commit/72c1582d4e) [#26094](https://github.com/sgl-project/sglang/pull/26094)
  [VLM] fix: fix only the grids from last split mm item is collected for qwen-vl (#26094)
  _Files: `python/sglang/srt/multimodal/processors/qwen_vl.py`_

## KV Cache / Memory  (19 commits)

- **2026-06-01** [`6965fe0eec`](https://github.com/sgl-project/sglang/commit/6965fe0eec) [#26615](https://github.com/sgl-project/sglang/pull/26615)
  [sgl] Window-aware LRU refresh for SWA prefix cache in unified cache (#26615)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/__init__.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py` _+1 more__
- **2026-06-01** [`cdd06011a1`](https://github.com/sgl-project/sglang/commit/cdd06011a1) [#26870](https://github.com/sgl-project/sglang/pull/26870)
  Make unified tree SWA hicache tests faithful to write-through backup (#26870)
  _Files: `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-31** [`c06220159b`](https://github.com/sgl-project/sglang/commit/c06220159b) [#26675](https://github.com/sgl-project/sglang/pull/26675)
  [mem_cache][1/N] refactor: split allocator.py into allocator/ subpackage (#26675)
  _Files: `python/sglang/srt/mem_cache/allocator/__init__.py`, `python/sglang/srt/mem_cache/allocator/base.py`, `python/sglang/srt/mem_cache/allocator/paged.py`, `python/sglang/srt/mem_cache/allocator/token.py`_
- **2026-05-31** [`30a22cc360`](https://github.com/sgl-project/sglang/commit/30a22cc360) [#26812](https://github.com/sgl-project/sglang/pull/26812)
  Add a periodic full-radix-tree KV-canary sweep (#26812)
  _Files: `python/sglang/jit_kernel/kv_canary/plan/api.py`, `python/sglang/jit_kernel/kv_canary/verify.py`, `python/sglang/jit_kernel/tests/kv_canary/test_pipeline_e2e.py`, `python/sglang/jit_kernel/tests/kv_canary/test_verify_hand.py` _+18 more__
- **2026-05-31** [`bad83ab427`](https://github.com/sgl-project/sglang/commit/bad83ab427) [#26329](https://github.com/sgl-project/sglang/pull/26329)
  Fix the EAGLE chunked-prefill next-token chain (#26329) (#26800)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-05-30** [`7662210406`](https://github.com/sgl-project/sglang/commit/7662210406) [#26549](https://github.com/sgl-project/sglang/pull/26549)
  [UnifiedTree]: Support eviction priority (#26549)
  _Files: `python/sglang/srt/mem_cache/radix_cache.py`, `python/sglang/srt/mem_cache/unified_cache_components/full_component.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/srt/mem_cache/utils.py` _+1 more__
- **2026-05-29** [`eb5d4827e8`](https://github.com/sgl-project/sglang/commit/eb5d4827e8) [#26666](https://github.com/sgl-project/sglang/pull/26666)
  [UnifiedTree]: Split unified tree kl ci into multiple files to reduce GPU usage. (#26666)
  _Files: `test/registered/radix_cache/test_unified_radix_cache_kl_hicache_part2.py`, `test/registered/radix_cache/test_unified_radix_cache_kl_mamba.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_dsv4.py`, `test/registered/radix_cache/unified_radix_tree/test_unified_radix_cache_kl_full.py` _+3 more__
- **2026-05-28** [`34ea682a07`](https://github.com/sgl-project/sglang/commit/34ea682a07) [#26302](https://github.com/sgl-project/sglang/pull/26302)
  [UnifiedTree] gate load back pre-evict on full-attn availability only (#26302)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-28** [`21ba329dac`](https://github.com/sgl-project/sglang/commit/21ba329dac) [#24649](https://github.com/sgl-project/sglang/pull/24649)
  [Xeon] CPU CI enhancement for Intel Xeon platforms (#24649)
  _Files: `.github/workflows/pr-test-xeon.yml`, `test/registered/bench_fn/test_benchmark_datasets_api.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py`, `test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py` _+84 more__
- **2026-05-28** [`14c1bb2721`](https://github.com/sgl-project/sglang/commit/14c1bb2721) [#24089](https://github.com/sgl-project/sglang/pull/24089)
  [Feat][LMCache] Support LMCache mp mode (#24089)
  _Files: `docs_new/docs/advanced_features/hicache_design.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`, `python/sglang/srt/mem_cache/storage/lmcache/README.md` _+5 more__
- **2026-05-27** [`034dd39189`](https://github.com/sgl-project/sglang/commit/034dd39189) [#26387](https://github.com/sgl-project/sglang/pull/26387)
  Support KV events for UnifiedRadixCache (#26387)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-27** [`5f8911183b`](https://github.com/sgl-project/sglang/commit/5f8911183b) [#26485](https://github.com/sgl-project/sglang/pull/26485)
  [UnifiedTree]: Update Unified Radix Cache README (#26485)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/README.md`_
- **2026-05-26** [`38f32c38ab`](https://github.com/sgl-project/sglang/commit/38f32c38ab) [#26062](https://github.com/sgl-project/sglang/pull/26062)
  [UnifiedRadixTree]: Support L3 HiStorage framework (#26062)
  _Files: `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/unified_cache_components/full_component.py` _+8 more__
- **2026-05-26** [`98eb84497d`](https://github.com/sgl-project/sglang/commit/98eb84497d) [#26148](https://github.com/sgl-project/sglang/pull/26148)
  [PP] Skip PP output communication for pure chunked prefill batches (#26148)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+2 more__
- **2026-05-26** [`48f3264807`](https://github.com/sgl-project/sglang/commit/48f3264807) [#26301](https://github.com/sgl-project/sglang/pull/26301)
  [HiCache]: Check return code of cudaHostRegister (#26301)
  _Files: `python/sglang/srt/mem_cache/memory_pool_host.py`_
- **2026-05-26** [`3142278c5f`](https://github.com/sgl-project/sglang/commit/3142278c5f) [#25683](https://github.com/sgl-project/sglang/pull/25683)
  [diffusion] feat: layerwise NVTX markers for Nsight Systems profiling (#25683)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/parallel_executor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/sync_executor.py` _+10 more__
- **2026-05-25** [`b13d3d18c6`](https://github.com/sgl-project/sglang/commit/b13d3d18c6) [#26295](https://github.com/sgl-project/sglang/pull/26295)
  Refactor HiCache stack dispatch into strategies (#26295)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/unit/mem_cache/test_unified_radix_hicache_dispatch.py`_
- **2026-05-25** [`e86fdf3a3c`](https://github.com/sgl-project/sglang/commit/e86fdf3a3c) [#26177](https://github.com/sgl-project/sglang/pull/26177)
  [Bug Fix][HiCache] TreeNode.get_prefix_hash_values @lru_cache can return mutated list (#26177)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`_
- **2026-05-25** [`821d5f4a5b`](https://github.com/sgl-project/sglang/commit/821d5f4a5b) [#25874](https://github.com/sgl-project/sglang/pull/25874)
  [CPU] add faster KV-cache writes (#25874)
  _Files: `docker/xeon.Dockerfile`, `python/sglang/srt/mem_cache/memory_pool.py`, `sgl-kernel/csrc/cpu/common.h`, `sgl-kernel/csrc/cpu/kvcache.cpp` _+2 more__

## Speculative Decoding  (18 commits)

- **2026-06-01** [`1f8d3c7a42`](https://github.com/sgl-project/sglang/commit/1f8d3c7a42) [#25644](https://github.com/sgl-project/sglang/pull/25644)
  [Speculative] [NPU] Adaptive-SD NPU support (#25644)
  _Files: `python/sglang/srt/hardware_backend/npu/graph_runner/npu_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-06-01** [`1bff7a290f`](https://github.com/sgl-project/sglang/commit/1bff7a290f) [#26871](https://github.com/sgl-project/sglang/pull/26871)
  Refactor EAGLE infer tests: shared fixture + kits + overlap matrix (#26871)
  _Files: `python/sglang/test/kits/spec_server_kits.py`, `python/sglang/test/server_fixtures/spec_eagle_fixture.py`, `test/registered/spec/eagle/test_eagle_infer_a.py`, `test/registered/spec/eagle/test_eagle_infer_b.py` _+8 more__
- **2026-06-01** [`d078cb72bd`](https://github.com/sgl-project/sglang/commit/d078cb72bd) [#26903](https://github.com/sgl-project/sglang/pull/26903)
  [NPU] [DOC] clarify Ascend NPU exclusive supported values for speculative args (#26903)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-05-31** [`268f4c82f1`](https://github.com/sgl-project/sglang/commit/268f4c82f1) [#26814](https://github.com/sgl-project/sglang/pull/26814)
  Add rids/bootstrap-room int-hash plumbing for deterministic per-request identification (#26814)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/sampling/sampling_batch_info.py` _+1 more__
- **2026-05-31** [`9c43c3719f`](https://github.com/sgl-project/sglang/commit/9c43c3719f) [#26813](https://github.com/sgl-project/sglang/pull/26813)
  Support EAGLE speculative decoding in the KV-canary (#26813)
  _Files: `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py` _+3 more__
- **2026-05-31** [`656e75b798`](https://github.com/sgl-project/sglang/commit/656e75b798) [#26801](https://github.com/sgl-project/sglang/pull/26801)
  Add a nullcontext placeholder in the forward path for KV-canary (#26801)
  _Files: `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-05-30** [`c2ac37dbcc`](https://github.com/sgl-project/sglang/commit/c2ac37dbcc) [#26753](https://github.com/sgl-project/sglang/pull/26753)
  [Bug] ngram verify: keep `batch.seq_lens_sum` in sync after accept (#26753)
  _Files: `python/sglang/srt/speculative/ngram_info.py`_
- **2026-05-29** [`1c2857b064`](https://github.com/sgl-project/sglang/commit/1c2857b064) [#25960](https://github.com/sgl-project/sglang/pull/25960)
  bugfix: --decrypted-draft-config-file not applied (#25960)
  _Files: `python/sglang/srt/arg_groups/speculative_hook.py`_
- **2026-05-28** [`68706e615a`](https://github.com/sgl-project/sglang/commit/68706e615a) [#26354](https://github.com/sgl-project/sglang/pull/26354)
  [SPEC] fix: use effective max draft tokens for adaptive spec initiali… (#26354)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/managers/utils.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/server_args.py`_
- **2026-05-28** [`8e0ed75f2d`](https://github.com/sgl-project/sglang/commit/8e0ed75f2d) [#26551](https://github.com/sgl-project/sglang/pull/26551)
  Remove dead fields and always-False plumbing across SB / FB / LogitsMetadata (#26551)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/logits_processor.py`, `python/sglang/srt/layers/utils/logprob.py`, `python/sglang/srt/managers/schedule_batch.py` _+3 more__
- **2026-05-27** [`21d0e74aff`](https://github.com/sgl-project/sglang/commit/21d0e74aff) [#26403](https://github.com/sgl-project/sglang/pull/26403)
  Disable torch.compile for NPU in speculative overlap utils (#26403)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-26** [`dd6f073377`](https://github.com/sgl-project/sglang/commit/dd6f073377) [#26235](https://github.com/sgl-project/sglang/pull/26235)
  Reland "[perf][spec decoding] Skip full-vocab softmax in EAGLE draft when topk == 1 (#26235)" (#26397)
  _Files: `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-05-26** [`9409969fd5`](https://github.com/sgl-project/sglang/commit/9409969fd5) [#26235](https://github.com/sgl-project/sglang/pull/26235)
  Revert "[perf][spec decoding] Skip full-vocab softmax in EAGLE draft when topk == 1 (#26235)" (#26358)
  _Files: `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-05-26** [`d9c82934c8`](https://github.com/sgl-project/sglang/commit/d9c82934c8) [#26271](https://github.com/sgl-project/sglang/pull/26271)
  Extract Scheduler init methods and add skills to enforce the splitting requirements (#26271)
  _Files: `.claude/rules/modify-component-must-read.md`, `.claude/rules/speculative-naming.md`, `.claude/skills/large-class-init-style/SKILL.md`, `python/sglang/srt/managers/scheduler.py`_
- **2026-05-25** [`3e67398a96`](https://github.com/sgl-project/sglang/commit/3e67398a96) [#26292](https://github.com/sgl-project/sglang/pull/26292)
  Zero `req_pool_indices` padding in cuda-graph populate (#26292)
  _Files: `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/frozen_kv_mtp_cuda_graph_runner.py`_
- **2026-05-25** [`a77449f86d`](https://github.com/sgl-project/sglang/commit/a77449f86d) [#26235](https://github.com/sgl-project/sglang/pull/26235)
  [perf][spec decoding] Skip full-vocab softmax in EAGLE draft when topk == 1 (#26235)
  _Files: `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-05-25** [`b0cf01eb85`](https://github.com/sgl-project/sglang/commit/b0cf01eb85) [#26270](https://github.com/sgl-project/sglang/pull/26270)
  Lazy-load speculative-naming via skill instead of always-on rule (#26270)
  _Files: `.claude/rules/speculative-naming.md`, `.claude/skills/speculative-naming/SKILL.md`_
- **2026-05-25** [`850887dc63`](https://github.com/sgl-project/sglang/commit/850887dc63) [#26244](https://github.com/sgl-project/sglang/pull/26244)
  [Spec] fix EAGLE v2 verify metadata init order on non-cuda-graph path (#26244)
  _Files: `python/sglang/srt/speculative/eagle_info_v2.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_

## Scheduler / Batching  (18 commits)

- **2026-06-01** [`afd2d0b2f4`](https://github.com/sgl-project/sglang/commit/afd2d0b2f4) [#26883](https://github.com/sgl-project/sglang/pull/26883)
  [PP][Bugfix] Handle input_ids assignment in prepare_for_extend (#26883)
  _Files: `python/sglang/srt/managers/scheduler_pp_mixin.py`_
- **2026-06-01** [`11411aa49d`](https://github.com/sgl-project/sglang/commit/11411aa49d) [#24000](https://github.com/sgl-project/sglang/pull/24000)
  [tokenizer] Surface scheduler load info (num_running_reqs / num_waiting_reqs) in meta_info (#24000)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-31** [`585baa97f7`](https://github.com/sgl-project/sglang/commit/585baa97f7) [#26797](https://github.com/sgl-project/sglang/pull/26797)
  [core] Compute token_type_ids in ForwardBatch.init_new (#26797)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-05-31** [`1eadb7a173`](https://github.com/sgl-project/sglang/commit/1eadb7a173) [#26831](https://github.com/sgl-project/sglang/pull/26831)
  Fix multi-tokenizer batch request output routing (health stuck at 503) (#26831)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-31** [`7f93952f79`](https://github.com/sgl-project/sglang/commit/7f93952f79) [#26802](https://github.com/sgl-project/sglang/pull/26802)
  Add a debug toggle for selectively reverting PR fixes (#26802)
  _Files: `python/sglang/srt/debug_utils/pr_fix_toggle.py`, `python/sglang/srt/debug_utils/source_patcher/source_editor.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/scheduler.py` _+1 more__
- **2026-05-31** [`9b4be9c574`](https://github.com/sgl-project/sglang/commit/9b4be9c574) [#26779](https://github.com/sgl-project/sglang/pull/26779)
  [core] Compute dimensions/return_pooled_hidden_states in ForwardBatch.init_new (#26779)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-05-30** [`1c79015434`](https://github.com/sgl-project/sglang/commit/1c79015434) [#26760](https://github.com/sgl-project/sglang/pull/26760)
  Drop dead ScheduleBatch return_routed_experts/return_indexer_topk fields (#26760)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/registered/rl/test_return_indexer_topk.py`_
- **2026-05-30** [`6f1c9fc77b`](https://github.com/sgl-project/sglang/commit/6f1c9fc77b) [#26423](https://github.com/sgl-project/sglang/pull/26423)
  [RL] Fix crash when the reqs in a batch have a mix of `return_routed_experts` = True and False. (#26423)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/rl/test_return_routed_experts.py`_
- **2026-05-29** [`6ce49e5f4c`](https://github.com/sgl-project/sglang/commit/6ce49e5f4c) [#26583](https://github.com/sgl-project/sglang/pull/26583)
  [Utils] Support configure log level at runtime (#26583)
  _Files: `docs_new/docs/advanced_features/observability.mdx`, `python/sglang/srt/managers/configure_logging.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/io_struct.py` _+2 more__
- **2026-05-29** [`4ff1296f5e`](https://github.com/sgl-project/sglang/commit/4ff1296f5e) [#26348](https://github.com/sgl-project/sglang/pull/26348)
  Optimize get load calls (/v1/loads) using shared-memory load snapshots (#26348)
  _Files: `python/sglang/srt/entrypoints/v1_loads.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/detokenizer_manager.py` _+10 more__
- **2026-05-29** [`ace730db48`](https://github.com/sgl-project/sglang/commit/ace730db48) [#26672](https://github.com/sgl-project/sglang/pull/26672)
  [AMD] Work around HIP TPOT regression from Event.wait() in MTP seq lens resolution (#26672)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-28** [`3ca8cb470f`](https://github.com/sgl-project/sglang/commit/3ca8cb470f) [#26590](https://github.com/sgl-project/sglang/pull/26590)
  [BugFix] preserve cached token details in multi-tokenizer output (#26590)
  _Files: `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `test/registered/unit/managers/test_multi_tokenizer_mixin.py`_
- **2026-05-28** [`686ef50672`](https://github.com/sgl-project/sglang/commit/686ef50672) [#26022](https://github.com/sgl-project/sglang/pull/26022)
  Group ScheduleBatch and ForwardBatch fields by data-flow role (#26022)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/model_executor/forward_batch_info.py`_
- **2026-05-27** [`98bc6f3c22`](https://github.com/sgl-project/sglang/commit/98bc6f3c22) [#26355](https://github.com/sgl-project/sglang/pull/26355)
  API Perf: Replace pydantic per-element validation with C loop validation (#26355)
  _Files: `benchmark/io/bench_input_ids_validator.py`, `python/sglang/srt/managers/io_struct.py`, `python/sglang/srt/utils/field_validators.py`, `test/registered/unit/utils/test_field_validators.py`_
- **2026-05-27** [`216ed270e5`](https://github.com/sgl-project/sglang/commit/216ed270e5) [#26463](https://github.com/sgl-project/sglang/pull/26463)
  refresh resolve_seq_lens_cpu comments (#26463)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-26** [`1a05b511e4`](https://github.com/sgl-project/sglang/commit/1a05b511e4) [#25025](https://github.com/sgl-project/sglang/pull/25025)
  dp: refactor idle batch logic (#25025)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`_
- **2026-05-26** [`8f2a4e70f8`](https://github.com/sgl-project/sglang/commit/8f2a4e70f8) [#26232](https://github.com/sgl-project/sglang/pull/26232)
  [SRT] minor: reuse req input id array for unpadded ids (#26232)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-25** [`ca029e816b`](https://github.com/sgl-project/sglang/commit/ca029e816b) [#25404](https://github.com/sgl-project/sglang/pull/25404)
  Fix missing idle-batch handling in prepare_mlp_sync_batch_raw (#25404)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`_

## Other  (17 commits)

- **2026-06-01** [`61cc70e8aa`](https://github.com/sgl-project/sglang/commit/61cc70e8aa) [#26481](https://github.com/sgl-project/sglang/pull/26481)
  Fixed incorrect indexing for slot 0 compatibility (#26481)
  _Files: `python/sglang/bench_one_batch.py`_
- **2026-05-31** [`cdee16e144`](https://github.com/sgl-project/sglang/commit/cdee16e144) [#26816](https://github.com/sgl-project/sglang/pull/26816)
  Add the KV-canary perturb framework for fault-injection self-tests (#26816)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/perturb/config.py`, `python/sglang/srt/kv_canary/perturb/manager.py` _+5 more__
- **2026-05-31** [`8a20c58252`](https://github.com/sgl-project/sglang/commit/8a20c58252) [#26804](https://github.com/sgl-project/sglang/pull/26804)
  Pull test_utils server-launch boilerplate into reusable helpers (#26804)
  _Files: `python/sglang/test/test_utils.py`_
- **2026-05-31** [`ce647cbcfd`](https://github.com/sgl-project/sglang/commit/ce647cbcfd) [#26803](https://github.com/sgl-project/sglang/pull/26803)
  Add a SimplePhaseChecker for execution-phase assertions (#26803)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/utils/phase_checker.py`, `test/registered/utils/test_phase_checker.py`_
- **2026-05-30** [`7ed53d15f3`](https://github.com/sgl-project/sglang/commit/7ed53d15f3) [#23988](https://github.com/sgl-project/sglang/pull/23988)
  [config] Recognize custom hybrid SWA models via hf_text_config.is_hybrid_swa (#23988)
  _Files: `python/sglang/srt/configs/model_config.py`_
- **2026-05-30** [`c048ebd10d`](https://github.com/sgl-project/sglang/commit/c048ebd10d) [#26764](https://github.com/sgl-project/sglang/pull/26764)
  [Hicache]: skip flaky test (#26764)
  _Files: `test/registered/hicache/test_hicache_storage_file_backend.py`_
- **2026-05-29** [`8652001b6a`](https://github.com/sgl-project/sglang/commit/8652001b6a) [#26534](https://github.com/sgl-project/sglang/pull/26534)
  fix: use req.req_pool_idx instead of loop variable for req_to_token i… (#26534)
  _Files: `python/sglang/bench_one_batch.py`_
- **2026-05-29** [`7dff4118b9`](https://github.com/sgl-project/sglang/commit/7dff4118b9) [#26680](https://github.com/sgl-project/sglang/pull/26680)
  Ignore `.humanize` folder (#26680)
  _Files: `.gitignore`_
- **2026-05-28** [`4f92e63c99`](https://github.com/sgl-project/sglang/commit/4f92e63c99) [#26616](https://github.com/sgl-project/sglang/pull/26616)
  Let unittest._ShouldStop propagate through retry() so subTest+failfast works (#26616)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-05-28** [`f143d54d78`](https://github.com/sgl-project/sglang/commit/f143d54d78) [#26553](https://github.com/sgl-project/sglang/pull/26553)
  Add env-var-conventions skill (#26553)
  _Files: `.claude/rules/modify-component-must-read.md`, `.claude/skills/env-var-conventions/SKILL.md`_
- **2026-05-28** [`68e5b4fdd6`](https://github.com/sgl-project/sglang/commit/68e5b4fdd6) [#26522](https://github.com/sgl-project/sglang/pull/26522)
  [NemotronH] Fix weight-loading unit test broken by Puzzle support (#26522)
  _Files: `test/registered/unit/models/test_nemotron_h_weight_loading.py`_
- **2026-05-27** [`83d5f4604c`](https://github.com/sgl-project/sglang/commit/83d5f4604c) [#26308](https://github.com/sgl-project/sglang/pull/26308)
  [NPU]add decord2 for npu (#26308)
  _Files: `python/pyproject_npu.toml`_
- **2026-05-27** [`9060509214`](https://github.com/sgl-project/sglang/commit/9060509214) [#26390](https://github.com/sgl-project/sglang/pull/26390)
  [NPU] fix CI (#26390)
  _Files: `python/pyproject_npu.toml`, `scripts/ci/npu/npu_ci_install_dependency.sh`_
- **2026-05-27** [`0c34fc5ace`](https://github.com/sgl-project/sglang/commit/0c34fc5ace) [#26435](https://github.com/sgl-project/sglang/pull/26435)
  [Misc] Update CI Permission (#26435)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-05-26** [`6989fede3c`](https://github.com/sgl-project/sglang/commit/6989fede3c) [#25911](https://github.com/sgl-project/sglang/pull/25911)
  Purge usage of pytorch named tensors (#25911)
  _Files: `python/sglang/srt/debug_utils/comparator/aligner/axis_aligner.py`, `python/sglang/srt/debug_utils/comparator/aligner/reorderer/executor.py`, `python/sglang/srt/debug_utils/comparator/aligner/token_aligner/concat_steps/executor.py`, `python/sglang/srt/debug_utils/comparator/aligner/token_aligner/smart/aux_loader.py` _+13 more__
- **2026-05-26** [`29e245e6a7`](https://github.com/sgl-project/sglang/commit/29e245e6a7) [#26336](https://github.com/sgl-project/sglang/pull/26336)
  [misc] Update permission (#26336)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-05-25** [`de3f6fb02e`](https://github.com/sgl-project/sglang/commit/de3f6fb02e) [#25856](https://github.com/sgl-project/sglang/pull/25856)
  Fix attr err (#25856)

## Triton / Kernels  (16 commits)

- **2026-05-31** [`f220c72929`](https://github.com/sgl-project/sglang/commit/f220c72929) [#26821](https://github.com/sgl-project/sglang/pull/26821)
  Add periodic KV-canary stats logging and kernel-run-counter health check (#26821)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/config.py`, `python/sglang/srt/kv_canary/runner/canary_manager.py`, `python/sglang/srt/kv_canary/runner/health_checker.py` _+5 more__
- **2026-05-31** [`6be4b32d8d`](https://github.com/sgl-project/sglang/commit/6be4b32d8d) [#26818](https://github.com/sgl-project/sglang/pull/26818)
  Add token-id verification to the KV-canary (#26818)
  _Files: `python/sglang/jit_kernel/benchmark/kv_canary/bench_scatter_req_token_ids.py`, `python/sglang/jit_kernel/kv_canary/scatter_req_token_ids.py`, `python/sglang/jit_kernel/tests/kv_canary/test_scatter_req_token_ids.py`, `python/sglang/srt/environ.py` _+14 more__
- **2026-05-31** [`678e73a9ee`](https://github.com/sgl-project/sglang/commit/678e73a9ee) [#26815](https://github.com/sgl-project/sglang/pull/26815)
  Add a deterministic token oracle and production write-input assertion (#26815)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/kv_canary/api.py`, `python/sglang/srt/kv_canary/config.py`, `python/sglang/srt/kv_canary/perturb/__init__.py` _+23 more__
- **2026-05-31** [`70e983a2da`](https://github.com/sgl-project/sglang/commit/70e983a2da) [#26806](https://github.com/sgl-project/sglang/pull/26806)
  Add the KV-canary write JIT kernel and reference implementation (#26806)
  _Files: `python/sglang/jit_kernel/benchmark/kv_canary/bench_write.py`, `python/sglang/jit_kernel/csrc/kv_canary/canary_write.cuh`, `python/sglang/jit_kernel/kv_canary/write.py`, `python/sglang/jit_kernel/kv_canary/write_ref.py` _+3 more__
- **2026-05-31** [`16950954c6`](https://github.com/sgl-project/sglang/commit/16950954c6) [#26805](https://github.com/sgl-project/sglang/pull/26805)
  Add the KV-canary verify JIT kernel and reference implementation (#26805)
  _Files: `python/sglang/jit_kernel/benchmark/kv_canary/bench_verify.py`, `python/sglang/jit_kernel/benchmark/kv_canary/utils.py`, `python/sglang/jit_kernel/csrc/kv_canary/canary_common.cuh`, `python/sglang/jit_kernel/csrc/kv_canary/canary_verify.cuh` _+9 more__
- **2026-05-30** [`e279b0bf72`](https://github.com/sgl-project/sglang/commit/e279b0bf72) [#24755](https://github.com/sgl-project/sglang/pull/24755)
  Optimize large add_constant tensors (#24755)
  _Files: `python/sglang/jit_kernel/benchmark/bench_add_constant.py`, `python/sglang/jit_kernel/csrc/add_constant.cuh`, `python/sglang/jit_kernel/tests/test_add_constant.py`_
- **2026-05-30** [`7c5708cba7`](https://github.com/sgl-project/sglang/commit/7c5708cba7) [#25976](https://github.com/sgl-project/sglang/pull/25976)
  [DeepSeek-V4] Add mhc_fused_post_pre kernel (#25976)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_nextn.py` _+1 more__
- **2026-05-30** [`b4bf489dea`](https://github.com/sgl-project/sglang/commit/b4bf489dea) [#26624](https://github.com/sgl-project/sglang/pull/26624)
  ci: allow /rerun-test to dispatch nightly/weekly CUDA tests (#26624)
  _Files: `scripts/ci/runner_configs.yml`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-05-29** [`ed85bcf8c3`](https://github.com/sgl-project/sglang/commit/ed85bcf8c3) [#26704](https://github.com/sgl-project/sglang/pull/26704)
  pin kernels<0.15 (#26704)
  _Files: `python/pyproject.toml`_
- **2026-05-29** [`a722b1a437`](https://github.com/sgl-project/sglang/commit/a722b1a437) [#26634](https://github.com/sgl-project/sglang/pull/26634)
  [CPU] fix incorrect index of b_ptr in fused_sigmoid_gating_delta_rule… (#26634)
  _Files: `sgl-kernel/csrc/cpu/mamba/fla.cpp`, `test/registered/cpu/test_mamba.py`_
- **2026-05-28** [`578d27e56a`](https://github.com/sgl-project/sglang/commit/578d27e56a) [#25920](https://github.com/sgl-project/sglang/pull/25920)
  [bugfix] Honor cast_x_before_out_mul in RMSNorm.forward_cuda residual path (#25920)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/fused_add_rmsnorm.cuh`, `python/sglang/jit_kernel/norm.py`, `python/sglang/jit_kernel/tests/test_fused_add_rmsnorm.py`, `python/sglang/srt/layers/layernorm.py`_
- **2026-05-28** [`8f21b3e2ef`](https://github.com/sgl-project/sglang/commit/8f21b3e2ef) [#25274](https://github.com/sgl-project/sglang/pull/25274)
  [Refactor] JIT kernel benchmark (#25274)
  _Files: `.claude/skills/add-jit-kernel/SKILL.md`, `python/sglang/jit_kernel/benchmark/bench_activation.py`, `python/sglang/jit_kernel/benchmark/bench_qknorm.py`, `python/sglang/jit_kernel/benchmark/bench_store_cache.py` _+2 more__
- **2026-05-28** [`e60f799b40`](https://github.com/sgl-project/sglang/commit/e60f799b40) [#26382](https://github.com/sgl-project/sglang/pull/26382)
  Enable Kimi-K2.5 piecewise CUDA graph (#26382)
  _Files: `python/sglang/srt/layers/layernorm.py`, `python/sglang/srt/models/kimi_k25.py`_
- **2026-05-27** [`14f81a67d9`](https://github.com/sgl-project/sglang/commit/14f81a67d9) [#26421](https://github.com/sgl-project/sglang/pull/26421)
  chore: bump sglang-kernel version to 0.4.3 (#26421)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`_
- **2026-05-26** [`f0ba651d66`](https://github.com/sgl-project/sglang/commit/f0ba651d66) [#26344](https://github.com/sgl-project/sglang/pull/26344)
  [Doc] Update pip install commands for Cuda12 (#26344)
  _Files: `docs_new/docs/get-started/install.mdx`_
- **2026-05-26** [`1953565ba1`](https://github.com/sgl-project/sglang/commit/1953565ba1) [#26338](https://github.com/sgl-project/sglang/pull/26338)
  Signal CUDA coredumps to tracker issue (#26338)
  _Files: `.github/actions/upload-cuda-coredumps/action.yml`, `.github/workflows/_pr-test-stage.yml`_

## Models  (13 commits)

- **2026-05-31** [`45194794d0`](https://github.com/sgl-project/sglang/commit/45194794d0) [#26799](https://github.com/sgl-project/sglang/pull/26799)
  Apply gemma's position offset out-of-place instead of in-place (#26799)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/gemma4_mm.py`_
- **2026-05-31** [`13ca55afa3`](https://github.com/sgl-project/sglang/commit/13ca55afa3) [#26798](https://github.com/sgl-project/sglang/pull/26798)
  Make qwen3's set_embed_and_head idempotent (#26798)
  _Files: `python/sglang/srt/models/qwen3.py`_
- **2026-05-30** [`23a825c694`](https://github.com/sgl-project/sglang/commit/23a825c694) [#26709](https://github.com/sgl-project/sglang/pull/26709)
  [DOC] [NPU] add qwen3.5-397b best practice to doc_new (#26709)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-05-29** [`6ea69efb7f`](https://github.com/sgl-project/sglang/commit/6ea69efb7f) [#26744](https://github.com/sgl-project/sglang/pull/26744)
  [RL] Forward Kimi K2.5 weight hooks to language model (#26744)
  _Files: `python/sglang/srt/models/kimi_k25.py`_
- **2026-05-29** [`69362cbc2c`](https://github.com/sgl-project/sglang/commit/69362cbc2c) [#26668](https://github.com/sgl-project/sglang/pull/26668)
  [Doc] Update benchmark instruction for dsv4 (#26668)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-05-28** [`cd65be98df`](https://github.com/sgl-project/sglang/commit/cd65be98df) [#26604](https://github.com/sgl-project/sglang/pull/26604)
  [CP] Add back qwen 30b test (#26604)
  _Files: `test/registered/cp/test_qwen3_30b.py`_
- **2026-05-28** [`a38620b92c`](https://github.com/sgl-project/sglang/commit/a38620b92c) [#26601](https://github.com/sgl-project/sglang/pull/26601)
  chore: add @pyc96 as codeowner for gemma4 files (#26601)
  _Files: `.github/CODEOWNERS`_
- **2026-05-28** [`f4eac50389`](https://github.com/sgl-project/sglang/commit/f4eac50389) [#26430](https://github.com/sgl-project/sglang/pull/26430)
  Fix GemmaRMSNorm gemma_weight buffer storage for Qwen3.5 (#26430)
  _Files: `python/sglang/srt/layers/layernorm.py`_
- **2026-05-28** [`a245cae3d1`](https://github.com/sgl-project/sglang/commit/a245cae3d1) [#26038](https://github.com/sgl-project/sglang/pull/26038)
  [NPU] fix model ERNIE-4.5-21B-A3B-PT bias need 1D error (#26038)
  _Files: `python/sglang/srt/models/ernie4.py`, `python/sglang/srt/models/llama.py`_
- **2026-05-28** [`eae03ce3b2`](https://github.com/sgl-project/sglang/commit/eae03ce3b2) [#26238](https://github.com/sgl-project/sglang/pull/26238)
  refactor(dsv4): route MHC prenorm through DeepGEMM wrapper (#26238)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py` _+2 more__
- **2026-05-27** [`d6032c04b6`](https://github.com/sgl-project/sglang/commit/d6032c04b6) [#26451](https://github.com/sgl-project/sglang/pull/26451)
  [docs] Fix V4 Pro balanced recipe (#26451)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-26** [`499eecce22`](https://github.com/sgl-project/sglang/commit/499eecce22) [#25023](https://github.com/sgl-project/sglang/pull/25023)
  [NemotronH] V3 Omni wrapper: WeightsMapper + config round-trip (#25023)
  _Files: `python/sglang/srt/configs/nano_nemotron_vl.py`, `python/sglang/srt/models/nano_nemotron_vl.py`_
- **2026-05-26** [`47617cc4df`](https://github.com/sgl-project/sglang/commit/47617cc4df) [#25971](https://github.com/sgl-project/sglang/pull/25971)
  [CPU Doc]Add Xeon CPU info in Qwen3 Cookbook (#25971)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.mdx`, `docs_new/src/snippets/autoregressive/qwen3-deployment.jsx`_

## CI / Build  (12 commits)

- **2026-06-01** [`1ee189831f`](https://github.com/sgl-project/sglang/commit/1ee189831f) [#26682](https://github.com/sgl-project/sglang/pull/26682)
  [CI] Bump xeon PR test unit tests timeout to 60 minutes (#26682)
  _Files: `.github/workflows/pr-test-xeon.yml`_
- **2026-05-30** [`804f01a823`](https://github.com/sgl-project/sglang/commit/804f01a823) [#26721](https://github.com/sgl-project/sglang/pull/26721)
  Allow PR test and lint workflows to trigger on non-main bases (#26721)
  _Files: `.github/workflows/lint.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-29** [`05bef58297`](https://github.com/sgl-project/sglang/commit/05bef58297) [#26699](https://github.com/sgl-project/sglang/pull/26699)
  [Misc] Tiny change default building branch of sgl-deep-gemm (#26699)
  _Files: `.github/workflows/release-whl-deepgemm.yml`_
- **2026-05-29** [`fba083c80f`](https://github.com/sgl-project/sglang/commit/fba083c80f) [#26648](https://github.com/sgl-project/sglang/pull/26648)
  [CI] Split PP tests into base and extra suites (#26648)
  _Files: `test/registered/pp/test_pp_single_node.py`, `test/registered/pp/test_pp_single_node_extra.py`_
- **2026-05-29** [`7619e77b7b`](https://github.com/sgl-project/sglang/commit/7619e77b7b) [#26466](https://github.com/sgl-project/sglang/pull/26466)
  [NPU] chore: basic software upgrade (#26466)
  _Files: `.github/workflows/nightly-test-npu.yml`, `.github/workflows/pr-test-npu.yml`, `.github/workflows/release-docker-npu-nightly.yml`, `.github/workflows/release-docker-npu.yml` _+2 more__
- **2026-05-28** [`0597242797`](https://github.com/sgl-project/sglang/commit/0597242797) [#26614](https://github.com/sgl-project/sglang/pull/26614)
  [CI] /rerun-test: descend into directories that a glob matched (#26614)
  _Files: `scripts/ci/utils/slash_command_handler.py`_
- **2026-05-28** [`5018e5c969`](https://github.com/sgl-project/sglang/commit/5018e5c969) [#26422](https://github.com/sgl-project/sglang/pull/26422)
  [CI] /rerun-test: support glob wildcard patterns (#26422)
  _Files: `.claude/skills/ci-workflow-guide/SKILL.md`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-05-28** [`9fea20a078`](https://github.com/sgl-project/sglang/commit/9fea20a078) [#25174](https://github.com/sgl-project/sglang/pull/25174)
  update XPU Dockerfile (#25174)
  _Files: `.github/workflows/pr-test-xpu.yml`, `docker/xpu.Dockerfile`_
- **2026-05-27** [`7c421ed3ec`](https://github.com/sgl-project/sglang/commit/7c421ed3ec) [#26509](https://github.com/sgl-project/sglang/pull/26509)
  [CI] runner-utilization: count in-flight queue waits + per-job status/links (#26509)
  _Files: `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/runner_utilization_report.py`, `scripts/ci/utils/test_runner_utilization_report.py`_
- **2026-05-26** [`a26913158b`](https://github.com/sgl-project/sglang/commit/a26913158b) [#26322](https://github.com/sgl-project/sglang/pull/26322)
  fix(ci): enforce legacy docs/ gate in Lint workflow (#26322)
  _Files: `.github/workflows/lint.yml`_
- **2026-05-25** [`7c04b9e942`](https://github.com/sgl-project/sglang/commit/7c04b9e942) [#26279](https://github.com/sgl-project/sglang/pull/26279)
  fix(docker): generate Cargo.lock in chef stage for sgl-router build (#26279)
  _Files: `docker/sgl-router.Dockerfile`_
- **2026-05-25** [`81704ad602`](https://github.com/sgl-project/sglang/commit/81704ad602) [#26273](https://github.com/sgl-project/sglang/pull/26273)
  ci: add nightly Docker workflow for experimental sgl-router (#26273)
  _Files: `.github/workflows/nightly-experimental-sgl-router-docker.yml`_

## Tensor / Data Parallel  (11 commits)

- **2026-06-01** [`3aaf8f115e`](https://github.com/sgl-project/sglang/commit/3aaf8f115e) [#26714](https://github.com/sgl-project/sglang/pull/26714)
  fix test cases failed in nightly pipeline (#26714)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `test/registered/ascend/llm_models/test_ascend_minimax_m2.py`_
- **2026-05-31** [`736ad1f32a`](https://github.com/sgl-project/sglang/commit/736ad1f32a) [#26807](https://github.com/sgl-project/sglang/pull/26807)
  Add the KV-canary plan JIT kernels (#26807)
  _Files: `python/sglang/jit_kernel/benchmark/kv_canary/bench_plan.py`, `python/sglang/jit_kernel/csrc/kv_canary/canary_plan_entries.cuh`, `python/sglang/jit_kernel/kv_canary/plan/__init__.py`, `python/sglang/jit_kernel/kv_canary/plan/api.py` _+14 more__
- **2026-05-30** [`acd689b407`](https://github.com/sgl-project/sglang/commit/acd689b407) [#24667](https://github.com/sgl-project/sglang/pull/24667)
  feat: add SGLANG_RAY_BUNDLE_INDICES for fine-grained Ray bundle index control (#24667)
  _Files: `docs_new/docs/basic_usage/offline_engine_api.ipynb`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/ray/data_parallel_controller.py` _+3 more__
- **2026-05-29** [`7fb7b41a3e`](https://github.com/sgl-project/sglang/commit/7fb7b41a3e) [#26695](https://github.com/sgl-project/sglang/pull/26695)
  [docs] Qwen3.5 cookbook: multi-node, MTP TP overrides, dense mamba flag (#26695)
  _Files: `docs_new/cookbook/autoregressive/Qwen/Qwen3.5.mdx`, `docs_new/src/snippets/autoregressive/qwen35-deployment.jsx`_
- **2026-05-29** [`621a79728c`](https://github.com/sgl-project/sglang/commit/621a79728c) [#26653](https://github.com/sgl-project/sglang/pull/26653)
  test: stabilize Gemma4 26B-A4B MTP GSM8K test with deterministic inference + tuned threshold (#26653)
  _Files: `test/registered/spec/test_gemma4_mtp_26b_a4b_extra.py`_
- **2026-05-28** [`3e255fd493`](https://github.com/sgl-project/sglang/commit/3e255fd493) [#25650](https://github.com/sgl-project/sglang/pull/25650)
  fix: Graceful fallback to CustomAllReduce when full_nvlink is not True (#25650)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce.py`, `python/sglang/srt/distributed/device_communicators/custom_all_reduce_v2.py`, `python/sglang/srt/distributed/parallel_state.py`_
- **2026-05-28** [`be32df33b9`](https://github.com/sgl-project/sglang/commit/be32df33b9) [#26437](https://github.com/sgl-project/sglang/pull/26437)
  [MUSA] Fix startup with patched torchada (#26437)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml`, `python/sglang/jit_kernel/utils.py`, `sgl-kernel/pyproject_musa.toml`_
- **2026-05-28** [`9040feebd8`](https://github.com/sgl-project/sglang/commit/9040feebd8) [#24552](https://github.com/sgl-project/sglang/pull/24552)
  [Gemma4] Add test for MTP models  (#24552)
  _Files: `test/registered/spec/test_frozen_kv_mtp.py`, `test/registered/spec/test_gemma4_mtp_26b_a4b_extra.py`, `test/registered/spec/test_gemma4_mtp_31b_extra.py`_
- **2026-05-27** [`0abe6a85a5`](https://github.com/sgl-project/sglang/commit/0abe6a85a5) [#24429](https://github.com/sgl-project/sglang/pull/24429)
  Support NemotronHPuzzleForCausalLM (#24429)
  _Files: `python/sglang/srt/configs/__init__.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/nemotron_h.py`, `python/sglang/srt/models/nemotron_h.py` _+3 more__
- **2026-05-25** [`e7b12fe6fa`](https://github.com/sgl-project/sglang/commit/e7b12fe6fa) [#26313](https://github.com/sgl-project/sglang/pull/26313)
  Fix stale forward_metadata leak in DP attn unpadded idle batch (#26313)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-25** [`6e8fe176be`](https://github.com/sgl-project/sglang/commit/6e8fe176be) [#25851](https://github.com/sgl-project/sglang/pull/25851)
  sgl-router: experimental Rust HTTP router for SGLang worker pools (#25851)

## ROCm / AMD  (10 commits)

- **2026-06-01** [`89410b380b`](https://github.com/sgl-project/sglang/commit/89410b380b) [#26879](https://github.com/sgl-project/sglang/pull/26879)
  [AMD] Pin compressed-tensors==0.15.0 to fix ROCm nightly build (#26879)
  _Files: `python/pyproject_other.toml`_
- **2026-06-01** [`b14fba17d9`](https://github.com/sgl-project/sglang/commit/b14fba17d9) [#26909](https://github.com/sgl-project/sglang/pull/26909)
  [AMD] make bypass-fastfail label also disable within-suite fast-fail (#26909)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-05-29** [`272066566f`](https://github.com/sgl-project/sglang/commit/272066566f) [#26591](https://github.com/sgl-project/sglang/pull/26591)
  [AMD] Pin compressed-tensors<0.16.0 for srt_hip (fixes ROCm 7.2 nightly build) (#26591)
  _Files: `python/pyproject_other.toml`_
- **2026-05-29** [`569ee93357`](https://github.com/sgl-project/sglang/commit/569ee93357) [#26642](https://github.com/sgl-project/sglang/pull/26642)
  [AMD] ci: switch CACHE_HOST to a fresh path to fix "No space left on device" (#26642)
  _Files: `scripts/ci/amd/amd_ci_start_container.sh`_
- **2026-05-28** [`bdfd5da53e`](https://github.com/sgl-project/sglang/commit/bdfd5da53e) [#26562](https://github.com/sgl-project/sglang/pull/26562)
  [AMD] AITER Upgrade (#26562)
  _Files: `docker/rocm.Dockerfile`_
- **2026-05-28** [`6f85957ff2`](https://github.com/sgl-project/sglang/commit/6f85957ff2) [#26544](https://github.com/sgl-project/sglang/pull/26544)
  [AMD] Fix aiter checkout (rocm dockerfile) (#26544)
  _Files: `docker/rocm.Dockerfile`_
- **2026-05-28** [`505f37a63d`](https://github.com/sgl-project/sglang/commit/505f37a63d) [#26535](https://github.com/sgl-project/sglang/pull/26535)
  [AMD] force AITER checkout to bypass CSV CRLF/LF smudge dirty state (#26535)
  _Files: `scripts/ci/amd/amd_ci_install_dependency.sh`_
- **2026-05-27** [`f32ca1e0e5`](https://github.com/sgl-project/sglang/commit/f32ca1e0e5) [#26443](https://github.com/sgl-project/sglang/pull/26443)
  [AMD] AＭD CI - temporarily change to mi325 (#26443)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-05-26** [`0753182b50`](https://github.com/sgl-project/sglang/commit/0753182b50) [#26414](https://github.com/sgl-project/sglang/pull/26414)
  chore: bump sgl-kernel version to 0.4.3 (#26414)
  _Files: `sgl-kernel/pyproject.toml`, `sgl-kernel/pyproject_cpu.toml`, `sgl-kernel/pyproject_musa.toml`, `sgl-kernel/pyproject_rocm.toml` _+1 more__
- **2026-05-26** [`d25a220fdb`](https://github.com/sgl-project/sglang/commit/d25a220fdb) [#26392](https://github.com/sgl-project/sglang/pull/26392)
  [AMD] Relaxing timeout for AMD CI (#26392)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_

## Quantization  (7 commits)

- **2026-05-29** [`3cecc77ccb`](https://github.com/sgl-project/sglang/commit/3cecc77ccb) [#26626](https://github.com/sgl-project/sglang/pull/26626)
  [perf] Fuse NVFP4 gate_up_gemm + swiglu + output FP4 quant  (#26626)
  _Files: `.codespellrc`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/quantization/nvfp4_gemm_swiglu_nvfp4_quant.py` _+1 more__
- **2026-05-29** [`226649e3b7`](https://github.com/sgl-project/sglang/commit/226649e3b7) [#26415](https://github.com/sgl-project/sglang/pull/26415)
  [Fix] Fix FP8 Online Quantization (#26415)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/fp8.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp4.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`, `python/sglang/multimodal_gen/runtime/server_args.py`_
- **2026-05-29** [`fffdfb6fcb`](https://github.com/sgl-project/sglang/commit/fffdfb6fcb) [#25755](https://github.com/sgl-project/sglang/pull/25755)
  [Fix][NPU] Preserve existing packed_modules_mapping when merging model-level fused module mappings (#25755)
  _Files: `python/sglang/srt/layers/quantization/base_config.py`, `python/sglang/srt/layers/quantization/modelslim/modelslim.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-28** [`81663cb5f1`](https://github.com/sgl-project/sglang/commit/81663cb5f1) [#26478](https://github.com/sgl-project/sglang/pull/26478)
  [AMD] [CI] Register MI35x GSM8K nightly tests (#26478)
  _Files: `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`, `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`_
- **2026-05-27** [`d44584e8d8`](https://github.com/sgl-project/sglang/commit/d44584e8d8) [#26396](https://github.com/sgl-project/sglang/pull/26396)
  [AMD] [CI] Add GLM-5.1 MXFP4 TP2 accuracy gate (#26396)
  _Files: `test/registered/amd/accuracy/mi35x/test_glm51_mxfp4_tp2_gsm8k_mi35x.py`_
- **2026-05-27** [`bf5bc23431`](https://github.com/sgl-project/sglang/commit/bf5bc23431) [#26395](https://github.com/sgl-project/sglang/pull/26395)
  [AMD] [CI] Add DeepSeek-R1-0528 FP8 HiCache GSM8K test on MI35x (#26395)
  _Files: `test/registered/amd/test_deepseek_r1_hicache_mi35x.py`_
- **2026-05-25** [`aae04b1241`](https://github.com/sgl-project/sglang/commit/aae04b1241) [#25904](https://github.com/sgl-project/sglang/pull/25904)
  :memo: docs(diffusion): add MXFP4 quantization docs (#25904)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `docs_new/docs/sglang-diffusion/quantization.mdx`_

## Docs / Examples  (6 commits)

- **2026-06-01** [`4d20dc44fc`](https://github.com/sgl-project/sglang/commit/4d20dc44fc) [#26725](https://github.com/sgl-project/sglang/pull/26725)
  【NPU】add MiniMax2.5 best practice docs (#26725)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-05-28** [`f838adb7d4`](https://github.com/sgl-project/sglang/commit/f838adb7d4) [#26378](https://github.com/sgl-project/sglang/pull/26378)
  bench_serving: add Zipfian shared-prefix sampling to generated-shared-prefix (#26378)
  _Files: `docs_new/docs/developer_guide/bench_serving.mdx`, `python/sglang/bench_serving.py`, `python/sglang/benchmark/datasets/generated_shared_prefix.py`, `test/registered/bench_fn/test_benchmark_datasets_api.py`_
- **2026-05-28** [`97d129f8c6`](https://github.com/sgl-project/sglang/commit/97d129f8c6) [#24149](https://github.com/sgl-project/sglang/pull/24149)
  # feat(bench): add SPEED-Bench dataset support to bench_serving (#24149)
  _Files: `docs_new/docs/developer_guide/bench_serving.mdx`, `python/sglang/bench_serving.py`, `python/sglang/benchmark/datasets/__init__.py`, `python/sglang/benchmark/datasets/speed_bench.py` _+1 more__
- **2026-05-27** [`561e54f803`](https://github.com/sgl-project/sglang/commit/561e54f803) [#26511](https://github.com/sgl-project/sglang/pull/26511)
  Update kimi k25 launch command in cookbook (#26511)
  _Files: `docs_new/src/snippets/autoregressive/kimi-k25-deployment.jsx`_
- **2026-05-27** [`a1ebc4917a`](https://github.com/sgl-project/sglang/commit/a1ebc4917a) [#26464](https://github.com/sgl-project/sglang/pull/26464)
  [NPU][DOCS]Add faq and feature Compatibilit (#26464)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`_
- **2026-05-25** [`a4db563c87`](https://github.com/sgl-project/sglang/commit/a4db563c87) [#26249](https://github.com/sgl-project/sglang/pull/26249)
  [hisparse]: update user guide (#26249)
  _Files: `docs/advanced_features/hisparse_guide.md`, `docs_new/docs/advanced_features/hisparse_guide.mdx`_

## Structured Output  (5 commits)

- **2026-05-29** [`b47366fbf9`](https://github.com/sgl-project/sglang/commit/b47366fbf9) [#24133](https://github.com/sgl-project/sglang/pull/24133)
  [NPU]: Optimize xgrammar token bitmask on NPU  with AscendC (#24133)
  _Files: `python/sglang/srt/constrained/torch_ops/bitmask_ops.py`, `python/sglang/srt/constrained/xgrammar_backend.py`_
- **2026-05-29** [`79c844527c`](https://github.com/sgl-project/sglang/commit/79c844527c) [#25676](https://github.com/sgl-project/sglang/pull/25676)
  Upgrade xgrammar to 0.2.1 (#25676)
  _Files: `.github/workflows/full-test-npu.yml`, `.github/workflows/nightly-test-npu.yml`, `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml` _+9 more__
- **2026-05-28** [`bed20249f1`](https://github.com/sgl-project/sglang/commit/bed20249f1) [#26433](https://github.com/sgl-project/sglang/pull/26433)
  fix(tool_call): reland schema type normalization (#26433)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/function_call/utils.py`, `test/registered/unit/function_call/test_normalize_json_schema_types.py`_
- **2026-05-26** [`7e6e5efe51`](https://github.com/sgl-project/sglang/commit/7e6e5efe51) [#26379](https://github.com/sgl-project/sglang/pull/26379)
  Revert "fix(tool_call): normalize non-standard JSON Schema types in tool params" (#26379)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/function_call/utils.py`, `test/registered/unit/function_call/test_normalize_json_schema_types.py`_
- **2026-05-26** [`64c7c6851b`](https://github.com/sgl-project/sglang/commit/64c7c6851b) [#23476](https://github.com/sgl-project/sglang/pull/23476)
  fix(tool_call): normalize non-standard JSON Schema types in tool params (#23476)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/function_call/utils.py`, `test/registered/unit/function_call/test_normalize_json_schema_types.py`_

## LoRA  (3 commits)

- **2026-05-31** [`e188745ee0`](https://github.com/sgl-project/sglang/commit/e188745ee0) [#26810](https://github.com/sgl-project/sglang/pull/26810)
  Add KV-canary SWA + DeepSeek-V4 pool support (#26810)
  _Files: `python/sglang/srt/kv_canary/pool_patcher/adapters/dsv4.py`, `python/sglang/srt/kv_canary/pool_patcher/adapters/swa.py`, `python/sglang/srt/kv_canary/pool_patcher/api.py`, `python/sglang/test/kv_canary/consts.py` _+6 more__
- **2026-05-30** [`95cd2fd29f`](https://github.com/sgl-project/sglang/commit/95cd2fd29f) [#20876](https://github.com/sgl-project/sglang/pull/20876)
  [lora] More efficient pinned memory (#20876)
  _Files: `python/sglang/srt/lora/lora.py`, `python/sglang/srt/lora/lora_manager.py`, `python/sglang/srt/lora/mem_pool.py`, `python/sglang/srt/lora/utils.py` _+1 more__
- **2026-05-25** [`87e69d57c4`](https://github.com/sgl-project/sglang/commit/87e69d57c4) [#25413](https://github.com/sgl-project/sglang/pull/25413)
  [lora] Fix overlap loading for cancelled requests (#25413)
  _Files: `python/sglang/srt/lora/lora_overlap_loader.py`, `test/registered/lora/test_lora_overlap_loading.py`_

---
_Generated 2026-06-01 13:45 UTC_