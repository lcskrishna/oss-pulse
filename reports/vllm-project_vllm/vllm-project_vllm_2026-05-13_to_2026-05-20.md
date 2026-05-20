# vllm-project/vllm — Weekly Change Report
**Period:** 2026-05-13 → 2026-05-20  |  **Total commits:** 225

## ✨ New Features This Week

- **2026-05-20** [#42111](https://github.com/vllm-project/vllm/pull/42111) — [CI] Add DSV4-Flash to gsm8k moe-refactor/config-b200.txt (#42111)
- **2026-05-20** [#42975](https://github.com/vllm-project/vllm/pull/42975) — add enqueue all option to throughput benchmark (#42975)
- **2026-05-20** [#43143](https://github.com/vllm-project/vllm/pull/43143) — [Cohere] Enable Cohere MoE (#43143)
- **2026-05-19** [#42764](https://github.com/vllm-project/vllm/pull/42764) — [Model] Support post-norm architecture for EAGLE-3 supeculators (#42764)
- **2026-05-19** [#42080](https://github.com/vllm-project/vllm/pull/42080) — [feat] Add FP8 per-tensor Q scale support to Triton attention backend (#42080)
- **2026-05-19** [#42540](https://github.com/vllm-project/vllm/pull/42540) — [Misc] add humming to dependencies (#42540)
- **2026-05-19** [#42654](https://github.com/vllm-project/vllm/pull/42654) — [Model] Openvla support (#42654)
- **2026-05-19** [#42677](https://github.com/vllm-project/vllm/pull/42677) — [CI] Add MTP + PD disagg test for Qwen3.5 (#42677)
- **2026-05-19** [#42828](https://github.com/vllm-project/vllm/pull/42828) — [KVConnector][DSV4] HMA support for Mooncake store connector (#42828)
- **2026-05-19** [#42626](https://github.com/vllm-project/vllm/pull/42626) — [Docs] Add SVG images for pooling models. (#42626)
- _…and 50 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-05-20** [`cd0ff26e7a`](https://github.com/vllm-project/vllm/commit/cd0ff26e7a) [#42111](https://github.com/vllm-project/vllm/pull/42111) — [CI] Add DSV4-Flash to gsm8k moe-refactor/config-b200.txt (#42111)
- **2026-05-19** [`07beaed842`](https://github.com/vllm-project/vllm/commit/07beaed842) [#43077](https://github.com/vllm-project/vllm/pull/43077) — [Model Refactoring] Rename deepseek_v4.py to model.py [4/N] (#43077)
- **2026-05-19** [`b14be81c1f`](https://github.com/vllm-project/vllm/commit/b14be81c1f) [#43073](https://github.com/vllm-project/vllm/pull/43073) — [Model Refactoring] Move deepseek_v4_ops to models/deepseek_v4 [3/N] (#43073)
- **2026-05-19** [`301d986473`](https://github.com/vllm-project/vllm/commit/301d986473) [#42946](https://github.com/vllm-project/vllm/pull/42946) — [Frontend] Consolidate beam search by BeamSearchMixin. (#42946)
- **2026-05-19** [`87b08c5f64`](https://github.com/vllm-project/vllm/commit/87b08c5f64) [#43039](https://github.com/vllm-project/vllm/pull/43039) — [Model Refactoring] Move DeepSeek V4 layers to `models/deepseek_v4/` [2/N] (#43039)
- **2026-05-19** [`287471b994`](https://github.com/vllm-project/vllm/commit/287471b994) [#43004](https://github.com/vllm-project/vllm/pull/43004) — [Model Refactoring] Migrate DeepSeek V4 to vllm/models/ [1/N]  (#43004)
- **2026-05-18** [`8fc1c284b9`](https://github.com/vllm-project/vllm/commit/8fc1c284b9) [#42880](https://github.com/vllm-project/vllm/pull/42880) — [ROCm] Guard AITER GDN decode fast path by layout (#42880)
- **2026-05-18** [`a2c8fc6657`](https://github.com/vllm-project/vllm/commit/a2c8fc6657) [#41436](https://github.com/vllm-project/vllm/pull/41436) — [ROCm][Quantization][3/N] Refactor quark_moe w4a4 w/ oracle (#41436)
- **2026-05-18** [`67f58ce23f`](https://github.com/vllm-project/vllm/commit/67f58ce23f) [#42930](https://github.com/vllm-project/vllm/pull/42930) — [Bugfix] Fix DSV4 MTP after ROCm mHC integration (#42930)
- **2026-05-18** [`b50646e5ef`](https://github.com/vllm-project/vllm/commit/b50646e5ef) [#42909](https://github.com/vllm-project/vllm/pull/42909) — [ROCm][CI] Stabilize ROCm pooling and multimodal CI (#42909)
- **2026-05-17** [`599e75f432`](https://github.com/vllm-project/vllm/commit/599e75f432) [#42810](https://github.com/vllm-project/vllm/pull/42810) — [ROCm] [Bugfix] Fix DeepSeek V4 Functionality and Accuracy (#42810)
- **2026-05-16** [`36e74c9ea4`](https://github.com/vllm-project/vllm/commit/36e74c9ea4) [#42689](https://github.com/vllm-project/vllm/pull/42689) — [KV Connector] Support disk offloading in MooncakeStoreConnector (#42689)
- **2026-05-16** [`8a56da3845`](https://github.com/vllm-project/vllm/commit/8a56da3845) [#42304](https://github.com/vllm-project/vllm/pull/42304) — [Experimental] Breakable CUDA graph (#42304)
- **2026-05-16** [`4db300e95f`](https://github.com/vllm-project/vllm/commit/4db300e95f) [#42807](https://github.com/vllm-project/vllm/pull/42807) — [ROCm][CI] Removed problematic command override mechanism (#42807)
- **2026-05-15** [`bd9dbe6060`](https://github.com/vllm-project/vllm/commit/bd9dbe6060) [#42606](https://github.com/vllm-project/vllm/pull/42606) — [ROCm][Bugfix] Fix fused_mla_dual_rms_norm for AITER API rename _fused_qk_rmsnorm (#42606)
- **2026-05-15** [`4d67d3bde2`](https://github.com/vllm-project/vllm/commit/4d67d3bde2) [#42072](https://github.com/vllm-project/vllm/pull/42072) — [ROCm] Restore fast top_k_per_row kernels for sparse MLA when topk_tokens=2048 (#42072)
- **2026-05-15** [`be7a03ea65`](https://github.com/vllm-project/vllm/commit/be7a03ea65) [#42409](https://github.com/vllm-project/vllm/pull/42409) — [ROCm] Widen AITER fused AR RMSNorm 1-stage gate (#42409)
- **2026-05-15** [`46a95815d3`](https://github.com/vllm-project/vllm/commit/46a95815d3) [#42509](https://github.com/vllm-project/vllm/pull/42509) — [ROCm][MLA] FP8 ASM prefill for AITER dense MLA backend on gfx950 (#42509)
- **2026-05-15** [`d792d993c1`](https://github.com/vllm-project/vllm/commit/d792d993c1) [#37826](https://github.com/vllm-project/vllm/pull/37826) — [ROCm] Widen OAI Triton MoE capability range to include gfx12 (RDNA4) (#37826)
- **2026-05-15** [`d735968f6d`](https://github.com/vllm-project/vllm/commit/d735968f6d) [#42025](https://github.com/vllm-project/vllm/pull/42025) — [ROCm][CI] Stage B gating (#42025)
- **2026-05-15** [`ccde9540be`](https://github.com/vllm-project/vllm/commit/ccde9540be) [#42604](https://github.com/vllm-project/vllm/pull/42604) — DeepSeekV4-Pro enable cuda graph full and piecewise mode (#42604)
- **2026-05-15** [`2676ab1e0b`](https://github.com/vllm-project/vllm/commit/2676ab1e0b) [#35024](https://github.com/vllm-project/vllm/pull/35024) — [Deprecation] Remove old locations of `get_tokenizer` and `resolve_hf_chat_template` (#35024)
- **2026-05-15** [`0d4d334eaa`](https://github.com/vllm-project/vllm/commit/0d4d334eaa) [#42150](https://github.com/vllm-project/vllm/pull/42150) — Bump llguidance to 1.7 (#42150)
- **2026-05-15** [`fa2a33b893`](https://github.com/vllm-project/vllm/commit/fa2a33b893) [#38288](https://github.com/vllm-project/vllm/pull/38288) — [Quant] Consolidate GPTQ: rename gptq_marlin.py to auto_gptq.py (#38288)
- **2026-05-14** [`4cfcc0866f`](https://github.com/vllm-project/vllm/commit/4cfcc0866f) [#38680](https://github.com/vllm-project/vllm/pull/38680) — [CI][ROCm] Remove unsupported cases in test_fusion.py (#38680)
- **2026-05-14** [`f887aa1a53`](https://github.com/vllm-project/vllm/commit/f887aa1a53) [#40710](https://github.com/vllm-project/vllm/pull/40710) — [Aiter][ROCm] RMSNormGated+GroupedQuantFP8 fusion (#40710)
- **2026-05-14** [`f07b1da797`](https://github.com/vllm-project/vllm/commit/f07b1da797) [#42062](https://github.com/vllm-project/vllm/pull/42062) — [ROCm] Enable gluon paged MQA logits on gfx950 (MI355X) (#42062)
- **2026-05-14** [`768f4a6f26`](https://github.com/vllm-project/vllm/commit/768f4a6f26) [#40857](https://github.com/vllm-project/vllm/pull/40857) — [CI][AMD][BugFix] Prevent triton compiler error when running test_moe_layer with use_ep = True on ROCm (#40857)
- **2026-05-14** [`addef3299c`](https://github.com/vllm-project/vllm/commit/addef3299c) [#42126](https://github.com/vllm-project/vllm/pull/42126) — [CI][AMD] Skip tests where models have problems or fails on both HW types (#42126)
- **2026-05-14** [`ce29c26b31`](https://github.com/vllm-project/vllm/commit/ce29c26b31) [#40453](https://github.com/vllm-project/vllm/pull/40453) — Update Dockerfile.rocm for AINIC & Thor NIC (#40453)
- **2026-05-14** [`fd7d858c8a`](https://github.com/vllm-project/vllm/commit/fd7d858c8a) [#42098](https://github.com/vllm-project/vllm/pull/42098) — Use hidden_pad and intermediate_pad from vLLM #34301 (#42098)
- **2026-05-13** [`a8887c208f`](https://github.com/vllm-project/vllm/commit/a8887c208f) [#41946](https://github.com/vllm-project/vllm/pull/41946) — [Bugfix] [ROCm] [DSV4] [Perf] Add aiter mhc support (#41946)
- **2026-05-13** [`0a62f5eec9`](https://github.com/vllm-project/vllm/commit/0a62f5eec9) [#42326](https://github.com/vllm-project/vllm/pull/42326) — [AMD] skip machete tests for rocm (#42326)
- **2026-05-13** [`d628a3c5cb`](https://github.com/vllm-project/vllm/commit/d628a3c5cb) [#41572](https://github.com/vllm-project/vllm/pull/41572) — [ROCm][CI] Skip ROCm batch invalid-input test pending torch fix (#41572)
- **2026-05-13** [`74dffae666`](https://github.com/vllm-project/vllm/commit/74dffae666) [#42411](https://github.com/vllm-project/vllm/pull/42411) — [ROCm] Run AITER RMSNorm pad fusion before AR RMS fusion (#42411)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#34186](https://github.com/vllm-project/vllm/issues/34186) | [Bug]: LoRA adapters with mismatched module name prefixes silently pro | stale | 2026-05-20 |
| [#34781](https://github.com/vllm-project/vllm/issues/34781) | [Feature]: parity with cuda - ROCm Kimi K2.5 disagg PD +wideEP recipe | feature request, rocm, stale | 2026-05-20 |
| [#28649](https://github.com/vllm-project/vllm/issues/28649) | [Feature]: Someone please upstream this gfx1201/RDNA4 FP8 Patch into v | feature request, rocm, unstale | 2026-05-20 |
| [#32554](https://github.com/vllm-project/vllm/issues/32554) | [Bug]: Error in inspecting model architecture 'Gemma3ForConditionalGen | bug, stale | 2026-05-20 |
| [#33857](https://github.com/vllm-project/vllm/issues/33857) | [Bug]: Qwen3-Coder-Next fails with Triton allocator error on DGX Spark | bug, stale | 2026-05-20 |
| [#43174](https://github.com/vllm-project/vllm/issues/43174) | [Bug]: ZeroDivisionError in deepgemm_post_process_fp8_weight_block whe | bug | 2026-05-20 |
| [#34573](https://github.com/vllm-project/vllm/issues/34573) | [Installation/Runtime]: Linux ROCM7 /  RuntimeError: No HIP GPUs are a | installation, rocm, stale | 2026-05-20 |
| [#34583](https://github.com/vllm-project/vllm/issues/34583) | [Bug] Missing Vocabulary Validation for MTP and Eagle Speculative Meth | bug, stale | 2026-05-20 |
| [#34755](https://github.com/vllm-project/vllm/issues/34755) | Qwen3-Coder-Next-FP8 with tool calling causes system hard-freeze on mu | usage, stale | 2026-05-20 |
| [#42808](https://github.com/vllm-project/vllm/issues/42808) | [Bug]: 这次崩溃的直接原因是 TurboQuant 注意力后端与 MTP 推测解码在 vLLM 0.21.0 版本中的兼容性问题，具体 | bug | 2026-05-20 |
| [#43009](https://github.com/vllm-project/vllm/issues/43009) | [Bug]: Triton kernel JIT compilation during inference | bug | 2026-05-20 |
| [#43163](https://github.com/vllm-project/vllm/issues/43163) | [Bug]: GLM-5.1-FP8 produces gibberish with RunAI streamer after ac3dac | — | 2026-05-20 |
| [#42781](https://github.com/vllm-project/vllm/issues/42781) | [Bug]: Gemma 4 speculative decoding truncating reasoning output | bug | 2026-05-19 |
| [#40554](https://github.com/vllm-project/vllm/issues/40554) | [AMD][CI Failure][Tracker] Static dashboard tracker for current CI fai | rocm, ci-failure | 2026-05-19 |
| [#42860](https://github.com/vllm-project/vllm/issues/42860) | [Bug]: integer overflow in activation_kernels.cu | bug | 2026-05-19 |
| [#42862](https://github.com/vllm-project/vllm/issues/42862) | [Bug]: integer overflow in layernorm_kernels.cu | bug | 2026-05-19 |
| [#43153](https://github.com/vllm-project/vllm/issues/43153) | [Bug][Perf Regression]: AMD MI355X Kimi K2.5/2.6 arch 38% perf regress | bug, rocm | 2026-05-19 |
| [#28640](https://github.com/vllm-project/vllm/issues/28640) | [Bug]: LoRA/Adapter Loading Error with Qwen3-VL-8B-Instruct Multimodal | bug, unstale | 2026-05-19 |
| [#42545](https://github.com/vllm-project/vllm/issues/42545) | [RFC]: Tensor descriptor (TD) adoption strategy for vLLM Triton kernel | — | 2026-05-19 |
| [#42261](https://github.com/vllm-project/vllm/issues/42261) | [Bug]: Frequent crashes with gemma4 MTP enabled | bug | 2026-05-19 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 34 |
| MoE / Expert Parallel | 32 |
| Attention | 31 |
| Other | 28 |
| Disaggregation / PD | 16 |
| Multimodal | 16 |
| Models | 11 |
| CI / Build | 11 |
| Quantization | 10 |
| Serving / API | 8 |
| Speculative Decoding | 8 |
| Scheduler / Engine | 6 |
| KV Cache / Offload | 4 |
| Perf / Benchmark | 4 |
| Compilation / CUDA Graph | 3 |
| Docs | 2 |
| LoRA | 1 |

## ROCm / AMD  (34 commits)

- **2026-05-20** [`cd0ff26e7a`](https://github.com/vllm-project/vllm/commit/cd0ff26e7a) [#42111](https://github.com/vllm-project/vllm/pull/42111)
  [CI] Add DSV4-Flash to gsm8k moe-refactor/config-b200.txt (#42111)
  _Files: `requirements/common.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt`, `requirements/test/xpu.txt` _+2 more__
- **2026-05-19** [`07beaed842`](https://github.com/vllm-project/vllm/commit/07beaed842) [#43077](https://github.com/vllm-project/vllm/pull/43077)
  [Model Refactoring] Rename deepseek_v4.py to model.py [4/N] (#43077)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/models/deepseek_v4/__init__.py`, `vllm/models/deepseek_v4/amd/deepseek_v4.py`, `vllm/models/deepseek_v4/amd/deepseek_v4_mtp.py` _+4 more__
- **2026-05-19** [`b14be81c1f`](https://github.com/vllm-project/vllm/commit/b14be81c1f) [#43073](https://github.com/vllm-project/vllm/pull/43073)
  [Model Refactoring] Move deepseek_v4_ops to models/deepseek_v4 [3/N] (#43073)
  _Files: `.github/CODEOWNERS`, `tests/kernels/core/test_fused_q_kv_rmsnorm.py`, `tests/kernels/test_compressor_kv_cache.py`, `tests/kernels/test_fused_deepseek_v4_qnorm_rope_kv_insert.py` _+16 more__
- **2026-05-19** [`301d986473`](https://github.com/vllm-project/vllm/commit/301d986473) [#42946](https://github.com/vllm-project/vllm/pull/42946)
  [Frontend] Consolidate beam search by BeamSearchMixin. (#42946)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/samplers.yaml`, `vllm/entrypoints/generate/__init__.py`, `vllm/entrypoints/generate/beam_search/__init__.py` _+5 more__
- **2026-05-19** [`87b08c5f64`](https://github.com/vllm-project/vllm/commit/87b08c5f64) [#43039](https://github.com/vllm-project/vllm/pull/43039)
  [Model Refactoring] Move DeepSeek V4 layers to `models/deepseek_v4/` [2/N] (#43039)
  _Files: `.github/CODEOWNERS`, `vllm/models/deepseek_v4/attention.py`, `vllm/models/deepseek_v4/compressor.py`, `vllm/models/deepseek_v4/nvidia/deepseek_v4.py` _+1 more__
- **2026-05-19** [`287471b994`](https://github.com/vllm-project/vllm/commit/287471b994) [#43004](https://github.com/vllm-project/vllm/pull/43004)
  [Model Refactoring] Migrate DeepSeek V4 to vllm/models/ [1/N]  (#43004)
  _Files: `tests/models/test_deepseek_v4_mega_moe.py`, `vllm/model_executor/layers/quantization/__init__.py`, `vllm/model_executor/models/registry.py`, `vllm/models/__init__.py` _+8 more__
- **2026-05-18** [`8fc1c284b9`](https://github.com/vllm-project/vllm/commit/8fc1c284b9) [#42880](https://github.com/vllm-project/vllm/pull/42880)
  [ROCm] Guard AITER GDN decode fast path by layout (#42880)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`_
- **2026-05-18** [`a2c8fc6657`](https://github.com/vllm-project/vllm/commit/a2c8fc6657) [#41436](https://github.com/vllm-project/vllm/pull/41436)
  [ROCm][Quantization][3/N] Refactor quark_moe w4a4 w/ oracle (#41436)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-EMU-TP2.yaml`, `tests/evals/gsm8k/configs/models-mi3xx.txt`, `tests/evals/gsm8k/configs/models-qwen35-mi355.txt` _+4 more__
- **2026-05-18** [`67f58ce23f`](https://github.com/vllm-project/vllm/commit/67f58ce23f) [#42930](https://github.com/vllm-project/vllm/pull/42930)
  [Bugfix] Fix DSV4 MTP after ROCm mHC integration (#42930)
  _Files: `vllm/model_executor/models/deepseek_v4.py`, `vllm/model_executor/models/deepseek_v4_mtp.py`_
- **2026-05-18** [`b50646e5ef`](https://github.com/vllm-project/vllm/commit/b50646e5ef) [#42909](https://github.com/vllm-project/vllm/pull/42909)
  [ROCm][CI] Stabilize ROCm pooling and multimodal CI (#42909)
  _Files: `tests/models/language/pooling/test_gritlm.py`, `tests/models/language/pooling/test_max_tokens_per_doc.py`, `tests/models/multimodal/generation/test_qwen2_5_vl.py`, `vllm/model_executor/models/transformers/base.py`_
- **2026-05-17** [`599e75f432`](https://github.com/vllm-project/vllm/commit/599e75f432) [#42810](https://github.com/vllm-project/vllm/pull/42810)
  [ROCm] [Bugfix] Fix DeepSeek V4 Functionality and Accuracy (#42810)
  _Files: `vllm/model_executor/layers/mhc.py`, `vllm/model_executor/layers/sparse_attn_indexer.py`, `vllm/model_executor/models/deepseek_v4.py`, `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-05-16** [`8a56da3845`](https://github.com/vllm-project/vllm/commit/8a56da3845) [#42304](https://github.com/vllm-project/vllm/pull/42304)
  [Experimental] Breakable CUDA graph (#42304)
  _Files: `.buildkite/test_areas/cuda.yaml`, `tests/v1/cudagraph/test_breakable_cudagraph.py`, `vllm/compilation/breakable_cudagraph.py`, `vllm/config/vllm.py` _+7 more__
- **2026-05-16** [`4db300e95f`](https://github.com/vllm-project/vllm/commit/4db300e95f) [#42807](https://github.com/vllm-project/vllm/pull/42807)
  [ROCm][CI] Removed problematic command override mechanism (#42807)
  _Files: `.buildkite/scripts/hardware_ci/run-amd-test.sh`_
- **2026-05-15** [`bd9dbe6060`](https://github.com/vllm-project/vllm/commit/bd9dbe6060) [#42606](https://github.com/vllm-project/vllm/pull/42606)
  [ROCm][Bugfix] Fix fused_mla_dual_rms_norm for AITER API rename _fused_qk_rmsnorm (#42606)
  _Files: `vllm/_aiter_ops.py`, `vllm/compilation/passes/pass_manager.py`_
- **2026-05-15** [`4d67d3bde2`](https://github.com/vllm-project/vllm/commit/4d67d3bde2) [#42072](https://github.com/vllm-project/vllm/pull/42072)
  [ROCm] Restore fast top_k_per_row kernels for sparse MLA when topk_tokens=2048 (#42072)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-05-15** [`be7a03ea65`](https://github.com/vllm-project/vllm/commit/be7a03ea65) [#42409](https://github.com/vllm-project/vllm/pull/42409)
  [ROCm] Widen AITER fused AR RMSNorm 1-stage gate (#42409)
  _Files: `vllm/_aiter_ops.py`_
- **2026-05-15** [`46a95815d3`](https://github.com/vllm-project/vllm/commit/46a95815d3) [#42509](https://github.com/vllm-project/vllm/pull/42509)
  [ROCm][MLA] FP8 ASM prefill for AITER dense MLA backend on gfx950 (#42509)
  _Files: `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-05-15** [`d792d993c1`](https://github.com/vllm-project/vllm/commit/d792d993c1) [#37826](https://github.com/vllm-project/vllm/pull/37826)
  [ROCm] Widen OAI Triton MoE capability range to include gfx12 (RDNA4) (#37826)
  _Files: `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`_
- **2026-05-15** [`d735968f6d`](https://github.com/vllm-project/vllm/commit/d735968f6d) [#42025](https://github.com/vllm-project/vllm/pull/42025)
  [ROCm][CI] Stage B gating (#42025)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/kernels.yaml` _+1 more__
- **2026-05-15** [`ccde9540be`](https://github.com/vllm-project/vllm/commit/ccde9540be) [#42604](https://github.com/vllm-project/vllm/pull/42604)
  DeepSeekV4-Pro enable cuda graph full and piecewise mode (#42604)
  _Files: `vllm/model_executor/layers/mhc.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla_sparse_dsv4.py`_
- **2026-05-15** [`2676ab1e0b`](https://github.com/vllm-project/vllm/commit/2676ab1e0b) [#35024](https://github.com/vllm-project/vllm/pull/35024)
  [Deprecation] Remove old locations of `get_tokenizer` and `resolve_hf_chat_template` (#35024)
  _Files: `.buildkite/lm-eval-harness/run-lm-eval-chartqa-vllm-vlm-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-hf-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-gsm-vllm-baseline.sh`, `.buildkite/lm-eval-harness/run-lm-eval-mmlupro-vllm-baseline.sh` _+13 more__
- **2026-05-15** [`0d4d334eaa`](https://github.com/vllm-project/vllm/commit/0d4d334eaa) [#42150](https://github.com/vllm-project/vllm/pull/42150)
  Bump llguidance to 1.7 (#42150)
  _Files: `requirements/common.txt`, `requirements/test/rocm.txt`_
- **2026-05-15** [`fa2a33b893`](https://github.com/vllm-project/vllm/commit/fa2a33b893) [#38288](https://github.com/vllm-project/vllm/pull/38288)
  [Quant] Consolidate GPTQ: rename gptq_marlin.py to auto_gptq.py (#38288)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `tests/models/quantization/test_gptq_marlin.py`, `tests/quantization/test_auto_gptq.py`, `tests/quantization/test_configs.py` _+17 more__
- **2026-05-14** [`4cfcc0866f`](https://github.com/vllm-project/vllm/commit/4cfcc0866f) [#38680](https://github.com/vllm-project/vllm/pull/38680)
  [CI][ROCm] Remove unsupported cases in test_fusion.py (#38680)
  _Files: `tests/compile/passes/test_fuse_act_padding.py`, `tests/compile/passes/test_fusion.py`, `vllm/model_executor/layers/quantization/utils/fp8_utils.py`_
- **2026-05-14** [`f887aa1a53`](https://github.com/vllm-project/vllm/commit/f887aa1a53) [#40710](https://github.com/vllm-project/vllm/pull/40710)
  [Aiter][ROCm] RMSNormGated+GroupedQuantFP8 fusion (#40710)
  _Files: `tests/compile/passes/test_fusion.py`, `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/matcher_utils.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py` _+2 more__
- **2026-05-14** [`f07b1da797`](https://github.com/vllm-project/vllm/commit/f07b1da797) [#42062](https://github.com/vllm-project/vllm/pull/42062)
  [ROCm] Enable gluon paged MQA logits on gfx950 (MI355X) (#42062)
  _Files: `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py`_
- **2026-05-14** [`768f4a6f26`](https://github.com/vllm-project/vllm/commit/768f4a6f26) [#40857](https://github.com/vllm-project/vllm/pull/40857)
  [CI][AMD][BugFix] Prevent triton compiler error when running test_moe_layer with use_ep = True on ROCm (#40857)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-05-14** [`addef3299c`](https://github.com/vllm-project/vllm/commit/addef3299c) [#42126](https://github.com/vllm-project/vllm/pull/42126)
  [CI][AMD] Skip tests where models have problems or fails on both HW types (#42126)
  _Files: `tests/models/multimodal/generation/test_common.py`_
- **2026-05-14** [`ce29c26b31`](https://github.com/vllm-project/vllm/commit/ce29c26b31) [#40453](https://github.com/vllm-project/vllm/pull/40453)
  Update Dockerfile.rocm for AINIC & Thor NIC (#40453)
  _Files: `docker/Dockerfile.rocm`_
- **2026-05-14** [`fd7d858c8a`](https://github.com/vllm-project/vllm/commit/fd7d858c8a) [#42098](https://github.com/vllm-project/vllm/pull/42098)
  Use hidden_pad and intermediate_pad from vLLM #34301 (#42098)
  _Files: `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`_
- **2026-05-13** [`a8887c208f`](https://github.com/vllm-project/vllm/commit/a8887c208f) [#41946](https://github.com/vllm-project/vllm/pull/41946)
  [Bugfix] [ROCm] [DSV4] [Perf] Add aiter mhc support (#41946)
  _Files: `requirements/rocm.txt`, `tests/kernels/test_mhc_kernels.py`, `vllm/_aiter_ops.py`, `vllm/_tilelang_ops.py` _+8 more__
- **2026-05-13** [`0a62f5eec9`](https://github.com/vllm-project/vllm/commit/0a62f5eec9) [#42326](https://github.com/vllm-project/vllm/pull/42326)
  [AMD] skip machete tests for rocm (#42326)
  _Files: `tests/quantization/test_cutlass_w4a16.py`_
- **2026-05-13** [`d628a3c5cb`](https://github.com/vllm-project/vllm/commit/d628a3c5cb) [#41572](https://github.com/vllm-project/vllm/pull/41572)
  [ROCm][CI] Skip ROCm batch invalid-input test pending torch fix (#41572)
  _Files: `vllm/sampling_params.py`_
- **2026-05-13** [`74dffae666`](https://github.com/vllm-project/vllm/commit/74dffae666) [#42411](https://github.com/vllm-project/vllm/pull/42411)
  [ROCm] Run AITER RMSNorm pad fusion before AR RMS fusion (#42411)
  _Files: `vllm/compilation/passes/pass_manager.py`_

## MoE / Expert Parallel  (32 commits)

- **2026-05-20** [`5774aaed0c`](https://github.com/vllm-project/vllm/commit/5774aaed0c) [#43143](https://github.com/vllm-project/vllm/pull/43143)
  [Cohere] Enable Cohere MoE (#43143)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`_
- **2026-05-19** [`f54721bcc3`](https://github.com/vllm-project/vllm/commit/f54721bcc3) [#42976](https://github.com/vllm-project/vllm/pull/42976)
  [Bugfix][MoE] FlashInfer one-sided: workspace union across heterogeneous layers (#42976)
  _Files: `tests/distributed/test_mnnvl_alltoall.py`, `vllm/distributed/device_communicators/all2all.py`_
- **2026-05-19** [`b82e908b4c`](https://github.com/vllm-project/vllm/commit/b82e908b4c) [#42347](https://github.com/vllm-project/vllm/pull/42347)
  [Perf][4/n] Eliminate various GPU<->CPU syncs (#42347)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/lora/ops/triton_ops/utils.py`, `vllm/lora/punica_wrapper/utils.py`, `vllm/model_executor/models/bert.py` _+19 more__
- **2026-05-19** [`8f16c4a5c0`](https://github.com/vllm-project/vllm/commit/8f16c4a5c0) [#42468](https://github.com/vllm-project/vllm/pull/42468)
  [BugFix][CPU][Spec Decode] Fix Eagle implementation on CPU backend (#42468)
  _Files: `vllm/v1/sample/ops/topk_topp_sampler.py`, `vllm/v1/worker/cpu_model_runner.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-18** [`00e20e76f7`](https://github.com/vllm-project/vllm/commit/00e20e76f7) [#42767](https://github.com/vllm-project/vllm/pull/42767)
  [Refactor] Remove dead cuda kernels (#42767)
  _Files: `CMakeLists.txt`, `csrc/attention/vertical_slash_index.cu`, `csrc/moe/torch_bindings.cpp`, `csrc/ops.h` _+2 more__
- **2026-05-18** [`6859ca7615`](https://github.com/vllm-project/vllm/commit/6859ca7615) [#42541](https://github.com/vllm-project/vllm/pull/42541)
  [Bugfix] fix swiglu limit issue for humming backend + deepseek v4 (#42541)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/utils/humming_utils.py`_
- **2026-05-18** [`8c296de63b`](https://github.com/vllm-project/vllm/commit/8c296de63b) [#42857](https://github.com/vllm-project/vllm/pull/42857)
  [Perf] Re-enable flashinfer autotune by default and cleanup (#42857)
  _Files: `vllm/config/vllm.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`, `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/warmup/kernel_warmup.py` _+1 more__
- **2026-05-18** [`78e7a7b9b0`](https://github.com/vllm-project/vllm/commit/78e7a7b9b0) [#42483](https://github.com/vllm-project/vllm/pull/42483)
  Refactor AWQ Marlin MoE onto modular WNA16 oracle (#42483)
  _Files: `tests/kernels/moe/test_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/int_wna16.py` _+2 more__
- **2026-05-18** [`2e40faf08b`](https://github.com/vllm-project/vllm/commit/2e40faf08b) [#42954](https://github.com/vllm-project/vllm/pull/42954)
  [XPU][CI] Temporarily skip test_moe_lora_align_block_size_mixed_base_and_lora[1] in Intel GPU CI (#42954)
  _Files: `.buildkite/intel_jobs/lora_intel.yaml`_
- **2026-05-18** [`88a860d754`](https://github.com/vllm-project/vllm/commit/88a860d754) [#41922](https://github.com/vllm-project/vllm/pull/41922)
  [CPU] Add MXFP4 W4A16 MoE support (#41922)
  _Files: `.buildkite/hardware_tests/cpu.yaml`, `csrc/cpu/sgl-kernels/common.h`, `csrc/cpu/sgl-kernels/gemm.h`, `csrc/cpu/sgl-kernels/gemm_fp8.cpp` _+12 more__
- **2026-05-18** [`2267f70070`](https://github.com/vllm-project/vllm/commit/2267f70070) [#42527](https://github.com/vllm-project/vllm/pull/42527)
  [Kernel] Pack topk id/weights triton kernel (#42527)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`, `vllm/model_executor/layers/fused_moe/utils.py`_
- **2026-05-18** [`7d5b033782`](https://github.com/vllm-project/vllm/commit/7d5b033782) [#42242](https://github.com/vllm-project/vllm/pull/42242)
  [LoRA] Support 2D and 3D MoE LoRA adapter  at the same time (#42242)
  _Files: `docs/features/lora.md`, `tests/lora/conftest.py`, `tests/lora/test_qwen36_moe_lora.py`, `tests/lora/test_qwen3moe_tp.py` _+12 more__
- **2026-05-18** [`e3aeee5ff8`](https://github.com/vllm-project/vllm/commit/e3aeee5ff8) [#40131](https://github.com/vllm-project/vllm/pull/40131)
  [Bugfix] moe lora align kernel grid (#40131)
  _Files: `csrc/moe/moe_align_sum_kernels.cu`, `tests/lora/test_moe_lora_align_sum.py`_
- **2026-05-18** [`03ddc1c9bc`](https://github.com/vllm-project/vllm/commit/03ddc1c9bc) [#42497](https://github.com/vllm-project/vllm/pull/42497)
  [Perf] Wire silu_and_mul_per_block_quant into TritonFP8MoE (MiniMax-M2)  (#42497)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-05-17** [`a94189295b`](https://github.com/vllm-project/vllm/commit/a94189295b) [#42716](https://github.com/vllm-project/vllm/pull/42716)
  Fix Weight loading for  Qwen3.5-MTP and Qwen3-VL using runai_streamer (#42716)
  _Files: `vllm/model_executor/models/qwen3_5_mtp.py`, `vllm/model_executor/models/qwen3_vl_moe.py`_
- **2026-05-16** [`0867497368`](https://github.com/vllm-project/vllm/commit/0867497368) [#41711](https://github.com/vllm-project/vllm/pull/41711)
  [CI/Build] Bump flashinfer to v0.6.11.post2 (#41711)
  _Files: `docker/Dockerfile`, `docker/Dockerfile.nightly_torch`, `docker/versions.json`, `requirements/cuda.txt` _+2 more__
- **2026-05-16** [`32b7177909`](https://github.com/vllm-project/vllm/commit/32b7177909) [#42757](https://github.com/vllm-project/vllm/pull/42757)
  [LoRA][Bugfix] Dedup LoRA wrapping for modules referenced from multiple attribute paths (MoE gate) (#42757)
  _Files: `tests/lora/test_lora_manager.py`, `vllm/lora/model_manager.py`_
- **2026-05-15** [`06d020bb6e`](https://github.com/vllm-project/vllm/commit/06d020bb6e) [#35568](https://github.com/vllm-project/vllm/pull/35568)
  [Bugfix] Fix SM121 (DGX Spark) exclusion from Marlin/CUTLASS FP8 paths (#35568)
  _Files: `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm.cuh`, `csrc/libtorch_stable/quantization/w8a8/cutlass/c3x/scaled_mm_sm120_fp8_dispatch.cuh`, `csrc/moe/marlin_moe_wna16/generate_kernels.py`, `csrc/moe/marlin_moe_wna16/ops.cu` _+4 more__
- **2026-05-15** [`31fa757cf9`](https://github.com/vllm-project/vllm/commit/31fa757cf9) [#42306](https://github.com/vllm-project/vllm/pull/42306)
  [Misc] Make it simpler to replace out-of-tree layer classes with related LoRA layers. (#42306)
  _Files: `vllm/lora/layers/column_parallel_linear.py`, `vllm/lora/layers/fused_moe.py`_
- **2026-05-14** [`f8848b2f2d`](https://github.com/vllm-project/vllm/commit/f8848b2f2d) [#41986](https://github.com/vllm-project/vllm/pull/41986)
  [Bugfix] Add swiglu limits to deepgemm fp8 methods (#41986)
  _Files: `tests/kernels/moe/test_silu_mul_per_token_group_quant_fp8_colmajor.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/deep_gemm_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py` _+9 more__
- **2026-05-14** [`c7560af424`](https://github.com/vllm-project/vllm/commit/c7560af424) [#39568](https://github.com/vllm-project/vllm/pull/39568)
  [RFC] Replace shared-memory routed experts with ModelRunnerOutput transfer and HTTP support (#39568)
  _Files: `tests/model_executor/test_routed_experts_capture.py`, `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `vllm/config/vllm.py` _+8 more__
- **2026-05-14** [`6548560496`](https://github.com/vllm-project/vllm/commit/6548560496) [#41261](https://github.com/vllm-project/vllm/pull/41261)
  [Compile] Fix compile warning with topk softplus sqrt (#41261)
  _Files: `csrc/moe/topk_softplus_sqrt_kernels.cu`_
- **2026-05-14** [`0a65d46628`](https://github.com/vllm-project/vllm/commit/0a65d46628) [#41263](https://github.com/vllm-project/vllm/pull/41263)
  [DSV4]   Fuse norm and router for low latency scenario (#41263)
  _Files: `CMakeLists.txt`, `benchmarks/kernels/benchmark_norm_router_gemm.py`, `csrc/moe/dsv4_norm_router_gemm.h`, `csrc/moe/dsv4_norm_router_gemm_entry.cu` _+7 more__
- **2026-05-14** [`8c79ad6580`](https://github.com/vllm-project/vllm/commit/8c79ad6580) [#39917](https://github.com/vllm-project/vllm/pull/39917)
  Revert "[Core] Replace routing replay with device cache and async D2H pipeline" (#39917) (#42434)
  _Files: `docs/training/routed_experts_replay.md`, `tests/model_executor/test_routed_experts_capture.py`, `vllm/config/vllm.py`, `vllm/entrypoints/openai/chat_completion/protocol.py` _+11 more__
- **2026-05-14** [`751b9f14bd`](https://github.com/vllm-project/vllm/commit/751b9f14bd) [#41918](https://github.com/vllm-project/vllm/pull/41918)
  [XPU][CT] Support mxfp8 moe model (#41918)
  _Files: `vllm/model_executor/layers/fused_moe/experts/xpu_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`_
- **2026-05-13** [`8efd508204`](https://github.com/vllm-project/vllm/commit/8efd508204) [#41566](https://github.com/vllm-project/vllm/pull/41566)
  [Quantization] Rework quantization_config to use QuantKey and allow for activation override (#41566)
  _Files: `docs/features/quantization/online.md`, `tests/compile/fusions_e2e/conftest.py`, `tests/compile/fusions_e2e/models.py`, `tests/evals/gpt_oss/configs/gpt-oss-20b-flashinfer-mxfp4-mxfp8-cutlass.yaml` _+12 more__
- **2026-05-13** [`3f611f6106`](https://github.com/vllm-project/vllm/commit/3f611f6106) [#42563](https://github.com/vllm-project/vllm/pull/42563)
  [CI] Fix pre-commit issue (#42563)
  _Files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`_
- **2026-05-13** [`40330967ab`](https://github.com/vllm-project/vllm/commit/40330967ab) [#35859](https://github.com/vllm-project/vllm/pull/35859)
  [Quark] Support loading Quark NVFP4 checkpoints in vLLM (#35859)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/quark/quark.py`, `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/model_executor/layers/quantization/quark/schemes/__init__.py` _+2 more__
- **2026-05-13** [`5794c65f8c`](https://github.com/vllm-project/vllm/commit/5794c65f8c) [#42250](https://github.com/vllm-project/vllm/pull/42250)
  [Bugfix][Model] Gemma4 MoE routing closure captures per_expert_scale, breaking functional_call substitution (#42250)
  _Files: `vllm/model_executor/models/gemma4.py`_
- **2026-05-13** [`3b1ef03be4`](https://github.com/vllm-project/vllm/commit/3b1ef03be4) [#41892](https://github.com/vllm-project/vllm/pull/41892)
  [Bugfix][Quark] Fix W8A8 INT8 garbage outputs on Step-3.5-Flash (and other 3-key fused-MoE Quark exports) (#41892)
  _Files: `vllm/model_executor/layers/quantization/quark/quark_moe.py`, `vllm/model_executor/layers/quantization/quark/schemes/quark_w8a8_int8.py`, `vllm/model_executor/models/step3p5.py`_
- **2026-05-13** [`cee6751e54`](https://github.com/vllm-project/vllm/commit/cee6751e54) [#42394](https://github.com/vllm-project/vllm/pull/42394)
  [Bugfix][Qwen3-VL] Fix pipeline-parallel deepstack initialization (#42394)
  _Files: `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl_moe.py`_
- **2026-05-13** [`18f6bf5a21`](https://github.com/vllm-project/vllm/commit/18f6bf5a21) [#41299](https://github.com/vllm-project/vllm/pull/41299)
  [MoE Refactor] Add sequence parallel tests to test_moe_layer.py (#41299)
  _Files: `tests/kernels/moe/test_moe_layer.py`, `vllm/distributed/device_communicators/all2all.py`, `vllm/distributed/device_communicators/cuda_communicator.py`, `vllm/model_executor/layers/fused_moe/prepare_finalize/flashinfer_nvlink_two_sided.py`_

## Attention  (31 commits)

- **2026-05-20** [`c628a93a64`](https://github.com/vllm-project/vllm/commit/c628a93a64) [#40727](https://github.com/vllm-project/vllm/pull/40727)
  [Perf][Bugfix] Update dflash aux layer indexing (#40727)
  _Files: `tests/v1/e2e/spec_decode/test_spec_decode.py`, `vllm/transformers_utils/configs/speculators/algos.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-19** [`9aaf83ef50`](https://github.com/vllm-project/vllm/commit/9aaf83ef50) [#43119](https://github.com/vllm-project/vllm/pull/43119)
  [CI failure] Temporarily disable using persistent cache for flashinfer autotune (#43119)
  _Files: `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-05-19** [`d247a931cc`](https://github.com/vllm-project/vllm/commit/d247a931cc) [#42080](https://github.com/vllm-project/vllm/pull/42080)
  [feat] Add FP8 per-tensor Q scale support to Triton attention backend (#42080)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-05-19** [`d740e2c029`](https://github.com/vllm-project/vllm/commit/d740e2c029) [#43043](https://github.com/vllm-project/vllm/pull/43043)
  [XPU] update xpu graph usage (#43043)
  _Files: `vllm/distributed/device_communicators/xpu_communicator.py`, `vllm/distributed/parallel_state.py`, `vllm/platforms/xpu.py`, `vllm/v1/attention/backends/flash_attn.py`_
- **2026-05-19** [`ef54a4d604`](https://github.com/vllm-project/vllm/commit/ef54a4d604) [#43046](https://github.com/vllm-project/vllm/pull/43046)
  [Misc][MM] Remove redundant code in CLIPAttention (#43046)
  _Files: `vllm/model_executor/models/clip.py`_
- **2026-05-19** [`3ca8db2ef8`](https://github.com/vllm-project/vllm/commit/3ca8db2ef8) [#42899](https://github.com/vllm-project/vllm/pull/42899)
  add cutedsl dsv4 indexer fp8 kernel (#42899)
  _Files: `tests/kernels/test_fused_indexer_q_rope_quant.py`, `vllm/v1/attention/ops/deepseek_v4_ops/cutedsl_utils.py`, `vllm/v1/attention/ops/deepseek_v4_ops/fused_indexer_q.py`, `vllm/v1/attention/ops/deepseek_v4_ops/fused_indexer_q_cutedsl.py`_
- **2026-05-19** [`da03e549b3`](https://github.com/vllm-project/vllm/commit/da03e549b3) [#42537](https://github.com/vllm-project/vllm/pull/42537)
  [UX] Add a persistent cache for FlashInfer autotuning (#42537)
  _Files: `docs/usage/security.md`, `tests/model_executor/test_flashinfer_autotune_cache.py`, `vllm/envs.py`, `vllm/model_executor/warmup/kernel_warmup.py`_
- **2026-05-18** [`37ece593c1`](https://github.com/vllm-project/vllm/commit/37ece593c1) [#42774](https://github.com/vllm-project/vllm/pull/42774)
  [Perf] Padded nvfp4 quant kernel to remove additional copy, 2.4%~5.7% e2e performance improvement (#42774)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_quant_kernels.cu`, `tests/kernels/quantization/test_nvfp4_quant.py`, `vllm/_custom_ops.py`, `vllm/model_executor/kernels/linear/nvfp4/cutlass.py` _+1 more__
- **2026-05-18** [`0191354827`](https://github.com/vllm-project/vllm/commit/0191354827) [#42885](https://github.com/vllm-project/vllm/pull/42885)
  [Perf][MLA] Enable FULL cudagraph capture for TRITON_MLA decode (#42885)
  _Files: `vllm/v1/attention/backends/mla/triton_mla.py`_
- **2026-05-18** [`47829b1159`](https://github.com/vllm-project/vllm/commit/47829b1159) [#42430](https://github.com/vllm-project/vllm/pull/42430)
  [Bugfix] mamba: run single-token extends as decodes (#42430)
  _Files: `tests/v1/attention/test_mamba_update_block_table.py`, `tests/v1/attention/utils.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `vllm/v1/attention/backends/mamba_attn.py`_
- **2026-05-18** [`737bfa3a43`](https://github.com/vllm-project/vllm/commit/737bfa3a43) [#41233](https://github.com/vllm-project/vllm/pull/41233)
  [Bugfix][Hybrid][NemotronH] Fix mamba_cache_mode=all + speculative decoding crash (#41233)
  _Files: `tests/v1/attention/test_mamba_update_block_table.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `vllm/model_executor/layers/mamba/mamba_mixer2.py`, `vllm/model_executor/models/config.py` _+6 more__
- **2026-05-18** [`df852ed503`](https://github.com/vllm-project/vllm/commit/df852ed503) [#41710](https://github.com/vllm-project/vllm/pull/41710)
  fix: remove unused norm for dpskv4 (#41710)
  _Files: `vllm/model_executor/layers/deepseek_v4_attention.py`_
- **2026-05-18** [`b4601ad43f`](https://github.com/vllm-project/vllm/commit/b4601ad43f) [#42707](https://github.com/vllm-project/vllm/pull/42707)
  [CPU] Add fused GDN support for AMX CPU platform (#42707)
  _Files: `csrc/cpu/sgl-kernels/conv.cpp`, `csrc/cpu/sgl-kernels/fla.cpp`, `csrc/cpu/torch_bindings.cpp`, `vllm/_custom_ops.py` _+4 more__
- **2026-05-18** [`965d076148`](https://github.com/vllm-project/vllm/commit/965d076148) [#42740](https://github.com/vllm-project/vllm/pull/42740)
  [CPU] Specify required KV cache layout for CPU attention backend (#42740)
  _Files: `vllm/v1/attention/backends/cpu_attn.py`_
- **2026-05-18** [`998714b21b`](https://github.com/vllm-project/vllm/commit/998714b21b) [#42849](https://github.com/vllm-project/vllm/pull/42849)
  [Perf] Add do_not_specialize in fused FP8 RoPE kernel (#42849)
  _Files: `vllm/v1/attention/ops/deepseek_v4_ops/fused_inv_rope_fp8_quant.py`_
- **2026-05-16** [`852f567444`](https://github.com/vllm-project/vllm/commit/852f567444) [#42782](https://github.com/vllm-project/vllm/pull/42782)
  [Bugfix] Respect explicit --kv-cache-dtype over checkpoint kv_cache_scheme (#42782)
  _Files: `vllm/model_executor/layers/attention/attention.py`_
- **2026-05-15** [`b2c58ee942`](https://github.com/vllm-project/vllm/commit/b2c58ee942) [#42685](https://github.com/vllm-project/vllm/pull/42685)
  [FlashAttn] Fix supports_kv_cache_dtype() accepting unhandled fp8 kv-cache dtype variants (#42685)
  _Files: `tests/kernels/attention/test_attention_selector.py`, `tests/models/quantization/test_fp8.py`, `tools/pre_commit/generate_attention_backend_docs.py`, `vllm/v1/attention/backends/fa_utils.py` _+2 more__
- **2026-05-15** [`ee58665aac`](https://github.com/vllm-project/vllm/commit/ee58665aac) [#42135](https://github.com/vllm-project/vllm/pull/42135)
  [Bugfix] Fix DeepGEMM context lens contiguity in MLA indexer (#42135)
  _Files: `vllm/v1/attention/backends/mla/indexer.py`_
- **2026-05-15** [`491e8d8539`](https://github.com/vllm-project/vllm/commit/491e8d8539) [#42561](https://github.com/vllm-project/vllm/pull/42561)
  [Perf] Optimize MLA attention `_v_up_proj` bmm by removing additional copy (#42561)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-05-15** [`0fe7550254`](https://github.com/vllm-project/vllm/commit/0fe7550254) [#42692](https://github.com/vllm-project/vllm/pull/42692)
  [Bugfix] DFlash FP8 KV-Cache (#42692)
  _Files: `vllm/model_executor/models/qwen3_dflash.py`, `vllm/v1/spec_decode/llm_base_proposer.py`_
- **2026-05-15** [`f351455f0f`](https://github.com/vllm-project/vllm/commit/f351455f0f) [#40119](https://github.com/vllm-project/vllm/pull/40119)
  [CPU][RISC-V] Add RVV-optimized attention kernels for RISC-V Vector Extension (#40119)
  _Files: `benchmarks/kernels/cpu/benchmark_cpu_attn.py`, `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_arch_macros.h`, `csrc/cpu/cpu_attn.cpp` _+7 more__
- **2026-05-14** [`3b6a204789`](https://github.com/vllm-project/vllm/commit/3b6a204789) [#42444](https://github.com/vllm-project/vllm/pull/42444)
  [Model Runner V2][Bug Fix][DSV4] Ensure lazy attention state initializations happen during cudagraph capture (#42444)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_
- **2026-05-14** [`9898f94abe`](https://github.com/vllm-project/vllm/commit/9898f94abe) [#42555](https://github.com/vllm-project/vllm/pull/42555)
  [Attention] Remove deprecated MLA prefill arguments (#42555)
  _Files: `benchmarks/attention_benchmarks/mla_runner.py`, `tests/engine/test_arg_utils.py`, `tests/v1/attention/test_mla_prefill_selector.py`, `vllm/config/attention.py` _+1 more__
- **2026-05-14** [`ae4f59f0ec`](https://github.com/vllm-project/vllm/commit/ae4f59f0ec) [#39337](https://github.com/vllm-project/vllm/pull/39337)
  [Model Runner v2] Oracle for model runner v2 - qwen3 dense model by default [1/N] (#39337)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`, `vllm/envs.py`, `vllm/v1/attention/backends/flashinfer.py` _+2 more__
- **2026-05-14** [`2317682f95`](https://github.com/vllm-project/vllm/commit/2317682f95) [#42112](https://github.com/vllm-project/vllm/pull/42112)
  [Bugfix] Fix TRTLLM ragged MLA prefill workspace warmup (#42112)
  _Files: `vllm/v1/attention/backends/mla/prefill/flashinfer.py`, `vllm/v1/attention/backends/mla/prefill/trtllm_ragged.py`_
- **2026-05-14** [`0d2732dd91`](https://github.com/vllm-project/vllm/commit/0d2732dd91) [#41778](https://github.com/vllm-project/vllm/pull/41778)
  [MLA Attention Backend] Add TOKENSPEED_MLA backend for DSR1/Kimi K25 prefill + decode on Blackwell (#41778)
  _Files: `benchmarks/attention_benchmarks/configs/mla_decode.yaml`, `benchmarks/attention_benchmarks/configs/mla_prefill.yaml`, `benchmarks/attention_benchmarks/mla_runner.py`, `docs/design/attention_backends.md` _+10 more__
- **2026-05-13** [`6b5c389ee3`](https://github.com/vllm-project/vllm/commit/6b5c389ee3) [#41252](https://github.com/vllm-project/vllm/pull/41252)
  expose flex block size for batch invariant mode (#41252)
  _Files: `tests/v1/determinism/test_batch_invariance.py`, `vllm/config/attention.py`, `vllm/model_executor/layers/attention/attention.py`, `vllm/v1/attention/backends/flex_attention.py`_
- **2026-05-13** [`2f821faeae`](https://github.com/vllm-project/vllm/commit/2f821faeae) [#39949](https://github.com/vllm-project/vllm/pull/39949)
  [Spec Decode] Support hybrid attention models in extract_hidden_states (#39949)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/kv_connector/extract_hidden_states_integration/test_extraction.py`, `tests/v1/kv_connector/unit/test_decode_bench_connector.py`, `tests/v1/kv_connector/unit/test_kv_connector_lifecycle.py` _+10 more__
- **2026-05-13** [`3c413a5481`](https://github.com/vllm-project/vllm/commit/3c413a5481) [#40327](https://github.com/vllm-project/vllm/pull/40327)
  Triton attention: add USE_TD constexpr for tensor descriptor Q/K/V load/store (#40327)
  _Files: `tests/kernels/attention/test_triton_unified_attention.py`, `vllm/envs.py`, `vllm/v1/attention/backends/triton_attn.py`, `vllm/v1/attention/ops/triton_unified_attention.py`_
- **2026-05-13** [`85b2fecab7`](https://github.com/vllm-project/vllm/commit/85b2fecab7) [#42339](https://github.com/vllm-project/vllm/pull/42339)
  [5/n] Migrate CUTLASS MLA, hadamard, awq, allspark and DSV3 fused a gemm to torch stable ABI (continued) (#42339)
  _Files: `CMakeLists.txt`, `csrc/core/scalar_type.hpp`, `csrc/libtorch_stable/attention/mla/cutlass_sm100_mla/device/sm100_mla.hpp`, `csrc/libtorch_stable/attention/mla/cutlass_sm100_mla/kernel/sm100_fmha_mla_reduction.hpp` _+16 more__
- **2026-05-13** [`dcacdf9a88`](https://github.com/vllm-project/vllm/commit/dcacdf9a88) [#41052](https://github.com/vllm-project/vllm/pull/41052)
  [Attention] Sync FA with upstream (#41052)
  _Files: `cmake/external_projects/vllm_flash_attn.cmake`_

## Other  (28 commits)

- **2026-05-20** [`73dd2f33b7`](https://github.com/vllm-project/vllm/commit/73dd2f33b7) [#43121](https://github.com/vllm-project/vllm/pull/43121)
  [bug] fix WeightTransferConfig.backend to allow for all strings (#43121)
  _Files: `tests/distributed/test_weight_transfer.py`, `vllm/config/weight_transfer.py`_
- **2026-05-19** [`42b4f1fdf7`](https://github.com/vllm-project/vllm/commit/42b4f1fdf7) [#43025](https://github.com/vllm-project/vllm/pull/43025)
  [Refactor] Extract extract_types_from_schema utility from Minimax M2 tool parser (#43025)
  _Files: `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-05-19** [`4a4fdabe28`](https://github.com/vllm-project/vllm/commit/4a4fdabe28) [#43041](https://github.com/vllm-project/vllm/pull/43041)
  [Misc] Aligning tokwise pooler heads for consistency (#43041)
  _Files: `vllm/model_executor/layers/pooler/seqwise/poolers.py`, `vllm/model_executor/layers/pooler/tokwise/__init__.py`, `vllm/model_executor/layers/pooler/tokwise/heads.py`, `vllm/model_executor/layers/pooler/tokwise/poolers.py`_
- **2026-05-19** [`f1e3f0e6d6`](https://github.com/vllm-project/vllm/commit/f1e3f0e6d6) [#41354](https://github.com/vllm-project/vllm/pull/41354)
  [XPU] Use custom op collective behavior  (#41354)
  _Files: `vllm/platforms/xpu.py`_
- **2026-05-19** [`27f4ba9481`](https://github.com/vllm-project/vllm/commit/27f4ba9481) [#42671](https://github.com/vllm-project/vllm/pull/42671)
  fix: use keyword arguments for shard_id and expert_id in weight_loade… (#42671)
- **2026-05-18** [`57fef4e0bf`](https://github.com/vllm-project/vllm/commit/57fef4e0bf) [#43006](https://github.com/vllm-project/vllm/pull/43006)
  [Refactor] Extract shared coerce_to_schema_type utility from Minimax M2 tool parser (#43006)
  _Files: `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-05-18** [`84747489de`](https://github.com/vllm-project/vllm/commit/84747489de) [#42529](https://github.com/vllm-project/vllm/pull/42529)
  Tier offload followup (#42529)
  _Files: `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/cpu/spec.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/example/__init__.py` _+4 more__
- **2026-05-18** [`b12745e4f3`](https://github.com/vllm-project/vllm/commit/b12745e4f3) [#42935](https://github.com/vllm-project/vllm/pull/42935)
  Fix `--convert` passed without `--runner` on causal models (#42935)
  _Files: `vllm/config/model.py`_
- **2026-05-18** [`e26736973a`](https://github.com/vllm-project/vllm/commit/e26736973a) [#42778](https://github.com/vllm-project/vllm/pull/42778)
  [Model Runner V2] Fix prompt logprobs calculation `Sizes of tensors must match` error (#42778)
  _Files: `vllm/v1/worker/gpu/sample/prompt_logprob.py`_
- **2026-05-18** [`f5d3dc7115`](https://github.com/vllm-project/vllm/commit/f5d3dc7115) [#42783](https://github.com/vllm-project/vllm/pull/42783)
  [Model Runner v2] Support update_config (#42783)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-18** [`69c91d010a`](https://github.com/vllm-project/vllm/commit/69c91d010a) [#42955](https://github.com/vllm-project/vllm/pull/42955)
  [MRv2] Default to MRv1 when a connector is present (#42955)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`_
- **2026-05-18** [`cac81b6eda`](https://github.com/vllm-project/vllm/commit/cac81b6eda) [#42666](https://github.com/vllm-project/vllm/pull/42666)
  [CPU Backend] Improve cpu thread utilization (#42666)
  _Files: `csrc/cpu/cpu_attn_impl.hpp`, `vllm/utils/ompmultiprocessing.py`_
- **2026-05-17** [`1c8e9c0399`](https://github.com/vllm-project/vllm/commit/1c8e9c0399) [#42851](https://github.com/vllm-project/vllm/pull/42851)
  Refactor: Pass num_labels explicitly to PoolerClassify instead of reading from global config (#42851)
  _Files: `tests/model_executor/layers/test_pooler_activations.py`, `vllm/model_executor/layers/pooler/activations.py`_
- **2026-05-17** [`0fa888465e`](https://github.com/vllm-project/vllm/commit/0fa888465e) [#42725](https://github.com/vllm-project/vllm/pull/42725)
  [XPU] fix weight scale shape (#42725)
  _Files: `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-05-17** [`ff712f6447`](https://github.com/vllm-project/vllm/commit/ff712f6447) [#42710](https://github.com/vllm-project/vllm/pull/42710)
  [MRV2][XPU] add Model Runner V2 log (#42710)
  _Files: `vllm/v1/worker/xpu_worker.py`_
- **2026-05-17** [`504a26ce2b`](https://github.com/vllm-project/vllm/commit/504a26ce2b) [#41680](https://github.com/vllm-project/vllm/pull/41680)
  Support bf16 for mamba ssm cache (#41680)
  _Files: `vllm/config/cache.py`_
- **2026-05-16** [`787bc0d031`](https://github.com/vllm-project/vllm/commit/787bc0d031) [#42824](https://github.com/vllm-project/vllm/pull/42824)
  Add unit tests for pooler activation functions (#42824)
  _Files: `tests/model_executor/layers/test_pooler_activations.py`, `vllm/model_executor/layers/pooler/activations.py`_
- **2026-05-15** [`1ccdf87507`](https://github.com/vllm-project/vllm/commit/1ccdf87507) [#42481](https://github.com/vllm-project/vllm/pull/42481)
  [Bugfix] Fix layerwise reload alias-buffer corruption (#42481)
  _Files: `tests/model_executor/model_loader/test_reload.py`, `vllm/model_executor/model_loader/reload/layerwise.py`, `vllm/model_executor/model_loader/reload/meta.py`_
- **2026-05-15** [`6147c70224`](https://github.com/vllm-project/vllm/commit/6147c70224) [#42673](https://github.com/vllm-project/vllm/pull/42673)
  [Model Runner v2] Support reload weights (sleep mode) (#42673)
  _Files: `vllm/v1/worker/gpu/model_runner.py`_
- **2026-05-15** [`af9616d845`](https://github.com/vllm-project/vllm/commit/af9616d845) [#42676](https://github.com/vllm-project/vllm/pull/42676)
  [Model Runner V2] Fix kv_connector `pre_forward` order (#42676)
  _Files: `vllm/v1/worker/gpu/kv_connector.py`_
- **2026-05-15** [`95cfe102a5`](https://github.com/vllm-project/vllm/commit/95cfe102a5) [#42709](https://github.com/vllm-project/vllm/pull/42709)
  [Bugfix] Ensure embeding model compilation on CPU (#42709)
  _Files: `vllm/v1/worker/cpu_worker.py`_
- **2026-05-15** [`4b364f810e`](https://github.com/vllm-project/vllm/commit/4b364f810e) [#42258](https://github.com/vllm-project/vllm/pull/42258)
  [Core][DSV4] Skip caching SWA blocks that can never serve a prefix-cache hit (#42258)
  _Files: `tests/v1/core/test_prefix_caching.py`, `vllm/v1/core/block_pool.py`, `vllm/v1/core/kv_cache_coordinator.py`, `vllm/v1/core/single_type_kv_cache_manager.py`_
- **2026-05-15** [`27b85d2084`](https://github.com/vllm-project/vllm/commit/27b85d2084) [#42479](https://github.com/vllm-project/vllm/pull/42479)
  [Bugfix] Clarify CPU backend memory error messages reference shared flag (#42479)
  _Files: `vllm/v1/core/kv_cache_utils.py`, `vllm/v1/worker/cpu_worker.py`_
- **2026-05-15** [`bf610c2f56`](https://github.com/vllm-project/vllm/commit/bf610c2f56) [#41674](https://github.com/vllm-project/vllm/pull/41674)
  [Bugfix] Fix inverted condition causing thinking_token_budget to be silently ignored (#41674)
  _Files: `tests/v1/logits_processors/test_correctness.py`, `vllm/v1/worker/gpu_input_batch.py`_
- **2026-05-14** [`bf0d2dc6d7`](https://github.com/vllm-project/vllm/commit/bf0d2dc6d7) [#42441](https://github.com/vllm-project/vllm/pull/42441)
  [Misc] Fix mypy error in parser_manager type narrowing (#42441)
  _Files: `vllm/parser/parser_manager.py`_
- **2026-05-14** [`1087676a90`](https://github.com/vllm-project/vllm/commit/1087676a90) [#42570](https://github.com/vllm-project/vllm/pull/42570)
  [Refactor] Use shared utils in hermes tool parser (#42570)
  _Files: `vllm/tool_parsers/hermes_tool_parser.py`_
- **2026-05-14** [`63cc8a55a9`](https://github.com/vllm-project/vllm/commit/63cc8a55a9) [#39599](https://github.com/vllm-project/vllm/pull/39599)
  fix(tool-parser): preserve "none"/"nil" strings as valid enum values in minimax_m2 (#39599)
  _Files: `tests/tool_parsers/test_minimax_m2_tool_parser.py`, `vllm/tool_parsers/minimax_m2_tool_parser.py`_
- **2026-05-13** [`b2198670b1`](https://github.com/vllm-project/vllm/commit/b2198670b1) [#40789](https://github.com/vllm-project/vllm/pull/40789)
  [Bugfix] V1: support tuple model outputs in ubatch wrapper (dbo + spec decode) (#40789)
  _Files: `vllm/v1/worker/gpu_ubatch_wrapper.py`_

## Disaggregation / PD  (16 commits)

- **2026-05-19** [`aed2eb355a`](https://github.com/vllm-project/vllm/commit/aed2eb355a) [#42994](https://github.com/vllm-project/vllm/pull/42994)
  [Docs] Fix MooncakeStoreConnector role in disaggregated example (#42994)
  _Files: `docs/features/mooncake_store_connector_usage.md`_
- **2026-05-19** [`129019f334`](https://github.com/vllm-project/vllm/commit/129019f334) [#42677](https://github.com/vllm-project/vllm/pull/42677)
  [CI] Add MTP + PD disagg test for Qwen3.5 (#42677)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_spec_decode_test.sh`, `tests/v1/kv_connector/nixl_integration/spec_decode_acceptance_test.sh`, `tests/v1/kv_connector/nixl_integration/test_spec_decode_acceptance.py`_
- **2026-05-19** [`056bc2e166`](https://github.com/vllm-project/vllm/commit/056bc2e166) [#42828](https://github.com/vllm-project/vllm/pull/42828)
  [KVConnector][DSV4] HMA support for Mooncake store connector (#42828)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_connector.py`, `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `tests/v1/kv_connector/unit/test_mooncake_store_hma_e2e.py`, `tests/v1/kv_connector/unit/test_mooncake_store_scheduler.py` _+6 more__
- **2026-05-19** [`afd7b1dce9`](https://github.com/vllm-project/vllm/commit/afd7b1dce9) [#42926](https://github.com/vllm-project/vllm/pull/42926)
  [Bugfix] Use platform-agnostic device in example_connector load (#42926)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`_
- **2026-05-18** [`e5417657e5`](https://github.com/vllm-project/vllm/commit/e5417657e5) [#42611](https://github.com/vllm-project/vllm/pull/42611)
  [KV Connector][Offloading] Flush all pending jobs on last step (#42611)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_connector/unit/offloading_connector/utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-05-16** [`36e74c9ea4`](https://github.com/vllm-project/vllm/commit/36e74c9ea4) [#42689](https://github.com/vllm-project/vllm/pull/42689)
  [KV Connector] Support disk offloading in MooncakeStoreConnector (#42689)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/rdma_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py` _+1 more__
- **2026-05-16** [`657b42b592`](https://github.com/vllm-project/vllm/commit/657b42b592) [#42114](https://github.com/vllm-project/vllm/pull/42114)
  [Docker][KVConnector] Build mooncake-transfer-engine from source (#42114)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`_
- **2026-05-15** [`f45c210885`](https://github.com/vllm-project/vllm/commit/f45c210885) [#42596](https://github.com/vllm-project/vllm/pull/42596)
  [LMCacheMPConnector] Prioritize importing the lmcache_mp_connector from lmcache (#42596)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`_
- **2026-05-15** [`e0a45f1455`](https://github.com/vllm-project/vllm/commit/e0a45f1455) [#37476](https://github.com/vllm-project/vllm/pull/37476)
  [Feat][RL] IPC weight sync optimizations: multigpu support and chunked packed tensors (#37476)
  _Files: `docs/training/weight_transfer/ipc.md`, `examples/rl/rlhf_http_ipc.py`, `examples/rl/rlhf_ipc.py`, `examples/rl/rlhf_ipc_fsdp_ep.py` _+6 more__
- **2026-05-14** [`24337fb860`](https://github.com/vllm-project/vllm/commit/24337fb860) [#41869](https://github.com/vllm-project/vllm/pull/41869)
  PD disagg with NIXL Connector: GDN support (Qwen3.5) (#41869)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`, `tests/v1/kv_connector/unit/test_nixl_connector_hma.py` _+2 more__
- **2026-05-14** [`5bd8c71e79`](https://github.com/vllm-project/vllm/commit/5bd8c71e79) [#41956](https://github.com/vllm-project/vllm/pull/41956)
  [kv_offload] Implement `reset_cache()` for the offloading connector (#41956)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading_connector.py`, `vllm/v1/kv_offload/base.py` _+4 more__
- **2026-05-13** [`cca32d55a2`](https://github.com/vllm-project/vllm/commit/cca32d55a2) [#42542](https://github.com/vllm-project/vllm/pull/42542)
  [PD] Fix broken NIXL EP installation (#42542)
  _Files: `docker/Dockerfile`_
- **2026-05-13** [`79fd1bc7ed`](https://github.com/vllm-project/vllm/commit/79fd1bc7ed) [#42507](https://github.com/vllm-project/vllm/pull/42507)
  [kv_offload] Add req_id to ReqContext for per-request tracking (#42507)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`, `vllm/v1/kv_offload/base.py`_
- **2026-05-13** [`13bf242100`](https://github.com/vllm-project/vllm/commit/13bf242100) [#39654](https://github.com/vllm-project/vllm/pull/39654)
  [Feat][KVConnector] Add `bind_gpu_block_pool()` to KVConnectorBase_V1 (#39654)
  _Files: `tests/v1/kv_connector/unit/test_multi_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/base.py`, `vllm/distributed/kv_transfer/kv_connector/v1/multi_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py` _+1 more__
- **2026-05-13** [`71bcd02ef3`](https://github.com/vllm-project/vllm/commit/71bcd02ef3) [#39907](https://github.com/vllm-project/vllm/pull/39907)
  [Bugfix][PD] Fix multi-node TP (TP>8) (#39907)
  _Files: `tests/v1/kv_connector/unit/test_kv_connector_lifecycle.py`, `vllm/distributed/kv_transfer/kv_transfer_state.py`_
- **2026-05-13** [`07534b8782`](https://github.com/vllm-project/vllm/commit/07534b8782) [#42364](https://github.com/vllm-project/vllm/pull/42364)
  [PD] Bump NIXL connector dependency to 1.x (#42364)
  _Files: `.buildkite/ci_config.yaml`, `requirements/kv_connectors.txt`_

## Multimodal  (16 commits)

- **2026-05-19** [`1c6158083a`](https://github.com/vllm-project/vllm/commit/1c6158083a) [#42654](https://github.com/vllm-project/vllm/pull/42654)
  [Model] Openvla support (#42654)
  _Files: `docs/models/supported_models.md`, `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_openvla.py`, `tests/models/registry.py` _+7 more__
- **2026-05-19** [`9fd8487d2f`](https://github.com/vllm-project/vllm/commit/9fd8487d2f) [#42626](https://github.com/vllm-project/vllm/pull/42626)
  [Docs] Add SVG images for pooling models. (#42626)
  _Files: `docs/assets/models/pooling_models/cheat_sheet.svg`, `docs/assets/models/pooling_models/pooling_types.svg`, `docs/assets/models/pooling_models/score_types.svg`, `docs/models/pooling_models/README.md` _+1 more__
- **2026-05-19** [`6e889b582b`](https://github.com/vllm-project/vllm/commit/6e889b582b) [#43030](https://github.com/vllm-project/vllm/pull/43030)
  [ci] Route 28 gpu_1_queue tests to h200_35gb queue (#43030)
  _Files: `.buildkite/test_areas/engine.yaml`, `.buildkite/test_areas/entrypoints.yaml`, `.buildkite/test_areas/lm_eval.yaml`, `.buildkite/test_areas/lora.yaml` _+8 more__
- **2026-05-18** [`9758a6e5c5`](https://github.com/vllm-project/vllm/commit/9758a6e5c5) [#42819](https://github.com/vllm-project/vllm/pull/42819)
  [BugFix] support PP for Cohere vision model (#42819)
  _Files: `vllm/model_executor/models/cohere2_vision.py`_
- **2026-05-18** [`990f49bdcb`](https://github.com/vllm-project/vllm/commit/990f49bdcb) [#42224](https://github.com/vllm-project/vllm/pull/42224)
  [MM][CG] Enable encoder Cudagraph for Step3VL (#42224)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/interfaces.py` _+4 more__
- **2026-05-16** [`d1586e1a12`](https://github.com/vllm-project/vllm/commit/d1586e1a12) [#42830](https://github.com/vllm-project/vllm/pull/42830)
  Fix: Propagate pinned model revisions into Ultravox secondary weight loading (#42830)
  _Files: `vllm/model_executor/models/ultravox.py`_
- **2026-05-15** [`d0921bafef`](https://github.com/vllm-project/vllm/commit/d0921bafef) [#42706](https://github.com/vllm-project/vllm/pull/42706)
  [Bugfix] Unwrap VLM wrappers for EPLB on Model Runner V2 (#42706)
  _Files: `vllm/v1/worker/gpu/eplb_utils.py`_
- **2026-05-15** [`d26a28ab03`](https://github.com/vllm-project/vllm/commit/d26a28ab03) [#42616](https://github.com/vllm-project/vllm/pull/42616)
  fix: propagate revision/code_revision pins to all artifact boundaries (#42616)
  _Files: `tests/models/test_gguf_download.py`, `vllm/model_executor/model_loader/gguf_loader.py`, `vllm/model_executor/models/kimi_audio.py`, `vllm/model_executor/models/kimi_k25.py` _+2 more__
- **2026-05-14** [`f3d5360591`](https://github.com/vllm-project/vllm/commit/f3d5360591) [#42586](https://github.com/vllm-project/vllm/pull/42586)
  [Bugfix][Multimodal] PyAV video backend returns keyframes labeled as targets (#42586)
  _Files: `tests/multimodal/test_video.py`, `tests/multimodal/utils.py`, `vllm/multimodal/video.py`_
- **2026-05-14** [`77e1421a68`](https://github.com/vllm-project/vllm/commit/77e1421a68) [#39805](https://github.com/vllm-project/vllm/pull/39805)
  [Bugfix] Fix EPLB initialization for VLM wrapper models (#39805)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-14** [`70c00163ff`](https://github.com/vllm-project/vllm/commit/70c00163ff) [#42412](https://github.com/vllm-project/vllm/pull/42412)
  [Feature] Add instruction support for score/rerank chat templates (#42412)
  _Files: `examples/pooling/score/template/qwen3_reranker.jinja`, `examples/pooling/score/template/qwen3_vl_reranker.jinja`, `tests/entrypoints/pooling/scoring/test_cross_encoder_online_vision.py`, `vllm/entrypoints/pooling/scoring/io_processor.py` _+1 more__
- **2026-05-13** [`597ed13803`](https://github.com/vllm-project/vllm/commit/597ed13803) [#42535](https://github.com/vllm-project/vllm/pull/42535)
  [Core][MM] Do not use urllib3 to parse data URLs (#42535)
  _Files: `vllm/multimodal/media/connector.py`_
- **2026-05-13** [`b3c69595a6`](https://github.com/vllm-project/vllm/commit/b3c69595a6) [#41736](https://github.com/vllm-project/vllm/pull/41736)
  [MM][CG] Support ViT CG for Qwen2-VL (#41736)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/qwen2_vl.py`_
- **2026-05-13** [`67671692ac`](https://github.com/vllm-project/vllm/commit/67671692ac) [#42498](https://github.com/vllm-project/vllm/pull/42498)
  [CI] Re-enable Nemotron Parse parity test and switch testing to nemotron-parse v1.2 (#42498)
  _Files: `tests/conftest.py`, `tests/models/multimodal/generation/test_nemotron_parse.py`, `tests/models/registry.py`_
- **2026-05-13** [`16863072ca`](https://github.com/vllm-project/vllm/commit/16863072ca) [#42233](https://github.com/vllm-project/vllm/pull/42233)
  [Bugfix] Fix scipy audio resampling ratio (#42233)
  _Files: `tests/multimodal/test_audio.py`, `vllm/multimodal/audio.py`_
- **2026-05-13** [`92def124bc`](https://github.com/vllm-project/vllm/commit/92def124bc) [#42151](https://github.com/vllm-project/vllm/pull/42151)
  [MM][Perf][CG] Support ViT full CUDA graph for Qwen3.5 (#42151)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/qwen3_5.py`_

## Models  (11 commits)

- **2026-05-19** [`117afeea46`](https://github.com/vllm-project/vllm/commit/117afeea46) [#41277](https://github.com/vllm-project/vllm/pull/41277)
  Fix error in Dynamic NTK scaling (#41277)
  _Files: `tests/models/language/pooling/test_nomic_max_model_len.py`, `vllm/model_executor/layers/rotary_embedding/__init__.py`, `vllm/model_executor/layers/rotary_embedding/dynamic_ntk_scaling_rope.py`, `vllm/model_executor/models/config.py`_
- **2026-05-18** [`4a39b4f553`](https://github.com/vllm-project/vllm/commit/4a39b4f553) [#41154](https://github.com/vllm-project/vllm/pull/41154)
  [Model] Add Apertus Tool Parser (#41154)
  _Files: `docs/features/tool_calling.md`, `examples/tool_chat_template_apertus.jinja`, `tests/tool_parsers/test_apertus_tool_parser.py`, `vllm/tool_parsers/__init__.py` _+1 more__
- **2026-05-18** [`9537542537`](https://github.com/vllm-project/vllm/commit/9537542537) [#42923](https://github.com/vllm-project/vllm/pull/42923)
  Revert checkpoint specific workaround in Transformers modelling backend (#42923)
  _Files: `vllm/model_executor/models/transformers/base.py`_
- **2026-05-18** [`5ab6d1b3fd`](https://github.com/vllm-project/vllm/commit/5ab6d1b3fd) [#42311](https://github.com/vllm-project/vllm/pull/42311)
  [Model] [Perf] Use flatten for Qwen3.5's GDN output projection (#42311)
  _Files: `vllm/model_executor/layers/mamba/gdn_linear_attn.py`_
- **2026-05-15** [`1dc3fe08ea`](https://github.com/vllm-project/vllm/commit/1dc3fe08ea) [#42630](https://github.com/vllm-project/vllm/pull/42630)
  gemma3 multi-gpu bug-fix (#42630)
  _Files: `vllm/model_executor/models/gemma3n_mm.py`_
- **2026-05-15** [`56434e8651`](https://github.com/vllm-project/vllm/commit/56434e8651) [#42660](https://github.com/vllm-project/vllm/pull/42660)
  [Bugfix] Fix incorrect chat template format for Qwen3.5 (#42660)
  _Files: `tests/renderers/test_hf.py`, `vllm/renderers/hf.py`_
- **2026-05-14** [`b8a25d0e12`](https://github.com/vllm-project/vllm/commit/b8a25d0e12) [#42641](https://github.com/vllm-project/vllm/pull/42641)
  [Bugfix] Fix LM detection for Nemotron Parse (#42641)
  _Files: `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/nemotron_parse.py`_
- **2026-05-14** [`23c85343fb`](https://github.com/vllm-project/vllm/commit/23c85343fb) [#42342](https://github.com/vllm-project/vllm/pull/42342)
  [Bug] Fix DeepSeek V4 `AttributeError: module 'cutlass.cute.nvgpu' has no attribute 'LoadCacheMode'` (#42342)
  _Files: `requirements/cuda.txt`_
- **2026-05-14** [`ca60a4e84f`](https://github.com/vllm-project/vllm/commit/ca60a4e84f) [#42521](https://github.com/vllm-project/vllm/pull/42521)
  [Fix]  Weight loading for qwen3_5 using runai_streamer (#42521)
  _Files: `vllm/model_executor/models/qwen3_5.py`_
- **2026-05-14** [`665f9c4253`](https://github.com/vllm-project/vllm/commit/665f9c4253) [#42128](https://github.com/vllm-project/vllm/pull/42128)
  [Bugfix] Fix Gemma4ToolParser streaming float corruption (#42128)
  _Files: `tests/tool_parsers/test_gemma4_tool_parser.py`, `vllm/tool_parsers/gemma4_tool_parser.py`_
- **2026-05-13** [`f1cc7aad3c`](https://github.com/vllm-project/vllm/commit/f1cc7aad3c) [#42320](https://github.com/vllm-project/vllm/pull/42320)
  [Bugfix] Fix DeepSeek V4 MTP HC state handling (#42320)
  _Files: `vllm/model_executor/models/deepseek_v4.py`, `vllm/model_executor/models/deepseek_v4_mtp.py`_

## CI / Build  (11 commits)

- **2026-05-19** [`a65093c1a3`](https://github.com/vllm-project/vllm/commit/a65093c1a3) [#43129](https://github.com/vllm-project/vllm/pull/43129)
  [ci] Move language models tests (hybrid) back to L4 (#43129)
  _Files: `.buildkite/test_areas/models_language.yaml`_
- **2026-05-18** [`f85c76d701`](https://github.com/vllm-project/vllm/commit/f85c76d701) [#42991](https://github.com/vllm-project/vllm/pull/42991)
  [CI/Build] Bump nvidia-cutlass-dsl to 4.5.1 (#42991)
  _Files: `requirements/cuda.txt`_
- **2026-05-18** [`c38bed4248`](https://github.com/vllm-project/vllm/commit/c38bed4248) [#42582](https://github.com/vllm-project/vllm/pull/42582)
  delete xpu ci (#42582)
  _Files: `.buildkite/hardware_tests/intel.yaml`, `.buildkite/scripts/hardware_ci/run-xpu-test.sh`_
- **2026-05-18** [`107210442d`](https://github.com/vllm-project/vllm/commit/107210442d) [#42567](https://github.com/vllm-project/vllm/pull/42567)
  [CI] Add NIXL EP import canary (#42567)
  _Files: `tests/v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_nixl_imports.py`_
- **2026-05-15** [`de2d76f352`](https://github.com/vllm-project/vllm/commit/de2d76f352) [#41668](https://github.com/vllm-project/vllm/pull/41668)
  [Build] Switch CUDA 12.9 wheel builds to PyTorch manylinux_2_28 base (#41668)
  _Files: `.buildkite/release-pipeline.yaml`_
- **2026-05-15** [`e30f39c4f1`](https://github.com/vllm-project/vllm/commit/e30f39c4f1) [#42607](https://github.com/vllm-project/vllm/pull/42607)
  Update Intel Xeon model list and vLLM Benchmark Suite BKMs (#42607)
  _Files: `.buildkite/performance-benchmarks/tests/serving-tests-cpu-text.json`, `docs/models/hardware_supported_models/cpu.md`_
- **2026-05-14** [`b26558d4a3`](https://github.com/vllm-project/vllm/commit/b26558d4a3) [#42598](https://github.com/vllm-project/vllm/pull/42598)
  [CI][XPU] skip ut of offload connector (#42598)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`_
- **2026-05-13** [`ca7e4546da`](https://github.com/vllm-project/vllm/commit/ca7e4546da) [#42104](https://github.com/vllm-project/vllm/pull/42104)
  [CI] set max transformers version for skywork model (#42104)
  _Files: `tests/models/registry.py`_
- **2026-05-13** [`e35c0d4c63`](https://github.com/vllm-project/vllm/commit/e35c0d4c63) [#42456](https://github.com/vllm-project/vllm/pull/42456)
  [Feature] Support compile mode for batch invariance on SM80 (#42456)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/determinism/test_batch_invariance.py`_
- **2026-05-13** [`f6e868fbdf`](https://github.com/vllm-project/vllm/commit/f6e868fbdf) [#42470](https://github.com/vllm-project/vllm/pull/42470)
  [CI] Use uv with Python 3.12 for PyPI wheel upload (#42470)
  _Files: `.buildkite/scripts/upload-release-wheels-pypi.sh`_
- **2026-05-13** [`140dc2ec30`](https://github.com/vllm-project/vllm/commit/140dc2ec30) [#42438](https://github.com/vllm-project/vllm/pull/42438)
  [Bugfix] Install nvidia-cutlass-dsl[cu13] extra on CUDA 13 platforms (#42438)
  _Files: `.github/workflows/scripts/build.sh`, `docker/Dockerfile`, `requirements/cuda.txt`, `setup.py`_

## Quantization  (10 commits)

- **2026-05-19** [`8200fbe1ac`](https://github.com/vllm-project/vllm/commit/8200fbe1ac) [#42540](https://github.com/vllm-project/vllm/pull/42540)
  [Misc] add humming to dependencies (#42540)
  _Files: `requirements/cuda.txt`, `setup.py`, `vllm/model_executor/layers/quantization/humming.py`_
- **2026-05-19** [`36dcaf25d8`](https://github.com/vllm-project/vllm/commit/36dcaf25d8) [#37844](https://github.com/vllm-project/vllm/pull/37844)
  [XPU] add gptq(int4) support (#37844)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/kernels/linear/mixed_precision/MPLinearKernel.py`, `vllm/model_executor/kernels/linear/mixed_precision/xpu.py`, `vllm/model_executor/layers/quantization/utils/marlin_utils.py`_
- **2026-05-18** [`cd49a05d5a`](https://github.com/vllm-project/vllm/commit/cd49a05d5a) [#42889](https://github.com/vllm-project/vllm/pull/42889)
  [Refactor] Remove dead code (#42889)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/__init__.py`, `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_24.py`, `vllm/model_executor/layers/quantization/schema.py` _+1 more__
- **2026-05-18** [`ce88f01c9a`](https://github.com/vllm-project/vllm/commit/ce88f01c9a) [#41666](https://github.com/vllm-project/vllm/pull/41666)
  [Docs] update attribution to reflect EDEN foundation (#41666)
  _Files: `vllm/model_executor/layers/quantization/turboquant/__init__.py`, `vllm/model_executor/layers/quantization/turboquant/config.py`_
- **2026-05-18** [`23c15acd77`](https://github.com/vllm-project/vllm/commit/23c15acd77) [#42869](https://github.com/vllm-project/vllm/pull/42869)
  [BugFix] Kimi-K2.5: skip vision tower dtype conversion when using quantization (#42869)
  _Files: `vllm/model_executor/models/kimi_k25.py`_
- **2026-05-16** [`b2a27b82d9`](https://github.com/vllm-project/vllm/commit/b2a27b82d9) [#39538](https://github.com/vllm-project/vllm/pull/39538)
  [Kernel][UX] Add `--linear-backend` arg for linear kernel selection (#39538)
  _Files: `tests/models/quantization/test_nvfp4.py`, `vllm/config/kernel.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-05-14** [`1ea9401364`](https://github.com/vllm-project/vllm/commit/1ea9401364) [#39778](https://github.com/vllm-project/vllm/pull/39778)
  [Quantization][Autoround][Toolkit] Add W4A16 Support (#39778)
  _Files: `requirements/xpu.txt`, `vllm/model_executor/layers/quantization/inc.py`_
- **2026-05-14** [`9946c38b7f`](https://github.com/vllm-project/vllm/commit/9946c38b7f) [#41689](https://github.com/vllm-project/vllm/pull/41689)
  [XPU] Fix double-transpose in XPUFP8ScaledMMLinearKernel for W8A8 quant method (#41689)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`_
- **2026-05-13** [`0ddaf6dffa`](https://github.com/vllm-project/vllm/commit/0ddaf6dffa) [#38896](https://github.com/vllm-project/vllm/pull/38896)
  [XPU] [CT] Enable CT W4A4MxFp4 path and add xpu kernel (#38896)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/mxfp4/xpu.py`_
- **2026-05-13** [`a8c13d2837`](https://github.com/vllm-project/vllm/commit/a8c13d2837) [#42464](https://github.com/vllm-project/vllm/pull/42464)
  Patch SlidingWindowSpec.real_page_size_bytes for nvfp4 kv (#42464)
  _Files: `vllm/v1/kv_cache_interface.py`_

## Serving / API  (8 commits)

- **2026-05-20** [`fadf5d332c`](https://github.com/vllm-project/vllm/commit/fadf5d332c) [#42975](https://github.com/vllm-project/vllm/pull/42975)
  add enqueue all option to throughput benchmark (#42975)
  _Files: `tests/entrypoints/llm/test_mm_processor_kwargs.py`, `vllm/benchmarks/throughput.py`, `vllm/entrypoints/llm.py`_
- **2026-05-19** [`a78b842d0e`](https://github.com/vllm-project/vllm/commit/a78b842d0e) [#42887](https://github.com/vllm-project/vllm/pull/42887)
  [Bugfix] Fix top logprobs token placeholders in `/inference/v1/generate` (#42887)
  _Files: `tests/entrypoints/serve/disagg/test_tokens_logprobs.py`, `vllm/entrypoints/serve/disagg/serving.py`_
- **2026-05-16** [`39c67d714e`](https://github.com/vllm-project/vllm/commit/39c67d714e) [#42594](https://github.com/vllm-project/vllm/pull/42594)
  fix: add API key authorization to /v2 endpoints (#42594)
  _Files: `docs/usage/security.md`, `tests/entrypoints/serve/instrumentator/test_optional_middleware.py`, `vllm/entrypoints/openai/server_utils.py`_
- **2026-05-15** [`75fd68c7a5`](https://github.com/vllm-project/vllm/commit/75fd68c7a5) [#42267](https://github.com/vllm-project/vllm/pull/42267)
  [Entrypoints] Split the pooling offline API into PoolingOfflineMixin. (#42267)
  _Files: `docs/models/pooling_models/README.md`, `docs/models/pooling_models/classify.md`, `docs/models/pooling_models/embed.md`, `docs/models/pooling_models/reward.md` _+5 more__
- **2026-05-13** [`873910d608`](https://github.com/vllm-project/vllm/commit/873910d608) [#42116](https://github.com/vllm-project/vllm/pull/42116)
  [Frontend] add support for thinking_token_budget in completions (#42116)
  _Files: `vllm/entrypoints/openai/completion/protocol.py`_
- **2026-05-13** [`0f69128a37`](https://github.com/vllm-project/vllm/commit/0f69128a37) [#42454](https://github.com/vllm-project/vllm/pull/42454)
  [Bugfix] Handle real-world gpt-oss tool call output in Harmony parsing (#42454)
  _Files: `tests/entrypoints/openai/chat_completion/test_serving_chat_stream_harmony.py`, `tests/entrypoints/openai/parser/test_harmony_utils.py`, `tests/entrypoints/openai/responses/test_harmony_utils.py`, `tests/tool_parsers/test_openai_tool_parser.py` _+8 more__
- **2026-05-13** [`97c4317bf5`](https://github.com/vllm-project/vllm/commit/97c4317bf5) [#42329](https://github.com/vllm-project/vllm/pull/42329)
  [Bugfix][Frontend] Default max_tokens server-side on /inference/v1/generate (#42329)
  _Files: `tests/entrypoints/openai/test_openai_schema.py`, `tests/entrypoints/serve/disagg/test_protocol.py`, `tests/entrypoints/serve/disagg/test_serving_tokens.py`, `vllm/entrypoints/serve/disagg/protocol.py` _+1 more__
- **2026-05-13** [`503697c9ce`](https://github.com/vllm-project/vllm/commit/503697c9ce) [#42368](https://github.com/vllm-project/vllm/pull/42368)
  [chore] Refactor pooling metadata token ID accessors (#42368)
  _Files: `vllm/entrypoints/pooling/embed/serving.py`, `vllm/entrypoints/pooling/pooling/serving.py`, `vllm/entrypoints/pooling/utils.py`, `vllm/v1/pool/metadata.py`_

## Speculative Decoding  (8 commits)

- **2026-05-19** [`1242196295`](https://github.com/vllm-project/vllm/commit/1242196295) [#42764](https://github.com/vllm-project/vllm/pull/42764)
  [Model] Support post-norm architecture for EAGLE-3 supeculators (#42764)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`, `vllm/model_executor/models/llama_eagle3.py`, `vllm/v1/worker/gpu_model_runner.py`_
- **2026-05-18** [`a171e6b52d`](https://github.com/vllm-project/vllm/commit/a171e6b52d) [#43010](https://github.com/vllm-project/vllm/pull/43010)
  Add parallel drafting to v2 model runner unsupported features (#43010)
  _Files: `vllm/config/vllm.py`_
- **2026-05-15** [`0162596603`](https://github.com/vllm-project/vllm/commit/0162596603) [#41775](https://github.com/vllm-project/vllm/pull/41775)
  [Model Runner V2] FP32 gumbel sampling. (#41775)
  _Files: `vllm/config/model.py`, `vllm/engine/arg_utils.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/sample/gumbel.py` _+4 more__
- **2026-05-15** [`faa4b76afa`](https://github.com/vllm-project/vllm/commit/faa4b76afa) [#42705](https://github.com/vllm-project/vllm/pull/42705)
  [Model] Support InternS2 Preview (#42705)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/interns2_preview.py` _+2 more__
- **2026-05-14** [`f51f6844f9`](https://github.com/vllm-project/vllm/commit/f51f6844f9) [#40269](https://github.com/vllm-project/vllm/pull/40269)
  [Bugfix][Spec Decode] Wire draft_probs into probabilistic draft_model rejection (#40269)
  _Files: `tests/test_config.py`, `tests/v1/spec_decode/test_eagle.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/config/speculative.py` _+3 more__
- **2026-05-13** [`a505cf807e`](https://github.com/vllm-project/vllm/commit/a505cf807e) [#42538](https://github.com/vllm-project/vllm/pull/42538)
  [ModelRunner V2] Share identical MTP weights (#42538)
  _Files: `vllm/v1/worker/gpu/spec_decode/eagle/utils.py`_
- **2026-05-13** [`ab1ad0d7a9`](https://github.com/vllm-project/vllm/commit/ab1ad0d7a9) [#42536](https://github.com/vllm-project/vllm/pull/42536)
  Remove verifier model type check in speculative config (#42536)
  _Files: `vllm/config/speculative.py`_
- **2026-05-13** [`256dbcaabf`](https://github.com/vllm-project/vllm/commit/256dbcaabf) [#39487](https://github.com/vllm-project/vllm/pull/39487)
  [Feature] Support custom callable proposer backend for speculative decoding (#39487)
  _Files: `docs/features/speculative_decoding/README.md`, `tests/spec_decode/test_custom_proposer.py`, `tools/pre_commit/mypy.py`, `vllm/config/speculative.py` _+3 more__

## Scheduler / Engine  (6 commits)

- **2026-05-19** [`f34623bf3c`](https://github.com/vllm-project/vllm/commit/f34623bf3c) [#42117](https://github.com/vllm-project/vllm/pull/42117)
  [bug] AsyncScheduler drops first post-resume token after pause_generation + clear_cache (#42117)
  _Files: `examples/rl/rlhf_async_new_apis.py`, `vllm/v1/core/sched/async_scheduler.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/request.py`_
- **2026-05-19** [`257af77bc2`](https://github.com/vllm-project/vllm/commit/257af77bc2) [#41907](https://github.com/vllm-project/vllm/pull/41907)
  [Docs] Reorganize online serving docs. (#41907)
  _Files: `docs/.nav.yml`, `docs/assets/models/pooling_models/cheat_sheet.svg`, `docs/configuration/README.md`, `docs/configuration/engine_args.md` _+20 more__
- **2026-05-19** [`fab07e4d0f`](https://github.com/vllm-project/vllm/commit/fab07e4d0f) [#42289](https://github.com/vllm-project/vllm/pull/42289)
  [Bugfix][KV Connector] Fix SimpleCPUOffloadScheduler TOCTOU between Phase A and Phase B (#42289)
  _Files: `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_
- **2026-05-19** [`239b5ff30c`](https://github.com/vllm-project/vllm/commit/239b5ff30c) [#42476](https://github.com/vllm-project/vllm/pull/42476)
  [Frontend] Add --spec-method/--spec-model/--spec-tokens CLI aliases (#42476)
  _Files: `vllm/engine/arg_utils.py`, `vllm/entrypoints/llm.py`_
- **2026-05-14** [`f60c6b33a5`](https://github.com/vllm-project/vllm/commit/f60c6b33a5) [#41626](https://github.com/vllm-project/vllm/pull/41626)
  [V1][DP][LB] Publish request counts at the start of each engine step (#41626)
  _Files: `vllm/v1/engine/core.py`_
- **2026-05-13** [`9ce74042d3`](https://github.com/vllm-project/vllm/commit/9ce74042d3) [#41289](https://github.com/vllm-project/vllm/pull/41289)
  [Bugfix][SimpleCPUOffloadBackend] Dedup in-flight CPU offload stores across scheduler steps (#41289)
  _Files: `.buildkite/test_areas/misc.yaml`, `tests/v1/simple_kv_offload/test_scheduler.py`, `vllm/v1/simple_kv_offload/manager.py`_

## KV Cache / Offload  (4 commits)

- **2026-05-20** [`4f940896a3`](https://github.com/vllm-project/vllm/commit/4f940896a3) [#43076](https://github.com/vllm-project/vllm/pull/43076)
  [KV Offload] Pass `OffloadingSpec` instead of `VllmConfig` to secondary tiers (#43076)
  _Files: `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/example/manager.py`, `vllm/v1/kv_offload/tiering/factory.py` _+1 more__
- **2026-05-19** [`fba010dd74`](https://github.com/vllm-project/vllm/commit/fba010dd74) [#42766](https://github.com/vllm-project/vllm/pull/42766)
  [Bugfix][MRV2] Fix KVCache tensor explicit `kernel_block_size` dim (#42766)
  _Files: `tests/test_config.py`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/attn_utils.py`, `vllm/v1/worker/gpu/block_table.py` _+2 more__
- **2026-05-18** [`e414e1f1c0`](https://github.com/vllm-project/vllm/commit/e414e1f1c0) [#42945](https://github.com/vllm-project/vllm/pull/42945)
  [Bugfix][KV Offload] count appended GPU blocks in store group_sizes (#42945)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-05-13** [`11f6b545d4`](https://github.com/vllm-project/vllm/commit/11f6b545d4) [#40020](https://github.com/vllm-project/vllm/pull/40020)
  [kv_offload] Add multi-tier KV cache offloading framework (#40020)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `tests/v1/kv_offload/cpu/test_manager.py`, `tests/v1/kv_offload/test_tiering_offloading.py`, `vllm/v1/kv_offload/base.py` _+10 more__

## Perf / Benchmark  (4 commits)

- **2026-05-20** [`2ae910ed88`](https://github.com/vllm-project/vllm/commit/2ae910ed88) [#42938](https://github.com/vllm-project/vllm/pull/42938)
  [Perf] Avoid forward scan for async output placeholders (#42938)
  _Files: `vllm/v1/worker/gpu_input_batch.py`_
- **2026-05-16** [`87a2adcb43`](https://github.com/vllm-project/vllm/commit/87a2adcb43) [#41632](https://github.com/vllm-project/vllm/pull/41632)
  [Misc] Add common random prefix option to structured-output serving benchmark (#41632)
  _Files: `benchmarks/benchmark_serving_structured_output.py`_
- **2026-05-15** [`9a7a273dfe`](https://github.com/vllm-project/vllm/commit/9a7a273dfe) [#42648](https://github.com/vllm-project/vllm/pull/42648)
  Add HumanEval and GSM8K benchmarks to datasets (#42648)
  _Files: `docs/benchmarking/cli.md`, `vllm/benchmarks/datasets/datasets.py`_
- **2026-05-15** [`fb5bd03f51`](https://github.com/vllm-project/vllm/commit/fb5bd03f51) [#42631](https://github.com/vllm-project/vllm/pull/42631)
  [Perf] Set IR Op Priority Once at Worker Init (#42631)
  _Files: `tests/ir/test_op.py`, `vllm/config/kernel.py`, `vllm/forward_context.py`, `vllm/ir/__init__.py` _+2 more__

## Compilation / CUDA Graph  (3 commits)

- **2026-05-18** [`1ac10f159a`](https://github.com/vllm-project/vllm/commit/1ac10f159a) [#42686](https://github.com/vllm-project/vllm/pull/42686)
  Revert "[torch.compile] Add patch for fullgraph compilation" (#42686) (#42913)
  _Files: `vllm/env_override.py`_
- **2026-05-17** [`966903eb93`](https://github.com/vllm-project/vllm/commit/966903eb93) [#42686](https://github.com/vllm-project/vllm/pull/42686)
  [torch.compile] Add patch for fullgraph compilation (#42686)
  _Files: `vllm/env_override.py`_
- **2026-05-14** [`a7737cb4f3`](https://github.com/vllm-project/vllm/commit/a7737cb4f3) [#38040](https://github.com/vllm-project/vllm/pull/38040)
  [Fix] Misc Fixes in ViT CUDA Graph (#38040)
  _Files: `tests/v1/cudagraph/test_encoder_cudagraph.py`, `vllm/config/compilation.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/v1/worker/encoder_cudagraph.py`_

## Docs  (2 commits)

- **2026-05-19** [`be16785998`](https://github.com/vllm-project/vllm/commit/be16785998) [#43115](https://github.com/vllm-project/vllm/pull/43115)
  [CPU][DOC] Fix installation commands for Arm CPUs (#43115)
  _Files: `docs/getting_started/installation/cpu.arm.inc.md`_
- **2026-05-18** [`c1f7854342`](https://github.com/vllm-project/vllm/commit/c1f7854342) [#42929](https://github.com/vllm-project/vllm/pull/42929)
  Improve logging when docs build is skipped (#42929)
  _Files: `.readthedocs.yaml`, `docs/pre_run_check.sh`_

## LoRA  (1 commits)

- **2026-05-20** [`39bba710be`](https://github.com/vllm-project/vllm/commit/39bba710be) [#43160](https://github.com/vllm-project/vllm/pull/43160)
  [MRV2][BugFix] Fix default-stream CG capture in P/W LoRA case (#43160)
  _Files: `vllm/v1/worker/gpu/cudagraph_utils.py`_

---
_Generated 2026-05-20 04:14 UTC_