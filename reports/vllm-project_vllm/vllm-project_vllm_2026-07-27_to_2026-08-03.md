# vllm-project/vllm — Weekly Change Report
**Period:** 2026-07-27 → 2026-08-03  |  **Total commits:** 329

## ✨ New Features This Week

- **2026-08-03** [#49664](https://github.com/vllm-project/vllm/pull/49664) — [XPU] [Linear] add torch as xpu linear backend (#49664)
- **2026-08-03** [#50688](https://github.com/vllm-project/vllm/pull/50688) — [Model] Support jina-embeddings-v5-text-nano (EuroBERT encoder backbone) (#50688)
- **2026-08-02** [#44972](https://github.com/vllm-project/vllm/pull/44972) — [Test][V1] Add sleep/wake correctness regression test for hybrid GDN/… (#44972)
- **2026-08-02** [#50032](https://github.com/vllm-project/vllm/pull/50032) — [Attention][MiniMax-M3] Add MSA speculative decode verification (#50032)
- **2026-08-02** [#50661](https://github.com/vllm-project/vllm/pull/50661) — [Model Runner v2] Enable BGE M3 pooling embed token_classify (#50661)
- **2026-08-02** [#49934](https://github.com/vllm-project/vllm/pull/49934) — [1/N] Unify multiple-path encoder cuda graph support (#49934)
- **2026-08-01** [#46789](https://github.com/vllm-project/vllm/pull/46789) — [DSV4] Implement Sequence Parallelism (#46789)
- **2026-08-01** [#50608](https://github.com/vllm-project/vllm/pull/50608) — Add @hongxiayang as code owner for AMD-specific model files and ROCm docs (#50608)
- **2026-08-01** [#49611](https://github.com/vllm-project/vllm/pull/49611) — [Benchmark] Add probe requests to vllm bench serve (#49611)
- **2026-08-01** [#50574](https://github.com/vllm-project/vllm/pull/50574) — [Model Runner V2] Enable encoder token embedding (#50574)
- _…and 71 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-02** [`0055b8bfa3`](https://github.com/vllm-project/vllm/commit/0055b8bfa3) [#50032](https://github.com/vllm-project/vllm/pull/50032) — [Attention][MiniMax-M3] Add MSA speculative decode verification (#50032)
- **2026-08-02** [`c666810676`](https://github.com/vllm-project/vllm/commit/c666810676) [#50761](https://github.com/vllm-project/vllm/pull/50761) — [ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32 (#50761)
- **2026-08-01** [`127a7cebc9`](https://github.com/vllm-project/vllm/commit/127a7cebc9) [#50608](https://github.com/vllm-project/vllm/pull/50608) — Add @hongxiayang as code owner for AMD-specific model files and ROCm docs (#50608)
- **2026-08-01** [`77469c9057`](https://github.com/vllm-project/vllm/commit/77469c9057) [#50476](https://github.com/vllm-project/vllm/pull/50476) — [ROCm][MLA] Mask the AITER MLA small-head verify flatten causally (#50476)
- **2026-08-01** [`9c110fa522`](https://github.com/vllm-project/vllm/commit/9c110fa522) [#47189](https://github.com/vllm-project/vllm/pull/47189) — [Frontend] Cohere chat v2 api support (#47189)
- **2026-08-01** [`f7097a92fd`](https://github.com/vllm-project/vllm/commit/f7097a92fd) [#50639](https://github.com/vllm-project/vllm/pull/50639) — [Bugfix][CI] Prevent common ops imports from initializing CUDA (#50639)
- **2026-08-01** [`fcdc7c2e9c`](https://github.com/vllm-project/vllm/commit/fcdc7c2e9c) [#50330](https://github.com/vllm-project/vllm/pull/50330) — [CI] Organize speculative decoding E2E tests by coverage (#50330)
- **2026-07-31** [`4fdd3e0b74`](https://github.com/vllm-project/vllm/commit/4fdd3e0b74) [#40289](https://github.com/vllm-project/vllm/pull/40289) — [ROCm][ViT] Detect Triton-AMD kernels at their new aiter location (#40289)
- **2026-07-31** [`963a658674`](https://github.com/vllm-project/vllm/commit/963a658674) [#50307](https://github.com/vllm-project/vllm/pull/50307) — Bump Helion to 1.4.0 (#50307)
- **2026-07-31** [`e67a2e0a56`](https://github.com/vllm-project/vllm/commit/e67a2e0a56) [#48949](https://github.com/vllm-project/vllm/pull/48949) — [ROCm][Quark][7/N] Use MXFP4 linear kernel abstraction for `emulation` backend (#48949)
- **2026-07-31** [`8d8a4e0f2b`](https://github.com/vllm-project/vllm/commit/8d8a4e0f2b) [#50515](https://github.com/vllm-project/vllm/pull/50515) — [ROCm][CI] Restore Mistral tool-parser compatibility after unification (#50515)
- **2026-07-31** [`5233368dac`](https://github.com/vllm-project/vllm/commit/5233368dac) [#50516](https://github.com/vllm-project/vllm/pull/50516) — [ROCm][CI] Fall back to lossless Kimi K3 MXFP4 emulation on gfx942 (#50516)
- **2026-07-31** [`864a87febb`](https://github.com/vllm-project/vllm/commit/864a87febb) [#50109](https://github.com/vllm-project/vllm/pull/50109) — [Kernel][CI] `--jit-monitor-mode error` e2e tests for kernel warmup infra (#50109)
- **2026-07-31** [`92643d68f5`](https://github.com/vllm-project/vllm/commit/92643d68f5) [#50242](https://github.com/vllm-project/vllm/pull/50242) — K3 DSpark AR fusion (#50242)
- **2026-07-31** [`6e311c6e20`](https://github.com/vllm-project/vllm/commit/6e311c6e20) [#44941](https://github.com/vllm-project/vllm/pull/44941) — [MoE Refactor] Rename FusedMoE to FusedMoEFactory (#44941)
- **2026-07-31** [`c911120a6f`](https://github.com/vllm-project/vllm/commit/c911120a6f) [#50517](https://github.com/vllm-project/vllm/pull/50517) — [ROCm][CI] Update Transformers AR+RMS fusion expectation (#50517)
- **2026-07-31** [`5d7647a109`](https://github.com/vllm-project/vllm/commit/5d7647a109) [#50530](https://github.com/vllm-project/vllm/pull/50530) — [UT] add skipif for rocm aiter sampler UT (#50530)
- **2026-07-31** [`2773ec31b3`](https://github.com/vllm-project/vllm/commit/2773ec31b3) [#49309](https://github.com/vllm-project/vllm/pull/49309) — [ROCm][CI] Use explicit wvSplitKrc skinny-GEMM test tolerance for bf16 (gfx950) (#49309)
- **2026-07-31** [`6724051c57`](https://github.com/vllm-project/vllm/commit/6724051c57) [#50328](https://github.com/vllm-project/vllm/pull/50328) — [CI/Build][AMD] Install triton_kernels via CMake (#50328)
- **2026-07-31** [`4689c7dd61`](https://github.com/vllm-project/vllm/commit/4689c7dd61) [#50006](https://github.com/vllm-project/vllm/pull/50006) — [ROCm] Add tuned selective_state_update float16 config for AMD Instinct MI325X (#50006)
- **2026-07-31** [`5d5f22ed7a`](https://github.com/vllm-project/vllm/commit/5d5f22ed7a) [#50450](https://github.com/vllm-project/vllm/pull/50450) — [ROCm][CI] Use larger atol value for INT3 in test_quick_all_reduce.py (#50450)
- **2026-07-31** [`d91f7af7d0`](https://github.com/vllm-project/vllm/commit/d91f7af7d0) [#50467](https://github.com/vllm-project/vllm/pull/50467) — [Hardware][AMD][Kernel][CI][Bugfix] Fix ROCm DeepEP FP8 max (#50467)
- **2026-07-31** [`f1899b2ffd`](https://github.com/vllm-project/vllm/commit/f1899b2ffd) [#45227](https://github.com/vllm-project/vllm/pull/45227) — [Bugfix][ROCm] AITER MLA: size MTP verification decode metadata for real qlen/dtype (#45227)
- **2026-07-31** [`4f1da84eb5`](https://github.com/vllm-project/vllm/commit/4f1da84eb5) [#46516](https://github.com/vllm-project/vllm/pull/46516) — Enable gfx1250 ROCm architecture (#46516)
- **2026-07-31** [`3333d7cb63`](https://github.com/vllm-project/vllm/commit/3333d7cb63) [#49361](https://github.com/vllm-project/vllm/pull/49361) — [ROCm]: bump AITER to 0.1.19 (#49361)
- **2026-07-30** [`3f90c7e9e6`](https://github.com/vllm-project/vllm/commit/3f90c7e9e6) [#50378](https://github.com/vllm-project/vllm/pull/50378) — [ROCm] Pass pointers to FlyDSL MoE kernels (#50378)
- **2026-07-30** [`12a34a6bc7`](https://github.com/vllm-project/vllm/commit/12a34a6bc7) [#46720](https://github.com/vllm-project/vllm/pull/46720) — [ROCm][DSV4] B-preshuffle the attention fp8 projections (#46720)
- **2026-07-30** [`904fae8be1`](https://github.com/vllm-project/vllm/commit/904fae8be1) [#50312](https://github.com/vllm-project/vllm/pull/50312) — [DSv4 Perf] Fix redundant memory allocation and copy for dsv4 pp buffer, 448 MiB GPU memory saved (#50312)
- **2026-07-30** [`59e831c09a`](https://github.com/vllm-project/vllm/commit/59e831c09a) [#48757](https://github.com/vllm-project/vllm/pull/48757) — [Compilation]Fuse Transformers Residual Add + RMSNorm (#48757)
- **2026-07-30** [`1a20d23dab`](https://github.com/vllm-project/vllm/commit/1a20d23dab) [#48947](https://github.com/vllm-project/vllm/pull/48947) — [PARSER][Mistral] unified engine-based parser for reasoning and tool calls (#48947)
- **2026-07-30** [`e2efe79695`](https://github.com/vllm-project/vllm/commit/e2efe79695) [#47207](https://github.com/vllm-project/vllm/pull/47207) — [ROCm]Migrating Deepseek V3.2 to vllm/models/deepseek_v32/ (#47207)
- **2026-07-30** [`aeeb36b1f1`](https://github.com/vllm-project/vllm/commit/aeeb36b1f1) [#50000](https://github.com/vllm-project/vllm/pull/50000) — [New model] Kimi K3 (#50000)
- **2026-07-30** [`0c64be8873`](https://github.com/vllm-project/vllm/commit/0c64be8873) [#49839](https://github.com/vllm-project/vllm/pull/49839) — [Test][ROCm] Account for gfx950 FP8 RMSNorm rounding (#49839)
- **2026-07-30** [`165ed33327`](https://github.com/vllm-project/vllm/commit/165ed33327) [#50340](https://github.com/vllm-project/vllm/pull/50340) — [CI][ROCm] Stabilize LLM GC teardown check (#50340)
- **2026-07-30** [`f1e8fd27ae`](https://github.com/vllm-project/vllm/commit/f1e8fd27ae) [#49937](https://github.com/vllm-project/vllm/pull/49937) — [ROCm] Add AITER FP8 ViT encoder attention (#49937)
- **2026-07-30** [`b88916617d`](https://github.com/vllm-project/vllm/commit/b88916617d) [#48257](https://github.com/vllm-project/vllm/pull/48257) — [ROCm] [CI] Support cached K/V (key/value=None) in Triton prefix-prefill (#48257)
- **2026-07-29** [`fa2a2589bd`](https://github.com/vllm-project/vllm/commit/fa2a2589bd) [#50304](https://github.com/vllm-project/vllm/pull/50304) — [CI][ROCm] Fix AMD nightly distributed regressions (#50304)
- **2026-07-29** [`435c4dad97`](https://github.com/vllm-project/vllm/commit/435c4dad97) [#50311](https://github.com/vllm-project/vllm/pull/50311) — [ROCm][CI] Avoid Ray worker startup env race (#50311)
- **2026-07-29** [`381b691620`](https://github.com/vllm-project/vllm/commit/381b691620) [#50262](https://github.com/vllm-project/vllm/pull/50262) — [ROCm][CI] Fix Kimi K3 KDA on ROCm (#50262)
- **2026-07-29** [`5b14019576`](https://github.com/vllm-project/vllm/commit/5b14019576) [#50222](https://github.com/vllm-project/vllm/pull/50222) — [CI] Fix MXFP8 MOE backend selection tests on gfx942 (#50222)
- **2026-07-29** [`6370e53f24`](https://github.com/vllm-project/vllm/commit/6370e53f24) [#48145](https://github.com/vllm-project/vllm/pull/48145) — [Frontend] Reuse prefill token ids on the decode chat path for disaggregated serving (#48145)
- **2026-07-29** [`0bb548b60e`](https://github.com/vllm-project/vllm/commit/0bb548b60e) [#50161](https://github.com/vllm-project/vllm/pull/50161) — [CI][ROCm] Stabilize Qwen2-VL LoRA test (#50161)
- **2026-07-29** [`7398a30d79`](https://github.com/vllm-project/vllm/commit/7398a30d79) [#50190](https://github.com/vllm-project/vllm/pull/50190) — [ROCm][CI] Stabilize ngram and suffix correctness test (#50190)
- **2026-07-28** [`176256b962`](https://github.com/vllm-project/vllm/commit/176256b962) [#50163](https://github.com/vllm-project/vllm/pull/50163) — [ROCm][CI] Stabilize ROCm audio streaming test (#50163)
- **2026-07-28** [`5369f7b7b8`](https://github.com/vllm-project/vllm/commit/5369f7b7b8) [#49747](https://github.com/vllm-project/vllm/pull/49747) — [MXFP8][ROCm] Fix MXFP8 MoE backend selection (#49747)
- **2026-07-28** [`6c7e679f04`](https://github.com/vllm-project/vllm/commit/6c7e679f04) [#49714](https://github.com/vllm-project/vllm/pull/49714) — [ROCm][Bugfix] Sanitize AITER paged-MQA logits before sparse top-k for DeepSeek-V4 (#49714)
- **2026-07-28** [`05a0814863`](https://github.com/vllm-project/vllm/commit/05a0814863) [#49906](https://github.com/vllm-project/vllm/pull/49906) — [ROCm] Fix and optimize GPT-J-style MRoPE (#49906)
- **2026-07-28** [`4f56321d7e`](https://github.com/vllm-project/vllm/commit/4f56321d7e) [#47773](https://github.com/vllm-project/vllm/pull/47773) — [ROCm] Cache fp32 upcast of static e8m0 weight scale in AITER scaled_mm (#47773)
- **2026-07-28** [`62d8db7c05`](https://github.com/vllm-project/vllm/commit/62d8db7c05) [#50131](https://github.com/vllm-project/vllm/pull/50131) — [Bugfix] Add missing `vllm/models/kimi_k3/__init__.py` (#50131)
- **2026-07-28** [`88402a41c4`](https://github.com/vllm-project/vllm/commit/88402a41c4) [#49945](https://github.com/vllm-project/vllm/pull/49945) — [Test] Skip ROCm AITER MLA prefill tests on non-ROCm platforms (#49945)
- **2026-07-28** [`61ac368021`](https://github.com/vllm-project/vllm/commit/61ac368021) [#50090](https://github.com/vllm-project/vllm/pull/50090) — [Kimi-K3] Add AttnRes kernels (#50090)
- **2026-07-28** [`99b57a4823`](https://github.com/vllm-project/vllm/commit/99b57a4823) [#50086](https://github.com/vllm-project/vllm/pull/50086) — [CI][ROCm] Soft fail LoRA mirror (#50086)
- **2026-07-28** [`f472ab0a4c`](https://github.com/vllm-project/vllm/commit/f472ab0a4c) [#49621](https://github.com/vllm-project/vllm/pull/49621) — Remove triton per group quant [ROCm] [Bugfix] (#49621)
- **2026-07-28** [`33fe71a4d3`](https://github.com/vllm-project/vllm/commit/33fe71a4d3) [#46491](https://github.com/vllm-project/vllm/pull/46491) — [AMD] Revert `Mxfp4MoeBackend.TRITON_UNFUSED` fallback (#46491)
- **2026-07-28** [`7aea73d83d`](https://github.com/vllm-project/vllm/commit/7aea73d83d) [#49348](https://github.com/vllm-project/vllm/pull/49348) — [ROCm][Quark][6/N] Use MXFP4 linear kernel abstraction for `aiter` backend (#49348)
- **2026-07-28** [`e68bfc2828`](https://github.com/vllm-project/vllm/commit/e68bfc2828) [#50041](https://github.com/vllm-project/vllm/pull/50041) — [CI][ROCm] Soft-fail Python-only installation mirror (#50041)
- **2026-07-28** [`02b6ecf07c`](https://github.com/vllm-project/vllm/commit/02b6ecf07c) [#44527](https://github.com/vllm-project/vllm/pull/44527) — [ROCm][DSv3.2] Eliminate per-decode FillFunctor launches in sparse-MLA hot loop (#44527)
- **2026-07-28** [`1206891822`](https://github.com/vllm-project/vllm/commit/1206891822) [#47764](https://github.com/vllm-project/vllm/pull/47764) — [ROCm][KVConnector][MoRI-IO] Fix WRITE-mode remote-TP rank collapse (#46332 follow-up) (#47764)
- **2026-07-27** [`28158b2fc3`](https://github.com/vllm-project/vllm/commit/28158b2fc3) [#48886](https://github.com/vllm-project/vllm/pull/48886) — [ROCm] [BugFix] Fix Quark GLM-5.2 Checkpoint inference: indexer wk per-channel FP8 dequant + missing sparse-MLA metadata fields (#48886)
- **2026-07-27** [`53f6dd5c6f`](https://github.com/vllm-project/vllm/commit/53f6dd5c6f) [#49690](https://github.com/vllm-project/vllm/pull/49690) — [CI][ROCm] Fix `test_ocp_mx_wikitext_correctness` reference value (#49690)
- **2026-07-27** [`1053e248f0`](https://github.com/vllm-project/vllm/commit/1053e248f0) [#46765](https://github.com/vllm-project/vllm/pull/46765) — [ROCm][Quantization][5/N] Refactor quark_moe w8a8-int8 w/ oracle (#46765)
- **2026-07-27** [`b5bcb3ce88`](https://github.com/vllm-project/vllm/commit/b5bcb3ce88) [#49745](https://github.com/vllm-project/vllm/pull/49745) — [Refactor] Remove dead code in multiple files (#49745)
- **2026-07-27** [`30fbd05537`](https://github.com/vllm-project/vllm/commit/30fbd05537) [#49909](https://github.com/vllm-project/vllm/pull/49909) — [ROCm] Use backend-default dot precision for ReplaySSM (#49909)
- **2026-07-27** [`0906123953`](https://github.com/vllm-project/vllm/commit/0906123953) [#48841](https://github.com/vllm-project/vllm/pull/48841) — [ROCm] [Model] Enable TML inkling (#48841)
- **2026-07-27** [`bc3629b1c4`](https://github.com/vllm-project/vllm/commit/bc3629b1c4) [#49732](https://github.com/vllm-project/vllm/pull/49732) — [ROCm][CI] Skip three torchao tests of gfx950 until `torchao==0.18` is released (#49732)
- **2026-07-27** [`312ea82e75`](https://github.com/vllm-project/vllm/commit/312ea82e75) [#49837](https://github.com/vllm-project/vllm/pull/49837) — [CI][ROCm] Make hf-xet reconstruction safe on shared NFS (#49837)
- **2026-07-27** [`394beb633b`](https://github.com/vllm-project/vllm/commit/394beb633b) [#49843](https://github.com/vllm-project/vllm/pull/49843) — [Bugfix][ROCm] Use batch DMA for CPU KV cache loads (#49843)
- **2026-07-27** [`7f599d7854`](https://github.com/vllm-project/vllm/commit/7f599d7854) [#46913](https://github.com/vllm-project/vllm/pull/46913) — [communication] [bugfix] fix quickreduce acc error in cudagraph mode (#46913)
- **2026-07-27** [`e09900436c`](https://github.com/vllm-project/vllm/commit/e09900436c) [#49915](https://github.com/vllm-project/vllm/pull/49915) — [CI][ROCm] Reduce kernel test runtime (#49915)
- **2026-07-27** [`49f31d7cee`](https://github.com/vllm-project/vllm/commit/49f31d7cee) [#49913](https://github.com/vllm-project/vllm/pull/49913) — [ROCm] Make vllm_c RMSNorm output contiguous (#49913)
- **2026-07-27** [`da99ffcc13`](https://github.com/vllm-project/vllm/commit/da99ffcc13) [#49516](https://github.com/vllm-project/vllm/pull/49516) — [ROCm][CI] Keep native datasets cache off shared NFS (#49516)
- **2026-07-27** [`854c33f380`](https://github.com/vllm-project/vllm/commit/854c33f380) [#49911](https://github.com/vllm-project/vllm/pull/49911) — [CI][ROCm] Keep global GPU memory cleanup opt-in (#49911)
- **2026-07-27** [`ac87549cbd`](https://github.com/vllm-project/vllm/commit/ac87549cbd) [#49916](https://github.com/vllm-project/vllm/pull/49916) — [CI][ROCm] Reduce V1 attention test runtime (#49916)
- **2026-07-27** [`ffc4f08c8e`](https://github.com/vllm-project/vllm/commit/ffc4f08c8e) [#46116](https://github.com/vllm-project/vllm/pull/46116) — [Core][KV-transfer] MoRIIO: heterogeneous TP<->DP prefill/decode read routing (#46116)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#50856](https://github.com/vllm-project/vllm/issues/50856) | [Doc]: recipe for MiniMax-M3- crushes on 8xH200 | documentation | 2026-08-03 |
| [#44335](https://github.com/vllm-project/vllm/issues/44335) | [Installation]: libcudart.so.13 required when torch-backend=cu129 on v | installation | 2026-08-03 |
| [#50850](https://github.com/vllm-project/vllm/issues/50850) | [Bug]: Qwen/Qwen3.6-35B-A3B and Qwen/Qwen3.6-35B-A3B-FP8 issue while i | bug, intel-gpu | 2026-08-03 |
| [#43226](https://github.com/vllm-project/vllm/issues/43226) | [Bug]: EngineCore crash — assert req_id in self.requests in _update_fr | — | 2026-08-03 |
| [#47761](https://github.com/vllm-project/vllm/issues/47761) | [Bug]: vllm 0.23.0 and 0.24.0 - Qwen3.6-35B-A3B-FP8 - Fails generating | bug | 2026-08-03 |
| [#50269](https://github.com/vllm-project/vllm/issues/50269) | [Bug]: Host memory is not reducing after the model is loaded into Inte | bug, intel-gpu, quantization | 2026-08-03 |
| [#50720](https://github.com/vllm-project/vllm/issues/50720) | [Bug]: DeepSeek-V4-Flash-0731 + DSpark fails on RTX PRO 6000 (SM120) w | bug | 2026-08-03 |
| [#41469](https://github.com/vllm-project/vllm/issues/41469) | [Bug]: AttributeError: '_C' object has no attribute 'awq_dequantize' o | bug, intel-gpu | 2026-08-03 |
| [#50834](https://github.com/vllm-project/vllm/issues/50834) | [RFC]:  Unify the Tensor Type for Device-Pointer Storage to `torch.uin | RFC | 2026-08-03 |
| [#50837](https://github.com/vllm-project/vllm/issues/50837) | [Bug]: Qwen3.5 DFlash speculative decoding produces repetitive/degener | bug | 2026-08-03 |
| [#50835](https://github.com/vllm-project/vllm/issues/50835) | [Bug]: Generation Hang after a while when using RayExecutorV2 cross tw | bug | 2026-08-03 |
| [#34303](https://github.com/vllm-project/vllm/issues/34303) | [RFC]: CUDA Checkpoint/Restore for Near-Zero Cold Starts | RFC | 2026-08-03 |
| [#50706](https://github.com/vllm-project/vllm/issues/50706) | [Bug]: Mistral3 (HF format): default text-only LLM() init fails in mul | — | 2026-08-03 |
| [#50682](https://github.com/vllm-project/vllm/issues/50682) | [ROCm][AMD] Kimi-K3 Gap and Roadmap Tracking | rocm, kimi, k3 | 2026-08-03 |
| [#45709](https://github.com/vllm-project/vllm/issues/45709) | [Performance]: TTFT of graph mode is about 25% worse than that of eage | performance | 2026-08-03 |
| [#49674](https://github.com/vllm-project/vllm/issues/49674) | [Bug]: Deferred KV block frees cause zero-progress preemption cascades | bug | 2026-08-03 |
| [#50576](https://github.com/vllm-project/vllm/issues/50576) | [Feature]: SM8x (Ampere A100/A800) support for DeepSeek-V4-Flash / Dee | — | 2026-08-03 |
| [#50792](https://github.com/vllm-project/vllm/issues/50792) | [Bug]: OverflowError crash in `prompt_logprobs` decode path on PD-disa | bug | 2026-08-03 |
| [#50780](https://github.com/vllm-project/vllm/issues/50780) | [Bug]: CUDA graph memory profiler charges an mnbt-linear profiling tra | — | 2026-08-02 |
| [#50767](https://github.com/vllm-project/vllm/issues/50767) | [Bug]: override-generation-config silently ignores presence_penalty /  | bug | 2026-08-02 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 73 |
| Other | 32 |
| MoE / Expert Parallel | 32 |
| Attention | 30 |
| CI / Build | 25 |
| Multimodal | 23 |
| Disaggregation / PD | 21 |
| Quantization | 20 |
| Models | 16 |
| Serving / API | 14 |
| Scheduler / Engine | 13 |
| KV Cache / Offload | 8 |
| Perf / Benchmark | 6 |
| Speculative Decoding | 6 |
| Docs | 6 |
| Compilation / CUDA Graph | 2 |
| LoRA | 2 |

## ROCm / AMD  (73 commits)

- **2026-08-02** [`0055b8bfa3`](https://github.com/vllm-project/vllm/commit/0055b8bfa3) [#50032](https://github.com/vllm-project/vllm/pull/50032)
  [Attention][MiniMax-M3] Add MSA speculative decode verification (#50032)
  _Files: `.buildkite/test_areas/kernels.yaml`, `cmake/external_projects/fmha_sm100.cmake`, `csrc/libtorch_stable/fused_minimax_m3_qknorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h` _+11 more__
- **2026-08-02** [`c666810676`](https://github.com/vllm-project/vllm/commit/c666810676) [#50761](https://github.com/vllm-project/vllm/pull/50761)
  [ROCm][Bugfix][Kimi-K3] Preserve MoE correction bias in FP32 (#50761)
  _Files: `vllm/models/kimi_k3/amd/linear.py`_
- **2026-08-01** [`127a7cebc9`](https://github.com/vllm-project/vllm/commit/127a7cebc9) [#50608](https://github.com/vllm-project/vllm/pull/50608)
  Add @hongxiayang as code owner for AMD-specific model files and ROCm docs (#50608)
  _Files: `.github/CODEOWNERS`_
- **2026-08-01** [`77469c9057`](https://github.com/vllm-project/vllm/commit/77469c9057) [#50476](https://github.com/vllm-project/vllm/pull/50476)
  [ROCm][MLA] Mask the AITER MLA small-head verify flatten causally (#50476)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_causal_verify_mask.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-08-01** [`9c110fa522`](https://github.com/vllm-project/vllm/commit/9c110fa522) [#47189](https://github.com/vllm-project/vllm/pull/47189)
  [Frontend] Cohere chat v2 api support (#47189)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/rocm.in` _+27 more__
- **2026-08-01** [`f7097a92fd`](https://github.com/vllm-project/vllm/commit/f7097a92fd) [#50639](https://github.com/vllm-project/vllm/pull/50639)
  [Bugfix][CI] Prevent common ops imports from initializing CUDA (#50639)
  _Files: `vllm/models/common/ops/__init__.py`, `vllm/models/deepseek_v32/amd/model.py`, `vllm/models/deepseek_v32/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/dspark_mla.py`_
- **2026-08-01** [`fcdc7c2e9c`](https://github.com/vllm-project/vllm/commit/fcdc7c2e9c) [#50330](https://github.com/vllm-project/vllm/pull/50330)
  [CI] Organize speculative decoding E2E tests by coverage (#50330)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/model_runner_v2_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml` _+35 more__
- **2026-07-31** [`4fdd3e0b74`](https://github.com/vllm-project/vllm/commit/4fdd3e0b74) [#40289](https://github.com/vllm-project/vllm/pull/40289)
  [ROCm][ViT] Detect Triton-AMD kernels at their new aiter location (#40289)
  _Files: `vllm/platforms/rocm.py`_
- **2026-07-31** [`963a658674`](https://github.com/vllm-project/vllm/commit/963a658674) [#50307](https://github.com/vllm-project/vllm/pull/50307)
  Bump Helion to 1.4.0 (#50307)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `setup.py`_
- **2026-07-31** [`e67a2e0a56`](https://github.com/vllm-project/vllm/commit/e67a2e0a56) [#48949](https://github.com/vllm-project/vllm/pull/48949)
  [ROCm][Quark][7/N] Use MXFP4 linear kernel abstraction for `emulation` backend (#48949)
  _Files: `csrc/core/scalar_type.hpp`, `tests/kernels/quantization/test_mxfp4_kernel_selection.py`, `tests/kernels/quantization/test_mxfp6_kernel_selection.py`, `vllm/model_executor/kernels/linear/__init__.py` _+13 more__
- **2026-07-31** [`8d8a4e0f2b`](https://github.com/vllm-project/vllm/commit/8d8a4e0f2b) [#50515](https://github.com/vllm-project/vllm/pull/50515)
  [ROCm][CI] Restore Mistral tool-parser compatibility after unification (#50515)
  _Files: `vllm/parser/mistral.py`, `vllm/tool_parsers/mistral_tool_parser.py`_
- **2026-07-31** [`5233368dac`](https://github.com/vllm-project/vllm/commit/5233368dac) [#50516](https://github.com/vllm-project/vllm/pull/50516)
  [ROCm][CI] Fall back to lossless Kimi K3 MXFP4 emulation on gfx942 (#50516)
  _Files: `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-07-31** [`864a87febb`](https://github.com/vllm-project/vllm/commit/864a87febb) [#50109](https://github.com/vllm-project/vllm/pull/50109)
  [Kernel][CI] `--jit-monitor-mode error` e2e tests for kernel warmup infra (#50109)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/jit_monitor.yaml` _+6 more__
- **2026-07-31** [`92643d68f5`](https://github.com/vllm-project/vllm/commit/92643d68f5) [#50242](https://github.com/vllm-project/vllm/pull/50242)
  K3 DSpark AR fusion (#50242)
  _Files: `vllm/models/common/ops/__init__.py`, `vllm/models/common/ops/fused_allreduce_rms_norm.py`, `vllm/models/deepseek_v32/amd/model.py`, `vllm/models/deepseek_v32/nvidia/model.py` _+1 more__
- **2026-07-31** [`6e311c6e20`](https://github.com/vllm-project/vllm/commit/6e311c6e20) [#44941](https://github.com/vllm-project/vllm/pull/44941)
  [MoE Refactor] Rename FusedMoE to FusedMoEFactory (#44941)
  _Files: `tests/distributed/test_eplb_fused_moe_layer.py`, `tests/distributed/test_eplb_fused_moe_layer_dep_nvfp4.py`, `tests/kernels/moe/test_deepep_v2_moe.py`, `tests/kernels/moe/test_moe_layer.py` _+76 more__
- **2026-07-31** [`c911120a6f`](https://github.com/vllm-project/vllm/commit/c911120a6f) [#50517](https://github.com/vllm-project/vllm/pull/50517)
  [ROCm][CI] Update Transformers AR+RMS fusion expectation (#50517)
  _Files: `tests/compile/fusions_e2e/test_tp2_ar_rms.py`_
- **2026-07-31** [`5d7647a109`](https://github.com/vllm-project/vllm/commit/5d7647a109) [#50530](https://github.com/vllm-project/vllm/pull/50530)
  [UT] add skipif for rocm aiter sampler UT (#50530)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`_
- **2026-07-31** [`2773ec31b3`](https://github.com/vllm-project/vllm/commit/2773ec31b3) [#49309](https://github.com/vllm-project/vllm/pull/49309)
  [ROCm][CI] Use explicit wvSplitKrc skinny-GEMM test tolerance for bf16 (gfx950) (#49309)
  _Files: `tests/kernels/quantization/test_rocm_skinny_gemms.py`_
- **2026-07-31** [`6724051c57`](https://github.com/vllm-project/vllm/commit/6724051c57) [#50328](https://github.com/vllm-project/vllm/pull/50328)
  [CI/Build][AMD] Install triton_kernels via CMake (#50328)
  _Files: `cmake/external_projects/triton_kernels.cmake`, `docker/Dockerfile.rocm_base`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-07-31** [`4689c7dd61`](https://github.com/vllm-project/vllm/commit/4689c7dd61) [#50006](https://github.com/vllm-project/vllm/pull/50006)
  [ROCm] Add tuned selective_state_update float16 config for AMD Instinct MI325X (#50006)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI325X,cache_dtype=float16.json`_
- **2026-07-31** [`5d5f22ed7a`](https://github.com/vllm-project/vllm/commit/5d5f22ed7a) [#50450](https://github.com/vllm-project/vllm/pull/50450)
  [ROCm][CI] Use larger atol value for INT3 in test_quick_all_reduce.py (#50450)
  _Files: `tests/distributed/test_quick_all_reduce.py`_
- **2026-07-31** [`d91f7af7d0`](https://github.com/vllm-project/vllm/commit/d91f7af7d0) [#50467](https://github.com/vllm-project/vllm/pull/50467)
  [Hardware][AMD][Kernel][CI][Bugfix] Fix ROCm DeepEP FP8 max (#50467)
  _Files: `docker/Dockerfile.rocm`, `tests/kernels/moe/test_deepep_moe.py`_
- **2026-07-31** [`f1899b2ffd`](https://github.com/vllm-project/vllm/commit/f1899b2ffd) [#45227](https://github.com/vllm-project/vllm/pull/45227)
  [Bugfix][ROCm] AITER MLA: size MTP verification decode metadata for real qlen/dtype (#45227)
  _Files: `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-07-31** [`4f1da84eb5`](https://github.com/vllm-project/vllm/commit/4f1da84eb5) [#46516](https://github.com/vllm-project/vllm/pull/46516)
  Enable gfx1250 ROCm architecture (#46516)
  _Files: `CMakeLists.txt`, `csrc/quickreduce/base.h`, `csrc/rocm/attention.cu`, `csrc/rocm/torch_bindings.cpp` _+29 more__
- **2026-07-31** [`3333d7cb63`](https://github.com/vllm-project/vllm/commit/3333d7cb63) [#49361](https://github.com/vllm-project/vllm/pull/49361)
  [ROCm]: bump AITER to 0.1.19 (#49361)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-07-30** [`3f90c7e9e6`](https://github.com/vllm-project/vllm/commit/3f90c7e9e6) [#50378](https://github.com/vllm-project/vllm/pull/50378)
  [ROCm] Pass pointers to FlyDSL MoE kernels (#50378)
  _Files: `vllm/model_executor/layers/fused_moe/fused_flydsl_moe.py`_
- **2026-07-30** [`12a34a6bc7`](https://github.com/vllm-project/vllm/commit/12a34a6bc7) [#46720](https://github.com/vllm-project/vllm/pull/46720)
  [ROCm][DSV4] B-preshuffle the attention fp8 projections (#46720)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py` _+1 more__
- **2026-07-30** [`904fae8be1`](https://github.com/vllm-project/vllm/commit/904fae8be1) [#50312](https://github.com/vllm-project/vllm/pull/50312)
  [DSv4 Perf] Fix redundant memory allocation and copy for dsv4 pp buffer, 448 MiB GPU memory saved (#50312)
  _Files: `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/xpu/model.py`_
- **2026-07-30** [`59e831c09a`](https://github.com/vllm-project/vllm/commit/59e831c09a) [#48757](https://github.com/vllm-project/vllm/pull/48757)
  [Compilation]Fuse Transformers Residual Add + RMSNorm (#48757)
  _Files: `tests/compile/passes/test_rmsnorm_reshape_fusion.py`, `vllm/compilation/passes/fusion/add_rms_fusion.py`, `vllm/compilation/passes/pass_manager.py`, `vllm/kernels/aiter_ops.py`_
- **2026-07-30** [`1a20d23dab`](https://github.com/vllm-project/vllm/commit/1a20d23dab) [#48947](https://github.com/vllm-project/vllm/pull/48947)
  [PARSER][Mistral] unified engine-based parser for reasoning and tool calls (#48947)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt` _+26 more__
- **2026-07-30** [`e2efe79695`](https://github.com/vllm-project/vllm/commit/e2efe79695) [#47207](https://github.com/vllm-project/vllm/pull/47207)
  [ROCm]Migrating Deepseek V3.2 to vllm/models/deepseek_v32/ (#47207)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/__init__.py`, `vllm/models/deepseek_v32/amd/__init__.py`, `vllm/models/deepseek_v32/amd/model.py` _+8 more__
- **2026-07-30** [`aeeb36b1f1`](https://github.com/vllm-project/vllm/commit/aeeb36b1f1) [#50000](https://github.com/vllm-project/vllm/pull/50000)
  [New model] Kimi K3 (#50000)
  _Files: `cmake/external_projects/deepgemm.cmake`, `docs/models/supported_models.md`, `pyproject.toml`, `requirements/cuda.txt` _+78 more__
- **2026-07-30** [`0c64be8873`](https://github.com/vllm-project/vllm/commit/0c64be8873) [#49839](https://github.com/vllm-project/vllm/pull/49839)
  [Test][ROCm] Account for gfx950 FP8 RMSNorm rounding (#49839)
  _Files: `tests/kernels/core/test_fused_quant_layernorm.py`, `tests/kernels/core/test_layernorm.py`_
- **2026-07-30** [`165ed33327`](https://github.com/vllm-project/vllm/commit/165ed33327) [#50340](https://github.com/vllm-project/vllm/pull/50340)
  [CI][ROCm] Stabilize LLM GC teardown check (#50340)
  _Files: `tests/basic_correctness/test_basic_correctness.py`_
- **2026-07-30** [`f1e8fd27ae`](https://github.com/vllm-project/vllm/commit/f1e8fd27ae) [#49937](https://github.com/vllm-project/vllm/pull/49937)
  [ROCm] Add AITER FP8 ViT encoder attention (#49937)
  _Files: `benchmarks/kernels/benchmark_vit_aiter_fp8_attn.py`, `docs/features/quantization/fp8_vit_attn.md`, `tests/kernels/attention/test_mha_attn.py`, `tests/kernels/core/test_vit_fp8_scaling.py` _+4 more__
- **2026-07-30** [`b88916617d`](https://github.com/vllm-project/vllm/commit/b88916617d) [#48257](https://github.com/vllm-project/vllm/pull/48257)
  [ROCm] [CI] Support cached K/V (key/value=None) in Triton prefix-prefill (#48257)
  _Files: `tests/kernels/attention/test_prefix_prefill.py`, `vllm/v1/attention/ops/prefix_prefill.py`_
- **2026-07-29** [`fa2a2589bd`](https://github.com/vllm-project/vllm/commit/fa2a2589bd) [#50304](https://github.com/vllm-project/vllm/pull/50304)
  [CI][ROCm] Fix AMD nightly distributed regressions (#50304)
  _Files: `tests/distributed/test_custom_all_reduce.py`, `tests/v1/shutdown/test_delete.py`_
- **2026-07-29** [`435c4dad97`](https://github.com/vllm-project/vllm/commit/435c4dad97) [#50311](https://github.com/vllm-project/vllm/pull/50311)
  [ROCm][CI] Avoid Ray worker startup env race (#50311)
  _Files: `requirements/test/rocm.in`, `requirements/test/rocm.txt`_
- **2026-07-29** [`381b691620`](https://github.com/vllm-project/vllm/commit/381b691620) [#50262](https://github.com/vllm-project/vllm/pull/50262)
  [ROCm][CI] Fix Kimi K3 KDA on ROCm (#50262)
  _Files: `.buildkite/test-amd.yaml`, `vllm/models/kimi_k3/nvidia/kda.py`_
- **2026-07-29** [`5b14019576`](https://github.com/vllm-project/vllm/commit/5b14019576) [#50222](https://github.com/vllm-project/vllm/pull/50222)
  [CI] Fix MXFP8 MOE backend selection tests on gfx942 (#50222)
  _Files: `tests/kernels/moe/test_mxfp8_aiter_backend_selection.py`_
- **2026-07-29** [`6370e53f24`](https://github.com/vllm-project/vllm/commit/6370e53f24) [#48145](https://github.com/vllm-project/vllm/pull/48145)
  [Frontend] Reuse prefill token ids on the decode chat path for disaggregated serving (#48145)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docs/features/disagg_prefill.md`, `tests/entrypoints/openai/chat_completion/test_chat_completion.py` _+2 more__
- **2026-07-29** [`0bb548b60e`](https://github.com/vllm-project/vllm/commit/0bb548b60e) [#50161](https://github.com/vllm-project/vllm/pull/50161)
  [CI][ROCm] Stabilize Qwen2-VL LoRA test (#50161)
  _Files: `.buildkite/test_areas/lora.yaml`, `tests/lora/test_qwenvl.py`_
- **2026-07-29** [`7398a30d79`](https://github.com/vllm-project/vllm/commit/7398a30d79) [#50190](https://github.com/vllm-project/vllm/pull/50190)
  [ROCm][CI] Stabilize ngram and suffix correctness test (#50190)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`_
- **2026-07-28** [`176256b962`](https://github.com/vllm-project/vllm/commit/176256b962) [#50163](https://github.com/vllm-project/vllm/pull/50163)
  [ROCm][CI] Stabilize ROCm audio streaming test (#50163)
  _Files: `tests/entrypoints/multimodal/openai/chat_completion/test_audio.py`_
- **2026-07-28** [`5369f7b7b8`](https://github.com/vllm-project/vllm/commit/5369f7b7b8) [#49747](https://github.com/vllm-project/vllm/pull/49747)
  [MXFP8][ROCm] Fix MXFP8 MoE backend selection (#49747)
  _Files: `tests/kernels/moe/test_mxfp8_aiter_backend_selection.py`, `tests/models/quantization/test_mxfp8.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`, `vllm/model_executor/layers/fused_moe/experts/mxfp8_emulation_moe.py` _+2 more__
- **2026-07-28** [`6c7e679f04`](https://github.com/vllm-project/vllm/commit/6c7e679f04) [#49714](https://github.com/vllm-project/vllm/pull/49714)
  [ROCm][Bugfix] Sanitize AITER paged-MQA logits before sparse top-k for DeepSeek-V4 (#49714)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-07-28** [`05a0814863`](https://github.com/vllm-project/vllm/commit/05a0814863) [#49906](https://github.com/vllm-project/vllm/pull/49906)
  [ROCm] Fix and optimize GPT-J-style MRoPE (#49906)
  _Files: `tests/kernels/core/test_mrope.py`, `vllm/model_executor/layers/rotary_embedding/mrope.py`_
- **2026-07-28** [`4f56321d7e`](https://github.com/vllm-project/vllm/commit/4f56321d7e) [#47773](https://github.com/vllm-project/vllm/pull/47773)
  [ROCm] Cache fp32 upcast of static e8m0 weight scale in AITER scaled_mm (#47773)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/aiter.py`_
- **2026-07-28** [`62d8db7c05`](https://github.com/vllm-project/vllm/commit/62d8db7c05) [#50131](https://github.com/vllm-project/vllm/pull/50131)
  [Bugfix] Add missing `vllm/models/kimi_k3/__init__.py` (#50131)
  _Files: `vllm/models/kimi_k3/__init__.py`, `vllm/models/kimi_k3/amd/ops/__init__.py`_
- **2026-07-28** [`88402a41c4`](https://github.com/vllm-project/vllm/commit/88402a41c4) [#49945](https://github.com/vllm-project/vllm/pull/49945)
  [Test] Skip ROCm AITER MLA prefill tests on non-ROCm platforms (#49945)
  _Files: `tests/v1/attention/test_mla_prefill_selector.py`_
- **2026-07-28** [`61ac368021`](https://github.com/vllm-project/vllm/commit/61ac368021) [#50090](https://github.com/vllm-project/vllm/pull/50090)
  [Kimi-K3] Add AttnRes kernels (#50090)
  _Files: `.buildkite/test_areas/models_basic.yaml`, `CMakeLists.txt`, `csrc/libtorch_stable/kimi_k3/attn_res_kernel.cu`, `csrc/libtorch_stable/ops.h` _+10 more__
- **2026-07-28** [`99b57a4823`](https://github.com/vllm-project/vllm/commit/99b57a4823) [#50086](https://github.com/vllm-project/vllm/pull/50086)
  [CI][ROCm] Soft fail LoRA mirror (#50086)
  _Files: `.buildkite/test_areas/lora.yaml`_
- **2026-07-28** [`f472ab0a4c`](https://github.com/vllm-project/vllm/commit/f472ab0a4c) [#49621](https://github.com/vllm-project/vllm/pull/49621)
  Remove triton per group quant [ROCm] [Bugfix] (#49621)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `tests/compile/passes/test_fusion.py`, `tests/compile/passes/test_silu_mul_quant_fusion.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py` _+2 more__
- **2026-07-28** [`33fe71a4d3`](https://github.com/vllm-project/vllm/commit/33fe71a4d3) [#46491](https://github.com/vllm-project/vllm/pull/46491)
  [AMD] Revert `Mxfp4MoeBackend.TRITON_UNFUSED` fallback (#46491)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/quantization/test_gfx950_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-07-28** [`7aea73d83d`](https://github.com/vllm-project/vllm/commit/7aea73d83d) [#49348](https://github.com/vllm-project/vllm/pull/49348)
  [ROCm][Quark][6/N] Use MXFP4 linear kernel abstraction for `aiter` backend (#49348)
  _Files: `tests/evals/gsm8k/configs/Qwen3-1.7B-MXFP4.yaml`, `tests/kernels/quantization/test_mxfp4_kernel_selection.py`, `tests/quantization/test_quark.py`, `vllm/model_executor/kernels/linear/__init__.py` _+2 more__
- **2026-07-28** [`e68bfc2828`](https://github.com/vllm-project/vllm/commit/e68bfc2828) [#50041](https://github.com/vllm-project/vllm/pull/50041)
  [CI][ROCm] Soft-fail Python-only installation mirror (#50041)
  _Files: `.buildkite/test_areas/misc.yaml`_
- **2026-07-28** [`02b6ecf07c`](https://github.com/vllm-project/vllm/commit/02b6ecf07c) [#44527](https://github.com/vllm-project/vllm/pull/44527)
  [ROCm][DSv3.2] Eliminate per-decode FillFunctor launches in sparse-MLA hot loop (#44527)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-07-28** [`1206891822`](https://github.com/vllm-project/vllm/commit/1206891822) [#47764](https://github.com/vllm-project/vllm/pull/47764)
  [ROCm][KVConnector][MoRI-IO] Fix WRITE-mode remote-TP rank collapse (#46332 follow-up) (#47764)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-07-27** [`28158b2fc3`](https://github.com/vllm-project/vllm/commit/28158b2fc3) [#48886](https://github.com/vllm-project/vllm/pull/48886)
  [ROCm] [BugFix] Fix Quark GLM-5.2 Checkpoint inference: indexer wk per-channel FP8 dequant + missing sparse-MLA metadata fields (#48886)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/v1/attention/backend.py` _+1 more__
- **2026-07-27** [`53f6dd5c6f`](https://github.com/vllm-project/vllm/commit/53f6dd5c6f) [#49690](https://github.com/vllm-project/vllm/pull/49690)
  [CI][ROCm] Fix `test_ocp_mx_wikitext_correctness` reference value (#49690)
  _Files: `tests/quantization/test_quark.py`_
- **2026-07-27** [`1053e248f0`](https://github.com/vllm-project/vllm/commit/1053e248f0) [#46765](https://github.com/vllm-project/vllm/pull/46765)
  [ROCm][Quantization][5/N] Refactor quark_moe w8a8-int8 w/ oracle (#46765)
  _Files: `tests/evals/gsm8k/configs/Qwen1.5-MoE-A2.7B-Chat-INT8.yaml`, `tests/evals/gsm8k/configs/models-mi3xx-fp8-and-mixed.txt`, `tests/quantization/test_int8_moe_oracle.py`, `tests/quantization/test_quark.py` _+4 more__
- **2026-07-27** [`b5bcb3ce88`](https://github.com/vllm-project/vllm/commit/b5bcb3ce88) [#49745](https://github.com/vllm-project/vllm/pull/49745)
  [Refactor] Remove dead code in multiple files (#49745)
  _Files: `vllm/model_executor/kernels/linear/cute_dsl/_ll_bf16_dotprod.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/nixl_ep.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+18 more__
- **2026-07-27** [`30fbd05537`](https://github.com/vllm-project/vllm/commit/30fbd05537) [#49909](https://github.com/vllm-project/vllm/pull/49909)
  [ROCm] Use backend-default dot precision for ReplaySSM (#49909)
  _Files: `.buildkite/test-amd.yaml`, `vllm/model_executor/layers/mamba/ops/selective_state_update_replayssm_output_only.py`_
- **2026-07-27** [`0906123953`](https://github.com/vllm-project/vllm/commit/0906123953) [#48841](https://github.com/vllm-project/vllm/pull/48841)
  [ROCm] [Model] Enable TML inkling (#48841)
  _Files: `benchmarks/kernels/benchmark_inkling_qkvr_prep.py`, `tests/models/inkling/rocm/conftest.py`, `tests/models/inkling/rocm/test_model_alignment.py`, `tests/models/inkling/rocm/test_mxfp4_load.py` _+29 more__
- **2026-07-27** [`bc3629b1c4`](https://github.com/vllm-project/vllm/commit/bc3629b1c4) [#49732](https://github.com/vllm-project/vllm/pull/49732)
  [ROCm][CI] Skip three torchao tests of gfx950 until `torchao==0.18` is released (#49732)
  _Files: `tests/quantization/test_torchao.py`_
- **2026-07-27** [`312ea82e75`](https://github.com/vllm-project/vllm/commit/312ea82e75) [#49837](https://github.com/vllm-project/vllm/pull/49837)
  [CI][ROCm] Make hf-xet reconstruction safe on shared NFS (#49837)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-27** [`394beb633b`](https://github.com/vllm-project/vllm/commit/394beb633b) [#49843](https://github.com/vllm-project/vllm/pull/49843)
  [Bugfix][ROCm] Use batch DMA for CPU KV cache loads (#49843)
  _Files: `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `vllm/v1/kv_offload/cpu/gpu_worker.py`_
- **2026-07-27** [`7f599d7854`](https://github.com/vllm-project/vllm/commit/7f599d7854) [#46913](https://github.com/vllm-project/vllm/pull/46913)
  [communication] [bugfix] fix quickreduce acc error in cudagraph mode (#46913)
  _Files: `csrc/quickreduce/quick_reduce.h`, `tests/distributed/test_rocm_quick_reduce.py`_
- **2026-07-27** [`e09900436c`](https://github.com/vllm-project/vllm/commit/e09900436c) [#49915](https://github.com/vllm-project/vllm/pull/49915)
  [CI][ROCm] Reduce kernel test runtime (#49915)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/core/test_fused_quant_layernorm.py`, `tests/kernels/core/test_vit_fp8_scaling.py`_
- **2026-07-27** [`49f31d7cee`](https://github.com/vllm-project/vllm/commit/49f31d7cee) [#49913](https://github.com/vllm-project/vllm/pull/49913)
  [ROCm] Make vllm_c RMSNorm output contiguous (#49913)
  _Files: `tests/kernels/ir/test_layernorm.py`, `vllm/kernels/vllm_c.py`_
- **2026-07-27** [`da99ffcc13`](https://github.com/vllm-project/vllm/commit/da99ffcc13) [#49516](https://github.com/vllm-project/vllm/pull/49516)
  [ROCm][CI] Keep native datasets cache off shared NFS (#49516)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-07-27** [`854c33f380`](https://github.com/vllm-project/vllm/commit/854c33f380) [#49911](https://github.com/vllm-project/vllm/pull/49911)
  [CI][ROCm] Keep global GPU memory cleanup opt-in (#49911)
  _Files: `tests/conftest.py`_
- **2026-07-27** [`ac87549cbd`](https://github.com/vllm-project/vllm/commit/ac87549cbd) [#49916](https://github.com/vllm-project/vllm/pull/49916)
  [CI][ROCm] Reduce V1 attention test runtime (#49916)
  _Files: `.buildkite/test-amd.yaml`, `tests/v1/attention/test_mla_backends.py`_

## Other  (32 commits)

- **2026-08-03** [`32c42c4f2f`](https://github.com/vllm-project/vllm/commit/32c42c4f2f) [#50750](https://github.com/vllm-project/vllm/pull/50750)
  [UX] remove torch compile warning when using breakable cudagraph (#50750)
  _Files: `vllm/config/vllm.py`_
- **2026-08-03** [`5e35a6f4f9`](https://github.com/vllm-project/vllm/commit/5e35a6f4f9) [#50547](https://github.com/vllm-project/vllm/pull/50547)
  cpu_model_runner.py: skip the warm up if CompilationMode.NONE (#50547)
  _Files: `vllm/v1/worker/cpu_model_runner.py`_
- **2026-08-02** [`0033211c0b`](https://github.com/vllm-project/vllm/commit/0033211c0b) [#44972](https://github.com/vllm-project/vllm/pull/44972)
  [Test][V1] Add sleep/wake correctness regression test for hybrid GDN/… (#44972)
  _Files: `csrc/cumem_allocator.cpp`, `tests/models/language/generation/test_gdn_sleep_wake.py`_
- **2026-08-02** [`55c98e370a`](https://github.com/vllm-project/vllm/commit/55c98e370a) [#50661](https://github.com/vllm-project/vllm/pull/50661)
  [Model Runner v2] Enable BGE M3 pooling embed token_classify (#50661)
  _Files: `tests/models/language/pooling/test_splade_sparse_pooler.py`, `vllm/v1/worker/gpu/pool/pooling_runner.py`_
- **2026-08-01** [`652ba59229`](https://github.com/vllm-project/vllm/commit/652ba59229) [#50574](https://github.com/vllm-project/vllm/pull/50574)
  [Model Runner V2] Enable encoder token embedding (#50574)
  _Files: `tests/models/language/pooling/test_colbert.py`, `tests/models/language/pooling/test_splade_sparse_pooler.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pool/pooling_runner.py`_
- **2026-08-01** [`6c91de3689`](https://github.com/vllm-project/vllm/commit/6c91de3689) [#50642](https://github.com/vllm-project/vllm/pull/50642)
  [Bugfix][Parser] Forward model_config to nested reasoning parsers (#50642)
  _Files: `vllm/parser/abstract_parser.py`_
- **2026-08-01** [`124154a884`](https://github.com/vllm-project/vllm/commit/124154a884) [#50655](https://github.com/vllm-project/vllm/pull/50655)
  Add @shen-shanshan to CODEOWNERS (#50655)
  _Files: `.github/CODEOWNERS`_
- **2026-07-31** [`9a7ae4b808`](https://github.com/vllm-project/vllm/commit/9a7ae4b808) [#49437](https://github.com/vllm-project/vllm/pull/49437)
  [chore] log process manager shutdown with more details (#49437)
  _Files: `vllm/v1/utils.py`_
- **2026-07-31** [`0f17394564`](https://github.com/vllm-project/vllm/commit/0f17394564) [#50293](https://github.com/vllm-project/vllm/pull/50293)
  [Model Runner V2] Enable encoder token classification (#50293)
  _Files: `tests/models/language/pooling/test_splade_sparse_pooler.py`, `tests/models/language/pooling/test_token_classification.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pool/pooling_runner.py`_
- **2026-07-31** [`ab98034d4c`](https://github.com/vllm-project/vllm/commit/ab98034d4c) [#50420](https://github.com/vllm-project/vllm/pull/50420)
  [Frontend][Bugfix] Use default tool call IDs for Kimi K3 for conversation-level uniqueness (#50420)
  _Files: `rust/src/chat/src/renderer/kimi_k3/encoding.rs`, `rust/src/chat/src/renderer/kimi_k3/tests.rs`, `rust/src/parser/src/unified/kimi_k3.rs`, `tests/tool_use/test_kimi_k3_tool_parser.py` _+1 more__
- **2026-07-31** [`d6938b7408`](https://github.com/vllm-project/vllm/commit/d6938b7408) [#50200](https://github.com/vllm-project/vllm/pull/50200)
  [Bugfix][Rust Frontend] Select earliest-completing stop string (#50200)
  _Files: `rust/src/text/src/output/decoded.rs`_
- **2026-07-30** [`e9096fcb12`](https://github.com/vllm-project/vllm/commit/e9096fcb12) [#50406](https://github.com/vllm-project/vllm/pull/50406)
  [Rust Frontend] Improve startup failure and readiness logs (#50406)
  _Files: `rust/src/cmd/src/main.rs`, `rust/src/server/src/lib.rs`_
- **2026-07-30** [`451227cb3f`](https://github.com/vllm-project/vllm/commit/451227cb3f) [#49660](https://github.com/vllm-project/vllm/pull/49660)
  [Bugfix][Kernel] Fix integer overflow in libtorch_stable/activation_kernels.cu (#49660)
  _Files: `csrc/libtorch_stable/activation_kernels.cu`_
- **2026-07-29** [`43eaefba5a`](https://github.com/vllm-project/vllm/commit/43eaefba5a) [#48791](https://github.com/vllm-project/vllm/pull/48791)
  [ModelRunner V2] Enable sequence pooling for embedding and classification models (#48791)
  _Files: `tests/models/language/pooling/test_all_pooling_plus_chunked_prefill.py`, `tests/models/language/pooling/test_classification.py`, `tests/models/language/pooling/test_embedding.py`, `tests/models/language/pooling/test_splade_sparse_pooler.py` _+6 more__
- **2026-07-29** [`72297d859b`](https://github.com/vllm-project/vllm/commit/72297d859b) [#47121](https://github.com/vllm-project/vllm/pull/47121)
  [XPU] Route weightless RMSNorm to _C dispatch (#47121)
  _Files: `vllm/kernels/xpu_ops.py`_
- **2026-07-29** [`f51193b9ae`](https://github.com/vllm-project/vllm/commit/f51193b9ae) [#49291](https://github.com/vllm-project/vllm/pull/49291)
  [Kernel][Mamba] Fused-kernel support for align-mode DS-conv state migration with num_accepted_tokens > 1 (#49291)
  _Files: `tests/kernels/mamba/test_precopy_mamba_align.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`, `vllm/v1/worker/gpu_model_runner.py` _+1 more__
- **2026-07-29** [`6f91edf96d`](https://github.com/vllm-project/vllm/commit/6f91edf96d) [#49974](https://github.com/vllm-project/vllm/pull/49974)
  [Test] dynamic_shapes_compilation (#49974)
  _Files: `tests/compile/test_dynamic_shapes_compilation.py`_
- **2026-07-29** [`6fbbcf2151`](https://github.com/vllm-project/vllm/commit/6fbbcf2151) [#49757](https://github.com/vllm-project/vllm/pull/49757)
  [BugFix] Stop dummy runs from writing mamba state through stale block-table rows (#49757)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/block_table.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/model_runner.py` _+1 more__
- **2026-07-29** [`56f31af62a`](https://github.com/vllm-project/vllm/commit/56f31af62a) [#41602](https://github.com/vllm-project/vllm/pull/41602)
  [Bugfix] Fix /wake_up crash on hybrid models (Mamba/DeltaNet) (#41602)
  _Files: `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-28** [`e7f6a39db8`](https://github.com/vllm-project/vllm/commit/e7f6a39db8) [#50110](https://github.com/vllm-project/vllm/pull/50110)
  [Test] Make EPD correctness tests configurable for XPU (#50110)
  _Files: `tests/v1/ec_connector/integration/run_epd_correctness_test.sh`, `tests/v1/ec_connector/integration/test_epd_correctness.py`_
- **2026-07-28** [`d552a68645`](https://github.com/vllm-project/vllm/commit/d552a68645) [#50129](https://github.com/vllm-project/vllm/pull/50129)
  [Rust Frontend] Extract shared tracing setup logic into `vllm-tracing` (#50129)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/bench/Cargo.toml`, `rust/src/bench/src/main.rs` _+4 more__
- **2026-07-28** [`118bcde449`](https://github.com/vllm-project/vllm/commit/118bcde449) [#45532](https://github.com/vllm-project/vllm/pull/45532)
  [BugFix] Fix clang spinloop mwaitx include (#45532)
  _Files: `csrc/spinloop.cpp`_
- **2026-07-28** [`d2bfc6fe20`](https://github.com/vllm-project/vllm/commit/d2bfc6fe20) [#50103](https://github.com/vllm-project/vllm/pull/50103)
  [Build] Fix DeepEP CUDA driver stub linking (#50103)
  _Files: `tools/ep_kernels/install_python_libraries.sh`_
- **2026-07-28** [`03a2d03367`](https://github.com/vllm-project/vllm/commit/03a2d03367) [#49966](https://github.com/vllm-project/vllm/pull/49966)
  [Bugfix] Respect cgroup memory limits on all platforms (#49966)
  _Files: `vllm/model_executor/model_loader/weight_utils.py`_
- **2026-07-28** [`d18ed2304a`](https://github.com/vllm-project/vllm/commit/d18ed2304a) [#49152](https://github.com/vllm-project/vllm/pull/49152)
  [KV-offload][FS] : Batch store/load_block in C  (#49152)
  _Files: `csrc/fs_io.cpp`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `vllm/v1/kv_offload/tiering/fs/io.py`, `vllm/v1/kv_offload/tiering/fs/manager.py`_
- **2026-07-28** [`60417b4b74`](https://github.com/vllm-project/vllm/commit/60417b4b74) [#50034](https://github.com/vllm-project/vllm/pull/50034)
  [Core][PCP] Select MRV2 when PCP is enabled (#50034)
  _Files: `vllm/config/vllm.py`_
- **2026-07-27** [`8112b6c997`](https://github.com/vllm-project/vllm/commit/8112b6c997) [#49364](https://github.com/vllm-project/vllm/pull/49364)
  [MRV2] Always build attn metadata at capture time (#49364) (#49995)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/cudagraph_utils.py`_
- **2026-07-27** [`3f47a8384d`](https://github.com/vllm-project/vllm/commit/3f47a8384d) [#49846](https://github.com/vllm-project/vllm/pull/49846)
  [Bugfix] Fix VLLM_ENFORCE_STRICT_TOOL_CALLING mutation in tests (#49846)
  _Files: `tests/parser/test_include_reasoning.py`, `tests/parser/test_parse.py`, `tests/parser/test_streaming.py`_
- **2026-07-27** [`d2ca3002d9`](https://github.com/vllm-project/vllm/commit/d2ca3002d9) [#47711](https://github.com/vllm-project/vllm/pull/47711)
  [MRV2][Performance] Skip no-op FP32 logits materialization (#47711)
  _Files: `vllm/v1/worker/gpu/sample/sampler.py`_
- **2026-07-27** [`cbc3a87200`](https://github.com/vllm-project/vllm/commit/cbc3a87200) [#49907](https://github.com/vllm-project/vllm/pull/49907)
  [Tokenizer] Use HF config for HF tokenizers (#49907)
  _Files: `vllm/tokenizers/registry.py`_
- **2026-07-27** [`74d3b799e1`](https://github.com/vllm-project/vllm/commit/74d3b799e1) [#49429](https://github.com/vllm-project/vllm/pull/49429)
  [Bugfix] Fix mHC block-M prenorm GEMM cross-row reduction carry-over (#49429)
  _Files: `vllm/model_executor/kernels/mhc/tilelang_kernels.py`_
- **2026-07-27** [`439f336212`](https://github.com/vllm-project/vllm/commit/439f336212) [#49736](https://github.com/vllm-project/vllm/pull/49736)
  [Core] Fix gpu<->cpu syncs in MRV2 mamba_hybrid.py (#49736)
  _Files: `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_

## MoE / Expert Parallel  (32 commits)

- **2026-08-03** [`c8602c7906`](https://github.com/vllm-project/vllm/commit/c8602c7906) [#50801](https://github.com/vllm-project/vllm/pull/50801)
  [CPU] Refine CPU kernel dispatch (#50801)
  _Files: `cmake/cpu_extension.cmake`, `docs/getting_started/installation/cpu.md`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/scaled_mm/cpu.py` _+2 more__
- **2026-08-03** [`b9d1e2437e`](https://github.com/vllm-project/vllm/commit/b9d1e2437e) [#50678](https://github.com/vllm-project/vllm/pull/50678)
  K3: Move LatentMoERunner (#50678)
  _Files: `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-03** [`4635cc3e8f`](https://github.com/vllm-project/vllm/commit/4635cc3e8f) [#50383](https://github.com/vllm-project/vllm/pull/50383)
  Shard the K3 Latent-MoE up-projection on large batches (#50383)
  _Files: `vllm/model_executor/layers/fused_moe/runner/latent_moe_runner.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-03** [`0a6446005d`](https://github.com/vllm-project/vllm/commit/0a6446005d) [#50133](https://github.com/vllm-project/vllm/pull/50133)
  [CPU] Migrate unquantized MoE to the modular-kernel experts structure (#50133)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_fused_moe_activations.hpp`, `csrc/cpu/cpu_types_riscv_impl.hpp`, `csrc/cpu/cpu_types_scalar.hpp` _+16 more__
- **2026-08-02** [`0601850791`](https://github.com/vllm-project/vllm/commit/0601850791) [#50704](https://github.com/vllm-project/vllm/pull/50704)
  [Bugfix][Models] Accept Qwen3_5MoeTextConfig in Qwen3_5MoeProcessingInfo for transformers 5.x compatibility (#50704)
  _Files: `vllm/model_executor/models/qwen3_5.py`_
- **2026-08-02** [`c67fe497a2`](https://github.com/vllm-project/vllm/commit/c67fe497a2) [#50701](https://github.com/vllm-project/vllm/pull/50701)
  [Bugfix][Doc] Fix references to FusedMoE in doc (#50701)
  _Files: `docs/design/fused_moe_modular_kernel.md`, `docs/design/moe_kernel_features.md`_
- **2026-08-01** [`c4a4a42d80`](https://github.com/vllm-project/vllm/commit/c4a4a42d80) [#50640](https://github.com/vllm-project/vllm/pull/50640)
  [Bugfix][Test] Fix monolithic routing replay test buffer capacity (#50640)
  _Files: `tests/kernels/moe/test_routed_experts_capture_monolithic.py`_
- **2026-07-31** [`454ea5b526`](https://github.com/vllm-project/vllm/commit/454ea5b526) [#44570](https://github.com/vllm-project/vllm/pull/44570)
  [MoE Refactor] Combine CompressedTensorsWNA16MarlinMoEMethod with CompressedTensorsWNA16MoEMethod (#44570)
  _Files: `tests/kernels/quantization/test_marlin_tile_padding.py`, `tests/quantization/test_compressed_tensors.py`, `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+10 more__
- **2026-07-31** [`94e9ef0768`](https://github.com/vllm-project/vllm/commit/94e9ef0768) [#50137](https://github.com/vllm-project/vllm/pull/50137)
  [Bugfix] Don't transpose fused MoE quantization scales in `RoutedExperts.load_weights` (#50137)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-07-31** [`0e9b50074e`](https://github.com/vllm-project/vllm/commit/0e9b50074e) [#50116](https://github.com/vllm-project/vllm/pull/50116)
  [chore] clean-up weight prepack for INT8 MoE (#50116)
  _Files: `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int8.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w8a8_int8.py`, `vllm/model_executor/layers/quantization/online/int8.py`_
- **2026-07-31** [`0bff0ce5d3`](https://github.com/vllm-project/vllm/commit/0bff0ce5d3) [#50458](https://github.com/vllm-project/vllm/pull/50458)
  [Kimi K3 Bug] Fix deepgemm support for kimi k3 (#50458)
  _Files: `tests/kernels/moe/test_deepgemm.py`, `vllm/model_executor/layers/fused_moe/deep_gemm_utils.py`_
- **2026-07-30** [`68fb303a41`](https://github.com/vllm-project/vllm/commit/68fb303a41) [#48438](https://github.com/vllm-project/vllm/pull/48438)
  [Bugfix] Preserve Marlin runtime tensor storage across weight reload (#48438)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/kernels/linear/mixed_precision/marlin.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16_marlin.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils.py` _+2 more__
- **2026-07-30** [`0eec856cc3`](https://github.com/vllm-project/vllm/commit/0eec856cc3) [#50468](https://github.com/vllm-project/vllm/pull/50468)
  Add Humming indexed-MoE regression test (#50468)
  _Files: `tests/kernels/moe/test_moe.py`_
- **2026-07-30** [`61cacd272f`](https://github.com/vllm-project/vllm/commit/61cacd272f) [#50338](https://github.com/vllm-project/vllm/pull/50338)
  [Bugfix][MoE] Write Humming results to the supplied output buffer (#50338)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`_
- **2026-07-30** [`072a472782`](https://github.com/vllm-project/vllm/commit/072a472782) [#50387](https://github.com/vllm-project/vllm/pull/50387)
  [CPU] Bump up CPU kernels to latest version (#50387)
  _Files: `csrc/cpu/sgl-kernels/common.h`, `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/sgl-kernels/fla.cpp`, `csrc/cpu/sgl-kernels/gemm.cpp` _+11 more__
- **2026-07-30** [`e5f48dfda2`](https://github.com/vllm-project/vllm/commit/e5f48dfda2) [#47124](https://github.com/vllm-project/vllm/pull/47124)
  [Quantization][Autoround][XPU] Add W4A16(moe) / MXFP4(linear/moe) Support (#47124)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/config_parser.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/__init__.py` _+5 more__
- **2026-07-30** [`b28c178ffd`](https://github.com/vllm-project/vllm/commit/b28c178ffd) [#38293](https://github.com/vllm-project/vllm/pull/38293)
  Fix: FusedMoE AssertionError with Speculative Decoding on Quark-Quantized Models (#38293)
- **2026-07-29** [`82642d7d6c`](https://github.com/vllm-project/vllm/commit/82642d7d6c) [#49750](https://github.com/vllm-project/vllm/pull/49750)
  [Perf] RMSNorm uncontiguous support, 1.2~3.1x kernel performance improvement (#49750)
  _Files: `csrc/libtorch_stable/layernorm_kernels.cu`, `tests/kernels/core/test_layernorm.py`, `vllm/model_executor/models/apertus.py`, `vllm/model_executor/models/deepseek_v2.py` _+5 more__
- **2026-07-29** [`ad5d29db70`](https://github.com/vllm-project/vllm/commit/ad5d29db70) [#50210](https://github.com/vllm-project/vllm/pull/50210)
  [Model] Support Qwen3.5 text-only dense and MoE models (#50210)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/config.py`, `vllm/model_executor/models/qwen3_5.py`, `vllm/model_executor/models/registry.py` _+1 more__
- **2026-07-29** [`6f00a1ae3b`](https://github.com/vllm-project/vllm/commit/6f00a1ae3b) [#42436](https://github.com/vllm-project/vllm/pull/42436)
  fused_moe: add VLLM_TRITON_USE_TD tensor-descriptor path (#42436)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/fused_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-07-29** [`32a423ac0a`](https://github.com/vllm-project/vllm/commit/32a423ac0a) [#49580](https://github.com/vllm-project/vllm/pull/49580)
  Integrate CuTeDSL MoE for ReLU2 NVFP4 (#49580)
  _Files: `tests/kernels/moe/test_flashinfer_cutedsl_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`, `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_
- **2026-07-29** [`17a74b745b`](https://github.com/vllm-project/vllm/commit/17a74b745b) [#48876](https://github.com/vllm-project/vllm/pull/48876)
  [Model] Add Inkling compressed-tensors dynamic FP8 support (#48876)
  _Files: `tests/models/inkling/test_moe_weight_layout.py`, `vllm/models/inkling/nvidia/moe.py`_
- **2026-07-28** [`bb3b61f2fd`](https://github.com/vllm-project/vllm/commit/bb3b61f2fd) [#49618](https://github.com/vllm-project/vllm/pull/49618)
  perf: dispatch non-grouped bias-less topk routing methods to fused path (#49618)
  _Files: `tests/kernels/moe/test_routing.py`, `vllm/model_executor/layers/fused_moe/router/router_factory.py`_
- **2026-07-28** [`60915c972c`](https://github.com/vllm-project/vllm/commit/60915c972c) [#47750](https://github.com/vllm-project/vllm/pull/47750)
  [Feature] Add VidCom2 video token pruning (#47750)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `docs/features/multimodal_inputs.md`, `tests/multimodal/test_vidcom2.py`, `vllm/config/model.py` _+13 more__
- **2026-07-27** [`1e34a13539`](https://github.com/vllm-project/vllm/commit/1e34a13539) [#49096](https://github.com/vllm-project/vllm/pull/49096)
  Fix Humming non-gated MoE (#49096)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/quantization/utils/humming_utils.py`_
- **2026-07-27** [`99115fcdcd`](https://github.com/vllm-project/vllm/commit/99115fcdcd) [#49912](https://github.com/vllm-project/vllm/pull/49912)
  [CI] Initialize DeepEP FP8 test weights (#49912)
  _Files: `tests/kernels/moe/test_deepep_moe.py`_
- **2026-07-27** [`b2f9e4caa4`](https://github.com/vllm-project/vllm/commit/b2f9e4caa4) [#50004](https://github.com/vllm-project/vllm/pull/50004)
  [DSv4 Perf] Adaptive topk width, 1.0% E2E throughput improvement (#50004)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/sparse_mla.py`_
- **2026-07-27** [`ed13deb376`](https://github.com/vllm-project/vllm/commit/ed13deb376) [#49985](https://github.com/vllm-project/vllm/pull/49985)
  [Bugfix][CPU] Fall back to torch for unaligned swigluoai on NEON/vec MoE (#49985)
  _Files: `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`_
- **2026-07-27** [`99de48e98f`](https://github.com/vllm-project/vllm/commit/99de48e98f) [#49982](https://github.com/vllm-project/vllm/pull/49982)
  Fix MLA padding and grouped topk routing in the Transformers modelling backend (#49982)
  _Files: `tests/models/transformers/fusers/test_moe.py`, `vllm/model_executor/models/transformers/__init__.py`, `vllm/model_executor/models/transformers/fusers/moe.py`, `vllm/model_executor/models/transformers/moe.py` _+1 more__
- **2026-07-27** [`96fa3f42c9`](https://github.com/vllm-project/vllm/commit/96fa3f42c9) [#49659](https://github.com/vllm-project/vllm/pull/49659)
  [Perf] Skip ll_bf16 router GEMM warmup for non-MoE models (#49659)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-07-27** [`eb290ab673`](https://github.com/vllm-project/vllm/commit/eb290ab673) [#49591](https://github.com/vllm-project/vllm/pull/49591)
  [Bugfix][CPU] Zero-pad MoE intermediate size for grouped-gemm TP alignment (#49591)
  _Files: `tests/kernels/moe/test_cpu_fused_moe.py`, `vllm/model_executor/layers/fused_moe/cpu_fused_moe.py`_
- **2026-07-27** [`c314af1abf`](https://github.com/vllm-project/vllm/commit/c314af1abf) [#48637](https://github.com/vllm-project/vllm/pull/48637)
  [CPU][Perf] INT8 Fused MoE Kernel for Arm CPUs (#48637)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_fused_moe.cpp`, `csrc/cpu/cpu_fused_moe_activations.hpp`, `csrc/cpu/cpu_fused_moe_int8.cpp` _+8 more__

## Attention  (30 commits)

- **2026-08-01** [`eb6453d95b`](https://github.com/vllm-project/vllm/commit/eb6453d95b) [#50474](https://github.com/vllm-project/vllm/pull/50474)
  [Build] Update pin to build ABI stable FA2 (#50474)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-07-31** [`90329913e9`](https://github.com/vllm-project/vllm/commit/90329913e9) [#50590](https://github.com/vllm-project/vllm/pull/50590)
  [UX] Reduce startup log noise (#50590)
  _Files: `vllm/config/vllm.py`, `vllm/distributed/device_communicators/custom_all_reduce.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`, `vllm/model_executor/warmup/cutedsl_warmup.py` _+5 more__
- **2026-07-31** [`aef85aed5d`](https://github.com/vllm-project/vllm/commit/aef85aed5d) [#50533](https://github.com/vllm-project/vllm/pull/50533)
  [Bugfix][TurboQuant] Add KV quant mode for turboquant  (#50533)
  _Files: `tests/quantization/test_turboquant.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/v1/kv_cache_interface.py`, `vllm/v1/worker/gpu/attn_utils.py`_
- **2026-07-31** [`a0cd2b69b3`](https://github.com/vllm-project/vllm/commit/a0cd2b69b3) [#50302](https://github.com/vllm-project/vllm/pull/50302)
  [Bugfix] Universally align block table width to 128 tokens (#50302)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/v1/attention/backend.py` _+4 more__
- **2026-07-31** [`df71917cf1`](https://github.com/vllm-project/vllm/commit/df71917cf1) [#49236](https://github.com/vllm-project/vllm/pull/49236)
  [DSv4 Perf] Optimize workspace reuse for eager break, 3.9% E2E TTFT improvement. (#49236)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/test_compressor_kv_cache.py` _+11 more__
- **2026-07-31** [`82ae4164ee`](https://github.com/vllm-project/vllm/commit/82ae4164ee) [#48770](https://github.com/vllm-project/vllm/pull/48770)
  [2/N][Attention] Enable masked MHA for sparse MLA prefills (#48770)
  _Files: `benchmarks/attention_benchmarks/benchmark.py`, `benchmarks/attention_benchmarks/common.py`, `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa.yaml`, `benchmarks/attention_benchmarks/mla_runner.py` _+7 more__
- **2026-07-31** [`b2fb83e7ff`](https://github.com/vllm-project/vllm/commit/b2fb83e7ff) [#50148](https://github.com/vllm-project/vllm/pull/50148)
  [Attention]: Use KVCacheSpec for AttentionMetadataBuilder type hints (#50148)
  _Files: `vllm/model_executor/layers/attention/chunked_local_attention.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/flash_attn.py` _+10 more__
- **2026-07-31** [`34bb795ff3`](https://github.com/vllm-project/vllm/commit/34bb795ff3) [#49143](https://github.com/vllm-project/vllm/pull/49143)
  [CI] Add M3 MSA tests to CI (#49143)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/common/indexer.py`_
- **2026-07-31** [`10e6b40015`](https://github.com/vllm-project/vllm/commit/10e6b40015) [#50437](https://github.com/vllm-project/vllm/pull/50437)
  [CPU][BugFix] Remove redundant kv cache write (#50437)
  _Files: `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-07-31** [`b49eaf205a`](https://github.com/vllm-project/vllm/commit/b49eaf205a) [#48047](https://github.com/vllm-project/vllm/pull/48047)
  [DSv4] Remove sparse-MLA q-head padding for FlashInfer >=0.6.14 (#48047)
  _Files: `vllm/models/deepseek_v4/nvidia/flashinfer_sparse.py`_
- **2026-07-31** [`541128bdeb`](https://github.com/vllm-project/vllm/commit/541128bdeb) [#50301](https://github.com/vllm-project/vllm/pull/50301)
  [KV Offload] Enable single-copy MLA layout for CPUOffloadingSpec (#50301)
  _Files: `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/cpu/spec.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-07-31** [`ef0d084b4b`](https://github.com/vllm-project/vllm/commit/ef0d084b4b) [#50349](https://github.com/vllm-project/vllm/pull/50349)
  [XPU] Fix FP8 block scale layout for MLA compatibility (#50349)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-07-30** [`dec13a33b7`](https://github.com/vllm-project/vllm/commit/dec13a33b7) [#48892](https://github.com/vllm-project/vllm/pull/48892)
  [Model Runner V2][Spec Decode] Add multi-layer MTP speculator (#48892)
  _Files: `vllm/config/speculative.py`, `vllm/models/inkling/nvidia/mtp.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py` _+5 more__
- **2026-07-30** [`c27b080d26`](https://github.com/vllm-project/vllm/commit/c27b080d26) [#50444](https://github.com/vllm-project/vllm/pull/50444)
  [compile] Fix fake kernel return dtype (#50444)
  _Files: `tests/compile/passes/test_rope_kvcache_fusion.py`, `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`, `vllm/model_executor/layers/attention/attention.py`_
- **2026-07-30** [`5f8f72866c`](https://github.com/vllm-project/vllm/commit/5f8f72866c) [#50243](https://github.com/vllm-project/vllm/pull/50243)
  [Build] Fix CUDA release wheel builds (#50243)
  _Files: `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`, `docker/Dockerfile`, `docs/assets/contributing/dockerfile-stages-dependency.png`_
- **2026-07-30** [`837eae6458`](https://github.com/vllm-project/vllm/commit/837eae6458) [#50298](https://github.com/vllm-project/vllm/pull/50298)
  [DSv4 Perf] Remove redundant full kernel for dsv4, 1.88x kernel performance improvement (#50298)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/common/ops/cache_utils.py`, `vllm/models/deepseek_v4/nvidia/flashmla.py`_
- **2026-07-30** [`5b95890742`](https://github.com/vllm-project/vllm/commit/5b95890742) [#50339](https://github.com/vllm-project/vllm/pull/50339)
  [FlexAttention] Avoid encoder block-mask compile explosion (#50339)
  _Files: `tests/entrypoints/pooling/embed/test_online_long_text.py`, `tests/kernels/test_flex_attention.py`, `vllm/config/attention.py`, `vllm/v1/attention/backends/flex_attention.py`_
- **2026-07-30** [`a7a204cc6e`](https://github.com/vllm-project/vllm/commit/a7a204cc6e) [#50322](https://github.com/vllm-project/vllm/pull/50322)
  Add FlashMLA H100 tests to CI, fix them after #32810 (#50322)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_flashmla.py`, `tests/kernels/attention/test_mla_cross_layer_kernel_equivalence.py`_
- **2026-07-29** [`65a1a16594`](https://github.com/vllm-project/vllm/commit/65a1a16594) [#50194](https://github.com/vllm-project/vllm/pull/50194)
  [CPU] Fix FP8 attention scratchpad sizing (#50194)
  _Files: `csrc/cpu/cpu_attn.cpp`, `csrc/cpu/torch_bindings.cpp`, `tests/kernels/attention/test_cpu_attn.py`, `vllm/_custom_ops.py` _+1 more__
- **2026-07-29** [`f37f03db4a`](https://github.com/vllm-project/vllm/commit/f37f03db4a) [#49762](https://github.com/vllm-project/vllm/pull/49762)
  [KV Connector] Support NIXL P/D for hybrid MLA+SSM models  (#49762)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+1 more__
- **2026-07-28** [`0b6aa3c47c`](https://github.com/vllm-project/vllm/commit/0b6aa3c47c) [#50065](https://github.com/vllm-project/vllm/pull/50065)
  [Bugfix][Spec Decode] Size DFlash query buffers for cudagraph-padded batches (#50065)
  _Files: `vllm/v1/spec_decode/dflash.py`_
- **2026-07-28** [`ba702e978e`](https://github.com/vllm-project/vllm/commit/ba702e978e) [#48407](https://github.com/vllm-project/vllm/pull/48407)
  [Attention] Skip sparse indexer scoring for dense short prefills (#48407)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`, `vllm/model_executor/layers/mla.py` _+3 more__
- **2026-07-28** [`9b9fc4039c`](https://github.com/vllm-project/vllm/commit/9b9fc4039c) [#45841](https://github.com/vllm-project/vllm/pull/45841)
  add epilogue hook to flex attention (#45841)
  _Files: `vllm/v1/attention/backends/flex_attention.py`_
- **2026-07-27** [`bf2b45b5d6`](https://github.com/vllm-project/vllm/commit/bf2b45b5d6) [#42669](https://github.com/vllm-project/vllm/pull/42669)
  [Attention] Integrate FlashAttention 4 SM100 headdim 256 support (#42669)
  _Files: `benchmarks/attention_benchmarks/benchmark.py`, `docs/design/attention_backends.md`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/v1/attention/backends/fa_utils.py` _+3 more__
- **2026-07-27** [`a89015c6df`](https://github.com/vllm-project/vllm/commit/a89015c6df) [#48739](https://github.com/vllm-project/vllm/pull/48739)
  [Perf] Make merge attention context count a runtime argument (#48739)
  _Files: `vllm/v1/attention/ops/triton_merge_attn_states.py`_
- **2026-07-27** [`81962bb699`](https://github.com/vllm-project/vllm/commit/81962bb699) [#49043](https://github.com/vllm-project/vllm/pull/49043)
  [Bugfix]Reject invalid FlashInfer MNNVL workspaces (#49043)
  _Files: `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-07-27** [`8061dc26bd`](https://github.com/vllm-project/vllm/commit/8061dc26bd) [#49392](https://github.com/vllm-project/vllm/pull/49392)
  [Bugfix] Normalize sparse MLA warmup compression ratios (#49392)
  _Files: `tests/v1/attention/test_indexer_deepseek_v4_slot_mapping.py`, `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-07-27** [`544cb724c8`](https://github.com/vllm-project/vllm/commit/544cb724c8) [#48577](https://github.com/vllm-project/vllm/pull/48577)
  [CPU][Spec Decode] Optimize GDN conv path for speculative decoding (#48577)
  _Files: `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/torch_bindings.cpp`, `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `vllm/_custom_ops.py` _+1 more__
- **2026-07-27** [`f0553889c0`](https://github.com/vllm-project/vllm/commit/f0553889c0) [#48366](https://github.com/vllm-project/vllm/pull/48366)
  [Bugfix] Prevent NaN poisoning in xpu_mla_sparse for fully-masked index chunks (#48366)
  _Files: `tests/kernels/attention/test_xpu_mla_sparse.py`, `vllm/v1/attention/ops/xpu_mla_sparse.py`_
- **2026-07-27** [`fdaa0d9e59`](https://github.com/vllm-project/vllm/commit/fdaa0d9e59) [#49331](https://github.com/vllm-project/vllm/pull/49331)
  [ModelRunner V2] Support encoder-only attention (#49331)
  _Files: `tests/models/language/pooling/test_embedding.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/model_runner.py` _+4 more__

## CI / Build  (25 commits)

- **2026-07-31** [`7c08664f5c`](https://github.com/vllm-project/vllm/commit/7c08664f5c) [#50522](https://github.com/vllm-project/vllm/pull/50522)
  Upgrade tpu-inference to v0.26.0 (#50522)
  _Files: `requirements/tpu.txt`_
- **2026-07-31** [`10ad649d6c`](https://github.com/vllm-project/vllm/commit/10ad649d6c) [#50412](https://github.com/vllm-project/vllm/pull/50412)
  Update torch version to 2.13.0+cpu (#50412)
  _Files: `requirements/build/tpu.txt`_
- **2026-07-31** [`0351e9aa1f`](https://github.com/vllm-project/vllm/commit/0351e9aa1f) [#50373](https://github.com/vllm-project/vllm/pull/50373)
  [XPU][CI]Adjust source_file_dependencies for NixlConnector PD accuracy (4 GPUs) (#50373)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`_
- **2026-07-31** [`60399d48eb`](https://github.com/vllm-project/vllm/commit/60399d48eb) [#50481](https://github.com/vllm-project/vllm/pull/50481)
  [CI] Retry Buildkite API rate limits (#50481)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-07-31** [`553fcb82d5`](https://github.com/vllm-project/vllm/commit/553fcb82d5) [#49908](https://github.com/vllm-project/vllm/pull/49908)
  [CI] Retry Hugging Face processor loading (#49908)
  _Files: `tests/conftest.py`_
- **2026-07-30** [`7fe5312332`](https://github.com/vllm-project/vllm/commit/7fe5312332) [#50475](https://github.com/vllm-project/vllm/pull/50475)
  [CI] Retire the v1 PR label rule, add mrv2 (#50475)
  _Files: `.github/mergify.yml`_
- **2026-07-30** [`bdc98bf506`](https://github.com/vllm-project/vllm/commit/bdc98bf506) [#50377](https://github.com/vllm-project/vllm/pull/50377)
  [CI] Initialize fused gated RMSNorm weights (#50377)
  _Files: `tests/kernels/core/test_fused_rms_norm_gated.py`_
- **2026-07-30** [`61c1d098e5`](https://github.com/vllm-project/vllm/commit/61c1d098e5) [#50284](https://github.com/vllm-project/vllm/pull/50284)
  [CI] Stabilize speculator memory teardown (#50284)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`_
- **2026-07-30** [`48a077e4cf`](https://github.com/vllm-project/vllm/commit/48a077e4cf) [#50414](https://github.com/vllm-project/vllm/pull/50414)
  [CI] Improve comment-triggered authorization and retries (#50414)
  _Files: `.github/workflows/notify-ci-authorized.yml`, `.github/workflows/record-ci-approval.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-07-30** [`445d3aac0a`](https://github.com/vllm-project/vllm/commit/445d3aac0a) [#50318](https://github.com/vllm-project/vllm/pull/50318)
  [CI] Retry failed steps on new PR commits (#50318)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-07-30** [`0028fc8d8d`](https://github.com/vllm-project/vllm/commit/0028fc8d8d) [#50207](https://github.com/vllm-project/vllm/pull/50207)
  [XPU][CI]Add back skipped V1 test (#50207)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-07-30** [`1ad5182ba9`](https://github.com/vllm-project/vllm/commit/1ad5182ba9) [#50357](https://github.com/vllm-project/vllm/pull/50357)
  [CI/Build] Limit wheel size check to CUDA 13 (#50357)
  _Files: `.buildkite/scripts/hardware_ci/run-gh200-test.sh`, `docker/Dockerfile`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-07-29** [`625871b52c`](https://github.com/vllm-project/vllm/commit/625871b52c) [#50241](https://github.com/vllm-project/vllm/pull/50241)
  [CI][Test] Fix pooling truncation test after VLLMError hierarchy change (#50241)
  _Files: `tests/models/language/pooling/test_truncation_control.py`_
- **2026-07-29** [`9a4e5f9539`](https://github.com/vllm-project/vllm/commit/9a4e5f9539) [#43538](https://github.com/vllm-project/vllm/pull/43538)
  [CI/Perf] Fix malformed serving benchmark config (#43538)
  _Files: `.buildkite/performance-benchmarks/tests/serving-tests.json`_
- **2026-07-29** [`5b29c958c7`](https://github.com/vllm-project/vllm/commit/5b29c958c7) [#48677](https://github.com/vllm-project/vllm/pull/48677)
  [XPU] upgrade to torch 2.13 (#48677)
  _Files: `.buildkite/scripts/hardware_ci/run-intel-test.sh`, `docker/Dockerfile.xpu`, `docs/getting_started/installation/gpu.xpu.inc.md`, `requirements/test/xpu.txt` _+3 more__
- **2026-07-29** [`100d655a23`](https://github.com/vllm-project/vllm/commit/100d655a23) [#50211](https://github.com/vllm-project/vllm/pull/50211)
  [CI] Allow PR comment acknowledgements (#50211)
  _Files: `.github/workflows/run-ci-command.yml`_
- **2026-07-29** [`7de49bab7e`](https://github.com/vllm-project/vllm/commit/7de49bab7e) [#48703](https://github.com/vllm-project/vllm/pull/48703)
  [XPU][UT][CI] add xpu config to run gpt-oss accuracy in ut and ci (#48703)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-baseline.yaml`, `tests/evals/gpt_oss/configs/gpt-oss-20b-xpu-triton-attn.yaml`, `tests/evals/gpt_oss/configs/models-xpu.txt`_
- **2026-07-29** [`db7a79cbf7`](https://github.com/vllm-project/vllm/commit/db7a79cbf7) [#50144](https://github.com/vllm-project/vllm/pull/50144)
  [CPU] Fix s390x builds and update torch version in dockerfile (#50144)
  _Files: `csrc/cpu/cpu_types_vxe.hpp`, `docker/Dockerfile.s390x`_
- **2026-07-29** [`54ab69b14e`](https://github.com/vllm-project/vllm/commit/54ab69b14e) [#50197](https://github.com/vllm-project/vllm/pull/50197)
  [CI] Allow comment-triggered builds past pipeline filters (#50197)
  _Files: `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-07-29** [`7f4c52f2ba`](https://github.com/vllm-project/vllm/commit/7f4c52f2ba) [#50132](https://github.com/vllm-project/vllm/pull/50132)
  [CI] Add comment-based Buildkite triggers (#50132)
  _Files: `.github/workflows/new_pr_bot.yml`, `.github/workflows/pre-commit.yml`, `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py` _+2 more__
- **2026-07-29** [`fe65aa6a97`](https://github.com/vllm-project/vllm/commit/fe65aa6a97) [#50171](https://github.com/vllm-project/vllm/pull/50171)
  [CI][NIXL] Fix flaky DP+EP test port conflict (#50171)
  _Files: `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`_
- **2026-07-28** [`247470f23a`](https://github.com/vllm-project/vllm/commit/247470f23a) [#48164](https://github.com/vllm-project/vllm/pull/48164)
  [CI] Add PyTorch stable ABI audit check (#48164)
  _Files: `.buildkite/check-torch-abi.py`, `.buildkite/ci_config.yaml`, `.buildkite/test_areas/torch_abi.yaml`, `requirements/test/cpu.txt` _+2 more__
- **2026-07-28** [`74587939b1`](https://github.com/vllm-project/vllm/commit/74587939b1) [#49904](https://github.com/vllm-project/vllm/pull/49904)
  [Build] Fix CUDA arch detection producing kernel-less builds on SM121 (#49904)
  _Files: `CMakeLists.txt`, `cmake/utils.cmake`, `tests/test_cmake_utils.py`_
- **2026-07-27** [`afc94523c9`](https://github.com/vllm-project/vllm/commit/afc94523c9) [#49939](https://github.com/vllm-project/vllm/pull/49939)
  [XPU][CI] Use platform device in InputBatch V2 test (#49939)
  _Files: `tests/v1/worker/test_gpu_input_batch_v2.py`_
- **2026-07-27** [`ff6173997d`](https://github.com/vllm-project/vllm/commit/ff6173997d) [#49895](https://github.com/vllm-project/vllm/pull/49895)
  [CI] Add kimi and k3 auto-labeling rules (#49895)
  _Files: `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`_

## Multimodal  (23 commits)

- **2026-08-03** [`9acb7b3699`](https://github.com/vllm-project/vllm/commit/9acb7b3699) [#50839](https://github.com/vllm-project/vllm/pull/50839)
  [CI] And PPL test for multimodal generation models  (#50839)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`, `tests/models/multimodal/generation_ppl_test/__init__.py`, `tests/models/multimodal/generation_ppl_test/ppl_utils.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`_
- **2026-08-03** [`89ac407e3d`](https://github.com/vllm-project/vllm/commit/89ac407e3d) [#50716](https://github.com/vllm-project/vllm/pull/50716)
  [Perf] Speed up multimodal placeholder and token-match scanning (#50716)
  _Files: `tests/multimodal/test_processing.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-03** [`d83eb0b36b`](https://github.com/vllm-project/vllm/commit/d83eb0b36b) [#50755](https://github.com/vllm-project/vllm/pull/50755)
  fix(security): classify DeepStream as GPU backend and enforce pixel limits (#50755)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/multimodal/media/video.py`, `vllm/multimodal/video.py`_
- **2026-08-02** [`e2fa28594f`](https://github.com/vllm-project/vllm/commit/e2fa28594f) [#49934](https://github.com/vllm-project/vllm/pull/49934)
  [1/N] Unify multiple-path encoder cuda graph support (#49934)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/interfaces.py` _+3 more__
- **2026-07-31** [`7fdc1ab29e`](https://github.com/vllm-project/vllm/commit/7fdc1ab29e) [#50560](https://github.com/vllm-project/vllm/pull/50560)
  [CI] Remove default_torch_num_threads workaround from llava-onevision-transformers test (#50560)
  _Files: `tests/models/multimodal/generation/test_common.py`_
- **2026-07-31** [`17beffd55f`](https://github.com/vllm-project/vllm/commit/17beffd55f) [#50141](https://github.com/vllm-project/vllm/pull/50141)
  [Misc] Clarify mono audio requirement (#50141)
  _Files: `docs/features/multimodal_inputs.md`, `tests/multimodal/test_audio.py`, `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/multimodal/audio.py`_
- **2026-07-31** [`f727951d3f`](https://github.com/vllm-project/vllm/commit/f727951d3f) [#50305](https://github.com/vllm-project/vllm/pull/50305)
  [Bugfix] Re-land MiniMax M3 default video processor (#50305)
  _Files: `tests/multimodal/test_video.py`, `vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py`, `vllm/models/minimax_m3/common/mm_preprocess.py`_
- **2026-07-31** [`3ee2bd1321`](https://github.com/vllm-project/vllm/commit/3ee2bd1321) [#49691](https://github.com/vllm-project/vllm/pull/49691)
  Fix duplicate HunyuanVL image boundary tokens (#49691)
  _Files: `vllm/model_executor/models/hunyuan_vision.py`_
- **2026-07-31** [`1180b604f8`](https://github.com/vllm-project/vllm/commit/1180b604f8) [#49686](https://github.com/vllm-project/vllm/pull/49686)
  [Multimodal] Expose mm hash algothrim selection to cli args (#49686)
  _Files: `docs/usage/security.md`, `tests/config/test_multimodal_config.py`, `tests/models/multimodal/processing/test_moss_audio.py`, `tests/multimodal/test_cache.py` _+13 more__
- **2026-07-30** [`8700f86a70`](https://github.com/vllm-project/vllm/commit/8700f86a70) [#50451](https://github.com/vllm-project/vllm/pull/50451)
  [CI] Fix `tests/entrypoints/multimodal/openai/chat_completion/test_audio.py::test_chat_streaming_audio` (#50451)
  _Files: `tests/entrypoints/multimodal/openai/chat_completion/test_audio.py`_
- **2026-07-30** [`f388dd6592`](https://github.com/vllm-project/vllm/commit/f388dd6592) [#50447](https://github.com/vllm-project/vllm/pull/50447)
  [XPU][CI] skip kimi-k3 test (#50447)
  _Files: `tests/models/multimodal/processing/test_common.py`_
- **2026-07-29** [`9d1aa4dda8`](https://github.com/vllm-project/vllm/commit/9d1aa4dda8) [#48543](https://github.com/vllm-project/vllm/pull/48543)
  [Frontend] Add diarized_json support for MOSS-Transcribe-Diarize (#48543)
  _Files: `docs/serving/online_serving/speech_to_text.md`, `tests/models/multimodal/processing/test_moss_transcribe_diarize.py`, `vllm/entrypoints/speech_to_text/base/protocol.py`, `vllm/entrypoints/speech_to_text/base/serving.py` _+5 more__
- **2026-07-29** [`2ecd8645d8`](https://github.com/vllm-project/vllm/commit/2ecd8645d8) [#50092](https://github.com/vllm-project/vllm/pull/50092)
  Revert "[Misc][Minimax-M3]add default video_processor (#50092)" (#50313)
  _Files: `tests/multimodal/test_video.py`, `vllm/models/minimax_m3/common/mm_preprocess.py`_
- **2026-07-29** [`5c7a7f9462`](https://github.com/vllm-project/vllm/commit/5c7a7f9462) [#49066](https://github.com/vllm-project/vllm/pull/49066)
  [docs] Add documentation for pynvvideocodec video decoding backend (#49066)
  _Files: `docs/features/multimodal_inputs.md`_
- **2026-07-29** [`242c591d5a`](https://github.com/vllm-project/vllm/commit/242c591d5a) [#49341](https://github.com/vllm-project/vllm/pull/49341)
  [Rust Frontend] Send multimodal tensors in auxiliary frames (#49341)
  _Files: `rust/src/chat/src/multimodal/expand.rs`, `rust/src/chat/src/multimodal/tensor.rs`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs` _+7 more__
- **2026-07-29** [`aeaa50a71c`](https://github.com/vllm-project/vllm/commit/aeaa50a71c) [#49975](https://github.com/vllm-project/vllm/pull/49975)
  [Bugfix][Multimodal] Include media IO config in MM cache hash (#49975)
  _Files: `tests/multimodal/test_hasher.py`, `vllm/multimodal/hasher.py`, `vllm/multimodal/media/base.py`, `vllm/multimodal/media/image.py` _+1 more__
- **2026-07-29** [`c44e191b01`](https://github.com/vllm-project/vllm/commit/c44e191b01) [#49604](https://github.com/vllm-project/vllm/pull/49604)
  [Rust Frontend] Add --limit-mm-per-prompt support (#49604)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/error.rs`, `rust/src/chat/src/multimodal.rs` _+10 more__
- **2026-07-29** [`df2735ea2e`](https://github.com/vllm-project/vllm/commit/df2735ea2e) [#50092](https://github.com/vllm-project/vllm/pull/50092)
  [Misc][Minimax-M3]add default video_processor (#50092)
  _Files: `tests/multimodal/test_video.py`, `vllm/models/minimax_m3/common/mm_preprocess.py`_
- **2026-07-29** [`58f9659397`](https://github.com/vllm-project/vllm/commit/58f9659397) [#49665](https://github.com/vllm-project/vllm/pull/49665)
  [Frontend][Core] Standardize request error handling with VLLMError hierarchy (#49665)
  _Files: `tests/engine/test_short_mm_context.py`, `tests/entrypoints/llm/test_chat.py`, `tests/entrypoints/llm/test_prompt_validation.py`, `tests/entrypoints/multimodal/llm/test_mm_embeds_only.py` _+42 more__
- **2026-07-28** [`2899dca843`](https://github.com/vllm-project/vllm/commit/2899dca843) [#50104](https://github.com/vllm-project/vllm/pull/50104)
  [Model] Add Kimi K3 support: Rust frontend [1/2] (#50104)
  _Files: `pyproject.toml`, `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/backend/hf.rs` _+31 more__
- **2026-07-28** [`1db989bbf1`](https://github.com/vllm-project/vllm/commit/1db989bbf1) [#49030](https://github.com/vllm-project/vllm/pull/49030)
  [Bugfix][Multimodal] Fix video temporal padding estimates (#49030)
  _Files: `tests/models/multimodal/processing/test_glm4_1v.py`, `vllm/model_executor/models/glm4_1v.py`, `vllm/model_executor/models/kanana_v.py`, `vllm/model_executor/models/keye.py` _+3 more__
- **2026-07-28** [`90245f4190`](https://github.com/vllm-project/vllm/commit/90245f4190) [#50073](https://github.com/vllm-project/vllm/pull/50073)
  [Bugfix] Fix multi-modal support on CPU MRV2 (#50073)
  _Files: `vllm/multimodal/inputs.py`, `vllm/v1/worker/cpu/shm.py`, `vllm/v1/worker/gpu/model_states/encoder_decoder.py`_
- **2026-07-27** [`04502deca2`](https://github.com/vllm-project/vllm/commit/04502deca2) [#49607](https://github.com/vllm-project/vllm/pull/49607)
  [Perf] Hash videos by source bytes (#49607)
  _Files: `tests/multimodal/test_hasher.py`, `vllm/multimodal/hasher.py`, `vllm/multimodal/inputs.py`, `vllm/multimodal/media/base.py` _+4 more__

## Disaggregation / PD  (21 commits)

- **2026-08-02** [`96add737ff`](https://github.com/vllm-project/vllm/commit/96add737ff) [#50641](https://github.com/vllm-project/vllm/pull/50641)
  [Elastic EP] Fix non-contiguous weight transfers (#50641)
  _Files: `vllm/distributed/elastic_ep/elastic_execute.py`_
- **2026-08-01** [`3986b967b2`](https://github.com/vllm-project/vllm/commit/3986b967b2) [#50498](https://github.com/vllm-project/vllm/pull/50498)
  (feat): optionally disable lookup on PD decode (#50498)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/scheduler.py` _+1 more__
- **2026-07-31** [`2c4d348848`](https://github.com/vllm-project/vllm/commit/2c4d348848) [#48408](https://github.com/vllm-project/vllm/pull/48408)
  [KV Connector] Add per-layer canonical KV page mappings for parallelism-agnostic offload (#48408)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_canonical_mapping.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py` _+2 more__
- **2026-07-30** [`30b4e7f479`](https://github.com/vllm-project/vllm/commit/30b4e7f479) [#48981](https://github.com/vllm-project/vllm/pull/48981)
  [rl] Stateful Trainer Send: IPC [2/N] (#48981)
  _Files: `examples/rl/rlhf_http_ipc.py`, `examples/rl/rlhf_ipc.py`, `examples/rl/rlhf_ipc_fsdp_ep.py`, `tests/distributed/test_weight_transfer.py` _+4 more__
- **2026-07-30** [`4e582c5b54`](https://github.com/vllm-project/vllm/commit/4e582c5b54) [#50326](https://github.com/vllm-project/vllm/pull/50326)
  [PD][Bugfix] Rebase KV lease deadlines onto worker clock (#50326)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py` _+1 more__
- **2026-07-30** [`437e0b7f8e`](https://github.com/vllm-project/vllm/commit/437e0b7f8e) [#50297](https://github.com/vllm-project/vllm/pull/50297)
  [BugFix] Fix P/D preemption race condition (#50297)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py` _+3 more__
- **2026-07-30** [`0a31372e5f`](https://github.com/vllm-project/vllm/commit/0a31372e5f) [#47301](https://github.com/vllm-project/vllm/pull/47301)
  [Frontend] Add detokenization streaming derender for disaggregated serving (#47301)
  _Files: `tests/entrypoints/scale_out/derender/test_derender_stream.py`, `vllm/entrypoints/scale_out/derender/api_router.py`, `vllm/entrypoints/scale_out/derender/serving.py`, `vllm/entrypoints/scale_out/token_in_token_out/protocol.py` _+2 more__
- **2026-07-29** [`48aa8d8d75`](https://github.com/vllm-project/vllm/commit/48aa8d8d75) [#41357](https://github.com/vllm-project/vllm/pull/41357)
  [Bugfix] Prevent stale multiproc RPC deadlines from becoming unbounded waits (#41357)
  _Files: `tests/v1/executor/test_multiproc_executor_timeout.py`, `vllm/distributed/device_communicators/shm_broadcast.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-07-29** [`5fa0154448`](https://github.com/vllm-project/vllm/commit/5fa0154448) [#49647](https://github.com/vllm-project/vllm/pull/49647)
  [Rubin] Enable NVLink all-reduce paths on SM107 (#49647)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/all_reduce_utils.py`, `vllm/distributed/device_communicators/symm_mem.py`_
- **2026-07-29** [`48fc2e2797`](https://github.com/vllm-project/vllm/commit/48fc2e2797) [#50033](https://github.com/vllm-project/vllm/pull/50033)
  feat(grpc): add KV event source discovery (#50033)
  _Files: `rust/proto/control.proto`, `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/engine-core-client/src/tests/client.rs` _+9 more__
- **2026-07-29** [`82553692b8`](https://github.com/vllm-project/vllm/commit/82553692b8) [#50153](https://github.com/vllm-project/vllm/pull/50153)
  [KV Connector] Fix NIXL mamba state pairing for multi-slot block tables (#50153)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py` _+2 more__
- **2026-07-29** [`dad7a6383b`](https://github.com/vllm-project/vllm/commit/dad7a6383b) [#49582](https://github.com/vllm-project/vllm/pull/49582)
  [EC Connector] Add has_pending_push_work  (#49582)
  _Files: `vllm/distributed/ec_transfer/ec_connector/base.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-07-28** [`a07fac758f`](https://github.com/vllm-project/vllm/commit/a07fac758f) [#48442](https://github.com/vllm-project/vllm/pull/48442)
  [Perf] Zero-copy torch.Tensor pickling in shm_broadcast MessageQueue (#48442)
  _Files: `tests/distributed/test_shm_broadcast.py`, `tools/pre_commit/check_forbidden_imports.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-07-28** [`94100b5915`](https://github.com/vllm-project/vllm/commit/94100b5915) [#49340](https://github.com/vllm-project/vllm/pull/49340)
  [CI] Wire untethered test files into CI jobs (#49340)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/kernels.yaml` _+5 more__
- **2026-07-28** [`601fa9a74e`](https://github.com/vllm-project/vllm/commit/601fa9a74e) [#49612](https://github.com/vllm-project/vllm/pull/49612)
  [KV Connector] Support NIXL heterogeneous P/D block sizes for hybrid models (#49612)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_desc_geometry.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py` _+3 more__
- **2026-07-28** [`98e91a9600`](https://github.com/vllm-project/vllm/commit/98e91a9600) [#49345](https://github.com/vllm-project/vllm/pull/49345)
  [PD][NixlPush] Skip extra `add_remote_agent` step in D->P handshake (#49345)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-07-28** [`35efdf6b34`](https://github.com/vllm-project/vllm/commit/35efdf6b34) [#47288](https://github.com/vllm-project/vllm/pull/47288)
  [Elastic EP] Async preparation (#47288)
  _Files: `.buildkite/test_areas/expert_parallelism.yaml`, `tests/distributed/test_elastic_ep.py`, `vllm/config/parallel.py`, `vllm/distributed/device_communicators/base_device_communicator.py` _+17 more__
- **2026-07-28** [`9069a57139`](https://github.com/vllm-project/vllm/commit/9069a57139) [#49040](https://github.com/vllm-project/vllm/pull/49040)
  [Core][Frontend] Add weight version tagging for RL rollouts (#49040)
  _Files: `docs/serving/offline_inference.md`, `docs/serving/online_serving/README.md`, `docs/training/async_rl.md`, `docs/training/weight_transfer/README.md` _+12 more__
- **2026-07-27** [`831d3848f1`](https://github.com/vllm-project/vllm/commit/831d3848f1) [#48879](https://github.com/vllm-project/vllm/pull/48879)
  [Core] Fail fast when /dev/shm is too small for the shm ring buffer (#48879)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-07-27** [`2b465b2c42`](https://github.com/vllm-project/vllm/commit/2b465b2c42) [#49988](https://github.com/vllm-project/vllm/pull/49988)
  [Misc][PD] Nixl cleanup `get_backend_aware_kv_block_len` and `virtually_split_kv_in_blocks` (#49988)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-07-27** [`ffc4f08c8e`](https://github.com/vllm-project/vllm/commit/ffc4f08c8e) [#46116](https://github.com/vllm-project/vllm/pull/46116)
  [Core][KV-transfer] MoRIIO: heterogeneous TP<->DP prefill/decode read routing (#46116)
  _Files: `tests/v1/kv_connector/unit/test_moriio_routing_fairness.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_

## Quantization  (20 commits)

- **2026-08-03** [`e481da9508`](https://github.com/vllm-project/vllm/commit/e481da9508) [#49664](https://github.com/vllm-project/vllm/pull/49664)
  [XPU] [Linear] add torch as xpu linear backend (#49664)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docs/features/quantization/online.md`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py` _+1 more__
- **2026-08-03** [`2755489a26`](https://github.com/vllm-project/vllm/commit/2755489a26) [#50807](https://github.com/vllm-project/vllm/pull/50807)
  [INC]  fix w4a4 model (#50807)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp4_linear.py`_
- **2026-08-01** [`ab06486175`](https://github.com/vllm-project/vllm/commit/ab06486175) [#46805](https://github.com/vllm-project/vllm/pull/46805)
  [Bugfix][Kernel] Fix dangling temporary in AWQ gemm torch::stable::sum dim arg (#46805)
  _Files: `csrc/libtorch_stable/quantization/awq/gemm_kernels.cu`_
- **2026-07-31** [`e3be89673d`](https://github.com/vllm-project/vllm/commit/e3be89673d) [#50019](https://github.com/vllm-project/vllm/pull/50019)
  Enable ModelOpt FP8 emulation on SM80 (#50019)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-07-31** [`d87d2ca747`](https://github.com/vllm-project/vllm/commit/d87d2ca747) [#50500](https://github.com/vllm-project/vllm/pull/50500)
  [Compressed-Tensors] Support Kimi-K3 quantized models (#50500)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-07-31** [`88bc8fb56f`](https://github.com/vllm-project/vllm/commit/88bc8fb56f) [#50219](https://github.com/vllm-project/vllm/pull/50219)
  [CPU][s390x] Optimize inference perf and add oneDNN INT8 GEMM for s390x (#50219)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_arch_macros.h`, `csrc/cpu/cpu_types_vxe.hpp`, `csrc/cpu/torch_bindings.cpp` _+2 more__
- **2026-07-31** [`1d8be5cb44`](https://github.com/vllm-project/vllm/commit/1d8be5cb44) [#50434](https://github.com/vllm-project/vllm/pull/50434)
  [XPU] [BugFix] Add deepseek_v4_fp8 to xpu supported_quantization list (#50434)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-30** [`45b60e3914`](https://github.com/vllm-project/vllm/commit/45b60e3914) [#50345](https://github.com/vllm-project/vllm/pull/50345)
  [Kernel][Helion] Disable unsafe B200 RMS reduction warp specialization (#50345)
  _Files: `tests/kernels/helion/test_rms_norm_per_block_quant.py`, `vllm/kernels/helion/configs/rms_norm_per_block_quant/nvidia_b200.json`_
- **2026-07-30** [`70bd10930b`](https://github.com/vllm-project/vllm/commit/70bd10930b) [#50273](https://github.com/vllm-project/vllm/pull/50273)
  [Quantization] Honor `--linear-backend` for ModelOpt W4A16 (#50273)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-07-30** [`38a267cdd5`](https://github.com/vllm-project/vllm/commit/38a267cdd5) [#49570](https://github.com/vllm-project/vllm/pull/49570)
  [MyPy][1/N] Fix mypy errors in some tests/ directories and enforce follow-imports=silent (#49570)
  _Files: `tests/compile/correctness_e2e/test_sequence_parallel.py`, `tests/compile/fullgraph/test_full_cudagraph.py`, `tests/compile/fullgraph/test_full_graph.py`, `tests/compile/fusions_e2e/conftest.py` _+26 more__
- **2026-07-29** [`1cb3fe5844`](https://github.com/vllm-project/vllm/commit/1cb3fe5844) [#50329](https://github.com/vllm-project/vllm/pull/50329)
  [CI Bugfix] Temp disable Humming wNa8 INT8 H100 CI (#50329)
  _Files: `.buildkite/test_areas/lm_eval.yaml`_
- **2026-07-29** [`30c2718eaa`](https://github.com/vllm-project/vllm/commit/30c2718eaa) [#43229](https://github.com/vllm-project/vllm/pull/43229)
  [CompressedTensors] FP4 Qutlass Integration (#43229)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/linear.py`, `vllm/model_executor/layers/quantization/compressed_tensors/transform/linear.py` _+3 more__
- **2026-07-28** [`8a7b3c2990`](https://github.com/vllm-project/vllm/commit/8a7b3c2990) [#49483](https://github.com/vllm-project/vllm/pull/49483)
  [compressed-tensors] update `find_matched_target` order to prioritize fused name matches over class match (#49483)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/utils.py`_
- **2026-07-28** [`b6cbba8bc8`](https://github.com/vllm-project/vllm/commit/b6cbba8bc8) [#48391](https://github.com/vllm-project/vllm/pull/48391)
  [Bugfix][Kernel] Fix batch invariance in RMSNorm kernels by pinning block size (#48391)
  _Files: `.buildkite/test_areas/misc.yaml`, `csrc/libtorch_stable/layernorm_kernels.cu`, `csrc/libtorch_stable/layernorm_quant_kernels.cu`, `csrc/libtorch_stable/quantization/fused_kernels/fused_layernorm_dynamic_per_token_quant.cu` _+2 more__
- **2026-07-28** [`948107acf7`](https://github.com/vllm-project/vllm/commit/948107acf7) [#48589](https://github.com/vllm-project/vllm/pull/48589)
  [Bugfix] Enhance extra_config handling for layer name suffix matching (#48589)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/config_parser.py`_
- **2026-07-28** [`25ace8fe5d`](https://github.com/vllm-project/vllm/commit/25ace8fe5d) [#49881](https://github.com/vllm-project/vllm/pull/49881)
  [CI] Increase Qwen3.5 MTP GSM8K generation length (#49881)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-397B-A17B-NVFP4-DEP2-MTP.yaml`_
- **2026-07-28** [`fbb1ef6803`](https://github.com/vllm-project/vllm/commit/fbb1ef6803) [#49634](https://github.com/vllm-project/vllm/pull/49634)
  [Bugfix] Fix DeepseekV4FP8 Quark MXFP4 crash on list-valued weight (#49634)
  _Files: `vllm/models/deepseek_v4/quant_config.py`_
- **2026-07-28** [`73af7a362a`](https://github.com/vllm-project/vllm/commit/73af7a362a) [#44513](https://github.com/vllm-project/vllm/pull/44513)
  [XPU] Add online fp8 quantization test (#44513)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `tests/models/multimodal/processing/test_common.py`, `tests/quantization/test_online.py`, `tests/quantization/utils.py` _+1 more__
- **2026-07-27** [`5d07e268b1`](https://github.com/vllm-project/vllm/commit/5d07e268b1) [#47514](https://github.com/vllm-project/vllm/pull/47514)
  [Quantization][INC]Add MXFP8 Linear Support (#47514)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/__init__.py`, `vllm/model_executor/layers/quantization/inc/schemes/factory.py` _+3 more__
- **2026-07-27** [`8de50e46d4`](https://github.com/vllm-project/vllm/commit/8de50e46d4) [#49376](https://github.com/vllm-project/vllm/pull/49376)
  [Docs] Document NVFP4 GEMM kernel selection and Marlin weight-only fallback (#49376)
  _Files: `docs/features/quantization/modelopt.md`_

## Models  (16 commits)

- **2026-08-03** [`e42c230e4f`](https://github.com/vllm-project/vllm/commit/e42c230e4f) [#50766](https://github.com/vllm-project/vllm/pull/50766)
  [Bugfix] serving_llama70B_tp4 benchmark was silently running at tensor_parallel_size=1 (#50766)
  _Files: `.buildkite/performance-benchmarks/tests/serving-tests.json`_
- **2026-08-03** [`9a4fd57cac`](https://github.com/vllm-project/vllm/commit/9a4fd57cac) [#50688](https://github.com/vllm-project/vllm/pull/50688)
  [Model] Support jina-embeddings-v5-text-nano (EuroBERT encoder backbone) (#50688)
  _Files: `docs/models/pooling_models/embed.md`, `tests/models/language/pooling/test_jina_embeddings_v5.py`, `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/test_jina.py` _+2 more__
- **2026-08-01** [`38a466e7b6`](https://github.com/vllm-project/vllm/commit/38a466e7b6) [#46789](https://github.com/vllm-project/vllm/pull/46789)
  [DSV4] Implement Sequence Parallelism (#46789)
  _Files: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/models/common/ops/sequence_parallel.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+3 more__
- **2026-08-01** [`03c782eb91`](https://github.com/vllm-project/vllm/commit/03c782eb91) [#50673](https://github.com/vllm-project/vllm/pull/50673)
  [model registry] some simple typos (#50673)
  _Files: `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/registry.py`_
- **2026-07-31** [`bebf918044`](https://github.com/vllm-project/vllm/commit/bebf918044) [#50352](https://github.com/vllm-project/vllm/pull/50352)
  [Bugfix][Model] Reject encoder-backbone jina-embeddings-v5 checkpoints with a clear error (fixes #50337) (#50352)
  _Files: `tests/models/language/pooling/test_jina_embeddings_v5.py`, `vllm/model_executor/models/config.py`_
- **2026-07-29** [`f98061ce6c`](https://github.com/vllm-project/vllm/commit/f98061ce6c) [#48883](https://github.com/vllm-project/vllm/pull/48883)
  fix(step3p5-mtp): honor exclude_modules for the MTP head via prefix (#48883)
  _Files: `vllm/model_executor/models/step3p5_mtp.py`_
- **2026-07-29** [`d6247d7173`](https://github.com/vllm-project/vllm/commit/d6247d7173) [#49731](https://github.com/vllm-project/vllm/pull/49731)
  [Spec Decode][Perf] Replicate DSpark Markov head across TP ranks (#49731)
  _Files: `tests/v1/sample/test_head_dtype.py`, `vllm/model_executor/layers/logits_processor.py`, `vllm/model_executor/layers/vocab_parallel_embedding.py`, `vllm/model_executor/models/qwen3_dspark.py`_
- **2026-07-29** [`f5a7cce9b6`](https://github.com/vllm-project/vllm/commit/f5a7cce9b6) [#50093](https://github.com/vllm-project/vllm/pull/50093)
  [Model] Add Kimi K3 support: Python frontend [2/2] (#50093)
  _Files: `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `tests/renderers/test_kimi_k3.py`, `tests/tool_parsers/test_kimi_k3_named_tool_choice.py`, `tests/tool_parsers/test_structural_tag_registry.py` _+16 more__
- **2026-07-29** [`7c6729b769`](https://github.com/vllm-project/vllm/commit/7c6729b769) [#50089](https://github.com/vllm-project/vllm/pull/50089)
  [Model] Add Kimi K3 support: model files and kernels [1/N] (#50089)
- **2026-07-28** [`0d0504b54c`](https://github.com/vllm-project/vllm/commit/0d0504b54c) [#49903](https://github.com/vllm-project/vllm/pull/49903)
  [Core] Warm up runner-owned Triton kernels before the first request (#49903)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/model_executor/warmup/kernel_warmup.py`, `vllm/model_executor/warmup/qwen_triton_warmup.py`, `vllm/model_executor/warmup/v1_block_table_warmup.py` _+3 more__
- **2026-07-28** [`d223c900d8`](https://github.com/vllm-project/vllm/commit/d223c900d8) [#50060](https://github.com/vllm-project/vllm/pull/50060)
  [Bugfix] Only pad transformers backend `value` when it is narrower (#50060)
  _Files: `vllm/model_executor/models/transformers/__init__.py`_
- **2026-07-27** [`272abd5f48`](https://github.com/vllm-project/vllm/commit/272abd5f48) [#47920](https://github.com/vllm-project/vllm/pull/47920)
  [Tests][Spec Decode] Add gemma4 MTP acceptance rates test (#47920)
  _Files: `.buildkite/test_areas/spec_decode.yaml`, `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/v1/spec_decode/gemma4.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py`_
- **2026-07-27** [`ebcef33766`](https://github.com/vllm-project/vllm/commit/ebcef33766) [#49987](https://github.com/vllm-project/vllm/pull/49987)
  Fix MQA with tensor parallelism on transformers modeling backend   (#49987)
  _Files: `tests/models/transformers/fusers/test_linear.py`, `vllm/model_executor/models/transformers/fuser.py`, `vllm/model_executor/models/transformers/fusers/__init__.py`, `vllm/model_executor/models/transformers/fusers/base.py` _+3 more__
- **2026-07-27** [`ef9975d021`](https://github.com/vllm-project/vllm/commit/ef9975d021) [#45828](https://github.com/vllm-project/vllm/pull/45828)
  [Bugfix] Reject pipeline parallelism for DiffusionGemma (#45828)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`_
- **2026-07-27** [`dbccc5ae32`](https://github.com/vllm-project/vllm/commit/dbccc5ae32) [#48912](https://github.com/vllm-project/vllm/pull/48912)
  [Model] Enable EVS for Qwen3.5 (#48912)
  _Files: `vllm/model_executor/models/qwen3_5.py`_
- **2026-07-27** [`92e8518d37`](https://github.com/vllm-project/vllm/commit/92e8518d37) [#49957](https://github.com/vllm-project/vllm/pull/49957)
  Improve Transformers modelling backend `fx` tracer (#49957)
  _Files: `tests/models/transformers/fusers/test_linear.py`, `tests/models/transformers/fusers/test_rms_norm.py`, `vllm/model_executor/models/transformers/base.py`, `vllm/model_executor/models/transformers/fuser.py` _+5 more__

## Serving / API  (14 commits)

- **2026-08-03** [`b3f97dae24`](https://github.com/vllm-project/vllm/commit/b3f97dae24) [#50816](https://github.com/vllm-project/vllm/pull/50816)
  [Frontend] Require cache_salt to be non-empty via schema (#50816)
  _Files: `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/pooling/base/protocol.py` _+1 more__
- **2026-08-03** [`f5bb701fa2`](https://github.com/vllm-project/vllm/commit/f5bb701fa2) [#50764](https://github.com/vllm-project/vllm/pull/50764)
  [Bugfix][Frontend] Constrain Anthropic cache_salt to non-empty (#50764)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`_
- **2026-08-01** [`dc818c198d`](https://github.com/vllm-project/vllm/commit/dc818c198d) [#45560](https://github.com/vllm-project/vllm/pull/45560)
  [GPT-OSS] Strict tool call and constrained decoding for Harmony (#45560)
  _Files: `tests/entrypoints/openai/responses/test_harmony.py`, `tests/parser/test_harmony.py`, `tests/reasoning/test_gptoss_reasoning_parser.py`, `tests/tool_parsers/test_structural_tag_registry.py` _+6 more__
- **2026-08-01** [`81a42d37b1`](https://github.com/vllm-project/vllm/commit/81a42d37b1) [#49498](https://github.com/vllm-project/vllm/pull/49498)
  [Frontend] Add cache_salt support to Anthropic Messages API (#49498)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-07-31** [`0c4dc7c488`](https://github.com/vllm-project/vllm/commit/0c4dc7c488) [#49668](https://github.com/vllm-project/vllm/pull/49668)
  [graceful shutdown] fix http server start firstly before app signal handler register (#49668)
  _Files: `vllm/entrypoints/launcher.py`_
- **2026-07-31** [`0b5b49dde8`](https://github.com/vllm-project/vllm/commit/0b5b49dde8) [#50491](https://github.com/vllm-project/vllm/pull/50491)
  [Bugfix][Frontend] Raise VLLMValidationError for user-facing errors in chat_utils.py (#50491)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `tests/renderers/test_chat_utils_prompt_embeds.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-07-31** [`f5ffc59b6a`](https://github.com/vllm-project/vllm/commit/f5ffc59b6a) [#50408](https://github.com/vllm-project/vllm/pull/50408)
  [Renderer] Warm up the renderer properly. (#50408)
  _Files: `vllm/entrypoints/generate/api_router.py`, `vllm/entrypoints/llm.py`, `vllm/entrypoints/openai/api_server.py`, `vllm/entrypoints/openai/chat_completion/serving.py` _+2 more__
- **2026-07-30** [`e04a30a77c`](https://github.com/vllm-project/vllm/commit/e04a30a77c) [#49914](https://github.com/vllm-project/vllm/pull/49914)
  [Frontend] Lazily initialize chat media connectors (#49914)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-07-29** [`e0cfa52d22`](https://github.com/vllm-project/vllm/commit/e0cfa52d22) [#49073](https://github.com/vllm-project/vllm/pull/49073)
  [Bugfix][Frontend] Return transcription and translation verbose as float (#49073)
  _Files: `vllm/entrypoints/speech_to_text/base/serving.py`, `vllm/entrypoints/speech_to_text/transcription/protocol.py`, `vllm/entrypoints/speech_to_text/translation/protocol.py`_
- **2026-07-28** [`01661cc57f`](https://github.com/vllm-project/vllm/commit/01661cc57f) [#50081](https://github.com/vllm-project/vllm/pull/50081)
  [Rust][Benchmark] Make `vllm bench serve` Rust delegation opt-in (#50081)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `tests/test_envs.py`, `vllm/entrypoints/cli/benchmark/main.py`, `vllm/entrypoints/cli/benchmark/serve.py` _+4 more__
- **2026-07-28** [`912d6b619d`](https://github.com/vllm-project/vllm/commit/912d6b619d) [#47494](https://github.com/vllm-project/vllm/pull/47494)
  [Rust Frontend] Align sampling validation with Python (#47494)
  _Files: `rust/src/server/src/error.rs`, `rust/src/server/src/grpc/tests.rs`, `rust/src/text/src/error.rs`, `rust/src/text/src/lib.rs` _+2 more__
- **2026-07-28** [`bf9f23003c`](https://github.com/vllm-project/vllm/commit/bf9f23003c) [#49496](https://github.com/vllm-project/vllm/pull/49496)
  [Rust Frontend] Fix finish reason for named tool choices (#49496)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-07-27** [`15d65f8669`](https://github.com/vllm-project/vllm/commit/15d65f8669) [#41131](https://github.com/vllm-project/vllm/pull/41131)
  [Bugfix] Changed speech to text chunk timestamp to cumulative approach (#41131)
  _Files: `docs/contributing/model/transcription.md`, `tests/entrypoints/speech_to_text/test_speech_to_text_cancellation.py`, `tests/entrypoints/speech_to_text/transcription/test_chunk_timestamp_offset.py`, `tests/entrypoints/speech_to_text/transcription/test_transcription_inter_chunk_spacing.py` _+1 more__
- **2026-07-27** [`27d7061ef6`](https://github.com/vllm-project/vllm/commit/27d7061ef6) [#49963](https://github.com/vllm-project/vllm/pull/49963)
  [Bugfix] Restore truncate_prompt_tokens for Jina rerank/score online (#49963)
  _Files: `tests/entrypoints/pooling/scoring/test_jina_ranking_io_processor_unit.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`_

## Scheduler / Engine  (13 commits)

- **2026-08-01** [`39f55ffdaa`](https://github.com/vllm-project/vllm/commit/39f55ffdaa) [#49608](https://github.com/vllm-project/vllm/pull/49608)
  [Core] Offload raw-prompt preprocessing to renderer thread pool in AsyncLLM (#49608)
  _Files: `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/input_processor.py`_
- **2026-07-31** [`e8b358b4c0`](https://github.com/vllm-project/vllm/commit/e8b358b4c0) [#50334](https://github.com/vllm-project/vllm/pull/50334)
  [Bugfix][Responses] Add tests for Chat Completions Responses API Render Parity (#50334)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context.py`, `tests/entrypoints/openai/responses/test_responses_utils.py`, `tests/entrypoints/openai/test_render_parity.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+4 more__
- **2026-07-31** [`726ef437a1`](https://github.com/vllm-project/vllm/commit/726ef437a1) [#49424](https://github.com/vllm-project/vllm/pull/49424)
  [chore] delete useless code (#49424)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `vllm/entrypoints/cli/serve.py`, `vllm/v1/engine/utils.py`_
- **2026-07-31** [`482cfc20f0`](https://github.com/vllm-project/vllm/commit/482cfc20f0) [#46981](https://github.com/vllm-project/vllm/pull/46981)
  [XPU] Unify XPU RMSNorm kernels with vllm_c and drop redundant XPU-specific implementation (#46981)
  _Files: `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/kernels_intel.yaml`, `tests/kernels/ir/test_layernorm.py`, `vllm/kernels/__init__.py` _+3 more__
- **2026-07-30** [`30e333ca5f`](https://github.com/vllm-project/vllm/commit/30e333ca5f) [#49840](https://github.com/vllm-project/vllm/pull/49840)
  [Bugfix] Shut down private Tensorizer engines (#49840)
  _Files: `tests/model_executor/model_loader/tensorizer_loader/test_tensorizer.py`, `vllm/model_executor/model_loader/tensorizer.py`_
- **2026-07-30** [`629a938a92`](https://github.com/vllm-project/vllm/commit/629a938a92) [#50403](https://github.com/vllm-project/vllm/pull/50403)
  [Frontend] Preserve bare Inkling text in Python and Rust parsers (#50403)
  _Files: `rust/src/parser/src/unified/inkling.rs`, `tests/parser/engine/test_inkling.py`, `vllm/parser/engine/streaming_parser_engine.py`, `vllm/parser/inkling.py`_
- **2026-07-29** [`a0c092ee72`](https://github.com/vllm-project/vllm/commit/a0c092ee72) [#48245](https://github.com/vllm-project/vllm/pull/48245)
  [BugFix] Fix `num_output_placeholders` preemption underflow (#48245)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/async_scheduler.py`, `vllm/v1/core/sched/scheduler.py` _+1 more__
- **2026-07-28** [`6453fc0b8c`](https://github.com/vllm-project/vllm/commit/6453fc0b8c) [#50053](https://github.com/vllm-project/vllm/pull/50053)
  [Bugfix] Don't reuse engine core payload buffer while zmq is sending it (#50053)
  _Files: `tests/v1/test_serial_utils.py`, `vllm/envs.py`, `vllm/v1/engine/core.py`, `vllm/v1/engine/core_client.py`_
- **2026-07-27** [`e3c2fc3b3c`](https://github.com/vllm-project/vllm/commit/e3c2fc3b3c) [#49491](https://github.com/vllm-project/vllm/pull/49491)
  [Rust Frontend][gRPC] Add server and model discovery (#49491)
  _Files: `rust/proto/control.proto`, `rust/proto/inference.proto`, `rust/src/chat/src/lib.rs`, `rust/src/engine-core-client/src/client.rs` _+14 more__
- **2026-07-27** [`59a6b0411d`](https://github.com/vllm-project/vllm/commit/59a6b0411d) [#49204](https://github.com/vllm-project/vllm/pull/49204)
  [Core] Fix internal LB load-balancing (#49204)
  _Files: `rust/src/engine-core-client/src/client/state.rs`, `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/core/sched/interface.py`, `vllm/v1/core/sched/scheduler.py` _+3 more__
- **2026-07-27** [`fd9d2ede6f`](https://github.com/vllm-project/vllm/commit/fd9d2ede6f) [#49944](https://github.com/vllm-project/vllm/pull/49944)
  [Rust Frontend] Keep `--max-model-len` engine-owned (#49944)
  _Files: `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs`, `rust/src/managed-engine/src/cli.rs`_
- **2026-07-27** [`29fdeab254`](https://github.com/vllm-project/vllm/commit/29fdeab254) [#49422](https://github.com/vllm-project/vllm/pull/49422)
  [XPU][CI] Add more test cases in Intel GPU CI (#49422)
  _Files: `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/engine_intel.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/model_runner_v2_intel.yaml` _+1 more__
- **2026-07-27** [`8040ef2426`](https://github.com/vllm-project/vllm/commit/8040ef2426) [#49754](https://github.com/vllm-project/vllm/pull/49754)
  [Frontend] expose stream_interval as req sampling param (#49754)
  _Files: `tests/v1/engine/test_output_processor.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/sampling_params.py` _+1 more__

## KV Cache / Offload  (8 commits)

- **2026-07-29** [`542a8fad6d`](https://github.com/vllm-project/vllm/commit/542a8fad6d) [#50094](https://github.com/vllm-project/vllm/pull/50094)
  [KV Offload] Move CPUOffloadingSpec onto SharedOffloadRegion (#50094)
  _Files: `tests/v1/kv_offload/test_factory.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-07-28** [`30217b0e80`](https://github.com/vllm-project/vllm/commit/30217b0e80) [#49877](https://github.com/vllm-project/vllm/pull/49877)
  [Bugfix][KV Offload][P2P] Scope serve state to fetch rounds (#49877)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `vllm/v1/kv_offload/tiering/p2p/session/client.py`, `vllm/v1/kv_offload/tiering/p2p/session/protocol.py` _+2 more__
- **2026-07-28** [`1e81853afc`](https://github.com/vllm-project/vllm/commit/1e81853afc) [#49964](https://github.com/vllm-project/vllm/pull/49964)
  [Bugfix][KV Offload] Keep Mamba block span unscaled under DCP (#49964)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-07-28** [`52c3c4a42f`](https://github.com/vllm-project/vllm/commit/52c3c4a42f) [#49947](https://github.com/vllm-project/vllm/pull/49947)
  [Bugfix][KV Offload][OBJ] Preserve job completion during cleanup (#49947)
  _Files: `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/tiering/obj/manager.py`_
- **2026-07-28** [`a8f296083f`](https://github.com/vllm-project/vllm/commit/a8f296083f) [#49858](https://github.com/vllm-project/vllm/pull/49858)
  [KV Offload] Make compact secondary identity TP-independent (#49858)
  _Files: `tests/v1/kv_offload/test_file_mapper.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py`, `vllm/v1/kv_offload/file_mapper.py`_
- **2026-07-27** [`77cba0259f`](https://github.com/vllm-project/vllm/commit/77cba0259f) [#48123](https://github.com/vllm-project/vllm/pull/48123)
  [KV Offloading] Per-request tier filtering with TierFilter/TierMatcher (#48123)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+12 more__
- **2026-07-27** [`d742856610`](https://github.com/vllm-project/vllm/commit/d742856610) [#49502](https://github.com/vllm-project/vllm/pull/49502)
  [3/N][Core][KV Connector] Support reliable partial-tail KV offload for sub-block prompts (#49502)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+9 more__
- **2026-07-27** [`53397fbfac`](https://github.com/vllm-project/vllm/commit/53397fbfac) [#49823](https://github.com/vllm-project/vllm/pull/49823)
  [Bugfix][KV Offload][P2P] Fix EngineCore crash reconnecting to a reaped peer (#49823)
  _Files: `tests/v1/kv_offload/tiering/p2p/test_zmq_transport.py`, `vllm/v1/kv_offload/tiering/p2p/control/base.py`, `vllm/v1/kv_offload/tiering/p2p/control/zmq.py`_

## Perf / Benchmark  (6 commits)

- **2026-08-03** [`d9dac2b3d4`](https://github.com/vllm-project/vllm/commit/d9dac2b3d4) [#46870](https://github.com/vllm-project/vllm/pull/46870)
  fix: remove stray duplicate from serving benchmark config (#46870)
  _Files: `.pre-commit-config.yaml`_
- **2026-08-01** [`63e78ce365`](https://github.com/vllm-project/vllm/commit/63e78ce365) [#49611](https://github.com/vllm-project/vllm/pull/49611)
  [Benchmark] Add probe requests to vllm bench serve (#49611)
  _Files: `docs/benchmarking/cli.md`, `tests/benchmarks/test_skip_tokenizer_init.py`, `vllm/benchmarks/serve.py`_
- **2026-08-01** [`62195e9784`](https://github.com/vllm-project/vllm/commit/62195e9784) [#50058](https://github.com/vllm-project/vllm/pull/50058)
  [Rust][Benchmark] Prevent invalid token IDs in random benchmarks (#50058)
  _Files: `rust/src/bench/src/tiktoken.rs`_
- **2026-08-01** [`b40d859c7b`](https://github.com/vllm-project/vllm/commit/b40d859c7b) [#48968](https://github.com/vllm-project/vllm/pull/48968)
  [Kernel][Helion] Add numerics checks to benchmark script (#48968)
  _Files: `scripts/benchmark_helion_kernels.py`, `tests/kernels/helion/test_benchmark_script.py`_
- **2026-07-27** [`56c96b0d91`](https://github.com/vllm-project/vllm/commit/56c96b0d91) [#48774](https://github.com/vllm-project/vllm/pull/48774)
  [Perf] Tune LL BF16 Router GEMM (#48774)
  _Files: `vllm/model_executor/kernels/linear/cute_dsl/ll_bf16.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-07-27** [`f19ee27e39`](https://github.com/vllm-project/vllm/commit/f19ee27e39) [#49571](https://github.com/vllm-project/vllm/pull/49571)
  [Hardware][Power] Add FAST_EXP for Power (#49571)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `csrc/cpu/cpu_arch_macros.h`, `csrc/cpu/cpu_types_vsx.hpp`_

## Speculative Decoding  (6 commits)

- **2026-08-03** [`5c4fe4b17e`](https://github.com/vllm-project/vllm/commit/5c4fe4b17e) [#49069](https://github.com/vllm-project/vllm/pull/49069)
  [Bugfix][KV Connector] Propagate EAGLE state across merged Mooncake store groups (#49069)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`_
- **2026-08-01** [`4ee9702bee`](https://github.com/vllm-project/vllm/commit/4ee9702bee) [#50600](https://github.com/vllm-project/vllm/pull/50600)
  Add Understanding the Latency Metrics docs (#50600)
  _Files: `docs/assets/benchmarking/latency-metrics-speculative-decoding-dark.svg`, `docs/assets/benchmarking/latency-metrics-speculative-decoding-light.svg`, `docs/benchmarking/cli.md`_
- **2026-07-29** [`32e657e689`](https://github.com/vllm-project/vllm/commit/32e657e689) [#49343](https://github.com/vllm-project/vllm/pull/49343)
  [BugFix] eagle draft max position embeddings (#49343)
  _Files: `tests/config/test_speculative_draft_max_position_embeddings.py`, `tests/v1/spec_decode/test_llm_base_proposer.py`, `vllm/config/speculative.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-07-28** [`b09688a6e7`](https://github.com/vllm-project/vllm/commit/b09688a6e7) [#49774](https://github.com/vllm-project/vllm/pull/49774)
  [Bugfix][Spec Decode] Preserve draft buffers across level-2 sleep (#49774)
  _Files: `vllm/v1/worker/gpu_worker.py`_
- **2026-07-27** [`fd10e8946d`](https://github.com/vllm-project/vllm/commit/fd10e8946d) [#43559](https://github.com/vllm-project/vllm/pull/43559)
  [Test] Regression test for hybrid-Mamba eagle cache-peek in Mooncake connector (#43559) (#48361)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`_
- **2026-07-27** [`5f89a03dcb`](https://github.com/vllm-project/vllm/commit/5f89a03dcb) [#49910](https://github.com/vllm-project/vllm/pull/49910)
  [CI] Explicitly tear down speculative decode runners (#49910)
  _Files: `tests/v1/spec_decode/test_max_len.py`_

## Docs  (6 commits)

- **2026-07-31** [`c036cb257f`](https://github.com/vllm-project/vllm/commit/c036cb257f) [#50571](https://github.com/vllm-project/vllm/pull/50571)
  [Doc] Add BgeM3EmbeddingModel to embedding supported models (#50571)
  _Files: `docs/models/pooling_models/embed.md`_
- **2026-07-30** [`89d97d9a16`](https://github.com/vllm-project/vllm/commit/89d97d9a16) [#50397](https://github.com/vllm-project/vllm/pull/50397)
  docs(security): document Ray cluster trust model and env var propagation (#50397)
  _Files: `docs/usage/security.md`_
- **2026-07-30** [`8122a10536`](https://github.com/vllm-project/vllm/commit/8122a10536) [#50308](https://github.com/vllm-project/vllm/pull/50308)
  [DOC][CPU] remove tcmalloc warning from CPU docs (#50308)
  _Files: `docs/getting_started/installation/cpu.arm.inc.md`, `docs/getting_started/installation/cpu.x86.inc.md`_
- **2026-07-29** [`dc1be79031`](https://github.com/vllm-project/vllm/commit/dc1be79031) [#49114](https://github.com/vllm-project/vllm/pull/49114)
  Add CachePolicyFactory for pluggable/external eviction policies (#49114)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/cpu/__init__.py`, `tests/v1/kv_offload/cpu/policies/__init__.py`, `tests/v1/kv_offload/cpu/policies/test_factory.py` _+11 more__
- **2026-07-28** [`4fb483ca86`](https://github.com/vllm-project/vllm/commit/4fb483ca86) [#45432](https://github.com/vllm-project/vllm/pull/45432)
  [Docs] Expand llm-d integration page (#45432)
  _Files: `docs/deployment/integrations/llm-d.md`_
- **2026-07-28** [`60b3d39cd3`](https://github.com/vllm-project/vllm/commit/60b3d39cd3) [#50057](https://github.com/vllm-project/vllm/pull/50057)
  [Docs] Remove experimental warning for EP (#50057)
  _Files: `docs/serving/expert_parallel_deployment.md`_

## Compilation / CUDA Graph  (2 commits)

- **2026-07-29** [`93477454f9`](https://github.com/vllm-project/vllm/commit/93477454f9) [#50244](https://github.com/vllm-project/vllm/pull/50244)
  [torch.compile] Compile `CustomOp.forward_native` for ReLU^2 to avoid raw torch ops inside opaque custom ops (#50244)
  _Files: `vllm/model_executor/layers/activation.py`_
- **2026-07-27** [`bf4f633b4c`](https://github.com/vllm-project/vllm/commit/bf4f633b4c) [#49394](https://github.com/vllm-project/vllm/pull/49394)
  [XPU] Enable QK Norm + RoPE fusion pass on XPU (#49394)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `vllm/compilation/passes/pass_manager.py`, `vllm/platforms/xpu.py`_

## LoRA  (2 commits)

- **2026-07-28** [`5ed3faa43d`](https://github.com/vllm-project/vllm/commit/5ed3faa43d) [#49992](https://github.com/vllm-project/vllm/pull/49992)
  [Rust Frontend] Add ordinary-text tokenizer encoding (#49992)
  _Files: `rust/src/chat/src/renderer/inkling/tests.rs`, `rust/src/parser/benches/utils/adapter.rs`, `rust/src/parser/src/unified/inkling.rs`, `rust/src/text/src/backend/hf/mod.rs` _+6 more__
- **2026-07-27** [`50aa830482`](https://github.com/vllm-project/vllm/commit/50aa830482) [#49751](https://github.com/vllm-project/vllm/pull/49751)
  [BugFix][MRV2] Don't create dummy requests longer than `max_model_len` (#49751)
  _Files: `tests/v1/worker/test_gpu_input_batch_v2.py`, `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/lora_utils.py`, `vllm/v1/worker/gpu/model_runner.py`_

---
_Generated 2026-08-03 11:39 UTC_