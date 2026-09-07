# vllm-project/vllm — Weekly Change Report
**Period:** 2026-08-31 → 2026-09-07  |  **Total commits:** 370

## ✨ New Features This Week

- **2026-09-07** [#50195](https://github.com/vllm-project/vllm/pull/50195) — [Frontend] Add stateless /v1/responses/render endpoint (#50195)
- **2026-09-07** [#54890](https://github.com/vllm-project/vllm/pull/54890) — [Qwen3.8-Flash-Next] Support FP8 indexer cache for QSA (#54890)
- **2026-09-07** [#55691](https://github.com/vllm-project/vllm/pull/55691) — [Docs] Add OLMo 2 to batch-invariance tested models (#55691)
- **2026-09-07** [#53689](https://github.com/vllm-project/vllm/pull/53689) — [XPU][LoRA] Support LoRA for DeepSeek V4 on XPU (#53689)
- **2026-09-07** [#54404](https://github.com/vllm-project/vllm/pull/54404) — [ROCm][CI] Add attention-sink support to ROCm AITER sparse MLA (#54404)
- **2026-09-07** [#55653](https://github.com/vllm-project/vllm/pull/55653) — [CI][ROCm] Temporarily skip unsupported HY-V4 initialization (#55653)
- **2026-09-07** [#41567](https://github.com/vllm-project/vllm/pull/41567) — [EPD] Add ECMooncakeConnector for encoder cache over Mooncake TransferEngine (#41567)
- **2026-09-07** [#55272](https://github.com/vllm-project/vllm/pull/55272) — [Qwen3.8-Flash-Next] Remove torch.compile for NVIDIA implementation (#55272)
- **2026-09-07** [#52890](https://github.com/vllm-project/vllm/pull/52890) — add 2/3/5/6/7 CUDA support in AutoRound format (#52890)
- **2026-09-07** [#55535](https://github.com/vllm-project/vllm/pull/55535) — [Kernel] Remove unused fake implementation (#55535)
- _…and 65 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-09-07** [`e476556189`](https://github.com/vllm-project/vllm/commit/e476556189) [#54404](https://github.com/vllm-project/vllm/pull/54404) — [ROCm][CI] Add attention-sink support to ROCm AITER sparse MLA (#54404)
- **2026-09-07** [`195bc9c4a1`](https://github.com/vllm-project/vllm/commit/195bc9c4a1) [#55653](https://github.com/vllm-project/vllm/pull/55653) — [CI][ROCm] Temporarily skip unsupported HY-V4 initialization (#55653)
- **2026-09-07** [`1f778486fc`](https://github.com/vllm-project/vllm/commit/1f778486fc) [#54975](https://github.com/vllm-project/vllm/pull/54975) — [Bugfix][Offloader] Preserve prefetch static-buffer slot ownership (#54975)
- **2026-09-07** [`de69e821b7`](https://github.com/vllm-project/vllm/commit/de69e821b7) [#53161](https://github.com/vllm-project/vllm/pull/53161) — [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts (#53161)
- **2026-09-07** [`199cb9b964`](https://github.com/vllm-project/vllm/commit/199cb9b964) [#55535](https://github.com/vllm-project/vllm/pull/55535) — [Kernel] Remove unused fake implementation (#55535)
- **2026-09-05** [`d4ef5e53fc`](https://github.com/vllm-project/vllm/commit/d4ef5e53fc) [#55409](https://github.com/vllm-project/vllm/pull/55409) — [CI][ROCm] Disable Transformers nightly groups (#55409)
- **2026-09-05** [`ea5f41edd7`](https://github.com/vllm-project/vllm/commit/ea5f41edd7) [#55410](https://github.com/vllm-project/vllm/pull/55410) — [CI][ROCm] Restore Wikitext coverage for Qwen OCP-MX (#55410)
- **2026-09-05** [`a7f9be9612`](https://github.com/vllm-project/vllm/commit/a7f9be9612) [#55308](https://github.com/vllm-project/vllm/pull/55308) — [CI][ROCm] Raise AMD job and server readiness timeouts (#55308)
- **2026-09-05** [`385ba6b5b0`](https://github.com/vllm-project/vllm/commit/385ba6b5b0) [#54770](https://github.com/vllm-project/vllm/pull/54770) — [Bugfix][Quantization] Register Quark per-block FP8 scales as weight_scale (#54770)
- **2026-09-05** [`8277c42e4c`](https://github.com/vllm-project/vllm/commit/8277c42e4c) [#55202](https://github.com/vllm-project/vllm/pull/55202) — [Perf] Ensure async h2d copies are pinned in more places (#55202)
- **2026-09-04** [`701a744490`](https://github.com/vllm-project/vllm/commit/701a744490) [#55136](https://github.com/vllm-project/vllm/pull/55136) — [CI] Raise AMD Spec Decode Eagle 1 job timeout to 35min (#55136)
- **2026-09-04** [`99a1ab8e4c`](https://github.com/vllm-project/vllm/commit/99a1ab8e4c) [#55354](https://github.com/vllm-project/vllm/pull/55354) — [ROCm][CI] Bump ROCk release image build timeout to 3h (#55354)
- **2026-09-04** [`3ff4f02dfe`](https://github.com/vllm-project/vllm/commit/3ff4f02dfe) [#52494](https://github.com/vllm-project/vllm/pull/52494) — [AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper (#52494)
- **2026-09-04** [`78300cdabf`](https://github.com/vllm-project/vllm/commit/78300cdabf) [#55214](https://github.com/vllm-project/vllm/pull/55214) — [Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings (#55214)
- **2026-09-04** [`156050598e`](https://github.com/vllm-project/vllm/commit/156050598e) [#55246](https://github.com/vllm-project/vllm/pull/55246) — [ROCm][CI] Bump ROCk base to ROCm 10.0 (#55246)
- **2026-09-04** [`7dc30f5a66`](https://github.com/vllm-project/vllm/commit/7dc30f5a66) [#55014](https://github.com/vllm-project/vllm/pull/55014) — [ROCm][CI] Build and publish TheRock nightly docker images (#55014)
- **2026-09-03** [`579aef4e8d`](https://github.com/vllm-project/vllm/commit/579aef4e8d) [#52826](https://github.com/vllm-project/vllm/pull/52826) — [ROCm] Bump AITER to 0.1.21.post1 (#52826)
- **2026-09-03** [`cee0f92c02`](https://github.com/vllm-project/vllm/commit/cee0f92c02) [#54682](https://github.com/vllm-project/vllm/pull/54682) — [ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k (#54682)
- **2026-09-03** [`8bf39632b8`](https://github.com/vllm-project/vllm/commit/8bf39632b8) [#54845](https://github.com/vllm-project/vllm/pull/54845) — [ROCm][Perf] Add low-M FP32 router GEMM for gfx950 (#54845)
- **2026-09-03** [`98ed0856f3`](https://github.com/vllm-project/vllm/commit/98ed0856f3) [#53906](https://github.com/vllm-project/vllm/pull/53906) — [Model] add GLM-5.3-Flash support (#53906)
- **2026-09-03** [`4cc0cb6f76`](https://github.com/vllm-project/vllm/commit/4cc0cb6f76) [#55094](https://github.com/vllm-project/vllm/pull/55094) — [CI][AMD] Avoid expandable segments in LoRA TP tests (#55094)
- **2026-09-03** [`e6eb9074e9`](https://github.com/vllm-project/vllm/commit/e6eb9074e9) [#53905](https://github.com/vllm-project/vllm/pull/53905) — [CI] Bump Transformers version to 5.16.1 (#53905)
- **2026-09-03** [`096d8e8ce6`](https://github.com/vllm-project/vllm/commit/096d8e8ce6) [#55057](https://github.com/vllm-project/vllm/pull/55057) — [ROCm][CI] Add MiniMax reduce RMS kernel coverage (#55057)
- **2026-09-03** [`5d09eb2cf3`](https://github.com/vllm-project/vllm/commit/5d09eb2cf3) [#46009](https://github.com/vllm-project/vllm/pull/46009) — [Bugfix][MoE] Preserve unquantized weight storage on ROCm (#46009)
- **2026-09-03** [`e47356c63e`](https://github.com/vllm-project/vllm/commit/e47356c63e) [#55002](https://github.com/vllm-project/vllm/pull/55002) — [ROCm][Installation] Add mooncake package to image using public wheels (#55002)
- **2026-09-02** [`e3e1241003`](https://github.com/vllm-project/vllm/commit/e3e1241003) [#55011](https://github.com/vllm-project/vllm/pull/55011) — [ROCm][CI] Extend Multimodal Processor Shard timeout on AMD CI (#55011)
- **2026-09-02** [`0e3ac4907d`](https://github.com/vllm-project/vllm/commit/0e3ac4907d) [#54989](https://github.com/vllm-project/vllm/pull/54989) — [ROCm][CI] Fix false multi-node detection on native CI (#54989)
- **2026-09-02** [`3e9d364ff7`](https://github.com/vllm-project/vllm/commit/3e9d364ff7) [#54984](https://github.com/vllm-project/vllm/pull/54984) — [CI/Build][ROCm] Guard the two CUDA-only tests in test_bf16_skinny_gemm (#54984)
- **2026-09-02** [`bf7a14d307`](https://github.com/vllm-project/vllm/commit/bf7a14d307) [#54852](https://github.com/vllm-project/vllm/pull/54852) — [CI][ROCm] Add DSpark evals (#54852)
- **2026-09-02** [`d539de1c5d`](https://github.com/vllm-project/vllm/commit/d539de1c5d) [#54980](https://github.com/vllm-project/vllm/pull/54980) — [Docs] Add missing return annotations flagged by griffe (#54980)
- **2026-09-02** [`b205750fe0`](https://github.com/vllm-project/vllm/commit/b205750fe0) [#54171](https://github.com/vllm-project/vllm/pull/54171) — [Bugfix][ROCm][Build] fix profiler hang due to queue interposition bug (#54171)
- **2026-09-02** [`c6005000d3`](https://github.com/vllm-project/vllm/commit/c6005000d3) [#54898](https://github.com/vllm-project/vllm/pull/54898) — [CI][ROCm] Prefetch safetensors weights in AMD CI (#54898)
- **2026-09-02** [`e52407ef4c`](https://github.com/vllm-project/vllm/commit/e52407ef4c) [#53399](https://github.com/vllm-project/vllm/pull/53399) — [ROCm][CI] Add MTP and other spec-decode acceptance coverage (#53399)
- **2026-09-02** [`01eeb798b6`](https://github.com/vllm-project/vllm/commit/01eeb798b6) [#53437](https://github.com/vllm-project/vllm/pull/53437) — [CI][AMD] Preserve diagnostics for unwritable checkouts (#53437)
- **2026-09-02** [`56b5495377`](https://github.com/vllm-project/vllm/commit/56b5495377) [#52650](https://github.com/vllm-project/vllm/pull/52650) — [ROCm][AMD][Installation] Add mooncake build to rocm base image (#52650)
- **2026-09-02** [`73029d4244`](https://github.com/vllm-project/vllm/commit/73029d4244) [#54695](https://github.com/vllm-project/vllm/pull/54695) — [CI][ROCm] Calibrate AMD test timeouts from nightly runtimes (#54695)
- **2026-09-01** [`e01d4acbb1`](https://github.com/vllm-project/vllm/commit/e01d4acbb1) [#52679](https://github.com/vllm-project/vllm/pull/52679) — [ROCm][CI] Handle tied experts in softplus sqrt top-k test (#52679)
- **2026-09-01** [`73723b707f`](https://github.com/vllm-project/vllm/commit/73723b707f) [#54773](https://github.com/vllm-project/vllm/pull/54773) — [ROCm][MoE] Fix gfx950 block scale swizzle for AITER Triton MXFP4 W4A16 (#54773)
- **2026-09-01** [`c0adee9231`](https://github.com/vllm-project/vllm/commit/c0adee9231) [#53279](https://github.com/vllm-project/vllm/pull/53279) — [ROCm][CI] Add ROCm misc ops and env tests (#53279)
- **2026-09-01** [`d1c15e589d`](https://github.com/vllm-project/vllm/commit/d1c15e589d) [#53291](https://github.com/vllm-project/vllm/pull/53291) — [CI] Speed up quantization test group (#53291)
- **2026-09-01** [`339e16cbb6`](https://github.com/vllm-project/vllm/commit/339e16cbb6) [#53870](https://github.com/vllm-project/vllm/pull/53870) — [Bugfix] Support MCP SDK 2.x tool input schemas (#53870)
- **2026-09-01** [`754d5e1f65`](https://github.com/vllm-project/vllm/commit/754d5e1f65) [#54750](https://github.com/vllm-project/vllm/pull/54750) — [CI/Build] Fix entrypoints coverage (#54750)
- **2026-09-01** [`8f03625b3d`](https://github.com/vllm-project/vllm/commit/8f03625b3d) [#44834](https://github.com/vllm-project/vllm/pull/44834) — [CPU][Zen] Route Int8 MoE inference through zentorch on AMD (#44834)
- **2026-09-01** [`b65af5e339`](https://github.com/vllm-project/vllm/commit/b65af5e339) [#54037](https://github.com/vllm-project/vllm/pull/54037) — [CI][ROCm] Expand weight loading test coverage on AMD and cap its KV cache (#54037)
- **2026-09-01** [`40b2f62061`](https://github.com/vllm-project/vllm/commit/40b2f62061) [#54403](https://github.com/vllm-project/vllm/pull/54403) — [ROCm][CI] Stabilize the sqrt-softplus top-k tie oracle (#54403)
- **2026-09-01** [`ce2e343be1`](https://github.com/vllm-project/vllm/commit/ce2e343be1) [#53155](https://github.com/vllm-project/vllm/pull/53155) — [ROCm] Keep GLM-5.2 on MRV1 and disable default breakable cudagraph (#53155)
- **2026-09-01** [`dc9114b201`](https://github.com/vllm-project/vllm/commit/dc9114b201) [#50622](https://github.com/vllm-project/vllm/pull/50622) — [ROCm][MoE] Split AITER CK and Triton MXFP4 W4A16 into separate backends (#50622)
- **2026-09-01** [`907b1a7f22`](https://github.com/vllm-project/vllm/commit/907b1a7f22) [#54408](https://github.com/vllm-project/vllm/pull/54408) — [CI][ROCm] Avoid redundant image pulls during smoke validation (#54408)
- **2026-08-31** [`2ba984a5d0`](https://github.com/vllm-project/vllm/commit/2ba984a5d0) [#53598](https://github.com/vllm-project/vllm/pull/53598) — [ROCm][DSpark][DCP] Serve prefix cache hits under DCP for Kimi-K3 (#53598)
- **2026-08-31** [`dbb7fffddb`](https://github.com/vllm-project/vllm/commit/dbb7fffddb) [#51705](https://github.com/vllm-project/vllm/pull/51705) — [ROCm][MLA][DCP] Support causal multi-token verification (#51705)
- **2026-08-31** [`3593c964de`](https://github.com/vllm-project/vllm/commit/3593c964de) [#49925](https://github.com/vllm-project/vllm/pull/49925) — [ROCm] Add TheRock preview docker updates, Keep Python 3.12 and Ubuntu 22.04 (#49925)
- **2026-08-31** [`76ff0cdff2`](https://github.com/vllm-project/vllm/commit/76ff0cdff2) [#53821](https://github.com/vllm-project/vllm/pull/53821) — [Bugfix][ROCm] Preserve AITER unified-attention metadata during graph replay (#53821)
- **2026-08-31** [`f9d666f917`](https://github.com/vllm-project/vllm/commit/f9d666f917) [#52067](https://github.com/vllm-project/vllm/pull/52067) — [KV Offload] Forward ownership in KV cache events (#52067)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#55722](https://github.com/vllm-project/vllm/issues/55722) | [Bug]: `fuse_attn_quant` without `use_inductor_graph_partition` drops  | rocm | 2026-09-07 |
| [#55720](https://github.com/vllm-project/vllm/issues/55720) | [Bug]: `fuse_rope_kvcache` / `fuse_qk_norm_rope_kvcache` silently regi | rocm | 2026-09-07 |
| [#55725](https://github.com/vllm-project/vllm/issues/55725) | [Bug]: Weight loading error on GLM-5.3-Flash (`KeyError: 'layers.11.sh | bug, glm | 2026-09-07 |
| [#55733](https://github.com/vllm-project/vllm/issues/55733) | [Bug]: Encoder-decoder encoder-cache budget (num_free_slots) inflates  | bug | 2026-09-07 |
| [#36456](https://github.com/vllm-project/vllm/issues/36456) | [Bug]: Local GGUF path fails with "architecture qwen35 is not supporte | bug | 2026-09-07 |
| [#55689](https://github.com/vllm-project/vllm/issues/55689) | [Bug]: GLM-5.3-Flash produces repetitive / off‑topic outputs in PD‑dis | bug, kv-connector, glm | 2026-09-07 |
| [#55697](https://github.com/vllm-project/vllm/issues/55697) | [RFC]: Application-Directed Prefix Checkpoints for Mamba / Hybrid Pref | kv-cache-manager | 2026-09-07 |
| [#38256](https://github.com/vllm-project/vllm/issues/38256) | [RFC]: Incremental MoE Expert Offloading — GPU Cache + Async Pipeline | — | 2026-09-07 |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | [Feature]: Batch Invariant Feature and Performance Optimization | good first issue, feature request | 2026-09-07 |
| [#54521](https://github.com/vllm-project/vllm/issues/54521) | [Bug]: Qwen3.8-Flash-Next: greedy decoding is non-deterministic from p | quantization | 2026-09-07 |
| [#54749](https://github.com/vllm-project/vllm/issues/54749) | [RFC]: The dynamic-SD K decision is a batch-keyed array index — agreei | — | 2026-09-07 |
| [#49011](https://github.com/vllm-project/vllm/issues/49011) | [Feature]: nvfp4 KV cache on SM120 — flashinfer ships the kernels, vLL | — | 2026-09-07 |
| [#53863](https://github.com/vllm-project/vllm/issues/53863) | [Bug]: Out-of-bounds attrIdxs in the C++ batch memcpy path (cache_kern | bug | 2026-09-07 |
| [#52409](https://github.com/vllm-project/vllm/issues/52409) | EPD (EC connector) Tracker | — | 2026-09-07 |
| [#55571](https://github.com/vllm-project/vllm/issues/55571) | [Bug]: Xid 13 "Out Of Range Address" / CUDA illegal memory access on R | bug, quantization | 2026-09-07 |
| [#55626](https://github.com/vllm-project/vllm/issues/55626) | [Bug]: GLM-5.3-Flash: CUDA illegal memory access in FlashInfer SM90 sp | bug, rocm, glm | 2026-09-07 |
| [#55345](https://github.com/vllm-project/vllm/issues/55345) | [Bug][ROCm] QuickReduce converts bf16 to fp16 without saturation: acti | rocm, quantization | 2026-09-07 |
| [#55633](https://github.com/vllm-project/vllm/issues/55633) | [Bug]: legacy qwen3_xml streaming parser emits whitespace-only content | bug, tool-calling | 2026-09-07 |
| [#52089](https://github.com/vllm-project/vllm/issues/52089) | [Bug]: Continuous Host Memory Growth / Possible Memory Leak with V2 Ru | bug | 2026-09-07 |
| [#55632](https://github.com/vllm-project/vllm/issues/55632) | [Bug][ROCm] 15s EngineCore cleanup grace is defeated by MultiprocExecu | rocm | 2026-09-07 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 53 |
| Attention | 52 |
| MoE / Expert Parallel | 32 |
| Multimodal | 32 |
| Other | 28 |
| CI / Build | 27 |
| Models | 22 |
| Disaggregation / PD | 22 |
| Quantization | 20 |
| Scheduler / Engine | 19 |
| Serving / API | 16 |
| KV Cache / Offload | 15 |
| Perf / Benchmark | 10 |
| Speculative Decoding | 8 |
| LoRA | 5 |
| Compilation / CUDA Graph | 5 |
| Docs | 4 |

## ROCm / AMD  (53 commits)

- **2026-09-07** [`e476556189`](https://github.com/vllm-project/vllm/commit/e476556189) [#54404](https://github.com/vllm-project/vllm/pull/54404)
  [ROCm][CI] Add attention-sink support to ROCm AITER sparse MLA (#54404)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_op_registration.py`, `tests/kernels/attention/test_rocm_aiter_mla_sink.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `tests/v1/attention/test_rocm_glm5next_sparse.py` _+4 more__
- **2026-09-07** [`195bc9c4a1`](https://github.com/vllm-project/vllm/commit/195bc9c4a1) [#55653](https://github.com/vllm-project/vllm/pull/55653)
  [CI][ROCm] Temporarily skip unsupported HY-V4 initialization (#55653)
  _Files: `tests/models/test_initialization.py`_
- **2026-09-07** [`1f778486fc`](https://github.com/vllm-project/vllm/commit/1f778486fc) [#54975](https://github.com/vllm-project/vllm/pull/54975)
  [Bugfix][Offloader] Preserve prefetch static-buffer slot ownership (#54975)
  _Files: `tests/model_executor/offloader/test_prefetch.py`, `vllm/model_executor/offloader/prefetch.py`_
- **2026-09-07** [`de69e821b7`](https://github.com/vllm-project/vllm/commit/de69e821b7) [#53161](https://github.com/vllm-project/vllm/pull/53161)
  [ROCm][Perf][DeepSeek V4] Fuse native FP8 shared expert with MXFP4 routed experts (#53161)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/_aiter_ops.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/models/deepseek_v4/amd/model.py`_
- **2026-09-07** [`199cb9b964`](https://github.com/vllm-project/vllm/commit/199cb9b964) [#55535](https://github.com/vllm-project/vllm/pull/55535)
  [Kernel] Remove unused fake implementation (#55535)
  _Files: `vllm/_aiter_ops.py`, `vllm/_custom_ops.py`, `vllm/_xpu_ops.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py` _+35 more__
- **2026-09-05** [`d4ef5e53fc`](https://github.com/vllm-project/vllm/commit/d4ef5e53fc) [#55409](https://github.com/vllm-project/vllm/pull/55409)
  [CI][ROCm] Disable Transformers nightly groups (#55409)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-05** [`ea5f41edd7`](https://github.com/vllm-project/vllm/commit/ea5f41edd7) [#55410](https://github.com/vllm-project/vllm/pull/55410)
  [CI][ROCm] Restore Wikitext coverage for Qwen OCP-MX (#55410)
  _Files: `tests/evals/gsm8k/configs/Qwen-1.5-MOE-W-MXFP4-A-MXFP6.yaml`, `tests/evals/gsm8k/configs/Qwen-1.5-MOE-W-MXFP6-A-MXFP6.yaml`, `tests/evals/gsm8k/configs/models-gfx950-large.txt`, `tests/evals/gsm8k/configs/models-mi3xx.txt` _+1 more__
- **2026-09-05** [`a7f9be9612`](https://github.com/vllm-project/vllm/commit/a7f9be9612) [#55308](https://github.com/vllm-project/vllm/pull/55308)
  [CI][ROCm] Raise AMD job and server readiness timeouts (#55308)
  _Files: `.buildkite/scripts/scheduled_integration_test/deepseek_v2_lite_ep_eplb.sh`, `.buildkite/scripts/scheduled_integration_test/qwen3_next_mtp_async_eplb.sh`, `.buildkite/test-amd.yaml`, `tests/v1/distributed/test_internal_lb_dp.py`_
- **2026-09-05** [`385ba6b5b0`](https://github.com/vllm-project/vllm/commit/385ba6b5b0) [#54770](https://github.com/vllm-project/vllm/pull/54770)
  [Bugfix][Quantization] Register Quark per-block FP8 scales as weight_scale (#54770)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_fp8.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`, `vllm/models/deepseek_v4/amd/model.py` _+3 more__
- **2026-09-05** [`8277c42e4c`](https://github.com/vllm-project/vllm/commit/8277c42e4c) [#55202](https://github.com/vllm-project/vllm/pull/55202)
  [Perf] Ensure async h2d copies are pinned in more places (#55202)
  _Files: `tests/kernels/attention/test_flashinfer.py`, `vllm/distributed/eplb/eplb_state.py`, `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+17 more__
- **2026-09-04** [`701a744490`](https://github.com/vllm-project/vllm/commit/701a744490) [#55136](https://github.com/vllm-project/vllm/pull/55136)
  [CI] Raise AMD Spec Decode Eagle 1 job timeout to 35min (#55136)
  _Files: `.buildkite/test_areas/spec_decode.yaml`_
- **2026-09-04** [`99a1ab8e4c`](https://github.com/vllm-project/vllm/commit/99a1ab8e4c) [#55354](https://github.com/vllm-project/vllm/pull/55354)
  [ROCm][CI] Bump ROCk release image build timeout to 3h (#55354)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-09-04** [`3ff4f02dfe`](https://github.com/vllm-project/vllm/commit/3ff4f02dfe) [#52494](https://github.com/vllm-project/vllm/pull/52494)
  [AMD][kimik3][ROCm][Perf] Fuse MLA q/kv RMSNorm in AMD Kimi-K3 MLA wrapper (#52494)
  _Files: `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/mla.py`_
- **2026-09-04** [`78300cdabf`](https://github.com/vllm-project/vllm/commit/78300cdabf) [#55214](https://github.com/vllm-project/vllm/pull/55214)
  [Bugfix][Docs] Package glm5next nvidia subtree and fix its docstrings (#55214)
  _Files: `vllm/models/glm5next/amd/ops/kpool_compress.py`, `vllm/models/glm5next/nvidia/__init__.py`, `vllm/models/glm5next/nvidia/ops/__init__.py`, `vllm/models/glm5next/nvidia/ops/kpool_compress.py`_
- **2026-09-04** [`156050598e`](https://github.com/vllm-project/vllm/commit/156050598e) [#55246](https://github.com/vllm-project/vllm/pull/55246)
  [ROCm][CI] Bump ROCk base to ROCm 10.0 (#55246)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile.rock_base`_
- **2026-09-04** [`7dc30f5a66`](https://github.com/vllm-project/vllm/commit/7dc30f5a66) [#55014](https://github.com/vllm-project/vllm/pull/55014)
  [ROCm][CI] Build and publish TheRock nightly docker images (#55014)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/push-nightly-builds-rocm.sh`_
- **2026-09-03** [`579aef4e8d`](https://github.com/vllm-project/vllm/commit/579aef4e8d) [#52826](https://github.com/vllm-project/vllm/pull/52826)
  [ROCm] Bump AITER to 0.1.21.post1 (#52826)
  _Files: `docker/Dockerfile.rocm_base`, `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/model_executor/layers/fused_moe/fused_flydsl_moe.py`_
- **2026-09-03** [`cee0f92c02`](https://github.com/vllm-project/vllm/commit/cee0f92c02) [#54682](https://github.com/vllm-project/vllm/pull/54682)
  [ROCm][Perf] Optimize MiniMax-M3 decode indexer and top-k (#54682)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/index_topk.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py` _+2 more__
- **2026-09-03** [`8bf39632b8`](https://github.com/vllm-project/vllm/commit/8bf39632b8) [#54845](https://github.com/vllm-project/vllm/pull/54845)
  [ROCm][Perf] Add low-M FP32 router GEMM for gfx950 (#54845)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/test_gate_linear_rocm_dispatch.py`, `tests/kernels/test_rocm_fp32_router_gemm.py`, `vllm/model_executor/layers/fused_moe/router/gate_linear.py` _+1 more__
- **2026-09-03** [`98ed0856f3`](https://github.com/vllm-project/vllm/commit/98ed0856f3) [#53906](https://github.com/vllm-project/vllm/pull/53906)
  [Model] add GLM-5.3-Flash support (#53906)
  _Files: `.buildkite/test_areas/kernels.yaml`, `csrc/libtorch_stable/cache_kernels.cu`, `tests/kernels/attention/test_flashinfer_mla_decode.py`, `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py` _+90 more__
- **2026-09-03** [`4cc0cb6f76`](https://github.com/vllm-project/vllm/commit/4cc0cb6f76) [#55094](https://github.com/vllm-project/vllm/pull/55094)
  [CI][AMD] Avoid expandable segments in LoRA TP tests (#55094)
  _Files: `.buildkite/test_areas/lora.yaml`_
- **2026-09-03** [`e6eb9074e9`](https://github.com/vllm-project/vllm/commit/e6eb9074e9) [#53905](https://github.com/vllm-project/vllm/pull/53905)
  [CI] Bump Transformers version to 5.16.1 (#53905)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+4 more__
- **2026-09-03** [`096d8e8ce6`](https://github.com/vllm-project/vllm/commit/096d8e8ce6) [#55057](https://github.com/vllm-project/vllm/pull/55057)
  [ROCm][CI] Add MiniMax reduce RMS kernel coverage (#55057)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/core/test_minimax_reduce_rms.py`_
- **2026-09-03** [`5d09eb2cf3`](https://github.com/vllm-project/vllm/commit/5d09eb2cf3) [#46009](https://github.com/vllm-project/vllm/pull/46009)
  [Bugfix][MoE] Preserve unquantized weight storage on ROCm (#46009)
  _Files: `.buildkite/test-amd.yaml`, `tests/rocm/test_moe_weight_replay.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`_
- **2026-09-03** [`e47356c63e`](https://github.com/vllm-project/vllm/commit/e47356c63e) [#55002](https://github.com/vllm-project/vllm/pull/55002)
  [ROCm][Installation] Add mooncake package to image using public wheels (#55002)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`, `docker/ci-rocm.hcl`, `requirements/rocm.txt`_
- **2026-09-02** [`e3e1241003`](https://github.com/vllm-project/vllm/commit/e3e1241003) [#55011](https://github.com/vllm-project/vllm/pull/55011)
  [ROCm][CI] Extend Multimodal Processor Shard timeout on AMD CI (#55011)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-02** [`0e3ac4907d`](https://github.com/vllm-project/vllm/commit/0e3ac4907d) [#54989](https://github.com/vllm-project/vllm/pull/54989)
  [ROCm][CI] Fix false multi-node detection on native CI (#54989)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-09-02** [`3e9d364ff7`](https://github.com/vllm-project/vllm/commit/3e9d364ff7) [#54984](https://github.com/vllm-project/vllm/pull/54984)
  [CI/Build][ROCm] Guard the two CUDA-only tests in test_bf16_skinny_gemm (#54984)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`_
- **2026-09-02** [`bf7a14d307`](https://github.com/vllm-project/vllm/commit/bf7a14d307) [#54852](https://github.com/vllm-project/vllm/pull/54852)
  [CI][ROCm] Add DSpark evals (#54852)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-AITER-TEP4.yaml`, `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-AITER-TP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode-rocm.txt`_
- **2026-09-02** [`d539de1c5d`](https://github.com/vllm-project/vllm/commit/d539de1c5d) [#54980](https://github.com/vllm-project/vllm/pull/54980)
  [Docs] Add missing return annotations flagged by griffe (#54980)
  _Files: `vllm/_aiter_ops.py`, `vllm/_custom_ops.py`, `vllm/model_executor/determinism/batch_invariant.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-09-02** [`b205750fe0`](https://github.com/vllm-project/vllm/commit/b205750fe0) [#54171](https://github.com/vllm-project/vllm/pull/54171)
  [Bugfix][ROCm][Build] fix profiler hang due to queue interposition bug (#54171)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-09-02** [`c6005000d3`](https://github.com/vllm-project/vllm/commit/c6005000d3) [#54898](https://github.com/vllm-project/vllm/pull/54898)
  [CI][ROCm] Prefetch safetensors weights in AMD CI (#54898)
  _Files: `.buildkite/lm-eval-harness/configs/Meta-Llama-4-Maverick-17B-128E-Instruct-FP8.yaml`, `tests/weight_loading/models-amd.txt`, `tests/weight_loading/models-large-amd.txt`, `tests/weight_loading/run_model_weight_loading_test.sh` _+1 more__
- **2026-09-02** [`e52407ef4c`](https://github.com/vllm-project/vllm/commit/e52407ef4c) [#53399](https://github.com/vllm-project/vllm/pull/53399)
  [ROCm][CI] Add MTP and other spec-decode acceptance coverage (#53399)
  _Files: `.buildkite/test-amd.yaml`, `vllm/v1/spec_decode/gemma4.py`_
- **2026-09-02** [`01eeb798b6`](https://github.com/vllm-project/vllm/commit/01eeb798b6) [#53437](https://github.com/vllm-project/vllm/pull/53437)
  [CI][AMD] Preserve diagnostics for unwritable checkouts (#53437)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-09-02** [`56b5495377`](https://github.com/vllm-project/vllm/commit/56b5495377) [#52650](https://github.com/vllm-project/vllm/pull/52650)
  [ROCm][AMD][Installation] Add mooncake build to rocm base image (#52650)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`, `docker/ci-rocm.hcl`_
- **2026-09-02** [`73029d4244`](https://github.com/vllm-project/vllm/commit/73029d4244) [#54695](https://github.com/vllm-project/vllm/pull/54695)
  [CI][ROCm] Calibrate AMD test timeouts from nightly runtimes (#54695)
  _Files: `.buildkite/test-amd.yaml`_
- **2026-09-01** [`e01d4acbb1`](https://github.com/vllm-project/vllm/commit/e01d4acbb1) [#52679](https://github.com/vllm-project/vllm/pull/52679)
  [ROCm][CI] Handle tied experts in softplus sqrt top-k test (#52679)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`_
- **2026-09-01** [`73723b707f`](https://github.com/vllm-project/vllm/commit/73723b707f) [#54773](https://github.com/vllm-project/vllm/pull/54773)
  [ROCm][MoE] Fix gfx950 block scale swizzle for AITER Triton MXFP4 W4A16 (#54773)
  _Files: `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py`_
- **2026-09-01** [`c0adee9231`](https://github.com/vllm-project/vllm/commit/c0adee9231) [#53279](https://github.com/vllm-project/vllm/pull/53279)
  [ROCm][CI] Add ROCm misc ops and env tests (#53279)
  _Files: `tests/kernels/core/test_rocm_misc_ops.py`_
- **2026-09-01** [`d1c15e589d`](https://github.com/vllm-project/vllm/commit/d1c15e589d) [#53291](https://github.com/vllm-project/vllm/pull/53291)
  [CI] Speed up quantization test group (#53291)
  _Files: `tests/evals/gsm8k/configs/Qwen-1.5-MOE-W-MXFP4-A-MXFP6.yaml`, `tests/evals/gsm8k/configs/Qwen-1.5-MOE-W-MXFP6-A-MXFP6.yaml`, `tests/evals/gsm8k/configs/Qwen3-30B-A3B-NVFP4-quark.yaml`, `tests/evals/gsm8k/configs/models-gfx950-large.txt` _+16 more__
- **2026-09-01** [`339e16cbb6`](https://github.com/vllm-project/vllm/commit/339e16cbb6) [#53870](https://github.com/vllm-project/vllm/pull/53870)
  [Bugfix] Support MCP SDK 2.x tool input schemas (#53870)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+3 more__
- **2026-09-01** [`754d5e1f65`](https://github.com/vllm-project/vllm/commit/754d5e1f65) [#54750](https://github.com/vllm-project/vllm/pull/54750)
  [CI/Build] Fix entrypoints coverage (#54750)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/unit_tests/test_offline_utils.py`_
- **2026-09-01** [`8f03625b3d`](https://github.com/vllm-project/vllm/commit/8f03625b3d) [#44834](https://github.com/vllm-project/vllm/pull/44834)
  [CPU][Zen] Route Int8 MoE inference through zentorch on AMD (#44834)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/kernels/moe/test_zen_cpu_int8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int8.py` _+2 more__
- **2026-09-01** [`b65af5e339`](https://github.com/vllm-project/vllm/commit/b65af5e339) [#54037](https://github.com/vllm-project/vllm/pull/54037)
  [CI][ROCm] Expand weight loading test coverage on AMD and cap its KV cache (#54037)
  _Files: `.buildkite/test_areas/weight_loading.yaml`, `tests/weight_loading/models-amd.txt`, `tests/weight_loading/test_weight_loading.py`_
- **2026-09-01** [`40b2f62061`](https://github.com/vllm-project/vllm/commit/40b2f62061) [#54403](https://github.com/vllm-project/vllm/pull/54403)
  [ROCm][CI] Stabilize the sqrt-softplus top-k tie oracle (#54403)
  _Files: `tests/kernels/moe/test_topk_softplus_sqrt.py`_
- **2026-09-01** [`ce2e343be1`](https://github.com/vllm-project/vllm/commit/ce2e343be1) [#53155](https://github.com/vllm-project/vllm/pull/53155)
  [ROCm] Keep GLM-5.2 on MRV1 and disable default breakable cudagraph (#53155)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-09-01** [`dc9114b201`](https://github.com/vllm-project/vllm/commit/dc9114b201) [#50622](https://github.com/vllm-project/vllm/pull/50622)
  [ROCm][MoE] Split AITER CK and Triton MXFP4 W4A16 into separate backends (#50622)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/models/quantization/test_gpt_oss.py`, `vllm/config/kernel.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a16_moe.py` _+2 more__
- **2026-09-01** [`907b1a7f22`](https://github.com/vllm-project/vllm/commit/907b1a7f22) [#54408](https://github.com/vllm-project/vllm/pull/54408)
  [CI][ROCm] Avoid redundant image pulls during smoke validation (#54408)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/rocm/smoke-test-image.sh`, `docker/Dockerfile.rocm`, `docker/ci-rocm.hcl` _+1 more__
- **2026-08-31** [`2ba984a5d0`](https://github.com/vllm-project/vllm/commit/2ba984a5d0) [#53598](https://github.com/vllm-project/vllm/pull/53598)
  [ROCm][DSpark][DCP] Serve prefix cache hits under DCP for Kimi-K3 (#53598)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/kv_cache_coordinator.py` _+2 more__
- **2026-08-31** [`dbb7fffddb`](https://github.com/vllm-project/vllm/commit/dbb7fffddb) [#51705](https://github.com/vllm-project/vllm/pull/51705)
  [ROCm][MLA][DCP] Support causal multi-token verification (#51705)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_causal_verify_mask.py`, `tests/kernels/attention/test_rocm_aiter_mla_head_padding.py`, `tests/v1/attention/test_rocm_aiter_mla_fp8_decode_routing.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py` _+3 more__
- **2026-08-31** [`3593c964de`](https://github.com/vllm-project/vllm/commit/3593c964de) [#49925](https://github.com/vllm-project/vllm/pull/49925)
  [ROCm] Add TheRock preview docker updates, Keep Python 3.12 and Ubuntu 22.04 (#49925)
  _Files: `docker/Dockerfile.rock`, `docker/Dockerfile.rock_base`, `pyproject.toml`, `requirements/build/rock.txt` _+3 more__
- **2026-08-31** [`76ff0cdff2`](https://github.com/vllm-project/vllm/commit/76ff0cdff2) [#53821](https://github.com/vllm-project/vllm/pull/53821)
  [Bugfix][ROCm] Preserve AITER unified-attention metadata during graph replay (#53821)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-08-31** [`f9d666f917`](https://github.com/vllm-project/vllm/commit/f9d666f917) [#52067](https://github.com/vllm-project/vllm/pull/52067)
  [KV Offload] Forward ownership in KV cache events (#52067)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`, `vllm/v1/kv_offload/base.py`_

## Attention  (52 commits)

- **2026-09-07** [`42801b3a6b`](https://github.com/vllm-project/vllm/commit/42801b3a6b) [#53565](https://github.com/vllm-project/vllm/pull/53565)
  [3/N][warmup][DSv4] Migrate FA4 MLA and shared CuTeDSL kernels (#53565)
  _Files: `tests/models/inkling/test_fa4_rel_attention.py`, `tests/v1/attention/test_mla_prefill_quant_output.py`, `vllm/model_executor/warmup/fa4_cutedsl_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+4 more__
- **2026-09-07** [`1713b9866a`](https://github.com/vllm-project/vllm/commit/1713b9866a) [#53564](https://github.com/vllm-project/vllm/pull/53564)
  [2/N][warmup][DSv4] Migrate sequence and DCP kernels (#53564)
  _Files: `.buildkite/test_areas/model_executor.yaml`, `tests/model_executor/test_jit_warmup.py`, `tests/model_executor/test_jit_warmup_cutedsl_launcher.py`, `tests/model_executor/test_jit_warmup_triton_launcher.py` _+8 more__
- **2026-09-07** [`94e26dd3dd`](https://github.com/vllm-project/vllm/commit/94e26dd3dd) [#54890](https://github.com/vllm-project/vllm/pull/54890)
  [Qwen3.8-Flash-Next] Support FP8 indexer cache for QSA (#54890)
  _Files: `tests/models/qwen4_exp/test_qsa_pre_indexer.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/common/qsa_cache.py`, `vllm/models/qwen4_exp/nvidia/indexer_qsa.py` _+1 more__
- **2026-09-07** [`d9105ea800`](https://github.com/vllm-project/vllm/commit/d9105ea800) [#55272](https://github.com/vllm-project/vllm/pull/55272)
  [Qwen3.8-Flash-Next] Remove torch.compile for NVIDIA implementation (#55272)
  _Files: `tests/models/qwen4_exp/test_config.py`, `tests/models/qwen4_exp/test_ple.py`, `tests/models/qwen4_exp/test_qsa_reference.py`, `tests/test_config.py` _+9 more__
- **2026-09-06** [`a1541f5742`](https://github.com/vllm-project/vllm/commit/a1541f5742) [#55285](https://github.com/vllm-project/vllm/pull/55285)
  [Perf] Use SDPA for BLIP-2 Q-Former attention (#55285)
  _Files: `vllm/model_executor/models/blip2.py`_
- **2026-09-06** [`1c344ed41e`](https://github.com/vllm-project/vllm/commit/1c344ed41e) [#49410](https://github.com/vllm-project/vllm/pull/49410)
  [CPU] [Feat]  Add native AMX-FP8 attention impl for Diamond Rapids (#49410)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_attn.cpp` _+6 more__
- **2026-09-05** [`8369affa54`](https://github.com/vllm-project/vllm/commit/8369affa54) [#55119](https://github.com/vllm-project/vllm/pull/55119)
  [Feat] Add EPLB support for GLM-5.3-Flash (#55119)
  _Files: `vllm/models/glm5next/nvidia/model.py`, `vllm/models/glm5next/nvidia/mtp.py`_
- **2026-09-05** [`4ee2595512`](https://github.com/vllm-project/vllm/commit/4ee2595512) [#54819](https://github.com/vllm-project/vllm/pull/54819)
  [Attention] Sync FA with upstream (#54819)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-09-05** [`d87a440f88`](https://github.com/vllm-project/vllm/commit/d87a440f88) [#50514](https://github.com/vllm-project/vllm/pull/50514)
  [Core][MRV2] Support eagle3 spec decode with pipeline parallel (#50514)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `tests/models/kimi_k3/test_aux_attn_res_stream.py`, `tests/v1/e2e/spec_decode/eagle/test_eagle3_pp.py`, `tests/v1/worker/test_eagle3_aux_hidden_states_pp.py` _+23 more__
- **2026-09-05** [`16328c7a77`](https://github.com/vllm-project/vllm/commit/16328c7a77) [#55242](https://github.com/vllm-project/vllm/pull/55242)
  [Perf] Kimi K3 nvfp4 Align in_proj weights by 128 to avoid elementwise copy (#55242)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`, `vllm/models/kimi_k3/nvidia/kda.py`, `vllm/models/kimi_k3/nvidia/mla.py` _+2 more__
- **2026-09-05** [`6cbb3c154e`](https://github.com/vllm-project/vllm/commit/6cbb3c154e) [#55404](https://github.com/vllm-project/vllm/pull/55404)
  [Perf][GDN] Build cudagraph-capture metadata without a device sync (#55404)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/v1/attention/backends/gdn_attn.py`, `vllm/v1/attention/backends/short_conv_attn.py`_
- **2026-09-04** [`874df9373d`](https://github.com/vllm-project/vllm/commit/874df9373d) [#55178](https://github.com/vllm-project/vllm/pull/55178)
  [Bugfix] Preserve Mamba state for padded prompt tails (#55178)
  _Files: `vllm/v1/attention/backends/mamba2_attn.py`, `vllm/v1/attention/backends/mamba_attn.py`_
- **2026-09-04** [`5093e4844a`](https://github.com/vllm-project/vllm/commit/5093e4844a) [#54374](https://github.com/vllm-project/vllm/pull/54374)
  [Bugfix][Spec Decode] Drop FlashAttention's AOT schedule for a sliding-window DFlash drafter (#54374)
  _Files: `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-09-04** [`2524051385`](https://github.com/vllm-project/vllm/commit/2524051385) [#54826](https://github.com/vllm-project/vllm/pull/54826)
  [Bugfix][Spec Decode] Honour the draft's attention_backend on Model Runner V2 (#54826)
  _Files: `tests/v1/spec_decode/test_draft_attention_backend_override.py`, `vllm/v1/worker/gpu/spec_decode/eagle/utils.py`_
- **2026-09-04** [`8cd95f7de7`](https://github.com/vllm-project/vllm/commit/8cd95f7de7) [#55234](https://github.com/vllm-project/vllm/pull/55234)
  [Bugfix][MLA] Restore DSpark cache-group capability under optimized Python (#55234)
  _Files: `tests/v1/attention/test_mla_noncausal.py`, `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-09-04** [`31a8a26662`](https://github.com/vllm-project/vllm/commit/31a8a26662) [#54873](https://github.com/vllm-project/vllm/pull/54873)
  [Qwen3.8-Flash-Next] Improve QSA sparse GQA for prefill and short-ctx decode (#54873)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/model_executor/warmup/qwen4_exp_qsa_warmup.py`, `vllm/models/qwen4_exp/nvidia/indexer_qsa.py`, `vllm/models/qwen4_exp/nvidia/ops/qsa.py` _+2 more__
- **2026-09-04** [`8340fe1bb9`](https://github.com/vllm-project/vllm/commit/8340fe1bb9) [#55317](https://github.com/vllm-project/vllm/pull/55317)
  [CI/Build] Fix flaky failures in CPU CI image building (#55317)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test.sh`, `csrc/cpu/sgl-kernels/mla_cache.cpp`, `docker/Dockerfile.cpu`, `tests/models/language/pooling/test_max_tokens_per_doc.py`_
- **2026-09-04** [`c615b1fd67`](https://github.com/vllm-project/vllm/commit/c615b1fd67) [#54177](https://github.com/vllm-project/vllm/pull/54177)
  [Mypy] Fix mypy typing for L models (#54177)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/laguna.py`, `vllm/model_executor/models/laguna_dflash.py`, `vllm/model_executor/models/lfm2_vl.py` _+15 more__
- **2026-09-04** [`a5c9179e73`](https://github.com/vllm-project/vllm/commit/a5c9179e73) [#54915](https://github.com/vllm-project/vllm/pull/54915)
  [Qwen3.8-Flash-Next] Compact indexer logits workspace to improve prefill efficiency (#54915)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/models/qwen4_exp/common/qsa_cache.py`, `vllm/models/qwen4_exp/nvidia/indexer_qsa.py`, `vllm/models/qwen4_exp/nvidia/ops/qsa_indexer.py`_
- **2026-09-04** [`29af8bd672`](https://github.com/vllm-project/vllm/commit/29af8bd672) [#55266](https://github.com/vllm-project/vllm/pull/55266)
  [XPU][UT] skip GLM-5.3-Flash test on XPU (#55266)
  _Files: `tests/models/multimodal/processing/test_tensor_schema.py`_
- **2026-09-03** [`9509fc8ae6`](https://github.com/vllm-project/vllm/commit/9509fc8ae6) [#54896](https://github.com/vllm-project/vllm/pull/54896)
  [Perf][Kimi-K3] Cut MLA decode concat/cache epilogue latency (#54896)
  _Files: `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`, `tests/kernels/attention/test_kimi_k3_mla_fused_epilogue.py`_
- **2026-09-03** [`fc8f10792c`](https://github.com/vllm-project/vllm/commit/fc8f10792c) [#45091](https://github.com/vllm-project/vllm/pull/45091)
  Fix DeepSeek V4 FlashMLA auto KV cache dtype (#45091)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-09-03** [`edc0fb7e03`](https://github.com/vllm-project/vllm/commit/edc0fb7e03) [#55054](https://github.com/vllm-project/vllm/pull/55054)
  Optimize PLE MTP metadata transfers (#55054)
  _Files: `vllm/v1/attention/backends/short_conv_attn.py`_
- **2026-09-03** [`848ab131bc`](https://github.com/vllm-project/vllm/commit/848ab131bc) [#55062](https://github.com/vllm-project/vllm/pull/55062)
  [Perf] Accumulate Conformer attention scores with baddbmm (#55062)
  _Files: `tests/models/multimodal/test_conformer_encoder.py`, `vllm/model_executor/models/conformer_encoder.py`_
- **2026-09-03** [`facd9a74a1`](https://github.com/vllm-project/vllm/commit/facd9a74a1) [#54856](https://github.com/vllm-project/vllm/pull/54856)
  [Model Runner V2][Spec Decode] Skip DP sync for all speculator uniform decodes (#54856)
  _Files: `vllm/v1/worker/gpu/dp_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`, `vllm/v1/worker/gpu/spec_decode/speculator.py`_
- **2026-09-03** [`c21751c90b`](https://github.com/vllm-project/vllm/commit/c21751c90b) [#54251](https://github.com/vllm-project/vllm/pull/54251)
  [Kernel] Warm up Qwen GDN gated RMSNorm (#54251)
  _Files: `tests/kernels/test_fla_layernorm_guard.py`, `vllm/model_executor/warmup/qwen_triton_warmup.py`, `vllm/third_party/flash_linear_attention/ops/layernorm_guard.py`_
- **2026-09-02** [`872084fb77`](https://github.com/vllm-project/vllm/commit/872084fb77) [#54817](https://github.com/vllm-project/vllm/pull/54817)
  [CI] Add Kimi-K3-pruned75-DSpark-TP4 gsm8k eval (#54817)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TEP4.yaml`, `tests/evals/gsm8k/configs/Kimi-K3-pruned75-DSpark-TP4.yaml`, `tests/evals/gsm8k/configs/models-spec-decode.txt` _+1 more__
- **2026-09-02** [`62588e0592`](https://github.com/vllm-project/vllm/commit/62588e0592) [#54558](https://github.com/vllm-project/vllm/pull/54558)
  [CI] Batch the swap_blocks verification instead of copying block by block (#54558)
  _Files: `tests/kernels/attention/test_cache.py`_
- **2026-09-02** [`f4e6136146`](https://github.com/vllm-project/vllm/commit/f4e6136146) [#54859](https://github.com/vllm-project/vllm/pull/54859)
  [Kimi-K3] Bump FlashKDA to fix unstable inverse (#54859)
  _Files: `cmake/external_projects/flashkda.cmake`, `tests/models/kimi_k3/test_kda.py`_
- **2026-09-02** [`f870b92976`](https://github.com/vllm-project/vllm/commit/f870b92976) [#54517](https://github.com/vllm-project/vllm/pull/54517)
  [Qwen3.8-Flash-Next] Fuse Qwen4Exp PLE kernels (#54517)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/mtp.py`, `vllm/models/qwen4_exp/nvidia/ops/ple.py` _+2 more__
- **2026-09-02** [`396c5a5632`](https://github.com/vllm-project/vllm/commit/396c5a5632) [#54869](https://github.com/vllm-project/vllm/pull/54869)
  [Bugfix] Lazy-import FlashInfer PCIe IPC all-reduce in kernel_warmup (#54869)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-09-02** [`a566ea7e8f`](https://github.com/vllm-project/vllm/commit/a566ea7e8f) [#54660](https://github.com/vllm-project/vllm/pull/54660)
  [Perf] Avoid more h2d copies from non-pinned tensors (#54660)
  _Files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/transformers/multimodal.py`, `vllm/multimodal/inputs.py` _+1 more__
- **2026-09-02** [`003e34341a`](https://github.com/vllm-project/vllm/commit/003e34341a) [#54513](https://github.com/vllm-project/vllm/pull/54513)
  [Qwen3.8-Flash-Next] Separate prefill and decode paths for QSA indexer (#54513)
  _Files: `tests/models/qwen4_exp/test_qsa_reference.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/qwen4_exp_qsa_warmup.py`, `vllm/models/qwen4_exp/common/qsa_cache.py` _+3 more__
- **2026-09-01** [`7a977c0699`](https://github.com/vllm-project/vllm/commit/7a977c0699) [#49381](https://github.com/vllm-project/vllm/pull/49381)
  [ModelOpt] Redesign the LinearMethod classes using the generic QuantKey-driven method (#49381)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/linear.py` _+2 more__
- **2026-09-01** [`6c58595c2d`](https://github.com/vllm-project/vllm/commit/6c58595c2d) [#54794](https://github.com/vllm-project/vllm/pull/54794)
  [Feature] Avoid flashinfer autotune each time when vllm source change (#54794)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/warmup/flashinfer_autotune_cache.py`_
- **2026-09-01** [`0d4ad47981`](https://github.com/vllm-project/vllm/commit/0d4ad47981) [#52017](https://github.com/vllm-project/vllm/pull/52017)
  [Kernel] Add B12X causal paged attention backend (#52017)
  _Files: `.buildkite/test_areas/kernels.yaml`, `docs/design/attention_backends.md`, `setup.py`, `tests/v1/attention/test_attention_backends.py` _+4 more__
- **2026-09-01** [`adebc41b7e`](https://github.com/vllm-project/vllm/commit/adebc41b7e) [#52506](https://github.com/vllm-project/vllm/pull/52506)
  [Mamba] Add FlashInfer ReplaySSM backend (#52506)
  _Files: `tests/kernels/mamba/test_ssu_dispatch.py`, `tests/model_executor/test_replayssm_warmup.py`, `tests/v1/attention/test_replayssm_metadata_builder.py`, `tests/v1/e2e/test_replayssm_decode.py` _+15 more__
- **2026-09-01** [`25efcfa788`](https://github.com/vllm-project/vllm/commit/25efcfa788) [#52724](https://github.com/vllm-project/vllm/pull/52724)
  [Attention] Enable adaptive verification for FLASHINFER_MLA_SPARSE_DSV4 (#52724)
  _Files: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`_
- **2026-09-01** [`7c5dc571cb`](https://github.com/vllm-project/vllm/commit/7c5dc571cb) [#51724](https://github.com/vllm-project/vllm/pull/51724)
  [Attention][DSA] Enable W4A16 DSA (#51724)
  _Files: `CMakeLists.txt`, `cmake/external_projects/flashmla.cmake`, `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/nvfp4_ds_mla_cache.h` _+13 more__
- **2026-09-01** [`446c769482`](https://github.com/vllm-project/vllm/commit/446c769482) [#53576](https://github.com/vllm-project/vllm/pull/53576)
  [Distributed] Add opt-in FlashInfer PCIe IPC all-reduce backend (#53576)
  _Files: `tests/distributed/test_comm_ops.py`, `tests/distributed/test_flashinfer_pcie_ipc_all_reduce.py`, `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/flashinfer_pcie_ipc_all_reduce.py` _+3 more__
- **2026-09-01** [`e16b5e518d`](https://github.com/vllm-project/vllm/commit/e16b5e518d) [#50175](https://github.com/vllm-project/vllm/pull/50175)
  [1/N][warmup][DSv4] Migrate generic MLA metadata and indexing kernels (#50175)
  _Files: `docs/contributing/jit_kernel_warmup.md`, `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/model_executor/test_jit_warmup.py`, `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py` _+13 more__
- **2026-09-01** [`882ca8d696`](https://github.com/vllm-project/vllm/commit/882ca8d696) [#53014](https://github.com/vllm-project/vllm/pull/53014)
  [Kernel] add Flashinfer cutedsl w4a16 linear (#53014)
  _Files: `docs/features/quantization/modelopt.md`, `tests/kernels/quantization/test_flashinfer_nvfp4_scaled_mm.py`, `tests/quantization/test_modelopt.py`, `vllm/config/kernel.py` _+4 more__
- **2026-09-01** [`58dace61fa`](https://github.com/vllm-project/vllm/commit/58dace61fa) [#54194](https://github.com/vllm-project/vllm/pull/54194)
  [Kernel] Make prefix-prefill tiling independent of the KV page size (#54194)
  _Files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/v1/attention/ops/prefix_prefill.py`_
- **2026-08-31** [`91752b7a3e`](https://github.com/vllm-project/vllm/commit/91752b7a3e) [#54634](https://github.com/vllm-project/vllm/pull/54634)
  [K3 Bug] Fix Kimi-K3 RecoverSSM startup failure `'MambaAttentionBackendEnum.GDN_ATTN declares 4 states, but provides 2 state copy funcs'` (#54634)
  _Files: `vllm/v1/worker/mamba_utils.py`_
- **2026-08-31** [`3a2ed6cbae`](https://github.com/vllm-project/vllm/commit/3a2ed6cbae) [#54636](https://github.com/vllm-project/vllm/pull/54636)
  [Kimi Bug] Fix gdn build_attn_metadata `'KimiK3KDAMetadataBuilder' object has no attribute 'layer_names'` (#54636)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-08-31** [`07ea9350ba`](https://github.com/vllm-project/vllm/commit/07ea9350ba) [#53147](https://github.com/vllm-project/vllm/pull/53147)
  [Kernel][Gemma4] Prune Triton sliding-window tiles for multimodal prefixes (#53147)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/v1/attention/ops/triton_attention_helpers.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-08-31** [`d61b6e1878`](https://github.com/vllm-project/vllm/commit/d61b6e1878) [#54373](https://github.com/vllm-project/vllm/pull/54373)
  [Bugfix][Spec Decode] Take the DFlash draft's RoPE layout from its own config (#54373)
  _Files: `vllm/model_executor/models/qwen3_dflash.py`, `vllm/v1/spec_decode/dflash.py`, `vllm/v1/worker/gpu/spec_decode/dflash/utils.py`_
- **2026-08-31** [`c5d840ff6a`](https://github.com/vllm-project/vllm/commit/c5d840ff6a) [#51689](https://github.com/vllm-project/vllm/pull/51689)
  [KV Connector][Offloading] Certify attention-only hybrids in the canonical portability gate (#51689)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-08-31** [`2cf82bcdd1`](https://github.com/vllm-project/vllm/commit/2cf82bcdd1) [#50005](https://github.com/vllm-project/vllm/pull/50005)
  [Bugfix][DCP] Fix NVIDIA DeepSeek-V3.2 / GLM-5.2 fused attention (#50005)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/attention.py`, `vllm/models/deepseek_v32/common/kernels.py`_
- **2026-08-31** [`da0b2d8b17`](https://github.com/vllm-project/vllm/commit/da0b2d8b17) [#53517](https://github.com/vllm-project/vllm/pull/53517)
  [Performance] Optimize Dots3 NOTE runtime (#53517)
  _Files: `vllm/config/vllm.py`, `vllm/models/dots3_note/nvidia/attention.py`, `vllm/models/dots3_note/nvidia/model.py`, `vllm/models/dots3_note/nvidia/mtp.py` _+2 more__
- **2026-08-31** [`e126687a9a`](https://github.com/vllm-project/vllm/commit/e126687a9a) [#53896](https://github.com/vllm-project/vllm/pull/53896)
  [Model] Support Qwen3.8-Flash-Next (#53896)
- **2026-08-31** [`5707355209`](https://github.com/vllm-project/vllm/commit/5707355209) [#54465](https://github.com/vllm-project/vllm/pull/54465)
  [Bugfix][MLA] Fix BLHNC addressing for FlashInfer sparse MLA (#54465)
  _Files: `tests/v1/attention/test_indexer_dcp_localize.py`, `vllm/models/deepseek_v32/common/kernels.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py`, `vllm/v1/attention/backends/mla/sparse_utils.py`_

## MoE / Expert Parallel  (32 commits)

- **2026-09-07** [`5e6f6a8ed4`](https://github.com/vllm-project/vllm/commit/5e6f6a8ed4) [#52651](https://github.com/vllm-project/vllm/pull/52651)
  [Bugfix][Quantization][XPU] Fix moe_wna16 linear weight loading (#52651)
  _Files: `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`, `vllm/platforms/xpu.py`_
- **2026-09-07** [`9b85112e13`](https://github.com/vllm-project/vllm/commit/9b85112e13) [#53580](https://github.com/vllm-project/vllm/pull/53580)
  [XPU] Route grouped_topk to the fused _moe_C kernel on XPU (#53580)
  _Files: `vllm/_custom_ops.py`, `vllm/model_executor/layers/fused_moe/router/grouped_topk_router.py`_
- **2026-09-07** [`5893426b88`](https://github.com/vllm-project/vllm/commit/5893426b88) [#53586](https://github.com/vllm-project/vllm/pull/53586)
  [Bugfix] DSv4 MXFP4 selector: stop narrowing explicit aliases to their BF16 variant (#53586)
  _Files: `tests/kernels/moe/test_b12x.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-09-07** [`6748217fb9`](https://github.com/vllm-project/vllm/commit/6748217fb9) [#55407](https://github.com/vllm-project/vllm/pull/55407)
  [Bugfix] Fix Kimi K3 NVFP4 MoE weight conversion OOM (#55407)
  _Files: `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_
- **2026-09-06** [`f2e2936f91`](https://github.com/vllm-project/vllm/commit/f2e2936f91) [#55511](https://github.com/vllm-project/vllm/pull/55511)
  [Kernel] Add fused MoE tuned config for E=256,N=512 on NVIDIA A100 80GB PCIe (#55511)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_A100_80GB_PCIe.json`_
- **2026-09-05** [`bc96d76aa9`](https://github.com/vllm-project/vllm/commit/bc96d76aa9) [#54110](https://github.com/vllm-project/vllm/pull/54110)
  [Kernel] Fall back from persistent top-k on low-shared-memory GPUs (#54110)
  _Files: `csrc/libtorch_stable/topk.cu`_
- **2026-09-04** [`784cac7c42`](https://github.com/vllm-project/vllm/commit/784cac7c42) [#54169](https://github.com/vllm-project/vllm/pull/54169)
  [Mypy] Fix mypy typing for P models (#54169)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/paddleocr_vl.py`, `vllm/model_executor/models/paligemma.py`, `vllm/model_executor/models/param2moe.py` _+5 more__
- **2026-09-04** [`5690b02c03`](https://github.com/vllm-project/vllm/commit/5690b02c03) [#51392](https://github.com/vllm-project/vllm/pull/51392)
  [Quantization] Support online quantization with partially pre-quantized checkpoints (#51392)
  _Files: `docs/features/quantization/online.md`, `tests/model_executor/test_eagle_quantization.py`, `tests/quantization/test_config_utils.py`, `tests/quantization/test_online.py` _+21 more__
- **2026-09-04** [`1ff5edb023`](https://github.com/vllm-project/vllm/commit/1ff5edb023) [#50220](https://github.com/vllm-project/vllm/pull/50220)
  [Bug-fix] Fix MoE fused sum row offsets (#50220)
  _Files: `vllm/model_executor/layers/fused_moe/moe_fused_mul_sum.py`_
- **2026-09-04** [`8ad2076c4a`](https://github.com/vllm-project/vllm/commit/8ad2076c4a) [#54941](https://github.com/vllm-project/vllm/pull/54941)
  [Transformers backend] Find attention with a fuser and attach vLLM's layer to it (#54941)
  _Files: `docs/models/supported_models.md`, `tests/models/transformers/fusers/test_linear.py`, `tests/models/transformers/fusers/test_mla.py`, `tests/models/transformers/fusers/test_rms_norm.py` _+10 more__
- **2026-09-04** [`f19431e5c8`](https://github.com/vllm-project/vllm/commit/f19431e5c8) [#55069](https://github.com/vllm-project/vllm/pull/55069)
  [Bugfix][MoE] Allow TRTLLM FP8 block-scale MoE with SwiGLU clamp (#55069)
  _Files: `tests/kernels/moe/test_flashinfer.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`_
- **2026-09-04** [`a69e75b9b6`](https://github.com/vllm-project/vllm/commit/a69e75b9b6) [#54921](https://github.com/vllm-project/vllm/pull/54921)
  Fast Start (#54921)
  _Files: `tests/model_executor/model_loader/test_weight_cache.py`, `tools/pre_commit/check_forbidden_imports.py`, `vllm/config/load.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py` _+12 more__
- **2026-09-04** [`9cd956c7e6`](https://github.com/vllm-project/vllm/commit/9cd956c7e6) [#53497](https://github.com/vllm-project/vllm/pull/53497)
  [CI/Test] Add expert parallelism coverage to external LB tests (#53497)
  _Files: `tests/v1/distributed/test_external_lb_dp.py`_
- **2026-09-03** [`d410fc12f3`](https://github.com/vllm-project/vllm/commit/d410fc12f3) [#54606](https://github.com/vllm-project/vllm/pull/54606)
  [Kernel] Enable Kimi-K3 SiTU on the CuteDSL MoE backend and the SM107 low-latency GEMM plan (#54606)
  _Files: `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`_
- **2026-09-03** [`bf95f58d10`](https://github.com/vllm-project/vllm/commit/bf95f58d10) [#54651](https://github.com/vllm-project/vllm/pull/54651)
  [Core] Triton kernel for small-batch top-p only masking (#54651)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`_
- **2026-09-02** [`9b38e3ad53`](https://github.com/vllm-project/vllm/commit/9b38e3ad53) [#54954](https://github.com/vllm-project/vllm/pull/54954)
  [CI][MoE] Moe kernels test cleanup (#54954)
  _Files: `tests/kernels/moe/conftest.py`, `tests/kernels/moe/test_fused_topk.py`_
- **2026-09-02** [`1356635d83`](https://github.com/vllm-project/vllm/commit/1356635d83) [#54566](https://github.com/vllm-project/vllm/pull/54566)
  [New model][Multimodal] Add DeepSeek-V4-Flash-Vision-Exp support (#54566)
  _Files: `csrc/libtorch_stable/moe/moe_ops.h`, `csrc/libtorch_stable/moe/topk_softplus_sqrt_kernels.cu`, `csrc/libtorch_stable/moe/torch_bindings.cpp`, `docs/models/supported_models.md` _+33 more__
- **2026-09-02** [`488e6fd53c`](https://github.com/vllm-project/vllm/commit/488e6fd53c) [#54991](https://github.com/vllm-project/vllm/pull/54991)
  [CI] Revert flaky `test_quark_int8_w8a8_moe` (#54991)
  _Files: `tests/quantization/test_quark.py`_
- **2026-09-02** [`1b4b2a18b8`](https://github.com/vllm-project/vllm/commit/1b4b2a18b8) [#52352](https://github.com/vllm-project/vllm/pull/52352)
  [CI] Shard H100 MoE refactor integration tests (#52352)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/moe-refactor/config-h100-shard-0.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-h100-shard-1.txt`, `tests/evals/gsm8k/configs/moe-refactor/config-h100-shard-2.txt` _+2 more__
- **2026-09-02** [`46c8a161f4`](https://github.com/vllm-project/vllm/commit/46c8a161f4) [#54747](https://github.com/vllm-project/vllm/pull/54747)
  [Bugfix] Handle padded routes in CUTLASS MoE permutations (#54747)
  _Files: `csrc/libtorch_stable/moe/moe_permute_unpermute_op.cu`, `csrc/libtorch_stable/quantization/fp4/mxfp4_experts_quant.cu`, `csrc/libtorch_stable/quantization/fp4/nvfp4_experts_quant.cu`, `csrc/libtorch_stable/quantization/w8a8/cutlass/moe/moe_data.cu` _+2 more__
- **2026-09-01** [`ce6a283c09`](https://github.com/vllm-project/vllm/commit/ce6a283c09) [#54824](https://github.com/vllm-project/vllm/pull/54824)
  [Bugfix] Restore `weight_dtype` in `QuarkW8A8Fp8MoEMethod` to fix GPT-OSS FP8 MoE weight loading (#54824)
  _Files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-09-01** [`ab54f5bd83`](https://github.com/vllm-project/vllm/commit/ab54f5bd83) [#46872](https://github.com/vllm-project/vllm/pull/46872)
  [Chore] Remove redundant `_pack_topk_ids_weights_kernel` in TrtLLM NvFP4 MoE (#46872)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py` _+2 more__
- **2026-09-01** [`2fe5cef35e`](https://github.com/vllm-project/vllm/commit/2fe5cef35e) [#54573](https://github.com/vllm-project/vllm/pull/54573)
  [Fix] Fix FSE compatibility detection for Quark-produced models (#54573)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/model_executor/layers/fused_moe/utils.py`, `vllm/model_executor/layers/quantization/utils/config_utils.py`_
- **2026-09-01** [`82b7d49a6e`](https://github.com/vllm-project/vllm/commit/82b7d49a6e) [#51217](https://github.com/vllm-project/vllm/pull/51217)
  [MoE] Generalize masked activation for padded layouts (#51217)
  _Files: `csrc/libtorch_stable/activation_kernels.cu`, `csrc/libtorch_stable/moe/permute_unpermute_kernels/moe_permute_unpermute_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+11 more__
- **2026-09-01** [`a232e29e9d`](https://github.com/vllm-project/vllm/commit/a232e29e9d) [#54306](https://github.com/vllm-project/vllm/pull/54306)
  [Bugfix] Gate sm_100-only kernel tests on the capability family, not >= (#54306)
  _Files: `tests/kernels/attention/test_cutlass_mla_decode.py`, `tests/kernels/moe/test_cutedsl_moe.py`, `tests/kernels/moe/test_routed_experts_capture_monolithic.py`, `tests/kernels/moe/test_trtllm_bf16_moe.py` _+1 more__
- **2026-09-01** [`55aa766dc8`](https://github.com/vllm-project/vllm/commit/55aa766dc8) [#54052](https://github.com/vllm-project/vllm/pull/54052)
  [Bugfix][Model] Fix GraniteMoeHybrid per-expert quantized weight loading (#54052)
  _Files: `vllm/model_executor/models/granitemoehybrid.py`_
- **2026-09-01** [`63988f3c2d`](https://github.com/vllm-project/vllm/commit/63988f3c2d) [#52958](https://github.com/vllm-project/vllm/pull/52958)
  [Quantization][Refactor][1/N] Adopt `QuantKey` in `QuarkConfig` and methods, relying on `weight_quant_key`, `act_quant_key` for quant method dispatch (#52958)
  _Files: `tests/quantization/test_online_mxfp4.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py` _+9 more__
- **2026-08-31** [`f5c3cc240b`](https://github.com/vllm-project/vllm/commit/f5c3cc240b) [#53382](https://github.com/vllm-project/vllm/pull/53382)
  [Perf][Kernel] Tune cooperative topk for medium batch-sizes (#53382)
  _Files: `csrc/libtorch_stable/cooperative_topk.cu`, `csrc/libtorch_stable/cooperative_topk.cuh`, `tests/kernels/test_top_k_per_row.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-08-31** [`699e180df4`](https://github.com/vllm-project/vllm/commit/699e180df4) [#53574](https://github.com/vllm-project/vllm/pull/53574)
  [Bugfix][SM120] DSv4: pass contiguous C128A decode topk indices on SM120 (#53574)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/sparse_mla.py`_
- **2026-08-31** [`1b9539d37c`](https://github.com/vllm-project/vllm/commit/1b9539d37c) [#51248](https://github.com/vllm-project/vllm/pull/51248)
  [Quantization][Autoround][XPU] Support AutoRound MXFP8 MoE models (#51248)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp8_moe.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp8_scheme.py`_
- **2026-08-31** [`fdbf2ddbd2`](https://github.com/vllm-project/vllm/commit/fdbf2ddbd2) [#54042](https://github.com/vllm-project/vllm/pull/54042)
  [Bugfix][CPU] Fix several bugs (#54042)
  _Files: `csrc/cpu/cpu_fused_moe.cpp`, `csrc/cpu/sgl-kernels/gemm.cpp`, `csrc/cpu/torch_bindings.cpp`, `tests/conftest.py` _+7 more__
- **2026-08-31** [`8e92248f79`](https://github.com/vllm-project/vllm/commit/8e92248f79) [#54040](https://github.com/vllm-project/vllm/pull/54040)
  [Kernel] Retire the DSv3 router GEMM CUDA kernel  (#54040)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_router_gemm.py`, `csrc/libtorch_stable/fp32_router_gemm.cu`, `csrc/libtorch_stable/fp32_router_gemm_entry.cu` _+8 more__

## Multimodal  (32 commits)

- **2026-09-07** [`f7f060d253`](https://github.com/vllm-project/vllm/commit/f7f060d253) [#55642](https://github.com/vllm-project/vllm/pull/55642)
  [Bugfix][Audio] Restore soundfile-first automatic decoding (#55642)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/media/test_audio.py`, `vllm/multimodal/media/audio.py`_
- **2026-09-07** [`ed29dfae6e`](https://github.com/vllm-project/vllm/commit/ed29dfae6e) [#52945](https://github.com/vllm-project/vllm/pull/52945)
  [XPU] Use fused_input_norm kernel in FusedInputNorm (#52945)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/models/vision.py`_
- **2026-09-06** [`52358e6e19`](https://github.com/vllm-project/vllm/commit/52358e6e19) [#54659](https://github.com/vllm-project/vllm/pull/54659)
  [Frontend] Expose multimodal metadata for disaggregated prefill (#54659)
  _Files: `docs/serving/online_serving/renderer.md`, `tests/entrypoints/scale_out/token_in_token_out/test_mm_serde.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/entrypoints/scale_out/render/serving.py` _+3 more__
- **2026-09-06** [`1970f3ed4b`](https://github.com/vllm-project/vllm/commit/1970f3ed4b) [#51898](https://github.com/vllm-project/vllm/pull/51898)
  Validate scale-out multimodal data before engine handoff (#51898)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_protocol.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py`_
- **2026-09-05** [`f4eccdadef`](https://github.com/vllm-project/vllm/commit/f4eccdadef) [#55448](https://github.com/vllm-project/vllm/pull/55448)
  [Bugfix][Multimodal] Bound renderer warmup to the prefill token budget (#55448)
  _Files: `tests/multimodal/test_registry.py`, `tests/renderers/test_warmup.py`, `vllm/multimodal/registry.py`, `vllm/renderers/base.py`_
- **2026-09-05** [`32601ef7a1`](https://github.com/vllm-project/vllm/commit/32601ef7a1) [#55415](https://github.com/vllm-project/vllm/pull/55415)
  [Perf][Multimodal] Avoid duplicate text embedding in Qwen2.5-Omni (#55415)
  _Files: `vllm/model_executor/models/qwen2_5_omni_thinker.py`_
- **2026-09-04** [`c81ace1859`](https://github.com/vllm-project/vllm/commit/c81ace1859) [#55331](https://github.com/vllm-project/vllm/pull/55331)
  [Perf] Read VidCom2 frame budgets once (#55331)
  _Files: `tests/multimodal/test_vidcom2.py`, `vllm/multimodal/video_prune/vidcom2.py`_
- **2026-09-04** [`761c5861e3`](https://github.com/vllm-project/vllm/commit/761c5861e3) [#54814](https://github.com/vllm-project/vllm/pull/54814)
  [Rust Frontend][gRPC] Preserve multimodal metadata for remote-prefill decode (#54814)
  _Files: `rust/src/server/src/grpc/convert.rs`, `rust/src/server/src/grpc/inference.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-09-04** [`6a039f465e`](https://github.com/vllm-project/vllm/commit/6a039f465e) [#51826](https://github.com/vllm-project/vllm/pull/51826)
  [feat] add torchcodec as audio loader and implement selective audio backend (#51826)
  _Files: `docs/features/multimodal_inputs.md`, `tests/entrypoints/speech_to_text/transcription/test_transcription_validation_whisper.py`, `tests/multimodal/media/test_audio.py`, `vllm/multimodal/media/audio.py`_
- **2026-09-04** [`a85d0738da`](https://github.com/vllm-project/vllm/commit/a85d0738da) [#55288](https://github.com/vllm-project/vllm/pull/55288)
  [Bugfix] Fix double BOS in LLM.chat() for multimodal models (#55288)
  _Files: `tests/entrypoints/multimodal/llm/test_mm_processor_kwargs.py`, `vllm/entrypoints/offline_utils.py`_
- **2026-09-04** [`8b6de0eb9a`](https://github.com/vllm-project/vllm/commit/8b6de0eb9a) [#54935](https://github.com/vllm-project/vllm/pull/54935)
  [Security] Cap GLMGA video sampling to prevent request-driven resource exhaustion (#54935)
  _Files: `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-09-04** [`8a728663c1`](https://github.com/vllm-project/vllm/commit/8a728663c1) [#54886](https://github.com/vllm-project/vllm/pull/54886)
  [Bugfix] Reject tokenizer-less Qwen VL processor init (#54886)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `vllm/model_executor/models/terratorch.py`, `vllm/multimodal/processing/processor.py`_
- **2026-09-03** [`6fdee17f84`](https://github.com/vllm-project/vllm/commit/6fdee17f84) [#50314](https://github.com/vllm-project/vllm/pull/50314)
  [CI] Zen5 image build (#50314)
  _Files: `docker/Dockerfile.cpu`, `docker/Dockerfile.zen`_
- **2026-09-03** [`3f1af35e01`](https://github.com/vllm-project/vllm/commit/3f1af35e01) [#54994](https://github.com/vllm-project/vllm/pull/54994)
  [Bugfix][Multimodal] Handle prefix-covered items in SHM worker cache (#54994)
  _Files: `tests/multimodal/test_cache.py`, `tests/v1/core/test_output.py`, `vllm/multimodal/cache.py`, `vllm/multimodal/utils.py`_
- **2026-09-02** [`2691c6cc53`](https://github.com/vllm-project/vllm/commit/2691c6cc53) [#54957](https://github.com/vllm-project/vllm/pull/54957)
  [Bugfix][CI] Set cudagraph_mode=FULL for the Ernie4.5-VL ViT cudagraph test (#54957)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`_
- **2026-09-02** [`3b45d053b4`](https://github.com/vllm-project/vllm/commit/3b45d053b4) [#53829](https://github.com/vllm-project/vllm/pull/53829)
  [Bugfix][Model] Fix CohereASR streaming audio-token estimate (unit + subsampling) (#53829)
  _Files: `tests/models/multimodal/test_cohere_asr.py`, `vllm/model_executor/models/cohere_asr.py`_
- **2026-09-02** [`c6bca6e585`](https://github.com/vllm-project/vllm/commit/c6bca6e585) [#54918](https://github.com/vllm-project/vllm/pull/54918)
  [Bugfix][Multimodal] Scope cache hash kwargs by modality (#54918)
  _Files: `tests/multimodal/test_processing.py`, `vllm/multimodal/processing/inputs.py`_
- **2026-09-02** [`c23e15be9f`](https://github.com/vllm-project/vllm/commit/c23e15be9f) [#50504](https://github.com/vllm-project/vllm/pull/50504)
  [CI][Fix] Resolved the Ascend NPU test build image fail and add file dependencies (#50504)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/scripts/hardware_ci/run-npu-test.sh`_
- **2026-09-02** [`c00091e026`](https://github.com/vllm-project/vllm/commit/c00091e026) [#54579](https://github.com/vllm-project/vllm/pull/54579)
  [Frontend] Gate scale-out endpoints behind opt-in flag (#54579)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/renderer.md`, `docs/usage/security.md` _+16 more__
- **2026-09-01** [`dc5cf437cf`](https://github.com/vllm-project/vllm/commit/dc5cf437cf) [#54813](https://github.com/vllm-project/vllm/pull/54813)
  [Rust Frontend] Enable Qwen4-exp multimodal support (#54813)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`_
- **2026-09-01** [`d9eb4e344f`](https://github.com/vllm-project/vllm/commit/d9eb4e344f) [#54708](https://github.com/vllm-project/vllm/pull/54708)
  [Bugfix] Reject tokenless chat and audio streams (#54708)
  _Files: `vllm/benchmarks/lib/endpoint_request_func.py`_
- **2026-09-01** [`1f1f628859`](https://github.com/vllm-project/vllm/commit/1f1f628859) [#54241](https://github.com/vllm-project/vllm/pull/54241)
  [Feat][MM Hashing]  include media_io_kwargs in multi-modal hashes (#54241)
  _Files: `tests/multimodal/test_processing.py`, `tests/renderers/test_multimodal_hashes.py`, `vllm/inputs/llm.py`, `vllm/multimodal/processing/inputs.py` _+2 more__
- **2026-09-01** [`504bb8b0c3`](https://github.com/vllm-project/vllm/commit/504bb8b0c3) [#52851](https://github.com/vllm-project/vllm/pull/52851)
  [CI] Add repository-local OTel tracing helpers (#52851)
  _Files: `.buildkite/image_build/image_build.sh`, `.buildkite/scripts/ci-otel/ci_otel.py`, `.buildkite/scripts/ci-otel/ci_otel.sh`, `.buildkite/scripts/ci-otel/ci_pytest.sh` _+1 more__
- **2026-09-01** [`4707679cd2`](https://github.com/vllm-project/vllm/commit/4707679cd2) [#54633](https://github.com/vllm-project/vllm/pull/54633)
  [Bugfix][MiniCPM-V] Route video_embeds to the shared vision parser (#54633)
  _Files: `tests/model_executor/test_minicpmv.py`, `vllm/model_executor/models/minicpmv.py`, `vllm/model_executor/models/minicpmv4_6.py`_
- **2026-09-01** [`ce7391712b`](https://github.com/vllm-project/vllm/commit/ce7391712b) [#54632](https://github.com/vllm-project/vllm/pull/54632)
  [Bugfix][Security] Bound embedding densification before to_dense() (#54632)
  _Files: `docs/usage/security.md`, `tests/renderers/test_sparse_tensor_validation.py`, `vllm/envs.py`, `vllm/multimodal/media/audio.py` _+4 more__
- **2026-09-01** [`ec32f669bb`](https://github.com/vllm-project/vllm/commit/ec32f669bb) [#54220](https://github.com/vllm-project/vllm/pull/54220)
  [Feature][MM_UUIDs] Allow empty video URLs when using multi-modal UUIDs (#54220)
  _Files: `docs/features/multimodal_inputs.md`, `tests/entrypoints/multimodal/openai/chat_completion/test_video.py`, `tests/multimodal/test_parse.py`, `vllm/multimodal/parse.py`_
- **2026-09-01** [`8600db5dff`](https://github.com/vllm-project/vllm/commit/8600db5dff) [#48750](https://github.com/vllm-project/vllm/pull/48750)
  [CI] Build CPU image against torch nightly for TORCH_NIGHTLY runs (#48750)
  _Files: `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/image_build/image_build_cpu.sh`, `docker/Dockerfile.cpu`, `use_existing_torch.py`_
- **2026-08-31** [`e9dd6d4834`](https://github.com/vllm-project/vllm/commit/e9dd6d4834) [#54365](https://github.com/vllm-project/vllm/pull/54365)
  [CI] Exclude kv_transfer changes from broad spec-decode/kernels/multimodal triggers (#54365)
  _Files: `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_multimodal.yaml`, `.buildkite/test_areas/spec_decode.yaml`_
- **2026-08-31** [`82936c409d`](https://github.com/vllm-project/vllm/commit/82936c409d) [#54172](https://github.com/vllm-project/vllm/pull/54172)
  [Tests][XPU] Limit Qwen2-VL generation length to avoid flaky numerical divergence (#54172)
  _Files: `tests/models/multimodal/generation/test_common.py`_
- **2026-08-31** [`399247cc88`](https://github.com/vllm-project/vllm/commit/399247cc88) [#54501](https://github.com/vllm-project/vllm/pull/54501)
  [Bugfix][MM] Fix MiniCPM-o image processor reuse on Transformers v5 (#54501)
  _Files: `tests/models/multimodal/processing/test_minicpmv.py`, `vllm/model_executor/models/minicpmo.py`, `vllm/model_executor/models/minicpmv.py`_
- **2026-08-31** [`7292ee2791`](https://github.com/vllm-project/vllm/commit/7292ee2791) [#53808](https://github.com/vllm-project/vllm/pull/53808)
  [Bugfix][Multimodal] Honor modality-scoped mm_processor_kwargs (#53808)
  _Files: `tests/models/multimodal/processing/test_qwen3_vl.py`, `tests/multimodal/test_processing.py`, `vllm/model_executor/models/qwen2_vl.py`, `vllm/model_executor/models/qwen3_vl.py` _+1 more__
- **2026-08-31** [`555ea65e8c`](https://github.com/vllm-project/vllm/commit/555ea65e8c) [#54242](https://github.com/vllm-project/vllm/pull/54242)
  [Frontend] Add video embeds input support (#54242)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/models/multimodal/processing/test_qwen3_vl.py`, `vllm/distributed/ec_transfer/ec_connector/example_connector.py` _+4 more__

## Other  (28 commits)

- **2026-09-07** [`9cc7793e32`](https://github.com/vllm-project/vllm/commit/9cc7793e32) [#54022](https://github.com/vllm-project/vllm/pull/54022)
  [Bugfix] Gracefully handle unsupported reasoning_effort in chat templates (#54022)
  _Files: `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-09-06** [`6865e67f0b`](https://github.com/vllm-project/vllm/commit/6865e67f0b) [#55455](https://github.com/vllm-project/vllm/pull/55455)
  [Bugfix] Defer adaptive verification until after kernel warmup (#55455)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `tests/v1/worker/test_mixed_warmup_gate.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-09-06** [`808f8cd3ac`](https://github.com/vllm-project/vllm/commit/808f8cd3ac) [#55529](https://github.com/vllm-project/vllm/pull/55529)
  [Governance] Add aoshen02 as code owner for RL components (#55529)
  _Files: `.github/CODEOWNERS`_
- **2026-09-06** [`dd0760165c`](https://github.com/vllm-project/vllm/commit/dd0760165c) [#55461](https://github.com/vllm-project/vllm/pull/55461)
  [Bugfix] Fall back to T1 when ARC cannot reclaim enough entries from T2 (#55461)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/policies/arc.py`_
- **2026-09-04** [`07ee97e023`](https://github.com/vllm-project/vllm/commit/07ee97e023) [#55315](https://github.com/vllm-project/vllm/pull/55315)
  [Test] Split test_sampling_mask_preserves_top_k_boundary_ties to remove Triton-kernel-specific assumption Description (#55315)
  _Files: `tests/v1/test_outputs.py`_
- **2026-09-04** [`605ca45b91`](https://github.com/vllm-project/vllm/commit/605ca45b91) [#53037](https://github.com/vllm-project/vllm/pull/53037)
  [XPU] Fix device assignment for DP external LB (#53037)
  _Files: `vllm/v1/worker/xpu_worker.py`_
- **2026-09-04** [`a8693df504`](https://github.com/vllm-project/vllm/commit/a8693df504) [#55245](https://github.com/vllm-project/vllm/pull/55245)
  [SpecDecode]Fix spec decode warmup device selection (#55245)
  _Files: `vllm/model_executor/warmup/spec_decode_rejection_warmup.py`_
- **2026-09-04** [`8f816a3f66`](https://github.com/vllm-project/vllm/commit/8f816a3f66) [#52358](https://github.com/vllm-project/vllm/pull/52358)
  [MRV2][Metrics] Support `CUDAGraphStat` in MRV2 (#52358)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-09-03** [`e55b93f296`](https://github.com/vllm-project/vllm/commit/e55b93f296) [#55041](https://github.com/vllm-project/vllm/pull/55041)
  [Core] Deprecate "all" mamba cache mode (#55041)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `vllm/config/cache.py`, `vllm/config/vllm.py`_
- **2026-09-02** [`443febe723`](https://github.com/vllm-project/vllm/commit/443febe723) [#55028](https://github.com/vllm-project/vllm/pull/55028)
  [Agents] Expose Triton kernel-writing skill to Claude (#55028)
  _Files: `.claude/skills/triton-kernel-writing`_
- **2026-09-02** [`3140531773`](https://github.com/vllm-project/vllm/commit/3140531773) [#53762](https://github.com/vllm-project/vllm/pull/53762)
  Include chat template fallbacks in package_data (#53762)
  _Files: `setup.py`_
- **2026-09-02** [`8052102c21`](https://github.com/vllm-project/vllm/commit/8052102c21) [#51667](https://github.com/vllm-project/vllm/pull/51667)
  [Bugfix] Fix cross-batch buffer race corrupting DiskBackend loads (#51667)
  _Files: `vllm/v1/simple_kv_offload/disk_backend.py`_
- **2026-09-02** [`798b557e06`](https://github.com/vllm-project/vllm/commit/798b557e06) [#45241](https://github.com/vllm-project/vllm/pull/45241)
  [Frontend] Add site-packages support for reasoning/tool parser plugins (#45241)
  _Files: `tests/utils_/test_import_utils.py`, `vllm/reasoning/abs_reasoning_parsers.py`, `vllm/tool_parsers/abstract_tool_parser.py`, `vllm/utils/import_utils.py`_
- **2026-09-01** [`80389cfedd`](https://github.com/vllm-project/vllm/commit/80389cfedd) [#54827](https://github.com/vllm-project/vllm/pull/54827)
  [CI/Build] Gate PR title check on ready PRs & use slim runners (#54827)
  _Files: `.github/actionlint.yaml`, `.github/workflows/pr-title.yml`_
- **2026-09-01** [`fc72fc39ac`](https://github.com/vllm-project/vllm/commit/fc72fc39ac) [#54781](https://github.com/vllm-project/vllm/pull/54781)
  [Kimi Bug] Fix `cannot access local variable 'active_non_spec_mask_cpu'` (#54781)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`_
- **2026-09-01** [`aa71f9bcc4`](https://github.com/vllm-project/vllm/commit/aa71f9bcc4) [#52285](https://github.com/vllm-project/vllm/pull/52285)
  [Bugfix] Log platform plugin detection failures (#52285)
  _Files: `tests/test_zen_cpu_platform_detection.py`, `vllm/platforms/__init__.py`_
- **2026-09-01** [`d98bb2a879`](https://github.com/vllm-project/vllm/commit/d98bb2a879) [#54799](https://github.com/vllm-project/vllm/pull/54799)
  [Bugfix][Frontend] Honor skip_decoder_start_token in async encoder-decoder rendering (#54799)
  _Files: `vllm/renderers/base.py`_
- **2026-09-01** [`8905633687`](https://github.com/vllm-project/vllm/commit/8905633687) [#54692](https://github.com/vllm-project/vllm/pull/54692)
  [Bugfix][Frontend] Preserve token offset origins after left text pre-trimming (#54692)
  _Files: `tests/renderers/test_token_offsets.py`, `vllm/renderers/base.py`, `vllm/renderers/params.py`_
- **2026-09-01** [`ff0c3cb03c`](https://github.com/vllm-project/vllm/commit/ff0c3cb03c) [#54539](https://github.com/vllm-project/vllm/pull/54539)
  [Bugfix][Frontend] Truncate the assistant tokens mask with the prompt (#54539)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `vllm/renderers/params.py`_
- **2026-09-01** [`923949e6e3`](https://github.com/vllm-project/vllm/commit/923949e6e3) [#49984](https://github.com/vllm-project/vllm/pull/49984)
  [Feat] Add request-level preemption count histogram metric (#49984)
  _Files: `tests/entrypoints/serve/instrumentator/test_metrics.py`, `vllm/v1/metrics/loggers.py`, `vllm/v1/metrics/stats.py`_
- **2026-09-01** [`225aec4809`](https://github.com/vllm-project/vllm/commit/225aec4809) [#53056](https://github.com/vllm-project/vllm/pull/53056)
  [Rust Frontend] Migrate to new tekken crate (#53056)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`_
- **2026-09-01** [`4c21d41733`](https://github.com/vllm-project/vllm/commit/4c21d41733) [#53734](https://github.com/vllm-project/vllm/pull/53734)
  [XPU] Route activation CustomOps to SYCL kernels (#53734)
  _Files: `vllm/model_executor/layers/activation.py`_
- **2026-08-31** [`6bafc049aa`](https://github.com/vllm-project/vllm/commit/6bafc049aa) [#54436](https://github.com/vllm-project/vllm/pull/54436)
  [Bugfix][PP] Never drop a decoding request from the sampled-token broadcast (#54436)
  _Files: `tests/v1/worker/test_gpu_batch_shard.py`, `tests/v1/worker/test_pp_utils.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py` _+2 more__
- **2026-08-31** [`a9dc631429`](https://github.com/vllm-project/vllm/commit/a9dc631429) [#53433](https://github.com/vllm-project/vllm/pull/53433)
  [Bugfix] Reject empty bad-word tokenizations (#53433)
  _Files: `tests/test_request_input_bounds.py`, `vllm/sampling_params.py`_
- **2026-08-31** [`28bf75c9a9`](https://github.com/vllm-project/vllm/commit/28bf75c9a9) [#54509](https://github.com/vllm-project/vllm/pull/54509)
  [Bugfix][Frontend] Truncate prompt_is_token_ids with the prompt (#54509)
  _Files: `tests/renderers/test_chat_utils_prompt_embeds.py`, `vllm/renderers/params.py`_
- **2026-08-31** [`5bfd76372d`](https://github.com/vllm-project/vllm/commit/5bfd76372d) [#52124](https://github.com/vllm-project/vllm/pull/52124)
  [Renderer] Shutdown the renderer properly.  (#52124)
  _Files: `vllm/renderers/base.py`_
- **2026-08-31** [`c6c33f2b1f`](https://github.com/vllm-project/vllm/commit/c6c33f2b1f) [#52191](https://github.com/vllm-project/vllm/pull/52191)
  [CPU] Support FP16/BF16 persisted GDN state on AMX (#52191)
  _Files: `csrc/cpu/sgl-kernels/fla.cpp`, `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `tests/platforms/test_cpu.py`, `vllm/platforms/cpu.py`_
- **2026-08-31** [`8fd9eb85d5`](https://github.com/vllm-project/vllm/commit/8fd9eb85d5) [#54407](https://github.com/vllm-project/vllm/pull/54407)
  [Bugfix][Frontend] Truncate prompt_token_offsets with the prompt (#54407)
  _Files: `tests/entrypoints/scale_out/render/test_render.py`, `tests/renderers/test_token_offsets.py`, `vllm/renderers/params.py`_

## CI / Build  (27 commits)

- **2026-09-06** [`722d169339`](https://github.com/vllm-project/vllm/commit/722d169339) [#55457](https://github.com/vllm-project/vllm/pull/55457)
  [CI] Align extraction test with canonical auxiliary layer order (#55457)
  _Files: `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`_
- **2026-09-05** [`52bc900d93`](https://github.com/vllm-project/vllm/commit/52bc900d93) [#53835](https://github.com/vllm-project/vllm/pull/53835)
  [Bugfix][Kernel] Build fused GDN MTP decode for SM110 (#53835)
  _Files: `CMakeLists.txt`_
- **2026-09-04** [`a11dfcff89`](https://github.com/vllm-project/vllm/commit/a11dfcff89) [#54860](https://github.com/vllm-project/vllm/pull/54860)
  [CI] Surface why the CRCR nightly report cannot read its Buildkite secret (#54860)
  _Files: `.buildkite/scripts/crcr-report.sh`_
- **2026-09-04** [`5e729d84eb`](https://github.com/vllm-project/vllm/commit/5e729d84eb) [#55349](https://github.com/vllm-project/vllm/pull/55349)
  [CI] Only run GitHub Actions on the main repo (#55349)
  _Files: `.github/workflows/add_label_automerge.yml`, `.github/workflows/buf.yml`, `.github/workflows/issue_autolabel.yml`, `.github/workflows/macos-smoke-test.yml` _+6 more__
- **2026-09-03** [`e41011129b`](https://github.com/vllm-project/vllm/commit/e41011129b) [#54379](https://github.com/vllm-project/vllm/pull/54379)
  [CI] Avoid logging test server environment values (#54379)
  _Files: `tests/entrypoints/unit_tests/test_remote_vllm_server.py`, `tests/utils.py`_
- **2026-09-03** [`859dd39512`](https://github.com/vllm-project/vllm/commit/859dd39512) [#54962](https://github.com/vllm-project/vllm/pull/54962)
  [Bugfix][Core] Wait for the previous PP tensor sends before the next forward pass (#54962)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-09-03** [`5e4e927b5e`](https://github.com/vllm-project/vllm/commit/5e4e927b5e) [#55044](https://github.com/vllm-project/vllm/pull/55044)
  [CI] Force HTTP/1.1 for runtime Git installs (#55044)
  _Files: `.buildkite/test_areas/misc.yaml`, `.buildkite/test_areas/models_language.yaml`_
- **2026-09-02** [`963054ed58`](https://github.com/vllm-project/vllm/commit/963054ed58) [#55023](https://github.com/vllm-project/vllm/pull/55023)
  [CI] Exclude nightly-dev tags from nightly DockerHub cleanup (#55023)
  _Files: `.buildkite/scripts/cleanup-nightly-builds.sh`_
- **2026-09-02** [`605c3ddcba`](https://github.com/vllm-project/vllm/commit/605c3ddcba) [#54190](https://github.com/vllm-project/vllm/pull/54190)
  [BUILD] Bump cutlass to v4.7.1 (#54190)
  _Files: `CMakeLists.txt`_
- **2026-09-02** [`76ba32160a`](https://github.com/vllm-project/vllm/commit/76ba32160a) [#54751](https://github.com/vllm-project/vllm/pull/54751)
  [CI] Shard CPU jobs above the 24h P90 threshold (#54751)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `tests/v1/e2e/test_cpu_linear_attn_chunked_prefix.py`_
- **2026-09-02** [`87deddc7a4`](https://github.com/vllm-project/vllm/commit/87deddc7a4) [#54893](https://github.com/vllm-project/vllm/pull/54893)
  [CI][Spec Decode] Add MTP placeholder-token regression coverage (#54893)
  _Files: `tests/v1/e2e/spec_decode/mtp/test_mtp.py`_
- **2026-09-02** [`878ec4bfee`](https://github.com/vllm-project/vllm/commit/878ec4bfee) [#52344](https://github.com/vllm-project/vllm/pull/52344)
  [CI] Shard entrypoints API-server tests (#52344)
  _Files: `.buildkite/test_areas/entrypoints.yaml`_
- **2026-09-02** [`3976eada8b`](https://github.com/vllm-project/vllm/commit/3976eada8b) [#54895](https://github.com/vllm-project/vllm/pull/54895)
  [CI] Use PR head label for Buildkite branch to avoid main collision (#54895)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-09-02** [`ad76610c40`](https://github.com/vllm-project/vllm/commit/ad76610c40) [#54863](https://github.com/vllm-project/vllm/pull/54863)
  [XPU][CI] Move heavy jobs to nightly test in Intel GPU CI (#54863)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-09-02** [`05201d8ecf`](https://github.com/vllm-project/vllm/commit/05201d8ecf) [#54753](https://github.com/vllm-project/vllm/pull/54753)
  [CI] Shard basic model initialization tests (#54753)
  _Files: `.buildkite/test_areas/models_basic.yaml`_
- **2026-09-01** [`3b6c0bdae9`](https://github.com/vllm-project/vllm/commit/3b6c0bdae9) [#54754](https://github.com/vllm-project/vllm/pull/54754)
  [CI] Shard long kernel test groups (#54754)
  _Files: `.buildkite/test_areas/kernels.yaml`_
- **2026-09-01** [`96031b8623`](https://github.com/vllm-project/vllm/commit/96031b8623) [#54752](https://github.com/vllm-project/vllm/pull/54752)
  [CI] Shard distributed model jobs above the 24h P90 threshold (#54752)
  _Files: `.buildkite/test_areas/models_distributed.yaml`_
- **2026-09-01** [`e90b608c42`](https://github.com/vllm-project/vllm/commit/e90b608c42) [#52353](https://github.com/vllm-project/vllm/pull/52353)
  [CI] Split nightly MTP acceptance tests (#52353)
  _Files: `.buildkite/test_areas/spec_decode.yaml`_
- **2026-09-01** [`a56e74afd6`](https://github.com/vllm-project/vllm/commit/a56e74afd6) [#54823](https://github.com/vllm-project/vllm/pull/54823)
  [CI] Remove MRV2-specific tests (#54823)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/model_runner_v2.yaml`, `tests/v1/distributed/test_pp_dp_v2.py`_
- **2026-09-01** [`16f16876fd`](https://github.com/vllm-project/vllm/commit/16f16876fd) [#54605](https://github.com/vllm-project/vllm/pull/54605)
  [CI] Read the CRCR report token from a Buildkite secret (#54605)
  _Files: `.buildkite/scripts/crcr-report.sh`_
- **2026-09-01** [`2f01039666`](https://github.com/vllm-project/vllm/commit/2f01039666) [#54806](https://github.com/vllm-project/vllm/pull/54806)
  [Misc] Share Buildkite CI failure skill across agents (#54806)
  _Files: `.agents/skills/ci-fails-buildkite/SKILL.md`, `.claude/skills/ci-fails-buildkite`_
- **2026-09-01** [`5414b4e694`](https://github.com/vllm-project/vllm/commit/5414b4e694) [#53980](https://github.com/vllm-project/vllm/pull/53980)
  [XPU][TEST] Add entrypoints test in Intel GPU CI (#53980)
  _Files: `.buildkite/intel_jobs/entrypoints_intel.yaml`_
- **2026-09-01** [`45aed9b0cd`](https://github.com/vllm-project/vllm/commit/45aed9b0cd) [#54650](https://github.com/vllm-project/vllm/pull/54650)
  [CI] Broaden tool-calling issue auto-labeling (#54650)
  _Files: `.github/workflows/issue_autolabel.yml`_
- **2026-09-01** [`e29af0a2af`](https://github.com/vllm-project/vllm/commit/e29af0a2af) [#54515](https://github.com/vllm-project/vllm/pull/54515)
  [XPU] bump up auto-round-lib to 0.15.0 (#54515)
  _Files: `requirements/xpu.txt`_
- **2026-08-31** [`89df6fcb80`](https://github.com/vllm-project/vllm/commit/89df6fcb80) [#54645](https://github.com/vllm-project/vllm/pull/54645)
  [CI] Broaden structured-output issue auto-labeling (#54645)
  _Files: `.github/workflows/issue_autolabel.yml`_
- **2026-08-31** [`b05acd2ae0`](https://github.com/vllm-project/vllm/commit/b05acd2ae0) [#53669](https://github.com/vllm-project/vllm/pull/53669)
  [XPU] [CI] Add retry for v1/sample in Intel GPU CI (#53669)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-08-31** [`e2c8eeac40`](https://github.com/vllm-project/vllm/commit/e2c8eeac40) [#53677](https://github.com/vllm-project/vllm/pull/53677)
  [kernel] Fused embedding kernel  (#53677)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_vocab_parallel_embedding.py`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+4 more__

## Models  (22 commits)

- **2026-09-07** [`f2d45f26bd`](https://github.com/vllm-project/vllm/commit/f2d45f26bd) [#54917](https://github.com/vllm-project/vllm/pull/54917)
  [Bugfix][Gemma] Conditionally create KV projections/norms on KV-shared layers (#54917)
  _Files: `tests/models/language/generation/test_gemma.py`, `vllm/model_executor/models/gemma3n.py`, `vllm/model_executor/models/gemma4.py`_
- **2026-09-07** [`3dc7a68ce4`](https://github.com/vllm-project/vllm/commit/3dc7a68ce4) [#54797](https://github.com/vllm-project/vllm/pull/54797)
  [Perf] Extend Qwen Triton warmup to avoid first-request latency spikes (#54797)
  _Files: `tests/model_executor/test_mamba_triton_warmup.py`, `tests/model_executor/test_qwen_triton_warmup.py`, `tests/model_executor/test_qwen_vl_triton_warmup.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+3 more__
- **2026-09-05** [`28e605fb33`](https://github.com/vllm-project/vllm/commit/28e605fb33) [#55375](https://github.com/vllm-project/vllm/pull/55375)
  [Bugfix][Qwen4Exp] fix state index strides in fused PLE conv (#55375)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/nvidia/ops/ple.py`_
- **2026-09-05** [`7fbd44cbe0`](https://github.com/vllm-project/vllm/commit/7fbd44cbe0) [#55299](https://github.com/vllm-project/vllm/pull/55299)
  [Bugfix][DSv4] Seed the -1 sentinel in the prefill sparse index workspace (#55299)
  _Files: `vllm/models/deepseek_v4/common/ops/cache_utils.py`_
- **2026-09-04** [`3f41d102c5`](https://github.com/vllm-project/vllm/commit/3f41d102c5) [#50945](https://github.com/vllm-project/vllm/pull/50945)
  [1/2][Model Runner V2] DBO support, eager mode (#50945)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `tests/v1/worker/test_gpu_ubatch_slicing.py`, `vllm/config/parallel.py`, `vllm/config/vllm.py` _+13 more__
- **2026-09-04** [`fd4a151262`](https://github.com/vllm-project/vllm/commit/fd4a151262) [#54687](https://github.com/vllm-project/vllm/pull/54687)
  [Kernel] Reuse Qwen4Exp HC combine-norm for MTP input (#54687)
  _Files: `tests/models/qwen4_exp/test_hc_ops.py`, `vllm/models/qwen4_exp/nvidia/hyperconnection.py`, `vllm/models/qwen4_exp/nvidia/model.py`, `vllm/models/qwen4_exp/nvidia/mtp.py` _+1 more__
- **2026-09-04** [`19c018ec05`](https://github.com/vllm-project/vllm/commit/19c018ec05) [#54908](https://github.com/vllm-project/vllm/pull/54908)
  [Bugfix][DCP] Materialize prefill keys on non-owner ranks (#54908)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/common/kernels.py`_
- **2026-09-03** [`bb363db9a5`](https://github.com/vllm-project/vllm/commit/bb363db9a5) [#54982](https://github.com/vllm-project/vllm/pull/54982)
  feat: Add support for reasoning_token_count to reasoning parser (#54982)
  _Files: `tests/reasoning/test_cohere_command_reasoning_parser.py`, `vllm/reasoning/cohere_command_reasoning_parser.py`_
- **2026-09-03** [`758c79e1c5`](https://github.com/vllm-project/vllm/commit/758c79e1c5) [#55083](https://github.com/vllm-project/vllm/pull/55083)
  [Bugfix] Retain vocab embeddings during replacement (#55083)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/model_executor/models/transformers/base.py`_
- **2026-09-03** [`1f76efaa21`](https://github.com/vllm-project/vllm/commit/1f76efaa21) [#55063](https://github.com/vllm-project/vllm/pull/55063)
  [Model] Add K2-Horizon model support (#55063)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/reasoning/test_k2_horizon_reasoning_parser.py`, `tests/tool_parsers/test_k2_horizon_tool_parser.py` _+6 more__
- **2026-09-03** [`27a94d1ce4`](https://github.com/vllm-project/vllm/commit/27a94d1ce4) [#55042](https://github.com/vllm-project/vllm/pull/55042)
  [CI] Fix DeepSeek-V4 registry platform guard (#55042)
  _Files: `tests/models/test_registry.py`_
- **2026-09-02** [`a0d3e5c16e`](https://github.com/vllm-project/vllm/commit/a0d3e5c16e) [#53678](https://github.com/vllm-project/vllm/pull/53678)
  [XPU] Add fused GemmaRMSNorm path for eager execution (#53678)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/layers/layernorm.py`_
- **2026-09-02** [`60857baa53`](https://github.com/vllm-project/vllm/commit/60857baa53) [#54854](https://github.com/vllm-project/vllm/pull/54854)
  [Bugfix][Rust Frontend][Renderer] Align DeepSeek V4 historical developer message handling (#54854)
  _Files: `rust/src/chat/src/renderer/deepseek_v4/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`_
- **2026-09-02** [`584e8f0dda`](https://github.com/vllm-project/vllm/commit/584e8f0dda) [#49869](https://github.com/vllm-project/vllm/pull/49869)
  [Model] Fix GLM-OCR MTP weight loading (#49869)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/utils.py`_
- **2026-09-02** [`1d8d7a3965`](https://github.com/vllm-project/vllm/commit/1d8d7a3965) [#54815](https://github.com/vllm-project/vllm/pull/54815)
  [Bugfix] Fix RoPE construction for deepseek-v4 sparse SWA layers (#54815)
  _Files: `vllm/models/deepseek_v4/common/rope.py`_
- **2026-09-02** [`dbf1a044ea`](https://github.com/vllm-project/vllm/commit/dbf1a044ea) [#54847](https://github.com/vllm-project/vllm/pull/54847)
  [Bugfix] Fix ColQwen3.5 pooler projector initialization (#54847)
  _Files: `vllm/model_executor/models/colqwen3_5.py`_
- **2026-09-01** [`3439bad37e`](https://github.com/vllm-project/vllm/commit/3439bad37e) [#54303](https://github.com/vllm-project/vllm/pull/54303)
  [Rust Frontend] Bound recursive argument parsers (#54303)
  _Files: `rust/src/parser/src/tool/minimax_m3.rs`, `rust/src/parser/src/unified/gemma4.rs`, `rust/src/parser/src/utils.rs`, `rust/src/parser/src/utils/recursion.rs`_
- **2026-09-01** [`f1e5fdd7f2`](https://github.com/vllm-project/vllm/commit/f1e5fdd7f2) [#54760](https://github.com/vllm-project/vllm/pull/54760)
  [Transformers backend] Replace vocab embeddings in `recursive_replace` (#54760)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/utils.py`_
- **2026-09-01** [`191cecd51e`](https://github.com/vllm-project/vllm/commit/191cecd51e) [#54560](https://github.com/vllm-project/vllm/pull/54560)
  [Kernel][Qwen] Add Hopper LL-GEMM tuning table for Qwen4Exp (#54560)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/qwen4_exp/nvidia/low_latency_gemm.py`_
- **2026-09-01** [`d4329ba53d`](https://github.com/vllm-project/vllm/commit/d4329ba53d) [#53281](https://github.com/vllm-project/vllm/pull/53281)
  [Bugfix][Rust Frontend] Fix adjacent DeepSeek V4 user content rendering (#53281)
  _Files: `rust/src/chat/src/renderer/deepseek_v4/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`_
- **2026-08-31** [`9debcd5990`](https://github.com/vllm-project/vllm/commit/9debcd5990) [#53529](https://github.com/vllm-project/vllm/pull/53529)
  [Test][Qwen3-VL] Cover compiled DeepStack input contract (#53529)
  _Files: `tests/compile/test_deepstack_input_contract.py`_
- **2026-08-31** [`44fe2a392b`](https://github.com/vllm-project/vllm/commit/44fe2a392b) [#53921](https://github.com/vllm-project/vllm/pull/53921)
  [CPU] add CPU support for Voxtral (#53921)
  _Files: `vllm/model_executor/models/whisper_causal.py`_

## Disaggregation / PD  (22 commits)

- **2026-09-07** [`49eb2accf0`](https://github.com/vllm-project/vllm/commit/49eb2accf0) [#47505](https://github.com/vllm-project/vllm/pull/47505)
  [KVConnector] Guard lmcache_mp_connector state transition with num_external_tokens (#47505)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`_
- **2026-09-07** [`34b1e9f7a6`](https://github.com/vllm-project/vllm/commit/34b1e9f7a6) [#54643](https://github.com/vllm-project/vllm/pull/54643)
  [Bugfix][MooncakeStore] Fix finish-time save crash on hybrid models (#54643)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py`_
- **2026-09-07** [`6fbb00b188`](https://github.com/vllm-project/vllm/commit/6fbb00b188) [#41567](https://github.com/vllm-project/vllm/pull/41567)
  [EPD] Add ECMooncakeConnector for encoder cache over Mooncake TransferEngine (#41567)
  _Files: `.buildkite/test_areas/disaggregated_mooncake.yaml`, `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/core/test_encoder_cache_manager.py`, `tests/v1/core/test_scheduler.py` _+26 more__
- **2026-09-04** [`eb74fbb3e7`](https://github.com/vllm-project/vllm/commit/eb74fbb3e7) [#54518](https://github.com/vllm-project/vllm/pull/54518)
  [Bugfix][NIXL] Don't assert when a failed transfer is cleaned up twice (#54518)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-09-04** [`ae2d1ca96f`](https://github.com/vllm-project/vllm/commit/ae2d1ca96f) [#52755](https://github.com/vllm-project/vllm/pull/52755)
  [Rust Frontend] Record Mooncake/NIXL KV-connector metrics (#52755)
  _Files: `rust/src/engine-core-client/src/metrics.rs`, `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py` _+6 more__
- **2026-09-04** [`e35298628f`](https://github.com/vllm-project/vllm/commit/e35298628f) [#54878](https://github.com/vllm-project/vllm/pull/54878)
  [Bugfix][KV Connector] Fix DecodeBenchConnector prefix block selection (#54878)
  _Files: `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-09-04** [`8a0a7ee40a`](https://github.com/vllm-project/vllm/commit/8a0a7ee40a) [#47941](https://github.com/vllm-project/vllm/pull/47941)
  [EC Connector] P2P NIXL + CPU EC Connector (#47941)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_embedding_cache.py`, `tests/v1/ec_connector/unit/cpu/test_connector.py`, `tests/v1/ec_connector/unit/cpu/worker/test_worker.py` _+24 more__
- **2026-09-04** [`25268f0c9c`](https://github.com/vllm-project/vllm/commit/25268f0c9c) [#51886](https://github.com/vllm-project/vllm/pull/51886)
  [KVConnector] Add retention interval to OffloadingConnector (#51886)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py` _+5 more__
- **2026-09-04** [`d9e2b5238d`](https://github.com/vllm-project/vllm/commit/d9e2b5238d) [#51381](https://github.com/vllm-project/vllm/pull/51381)
  [Core][KV Events] Echo session_id on GPU BlockStored events (#51381)
  _Files: `examples/features/kv_events/kv_events_subscriber.py`, `tests/distributed/test_kv_cache_events.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py`, `tests/v1/core/test_prefix_caching.py` _+2 more__
- **2026-09-03** [`4ae6228284`](https://github.com/vllm-project/vllm/commit/4ae6228284) [#54325](https://github.com/vllm-project/vllm/pull/54325)
  [Bugfix][KV Connector] Populate SimpleCPUOffload BlockStored metadata (#54325)
  _Files: `tests/v1/kv_connector/unit/test_simple_cpu_offload_connector.py`, `tests/v1/simple_kv_offload/test_kv_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-09-03** [`31e9c13685`](https://github.com/vllm-project/vllm/commit/31e9c13685) [#54879](https://github.com/vllm-project/vllm/pull/54879)
  [Bugfix][KV Connector] Safely fill circular buffers in DecodeBench (#54879)
  _Files: `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-09-03** [`092334c828`](https://github.com/vllm-project/vllm/commit/092334c828) [#52923](https://github.com/vllm-project/vllm/pull/52923)
  [Bugfix] Wait for offload keys before storing chunks (#52923)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-02** [`41848caa63`](https://github.com/vllm-project/vllm/commit/41848caa63) [#51952](https://github.com/vllm-project/vllm/pull/51952)
  [NIXL] Use int32 array for indices to avoid intermediate conversion (#51952)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/distributed/eplb/eplb_communicator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/v1/kv_offload/base.py` _+5 more__
- **2026-09-02** [`f81eb41934`](https://github.com/vllm-project/vllm/commit/f81eb41934) [#54803](https://github.com/vllm-project/vllm/pull/54803)
  [Bugfix] `adjust_dcp_kv_cache_interleave_size` for NixlConnector only (#54803)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`, `vllm/distributed/kv_transfer/kv_transfer_state.py`_
- **2026-09-01** [`18c53727ce`](https://github.com/vllm-project/vllm/commit/18c53727ce) [#54679](https://github.com/vllm-project/vllm/pull/54679)
  [Bugfix][KV Connector] Fix DecodeBench DCP block selection (#54679)
  _Files: `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-09-01** [`5cc32fbdfa`](https://github.com/vllm-project/vllm/commit/5cc32fbdfa) [#54272](https://github.com/vllm-project/vllm/pull/54272)
  [Bugfix][KV Connector] Fix Mooncake physical-block transfer length (#54272)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-09-01** [`7cb9a88f50`](https://github.com/vllm-project/vllm/commit/7cb9a88f50) [#52832](https://github.com/vllm-project/vllm/pull/52832)
  [Bugfix][Mooncake] Offload producer partial tails on request finish (#52832)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py` _+6 more__
- **2026-09-01** [`c866ba9d11`](https://github.com/vllm-project/vllm/commit/c866ba9d11) [#53129](https://github.com/vllm-project/vllm/pull/53129)
  [KV Connector] Support heterogeneous TP sharing in Mooncake Store Connector (#53129)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_layout.py`, `tests/v1/kv_connector/unit/test_mooncake_store_prepare_values.py` _+4 more__
- **2026-09-01** [`d0e695a91b`](https://github.com/vllm-project/vllm/commit/d0e695a91b) [#53784](https://github.com/vllm-project/vllm/pull/53784)
  [Distributed] Support pre-shared ncclUniqueId rendezvous for weight transfer (#53784)
  _Files: `tests/distributed/test_weight_transfer_nccl_uid.py`, `vllm/distributed/device_communicators/pynccl.py`, `vllm/distributed/device_communicators/pynccl_wrapper.py`, `vllm/distributed/weight_transfer/nccl_common.py` _+2 more__
- **2026-09-01** [`4ac452ad98`](https://github.com/vllm-project/vllm/commit/4ac452ad98) [#51485](https://github.com/vllm-project/vllm/pull/51485)
  [Core] Release NCCL communicator memory in sleep mode (#51485)
  _Files: `tests/distributed/test_pynccl.py`, `tests/v1/worker/test_kv_cache_allocation_scope.py`, `tests/v1/worker/test_sleep_mode_backend.py`, `vllm/config/model.py` _+8 more__
- **2026-09-01** [`30dd1a7954`](https://github.com/vllm-project/vllm/commit/30dd1a7954) [#54647](https://github.com/vllm-project/vllm/pull/54647)
  [DecodeBenchConnector] Fix HMA cache-group mapping (#54647)
  _Files: `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`_
- **2026-09-01** [`188716ace7`](https://github.com/vllm-project/vllm/commit/188716ace7) [#53190](https://github.com/vllm-project/vllm/pull/53190)
  [Bugfix][EC Connector] Fall back when MADV_POPULATE_WRITE is unsupported (#53190)
  _Files: `tests/v1/ec_connector/unit/cpu/test_ec_shared_region.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/ec_shared_region.py`_

## Quantization  (20 commits)

- **2026-09-07** [`392db567b2`](https://github.com/vllm-project/vllm/commit/392db567b2) [#55660](https://github.com/vllm-project/vllm/pull/55660)
  [CI] [Test] skip test_wna16_cuda_high_bit_skips_humming on non-CUDA platforms (#55660)
  _Files: `tests/quantization/test_auto_round.py`_
- **2026-09-07** [`f43ef1531d`](https://github.com/vllm-project/vllm/commit/f43ef1531d) [#55630](https://github.com/vllm-project/vllm/pull/55630)
  [CI] fix pre-commit (#55630)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8.cu`_
- **2026-09-07** [`294fbb4f59`](https://github.com/vllm-project/vllm/commit/294fbb4f59) [#52890](https://github.com/vllm-project/vllm/pull/52890)
  add 2/3/5/6/7 CUDA support in AutoRound format (#52890)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`_
- **2026-09-07** [`4df80187b5`](https://github.com/vllm-project/vllm/commit/4df80187b5) [#55180](https://github.com/vllm-project/vllm/pull/55180)
  [Kernel] SM 12.x blockwise FP8: swizzle the CTA raster when the weight exceeds the L2 (#55180)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8.cu`, `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`, `tests/kernels/quantization/test_cutlass_scaled_mm.py`_
- **2026-09-04** [`69cf055936`](https://github.com/vllm-project/vllm/commit/69cf055936) [#55061](https://github.com/vllm-project/vllm/pull/55061)
  [Performance][DSv4] Size dequant gather launch grid by rows (#55061)
  _Files: `vllm/models/deepseek_v4/nvidia/ops/dequant_gather_k_cutedsl.py`_
- **2026-09-03** [`b7624069ff`](https://github.com/vllm-project/vllm/commit/b7624069ff) [#51415](https://github.com/vllm-project/vllm/pull/51415)
  [Fusion] Manual `ActivationQuantFusionPass` initial application (#51415)
  _Files: `tests/compile/fusions_e2e/common.py`, `tests/compile/fusions_e2e/test_tp1_quant.py`, `tests/compile/fusions_e2e/test_tp2_ar_rms.py`, `tests/compile/fusions_e2e/test_tp2_async_tp.py` _+6 more__
- **2026-09-03** [`d4d703caf9`](https://github.com/vllm-project/vllm/commit/d4d703caf9) [#54882](https://github.com/vllm-project/vllm/pull/54882)
  [Bugfix][Model] Fix FP8 PLE loading in mixed ModelOpt checkpoints (#54882)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/nvidia/ple_layer.py`_
- **2026-09-02** [`1945a94575`](https://github.com/vllm-project/vllm/commit/1945a94575) [#54996](https://github.com/vllm-project/vllm/pull/54996)
  [Bugfix][Tests] Stabilize B12X linear kernel checks (#54996)
  _Files: `tests/kernels/quantization/test_block_fp8.py`, `tests/model_executor/kernels/test_b12x_linear.py`_
- **2026-09-02** [`7894394b07`](https://github.com/vllm-project/vllm/commit/7894394b07) [#51285](https://github.com/vllm-project/vllm/pull/51285)
  [Online quantization] Add targeted online quantization configuration based on user patterns (#51285)
  _Files: `docs/features/quantization/online.md`, `tests/quantization/test_config_utils.py`, `tests/quantization/test_online.py`, `tests/quantization/test_quantization_config_args.py` _+7 more__
- **2026-09-02** [`aae36577fb`](https://github.com/vllm-project/vllm/commit/aae36577fb) [#54861](https://github.com/vllm-project/vllm/pull/54861)
  [XPU][UT] skip fp8_per_channel test on XPU (#54861)
  _Files: `tests/quantization/test_online.py`_
- **2026-09-02** [`1e300895ac`](https://github.com/vllm-project/vllm/commit/1e300895ac) [#54722](https://github.com/vllm-project/vllm/pull/54722)
  [Qwen4] validate FP8 PLE weight scale after loading (#54722)
  _Files: `tests/models/qwen4_exp/test_ple.py`, `vllm/models/qwen4_exp/nvidia/ple_layer.py`_
- **2026-09-02** [`ee3c00bbf4`](https://github.com/vllm-project/vllm/commit/ee3c00bbf4) [#51453](https://github.com/vllm-project/vllm/pull/51453)
  [Performance] Register Triton W4A16 GEMM as a custom op (#51453)
  _Files: `tests/kernels/quantization/test_triton_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`_
- **2026-09-01** [`4bf06be985`](https://github.com/vllm-project/vllm/commit/4bf06be985) [#54745](https://github.com/vllm-project/vllm/pull/54745)
  [CI] Disable CUDA graphs for GLM PCP evals (#54745)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`_
- **2026-09-01** [`514c7314a0`](https://github.com/vllm-project/vllm/commit/514c7314a0) [#53568](https://github.com/vllm-project/vllm/pull/53568)
  [Perf][Kernel] Initialize NVFP4 padding in quant kernel (#53568)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_quant_kernels.cu`, `tests/kernels/quantization/test_nvfp4_quant.py`, `vllm/_custom_ops.py`_
- **2026-09-01** [`40824284bc`](https://github.com/vllm-project/vllm/commit/40824284bc) [#49936](https://github.com/vllm-project/vllm/pull/49936)
  [Doc] Document FP8 GEMM kernel selection and Blackwell support (#49936)
  _Files: `.github/CODEOWNERS`, `docs/features/quantization/llm_compressor/fp8.md`_
- **2026-09-01** [`92ccd2c306`](https://github.com/vllm-project/vllm/commit/92ccd2c306) [#47237](https://github.com/vllm-project/vllm/pull/47237)
  [Bugifx][INC] Fix INC quantization method selection for non-quantized layers (#47237)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/inc.py`_
- **2026-08-31** [`85c1365bd9`](https://github.com/vllm-project/vllm/commit/85c1365bd9) [#53790](https://github.com/vllm-project/vllm/pull/53790)
  [Bugfix] NemotronHMTP: add hf_to_vllm_mapper so quant exclusions reach the MTP draft (#53790)
  _Files: `vllm/model_executor/models/nemotron_h_mtp.py`_
- **2026-08-31** [`65ce85fcdc`](https://github.com/vllm-project/vllm/commit/65ce85fcdc) [#52961](https://github.com/vllm-project/vllm/pull/52961)
  Add Laguna-XS-2.1-INT4 to nightly CI (#52961)
  _Files: `tests/evals/gsm8k/configs/Laguna-XS-2.1-INT4.yaml`, `tests/evals/gsm8k/configs/Laguna-XS.2-NVFP4.yaml`, `tests/evals/gsm8k/configs/models-blackwell.txt`, `tests/evals/gsm8k/configs/models-small.txt`_
- **2026-08-31** [`bd575a0d0b`](https://github.com/vllm-project/vllm/commit/bd575a0d0b) [#47434](https://github.com/vllm-project/vllm/pull/47434)
  [AutoRound] Support AutoRound Format Block-Wise FP8 in vLLM (#47434)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/config_parser.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/__init__.py` _+6 more__
- **2026-08-31** [`2a61f060d3`](https://github.com/vllm-project/vllm/commit/2a61f060d3) [#53536](https://github.com/vllm-project/vllm/pull/53536)
  [XPU] Ensure unquantized linear weight is N-contiguous (#53536)
  _Files: `vllm/envs.py`, `vllm/model_executor/layers/linear.py`_

## Scheduler / Engine  (19 commits)

- **2026-09-07** [`cd64c2dea9`](https://github.com/vllm-project/vllm/commit/cd64c2dea9) [#55124](https://github.com/vllm-project/vllm/pull/55124)
  [Docs] Clarify admission control limits apply server-wide, not per DP rank (#55124)
  _Files: `docs/serving/data_parallel_deployment.md`, `vllm/config/scheduler.py`_
- **2026-09-07** [`c3ec0d29f5`](https://github.com/vllm-project/vllm/commit/c3ec0d29f5) [#55237](https://github.com/vllm-project/vllm/pull/55237)
  [Bugfix] Fix cuda profiler missing bug (#55237)
  _Files: `tests/v1/engine/test_async_llm.py`, `vllm/v1/engine/async_llm.py`_
- **2026-09-06** [`039ea82660`](https://github.com/vllm-project/vllm/commit/039ea82660) [#52957](https://github.com/vllm-project/vllm/pull/52957)
  [Core] Sync DP state on the first step of a wave (#52957)
  _Files: `tests/v1/engine/test_engine_core.py`, `vllm/config/parallel.py`, `vllm/engine/arg_utils.py`, `vllm/v1/engine/core.py`_
- **2026-09-04** [`131e0285f6`](https://github.com/vllm-project/vllm/commit/131e0285f6) [#54285](https://github.com/vllm-project/vllm/pull/54285)
  [Frontend] Warn when removed guided-decoding fields are present in a request (#54285)
  _Files: `vllm/entrypoints/serve/engine/protocol.py`_
- **2026-09-04** [`e862c2f45b`](https://github.com/vllm-project/vllm/commit/e862c2f45b) [#54265](https://github.com/vllm-project/vllm/pull/54265)
  [Docs] Add example for Renderer.render_cmpl() usage (#54265)
  _Files: `vllm/v1/engine/async_llm.py`_
- **2026-09-04** [`560ef78bfe`](https://github.com/vllm-project/vllm/commit/560ef78bfe) [#54901](https://github.com/vllm-project/vllm/pull/54901)
  [Perf][Model Runner V2] Compact sampling masks on GPU instead of unpacking the full-vocab bitmask on CPU (#54901)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py`, `tests/test_config.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/test_outputs.py` _+6 more__
- **2026-09-03** [`2a336d8239`](https://github.com/vllm-project/vllm/commit/2a336d8239) [#54557](https://github.com/vllm-project/vllm/pull/54557)
  [warmup] overlap renderer warmup and engine core initialization (#54557)
  _Files: `tests/renderers/test_warmup.py`, `vllm/renderers/base.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/core_client.py` _+1 more__
- **2026-09-03** [`ee0a4c46ae`](https://github.com/vllm-project/vllm/commit/ee0a4c46ae) [#55111](https://github.com/vllm-project/vllm/pull/55111)
  [Bugfix] Account for PCP in multi-node world size validation (#55111)
  _Files: `tests/engine/test_arg_utils.py`, `vllm/engine/arg_utils.py`_
- **2026-09-02** [`ad127d9a0f`](https://github.com/vllm-project/vllm/commit/ad127d9a0f) [#55012](https://github.com/vllm-project/vllm/pull/55012)
  [Perf][Rust Frontend] Coalesce decoded chunks per engine update (#55012)
  _Files: `rust/src/text/src/output/decoded.rs`_
- **2026-09-02** [`ffe3bb3c72`](https://github.com/vllm-project/vllm/commit/ffe3bb3c72) [#49209](https://github.com/vllm-project/vllm/pull/49209)
  [Hardware][XPU] Register matmul and linear batch-invariant kernels for XPU (#49209)
  _Files: `docs/features/batch_invariance.md`, `tests/v1/determinism/test_batch_invariance.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/determinism/batch_invariant.py` _+3 more__
- **2026-09-02** [`300f688321`](https://github.com/vllm-project/vllm/commit/300f688321) [#54838](https://github.com/vllm-project/vllm/pull/54838)
  [Bugfix] Implicitly close DeepSeek DSML parameters (#54838)
  _Files: `tests/parser/engine/test_deepseek_v32.py`, `tests/parser/engine/test_deepseek_v4.py`, `vllm/parser/deepseek_v32.py`, `vllm/parser/deepseek_v4.py`_
- **2026-09-01** [`55178f2d09`](https://github.com/vllm-project/vllm/commit/55178f2d09) [#51678](https://github.com/vllm-project/vllm/pull/51678)
  [Bugfix][Profiler] Fix API server crash on double /stop_profile (#51678)
  _Files: `vllm/v1/engine/async_llm.py`_
- **2026-08-31** [`24d42f3553`](https://github.com/vllm-project/vllm/commit/24d42f3553) [#54549](https://github.com/vllm-project/vllm/pull/54549)
  [CI] Mark 1-GPU L4 test steps with device: l4 for EKS migration (#54549)
  _Files: `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/models_language.yaml` _+1 more__
- **2026-08-31** [`f9c7c6e090`](https://github.com/vllm-project/vllm/commit/f9c7c6e090) [#54481](https://github.com/vllm-project/vllm/pull/54481)
  [Rust Frontend][CI] Remove TCP port races from mock-engine tests (#54481)
  _Files: `rust/src/mock-engine/src/tests.rs`_
- **2026-08-31** [`f5e441de10`](https://github.com/vllm-project/vllm/commit/f5e441de10) [#53976](https://github.com/vllm-project/vllm/pull/53976)
  [Bugfix][Test] Fix off-by-one error in sampled token rank causing flaky logprobs test (#53976)
  _Files: `tests/v1/engine/utils.py`_
- **2026-08-31** [`39e276eaeb`](https://github.com/vllm-project/vllm/commit/39e276eaeb) [#54218](https://github.com/vllm-project/vllm/pull/54218)
  [Structured Output] Let terminal grammars stop under min_tokens (II) (#54218)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/e2e/general/test_min_tokens.py`, `tests/v1/logits_processors/test_correctness.py`, `tests/v1/worker/test_gpu_logit_bias.py` _+3 more__
- **2026-08-31** [`dafbef15a1`](https://github.com/vllm-project/vllm/commit/dafbef15a1) [#49445](https://github.com/vllm-project/vllm/pull/49445)
  [Core] Add `max_num_queued_reqs` and `max_num_queued_tokens` for queue size management (#49445)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/speech_to_text/test_speech_to_text_cancellation.py`, `tests/v1/engine/test_admission_control.py`, `vllm/config/scheduler.py` _+14 more__
- **2026-08-31** [`eeb549a74d`](https://github.com/vllm-project/vllm/commit/eeb549a74d) [#54492](https://github.com/vllm-project/vllm/pull/54492)
  [Frontend] Move engine/protocol.py out openai folder (#54492)
- **2026-08-31** [`d8de4ae322`](https://github.com/vllm-project/vllm/commit/d8de4ae322) [#52912](https://github.com/vllm-project/vllm/pull/52912)
  [Bugfix][KVOffload] P2P tier declares REQUEST_LEVEL on the producer leg (#52912)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+1 more__

## Serving / API  (16 commits)

- **2026-09-07** [`ecd600d91e`](https://github.com/vllm-project/vllm/commit/ecd600d91e) [#55551](https://github.com/vllm-project/vllm/pull/55551)
  [Pooling] Honor max_embed_len for chunked embeddings (#55551)
  _Files: `vllm/entrypoints/pooling/base/protocol.py`_
- **2026-09-07** [`167858ea17`](https://github.com/vllm-project/vllm/commit/167858ea17) [#55701](https://github.com/vllm-project/vllm/pull/55701)
  [Frontend] Migrate Responses harmony input validation to VLLMValidationError (#55701)
  _Files: `tests/entrypoints/openai/responses/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_response_input_to_harmony.py`, `vllm/entrypoints/openai/responses/harmony.py`_
- **2026-09-07** [`6a2a2bb02b`](https://github.com/vllm-project/vllm/commit/6a2a2bb02b) [#50195](https://github.com/vllm-project/vllm/pull/50195)
  [Frontend] Add stateless /v1/responses/render endpoint (#50195)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/renderer.md`, `docs/usage/security.md`, `tests/entrypoints/launchers/test_cli_args.py` _+15 more__
- **2026-09-07** [`7dbe386833`](https://github.com/vllm-project/vllm/commit/7dbe386833) [#50257](https://github.com/vllm-project/vllm/pull/50257)
  [Frontend] Migrate Responses API validation errors to VLLMValidationError (#50257)
  _Files: `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `vllm/entrypoints/openai/parser/harmony_utils.py`, `vllm/entrypoints/openai/responses/utils.py`_
- **2026-09-05** [`2902ca17e3`](https://github.com/vllm-project/vllm/commit/2902ca17e3) [#50254](https://github.com/vllm-project/vllm/pull/50254)
  [Bugfix] complete VLLMValidationError migration in chat_utils.py (#50254)
  _Files: `tests/entrypoints/launchers/test_cli_args.py`, `tests/renderers/test_hf.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-09-05** [`e962733e08`](https://github.com/vllm-project/vllm/commit/e962733e08) [#51444](https://github.com/vllm-project/vllm/pull/51444)
  [Security] Validate cache salts before they reach LMCache (#51444)
  _Files: `tests/entrypoints/openai/chat_completion/test_non_object_body_validation.py`, `tests/entrypoints/unit_tests/test_non_object_body_validation.py`, `vllm/entrypoints/generate/base/protocol.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+4 more__
- **2026-09-03** [`d6bce42983`](https://github.com/vllm-project/vllm/commit/d6bce42983) [#54883](https://github.com/vllm-project/vllm/pull/54883)
  [Rust Frontend] Report reasoning tokens in chat completion usage (#54883)
  _Files: `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/chat/src/event.rs`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/output/default/unified.rs` _+11 more__
- **2026-09-03** [`ee17d0d869`](https://github.com/vllm-project/vllm/commit/ee17d0d869) [#51445](https://github.com/vllm-project/vllm/pull/51445)
  Use server-generated keys for late-interaction query caches (#51445)
  _Files: `tests/entrypoints/pooling/scoring/test_late_interaction_serving.py`, `vllm/entrypoints/pooling/scoring/serving.py`, `vllm/entrypoints/pooling/typing.py`_
- **2026-09-02** [`cf3263d571`](https://github.com/vllm-project/vllm/commit/cf3263d571) [#55019](https://github.com/vllm-project/vllm/pull/55019)
  [Agents] Add Triton kernel-writing skill (#55019)
  _Files: `.agents/skills/triton-kernel-writing/SKILL.md`, `.agents/skills/triton-kernel-writing/agents/openai.yaml`_
- **2026-09-02** [`b2558f8da3`](https://github.com/vllm-project/vllm/commit/b2558f8da3) [#54913](https://github.com/vllm-project/vllm/pull/54913)
  [Bugfix] Fix launch render hanging on shutdown (#54913)
  _Files: `vllm/entrypoints/launchers/launcher.py`_
- **2026-09-01** [`b911fe85c4`](https://github.com/vllm-project/vllm/commit/b911fe85c4) [#52910](https://github.com/vllm-project/vllm/pull/52910)
  [Rust Frontend] Attribute decoded text to tokens (#52910)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/output/default/unified.rs`, `rust/src/chat/src/output/harmony/mod.rs` _+13 more__
- **2026-09-01** [`0ad5652a52`](https://github.com/vllm-project/vllm/commit/0ad5652a52) [#54622](https://github.com/vllm-project/vllm/pull/54622)
  [Bugfix][Frontend] Restore the chat template content format mismatch warning (#54622)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `vllm/renderers/hf.py`_
- **2026-09-01** [`fa99a6fea6`](https://github.com/vllm-project/vllm/commit/fa99a6fea6) [#54684](https://github.com/vllm-project/vllm/pull/54684)
  [Bugfix][Security] Bound the validation-error response body (#54684)
  _Files: `tests/entrypoints/serve/exception_handling/test_validation_exception_handler.py`, `vllm/entrypoints/serve/exception_handling/handlers/validation.py`_
- **2026-08-31** [`810bc3250c`](https://github.com/vllm-project/vllm/commit/810bc3250c) [#54537](https://github.com/vllm-project/vllm/pull/54537)
  [Frontend][Performance] Resolve async media across modalities concurrently (#54537)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-08-31** [`4ae172231c`](https://github.com/vllm-project/vllm/commit/4ae172231c) [#54315](https://github.com/vllm-project/vllm/pull/54315)
  [Frontend] Forward cache salt for content parts (#54315)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-31** [`687db59744`](https://github.com/vllm-project/vllm/commit/687db59744) [#54364](https://github.com/vllm-project/vllm/pull/54364)
  [Bugfix][Frontend] Truncate pooling prompts before padding them (#54364)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/renderers/test_completions.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`, `vllm/renderers/params.py`_

## KV Cache / Offload  (15 commits)

- **2026-09-06** [`dc02934a07`](https://github.com/vllm-project/vllm/commit/dc02934a07) [#54288](https://github.com/vllm-project/vllm/pull/54288)
  [Bugfix][KV Offload] Stop offloading the final sampled token's KV slot (#54288)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-06** [`569adb5a97`](https://github.com/vllm-project/vllm/commit/569adb5a97) [#54362](https://github.com/vllm-project/vllm/pull/54362)
  [Bugfix][KV Offload] Fix SWA store reachability during chunked prefill (#54362)
  _Files: `tests/v1/core/test_prefix_caching.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-09-06** [`9afb878a55`](https://github.com/vllm-project/vllm/commit/9afb878a55) [#55075](https://github.com/vllm-project/vllm/pull/55075)
  [Bugfix][KV Offload] Skip cleaned-up async lookup batches (#55075)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-09-06** [`144e79c810`](https://github.com/vllm-project/vllm/commit/144e79c810) [#53614](https://github.com/vllm-project/vllm/pull/53614)
  [Kimi K3] Support internal prefix checkpoints with partial prefix caching and spec-decoding (#53614)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_mamba_align_chunk_split.py`, `tests/v1/core/test_prefix_caching.py` _+7 more__
- **2026-09-03** [`da8ec28268`](https://github.com/vllm-project/vllm/commit/da8ec28268) [#52807](https://github.com/vllm-project/vllm/pull/52807)
  [Bugfix][KV Offload] Do not let a recurrent group's unhashed block truncate the load boundary (#52807)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-02** [`ba6c60e98f`](https://github.com/vllm-project/vllm/commit/ba6c60e98f) [#50883](https://github.com/vllm-project/vllm/pull/50883)
  [Bugfix][KV Offload] Scale UniformTypeKVCacheSpecs groups by DCP (#50883)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-09-02** [`35faf957d6`](https://github.com/vllm-project/vllm/commit/35faf957d6) [#54872](https://github.com/vllm-project/vllm/pull/54872)
  [Bugfix][KV Offload] Ignore stale async lookup results (#54872)
  _Files: `tests/v1/kv_offload/tiering/test_async_lookup.py`, `vllm/v1/kv_offload/tiering/async_lookup.py`_
- **2026-09-02** [`2a4e3cc3db`](https://github.com/vllm-project/vllm/commit/2a4e3cc3db) [#54759](https://github.com/vllm-project/vllm/pull/54759)
  [Bugfix][KV Offload] Ensure tracker progress for oversized offers (#54759)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py`_
- **2026-09-02** [`df09c76735`](https://github.com/vllm-project/vllm/commit/df09c76735) [#51690](https://github.com/vllm-project/vllm/pull/51690)
  [KV Connector][Offloading] Look through UniformTypeKVCacheSpecs in the canonical portability gate (#51690)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-09-02** [`12b9573c98`](https://github.com/vllm-project/vllm/commit/12b9573c98) [#53532](https://github.com/vllm-project/vllm/pull/53532)
  [Bugfix][KV Offloading] Fix eager SimpleCPUOffload cache registration and final flush (#53532)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-09-01** [`c35551f892`](https://github.com/vllm-project/vllm/commit/c35551f892) [#52290](https://github.com/vllm-project/vllm/pull/52290)
  [Bugfix][KV Offload] Isolate tiering shutdown failures (#52290)
  _Files: `vllm/v1/kv_offload/tiering/manager.py`_
- **2026-08-31** [`4c58a0c398`](https://github.com/vllm-project/vllm/commit/4c58a0c398) [#52596](https://github.com/vllm-project/vllm/pull/52596)
  [Bugfix][KV Offload] Unlink /dev/shm region after all workers map it (barrier variant of #51317) (#52596)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-08-31** [`e0d27040dd`](https://github.com/vllm-project/vllm/commit/e0d27040dd) [#52571](https://github.com/vllm-project/vllm/pull/52571)
  [Bugfix][KV Offload][P2P] Preserve aborted loads until abort completion (#52571)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py`_
- **2026-08-31** [`bed3280f50`](https://github.com/vllm-project/vllm/commit/bed3280f50) [#50696](https://github.com/vllm-project/vllm/pull/50696)
  [KV offload] Order CPU->GPU loads against the compute stream (#50696)
  _Files: `vllm/v1/kv_offload/cpu/gpu_worker.py`_
- **2026-08-31** [`9acbc5360a`](https://github.com/vllm-project/vllm/commit/9acbc5360a) [#52068](https://github.com/vllm-project/vllm/pull/52068)
  [KV Offload] Preserve KV event metadata until final residency removal (#52068)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`, `vllm/v1/kv_offload/base.py`_

## Perf / Benchmark  (10 commits)

- **2026-09-05** [`7985444339`](https://github.com/vllm-project/vllm/commit/7985444339) [#55059](https://github.com/vllm-project/vllm/pull/55059)
  [Kernel][HY V4] Add Triton iHC pre/post fallback (#55059)
  _Files: `benchmarks/kernels/benchmark_hy_v4_ihc.py`, `vllm/models/hy_v4/nvidia/hc.py`, `vllm/models/hy_v4/nvidia/triton_ihc.py`_
- **2026-09-04** [`3284af6bf1`](https://github.com/vllm-project/vllm/commit/3284af6bf1) [#54887](https://github.com/vllm-project/vllm/pull/54887)
  [Bugfix] Reject 0 or non-positive max concurrency (#54887)
  _Files: `vllm/benchmarks/serve.py`_
- **2026-09-03** [`bc2ee48073`](https://github.com/vllm-project/vllm/commit/bc2ee48073) [#55020](https://github.com/vllm-project/vllm/pull/55020)
  [Perf] Prefetch the weight before the PDL wait in fused_q_kv_rmsnorm (#55020)
  _Files: `vllm/models/common/ops/fused_qk_rmsnorm.py`_
- **2026-09-03** [`0e14198a63`](https://github.com/vllm-project/vllm/commit/0e14198a63) [#54995](https://github.com/vllm-project/vllm/pull/54995)
  [Skills] Add kernel benchmark sanity references (#54995)
  _Files: `.agents/skills/kernel-microbenchmark/SKILL.md`_
- **2026-09-02** [`a56654d6de`](https://github.com/vllm-project/vllm/commit/a56654d6de) [#54565](https://github.com/vllm-project/vllm/pull/54565)
  [K3 Perf] Enable DSV3 GEMM for inner-contiguous and row-strided tensors, 12%~81% kernel performance improvement (#54565)
  _Files: `csrc/libtorch_stable/dsv3_fused_a_gemm.cu`, `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`_
- **2026-09-02** [`3ba9907a1d`](https://github.com/vllm-project/vllm/commit/3ba9907a1d) [#54697](https://github.com/vllm-project/vllm/pull/54697)
  [Kimi-K3] Overlap low-M TP8 KDA projections (#54697)
  _Files: `benchmarks/kernels/benchmark_kimi_k3_kda_projection.py`, `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/models/kimi_k3/nvidia/kda.py` _+3 more__
- **2026-09-01** [`259a209bfa`](https://github.com/vllm-project/vllm/commit/259a209bfa) [#53524](https://github.com/vllm-project/vllm/pull/53524)
  [Kimi-K3][Perf] Prefetch ll_bf16 router weights for M=1 (#53524)
  _Files: `tests/kernels/test_ll_bf16_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/_ll_bf16_dotprod.py`, `vllm/model_executor/kernels/linear/cute_dsl/ll_bf16.py`_
- **2026-09-01** [`9e905f7450`](https://github.com/vllm-project/vllm/commit/9e905f7450) [#54136](https://github.com/vllm-project/vllm/pull/54136)
  [Bugfix] Account for client queue time in serve benchmarks (#54136)
  _Files: `docs/benchmarking/cli.md`, `vllm/benchmarks/lib/endpoint_request_func.py`, `vllm/benchmarks/serve.py`_
- **2026-09-01** [`22df3a34e0`](https://github.com/vllm-project/vllm/commit/22df3a34e0) [#54449](https://github.com/vllm-project/vllm/pull/54449)
  [Perf][Rust Frontend] Count the tokenizer vocabulary once at construction (#54449)
  _Files: `rust/src/tokenizer/src/hf.rs`_
- **2026-08-31** [`d6d6658543`](https://github.com/vllm-project/vllm/commit/d6d6658543) [#54261](https://github.com/vllm-project/vllm/pull/54261)
  [Kimi-K3][Perf] Make native CUDA AttnRes the SM100 default (#54261)
  _Files: `benchmarks/kernels/benchmark_kimi_k3_attn_res.py`, `csrc/libtorch_stable/kimi_k3/attn_res_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+3 more__

## Speculative Decoding  (8 commits)

- **2026-09-07** [`b339d75a41`](https://github.com/vllm-project/vllm/commit/b339d75a41) [#55369](https://github.com/vllm-project/vllm/pull/55369)
  [Bugfix][Spec Decode] Resolve n_predict from text_config for Qwen3.5 multimodal MTP (#55369)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `tests/models/test_qwen3_5_mtp_config.py`, `vllm/config/speculative.py`_
- **2026-09-07** [`4a806d08ee`](https://github.com/vllm-project/vllm/commit/4a806d08ee) [#52771](https://github.com/vllm-project/vllm/pull/52771)
  [Bugfix] OffloadingConnector: stop zeroing offload hits under MTP/EAGLE spec decode (#52771)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-09-04** [`8f269a93bb`](https://github.com/vllm-project/vllm/commit/8f269a93bb) [#55392](https://github.com/vllm-project/vllm/pull/55392)
  Revert "[CI] Remove deleted nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 and its arch aliases" (#55392)
  _Files: `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/registry.py`_
- **2026-09-04** [`a26b71d868`](https://github.com/vllm-project/vllm/commit/a26b71d868) [#55126](https://github.com/vllm-project/vllm/pull/55126)
  [Bugfix][PD] Pad resumed speculative decode requests (#55126)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-09-02** [`6c6376a09e`](https://github.com/vllm-project/vllm/commit/6c6376a09e) [#55026](https://github.com/vllm-project/vllm/pull/55026)
  [CI] Remove deleted nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16 and its arch aliases (#55026)
  _Files: `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/registry.py`_
- **2026-09-01** [`76f3249fbd`](https://github.com/vllm-project/vllm/commit/76f3249fbd) [#54262](https://github.com/vllm-project/vllm/pull/54262)
  [Mypy] Fix typing for M models (#54262)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/mamba.py`, `vllm/model_executor/models/medusa.py`, `vllm/model_executor/models/mellum.py` _+22 more__
- **2026-09-01** [`481839ad9e`](https://github.com/vllm-project/vllm/commit/481839ad9e) [#53388](https://github.com/vllm-project/vllm/pull/53388)
  [Feature][Spec] Support disabling trailing prefix-cache block dropping (#53388)
  _Files: `tests/test_config.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/core/test_mamba_align_chunk_split.py` _+9 more__
- **2026-08-31** [`648b7468b8`](https://github.com/vllm-project/vllm/commit/648b7468b8) [#54482](https://github.com/vllm-project/vllm/pull/54482)
  [CI/Build] Fix Kimi K3 Eagle3 test fixture (#54482)
  _Files: `tests/models/kimi_k3/test_eagle3.py`_

## LoRA  (5 commits)

- **2026-09-07** [`8648446515`](https://github.com/vllm-project/vllm/commit/8648446515) [#53689](https://github.com/vllm-project/vllm/pull/53689)
  [XPU][LoRA] Support LoRA for DeepSeek V4 on XPU (#53689)
  _Files: `vllm/models/deepseek_v4/xpu/model.py`_
- **2026-09-03** [`2db1c4dc31`](https://github.com/vllm-project/vllm/commit/2db1c4dc31) [#54837](https://github.com/vllm-project/vllm/pull/54837)
  [Rust Frontend] Support `--lora-modules` for static adapter loading (#54837)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/cmd/src/cli/unsupported.rs`, `rust/src/engine-core-client/src/protocol/lora.rs` _+8 more__
- **2026-09-03** [`21a2211040`](https://github.com/vllm-project/vllm/commit/21a2211040) [#54884](https://github.com/vllm-project/vllm/pull/54884)
  [Rust Frontend] Use token-attributed text in reasoning and unified parsers (#54884)
  _Files: `rust/src/chat/src/output/default/unified.rs`, `rust/src/parser/benches/utils/adapter.rs`, `rust/src/parser/src/reasoning/cohere_cmd.rs`, `rust/src/parser/src/reasoning/deepseek_r1.rs` _+18 more__
- **2026-09-02** [`f5711fa138`](https://github.com/vllm-project/vllm/commit/f5711fa138) [#52350](https://github.com/vllm-project/vllm/pull/52350)
  [CI] Shard LoRA TP distributed tests (#52350)
  _Files: `.buildkite/test_areas/lora.yaml`_
- **2026-09-01** [`e7cf4730d6`](https://github.com/vllm-project/vllm/commit/e7cf4730d6) [#47562](https://github.com/vllm-project/vllm/pull/47562)
  [Bugfix] Drop incomplete tool-call markup in non-streaming to match streaming (#47562)
  _Files: `tests/parser/engine/test_inkling.py`, `tests/parser/engine/test_parser_engine.py`, `vllm/parser/abstract_parser.py`, `vllm/parser/engine/adapters.py` _+2 more__

## Compilation / CUDA Graph  (5 commits)

- **2026-09-04** [`685074cd61`](https://github.com/vllm-project/vllm/commit/685074cd61) [#55341](https://github.com/vllm-project/vllm/pull/55341)
  [Bugfix][V2] Warm up kernels before capturing CUDA graphs (#55341)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2.py`, `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `tests/v1/worker/test_workspace.py`, `vllm/v1/worker/gpu/cudagraph_utils.py` _+3 more__
- **2026-09-04** [`da55494a12`](https://github.com/vllm-project/vllm/commit/da55494a12) [#55271](https://github.com/vllm-project/vllm/pull/55271)
  docs: note that enforce_eager also disables torch.compile (#55271)
  _Files: `vllm/config/model.py`_
- **2026-09-03** [`0d3ede3e3b`](https://github.com/vllm-project/vllm/commit/0d3ede3e3b) [#54969](https://github.com/vllm-project/vllm/pull/54969)
  [Bugfix][Model] Enable torch.compile for StableLM (#54969)
  _Files: `vllm/model_executor/models/stablelm.py`_
- **2026-09-02** [`1c26e57d3c`](https://github.com/vllm-project/vllm/commit/1c26e57d3c) [#54782](https://github.com/vllm-project/vllm/pull/54782)
  [Bugfix] Raise for unavailable piecewise CUDA graphs (#54782)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-09-01** [`c28feab989`](https://github.com/vllm-project/vllm/commit/c28feab989) [#54646](https://github.com/vllm-project/vllm/pull/54646)
  [Core][MRV2] Freeze gc during V2 CG capture; skip per-descriptor cleanup (#54646)
  _Files: `vllm/compilation/breakable_cudagraph.py`, `vllm/utils/gc_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_

## Docs  (4 commits)

- **2026-09-07** [`58ad1f3b89`](https://github.com/vllm-project/vllm/commit/58ad1f3b89) [#55691](https://github.com/vllm-project/vllm/pull/55691)
  [Docs] Add OLMo 2 to batch-invariance tested models (#55691)
  _Files: `docs/features/batch_invariance.md`_
- **2026-09-05** [`e473e9036f`](https://github.com/vllm-project/vllm/commit/e473e9036f) [#54944](https://github.com/vllm-project/vllm/pull/54944)
  [Docs][Models] Use the official FunASR Nano vLLM checkpoint (#54944)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-09-03** [`c7e6e36fa9`](https://github.com/vllm-project/vllm/commit/c7e6e36fa9) [#54999](https://github.com/vllm-project/vllm/pull/54999)
  [Rust Frontend] Add support for TLS in render server (#54999)
  _Files: `rust/README.md`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/ssl.rs`, `rust/src/cmd/src/cli/tests.rs` _+1 more__
- **2026-09-01** [`cdefd9d499`](https://github.com/vllm-project/vllm/commit/cdefd9d499) [#54533](https://github.com/vllm-project/vllm/pull/54533)
  [Bugfix] Support Sentence Transformers 5.4+ serialized configs (#54533)
  _Files: `docs/models/pooling_models/README.md`, `tests/test_config.py`, `vllm/transformers_utils/config.py`_

---
_Generated 2026-09-07 14:14 UTC_