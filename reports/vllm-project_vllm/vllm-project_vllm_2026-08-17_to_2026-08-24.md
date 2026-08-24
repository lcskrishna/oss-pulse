# vllm-project/vllm — Weekly Change Report
**Period:** 2026-08-17 → 2026-08-24  |  **Total commits:** 308

## ✨ New Features This Week

- **2026-08-24** [#53226](https://github.com/vllm-project/vllm/pull/53226) — [Xeon][doc]add Xeon recipes into table (#53226)
- **2026-08-24** [#52786](https://github.com/vllm-project/vllm/pull/52786) — [LoRA] Add Qwen3-Omni multimodal LoRA support (#52786)
- **2026-08-24** [#53361](https://github.com/vllm-project/vllm/pull/53361) — [LoRA] feat: Support LoRA for DeepSeek V4 (#53361)
- **2026-08-24** [#53101](https://github.com/vllm-project/vllm/pull/53101) — [Model] Add FP8 quantization support for ModernBERT (#53101)
- **2026-08-24** [#51034](https://github.com/vllm-project/vllm/pull/51034) — feat: add SSE keep-alive comments for idle streaming responses (#51034)
- **2026-08-24** [#53121](https://github.com/vllm-project/vllm/pull/53121) — Add MTP support for Nemotron VL models (#53121)
- **2026-08-23** [#52209](https://github.com/vllm-project/vllm/pull/52209) — Add routed expert loading for gpt-oss (#52209)
- **2026-08-22** [#52560](https://github.com/vllm-project/vllm/pull/52560) — [Model] Add Qwen3-Omni DSpark support (#52560)
- **2026-08-22** [#50723](https://github.com/vllm-project/vllm/pull/50723) — [Core][RL] Support sparse checkpoint updates through native weight loaders (#50723)
- **2026-08-21** [#52854](https://github.com/vllm-project/vllm/pull/52854) — [ROCm][CI] aiter kernel ops - enable rope test (#52854)
- _…and 50 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-23** [`d569e71bd0`](https://github.com/vllm-project/vllm/commit/d569e71bd0) [#52547](https://github.com/vllm-project/vllm/pull/52547) — [CI][AMD] Honor single-node Docker workload timeout (#52547)
- **2026-08-23** [`30b34171b1`](https://github.com/vllm-project/vllm/commit/30b34171b1) [#53351](https://github.com/vllm-project/vllm/pull/53351) — [ROCm][CI] Restore attention coverage after KV-cache layout refactor (#53351)
- **2026-08-22** [`610bfc58e9`](https://github.com/vllm-project/vllm/commit/610bfc58e9) [#53182](https://github.com/vllm-project/vllm/pull/53182) — [ROCm] Ship rocprofiler-sdk 1.3.2 in Dockerfile.rocm_base to fix torch.profiler traces (#53182)
- **2026-08-22** [`7f4a1b7e24`](https://github.com/vllm-project/vllm/commit/7f4a1b7e24) [#53110](https://github.com/vllm-project/vllm/pull/53110) — [Bugfix][ROCM] Fix the MXFP8 block scale exponent (#53110)
- **2026-08-21** [`f37d5868b9`](https://github.com/vllm-project/vllm/commit/f37d5868b9) [#53117](https://github.com/vllm-project/vllm/pull/53117) — [CI/Build][ROCm] Run the TileLang HIP symbol checks in their own interpreter (#53117)
- **2026-08-21** [`592e06f2ae`](https://github.com/vllm-project/vllm/commit/592e06f2ae) [#53294](https://github.com/vllm-project/vllm/pull/53294) — Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill" (#53294)
- **2026-08-21** [`29b7c2f7d4`](https://github.com/vllm-project/vllm/commit/29b7c2f7d4) [#52854](https://github.com/vllm-project/vllm/pull/52854) — [ROCm][CI] aiter kernel ops - enable rope test (#52854)
- **2026-08-21** [`a0af854f5d`](https://github.com/vllm-project/vllm/commit/a0af854f5d) [#53024](https://github.com/vllm-project/vllm/pull/53024) — [ROCm][CI] Stabilize MI355 FlyDSL MoE accuracy test (#53024)
- **2026-08-21** [`b5f7fcc79d`](https://github.com/vllm-project/vllm/commit/b5f7fcc79d) [#53177](https://github.com/vllm-project/vllm/pull/53177) — [ROCm][CI] Add float16 dtype and unsupported head size tests for paged attention (#53177)
- **2026-08-21** [`88eb946cb1`](https://github.com/vllm-project/vllm/commit/88eb946cb1) [#53025](https://github.com/vllm-project/vllm/pull/53025) — [ROCm][CI] Stabilize MI355 FusedMoE test group (#53025)
- **2026-08-21** [`f15ea66b30`](https://github.com/vllm-project/vllm/commit/f15ea66b30) [#53268](https://github.com/vllm-project/vllm/pull/53268) — [ROCm][Test] Use platform FP8 dtype in ModelOpt FP8_PB_WO test (#53268)
- **2026-08-21** [`7a2fdbaac4`](https://github.com/vllm-project/vllm/commit/7a2fdbaac4) [#53152](https://github.com/vllm-project/vllm/pull/53152) — [K3 Perf] Fuse MXFP4 top-k finalization into latent-tail, ~5% E2E latency reduction (#53152)
- **2026-08-21** [`fe76112ff2`](https://github.com/vllm-project/vllm/commit/fe76112ff2) [#52882](https://github.com/vllm-project/vllm/pull/52882) — [ROCm][Perf] Optimize DeepSeek V4 C4A top-k with AITER (#52882)
- **2026-08-21** [`463aa5e30f`](https://github.com/vllm-project/vllm/commit/463aa5e30f) [#52606](https://github.com/vllm-project/vllm/pull/52606) — [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill (#52606)
- **2026-08-21** [`cd7b7c265a`](https://github.com/vllm-project/vllm/commit/cd7b7c265a) [#43018](https://github.com/vllm-project/vllm/pull/43018) — [ROCm] Cpu offload for ROCm 7.13+ to align the hipMemcpyBatchAsync params and perf in 7.14x (#43018)
- **2026-08-21** [`83c5d59209`](https://github.com/vllm-project/vllm/commit/83c5d59209) [#52892](https://github.com/vllm-project/vllm/pull/52892) — [Rust Frontend] Replace external `protoc` with pure Rust lib `protox` (#52892)
- **2026-08-20** [`3b829cf176`](https://github.com/vllm-project/vllm/commit/3b829cf176) [#53113](https://github.com/vllm-project/vllm/pull/53113) — [CI/Build][ROCm] Keep the CUDA-only kernel tests out of the ROCm run (#53113)
- **2026-08-20** [`1fe3a1571a`](https://github.com/vllm-project/vllm/commit/1fe3a1571a) [#53106](https://github.com/vllm-project/vllm/pull/53106) — Reduce `AutoWeightsLoader` kwargs (#53106)
- **2026-08-20** [`f0c14b4f77`](https://github.com/vllm-project/vllm/commit/f0c14b4f77) [#51665](https://github.com/vllm-project/vllm/pull/51665) — Fix weight tying (#51665)
- **2026-08-20** [`1eab6fef01`](https://github.com/vllm-project/vllm/commit/1eab6fef01) [#52572](https://github.com/vllm-project/vllm/pull/52572) — [CI] replace shellcheck script with shellcheck-py hook (#52572)
- **2026-08-20** [`6b68db441e`](https://github.com/vllm-project/vllm/commit/6b68db441e) [#50803](https://github.com/vllm-project/vllm/pull/50803) — [ROCm] Fix DeepSeek V4 indexer numerics and coverage (#50803)
- **2026-08-20** [`5d4d470470`](https://github.com/vllm-project/vllm/commit/5d4d470470) [#53026](https://github.com/vllm-project/vllm/pull/53026) — [CI] Fix nonexistent dependency for data-parallel example test selection (#53026)
- **2026-08-20** [`4666a8ba9e`](https://github.com/vllm-project/vllm/commit/4666a8ba9e) [#53064](https://github.com/vllm-project/vllm/pull/53064) — [Refactor] Remove InputPreprocessor (#53064)
- **2026-08-20** [`d626108b18`](https://github.com/vllm-project/vllm/commit/d626108b18) [#52737](https://github.com/vllm-project/vllm/pull/52737) — [ROCm][Perf] Fuse DeepSeek-V4 mHC post/pre and RMSNorm with AITER (#52737)
- **2026-08-20** [`cd5035379c`](https://github.com/vllm-project/vllm/commit/cd5035379c) [#51585](https://github.com/vllm-project/vllm/pull/51585) — [ROCm] [Bugfix] Preserve CPU query offsets during capture (#51585)
- **2026-08-20** [`4f66bc3e0d`](https://github.com/vllm-project/vllm/commit/4f66bc3e0d) [#52976](https://github.com/vllm-project/vllm/pull/52976) — [CI][ROCm] Standardize AMD test job labels by device (#52976)
- **2026-08-20** [`fbb4c04db4`](https://github.com/vllm-project/vllm/commit/fbb4c04db4) [#53004](https://github.com/vllm-project/vllm/pull/53004) — [ROCm][CI] Speed up `test_rocm_aiter_qk_norm_rope_kvcache_fusion` (#53004)
- **2026-08-19** [`823ec22b78`](https://github.com/vllm-project/vllm/commit/823ec22b78) [#52819](https://github.com/vllm-project/vllm/pull/52819) — [ROCm]: Bump triton 3.7 commit (#52819)
- **2026-08-19** [`480d4f0d15`](https://github.com/vllm-project/vllm/commit/480d4f0d15) [#46434](https://github.com/vllm-project/vllm/pull/46434) — [ROCm][CI] Enable modular OAI Triton MoE tests (#46434)
- **2026-08-19** [`3a386cfaf5`](https://github.com/vllm-project/vllm/commit/3a386cfaf5) [#52281](https://github.com/vllm-project/vllm/pull/52281) — [ROCm] Give EngineCore cleanup grace after request abort (#52281)
- **2026-08-19** [`583a00257d`](https://github.com/vllm-project/vllm/commit/583a00257d) [#51632](https://github.com/vllm-project/vllm/pull/51632) — [ROCm] [Bugfix] Fix Triton fused shared expert alignment (#51632)
- **2026-08-19** [`17dbd42930`](https://github.com/vllm-project/vllm/commit/17dbd42930) [#37835](https://github.com/vllm-project/vllm/pull/37835) — [ROCm] Add UE8M0 scale packing for Triton silu_mul_quant (#37835)
- **2026-08-19** [`160f7f0840`](https://github.com/vllm-project/vllm/commit/160f7f0840) [#41100](https://github.com/vllm-project/vllm/pull/41100) — [ROCm][CI] Extended Fused MoE and FP8 MoE test support (#41100)
- **2026-08-19** [`eac636a7fa`](https://github.com/vllm-project/vllm/commit/eac636a7fa) [#52131](https://github.com/vllm-project/vllm/pull/52131) — [Frontend] Move api_server.py out openai folder (#52131)
- **2026-08-19** [`b09bd69b5b`](https://github.com/vllm-project/vllm/commit/b09bd69b5b) [#52861](https://github.com/vllm-project/vllm/pull/52861) — [Model][NVIDIA] Route DSA models to the CUDA non-compiled path (#52861)
- **2026-08-18** [`8f4a7f45c5`](https://github.com/vllm-project/vllm/commit/8f4a7f45c5) [#44969](https://github.com/vllm-project/vllm/pull/44969) — [ROCm][CI] Gating more ROCm tests (#44969)
- **2026-08-18** [`aa6abec49a`](https://github.com/vllm-project/vllm/commit/aa6abec49a) [#52810](https://github.com/vllm-project/vllm/pull/52810) — [CI][ROCm] Prevent Git maintenance races during shallow fetches (#52810)
- **2026-08-18** [`203926c477`](https://github.com/vllm-project/vllm/commit/203926c477) [#52822](https://github.com/vllm-project/vllm/pull/52822) — [ROCm][CI] Add AMD CI Pull-Request Commands (#52822)
- **2026-08-18** [`5f7a20b316`](https://github.com/vllm-project/vllm/commit/5f7a20b316) [#52046](https://github.com/vllm-project/vllm/pull/52046) — [nv] add pcp support in dsv3.2 (#52046)
- **2026-08-18** [`6066bb3d50`](https://github.com/vllm-project/vllm/commit/6066bb3d50) [#52763](https://github.com/vllm-project/vllm/pull/52763) — [ROCM][CI] Attention test speedup (#52763)
- **2026-08-18** [`5d8a4cf976`](https://github.com/vllm-project/vllm/commit/5d8a4cf976) [#51647](https://github.com/vllm-project/vllm/pull/51647) — [ROCm] Pad non-aligned AITER MLA heads (#51647)
- **2026-08-18** [`90984ddbed`](https://github.com/vllm-project/vllm/commit/90984ddbed) [#52797](https://github.com/vllm-project/vllm/pull/52797) — [CI] Upgrade huggingface-hub to 1.28.0 (#52797)
- **2026-08-18** [`ad5e71b276`](https://github.com/vllm-project/vllm/commit/ad5e71b276) [#52293](https://github.com/vllm-project/vllm/pull/52293) — [ROCm][Perf] Enable fused KDA decode on gfx942 (MI325X) (#52293)
- **2026-08-18** [`ddbf826bee`](https://github.com/vllm-project/vllm/commit/ddbf826bee) [#51021](https://github.com/vllm-project/vllm/pull/51021) — [ROCm] Gate Torch FP8 scaled-MM on architecture support (#51021)
- **2026-08-18** [`88b2bff2c6`](https://github.com/vllm-project/vllm/commit/88b2bff2c6) [#51695](https://github.com/vllm-project/vllm/pull/51695) — [MOE] Standardize and abstract fused shared expert optimization selection (#51695)
- **2026-08-18** [`41f179b57a`](https://github.com/vllm-project/vllm/commit/41f179b57a) [#52575](https://github.com/vllm-project/vllm/pull/52575) — [Rust Frontend] Simplify data-parallel size ownership (#52575)
- **2026-08-18** [`e8ad2855e7`](https://github.com/vllm-project/vllm/commit/e8ad2855e7) [#52112](https://github.com/vllm-project/vllm/pull/52112) — [Bugfix][ROCm] Fix a few int4/int8 quantization errors (#52112)
- **2026-08-18** [`5fa8ca971a`](https://github.com/vllm-project/vllm/commit/5fa8ca971a) [#40938](https://github.com/vllm-project/vllm/pull/40938) — [ROCm][CI] Move ROCm AITER quantization tests (#40938)
- **2026-08-18** [`c89d692cb5`](https://github.com/vllm-project/vllm/commit/c89d692cb5) [#52593](https://github.com/vllm-project/vllm/pull/52593) — [Build] Propagate vLLM version to Rust binaries (#52593)
- **2026-08-18** [`0e8989b416`](https://github.com/vllm-project/vllm/commit/0e8989b416) [#52625](https://github.com/vllm-project/vllm/pull/52625) — [ROCm] gaurd on_gfx1250 call with rocm platform (#52625)
- **2026-08-17** [`49fb2ee348`](https://github.com/vllm-project/vllm/commit/49fb2ee348) [#52208](https://github.com/vllm-project/vllm/pull/52208) — [ROCm][CI] add Aiter ops tests (#52208)
- **2026-08-17** [`60c3a31b12`](https://github.com/vllm-project/vllm/commit/60c3a31b12) [#52264](https://github.com/vllm-project/vllm/pull/52264) — [CI][AMD] Improve Kubernetes failure diagnostics (#52264)
- **2026-08-17** [`e68fb75b25`](https://github.com/vllm-project/vllm/commit/e68fb75b25) [#51208](https://github.com/vllm-project/vllm/pull/51208) — [ROCm][AMD][Installation] add LMCache kv-connector installation and runtime packages to docker image (#51208)
- **2026-08-17** [`8878ebd8fd`](https://github.com/vllm-project/vllm/commit/8878ebd8fd) [#52647](https://github.com/vllm-project/vllm/pull/52647) — [ROCm][CI] Expand AITER W4A4 MoE Coverage (#52647)
- **2026-08-17** [`c1e438728c`](https://github.com/vllm-project/vllm/commit/c1e438728c) [#52566](https://github.com/vllm-project/vllm/pull/52566) — [ROCm][CI] Restore Torch defaults and type DSV4 scratch buffers (#52566)
- **2026-08-17** [`1d3a8b9e22`](https://github.com/vllm-project/vllm/commit/1d3a8b9e22) [#48998](https://github.com/vllm-project/vllm/pull/48998) — [ROCm][Bugfix] Fix Triton W4A16 bug in determining if transpose is required for GPTQ/AutoGPTQ  (#48998)
- **2026-08-17** [`95901ce70a`](https://github.com/vllm-project/vllm/commit/95901ce70a) [#51823](https://github.com/vllm-project/vllm/pull/51823) — fix(pooling): validate BGE-M3 combined task ownership (#51823)
- **2026-08-17** [`c05d923f18`](https://github.com/vllm-project/vllm/commit/c05d923f18) [#52303](https://github.com/vllm-project/vllm/pull/52303) — [Doc] [ROCm] Update installation documentation (#52303)
- **2026-08-17** [`311b3513af`](https://github.com/vllm-project/vllm/commit/311b3513af) [#52565](https://github.com/vllm-project/vllm/pull/52565) — [ROCm][CI] Avoid forcing FlashAttention in the ColPali pooling test (#52565)
- **2026-08-17** [`71b578b9cc`](https://github.com/vllm-project/vllm/commit/71b578b9cc) [#49514](https://github.com/vllm-project/vllm/pull/49514) — [ROCm][CI] Use the same-build wheel in Python-only CI (#49514)
- **2026-08-17** [`0ad04cff1b`](https://github.com/vllm-project/vllm/commit/0ad04cff1b) [#52256](https://github.com/vllm-project/vllm/pull/52256) — [ROCm][CI] Enable ViT CUDA graph tests on AMD gfx950 GPUs (#52256)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#52885](https://github.com/vllm-project/vllm/issues/52885) | [Bug] Official image crashes on CPUs without AVX because bundled NIXL/ | bug | 2026-08-24 |
| [#52911](https://github.com/vllm-project/vllm/issues/52911) | [RFC]: DeepSeek-V4 Performance Optimization on ROCm (Phase Two) | rocm, RFC, deepseek, DSv4 | 2026-08-24 |
| [#53548](https://github.com/vllm-project/vllm/issues/53548) | [Performance]: higher Mooncake Store tail latency with all-HCA registr | performance | 2026-08-24 |
| [#53428](https://github.com/vllm-project/vllm/issues/53428) | [Bug]: DFlash2 draft models fail to load on main — #52560 reverted the | speculative-decoding | 2026-08-24 |
| [#51581](https://github.com/vllm-project/vllm/issues/51581) | [Bug][Spec Decode]: DFlash fused-KV projection calls F.linear on a sli | quantization | 2026-08-24 |
| [#52803](https://github.com/vllm-project/vllm/issues/52803) | [ROCm][AMD] Kimi-K3 gfx942 / MI325X Gap and Roadmap | rocm, quantization, kimi, k3 | 2026-08-24 |
| [#53363](https://github.com/vllm-project/vllm/issues/53363) | [Bug]: tool_choice="required" not enforced with gemma4 tool parser — p | tool-calling | 2026-08-24 |
| [#53049](https://github.com/vllm-project/vllm/issues/53049) | [Bug]: MultiConnector: finished_recving lacks per-connector dedup — la | bug, scheduler | 2026-08-24 |
| [#53505](https://github.com/vllm-project/vllm/issues/53505) | [Bug]: [SpecDecode] Hybrid Mamba (align) corrupts under speculative de | bug, speculative-decoding | 2026-08-24 |
| [#53488](https://github.com/vllm-project/vllm/issues/53488) | [Bug]: `prompt_logprobs` silently corrupted for some requests when MTP | speculative-decoding, quantization | 2026-08-24 |
| [#53343](https://github.com/vllm-project/vllm/issues/53343) | [RFC]: Sleep Mode Tensor Ownership and Recovery | RFC, quantization | 2026-08-24 |
| [#43456](https://github.com/vllm-project/vllm/issues/43456) | [deepseek_v4] DeepSeekV4MTP loader silently skips top-level head.weigh | stale | 2026-08-24 |
| [#43545](https://github.com/vllm-project/vllm/issues/43545) | [RFC]: Add Gumiho speculative decoding to vLLM | RFC, stale | 2026-08-24 |
| [#43563](https://github.com/vllm-project/vllm/issues/43563) | [Usage]: Intel Xeon Prefill Decode Disaggregation | usage, stale | 2026-08-24 |
| [#53194](https://github.com/vllm-project/vllm/issues/53194) | [RFC]: A conformance suite for KV-cache key partitioning | RFC | 2026-08-24 |
| [#53192](https://github.com/vllm-project/vllm/issues/53192) | [RFC]: V1/V2 Weight Reload with Streaming Quantization Units | quantization, kimi, k3 | 2026-08-24 |
| [#53485](https://github.com/vllm-project/vllm/issues/53485) | [RFC]: Reconcile Backpressure Admission | RFC | 2026-08-23 |
| [#53484](https://github.com/vllm-project/vllm/issues/53484) | [RFC]: Generalize Connector Metrics | RFC | 2026-08-23 |
| [#53481](https://github.com/vllm-project/vllm/issues/53481) | [Bug]: FLASHINFER backend produces degenerate output for Mistral3 (Min | mistral | 2026-08-23 |
| [#53462](https://github.com/vllm-project/vllm/issues/53462) | [Bug]: GDN MTP fused decode kernel (fused_gdn_decode_post_conv_mtp) cr | — | 2026-08-23 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 61 |
| Attention | 41 |
| MoE / Expert Parallel | 39 |
| Multimodal | 27 |
| Other | 24 |
| CI / Build | 20 |
| Models | 16 |
| Serving / API | 15 |
| Scheduler / Engine | 13 |
| Disaggregation / PD | 10 |
| Speculative Decoding | 9 |
| LoRA | 8 |
| Perf / Benchmark | 7 |
| Quantization | 6 |
| Docs | 5 |
| Compilation / CUDA Graph | 4 |
| KV Cache / Offload | 2 |
| Distributed | 1 |

## ROCm / AMD  (61 commits)

- **2026-08-23** [`d569e71bd0`](https://github.com/vllm-project/vllm/commit/d569e71bd0) [#52547](https://github.com/vllm-project/vllm/pull/52547)
  [CI][AMD] Honor single-node Docker workload timeout (#52547)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-08-23** [`30b34171b1`](https://github.com/vllm-project/vllm/commit/30b34171b1) [#53351](https://github.com/vllm-project/vllm/pull/53351)
  [ROCm][CI] Restore attention coverage after KV-cache layout refactor (#53351)
  _Files: `tests/kernels/attention/test_minimax_m3.py`, `tests/v1/attention/test_attention_backends.py`, `tests/v1/attention/test_mla_backends.py`_
- **2026-08-22** [`610bfc58e9`](https://github.com/vllm-project/vllm/commit/610bfc58e9) [#53182](https://github.com/vllm-project/vllm/pull/53182)
  [ROCm] Ship rocprofiler-sdk 1.3.2 in Dockerfile.rocm_base to fix torch.profiler traces (#53182)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-08-22** [`7f4a1b7e24`](https://github.com/vllm-project/vllm/commit/7f4a1b7e24) [#53110](https://github.com/vllm-project/vllm/pull/53110)
  [Bugfix][ROCM] Fix the MXFP8 block scale exponent (#53110)
  _Files: `vllm/model_executor/layers/quantization/utils/mxfp8_utils.py`_
- **2026-08-21** [`f37d5868b9`](https://github.com/vllm-project/vllm/commit/f37d5868b9) [#53117](https://github.com/vllm-project/vllm/pull/53117)
  [CI/Build][ROCm] Run the TileLang HIP symbol checks in their own interpreter (#53117)
  _Files: `tests/kernels/scripts/check_no_tilelang_hijack.py`, `tests/kernels/test_mhc_tilelang_jit.py`_
- **2026-08-21** [`592e06f2ae`](https://github.com/vllm-project/vllm/commit/592e06f2ae) [#53294](https://github.com/vllm-project/vllm/pull/53294)
  Revert "[ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill" (#53294)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+5 more__
- **2026-08-21** [`29b7c2f7d4`](https://github.com/vllm-project/vllm/commit/29b7c2f7d4) [#52854](https://github.com/vllm-project/vllm/pull/52854)
  [ROCm][CI] aiter kernel ops - enable rope test (#52854)
  _Files: `tests/kernels/core/test_rocm_aiter_ops.py`_
- **2026-08-21** [`a0af854f5d`](https://github.com/vllm-project/vllm/commit/a0af854f5d) [#53024](https://github.com/vllm-project/vllm/pull/53024)
  [ROCm][CI] Stabilize MI355 FlyDSL MoE accuracy test (#53024)
  _Files: `tests/kernels/moe/test_flydsl_moe.py`_
- **2026-08-21** [`b5f7fcc79d`](https://github.com/vllm-project/vllm/commit/b5f7fcc79d) [#53177](https://github.com/vllm-project/vllm/pull/53177)
  [ROCm][CI] Add float16 dtype and unsupported head size tests for paged attention (#53177)
  _Files: `tests/kernels/attention/test_attention.py`_
- **2026-08-21** [`88eb946cb1`](https://github.com/vllm-project/vllm/commit/88eb946cb1) [#53025](https://github.com/vllm-project/vllm/pull/53025)
  [ROCm][CI] Stabilize MI355 FusedMoE test group (#53025)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_moe_layer.py`_
- **2026-08-21** [`f15ea66b30`](https://github.com/vllm-project/vllm/commit/f15ea66b30) [#53268](https://github.com/vllm-project/vllm/pull/53268)
  [ROCm][Test] Use platform FP8 dtype in ModelOpt FP8_PB_WO test (#53268)
  _Files: `tests/quantization/test_modelopt.py`_
- **2026-08-21** [`7a2fdbaac4`](https://github.com/vllm-project/vllm/commit/7a2fdbaac4) [#53152](https://github.com/vllm-project/vllm/pull/53152)
  [K3 Perf] Fuse MXFP4 top-k finalization into latent-tail, ~5% E2E latency reduction (#53152)
  _Files: `benchmarks/kernels/benchmark_kimi_k3_latent_moe_tail.py`, `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py` _+13 more__
- **2026-08-21** [`fe76112ff2`](https://github.com/vllm-project/vllm/commit/fe76112ff2) [#52882](https://github.com/vllm-project/vllm/pull/52882)
  [ROCm][Perf] Optimize DeepSeek V4 C4A top-k with AITER (#52882)
  _Files: `csrc/libtorch_stable/sampler.cu`, `tests/kernels/test_top_k_per_row.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/deepseek_v4/attention.py` _+1 more__
- **2026-08-21** [`463aa5e30f`](https://github.com/vllm-project/vllm/commit/463aa5e30f) [#52606](https://github.com/vllm-project/vllm/pull/52606)
  [ROCm][Perf] Kimi-K3 Fused kernels for KDA prefill (#52606)
  _Files: `CMakeLists.txt`, `csrc/libtorch_stable/kimi_k3/fused_kda_chunk_kernel_rocm.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+5 more__
- **2026-08-21** [`cd7b7c265a`](https://github.com/vllm-project/vllm/commit/cd7b7c265a) [#43018](https://github.com/vllm-project/vllm/pull/43018)
  [ROCm] Cpu offload for ROCm 7.13+ to align the hipMemcpyBatchAsync params and perf in 7.14x (#43018)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `tests/v1/simple_kv_offload/test_hip_mem_ops.py`, `vllm/envs.py`, `vllm/v1/simple_kv_offload/cuda_mem_ops.py`_
- **2026-08-21** [`83c5d59209`](https://github.com/vllm-project/vllm/commit/83c5d59209) [#52892](https://github.com/vllm-project/vllm/pull/52892)
  [Rust Frontend] Replace external `protoc` with pure Rust lib `protox` (#52892)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/scripts/build-macos-wheel.sh`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/run-rust-frontend-cargo-ci.sh` _+10 more__
- **2026-08-20** [`3b829cf176`](https://github.com/vllm-project/vllm/commit/3b829cf176) [#53113](https://github.com/vllm-project/vllm/pull/53113)
  [CI/Build][ROCm] Keep the CUDA-only kernel tests out of the ROCm run (#53113)
  _Files: `tests/kernels/test_fp32_router_gemm.py`, `tests/kernels/test_kimi_k3_gemm_rs.py`_
- **2026-08-20** [`1fe3a1571a`](https://github.com/vllm-project/vllm/commit/1fe3a1571a) [#53106](https://github.com/vllm-project/vllm/pull/53106)
  Reduce `AutoWeightsLoader` kwargs (#53106)
  _Files: `tests/models/inkling/test_moe_weight_layout.py`, `tests/models/test_dspark_mla.py`, `tests/models/test_utils.py`, `tests/quantization/test_modelopt.py` _+80 more__
- **2026-08-20** [`f0c14b4f77`](https://github.com/vllm-project/vllm/commit/f0c14b4f77) [#51665](https://github.com/vllm-project/vllm/pull/51665)
  Fix weight tying (#51665)
  _Files: `tests/model_executor/model_loader/test_weight_tying.py`, `tests/models/test_utils.py`, `tests/test_config.py`, `tests/transformers_utils/test_config.py` _+66 more__
- **2026-08-20** [`1eab6fef01`](https://github.com/vllm-project/vllm/commit/1eab6fef01) [#52572](https://github.com/vllm-project/vllm/pull/52572)
  [CI] replace shellcheck script with shellcheck-py hook (#52572)
  _Files: `.buildkite/scripts/ci-fetch-log.sh`, `.buildkite/scripts/docker-build-metadata-args.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/scripts/publish-release-images.sh` _+16 more__
- **2026-08-20** [`6b68db441e`](https://github.com/vllm-project/vllm/commit/6b68db441e) [#50803](https://github.com/vllm-project/vllm/pull/50803)
  [ROCm] Fix DeepSeek V4 indexer numerics and coverage (#50803)
  _Files: `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_indexer_q_rope_quant.py`, `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`_
- **2026-08-20** [`5d4d470470`](https://github.com/vllm-project/vllm/commit/5d4d470470) [#53026](https://github.com/vllm-project/vllm/pull/53026)
  [CI] Fix nonexistent dependency for data-parallel example test selection (#53026)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`_
- **2026-08-20** [`4666a8ba9e`](https://github.com/vllm-project/vllm/commit/4666a8ba9e) [#53064](https://github.com/vllm-project/vllm/pull/53064)
  [Refactor] Remove InputPreprocessor (#53064)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `.github/CODEOWNERS`, `tests/renderers/test_process_multi_modal_uuids.py` _+4 more__
- **2026-08-20** [`d626108b18`](https://github.com/vllm-project/vllm/commit/d626108b18) [#52737](https://github.com/vllm-project/vllm/pull/52737)
  [ROCm][Perf] Fuse DeepSeek-V4 mHC post/pre and RMSNorm with AITER (#52737)
  _Files: `vllm/_aiter_ops.py`, `vllm/model_executor/kernels/mhc/aiter.py`, `vllm/model_executor/layers/mhc.py`, `vllm/models/deepseek_v4/amd/dspark.py` _+1 more__
- **2026-08-20** [`cd5035379c`](https://github.com/vllm-project/vllm/commit/cd5035379c) [#51585](https://github.com/vllm-project/vllm/pull/51585)
  [ROCm] [Bugfix] Preserve CPU query offsets during capture (#51585)
  _Files: `vllm/v1/attention/backends/rocm_attn.py`_
- **2026-08-20** [`4f66bc3e0d`](https://github.com/vllm-project/vllm/commit/4f66bc3e0d) [#52976](https://github.com/vllm-project/vllm/pull/52976)
  [CI][ROCm] Standardize AMD test job labels by device (#52976)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/models_multimodal.yaml`, `tests/models/test_vision.py`_
- **2026-08-20** [`fbb4c04db4`](https://github.com/vllm-project/vllm/commit/fbb4c04db4) [#53004](https://github.com/vllm-project/vllm/pull/53004)
  [ROCm][CI] Speed up `test_rocm_aiter_qk_norm_rope_kvcache_fusion` (#53004)
  _Files: `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`_
- **2026-08-19** [`823ec22b78`](https://github.com/vllm-project/vllm/commit/823ec22b78) [#52819](https://github.com/vllm-project/vllm/pull/52819)
  [ROCm]: Bump triton 3.7 commit (#52819)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-08-19** [`480d4f0d15`](https://github.com/vllm-project/vllm/commit/480d4f0d15) [#46434](https://github.com/vllm-project/vllm/pull/46434)
  [ROCm][CI] Enable modular OAI Triton MoE tests (#46434)
  _Files: `tests/kernels/moe/test_modular_oai_triton_moe.py`_
- **2026-08-19** [`3a386cfaf5`](https://github.com/vllm-project/vllm/commit/3a386cfaf5) [#52281](https://github.com/vllm-project/vllm/pull/52281)
  [ROCm] Give EngineCore cleanup grace after request abort (#52281)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `tests/v1/engine/test_startup_watch_processes.py`, `vllm/entrypoints/openai/dp_supervisor.py`, `vllm/v1/engine/core.py` _+1 more__
- **2026-08-19** [`583a00257d`](https://github.com/vllm-project/vllm/commit/583a00257d) [#51632](https://github.com/vllm-project/vllm/pull/51632)
  [ROCm] [Bugfix] Fix Triton fused shared expert alignment (#51632)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-08-19** [`17dbd42930`](https://github.com/vllm-project/vllm/commit/17dbd42930) [#37835](https://github.com/vllm-project/vllm/pull/37835)
  [ROCm] Add UE8M0 scale packing for Triton silu_mul_quant (#37835)
  _Files: `tests/kernels/moe/test_silu_mul_fp8_quant_deep_gemm.py`, `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`_
- **2026-08-19** [`160f7f0840`](https://github.com/vllm-project/vllm/commit/160f7f0840) [#41100](https://github.com/vllm-project/vllm/pull/41100)
  [ROCm][CI] Extended Fused MoE and FP8 MoE test support (#41100)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/moe/test_modular_oai_triton_moe.py`, `tests/kernels/moe/test_moe.py` _+5 more__
- **2026-08-19** [`eac636a7fa`](https://github.com/vllm-project/vllm/commit/eac636a7fa) [#52131](https://github.com/vllm-project/vllm/pull/52131)
  [Frontend] Move api_server.py out openai folder (#52131)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docs/deployment/integrations/kthena.md` _+39 more__
- **2026-08-19** [`b09bd69b5b`](https://github.com/vllm-project/vllm/commit/b09bd69b5b) [#52861](https://github.com/vllm-project/vllm/pull/52861)
  [Model][NVIDIA] Route DSA models to the CUDA non-compiled path (#52861)
  _Files: `tests/compile/fusions_e2e/conftest.py`, `tests/compile/fusions_e2e/models.py`, `tests/compile/fusions_e2e/test_tp1_quant.py`, `tests/compile/fusions_e2e/test_tp2_ar_rms.py` _+12 more__
- **2026-08-18** [`8f4a7f45c5`](https://github.com/vllm-project/vllm/commit/8f4a7f45c5) [#44969](https://github.com/vllm-project/vllm/pull/44969)
  [ROCm][CI] Gating more ROCm tests (#44969)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lora.yaml`, `.buildkite/test_areas/misc.yaml` _+7 more__
- **2026-08-18** [`aa6abec49a`](https://github.com/vllm-project/vllm/commit/aa6abec49a) [#52810](https://github.com/vllm-project/vllm/pull/52810)
  [CI][ROCm] Prevent Git maintenance races during shallow fetches (#52810)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `tests/tools/test_docker_build_metadata_args.py`_
- **2026-08-18** [`203926c477`](https://github.com/vllm-project/vllm/commit/203926c477) [#52822](https://github.com/vllm-project/vllm/pull/52822)
  [ROCm][CI] Add AMD CI Pull-Request Commands (#52822)
  _Files: `.github/workflows/new_pr_bot.yml`, `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py` _+1 more__
- **2026-08-18** [`5f7a20b316`](https://github.com/vllm-project/vllm/commit/5f7a20b316) [#52046](https://github.com/vllm-project/vllm/pull/52046)
  [nv] add pcp support in dsv3.2 (#52046)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/models/deepseek_v32/attention.py` _+2 more__
- **2026-08-18** [`6066bb3d50`](https://github.com/vllm-project/vllm/commit/6066bb3d50) [#52763](https://github.com/vllm-project/vllm/pull/52763)
  [ROCM][CI] Attention test speedup (#52763)
  _Files: `tests/kernels/attention/test_attention.py`, `tests/kernels/attention/test_cache.py`, `tests/kernels/attention/test_cutlass_mla_decode.py`, `tests/kernels/attention/test_flashmla.py` _+5 more__
- **2026-08-18** [`5d8a4cf976`](https://github.com/vllm-project/vllm/commit/5d8a4cf976) [#51647](https://github.com/vllm-project/vllm/pull/51647)
  [ROCm] Pad non-aligned AITER MLA heads (#51647)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_head_padding.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`_
- **2026-08-18** [`90984ddbed`](https://github.com/vllm-project/vllm/commit/90984ddbed) [#52797](https://github.com/vllm-project/vllm/pull/52797)
  [CI] Upgrade huggingface-hub to 1.28.0 (#52797)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+1 more__
- **2026-08-18** [`ad5e71b276`](https://github.com/vllm-project/vllm/commit/ad5e71b276) [#52293](https://github.com/vllm-project/vllm/pull/52293)
  [ROCm][Perf] Enable fused KDA decode on gfx942 (MI325X) (#52293)
  _Files: `CMakeLists.txt`, `tests/models/kimi_k3/test_amd_kda_decode.py`, `vllm/models/kimi_k3/amd/ops/kda_decode.py`_
- **2026-08-18** [`ddbf826bee`](https://github.com/vllm-project/vllm/commit/ddbf826bee) [#51021](https://github.com/vllm-project/vllm/pull/51021)
  [ROCm] Gate Torch FP8 scaled-MM on architecture support (#51021)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py`_
- **2026-08-18** [`88b2bff2c6`](https://github.com/vllm-project/vllm/commit/88b2bff2c6) [#51695](https://github.com/vllm-project/vllm/pull/51695)
  [MOE] Standardize and abstract fused shared expert optimization selection (#51695)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/model_executor/layers/fused_moe/layer.py`, `vllm/model_executor/layers/fused_moe/utils.py`, `vllm/model_executor/layers/quantization/quark/quark.py` _+16 more__
- **2026-08-18** [`41f179b57a`](https://github.com/vllm-project/vllm/commit/41f179b57a) [#52575](https://github.com/vllm-project/vllm/pull/52575)
  [Rust Frontend] Simplify data-parallel size ownership (#52575)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `rust/src/cmd/src/cli.rs` _+15 more__
- **2026-08-18** [`e8ad2855e7`](https://github.com/vllm-project/vllm/commit/e8ad2855e7) [#52112](https://github.com/vllm-project/vllm/pull/52112)
  [Bugfix][ROCm] Fix a few int4/int8 quantization errors (#52112)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16.py`, `vllm/model_executor/layers/quantization/moe_wna16.py`_
- **2026-08-18** [`5fa8ca971a`](https://github.com/vllm-project/vllm/commit/5fa8ca971a) [#40938](https://github.com/vllm-project/vllm/pull/40938)
  [ROCm][CI] Move ROCm AITER quantization tests (#40938)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/kernels.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_fp8_support.py`, `tests/kernels/quantization/test_aiter_hipb_mm_linear_kernel.py` _+3 more__
- **2026-08-18** [`c89d692cb5`](https://github.com/vllm-project/vllm/commit/c89d692cb5) [#52593](https://github.com/vllm-project/vllm/pull/52593)
  [Build] Propagate vLLM version to Rust binaries (#52593)
  _Files: `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/rust_frontend.yaml`, `docker/Dockerfile` _+20 more__
- **2026-08-18** [`0e8989b416`](https://github.com/vllm-project/vllm/commit/0e8989b416) [#52625](https://github.com/vllm-project/vllm/pull/52625)
  [ROCm] gaurd on_gfx1250 call with rocm platform (#52625)
  _Files: `vllm/model_executor/layers/quantization/utils/fp8_utils.py`_
- **2026-08-17** [`49fb2ee348`](https://github.com/vllm-project/vllm/commit/49fb2ee348) [#52208](https://github.com/vllm-project/vllm/pull/52208)
  [ROCm][CI] add Aiter ops tests (#52208)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/core/test_rocm_aiter_ops.py`, `vllm/_aiter_ops.py`_
- **2026-08-17** [`60c3a31b12`](https://github.com/vllm-project/vllm/commit/60c3a31b12) [#52264](https://github.com/vllm-project/vllm/pull/52264)
  [CI][AMD] Improve Kubernetes failure diagnostics (#52264)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-08-17** [`e68fb75b25`](https://github.com/vllm-project/vllm/commit/e68fb75b25) [#51208](https://github.com/vllm-project/vllm/pull/51208)
  [ROCm][AMD][Installation] add LMCache kv-connector installation and runtime packages to docker image (#51208)
  _Files: `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/ci-bake-rocm.sh`, `docker/Dockerfile.rocm`_
- **2026-08-17** [`8878ebd8fd`](https://github.com/vllm-project/vllm/commit/8878ebd8fd) [#52647](https://github.com/vllm-project/vllm/pull/52647)
  [ROCm][CI] Expand AITER W4A4 MoE Coverage (#52647)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `tests/quantization/test_gfx950_moe.py`_
- **2026-08-17** [`c1e438728c`](https://github.com/vllm-project/vllm/commit/c1e438728c) [#52566](https://github.com/vllm-project/vllm/pull/52566)
  [ROCm][CI] Restore Torch defaults and type DSV4 scratch buffers (#52566)
  _Files: `tests/kernels/attention/test_mha_attn.py`, `tests/kernels/attention/test_rocm_triton_attn_dsv4.py`_
- **2026-08-17** [`1d3a8b9e22`](https://github.com/vllm-project/vllm/commit/1d3a8b9e22) [#48998](https://github.com/vllm-project/vllm/pull/48998)
  [ROCm][Bugfix] Fix Triton W4A16 bug in determining if transpose is required for GPTQ/AutoGPTQ  (#48998)
  _Files: `tests/kernels/quantization/test_triton_w4a16.py`, `vllm/model_executor/kernels/linear/mixed_precision/triton_w4a16.py`_
- **2026-08-17** [`95901ce70a`](https://github.com/vllm-project/vllm/commit/95901ce70a) [#51823](https://github.com/vllm-project/vllm/pull/51823)
  fix(pooling): validate BGE-M3 combined task ownership (#51823)
  _Files: `docs/models/pooling_models/specific_models.md`, `tests/entrypoints/pooling/test_factories.py`, `vllm/entrypoints/pooling/factories.py`, `vllm/entrypoints/pooling/pooling/io_processor.py`_
- **2026-08-17** [`c05d923f18`](https://github.com/vllm-project/vllm/commit/c05d923f18) [#52303](https://github.com/vllm-project/vllm/pull/52303)
  [Doc] [ROCm] Update installation documentation (#52303)
  _Files: `docs/getting_started/installation/gpu.rocm.inc.md`_
- **2026-08-17** [`311b3513af`](https://github.com/vllm-project/vllm/commit/311b3513af) [#52565](https://github.com/vllm-project/vllm/pull/52565)
  [ROCm][CI] Avoid forcing FlashAttention in the ColPali pooling test (#52565)
  _Files: `tests/models/multimodal/pooling/test_colpali.py`_
- **2026-08-17** [`71b578b9cc`](https://github.com/vllm-project/vllm/commit/71b578b9cc) [#49514](https://github.com/vllm-project/vllm/pull/49514)
  [ROCm][CI] Use the same-build wheel in Python-only CI (#49514)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/standalone_tests/python_only_compile.sh`_
- **2026-08-17** [`0ad04cff1b`](https://github.com/vllm-project/vllm/commit/0ad04cff1b) [#52256](https://github.com/vllm-project/vllm/pull/52256)
  [ROCm][CI] Enable ViT CUDA graph tests on AMD gfx950 GPUs (#52256)
  _Files: `.buildkite/test-amd.yaml`, `docs/design/cuda_graphs_multimodal.md`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `tests/v1/cudagraph/test_encoder_cudagraph.py`_

## Attention  (41 commits)

- **2026-08-24** [`e6e1af4ca1`](https://github.com/vllm-project/vllm/commit/e6e1af4ca1) [#53318](https://github.com/vllm-project/vllm/pull/53318)
  [Perf] Tune FlashInfer all-reduce selection on SM103 (#53318)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/all_reduce_utils.py`, `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_
- **2026-08-23** [`185cada36b`](https://github.com/vllm-project/vllm/commit/185cada36b) [#53460](https://github.com/vllm-project/vllm/pull/53460)
  [Model] Fix KV cache layout and optimize Dots3 NOTE Omni encoders (#53460)
  _Files: `vllm/models/dots3_note/nvidia/attention.py`, `vllm/models/dots3_note/nvidia/audio.py`, `vllm/models/dots3_note/nvidia/multimodal.py`, `vllm/models/dots3_note/nvidia/vision.py` _+1 more__
- **2026-08-22** [`bbe8b23e1a`](https://github.com/vllm-project/vllm/commit/bbe8b23e1a) [#52557](https://github.com/vllm-project/vllm/pull/52557)
  [Deprecation] Remove dead use_prefill_decode_attention flag (#52557)
  _Files: `tests/engine/test_arg_utils.py`, `tests/v1/attention/utils.py`, `vllm/config/attention.py`_
- **2026-08-22** [`9eb9d9d395`](https://github.com/vllm-project/vllm/commit/9eb9d9d395) [#52789](https://github.com/vllm-project/vllm/pull/52789)
  [Perf] Support internal prefill checkpoints for Mamba prefix caching, 9%~25% TTFT improvement (#52789)
  _Files: `cmake/external_projects/flashkda.cmake`, `csrc/flashkda_registration.cpp`, `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py` _+8 more__
- **2026-08-22** [`9ff7041b55`](https://github.com/vllm-project/vllm/commit/9ff7041b55) [#53002](https://github.com/vllm-project/vllm/pull/53002)
  [Bugfix][Spec Decode] Use group geometry for FlashAttention metadata (#53002)
  _Files: `tests/v1/attention/test_group_head_counts.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/backends/utils.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-08-21** [`d6c2fec9fd`](https://github.com/vllm-project/vllm/commit/d6c2fec9fd) [#53139](https://github.com/vllm-project/vllm/pull/53139)
  [Cleanup][MLA] Remove FlashInfer DSpark DCP support (#53139)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-08-21** [`d9e0ace7a0`](https://github.com/vllm-project/vllm/commit/d9e0ace7a0) [#53111](https://github.com/vllm-project/vllm/pull/53111)
  [Bugfix][Attention] Fall back to native FlashInfer decode when XQA cannot serve a KV-cache group's head_dim (#53111)
  _Files: `vllm/v1/attention/backends/flashinfer.py`_
- **2026-08-21** [`72aedcc426`](https://github.com/vllm-project/vllm/commit/72aedcc426) [#50382](https://github.com/vllm-project/vllm/pull/50382)
  [DCP] Default query replication for GLM sparse attention (#50382)
  _Files: `tests/distributed/test_dcp_a2a.py`, `vllm/config/parallel.py`, `vllm/config/vllm.py`, `vllm/engine/arg_utils.py` _+2 more__
- **2026-08-21** [`574e6a00ef`](https://github.com/vllm-project/vllm/commit/574e6a00ef) [#52796](https://github.com/vllm-project/vllm/pull/52796)
  [Bugfix][Attention] Normalize FlashInfer prefill LSE before merging (#52796)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/v1/attention/backends/flashinfer.py`, `vllm/v1/attention/backends/mla/prefill/flashinfer.py`, `vllm/v1/attention/backends/mla/prefill/trtllm_ragged.py` _+1 more__
- **2026-08-21** [`b389ac2946`](https://github.com/vllm-project/vllm/commit/b389ac2946) [#52816](https://github.com/vllm-project/vllm/pull/52816)
  [Spec Decode] DFlash2: local convolution + candidate selector (#52816)
  _Files: `tests/models/registry.py`, `tests/test_config.py`, `tests/v1/spec_decode/test_dflash2.py`, `tests/v1/spec_decode/test_dflash_causality.py` _+10 more__
- **2026-08-21** [`2785c72a14`](https://github.com/vllm-project/vllm/commit/2785c72a14) [#53053](https://github.com/vllm-project/vllm/pull/53053)
  [Kimi-K3] Extend GEMM-RS to GEMM-AR (#53053)
  _Files: `.buildkite/test_areas/distributed.yaml`, `benchmarks/kernels/benchmark_kimi_k3_gemm_rs_ar.py`, `tests/kernels/test_kimi_k3_gemm_rs_ar.py`, `vllm/envs.py` _+5 more__
- **2026-08-21** [`5df31ea52d`](https://github.com/vllm-project/vllm/commit/5df31ea52d) [#52795](https://github.com/vllm-project/vllm/pull/52795)
  [Spec Decode] Enable adaptive verification on DSv4 + sm90 (#52795)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-08-20** [`7c8b68b9ce`](https://github.com/vllm-project/vllm/commit/7c8b68b9ce) [#51203](https://github.com/vllm-project/vllm/pull/51203)
  [Bugfix][MiniMax-M3] Keep FP8 query allocation stable across CUDA graph replay (#51203)
  _Files: `tests/kernels/attention/test_minimax_m3_msa_cutlass_sparse_decode.py`, `vllm/models/minimax_m3/nvidia/model.py`_
- **2026-08-20** [`2dd17225c6`](https://github.com/vllm-project/vllm/commit/2dd17225c6) [#52766](https://github.com/vllm-project/vllm/pull/52766)
  Fix Transformers modelling backend `RMSNormFuser.fuse` performance (#52766)
  _Files: `tests/models/transformers/fusers/test_rms_norm.py`, `vllm/model_executor/models/transformers/fusers/mla.py`, `vllm/model_executor/models/transformers/fusers/rms_norm.py`_
- **2026-08-20** [`bd8865a299`](https://github.com/vllm-project/vllm/commit/bd8865a299) [#52204](https://github.com/vllm-project/vllm/pull/52204)
  [Kernel] Add FlashInfer TRTLLM MXFP8 linear backend (#52204)
  _Files: `docs/features/quantization/modelopt.md`, `tests/kernels/quantization/test_flashinfer_mxfp8_trtllm.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py` _+1 more__
- **2026-08-20** [`6df7adc17f`](https://github.com/vllm-project/vllm/commit/6df7adc17f) [#53077](https://github.com/vllm-project/vllm/pull/53077)
  [Bugfix][GDN] Reset speculative decode count for an empty draft schedule (#53077)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-08-20** [`30e2394c83`](https://github.com/vllm-project/vllm/commit/30e2394c83) [#51703](https://github.com/vllm-project/vllm/pull/51703)
  [Bugfix] Record non-ImportError attention backend probe failures instead of crashing engine init (#51703)
  _Files: `tests/v1/attention/test_cuda_backend_probe_errors.py`, `vllm/platforms/cuda.py`_
- **2026-08-20** [`11baa0ebd8`](https://github.com/vllm-project/vllm/commit/11baa0ebd8) [#52078](https://github.com/vllm-project/vllm/pull/52078)
  [Attention] Avoid redundant mask compute in GDN metadata build (#52078)
  _Files: `vllm/v1/attention/backends/gdn_attn.py`_
- **2026-08-20** [`c0233fcf01`](https://github.com/vllm-project/vllm/commit/c0233fcf01) [#53021](https://github.com/vllm-project/vllm/pull/53021)
  [Model] Remove unused DeepseekV32Indexer forward (#53021)
  _Files: `vllm/models/deepseek_v32/attention.py`_
- **2026-08-20** [`6a962071bd`](https://github.com/vllm-project/vllm/commit/6a962071bd) [#52998](https://github.com/vllm-project/vllm/pull/52998)
  [Distributed] Enable FlashInfer all-reduce by default (#52998)
  _Files: `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/envs.py`_
- **2026-08-20** [`58e5ee0158`](https://github.com/vllm-project/vllm/commit/58e5ee0158) [#52839](https://github.com/vllm-project/vllm/pull/52839)
  [refactor] consolidate cp attn ops (#52839)
  _Files: `tests/distributed/test_dcp_a2a.py`, `tests/distributed/test_dcp_direct_a2a_lse_reduce.py`, `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_indexer_dcp_localize.py` _+14 more__
- **2026-08-19** [`755492e37d`](https://github.com/vllm-project/vllm/commit/755492e37d) [#52987](https://github.com/vllm-project/vllm/pull/52987)
  Revert "[Kernel] Gemma-4 FA4 FP8 Kernel" (#52987)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `vllm/model_executor/layers/attention/attention.py`, `vllm/platforms/interface.py`, `vllm/v1/attention/backend.py` _+4 more__
- **2026-08-19** [`e9e1630e93`](https://github.com/vllm-project/vllm/commit/e9e1630e93) [#52948](https://github.com/vllm-project/vllm/pull/52948)
  [Model] Support bidirectional (encoder-only) attention for DeepSeek e… (#52948)
  _Files: `tests/models/registry.py`, `vllm/config/model.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/registry.py`_
- **2026-08-19** [`525b7bbb3a`](https://github.com/vllm-project/vllm/commit/525b7bbb3a) [#49688](https://github.com/vllm-project/vllm/pull/49688)
  [Bugfix][CPU] Enable C++ causal_conv1d GDN path and float32 SSM cache on non-AMX AVX-512BF16 CPUs (#49688)
  _Files: `tests/kernels/mamba/cpu/test_cpu_gdn_ops.py`, `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`, `vllm/model_executor/layers/utils.py`, `vllm/platforms/cpu.py`_
- **2026-08-19** [`63ff748f65`](https://github.com/vllm-project/vllm/commit/63ff748f65) [#46514](https://github.com/vllm-project/vllm/pull/46514)
  [Attention][MLA] FlashMLA sparse: DCP on the fp8_ds_mla mixed-batch path + MTP (#46514)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashmla.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-08-19** [`8e46accab2`](https://github.com/vllm-project/vllm/commit/8e46accab2) [#52217](https://github.com/vllm-project/vllm/pull/52217)
  [Attention] Vectorize sparse MLA mask loads (#52217)
  _Files: `tests/v1/attention/test_sparse_mla_mask.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`, `vllm/model_executor/layers/attention/sparse_mla_mask.py`_
- **2026-08-19** [`e4d61d0d22`](https://github.com/vllm-project/vllm/commit/e4d61d0d22) [#52616](https://github.com/vllm-project/vllm/pull/52616)
  [CPU] Add AMX-only high-performance MLA backend for DeepSeek V2/V3/R1 (#52616)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `cmake/cpu_extension.cmake`, `csrc/cpu/sgl-kernels/bmm.cpp`, `csrc/cpu/sgl-kernels/decode.cpp` _+16 more__
- **2026-08-19** [`f1178f3a06`](https://github.com/vllm-project/vllm/commit/f1178f3a06) [#52836](https://github.com/vllm-project/vllm/pull/52836)
  Revert DSv4 eager workspace reuse (#52836)
  _Files: `csrc/libtorch_stable/fused_deepseek_v4_qnorm_rope_kv_insert_kernel.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/kernels/test_compressor_kv_cache.py` _+11 more__
- **2026-08-18** [`8d6b18329a`](https://github.com/vllm-project/vllm/commit/8d6b18329a) [#52659](https://github.com/vllm-project/vllm/pull/52659)
  [CI] Standardize test job labels by device (#52659)
  _Files: `.buildkite/test_areas/attention.yaml`, `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/compile.yaml` _+31 more__
- **2026-08-18** [`6948a43fbb`](https://github.com/vllm-project/vllm/commit/6948a43fbb) [#52161](https://github.com/vllm-project/vllm/pull/52161)
  [Bugfix] Detect all attention-spelling variants in ModelConfig.is_hybrid (#52161)
  _Files: `vllm/config/model.py`_
- **2026-08-18** [`01e56caaf2`](https://github.com/vllm-project/vllm/commit/01e56caaf2) [#52512](https://github.com/vllm-project/vllm/pull/52512)
  [Bugfix][MLA] Do not use Dense MHA for GLM-5.2 (#52512)
  _Files: `tests/model_executor/layers/test_mla_short_prefill_indexer.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/models/deepseek_v32/attention.py`_
- **2026-08-18** [`689be2bcd3`](https://github.com/vllm-project/vllm/commit/689be2bcd3) [#52681](https://github.com/vllm-project/vllm/pull/52681)
  Upgrade Flashinfer version to 0.6.17 (#52681)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`_
- **2026-08-18** [`69d3335066`](https://github.com/vllm-project/vllm/commit/69d3335066) [#52648](https://github.com/vllm-project/vllm/pull/52648)
  [Bugfix][Quantization] Guard the MXFP8 FlashInfer path on FlashInfer availability (#52648)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/flashinfer.py`, `vllm/model_executor/layers/quantization/utils/mxfp8_utils.py`_
- **2026-08-18** [`0db502c8d8`](https://github.com/vllm-project/vllm/commit/0db502c8d8) [#50493](https://github.com/vllm-project/vllm/pull/50493)
  [Kimi-K3] support DCP partial prefix cache hit (#50493)
  _Files: `tests/distributed/test_kimi_linear_context_parallel.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/prefix_cache/test_partial_prefix_cache_primitives.py` _+4 more__
- **2026-08-17** [`58aa1e3d26`](https://github.com/vllm-project/vllm/commit/58aa1e3d26) [#51395](https://github.com/vllm-project/vllm/pull/51395)
  [Bugfix][SM120][MLA] Disable dense prefill for FlashInfer sparse MLA (#51395)
  _Files: `tests/v1/attention/test_flashinfer_sparse_mla_sm120_api.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse_sm120.py`_
- **2026-08-17** [`455edc022b`](https://github.com/vllm-project/vllm/commit/455edc022b) [#42963](https://github.com/vllm-project/vllm/pull/42963)
  [ModelRunnerV2] Support prompt embeds (#42963)
  _Files: `tests/v1/worker/test_encoder_runner.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_prompt_embeds_state.py`, `vllm/config/model.py` _+13 more__
- **2026-08-17** [`d1e3eee6fb`](https://github.com/vllm-project/vllm/commit/d1e3eee6fb) [#52188](https://github.com/vllm-project/vllm/pull/52188)
  [Spec decode] Support Kimi-K3 DCP with DSpark (#52188)
  _Files: `tests/transformers_utils/test_dspark_mla_config.py`, `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/spec_decode/test_dflash_prepare_inputs.py` _+11 more__
- **2026-08-17** [`70afdedc10`](https://github.com/vllm-project/vllm/commit/70afdedc10) [#51855](https://github.com/vllm-project/vllm/pull/51855)
  [K3] support recoverssm for K3 (#51855)
  _Files: `tests/models/kimi_k3/test_kda.py`, `tests/models/kimi_k3/test_kda_metadata.py`, `tests/models/test_registry.py`, `tests/test_config.py` _+15 more__
- **2026-08-17** [`f27ae25473`](https://github.com/vllm-project/vllm/commit/f27ae25473) [#51852](https://github.com/vllm-project/vllm/pull/51852)
  [Bugfix][CPU] Take an attention group's query head count from its layers (#51852)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/v1/attention/test_group_head_counts.py`, `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-08-17** [`292187dd8c`](https://github.com/vllm-project/vllm/commit/292187dd8c) [#52492](https://github.com/vllm-project/vllm/pull/52492)
  [Bugfix][DSv4] Keep indexer scoring in breakable graphs (#52492)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-08-17** [`a18c9b56ff`](https://github.com/vllm-project/vllm/commit/a18c9b56ff) [#52458](https://github.com/vllm-project/vllm/pull/52458)
  [Kimi-K3][Perf] Update FlashKDA for automatic K2 V-split (#52458)
  _Files: `cmake/external_projects/flashkda.cmake`_

## MoE / Expert Parallel  (39 commits)

- **2026-08-24** [`460c08bc8a`](https://github.com/vllm-project/vllm/commit/460c08bc8a) [#52786](https://github.com/vllm-project/vllm/pull/52786)
  [LoRA] Add Qwen3-Omni multimodal LoRA support (#52786)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-08-24** [`702e1d7186`](https://github.com/vllm-project/vllm/commit/702e1d7186) [#53361](https://github.com/vllm-project/vllm/pull/53361)
  [LoRA] feat: Support LoRA for DeepSeek V4 (#53361)
  _Files: `vllm/lora/layers/base.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-08-23** [`ebcd606467`](https://github.com/vllm-project/vllm/commit/ebcd606467) [#53372](https://github.com/vllm-project/vllm/pull/53372)
  [MM] Simplify prompt updates: replace `PromptSeq` with `list[int]` (#53372)
  _Files: `docs/contributing/model/multimodal.md`, `tests/models/multimodal/processing/test_openvla.py`, `tests/multimodal/test_cache.py`, `tests/multimodal/test_processing.py` _+49 more__
- **2026-08-22** [`2f55ef254c`](https://github.com/vllm-project/vllm/commit/2f55ef254c) [#52560](https://github.com/vllm-project/vllm/pull/52560)
  [Model] Add Qwen3-Omni DSpark support (#52560)
  _Files: `tests/model_executor/test_qwen3_omni.py`, `tests/models/registry.py`, `tests/test_config.py`, `tests/transformers_utils/test_speculators_dspark_config.py` _+7 more__
- **2026-08-22** [`811d12ee26`](https://github.com/vllm-project/vllm/commit/811d12ee26) [#53381](https://github.com/vllm-project/vllm/pull/53381)
  [Mypy Fix] Mypy fix for "vllm/model_executor/models/[eE][fF]" (#53381)
  _Files: `tools/pre_commit/mypy.py`, `vllm/compilation/decorators.py`, `vllm/model_executor/models/eagle2_5_vl.py`, `vllm/model_executor/models/ernie45_moe.py` _+12 more__
- **2026-08-22** [`020829f66b`](https://github.com/vllm-project/vllm/commit/020829f66b) [#53385](https://github.com/vllm-project/vllm/pull/53385)
  [MM] Remove renderer_applies_updates flag (#53385)
  _Files: `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/pixtral.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_asr_realtime.py` _+4 more__
- **2026-08-22** [`0b19ebcacd`](https://github.com/vllm-project/vllm/commit/0b19ebcacd) [#53275](https://github.com/vllm-project/vllm/pull/53275)
  [MM] Simplify _apply_hf_processor_main (#53275)
  _Files: `docs/contributing/model/multimodal.md`, `docs/design/mm_processing.md`, `requirements/common.txt`, `tests/models/multimodal/processing/test_audio_in_video.py` _+86 more__
- **2026-08-22** [`e9d1398d9e`](https://github.com/vllm-project/vllm/commit/e9d1398d9e) [#53327](https://github.com/vllm-project/vllm/pull/53327)
  [Bugfix][Kimi K3] Enable deferred MoE finalization before weight loading (#53327)
  _Files: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/latent_moe_runner.py`_
- **2026-08-22** [`b2db227a7c`](https://github.com/vllm-project/vllm/commit/b2db227a7c) [#53240](https://github.com/vllm-project/vllm/pull/53240)
  [Bugfix][R3] Unwrap UniformTypeKVCacheSpecs when selecting the routed-experts KV group (#53240)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `tests/v1/core/test_kv_cache_utils.py`, `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`, `vllm/v1/attention/backends/flashinfer.py` _+1 more__
- **2026-08-21** [`e6f35d3c69`](https://github.com/vllm-project/vllm/commit/e6f35d3c69) [#52823](https://github.com/vllm-project/vllm/pull/52823)
  [DSv4 Perf] Adaptive topk width for dsv4, making #50004 back (#52823)
  _Files: `tests/kernels/attention/test_flashmla_sparse.py`, `vllm/models/deepseek_v4/sparse_mla.py`_
- **2026-08-21** [`ba53da60bb`](https://github.com/vllm-project/vllm/commit/ba53da60bb) [#52989](https://github.com/vllm-project/vllm/pull/52989)
  Revert "[Bugfix][MoE] Tune FlashInfer experts to scheduler token limit" (#52989) (#53186)
  _Files: `tests/kernels/moe/test_flashinfer_moe.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py` _+2 more__
- **2026-08-21** [`fbb17e780b`](https://github.com/vllm-project/vllm/commit/fbb17e780b) [#50479](https://github.com/vllm-project/vllm/pull/50479)
  [Bugfix] Fix six quantization exception messages split across positional args (#50479)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe.py`, `vllm/model_executor/layers/quantization/quark/quark.py`_
- **2026-08-21** [`2740c817ff`](https://github.com/vllm-project/vllm/commit/2740c817ff) [#52018](https://github.com/vllm-project/vllm/pull/52018)
  [Kernel] Add b12x FP4 MoE backend (#52018)
  _Files: `.buildkite/test_areas/kernels.yaml`, `docs/features/quantization/b12x.md`, `setup.py`, `tests/kernels/moe/test_b12x.py` _+19 more__
- **2026-08-21** [`cda3868f5d`](https://github.com/vllm-project/vllm/commit/cda3868f5d) [#45683](https://github.com/vllm-project/vllm/pull/45683)
  [Bugfix] Deterministic MoE combine (reduce_scatterv) under VLLM_BATCH_INVARIANT (#45683)
  _Files: `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/pynccl.py`_
- **2026-08-21** [`f8e0602713`](https://github.com/vllm-project/vllm/commit/f8e0602713) [#53132](https://github.com/vllm-project/vllm/pull/53132)
  Support kimi k3 nvfp4 checkpoint (#53132)
  _Files: `tests/kernels/moe/test_trtllm_nvfp4_moe.py`, `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py` _+2 more__
- **2026-08-21** [`b00f475f09`](https://github.com/vllm-project/vllm/commit/b00f475f09) [#53093](https://github.com/vllm-project/vllm/pull/53093)
  [MM] Remove text components from ProcessorInputs (#53093)
  _Files: `docs/contributing/model/multimodal.md`, `tests/models/multimodal/processing/test_audioflamingo3.py`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_llava_next.py` _+88 more__
- **2026-08-20** [`2f41c894e3`](https://github.com/vllm-project/vllm/commit/2f41c894e3) [#51866](https://github.com/vllm-project/vllm/pull/51866)
  Fix seed loss when batch contains unseeded requests (#51866)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`_
- **2026-08-20** [`bfb6c13499`](https://github.com/vllm-project/vllm/commit/bfb6c13499) [#52989](https://github.com/vllm-project/vllm/pull/52989)
  [Bugfix][MoE] Tune FlashInfer experts to scheduler token limit (#52989)
  _Files: `tests/kernels/moe/test_flashinfer_moe.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_lora_moe.py` _+2 more__
- **2026-08-20** [`4f6885fffc`](https://github.com/vllm-project/vllm/commit/4f6885fffc) [#53040](https://github.com/vllm-project/vllm/pull/53040)
  [DSV4][Kernel] Fuse shared experts into MegaMoE (#53040)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/envs.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/ops/prepare_megamoe.py` _+1 more__
- **2026-08-20** [`44cf3f0466`](https://github.com/vllm-project/vllm/commit/44cf3f0466) [#51968](https://github.com/vllm-project/vllm/pull/51968)
  [XPU][Tests] Make tests device-agnostic (#51968)
  _Files: `tests/conftest.py`, `tests/kernels/attention/test_merge_attn_states.py`, `tests/kernels/mamba/test_replayssm_prefill_decode_equivalence_mamba2.py`, `tests/kernels/moe/test_batched_moe.py` _+8 more__
- **2026-08-20** [`14617c2b6c`](https://github.com/vllm-project/vllm/commit/14617c2b6c) [#52632](https://github.com/vllm-project/vllm/pull/52632)
  [Bugfix] DeepEP-V2: expert_tokens_meta must be None on the decode/cudagraph path (empty recv_expert_num_tokens) (#52632)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-08-20** [`5bf0dbd6fd`](https://github.com/vllm-project/vllm/commit/5bf0dbd6fd) [#51824](https://github.com/vllm-project/vllm/pull/51824)
  [Bugfix] vLLM crashes at startup when DeepEP v2 is used with `--enforce-eager` wiht TRTLLM Bf16 (#51824)
  _Files: `tests/kernels/moe/parallel_utils.py`, `tests/kernels/moe/test_deepep_v2_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`_
- **2026-08-19** [`d591d1d511`](https://github.com/vllm-project/vllm/commit/d591d1d511) [#50082](https://github.com/vllm-project/vllm/pull/50082)
  [Bugfix] Add Kimi K3 MoE support to benchmark_moe.py (#50082)
  _Files: `benchmarks/kernels/benchmark_moe.py`_
- **2026-08-19** [`54dd98be28`](https://github.com/vllm-project/vllm/commit/54dd98be28) [#48918](https://github.com/vllm-project/vllm/pull/48918)
  [CT] Support Humming for WNA16 MoE (#48918)
  _Files: `tests/quantization/test_compressed_tensors.py`, `tests/quantization/test_moe_wna16.py`, `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` _+3 more__
- **2026-08-19** [`c676232313`](https://github.com/vllm-project/vllm/commit/c676232313) [#52704](https://github.com/vllm-project/vllm/pull/52704)
  [Bugfix][Quantization] Fix OCP MX MoE emulation silently skipping mxfp6 activation QDQ (#52704)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/experts/ocp_mx_emulation_moe.py`_
- **2026-08-19** [`be06873198`](https://github.com/vllm-project/vllm/commit/be06873198) [#52002](https://github.com/vllm-project/vllm/pull/52002)
  [Bugfix] compressed-tensors: restore int8 grouped WNA16 MoE support (#52002)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_wna16.py`_
- **2026-08-19** [`cba06764d7`](https://github.com/vllm-project/vllm/commit/cba06764d7) [#51781](https://github.com/vllm-project/vllm/pull/51781)
  [Platform] Fill in the missing backend parameter for torch.compile (#51781)
  _Files: `vllm/model_executor/models/diffusion_gemma.py`, `vllm/model_executor/models/kimi_k25_vit.py`, `vllm/model_executor/models/parakeet.py`, `vllm/transformers_utils/processors/nano_nemotron_vl.py` _+1 more__
- **2026-08-19** [`3130573630`](https://github.com/vllm-project/vllm/commit/3130573630) [#52706](https://github.com/vllm-project/vllm/pull/52706)
  [Model] Add GraniteSWA and GraniteMoeSWA via existing Granite (#52706)
  _Files: `docs/models/supported_models.md`, `tests/models/language/generation/test_granite.py`, `tests/models/registry.py`, `vllm/model_executor/models/granite.py` _+3 more__
- **2026-08-19** [`deeeae75d0`](https://github.com/vllm-project/vllm/commit/deeeae75d0) [#52827](https://github.com/vllm-project/vllm/pull/52827)
  [MM] Keep more metadata tensors on CPU (#52827)
  _Files: `vllm/model_executor/models/cohere2_vision.py`, `vllm/model_executor/models/deepseek_ocr.py`, `vllm/model_executor/models/deepseek_ocr2.py`, `vllm/model_executor/models/deepseek_vl2.py` _+34 more__
- **2026-08-19** [`a9f4afb66f`](https://github.com/vllm-project/vllm/commit/a9f4afb66f) [#51368](https://github.com/vllm-project/vllm/pull/51368)
  [Bugfix] Fix DeepSeek V4 mHC broadcast buffer for dummy load (#51368)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/nvidia/dspark.py`, `vllm/models/deepseek_v4/nvidia/model.py`, `vllm/models/deepseek_v4/nvidia/mtp.py`_
- **2026-08-18** [`d3fafe0c27`](https://github.com/vllm-project/vllm/commit/d3fafe0c27) [#52603](https://github.com/vllm-project/vllm/pull/52603)
  [Quantization] Remove the dead ocp_mx_scheme branch from moe_kernel_quantize_input (#52603)
  _Files: `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-08-18** [`bca7bea240`](https://github.com/vllm-project/vllm/commit/bca7bea240) [#52182](https://github.com/vllm-project/vllm/pull/52182)
  Remove VLLM_TEST_FORCE_FP8_MARLIN to replace with linear_backend/moe_backend (#52182)
  _Files: `tests/compile/passes/test_fusion.py`, `tests/compile/passes/test_mla_attn_quant_fusion.py`, `tests/evals/gsm8k/configs/moe-refactor/Llama-4-Scout-Fp8-ModelOpt-marlin.yaml`, `tests/evals/gsm8k/configs/moe-refactor/Qwen3-30B-A3B-Fp8-AutoFp8-marlin.yaml` _+11 more__
- **2026-08-18** [`aa9903490c`](https://github.com/vllm-project/vllm/commit/aa9903490c) [#50156](https://github.com/vllm-project/vllm/pull/50156)
  [Cohere] Misc changes to cohere model definitions (#50156)
  _Files: `vllm/model_executor/models/cohere2_moe.py`, `vllm/model_executor/models/commandr.py`_
- **2026-08-18** [`101c4477dd`](https://github.com/vllm-project/vllm/commit/101c4477dd) [#52044](https://github.com/vllm-project/vllm/pull/52044)
  [Bugfix] Handle DeepseekV4ForCausalLM in benchmark_moe get_model_params (#52044)
  _Files: `benchmarks/kernels/benchmark_moe.py`_
- **2026-08-18** [`c296851a7d`](https://github.com/vllm-project/vllm/commit/c296851a7d) [#51924](https://github.com/vllm-project/vllm/pull/51924)
  [MoE] Refine FlashInfer one-sided All2All integration (#51924)
  _Files: `docs/design/moe_kernel_features.md`, `tests/distributed/test_mnnvl_alltoall.py`, `tests/kernels/moe/test_moe_layer.py`, `vllm/config/parallel.py` _+4 more__
- **2026-08-17** [`75dde08d3f`](https://github.com/vllm-project/vllm/commit/75dde08d3f) [#51114](https://github.com/vllm-project/vllm/pull/51114)
  [Perf][MoE] Optimize deepep_v2 receiver CPU Overhead (#51114)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-08-17** [`cfbc5afbf7`](https://github.com/vllm-project/vllm/commit/cfbc5afbf7) [#52552](https://github.com/vllm-project/vllm/pull/52552)
  [BugFix] lora_base_layer / routed_experts order in expert param mapping (#52552)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-08-17** [`7ea4b40954`](https://github.com/vllm-project/vllm/commit/7ea4b40954) [#52502](https://github.com/vllm-project/vllm/pull/52502)
  [Hardware][NVIDIA] Add GB10 fused-MoE fp8 tuning configs (E=256, E=512) (#52502)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json`, `vllm/model_executor/layers/fused_moe/configs/E=512,N=512,device_name=NVIDIA_GB10,dtype=fp8_w8a8,block_shape=[128,128].json`_
- **2026-08-17** [`967e104fad`](https://github.com/vllm-project/vllm/commit/967e104fad) [#52550](https://github.com/vllm-project/vllm/pull/52550)
  [Config] Unify indexer cache dtype under attention_config.indexer_kv_dtype (#52550)
  _Files: `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-DSpark-confidence-TP4.yaml`, `tests/evals/gsm8k/configs/moe-refactor/DeepSeek-V4-Flash-deepgemm-mega-moe.yaml`, `vllm/config/attention.py`, `vllm/models/deepseek_v4/attention.py` _+2 more__

## Multimodal  (27 commits)

- **2026-08-24** [`8c2bbe00d5`](https://github.com/vllm-project/vllm/commit/8c2bbe00d5) [#53513](https://github.com/vllm-project/vllm/pull/53513)
  [Bugfix][LoRA] Add multimodal module mapping for Muse-Glimmer (#53513)
  _Files: `vllm/model_executor/models/muse_glimmer.py`_
- **2026-08-24** [`2ec6f0d71e`](https://github.com/vllm-project/vllm/commit/2ec6f0d71e) [#51896](https://github.com/vllm-project/vllm/pull/51896)
  Reject oversized media before fully downloading it (#51896)
  _Files: `docs/usage/security.md`, `tests/entrypoints/openai/test_run_batch.py`, `tests/entrypoints/speech_to_text/transcription/test_chunk_timestamp_offset.py`, `tests/multimodal/media/test_unprocessable_entity_error.py` _+9 more__
- **2026-08-23** [`a3561ef8e4`](https://github.com/vllm-project/vllm/commit/a3561ef8e4) [#52874](https://github.com/vllm-project/vllm/pull/52874)
  [Bugfix][Model] Mistral3: fix image placeholder grid for processor size overrides (#52874)
  _Files: `tests/models/multimodal/processing/test_mistral3.py`, `vllm/model_executor/models/lightonocr.py`, `vllm/model_executor/models/mistral3.py`_
- **2026-08-22** [`10704541aa`](https://github.com/vllm-project/vllm/commit/10704541aa) [#53374](https://github.com/vllm-project/vllm/pull/53374)
  [CI][ARM64] Restore known-good CUDA 13 builder image (#53374)
  _Files: `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/hardware_ci/run-gh200-test.sh`_
- **2026-08-22** [`040700aaa6`](https://github.com/vllm-project/vllm/commit/040700aaa6) [#53364](https://github.com/vllm-project/vllm/pull/53364)
  [MM] Address comments on #53275 (#53364)
  _Files: `vllm/model_executor/models/nano_nemotron_vl.py`, `vllm/model_executor/models/pixtral.py`, `vllm/model_executor/models/voxtral.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-22** [`7ca49fbe4b`](https://github.com/vllm-project/vllm/commit/7ca49fbe4b) [#53176](https://github.com/vllm-project/vllm/pull/53176)
  [Refactor][Model Runner V2][Multimodal] Move the encoder-only path out of the shared runner (#53176)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `vllm/config/vllm.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/worker/gpu/model_runner.py` _+3 more__
- **2026-08-21** [`e3f6026503`](https://github.com/vllm-project/vllm/commit/e3f6026503) [#53296](https://github.com/vllm-project/vllm/pull/53296)
  Revert "Remove native Hunyuan V1 and VL implementations" (#53296)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/hunyuan_v1.py`, `vllm/model_executor/models/hunyuan_vision.py`, `vllm/model_executor/models/registry.py` _+3 more__
- **2026-08-21** [`d53b1c2efc`](https://github.com/vllm-project/vllm/commit/d53b1c2efc) [#53272](https://github.com/vllm-project/vllm/pull/53272)
  Remove native Hunyuan V1 and VL implementations (#53272)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/hunyuan_v1.py`, `vllm/model_executor/models/hunyuan_vision.py`, `vllm/model_executor/models/registry.py` _+3 more__
- **2026-08-21** [`e85d1b69cf`](https://github.com/vllm-project/vllm/commit/e85d1b69cf) [#53092](https://github.com/vllm-project/vllm/pull/53092)
  [Bugfix][LoRA] Use an explicit capability flag for tower connector LoRA (#53092)
  _Files: `vllm/lora/model_manager.py`, `vllm/model_executor/models/blip2.py`, `vllm/model_executor/models/dots_ocr.py`, `vllm/model_executor/models/gemma3_mm.py` _+17 more__
- **2026-08-21** [`36bad1b90c`](https://github.com/vllm-project/vllm/commit/36bad1b90c) [#51630](https://github.com/vllm-project/vllm/pull/51630)
  [XPU][CI]Add more cases in intel GPU CI and reorganize to align non-xpu part (#51630)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/basic_correctness_intel.yaml`, `.buildkite/intel_jobs/expert_parallelism_intel.yaml`, `.buildkite/intel_jobs/lm_eval_intel.yaml` _+3 more__
- **2026-08-20** [`0a5a55136f`](https://github.com/vllm-project/vllm/commit/0a5a55136f) [#53172](https://github.com/vllm-project/vllm/pull/53172)
  [CI][Docker] Pin remaining manylinux builder images (#53172)
  _Files: `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/hardware_ci/run-gh200-test.sh`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-08-20** [`54ba80d961`](https://github.com/vllm-project/vllm/commit/54ba80d961) [#52994](https://github.com/vllm-project/vllm/pull/52994)
  [CI][Docker] Pin manylinux2_28-builder:cuda13.0 to the release/2.13 image (#52994)
  _Files: `.buildkite/image_build/image_build_torch_nightly.sh`, `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docker/versions.json`_
- **2026-08-20** [`cb09dd7488`](https://github.com/vllm-project/vllm/commit/cb09dd7488) [#52925](https://github.com/vllm-project/vllm/pull/52925)
  [Core][Multimodal] Skip redundant placeholder scan when token match succeeds (#52925)
  _Files: `tests/multimodal/test_processing.py`, `vllm/model_executor/models/gemma3_mm.py`, `vllm/model_executor/models/gemma3n_mm.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-20** [`de216b6e64`](https://github.com/vllm-project/vllm/commit/de216b6e64) [#53016](https://github.com/vllm-project/vllm/pull/53016)
  [Bugfix] Skip MM processor cache inserts larger than capacity (#53016)
  _Files: `docs/configuration/optimization.md`, `tests/multimodal/test_cache.py`, `tests/utils_/test_cache.py`, `vllm/config/multimodal.py` _+2 more__
- **2026-08-20** [`6e85feb1b7`](https://github.com/vllm-project/vllm/commit/6e85feb1b7) [#51827](https://github.com/vllm-project/vllm/pull/51827)
  [3/N] Harden Transformers modelling backend multi-modal path (#51827)
  _Files: `tests/models/multimodal/processing/test_transformers_audio.py`, `tests/models/multimodal/processing/test_transformers_image.py`, `tests/models/multimodal/processing/transformers_backend.py`, `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-08-20** [`c8de519917`](https://github.com/vllm-project/vllm/commit/c8de519917) [#50400](https://github.com/vllm-project/vllm/pull/50400)
  [Kernel][Kimi] fused vision q/k roper kernel (#50400)
  _Files: `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-08-20** [`c0a25c089a`](https://github.com/vllm-project/vllm/commit/c0a25c089a) [#52952](https://github.com/vllm-project/vllm/pull/52952)
  [Bugfix][Security] Guard _load_ov2_processor with resolve_trust_remote_code (#52952)
  _Files: `vllm/model_executor/models/llava_onevision2.py`_
- **2026-08-20** [`9b2aef5124`](https://github.com/vllm-project/vllm/commit/9b2aef5124) [#48608](https://github.com/vllm-project/vllm/pull/48608)
  [Bugfix] Video loading: sample over presentable frames, not header sample count (MP4 edit-list trims) (#48608)
  _Files: `tests/multimodal/test_video.py`, `tests/multimodal/utils.py`, `vllm/multimodal/video_decoders/opencv.py`, `vllm/multimodal/video_decoders/pyav.py`_
- **2026-08-19** [`db92053e97`](https://github.com/vllm-project/vllm/commit/db92053e97) [#52041](https://github.com/vllm-project/vllm/pull/52041)
  [Core] Skip broadcasting mm tensor data to workers for prefix-cache-covered items (#52041)
  _Files: `tests/v1/core/test_output.py`, `vllm/multimodal/utils.py`, `vllm/v1/core/sched/output.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-19** [`2f54100a59`](https://github.com/vllm-project/vllm/commit/2f54100a59) [#52937](https://github.com/vllm-project/vllm/pull/52937)
  [CI] Fix docs build (#52937)
  _Files: `docs/mkdocs/gen_files/generate_argparse.py`, `vllm/multimodal/video.py`_
- **2026-08-19** [`ee11730751`](https://github.com/vllm-project/vllm/commit/ee11730751) [#52881](https://github.com/vllm-project/vllm/pull/52881)
  [BugFix] Revert incorrect MM keep_on_cpu=True changes (#52881)
  _Files: `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/fireredlid.py`, `vllm/model_executor/models/isaac.py`, `vllm/model_executor/models/llava_onevision2.py` _+3 more__
- **2026-08-19** [`b1d9337e92`](https://github.com/vllm-project/vllm/commit/b1d9337e92) [#52697](https://github.com/vllm-project/vllm/pull/52697)
  [EPD] Allow KV consumers to omit MM embeddings (#52697)
  _Files: `tests/v1/ec_connector/integration/run_epd_correctness_test.sh`, `vllm/config/multimodal.py`, `vllm/config/vllm.py`, `vllm/model_executor/models/colqwen3.py` _+12 more__
- **2026-08-18** [`f9f066d195`](https://github.com/vllm-project/vllm/commit/f9f066d195) [#52692](https://github.com/vllm-project/vllm/pull/52692)
  [Bugfix][PaliGemma] Remove stale image embedding scaling (#52692)
  _Files: `vllm/model_executor/models/paligemma.py`_
- **2026-08-18** [`3bb9c18f0c`](https://github.com/vllm-project/vllm/commit/3bb9c18f0c) [#49155](https://github.com/vllm-project/vllm/pull/49155)
  [Multimodal] Reorganize video decoder backends (#49155)
  _Files: `tests/multimodal/media/test_video.py`, `tests/multimodal/test_gpu_ipc_memory.py`, `tests/multimodal/test_video.py`, `vllm/multimodal/gpu_ipc_memory.py` _+8 more__
- **2026-08-18** [`f4b161d7fc`](https://github.com/vllm-project/vllm/commit/f4b161d7fc) [#49287](https://github.com/vllm-project/vllm/pull/49287)
  [XPU][UT] Fix OOM and skip graph case (#49287)
  _Files: `tests/conftest.py`, `tests/models/language/generation/test_hybrid.py`, `tests/models/language/pooling/test_colbert.py`, `tests/models/multimodal/generation/test_voxtral_realtime.py` _+2 more__
- **2026-08-17** [`ceb340e2eb`](https://github.com/vllm-project/vllm/commit/ceb340e2eb) [#52126](https://github.com/vllm-project/vllm/pull/52126)
  fix: prevent PyNvVideoCodec decoder slot limit bypass via ClassVar shadowing (#52126)
  _Files: `tests/multimodal/test_video.py`, `vllm/multimodal/video.py`_
- **2026-08-17** [`5fd7a88838`](https://github.com/vllm-project/vllm/commit/5fd7a88838) [#52578](https://github.com/vllm-project/vllm/pull/52578)
  [CI/Build] Fix accident pre-commit breakage due to concurrent merge (#52578)
  _Files: `tests/models/multimodal/pooling/test_colpali.py`_

## Other  (24 commits)

- **2026-08-24** [`0ecc284790`](https://github.com/vllm-project/vllm/commit/0ecc284790) [#51031](https://github.com/vllm-project/vllm/pull/51031)
  [Bugfix][Kernel] Handle kernel block sizes in V2 DCP slot mapping (#51031)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`_
- **2026-08-22** [`236f78cc5c`](https://github.com/vllm-project/vllm/commit/236f78cc5c) [#50723](https://github.com/vllm-project/vllm/pull/50723)
  [Core][RL] Support sparse checkpoint updates through native weight loaders (#50723)
  _Files: `tests/model_executor/model_loader/test_checkpoint_weight_patch.py`, `vllm/model_executor/model_loader/checkpoint_weight_patch.py`_
- **2026-08-21** [`08b73d07cc`](https://github.com/vllm-project/vllm/commit/08b73d07cc) [#52889](https://github.com/vllm-project/vllm/pull/52889)
  [Frontend] Prevent Kimi K3 reserved markers in response text (#52889)
  _Files: `rust/src/parser/src/unified/kimi_k3.rs`, `rust/src/parser/src/unified/kimi_k3/structural_tag.rs`, `tests/tool_parsers/test_structural_tag_registry.py`, `vllm/tool_parsers/structural_tag_registry.py`_
- **2026-08-21** [`6feafb8b7d`](https://github.com/vllm-project/vllm/commit/6feafb8b7d) [#53201](https://github.com/vllm-project/vllm/pull/53201)
  [XPU] follow cuda path for mrope on XPU (#53201)
  _Files: `vllm/model_executor/layers/rotary_embedding/mrope.py`_
- **2026-08-21** [`ba07e4a48f`](https://github.com/vllm-project/vllm/commit/ba07e4a48f) [#52960](https://github.com/vllm-project/vllm/pull/52960)
  [Bugfix] Fix batch-invariant fp32 matmul OOR on SM89 for N=1 (#52960)
  _Files: `vllm/model_executor/layers/batch_invariant.py`_
- **2026-08-21** [`2adf4b9e2a`](https://github.com/vllm-project/vllm/commit/2adf4b9e2a) [#53043](https://github.com/vllm-project/vllm/pull/53043)
  [Rust Frontend] Fix Kimi K3 reasoning_effort="none" handling (#53043)
  _Files: `rust/src/chat/src/renderer/kimi_k3/encoding.rs`, `rust/src/chat/src/renderer/kimi_k3/tests.rs`_
- **2026-08-21** [`df3b3422b4`](https://github.com/vllm-project/vllm/commit/df3b3422b4) [#53054](https://github.com/vllm-project/vllm/pull/53054)
  [Rust Frontend] Add HY3 unified parser and local XGrammar structural-tag builder (#53054)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/unified.rs` _+13 more__
- **2026-08-20** [`00f7f25828`](https://github.com/vllm-project/vllm/commit/00f7f25828) [#53127](https://github.com/vllm-project/vllm/pull/53127)
  [Misc] Don't allow language-model-only used with encoder CG together (#53127)
  _Files: `vllm/config/vllm.py`_
- **2026-08-20** [`01af92e175`](https://github.com/vllm-project/vllm/commit/01af92e175) [#49811](https://github.com/vllm-project/vllm/pull/49811)
  [Feature][Model Runner V2] Support extract_hidden_states speculation (#49811)
  _Files: `tests/test_config.py`, `tests/v1/worker/test_gpu_extract_hidden_states_speculator.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/model_runner.py` _+2 more__
- **2026-08-20** [`6259572b28`](https://github.com/vllm-project/vllm/commit/6259572b28) [#53098](https://github.com/vllm-project/vllm/pull/53098)
  [Docs] Use incremental builds for C++ changes in `AGENTS.md` (#53098)
  _Files: `AGENTS.md`_
- **2026-08-20** [`16cfe728d8`](https://github.com/vllm-project/vllm/commit/16cfe728d8) [#52844](https://github.com/vllm-project/vllm/pull/52844)
  [Bugfix][Rust Frontend] Reject n > 1 in the `/inference/v1/generate` route (#52844)
  _Files: `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/inference/generate/convert.rs`, `rust/src/server/src/routes/inference/generate/types.rs`, `rust/src/server/src/routes/inference/generate/validate.rs` _+2 more__
- **2026-08-20** [`0a111cca2c`](https://github.com/vllm-project/vllm/commit/0a111cca2c) [#52812](https://github.com/vllm-project/vllm/pull/52812)
  [kv_offload] fix(metrics): rename kv_offload_tiering_block_{queries,hits} → chunk (#52812)
  _Files: `vllm/v1/kv_offload/tiering/base.py`_
- **2026-08-19** [`f76d71d7ce`](https://github.com/vllm-project/vllm/commit/f76d71d7ce) [#52981](https://github.com/vllm-project/vllm/pull/52981)
  [CI/Build] Fix CPU platform pre-commit formatting (#52981)
  _Files: `vllm/platforms/cpu.py`_
- **2026-08-19** [`340b7e4909`](https://github.com/vllm-project/vllm/commit/340b7e4909) [#49996](https://github.com/vllm-project/vllm/pull/49996)
  fix: reject string schemas that mix pattern/format with length bounds (#49996)
  _Files: `tests/v1/structured_output/test_utils.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-08-19** [`08afae2786`](https://github.com/vllm-project/vllm/commit/08afae2786) [#48290](https://github.com/vllm-project/vllm/pull/48290)
  [ModelRunner v2] Enable MRV2 for pooling models by default (#48290)
  _Files: `tests/models/language/pooling/test_colbert.py`, `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-08-19** [`f936a267f9`](https://github.com/vllm-project/vllm/commit/f936a267f9) [#48109](https://github.com/vllm-project/vllm/pull/48109)
  [Bugfix][XPU] Fix Mamba state pointer overflow (#48109)
  _Files: `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-08-18** [`12f64b39d2`](https://github.com/vllm-project/vllm/commit/12f64b39d2) [#52805](https://github.com/vllm-project/vllm/pull/52805)
  [Bugfix][Structured Output] Stop XGrammar token batches at termination (#52805)
  _Files: `tests/v1/spec_decode/test_mtp_structured_output.py`, `vllm/v1/structured_output/backend_xgrammar.py`_
- **2026-08-18** [`d785eb51ce`](https://github.com/vllm-project/vllm/commit/d785eb51ce) [#52144](https://github.com/vllm-project/vllm/pull/52144)
  [Test] Add pause/resume E2E tests (#52144)
  _Files: `tests/entrypoints/serve/dev/rlhf/conftest.py`, `tests/entrypoints/serve/dev/rlhf/state_transitions/__init__.py`, `tests/entrypoints/serve/dev/rlhf/state_transitions/test_pause_resume.py`_
- **2026-08-18** [`e0e5a7fb28`](https://github.com/vllm-project/vllm/commit/e0e5a7fb28) [#51426](https://github.com/vllm-project/vllm/pull/51426)
  [Rust Frontend] Fix GLM-5.2 chat template rendering parity (#51426)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/chat/src/renderer/hf/mod.rs`, `rust/src/chat/src/renderer/hf/template.rs` _+1 more__
- **2026-08-17** [`c296cf8259`](https://github.com/vllm-project/vllm/commit/c296cf8259) [#52174](https://github.com/vllm-project/vllm/pull/52174)
  [Bugfix] Add forward_xpu to XDRotaryEmbedding for HunyuanOCR on XPU (#52174)
  _Files: `vllm/model_executor/layers/rotary_embedding/xdrope.py`_
- **2026-08-17** [`3fc2893909`](https://github.com/vllm-project/vllm/commit/3fc2893909) [#52385](https://github.com/vllm-project/vllm/pull/52385)
  [Bugfix] Account for local DP workers in startup thread allocation (#52385)
  _Files: `tests/distributed/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-08-17** [`cc7cf71fc8`](https://github.com/vllm-project/vllm/commit/cc7cf71fc8) [#51809](https://github.com/vllm-project/vllm/pull/51809)
  [XPU] Enable Kimi K3 KDA kernel tests on XPU (#51809)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/model_executor/layers/mamba/ops/gather_initial_states.py`_
- **2026-08-17** [`a02cfccbc6`](https://github.com/vllm-project/vllm/commit/a02cfccbc6) [#50729](https://github.com/vllm-project/vllm/pull/50729)
  [Bugfix][Mamba] Fix overlapping state copy race (#50729)
  _Files: `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-08-17** [`6664d397bf`](https://github.com/vllm-project/vllm/commit/6664d397bf) [#52329](https://github.com/vllm-project/vllm/pull/52329)
  [Performance][MRV2] Cache logits-processing request state (#52329)
  _Files: `tests/v1/worker/test_gpu_sampler_flags.py`, `tests/v1/worker/test_gpu_thinking_budget.py`, `vllm/v1/worker/gpu/sample/sampler.py`_

## CI / Build  (20 commits)

- **2026-08-24** [`a047e2543d`](https://github.com/vllm-project/vllm/commit/a047e2543d) [#53000](https://github.com/vllm-project/vllm/pull/53000)
  Fix MNNVL Lamport mailbox publication and cleanup (#53000)
  _Files: `.buildkite/test_areas/distributed.yaml`, `csrc/custom_all_gather_reduce_scatter.cuh`, `tests/distributed/test_custom_all_gather_reduce_scatter.py`_
- **2026-08-23** [`e25c586b90`](https://github.com/vllm-project/vllm/commit/e25c586b90) [#53358](https://github.com/vllm-project/vllm/pull/53358)
  [CI/Build] Pin Cython below 3.3 for arm64 tilelang sdist (#53358)
  _Files: `docker/Dockerfile`_
- **2026-08-21** [`3e47a9a824`](https://github.com/vllm-project/vllm/commit/3e47a9a824) [#53023](https://github.com/vllm-project/vllm/pull/53023)
  [CI] Fix MultiConnector accuracy test lifecycle (#53023)
  _Files: `tests/v1/kv_connector/nixl_integration/run_multi_connector_accuracy_test.sh`_
- **2026-08-21** [`5ee84d3c52`](https://github.com/vllm-project/vllm/commit/5ee84d3c52) [#53146](https://github.com/vllm-project/vllm/pull/53146)
  [CI][Bugfix] Use a prompt that survives offload-resume rounding in mamba offload test (#53146)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`_
- **2026-08-21** [`0a21947d71`](https://github.com/vllm-project/vllm/commit/0a21947d71) [#52257](https://github.com/vllm-project/vllm/pull/52257)
  [XPU][CI]Add parallelism for long-running Intel GPU cases (#52257)
  _Files: `.buildkite/hardware_tests/intel_xpu_ci/test-intel.yaml`, `.buildkite/intel_jobs/misc_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-test.sh`_
- **2026-08-20** [`ae25628995`](https://github.com/vllm-project/vllm/commit/ae25628995) [#53088](https://github.com/vllm-project/vllm/pull/53088)
  upgrade tpu-inference to v0.27.0 (#53088)
  _Files: `requirements/tpu.txt`_
- **2026-08-20** [`4b7cb949a9`](https://github.com/vllm-project/vllm/commit/4b7cb949a9) [#51777](https://github.com/vllm-project/vllm/pull/51777)
  [Docker] Update to nixl-1.3.2 (#51777)
  _Files: `docker/Dockerfile.xpu`_
- **2026-08-20** [`963fcfa48c`](https://github.com/vllm-project/vllm/commit/963fcfa48c) [#51592](https://github.com/vllm-project/vllm/pull/51592)
  [Rust][Benchmark] Align speed-bench CLI flags with Python and add flag parity test (#51592)
  _Files: `.buildkite/test_areas/benchmarks.yaml`, `rust/src/bench/README.md`, `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/cli.rs` _+4 more__
- **2026-08-20** [`754e1c3de4`](https://github.com/vllm-project/vllm/commit/754e1c3de4) [#53035](https://github.com/vllm-project/vllm/pull/53035)
  [CI][XPU] Skip test_fused_shared_expert.py on XPU (#53035)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`_
- **2026-08-19** [`c205726108`](https://github.com/vllm-project/vllm/commit/c205726108) [#51459](https://github.com/vllm-project/vllm/pull/51459)
  [CI] Fix and extend PR/issue auto-labeling (#51459)
  _Files: `.github/ISSUE_TEMPLATE/600-new-model.yml`, `.github/mergify.yml`, `.github/workflows/issue_autolabel.yml`, `.pre-commit-config.yaml` _+2 more__
- **2026-08-19** [`cb58bb9c1e`](https://github.com/vllm-project/vllm/commit/cb58bb9c1e) [#52282](https://github.com/vllm-project/vllm/pull/52282)
  [CI] Harden RemoteVLLMServer GPU cleanup checks (#52282)
  _Files: `tests/entrypoints/launchers/test_shutdown.py`, `tests/entrypoints/unit_tests/test_remote_vllm_server.py`, `tests/utils.py`_
- **2026-08-19** [`2d7f42b4f3`](https://github.com/vllm-project/vllm/commit/2d7f42b4f3) [#52801](https://github.com/vllm-project/vllm/pull/52801)
  [Build] Add InstantTensor to CUDA dependencies (#52801)
  _Files: `requirements/cuda.txt`, `requirements/test/cuda.txt`_
- **2026-08-19** [`93eea4f665`](https://github.com/vllm-project/vllm/commit/93eea4f665) [#52904](https://github.com/vllm-project/vllm/pull/52904)
  [XPU][CI] downgrade sentencepiece (#52904)
  _Files: `requirements/test/xpu.txt`_
- **2026-08-19** [`e575b5f1a9`](https://github.com/vllm-project/vllm/commit/e575b5f1a9) [#52730](https://github.com/vllm-project/vllm/pull/52730)
  [XPU][CI] fix hf runner (#52730)
  _Files: `tests/conftest.py`_
- **2026-08-19** [`03b87dc42f`](https://github.com/vllm-project/vllm/commit/03b87dc42f) [#52672](https://github.com/vllm-project/vllm/pull/52672)
  [XPU] upgrade requirements/test/xpu.txt (#52672)
  _Files: `requirements/test/xpu.txt`_
- **2026-08-18** [`9842d70145`](https://github.com/vllm-project/vllm/commit/9842d70145) [#48628](https://github.com/vllm-project/vllm/pull/48628)
  [DBO][CI] Increase the coverage of prefill DBO in test_dbo.py (#48628)
  _Files: `tests/v1/distributed/test_dbo.py`_
- **2026-08-18** [`be3f614ff1`](https://github.com/vllm-project/vllm/commit/be3f614ff1) [#52633](https://github.com/vllm-project/vllm/pull/52633)
  [CI] Register CPU CI "VLLM_CPU_CI_ENV" environment variable (#52633)
  _Files: `vllm/envs.py`, `vllm/platforms/cpu.py`_
- **2026-08-18** [`b0e9cff5e7`](https://github.com/vllm-project/vllm/commit/b0e9cff5e7) [#52569](https://github.com/vllm-project/vllm/pull/52569)
  [XPU] update xpu-manager to v2.1.0 (#52569)
  _Files: `docker/Dockerfile.xpu`_
- **2026-08-17** [`9633933dd8`](https://github.com/vllm-project/vllm/commit/9633933dd8) [#44284](https://github.com/vllm-project/vllm/pull/44284)
  Relax CuPy constraint to only exclude 14.1.0 (#44284)
  _Files: `requirements/kv_connectors.txt`_
- **2026-08-17** [`bb233626ca`](https://github.com/vllm-project/vllm/commit/bb233626ca) [#52325](https://github.com/vllm-project/vllm/pull/52325)
  [CI] Shard Humming A100 eval (#52325)
  _Files: `.buildkite/test_areas/lm_eval.yaml`, `tests/evals/gsm8k/configs/humming/config-a100-shard-0.txt`, `tests/evals/gsm8k/configs/humming/config-a100-shard-1.txt`, `tests/evals/gsm8k/configs/humming/config-a100-shard-2.txt`_

## Models  (16 commits)

- **2026-08-24** [`a7195188a4`](https://github.com/vllm-project/vllm/commit/a7195188a4) [#53121](https://github.com/vllm-project/vllm/pull/53121)
  Add MTP support for Nemotron VL models (#53121)
  _Files: `vllm/model_executor/models/nemotron_h_mtp.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-08-24** [`cd329413e2`](https://github.com/vllm-project/vllm/commit/cd329413e2) [#52467](https://github.com/vllm-project/vllm/pull/52467)
  [Misc] Use VLLMValidationError in Cohere request validation (#52467)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/cohere/test_protocol.py`, `vllm/entrypoints/cohere/protocol.py`_
- **2026-08-23** [`b26039b09f`](https://github.com/vllm-project/vllm/commit/b26039b09f) [#52209](https://github.com/vllm-project/vllm/pull/52209)
  Add routed expert loading for gpt-oss (#52209)
  _Files: `tests/model_executor/model_loader/test_gpt_oss_weight_loading.py`, `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/meta.py`, `vllm/model_executor/models/gpt_oss.py`_
- **2026-08-21** [`f94dcde5c5`](https://github.com/vllm-project/vllm/commit/f94dcde5c5) [#52175](https://github.com/vllm-project/vllm/pull/52175)
  Fix Cohere ChatV2 citation and tool handling issues (#52175)
  _Files: `tests/entrypoints/cohere/test_serving_conversion.py`, `tests/reasoning/test_cohere_command_reasoning_parser.py`, `tests/renderers/test_cohere.py`, `vllm/entrypoints/cohere/serving.py` _+3 more__
- **2026-08-21** [`c1d7a3808d`](https://github.com/vllm-project/vllm/commit/c1d7a3808d) [#48682](https://github.com/vllm-project/vllm/pull/48682)
  [Bugfix] Fix HYV3 shared_mlp prefix for compressed-tensors ignore matching (#48682)
  _Files: `vllm/model_executor/models/hy_v3.py`_
- **2026-08-21** [`91a893de64`](https://github.com/vllm-project/vllm/commit/91a893de64) [#52809](https://github.com/vllm-project/vllm/pull/52809)
  [Bugfix][Spec Decode] Scope DSpark backend inheritance to DeepSeek V4 (#52809)
  _Files: `vllm/v1/worker/gpu/spec_decode/dspark/utils.py`_
- **2026-08-21** [`d29f7f5c92`](https://github.com/vllm-project/vllm/commit/d29f7f5c92) [#53170](https://github.com/vllm-project/vllm/pull/53170)
  [Bugfix] Load untied Gemma LM head weights (#53170)
  _Files: `tests/models/language/generation/test_gemma.py`, `vllm/model_executor/models/gemma.py`_
- **2026-08-20** [`d56bbf3995`](https://github.com/vllm-project/vllm/commit/d56bbf3995) [#52720](https://github.com/vllm-project/vllm/pull/52720)
  [Bugfix] Support MistralCommonBackend tokenizers in structured output (#52720)
  _Files: `tests/v1/structured_output/test_mistral_common_tokenizer.py`, `vllm/v1/structured_output/__init__.py`, `vllm/v1/structured_output/utils.py`_
- **2026-08-20** [`727274a75b`](https://github.com/vllm-project/vllm/commit/727274a75b) [#51169](https://github.com/vllm-project/vllm/pull/51169)
  [Rust Frontend] Fix Qwen parser auto-detection (#51169)
  _Files: `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/reasoning/tests.rs`, `rust/src/chat/src/parser/tool/mod.rs`, `rust/src/chat/src/parser/tool/tests.rs`_
- **2026-08-20** [`38e9cefdef`](https://github.com/vllm-project/vllm/commit/38e9cefdef) [#53071](https://github.com/vllm-project/vllm/pull/53071)
  [Bugfix] Return HTTP 400 instead of 501 for unknown chat roles in DeepSeek encoders (#53071)
  _Files: `tests/test_request_input_bounds.py`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v32_encoding.py`, `vllm/tokenizers/deepseek_v4_encoding.py`_
- **2026-08-19** [`b160cab156`](https://github.com/vllm-project/vllm/commit/b160cab156) [#52690](https://github.com/vllm-project/vllm/pull/52690)
  [Bugfix] Restore model info caching for package backends (#52690)
  _Files: `tests/models/test_registry.py`, `vllm/model_executor/models/registry.py`_
- **2026-08-19** [`b05ae5dc00`](https://github.com/vllm-project/vllm/commit/b05ae5dc00) [#52842](https://github.com/vllm-project/vllm/pull/52842)
  [CI][Bugfix] Complete DeepSeek-V4 FSE test fixture contract (#52842)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`_
- **2026-08-18** [`eab1cff5b0`](https://github.com/vllm-project/vllm/commit/eab1cff5b0) [#52381](https://github.com/vllm-project/vllm/pull/52381)
  Harden DeepSeek V3.2 fused kernel grids (#52381)
  _Files: `tests/kernels/test_fused_deepseek_v32_norm_rope.py`, `vllm/models/deepseek_v32/common/kernels.py`_
- **2026-08-18** [`2687fec6ef`](https://github.com/vllm-project/vllm/commit/2687fec6ef) [#48484](https://github.com/vllm-project/vllm/pull/48484)
  Replicated embedding and norm fusion for DSV3 flat model (#48484)
  _Files: `tests/kernels/core/test_fused_embed_norm.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_embed_norm.py`, `vllm/models/deepseek_v32/nvidia/model.py` _+1 more__
- **2026-08-18** [`d5f5de7a7d`](https://github.com/vllm-project/vllm/commit/d5f5de7a7d) [#52626](https://github.com/vllm-project/vllm/pull/52626)
  [Bugfix] Fix DeepSeek V4 mHC broadcast buffer for weight sync (#52626)
  _Files: `tests/kernels/test_mhc_kernels.py`, `vllm/models/deepseek_v4/nvidia/model.py`_
- **2026-08-18** [`cdb8545a91`](https://github.com/vllm-project/vllm/commit/cdb8545a91) [#52539](https://github.com/vllm-project/vllm/pull/52539)
  [Kernel][Perf] Support Qwen head ratios in fused GDN MTP (#52539)
  _Files: `csrc/libtorch_stable/gdn/fused_gdn_decode_kernel.cu`, `tests/kernels/mamba/test_gdn_fused_mtp.py`, `tests/kernels/test_fused_gdn_post_conv.py`, `vllm/model_executor/layers/mamba/gdn/qwen_gdn_linear_attn.py`_

## Serving / API  (15 commits)

- **2026-08-24** [`585bb07c70`](https://github.com/vllm-project/vllm/commit/585bb07c70) [#51034](https://github.com/vllm-project/vllm/pull/51034)
  feat: add SSE keep-alive comments for idle streaming responses (#51034)
  _Files: `tests/entrypoints/openai/test_cli_args.py`, `tests/entrypoints/openai/test_sse_keep_alive.py`, `vllm/entrypoints/openai/chat_completion/api_router.py`, `vllm/entrypoints/openai/cli_args.py` _+2 more__
- **2026-08-21** [`a556f3fccb`](https://github.com/vllm-project/vllm/commit/a556f3fccb) [#53308](https://github.com/vllm-project/vllm/pull/53308)
  Forward Anthropic vllm_xargs to sampling params (#53308)
  _Files: `docs/features/custom_arguments.md`, `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-08-21** [`1baf372bfc`](https://github.com/vllm-project/vllm/commit/1baf372bfc) [#50191](https://github.com/vllm-project/vllm/pull/50191)
  [Frontend] Use VLLMValidationError for batch request URL validation (#50191)
  _Files: `tests/entrypoints/openai/test_run_batch.py`, `vllm/entrypoints/openai/run_batch.py`_
- **2026-08-21** [`b41dc4ec72`](https://github.com/vllm-project/vllm/commit/b41dc4ec72) [#49195](https://github.com/vllm-project/vllm/pull/49195)
  [Bugfix] Return HTTP 500 for non-streaming generate errors (#49195)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_generate_stream.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-21** [`18aa245a99`](https://github.com/vllm-project/vllm/commit/18aa245a99) [#52473](https://github.com/vllm-project/vllm/pull/52473)
  using existing uvicorn configuration for dp supervisor (#52473)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/entrypoints/openai/dp_supervisor.py`_
- **2026-08-20** [`a34fd69106`](https://github.com/vllm-project/vllm/commit/a34fd69106) [#52939](https://github.com/vllm-project/vllm/pull/52939)
  [CI][Bugfix] Update distributed DP API server test path (#52939)
- **2026-08-20** [`e85dd21497`](https://github.com/vllm-project/vllm/commit/e85dd21497) [#45807](https://github.com/vllm-project/vllm/pull/45807)
  fix: report stop_sequence stop_reason in Anthropic Messages API (#45807)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/serving.py`_
- **2026-08-19** [`92bdee05cb`](https://github.com/vllm-project/vllm/commit/92bdee05cb) [#52399](https://github.com/vllm-project/vllm/pull/52399)
  [Bugfix][Frontend] Return all choices from /inference/v1/generate when n > 1 (#52399)
  _Files: `tests/entrypoints/scale_out/token_in_token_out/test_serving_tokens.py`, `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-19** [`9a9aa2b017`](https://github.com/vllm-project/vllm/commit/9a9aa2b017) [#52523](https://github.com/vllm-project/vllm/pull/52523)
  [Bugfix] Redact api_key in non-default args log (#52523)
  _Files: `tests/entrypoints/serve/utils/test_api_utils.py`, `tests/test_envs.py`, `vllm/entrypoints/serve/utils/api_utils.py`, `vllm/envs.py`_
- **2026-08-19** [`842dd8fd96`](https://github.com/vllm-project/vllm/commit/842dd8fd96) [#52867](https://github.com/vllm-project/vllm/pull/52867)
  [Pooling] Use semantic task validation errors (#52867)
  _Files: `vllm/entrypoints/pooling/pooling/serving.py`_
- **2026-08-19** [`86a89a9348`](https://github.com/vllm-project/vllm/commit/86a89a9348) [#52825](https://github.com/vllm-project/vllm/pull/52825)
  [Bugfix][Frontend] Run the serve arg checks for `vllm launch` too (#52825)
  _Files: `tests/entrypoints/openai/test_cli_args.py`, `vllm/entrypoints/openai/cli_args.py`_
- **2026-08-18** [`5c9ff5366b`](https://github.com/vllm-project/vllm/commit/5c9ff5366b) [#46175](https://github.com/vllm-project/vllm/pull/46175)
  [Bugfix] Accept logprobs=-1 in the Completion API (#46175)
  _Files: `tests/entrypoints/openai/completion/test_completion_error.py`, `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-08-18** [`b01728b088`](https://github.com/vllm-project/vllm/commit/b01728b088) [#52622](https://github.com/vllm-project/vllm/pull/52622)
  [Bugfix] Return 4xx for client-caused errors in /detokenize (#52622)
  _Files: `tests/entrypoints/serve/tokenize/test_serving_tokenization.py`, `vllm/entrypoints/serve/tokenize/api_router.py`_
- **2026-08-17** [`93550cc4cd`](https://github.com/vllm-project/vllm/commit/93550cc4cd) [#52309](https://github.com/vllm-project/vllm/pull/52309)
  [Frontend] Consolidate entrypoint middleware (#52309)
  _Files: `tests/entrypoints/serve/middleware/__init__.py`, `tests/entrypoints/serve/middleware/test_authentication_middleware.py`, `tests/entrypoints/serve/middleware/test_optional_middleware.py`, `vllm/entrypoints/launchers/__init__.py` _+10 more__
- **2026-08-17** [`a6a2a93f9b`](https://github.com/vllm-project/vllm/commit/a6a2a93f9b) [#52528](https://github.com/vllm-project/vllm/pull/52528)
  [Bugfix][Frontend] Guard remaining before-validators against non-object JSON bodies (#52528)
  _Files: `tests/entrypoints/unit_tests/test_non_object_body_validation.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/pooling/base/protocol.py` _+3 more__

## Scheduler / Engine  (13 commits)

- **2026-08-23** [`9dba2c9b37`](https://github.com/vllm-project/vllm/commit/9dba2c9b37) [#53204](https://github.com/vllm-project/vllm/pull/53204)
  [Rust Frontend][RL]: report engine world size over gRPC (#53204)
  _Files: `rust/proto/control.proto`, `rust/src/engine-core-client/src/protocol/handshake.rs`, `rust/src/server/src/grpc/control.rs`, `rust/src/server/src/grpc/tests.rs`_
- **2026-08-22** [`a34f2ab70a`](https://github.com/vllm-project/vllm/commit/a34f2ab70a) [#53189](https://github.com/vllm-project/vllm/pull/53189)
  [Test] Add focused hybrid MTP prefix-cache regressions (#53189)
  _Files: `.buildkite/test_areas/engine.yaml`, `tests/v1/e2e/test_hybrid_chunked_prefill.py`_
- **2026-08-21** [`e00a034ad1`](https://github.com/vllm-project/vllm/commit/e00a034ad1) [#46588](https://github.com/vllm-project/vllm/pull/46588)
  (security) fix: enforce decoder prompt-length validation for skip-che… (#46588)
  _Files: `vllm/v1/engine/input_processor.py`_
- **2026-08-21** [`f32b17b6d6`](https://github.com/vllm-project/vllm/commit/f32b17b6d6) [#53044](https://github.com/vllm-project/vllm/pull/53044)
  [Rust Frontend] Support `--generation-config vllm` (#53044)
  _Files: `rust/src/chat/src/backend/hf.rs`, `rust/src/chat/src/backend/mod.rs`, `rust/src/chat/src/lib.rs`, `rust/src/cmd/src/cli.rs` _+10 more__
- **2026-08-20** [`a1c5b1fd9f`](https://github.com/vllm-project/vllm/commit/a1c5b1fd9f) [#46701](https://github.com/vllm-project/vllm/pull/46701)
  [Core][V1] Support trace_decode_token_ids for deterministic decode replay (#46701)
  _Files: `docs/serving/online_serving/trace_replay.md`, `examples/generate/trace_replay_offline.py`, `tests/v1/engine/test_input_processor_trace_replay.py`, `tests/v1/sample/test_trace_replay_params.py` _+9 more__
- **2026-08-20** [`76fb6d210a`](https://github.com/vllm-project/vllm/commit/76fb6d210a) [#47272](https://github.com/vllm-project/vllm/pull/47272)
  [Bugfix][Core] Reserve the KV null block when validating max_model_len (#47272)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/e2e/general/test_async_scheduling.py`, `tests/v1/e2e/general/test_context_length.py`, `tests/v1/engine/test_init_error_messaging.py` _+2 more__
- **2026-08-19** [`0c8c3f41cf`](https://github.com/vllm-project/vllm/commit/0c8c3f41cf) [#50809](https://github.com/vllm-project/vllm/pull/50809)
  [Bugfix][V1] Sync mamba_block_size via EngineCoreReadyResponse (#50809)
  _Files: `tests/v1/engine/test_engine_core_client.py`, `vllm/v1/engine/__init__.py`, `vllm/v1/engine/core.py`, `vllm/v1/engine/core_client.py`_
- **2026-08-19** [`d36cc4254e`](https://github.com/vllm-project/vllm/commit/d36cc4254e) [#52702](https://github.com/vllm-project/vllm/pull/52702)
  [Bugfix][Elastic EP] Reject scale below the minimum data parallel size (#52702)
  _Files: `vllm/entrypoints/serve/elastic_ep/api_router.py`, `vllm/v1/engine/core_client.py`_
- **2026-08-18** [`7ddb50788d`](https://github.com/vllm-project/vllm/commit/7ddb50788d) [#51481](https://github.com/vllm-project/vllm/pull/51481)
  [Bugfix][DP] Don't assume the engines started when forwarding a wake (#51481)
  _Files: `tests/v1/distributed/test_async_llm_dp.py`, `vllm/v1/engine/coordinator.py`, `vllm/v1/engine/core.py`_
- **2026-08-18** [`6a391a931a`](https://github.com/vllm-project/vllm/commit/6a391a931a) [#52703](https://github.com/vllm-project/vllm/pull/52703)
  [Rust Frontend][RL] add routed expert prompt offset (#52703)
  _Files: `rust/src/engine-core-client/src/protocol/sampling.rs`, `rust/src/engine-core-client/src/tests/client.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`, `rust/src/text/src/lower.rs`_
- **2026-08-18** [`d75136c030`](https://github.com/vllm-project/vllm/commit/d75136c030) [#52671](https://github.com/vllm-project/vllm/pull/52671)
  [Rust Frontend] Wait for all utility calls to finish (#52671)
  _Files: `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/client/imp.rs`, `rust/src/engine-core-client/src/client/state.rs`, `rust/src/engine-core-client/src/tests/client.rs`_
- **2026-08-18** [`d29dc3ab87`](https://github.com/vllm-project/vllm/commit/d29dc3ab87) [#52430](https://github.com/vllm-project/vllm/pull/52430)
  [Bugfix][Gemma4] Align parser enable_thinking default with template (#52430)
  _Files: `tests/parser/engine/test_gemma4_streaming_reasoning.py`, `tests/reasoning/test_gemma4_reasoning_parser.py`, `vllm/parser/gemma4.py`_
- **2026-08-17** [`402547d7f0`](https://github.com/vllm-project/vllm/commit/402547d7f0) [#52608](https://github.com/vllm-project/vllm/pull/52608)
  [Bugfix][CI] Release the shared ColBERT engine before `test_colbert_hf_comparison` (#52608)
  _Files: `tests/models/language/pooling/test_colbert.py`_

## Disaggregation / PD  (10 commits)

- **2026-08-24** [`26858770ec`](https://github.com/vllm-project/vllm/commit/26858770ec) [#52951](https://github.com/vllm-project/vllm/pull/52951)
  [Bugfix] Reuse CUDA streams in packed weight transfer to cap reserved-memory waste (#52951)
  _Files: `vllm/distributed/weight_transfer/packed_tensor.py`_
- **2026-08-23** [`6cd9713463`](https://github.com/vllm-project/vllm/commit/6cd9713463) [#43375](https://github.com/vllm-project/vllm/pull/43375)
  [RL] P2P RDT weight sync (#43375)
  _Files: `.buildkite/test_areas/distributed.yaml`, `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/base.md`, `docs/training/weight_transfer/sharded_rdt.md` _+20 more__
- **2026-08-21** [`0a3a4f7f35`](https://github.com/vllm-project/vllm/commit/0a3a4f7f35) [#52779](https://github.com/vllm-project/vllm/pull/52779)
  [Bugfix][KV Connector][NIXL] Support PCP producers (#52779)
  _Files: `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py` _+5 more__
- **2026-08-21** [`c8438a3d40`](https://github.com/vllm-project/vllm/commit/c8438a3d40) [#53230](https://github.com/vllm-project/vllm/pull/53230)
  [Doc] Fix dead link in KV transfer README (#53230)
  _Files: `vllm/distributed/kv_transfer/README.md`_
- **2026-08-20** [`5b1e7a812b`](https://github.com/vllm-project/vllm/commit/5b1e7a812b) [#51362](https://github.com/vllm-project/vllm/pull/51362)
  [BugFix][Mooncake] Fix Mooncake saves from sparse Mamba block tables (#51362)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-08-20** [`d66300a1ba`](https://github.com/vllm-project/vllm/commit/d66300a1ba) [#52491](https://github.com/vllm-project/vllm/pull/52491)
  [Bugfix][EPD] Fix encoder round-robin fan-out (#52491)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/ec_connector/unit/test_epd_proxy_round_robin.py`_
- **2026-08-20** [`bf2866f8bf`](https://github.com/vllm-project/vllm/commit/bf2866f8bf) [#52466](https://github.com/vllm-project/vllm/pull/52466)
  [KV Connector] Add decode offloading to Mooncake Store consumers (#52466)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector.py` _+3 more__
- **2026-08-19** [`a2257f95b7`](https://github.com/vllm-project/vllm/commit/a2257f95b7) [#51885](https://github.com/vllm-project/vllm/pull/51885)
  [Elastic EP] Reduce eager-mode reconfiguration downtime (#51885)
  _Files: `tests/distributed/test_eplb_execute.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/config/parallel.py`, `vllm/distributed/elastic_ep/elastic_execute.py` _+8 more__
- **2026-08-18** [`ef47a897e2`](https://github.com/vllm-project/vllm/commit/ef47a897e2) [#51875](https://github.com/vllm-project/vllm/pull/51875)
  [Core] Make prefix-cache NONE_HASH deterministic by default (#51875)
  _Files: `docs/features/kv_offloading_usage.md`, `docs/features/mooncake_store_connector_usage.md`, `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py` _+6 more__
- **2026-08-17** [`017e9f4448`](https://github.com/vllm-project/vllm/commit/017e9f4448) [#52216](https://github.com/vllm-project/vllm/pull/52216)
  Promote `prefix_cache_retention_interval` to an argument and change the default to 0 (#52216)
  _Files: `tests/config/test_config_utils.py`, `tests/engine/test_arg_utils.py`, `tests/v1/core/test_contiguous_kv_packing.py`, `tests/v1/core/test_kv_cache_utils.py` _+13 more__

## Speculative Decoding  (9 commits)

- **2026-08-22** [`da329cc303`](https://github.com/vllm-project/vllm/commit/da329cc303) [#50272](https://github.com/vllm-project/vllm/pull/50272)
  [Bugfix] Fix speculative decoding for short_conv (LFM2) models (#50272)
  _Files: `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/layers/mamba/short_conv.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-21** [`27ec8ac626`](https://github.com/vllm-project/vllm/commit/27ec8ac626) [#42079](https://github.com/vllm-project/vllm/pull/42079)
  [Bugfix] Fix MTP draft model using local cache path instead of S3 URL with runai_streamer (#42079)
  _Files: `tests/test_config.py`, `vllm/config/speculative.py`_
- **2026-08-21** [`1183f04b74`](https://github.com/vllm-project/vllm/commit/1183f04b74) [#48040](https://github.com/vllm-project/vllm/pull/48040)
  [Bugfix] test_batch_inference_correctness now uses batch invariance (#48040)
  _Files: `tests/v1/e2e/spec_decode/draft_model/test_lora.py`_
- **2026-08-21** [`6f74337c47`](https://github.com/vllm-project/vllm/commit/6f74337c47) [#42376](https://github.com/vllm-project/vllm/pull/42376)
  [Bugfix][Spec Decode]Preserve user --speculative-config overrides for speculators-format models (#42376)
  _Files: `tests/transformers_utils/test_speculators_override.py`, `vllm/transformers_utils/config.py`_
- **2026-08-21** [`c6e19b3be2`](https://github.com/vllm-project/vllm/commit/c6e19b3be2) [#53046](https://github.com/vllm-project/vllm/pull/53046)
  [Bugfix][Structured Output] Avoid spurious FSM errors after speculative reasoning end (#53046)
  _Files: `tests/v1/spec_decode/test_mtp_structured_output.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-08-20** [`7cfb97e337`](https://github.com/vllm-project/vllm/commit/7cfb97e337) [#48915](https://github.com/vllm-project/vllm/pull/48915)
  [Frontend][Core][Spec Decode] Per-request acceptance stats in OpenAI API responses (#48915)
  _Files: `docs/features/per_request_metrics.md`, `docs/features/speculative_decoding/README.md`, `docs/features/speculative_decoding/acceptance_metrics.md`, `rust/src/engine-core-client/src/protocol/output.rs` _+21 more__
- **2026-08-20** [`d4f4d3f40f`](https://github.com/vllm-project/vllm/commit/d4f4d3f40f) [#53017](https://github.com/vllm-project/vllm/pull/53017)
  [Model Runner V2][Spec Decode] Fix draft logits cache column stride in gumbel_sample (#53017)
  _Files: `tests/v1/worker/test_gpu_gumbel_sample.py`, `vllm/v1/worker/gpu/sample/gumbel.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-08-19** [`58de6cbdc2`](https://github.com/vllm-project/vllm/commit/58de6cbdc2) [#52929](https://github.com/vllm-project/vllm/pull/52929)
  Add NemotronH_Omni_Reasoning_V3 as a supported Nemotron architecture (#52929)
  _Files: `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/registry.py`_
- **2026-08-17** [`7075ddac28`](https://github.com/vllm-project/vllm/commit/7075ddac28) [#52197](https://github.com/vllm-project/vllm/pull/52197)
  Support DSpark configs with `architectures=DSparkDraftModel` + `model_type=qwen3` (#52197)
  _Files: `vllm/config/speculative.py`_

## LoRA  (8 commits)

- **2026-08-23** [`39eba6ac36`](https://github.com/vllm-project/vllm/commit/39eba6ac36) [#53432](https://github.com/vllm-project/vllm/pull/53432)
  [Misc] Use VLLMValidationError in offline inference input validation (#53432)
  _Files: `tests/entrypoints/llm/test_generate.py`, `tests/entrypoints/test_offline_utils.py`, `tests/lora/test_qwen3_with_multi_loras.py`, `vllm/entrypoints/offline_utils.py`_
- **2026-08-21** [`a60c66e3dc`](https://github.com/vllm-project/vllm/commit/a60c66e3dc) [#53034](https://github.com/vllm-project/vllm/pull/53034)
  [Bugfix] Fix int32 index overflow in LoRA punica kernels at long context (#53034)
  _Files: `vllm/lora/ops/triton_ops/kernel_utils.py`_
- **2026-08-20** [`df1376907b`](https://github.com/vllm-project/vllm/commit/df1376907b) [#51498](https://github.com/vllm-project/vllm/pull/51498)
  [Model] Add tower and connector LoRA support for LFM2-VL (#51498)
  _Files: `vllm/model_executor/models/lfm2_siglip2.py`, `vllm/model_executor/models/lfm2_vl.py`_
- **2026-08-19** [`9b5f3454f2`](https://github.com/vllm-project/vllm/commit/9b5f3454f2) [#52313](https://github.com/vllm-project/vllm/pull/52313)
  [LoRA] Avoid false target matches for unsupported module types (#52313)
  _Files: `tests/lora/test_lora_utils.py`, `vllm/lora/model_manager.py`, `vllm/lora/utils.py`_
- **2026-08-19** [`c2e7242ab7`](https://github.com/vllm-project/vllm/commit/c2e7242ab7) [#47640](https://github.com/vllm-project/vllm/pull/47640)
  [Bugfix][LoRA] Guard None group members in expand_packed_lora (partial LoRA on Qwen3.5/3.6 GatedDeltaNet) (#47640)
  _Files: `vllm/lora/layers/column_parallel_linear.py`_
- **2026-08-19** [`5a4c8d9924`](https://github.com/vllm-project/vllm/commit/5a4c8d9924) [#48850](https://github.com/vllm-project/vllm/pull/48850)
  [Bugfix][LoRA] Add embedding_modules for Qwen3.5 CausalLM (#48850)
  _Files: `vllm/model_executor/models/qwen3_5.py`_
- **2026-08-18** [`241ff8c443`](https://github.com/vllm-project/vllm/commit/241ff8c443) [#49788](https://github.com/vllm-project/vllm/pull/49788)
  [Model] Enable LoRA support for tower and connector in LlavaNextForConditionalGeneration (#49788)
  _Files: `docs/models/supported_models.md`, `vllm/model_executor/models/llava_next.py`_
- **2026-08-17** [`f08a95f8d8`](https://github.com/vllm-project/vllm/commit/f08a95f8d8) [#52031](https://github.com/vllm-project/vllm/pull/52031)
  [Rust Frontend][gRPC] Advertise LoRA capabilities (#52031)
  _Files: `rust/proto/control.proto`, `rust/src/engine-core-client/src/client.rs`, `rust/src/engine-core-client/src/mock_engine.rs`, `rust/src/engine-core-client/src/protocol/handshake.rs` _+6 more__

## Perf / Benchmark  (7 commits)

- **2026-08-22** [`a014e35f38`](https://github.com/vllm-project/vllm/commit/a014e35f38) [#53352](https://github.com/vllm-project/vllm/pull/53352)
  [Pooling] Fix Rust pooling endpoint for benchmark (#53352)
  _Files: `rust/src/bench/README.md`, `rust/src/bench/src/backends/pooling.rs`, `rust/src/bench/src/cli.rs`_
- **2026-08-22** [`704f12aa1e`](https://github.com/vllm-project/vllm/commit/704f12aa1e) [#53213](https://github.com/vllm-project/vllm/pull/53213)
  [Pooling] Report input throughput for batched requests (#53213)
  _Files: `rust/src/bench/src/backends/mod.rs`, `rust/src/bench/src/backends/pooling.rs`, `rust/src/bench/src/compare.rs`, `rust/src/bench/src/metrics/calculator.rs` _+8 more__
- **2026-08-21** [`df344bf36f`](https://github.com/vllm-project/vllm/commit/df344bf36f) [#51570](https://github.com/vllm-project/vllm/pull/51570)
  [Rust][Benchmark] Load HF datasets from parquet shards via hf-hub, fixing truncated-cache sampling (#51570)
  _Files: `rust/Cargo.lock`, `rust/Cargo.toml`, `rust/src/bench/AGENTS.md`, `rust/src/bench/Cargo.toml` _+4 more__
- **2026-08-19** [`aabc1a0a0b`](https://github.com/vllm-project/vllm/commit/aabc1a0a0b) [#51863](https://github.com/vllm-project/vllm/pull/51863)
  [Bugfix][Benchmark] Check readiness before tokenizer init in rust vllm-bench (#51863)
  _Files: `rust/src/bench/src/benchmark.rs`, `rust/src/bench/src/multi_turn.rs`, `rust/src/bench/src/ready_checker.rs`, `rust/src/bench/src/tokenizer.rs`_
- **2026-08-17** [`5ae2d38821`](https://github.com/vllm-project/vllm/commit/5ae2d38821) [#52573](https://github.com/vllm-project/vllm/pull/52573)
  [Perf][Structured Output] Skip unused request-local reasoners (#52573)
  _Files: `tests/v1/structured_output/test_reasoning_structured_output.py`, `vllm/v1/structured_output/__init__.py`_
- **2026-08-17** [`49905ad94d`](https://github.com/vllm-project/vllm/commit/49905ad94d) [#50174](https://github.com/vllm-project/vllm/pull/50174)
  [3/N][Feat][Perf] Add new warmup infrastructure for JITs. Add provider registry and orchestration for JIT warmup (#50174)
  _Files: `docs/contributing/README.md`, `docs/contributing/jit_kernel_warmup.md`, `tests/model_executor/test_jit_warmup.py`, `tests/v1/worker/test_jit_warmup_migration.py` _+8 more__
- **2026-08-17** [`0ff370b51c`](https://github.com/vllm-project/vllm/commit/0ff370b51c) [#52588](https://github.com/vllm-project/vllm/pull/52588)
  docs: fix incorrect --custom-skip-chat-template flag reference (#52588)
  _Files: `docs/benchmarking/cli.md`_

## Quantization  (6 commits)

- **2026-08-24** [`e8888b2d68`](https://github.com/vllm-project/vllm/commit/e8888b2d68) [#53101](https://github.com/vllm-project/vllm/pull/53101)
  [Model] Add FP8 quantization support for ModernBERT (#53101)
  _Files: `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/test_modernbert_fp8.py`, `vllm/model_executor/models/modernbert.py`_
- **2026-08-21** [`9fd750f00d`](https://github.com/vllm-project/vllm/commit/9fd750f00d) [#50501](https://github.com/vllm-project/vllm/pull/50501)
  [XPU][INC] Add int4 w4a8 (dynamic int8 activation) backend for INC linear layers (#50501)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/envs.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_w4a8_linear.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_scheme.py`_
- **2026-08-19** [`541c6d64c1`](https://github.com/vllm-project/vllm/commit/541c6d64c1) [#52966](https://github.com/vllm-project/vllm/pull/52966)
  [Bugfix][Quantization] Support CT block FP8 with Marlin (#52966)
  _Files: `tests/quantization/test_compressed_tensors.py`, `vllm/model_executor/kernels/linear/scaled_mm/marlin.py`_
- **2026-08-19** [`2b7fcbf527`](https://github.com/vllm-project/vllm/commit/2b7fcbf527) [#52775](https://github.com/vllm-project/vllm/pull/52775)
  [Kernel] SM120: stop routing misaligned-M blockwise FP8 GEMMs to the small-M swapAB config (#52775)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`_
- **2026-08-17** [`4ab5e5012a`](https://github.com/vllm-project/vllm/commit/4ab5e5012a) [#52368](https://github.com/vllm-project/vllm/pull/52368)
  [Refactor] Simplify B12X linear kernels and warmup (#52368)
  _Files: `.buildkite/test_areas/kernels.yaml`, `tests/kernels/quantization/test_block_fp8.py`, `tests/model_executor/kernels/test_b12x_linear.py`, `tests/model_executor/kernels/test_b12x_mxfp4_linear.py` _+11 more__
- **2026-08-17** [`53e211d292`](https://github.com/vllm-project/vllm/commit/53e211d292) [#52570](https://github.com/vllm-project/vllm/pull/52570)
  [CI/Build] Reduce more duplicate runner startup in tests (#52570)
  _Files: `tests/models/language/pooling/test_colbert.py`, `tests/models/language/pooling/test_truncation_control.py`, `tests/models/multimodal/generation/test_whisper.py`, `tests/models/multimodal/pooling/test_clip.py` _+6 more__

## Docs  (5 commits)

- **2026-08-24** [`cc40c3673b`](https://github.com/vllm-project/vllm/commit/cc40c3673b) [#53226](https://github.com/vllm-project/vllm/pull/53226)
  [Xeon][doc]add Xeon recipes into table (#53226)
  _Files: `docs/models/hardware_supported_models/cpu.md`_
- **2026-08-21** [`6d8cd88e8d`](https://github.com/vllm-project/vllm/commit/6d8cd88e8d) [#39082](https://github.com/vllm-project/vllm/pull/39082)
  [Docs] document cache salting for prefix cache timing side-channel mitigation (#39082)
  _Files: `docs/usage/security.md`_
- **2026-08-20** [`f85e060ec2`](https://github.com/vllm-project/vllm/commit/f85e060ec2) [#52726](https://github.com/vllm-project/vllm/pull/52726)
  [Doc] Update Gaudi HPU committers (#52726)
  _Files: `docs/governance/committers.md`_
- **2026-08-19** [`58302b4591`](https://github.com/vllm-project/vllm/commit/58302b4591) [#52160](https://github.com/vllm-project/vllm/pull/52160)
  [Doc] Fix group numbering in Case 3 of hybrid_kv_cache_manager.md (#52160)
  _Files: `docs/design/hybrid_kv_cache_manager.md`_
- **2026-08-17** [`502af5ed00`](https://github.com/vllm-project/vllm/commit/502af5ed00) [#50492](https://github.com/vllm-project/vllm/pull/50492)
  [Doc] Add MatrixHub as a model loading source (#50492)
  _Files: `docs/models/supported_models.md`_

## Compilation / CUDA Graph  (4 commits)

- **2026-08-24** [`a4d70bef37`](https://github.com/vllm-project/vllm/commit/a4d70bef37) [#53306](https://github.com/vllm-project/vllm/pull/53306)
  [Model Runner V2] Reserve CUDA graph memory (#53306)
  _Files: `tests/test_config.py`, `tests/v1/sample/test_logprobs.py`, `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` _+9 more__
- **2026-08-21** [`c0ff33404b`](https://github.com/vllm-project/vllm/commit/c0ff33404b) [#53304](https://github.com/vllm-project/vllm/pull/53304)
  Revert compile-cache device index regression on CPU (#53304)
  _Files: `vllm/compilation/backends.py`, `vllm/compilation/decorators.py`_
- **2026-08-21** [`47cd1c8885`](https://github.com/vllm-project/vllm/commit/47cd1c8885) [#40834](https://github.com/vllm-project/vllm/pull/40834)
  [Core] Add dynamo_timed tracing for print_readable (#40834)
  _Files: `vllm/compilation/backends.py`_
- **2026-08-21** [`6dcc5d7cae`](https://github.com/vllm-project/vllm/commit/6dcc5d7cae) [#38962](https://github.com/vllm-project/vllm/pull/38962)
  [Bugfix] Include device index in compile cache paths (#38962)
  _Files: `vllm/compilation/backends.py`, `vllm/compilation/decorators.py`_

## KV Cache / Offload  (2 commits)

- **2026-08-22** [`8bdc70ec7b`](https://github.com/vllm-project/vllm/commit/8bdc70ec7b) [#51718](https://github.com/vllm-project/vllm/pull/51718)
  [6/N][KV-Cache Layout Refactor] Standardize KV cache layout (#51718)
- **2026-08-19** [`f485081e8b`](https://github.com/vllm-project/vllm/commit/f485081e8b) [#49532](https://github.com/vllm-project/vllm/pull/49532)
  [XPU] Support EC connector KV Offloading on XPU (#49532)
  _Files: `.buildkite/intel_jobs/misc_intel.yaml`, `tests/v1/ec_connector/unit/cpu/worker/test_worker.py`, `tests/v1/ec_connector/unit/test_ec_cpu_connector.py`, `vllm/distributed/ec_transfer/ec_connector/cpu/worker/__init__.py` _+1 more__

## Distributed  (1 commits)

- **2026-08-24** [`f94666b60d`](https://github.com/vllm-project/vllm/commit/f94666b60d) [#52389](https://github.com/vllm-project/vllm/pull/52389)
  [Bugfix][XPU] Skip oneCCL warm-up all_reduce when world_size == 1 (#52389)
  _Files: `vllm/v1/worker/xpu_worker.py`_

---
_Generated 2026-08-24 09:00 UTC_