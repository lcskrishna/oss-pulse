# vllm-project/vllm — Weekly Change Report
**Period:** 2026-08-24 → 2026-08-31  |  **Total commits:** 300

## ✨ New Features This Week

- **2026-08-31** [#47434](https://github.com/vllm-project/vllm/pull/47434) — [AutoRound] Support AutoRound Format Block-Wise FP8 in vLLM (#47434)
- **2026-08-31** [#49445](https://github.com/vllm-project/vllm/pull/49445) — [Core] Add `max_num_queued_reqs` and `max_num_queued_tokens` for queue size management (#49445)
- **2026-08-31** [#51248](https://github.com/vllm-project/vllm/pull/51248) — [Quantization][Autoround][XPU] Support AutoRound MXFP8 MoE models (#51248)
- **2026-08-31** [#52191](https://github.com/vllm-project/vllm/pull/52191) — [CPU] Support FP16/BF16 persisted GDN state on AMX (#52191)
- **2026-08-31** [#53896](https://github.com/vllm-project/vllm/pull/53896) — [Model] Support Qwen3.8-Flash-Next (#53896)
- **2026-08-31** [#53921](https://github.com/vllm-project/vllm/pull/53921) — [CPU] add CPU support for Voxtral (#53921)
- **2026-08-31** [#54242](https://github.com/vllm-project/vllm/pull/54242) — [Frontend] Add video embeds input support (#54242)
- **2026-08-30** [#54358](https://github.com/vllm-project/vllm/pull/54358) — [codeowners] Add jperezdealgaba to security file ownership (#54358)
- **2026-08-30** [#53531](https://github.com/vllm-project/vllm/pull/53531) — [Test][VLM] Add batch-invariance tests for Qwen3-VL (#53531)
- **2026-08-30** [#54420](https://github.com/vllm-project/vllm/pull/54420) — ci: add MIG slice size to H200 job labels (#54420)
- _…and 44 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-31** [`76ff0cdff2`](https://github.com/vllm-project/vllm/commit/76ff0cdff2) [#53821](https://github.com/vllm-project/vllm/pull/53821) — [Bugfix][ROCm] Preserve AITER unified-attention metadata during graph replay (#53821)
- **2026-08-31** [`f9d666f917`](https://github.com/vllm-project/vllm/commit/f9d666f917) [#52067](https://github.com/vllm-project/vllm/pull/52067) — [KV Offload] Forward ownership in KV cache events (#52067)
- **2026-08-30** [`e79961c946`](https://github.com/vllm-project/vllm/commit/e79961c946) [#54358](https://github.com/vllm-project/vllm/pull/54358) — [codeowners] Add jperezdealgaba to security file ownership (#54358)
- **2026-08-30** [`2c7d7dd64a`](https://github.com/vllm-project/vllm/commit/2c7d7dd64a) [#52033](https://github.com/vllm-project/vllm/pull/52033) — [Perf][ROCm] Dual-stream decode with hipgraphs (#52033)
- **2026-08-30** [`1ebff996a1`](https://github.com/vllm-project/vllm/commit/1ebff996a1) [#38434](https://github.com/vllm-project/vllm/pull/38434) — [Fix] Improve ROCm detection in WSL environments (#38434)
- **2026-08-30** [`dbf662c9e8`](https://github.com/vllm-project/vllm/commit/dbf662c9e8) [#51171](https://github.com/vllm-project/vllm/pull/51171) — [ROCm][MLA] Reach FULL cudagraphs for AITER MLA speculative decoding (#51171)
- **2026-08-29** [`cacc429f62`](https://github.com/vllm-project/vllm/commit/cacc429f62) [#50920](https://github.com/vllm-project/vllm/pull/50920) — [ROCm][CI] Stage E gating (#50920)
- **2026-08-29** [`93ab92be0c`](https://github.com/vllm-project/vllm/commit/93ab92be0c) [#52047](https://github.com/vllm-project/vllm/pull/52047) — [Bugfix][AMD] Annotate draft KV cache groups on the hybrid grouping path (#52047)
- **2026-08-29** [`16d6c376bc`](https://github.com/vllm-project/vllm/commit/16d6c376bc) [#53507](https://github.com/vllm-project/vllm/pull/53507) — [Bugfix][Models] Register sleep-managed runtime buffers (#53507)
- **2026-08-29** [`43196f2458`](https://github.com/vllm-project/vllm/commit/43196f2458) [#54295](https://github.com/vllm-project/vllm/pull/54295) — [Perf][MLA Sparse] Pin req_id_per_token before non_blocking H2D on XPU and ROCm (#54295)
- **2026-08-28** [`ae5b8e4a8d`](https://github.com/vllm-project/vllm/commit/ae5b8e4a8d) [#52849](https://github.com/vllm-project/vllm/pull/52849) — [ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers (#52849)
- **2026-08-28** [`fd98d32f73`](https://github.com/vllm-project/vllm/commit/fd98d32f73) [#54249](https://github.com/vllm-project/vllm/pull/54249) — [ROCm][CI] Fix test_ray_v2_executor (#54249)
- **2026-08-28** [`70732942c6`](https://github.com/vllm-project/vllm/commit/70732942c6) [#54247](https://github.com/vllm-project/vllm/pull/54247) — [Bugfix][ROCm] Pre-allocate `wvSplitKrc` static workspaces before KV init (#54247)
- **2026-08-28** [`2f1cba799e`](https://github.com/vllm-project/vllm/commit/2f1cba799e) [#53141](https://github.com/vllm-project/vllm/pull/53141) — [ROCm] remove VLLM_ROCM_USE_AITER_FP4_ASM_GEMM environment variable; make w4a4 use the preshuffle triton+asm by default (#53141)
- **2026-08-28** [`06569a8696`](https://github.com/vllm-project/vllm/commit/06569a8696) [#53097](https://github.com/vllm-project/vllm/pull/53097) — [ROCm][Quantization][MOE] Enable fused shared experts for block-quantized FP8 (#53097)
- **2026-08-28** [`5f213ed159`](https://github.com/vllm-project/vllm/commit/5f213ed159) [#53594](https://github.com/vllm-project/vllm/pull/53594) — [ROCm][CI] Warm up the RLHF dev server before the pause/resume timing checks (#53594)
- **2026-08-28** [`9236159bb6`](https://github.com/vllm-project/vllm/commit/9236159bb6) [#53591](https://github.com/vllm-project/vllm/pull/53591) — [ROCm][CI] Keep startup profiling from aborting when free memory grows (#53591)
- **2026-08-27** [`32ad1400d7`](https://github.com/vllm-project/vllm/commit/32ad1400d7) [#53540](https://github.com/vllm-project/vllm/pull/53540) — [ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4 (#53540)
- **2026-08-27** [`fd57c4b7af`](https://github.com/vllm-project/vllm/commit/fd57c4b7af) [#53949](https://github.com/vllm-project/vllm/pull/53949) — [Rocm][CI] add dockerfile.xpu to rocm ci artifact (#53949)
- **2026-08-27** [`aa640684cc`](https://github.com/vllm-project/vllm/commit/aa640684cc) [#53396](https://github.com/vllm-project/vllm/pull/53396) — [Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel (#53396)
- **2026-08-27** [`2dc53bae17`](https://github.com/vllm-project/vllm/commit/2dc53bae17) [#53641](https://github.com/vllm-project/vllm/pull/53641) — [AMD][BugFix] Add gpu_sync_allowed to ROCm AITER FA backend (#53641)
- **2026-08-26** [`1a085dadf2`](https://github.com/vllm-project/vllm/commit/1a085dadf2) [#51040](https://github.com/vllm-project/vllm/pull/51040) — [ROCm][K3] Extend FP8 asm MLA prefill to non-divisor small head counts (#51040)
- **2026-08-26** [`8d301f075b`](https://github.com/vllm-project/vllm/commit/8d301f075b) [#53698](https://github.com/vllm-project/vllm/pull/53698) — [Bugfix][ROCm][Disagg] Fix MoRIIO shared KV memory region registration (#53698)
- **2026-08-26** [`657f9b9ce2`](https://github.com/vllm-project/vllm/commit/657f9b9ce2) [#53838](https://github.com/vllm-project/vllm/pull/53838) — [ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs (#53838)
- **2026-08-26** [`080a66a69c`](https://github.com/vllm-project/vllm/commit/080a66a69c) [#53818](https://github.com/vllm-project/vllm/pull/53818) — [Bugfix][ROCm] Capture CUDA graphs on the current stream (#53818)
- **2026-08-26** [`cde7ba92da`](https://github.com/vllm-project/vllm/commit/cde7ba92da) [#49218](https://github.com/vllm-project/vllm/pull/49218) — [CI/Build][The Rock] Use model_class_overrides so spawned worker can use test PredictableLlamaForCausalLM class when worker spawned using Python 3.14 (#49218)
- **2026-08-26** [`796822d141`](https://github.com/vllm-project/vllm/commit/796822d141) [#53712](https://github.com/vllm-project/vllm/pull/53712) — [Hardware][AMD][Perf][Bugfix] Update ROCr and clr in base image (#53712)
- **2026-08-25** [`bc11ecaf4e`](https://github.com/vllm-project/vllm/commit/bc11ecaf4e) [#50632](https://github.com/vllm-project/vllm/pull/50632) — [CI] Add GSM8K accuracy test for amd/DeepSeek-V4-Flash-MXFP4 (#50632)
- **2026-08-25** [`d9fbe526c0`](https://github.com/vllm-project/vllm/commit/d9fbe526c0) [#53589](https://github.com/vllm-project/vllm/pull/53589) — [ROCm][CI] Skip ModernBERT FP8 MTEB test when no FP8 ScaledMM kernel exists (#53589)
- **2026-08-24** [`d154d90d6c`](https://github.com/vllm-project/vllm/commit/d154d90d6c) [#50465](https://github.com/vllm-project/vllm/pull/50465) — [Model Runner V2] batch-sharded sample (#50465)
- **2026-08-24** [`4c56e62c85`](https://github.com/vllm-project/vllm/commit/4c56e62c85) [#53581](https://github.com/vllm-project/vllm/pull/53581) — [Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling (#53581)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#54521](https://github.com/vllm-project/vllm/issues/54521) | [Bug]: Qwen3.8-Flash-Next: greedy decoding is non-deterministic from p | quantization | 2026-08-31 |
| [#54526](https://github.com/vllm-project/vllm/issues/54526) | [Bug]: Cannot load an Eagle3 model, trained with Speculators | bug | 2026-08-31 |
| [#54595](https://github.com/vllm-project/vllm/issues/54595) | [Bug]: Qwen4Exp is gated off on XPU, but most of what the gate hides i | intel-gpu | 2026-08-31 |
| [#43743](https://github.com/vllm-project/vllm/issues/43743) | [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline  | — | 2026-08-31 |
| [#54591](https://github.com/vllm-project/vllm/issues/54591) | [Bug][Core] --enable-dbo forces the V1 model runner, making dual batch | rocm, quantization, glm | 2026-08-31 |
| [#27433](https://github.com/vllm-project/vllm/issues/27433) | [Feature]: Batch Invariant Feature and Performance Optimization | good first issue, feature request | 2026-08-31 |
| [#49878](https://github.com/vllm-project/vllm/issues/49878) | [Bug]: Dramatic KV cache size increase (~40%) for Gemma4 from v0.25.1  | bug, quantization | 2026-08-31 |
| [#54376](https://github.com/vllm-project/vllm/issues/54376) | [ROCm] Fused shared experts unavailable for GLM-5.3-Flash: Fp8Config n | rocm, quantization, glm | 2026-08-31 |
| [#52911](https://github.com/vllm-project/vllm/issues/52911) | [RFC]: DeepSeek-V4 Performance Optimization on ROCm (Phase Two) | rocm, RFC, deepseek, DSv4 | 2026-08-31 |
| [#54569](https://github.com/vllm-project/vllm/issues/54569) | [Bug]: FunASR get error result with fp16 dtype | bug | 2026-08-31 |
| [#54547](https://github.com/vllm-project/vllm/issues/54547) | [Bug][Quantization] Quark MXFP4 checkpoints are unloadable for multimo | rocm, multi-modality, quantization | 2026-08-31 |
| [#52568](https://github.com/vllm-project/vllm/issues/52568) | [Bug]: Qwen3.5-9B hybrid-GDN + dynamic LoRA on H20 produces NaN output | bug | 2026-08-31 |
| [#54567](https://github.com/vllm-project/vllm/issues/54567) | [Bug]: Prefix caching never hits for DeepSeek-V4-Flash on Jetson Thor  | deepseek, DSv4, kv-cache-manager | 2026-08-31 |
| [#54561](https://github.com/vllm-project/vllm/issues/54561) | [Feature]: DeepSeek-V4-Flash-Vision-Exp (multimodal) — implementation  | multi-modality, deepseek, DSv4 | 2026-08-31 |
| [#54493](https://github.com/vllm-project/vllm/issues/54493) | [Bug]: --enable-dbo reaches an assertion-backed all2all backend valida | bug | 2026-08-31 |
| [#54559](https://github.com/vllm-project/vllm/issues/54559) | [Bug]: qwen3.8-flash-next-fp8: No available shared memory broadcast bl | bug, quantization | 2026-08-31 |
| [#54498](https://github.com/vllm-project/vllm/issues/54498) | [Bug]: V1 EAGLE/MTP drafter mis-addresses KV slots on M-RoPE models | bug, speculative-decoding | 2026-08-31 |
| [#49288](https://github.com/vllm-project/vllm/issues/49288) | [RFC]: Multimodal Asynchronous Collaborative Architecture Sidecar | RFC | 2026-08-31 |
| [#53717](https://github.com/vllm-project/vllm/issues/53717) | [Bug]: MedGemma 27B model:  Repetitive newline-token generation loop | bug | 2026-08-31 |
| [#53241](https://github.com/vllm-project/vllm/issues/53241) | [Usage]: performance degradation 0.26 vs 0.27 for Qwen3.5 122B A10 on  | usage, quantization | 2026-08-31 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Attention | 38 |
| Other | 38 |
| ROCm / AMD | 31 |
| Multimodal | 29 |
| MoE / Expert Parallel | 29 |
| Serving / API | 20 |
| CI / Build | 18 |
| Models | 17 |
| Scheduler / Engine | 16 |
| KV Cache / Offload | 12 |
| Disaggregation / PD | 11 |
| Quantization | 9 |
| Perf / Benchmark | 9 |
| Docs | 8 |
| LoRA | 7 |
| Speculative Decoding | 4 |
| Compilation / CUDA Graph | 3 |
| Distributed | 1 |

## Attention  (38 commits)

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
- **2026-08-30** [`7ab2923489`](https://github.com/vllm-project/vllm/commit/7ab2923489) [#54313](https://github.com/vllm-project/vllm/pull/54313)
  [Flashinfer] Upgrade Flashinfer version to 0.6.18 (#54313)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-bf16-cutlass.yaml` _+1 more__
- **2026-08-30** [`56058fd572`](https://github.com/vllm-project/vllm/commit/56058fd572) [#53877](https://github.com/vllm-project/vllm/pull/53877)
  [Bugfix][Kernel] Keep packed GDN decode beta in FP32 (#53877)
  _Files: `tests/kernels/test_fused_recurrent_packed_decode.py`, `vllm/third_party/flash_linear_attention/ops/fused_recurrent.py`_
- **2026-08-29** [`fe755c8899`](https://github.com/vllm-project/vllm/commit/fe755c8899) [#54282](https://github.com/vllm-project/vllm/pull/54282)
  [Bugfix][Model Runner V2][Spec Decode] Decouple the draft's gumbel noise stream from the target's (#54282)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/v1/worker/test_gpu_gumbel_sample.py`, `vllm/v1/worker/gpu/sample/gumbel.py`, `vllm/v1/worker/gpu/sample/sampler.py` _+7 more__
- **2026-08-29** [`7f4793eaa3`](https://github.com/vllm-project/vllm/commit/7f4793eaa3) [#50611](https://github.com/vllm-project/vllm/pull/50611)
  [Nixl][PD] DCP support for MLA models   (#50611)
  _Files: `tests/test_config.py`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_tp_mapping.py` _+19 more__
- **2026-08-29** [`6d4562c59b`](https://github.com/vllm-project/vllm/commit/6d4562c59b) [#54277](https://github.com/vllm-project/vllm/pull/54277)
  [Attention][DCP] Enable FlashInfer MLA for DSpark drafting (#54277)
  _Files: `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_mla_noncausal.py`, `tests/v1/spec_decode/test_eagle_draft_attn_metadata.py` _+4 more__
- **2026-08-29** [`46a83642f6`](https://github.com/vllm-project/vllm/commit/46a83642f6) [#54292](https://github.com/vllm-project/vllm/pull/54292)
  [Perf] Pin CPU tensors before non_blocking H2D in three MM paths (#54292)
  _Files: `vllm/model_executor/layers/attention/mm_encoder_attention.py`, `vllm/model_executor/models/kanana_v.py`, `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-08-28** [`c01b50e390`](https://github.com/vllm-project/vllm/commit/c01b50e390) [#54132](https://github.com/vllm-project/vllm/pull/54132)
  [Test] Fix mock_current_vllm_config missing kernel_config in test_dflash2 (#54132)
  _Files: `tests/v1/spec_decode/test_dflash2.py`_
- **2026-08-28** [`6f7df92a8e`](https://github.com/vllm-project/vllm/commit/6f7df92a8e) [#51471](https://github.com/vllm-project/vllm/pull/51471)
  [CPU][MLA] Fix prefill backend selection so MLA runs end-to-end on CPU (#51471)
  _Files: `tests/v1/attention/test_cpu_mla_backend.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/_custom_ops.py`, `vllm/model_executor/layers/attention/mla_attention.py` _+5 more__
- **2026-08-28** [`6ec92bcbc8`](https://github.com/vllm-project/vllm/commit/6ec92bcbc8) [#54015](https://github.com/vllm-project/vllm/pull/54015)
  [Kimi-K3] Merge MLA gate into QKV-A projection (#54015)
  _Files: `vllm/model_executor/layers/linear.py`, `vllm/models/kimi_k3/nvidia/mla.py`, `vllm/models/kimi_k3/nvidia/model.py`, `vllm/models/kimi_k3/nvidia/mtp.py`_
- **2026-08-27** [`e5377e6727`](https://github.com/vllm-project/vllm/commit/e5377e6727) [#54005](https://github.com/vllm-project/vllm/pull/54005)
  [Bugfix][Model] Fix K3 DSpark config for 96-head drafts (#54005)
  _Files: `tests/transformers_utils/test_dspark_mla_config.py`, `vllm/transformers_utils/configs/k3_dspark.py`_
- **2026-08-27** [`7c877062ac`](https://github.com/vllm-project/vllm/commit/7c877062ac) [#50572](https://github.com/vllm-project/vllm/pull/50572)
  [kernel] Integrate FlashInfer BF16 CuTeDSL Low Latency GEMM (#50572)
  _Files: `tests/kernels/test_flashinfer_bf16_gemm.py`, `vllm/config/kernel.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/layers/linear.py` _+3 more__
- **2026-08-27** [`f79a2f5582`](https://github.com/vllm-project/vllm/commit/f79a2f5582) [#53797](https://github.com/vllm-project/vllm/pull/53797)
  Add support for loading dflash2 model in speculators format (#53797)
  _Files: `vllm/transformers_utils/configs/speculators/algos.py`, `vllm/transformers_utils/configs/speculators/base.py`_
- **2026-08-27** [`de9250ac9e`](https://github.com/vllm-project/vllm/commit/de9250ac9e) [#53785](https://github.com/vllm-project/vllm/pull/53785)
  [Attention] Enable masked MHA for GLM-5 head dimensions (#53785)
  _Files: `benchmarks/attention_benchmarks/benchmark.py`, `benchmarks/attention_benchmarks/configs/mla_sparse_masked_mha_vs_mqa_glm5.yaml`, `benchmarks/attention_benchmarks/mla_runner.py`, `cmake/external_projects/vllm_flash_attn.cmake` _+6 more__
- **2026-08-27** [`4aab2b0ebe`](https://github.com/vllm-project/vllm/commit/4aab2b0ebe) [#53183](https://github.com/vllm-project/vllm/pull/53183)
  [Model Runner V2] Use MRV2 for all models by default (#53183)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `tests/test_config.py`, `vllm/compilation/decorators.py`, `vllm/config/vllm.py` _+1 more__
- **2026-08-27** [`07242faa46`](https://github.com/vllm-project/vllm/commit/07242faa46) [#54012](https://github.com/vllm-project/vllm/pull/54012)
  [Attention][DCP] Use FlashInfer native CP for MLA decode (#54012)
  _Files: `tests/v1/attention/test_flashinfer_mla_dcp.py`, `tests/v1/attention/test_mla_backends.py`, `vllm/v1/attention/backends/mla/flashinfer_mla.py`_
- **2026-08-27** [`d21c5b50a1`](https://github.com/vllm-project/vllm/commit/d21c5b50a1) [#53878](https://github.com/vllm-project/vllm/pull/53878)
  [Perf][GLM5.2] Fuse sparse MLA Q concatenation with head padding (#53878)
  _Files: `tests/kernels/test_concat_mla_q.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/flashmla_sparse.py`_
- **2026-08-27** [`c7b0467c25`](https://github.com/vllm-project/vllm/commit/c7b0467c25) [#50932](https://github.com/vllm-project/vllm/pull/50932)
  buffer size insuffient Dspark sd for FlashInfer MNNVL allreduce (#50932)
  _Files: `vllm/distributed/device_communicators/flashinfer_all_reduce.py`, `vllm/model_executor/layers/fused_allreduce_gemma_rms_norm.py`_
- **2026-08-27** [`75dea9b4ae`](https://github.com/vllm-project/vllm/commit/75dea9b4ae) [#53755](https://github.com/vllm-project/vllm/pull/53755)
  [Bugfix] Update FlashMLA for sparse decode workspace fix (#53755)
  _Files: `cmake/external_projects/flashmla.cmake`_
- **2026-08-27** [`5acc1c4e4b`](https://github.com/vllm-project/vllm/commit/5acc1c4e4b) [#53694](https://github.com/vllm-project/vllm/pull/53694)
  [Model Runner V2][Spec Decode] Skip DP sync before EAGLE/MTP draft prefill (#53694)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/v1/worker/gpu/dp_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/spec_decode/autoregressive/speculator.py` _+4 more__
- **2026-08-26** [`0a5ad6f0d4`](https://github.com/vllm-project/vllm/commit/0a5ad6f0d4) [#53697](https://github.com/vllm-project/vllm/pull/53697)
  [Model] Remove unused DeepSeek V4 top-k buffer helper (#53697)
  _Files: `vllm/models/deepseek_v4/attention.py`_
- **2026-08-26** [`28b484e5d7`](https://github.com/vllm-project/vllm/commit/28b484e5d7) [#52185](https://github.com/vllm-project/vllm/pull/52185)
  [Model] Pixtral: use packed multimodal encoder attention (#52185)
  _Files: `tests/models/multimodal/generation/test_pixtral.py`, `vllm/model_executor/models/pixtral.py`_
- **2026-08-26** [`2267d3b112`](https://github.com/vllm-project/vllm/commit/2267d3b112) [#53705](https://github.com/vllm-project/vllm/pull/53705)
  [AttentionBackend][HPC-ops] update hpc rope norm to support stride kv cache (#53705)
  _Files: `vllm/model_executor/layers/hpc/rope_norm.py`_
- **2026-08-26** [`7156c63bef`](https://github.com/vllm-project/vllm/commit/7156c63bef) [#52980](https://github.com/vllm-project/vllm/pull/52980)
  [SM100] Hdim 256 optimized (#52980)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`, `docs/design/attention_backends.md`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_flash_attn.py` _+3 more__
- **2026-08-26** [`88e1b11313`](https://github.com/vllm-project/vllm/commit/88e1b11313) [#53606](https://github.com/vllm-project/vllm/pull/53606)
  [Perf] Tune FlashInfer all-reduce thresholds for single-node TP8 on SM103 (#53606)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`, `vllm/distributed/device_communicators/all_reduce_utils.py`_
- **2026-08-25** [`7de96050c5`](https://github.com/vllm-project/vllm/commit/7de96050c5) [#52783](https://github.com/vllm-project/vllm/pull/52783)
  [Spec Decode] Enable adaptive DSpark on SM100 sparse MLA (#52783)
  _Files: `tests/v1/attention/test_dspark_noncausal_sparse_mla.py`, `tests/v1/spec_decode/test_adaptive_verification.py`, `tests/v1/worker/test_attn_utils.py`, `vllm/v1/attention/backends/mla/flashinfer_mla_sparse.py` _+3 more__
- **2026-08-25** [`a9a17e7095`](https://github.com/vllm-project/vllm/commit/a9a17e7095) [#53435](https://github.com/vllm-project/vllm/pull/53435)
  Dflash2 load fix (#53435)
  _Files: `tests/v1/spec_decode/test_dflash2.py`, `vllm/model_executor/models/qwen3_dflash.py`_
- **2026-08-25** [`cbe3966f9c`](https://github.com/vllm-project/vllm/commit/cbe3966f9c) [#52066](https://github.com/vllm-project/vllm/pull/52066)
  [XPU] Fix sparse-MLA metadata sync (#52066)
  _Files: `vllm/v1/attention/backends/mla/xpu_mla_sparse.py`_
- **2026-08-24** [`a0f1b9ad05`](https://github.com/vllm-project/vllm/commit/a0f1b9ad05) [#53646](https://github.com/vllm-project/vllm/pull/53646)
  [CI][The Rock] Increase flex attention abs tol (#53646)
  _Files: `tests/entrypoints/pooling/scoring/test_cross_encoder_online_vision.py`_
- **2026-08-24** [`6a9c69fa85`](https://github.com/vllm-project/vllm/commit/6a9c69fa85) [#52157](https://github.com/vllm-project/vllm/pull/52157)
  [Attention][Spec Decode] Support varlen trtllm-gen decode for adaptive verification (#52157)
  _Files: `tests/kernels/attention/test_flashinfer_trtllm_attention.py`, `vllm/v1/attention/backends/flashinfer.py`_
- **2026-08-24** [`4f686e182a`](https://github.com/vllm-project/vllm/commit/4f686e182a) [#53559](https://github.com/vllm-project/vllm/pull/53559)
  [MISC] Cleanup deprecated parameters (#53559)
  _Files: `tests/plugins/bge_m3_sparse_plugin/bge_m3_sparse_processor/sparse_embeddings_processor.py`, `vllm/config/attention.py`, `vllm/entrypoints/pooling/base/io_processor.py`, `vllm/entrypoints/pooling/offline.py` _+8 more__
- **2026-08-24** [`f620499ee3`](https://github.com/vllm-project/vllm/commit/f620499ee3) [#53336](https://github.com/vllm-project/vllm/pull/53336)
  [Bugfix][Spec Decode] Reapply group geometry for FlashAttention metadata (#53336)
  _Files: `tests/v1/attention/test_group_head_counts.py`, `vllm/v1/attention/backends/flash_attn.py`, `vllm/v1/attention/backends/utils.py`, `vllm/v1/worker/gpu/spec_decode/dflash/speculator.py`_
- **2026-08-24** [`22099afc64`](https://github.com/vllm-project/vllm/commit/22099afc64) [#52377](https://github.com/vllm-project/vllm/pull/52377)
  [Bugfix][DCP] Handle sparse MLA metadata after DCP Manager refactor (#52377)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/v1/attention/ops/dcp.py`_
- **2026-08-24** [`e6e1af4ca1`](https://github.com/vllm-project/vllm/commit/e6e1af4ca1) [#53318](https://github.com/vllm-project/vllm/pull/53318)
  [Perf] Tune FlashInfer all-reduce selection on SM103 (#53318)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/device_communicators/all_reduce_utils.py`, `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/distributed/device_communicators/flashinfer_all_reduce.py`_

## Other  (38 commits)

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
- **2026-08-30** [`8c51b92654`](https://github.com/vllm-project/vllm/commit/8c51b92654) [#54400](https://github.com/vllm-project/vllm/pull/54400)
  [Bugfix] Avoid global config lookup in sparse indexer forward (#54400)
  _Files: `vllm/model_executor/layers/sparse_attn_indexer.py`_
- **2026-08-30** [`b383e16396`](https://github.com/vllm-project/vllm/commit/b383e16396) [#54044](https://github.com/vllm-project/vllm/pull/54044)
  [Bugfix] Reset cached Mamba align metadata on profiling teardown (#54044)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-29** [`5b0e5b69ac`](https://github.com/vllm-project/vllm/commit/5b0e5b69ac) [#54196](https://github.com/vllm-project/vllm/pull/54196)
  [Bugfix][Frontend] Validate stop_token_ids against vocab size (#54196)
  _Files: `vllm/sampling_params.py`_
- **2026-08-29** [`d3d79ffc1e`](https://github.com/vllm-project/vllm/commit/d3d79ffc1e) [#50488](https://github.com/vllm-project/vllm/pull/50488)
  [Bugfix][Spec Decode] Capture the widest uniform decode batch by default (#50488)
  _Files: `tests/compile/test_config.py`, `tests/v1/cudagraph/test_cudagraph_manager.py`, `tests/v1/spec_decode/test_dynamic_sd_cug.py`, `vllm/config/compilation.py` _+2 more__
- **2026-08-29** [`f4f3bcd4b4`](https://github.com/vllm-project/vllm/commit/f4f3bcd4b4) [#54310](https://github.com/vllm-project/vllm/pull/54310)
  [Test] Assert co-located RayExecutorV2 stores publish distinct ports (#54310)
  _Files: `tests/distributed/test_ray_v2_executor.py`_
- **2026-08-29** [`3958a420f0`](https://github.com/vllm-project/vllm/commit/3958a420f0) [#54284](https://github.com/vllm-project/vllm/pull/54284)
  [Bugfix][V1] Keep an encoder cache entry until its last occurrence is freed (#54284)
  _Files: `tests/v1/core/test_encoder_cache_manager.py`, `vllm/v1/core/encoder_cache_manager.py`_
- **2026-08-29** [`5182f2705b`](https://github.com/vllm-project/vllm/commit/5182f2705b) [#52367](https://github.com/vllm-project/vllm/pull/52367)
  [CI/Build] Use file rendezvous for UniProc loader fixtures (#52367)
  _Files: `tests/model_executor/model_loader/runai_streamer_loader/conftest.py`, `tests/model_executor/model_loader/tensorizer_loader/conftest.py`_
- **2026-08-29** [`68c52b5a93`](https://github.com/vllm-project/vllm/commit/68c52b5a93) [#36255](https://github.com/vllm-project/vllm/pull/36255)
  fix: improve token_ids_cpu swap to copy only valid indices (#36255)
  _Files: `vllm/v1/worker/tpu_input_batch.py`_
- **2026-08-28** [`9662ab0835`](https://github.com/vllm-project/vllm/commit/9662ab0835) [#53293](https://github.com/vllm-project/vllm/pull/53293)
  [Bugfix] Set breakable graph env before Ray actor import (#53293)
  _Files: `tests/test_ray_env_utils.py`, `vllm/v1/executor/ray_env_utils.py`, `vllm/v1/executor/ray_executor.py`, `vllm/v1/executor/ray_executor_v2.py`_
- **2026-08-28** [`67e86d1e6f`](https://github.com/vllm-project/vllm/commit/67e86d1e6f) [#50969](https://github.com/vllm-project/vllm/pull/50969)
  [BugFix] Bind RayExecutorV2 TCPStore before publishing its port (#50969)
  _Files: `tests/distributed/test_ray_v2_executor.py`, `vllm/v1/executor/ray_executor_v2.py`_
- **2026-08-28** [`e6bfe03ad7`](https://github.com/vllm-project/vllm/commit/e6bfe03ad7) [#52227](https://github.com/vllm-project/vllm/pull/52227)
  Count store offers, not lookups, for CPU offload store_threshold (#52227)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/manager.py`, `vllm/v1/kv_offload/cpu/spec.py`_
- **2026-08-28** [`8cfba696ee`](https://github.com/vllm-project/vllm/commit/8cfba696ee) [#54108](https://github.com/vllm-project/vllm/pull/54108)
  [Misc] Separate adaptive verification config validation (#54108)
  _Files: `vllm/config/vllm.py`_
- **2026-08-28** [`b2a6e9dca0`](https://github.com/vllm-project/vllm/commit/b2a6e9dca0) [#52743](https://github.com/vllm-project/vllm/pull/52743)
  fix(build): correct preprocessor guard for GDN decode to fix Ampere c… (#52743)
  _Files: `csrc/libtorch_stable/ops.h`_
- **2026-08-27** [`479eeb32d2`](https://github.com/vllm-project/vllm/commit/479eeb32d2) [#53508](https://github.com/vllm-project/vllm/pull/53508)
  [Bugfix][MRV2] Isolate sleep-mode KV allocations (#53508)
  _Files: `tests/basic_correctness/test_mem.py`, `tests/v1/worker/test_gpu_model_runner.py`, `tests/v1/worker/test_kv_cache_allocation_scope.py`, `vllm/v1/worker/cpu_model_runner.py` _+5 more__
- **2026-08-27** [`f18e29834b`](https://github.com/vllm-project/vllm/commit/f18e29834b) [#53965](https://github.com/vllm-project/vllm/pull/53965)
  [Bugfix] Preserve parallel HY-V3 calls delivered in one streaming delta (#53965)
  _Files: `vllm/tool_parsers/hy_v3_tool_parser.py`_
- **2026-08-27** [`6d11122607`](https://github.com/vllm-project/vllm/commit/6d11122607) [#53378](https://github.com/vllm-project/vllm/pull/53378)
  [Elastic EP] Preserve AOT cache reuse during scaling (#53378)
  _Files: `vllm/config/compilation.py`, `vllm/envs.py`_
- **2026-08-27** [`51d1b45182`](https://github.com/vllm-project/vllm/commit/51d1b45182) [#52222](https://github.com/vllm-project/vllm/pull/52222)
  [Bugfix][GPT-OSS] Fix strict tool-call grammar to accept Harmony renders (#52222)
  _Files: `tests/parser/test_harmony.py`, `vllm/parser/harmony.py`_
- **2026-08-26** [`d1e5e66ee3`](https://github.com/vllm-project/vllm/commit/d1e5e66ee3) [#53952](https://github.com/vllm-project/vllm/pull/53952)
  [Bugfix] Restore portable all2all backend default (#53952)
  _Files: `tests/test_config.py`, `vllm/config/parallel.py`_
- **2026-08-26** [`31739ceb0b`](https://github.com/vllm-project/vllm/commit/31739ceb0b) [#53866](https://github.com/vllm-project/vllm/pull/53866)
  [CI/Build] Improve pre-commit fail message (#53866)
  _Files: `.github/workflows/pre-commit.yml`_
- **2026-08-26** [`e376d45e82`](https://github.com/vllm-project/vllm/commit/e376d45e82) [#53853](https://github.com/vllm-project/vllm/pull/53853)
  [Config] Delegate PCP compatibility checks to PCP manager (#53853)
  _Files: `vllm/config/vllm.py`_
- **2026-08-26** [`a447955aca`](https://github.com/vllm-project/vllm/commit/a447955aca) [#53773](https://github.com/vllm-project/vllm/pull/53773)
  [Kimi Bug] Fix k3 torch.AcceleratorError: CUDA error: an illegal memory access was encountered (#53773)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-25** [`80771bbbdd`](https://github.com/vllm-project/vllm/commit/80771bbbdd) [#51292](https://github.com/vllm-project/vllm/pull/51292)
  [Core] Disable fuse_allreduce_rms under VLLM_BATCH_INVARIANT (non-deterministic under TP) (#51292)
  _Files: `vllm/config/vllm.py`_
- **2026-08-25** [`0e30bd62fe`](https://github.com/vllm-project/vllm/commit/0e30bd62fe) [#53766](https://github.com/vllm-project/vllm/pull/53766)
  [CI Bug] Fix kimi test `AssertionError: Aligned Mamba state indices must be precomputed` (#53766)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`_
- **2026-08-25** [`e6cc0899b6`](https://github.com/vllm-project/vllm/commit/e6cc0899b6) [#53682](https://github.com/vllm-project/vllm/pull/53682)
  [Bugfix][MRV2] Run cudagraph memory profiling in a throwaway graph pool (#53682)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-25** [`3454335f7b`](https://github.com/vllm-project/vllm/commit/3454335f7b) [#53326](https://github.com/vllm-project/vllm/pull/53326)
  [Bugfix] Resolve B12X modules before Dynamo tracing (#53326)
  _Files: `tests/model_executor/kernels/test_b12x_linear.py`, `vllm/utils/b12x.py`_
- **2026-08-25** [`41729fc53b`](https://github.com/vllm-project/vllm/commit/41729fc53b) [#52388](https://github.com/vllm-project/vllm/pull/52388)
  [K3 Perf] Optimize k3 mamba metadata preparation, 6.6~7.6x kernel performance improvement (#52388)
  _Files: `tests/models/kimi_k3/test_kda_metadata.py`, `vllm/models/kimi_k3/nvidia/kda_metadata.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-08-25** [`2014e47485`](https://github.com/vllm-project/vllm/commit/2014e47485) [#53467](https://github.com/vllm-project/vllm/pull/53467)
  [Pooling UX] Improve serve --task error guidance (#53467)
  _Files: `vllm/utils/argparse_utils.py`_
- **2026-08-25** [`afc91fa0d2`](https://github.com/vllm-project/vllm/commit/afc91fa0d2) [#51839](https://github.com/vllm-project/vllm/pull/51839)
  [Profiler] Fix start_profile permanently no-op after max_iterations auto-stop (#51839)
  _Files: `tests/v1/worker/test_gpu_profiler.py`, `vllm/profiler/wrapper.py`_
- **2026-08-25** [`c74dd2d208`](https://github.com/vllm-project/vllm/commit/c74dd2d208) [#53407](https://github.com/vllm-project/vllm/pull/53407)
  [Bugfix][MRV2] Dispatch uniform decode to a padded FULL cudagraph (#53407)
  _Files: `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-25** [`af119619c4`](https://github.com/vllm-project/vllm/commit/af119619c4) [#53530](https://github.com/vllm-project/vllm/pull/53530)
  Exclude the cpu backend from vLLM's active-Triton-driver count (#53530) (#53530)
  _Files: `tests/test_triton_utils.py`, `vllm/triton_utils/importing.py`_
- **2026-08-24** [`f59bb0bd8c`](https://github.com/vllm-project/vllm/commit/f59bb0bd8c) [#53619](https://github.com/vllm-project/vllm/pull/53619)
  [Refactor] Refactor batch invariance folder (#53619)
  _Files: `.github/CODEOWNERS`, `examples/rl/rlhf_async_new_apis.py`, `tests/v1/determinism/test_matmul_batch_invariant.py`, `tests/v1/determinism/test_rms_norm_batch_invariant.py` _+7 more__
- **2026-08-24** [`6648eb118d`](https://github.com/vllm-project/vllm/commit/6648eb118d) [#48687](https://github.com/vllm-project/vllm/pull/48687)
  [Core] drop duplicate VLLM_USE_DEEP_GEMM check (#48687)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-08-24** [`4ca856b0b5`](https://github.com/vllm-project/vllm/commit/4ca856b0b5) [#51979](https://github.com/vllm-project/vllm/pull/51979)
  [Bugfix] Release worker RPC payload before next dequeue (#51979)
  _Files: `tests/v1/executor/test_multiproc_executor.py`, `vllm/v1/executor/multiproc_executor.py`_
- **2026-08-24** [`0ecc284790`](https://github.com/vllm-project/vllm/commit/0ecc284790) [#51031](https://github.com/vllm-project/vllm/pull/51031)
  [Bugfix][Kernel] Handle kernel block sizes in V2 DCP slot mapping (#51031)
  _Files: `tests/v1/worker/test_gpu_block_table.py`, `vllm/v1/worker/gpu/block_table.py`_

## ROCm / AMD  (31 commits)

- **2026-08-31** [`76ff0cdff2`](https://github.com/vllm-project/vllm/commit/76ff0cdff2) [#53821](https://github.com/vllm-project/vllm/pull/53821)
  [Bugfix][ROCm] Preserve AITER unified-attention metadata during graph replay (#53821)
  _Files: `tests/v1/attention/test_rocm_attention_backends_selection.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-08-31** [`f9d666f917`](https://github.com/vllm-project/vllm/commit/f9d666f917) [#52067](https://github.com/vllm-project/vllm/pull/52067)
  [KV Offload] Forward ownership in KV cache events (#52067)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `vllm/distributed/kv_events.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py`, `vllm/v1/kv_offload/base.py`_
- **2026-08-30** [`e79961c946`](https://github.com/vllm-project/vllm/commit/e79961c946) [#54358](https://github.com/vllm-project/vllm/pull/54358)
  [codeowners] Add jperezdealgaba to security file ownership (#54358)
  _Files: `.github/CODEOWNERS`_
- **2026-08-30** [`2c7d7dd64a`](https://github.com/vllm-project/vllm/commit/2c7d7dd64a) [#52033](https://github.com/vllm-project/vllm/pull/52033)
  [Perf][ROCm] Dual-stream decode with hipgraphs (#52033)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`_
- **2026-08-30** [`1ebff996a1`](https://github.com/vllm-project/vllm/commit/1ebff996a1) [#38434](https://github.com/vllm-project/vllm/pull/38434)
  [Fix] Improve ROCm detection in WSL environments (#38434)
  _Files: `vllm/platforms/__init__.py`_
- **2026-08-30** [`dbf662c9e8`](https://github.com/vllm-project/vllm/commit/dbf662c9e8) [#51171](https://github.com/vllm-project/vllm/pull/51171)
  [ROCm][MLA] Reach FULL cudagraphs for AITER MLA speculative decoding (#51171)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_causal_verify_mask.py`, `tests/v1/attention/test_rocm_aiter_mla_mtp_split.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`, `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-08-29** [`cacc429f62`](https://github.com/vllm-project/vllm/commit/cacc429f62) [#50920](https://github.com/vllm-project/vllm/pull/50920)
  [ROCm][CI] Stage E gating (#50920)
  _Files: `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/docker.yaml`, `.buildkite/test_areas/e2e_integration.yaml` _+6 more__
- **2026-08-29** [`93ab92be0c`](https://github.com/vllm-project/vllm/commit/93ab92be0c) [#52047](https://github.com/vllm-project/vllm/pull/52047)
  [Bugfix][AMD] Annotate draft KV cache groups on the hybrid grouping path (#52047)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-08-29** [`16d6c376bc`](https://github.com/vllm-project/vllm/commit/16d6c376bc) [#53507](https://github.com/vllm-project/vllm/pull/53507)
  [Bugfix][Models] Register sleep-managed runtime buffers (#53507)
  _Files: `tests/basic_correctness/test_mem.py`, `tests/model_executor/test_sleep_mode_tensor_ownership.py`, `vllm/model_executor/models/conformer_encoder.py`, `vllm/model_executor/models/ernie45_vl.py` _+2 more__
- **2026-08-29** [`43196f2458`](https://github.com/vllm-project/vllm/commit/43196f2458) [#54295](https://github.com/vllm-project/vllm/pull/54295)
  [Perf][MLA Sparse] Pin req_id_per_token before non_blocking H2D on XPU and ROCm (#54295)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse.py`, `vllm/v1/attention/backends/mla/xpu_mla_sparse.py`_
- **2026-08-28** [`ae5b8e4a8d`](https://github.com/vllm-project/vllm/commit/ae5b8e4a8d) [#52849](https://github.com/vllm-project/vllm/pull/52849)
  [ROCm][PERF] Enable AITER PA gluon decode for MiniMax-M3 MTP and dense layers (#52849)
  _Files: `vllm/models/minimax_m3/amd/model.py`, `vllm/models/minimax_m3/amd/ops/sparse_pa.py`, `vllm/models/minimax_m3/amd/sparse_attention_msa.py`, `vllm/models/minimax_m3/common/sparse_attention.py` _+1 more__
- **2026-08-28** [`fd98d32f73`](https://github.com/vllm-project/vllm/commit/fd98d32f73) [#54249](https://github.com/vllm-project/vllm/pull/54249)
  [ROCm][CI] Fix test_ray_v2_executor (#54249)
  _Files: `vllm/v1/executor/ray_utils.py`_
- **2026-08-28** [`70732942c6`](https://github.com/vllm-project/vllm/commit/70732942c6) [#54247](https://github.com/vllm-project/vllm/pull/54247)
  [Bugfix][ROCm] Pre-allocate `wvSplitKrc` static workspaces before KV init (#54247)
  _Files: `vllm/model_executor/layers/utils.py`, `vllm/v1/worker/utils.py`_
- **2026-08-28** [`2f1cba799e`](https://github.com/vllm-project/vllm/commit/2f1cba799e) [#53141](https://github.com/vllm-project/vllm/pull/53141)
  [ROCm] remove VLLM_ROCM_USE_AITER_FP4_ASM_GEMM environment variable; make w4a4 use the preshuffle triton+asm by default (#53141)
  _Files: `tests/kernels/quantization/test_rocm_mxfp4.py`, `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/kernels/linear/mxfp4/aiter.py`_
- **2026-08-28** [`06569a8696`](https://github.com/vllm-project/vllm/commit/06569a8696) [#53097](https://github.com/vllm-project/vllm/pull/53097)
  [ROCm][Quantization][MOE] Enable fused shared experts for block-quantized FP8 (#53097)
  _Files: `tests/model_executor/layers/test_fused_shared_expert.py`, `vllm/model_executor/layers/quantization/utils/config_utils.py`_
- **2026-08-28** [`5f213ed159`](https://github.com/vllm-project/vllm/commit/5f213ed159) [#53594](https://github.com/vllm-project/vllm/pull/53594)
  [ROCm][CI] Warm up the RLHF dev server before the pause/resume timing checks (#53594)
  _Files: `tests/entrypoints/serve/dev/rlhf/conftest.py`_
- **2026-08-28** [`9236159bb6`](https://github.com/vllm-project/vllm/commit/9236159bb6) [#53591](https://github.com/vllm-project/vllm/pull/53591)
  [ROCm][CI] Keep startup profiling from aborting when free memory grows (#53591)
  _Files: `tests/v1/worker/test_gpu_worker.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-08-27** [`32ad1400d7`](https://github.com/vllm-project/vllm/commit/32ad1400d7) [#53540](https://github.com/vllm-project/vllm/pull/53540)
  [ROCm][Perf] Fuse SWA q/kv RMSNorm and q FP8 group quant for DeepSeek-V4 (#53540)
  _Files: `tests/kernels/core/test_rocm_aiter_ops.py`, `vllm/_aiter_ops.py`, `vllm/models/deepseek_v4/amd/rocm.py`, `vllm/models/deepseek_v4/attention.py`_
- **2026-08-27** [`fd57c4b7af`](https://github.com/vllm-project/vllm/commit/fd57c4b7af) [#53949](https://github.com/vllm-project/vllm/pull/53949)
  [Rocm][CI] add dockerfile.xpu to rocm ci artifact (#53949)
  _Files: `tests/tools/test_docker_build_metadata_args.py`_
- **2026-08-27** [`aa640684cc`](https://github.com/vllm-project/vllm/commit/aa640684cc) [#53396](https://github.com/vllm-project/vllm/pull/53396)
  [Kimi K3][Kernel] Support DS conv-state layout in fused KDA decode kernel (#53396)
  _Files: `benchmarks/kernels/benchmark_kimi_k3_kda_decode.py`, `csrc/libtorch_stable/kimi_k3/fused_kda_decode_kernel.cu`, `csrc/libtorch_stable/kimi_k3/fused_kda_decode_kernel_rocm.cu`, `tests/models/kimi_k3/test_kda.py` _+1 more__
- **2026-08-27** [`2dc53bae17`](https://github.com/vllm-project/vllm/commit/2dc53bae17) [#53641](https://github.com/vllm-project/vllm/pull/53641)
  [AMD][BugFix] Add gpu_sync_allowed to ROCm AITER FA backend (#53641)
  _Files: `vllm/v1/attention/backends/rocm_aiter_fa.py`_
- **2026-08-26** [`1a085dadf2`](https://github.com/vllm-project/vllm/commit/1a085dadf2) [#51040](https://github.com/vllm-project/vllm/pull/51040)
  [ROCm][K3] Extend FP8 asm MLA prefill to non-divisor small head counts (#51040)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_prefill.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-08-26** [`8d301f075b`](https://github.com/vllm-project/vllm/commit/8d301f075b) [#53698](https://github.com/vllm-project/vllm/pull/53698)
  [Bugfix][ROCm][Disagg] Fix MoRIIO shared KV memory region registration (#53698)
  _Files: `tests/v1/kv_connector/unit/test_moriio_kv_layout.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py` _+1 more__
- **2026-08-26** [`657f9b9ce2`](https://github.com/vllm-project/vllm/commit/657f9b9ce2) [#53838](https://github.com/vllm-project/vllm/pull/53838)
  [ROCm][DSV4][Perf] Fuse DeepSeek V4 C4 compressor GEMMs (#53838)
  _Files: `tests/models/test_deepseek_v4_rocm_compressor_gemm_fusion.py`, `vllm/models/deepseek_v4/amd/model.py`, `vllm/models/deepseek_v4/amd/rocm.py`_
- **2026-08-26** [`080a66a69c`](https://github.com/vllm-project/vllm/commit/080a66a69c) [#53818](https://github.com/vllm-project/vllm/pull/53818)
  [Bugfix][ROCm] Capture CUDA graphs on the current stream (#53818)
  _Files: `vllm/v1/spec_decode/gemma4.py`, `vllm/v1/worker/encoder_cudagraph.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-26** [`cde7ba92da`](https://github.com/vllm-project/vllm/commit/cde7ba92da) [#49218](https://github.com/vllm-project/vllm/pull/49218)
  [CI/Build][The Rock] Use model_class_overrides so spawned worker can use test PredictableLlamaForCausalLM class when worker spawned using Python 3.14 (#49218)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`_
- **2026-08-26** [`796822d141`](https://github.com/vllm-project/vllm/commit/796822d141) [#53712](https://github.com/vllm-project/vllm/pull/53712)
  [Hardware][AMD][Perf][Bugfix] Update ROCr and clr in base image (#53712)
  _Files: `docker/Dockerfile.rocm_base`_
- **2026-08-25** [`bc11ecaf4e`](https://github.com/vllm-project/vllm/commit/bc11ecaf4e) [#50632](https://github.com/vllm-project/vllm/pull/50632)
  [CI] Add GSM8K accuracy test for amd/DeepSeek-V4-Flash-MXFP4 (#50632)
  _Files: `.buildkite/lm-eval-harness/configs/DeepSeek-V4-Flash-MXFP4.yaml`, `.buildkite/lm-eval-harness/configs/models-large-rocm-tp4.txt`, `.buildkite/lm-eval-harness/test_lm_eval_correctness.py`, `.buildkite/test-amd.yaml`_
- **2026-08-25** [`d9fbe526c0`](https://github.com/vllm-project/vllm/commit/d9fbe526c0) [#53589](https://github.com/vllm-project/vllm/pull/53589)
  [ROCm][CI] Skip ModernBERT FP8 MTEB test when no FP8 ScaledMM kernel exists (#53589)
  _Files: `.buildkite/test-amd.yaml`, `tests/models/language/pooling_mteb_test/test_modernbert_fp8.py`_
- **2026-08-24** [`d154d90d6c`](https://github.com/vllm-project/vllm/commit/d154d90d6c) [#50465](https://github.com/vllm-project/vllm/pull/50465)
  [Model Runner V2] batch-sharded sample (#50465)
  _Files: `.buildkite/test_areas/model_runner_v2.yaml`, `tests/v1/e2e/general/test_sharded_sampling.py`, `tests/v1/e2e/spec_decode/test_sharded_sampling.py`, `tests/v1/worker/test_gpu_batch_shard.py` _+15 more__
- **2026-08-24** [`4c56e62c85`](https://github.com/vllm-project/vllm/commit/4c56e62c85) [#53581](https://github.com/vllm-project/vllm/pull/53581)
  [Bugfix][Kimi K3] Skip absent metadata during CUDA graph profiling (#53581)
  _Files: `tests/models/kimi_k3/test_kda.py`, `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/nvidia/kda.py`_

## Multimodal  (29 commits)

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
- **2026-08-30** [`f6895a5fcb`](https://github.com/vllm-project/vllm/commit/f6895a5fcb) [#54439](https://github.com/vllm-project/vllm/pull/54439)
  [Bugfix][Multimodal] Avoid caching full prompts in fallback (#54439)
  _Files: `vllm/multimodal/processing/processor.py`_
- **2026-08-30** [`87b9b5b8d9`](https://github.com/vllm-project/vllm/commit/87b9b5b8d9) [#53531](https://github.com/vllm-project/vllm/pull/53531)
  [Test][VLM] Add batch-invariance tests for Qwen3-VL (#53531)
  _Files: `.buildkite/test_areas/misc.yaml`, `docs/features/batch_invariance.md`, `tests/v1/determinism/test_batch_invariance_vlm.py`_
- **2026-08-30** [`4f78a8fdd0`](https://github.com/vllm-project/vllm/commit/4f78a8fdd0) [#54380](https://github.com/vllm-project/vllm/pull/54380)
  [Model] Honor cap_pixels_per_frame in Qwen3-VL memory profiling (#54380)
  _Files: `tests/models/multimodal/processing/test_qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-08-30** [`7a67941c1d`](https://github.com/vllm-project/vllm/commit/7a67941c1d) [#53760](https://github.com/vllm-project/vllm/pull/53760)
  [Rust Frontend][gRPC] Add audio and video media inputs (#53760)
  _Files: `rust/src/chat/src/multimodal/expand.rs`, `rust/src/server/src/grpc/convert.rs`, `tests/model_executor/test_qwen3_asr_mrope.py`, `vllm/model_executor/models/qwen3_asr.py`_
- **2026-08-30** [`b016ed8ea3`](https://github.com/vllm-project/vllm/commit/b016ed8ea3) [#54346](https://github.com/vllm-project/vllm/pull/54346)
  [Bugfix][Multimodal] Release Qwen2.5-VL and Qwen3-VL RoPE caches with the model (#54346)
  _Files: `vllm/model_executor/models/qwen2_5_vl.py`, `vllm/model_executor/models/qwen3_vl.py`_
- **2026-08-29** [`4fc943b867`](https://github.com/vllm-project/vllm/commit/4fc943b867) [#54231](https://github.com/vllm-project/vllm/pull/54231)
  [Multimodal] Deprecate PyAV video decoder backend (#54231)
  _Files: `docs/features/multimodal_inputs.md`, `tests/models/multimodal/processing/test_glm4_1v.py`, `tests/multimodal/media/test_video.py`, `tests/multimodal/test_video.py` _+5 more__
- **2026-08-29** [`4c6c9d569f`](https://github.com/vllm-project/vllm/commit/4c6c9d569f) [#53528](https://github.com/vllm-project/vllm/pull/53528)
  [Rust Frontend] Take the raw buffer in mm tensor lowering when possible (#53528)
  _Files: `rust/src/chat/Cargo.toml`, `rust/src/chat/src/multimodal/tensor.rs`_
- **2026-08-28** [`ffe690eca9`](https://github.com/vllm-project/vllm/commit/ffe690eca9) [#47625](https://github.com/vllm-project/vllm/pull/47625)
  [MM][CG] Support ViT full CUDA graph for Idefics3 and SmolVLM (#47625)
  _Files: `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/idefics2_vision_model.py`, `vllm/model_executor/models/idefics3.py`_
- **2026-08-28** [`d1922cb5a7`](https://github.com/vllm-project/vllm/commit/d1922cb5a7) [#52168](https://github.com/vllm-project/vllm/pull/52168)
  [Bugfix] Restore multimodal support on the plain "vllm" throughput backend (#52168)
  _Files: `tests/benchmarks/test_throughput_cli.py`, `vllm/benchmarks/throughput.py`_
- **2026-08-27** [`4a6a3272e8`](https://github.com/vllm-project/vllm/commit/4a6a3272e8) [#51157](https://github.com/vllm-project/vllm/pull/51157)
  [Bugfix][Frontend] Let pooling requests set padding (#51157)
  _Files: `examples/pooling/embed/vision_embedding_offline.py`, `examples/pooling/embed/vision_embedding_online.py`, `tests/entrypoints/pooling/embed/test_online.py`, `vllm/entrypoints/pooling/base/protocol.py`_
- **2026-08-27** [`acd0af90e8`](https://github.com/vllm-project/vllm/commit/acd0af90e8) [#53999](https://github.com/vllm-project/vllm/pull/53999)
  [Bugfix] Raise clear error on interleaved multimodal placeholder overcount (#53999)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-08-26** [`00ca27d0c1`](https://github.com/vllm-project/vllm/commit/00ca27d0c1) [#53841](https://github.com/vllm-project/vllm/pull/53841)
  [XPU][TEST]Move LoRA Multimodal to B70 in Intel GPU CI (#53841)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`_
- **2026-08-26** [`73bd7c83c4`](https://github.com/vllm-project/vllm/commit/73bd7c83c4) [#53854](https://github.com/vllm-project/vllm/pull/53854)
  [Bugfix][Processor] Replace bare asserts with ValueError in DeepseekVLV2/OCR processors (#53854)
  _Files: `tests/models/multimodal/processing/test_deepseek_ocr.py`, `vllm/transformers_utils/processors/deepseek_ocr.py`, `vllm/transformers_utils/processors/deepseek_vl2.py`_
- **2026-08-26** [`a5f82882a6`](https://github.com/vllm-project/vllm/commit/a5f82882a6) [#53830](https://github.com/vllm-project/vllm/pull/53830)
  [Bugfix][Model] Honor Molmo2 dummy video num_frames >= 2 override (#53830)
  _Files: `tests/models/multimodal/processing/test_molmo2.py`, `vllm/model_executor/models/molmo2.py`_
- **2026-08-25** [`299ebd094a`](https://github.com/vllm-project/vllm/commit/299ebd094a) [#53744](https://github.com/vllm-project/vllm/pull/53744)
  [Bugfix][Multimodal] Reject malformed base64 audio with 400 instead of 500 (#53744)
  _Files: `tests/multimodal/media/test_audio.py`, `vllm/multimodal/media/audio.py`_
- **2026-08-25** [`12c84b98dd`](https://github.com/vllm-project/vllm/commit/12c84b98dd) [#53656](https://github.com/vllm-project/vllm/pull/53656)
  [Config][EC] Normalize producer-only encoder config (#53656)
  _Files: `tests/config/test_multimodal_config.py`, `tests/v1/core/utils.py`, `vllm/config/vllm.py`_
- **2026-08-25** [`06ecec7a84`](https://github.com/vllm-project/vllm/commit/06ecec7a84) [#53553](https://github.com/vllm-project/vllm/pull/53553)
  [Bugfix][MM] Fix JinaVL processing cache order (#53553)
  _Files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_qwen2_vl.py`, `vllm/model_executor/models/jina_vl.py`_
- **2026-08-25** [`9bf0d4717e`](https://github.com/vllm-project/vllm/commit/9bf0d4717e) [#53456](https://github.com/vllm-project/vllm/pull/53456)
  [Bugfix] Keep grid dims for XD-RoPE models on a prefix-cache hit (#53456)
  _Files: `tests/v1/core/test_output.py`, `vllm/config/model.py`, `vllm/multimodal/utils.py`, `vllm/v1/core/sched/output.py` _+1 more__
- **2026-08-25** [`7ca336929c`](https://github.com/vllm-project/vllm/commit/7ca336929c) [#53608](https://github.com/vllm-project/vllm/pull/53608)
  [Model] Remove ten deprecated model architectures (#53608)
  _Files: `docs/contributing/model/multimodal.md`, `docs/models/pooling_models/embed.md`, `docs/models/supported_models.md`, `examples/generate/multimodal/audio_language_offline.py` _+42 more__
- **2026-08-24** [`0d7d5ed0b2`](https://github.com/vllm-project/vllm/commit/0d7d5ed0b2) [#53561](https://github.com/vllm-project/vllm/pull/53561)
  fix(security): enforce VLLM_MAX_AUDIO_CLIP_FILESIZE_MB on all audio paths (#53561)
  _Files: `docs/usage/security.md`, `tests/test_audio_media_size_precheck.py`, `vllm/envs.py`, `vllm/multimodal/media/audio.py`_
- **2026-08-24** [`342b8ebd8b`](https://github.com/vllm-project/vllm/commit/342b8ebd8b) [#53165](https://github.com/vllm-project/vllm/pull/53165)
  [Bugfix][Multimodal] Encode text in mixed CLIP/SigLIP pooling batches (#53165)
  _Files: `tests/models/multimodal/pooling/test_clip.py`, `tests/models/multimodal/pooling/test_dual_encoder_routing.py`, `tests/models/multimodal/pooling/test_siglip.py`, `vllm/model_executor/models/clip.py` _+1 more__
- **2026-08-24** [`ecfa7bb373`](https://github.com/vllm-project/vllm/commit/ecfa7bb373) [#53560](https://github.com/vllm-project/vllm/pull/53560)
  [MM] Cache common token sequences (#53560)
  _Files: `tests/multimodal/test_processing.py`, `vllm/model_executor/models/llava_onevision2.py`, `vllm/model_executor/models/minicpmv.py`, `vllm/model_executor/models/minicpmv4_6.py` _+10 more__
- **2026-08-24** [`9f295fe8ce`](https://github.com/vllm-project/vllm/commit/9f295fe8ce) [#53582](https://github.com/vllm-project/vllm/pull/53582)
  [Docs][Security] Document multimodal media UUID security implications (#53582)
  _Files: `docs/usage/security.md`_
- **2026-08-24** [`8c2bbe00d5`](https://github.com/vllm-project/vllm/commit/8c2bbe00d5) [#53513](https://github.com/vllm-project/vllm/pull/53513)
  [Bugfix][LoRA] Add multimodal module mapping for Muse-Glimmer (#53513)
  _Files: `vllm/model_executor/models/muse_glimmer.py`_
- **2026-08-24** [`2ec6f0d71e`](https://github.com/vllm-project/vllm/commit/2ec6f0d71e) [#51896](https://github.com/vllm-project/vllm/pull/51896)
  Reject oversized media before fully downloading it (#51896)
  _Files: `docs/usage/security.md`, `tests/entrypoints/openai/test_run_batch.py`, `tests/entrypoints/speech_to_text/transcription/test_chunk_timestamp_offset.py`, `tests/multimodal/media/test_unprocessable_entity_error.py` _+9 more__

## MoE / Expert Parallel  (29 commits)

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
- **2026-08-30** [`9d0fe9bac8`](https://github.com/vllm-project/vllm/commit/9d0fe9bac8) [#54427](https://github.com/vllm-project/vllm/pull/54427)
  [Bugfix][Quantization][MoE] Route weight only NVFP4 checkpoints through W4A16 (#54427)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-08-30** [`b5707bf994`](https://github.com/vllm-project/vllm/commit/b5707bf994) [#54048](https://github.com/vllm-project/vllm/pull/54048)
  [Bugfix][MoE] Enable cuBLAS out_dtype router GEMM on all CUDA archs (fixes family-120/GB10) (#54048)
  _Files: `vllm/model_executor/layers/fused_moe/router/gate_linear.py`_
- **2026-08-29** [`129087ddab`](https://github.com/vllm-project/vllm/commit/129087ddab) [#45457](https://github.com/vllm-project/vllm/pull/45457)
  [Perf] Reuse topk SparseMatrix routing metadata in GPT-OSS MoE forward (#45457)
  _Files: `tests/kernels/moe/test_gpt_oss_triton_kernels.py`, `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-08-29** [`b2f685834a`](https://github.com/vllm-project/vllm/commit/b2f685834a) [#54160](https://github.com/vllm-project/vllm/pull/54160)
  [Hy4] support Hy4-preview model (#54160)
  _Files: `docs/models/supported_models.md`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/parser/reasoning/mod.rs`, `rust/src/chat/src/parser/tool/mod.rs` _+43 more__
- **2026-08-29** [`6c18a54648`](https://github.com/vllm-project/vllm/commit/6c18a54648) [#54299](https://github.com/vllm-project/vllm/pull/54299)
  [Perf] Avoid h2d copies from non-pinned CPU tensors (#54299)
  _Files: `vllm/model_executor/layers/pooler/tokwise/methods.py`, `vllm/model_executor/model_loader/utils.py`, `vllm/model_executor/models/ernie45_vl.py`, `vllm/model_executor/models/glm4_1v.py` _+10 more__
- **2026-08-29** [`738bc8811a`](https://github.com/vllm-project/vllm/commit/738bc8811a) [#50858](https://github.com/vllm-project/vllm/pull/50858)
  [BugFix] Disable TP for Qwen3-Omni audio encoder when heads % TP != 0 (#50858)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-08-28** [`c274d36103`](https://github.com/vllm-project/vllm/commit/c274d36103) [#54152](https://github.com/vllm-project/vllm/pull/54152)
  [Bugfix] Keep the Moondream3 MoE all-reduce out of the fused-path try (#54152)
  _Files: `tests/models/multimodal/generation/test_moondream3_moe.py`, `vllm/model_executor/models/moondream3.py`_
- **2026-08-28** [`21fa2c5a2a`](https://github.com/vllm-project/vllm/commit/21fa2c5a2a) [#54079](https://github.com/vllm-project/vllm/pull/54079)
  [Mypy] Fix mypy typing for model interfaces and H/I models (#54079)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/chatglm.py`, `vllm/model_executor/models/commandr.py`, `vllm/model_executor/models/gemma.py` _+19 more__
- **2026-08-28** [`d9dabfa351`](https://github.com/vllm-project/vllm/commit/d9dabfa351) [#54168](https://github.com/vllm-project/vllm/pull/54168)
  [Kimi-K3][Kernel] Optimize the low-M fused latent MoE tail (#54168)
  _Files: `tests/models/kimi_k3/test_latent_moe_tail.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/allreduce_rmsnorm_reduce_scatter_early_exit.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/fused_add_multicast_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy.py` _+2 more__
- **2026-08-27** [`7d5769b2d9`](https://github.com/vllm-project/vllm/commit/7d5769b2d9) [#53685](https://github.com/vllm-project/vllm/pull/53685)
  [Perf][DSv4] Use native CUDA SwiGLU clamp kernel for Humming MoE (throughput +1.40%) (#53685)
  _Files: `tests/kernels/core/test_activation.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-08-27** [`674c284dbd`](https://github.com/vllm-project/vllm/commit/674c284dbd) [#54056](https://github.com/vllm-project/vllm/pull/54056)
  Fix Humming MoE activation_output aliasing (#54056)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`_
- **2026-08-26** [`6a5e8f5979`](https://github.com/vllm-project/vllm/commit/6a5e8f5979) [#51398](https://github.com/vllm-project/vllm/pull/51398)
  [DeepEPv2] Support MXFp8 Activation Scale Dispatch (#51398)
  _Files: `vllm/model_executor/layers/fused_moe/prepare_finalize/deepep_v2.py`_
- **2026-08-26** [`2cd6c664c1`](https://github.com/vllm-project/vllm/commit/2cd6c664c1) [#53311](https://github.com/vllm-project/vllm/pull/53311)
  [MoE] enable all2all fi_one_sided by default (#53311)
  _Files: `vllm/config/parallel.py`, `vllm/distributed/device_communicators/all2all.py`_
- **2026-08-26** [`044b05220e`](https://github.com/vllm-project/vllm/commit/044b05220e) [#53819](https://github.com/vllm-project/vllm/pull/53819)
  [Kernel][Perf] Tune fused_moe FP8 config for Qwen3.5 on L40S (+7%) (#53819)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_L40S,dtype=fp8_w8a8.json`_
- **2026-08-26** [`a5e0045433`](https://github.com/vllm-project/vllm/commit/a5e0045433) [#52821](https://github.com/vllm-project/vllm/pull/52821)
  [Refactor] Remove dead code quantization 2 (#52821)
  _Files: `csrc/libtorch_stable/quantization/gptq/matrix_view.cuh`, `csrc/libtorch_stable/quantization/gptq/q_gemm.cu`, `csrc/libtorch_stable/quantization/gptq/qdq_4.cuh`, `csrc/libtorch_stable/quantization/gptq/qdq_util.cuh` _+10 more__
- **2026-08-26** [`f6130145c8`](https://github.com/vllm-project/vllm/commit/f6130145c8) [#53557](https://github.com/vllm-project/vllm/pull/53557)
  [Bugfix][LoRA] Enable tower/connector LoRA for Qwen3-Omni (#53557)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-08-25** [`70021a0081`](https://github.com/vllm-project/vllm/commit/70021a0081) [#53616](https://github.com/vllm-project/vllm/pull/53616)
  [Mypy Fix] Mypy fix for "vllm/model_executor/models/[gG]" (#53616)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/deepseek_v2.py`, `vllm/model_executor/models/gemma.py`, `vllm/model_executor/models/gemma3_mm.py` _+22 more__
- **2026-08-25** [`ca29cd48ba`](https://github.com/vllm-project/vllm/commit/ca29cd48ba) [#51332](https://github.com/vllm-project/vllm/pull/51332)
  [Quantization][Humming] Support MXFP4 weight + block-FP8 activation for MoE (#51332)
  _Files: `csrc/libtorch_stable/activation_kernels.cu`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp`, `tests/evals/gsm8k/configs/humming/Qwen3-30B-A3B-MXFP4A16-humming-act-fp8-block.yaml` _+13 more__
- **2026-08-25** [`48d7132962`](https://github.com/vllm-project/vllm/commit/48d7132962) [#53615](https://github.com/vllm-project/vllm/pull/53615)
  [Model] Migrate FlexOlmo, Olmo3 and Hunyuan V1/VL to the Transformers modeling backend (#53615)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/flex_olmo.py`, `vllm/model_executor/models/hunyuan_v1.py` _+10 more__
- **2026-08-25** [`8fe9317f2e`](https://github.com/vllm-project/vllm/commit/8fe9317f2e) [#49636](https://github.com/vllm-project/vllm/pull/49636)
  [Model][MoE] DeepSeek-V4: add opt-in FlashInfer moe_ep expert backend (#49636)
  _Files: `tests/models/test_deepseek_v4_fi_moe_ep.py`, `vllm/config/kernel.py`, `vllm/models/deepseek_v4/nvidia/fi_moe.py`, `vllm/models/deepseek_v4/nvidia/model.py` _+1 more__
- **2026-08-25** [`b2dd9ce73d`](https://github.com/vllm-project/vllm/commit/b2dd9ce73d) [#53604](https://github.com/vllm-project/vllm/pull/53604)
  [Docs] Fix docstring continuation indentation in `routed_experts.py` (#53604)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-08-25** [`09fddeb4ce`](https://github.com/vllm-project/vllm/commit/09fddeb4ce) [#53593](https://github.com/vllm-project/vllm/pull/53593)
  [Bugfix] BailingMoeV3 KDA: skip absent metadata during CUDA graph profiling (#53593)
  _Files: `vllm/model_executor/models/bailing_moe_v3.py`_
- **2026-08-24** [`29c9af5211`](https://github.com/vllm-project/vllm/commit/29c9af5211) [#53310](https://github.com/vllm-project/vllm/pull/53310)
  [Kimi K3 Refactor] Add `UnfinalizedMoEOutput` proto following up for #53152 (#53310)
  _Files: `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`, `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`, `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a4_nvfp4.py`, `vllm/model_executor/layers/quantization/modelopt.py` _+2 more__
- **2026-08-24** [`460c08bc8a`](https://github.com/vllm-project/vllm/commit/460c08bc8a) [#52786](https://github.com/vllm-project/vllm/pull/52786)
  [LoRA] Add Qwen3-Omni multimodal LoRA support (#52786)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-08-24** [`702e1d7186`](https://github.com/vllm-project/vllm/commit/702e1d7186) [#53361](https://github.com/vllm-project/vllm/pull/53361)
  [LoRA] feat: Support LoRA for DeepSeek V4 (#53361)
  _Files: `vllm/lora/layers/base.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/models/deepseek_v4/nvidia/model.py`_

## Serving / API  (20 commits)

- **2026-08-31** [`810bc3250c`](https://github.com/vllm-project/vllm/commit/810bc3250c) [#54537](https://github.com/vllm-project/vllm/pull/54537)
  [Frontend][Performance] Resolve async media across modalities concurrently (#54537)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-08-31** [`4ae172231c`](https://github.com/vllm-project/vllm/commit/4ae172231c) [#54315](https://github.com/vllm-project/vllm/pull/54315)
  [Frontend] Forward cache salt for content parts (#54315)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-31** [`687db59744`](https://github.com/vllm-project/vllm/commit/687db59744) [#54364](https://github.com/vllm-project/vllm/pull/54364)
  [Bugfix][Frontend] Truncate pooling prompts before padding them (#54364)
  _Files: `tests/entrypoints/pooling/scoring/test_io_processor_unit.py`, `tests/renderers/test_completions.py`, `vllm/entrypoints/pooling/scoring/io_processor.py`, `vllm/renderers/params.py`_
- **2026-08-30** [`fe6db3ed5e`](https://github.com/vllm-project/vllm/commit/fe6db3ed5e) [#54324](https://github.com/vllm-project/vllm/pull/54324)
  [Bugfix] Validate scale-out transfer params (#54324)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-29** [`7fbfca2670`](https://github.com/vllm-project/vllm/commit/7fbfca2670) [#52529](https://github.com/vllm-project/vllm/pull/52529)
  [Bugfix][Frontend] Only echo the assistant turn in batched chat completions (#52529)
  _Files: `tests/entrypoints/openai/chat_completion/test_batched_chat_completions.py`, `vllm/entrypoints/openai/chat_completion/batch_serving.py`_
- **2026-08-29** [`085e9bb07e`](https://github.com/vllm-project/vllm/commit/085e9bb07e) [#48584](https://github.com/vllm-project/vllm/pull/48584)
  [Rust Frontend] Add support for `truncate_prompt_tokens` and `truncation_side` (#48584)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/chat/src/request.rs`, `rust/src/server/src/error.rs`, `rust/src/server/src/grpc/convert.rs` _+13 more__
- **2026-08-28** [`74850f9f66`](https://github.com/vllm-project/vllm/commit/74850f9f66) [#51321](https://github.com/vllm-project/vllm/pull/51321)
  [Rust Frontend] Optimize SSE streaming hot path (#51321)
  _Files: `rust/Cargo.toml`, `rust/src/server/src/routes/inference/generate.rs`, `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs` _+4 more__
- **2026-08-27** [`9db222c6be`](https://github.com/vllm-project/vllm/commit/9db222c6be) [#53218](https://github.com/vllm-project/vllm/pull/53218)
  [Rust Frontend] Align OpenAI request and response edge cases (#53218)
  _Files: `rust/src/server/src/routes/openai/chat_completions.rs`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/chat_completions/types.rs`, `rust/src/server/src/routes/openai/chat_completions/validate.rs` _+12 more__
- **2026-08-27** [`d7b6a35967`](https://github.com/vllm-project/vllm/commit/d7b6a35967) [#53763](https://github.com/vllm-project/vllm/pull/53763)
  [Bugfix] Handle malformed namespace tools (#53763)
  _Files: `vllm/entrypoints/openai/responses/protocol.py`_
- **2026-08-27** [`50708f95ae`](https://github.com/vllm-project/vllm/commit/50708f95ae) [#47815](https://github.com/vllm-project/vllm/pull/47815)
  [Bugfix][OpenAI] Fix streamed completion logprob offsets with echo (#47815)
  _Files: `vllm/entrypoints/openai/completion/serving.py`_
- **2026-08-26** [`161ffd37d2`](https://github.com/vllm-project/vllm/commit/161ffd37d2) [#48922](https://github.com/vllm-project/vllm/pull/48922)
  [Bugfix] Guard tool call argument JSON parsing in chat message postprocessing (#48922)
  _Files: `tests/entrypoints/unit_tests/test_chat_utils.py`, `vllm/entrypoints/chat_utils.py`_
- **2026-08-26** [`15baeaee98`](https://github.com/vllm-project/vllm/commit/15baeaee98) [#53220](https://github.com/vllm-project/vllm/pull/53220)
  [Doc] Fix local input path in run-batch examples across docs (#53220)
  _Files: `docs/cli/README.md`, `examples/features/openai_batch/README.md`_
- **2026-08-26** [`f25c2692fe`](https://github.com/vllm-project/vllm/commit/f25c2692fe) [#45803](https://github.com/vllm-project/vllm/pull/45803)
  [Frontend] Add `/v1/messages/render` endpoint for the Anthropic Messages API (#45803)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `tests/entrypoints/scale_out/render/test_render.py`, `vllm/entrypoints/anthropic/serving.py`, `vllm/entrypoints/scale_out/render/api_router.py` _+1 more__
- **2026-08-26** [`d125b540b7`](https://github.com/vllm-project/vllm/commit/d125b540b7) [#53702](https://github.com/vllm-project/vllm/pull/53702)
  [Agents] Add CUDA IMA debugging skill (#53702)
  _Files: `.agents/skills/debug-ima/SKILL.md`, `.agents/skills/debug-ima/agents/openai.yaml`, `.claude/skills/debug-ima`_
- **2026-08-25** [`3e833933dc`](https://github.com/vllm-project/vllm/commit/3e833933dc) [#53738](https://github.com/vllm-project/vllm/pull/53738)
  [Bugfix][Frontend] Keep credentials out of the Rust frontend launch log (#53738)
  _Files: `tests/entrypoints/launchers/api_server/test_api_server_process_manager.py`, `tests/entrypoints/serve/utils/test_api_utils.py`, `vllm/entrypoints/serve/utils/api_utils.py`, `vllm/v1/utils.py`_
- **2026-08-25** [`5e379a361e`](https://github.com/vllm-project/vllm/commit/5e379a361e) [#53688](https://github.com/vllm-project/vllm/pull/53688)
  [Agents] Add kernel microbenchmark skill (#53688)
  _Files: `.agents/skills/kernel-microbenchmark/SKILL.md`, `.agents/skills/kernel-microbenchmark/agents/openai.yaml`, `.agents/skills/kernel-microbenchmark/benchmarks/cupti_microbenchmark.py`, `.agents/skills/kernel-microbenchmark/benchmarks/multi_gpu_gemm_rs.py` _+1 more__
- **2026-08-25** [`d3e2888c75`](https://github.com/vllm-project/vllm/commit/d3e2888c75) [#53625](https://github.com/vllm-project/vllm/pull/53625)
  [Bugfix][Frontend] Redact hf_token in the non-default args log (#53625)
  _Files: `tests/entrypoints/serve/utils/test_api_utils.py`, `vllm/entrypoints/serve/utils/api_utils.py`_
- **2026-08-24** [`9cef631f30`](https://github.com/vllm-project/vllm/commit/9cef631f30) [#53500](https://github.com/vllm-project/vllm/pull/53500)
  [Frontend] Move run_batch.py out openai folder (#53500)
  _Files: `docs/mkdocs/gen_files/generate_argparse.py`, `examples/features/openai_batch/README.md`, `tests/entrypoints/launchers/test_run_batch.py`, `tests/entrypoints/serve/instrumentator/test_metrics.py` _+3 more__
- **2026-08-24** [`e239947777`](https://github.com/vllm-project/vllm/commit/e239947777) [#50588](https://github.com/vllm-project/vllm/pull/50588)
  [Bugfix][Frontend] Fix run_batch upload retrying on success and unawaited error body (#50588)
  _Files: `tests/entrypoints/openai/test_run_batch.py`, `vllm/entrypoints/openai/run_batch.py`_
- **2026-08-24** [`585bb07c70`](https://github.com/vllm-project/vllm/commit/585bb07c70) [#51034](https://github.com/vllm-project/vllm/pull/51034)
  feat: add SSE keep-alive comments for idle streaming responses (#51034)
  _Files: `tests/entrypoints/openai/test_cli_args.py`, `tests/entrypoints/openai/test_sse_keep_alive.py`, `vllm/entrypoints/openai/chat_completion/api_router.py`, `vllm/entrypoints/openai/cli_args.py` _+2 more__

## CI / Build  (18 commits)

- **2026-08-31** [`e2c8eeac40`](https://github.com/vllm-project/vllm/commit/e2c8eeac40) [#53677](https://github.com/vllm-project/vllm/pull/53677)
  [kernel] Fused embedding kernel  (#53677)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_vocab_parallel_embedding.py`, `csrc/libtorch_stable/ops.h`, `csrc/libtorch_stable/torch_bindings.cpp` _+4 more__
- **2026-08-30** [`7a100bb617`](https://github.com/vllm-project/vllm/commit/7a100bb617) [#54468](https://github.com/vllm-project/vllm/pull/54468)
  [CI] Restore gpu_1_queue routing for torch-abi audit (#54468)
  _Files: `.buildkite/test_areas/torch_abi.yaml`_
- **2026-08-30** [`8fa4c6cdb3`](https://github.com/vllm-project/vllm/commit/8fa4c6cdb3) [#54330](https://github.com/vllm-project/vllm/pull/54330)
  [CI] Add explicit step keys to 18 hardware test steps (#54330)
  _Files: `.buildkite/hardware_tests/ascend_npu.yaml`, `.buildkite/hardware_tests/cpu.yaml`, `.buildkite/hardware_tests/gh200.yaml`, `.buildkite/hardware_tests/intel.yaml` _+1 more__
- **2026-08-29** [`680e2177e4`](https://github.com/vllm-project/vllm/commit/680e2177e4) [#53621](https://github.com/vllm-project/vllm/pull/53621)
  [CI][Ray] Fix flaky multi-node assignment test after placement-group teardown (#53621)
  _Files: `tests/distributed/test_multi_node_assignment.py`, `vllm/v1/executor/ray_utils.py`_
- **2026-08-29** [`6cddad414e`](https://github.com/vllm-project/vllm/commit/6cddad414e) [#54312](https://github.com/vllm-project/vllm/pull/54312)
  [CI][Test] Deflake test_mem.py sleep-mode asserts via allocator bookeeping (#54312)
  _Files: `tests/basic_correctness/test_mem.py`_
- **2026-08-29** [`1a16c2ad2c`](https://github.com/vllm-project/vllm/commit/1a16c2ad2c) [#54271](https://github.com/vllm-project/vllm/pull/54271)
  [CI][Test] Deflake the rms_norm scaling-property assertions (#54271)
  _Files: `tests/kernels/ir/test_layernorm.py`_
- **2026-08-28** [`94a54f581e`](https://github.com/vllm-project/vllm/commit/94a54f581e) [#54203](https://github.com/vllm-project/vllm/pull/54203)
  [XPU]bump up vllm_xpu_kernels to 0.1.14.1 (#54203)
  _Files: `requirements/xpu.txt`_
- **2026-08-28** [`3bb19cd8a3`](https://github.com/vllm-project/vllm/commit/3bb19cd8a3) [#52545](https://github.com/vllm-project/vllm/pull/52545)
  [Bugfix][CI/Build] Fail closed when selected precompiled CUDA variant is unavailable (#52545)
  _Files: `docs/contributing/ci/nightly_builds.md`, `setup.py`_
- **2026-08-27** [`d262964e8c`](https://github.com/vllm-project/vllm/commit/d262964e8c) [#54020](https://github.com/vllm-project/vllm/pull/54020)
  Upgrade tpu-inference to v0.28.0 (#54020)
  _Files: `requirements/tpu.txt`_
- **2026-08-27** [`9650dc73e2`](https://github.com/vllm-project/vllm/commit/9650dc73e2) [#53443](https://github.com/vllm-project/vllm/pull/53443)
  [CI/Build][Hardware][NVIDIA] Add opt-in Rubin Docker builds (#53443)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `docs/assets/contributing/dockerfile-stages-dependency.png`, `docs/contributing/dockerfile/dockerfile.md` _+3 more__
- **2026-08-27** [`f25c580af1`](https://github.com/vllm-project/vllm/commit/f25c580af1) [#53817](https://github.com/vllm-project/vllm/pull/53817)
  [XPU][Dockerfile] Update UCX install (#53817)
  _Files: `docker/Dockerfile.xpu`_
- **2026-08-26** [`a27e88c862`](https://github.com/vllm-project/vllm/commit/a27e88c862) [#53862](https://github.com/vllm-project/vllm/pull/53862)
  [XPU][CI] increase timeout of extract_hidden_states tp2 (#53862)
  _Files: `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`_
- **2026-08-26** [`7a9993878c`](https://github.com/vllm-project/vllm/commit/7a9993878c) [#53732](https://github.com/vllm-project/vllm/pull/53732)
  [CI] forward fix CRCR report step in the torch-nightly lane (#53732)
  _Files: `.buildkite/scripts/crcr-report.sh`, `.buildkite/test_areas/crcr_report.yaml`_
- **2026-08-26** [`b821d7b2a6`](https://github.com/vllm-project/vllm/commit/b821d7b2a6) [#49600](https://github.com/vllm-project/vllm/pull/49600)
  [CI] Build mamba-ssm with C++20 for torch 2.14 nightly compatibility (#49600)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-08-25** [`c9331d8064`](https://github.com/vllm-project/vllm/commit/c9331d8064) [#53290](https://github.com/vllm-project/vllm/pull/53290)
  [CI] Preserve Rust Docker cache across commits (#53290)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.cpu`, `docker/Dockerfile.xpu`, `docs/assets/contributing/dockerfile-stages-dependency.png` _+1 more__
- **2026-08-25** [`34c3824a11`](https://github.com/vllm-project/vllm/commit/34c3824a11) [#53618](https://github.com/vllm-project/vllm/pull/53618)
  [CI] Increase Entrypoints Unit timeout after launcher suite growth (#53618)
  _Files: `.buildkite/test_areas/entrypoints.yaml`_
- **2026-08-25** [`e3dde1ee9b`](https://github.com/vllm-project/vllm/commit/e3dde1ee9b) [#51830](https://github.com/vllm-project/vllm/pull/51830)
  [CI] Report torch-nightly results to PyTorch CRCR (#51830)
  _Files: `.buildkite/scripts/crcr-report.sh`, `.buildkite/scripts/crcr_report.py`, `.buildkite/test_areas/crcr_report.yaml`_
- **2026-08-24** [`a047e2543d`](https://github.com/vllm-project/vllm/commit/a047e2543d) [#53000](https://github.com/vllm-project/vllm/pull/53000)
  Fix MNNVL Lamport mailbox publication and cleanup (#53000)
  _Files: `.buildkite/test_areas/distributed.yaml`, `csrc/custom_all_gather_reduce_scatter.cuh`, `tests/distributed/test_custom_all_gather_reduce_scatter.py`_

## Models  (17 commits)

- **2026-08-31** [`9debcd5990`](https://github.com/vllm-project/vllm/commit/9debcd5990) [#53529](https://github.com/vllm-project/vllm/pull/53529)
  [Test][Qwen3-VL] Cover compiled DeepStack input contract (#53529)
  _Files: `tests/compile/test_deepstack_input_contract.py`_
- **2026-08-31** [`44fe2a392b`](https://github.com/vllm-project/vllm/commit/44fe2a392b) [#53921](https://github.com/vllm-project/vllm/pull/53921)
  [CPU] add CPU support for Voxtral (#53921)
  _Files: `vllm/model_executor/models/whisper_causal.py`_
- **2026-08-29** [`fd5d3aea94`](https://github.com/vllm-project/vllm/commit/fd5d3aea94) [#54130](https://github.com/vllm-project/vllm/pull/54130)
  [Mypy] Fix typing for J models (#54130)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/jamba.py`, `vllm/model_executor/models/jina.py`_
- **2026-08-27** [`42e7942ac9`](https://github.com/vllm-project/vllm/commit/42e7942ac9) [#50536](https://github.com/vllm-project/vllm/pull/50536)
  fix(config): guard LlamaBidirectionalConfig against missing hf_config.pooling (#50536)
  _Files: `vllm/model_executor/models/config.py`_
- **2026-08-26** [`2ab187430b`](https://github.com/vllm-project/vllm/commit/2ab187430b) [#53884](https://github.com/vllm-project/vllm/pull/53884)
  [Bugfix] Make Gemma4 MTP suppress_tokens masking CUDA-graph-safe (#53884)
  _Files: `vllm/model_executor/models/gemma4_mtp.py`_
- **2026-08-26** [`c47ca4aaeb`](https://github.com/vllm-project/vllm/commit/c47ca4aaeb) [#53466](https://github.com/vllm-project/vllm/pull/53466)
  [Mypy Fix] Mypy fix for "vllm/model_executor/models/[tT]" (#53466)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/models/telechat2.py`, `vllm/model_executor/models/terratorch.py`_
- **2026-08-26** [`61d4f56635`](https://github.com/vllm-project/vllm/commit/61d4f56635) [#53120](https://github.com/vllm-project/vllm/pull/53120)
  [Offloader] Offload submodules that make_layers never reaches (#53120)
  _Files: `tests/basic_correctness/test_cpu_offload.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/offloader/base.py`, `vllm/model_executor/offloader/prefetch.py` _+1 more__
- **2026-08-25** [`217a0b5cef`](https://github.com/vllm-project/vllm/commit/217a0b5cef) [#53750](https://github.com/vllm-project/vllm/pull/53750)
  [Bugfix][Frontend] Apply the stop string limit to Cohere requests (#53750)
  _Files: `tests/entrypoints/cohere/test_protocol.py`, `vllm/entrypoints/cohere/protocol.py`_
- **2026-08-25** [`19406fae28`](https://github.com/vllm-project/vllm/commit/19406fae28) [#53747](https://github.com/vllm-project/vllm/pull/53747)
  [Bugfix][Tokenizer] Replace bare asserts in the DeepSeek V4 encoder (#53747)
  _Files: `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`_
- **2026-08-25** [`9c8e90eb26`](https://github.com/vllm-project/vllm/commit/9c8e90eb26) [#53657](https://github.com/vllm-project/vllm/pull/53657)
  [Bugfix] Handle parenthesized Gemma4 tool calls (#53657)
  _Files: `vllm/parser/gemma4.py`_
- **2026-08-25** [`59d7fc92ea`](https://github.com/vllm-project/vllm/commit/59d7fc92ea) [#51262](https://github.com/vllm-project/vllm/pull/51262)
  [Bugfix][DeepSeek V4] Handle trailing system messages in prompt rendering (#51262)
  _Files: `rust/src/chat/src/renderer/deepseek_v4/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4_encoding.py`_
- **2026-08-25** [`4f3e255dca`](https://github.com/vllm-project/vllm/commit/4f3e255dca) [#51302](https://github.com/vllm-project/vllm/pull/51302)
  [Bugfix][Model] deepseek-vl2: restore original DeepseekV2Config defaults for omitted language_config fields (#51302)
  _Files: `vllm/transformers_utils/configs/deepseek_vl2.py`_
- **2026-08-25** [`07ef21bc69`](https://github.com/vllm-project/vllm/commit/07ef21bc69) [#52676](https://github.com/vllm-project/vllm/pull/52676)
  [Kernel][Perf] Enable fused QK-norm + partial MRoPE + gate for Qwen3.6 (#52676)
  _Files: `tests/kernels/test_fused_qk_norm_rope_gate.py`, `vllm/model_executor/layers/fused_qk_norm_rope.py`, `vllm/model_executor/models/qwen3_next.py`_
- **2026-08-24** [`79bb395eea`](https://github.com/vllm-project/vllm/commit/79bb395eea) [#53464](https://github.com/vllm-project/vllm/pull/53464)
  [Pooling] Improve BGE-M3 sync pooling throughput by up to 3.13% (#53464)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`, `tests/models/language/pooling/test_splade_sparse_pooler.py`, `tests/v1/worker/test_gpu_input_batch.py`, `vllm/model_executor/layers/pooler/common.py` _+6 more__
- **2026-08-24** [`41ae917c12`](https://github.com/vllm-project/vllm/commit/41ae917c12) [#53219](https://github.com/vllm-project/vllm/pull/53219)
  Add Cohere ChatV2 render endpoint (#53219)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/cohere/test_chat_v2.py`, `vllm/entrypoints/cohere/api_router.py`, `vllm/entrypoints/cohere/serving.py` _+1 more__
- **2026-08-24** [`a7195188a4`](https://github.com/vllm-project/vllm/commit/a7195188a4) [#53121](https://github.com/vllm-project/vllm/pull/53121)
  Add MTP support for Nemotron VL models (#53121)
  _Files: `vllm/model_executor/models/nemotron_h_mtp.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-08-24** [`cd329413e2`](https://github.com/vllm-project/vllm/commit/cd329413e2) [#52467](https://github.com/vllm-project/vllm/pull/52467)
  [Misc] Use VLLMValidationError in Cohere request validation (#52467)
  _Files: `tests/entrypoints/cohere/test_api_router.py`, `tests/entrypoints/cohere/test_protocol.py`, `vllm/entrypoints/cohere/protocol.py`_

## Scheduler / Engine  (16 commits)

- **2026-08-31** [`dafbef15a1`](https://github.com/vllm-project/vllm/commit/dafbef15a1) [#49445](https://github.com/vllm-project/vllm/pull/49445)
  [Core] Add `max_num_queued_reqs` and `max_num_queued_tokens` for queue size management (#49445)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat.py`, `tests/entrypoints/speech_to_text/test_speech_to_text_cancellation.py`, `tests/v1/engine/test_admission_control.py`, `vllm/config/scheduler.py` _+14 more__
- **2026-08-31** [`eeb549a74d`](https://github.com/vllm-project/vllm/commit/eeb549a74d) [#54492](https://github.com/vllm-project/vllm/pull/54492)
  [Frontend] Move engine/protocol.py out openai folder (#54492)
- **2026-08-31** [`d8de4ae322`](https://github.com/vllm-project/vllm/commit/d8de4ae322) [#52912](https://github.com/vllm-project/vllm/pull/52912)
  [Bugfix][KVOffload] P2P tier declares REQUEST_LEVEL on the producer leg (#52912)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/test_tiering_offloading.py` _+1 more__
- **2026-08-30** [`1dc464d426`](https://github.com/vllm-project/vllm/commit/1dc464d426) [#54353](https://github.com/vllm-project/vllm/pull/54353)
  [Bugfix] Bound cache_salt length to prevent DoS via scheduler CPU exhaustion (#54353)
  _Files: `vllm/entrypoints/anthropic/protocol.py`, `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py` _+2 more__
- **2026-08-28** [`11012d2a35`](https://github.com/vllm-project/vllm/commit/11012d2a35) [#54148](https://github.com/vllm-project/vllm/pull/54148)
  [Rust Frontend] Reduce copy in auxiliary frame resolution (#54148)
  _Files: `rust/src/engine-core-client/src/protocol/logprobs.rs`, `rust/src/engine-core-client/src/protocol/logprobs/array.rs`, `rust/src/engine-core-client/src/protocol/output.rs`, `rust/src/engine-core-client/src/protocol/tensor.rs`_
- **2026-08-27** [`d04d3e0a07`](https://github.com/vllm-project/vllm/commit/d04d3e0a07) [#54023](https://github.com/vllm-project/vllm/pull/54023)
  [Bugfix] Revert renderer warmup overlap to avoid fork deadlock (#54023)
  _Files: `tests/renderers/test_warmup.py`, `vllm/renderers/base.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/llm_engine.py`_
- **2026-08-27** [`3a9bfc209f`](https://github.com/vllm-project/vllm/commit/3a9bfc209f) [#54089](https://github.com/vllm-project/vllm/pull/54089)
  [Bugfix][Parser] Scope reasoning-end detection to the current turn via turn-boundary tokens (#54089)
  _Files: `tests/parser/engine/test_qwen3_reasoning.py`, `vllm/parser/engine/parser_engine.py`, `vllm/parser/engine/parser_engine_config.py`, `vllm/parser/nemotron_v3.py` _+1 more__
- **2026-08-27** [`79378fe6e8`](https://github.com/vllm-project/vllm/commit/79378fe6e8) [#53666](https://github.com/vllm-project/vllm/pull/53666)
  [Bugfix] Avoid TCPStore port collision for co-located non-DP Ray engines (#53666)
  _Files: `tests/distributed/test_ray_v2_executor.py`, `vllm/v1/executor/ray_executor_v2.py`_
- **2026-08-27** [`76c0c6530e`](https://github.com/vllm-project/vllm/commit/76c0c6530e) [#53962](https://github.com/vllm-project/vllm/pull/53962)
  [Bugfix][Scheduler] Don't pad spec decode up to `max_model_len` (#53962)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/utils.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-27** [`ca90b9e7d4`](https://github.com/vllm-project/vllm/commit/ca90b9e7d4) [#52764](https://github.com/vllm-project/vllm/pull/52764)
  [warmup] overlap renderer warmup and engine core initialization (#52764)
  _Files: `tests/renderers/test_warmup.py`, `vllm/renderers/base.py`, `vllm/v1/engine/async_llm.py`, `vllm/v1/engine/llm_engine.py`_
- **2026-08-26** [`3fd72ffd7b`](https://github.com/vllm-project/vllm/commit/3fd72ffd7b) [#53939](https://github.com/vllm-project/vllm/pull/53939)
  [Bugfix][Rust Frontend] Fix LogprobsTensors wire schema mismatch (#53939)
  _Files: `rust/src/engine-core-client/src/protocol/logprobs.rs`, `rust/src/engine-core-client/src/protocol/logprobs/tests.rs`, `rust/src/engine-core-client/src/protocol/logprobs/wire.rs`, `rust/src/engine-core-client/src/tests/python_compat.py`_
- **2026-08-26** [`17da48596c`](https://github.com/vllm-project/vllm/commit/17da48596c) [#52914](https://github.com/vllm-project/vllm/pull/52914)
  [Bugfix][DP] Synchronize the device on pause completion (#52914)
  _Files: `tests/v1/distributed/test_async_llm_dp.py`, `tests/v1/engine/test_engine_core.py`, `vllm/v1/engine/core.py`, `vllm/v1/worker/gpu_worker.py` _+1 more__
- **2026-08-26** [`c71f6f8a81`](https://github.com/vllm-project/vllm/commit/c71f6f8a81) [#42644](https://github.com/vllm-project/vllm/pull/42644)
  [Bugfix] Thread kv_transfer_params into engine for /inference/v1/generate (disagg) (#42644)
  _Files: `vllm/entrypoints/scale_out/token_in_token_out/serving.py`_
- **2026-08-26** [`903a02192f`](https://github.com/vllm-project/vllm/commit/903a02192f) [#53704](https://github.com/vllm-project/vllm/pull/53704)
  [Bugfix] Handle empty FlatLogprobs slices and delta output (#53704)
  _Files: `tests/test_logprobs.py`, `tests/v1/engine/test_output_processor.py`, `vllm/logprobs.py`, `vllm/v1/engine/output_processor.py`_
- **2026-08-25** [`23310bc3de`](https://github.com/vllm-project/vllm/commit/23310bc3de) [#50431](https://github.com/vllm-project/vllm/pull/50431)
  [sleep functionality] code refactor about sleep/wake_up (#50431)
  _Files: `vllm/entrypoints/serve/dev/sleep/api_router.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/engine/core.py`_
- **2026-08-25** [`735daf8ef6`](https://github.com/vllm-project/vllm/commit/735daf8ef6) [#53659](https://github.com/vllm-project/vllm/pull/53659)
  [Frontend] Move cli_args.py and dp_supervisor.py out openai folder (#53659)
  _Files: `docs/mkdocs/gen_files/generate_argparse.py`, `tests/engine/test_arg_utils.py`, `tests/entrypoints/cohere/test_registry_and_args.py`, `tests/entrypoints/launchers/test_cli_args.py` _+10 more__

## KV Cache / Offload  (12 commits)

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
- **2026-08-29** [`fb68025138`](https://github.com/vllm-project/vllm/commit/fb68025138) [#54162](https://github.com/vllm-project/vllm/pull/54162)
  [Bugfix][MRV2] Release model and KV cache on in-process engine shutdown (#54162)
  _Files: `tests/models/test_language_model_cache_is_weak.py`, `tests/v1/engine/test_llm_engine_finalizer_is_weak.py`, `vllm/model_executor/models/interfaces.py`, `vllm/v1/engine/llm_engine.py`_
- **2026-08-29** [`7fd9cc036e`](https://github.com/vllm-project/vllm/commit/7fd9cc036e) [#53324](https://github.com/vllm-project/vllm/pull/53324)
  [KV Connector] Support MooncakeStore with hybrid DCP prefix caching (#53324)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+10 more__
- **2026-08-28** [`96242aa50d`](https://github.com/vllm-project/vllm/commit/96242aa50d) [#54246](https://github.com/vllm-project/vllm/pull/54246)
  [Bugfix][MRV2] Release layer-bound KV cache memory in shutdown() (#54246)
  _Files: `tests/conftest.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/utils.py`_
- **2026-08-28** [`53bf990502`](https://github.com/vllm-project/vllm/commit/53bf990502) [#52707](https://github.com/vllm-project/vllm/pull/52707)
  [Bugfix][KV Cache] Prevent negative external block allocation (#52707)
  _Files: `tests/v1/core/test_single_type_kv_cache_manager.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-08-27** [`d85708f7a4`](https://github.com/vllm-project/vllm/commit/d85708f7a4) [#53779](https://github.com/vllm-project/vllm/pull/53779)
  [1/N][KV Connector] Identify externally transferable KV cache groups (#53779)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/utils.py` _+7 more__
- **2026-08-27** [`478ec3ea41`](https://github.com/vllm-project/vllm/commit/478ec3ea41) [#54021](https://github.com/vllm-project/vllm/pull/54021)
  [Bugfix][KV Offload] Handle padded GPU cache storage (#54021)
  _Files: `tests/v1/simple_kv_offload/test_worker.py`, `vllm/v1/simple_kv_offload/worker.py`_
- **2026-08-27** [`94d96e2446`](https://github.com/vllm-project/vllm/commit/94d96e2446) [#53955](https://github.com/vllm-project/vllm/pull/53955)
  [Bugfix] Release CUDA graph profiling memory before KV cache allocation (#53955)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-08-25** [`bc39ded3c4`](https://github.com/vllm-project/vllm/commit/bc39ded3c4) [#53329](https://github.com/vllm-project/vllm/pull/53329)
  [Bugfix][KV Offload] Defer request-level cascade of in-flight primary keys (#53329)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/manager.py`_

## Disaggregation / PD  (11 commits)

- **2026-08-30** [`c92b29a1d4`](https://github.com/vllm-project/vllm/commit/c92b29a1d4) [#49274](https://github.com/vllm-project/vllm/pull/49274)
  [Bugfix] Make metadata send non-blocking in GroupCoordinator.isend_tensor_dict (#49274)
  _Files: `tests/distributed/test_comm_ops.py`, `vllm/distributed/parallel_state.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-08-29** [`a758a9f671`](https://github.com/vllm-project/vllm/commit/a758a9f671) [#54293](https://github.com/vllm-project/vllm/pull/54293)
  [Perf][KV Connector] Pin token_indices before non_blocking H2D in hf3fs helper (#54293)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`_
- **2026-08-29** [`6b110badbb`](https://github.com/vllm-project/vllm/commit/6b110badbb) [#51358](https://github.com/vllm-project/vllm/pull/51358)
  [Bugfix][Mooncake] Save exact Mamba boundary states (#51358)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_single_type_kv_cache_manager.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_connector.py` _+16 more__
- **2026-08-29** [`99013d77d3`](https://github.com/vllm-project/vllm/commit/99013d77d3) [#53253](https://github.com/vllm-project/vllm/pull/53253)
  [Bugfix][Distributed] Gate cross-node MNNVL custom all-reduce by group capability (#53253)
  _Files: `tests/distributed/test_custom_all_reduce.py`, `vllm/distributed/device_communicators/custom_all_reduce.py`_
- **2026-08-29** [`026d5af7f4`](https://github.com/vllm-project/vllm/commit/026d5af7f4) [#53008](https://github.com/vllm-project/vllm/pull/53008)
  [Bugfix] Fix ncclCommQueryProperties heap overflow with NCCL >= 2.31 (#53008)
  _Files: `vllm/distributed/device_communicators/pynccl_wrapper.py`, `vllm/utils/nccl.py`_
- **2026-08-27** [`6c4aa8bec3`](https://github.com/vllm-project/vllm/commit/6c4aa8bec3) [#53751](https://github.com/vllm-project/vllm/pull/53751)
  [RL] Support checkpoint-coordinate sparse NCCL weight updates (#53751)
  _Files: `docs/training/weight_transfer/README.md`, `docs/training/weight_transfer/nccl.md`, `examples/rl/rlhf_sparse_nccl.py`, `tests/distributed/test_weight_transfer.py` _+1 more__
- **2026-08-27** [`f8d38fbc87`](https://github.com/vllm-project/vllm/commit/f8d38fbc87) [#49994](https://github.com/vllm-project/vllm/pull/49994)
  [EC Connector] EC Offloading Connector use events instead of StepTracker (#49994)
  _Files: `tests/v1/ec_connector/__init__.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_embedding_cache.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_scheduler.py`, `tests/v1/ec_connector/unit/cpu/scheduler/test_step_tracker.py` _+11 more__
- **2026-08-26** [`f14369c7f9`](https://github.com/vllm-project/vllm/commit/f14369c7f9) [#53663](https://github.com/vllm-project/vllm/pull/53663)
  [Bugfix][Mooncake] Fix Mamba prefill truncation ordering (#53663)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_connector_hybrid_mamba.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_connector.py`_
- **2026-08-26** [`ee5ae2ae70`](https://github.com/vllm-project/vllm/commit/ee5ae2ae70) [#52497](https://github.com/vllm-project/vllm/pull/52497)
  [RL] Add rank-local IPC weight updates (#52497)
  _Files: `docs/training/weight_transfer/ipc.md`, `tests/distributed/test_weight_transfer.py`, `tests/v1/worker/test_gpu_worker_weight_transfer.py`, `vllm/distributed/weight_transfer/base.py` _+2 more__
- **2026-08-25** [`d4c4ceb31e`](https://github.com/vllm-project/vllm/commit/d4c4ceb31e) [#53523](https://github.com/vllm-project/vllm/pull/53523)
  [Bugfix][NIXL] Fix Mamba prefill truncation ordering (#53523)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_scheduler.py` _+1 more__
- **2026-08-24** [`26858770ec`](https://github.com/vllm-project/vllm/commit/26858770ec) [#52951](https://github.com/vllm-project/vllm/pull/52951)
  [Bugfix] Reuse CUDA streams in packed weight transfer to cap reserved-memory waste (#52951)
  _Files: `vllm/distributed/weight_transfer/packed_tensor.py`_

## Quantization  (9 commits)

- **2026-08-31** [`bd575a0d0b`](https://github.com/vllm-project/vllm/commit/bd575a0d0b) [#47434](https://github.com/vllm-project/vllm/pull/47434)
  [AutoRound] Support AutoRound Format Block-Wise FP8 in vLLM (#47434)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/config_parser.py`, `vllm/model_executor/layers/quantization/inc/inc.py`, `vllm/model_executor/layers/quantization/inc/schemes/__init__.py` _+6 more__
- **2026-08-31** [`2a61f060d3`](https://github.com/vllm-project/vllm/commit/2a61f060d3) [#53536](https://github.com/vllm-project/vllm/pull/53536)
  [XPU] Ensure unquantized linear weight is N-contiguous (#53536)
  _Files: `vllm/envs.py`, `vllm/model_executor/layers/linear.py`_
- **2026-08-30** [`78fa18910e`](https://github.com/vllm-project/vllm/commit/78fa18910e) [#54420](https://github.com/vllm-project/vllm/pull/54420)
  ci: add MIG slice size to H200 job labels (#54420)
  _Files: `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/cuda.yaml`, `.buildkite/test_areas/engine.yaml` _+19 more__
- **2026-08-28** [`06cccf8730`](https://github.com/vllm-project/vllm/commit/06cccf8730) [#53409](https://github.com/vllm-project/vllm/pull/53409)
  [Bugfix] Fix int32 token offset overflow in fused SiLU block quant (#53409)
  _Files: `csrc/libtorch_stable/quantization/fused_kernels/fused_silu_mul_block_quant.cu`, `tests/kernels/core/test_fused_silu_mul_block_quant.py`_
- **2026-08-28** [`31c579503d`](https://github.com/vllm-project/vllm/commit/31c579503d) [#52736](https://github.com/vllm-project/vllm/pull/52736)
  update quark docs to include online quantization (#52736)
  _Files: `docs/features/quantization/quark.md`_
- **2026-08-28** [`f3b91f1af2`](https://github.com/vllm-project/vllm/commit/f3b91f1af2) [#54099](https://github.com/vllm-project/vllm/pull/54099)
  Remove wrongly added e2e test (#54099)
  _Files: `tests/evals/gsm8k/configs/humming/Qwen3-30B-A3B-MXFP4A16-humming-act-fp8-block.yaml`, `tests/evals/gsm8k/configs/humming/config-act-fp8.txt`_
- **2026-08-28** [`5bbc58c0ad`](https://github.com/vllm-project/vllm/commit/5bbc58c0ad) [#54111](https://github.com/vllm-project/vllm/pull/54111)
  [Bugfix] Remove race in fused groupwise RMSNorm quantization (#54111)
  _Files: `csrc/libtorch_stable/quantization/fused_kernels/layernorm_utils.cuh`, `tests/kernels/core/test_fused_quant_layernorm.py`_
- **2026-08-27** [`b3af042abd`](https://github.com/vllm-project/vllm/commit/b3af042abd) [#53869](https://github.com/vllm-project/vllm/pull/53869)
  Bugfix: use PCP slot mappings for PIECEWISE capture (#53869)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`, `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP2-PCP2-EP.yaml`, `tests/v1/cudagraph/test_cudagraph_manager.py`, `vllm/v1/worker/gpu/cudagraph_utils.py` _+1 more__
- **2026-08-24** [`e8888b2d68`](https://github.com/vllm-project/vllm/commit/e8888b2d68) [#53101](https://github.com/vllm-project/vllm/pull/53101)
  [Model] Add FP8 quantization support for ModernBERT (#53101)
  _Files: `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/test_modernbert_fp8.py`, `vllm/model_executor/models/modernbert.py`_

## Perf / Benchmark  (9 commits)

- **2026-08-28** [`6f91e3d953`](https://github.com/vllm-project/vllm/commit/6f91e3d953) [#53412](https://github.com/vllm-project/vllm/pull/53412)
  [Perf] Split xdrope_positions H2D copy into per-row transfers (#53412)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-28** [`f956e1c343`](https://github.com/vllm-project/vllm/commit/f956e1c343) [#54167](https://github.com/vllm-project/vllm/pull/54167)
  [Kimi-K3][Bugfix] Fix low-latency GEMM fallback initialization (#54167)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`_
- **2026-08-28** [`b74ac0bc61`](https://github.com/vllm-project/vllm/commit/b74ac0bc61) [#53109](https://github.com/vllm-project/vllm/pull/53109)
  [Bugfix] Allocate packed outputs in fused_q_kv_rmsnorm so q_b_proj keeps its low-latency GEMM path at decode (#53109)
  _Files: `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `vllm/models/common/ops/fused_qk_rmsnorm.py`_
- **2026-08-27** [`9818bb3db8`](https://github.com/vllm-project/vllm/commit/9818bb3db8) [#54088](https://github.com/vllm-project/vllm/pull/54088)
  [Kimi Perf] Tune hopper low latency gemm kernel, 4%~97% performance improvement (#54088)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`_
- **2026-08-27** [`833fa6233c`](https://github.com/vllm-project/vllm/commit/833fa6233c) [#53920](https://github.com/vllm-project/vllm/pull/53920)
  [Benchmark] Warn on warm prefix cache for random serve runs (#53920)
  _Files: `docs/benchmarking/cli.md`_
- **2026-08-26** [`76cfe1cd88`](https://github.com/vllm-project/vllm/commit/76cfe1cd88) [#53942](https://github.com/vllm-project/vllm/pull/53942)
  [Kimi K3 Perf] Optimize `eh_proj` linear calculation, 12.9 ~ 25.2% kernel performance improvement (#53942)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`, `vllm/models/kimi_k3/nvidia/mtp.py`_
- **2026-08-25** [`bc2d63e650`](https://github.com/vllm-project/vllm/commit/bc2d63e650) [#53534](https://github.com/vllm-project/vllm/pull/53534)
  [Kimi K3][Kernel] Enable low-latency decode GEMM dispatch on SM100 (#53534)
  _Files: `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`_
- **2026-08-25** [`384d079697`](https://github.com/vllm-project/vllm/commit/384d079697) [#53649](https://github.com/vllm-project/vllm/pull/53649)
  [Perf] Autotune batch invariance triton kernel in blackwell, 33.6% E2E latency reduction (#53649)
  _Files: `tests/v1/determinism/test_matmul_batch_invariant.py`, `vllm/model_executor/determinism/batch_invariant_configs.py`_
- **2026-08-24** [`7797b6022c`](https://github.com/vllm-project/vllm/commit/7797b6022c) [#53247](https://github.com/vllm-project/vllm/pull/53247)
  [Kernel][Perf] Per-architecture tuned configs for batch-invariant persistent matmul (~3x decode kernels on RTX 4090D/H20) (#53247)
  _Files: `tests/v1/determinism/test_matmul_batch_invariant.py`, `vllm/model_executor/layers/batch_invariant.py`, `vllm/model_executor/layers/batch_invariant_configs.py`_

## Docs  (8 commits)

- **2026-08-30** [`488b6da105`](https://github.com/vllm-project/vllm/commit/488b6da105) [#54412](https://github.com/vllm-project/vllm/pull/54412)
  [Doc] Fix griffe warnings in HYV4 tool parser (#54412)
  _Files: `vllm/tool_parsers/hy_v4_tool_parser.py`_
- **2026-08-28** [`b131311fb4`](https://github.com/vllm-project/vllm/commit/b131311fb4) [#54263](https://github.com/vllm-project/vllm/pull/54263)
  [CI/Build] Add advisory PR title format check (#54263)
  _Files: `.github/workflows/pr-title.yml`, `docs/contributing/README.md`_
- **2026-08-27** [`a18dbe49ad`](https://github.com/vllm-project/vllm/commit/a18dbe49ad) [#53839](https://github.com/vllm-project/vllm/pull/53839)
  [Doc] Add EXAONE-4.0-1.2B to batch invariance tested models (#53839)
  _Files: `docs/features/batch_invariance.md`_
- **2026-08-27** [`79651d6085`](https://github.com/vllm-project/vllm/commit/79651d6085) [#53946](https://github.com/vllm-project/vllm/pull/53946)
  [Tools][Recipes] Improve sweep recommendations and short-alias parsing (#53946)
  _Files: `docs/models/hardware_supported_models/cpu.md`, `tools/recipes/README.md`, `tools/recipes/RUNTIME_TUNING.md`, `tools/recipes/SWEEP_TUNING.md` _+3 more__
- **2026-08-26** [`f18d0ba90d`](https://github.com/vllm-project/vllm/commit/f18d0ba90d) [#53650](https://github.com/vllm-project/vllm/pull/53650)
  [Doc] Add Granite 3.1 series to batch invariance tested models (#53650)
  _Files: `docs/features/batch_invariance.md`_
- **2026-08-25** [`10ade93979`](https://github.com/vllm-project/vllm/commit/10ade93979) [#53494](https://github.com/vllm-project/vllm/pull/53494)
  [XPU] update key supported models (#53494)
  _Files: `docs/models/hardware_supported_models/xpu.md`_
- **2026-08-25** [`4af586e185`](https://github.com/vllm-project/vllm/commit/4af586e185) [#53325](https://github.com/vllm-project/vllm/pull/53325)
  Vllm recipes tool improve (#53325)
  _Files: `tools/recipes/README.md`, `tools/recipes/REFERENCE.md`, `tools/recipes/RUNTIME_TUNING.md`, `tools/recipes/SWEEP_TUNING.md` _+5 more__
- **2026-08-24** [`cc40c3673b`](https://github.com/vllm-project/vllm/commit/cc40c3673b) [#53226](https://github.com/vllm-project/vllm/pull/53226)
  [Xeon][doc]add Xeon recipes into table (#53226)
  _Files: `docs/models/hardware_supported_models/cpu.md`_

## LoRA  (7 commits)

- **2026-08-30** [`5e71a11eb2`](https://github.com/vllm-project/vllm/commit/5e71a11eb2) [#54326](https://github.com/vllm-project/vllm/pull/54326)
  [CI] Mark L4 GPU test steps with device: l4 for EKS migration (#54326)
  _Files: `.buildkite/test_areas/crcr_report.yaml`, `.buildkite/test_areas/disaggregated.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/engine.yaml` _+9 more__
- **2026-08-28** [`2aac565cae`](https://github.com/vllm-project/vllm/commit/2aac565cae) [#53333](https://github.com/vllm-project/vllm/pull/53333)
  [Core][KV Connector] Start async KV loads after the forward launch when no sync loads are scheduled (#53333)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/test_nixl_simple_cpu_offload.py` _+13 more__
- **2026-08-27** [`3cc015acd2`](https://github.com/vllm-project/vllm/commit/3cc015acd2) [#53756](https://github.com/vllm-project/vllm/pull/53756)
  [Rust Frontend][gRPC] Enforce LoRA path validation across transports (#53756)
  _Files: `rust/src/server/src/grpc/control.rs`, `rust/src/server/src/grpc/tests.rs`, `rust/src/server/src/lora.rs`, `rust/src/server/src/routes/lora.rs`_
- **2026-08-26** [`75aa189ba0`](https://github.com/vllm-project/vllm/commit/75aa189ba0) [#53843](https://github.com/vllm-project/vllm/pull/53843)
  [LoRA] Cleanup VocabParallelEmbedding (#53843)
  _Files: `vllm/lora/layers/__init__.py`, `vllm/lora/layers/logits_processor.py`, `vllm/lora/layers/vocab_parallel_embedding.py`, `vllm/lora/punica_wrapper/punica_base.py` _+2 more__
- **2026-08-26** [`46638857fd`](https://github.com/vllm-project/vllm/commit/46638857fd) [#52830](https://github.com/vllm-project/vllm/pull/52830)
  [Bugfix][Structured Output] Preserve reasoning adapters for shared parser engines (#52830)
  _Files: `tests/parser/engine/test_parser_engine.py`, `vllm/parser/parser_manager.py`_
- **2026-08-25** [`1f9444a34f`](https://github.com/vllm-project/vllm/commit/1f9444a34f) [#52840](https://github.com/vllm-project/vllm/pull/52840)
  [Rust Frontend][gRPC] Add LoRA lifecycle control (#52840)
  _Files: `rust/Cargo.lock`, `rust/proto/control.proto`, `rust/proto/inference.proto`, `rust/src/engine-core-client/src/protocol/lora.rs` _+8 more__
- **2026-08-25** [`7b7e5cbfcd`](https://github.com/vllm-project/vllm/commit/7b7e5cbfcd) [#53519](https://github.com/vllm-project/vllm/pull/53519)
  [Bugfix][LoRA] Restore tower and connector LoRA support for LFM2-VL (#53519)
  _Files: `vllm/model_executor/models/lfm2_vl.py`_

## Speculative Decoding  (4 commits)

- **2026-08-31** [`648b7468b8`](https://github.com/vllm-project/vllm/commit/648b7468b8) [#54482](https://github.com/vllm-project/vllm/pull/54482)
  [CI/Build] Fix Kimi K3 Eagle3 test fixture (#54482)
  _Files: `tests/models/kimi_k3/test_eagle3.py`_
- **2026-08-28** [`df14152ac6`](https://github.com/vllm-project/vllm/commit/df14152ac6) [#54239](https://github.com/vllm-project/vllm/pull/54239)
  [Model] Support speculative decoding method for PLaMo3 (#54239)
  _Files: `tests/model_executor/test_plamo3.py`, `vllm/model_executor/models/plamo3.py`_
- **2026-08-25** [`d5cadcee86`](https://github.com/vllm-project/vllm/commit/d5cadcee86) [#52242](https://github.com/vllm-project/vllm/pull/52242)
  [Feature][DSpark]: Logprobs adaptive verification (#52242)
  _Files: `docs/features/speculative_decoding/adaptive_verification.md`, `tests/v1/engine/test_output_processor.py`, `tests/v1/test_outputs.py`, `tests/v1/worker/test_gpu_rejection_sampler_chunking.py` _+6 more__
- **2026-08-24** [`23ab0cfdbc`](https://github.com/vllm-project/vllm/commit/23ab0cfdbc) [#52193](https://github.com/vllm-project/vllm/pull/52193)
  speculative decoding under tensor parallelism (TP>1) , workspace creation select max hidden dim of target and draft model (#52193)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_

## Compilation / CUDA Graph  (3 commits)

- **2026-08-30** [`b2dc864bb6`](https://github.com/vllm-project/vllm/commit/b2dc864bb6) [#54418](https://github.com/vllm-project/vllm/pull/54418)
  [Bugfix][Spec Decode] Keep default CUDA graph sizes memory-safe (#54418)
  _Files: `tests/compile/test_config.py`, `vllm/config/compilation.py`, `vllm/config/vllm.py`_
- **2026-08-26** [`b1fbbc2ade`](https://github.com/vllm-project/vllm/commit/b1fbbc2ade) [#53515](https://github.com/vllm-project/vllm/pull/53515)
  BugFix(PCP): use persistent input buffers for PIECEWISE CUDA graphs (#53515)
  _Files: `tests/v1/worker/test_gpu_pcp_manager.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pcp_manager.py`_
- **2026-08-24** [`a4d70bef37`](https://github.com/vllm-project/vllm/commit/a4d70bef37) [#53306](https://github.com/vllm-project/vllm/pull/53306)
  [Model Runner V2] Reserve CUDA graph memory (#53306)
  _Files: `tests/test_config.py`, `tests/v1/sample/test_logprobs.py`, `tests/v1/worker/test_gpu_model_runner_v2_cudagraph_profiling.py`, `vllm/model_executor/layers/mamba/gdn/kimi_gdn_linear_attn.py` _+9 more__

## Distributed  (1 commits)

- **2026-08-24** [`f94666b60d`](https://github.com/vllm-project/vllm/commit/f94666b60d) [#52389](https://github.com/vllm-project/vllm/pull/52389)
  [Bugfix][XPU] Skip oneCCL warm-up all_reduce when world_size == 1 (#52389)
  _Files: `vllm/v1/worker/xpu_worker.py`_

---
_Generated 2026-08-31 16:08 UTC_