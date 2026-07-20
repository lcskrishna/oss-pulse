# vllm-project/vllm — Weekly Change Report
**Period:** 2026-07-13 → 2026-07-20  |  **Total commits:** 242

## ✨ New Features This Week

- **2026-07-20** [#47122](https://github.com/vllm-project/vllm/pull/47122) — [XPU] [MoE] add quant input when prepare for fusedmoe (#47122)
- **2026-07-20** [#47641](https://github.com/vllm-project/vllm/pull/47641) — [Hardware][CPU] Enable granite-4 model on cpu (#47641)
- **2026-07-19** [#49044](https://github.com/vllm-project/vllm/pull/49044) — [ROCm] [Release] [Per-commit] Reenable per commit rocm wheel (#49044)
- **2026-07-19** [#46570](https://github.com/vllm-project/vllm/pull/46570) — [Core] Add MRV2 virtual-batch PCP for MLA (#46570)
- **2026-07-17** [#47975](https://github.com/vllm-project/vllm/pull/47975) — [XPU] support HND layout (#47975)
- **2026-07-17** [#48281](https://github.com/vllm-project/vllm/pull/48281) — [KV Offload] Add optional tier locality to FS/OBJ KV events (#48281)
- **2026-07-17** [#41599](https://github.com/vllm-project/vllm/pull/41599) — [Model] Support TranslateGemma-12b-it (#41599)
- **2026-07-17** [#48042](https://github.com/vllm-project/vllm/pull/48042) — [rl] Stateful Trainer Send: New Abstractions [1/N]  (#48042)
- **2026-07-17** [#48878](https://github.com/vllm-project/vllm/pull/48878) — Add blocks_per_chunk configuration for KV offloading to support heterogeneous KV cache groups (#48878)
- **2026-07-17** [#48617](https://github.com/vllm-project/vllm/pull/48617) — [Render] Add round trip parity test and docs for derender (#48617)
- _…and 46 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-07-20** [`752bd10647`](https://github.com/vllm-project/vllm/commit/752bd10647) [#49128](https://github.com/vllm-project/vllm/pull/49128) — [ROCm][CI] Fix sparse MLA metadata sync fixture (#49128)
- **2026-07-19** [`ace9fda495`](https://github.com/vllm-project/vllm/commit/ace9fda495) [#47932](https://github.com/vllm-project/vllm/pull/47932) — [CI/Build][BugFix][The Rock][AMD] Add spawn method in vision examples to avoid reinitialization (#47932)
- **2026-07-19** [`ef0aa7ca2f`](https://github.com/vllm-project/vllm/commit/ef0aa7ca2f) [#49044](https://github.com/vllm-project/vllm/pull/49044) — [ROCm] [Release] [Per-commit] Reenable per commit rocm wheel (#49044)
- **2026-07-18** [`df362b2d6d`](https://github.com/vllm-project/vllm/commit/df362b2d6d) [#49055](https://github.com/vllm-project/vllm/pull/49055) — [ROCm][CI] Ensure sliding window tests release GPU memory (#49055)
- **2026-07-18** [`e94243893d`](https://github.com/vllm-project/vllm/commit/e94243893d) [#46832](https://github.com/vllm-project/vllm/pull/46832) — [ROCm][DSv3.2][Perf] Cap sparse MLA decode KV-splits with a work-per-split heuristic (#46832)
- **2026-07-18** [`f12b80c6ef`](https://github.com/vllm-project/vllm/commit/f12b80c6ef) [#43979](https://github.com/vllm-project/vllm/pull/43979) — [ROCm][Bugfix] Fix GPT-OSS Quark MXFP4 MoE loading - emulation buffer not block-aligned (#43979)
- **2026-07-17** [`cc25f028b7`](https://github.com/vllm-project/vllm/commit/cc25f028b7) [#46868](https://github.com/vllm-project/vllm/pull/46868) — [Loader] Improve InstantTensor loading (#46868)
- **2026-07-17** [`c4cd2bd544`](https://github.com/vllm-project/vllm/commit/c4cd2bd544) [#46115](https://github.com/vllm-project/vllm/pull/46115) — [Bugfix] MoRIIO toy P/D proxy: fix DP-rank index aliasing + harden for high-concurrency bursts (#46115)
- **2026-07-17** [`efed8a1e83`](https://github.com/vllm-project/vllm/commit/efed8a1e83) [#48788](https://github.com/vllm-project/vllm/pull/48788) — [ROCm][Perf][DSV4] Improve sparse decode reduction occupancy on gfx950 (#48788)
- **2026-07-17** [`867ff69733`](https://github.com/vllm-project/vllm/commit/867ff69733) [#48772](https://github.com/vllm-project/vllm/pull/48772) — [CI] Gate non-default release wheel builds (#48772)
- **2026-07-16** [`f17be06fbe`](https://github.com/vllm-project/vllm/commit/f17be06fbe) [#48143](https://github.com/vllm-project/vllm/pull/48143) — [Perf] Optimize `clamp` to `clamp_` (#48143)
- **2026-07-16** [`2cab53ddee`](https://github.com/vllm-project/vllm/commit/2cab53ddee) [#42749](https://github.com/vllm-project/vllm/pull/42749) — [Model][Hardware][AMD]: Part 1/2 -> Enable e2e QK Norm + RoPE + KV Cache runtime fusion for Qwen3-30B-A3B on ROCM_AITER_FA, and ROCM_AITER_UNIFIED_ATTN (#42749)
- **2026-07-16** [`971dac2caa`](https://github.com/vllm-project/vllm/commit/971dac2caa) [#47495](https://github.com/vllm-project/vllm/pull/47495) — [Bugfix][KV-transfer] MoRIIO: retry RDMA send-queue-full backpressure instead of failing the read (#47495)
- **2026-07-16** [`626c90b2d5`](https://github.com/vllm-project/vllm/commit/626c90b2d5) [#48500](https://github.com/vllm-project/vllm/pull/48500) — [Refactor] Move fla to third party (#48500)
- **2026-07-16** [`7d56fe2adc`](https://github.com/vllm-project/vllm/commit/7d56fe2adc) [#48015](https://github.com/vllm-project/vllm/pull/48015) — [ROCm][CI] Avoid HIP init at config time via lazy aiter import in Quark OCP-MX (#48015)
- **2026-07-16** [`b8168e33e0`](https://github.com/vllm-project/vllm/commit/b8168e33e0) [#46275](https://github.com/vllm-project/vllm/pull/46275) — [ROCm][Perf][DSV4] Enable split sparse decode on gfx942 (#46275)
- **2026-07-16** [`7dc2698632`](https://github.com/vllm-project/vllm/commit/7dc2698632) [#48784](https://github.com/vllm-project/vllm/pull/48784) — [ROCm][CI] Set "highest" matmul precision for reference hf_runner in `test_bert_for_masked_lm` (#48784)
- **2026-07-16** [`6a9f24aa8c`](https://github.com/vllm-project/vllm/commit/6a9f24aa8c) [#48764](https://github.com/vllm-project/vllm/pull/48764) — [ROCm][CI] Fix cuda graph mem profile issue (#48764)
- **2026-07-16** [`3c1bc1fc0d`](https://github.com/vllm-project/vllm/commit/3c1bc1fc0d) [#48519](https://github.com/vllm-project/vllm/pull/48519) — [ROCm][Perf] Optimize sparse attention prefill kernel for DeepSeek-V4 (#48519)
- **2026-07-15** [`015b0320de`](https://github.com/vllm-project/vllm/commit/015b0320de) [#48643](https://github.com/vllm-project/vllm/pull/48643) — Add giuseppegrossi to rocm label auto cc action (#48643)
- **2026-07-15** [`eb33ff34dd`](https://github.com/vllm-project/vllm/commit/eb33ff34dd) [#47718](https://github.com/vllm-project/vllm/pull/47718) — [ROCm][Perf] DSv4 two-stage compressor kernel for HCA prefill (#47718)
- **2026-07-15** [`49e777cf08`](https://github.com/vllm-project/vllm/commit/49e777cf08) [#48773](https://github.com/vllm-project/vllm/pull/48773) — [CI][ROCm] Retry failed Docker build steps once (#48773)
- **2026-07-15** [`1d99f0f421`](https://github.com/vllm-project/vllm/commit/1d99f0f421) [#47770](https://github.com/vllm-project/vllm/pull/47770) — [ROCm][BugFix] Triton W4A16 handling for GPTQ/AutoGPTQ qzeros layout  (#47770)
- **2026-07-15** [`0885b51981`](https://github.com/vllm-project/vllm/commit/0885b51981) [#48746](https://github.com/vllm-project/vllm/pull/48746) — [CI][ROCm] Stabilize ci_base hash calculation and image handoff (#48746)
- **2026-07-15** [`05eed72aec`](https://github.com/vllm-project/vllm/commit/05eed72aec) [#48526](https://github.com/vllm-project/vllm/pull/48526) — [ROCm] Re-enable cudagraph memory profiling, captured on the current stream (#48526)
- **2026-07-15** [`7aab6e2684`](https://github.com/vllm-project/vllm/commit/7aab6e2684) [#48688](https://github.com/vllm-project/vllm/pull/48688) — [ROCm][Bugfix] Enable the fp32 head_dtype torch.mm fast path on ROCm (#48688)
- **2026-07-15** [`d119beb1b9`](https://github.com/vllm-project/vllm/commit/d119beb1b9) [#48159](https://github.com/vllm-project/vllm/pull/48159) — [ROCm] Add tuned selective_state_update config for AMD MI350 (#48159)
- **2026-07-15** [`adce068118`](https://github.com/vllm-project/vllm/commit/adce068118) [#48676](https://github.com/vllm-project/vllm/pull/48676) — [ROCm][CI] fix test_common.py (#48676)
- **2026-07-15** [`b6770d7b54`](https://github.com/vllm-project/vllm/commit/b6770d7b54) [#48527](https://github.com/vllm-project/vllm/pull/48527) — [ROCm] Run init test engine in-process to avoid KV-cache OOM (#48527)
- **2026-07-15** [`96d2ceda4b`](https://github.com/vllm-project/vllm/commit/96d2ceda4b) [#44549](https://github.com/vllm-project/vllm/pull/44549) — [Security] Replace diskcache to eliminate pickle deserialization (#44549)
- **2026-07-15** [`3ad85e0de4`](https://github.com/vllm-project/vllm/commit/3ad85e0de4) [#48387](https://github.com/vllm-project/vllm/pull/48387) — [CI][AMD] Configure MI300 tests for native execution without DinD (#48387)
- **2026-07-15** [`6e073440b1`](https://github.com/vllm-project/vllm/commit/6e073440b1) [#47330](https://github.com/vllm-project/vllm/pull/47330) — [ROCm][CI] Remove mxfp4 test skips after `amd-quark` 0.12 release (#47330)
- **2026-07-14** [`0f0f28b537`](https://github.com/vllm-project/vllm/commit/0f0f28b537) [#48654](https://github.com/vllm-project/vllm/pull/48654) — [Bugfix][CI] Fix test_head_dtype quant_method test on ROCm (#48654)
- **2026-07-14** [`520a20ba4e`](https://github.com/vllm-project/vllm/commit/520a20ba4e) [#45222](https://github.com/vllm-project/vllm/pull/45222) — [Bugfix] MoRIIO toy P/D proxy: add /health (#45222)
- **2026-07-14** [`05d4f8bba3`](https://github.com/vllm-project/vllm/commit/05d4f8bba3) [#48647](https://github.com/vllm-project/vllm/pull/48647) — [ROCm][CI] fix flashinfer import check (#48647)
- **2026-07-14** [`7ffb98e248`](https://github.com/vllm-project/vllm/commit/7ffb98e248) [#48373](https://github.com/vllm-project/vllm/pull/48373) — [ROCm] Retune MI355 selective_state_update float32 config on the unified effective_batch grid (#48373)
- **2026-07-14** [`ca3618bc69`](https://github.com/vllm-project/vllm/commit/ca3618bc69) [#45437](https://github.com/vllm-project/vllm/pull/45437) — [Doc] Sync four function docstrings with their signatures (#45437)
- **2026-07-14** [`31be872f55`](https://github.com/vllm-project/vllm/commit/31be872f55) [#48372](https://github.com/vllm-project/vllm/pull/48372) — [ROCm] Retune MI355 selective_state_update float16 config on the unified effective_batch grid (#48372)
- **2026-07-14** [`95aab66e95`](https://github.com/vllm-project/vllm/commit/95aab66e95) [#47984](https://github.com/vllm-project/vllm/pull/47984) — [ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA (#47984)
- **2026-07-14** [`dcf4072da9`](https://github.com/vllm-project/vllm/commit/dcf4072da9) [#45000](https://github.com/vllm-project/vllm/pull/45000) — [Perf][ROCm] Fix GDN KKT warmup regression on RDNA by avoiding fp32 tl.dot (#45000)
- **2026-07-14** [`382bbd5144`](https://github.com/vllm-project/vllm/commit/382bbd5144) [#40977](https://github.com/vllm-project/vllm/pull/40977) — [ROCm][Kernel] Add HybridW4A16LinearKernel: Triton prefill + HIP skinny decode (#40977)
- **2026-07-14** [`b50ef9c6ed`](https://github.com/vllm-project/vllm/commit/b50ef9c6ed) [#44849](https://github.com/vllm-project/vllm/pull/44849) — [ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER (#44849)
- **2026-07-14** [`c4f5cd60da`](https://github.com/vllm-project/vllm/commit/c4f5cd60da) [#47327](https://github.com/vllm-project/vllm/pull/47327) — [1/N] Add dense MHA path for sparse MLA short sequences (#47327)
- **2026-07-13** [`18c4067a54`](https://github.com/vllm-project/vllm/commit/18c4067a54) [#48513](https://github.com/vllm-project/vllm/pull/48513) — [ROCm][CI] Unblock `AMD: Language Models Test (Extended Pooling)` (#48513)
- **2026-07-13** [`9427c45386`](https://github.com/vllm-project/vllm/commit/9427c45386) [#48258](https://github.com/vllm-project/vllm/pull/48258) — [ROCm][CI] Transformers: pass only one of input_ids/inputs_embeds (#48258)
- **2026-07-13** [`bea70c7cfc`](https://github.com/vllm-project/vllm/commit/bea70c7cfc) [#48011](https://github.com/vllm-project/vllm/pull/48011) — [Attention] Make sliding-window support an explicit backend capability (#48011)
- **2026-07-13** [`b7b58d1eba`](https://github.com/vllm-project/vllm/commit/b7b58d1eba) [#46527](https://github.com/vllm-project/vllm/pull/46527) — [ROCm][CI] Cache Rust builds by source inputs (#46527)
- **2026-07-13** [`d973cce3ca`](https://github.com/vllm-project/vllm/commit/d973cce3ca) [#48440](https://github.com/vllm-project/vllm/pull/48440) — Re-disable CUDA graph memory profiling on ROCm (#48440)
- **2026-07-13** [`775c1589ea`](https://github.com/vllm-project/vllm/commit/775c1589ea) [#48446](https://github.com/vllm-project/vllm/pull/48446) — [Bugfix][ROCm] Keep TP all_gather on base-class collective (#48446)
- **2026-07-13** [`ee5a89f4d7`](https://github.com/vllm-project/vllm/commit/ee5a89f4d7) [#47287](https://github.com/vllm-project/vllm/pull/47287) — [ROCm][MiniMax-M3] Add AITER sparse paged attention (#47287)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#49181](https://github.com/vllm-project/vllm/issues/49181) | [Bug]: /inference/v1/generate returns HTTP 200 on internal generation  | bug | 2026-07-20 |
| [#49090](https://github.com/vllm-project/vllm/issues/49090) | [RFC][SpecDecode] Move MTP completeness validation to the weight-updat | — | 2026-07-20 |
| [#47761](https://github.com/vllm-project/vllm/issues/47761) | [Bug]: vllm 0.23.0 and 0.24.0 - Qwen3.6-35B-A3B-FP8 - Fails generating | bug | 2026-07-20 |
| [#49127](https://github.com/vllm-project/vllm/issues/49127) | [Bug]: Native KV offloading with prefix caching changes tool visibilit | bug | 2026-07-20 |
| [#38976](https://github.com/vllm-project/vllm/issues/38976) | [Bug]:TimeoutError: RPC call to sample_tokens timed out. when pp is on | bug, stale | 2026-07-20 |
| [#43559](https://github.com/vllm-project/vllm/issues/43559) | [Bug]: Accuracy drops ~20% when `--enable-prefix-caching` is used toge | bug | 2026-07-20 |
| [#48808](https://github.com/vllm-project/vllm/issues/48808) | [Bug]: DP request distribution becomes imbalanced under long-context w | bug | 2026-07-20 |
| [#49147](https://github.com/vllm-project/vllm/issues/49147) | [Bug]: Minimax-M3 running crase | bug | 2026-07-20 |
| [#49141](https://github.com/vllm-project/vllm/issues/49141) | [Bug]: Fused_moe dimension mismatch for Qwen mxfp4 model on ROCM | bug, rocm | 2026-07-20 |
| [#49118](https://github.com/vllm-project/vllm/issues/49118) | [Bug]: OffloadingConnector — aborting a queued (never-scheduled) reque | — | 2026-07-20 |
| [#48576](https://github.com/vllm-project/vllm/issues/48576) | [Perf][ROCm] Optimize DSA lightning-indexer fp8_mqa_logits scoring ker | rocm | 2026-07-20 |
| [#33099](https://github.com/vllm-project/vllm/issues/33099) | [Bug]: vllm Requests stuck indefinitely | bug, stale | 2026-07-20 |
| [#41663](https://github.com/vllm-project/vllm/issues/41663) | [Bug]: XPU TP=2 on dual Intel Arc Pro B70 (Battlemage): GP fault + xe  | bug, intel-gpu | 2026-07-20 |
| [#28649](https://github.com/vllm-project/vllm/issues/28649) | [Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into v | feature request, rocm, unstale | 2026-07-20 |
| [#37729](https://github.com/vllm-project/vllm/issues/37729) | [Bug]: V1 engine core deadlocks under concurrent load (fp8 + prefix ca | bug | 2026-07-20 |
| [#40290](https://github.com/vllm-project/vllm/issues/40290) | [Bug]: Gemma 4 (31B/26B-A4B) vision outputs only <pad> under fp16 — vi | — | 2026-07-19 |
| [#48680](https://github.com/vllm-project/vllm/issues/48680) | [Bug]: `--enable-sleep-mode` OOMs loading an NVFP4 (modelopt) 30B on 1 | — | 2026-07-19 |
| [#49122](https://github.com/vllm-project/vllm/issues/49122) | [Bug]: AriaForConditionalGeneration produces incoherent garbage output | bug | 2026-07-19 |
| [#32335](https://github.com/vllm-project/vllm/issues/32335) | [Feature]: Extract KV-Cache update from all attention backends | help wanted, good first issue, feature request | 2026-07-19 |
| [#49068](https://github.com/vllm-project/vllm/issues/49068) | [Bug]: verbose_json returns duration as a string instead of a number | bug, rocm | 2026-07-19 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 47 |
| Attention | 28 |
| MoE / Expert Parallel | 26 |
| Other | 22 |
| Disaggregation / PD | 15 |
| Serving / API | 14 |
| Quantization | 12 |
| Multimodal | 11 |
| Scheduler / Engine | 11 |
| KV Cache / Offload | 10 |
| Models | 10 |
| CI / Build | 9 |
| Speculative Decoding | 9 |
| Docs | 8 |
| Compilation / CUDA Graph | 4 |
| LoRA | 4 |
| Perf / Benchmark | 2 |

## ROCm / AMD  (47 commits)

- **2026-07-20** [`752bd10647`](https://github.com/vllm-project/vllm/commit/752bd10647) [#49128](https://github.com/vllm-project/vllm/pull/49128)
  [ROCm][CI] Fix sparse MLA metadata sync fixture (#49128)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_sparse_metadata_sync.py`_
- **2026-07-19** [`ace9fda495`](https://github.com/vllm-project/vllm/commit/ace9fda495) [#47932](https://github.com/vllm-project/vllm/pull/47932)
  [CI/Build][BugFix][The Rock][AMD] Add spawn method in vision examples to avoid reinitialization (#47932)
  _Files: `examples/generate/multimodal/vision_language_multi_image_offline.py`, `examples/generate/multimodal/vision_language_offline.py`_
- **2026-07-19** [`ef0aa7ca2f`](https://github.com/vllm-project/vllm/commit/ef0aa7ca2f) [#49044](https://github.com/vllm-project/vllm/pull/49044)
  [ROCm] [Release] [Per-commit] Reenable per commit rocm wheel (#49044)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-07-18** [`df362b2d6d`](https://github.com/vllm-project/vllm/commit/df362b2d6d) [#49055](https://github.com/vllm-project/vllm/pull/49055)
  [ROCm][CI] Ensure sliding window tests release GPU memory (#49055)
  _Files: `tests/v1/e2e/general/test_correctness_sliding_window.py`_
- **2026-07-18** [`e94243893d`](https://github.com/vllm-project/vllm/commit/e94243893d) [#46832](https://github.com/vllm-project/vllm/pull/46832)
  [ROCm][DSv3.2][Perf] Cap sparse MLA decode KV-splits with a work-per-split heuristic (#46832)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-07-18** [`f12b80c6ef`](https://github.com/vllm-project/vllm/commit/f12b80c6ef) [#43979](https://github.com/vllm-project/vllm/pull/43979)
  [ROCm][Bugfix] Fix GPT-OSS Quark MXFP4 MoE loading - emulation buffer not block-aligned (#43979)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-07-17** [`cc25f028b7`](https://github.com/vllm-project/vllm/commit/cc25f028b7) [#46868](https://github.com/vllm-project/vllm/pull/46868)
  [Loader] Improve InstantTensor loading (#46868)
  _Files: `requirements/test/cpu.txt`, `requirements/test/cuda.in`, `requirements/test/cuda.txt`, `requirements/test/nightly-torch.txt` _+5 more__
- **2026-07-17** [`efed8a1e83`](https://github.com/vllm-project/vllm/commit/efed8a1e83) [#48788](https://github.com/vllm-project/vllm/pull/48788)
  [ROCm][Perf][DSV4] Improve sparse decode reduction occupancy on gfx950 (#48788)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-07-17** [`867ff69733`](https://github.com/vllm-project/vllm/commit/867ff69733) [#48772](https://github.com/vllm-project/vllm/pull/48772)
  [CI] Gate non-default release wheel builds (#48772)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/generate-and-upload-nightly-index.sh`, `.buildkite/scripts/upload-rocm-wheels.sh`, `docs/contributing/ci/nightly_builds.md`_
- **2026-07-16** [`f17be06fbe`](https://github.com/vllm-project/vllm/commit/f17be06fbe) [#48143](https://github.com/vllm-project/vllm/pull/48143)
  [Perf] Optimize `clamp` to `clamp_` (#48143)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/deepseek_v4/sparse_mla.py`, `vllm/v1/attention/backends/mamba_attn.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py` _+3 more__
- **2026-07-16** [`2cab53ddee`](https://github.com/vllm-project/vllm/commit/2cab53ddee) [#42749](https://github.com/vllm-project/vllm/pull/42749)
  [Model][Hardware][AMD]: Part 1/2 -> Enable e2e QK Norm + RoPE + KV Cache runtime fusion for Qwen3-30B-A3B on ROCM_AITER_FA, and ROCM_AITER_UNIFIED_ATTN (#42749)
  _Files: `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`, `tests/quantization/test_fp8.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/qk_norm_rope_fusion.py` _+11 more__
- **2026-07-16** [`626c90b2d5`](https://github.com/vllm-project/vllm/commit/626c90b2d5) [#48500](https://github.com/vllm-project/vllm/pull/48500)
  [Refactor] Move fla to third party (#48500)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.github/CODEOWNERS` _+38 more__
- **2026-07-16** [`7d56fe2adc`](https://github.com/vllm-project/vllm/commit/7d56fe2adc) [#48015](https://github.com/vllm-project/vllm/pull/48015)
  [ROCm][CI] Avoid HIP init at config time via lazy aiter import in Quark OCP-MX (#48015)
  _Files: `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`_
- **2026-07-16** [`b8168e33e0`](https://github.com/vllm-project/vllm/commit/b8168e33e0) [#46275](https://github.com/vllm-project/vllm/pull/46275)
  [ROCm][Perf][DSV4] Enable split sparse decode on gfx942 (#46275)
  _Files: `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-07-16** [`7dc2698632`](https://github.com/vllm-project/vllm/commit/7dc2698632) [#48784](https://github.com/vllm-project/vllm/pull/48784)
  [ROCm][CI] Set "highest" matmul precision for reference hf_runner in `test_bert_for_masked_lm` (#48784)
  _Files: `tests/models/language/pooling/test_token_classification.py`_
- **2026-07-16** [`6a9f24aa8c`](https://github.com/vllm-project/vllm/commit/6a9f24aa8c) [#48764](https://github.com/vllm-project/vllm/pull/48764)
  [ROCm][CI] Fix cuda graph mem profile issue (#48764)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-16** [`3c1bc1fc0d`](https://github.com/vllm-project/vllm/commit/3c1bc1fc0d) [#48519](https://github.com/vllm-project/vllm/pull/48519)
  [ROCm][Perf] Optimize sparse attention prefill kernel for DeepSeek-V4 (#48519)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-07-15** [`015b0320de`](https://github.com/vllm-project/vllm/commit/015b0320de) [#48643](https://github.com/vllm-project/vllm/pull/48643)
  Add giuseppegrossi to rocm label auto cc action (#48643)
  _Files: `.github/workflows/issue_autolabel.yml`_
- **2026-07-15** [`eb33ff34dd`](https://github.com/vllm-project/vllm/commit/eb33ff34dd) [#47718](https://github.com/vllm-project/vllm/pull/47718)
  [ROCm][Perf] DSv4 two-stage compressor kernel for HCA prefill (#47718)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`, `vllm/models/deepseek_v4/compressor.py`_
- **2026-07-15** [`49e777cf08`](https://github.com/vllm-project/vllm/commit/49e777cf08) [#48773](https://github.com/vllm-project/vllm/pull/48773)
  [CI][ROCm] Retry failed Docker build steps once (#48773)
  _Files: `.buildkite/hardware_tests/amd.yaml`_
- **2026-07-15** [`1d99f0f421`](https://github.com/vllm-project/vllm/commit/1d99f0f421) [#47770](https://github.com/vllm-project/vllm/pull/47770)
  [ROCm][BugFix] Triton W4A16 handling for GPTQ/AutoGPTQ qzeros layout  (#47770)
  _Files: `tests/kernels/quantization/test_triton_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`_
- **2026-07-15** [`0885b51981`](https://github.com/vllm-project/vllm/commit/0885b51981) [#48746](https://github.com/vllm-project/vllm/pull/48746)
  [CI][ROCm] Stabilize ci_base hash calculation and image handoff (#48746)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/rocm/build-test-image.sh`_
- **2026-07-15** [`05eed72aec`](https://github.com/vllm-project/vllm/commit/05eed72aec) [#48526](https://github.com/vllm-project/vllm/pull/48526)
  [ROCm] Re-enable cudagraph memory profiling, captured on the current stream (#48526)
  _Files: `vllm/distributed/parallel_state.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-15** [`7aab6e2684`](https://github.com/vllm-project/vllm/commit/7aab6e2684) [#48688](https://github.com/vllm-project/vllm/pull/48688)
  [ROCm][Bugfix] Enable the fp32 head_dtype torch.mm fast path on ROCm (#48688)
  _Files: `tests/v1/sample/test_head_dtype.py`, `vllm/model_executor/layers/logits_processor.py`_
- **2026-07-15** [`d119beb1b9`](https://github.com/vllm-project/vllm/commit/d119beb1b9) [#48159](https://github.com/vllm-project/vllm/pull/48159)
  [ROCm] Add tuned selective_state_update config for AMD MI350 (#48159)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI350_OAM,cache_dtype=float16.json`, `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI350_OAM,cache_dtype=float32.json`_
- **2026-07-15** [`adce068118`](https://github.com/vllm-project/vllm/commit/adce068118) [#48676](https://github.com/vllm-project/vllm/pull/48676)
  [ROCm][CI] fix test_common.py (#48676)
  _Files: `tests/conftest.py`, `vllm/model_executor/models/hyperclovax.py`_
- **2026-07-15** [`b6770d7b54`](https://github.com/vllm-project/vllm/commit/b6770d7b54) [#48527](https://github.com/vllm-project/vllm/pull/48527)
  [ROCm] Run init test engine in-process to avoid KV-cache OOM (#48527)
  _Files: `tests/models/test_initialization.py`_
- **2026-07-15** [`96d2ceda4b`](https://github.com/vllm-project/vllm/commit/96d2ceda4b) [#44549](https://github.com/vllm-project/vllm/pull/44549)
  [Security] Replace diskcache to eliminate pickle deserialization (#44549)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+3 more__
- **2026-07-15** [`3ad85e0de4`](https://github.com/vllm-project/vllm/commit/3ad85e0de4) [#48387](https://github.com/vllm-project/vllm/pull/48387)
  [CI][AMD] Configure MI300 tests for native execution without DinD (#48387)
  _Files: `.buildkite/lm-eval-harness/configs/Meta-Llama-4-Maverick-17B-128E-Instruct-FP8.yaml`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh` _+19 more__
- **2026-07-15** [`6e073440b1`](https://github.com/vllm-project/vllm/commit/6e073440b1) [#47330](https://github.com/vllm-project/vllm/pull/47330)
  [ROCm][CI] Remove mxfp4 test skips after `amd-quark` 0.12 release (#47330)
  _Files: `requirements/rocm.txt`, `tests/evals/gsm8k/test_gsm8k_correctness.py`, `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/lora/test_gptoss_tp.py` _+1 more__
- **2026-07-14** [`0f0f28b537`](https://github.com/vllm-project/vllm/commit/0f0f28b537) [#48654](https://github.com/vllm-project/vllm/pull/48654)
  [Bugfix][CI] Fix test_head_dtype quant_method test on ROCm (#48654)
  _Files: `tests/v1/sample/test_head_dtype.py`_
- **2026-07-14** [`05d4f8bba3`](https://github.com/vllm-project/vllm/commit/05d4f8bba3) [#48647](https://github.com/vllm-project/vllm/pull/48647)
  [ROCm][CI] fix flashinfer import check (#48647)
  _Files: `tests/v1/attention/test_flashinfer_dcp_spec_reorder.py`_
- **2026-07-14** [`7ffb98e248`](https://github.com/vllm-project/vllm/commit/7ffb98e248) [#48373](https://github.com/vllm-project/vllm/pull/48373)
  [ROCm] Retune MI355 selective_state_update float32 config on the unified effective_batch grid (#48373)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI355_OAM,cache_dtype=float32.json`_
- **2026-07-14** [`ca3618bc69`](https://github.com/vllm-project/vllm/commit/ca3618bc69) [#45437](https://github.com/vllm-project/vllm/pull/45437)
  [Doc] Sync four function docstrings with their signatures (#45437)
  _Files: `vllm/_aiter_ops.py`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`_
- **2026-07-14** [`31be872f55`](https://github.com/vllm-project/vllm/commit/31be872f55) [#48372](https://github.com/vllm-project/vllm/pull/48372)
  [ROCm] Retune MI355 selective_state_update float16 config on the unified effective_batch grid (#48372)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI355_OAM,cache_dtype=float16.json`_
- **2026-07-14** [`95aab66e95`](https://github.com/vllm-project/vllm/commit/95aab66e95) [#47984](https://github.com/vllm-project/vllm/pull/47984)
  [ROCm][MiniMax-M3][Spec Decode] Support speculative decode with AITER sparse PA (#47984)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`_
- **2026-07-14** [`dcf4072da9`](https://github.com/vllm-project/vllm/commit/dcf4072da9) [#45000](https://github.com/vllm-project/vllm/pull/45000)
  [Perf][ROCm] Fix GDN KKT warmup regression on RDNA by avoiding fp32 tl.dot (#45000)
  _Files: `vllm/model_executor/layers/fla/ops/chunk_scaled_dot_kkt.py`_
- **2026-07-14** [`382bbd5144`](https://github.com/vllm-project/vllm/commit/382bbd5144) [#40977](https://github.com/vllm-project/vllm/pull/40977)
  [ROCm][Kernel] Add HybridW4A16LinearKernel: Triton prefill + HIP skinny decode (#40977)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_rdna_hybrid_w4a16_gemm.py`, `csrc/rocm/ops.h`, `csrc/rocm/skinny_gemms_int4.cu` _+7 more__
- **2026-07-14** [`b50ef9c6ed`](https://github.com/vllm-project/vllm/commit/b50ef9c6ed) [#44849](https://github.com/vllm-project/vllm/pull/44849)
  [ROCm][MiniMax-M2] Dispatch fused QK-norm + AllReduce via AITER (#44849)
  _Files: `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`_
- **2026-07-14** [`c4f5cd60da`](https://github.com/vllm-project/vllm/commit/c4f5cd60da) [#47327](https://github.com/vllm-project/vllm/pull/47327)
  [1/N] Add dense MHA path for sparse MLA short sequences (#47327)
  _Files: `benchmarks/attention_benchmarks/benchmark.py`, `benchmarks/attention_benchmarks/common.py`, `benchmarks/attention_benchmarks/configs/mla_sparse_mha_vs_mqa.yaml`, `benchmarks/attention_benchmarks/mla_runner.py` _+17 more__
- **2026-07-13** [`18c4067a54`](https://github.com/vllm-project/vllm/commit/18c4067a54) [#48513](https://github.com/vllm-project/vllm/pull/48513)
  [ROCm][CI] Unblock `AMD: Language Models Test (Extended Pooling)` (#48513)
  _Files: `tests/models/language/pooling/test_token_classification.py`_
- **2026-07-13** [`9427c45386`](https://github.com/vllm-project/vllm/commit/9427c45386) [#48258](https://github.com/vllm-project/vllm/pull/48258)
  [ROCm][CI] Transformers: pass only one of input_ids/inputs_embeds (#48258)
  _Files: `vllm/model_executor/models/transformers/base.py`_
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

## Attention  (28 commits)

- **2026-07-20** [`5c9f6557d7`](https://github.com/vllm-project/vllm/commit/5c9f6557d7) [#47641](https://github.com/vllm-project/vllm/pull/47641)
  [Hardware][CPU] Enable granite-4 model on cpu (#47641)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/scripts/hardware_ci/run-cpu-test-arm.sh`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vsx.hpp` _+17 more__
- **2026-07-17** [`5784507da4`](https://github.com/vllm-project/vllm/commit/5784507da4) [#48012](https://github.com/vllm-project/vllm/pull/48012)
  [Attention] Allow selecting a different attention backend per KV-cache group (#48012)
  _Files: `tests/v1/attention/test_backend_per_kind.py`, `tests/v1/e2e/general/test_attention_backend_per_kind.py`, `vllm/config/attention.py`, `vllm/v1/attention/selector.py`_
- **2026-07-17** [`ce2aecc4dc`](https://github.com/vllm-project/vllm/commit/ce2aecc4dc) [#48417](https://github.com/vllm-project/vllm/pull/48417)
  [Performance] Use CuTe-DSL for FlashInfer MXFP4 quantization (#48417)
  _Files: `vllm/model_executor/kernels/linear/mxfp4/flashinfer.py`, `vllm/utils/flashinfer.py`_
- **2026-07-17** [`ce4bdcbda4`](https://github.com/vllm-project/vllm/commit/ce4bdcbda4) [#48855](https://github.com/vllm-project/vllm/pull/48855)
  [Bugfix] Enable FlashAttention MLA prefill for Mistral Small 4 head dims (#48855)
  _Files: `docs/design/attention_backends.md`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/v1/attention/backends/mla/prefill/flash_attn.py`_
- **2026-07-17** [`d5b1ec2684`](https://github.com/vllm-project/vllm/commit/d5b1ec2684) [#48828](https://github.com/vllm-project/vllm/pull/48828)
  [XPU] allow forcing flash attn for mm_prefix (#48828)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-17** [`17fdd42100`](https://github.com/vllm-project/vllm/commit/17fdd42100) [#48251](https://github.com/vllm-project/vllm/pull/48251)
  [Bugfix][Attention] Preserve post-load tensors across weight reloads (#48251)
  _Files: `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_mla_backends.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-07-17** [`fe784ff22e`](https://github.com/vllm-project/vllm/commit/fe784ff22e) [#48582](https://github.com/vllm-project/vllm/pull/48582)
  [M3] Improve indexer for long-context decode (sm100) (#48582)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `vllm/cute_utils/__init__.py`, `vllm/cute_utils/cvt.py`, `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/kernel_kkt_inv_uw.py` _+3 more__
- **2026-07-16** [`67f9046e4a`](https://github.com/vllm-project/vllm/commit/67f9046e4a) [#48642](https://github.com/vllm-project/vllm/pull/48642)
  [Bugfix] Sparse MLA: enable fp8_ds_mla dense prefill (#48642)
  _Files: `benchmarks/kernels/bench_cp_gather_fp8.py`, `csrc/cache.h`, `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/ops.h` _+9 more__
- **2026-07-16** [`f61163e6c7`](https://github.com/vllm-project/vllm/commit/f61163e6c7) [#48858](https://github.com/vllm-project/vllm/pull/48858)
  [Model] Add Hopper FA4 relative attention for Inkling (#48858)
  _Files: `tests/models/inkling/test_fa4_rel_attention.py`, `vllm/models/inkling/nvidia/ops/fa4_rel_attention.py`_
- **2026-07-16** [`251f7e478e`](https://github.com/vllm-project/vllm/commit/251f7e478e) [#48822](https://github.com/vllm-project/vllm/pull/48822)
  [Model] Add PW CUDA graph support for Inkling [2/N] (#48822)
  _Files: `tests/models/inkling/test_contract_validation.py`, `tests/v1/cudagraph/test_breakable_cudagraph.py`, `vllm/config/vllm.py`, `vllm/models/inkling/nvidia/attention.py` _+6 more__
- **2026-07-16** [`7cd1d57b74`](https://github.com/vllm-project/vllm/commit/7cd1d57b74) [#47442](https://github.com/vllm-project/vllm/pull/47442)
  [CI/Build][Docker] Bump nvidia-cutlass-dsl to 4.6.0 and drop packaging workarounds (#47442)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `docker/Dockerfile`, `requirements/cuda.txt`, `requirements/test/cuda.txt` _+3 more__
- **2026-07-16** [`8bfd683901`](https://github.com/vllm-project/vllm/commit/8bfd683901) [#48787](https://github.com/vllm-project/vllm/pull/48787)
  [Spec Decode] Add kv_cache_dtype to speculative_config to control separately from target (#48787)
  _Files: `vllm/config/speculative.py`, `vllm/engine/arg_utils.py`, `vllm/v1/spec_decode/llm_base_proposer.py`, `vllm/v1/worker/gpu/spec_decode/dflash/utils.py` _+2 more__
- **2026-07-16** [`ba47bb5be1`](https://github.com/vllm-project/vllm/commit/ba47bb5be1) [#47669](https://github.com/vllm-project/vllm/pull/47669)
  Bump flashinfer version to 0.6.14 (#47669)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `setup.py` _+2 more__
- **2026-07-16** [`915dffaa5f`](https://github.com/vllm-project/vllm/commit/915dffaa5f) [#47060](https://github.com/vllm-project/vllm/pull/47060)
  [Attention] Mirror Triton KV dtype checks in MLA (#47060)
  _Files: `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-07-16** [`0becb7486b`](https://github.com/vllm-project/vllm/commit/0becb7486b) [#47309](https://github.com/vllm-project/vllm/pull/47309)
  [BugFix][MLA] Support kv_cache_dtype_skip_layers for MLA attention (#47309)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-07-15** [`ecf4aa5ce2`](https://github.com/vllm-project/vllm/commit/ecf4aa5ce2) [#48167](https://github.com/vllm-project/vllm/pull/48167)
  [Bugfix] Fix FlashInfer non-causal draft attention (DFlash/DSpark) on Blackwell (#48167)
  _Files: `tests/v1/spec_decode/test_dflash_causality.py`, `tools/pre_commit/generate_attention_backend_docs.py`, `vllm/model_executor/models/qwen3_dflash.py`, `vllm/platforms/cuda.py` _+8 more__
- **2026-07-15** [`6472131298`](https://github.com/vllm-project/vllm/commit/6472131298) [#48379](https://github.com/vllm-project/vllm/pull/48379)
  [Bugfix] Set kv_quant_mode on the generic MLA KV-cache spec (#48379)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-07-15** [`37aa52821d`](https://github.com/vllm-project/vllm/commit/37aa52821d) [#48174](https://github.com/vllm-project/vllm/pull/48174)
  Build with ABI stable FlashMLA (#48174)
  _Files: `cmake/external_projects/flashmla.cmake`_
- **2026-07-15** [`7e950521b3`](https://github.com/vllm-project/vllm/commit/7e950521b3) [#48428](https://github.com/vllm-project/vllm/pull/48428)
  fix: size FlashInfer prefill workspace to batch head footprint (#48428)
  _Files: `vllm/v1/attention/backends/flashinfer.py`_
- **2026-07-14** [`313d01f507`](https://github.com/vllm-project/vllm/commit/313d01f507) [#48631](https://github.com/vllm-project/vllm/pull/48631)
  [CI][Bugfix] Fix FlashAttention reported MLA dimension support (#48631)
  _Files: `docs/design/attention_backends.md`, `tests/v1/attention/test_mla_prefill_selector.py`, `tools/pre_commit/generate_attention_backend_docs.py`, `vllm/v1/attention/backends/mla/prefill/base.py` _+1 more__
- **2026-07-14** [`b2f7d2560a`](https://github.com/vllm-project/vllm/commit/b2f7d2560a) [#48520](https://github.com/vllm-project/vllm/pull/48520)
  [Bugfix] Make MLA+SWA check the layer's backend, not the model config (#48520)
  _Files: `vllm/model_executor/layers/attention/attention.py`_
- **2026-07-14** [`50ac1c7bab`](https://github.com/vllm-project/vllm/commit/50ac1c7bab) [#45781](https://github.com/vllm-project/vllm/pull/45781)
  [Misc] Rename VLLM_TRITON_ATTN_USE_TD to VLLM_TRITON_USE_TD (#45781)
  _Files: `vllm/envs.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-07-13** [`7dc447dda7`](https://github.com/vllm-project/vllm/commit/7dc447dda7) [#47568](https://github.com/vllm-project/vllm/pull/47568)
  Added sliding window attention support for qwen-eagle3 architecture (#47568)
  _Files: `vllm/model_executor/models/qwen3.py`, `vllm/model_executor/models/qwen3_eagle3.py`_
- **2026-07-13** [`7fc97042c3`](https://github.com/vllm-project/vllm/commit/7fc97042c3) [#48180](https://github.com/vllm-project/vllm/pull/48180)
  Add DCP + Eagle support for Tokenspeed MLA backends (#48180)
  _Files: `docs/design/attention_backends.md`, `requirements/cuda.txt`, `tests/kernels/attention/test_use_trtllm_attention.py`, `tests/v1/attention/test_flashinfer_dcp_spec_reorder.py` _+4 more__
- **2026-07-13** [`26587f9519`](https://github.com/vllm-project/vllm/commit/26587f9519) [#48261](https://github.com/vllm-project/vllm/pull/48261)
  [BugFix][ModelRunner V2] Fix stale attn metadata in speculator prefill cudagraph capture (#48261)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/cudagraph_utils.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py` _+3 more__
- **2026-07-13** [`56a357ed33`](https://github.com/vllm-project/vllm/commit/56a357ed33) [#48256](https://github.com/vllm-project/vllm/pull/48256)
  [Bugfix][KV Cache] Don't route uniform-page-size MLA+SWA models into DeepseekV4 packing (#48256)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-07-13** [`75fe92a316`](https://github.com/vllm-project/vllm/commit/75fe92a316) [#48064](https://github.com/vllm-project/vllm/pull/48064)
  [Distributed][Perf] Enable FlashInfer MNNVL allreduce RMS quant fusion (#48064)
  _Files: `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-07-13** [`05fa8183a6`](https://github.com/vllm-project/vllm/commit/05fa8183a6) [#46090](https://github.com/vllm-project/vllm/pull/46090)
  [CPU][Spec Decode] Support DFlash speculative decoding for GDN models on CPU (#46090)
  _Files: `csrc/cpu/sgl-kernels/fla.cpp`, `csrc/cpu/torch_bindings.cpp`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py` _+1 more__

## MoE / Expert Parallel  (26 commits)

- **2026-07-20** [`df13b5aef5`](https://github.com/vllm-project/vllm/commit/df13b5aef5) [#47122](https://github.com/vllm-project/vllm/pull/47122)
  [XPU] [MoE] add quant input when prepare for fusedmoe (#47122)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-07-19** [`b6ff8a2f50`](https://github.com/vllm-project/vllm/commit/b6ff8a2f50) [#46570](https://github.com/vllm-project/vllm/pull/46570)
  [Core] Add MRV2 virtual-batch PCP for MLA (#46570)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`, `tests/evals/gsm8k/configs/models-pcp.txt` _+35 more__
- **2026-07-18** [`c233d90aa8`](https://github.com/vllm-project/vllm/commit/c233d90aa8) [#48496](https://github.com/vllm-project/vllm/pull/48496)
  Remove even more unnecessary `load_weights` methods (#48496)
  _Files: `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/aria.py`, `vllm/model_executor/models/bailing_moe.py`, `vllm/model_executor/models/bloom.py` _+40 more__
- **2026-07-18** [`da64db78b9`](https://github.com/vllm-project/vllm/commit/da64db78b9) [#48759](https://github.com/vllm-project/vllm/pull/48759)
  [LoRA] Optimize TrtLlmLoRAExperts (#48759)
  _Files: `vllm/model_executor/layers/fused_moe/experts/lora_experts_mixin.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py`_
- **2026-07-18** [`425c4eafb0`](https://github.com/vllm-project/vllm/commit/425c4eafb0) [#48641](https://github.com/vllm-project/vllm/pull/48641)
  [Sampler] Stop upcasting logits to fp32 in apply_sampling_params (#48641)
  _Files: `tests/v1/sample/test_topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/sample/ops/topk_topp_triton.py`, `vllm/v1/worker/gpu/sample/logit_bias.py` _+1 more__
- **2026-07-18** [`02c01f442b`](https://github.com/vllm-project/vllm/commit/02c01f442b) [#48990](https://github.com/vllm-project/vllm/pull/48990)
  [Model] Use standard ModelOpt config for Inkling NVFP4 (#48990)
  _Files: `tests/config/test_model_arch_config.py`, `tests/models/inkling/test_moe_weight_layout.py`, `vllm/models/inkling/nvfp4.py`, `vllm/models/inkling/nvidia/model.py` _+3 more__
- **2026-07-17** [`b5433b6f50`](https://github.com/vllm-project/vllm/commit/b5433b6f50) [#48660](https://github.com/vllm-project/vllm/pull/48660)
  [Perf] Optimize dsv4 routing using specialized kernel, 2.94% E2E TPOT improvement (#48660)
  _Files: `csrc/libtorch_stable/moe/topk_softplus_sqrt_kernels.cu`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `vllm/model_executor/layers/fused_moe/router/dsv4_topk.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-07-17** [`c4dd6d78fd`](https://github.com/vllm-project/vllm/commit/c4dd6d78fd) [#48849](https://github.com/vllm-project/vllm/pull/48849)
  Fix: Restore data_parallel_size > 1 for use_sequence_parallel_moe (#48849)
  _Files: `vllm/config/parallel.py`_
- **2026-07-17** [`69d4f5ef63`](https://github.com/vllm-project/vllm/commit/69d4f5ef63) [#46213](https://github.com/vllm-project/vllm/pull/46213)
  [Bugfix][Multimodal] Fix Qwen3-Omni use_audio_in_video with mixed image/video inputs (#46213)
  _Files: `tests/models/multimodal/processing/test_qwen2_5_omni_embed.py`, `tests/v1/worker/test_encoder_runner.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py` _+4 more__
- **2026-07-17** [`f3e9497e92`](https://github.com/vllm-project/vllm/commit/f3e9497e92) [#48884](https://github.com/vllm-project/vllm/pull/48884)
  [Model] Add Inkling LoRA support [4/N] (#48884)
  _Files: `tests/models/inkling/test_moe_weight_layout.py`, `vllm/config/lora.py`, `vllm/engine/arg_utils.py`, `vllm/lora/layers/fused_moe.py` _+8 more__
- **2026-07-16** [`c95c663049`](https://github.com/vllm-project/vllm/commit/c95c663049) [#48538](https://github.com/vllm-project/vllm/pull/48538)
  [Quant] Add `nvfp4_per_token` online MoE quantization (#48538)
  _Files: `tests/quantization/test_online.py`, `vllm/config/quantization.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py` _+3 more__
- **2026-07-16** [`d08eebad16`](https://github.com/vllm-project/vllm/commit/d08eebad16) [#47156](https://github.com/vllm-project/vllm/pull/47156)
  [Perf][MoE] Write FlashInfer combine into final output (#47156)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_one_sided.py`_
- **2026-07-16** [`85e296950c`](https://github.com/vllm-project/vllm/commit/85e296950c) [#47973](https://github.com/vllm-project/vllm/pull/47973)
  BF16x3 router GEMM (#47973)
  _Files: `tests/kernels/test_bf16x3_router_gemm_cutedsl.py`, `vllm/config/kernel.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/fused_moe/router/bf16x3_router_gemm_cutedsl.py` _+1 more__
- **2026-07-16** [`6570c9800c`](https://github.com/vllm-project/vllm/commit/6570c9800c) [#48799](https://github.com/vllm-project/vllm/pull/48799)
  [Model] Add Inkling model support [1/N] (#48799)
  _Files: `.gitignore`, `CMakeLists.txt`, `cmake/external_projects/tml_fa4.cmake`, `requirements/cuda.txt` _+91 more__
- **2026-07-16** [`5de1add806`](https://github.com/vllm-project/vllm/commit/5de1add806) [#48451](https://github.com/vllm-project/vllm/pull/48451)
  [feature]Add int4 quantization support for emulation moe backend (#48451)
  _Files: `tests/kernels/quantization/test_int4_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/int4_emulation_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` _+5 more__
- **2026-07-15** [`2dab187f75`](https://github.com/vllm-project/vllm/commit/2dab187f75) [#47463](https://github.com/vllm-project/vllm/pull/47463)
  [Perf] Optimize `fused_topk_bias` for DSv4, 1.5~2x kernel performance improvement (#47463)
  _Files: `csrc/libtorch_stable/moe/topk_softplus_sqrt_kernels.cu`, `tests/kernels/moe/test_topk_softplus_sqrt.py`, `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-07-15** [`4238b011a7`](https://github.com/vllm-project/vllm/commit/4238b011a7) [#47881](https://github.com/vllm-project/vllm/pull/47881)
  [Feature] Migrate moe sp support to non-torch compiled path for GLM5.2 (#47881)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/model.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-07-15** [`2bd8957627`](https://github.com/vllm-project/vllm/commit/2bd8957627) [#46880](https://github.com/vllm-project/vllm/pull/46880)
  [Bugfix][NVFP4 MoE] Pad gated intermediate to 64 for FlashInfer TRT-LLM shuffle (M%128) (#46880)
  _Files: `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`_
- **2026-07-15** [`fdf2cf66d3`](https://github.com/vllm-project/vllm/commit/fdf2cf66d3) [#48632](https://github.com/vllm-project/vllm/pull/48632)
  [LoRA][1/N] Integrate flashinfer MoE LoRA for BF16 model (#48632)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-07-15** [`f7aadae5e5`](https://github.com/vllm-project/vllm/commit/f7aadae5e5) [#48385](https://github.com/vllm-project/vllm/pull/48385)
  add pad-aware reduce path (#48385)
  _Files: `csrc/libtorch_stable/dispatch_utils.h`, `csrc/libtorch_stable/moe/moe_align_sum_kernels.cu`, `csrc/libtorch_stable/moe/moe_ops.h`, `csrc/libtorch_stable/moe/torch_bindings.cpp` _+3 more__
- **2026-07-14** [`0762f2afeb`](https://github.com/vllm-project/vllm/commit/0762f2afeb) [#42562](https://github.com/vllm-project/vllm/pull/42562)
  [Perf][Feat] Add generic cuteDSL LL BF16 router (GEMM) (#42562)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/test_ll_bf16_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/__init__.py`, `vllm/model_executor/kernels/linear/cute_dsl/_ll_bf16_dotprod.py` _+4 more__
- **2026-07-14** [`9e289c553c`](https://github.com/vllm-project/vllm/commit/9e289c553c) [#44462](https://github.com/vllm-project/vllm/pull/44462)
  up FI fp8 moe topk to 32 (#44462)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`_
- **2026-07-13** [`21472f32ea`](https://github.com/vllm-project/vllm/commit/21472f32ea) [#48287](https://github.com/vllm-project/vllm/pull/48287)
  add pad-aware swiglu limit kernel (#48287)
  _Files: `vllm/model_executor/layers/fused_moe/activation.py`, `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`, `vllm/model_executor/layers/fused_moe/modular_kernel.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-07-13** [`9a21f0d1a3`](https://github.com/vllm-project/vllm/commit/9a21f0d1a3) [#44863](https://github.com/vllm-project/vllm/pull/44863)
  [BugFix] Initialize model_config for Qwen3-VL MoE (#44863)
  _Files: `vllm/model_executor/models/qwen3_vl_moe.py`_
- **2026-07-13** [`36484e464a`](https://github.com/vllm-project/vllm/commit/36484e464a) [#48429](https://github.com/vllm-project/vllm/pull/48429)
  [BugFix] Restore full tokens for Qwen MTP When MoE SP (#48429)
  _Files: `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_next_mtp.py`_
- **2026-07-13** [`2595d5cebc`](https://github.com/vllm-project/vllm/commit/2595d5cebc) [#48350](https://github.com/vllm-project/vllm/pull/48350)
  [Model] Optimize Qwen3.5 on H20 (#48350)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=256,device_name=NVIDIA_H20.json`_

## Other  (22 commits)

- **2026-07-20** [`818cf61e91`](https://github.com/vllm-project/vllm/commit/818cf61e91) [#49042](https://github.com/vllm-project/vllm/pull/49042)
  [Rust Frontend] Fix macro-based content format detection (#49042)
  _Files: `rust/src/chat/src/renderer/hf/format.rs`, `rust/src/chat/src/renderer/hf/mod.rs`_
- **2026-07-20** [`9459fc6471`](https://github.com/vllm-project/vllm/commit/9459fc6471) [#45989](https://github.com/vllm-project/vllm/pull/45989)
  [Bugfix][RL] Set vLLM config during weight reload (#45989)
  _Files: `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-20** [`dcfebf93f4`](https://github.com/vllm-project/vllm/commit/dcfebf93f4) [#48674](https://github.com/vllm-project/vllm/pull/48674)
  [Bugfix] Fix logprobs token-string collision from SentencePiece space… (#48674)
  _Files: `tests/tokenizers_/test_detokenize.py`, `vllm/tokenizers/detokenizer_utils.py`_
- **2026-07-18** [`d96aee0951`](https://github.com/vllm-project/vllm/commit/d96aee0951) [#48025](https://github.com/vllm-project/vllm/pull/48025)
  [Bugfix] Re-sync parameter tp_rank after process_weights_after_loading (fix replicated / disable_tp weight reload) (#48025)
  _Files: `vllm/model_executor/layers/linear.py`, `vllm/model_executor/model_loader/reload/layerwise.py`, `vllm/model_executor/model_loader/utils.py`_
- **2026-07-17** [`fcd2255d16`](https://github.com/vllm-project/vllm/commit/fcd2255d16) [#37524](https://github.com/vllm-project/vllm/pull/37524)
  [Hardware][GPU] Profiler config additional to increase it scope and annotation details (#37524)
  _Files: `tests/v1/worker/test_gpu_profiler.py`, `vllm/config/profiler.py`, `vllm/v1/worker/gpu_model_runner.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-07-17** [`4c6e2e4b30`](https://github.com/vllm-project/vllm/commit/4c6e2e4b30) [#47516](https://github.com/vllm-project/vllm/pull/47516)
  [XPU][UT]fix _POSSIBLE_KERNELS error on XPU (#47516)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-07-17** [`8502958810`](https://github.com/vllm-project/vllm/commit/8502958810) [#47975](https://github.com/vllm-project/vllm/pull/47975)
  [XPU] support HND layout (#47975)
  _Files: `vllm/platforms/xpu.py`_
- **2026-07-17** [`ee8f36d0b3`](https://github.com/vllm-project/vllm/commit/ee8f36d0b3) [#48881](https://github.com/vllm-project/vllm/pull/48881)
  [Warmup] Show CuTeDSL compilation progress (#48881)
  _Files: `vllm/model_executor/warmup/cutedsl_warmup.py`_
- **2026-07-16** [`cc706b05a5`](https://github.com/vllm-project/vllm/commit/cc706b05a5) [#47707](https://github.com/vllm-project/vllm/pull/47707)
  [Bugfix][Rust Frontend] Detokenizer: avoid leaking prompt on zero-generated-token completions (#47707)
  _Files: `rust/src/tokenizer/src/incremental.rs`_
- **2026-07-16** [`df8a0900df`](https://github.com/vllm-project/vllm/commit/df8a0900df) [#48741](https://github.com/vllm-project/vllm/pull/48741)
  [BugFix] Don't apply weight in batch-invariant RMSNorm when has_weight=False (#48741)
  _Files: `vllm/model_executor/layers/batch_invariant.py`, `vllm/model_executor/layers/layernorm.py`_
- **2026-07-16** [`f95e3f0edb`](https://github.com/vllm-project/vllm/commit/f95e3f0edb) [#44349](https://github.com/vllm-project/vllm/pull/44349)
  [Tests] Gate Step3VL under Transformers v5 (#44349)
  _Files: `tests/models/registry.py`_
- **2026-07-15** [`2fa63e0fff`](https://github.com/vllm-project/vllm/commit/2fa63e0fff) [#48264](https://github.com/vllm-project/vllm/pull/48264)
  [Kernel][Helion] Helion kernel lazy registration (#48264)
  _Files: `scripts/autotune_helion_kernels.py`, `vllm/kernels/helion/__init__.py`, `vllm/kernels/helion/ops/__init__.py`_
- **2026-07-15** [`5811ed6a05`](https://github.com/vllm-project/vllm/commit/5811ed6a05) [#48545](https://github.com/vllm-project/vllm/pull/48545)
  [Test][kv_offload] Fix flaky drain() helper in test_fs_tier.py (#48545)
  _Files: `tests/v1/kv_offload/tiering/test_fs_tier.py`_
- **2026-07-15** [`1b30ae4ca4`](https://github.com/vllm-project/vllm/commit/1b30ae4ca4) [#47873](https://github.com/vllm-project/vllm/pull/47873)
  [Rust Frontend] Fix flaky `tls_handshake_timeout_drops_silent_client` test (#47873)
  _Files: `rust/.config/nextest.toml`, `rust/src/server/src/tls_tests.rs`_
- **2026-07-15** [`313fae3e89`](https://github.com/vllm-project/vllm/commit/313fae3e89) [#48711](https://github.com/vllm-project/vllm/pull/48711)
  [Bugfix] Fix GLM5 config (#48711)
  _Files: `vllm/transformers_utils/config.py`_
- **2026-07-15** [`9dd2e72828`](https://github.com/vllm-project/vllm/commit/9dd2e72828) [#48206](https://github.com/vllm-project/vllm/pull/48206)
  fix flaky multi example connector consistency (#48206)
  _Files: `tests/v1/kv_connector/unit/test_multi_connector.py`_
- **2026-07-15** [`0bd6b85a1f`](https://github.com/vllm-project/vllm/commit/0bd6b85a1f) [#44371](https://github.com/vllm-project/vllm/pull/44371)
  [Bugfix] Preserve unloaded non-persistent buffers during layerwise reload (#44371)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/layerwise.py`, `vllm/model_executor/model_loader/reload/meta.py`, `vllm/model_executor/model_loader/reload/types.py`_
- **2026-07-14** [`c9a788eedc`](https://github.com/vllm-project/vllm/commit/c9a788eedc) [#47595](https://github.com/vllm-project/vllm/pull/47595)
  fix(security): guard lm-format-enforcer regex compile with timeout (#47595)
  _Files: `vllm/v1/structured_output/backend_lm_format_enforcer.py`_
- **2026-07-14** [`af1f036a70`](https://github.com/vllm-project/vllm/commit/af1f036a70) [#48523](https://github.com/vllm-project/vllm/pull/48523)
  [Bugfix] Skip minimax_m3 tool parser tests when Rust extension is absent (#48523)
  _Files: `tests/tool_parsers/test_minimax_m3_tool_parser.py`_
- **2026-07-13** [`62286308c9`](https://github.com/vllm-project/vllm/commit/62286308c9) [#48057](https://github.com/vllm-project/vllm/pull/48057)
  [Misc]  Improve Matryoshka pooling dimensions validation (#48057)
  _Files: `vllm/pooling_params.py`_
- **2026-07-13** [`1be6e937b2`](https://github.com/vllm-project/vllm/commit/1be6e937b2) [#48483](https://github.com/vllm-project/vllm/pull/48483)
  lower memory required for capturing cudagraphs for large cudagraph sizes (#48483)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-13** [`b3cfca996c`](https://github.com/vllm-project/vllm/commit/b3cfca996c) [#48490](https://github.com/vllm-project/vllm/pull/48490)
  [Mypy Fix] Split mypy work (#48490)
  _Files: `tools/pre_commit/mypy.py`_

## Disaggregation / PD  (15 commits)

- **2026-07-20** [`4938d44a3b`](https://github.com/vllm-project/vllm/commit/4938d44a3b) [#47871](https://github.com/vllm-project/vllm/pull/47871)
  [CPU] fixes heterogeneous NIXL KV transfer into CPU_ATTN decode workers (#47871)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/platforms/cpu.py`_
- **2026-07-20** [`37bf988c2f`](https://github.com/vllm-project/vllm/commit/37bf988c2f) [#47295](https://github.com/vllm-project/vllm/pull/47295)
  [XPU][Bugfix] Fix GroupCoordinator device_index (#47295)
  _Files: `vllm/distributed/parallel_state.py`_
- **2026-07-17** [`c4cd2bd544`](https://github.com/vllm-project/vllm/commit/c4cd2bd544) [#46115](https://github.com/vllm-project/vllm/pull/46115)
  [Bugfix] MoRIIO toy P/D proxy: fix DP-rank index aliasing + harden for high-concurrency bursts (#46115)
  _Files: `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`, `tests/v1/kv_connector/unit/test_moriio_proxy_routing.py`_
- **2026-07-17** [`fb1d8ccaf5`](https://github.com/vllm-project/vllm/commit/fb1d8ccaf5) [#48042](https://github.com/vllm-project/vllm/pull/48042)
  [rl] Stateful Trainer Send: New Abstractions [1/N]  (#48042)
  _Files: `tests/distributed/test_weight_transfer.py`, `tools/pre_commit/check_forbidden_imports.py`, `vllm/distributed/weight_transfer/__init__.py`, `vllm/distributed/weight_transfer/base.py` _+3 more__
- **2026-07-16** [`971dac2caa`](https://github.com/vllm-project/vllm/commit/971dac2caa) [#47495](https://github.com/vllm-project/vllm/pull/47495)
  [Bugfix][KV-transfer] MoRIIO: retry RDMA send-queue-full backpressure instead of failing the read (#47495)
  _Files: `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`_
- **2026-07-16** [`a317bc5739`](https://github.com/vllm-project/vllm/commit/a317bc5739) [#48717](https://github.com/vllm-project/vllm/pull/48717)
  [Misc][Nixl] Unify `_logical_to_remote_kernel_block_ids` (#48717)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py` _+1 more__
- **2026-07-16** [`9f8cbfd8eb`](https://github.com/vllm-project/vllm/commit/9f8cbfd8eb) [#48209](https://github.com/vllm-project/vllm/pull/48209)
  Vectorize prep xfer list creation (#48209)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-07-15** [`3034c8d389`](https://github.com/vllm-project/vllm/commit/3034c8d389) [#42310](https://github.com/vllm-project/vllm/pull/42310)
  [CI][PD] Add optional/nightly DSv4 Disaggregated eval (#42310)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_
- **2026-07-15** [`66b6c684ab`](https://github.com/vllm-project/vllm/commit/66b6c684ab) [#48125](https://github.com/vllm-project/vllm/pull/48125)
  [PD][Bugfix] Fix validation of cache shape for attn backends enforcing different `kernel_block_size` (#48125)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`_
- **2026-07-14** [`520a20ba4e`](https://github.com/vllm-project/vllm/commit/520a20ba4e) [#45222](https://github.com/vllm-project/vllm/pull/45222)
  [Bugfix] MoRIIO toy P/D proxy: add /health (#45222)
  _Files: `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`, `tests/v1/kv_connector/unit/test_moriio_toy_proxy_server.py`_
- **2026-07-14** [`32aef44388`](https://github.com/vllm-project/vllm/commit/32aef44388) [#48411](https://github.com/vllm-project/vllm/pull/48411)
  [Bugfix] Include inline per-token-head scales in offloaded page transfer width (#48411)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`, `vllm/v1/kv_cache_interface.py`_
- **2026-07-14** [`7a74a9662b`](https://github.com/vllm-project/vllm/commit/7a74a9662b) [#47021](https://github.com/vllm-project/vllm/pull/47021)
  [NIXL] Avoid reading expired blocks in bidirectional turn-2 read (#47021)
  _Files: `docs/design/nixl_kv_cache_lease.md`, `tests/v1/kv_connector/unit/test_bidirectional_kv_transfer.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+6 more__
- **2026-07-13** [`8ac8375270`](https://github.com/vllm-project/vllm/commit/8ac8375270) [#47782](https://github.com/vllm-project/vllm/pull/47782)
  [Core] Preserve Marconi caching with selective hybrid cache retention (#47782)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_prefix_caching.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`, `vllm/v1/core/kv_cache_coordinator.py` _+5 more__
- **2026-07-13** [`43c8cbf79b`](https://github.com/vllm-project/vllm/commit/43c8cbf79b) [#47423](https://github.com/vllm-project/vllm/pull/47423)
  [EC Connector] CPU Offloading EC Connector (#47423)
  _Files: `tests/v1/ec_connector/unit/cpu/scheduler/test_embedding_cache.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_scheduler.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_step_tracker.py`, `tests/v1/ec_connector/unit/cpu/test_connector.py` _+14 more__
- **2026-07-13** [`9e57de7197`](https://github.com/vllm-project/vllm/commit/9e57de7197) [#40714](https://github.com/vllm-project/vllm/pull/40714)
  [CPU] Create Proper Numa topology for s390x (#40714)
  _Files: `docker/Dockerfile.s390x`, `requirements/common.txt`, `vllm/distributed/device_communicators/cpu_communicator.py`, `vllm/platforms/cpu.py` _+3 more__

## Serving / API  (14 commits)

- **2026-07-20** [`530ee36a0d`](https://github.com/vllm-project/vllm/commit/530ee36a0d) [#49144](https://github.com/vllm-project/vllm/pull/49144)
  fix(openai): reject non-numeric logprobs with 400 instead of 500 (#49144)
  _Files: `tests/entrypoints/openai/chat_completion/test_chat_error.py`, `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-07-20** [`d835ad572c`](https://github.com/vllm-project/vllm/commit/d835ad572c) [#49111](https://github.com/vllm-project/vllm/pull/49111)
  [Bugfix][Rust Frontend] Map missing prompt logprobs for single-token prompts in chat and raw generate (#49111)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/completions.rs`, `rust/src/server/src/routes/openai/utils/logprobs.rs`_
- **2026-07-20** [`c01618fdc8`](https://github.com/vllm-project/vllm/commit/c01618fdc8) [#48930](https://github.com/vllm-project/vllm/pull/48930)
  [Rust][Benchmark] Integrate `vllm-bench` to `vllm-rs` & `vllm` CLI (#48930)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/bench/src/cli.rs`, `rust/src/bench/src/config.rs` _+8 more__
- **2026-07-19** [`e6d1310b2a`](https://github.com/vllm-project/vllm/commit/e6d1310b2a) [#48984](https://github.com/vllm-project/vllm/pull/48984)
  [Bugfix] Reject removed pooling parameters (#48984)
  _Files: `tests/test_pooling_params.py`, `vllm/config/pooler.py`, `vllm/entrypoints/pooling/base/protocol.py`, `vllm/entrypoints/pooling/classify/protocol.py` _+5 more__
- **2026-07-18** [`29c0ec4d63`](https://github.com/vllm-project/vllm/commit/29c0ec4d63) [#43164](https://github.com/vllm-project/vllm/pull/43164)
  [ci] Move 3 entrypoints tests to h200_35gb queue (#43164)
  _Files: `.buildkite/test_areas/entrypoints.yaml`, `tests/entrypoints/openai/responses/test_parsable_context.py`_
- **2026-07-17** [`fae543015c`](https://github.com/vllm-project/vllm/commit/fae543015c) [#48829](https://github.com/vllm-project/vllm/pull/48829)
  [Frontend]Flatten beam-search beams with itertools.chain instead of sum (#48829)
  _Files: `vllm/entrypoints/generate/beam_search/offline.py`_
- **2026-07-17** [`9354f22204`](https://github.com/vllm-project/vllm/commit/9354f22204) [#48107](https://github.com/vllm-project/vllm/pull/48107)
  [Rust][Benchmark] Port in vllm-bench (#48107)
  _Files: `.pre-commit-config.yaml`, `pyproject.toml`, `rust/Cargo.lock`, `rust/Cargo.toml` _+41 more__
- **2026-07-17** [`4d4e04f452`](https://github.com/vllm-project/vllm/commit/4d4e04f452) [#48617](https://github.com/vllm-project/vllm/pull/48617)
  [Render] Add round trip parity test and docs for derender (#48617)
  _Files: `docs/serving/online_serving/README.md`, `docs/serving/online_serving/derenderer.md`, `docs/serving/online_serving/renderer.md`, `docs/usage/security.md` _+3 more__
- **2026-07-17** [`67fe73b2b4`](https://github.com/vllm-project/vllm/commit/67fe73b2b4) [#48873](https://github.com/vllm-project/vllm/pull/48873)
  [CI] Extend max-model-len for `test_parsable_context` to allow reasoning to finish (#48873)
  _Files: `tests/entrypoints/openai/responses/test_parsable_context.py`_
- **2026-07-16** [`8c3393f373`](https://github.com/vllm-project/vllm/commit/8c3393f373) [#48134](https://github.com/vllm-project/vllm/pull/48134)
  [Bugfix][Rust Frontend] Limit chat top_logprobs in responses (#48134)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/utils/logprobs.rs`, `rust/src/server/src/routes/tests.rs`_
- **2026-07-15** [`43cd340247`](https://github.com/vllm-project/vllm/commit/43cd340247) [#48252](https://github.com/vllm-project/vllm/pull/48252)
  [Fix] Align OpenAI vllm_xargs value types across request schemas (#48252)
  _Files: `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/speech_to_text/transcription/protocol.py`_
- **2026-07-15** [`c0302d9497`](https://github.com/vllm-project/vllm/commit/c0302d9497) [#48098](https://github.com/vllm-project/vllm/pull/48098)
  [Bugfix] Fix parallel_tool_calls=null crash in Responses API from_request() (#48098)
  _Files: `tests/tool_use/test_responses_request_validations.py`, `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-07-14** [`94c0ef3001`](https://github.com/vllm-project/vllm/commit/94c0ef3001) [#48549](https://github.com/vllm-project/vllm/pull/48549)
  [Misc] Clean up "swap_space" (#48549)
  _Files: `vllm/entrypoints/llm.py`_
- **2026-07-13** [`8b8af2caf7`](https://github.com/vllm-project/vllm/commit/8b8af2caf7) [#43463](https://github.com/vllm-project/vllm/pull/43463)
  [Frontend] Expose logprob_token_ids on Python OpenAI endpoints (#43463)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `tests/entrypoints/openai/chat_completion/test_logprob_token_ids.py`, `tests/entrypoints/openai/completion/test_completion.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py` _+5 more__

## Quantization  (12 commits)

- **2026-07-20** [`823eaf667d`](https://github.com/vllm-project/vllm/commit/823eaf667d) [#48334](https://github.com/vllm-project/vllm/pull/48334)
  [XPU] FP8 o_proj with fp8_bmm and load-time scale transpose (#48334)
  _Files: `vllm/_xpu_ops.py`, `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`, `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`, `vllm/models/deepseek_v4/xpu/model.py` _+1 more__
- **2026-07-20** [`1dcbbd9cac`](https://github.com/vllm-project/vllm/commit/1dcbbd9cac) [#43024](https://github.com/vllm-project/vllm/pull/43024)
  [CI] Move compatible 1xL4 jobs to H200 35GB MIG (#43024)
  _Files: `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml`, `.buildkite/test_areas/misc.yaml` _+13 more__
- **2026-07-17** [`c9be3a8aa1`](https://github.com/vllm-project/vllm/commit/c9be3a8aa1) [#48797](https://github.com/vllm-project/vllm/pull/48797)
  [Kernel][Helion] Disable warp specialization in rms_norm_per_block_quant B200 configs (#48797)
  _Files: `vllm/kernels/helion/configs/rms_norm_per_block_quant/nvidia_b200.json`_
- **2026-07-16** [`ab3c1aedf3`](https://github.com/vllm-project/vllm/commit/ab3c1aedf3) [#48785](https://github.com/vllm-project/vllm/pull/48785)
  [Bugfix] Fix activation quantization dispatch for WNA4Int/WNA8Int (#48785)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa4.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa8.py`, `vllm/model_executor/layers/quantization/utils/humming_utils.py`_
- **2026-07-16** [`efa2e424f6`](https://github.com/vllm-project/vllm/commit/efa2e424f6) [#48868](https://github.com/vllm-project/vllm/pull/48868)
  [Helion] Fix degenerate scale_ub in kernel input generators (#48868)
  _Files: `vllm/kernels/helion/ops/dynamic_per_token_scaled_fp8_quant.py`, `vllm/kernels/helion/ops/rms_norm_dynamic_per_token_quant.py`, `vllm/kernels/helion/ops/rms_norm_per_block_quant.py`, `vllm/kernels/helion/ops/silu_and_mul_per_block_quant.py`_
- **2026-07-16** [`02bf9c7907`](https://github.com/vllm-project/vllm/commit/02bf9c7907) [#46757](https://github.com/vllm-project/vllm/pull/46757)
  Fix Quark mxfp4 quantized model loading issue under mtp (#46757)
  _Files: `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/utils.py`_
- **2026-07-16** [`75bdad40b5`](https://github.com/vllm-project/vllm/commit/75bdad40b5) [#48507](https://github.com/vllm-project/vllm/pull/48507)
  [Bug][Quantization] Fix humming is_layer_skipped for compressed-tensors "re:" ignore entries (#48507)
  _Files: `tests/quantization/test_humming_ignore.py`, `vllm/model_executor/layers/quantization/humming.py`_
- **2026-07-16** [`2db39c7049`](https://github.com/vllm-project/vllm/commit/2db39c7049) [#48068](https://github.com/vllm-project/vllm/pull/48068)
  [Bugfix][Spec Decode] Fix eagle3 first-layer qkv_proj prefix for quantized drafts (#48068)
  _Files: `vllm/model_executor/models/llama_eagle3.py`_
- **2026-07-15** [`6036bf110a`](https://github.com/vllm-project/vllm/commit/6036bf110a) [#48512](https://github.com/vllm-project/vllm/pull/48512)
  [Kernel][Helion] Add Helion kernel benchmark script (#48512)
  _Files: `scripts/benchmark_helion_kernels.py`, `vllm/kernels/helion/ops/dynamic_per_token_scaled_fp8_quant.py`, `vllm/kernels/helion/ops/per_token_group_fp8_quant.py`, `vllm/kernels/helion/ops/rms_norm_dynamic_per_token_quant.py` _+2 more__
- **2026-07-15** [`61141ed265`](https://github.com/vllm-project/vllm/commit/61141ed265) [#41934](https://github.com/vllm-project/vllm/pull/41934)
  [Hardware][XPU] Register batch-invariant kernels for XPU (#41934)
  _Files: `tests/v1/determinism/test_batch_invariance.py`, `tests/v1/determinism/test_nvfp4_batch_invariant.py`, `tests/v1/determinism/test_online_batch_invariance.py`, `tests/v1/determinism/test_rms_norm_batch_invariant.py` _+2 more__
- **2026-07-15** [`9b2be4e9a5`](https://github.com/vllm-project/vllm/commit/9b2be4e9a5) [#46390](https://github.com/vllm-project/vllm/pull/46390)
  [Quant] Enable humming w[2-7]a[4,8] inference with compressed-tensors (#46390)
  _Files: `tests/evals/gsm8k/configs/humming/Qwen3-4B-mixed-quant-RTN-humming.yaml`, `tests/evals/gsm8k/configs/humming/config-act-int8.txt`, `vllm/model_executor/kernels/linear/mixed_precision/humming.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py` _+4 more__
- **2026-07-14** [`0b0ef8d7eb`](https://github.com/vllm-project/vllm/commit/0b0ef8d7eb) [#47521](https://github.com/vllm-project/vllm/pull/47521)
  [Quantization][INC][ARK] Support INT2 XPU WOQ Linear (#47521)
  _Files: `requirements/xpu.txt`, `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`_

## Multimodal  (11 commits)

- **2026-07-20** [`f1f1259692`](https://github.com/vllm-project/vllm/commit/f1f1259692) [#48781](https://github.com/vllm-project/vllm/pull/48781)
  [Rust Frontend] Use zero-copy slicing for multimodal tensors (#48781)
  _Files: `rust/src/chat/src/multimodal/item.rs`, `rust/src/chat/src/multimodal/tensor.rs`, `rust/src/chat/src/multimodal/video.rs`, `rust/src/engine-core-client/src/protocol/tensor.rs`_
- **2026-07-18** [`9243e0124e`](https://github.com/vllm-project/vllm/commit/9243e0124e) [#49046](https://github.com/vllm-project/vllm/pull/49046)
  [Multimodal] Automatically fallback to ViT DP when TP is unavailable (#49046)
  _Files: `vllm/model_executor/models/kimi_k25.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/vision.py`_
- **2026-07-18** [`7c2acd38b7`](https://github.com/vllm-project/vllm/commit/7c2acd38b7) [#49015](https://github.com/vllm-project/vllm/pull/49015)
  [Bugfix] Qwen3-VL/Qwen-Omni: honor max_pixels/min_pixels for video prompts (#49015)
  _Files: `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-07-17** [`bf578e1abd`](https://github.com/vllm-project/vllm/commit/bf578e1abd) [#48729](https://github.com/vllm-project/vllm/pull/48729)
  [Bugfix][GLM4V] Fix video dummy profiling and memory usage (#48729)
  _Files: `tests/models/multimodal/processing/test_glm4_1v.py`, `vllm/model_executor/models/glm4_1v.py`_
- **2026-07-15** [`e281ac663a`](https://github.com/vllm-project/vllm/commit/e281ac663a) [#48554](https://github.com/vllm-project/vllm/pull/48554)
  [Rust Frontend] Integrate MM audio support (#48554)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/Cargo.toml`, `rust/src/chat/src/backend/hf.rs` _+14 more__
- **2026-07-14** [`b6754f536e`](https://github.com/vllm-project/vllm/commit/b6754f536e) [#48594](https://github.com/vllm-project/vllm/pull/48594)
  [Model] Enable LoRA support for tower and connector in LlavaNextVideo (#48594)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_llava_next_video.py`, `vllm/model_executor/models/llava_next_video.py`_
- **2026-07-14** [`793cf79c89`](https://github.com/vllm-project/vllm/commit/793cf79c89) [#48583](https://github.com/vllm-project/vllm/pull/48583)
  [Bugfix][Security] Fix concurrent sparse invariant race bypassing CVE remediation (#48583)
  _Files: `tests/renderers/test_sparse_tensor_concurrent_race.py`, `vllm/multimodal/media/audio.py`, `vllm/multimodal/media/image.py`, `vllm/renderers/embed_utils.py` _+1 more__
- **2026-07-14** [`038ec293b1`](https://github.com/vllm-project/vllm/commit/038ec293b1) [#48473](https://github.com/vllm-project/vllm/pull/48473)
  [Bugfix] Return 400 instead of 500 when multimodal data is sent to a text-only model (#48473)
  _Files: `tests/renderers/test_process_multi_modal_uuids.py`, `vllm/renderers/base.py`_
- **2026-07-14** [`894ebb27f5`](https://github.com/vllm-project/vllm/commit/894ebb27f5) [#48291](https://github.com/vllm-project/vllm/pull/48291)
  Add Cosmos3 Edge Reasoner model (#48291)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_cosmos3_edge.py`, `tests/models/multimodal/test_mapping.py`, `tests/models/registry.py` _+9 more__
- **2026-07-13** [`93e3bc8f30`](https://github.com/vllm-project/vllm/commit/93e3bc8f30) [#48418](https://github.com/vllm-project/vllm/pull/48418)
  [XPU][CI]Adjust timeout_in_minutes in Intel GPU CI (#48418)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/lora_intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml` _+3 more__
- **2026-07-13** [`c2c9f7c5e2`](https://github.com/vllm-project/vllm/commit/c2c9f7c5e2) [#48467](https://github.com/vllm-project/vllm/pull/48467)
  remove force channels_last in Idefics3MultiModalProcessor (#48467)
  _Files: `vllm/model_executor/models/idefics3.py`_

## Scheduler / Engine  (11 commits)

- **2026-07-19** [`ac5f38a0f7`](https://github.com/vllm-project/vllm/commit/ac5f38a0f7) [#49003](https://github.com/vllm-project/vllm/pull/49003)
  [Refactor] Extract StructuredOutputsParams creation logic from Request.to_sampling_params (#49003)
  _Files: `tests/entrypoints/openai/responses/test_sampling_params.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/engine/protocol.py` _+1 more__
- **2026-07-18** [`a287eb163f`](https://github.com/vllm-project/vllm/commit/a287eb163f) [#48535](https://github.com/vllm-project/vllm/pull/48535)
  [Front-end] [Messages] Populate `num_cache_creation_tokens` (#48535)
  _Files: `rust/src/engine-core-client/src/protocol/stats.rs`, `rust/src/llm/src/request_metrics.rs`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/anthropic/test_messages.py` _+11 more__
- **2026-07-17** [`11d291511a`](https://github.com/vllm-project/vllm/commit/11d291511a) [#48846](https://github.com/vllm-project/vllm/pull/48846)
  [Bugfix][Tool Parser] Preserve whitespace in parameter values (MiniMax M2, Qwen3, MiniCPM5 XML) (#48846)
  _Files: `tests/parser/engine/test_qwen3.py`, `tests/tool_parsers/test_minicpm5xml_tool_parser.py`, `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `tests/tool_parsers/test_qwen3coder_tool_parser.py` _+3 more__
- **2026-07-16** [`3e90d015ba`](https://github.com/vllm-project/vllm/commit/3e90d015ba) [#47699](https://github.com/vllm-project/vllm/pull/47699)
  [Frontend] Overlap preprocessing and computation for pooling models offline inference  (#47699)
  _Files: `.buildkite/test_areas/models_language.yaml`, `tests/entrypoints/pooling/basic/test_tiling_engine.py`, `tests/models/language/pooling/test_multi_vector_retrieval.py`, `vllm/entrypoints/llm.py` _+6 more__
- **2026-07-16** [`530852f959`](https://github.com/vllm-project/vllm/commit/530852f959) [#48481](https://github.com/vllm-project/vllm/pull/48481)
  [KV Connector] Fix PD async scheduling race condition for hybrid attn models (#48481)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/v1/core/kv_cache_manager.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-07-16** [`f44f3d6f79`](https://github.com/vllm-project/vllm/commit/f44f3d6f79) [#47965](https://github.com/vllm-project/vllm/pull/47965)
  [Rust Frontend] Wait for mock engine endpoints before ZMQ connect (#47965)
  _Files: `rust/src/engine-core-client/src/mock_engine.rs`_
- **2026-07-16** [`dc9f845ddc`](https://github.com/vllm-project/vllm/commit/dc9f845ddc) [#48738](https://github.com/vllm-project/vllm/pull/48738)
  [Rust Frontend] Fix mock engine test shutdown race (#48738)
  _Files: `rust/src/mock-engine/src/tests.rs`_
- **2026-07-16** [`5a65ba5f17`](https://github.com/vllm-project/vllm/commit/5a65ba5f17) [#46647](https://github.com/vllm-project/vllm/pull/46647)
  [Refactor] Move iteration logging to the frontend (#46647)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/engine/test_iteration_logging.py`, `tests/v1/metrics/test_stats.py`, `vllm/v1/core/sched/output.py` _+5 more__
- **2026-07-14** [`9182e86971`](https://github.com/vllm-project/vllm/commit/9182e86971) [#48030](https://github.com/vllm-project/vllm/pull/48030)
  Log fully resolved pooling config at startup (#48030)
  _Files: `vllm/config/model.py`, `vllm/config/pooler.py`, `vllm/v1/engine/core.py`_
- **2026-07-14** [`af453e5647`](https://github.com/vllm-project/vllm/commit/af453e5647) [#48262](https://github.com/vllm-project/vllm/pull/48262)
  [Bugfix] Gemma4 parser: classify channel-less output consistently in streaming and non-streaming (#48262)
  _Files: `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `vllm/parser/gemma4.py`_
- **2026-07-13** [`550218b136`](https://github.com/vllm-project/vllm/commit/550218b136) [#47606](https://github.com/vllm-project/vllm/pull/47606)
  [Bugfix][Frontend] Flush engine reasoning parser at engine-reasoning → tool streaming boundary (#47606)
  _Files: `tests/parser/test_streaming.py`, `vllm/parser/abstract_parser.py`_

## KV Cache / Offload  (10 commits)

- **2026-07-20** [`5245c80564`](https://github.com/vllm-project/vllm/commit/5245c80564) [#49100](https://github.com/vllm-project/vllm/pull/49100)
  [Doc] Document blocks_per_chunk in the KV offloading guide (#49100)
  _Files: `docs/features/kv_offloading_usage.md`_
- **2026-07-20** [`9bc266d923`](https://github.com/vllm-project/vllm/commit/9bc266d923) [#49071](https://github.com/vllm-project/vllm/pull/49071)
  [Bugfix][KV Offload] Propagate EAGLE mode to SimpleCPU coordinator (#49071)
  _Files: `vllm/v1/simple_kv_offload/manager.py`_
- **2026-07-17** [`f38f3d11fb`](https://github.com/vllm-project/vllm/commit/f38f3d11fb) [#48596](https://github.com/vllm-project/vllm/pull/48596)
  [Bugfix][KV Offloading] Offload last block at request finish and prevent reuse race (#48596)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`_
- **2026-07-17** [`426d48bfa1`](https://github.com/vllm-project/vllm/commit/426d48bfa1) [#48281](https://github.com/vllm-project/vllm/pull/48281)
  [KV Offload] Add optional tier locality to FS/OBJ KV events (#48281)
  _Files: `docs/features/kv_offloading_usage.md`, `examples/features/kv_events/kv_events_subscriber.py`, `tests/distributed/test_kv_cache_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py` _+7 more__
- **2026-07-17** [`472d330c21`](https://github.com/vllm-project/vllm/commit/472d330c21) [#48878](https://github.com/vllm-project/vllm/pull/48878)
  Add blocks_per_chunk configuration for KV offloading to support heterogeneous KV cache groups (#48878)
  _Files: `tests/v1/kv_offload/test_factory.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/config.py`_
- **2026-07-16** [`ce65385618`](https://github.com/vllm-project/vllm/commit/ce65385618) [#47679](https://github.com/vllm-project/vllm/pull/47679)
  [KV Offload] Split tiering_lookup_delay into sync/async histograms (#47679)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/manager.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-07-16** [`a9531edfa6`](https://github.com/vllm-project/vllm/commit/a9531edfa6) [#48150](https://github.com/vllm-project/vllm/pull/48150)
  [KV Offload] Define clean backend configuration boundary (#48150)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/test_worker.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py` _+23 more__
- **2026-07-16** [`12f2c515a7`](https://github.com/vllm-project/vllm/commit/12f2c515a7) [#48530](https://github.com/vllm-project/vllm/pull/48530)
  [Bugfix] Fix offloading set_ overflow for packed non-uniform KV caches (#48530)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/worker.py`_
- **2026-07-14** [`cdaa40d2a8`](https://github.com/vllm-project/vllm/commit/cdaa40d2a8) [#47666](https://github.com/vllm-project/vllm/pull/47666)
  [KV Offload] Split cpu_cache_usage_perc into write/read usage gauges (#47666)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/common.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-07-14** [`f04d3f640e`](https://github.com/vllm-project/vllm/commit/f04d3f640e) [#47754](https://github.com/vllm-project/vllm/pull/47754)
  [Test] Enable KV cache events for HMA models in CPU offloading test (#47754)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`_

## Models  (10 commits)

- **2026-07-17** [`41ea2dd44a`](https://github.com/vllm-project/vllm/commit/41ea2dd44a) [#47680](https://github.com/vllm-project/vllm/pull/47680)
  [Bugfix][V1/V2] Fix prompt_logprobs to respect logprobs_mode (#47680)
  _Files: `tests/v1/sample/test_logprobs.py`, `vllm/config/model.py`, `vllm/config/vllm.py`, `vllm/model_executor/models/diffusion_gemma.py` _+7 more__
- **2026-07-17** [`7b3192523e`](https://github.com/vllm-project/vllm/commit/7b3192523e) [#48699](https://github.com/vllm-project/vllm/pull/48699)
  [Bugfix]Fix transformer backend failed: AttributeError: 'Parameter' object has no attribute 'weight_loader' (#48699)
  _Files: `vllm/model_executor/models/transformers/base.py`_
- **2026-07-17** [`26c909ed74`](https://github.com/vllm-project/vllm/commit/26c909ed74) [#41599](https://github.com/vllm-project/vllm/pull/41599)
  [Model] Support TranslateGemma-12b-it (#41599)
  _Files: `tests/entrypoints/openai/chat_completion/test_extra_content_fields.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-07-16** [`ea1d65fe6d`](https://github.com/vllm-project/vllm/commit/ea1d65fe6d) [#47741](https://github.com/vllm-project/vllm/pull/47741)
  [Rust Frontend] Add Seed-OSS tool parser (#47741)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`, `rust/src/chat/tests/roundtrip.rs` _+3 more__
- **2026-07-15** [`5810e884f1`](https://github.com/vllm-project/vllm/commit/5810e884f1) [#47991](https://github.com/vllm-project/vllm/pull/47991)
  [Model] Add RobertaForTokenClassification / XLMRobertaForTokenClassification (#47991)
  _Files: `docs/models/pooling_models/token_classify.md`, `tests/models/language/pooling/test_token_classification.py`, `tests/models/registry.py`, `vllm/model_executor/models/registry.py` _+1 more__
- **2026-07-15** [`4e04bcbce6`](https://github.com/vllm-project/vllm/commit/4e04bcbce6) [#48034](https://github.com/vllm-project/vllm/pull/48034)
  [Rust Frontend] Tolerate whitespace before the outer brace in JSON tool-call parsers (#48034)
  _Files: `rust/src/chat/src/output/default/unified.rs`, `rust/src/parser/src/tool/json/llama.rs`, `rust/src/parser/src/tool/json/mod.rs`_
- **2026-07-15** [`442c421e79`](https://github.com/vllm-project/vllm/commit/442c421e79) [#48137](https://github.com/vllm-project/vllm/pull/48137)
  [Perf] Remove redundant repeat and copy for dsv4, 1.8% E2E TPOT improvement. (#48137)
  _Files: `vllm/model_executor/kernels/mhc/tilelang.py`, `vllm/model_executor/kernels/mhc/tilelang_kernels.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-07-14** [`1ff9429655`](https://github.com/vllm-project/vllm/commit/1ff9429655) [#48036](https://github.com/vllm-project/vllm/pull/48036)
  [CI Bug] Fully solve accuracy issue for DSv3.2 + MTP + Sequence Parallel (#48036)
  _Files: `vllm/config/parallel.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-07-13** [`7738ef35b8`](https://github.com/vllm-project/vllm/commit/7738ef35b8) [#48463](https://github.com/vllm-project/vllm/pull/48463)
  [Feat] Add Support for BertForMaskedLM to vLLM (#48463)
  _Files: `tests/models/language/pooling/test_token_classification.py`, `tests/models/registry.py`, `vllm/model_executor/models/bert.py`, `vllm/model_executor/models/registry.py`_
- **2026-07-13** [`5c342876a6`](https://github.com/vllm-project/vllm/commit/5c342876a6) [#48293](https://github.com/vllm-project/vllm/pull/48293)
  [Doc] Add DeepseekV32ForCausalLM to supported_models.md (#48293)
  _Files: `docs/models/supported_models.md`_

## CI / Build  (9 commits)

- **2026-07-20** [`2730b657c4`](https://github.com/vllm-project/vllm/commit/2730b657c4) [#49108](https://github.com/vllm-project/vllm/pull/49108)
  [Bugfix] Fix broken NVVM caused by CuteDSL 4.6.0 (#49108)
  _Files: `.buildkite/test_areas/kernels.yaml`, `vllm/cute_utils/_tcgen05.py`_
- **2026-07-18** [`c7ce03bcbd`](https://github.com/vllm-project/vllm/commit/c7ce03bcbd) [#48988](https://github.com/vllm-project/vllm/pull/48988)
  [Bugfix] Bump tml-fa4 for cutlass-dsl 4.6 API compatibility (#48988)
  _Files: `cmake/external_projects/tml_fa4.cmake`_
- **2026-07-17** [`088c0be268`](https://github.com/vllm-project/vllm/commit/088c0be268) [#48771](https://github.com/vllm-project/vllm/pull/48771)
  [CI] Fix macOS wheel release annotation context (#48771)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-07-17** [`d4b4562917`](https://github.com/vllm-project/vllm/commit/d4b4562917) [#48942](https://github.com/vllm-project/vllm/pull/48942)
  [XPU] Bump vllm_xpu_kernels to v0.1.11.1 (#48942)
  _Files: `requirements/xpu.txt`_
- **2026-07-16** [`d803b44dbe`](https://github.com/vllm-project/vllm/commit/d803b44dbe) [#47559](https://github.com/vllm-project/vllm/pull/47559)
  [NIXL] Bump nixl to 1.3.1 (#47559)
  _Files: `requirements/kv_connectors.txt`_
- **2026-07-15** [`12a8057bfe`](https://github.com/vllm-project/vllm/commit/12a8057bfe) [#48600](https://github.com/vllm-project/vllm/pull/48600)
  [CI/Build] Split release artifact annotations by type (#48600)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/annotate-build-artifact.sh`_
- **2026-07-14** [`0b54201a04`](https://github.com/vllm-project/vllm/commit/0b54201a04) [#48289](https://github.com/vllm-project/vllm/pull/48289)
  [CI] Build macOS arm64 CPU wheel natively on the macmini queue (#48289)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/build-macos-wheel.sh`, `.buildkite/scripts/upload-nightly-wheels.sh`, `csrc/cpu/torch_bindings.cpp`_
- **2026-07-14** [`0a9396a25e`](https://github.com/vllm-project/vllm/commit/0a9396a25e) [#47231](https://github.com/vllm-project/vllm/pull/47231)
  [XPU][CI] Add tests/v1/e2e/general/test_correctness_sliding_window.py in Intel GPU CI (#47231)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-07-13** [`487dfb3418`](https://github.com/vllm-project/vllm/commit/487dfb3418) [#48472](https://github.com/vllm-project/vllm/pull/48472)
  [CI] Add SPDX license header to Rust/Protobuf sources (#48472)

## Speculative Decoding  (9 commits)

- **2026-07-17** [`877dae9c68`](https://github.com/vllm-project/vllm/commit/877dae9c68) [#48780](https://github.com/vllm-project/vllm/pull/48780)
  [Refactor] Remove deepseek dead code (#48780)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`, `vllm/model_executor/models/deepseek_mtp.py`, `vllm/model_executor/warmup/deepseek_v4_mhc_warmup.py`, `vllm/renderers/deepseek_v32.py` _+3 more__
- **2026-07-16** [`4a394bfcda`](https://github.com/vllm-project/vllm/commit/4a394bfcda) [#47216](https://github.com/vllm-project/vllm/pull/47216)
  [Spec Decode][DSpark] Add Gemma4-12B DSpark draft model (#47216)
  _Files: `tests/evals/gsm8k/gsm8k_eval.py`, `tests/models/registry.py`, `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/config/speculative.py` _+2 more__
- **2026-07-16** [`fb5ec0dc9e`](https://github.com/vllm-project/vllm/commit/fb5ec0dc9e) [#48869](https://github.com/vllm-project/vllm/pull/48869)
  [Model] Add Inkling MTP=1 support [3/N] (#48869)
  _Files: `tests/config/test_speculative_draft_hf_overrides.py`, `tests/models/inkling/test_contract_validation.py`, `tests/models/inkling/test_mtp_input_fusion.py`, `tests/models/registry.py` _+7 more__
- **2026-07-16** [`9d1c695be5`](https://github.com/vllm-project/vllm/commit/9d1c695be5) [#47677](https://github.com/vllm-project/vllm/pull/47677)
  [XPU] Add DSpark speculative decoding support for DeepSeek-V4 (#47677)
  _Files: `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/xpu/dspark.py`, `vllm/models/deepseek_v4/xpu/model.py`_
- **2026-07-16** [`3a5e88e629`](https://github.com/vllm-project/vllm/commit/3a5e88e629) [#48754](https://github.com/vllm-project/vllm/pull/48754)
  [Bugfix] Fix local speculators with dots in the name from classifying as custom_class (#48754)
  _Files: `vllm/config/speculative.py`_
- **2026-07-15** [`b7950e798f`](https://github.com/vllm-project/vllm/commit/b7950e798f) [#47460](https://github.com/vllm-project/vllm/pull/47460)
  [Bugfix] Initialize draft CUDA-graph keys for the native draft_model proposer (#47460)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-15** [`3ca242d1b6`](https://github.com/vllm-project/vllm/commit/3ca242d1b6) [#48622](https://github.com/vllm-project/vllm/pull/48622)
  [Bugfix][R3] Exclude draft routers from expert capture (#48622)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-14** [`32e632dfeb`](https://github.com/vllm-project/vllm/commit/32e632dfeb) [#46662](https://github.com/vllm-project/vllm/pull/46662)
  [Reasoning] Optimize TPOT for thinking budget when used with speculative decoding (#46662)
  _Files: `vllm/v1/sample/rejection_sampler.py`, `vllm/v1/sample/sampler.py`, `vllm/v1/sample/thinking_budget_state.py`_
- **2026-07-13** [`8c5dafcd09`](https://github.com/vllm-project/vllm/commit/8c5dafcd09) [#48452](https://github.com/vllm-project/vllm/pull/48452)
  [Bugfix][UT]Fix EagleMiniCPMForCausalLM meet TypeError (#48452)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/minicpm_eagle.py`_

## Docs  (8 commits)

- **2026-07-20** [`ae10e855ab`](https://github.com/vllm-project/vllm/commit/ae10e855ab) [#47210](https://github.com/vllm-project/vllm/pull/47210)
  [Misc][Docs] Remove duplicate CodeGeex4 row in XPU model table (#47210)
  _Files: `docs/models/hardware_supported_models/xpu.md`_
- **2026-07-20** [`47d0597ca2`](https://github.com/vllm-project/vllm/commit/47d0597ca2) [#47211](https://github.com/vllm-project/vllm/pull/47211)
  [Misc][Docs] Fix broken csrc kernel links in fusions doc (#47211)
  _Files: `docs/design/fusions.md`_
- **2026-07-17** [`109b736b86`](https://github.com/vllm-project/vllm/commit/109b736b86) [#48839](https://github.com/vllm-project/vllm/pull/48839)
  [docs] preserve page path in stable-docs announcement link (#48839)
  _Files: `docs/mkdocs/overrides/main.html`_
- **2026-07-17** [`b88abb5036`](https://github.com/vllm-project/vllm/commit/b88abb5036) [#44749](https://github.com/vllm-project/vllm/pull/44749)
  [Misc] Remove orphaned env vars and stale env-var references (#44749)
  _Files: `docs/configuration/env_vars.md`, `docs/serving/expert_parallel_deployment.md`, `vllm/envs.py`_
- **2026-07-16** [`ab0a20d151`](https://github.com/vllm-project/vllm/commit/ab0a20d151) [#46396](https://github.com/vllm-project/vllm/pull/46396)
  [Docs] Add Phi-3.5-mini-instruct to batch invariance tested models (#46396)
  _Files: `docs/features/batch_invariance.md`_
- **2026-07-16** [`3935829f89`](https://github.com/vllm-project/vllm/commit/3935829f89) [#48802](https://github.com/vllm-project/vllm/pull/48802)
  [Docs] fix error key name (#48802)
  _Files: `docs/deployment/k8s.md`_
- **2026-07-15** [`de100ffb62`](https://github.com/vllm-project/vllm/commit/de100ffb62) [#48497](https://github.com/vllm-project/vllm/pull/48497)
  [Docs] Document pooling config resolution (#48497)
  _Files: `docs/models/pooling_models/README.md`_
- **2026-07-15** [`615834ee58`](https://github.com/vllm-project/vllm/commit/615834ee58) [#47636](https://github.com/vllm-project/vllm/pull/47636)
  [KVOffload][P2P] Well-known default host/port env vars and per-DP-rank control port (#47636)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/test_envs.py`, `tests/v1/kv_offload/tiering/p2p/p2p_connector_proxy.py`, `tests/v1/kv_offload/tiering/p2p/run_accuracy_test.sh` _+9 more__

## Compilation / CUDA Graph  (4 commits)

- **2026-07-17** [`3b6c96a101`](https://github.com/vllm-project/vllm/commit/3b6c96a101) [#48901](https://github.com/vllm-project/vllm/pull/48901)
  [Bugfix][Pooling] Fix wrong scores for chunked prefill under torch.compile (#48901)
  _Files: `tests/models/language/pooling/test_all_pooling_plus_chunked_prefill.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-07-16** [`81e13a0591`](https://github.com/vllm-project/vllm/commit/81e13a0591) [#42543](https://github.com/vllm-project/vllm/pull/42543)
  [Compilation] Skip x.size(dim) in _decompose_size_nodes (#42543)
  _Files: `tests/compile/test_graph_partition.py`, `vllm/compilation/backends.py`_
- **2026-07-15** [`3b39fd284a`](https://github.com/vllm-project/vllm/commit/3b39fd284a) [#48671](https://github.com/vllm-project/vllm/pull/48671)
  [Bugfix][Spec Decode] Support heterogeneous QK fusion geometry (#48671)
  _Files: `tests/compile/passes/test_qk_norm_rope_fusion.py`, `vllm/compilation/passes/fusion/qk_norm_rope_fusion.py`_
- **2026-07-13** [`fec64fea75`](https://github.com/vllm-project/vllm/commit/fec64fea75) [#40698](https://github.com/vllm-project/vllm/pull/40698)
  [BugFix] Correct OTEL span start time for Dynamo compilation (#40698)
  _Files: `vllm/compilation/backends.py`_

## LoRA  (4 commits)

- **2026-07-16** [`59b964f37d`](https://github.com/vllm-project/vllm/commit/59b964f37d) [#48437](https://github.com/vllm-project/vllm/pull/48437)
  fix(lora): validate LoRA rank is positive in PEFTHelper (#48437)
  _Files: `tests/lora/test_peft_helper.py`, `vllm/lora/peft_helper.py`_
- **2026-07-16** [`7746961277`](https://github.com/vllm-project/vllm/commit/7746961277) [#47375](https://github.com/vllm-project/vllm/pull/47375)
  [CI] Fix flaky lora test (#47375)
  _Files: `tests/lora/test_gptoss_tp.py`_
- **2026-07-15** [`4f7fffb92f`](https://github.com/vllm-project/vllm/commit/4f7fffb92f) [#48525](https://github.com/vllm-project/vllm/pull/48525)
  [Core][LoRA] Support fp32 lm_head (head_dtype) on the LoRA path (#48525)
  _Files: `tests/lora/test_layers.py`, `tests/v1/sample/test_head_dtype.py`, `vllm/lora/layers/logits_processor.py`_
- **2026-07-13** [`107a03ba63`](https://github.com/vllm-project/vllm/commit/107a03ba63) [#48390](https://github.com/vllm-project/vllm/pull/48390)
  [Core] Support fp32 lm_head for generation models via head_dtype (RFC #48305 §3.6) (#48390)
  _Files: `tests/models/language/generation_ppl_test/ppl_utils.py`, `tests/models/language/generation_ppl_test/test_gpt.py`, `tests/v1/sample/test_head_dtype.py`, `vllm/config/model.py` _+2 more__

## Perf / Benchmark  (2 commits)

- **2026-07-18** [`c71a583aa9`](https://github.com/vllm-project/vllm/commit/c71a583aa9) [#48110](https://github.com/vllm-project/vllm/pull/48110)
  [Perf][Hybrid] Vectorize _copy_mamba_state_block to uint64 for temporal (#48110)
  _Files: `vllm/v1/worker/mamba_utils.py`_
- **2026-07-13** [`e26264f3ef`](https://github.com/vllm-project/vllm/commit/e26264f3ef) [#39058](https://github.com/vllm-project/vllm/pull/39058)
  [Kernel] Implement CUDA kernel for ReLUSquaredActivation (relu^2) (#39058)
  _Files: `benchmarks/kernels/benchmark_relu_squared.py`, `csrc/libtorch_stable/activation_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+3 more__

---
_Generated 2026-07-20 11:11 UTC_