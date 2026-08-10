# vllm-project/vllm — Weekly Change Report
**Period:** 2026-08-03 → 2026-08-10  |  **Total commits:** 302

## ✨ New Features This Week

- **2026-08-10** [#51604](https://github.com/vllm-project/vllm/pull/51604) — [CI][XPU] Add VLLM_DISABLE_COMPILE_CACHE=1 for other random failed cases in Intel GPU CI (#51604)
- **2026-08-10** [#51265](https://github.com/vllm-project/vllm/pull/51265) — `[Model][Quantization] Add Ling-3.0-flash-fp8 support` (#51265)
- **2026-08-10** [#51148](https://github.com/vllm-project/vllm/pull/51148) — [CPU] Enable GPTQ and AWQ quantization for s390x (#51148)
- **2026-08-10** [#48798](https://github.com/vllm-project/vllm/pull/48798) — Add tiering offloading metrics (#48798)
- **2026-08-09** [#43529](https://github.com/vllm-project/vllm/pull/43529) — [Migration] Migrate bitsandbytes support to OOT plugin (#43529)
- **2026-08-09** [#51457](https://github.com/vllm-project/vllm/pull/51457) — [Test] Add ROCm AITER FP8 MLA prefill accuracy test (#51457)
- **2026-08-08** [#40116](https://github.com/vllm-project/vllm/pull/40116) — Add torch compile for qwen3_vl encoder (#40116)
- **2026-08-07** [#51440](https://github.com/vllm-project/vllm/pull/51440) — [CI Test] Add specific unit test for mrv2 offloading (#51440)
- **2026-08-07** [#45187](https://github.com/vllm-project/vllm/pull/45187) — Add NVFP4 KV 4-over-6 scale search (#45187)
- **2026-08-07** [#49347](https://github.com/vllm-project/vllm/pull/49347) — [Online quantization] Add online MXFP4 quantization support (#49347)
- _…and 54 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-08-10** [`74c94b9f29`](https://github.com/vllm-project/vllm/commit/74c94b9f29) [#51422](https://github.com/vllm-project/vllm/pull/51422) — [CI] Upgrade huggingface-hub to 1.27.0 (#51422)
- **2026-08-10** [`31cd109f18`](https://github.com/vllm-project/vllm/commit/31cd109f18) [#40958](https://github.com/vllm-project/vllm/pull/40958) — [ROCm][CI] Extend ROCm AITER MHA (FA) coverage (#40958)
- **2026-08-09** [`7f6432cc0d`](https://github.com/vllm-project/vllm/commit/7f6432cc0d) [#48646](https://github.com/vllm-project/vllm/pull/48646) — [ROCm][CI] Reuse equivalent ROCm CI images (#48646)
- **2026-08-09** [`073c510c91`](https://github.com/vllm-project/vllm/commit/073c510c91) [#43529](https://github.com/vllm-project/vllm/pull/43529) — [Migration] Migrate bitsandbytes support to OOT plugin (#43529)
- **2026-08-09** [`cb1a52aee3`](https://github.com/vllm-project/vllm/commit/cb1a52aee3) [#51058](https://github.com/vllm-project/vllm/pull/51058) — [Build] Upgrade runtime image to Ubuntu 24.04, pick up rdma-core > 44 (#51058)
- **2026-08-09** [`7581c56c86`](https://github.com/vllm-project/vllm/commit/7581c56c86) [#51457](https://github.com/vllm-project/vllm/pull/51457) — [Test] Add ROCm AITER FP8 MLA prefill accuracy test (#51457)
- **2026-08-08** [`643c125fab`](https://github.com/vllm-project/vllm/commit/643c125fab) [#50805](https://github.com/vllm-project/vllm/pull/50805) — [ROCm][CI] Baseline legacy extensions in the Torch ABI audit (#50805)
- **2026-08-08** [`44351f81d5`](https://github.com/vllm-project/vllm/commit/44351f81d5) [#51410](https://github.com/vllm-project/vllm/pull/51410) — [CI] Refresh hybrid Model Runner V2 coverage (#51410)
- **2026-08-07** [`46b5864054`](https://github.com/vllm-project/vllm/commit/46b5864054) [#51425](https://github.com/vllm-project/vllm/pull/51425) — [Perf] Narrow DeepSeek V3.2 eager CUDA graph region (#51425)
- **2026-08-07** [`3518110f2f`](https://github.com/vllm-project/vllm/commit/3518110f2f) [#49347](https://github.com/vllm-project/vllm/pull/49347) — [Online quantization] Add online MXFP4 quantization support (#49347)
- **2026-08-07** [`a0056e103e`](https://github.com/vllm-project/vllm/commit/a0056e103e) [#50930](https://github.com/vllm-project/vllm/pull/50930) — [Test] Add ROCm AITER MLA op registration and env gating tests (#50930)
- **2026-08-07** [`ebb2972562`](https://github.com/vllm-project/vllm/commit/ebb2972562) [#51402](https://github.com/vllm-project/vllm/pull/51402) — [ROCm][CI][Bugfix] Do not microbatch a step that splits a prefix from its writer (#51402)
- **2026-08-07** [`e229fdbc87`](https://github.com/vllm-project/vllm/commit/e229fdbc87) [#50007](https://github.com/vllm-project/vllm/pull/50007) — [ROCm] Add tuned selective_state_update float32 config for AMD Instinct MI325X (#50007)
- **2026-08-07** [`34c1cd20a5`](https://github.com/vllm-project/vllm/commit/34c1cd20a5) [#49373](https://github.com/vllm-project/vllm/pull/49373) — [Bugfix][ROCm] Fix ROCM_AITER_FA & ROCM_AITER_UNIFIED_ATTN QK-Norm+RoPE+KVCache fusion for the packed KV-cache [BLOCKS, HEADS, BLOCK_SIZE, 2*HEAD_DIM] layout (#49373)
- **2026-08-07** [`7e85d3a42c`](https://github.com/vllm-project/vllm/commit/7e85d3a42c) [#50126](https://github.com/vllm-project/vllm/pull/50126) — [ROCm] Enable pinned memory on supported WSL2 kernels (#50126)
- **2026-08-07** [`47228db84c`](https://github.com/vllm-project/vllm/commit/47228db84c) [#48534](https://github.com/vllm-project/vllm/pull/48534) — [Bugfix][KV-transfer] MoRIIO: per-layer READ-completion barrier in wait_for_layer_load (#48534)
- **2026-08-07** [`f2bfad9167`](https://github.com/vllm-project/vllm/commit/f2bfad9167) [#50068](https://github.com/vllm-project/vllm/pull/50068) — [Model] Enable Qwen3.8 for AMD Rocm (#50068)
- **2026-08-07** [`d5aae2b464`](https://github.com/vllm-project/vllm/commit/d5aae2b464) [#51357](https://github.com/vllm-project/vllm/pull/51357) — Fix ROCm architecture import on non-ROCm platforms (#51357)
- **2026-08-07** [`c84789c40b`](https://github.com/vllm-project/vllm/commit/c84789c40b) [#51051](https://github.com/vllm-project/vllm/pull/51051) — [Refactor] Remove kernel dead code (#51051)
- **2026-08-07** [`da788334bc`](https://github.com/vllm-project/vllm/commit/da788334bc) [#47972](https://github.com/vllm-project/vllm/pull/47972) — Support DeepSeek-V4 AMD Quark NVFP4 with emulation kernel  (#47972)
- **2026-08-07** [`0de0362ea1`](https://github.com/vllm-project/vllm/commit/0de0362ea1) [#48847](https://github.com/vllm-project/vllm/pull/48847) — [ROCm][CI] Loosen block-FP8 fused MoE test tolerance for large-K shapes (#48847)
- **2026-08-07** [`43d691ec6b`](https://github.com/vllm-project/vllm/commit/43d691ec6b) [#51253](https://github.com/vllm-project/vllm/pull/51253) — [ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path (#51253)
- **2026-08-06** [`a07086e403`](https://github.com/vllm-project/vllm/commit/a07086e403) [#50827](https://github.com/vllm-project/vllm/pull/50827) — [Misc] Upgrade fastsafetensors version, fix metadata is null (#50827)
- **2026-08-06** [`d8eabdbfbe`](https://github.com/vllm-project/vllm/commit/d8eabdbfbe) [#50578](https://github.com/vllm-project/vllm/pull/50578) — [ROCm][MLA] Use asm decode for non-divisor small head counts (#50578)
- **2026-08-06** [`4f851bef6c`](https://github.com/vllm-project/vllm/commit/4f851bef6c) [#51273](https://github.com/vllm-project/vllm/pull/51273) — [ROCm][CI] Update AITER AR+RMS e2e fusion counts for final-norm coverage (#51273)
- **2026-08-06** [`81be2e09ae`](https://github.com/vllm-project/vllm/commit/81be2e09ae) [#49601](https://github.com/vllm-project/vllm/pull/49601) — [Weight processing] Copy over `new_data` attributes in `replace_parameter` (#49601)
- **2026-08-06** [`b38e111d3e`](https://github.com/vllm-project/vllm/commit/b38e111d3e) [#50613](https://github.com/vllm-project/vllm/pull/50613) — [Attention][MLA] Per-request scheduling for MLA chunked context (#50613)
- **2026-08-06** [`ad5280255b`](https://github.com/vllm-project/vllm/commit/ad5280255b) [#50904](https://github.com/vllm-project/vllm/pull/50904) — [GLM Perf] DSv32/glm use skip topk for MTP case, 2.0x kernel performance improvement (#50904)
- **2026-08-06** [`7e724dca89`](https://github.com/vllm-project/vllm/commit/7e724dca89) [#50802](https://github.com/vllm-project/vllm/pull/50802) — [ROCm] Fix AITER all-reduce fusion coverage (#50802)
- **2026-08-06** [`71f975af43`](https://github.com/vllm-project/vllm/commit/71f975af43) [#50480](https://github.com/vllm-project/vllm/pull/50480) — [ROCm][CI] Add MLA decode accuracy and determinism tests (#50480)
- **2026-08-05** [`38ebd97bca`](https://github.com/vllm-project/vllm/commit/38ebd97bca) [#51083](https://github.com/vllm-project/vllm/pull/51083) — [ROCm] Relax MLA rope+cache test tolerances for bf16 (#51083)
- **2026-08-05** [`4282fe52d5`](https://github.com/vllm-project/vllm/commit/4282fe52d5) [#49375](https://github.com/vllm-project/vllm/pull/49375) — [ROCm][CI] Add More AITER quantization/MoE kernel tests (#49375)
- **2026-08-05** [`65addac701`](https://github.com/vllm-project/vllm/commit/65addac701) [#51173](https://github.com/vllm-project/vllm/pull/51173) — [ROCm][CI] Keep rocprofiler-sdk out of DeepEP HT MoE test workers (#51173)
- **2026-08-05** [`c2d8009044`](https://github.com/vllm-project/vllm/commit/c2d8009044) [#51174](https://github.com/vllm-project/vllm/pull/51174) — [ROCm] Work around DeepEP teardown SIGSEGV in MoE test harness (#51174)
- **2026-08-05** [`397094da17`](https://github.com/vllm-project/vllm/commit/397094da17) [#49990](https://github.com/vllm-project/vllm/pull/49990) — Resolve revision to commit_hash once per model load, via huggingface_hub's `resolve_revision` (#49990)
- **2026-08-05** [`f5cd862dbd`](https://github.com/vllm-project/vllm/commit/f5cd862dbd) [#50649](https://github.com/vllm-project/vllm/pull/50649) — [ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config (#50649)
- **2026-08-05** [`bb543efdfd`](https://github.com/vllm-project/vllm/commit/bb543efdfd) [#50905](https://github.com/vllm-project/vllm/pull/50905) — [ROCm][CI] Add aiter per-token FP8 quant roundtrip and RMSNorm determinism tests (#50905)
- **2026-08-05** [`33c50587d2`](https://github.com/vllm-project/vllm/commit/33c50587d2) [#50806](https://github.com/vllm-project/vllm/pull/50806) — [ROCm] Restore Inkling MTP backend parity (#50806)
- **2026-08-05** [`d0ce3dadb6`](https://github.com/vllm-project/vllm/commit/d0ce3dadb6) [#50607](https://github.com/vllm-project/vllm/pull/50607) — [ROCm]: Bump torch 2.12, triton 3.7, torchaudio, torchvision (#50607)
- **2026-08-04** [`7ac2ec7582`](https://github.com/vllm-project/vllm/commit/7ac2ec7582) [#50593](https://github.com/vllm-project/vllm/pull/50593) — [Kimi-K3][AMD] Fuse AttnRes state updates and norms (#50593)
- **2026-08-04** [`385d4c084e`](https://github.com/vllm-project/vllm/commit/385d4c084e) [#50859](https://github.com/vllm-project/vllm/pull/50859) — [ROCm][AITER] Hotfix for `memory access fault` errors in AITER triton MOE routing (#50859)
- **2026-08-04** [`8adc840c45`](https://github.com/vllm-project/vllm/commit/8adc840c45) [#50917](https://github.com/vllm-project/vllm/pull/50917) — [ROCm][Test] Use BF16 for Jina v5 nano MTEB test (#50917)
- **2026-08-04** [`f42761204f`](https://github.com/vllm-project/vllm/commit/f42761204f) [#45043](https://github.com/vllm-project/vllm/pull/45043) — llmd+vllm+mori-ep(inter node wide-ep)+mori-io(write) for 2p2d with dp=ep=16 tp=1 (#45043)
- **2026-08-03** [`f43e1d26e3`](https://github.com/vllm-project/vllm/commit/f43e1d26e3) [#43615](https://github.com/vllm-project/vllm/pull/43615) — [ROCm] Enable AITER and FP8 inference on GFX120x (#43615)
- **2026-08-03** [`4a3447d200`](https://github.com/vllm-project/vllm/commit/4a3447d200) [#50417](https://github.com/vllm-project/vllm/pull/50417) — [Bugfix][Model Runner V2] Restore multimodal draft capability detection (#50417)
- **2026-08-03** [`e279f71583`](https://github.com/vllm-project/vllm/commit/e279f71583) [#50728](https://github.com/vllm-project/vllm/pull/50728) — [ROCm][Test] Fix AITER MXFP4 oracle contract (#50728)
- **2026-08-03** [`8f50685c48`](https://github.com/vllm-project/vllm/commit/8f50685c48) [#50582](https://github.com/vllm-project/vllm/pull/50582) — [ROCm][Kimi-K3] aiter moe environment variable cleanup (#50582)
- **2026-08-03** [`76d995df2c`](https://github.com/vllm-project/vllm/commit/76d995df2c) [#50726](https://github.com/vllm-project/vllm/pull/50726) — [CI][ROCm] Export Helion benchmark script in test artifacts (#50726)
- **2026-08-03** [`dd11df04f3`](https://github.com/vllm-project/vllm/commit/dd11df04f3) [#49389](https://github.com/vllm-project/vllm/pull/49389) — [Misc] Remove deprecated calculate_kv_scales runtime KV scale calculation (#49389)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#51651](https://github.com/vllm-project/vllm/issues/51651) | [Bug]: Missing `reasoning` on Some Turns in Multi-Turn Tool-Calling (D | bug | 2026-08-10 |
| [#51063](https://github.com/vllm-project/vllm/issues/51063) | [Bug]: Composite VLM wrapper (Mistral3ForConditionalGeneration) resolv | bug | 2026-08-10 |
| [#51593](https://github.com/vllm-project/vllm/issues/51593) | [Bug]: DeepSeek-V4-Flash MTP hangs after the batch drains to 3 request | — | 2026-08-10 |
| [#51644](https://github.com/vllm-project/vllm/issues/51644) | [CI Failure]: tests/kernels/moe/test_deepep_moe.py SIGSEGV on ROCm, dr | rocm, ci-failure | 2026-08-10 |
| [#51275](https://github.com/vllm-project/vllm/issues/51275) | [RFC]: Race-free port management: pick ports at bind time, publish ove | RFC | 2026-08-10 |
| [#51637](https://github.com/vllm-project/vllm/issues/51637) | [Bug][MooncakeStoreConnector]: Request-ID ABA across preemption corrup | bug | 2026-08-10 |
| [#50576](https://github.com/vllm-project/vllm/issues/50576) | [Feature]: SM8x (Ampere A100/A800) support for DeepSeek-V4-Flash / Dee | — | 2026-08-10 |
| [#48193](https://github.com/vllm-project/vllm/issues/48193) | [Roadmap] Cold Start Q3 2026 | — | 2026-08-10 |
| [#47761](https://github.com/vllm-project/vllm/issues/47761) | [Bug]: vllm 0.23.0 and 0.24.0 - Qwen3.6-35B-A3B-FP8 - Fails generating | bug | 2026-08-10 |
| [#51608](https://github.com/vllm-project/vllm/issues/51608) | [RFC]: Extensible Scheduler Plugin Framework for vLLM | RFC | 2026-08-10 |
| [#49413](https://github.com/vllm-project/vllm/issues/49413) | [RFC]: KV offload event path refactor — provenance-carrying events and | — | 2026-08-10 |
| [#51541](https://github.com/vllm-project/vllm/issues/51541) | [ROCm][AITER] Port FlyDSL int4 MoE integration to AITER fused_moe API | rocm, quantization | 2026-08-10 |
| [#51594](https://github.com/vllm-project/vllm/issues/51594) | [Bug]: LoRA lm_head delta is silently dropped from prompt_logprobs | — | 2026-08-10 |
| [#41071](https://github.com/vllm-project/vllm/issues/41071) | [Bug]: KeyError: 'layers.0.mlp.experts.w13_bias' when running quantize | bug, stale | 2026-08-10 |
| [#42065](https://github.com/vllm-project/vllm/issues/42065) | [Feature]: Add nemotron_json as built-in tool parser (NVIDIA Nemotron- | feature request, stale | 2026-08-10 |
| [#42125](https://github.com/vllm-project/vllm/issues/42125) | [Bug]: Runtime LoRA same-name reload can reuse stale prefix-cache bloc | stale | 2026-08-10 |
| [#42210](https://github.com/vllm-project/vllm/issues/42210) | [Bug]: Streaming chat completion drops partial content when stop strin | bug, stale | 2026-08-10 |
| [#42303](https://github.com/vllm-project/vllm/issues/42303) | [Bug]: `prompt_token_ids` dropped in `EmbedsInput` pipeline | bug, stale | 2026-08-10 |
| [#50720](https://github.com/vllm-project/vllm/issues/50720) | [Bug]: DeepSeek-V4-Flash-0731 + DSpark fails on RTX PRO 6000 (SM120) w | bug | 2026-08-10 |
| [#51572](https://github.com/vllm-project/vllm/issues/51572) | [Bug]:Anthropic Messages API: x-api-key authentication header not supp | bug | 2026-08-10 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| ROCm / AMD | 46 |
| MoE / Expert Parallel | 45 |
| Other | 36 |
| Multimodal | 23 |
| Quantization | 22 |
| CI / Build | 19 |
| Scheduler / Engine | 18 |
| Attention | 18 |
| Disaggregation / PD | 17 |
| Models | 16 |
| KV Cache / Offload | 14 |
| Speculative Decoding | 7 |
| Serving / API | 6 |
| Perf / Benchmark | 5 |
| Compilation / CUDA Graph | 4 |
| Docs | 3 |
| LoRA | 3 |

## ROCm / AMD  (46 commits)

- **2026-08-10** [`74c94b9f29`](https://github.com/vllm-project/vllm/commit/74c94b9f29) [#51422](https://github.com/vllm-project/vllm/pull/51422)
  [CI] Upgrade huggingface-hub to 1.27.0 (#51422)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+1 more__
- **2026-08-10** [`31cd109f18`](https://github.com/vllm-project/vllm/commit/31cd109f18) [#40958](https://github.com/vllm-project/vllm/pull/40958)
  [ROCm][CI] Extend ROCm AITER MHA (FA) coverage (#40958)
  _Files: `tests/kernels/attention/test_aiter_flash_attn.py`, `tests/kernels/attention/test_rocm_aiter_fa.py`_
- **2026-08-09** [`7f6432cc0d`](https://github.com/vllm-project/vllm/commit/7f6432cc0d) [#48646](https://github.com/vllm-project/vllm/pull/48646)
  [ROCm][CI] Reuse equivalent ROCm CI images (#48646)
  _Files: `.buildkite/ci_config_rocm.yaml`, `.buildkite/hardware_tests/amd.yaml`, `.buildkite/scripts/ci-bake-rocm.sh`, `.buildkite/scripts/hardware_ci/run-amd-test.sh` _+9 more__
- **2026-08-09** [`073c510c91`](https://github.com/vllm-project/vllm/commit/073c510c91) [#43529](https://github.com/vllm-project/vllm/pull/43529)
  [Migration] Migrate bitsandbytes support to OOT plugin (#43529)
  _Files: `.buildkite/test_areas/plugins.yaml`, `docker/Dockerfile`, `docker/versions.json`, `docs/features/quantization/bnb.md` _+27 more__
- **2026-08-09** [`7581c56c86`](https://github.com/vllm-project/vllm/commit/7581c56c86) [#51457](https://github.com/vllm-project/vllm/pull/51457)
  [Test] Add ROCm AITER FP8 MLA prefill accuracy test (#51457)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_fp8_prefill.py`_
- **2026-08-08** [`643c125fab`](https://github.com/vllm-project/vllm/commit/643c125fab) [#50805](https://github.com/vllm-project/vllm/pull/50805)
  [ROCm][CI] Baseline legacy extensions in the Torch ABI audit (#50805)
  _Files: `.buildkite/check-torch-abi.py`_
- **2026-08-08** [`44351f81d5`](https://github.com/vllm-project/vllm/commit/44351f81d5) [#51410](https://github.com/vllm-project/vllm/pull/51410)
  [CI] Refresh hybrid Model Runner V2 coverage (#51410)
  _Files: `.buildkite/intel_jobs/model_runner_v2_intel.yaml`, `.buildkite/test-amd.yaml`, `.buildkite/test_areas/model_runner_v2.yaml`, `.buildkite/test_areas/quantization.yaml` _+1 more__
- **2026-08-07** [`46b5864054`](https://github.com/vllm-project/vllm/commit/46b5864054) [#51425](https://github.com/vllm-project/vllm/pull/51425)
  [Perf] Narrow DeepSeek V3.2 eager CUDA graph region (#51425)
  _Files: `vllm/models/deepseek_v32/amd/rocm.py`, `vllm/models/deepseek_v32/attention.py`_
- **2026-08-07** [`3518110f2f`](https://github.com/vllm-project/vllm/commit/3518110f2f) [#49347](https://github.com/vllm-project/vllm/pull/49347)
  [Online quantization] Add online MXFP4 quantization support (#49347)
  _Files: `docs/features/quantization/online.md`, `tests/evals/gsm8k/configs/Qwen3-30B-A3B-MXFP4-AITER-TP2-online.yaml`, `tests/evals/gsm8k/configs/Qwen3-30B-A3B-MXFP4-AITER-TP2.yaml`, `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml` _+14 more__
- **2026-08-07** [`a0056e103e`](https://github.com/vllm-project/vllm/commit/a0056e103e) [#50930](https://github.com/vllm-project/vllm/pull/50930)
  [Test] Add ROCm AITER MLA op registration and env gating tests (#50930)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_op_registration.py`_
- **2026-08-07** [`ebb2972562`](https://github.com/vllm-project/vllm/commit/ebb2972562) [#51402](https://github.com/vllm-project/vllm/pull/51402)
  [ROCm][CI][Bugfix] Do not microbatch a step that splits a prefix from its writer (#51402)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-07** [`e229fdbc87`](https://github.com/vllm-project/vllm/commit/e229fdbc87) [#50007](https://github.com/vllm-project/vllm/pull/50007)
  [ROCm] Add tuned selective_state_update float32 config for AMD Instinct MI325X (#50007)
  _Files: `vllm/model_executor/layers/mamba/ops/configs/selective_state_update/headdim=64,dstate=128,device_name=AMD_Instinct_MI325X,cache_dtype=float32.json`_
- **2026-08-07** [`34c1cd20a5`](https://github.com/vllm-project/vllm/commit/34c1cd20a5) [#49373](https://github.com/vllm-project/vllm/pull/49373)
  [Bugfix][ROCm] Fix ROCM_AITER_FA & ROCM_AITER_UNIFIED_ATTN QK-Norm+RoPE+KVCache fusion for the packed KV-cache [BLOCKS, HEADS, BLOCK_SIZE, 2*HEAD_DIM] layout (#49373)
  _Files: `tests/compile/passes/test_rocm_aiter_qk_norm_rope_kvcache_fusion.py`, `vllm/v1/attention/backends/rocm_aiter_fa.py`, `vllm/v1/attention/backends/rocm_aiter_unified_attn.py`_
- **2026-08-07** [`7e85d3a42c`](https://github.com/vllm-project/vllm/commit/7e85d3a42c) [#50126](https://github.com/vllm-project/vllm/pull/50126)
  [ROCm] Enable pinned memory on supported WSL2 kernels (#50126)
  _Files: `.buildkite/scripts/xpu/create-xpu-ecr-manifest.sh`, `vllm/platforms/rocm.py`_
- **2026-08-07** [`f2bfad9167`](https://github.com/vllm-project/vllm/commit/f2bfad9167) [#50068](https://github.com/vllm-project/vllm/pull/50068)
  [Model] Enable Qwen3.8 for AMD Rocm (#50068)
  _Files: `vllm/model_executor/models/qwen3_5.py`_
- **2026-08-07** [`d5aae2b464`](https://github.com/vllm-project/vllm/commit/d5aae2b464) [#51357](https://github.com/vllm-project/vllm/pull/51357)
  Fix ROCm architecture import on non-ROCm platforms (#51357)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-08-07** [`c84789c40b`](https://github.com/vllm-project/vllm/commit/c84789c40b) [#51051](https://github.com/vllm-project/vllm/pull/51051)
  [Refactor] Remove kernel dead code (#51051)
  _Files: `csrc/cpu/cpu_attn_fp8.hpp`, `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/moe/grouped_topk_kernels.cu`, `csrc/libtorch_stable/quantization/fused_kernels/quant_conversions.cuh` _+4 more__
- **2026-08-07** [`da788334bc`](https://github.com/vllm-project/vllm/commit/da788334bc) [#47972](https://github.com/vllm-project/vllm/pull/47972)
  Support DeepSeek-V4 AMD Quark NVFP4 with emulation kernel  (#47972)
  _Files: `.buildkite/test-amd.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Flash-NVFP4.yaml`, `tests/evals/gsm8k/configs/DeepSeek-V4-Pro-NVFP4.yaml`, `tests/evals/gsm8k/configs/models-gfx950-large.txt` _+7 more__
- **2026-08-07** [`0de0362ea1`](https://github.com/vllm-project/vllm/commit/0de0362ea1) [#48847](https://github.com/vllm-project/vllm/pull/48847)
  [ROCm][CI] Loosen block-FP8 fused MoE test tolerance for large-K shapes (#48847)
  _Files: `tests/kernels/moe/test_block_fp8.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe.py`_
- **2026-08-07** [`43d691ec6b`](https://github.com/vllm-project/vllm/commit/43d691ec6b) [#51253](https://github.com/vllm-project/vllm/pull/51253)
  [ROCm][Perf] Kimi-K3 Shard Latent MoE up-projection for ROCm path (#51253)
  _Files: `tests/models/kimi_k3/__init__.py`, `tests/models/kimi_k3/test_amd_latent_moe_runner.py`, `vllm/models/kimi_k3/amd/latent_moe_runner.py`, `vllm/models/kimi_k3/amd/linear.py`_
- **2026-08-06** [`a07086e403`](https://github.com/vllm-project/vllm/commit/a07086e403) [#50827](https://github.com/vllm-project/vllm/pull/50827)
  [Misc] Upgrade fastsafetensors version, fix metadata is null (#50827)
  _Files: `requirements/cuda.txt`, `requirements/rocm.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.in` _+5 more__
- **2026-08-06** [`d8eabdbfbe`](https://github.com/vllm-project/vllm/commit/d8eabdbfbe) [#50578](https://github.com/vllm-project/vllm/pull/50578)
  [ROCm][MLA] Use asm decode for non-divisor small head counts (#50578)
  _Files: `tests/kernels/attention/test_rocm_aiter_mla_causal_verify_mask.py`, `tests/kernels/attention/test_rocm_aiter_mla_head_padding.py`, `vllm/envs.py`, `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`_
- **2026-08-06** [`4f851bef6c`](https://github.com/vllm-project/vllm/commit/4f851bef6c) [#51273](https://github.com/vllm-project/vllm/pull/51273)
  [ROCm][CI] Update AITER AR+RMS e2e fusion counts for final-norm coverage (#51273)
  _Files: `tests/compile/fusions_e2e/models.py`_
- **2026-08-06** [`81be2e09ae`](https://github.com/vllm-project/vllm/commit/81be2e09ae) [#49601](https://github.com/vllm-project/vllm/pull/49601)
  [Weight processing] Copy over `new_data` attributes in `replace_parameter` (#49601)
  _Files: `tests/model_executor/test_utils.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp8_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/fp8.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+6 more__
- **2026-08-06** [`b38e111d3e`](https://github.com/vllm-project/vllm/commit/b38e111d3e) [#50613](https://github.com/vllm-project/vllm/pull/50613)
  [Attention][MLA] Per-request scheduling for MLA chunked context (#50613)
  _Files: `tests/kernels/attention/test_merge_attn_states.py`, `tests/v1/attention/test_mla_backends.py`, `tests/v1/attention/test_mla_context_chunks.py`, `tests/v1/attention/test_mla_prefill_registry.py` _+11 more__
- **2026-08-06** [`ad5280255b`](https://github.com/vllm-project/vllm/commit/ad5280255b) [#50904](https://github.com/vllm-project/vllm/pull/50904)
  [GLM Perf] DSv32/glm use skip topk for MTP case, 2.0x kernel performance improvement (#50904)
  _Files: `vllm/models/deepseek_v32/amd/rocm.py`, `vllm/models/deepseek_v32/attention.py`_
- **2026-08-06** [`7e724dca89`](https://github.com/vllm-project/vllm/commit/7e724dca89) [#50802](https://github.com/vllm-project/vllm/pull/50802)
  [ROCm] Fix AITER all-reduce fusion coverage (#50802)
  _Files: `tests/compile/passes/distributed/test_fusion_all_reduce.py`, `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`_
- **2026-08-06** [`71f975af43`](https://github.com/vllm-project/vllm/commit/71f975af43) [#50480](https://github.com/vllm-project/vllm/pull/50480)
  [ROCm][CI] Add MLA decode accuracy and determinism tests (#50480)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/attention/test_rocm_aiter_mla_decode.py`_
- **2026-08-05** [`38ebd97bca`](https://github.com/vllm-project/vllm/commit/38ebd97bca) [#51083](https://github.com/vllm-project/vllm/pull/51083)
  [ROCm] Relax MLA rope+cache test tolerances for bf16 (#51083)
  _Files: `tests/kernels/core/test_rotary_embedding_mla_cache_fused.py`_
- **2026-08-05** [`4282fe52d5`](https://github.com/vllm-project/vllm/commit/4282fe52d5) [#49375](https://github.com/vllm-project/vllm/pull/49375)
  [ROCm][CI] Add More AITER quantization/MoE kernel tests (#49375)
  _Files: `.buildkite/test-amd.yaml`, `tests/kernels/moe/test_rocm_aiter_moe.py`, `tests/kernels/quantization/test_rocm_fp8.py`, `tests/kernels/quantization/test_rocm_mxfp4.py` _+1 more__
- **2026-08-05** [`65addac701`](https://github.com/vllm-project/vllm/commit/65addac701) [#51173](https://github.com/vllm-project/vllm/pull/51173)
  [ROCm][CI] Keep rocprofiler-sdk out of DeepEP HT MoE test workers (#51173)
  _Files: `tests/kernels/moe/test_deepep_moe.py`_
- **2026-08-05** [`c2d8009044`](https://github.com/vllm-project/vllm/commit/c2d8009044) [#51174](https://github.com/vllm-project/vllm/pull/51174)
  [ROCm] Work around DeepEP teardown SIGSEGV in MoE test harness (#51174)
  _Files: `tests/kernels/moe/parallel_utils.py`_
- **2026-08-05** [`397094da17`](https://github.com/vllm-project/vllm/commit/397094da17) [#49990](https://github.com/vllm-project/vllm/pull/49990)
  Resolve revision to commit_hash once per model load, via huggingface_hub's `resolve_revision` (#49990)
  _Files: `requirements/common.txt`, `requirements/test/cpu.txt`, `requirements/test/cuda.txt`, `requirements/test/rocm.txt` _+5 more__
- **2026-08-05** [`f5cd862dbd`](https://github.com/vllm-project/vllm/commit/f5cd862dbd) [#50649](https://github.com/vllm-project/vllm/pull/50649)
  [ROCm][Bugfix] Kimi-K3 Fix KDA NaN on mixed batches and racy autotune config (#50649)
  _Files: `vllm/models/kimi_k3/amd/kda.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`_
- **2026-08-05** [`bb543efdfd`](https://github.com/vllm-project/vllm/commit/bb543efdfd) [#50905](https://github.com/vllm-project/vllm/pull/50905)
  [ROCm][CI] Add aiter per-token FP8 quant roundtrip and RMSNorm determinism tests (#50905)
  _Files: `tests/rocm/aiter/test_quant_op_schema.py`_
- **2026-08-05** [`33c50587d2`](https://github.com/vllm-project/vllm/commit/33c50587d2) [#50806](https://github.com/vllm-project/vllm/pull/50806)
  [ROCm] Restore Inkling MTP backend parity (#50806)
  _Files: `vllm/models/inkling/amd/mtp.py`_
- **2026-08-05** [`d0ce3dadb6`](https://github.com/vllm-project/vllm/commit/d0ce3dadb6) [#50607](https://github.com/vllm-project/vllm/pull/50607)
  [ROCm]: Bump torch 2.12, triton 3.7, torchaudio, torchvision (#50607)
  _Files: `docker/Dockerfile.rocm_base`, `vllm/compilation/caching.py`_
- **2026-08-04** [`7ac2ec7582`](https://github.com/vllm-project/vllm/commit/7ac2ec7582) [#50593](https://github.com/vllm-project/vllm/pull/50593)
  [Kimi-K3][AMD] Fuse AttnRes state updates and norms (#50593)
  _Files: `tests/models/kimi_k3/test_amd_attn_res.py`, `vllm/models/kimi_k3/amd/linear.py`, `vllm/models/kimi_k3/amd/ops/attn_res.py`_
- **2026-08-04** [`385d4c084e`](https://github.com/vllm-project/vllm/commit/385d4c084e) [#50859](https://github.com/vllm-project/vllm/pull/50859)
  [ROCm][AITER] Hotfix for `memory access fault` errors in AITER triton MOE routing (#50859)
  _Files: `tests/models/quantization/test_gpt_oss.py`, `vllm/model_executor/layers/fused_moe/experts/aiter_mxfp4_w4a8_moe.py`_
- **2026-08-04** [`8adc840c45`](https://github.com/vllm-project/vllm/commit/8adc840c45) [#50917](https://github.com/vllm-project/vllm/pull/50917)
  [ROCm][Test] Use BF16 for Jina v5 nano MTEB test (#50917)
  _Files: `tests/models/language/pooling_mteb_test/test_jina.py`_
- **2026-08-03** [`f43e1d26e3`](https://github.com/vllm-project/vllm/commit/f43e1d26e3) [#43615](https://github.com/vllm-project/vllm/pull/43615)
  [ROCm] Enable AITER and FP8 inference on GFX120x (#43615)
  _Files: `vllm/_aiter_ops.py`, `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`, `vllm/compilation/passes/pass_manager.py`, `vllm/model_executor/kernels/linear/scaled_mm/aiter.py` _+8 more__
- **2026-08-03** [`4a3447d200`](https://github.com/vllm-project/vllm/commit/4a3447d200) [#50417](https://github.com/vllm-project/vllm/pull/50417)
  [Bugfix][Model Runner V2] Restore multimodal draft capability detection (#50417)
  _Files: `tests/v1/worker/test_gpu_autoregressive_speculator.py`, `vllm/model_executor/models/__init__.py`, `vllm/model_executor/models/interfaces.py`, `vllm/model_executor/models/llama4_eagle.py` _+8 more__
- **2026-08-03** [`e279f71583`](https://github.com/vllm-project/vllm/commit/e279f71583) [#50728](https://github.com/vllm-project/vllm/pull/50728)
  [ROCm][Test] Fix AITER MXFP4 oracle contract (#50728)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`_
- **2026-08-03** [`8f50685c48`](https://github.com/vllm-project/vllm/commit/8f50685c48) [#50582](https://github.com/vllm-project/vllm/pull/50582)
  [ROCm][Kimi-K3] aiter moe environment variable cleanup (#50582)
  _Files: `vllm/_aiter_ops.py`, `vllm/envs.py`, `vllm/model_executor/layers/fused_moe/experts/rocm_aiter_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py` _+1 more__
- **2026-08-03** [`76d995df2c`](https://github.com/vllm-project/vllm/commit/76d995df2c) [#50726](https://github.com/vllm-project/vllm/pull/50726)
  [CI][ROCm] Export Helion benchmark script in test artifacts (#50726)
  _Files: `.buildkite/test-amd.yaml`, `docker/Dockerfile.rocm`_
- **2026-08-03** [`dd11df04f3`](https://github.com/vllm-project/vllm/commit/dd11df04f3) [#49389](https://github.com/vllm-project/vllm/pull/49389)
  [Misc] Remove deprecated calculate_kv_scales runtime KV scale calculation (#49389)
  _Files: `.buildkite/test-amd.yaml`, `.buildkite/test_areas/compile.yaml`, `.buildkite/test_areas/pytorch.yaml`, `docs/design/metrics.md` _+15 more__

## MoE / Expert Parallel  (45 commits)

- **2026-08-10** [`ba1cdcfcf0`](https://github.com/vllm-project/vllm/commit/ba1cdcfcf0) [#51265](https://github.com/vllm-project/vllm/pull/51265)
  `[Model][Quantization] Add Ling-3.0-flash-fp8 support` (#51265)
  _Files: `tests/quantization/test_quark.py`, `vllm/model_executor/layers/quantization/auto_awq.py`, `vllm/model_executor/layers/quantization/fp8.py`, `vllm/model_executor/layers/quantization/utils/quant_utils.py` _+2 more__
- **2026-08-10** [`3b4c86e489`](https://github.com/vllm-project/vllm/commit/3b4c86e489) [#51419](https://github.com/vllm-project/vllm/pull/51419)
  [Bugfix][Quantization] Fix fp32 weight scale for mxfp4 quantization and per-expert checkpoint mapping (#51419)
  _Files: `vllm/model_executor/layers/fused_moe/routed_experts.py`, `vllm/model_executor/layers/quantization/mxfp4.py`_
- **2026-08-09** [`9b0afeb4f6`](https://github.com/vllm-project/vllm/commit/9b0afeb4f6) [#51458](https://github.com/vllm-project/vllm/pull/51458)
  [Perf] Avoid some more unnecessary GPU<->CPU syncs (#51458)
  _Files: `tests/basic_correctness/test_basic_correctness.py`, `tests/v1/e2e/general/test_mamba_prefix_cache.py`, `tests/v1/logits_processors/utils.py`, `vllm/distributed/kv_transfer/kv_connector/utils.py` _+9 more__
- **2026-08-08** [`0fe9a916e8`](https://github.com/vllm-project/vllm/commit/0fe9a916e8) [#51495](https://github.com/vllm-project/vllm/pull/51495)
  [Bugfix] Fix LFM2 ShortConv prefix breaking quant ignore list (#51495)
  _Files: `vllm/model_executor/models/lfm2.py`, `vllm/model_executor/models/lfm2_moe.py`_
- **2026-08-08** [`700d39b558`](https://github.com/vllm-project/vllm/commit/700d39b558) [#50949](https://github.com/vllm-project/vllm/pull/50949)
  [CPU] Optimize routed FP8/MXFP4 MoE GEMM dispatch (#50949)
  _Files: `csrc/cpu/sgl-kernels/gemm.h`, `csrc/cpu/sgl-kernels/moe_fp8.cpp`, `tests/kernels/moe/test_cpu_quant_fused_moe.py`_
- **2026-08-08** [`5eaa70dac5`](https://github.com/vllm-project/vllm/commit/5eaa70dac5) [#51411](https://github.com/vllm-project/vllm/pull/51411)
  [Bugfix][Quantization] Fix INT8 W8A8 MoE crash in TritonExperts (#51411)
  _Files: `vllm/model_executor/layers/fused_moe/experts/triton_moe.py`_
- **2026-08-07** [`4a11ed5bc4`](https://github.com/vllm-project/vllm/commit/4a11ed5bc4) [#51298](https://github.com/vllm-project/vllm/pull/51298)
  [DSv32/GLM Perf] Skip short prefill topk for dense mha layer, 97.9% kernel level latency reduction (#51298)
  _Files: `vllm/models/deepseek_v32/attention.py`_
- **2026-08-07** [`70456e5e6f`](https://github.com/vllm-project/vllm/commit/70456e5e6f) [#50937](https://github.com/vllm-project/vllm/pull/50937)
  [Bugfix] when loading weights skip empty expert bias if model does not support them (#50937)
  _Files: `tests/kernels/moe/test_moe_weight_loading_padded.py`, `vllm/model_executor/layers/fused_moe/routed_experts.py`_
- **2026-08-07** [`fcde8e1460`](https://github.com/vllm-project/vllm/commit/fcde8e1460) [#49610](https://github.com/vllm-project/vllm/pull/49610)
  [Refactor] refactor humming linear and moe backends to use explicit layer configs (#49610)
  _Files: `requirements/cuda.txt`, `tests/evals/gsm8k/configs/humming/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4-humming.yaml`, `tests/evals/gsm8k/configs/humming/Qwen3-4B-mixed-quant-RTN-humming.yaml`, `tests/evals/gsm8k/configs/humming/config-act-int8.txt` _+33 more__
- **2026-08-07** [`ae934ba8a5`](https://github.com/vllm-project/vllm/commit/ae934ba8a5) [#48355](https://github.com/vllm-project/vllm/pull/48355)
  feat: extended EPLB support for Mistral Large 3 and additional MoE backends (#48355)
  _Files: `tests/distributed/test_eplb_quant_scale_consistency.py`, `tests/kernels/moe/test_flashinfer_cutedsl_nvfp4_moe.py`, `tests/quantization/test_trtllm_nvfp4_hidden_dim_padding.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+12 more__
- **2026-08-07** [`b8db7f4abd`](https://github.com/vllm-project/vllm/commit/b8db7f4abd) [#50833](https://github.com/vllm-project/vllm/pull/50833)
  [Bugfix][Quantization] Fix dynamic INT8 W8A8 MoE config being built as W8A16 (#50833)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/int8.py`_
- **2026-08-07** [`e08111211b`](https://github.com/vllm-project/vllm/commit/e08111211b) [#47106](https://github.com/vllm-project/vllm/pull/47106)
  [Kernel] Support Nvfp4 Cutedsl Moe Swiglu-oai and Relu2(non-gated) Activation (#47106)
  _Files: `tests/kernels/moe/test_flashinfer_cutedsl_layout.py`, `tests/kernels/moe/test_flashinfer_cutedsl_nvfp4_moe.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py` _+5 more__
- **2026-08-06** [`adc3e03517`](https://github.com/vllm-project/vllm/commit/adc3e03517) [#48977](https://github.com/vllm-project/vllm/pull/48977)
  [Mypy Fix] Mypy fix for "vllm/model_executor/models/[aA][bB]" (#48977)
  _Files: `tools/pre_commit/mypy.py`, `vllm/model_executor/layers/mamba/mamba_utils.py`, `vllm/model_executor/models/AXK1.py`, `vllm/model_executor/models/adapters.py` _+19 more__
- **2026-08-06** [`1e05b21d61`](https://github.com/vllm-project/vllm/commit/1e05b21d61) [#51242](https://github.com/vllm-project/vllm/pull/51242)
  Remove the XPU branch of topk_softplus_sqrt (#51242)
  _Files: `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`_
- **2026-08-06** [`22013f74ff`](https://github.com/vllm-project/vllm/commit/22013f74ff) [#51149](https://github.com/vllm-project/vllm/pull/51149)
  Interns2mobius support (#51149)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/config/speculative.py`, `vllm/model_executor/layers/fused_moe/experts/triton_moe.py` _+4 more__
- **2026-08-06** [`872fd5973e`](https://github.com/vllm-project/vllm/commit/872fd5973e) [#51002](https://github.com/vllm-project/vllm/pull/51002)
  [Bugfix][LoRA] Guard TrtLlm BF16 MoE LoRA gate on activation type (#51002)
  _Files: `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`_
- **2026-08-06** [`470297c143`](https://github.com/vllm-project/vllm/commit/470297c143) [#50980](https://github.com/vllm-project/vllm/pull/50980)
  [HPC Attention Backend] hpc attention backend support bf16 kv cache with fp8 weight  (#50980)
  _Files: `vllm/model_executor/layers/fused_moe/hpc_moe.py`, `vllm/model_executor/layers/hpc/rope_norm.py`, `vllm/v1/attention/backends/hpc_attn.py`_
- **2026-08-06** [`2e35c529b8`](https://github.com/vllm-project/vllm/commit/2e35c529b8) [#51038](https://github.com/vllm-project/vllm/pull/51038)
  [Bugfix][Quantization] Fix MXFP4 conversion for FlashInfer CUTLASS (#51038)
  _Files: `tests/kernels/moe/test_ocp_mx_moe.py`, `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`_
- **2026-08-06** [`f85c1d2f84`](https://github.com/vllm-project/vllm/commit/f85c1d2f84) [#51146](https://github.com/vllm-project/vllm/pull/51146)
  K3: remove the add operation for megamoe path (#51146)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-06** [`9f3169960a`](https://github.com/vllm-project/vllm/commit/9f3169960a) [#50942](https://github.com/vllm-project/vllm/pull/50942)
  [MoE] Align TRTLLM MXFP4 autotune buckets (#50942)
  _Files: `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`_
- **2026-08-06** [`7c77868cdf`](https://github.com/vllm-project/vllm/commit/7c77868cdf) [#51125](https://github.com/vllm-project/vllm/pull/51125)
  [Bugfix] Size and iterate w13 by shard count for non-gated MoE (#51125)
  _Files: `tests/quantization/test_auto_gptq.py`, `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/fused_moe/config.py`, `vllm/model_executor/layers/quantization/auto_awq.py` _+12 more__
- **2026-08-05** [`373fe8b83e`](https://github.com/vllm-project/vllm/commit/373fe8b83e) [#51078](https://github.com/vllm-project/vllm/pull/51078)
  [MoE Refactor] Remove MoE legacy code (#51078)
  _Files: `tests/v1/worker/test_gpu_model_runner_v2_eplb.py`, `vllm/distributed/device_communicators/base_device_communicator.py`, `vllm/distributed/elastic_ep/elastic_execute.py`, `vllm/distributed/elastic_ep/elastic_state.py` _+18 more__
- **2026-08-05** [`8f158d0ee2`](https://github.com/vllm-project/vllm/commit/8f158d0ee2) [#44359](https://github.com/vllm-project/vllm/pull/44359)
  [MoE] Share apply_moe_activation support metadata (#44359)
  _Files: `tests/kernels/moe/test_cutlass_moe.py`, `tests/kernels/moe/test_moe.py`, `tests/kernels/moe/test_triton_moe_no_act_mul.py`, `vllm/model_executor/layers/fused_moe/__init__.py` _+9 more__
- **2026-08-05** [`bc37fc970e`](https://github.com/vllm-project/vllm/commit/bc37fc970e) [#50879](https://github.com/vllm-project/vllm/pull/50879)
  Revert [Misc] Avoid importing `nixl_ep` on every `vllm serve` config (#50879) (#51176)
  _Files: `vllm/model_executor/layers/fused_moe/all2all_utils.py`_
- **2026-08-05** [`d4da0c55af`](https://github.com/vllm-project/vllm/commit/d4da0c55af) [#51045](https://github.com/vllm-project/vllm/pull/51045)
  [Model][Frontend] Add Ling 3.0 Flash BF16, MTP, and parser support (#51045)
  _Files: `benchmarks/kernels/benchmark_moe.py`, `docs/models/supported_models.md`, `tests/models/registry.py`, `tests/parser/engine/test_ling3.py` _+11 more__
- **2026-08-05** [`08b8613b7b`](https://github.com/vllm-project/vllm/commit/08b8613b7b) [#48929](https://github.com/vllm-project/vllm/pull/48929)
  [Bugfix][Model] Fix MiniMax-M3 NVFP4 inference correctness (#48929)
  _Files: `tests/kernels/moe/test_flashinfer_moe.py`, `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutlass_moe.py`_
- **2026-08-05** [`beca88e59e`](https://github.com/vllm-project/vllm/commit/beca88e59e) [#51131](https://github.com/vllm-project/vllm/pull/51131)
  [BugFix][K3] Skip moe_intermediate padding when EP is enabled (#51131)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-05** [`7794b1e08b`](https://github.com/vllm-project/vllm/commit/7794b1e08b) [#49397](https://github.com/vllm-project/vllm/pull/49397)
  [Bugfix] Skip Qwen3 deepstack buffers without vision (#49397)
  _Files: `vllm/model_executor/models/qwen3_omni_moe_thinker.py`, `vllm/model_executor/models/qwen3_vl.py`, `vllm/model_executor/models/qwen3_vl_moe.py`_
- **2026-08-05** [`c25093a305`](https://github.com/vllm-project/vllm/commit/c25093a305) [#40372](https://github.com/vllm-project/vllm/pull/40372)
  [Kernel] Batch invariant NVFP4 MoE using cutlass (#40372)
  _Files: `.buildkite/test_areas/misc.yaml`, `csrc/libtorch_stable/quantization/fp4/nvfp4_blockwise_moe_kernel.cu`, `tests/v1/determinism/test_cutlass_batch_invariance.py`, `tests/v1/determinism/test_nvfp4_batch_invariant_scaled_mm.py` _+1 more__
- **2026-08-05** [`6153dbe036`](https://github.com/vllm-project/vllm/commit/6153dbe036) [#50940](https://github.com/vllm-project/vllm/pull/50940)
  [R3] Unify routed expert shape configuration (#50940)
  _Files: `tests/config/test_model_arch_config.py`, `tests/model_executor/test_routed_experts_capture.py`, `vllm/config/model.py`, `vllm/config/model_arch.py` _+3 more__
- **2026-08-04** [`05b7876f50`](https://github.com/vllm-project/vllm/commit/05b7876f50) [#50510](https://github.com/vllm-project/vllm/pull/50510)
  [MoE][Humming] Support SiTU activation for Kimi-K3 (#50510)
  _Files: `vllm/model_executor/layers/fused_moe/experts/fused_humming_moe.py`_
- **2026-08-04** [`edbc4969a7`](https://github.com/vllm-project/vllm/commit/edbc4969a7) [#50697](https://github.com/vllm-project/vllm/pull/50697)
  [Kernel][Inkling] Fuse shared-expert partial addition into the Lamport collective (#50697)
  _Files: `vllm/models/inkling/nvidia/model.py`, `vllm/models/inkling/nvidia/moe.py`, `vllm/models/inkling/nvidia/ops/lamport.py`_
- **2026-08-04** [`d31de3c421`](https://github.com/vllm-project/vllm/commit/d31de3c421) [#50912](https://github.com/vllm-project/vllm/pull/50912)
  [Kimi K3 Perf] option to shard the shared expert for non mega case, 16.98 GiB memory/GPU saved (#50912)
  _Files: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-04** [`7153fd70f6`](https://github.com/vllm-project/vllm/commit/7153fd70f6) [#49558](https://github.com/vllm-project/vllm/pull/49558)
  [Bugfix][MoE] Filter packed expert weights during EP loading (#49558)
  _Files: `tests/model_executor/model_loader/test_ep_weight_filter.py`, `vllm/model_executor/model_loader/ep_weight_filter.py`_
- **2026-08-04** [`7b50d2c0bc`](https://github.com/vllm-project/vllm/commit/7b50d2c0bc) [#50879](https://github.com/vllm-project/vllm/pull/50879)
  [Misc] Avoid importing `nixl_ep` on every `vllm serve` config (#50879)
  _Files: `vllm/model_executor/layers/fused_moe/all2all_utils.py`_
- **2026-08-04** [`5789897aa4`](https://github.com/vllm-project/vllm/commit/5789897aa4) [#49969](https://github.com/vllm-project/vllm/pull/49969)
  [Spec Decode] Add top-k DSpark Markov projection (#49969)
  _Files: `tests/v1/spec_decode/test_dspark_topk.py`, `vllm/config/speculative.py`, `vllm/model_executor/models/qwen3_dspark.py`, `vllm/v1/worker/gpu/spec_decode/dspark/speculator.py`_
- **2026-08-04** [`1eb3694521`](https://github.com/vllm-project/vllm/commit/1eb3694521) [#51014](https://github.com/vllm-project/vllm/pull/51014)
  [Docs] Fix two docs build warnings (#51014)
  _Files: `docs/design/moe_kernel_features.md`, `vllm/model_executor/kernels/linear/mxfp6/base.py`_
- **2026-08-04** [`413e70d52c`](https://github.com/vllm-project/vllm/commit/413e70d52c) [#48825](https://github.com/vllm-project/vllm/pull/48825)
  Perf/h20 moe config e256 n512 (#48825)
  _Files: `vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=NVIDIA_H20.json`_
- **2026-08-03** [`6a9109d865`](https://github.com/vllm-project/vllm/commit/6a9109d865) [#48420](https://github.com/vllm-project/vllm/pull/48420)
  [Bugfix] Fix Qwen3-Omni crash on video with no audio track when use_audio_in_video=True (#48420)
  _Files: `tests/models/multimodal/processing/test_audio_in_video.py`, `vllm/model_executor/models/qwen2_5_omni_thinker.py`, `vllm/model_executor/models/qwen3_omni_moe_thinker.py`_
- **2026-08-03** [`42ab184ea7`](https://github.com/vllm-project/vllm/commit/42ab184ea7) [#50721](https://github.com/vllm-project/vllm/pull/50721)
  [MRV2] Enable routed-experts capture (#50721)
  _Files: `tests/kernels/moe/test_routed_experts_capture_monolithic.py`, `tests/model_executor/test_routed_experts_capture.py`, `tests/v1/executor/test_ray_utils.py`, `tests/v1/worker/test_gpu_model_runner_v2_eplb.py` _+6 more__
- **2026-08-03** [`9ae11a6b89`](https://github.com/vllm-project/vllm/commit/9ae11a6b89) [#50524](https://github.com/vllm-project/vllm/pull/50524)
  [Model] Add K-EXAONE-2.0-750B-A37B (#50524)
  _Files: `docs/models/supported_models.md`, `tests/models/registry.py`, `vllm/model_executor/models/exaone4.py`, `vllm/model_executor/models/exaone_moe.py` _+2 more__
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

## Other  (36 commits)

- **2026-08-10** [`7303c66f68`](https://github.com/vllm-project/vllm/commit/7303c66f68) [#48171](https://github.com/vllm-project/vllm/pull/48171)
  [Bugfix] Fix lfm2 tool parser dropping calls with brackets or newline… (#48171)
  _Files: `tests/tool_parsers/test_lfm2_tool_parser.py`, `tests/tool_parsers/test_utils.py`, `vllm/tool_parsers/lfm2_tool_parser.py`, `vllm/tool_parsers/utils.py`_
- **2026-08-10** [`a123159f7a`](https://github.com/vllm-project/vllm/commit/a123159f7a) [#48798](https://github.com/vllm-project/vllm/pull/48798)
  Add tiering offloading metrics (#48798)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_metrics.py`, `tests/v1/kv_offload/tiering/p2p/test_manager.py`, `tests/v1/kv_offload/tiering/p2p/test_sessions.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py` _+12 more__
- **2026-08-09** [`04d13b5d65`](https://github.com/vllm-project/vllm/commit/04d13b5d65) [#51529](https://github.com/vllm-project/vllm/pull/51529)
  [K3] Allow tpu to import kimi_k3.common (#51529)
  _Files: `vllm/models/kimi_k3/__init__.py`_
- **2026-08-09** [`fbff187d59`](https://github.com/vllm-project/vllm/commit/fbff187d59) [#51455](https://github.com/vllm-project/vllm/pull/51455)
  [Core] Make the GPU sync check thread-local and fix its suppressors (#51455)
  _Files: `tests/utils_/test_gpu_sync_debug.py`, `vllm/utils/gpu_sync_debug.py`_
- **2026-08-08** [`1c008a346c`](https://github.com/vllm-project/vllm/commit/1c008a346c) [#51219](https://github.com/vllm-project/vllm/pull/51219)
  [Bugfix] Close usage telemetry HTTP sessions (#51219)
  _Files: `vllm/usage/usage_lib.py`_
- **2026-08-07** [`c39076feff`](https://github.com/vllm-project/vllm/commit/c39076feff) [#51440](https://github.com/vllm-project/vllm/pull/51440)
  [CI Test] Add specific unit test for mrv2 offloading (#51440)
  _Files: `tests/basic_correctness/test_cpu_offload.py`, `tests/basic_correctness/test_prefetch_offload.py`_
- **2026-08-07** [`99950b0b86`](https://github.com/vllm-project/vllm/commit/99950b0b86) [#51389](https://github.com/vllm-project/vllm/pull/51389)
  [Profiler] Stamp vLLM version/commit into torch profiler trace metadata (#51389)
  _Files: `vllm/profiler/wrapper.py`_
- **2026-08-07** [`a671679e9f`](https://github.com/vllm-project/vllm/commit/a671679e9f) [#51413](https://github.com/vllm-project/vllm/pull/51413)
  [MRv2 Feature] MR v2 weight offloading support (#51413)
  _Files: `tests/basic_correctness/test_cpu_offload.py`, `tests/basic_correctness/test_prefetch_offload.py`, `vllm/v1/worker/gpu/model_runner.py`_
- **2026-08-07** [`448344c0e2`](https://github.com/vllm-project/vllm/commit/448344c0e2) [#50965](https://github.com/vllm-project/vllm/pull/50965)
  [Bugfix] Fix get_open_port() livelock on DP-reserved ports and cover get_open_ports_list (#50965)
  _Files: `tests/utils_/test_network_utils.py`, `vllm/utils/network_utils.py`_
- **2026-08-07** [`4f76c8ad9d`](https://github.com/vllm-project/vllm/commit/4f76c8ad9d) [#50393](https://github.com/vllm-project/vllm/pull/50393)
  [Bugfix][Platform] Stop re-initializing NVML on every device-capability check (fixes #50381) (#50393)
  _Files: `tests/cuda/test_cuda_context.py`, `vllm/platforms/cuda.py`_
- **2026-08-07** [`b1e12d142d`](https://github.com/vllm-project/vllm/commit/b1e12d142d) [#51304](https://github.com/vllm-project/vllm/pull/51304)
  [V1] Copy NaN-in-logits counts to host asynchronously (#51304)
  _Files: `vllm/v1/worker/gpu_model_runner.py`_
- **2026-08-06** [`9464529612`](https://github.com/vllm-project/vllm/commit/9464529612) [#50931](https://github.com/vllm-project/vllm/pull/50931)
  [ModelRunner v2] Enable decoder token-wise pooling (#50931)
  _Files: `tests/model_executor/layers/test_pooler_methods.py`, `tests/models/language/pooling/test_all_pooling_plus_chunked_prefill.py`, `tests/models/language/pooling/test_jina_reranker_v3.py`, `tests/models/language/pooling/test_reward.py` _+4 more__
- **2026-08-06** [`c5d470ac4c`](https://github.com/vllm-project/vllm/commit/c5d470ac4c) [#51210](https://github.com/vllm-project/vllm/pull/51210)
  [ModelRunner V2] Minor indexing optimizations (#51210)
  _Files: `vllm/v1/worker/gpu/input_batch.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pcp_manager.py`_
- **2026-08-06** [`d6af803f43`](https://github.com/vllm-project/vllm/commit/d6af803f43) [#50276](https://github.com/vllm-project/vllm/pull/50276)
  [Bugfix] Fix packed KV block zeroing stride (#50276)
  _Files: `tests/v1/worker/test_kv_block_zeroer.py`, `vllm/v1/worker/utils.py`_
- **2026-08-06** [`62a86318de`](https://github.com/vllm-project/vllm/commit/62a86318de) [#51224](https://github.com/vllm-project/vllm/pull/51224)
  [VocabParallelEmbedding] fix extra_repr fields concat (#51224)
  _Files: `vllm/model_executor/layers/vocab_parallel_embedding.py`_
- **2026-08-06** [`276f0bb5c1`](https://github.com/vllm-project/vllm/commit/276f0bb5c1) [#50946](https://github.com/vllm-project/vllm/pull/50946)
  [XPU] Register fake meta kernel for fp4_gemm (#50946)
  _Files: `vllm/_xpu_ops.py`_
- **2026-08-06** [`2a0323b4e0`](https://github.com/vllm-project/vllm/commit/2a0323b4e0) [#51160](https://github.com/vllm-project/vllm/pull/51160)
  [XPU][Test] Support MultiConnector accuracy testing on XPU (#51160)
  _Files: `tests/v1/kv_connector/nixl_integration/run_multi_connector_accuracy_test.sh`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_
- **2026-08-06** [`47a4e410ba`](https://github.com/vllm-project/vllm/commit/47a4e410ba) [#50183](https://github.com/vllm-project/vllm/pull/50183)
  [Bugfix][Spec Decode] Fix NaN handling in rejection sampler tl.argmax (#50183)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-08-05** [`811622c410`](https://github.com/vllm-project/vllm/commit/811622c410) [#50066](https://github.com/vllm-project/vllm/pull/50066)
  [Refactor][PCP] Make PCPManager construction extensible (#50066)
  _Files: `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/pcp_manager.py`_
- **2026-08-05** [`877975897d`](https://github.com/vllm-project/vllm/commit/877975897d) [#51070](https://github.com/vllm-project/vllm/pull/51070)
  [K3 Perf] Combine multiple all gather together for SP, 1.5~3x kernel level performance improvement (#51070)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-05** [`e76b71f659`](https://github.com/vllm-project/vllm/commit/e76b71f659) [#51179](https://github.com/vllm-project/vllm/pull/51179)
  [CI Bug] Fix `pydantic_core._pydantic_core.ValidationError: Input should be a valid integer` (#51179)
  _Files: `vllm/transformers_utils/model_arch_config_convertor.py`_
- **2026-08-05** [`9833aa53d5`](https://github.com/vllm-project/vllm/commit/9833aa53d5) [#50358](https://github.com/vllm-project/vllm/pull/50358)
  [Bugfix] Fail fast with a clear error when CPU offload region exceeds available space (#50358)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`_
- **2026-08-05** [`5bf32605a9`](https://github.com/vllm-project/vllm/commit/5bf32605a9) [#50448](https://github.com/vllm-project/vllm/pull/50448)
  [Rust Frontend] Deduplicate request preprocessing for `/tokenize` (#50448)
  _Files: `rust/src/chat/src/lib.rs`, `rust/src/server/src/routes/tests.rs`, `rust/src/server/src/routes/tokenize.rs`, `rust/src/server/src/routes/tokenize/types.rs` _+1 more__
- **2026-08-05** [`999dd8b490`](https://github.com/vllm-project/vllm/commit/999dd8b490) [#50526](https://github.com/vllm-project/vllm/pull/50526)
  [XPU] Alias is_current_stream_capturing to XPU in cuda wrapper (#50526)
  _Files: `vllm/v1/worker/xpu_model_runner.py`_
- **2026-08-04** [`7635a9002b`](https://github.com/vllm-project/vllm/commit/7635a9002b) [#49919](https://github.com/vllm-project/vllm/pull/49919)
  [Core] Explicitly manage torch CPU threads in workers (#49919)
  _Files: `tests/utils_/test_torch_utils.py`, `vllm/utils/torch_utils.py`, `vllm/v1/executor/multiproc_executor.py`, `vllm/v1/worker/gpu_worker.py`_
- **2026-08-04** [`122b3d46b6`](https://github.com/vllm-project/vllm/commit/122b3d46b6) [#50915](https://github.com/vllm-project/vllm/pull/50915)
  [Bugfix][CPU] Fix macOS build: std::sqrt is not constexpr under libc++ (#50915)
  _Files: `csrc/cpu/sgl-kernels/fla.cpp`_
- **2026-08-04** [`24c939c47d`](https://github.com/vllm-project/vllm/commit/24c939c47d) [#47104](https://github.com/vllm-project/vllm/pull/47104)
  [XPU] fix collecting oneccl version info (#47104)
  _Files: `vllm/collect_env.py`_
- **2026-08-04** [`0b1c151cbc`](https://github.com/vllm-project/vllm/commit/0b1c151cbc) [#50540](https://github.com/vllm-project/vllm/pull/50540)
  [Rust Frontend] Align tool rendering for Kimi K3 (#50540)
  _Files: `rust/src/chat/src/renderer/kimi_k3/encoding.rs`, `rust/src/chat/src/renderer/kimi_k3/fixtures/dynamic_system_tool_declare_input.json`, `rust/src/chat/src/renderer/kimi_k3/fixtures/dynamic_system_tool_declare_output.txt`, `rust/src/chat/src/renderer/kimi_k3/tests.rs`_
- **2026-08-04** [`adbf08d977`](https://github.com/vllm-project/vllm/commit/adbf08d977) [#50886](https://github.com/vllm-project/vllm/pull/50886)
  [Bugfix][Reasoning] kimi_k3: O(delta) reasoning-end check on the decode path (#50886)
  _Files: `tests/reasoning/test_kimi_k3_reasoning_parser.py`, `vllm/reasoning/kimi_k3_reasoning_parser.py`_
- **2026-08-04** [`41ba11b841`](https://github.com/vllm-project/vllm/commit/41ba11b841) [#50567](https://github.com/vllm-project/vllm/pull/50567)
  [Bugfix][Kimi-K3] Enforce packed rows and op availability in AttnRes dispatch (#50567)
  _Files: `csrc/libtorch_stable/kimi_k3/attn_res_kernel.cu`, `vllm/models/kimi_k3/nvidia/ops/attn_res.py`_
- **2026-08-03** [`c2881ce603`](https://github.com/vllm-project/vllm/commit/c2881ce603) [#50432](https://github.com/vllm-project/vllm/pull/50432)
  [Bugfix][Hybrid] Fix cross-block race on num_accepted in MRv2 align prefix cache (#50432)
  _Files: `vllm/v1/worker/mamba_utils.py`_
- **2026-08-03** [`e578de311c`](https://github.com/vllm-project/vllm/commit/e578de311c) [#50327](https://github.com/vllm-project/vllm/pull/50327)
  [ModelRunnerV2] Fix scalar Mamba state update with int32 mappings (#50327)
  _Files: `tests/v1/worker/test_mamba_hybrid_model_state.py`, `vllm/v1/worker/gpu/model_states/mamba_hybrid.py`_
- **2026-08-03** [`755513d9a2`](https://github.com/vllm-project/vllm/commit/755513d9a2) [#48120](https://github.com/vllm-project/vllm/pull/48120)
  [Hybrid] Stage the postprocess inputs with a single loop over the request list (#48120)
  _Files: `tests/v1/worker/test_mamba_utils.py`, `vllm/v1/worker/mamba_utils.py`_
- **2026-08-03** [`5df9999fcf`](https://github.com/vllm-project/vllm/commit/5df9999fcf) [#50656](https://github.com/vllm-project/vllm/pull/50656)
  [Kimi-K3] Add option to shard the shared expert instead of replicating (#50656)
  _Files: `tests/models/kimi_k3/test_sequence_parallel.py`, `vllm/envs.py`, `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-03** [`32c42c4f2f`](https://github.com/vllm-project/vllm/commit/32c42c4f2f) [#50750](https://github.com/vllm-project/vllm/pull/50750)
  [UX] remove torch compile warning when using breakable cudagraph (#50750)
  _Files: `vllm/config/vllm.py`_
- **2026-08-03** [`5e35a6f4f9`](https://github.com/vllm-project/vllm/commit/5e35a6f4f9) [#50547](https://github.com/vllm-project/vllm/pull/50547)
  cpu_model_runner.py: skip the warm up if CompilationMode.NONE (#50547)
  _Files: `vllm/v1/worker/cpu_model_runner.py`_

## Multimodal  (23 commits)

- **2026-08-09** [`83ad767eed`](https://github.com/vllm-project/vllm/commit/83ad767eed) [#51539](https://github.com/vllm-project/vllm/pull/51539)
  [CI] fix docs on `main` (#51539)
  _Files: `vllm/benchmarks/throughput.py`, `vllm/multimodal/video.py`_
- **2026-08-09** [`cb1a52aee3`](https://github.com/vllm-project/vllm/commit/cb1a52aee3) [#51058](https://github.com/vllm-project/vllm/pull/51058)
  [Build] Upgrade runtime image to Ubuntu 24.04, pick up rdma-core > 44 (#51058)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `docs/getting_started/installation/gpu.cuda.inc.md`_
- **2026-08-08** [`6e18901195`](https://github.com/vllm-project/vllm/commit/6e18901195) [#51435](https://github.com/vllm-project/vllm/pull/51435)
  [Bugfix][MM] Avoid device sync in FusedInputNorm initialization (#51435)
  _Files: `tests/models/multimodal/processing/test_qwen2_vl.py`, `vllm/model_executor/models/vision.py`_
- **2026-08-08** [`d3621c1eb3`](https://github.com/vllm-project/vllm/commit/d3621c1eb3) [#51076](https://github.com/vllm-project/vllm/pull/51076)
  [Bugfix][Multimodal] Fix PyNvVideoCodec video backend returning NCHW instead of NHWC (#51076)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/multimodal/video.py`_
- **2026-08-08** [`d21fed9522`](https://github.com/vllm-project/vllm/commit/d21fed9522) [#51427](https://github.com/vllm-project/vllm/pull/51427)
  [Bugfix][models_multimodal] Remote HF python code misses importing class (#51427)
  _Files: `tests/models/multimodal/conftest.py`_
- **2026-08-08** [`a828536fb5`](https://github.com/vllm-project/vllm/commit/a828536fb5) [#51432](https://github.com/vllm-project/vllm/pull/51432)
  [Bugfix][multi_modal] Fix pos_ids being unitialized for minicpmv2.6 in hf runner (#51432)
  _Files: `tests/models/multimodal/generation/vlm_utils/model_utils.py`_
- **2026-08-07** [`45273b8dcb`](https://github.com/vllm-project/vllm/commit/45273b8dcb) [#51408](https://github.com/vllm-project/vllm/pull/51408)
  [1/N] Harden Transformers modelling backend multi-modal path (#51408)
  _Files: `tests/models/multimodal/processing/test_common.py`, `tests/models/multimodal/processing/test_transformers_audio.py`, `tests/models/multimodal/processing/test_transformers_image.py`, `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-08-07** [`a231c5ceac`](https://github.com/vllm-project/vllm/commit/a231c5ceac) [#51260](https://github.com/vllm-project/vllm/pull/51260)
  [Bugfix] Skip fetching revision for model when model and weights_model are different (#51260)
  _Files: `tests/test_config.py`, `vllm/config/model.py`_
- **2026-08-06** [`d35eb6c440`](https://github.com/vllm-project/vllm/commit/d35eb6c440) [#51046](https://github.com/vllm-project/vllm/pull/51046)
  [CI] Exclude KV-connector subtree from broad source dependencies (#51046)
  _Files: `.buildkite/test_areas/basic_correctness.yaml`, `.buildkite/test_areas/benchmarks.yaml`, `.buildkite/test_areas/distributed.yaml`, `.buildkite/test_areas/engine.yaml` _+9 more__
- **2026-08-06** [`2fa490470d`](https://github.com/vllm-project/vllm/commit/2fa490470d) [#50411](https://github.com/vllm-project/vllm/pull/50411)
  [Model] Fused mm preprocess normalisation on the Device (#50411)
  _Files: `docs/design/mm_processing.md`, `tests/models/multimodal/generation_ppl_test/ppl_utils.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`, `tests/models/multimodal/processing/test_qwen2_vl.py` _+9 more__
- **2026-08-06** [`777b01d1a8`](https://github.com/vllm-project/vllm/commit/777b01d1a8) [#45254](https://github.com/vllm-project/vllm/pull/45254)
  [MM][CG] Support ViT full CUDA graph for Ernie-4.5-VL image inference (#45254)
  _Files: `docs/design/cuda_graphs_multimodal.md`, `examples/generate/multimodal/vision_language_offline.py`, `tests/models/multimodal/generation/test_vit_cudagraph.py`, `vllm/model_executor/models/ernie45_vl.py`_
- **2026-08-06** [`f84df12c6a`](https://github.com/vllm-project/vllm/commit/f84df12c6a) [#48413](https://github.com/vllm-project/vllm/pull/48413)
  [Bugfix][MM] Fix MiniCPM-V placeholder replacement and image processor loading on Transformers v5 (#48413)
  _Files: `tests/models/multimodal/processing/test_minicpmv.py`, `tests/models/registry.py`, `vllm/model_executor/models/minicpmv.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-05** [`b30291cf0c`](https://github.com/vllm-project/vllm/commit/b30291cf0c) [#50390](https://github.com/vllm-project/vllm/pull/50390)
  [EPD] Remove duplicate image preprocessing in EPD and enable preprocess on GPU (#50390)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/config/test_multimodal_config.py`, `vllm/config/ec_transfer.py`, `vllm/config/model.py` _+18 more__
- **2026-08-05** [`e8586b2878`](https://github.com/vllm-project/vllm/commit/e8586b2878) [#51060](https://github.com/vllm-project/vllm/pull/51060)
  [Build] Remove Ubuntu build-stage option from the CUDA dockerfile (#51060)
  _Files: `.buildkite/image_build/image_build_arm64.sh`, `.buildkite/image_build/image_build_torch_nightly.sh`, `.buildkite/release-pipeline.yaml`, `.buildkite/scripts/hardware_ci/run-gh200-test.sh` _+4 more__
- **2026-08-05** [`50c51682a1`](https://github.com/vllm-project/vllm/commit/50c51682a1) [#50275](https://github.com/vllm-project/vllm/pull/50275)
  [Bugfix][EC Connector] Don't stop an encoder-instance request before its images are encoded (#50275)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_epd_proxy.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/outputs.py`_
- **2026-08-05** [`eb3dce9757`](https://github.com/vllm-project/vllm/commit/eb3dce9757) [#50958](https://github.com/vllm-project/vllm/pull/50958)
  [Bugfix][Model] Gemma3n/Gemma4: pad variable-length audio batches (#50958)
  _Files: `tests/models/multimodal/generation/test_gemma_ragged_audio.py`, `vllm/model_executor/models/gemma3n_mm.py`, `vllm/model_executor/models/gemma4_mm.py`, `vllm/model_executor/models/gemma4_unified.py`_
- **2026-08-04** [`7c40d61eaf`](https://github.com/vllm-project/vllm/commit/7c40d61eaf) [#50250](https://github.com/vllm-project/vllm/pull/50250)
  [Bugfix] Flatten >2D multimodal embeddings, not just 3D (#50250)
  _Files: `vllm/model_executor/models/transformers/multimodal.py`_
- **2026-08-04** [`6a9fdf0dc7`](https://github.com/vllm-project/vllm/commit/6a9fdf0dc7) [#50950](https://github.com/vllm-project/vllm/pull/50950)
  [Bugfix] Resolve seq-cls `num_labels` from the top-level config for multimodal checkpoints (#50950)
  _Files: `tests/models/test_adapters.py`, `vllm/model_executor/models/adapters.py`_
- **2026-08-04** [`e98a8774cb`](https://github.com/vllm-project/vllm/commit/e98a8774cb) [#50368](https://github.com/vllm-project/vllm/pull/50368)
  [Rust Frontend][gRPC] Add multimodal image inference (#50368)
  _Files: `rust/Cargo.lock`, `rust/proto/inference.proto`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/multimodal.rs` _+8 more__
- **2026-08-03** [`7f2e78ba4d`](https://github.com/vllm-project/vllm/commit/7f2e78ba4d) [#49056](https://github.com/vllm-project/vllm/pull/49056)
  [Bugfix] Emit a valid media type from encode_{audio,image,video}_url (#49056)
  _Files: `tests/multimodal/test_utils.py`, `vllm/multimodal/utils.py`_
- **2026-08-03** [`9acb7b3699`](https://github.com/vllm-project/vllm/commit/9acb7b3699) [#50839](https://github.com/vllm-project/vllm/pull/50839)
  [CI] And PPL test for multimodal generation models  (#50839)
  _Files: `.buildkite/test_areas/models_multimodal.yaml`, `tests/models/multimodal/generation_ppl_test/__init__.py`, `tests/models/multimodal/generation_ppl_test/ppl_utils.py`, `tests/models/multimodal/generation_ppl_test/test_qwen.py`_
- **2026-08-03** [`89ac407e3d`](https://github.com/vllm-project/vllm/commit/89ac407e3d) [#50716](https://github.com/vllm-project/vllm/pull/50716)
  [Perf] Speed up multimodal placeholder and token-match scanning (#50716)
  _Files: `tests/multimodal/test_processing.py`, `vllm/multimodal/processing/processor.py`_
- **2026-08-03** [`d83eb0b36b`](https://github.com/vllm-project/vllm/commit/d83eb0b36b) [#50755](https://github.com/vllm-project/vllm/pull/50755)
  fix(security): classify DeepStream as GPU backend and enforce pixel limits (#50755)
  _Files: `tests/multimodal/media/test_video.py`, `vllm/multimodal/media/video.py`, `vllm/multimodal/video.py`_

## Quantization  (22 commits)

- **2026-08-10** [`b22afe45ac`](https://github.com/vllm-project/vllm/commit/b22afe45ac) [#51148](https://github.com/vllm-project/vllm/pull/51148)
  [CPU] Enable GPTQ and AWQ quantization for s390x (#51148)
  _Files: `cmake/cpu_extension.cmake`, `csrc/cpu/cpu_types_vxe.hpp`, `csrc/cpu/torch_bindings.cpp`, `docs/getting_started/installation/cpu.md` _+1 more__
- **2026-08-10** [`7ce84b99ce`](https://github.com/vllm-project/vllm/commit/7ce84b99ce) [#51379](https://github.com/vllm-project/vllm/pull/51379)
  [CPU] Restore linear dispatch for small unquantized GEMMs (#51379)
  _Files: `vllm/model_executor/layers/utils.py`_
- **2026-08-10** [`751f2ccdd3`](https://github.com/vllm-project/vllm/commit/751f2ccdd3) [#47205](https://github.com/vllm-project/vllm/pull/47205)
  [Kernel][XPU] Tensor-descriptor operand loads for Triton W8A8 scaled_mm (#47205)
  _Files: `tests/kernels/quantization/test_triton_scaled_mm.py`, `vllm/_custom_ops.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/triton.py` _+1 more__
- **2026-08-07** [`9823714346`](https://github.com/vllm-project/vllm/commit/9823714346) [#51442](https://github.com/vllm-project/vllm/pull/51442)
  [Bugfix] Drop stale layer kwarg from online MXFP4 kernel creation (fix precommit) (#51442)
  _Files: `vllm/model_executor/layers/quantization/online/mxfp4.py`_
- **2026-08-07** [`8d9b52f7c2`](https://github.com/vllm-project/vllm/commit/8d9b52f7c2) [#51365](https://github.com/vllm-project/vllm/pull/51365)
  [XPU] quick fix online quantization UT break (#51365)
  _Files: `tests/quantization/test_online.py`_
- **2026-08-07** [`6b5bec7bed`](https://github.com/vllm-project/vllm/commit/6b5bec7bed) [#45694](https://github.com/vllm-project/vllm/pull/45694)
  [Misc] Add and enable Triton kernel unit tests on XPU (#45694)
  _Files: `tests/kernels/core/test_fused_rms_norm_gated.py`, `tests/kernels/quantization/test_block_int8.py`, `tests/kernels/quantization/test_int8_kernel.py`, `tests/kernels/quantization/test_triton_scaled_mm.py` _+1 more__
- **2026-08-06** [`8170c23c4f`](https://github.com/vllm-project/vllm/commit/8170c23c4f) [#49764](https://github.com/vllm-project/vllm/pull/49764)
  [Quantization] Share online weight scales across TP (#49764)
  _Files: `tests/quantization/test_online.py`, `vllm/model_executor/layers/quantization/online/fp8.py`, `vllm/model_executor/layers/quantization/online/int8.py`, `vllm/model_executor/layers/quantization/online/nvfp4.py` _+1 more__
- **2026-08-06** [`9c22668436`](https://github.com/vllm-project/vllm/commit/9c22668436) [#50029](https://github.com/vllm-project/vllm/pull/50029)
  [Quantization] Preserve precision in online NVFP4 expert packing (#50029)
  _Files: `tests/quantization/test_online.py`, `vllm/model_executor/layers/quantization/online/nvfp4.py`_
- **2026-08-06** [`2dfb8ba590`](https://github.com/vllm-project/vllm/commit/2dfb8ba590) [#50230](https://github.com/vllm-project/vllm/pull/50230)
  [Perf][CUDA] Programmatic dependent launch for the DSA decode kernels (#50230)
  _Files: `csrc/libtorch_stable/quantization/fp4/nvfp4_quant_kernels.cu`, `vllm/models/deepseek_v32/common/kernels.py`_
- **2026-08-06** [`8060260e1d`](https://github.com/vllm-project/vllm/commit/8060260e1d) [#49932](https://github.com/vllm-project/vllm/pull/49932)
  [Linear] [Kernel] add block-wise scaled_mm (#49932)
  _Files: `tests/kernels/quantization/test_block_fp8.py`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py`_
- **2026-08-06** [`b976e980ef`](https://github.com/vllm-project/vllm/commit/b976e980ef) [#50840](https://github.com/vllm-project/vllm/pull/50840)
  [XPU] Route AWQ linear through choose_mp_linear_kernel (#50840)
  _Files: `.buildkite/intel_jobs/quantization.yaml`, `vllm/model_executor/layers/quantization/auto_awq.py`_
- **2026-08-06** [`d779835a11`](https://github.com/vllm-project/vllm/commit/d779835a11) [#48476](https://github.com/vllm-project/vllm/pull/48476)
  [XPU] Support MXFP8 linear weights for INC DeepSeek V4 model (#48476)
  _Files: `vllm/model_executor/kernels/linear/mxfp8/xpu.py`_
- **2026-08-05** [`482c613423`](https://github.com/vllm-project/vllm/commit/482c613423) [#51093](https://github.com/vllm-project/vllm/pull/51093)
  [Bugfix][Humming] Preserve ModelOpt FP8 weight dimensions (#51093)
  _Files: `tests/quantization/test_modelopt.py`, `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-08-05** [`613411a90c`](https://github.com/vllm-project/vllm/commit/613411a90c) [#51177](https://github.com/vllm-project/vllm/pull/51177)
  [CI Bug] Fix `Chunked prefill is required for mamba cache mode 'align'.` (#51177)
  _Files: `tests/quantization/test_experts_int8.py`_
- **2026-08-05** [`2cb3ff88cc`](https://github.com/vllm-project/vllm/commit/2cb3ff88cc) [#50405](https://github.com/vllm-project/vllm/pull/50405)
  [BUGFIX][Quant]Fix test_kv_scale_reload failed (#50405)
  _Files: `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a16_fp8.py`_
- **2026-08-04** [`a5149b2fee`](https://github.com/vllm-project/vllm/commit/a5149b2fee) [#51015](https://github.com/vllm-project/vllm/pull/51015)
  [CI] Stabilize GLM-5.2 PCP evaluation (#51015)
  _Files: `tests/evals/gsm8k/configs/GLM-5.2-NVFP4-TP1-PCP4-EP.yaml`_
- **2026-08-04** [`a1657a0235`](https://github.com/vllm-project/vllm/commit/a1657a0235) [#51003](https://github.com/vllm-project/vllm/pull/51003)
  [Bugfix][Build] Fix DeepGEMM CUDA 12.9 FP8 header visibility (#51003)
  _Files: `cmake/external_projects/deepgemm.cmake`, `tools/install_deepgemm.sh`_
- **2026-08-03** [`0b37d8389f`](https://github.com/vllm-project/vllm/commit/0b37d8389f) [#48861](https://github.com/vllm-project/vllm/pull/48861)
  fix: NVFP4 quantization out_dtype should match model dtype, not torch default (#48861)
  _Files: `vllm/model_executor/layers/quantization/modelopt.py`_
- **2026-08-03** [`0cf49a5d15`](https://github.com/vllm-project/vllm/commit/0cf49a5d15) [#50285](https://github.com/vllm-project/vllm/pull/50285)
  [Refactor] Remove multiple dead codes (#50285)
  _Files: `vllm/compilation/passes/fx_utils.py`, `vllm/compilation/passes/vllm_inductor_pass.py`, `vllm/distributed/parallel_state.py`, `vllm/entrypoints/chat_utils.py` _+18 more__
- **2026-08-03** [`b977407d8b`](https://github.com/vllm-project/vllm/commit/b977407d8b) [#50424](https://github.com/vllm-project/vllm/pull/50424)
  Support quantized DSpark Markov heads (#50424)
  _Files: `vllm/model_executor/models/qwen3_dspark.py`_
- **2026-08-03** [`e481da9508`](https://github.com/vllm-project/vllm/commit/e481da9508) [#49664](https://github.com/vllm-project/vllm/pull/49664)
  [XPU] [Linear] add torch as xpu linear backend (#49664)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `docs/features/quantization/online.md`, `vllm/model_executor/kernels/linear/__init__.py`, `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py` _+1 more__
- **2026-08-03** [`2755489a26`](https://github.com/vllm-project/vllm/commit/2755489a26) [#50807](https://github.com/vllm-project/vllm/pull/50807)
  [INC]  fix w4a4 model (#50807)
  _Files: `tests/quantization/test_auto_round.py`, `vllm/model_executor/layers/quantization/inc/schemes/inc_mxfp4_linear.py`_

## CI / Build  (19 commits)

- **2026-08-10** [`51562de5ab`](https://github.com/vllm-project/vllm/commit/51562de5ab) [#51604](https://github.com/vllm-project/vllm/pull/51604)
  [CI][XPU] Add VLLM_DISABLE_COMPILE_CACHE=1 for other random failed cases in Intel GPU CI (#51604)
  _Files: `.buildkite/intel_jobs/benchmarks_intel.yaml`, `.buildkite/intel_jobs/test-intel.yaml`, `.buildkite/scripts/hardware_ci/run-intel-ci-test.sh`_
- **2026-08-10** [`d89ba6481b`](https://github.com/vllm-project/vllm/commit/d89ba6481b) [#50441](https://github.com/vllm-project/vllm/pull/50441)
  [XPU] bump up xpu kernel to v0.1.12.3 (#50441)
  _Files: `requirements/xpu.txt`_
- **2026-08-09** [`f8d03e7741`](https://github.com/vllm-project/vllm/commit/f8d03e7741) [#51185](https://github.com/vllm-project/vllm/pull/51185)
  [Bugfix][Build] Patch stable string memleak fix from 2.14 for 2.13 (#51185)
  _Files: `CMakeLists.txt`, `cmake/patches/pytorch_stable_string.patch`_
- **2026-08-08** [`12da9b23ae`](https://github.com/vllm-project/vllm/commit/12da9b23ae) [#51451](https://github.com/vllm-project/vllm/pull/51451)
  [CI] Guard remote-code Transformers compatibility (#51451)
  _Files: `tests/models/registry.py`_
- **2026-08-07** [`27d7303802`](https://github.com/vllm-project/vllm/commit/27d7303802) [#51417](https://github.com/vllm-project/vllm/pull/51417)
  [CI] Fix Batch Invariance (B200) (#51417)
  _Files: `requirements/cuda.txt`_
- **2026-08-07** [`b706fd1628`](https://github.com/vllm-project/vllm/commit/b706fd1628) [#51337](https://github.com/vllm-project/vllm/pull/51337)
  [CI][XPU] Work around intermittent segfault in Intel XPU CI with VLLM_DISABLE_COMPILE_CACHE=1 (#51337)
  _Files: `.buildkite/intel_jobs/basic_correctness.yaml`, `.buildkite/intel_jobs/model_executor_intel.yaml`, `.buildkite/intel_jobs/model_runner_v2_intel.yaml`, `.buildkite/intel_jobs/models_distributed_intel.yaml` _+1 more__
- **2026-08-06** [`566c80edf9`](https://github.com/vllm-project/vllm/commit/566c80edf9) [#51271](https://github.com/vllm-project/vllm/pull/51271)
  [CI] Run basic fullgraph correctness on one GPU (#51271)
  _Files: `.buildkite/test_areas/distributed.yaml`, `tests/compile/fullgraph/test_basic_correctness.py`_
- **2026-08-06** [`8c0f029ac7`](https://github.com/vllm-project/vllm/commit/8c0f029ac7) [#50236](https://github.com/vllm-project/vllm/pull/50236)
  [XPU] update warning of XPU Graph (#50236)
  _Files: `.buildkite/intel_jobs/test-intel.yaml`, `vllm/platforms/xpu.py`_
- **2026-08-05** [`e6d67fddb4`](https://github.com/vllm-project/vllm/commit/e6d67fddb4) [#51074](https://github.com/vllm-project/vllm/pull/51074)
  [CI] Prune PyTorch Fullgraph Test (#51074)
  _Files: `.buildkite/test_areas/pytorch.yaml`, `tests/compile/fullgraph/test_basic_correctness.py`, `tests/compile/fullgraph/test_full_graph.py`_
- **2026-08-05** [`a3b86752fb`](https://github.com/vllm-project/vllm/commit/a3b86752fb) [#51095](https://github.com/vllm-project/vllm/pull/51095)
  [CI] Fix CI authorization notification fallback (#51095)
  _Files: `.github/workflows/add_label_automerge.yml`, `.github/workflows/notify-ci-authorized.yml`, `.github/workflows/record-ci-approval.yml`, `.github/workflows/scripts/run_ci_command.py` _+1 more__
- **2026-08-05** [`96e333e81a`](https://github.com/vllm-project/vllm/commit/96e333e81a) [#51127](https://github.com/vllm-project/vllm/pull/51127)
  [CI] Run control-plane workflows on vLLM runners (#51127)
  _Files: `.github/workflows/pre-commit.yml`, `.github/workflows/run-ci-command.yml`_
- **2026-08-05** [`0187f4c88e`](https://github.com/vllm-project/vllm/commit/0187f4c88e) [#50841](https://github.com/vllm-project/vllm/pull/50841)
  [CPU] Enable tcmalloc for s390x (#50841)
  _Files: `docker/Dockerfile.s390x`, `docs/getting_started/installation/cpu.s390x.inc.md`, `setup.py`, `vllm/platforms/cpu.py`_
- **2026-08-05** [`9cd9f8c20b`](https://github.com/vllm-project/vllm/commit/9cd9f8c20b) [#51068](https://github.com/vllm-project/vllm/pull/51068)
  Prune redundant tests points in `correctness_e2e/[test_sequence_parallel,test_async_tp]` (#51068)
  _Files: `.buildkite/test_areas/compile.yaml`, `tests/compile/correctness_e2e/test_async_tp.py`, `tests/compile/correctness_e2e/test_sequence_parallel.py`, `tests/compile/passes/distributed/test_async_tp.py` _+1 more__
- **2026-08-05** [`d16e7f9da4`](https://github.com/vllm-project/vllm/commit/d16e7f9da4) [#51069](https://github.com/vllm-project/vllm/pull/51069)
  [CI] Prune `PyTorch Compilation Unit Tests` (#51069)
  _Files: `.buildkite/test_areas/pytorch.yaml`, `tests/compile/test_aot_compile.py`, `tests/compile/test_dynamic_shapes_compilation.py`_
- **2026-08-05** [`43c4bdcae9`](https://github.com/vllm-project/vllm/commit/43c4bdcae9) [#51087](https://github.com/vllm-project/vllm/pull/51087)
  [CI] Add run-all comment commands (#51087)
  _Files: `.github/workflows/run-ci-command.yml`, `.github/workflows/scripts/run_ci_command.py`, `.github/workflows/scripts/test_run_ci_command.py`_
- **2026-08-04** [`12292d94b2`](https://github.com/vllm-project/vllm/commit/12292d94b2) [#50323](https://github.com/vllm-project/vllm/pull/50323)
  [CI] Detect and fail evals on when NaNs appear in logits (#50323)
  _Files: `tests/basic_correctness/test_basic_correctness.py`, `tests/v1/worker/test_gpu_model_runner.py`, `vllm/envs.py`, `vllm/v1/worker/gpu/async_utils.py` _+2 more__
- **2026-08-04** [`c687c1abb8`](https://github.com/vllm-project/vllm/commit/c687c1abb8) [#51079](https://github.com/vllm-project/vllm/pull/51079)
  [ci] Update CI notify workflow with PR write permissions (#51079)
  _Files: `.github/workflows/notify-ci-authorized.yml`_
- **2026-08-04** [`cb8104839c`](https://github.com/vllm-project/vllm/commit/cb8104839c) [#50199](https://github.com/vllm-project/vllm/pull/50199)
  [XPU][CI]Adjust Samplers test ENV for Intel GPU (#50199)
  _Files: `.buildkite/intel_jobs/samplers_intel.yaml`_
- **2026-08-04** [`74295e3bd4`](https://github.com/vllm-project/vllm/commit/74295e3bd4) [#50926](https://github.com/vllm-project/vllm/pull/50926)
  [CI][Bugfix] Fix flaky `test_store_orders_after_compute_write` (#50926)
  _Files: `tests/v1/simple_kv_offload/test_worker.py`_

## Scheduler / Engine  (18 commits)

- **2026-08-10** [`243c63baf5`](https://github.com/vllm-project/vllm/commit/243c63baf5) [#51603](https://github.com/vllm-project/vllm/pull/51603)
  [V1][Scheduler] Apply Mamba alignment before encoder caps (#51603)
  _Files: `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-10** [`61c1dd0966`](https://github.com/vllm-project/vllm/commit/61c1dd0966) [#49579](https://github.com/vllm-project/vllm/pull/49579)
  [EC Connector] Call to EC Connector update_connector_output from scheduler (#49579)
  _Files: `tests/v1/core/test_async_scheduler.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-10** [`0820125ae9`](https://github.com/vllm-project/vllm/commit/0820125ae9) [#50528](https://github.com/vllm-project/vllm/pull/50528)
  [Bugfix][Parser] Emit REASONING_END for Inkling tool calls that follow no thinking block (#50528)
  _Files: `tests/parser/engine/test_engine.py`, `tests/parser/engine/test_inkling.py`, `vllm/parser/engine/streaming_parser_engine.py`, `vllm/parser/inkling.py`_
- **2026-08-09** [`dedbf6be8b`](https://github.com/vllm-project/vllm/commit/dedbf6be8b) [#48668](https://github.com/vllm-project/vllm/pull/48668)
  [V1][Metrics] Preserve prefix-cache stats on zero-output steps (#48668)
  _Files: `vllm/v1/engine/llm_engine.py`_
- **2026-08-08** [`d608dfabfd`](https://github.com/vllm-project/vllm/commit/d608dfabfd) [#51438](https://github.com/vllm-project/vllm/pull/51438)
  [Bugfix][MRV2] Reserve spec-decode lookahead blocks in V2 warmup (#51438)
  _Files: `tests/v1/worker/test_gpu_warmup_blocks.py`, `vllm/config/vllm.py`, `vllm/v1/core/sched/scheduler.py`, `vllm/v1/worker/gpu/warmup.py`_
- **2026-08-08** [`1c1077c6cc`](https://github.com/vllm-project/vllm/commit/1c1077c6cc) [#49876](https://github.com/vllm-project/vllm/pull/49876)
  [Bugfix][Parser] Confirm reasoning end when an Inkling content block opens (#49876)
  _Files: `tests/parser/engine/test_inkling.py`, `vllm/parser/inkling.py`_
- **2026-08-08** [`75231eff2f`](https://github.com/vllm-project/vllm/commit/75231eff2f) [#51391](https://github.com/vllm-project/vllm/pull/51391)
  [Bugfix][Parser] Prevent Inkling block-end leakage with tools (#51391)
  _Files: `tests/parser/engine/test_inkling.py`, `tests/parser/engine/test_parser_engine.py`, `vllm/parser/engine/streaming_parser_engine.py`_
- **2026-08-08** [`58d3918e3e`](https://github.com/vllm-project/vllm/commit/58d3918e3e) [#51468](https://github.com/vllm-project/vllm/pull/51468)
  [BugFix] Preserve divergent FA hits with external Mamba state (#51468)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_scheduler.py`, `vllm/v1/core/kv_cache_manager.py`_
- **2026-08-08** [`22a175921c`](https://github.com/vllm-project/vllm/commit/22a175921c) [#51469](https://github.com/vllm-project/vllm/pull/51469)
  [BugFix] Reject invalid data-parallel RPC ports (#51469)
  _Files: `tests/test_config.py`, `vllm/config/parallel.py`, `vllm/engine/arg_utils.py`, `vllm/v1/engine/utils.py`_
- **2026-08-07** [`dd856e48bb`](https://github.com/vllm-project/vllm/commit/dd856e48bb) [#51222](https://github.com/vllm-project/vllm/pull/51222)
  [Bugfix][EPD][Model Runner V2] Skip gather mm embeddings for encoder only instance (#51222)
  _Files: `tests/v1/core/test_scheduler.py`, `tests/v1/worker/test_encoder_runner.py`, `vllm/v1/worker/gpu/model_runner.py`, `vllm/v1/worker/gpu/model_states/default.py` _+1 more__
- **2026-08-07** [`72c0d67657`](https://github.com/vllm-project/vllm/commit/72c0d67657) [#46727](https://github.com/vllm-project/vllm/pull/46727)
  [Feat] Support thinking_token_budget in Model Runner V2 (#46727)
  _Files: `benchmarks/kernels/benchmark_thinking_budget.py`, `tests/entrypoints/openai/chat_completion/test_thinking_token_budget.py`, `tests/v1/worker/test_gpu_thinking_budget.py`, `vllm/config/reasoning.py` _+6 more__
- **2026-08-06** [`4d341ca829`](https://github.com/vllm-project/vllm/commit/4d341ca829) [#49206](https://github.com/vllm-project/vllm/pull/49206)
  fix: resolve silent request skipping in PRIORITY scheduling (#49206)
  _Files: `tests/v1/core/test_priority_preemption_bug.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-06** [`7b9f2dad89`](https://github.com/vllm-project/vllm/commit/7b9f2dad89) [#43417](https://github.com/vllm-project/vllm/pull/43417)
  [Frontend] Watch frontend processes during engine startup (#43417)
  _Files: `tests/v1/engine/test_core_engine_actor_manager.py`, `tests/v1/engine/test_startup_watch_processes.py`, `vllm/entrypoints/cli/serve.py`, `vllm/v1/engine/core_client.py` _+1 more__
- **2026-08-06** [`c56f169d9a`](https://github.com/vllm-project/vllm/commit/c56f169d9a) [#51113](https://github.com/vllm-project/vllm/pull/51113)
  [Bugfix] Keep mamba align prefill chunks block-aligned past last_cache_position (#51113)
  _Files: `tests/v1/core/test_mamba_align_chunk_split.py`, `vllm/v1/core/sched/scheduler.py`_
- **2026-08-06** [`8cfa01cdd2`](https://github.com/vllm-project/vllm/commit/8cfa01cdd2) [#49212](https://github.com/vllm-project/vllm/pull/49212)
  [BugFix] Dense multinode DP rescope with regression test (#49212)
  _Files: `tests/test_config.py`, `vllm/config/parallel.py`, `vllm/v1/engine/core.py`_
- **2026-08-05** [`77b519912b`](https://github.com/vllm-project/vllm/commit/77b519912b) [#51050](https://github.com/vllm-project/vllm/pull/51050)
  [CI][Bugfix] Fix `test_shutdown_on_engine_failure` startup deadlock (#51050)
  _Files: `tests/entrypoints/openai/completion/test_shutdown.py`_
- **2026-08-04** [`f9c74b4b9c`](https://github.com/vllm-project/vllm/commit/f9c74b4b9c) [#50991](https://github.com/vllm-project/vllm/pull/50991)
  [Mamba] enable prefix cache by default (#50991)
  _Files: `tests/models/language/generation/test_hybrid.py`, `vllm/config/cache.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/models/config.py`_
- **2026-08-03** [`f57123aa2d`](https://github.com/vllm-project/vllm/commit/f57123aa2d) [#48048](https://github.com/vllm-project/vllm/pull/48048)
  feat(frontend): session id plumbing into requests (#48048)
  _Files: `rust/proto/inference.proto`, `rust/src/chat/src/lib.rs`, `rust/src/chat/src/request.rs`, `rust/src/engine-core-client/src/protocol/request.rs` _+35 more__

## Attention  (18 commits)

- **2026-08-09** [`f18e10a7e1`](https://github.com/vllm-project/vllm/commit/f18e10a7e1) [#50892](https://github.com/vllm-project/vllm/pull/50892)
  Bump Flashinfer version to 0.6.16.post3 (#50892)
  _Files: `docker/Dockerfile`, `docker/versions.json`, `requirements/cuda.txt`, `vllm/model_executor/warmup/kernel_warmup.py` _+1 more__
- **2026-08-09** [`eb24bc38cf`](https://github.com/vllm-project/vllm/commit/eb24bc38cf) [#51161](https://github.com/vllm-project/vllm/pull/51161)
  [Bugfix][KV Offload] Handle chunked local attention in offloading scheduler (#51161)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-08-08** [`9e6be4a72b`](https://github.com/vllm-project/vllm/commit/9e6be4a72b) [#50365](https://github.com/vllm-project/vllm/pull/50365)
  [Perf][Sparse MLA] Drop the atomic contention in the index remap (#50365)
  _Files: `tests/v1/attention/test_indexer_dcp_localize.py`, `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/v1/attention/backends/mla/sparse_utils.py`_
- **2026-08-07** [`1c94e8dc7d`](https://github.com/vllm-project/vllm/commit/1c94e8dc7d) [#45187](https://github.com/vllm-project/vllm/pull/45187)
  Add NVFP4 KV 4-over-6 scale search (#45187)
  _Files: `csrc/libtorch_stable/cache_kernels.cu`, `csrc/libtorch_stable/nvfp4_kv_cache_kernels.cu`, `tests/kernels/attention/test_attention_selector.py`, `tests/kernels/attention/test_cache.py` _+7 more__
- **2026-08-07** [`56a4b63d44`](https://github.com/vllm-project/vllm/commit/56a4b63d44) [#50585](https://github.com/vllm-project/vllm/pull/50585)
  [K3 Perf] Optimize k3 dspark fused kv, 4.5~4.6x kernel performance improvement (#50585)
  _Files: `tests/models/test_dspark_mla.py`, `vllm/models/kimi_k3/nvidia/dspark_mla.py`_
- **2026-08-07** [`4eccf906ca`](https://github.com/vllm-project/vllm/commit/4eccf906ca) [#44857](https://github.com/vllm-project/vllm/pull/44857)
  [Attention] Mamba attention module refactor - Final part (#44857)
  _Files: `vllm/model_executor/layers/mamba/short_conv.py`_
- **2026-08-06** [`41e7746b82`](https://github.com/vllm-project/vllm/commit/41e7746b82) [#49599](https://github.com/vllm-project/vllm/pull/49599)
  Update vllm to point to flash-attention commit that builds FA3 with torch stable API. (Retry) (#49599)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/vllm_flash_attn.cmake`_
- **2026-08-06** [`13726c80fe`](https://github.com/vllm-project/vllm/commit/13726c80fe) [#49453](https://github.com/vllm-project/vllm/pull/49453)
  [CPU] Add MLA backend so DeepSeek-V2/V3 can run on CPU (#49453)
  _Files: `csrc/cpu/cpu_types_arm.hpp`, `csrc/cpu/mla_decode.cpp`, `tests/v1/attention/test_cpu_mla_backend.py`, `vllm/platforms/cpu.py` _+2 more__
- **2026-08-06** [`2e09247c2d`](https://github.com/vllm-project/vllm/commit/2e09247c2d) [#51215](https://github.com/vllm-project/vllm/pull/51215)
  [Docs] List Intel XPU attention backends (#51215)
  _Files: `docs/getting_started/quickstart.md`_
- **2026-08-05** [`66b3c0e61f`](https://github.com/vllm-project/vllm/commit/66b3c0e61f) [#50294](https://github.com/vllm-project/vllm/pull/50294)
  [Kernel][Model] Optimize FA4 mm_prefix range lookup (#50294)
  _Files: `tests/v1/attention/test_mm_prefix.py`, `vllm/model_executor/models/gemma4_mm.py`, `vllm/v1/attention/backend.py`, `vllm/v1/attention/backends/flash_attn.py` _+1 more__
- **2026-08-05** [`cd930c8e78`](https://github.com/vllm-project/vllm/commit/cd930c8e78) [#38771](https://github.com/vllm-project/vllm/pull/38771)
  [Bugfix] Fix MLA kv_b_proj activation dtype with Marlin FP8 (#38771)
  _Files: `vllm/model_executor/layers/attention/mla_attention.py`_
- **2026-08-05** [`c416f15710`](https://github.com/vllm-project/vllm/commit/c416f15710) [#50404](https://github.com/vllm-project/vllm/pull/50404)
  [Model] Fix Kimi-K3 MLA with disabled context parallelism (#50404)
  _Files: `vllm/models/kimi_k3/nvidia/mla.py`_
- **2026-08-04** [`8ae8337ffa`](https://github.com/vllm-project/vllm/commit/8ae8337ffa) [#50911](https://github.com/vllm-project/vllm/pull/50911)
  [Spec Decode] Enable fused non-causal TokenSpeed MLA for DSpark (#50911)
  _Files: `tests/v1/attention/test_mla_backends.py`, `vllm/v1/attention/backends/mla/tokenspeed_mla.py`_
- **2026-08-04** [`52c0e3cb08`](https://github.com/vllm-project/vllm/commit/52c0e3cb08) [#50157](https://github.com/vllm-project/vllm/pull/50157)
  [Kernel] Add support for Flashinfer Mamba SSU algorithm selection (#50157)
  _Files: `tests/kernels/mamba/test_ssu_dispatch.py`, `vllm/config/mamba.py`, `vllm/engine/arg_utils.py`, `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`_
- **2026-08-04** [`199644d410`](https://github.com/vllm-project/vllm/commit/199644d410) [#50906](https://github.com/vllm-project/vllm/pull/50906)
  [Bugfix][Attention] Guard sparse MLA masked MHA workspace (#50906)
  _Files: `tests/v1/attention/test_sparse_mla_backends.py`, `vllm/model_executor/layers/attention/mla_attention.py`, `vllm/model_executor/layers/attention/sparse_mla_attention.py`_
- **2026-08-04** [`59b2fdfc4e`](https://github.com/vllm-project/vllm/commit/59b2fdfc4e) [#48250](https://github.com/vllm-project/vllm/pull/48250)
  Support MLA properly in the Transformers modeling backend (#48250)
  _Files: `tests/models/transformers/fusers/test_mla.py`, `tests/models/transformers/test_backend.py`, `vllm/config/model.py`, `vllm/model_executor/models/transformers/__init__.py` _+5 more__
- **2026-08-04** [`11f88260a2`](https://github.com/vllm-project/vllm/commit/11f88260a2) [#50818](https://github.com/vllm-project/vllm/pull/50818)
  [Kimi-K3] Migrate FlashKDA to PyTorch stable ABI (#50818)
  _Files: `.buildkite/check-torch-abi.py`, `cmake/external_projects/flashkda.cmake`, `csrc/flashkda_registration.cpp`_
- **2026-08-03** [`65cf1276a2`](https://github.com/vllm-project/vllm/commit/65cf1276a2) [#50776](https://github.com/vllm-project/vllm/pull/50776)
  [Kernel] Skip fully masked key blocks in windowed Triton prefill (#50776)
  _Files: `vllm/v1/attention/ops/triton_prefill_attention.py`_

## Disaggregation / PD  (17 commits)

- **2026-08-10** [`11ba93f364`](https://github.com/vllm-project/vllm/commit/11ba93f364) [#50999](https://github.com/vllm-project/vllm/pull/50999)
  [BugFix] Use file:// rendezvous for single-node executors to eliminate startup port races (#50999)
  _Files: `tests/distributed/test_file_store.py`, `vllm/distributed/parallel_state.py`, `vllm/utils/network_utils.py`, `vllm/v1/executor/multiproc_executor.py` _+2 more__
- **2026-08-09** [`d6941300fc`](https://github.com/vllm-project/vllm/commit/d6941300fc) [#50344](https://github.com/vllm-project/vllm/pull/50344)
  [BugFix] Scope divergent hybrid cache hits to capable connectors (#50344)
  _Files: `tests/v1/core/prefix_cache/test_partial_prefix_cache_hits.py`, `tests/v1/core/test_scheduler.py`, `tests/v1/kv_connector/unit/test_multi_connector.py`, `tests/v1/kv_connector/unit/utils.py` _+4 more__
- **2026-08-08** [`f7ef489e93`](https://github.com/vllm-project/vllm/commit/f7ef489e93) [#50960](https://github.com/vllm-project/vllm/pull/50960)
  [Bugfix] Fix ZMQ port TOCTOU race in shm_broadcast MessageQueue (#50960)
  _Files: `tests/distributed/test_shm_broadcast.py`, `vllm/distributed/device_communicators/shm_broadcast.py`_
- **2026-08-07** [`47228db84c`](https://github.com/vllm-project/vllm/commit/47228db84c) [#48534](https://github.com/vllm-project/vllm/pull/48534)
  [Bugfix][KV-transfer] MoRIIO: per-layer READ-completion barrier in wait_for_layer_load (#48534)
  _Files: `tests/v1/kv_connector/unit/test_moriio_tp_ack.py`, `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector.py`_
- **2026-08-07** [`5ec47f3e48`](https://github.com/vllm-project/vllm/commit/5ec47f3e48) [#50234](https://github.com/vllm-project/vllm/pull/50234)
  [PD][PushConnector] Record last activity of remotes to allow clean up of stale ones (#50234)
  _Files: `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/push_worker.py`_
- **2026-08-07** [`58fcaa0baa`](https://github.com/vllm-project/vllm/commit/58fcaa0baa) [#49644](https://github.com/vllm-project/vllm/pull/49644)
  [Feat][Core] Add disk offloading support to SimpleCPUOffloadConnector (#49644)
  _Files: `vllm/distributed/kv_transfer/kv_connector/v1/simple_cpu_offload_connector.py`, `vllm/v1/simple_kv_offload/disk_backend.py`, `vllm/v1/simple_kv_offload/manager.py`, `vllm/v1/simple_kv_offload/worker.py`_
- **2026-08-07** [`21ea5b4fa1`](https://github.com/vllm-project/vllm/commit/21ea5b4fa1) [#50902](https://github.com/vllm-project/vllm/pull/50902)
  [rl] Stateful Trainer Send: NCCL + Sparse NCCL [3/N] (#50902)
  _Files: `examples/rl/rlhf_async_new_apis.py`, `examples/rl/rlhf_http_nccl.py`, `examples/rl/rlhf_nccl.py`, `examples/rl/rlhf_nccl_fsdp_ep.py` _+10 more__
- **2026-08-07** [`c810e5ee99`](https://github.com/vllm-project/vllm/commit/c810e5ee99) [#51100](https://github.com/vllm-project/vllm/pull/51100)
  [Bugfix] Fix Mamba all-mode CPU offload boundary alignment (#51100)
  _Files: `tests/v1/kv_connector/unit/test_offloading_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-08-06** [`d54b58cc48`](https://github.com/vllm-project/vllm/commit/d54b58cc48) [#51107](https://github.com/vllm-project/vllm/pull/51107)
  [Hardware] Use torch.accelerator.empty_host_cache() for host cache cl… (#51107)
  _Files: `vllm/distributed/parallel_state.py`_
- **2026-08-06** [`d36f24b66a`](https://github.com/vllm-project/vllm/commit/d36f24b66a) [#48069](https://github.com/vllm-project/vllm/pull/48069)
  [KV Connector][Mooncake] Add tenant ID support to MooncakeStoreConnector (#48069)
  _Files: `docs/features/mooncake_store_connector_usage.md`, `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-08-05** [`14e57ad47d`](https://github.com/vllm-project/vllm/commit/14e57ad47d) [#51067](https://github.com/vllm-project/vllm/pull/51067)
  [Docker][KVConnector] Install mooncake from official wheels instead of a custom build (#51067)
  _Files: `.buildkite/release-pipeline.yaml`, `docker/Dockerfile`, `docs/features/mooncake_connector_usage.md`_
- **2026-08-05** [`fd859d2e06`](https://github.com/vllm-project/vllm/commit/fd859d2e06) [#44956](https://github.com/vllm-project/vllm/pull/44956)
  [KV Connector][Mooncake] Add store group semantics (#44956)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-08-05** [`ffee32460d`](https://github.com/vllm-project/vllm/commit/ffee32460d) [#48061](https://github.com/vllm-project/vllm/pull/48061)
  [BugFix][Mooncake] Use global data_parallel_index for the DP engine index (#48061)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/mooncake_utils.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`_
- **2026-08-04** [`4f819f801b`](https://github.com/vllm-project/vllm/commit/4f819f801b) [#38390](https://github.com/vllm-project/vllm/pull/38390)
  [Model Runner v2] E/P/D disaggregation support (#38390)
  _Files: `examples/disaggregated/disaggregated_encoder/disagg_1e1pd_example.sh`, `vllm/config/vllm.py`, `vllm/v1/worker/gpu/block_table.py`, `vllm/v1/worker/gpu/ec_connector.py` _+3 more__
- **2026-08-04** [`f42761204f`](https://github.com/vllm-project/vllm/commit/f42761204f) [#45043](https://github.com/vllm-project/vllm/pull/45043)
  llmd+vllm+mori-ep(inter node wide-ep)+mori-io(write) for 2p2d with dp=ep=16 tp=1 (#45043)
  _Files: `examples/disaggregated/disaggregated_serving/moriio_toy_proxy_server.py`, `tests/v1/kv_connector/unit/test_moriio_connector.py`, `tests/v1/kv_connector/unit/test_moriio_routing.py`, `tests/v1/kv_connector/unit/test_moriio_tp_ack.py` _+4 more__
- **2026-08-03** [`8ba87e0181`](https://github.com/vllm-project/vllm/commit/8ba87e0181) [#46844](https://github.com/vllm-project/vllm/pull/46844)
  [CI] Mooncake PD integration tests (#46844)
  _Files: `.buildkite/scripts/install-kv-connectors.sh`, `.buildkite/test_areas/disaggregated_mooncake.yaml`, `docs/features/mooncake_connector_usage.md`, `requirements/kv_connectors.txt` _+5 more__
- **2026-08-03** [`ad0bf3963e`](https://github.com/vllm-project/vllm/commit/ad0bf3963e) [#50266](https://github.com/vllm-project/vllm/pull/50266)
  [CI] KimiLinear PD in nightlies  (#50266)
  _Files: `.buildkite/test_areas/disaggregated.yaml`, `tests/v1/kv_connector/nixl_integration/test_accuracy.py`_

## Models  (16 commits)

- **2026-08-10** [`70b84f0bcb`](https://github.com/vllm-project/vllm/commit/70b84f0bcb) [#49797](https://github.com/vllm-project/vllm/pull/49797)
  Fix Gemma 4 for upcoming Transformers version (#49797)
  _Files: `tests/config/test_model_arch_config.py`, `tests/models/transformers/fusers/test_linear.py`, `vllm/config/model.py`, `vllm/config/model_arch.py` _+11 more__
- **2026-08-08** [`653ebb52df`](https://github.com/vllm-project/vllm/commit/653ebb52df) [#40116](https://github.com/vllm-project/vllm/pull/40116)
  Add torch compile for qwen3_vl encoder (#40116)
  _Files: `vllm/model_executor/models/qwen3_vl.py`_
- **2026-08-07** [`e644c8cd8c`](https://github.com/vllm-project/vllm/commit/e644c8cd8c) [#51434](https://github.com/vllm-project/vllm/pull/51434)
  [Perf] Optimize DeepSeek V3.2 sequence parallelism (#51434)
  _Files: `tests/models/deepseek_v32/test_sequence_parallel.py`, `vllm/models/deepseek_v32/nvidia/model.py`, `vllm/models/deepseek_v32/nvidia/mtp.py`_
- **2026-08-07** [`c8fe1d5715`](https://github.com/vllm-project/vllm/commit/c8fe1d5715) [#51310](https://github.com/vllm-project/vllm/pull/51310)
  [Spec Decode] Register Qwen3.6 dSpark acceptance coverage (#51310)
  _Files: `tests/evals/gsm8k/gsm8k_eval.py`, `tests/v1/e2e/spec_decode/acceptance_rates/dspark/test_dspark.py`_
- **2026-08-07** [`0df620d429`](https://github.com/vllm-project/vllm/commit/0df620d429) [#51288](https://github.com/vllm-project/vllm/pull/51288)
  [Test] Add packed DeepSeek-V4 KV zeroer geometry regression (#51288)
  _Files: `tests/v1/worker/test_dsv4_packed_zeroer_geometry.py`_
- **2026-08-07** [`5ac2684976`](https://github.com/vllm-project/vllm/commit/5ac2684976) [#51293](https://github.com/vllm-project/vllm/pull/51293)
  [CI] Re-enable FI autotune in GSM8K config for Qwen3.5-35B-A3B (#51293)
  _Files: `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-DEP2.yaml`_
- **2026-08-06** [`5fba75aefe`](https://github.com/vllm-project/vllm/commit/5fba75aefe) [#51249](https://github.com/vllm-project/vllm/pull/51249)
  [Bugfix][Model] Add missing fused_qkv_a_proj to Kimi-Linear packed_modules_mapping (#51249)
  _Files: `vllm/models/kimi_k3/nvidia/model.py`_
- **2026-08-06** [`febea17f6a`](https://github.com/vllm-project/vllm/commit/febea17f6a) [#50355](https://github.com/vllm-project/vllm/pull/50355)
  [Model] Fix weight prefix mapping for native Qwen3.5 text-only checkp… (#50355)
  _Files: `tests/models/registry.py`, `vllm/model_executor/models/qwen3_5.py`_
- **2026-08-05** [`a9b39d6dcb`](https://github.com/vllm-project/vllm/commit/a9b39d6dcb) [#51153](https://github.com/vllm-project/vllm/pull/51153)
  [Bugfix] Enable chunked prefill for qwen3.5-0.8B ppl test (#51153)
  _Files: `tests/models/language/generation_ppl_test/test_qwen.py`_
- **2026-08-04** [`3756bf1e2b`](https://github.com/vllm-project/vllm/commit/3756bf1e2b) [#49792](https://github.com/vllm-project/vllm/pull/49792)
  [Kernel][SM100] Add a CuTeDSL fused query kernel (#49792)
  _Files: `benchmarks/kernels/benchmark_fused_q_cutedsl.py`, `vllm/cute_utils/__init__.py`, `vllm/cute_utils/cvt.py`, `vllm/models/deepseek_v32/common/kernels.py` _+2 more__
- **2026-08-04** [`166f4e2dc3`](https://github.com/vllm-project/vllm/commit/166f4e2dc3) [#50867](https://github.com/vllm-project/vllm/pull/50867)
  fix: fuse weightless RMSNorms at their declared width (#50867)
  _Files: `tests/models/transformers/fusers/test_rms_norm.py`, `vllm/model_executor/models/transformers/fusers/rms_norm.py`_
- **2026-08-04** [`7743486190`](https://github.com/vllm-project/vllm/commit/7743486190) [#50580](https://github.com/vllm-project/vllm/pull/50580)
  [Frontend] DeepSeek V4 0731 reasoning effort prompts & mappings (#50580)
  _Files: `rust/src/chat/src/renderer/deepseek_v4/encoding.rs`, `rust/src/chat/src/renderer/deepseek_v4/tests.rs`, `tests/tokenizers_/test_deepseek_v4.py`, `vllm/tokenizers/deepseek_v4.py` _+1 more__
- **2026-08-03** [`c810937573`](https://github.com/vllm-project/vllm/commit/c810937573) [#49791](https://github.com/vllm-project/vllm/pull/49791)
  [Kernel] Extend CuTe DSL skinny GEMM to GLM-5.2 (#49791)
  _Files: `csrc/libtorch_stable/dsv3_fused_a_gemm.cu`, `tests/kernels/test_bf16_skinny_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/_skinny_gemm.py`, `vllm/model_executor/kernels/linear/cute_dsl/skinny_gemm.py` _+3 more__
- **2026-08-03** [`1c0d207915`](https://github.com/vllm-project/vllm/commit/1c0d207915) [#50777](https://github.com/vllm-project/vllm/pull/50777)
  [Bugfix] Default Gemma3 Model intermediate_tensors to None (#50777)
  _Files: `vllm/model_executor/models/gemma3.py`_
- **2026-08-03** [`e42c230e4f`](https://github.com/vllm-project/vllm/commit/e42c230e4f) [#50766](https://github.com/vllm-project/vllm/pull/50766)
  [Bugfix] serving_llama70B_tp4 benchmark was silently running at tensor_parallel_size=1 (#50766)
  _Files: `.buildkite/performance-benchmarks/tests/serving-tests.json`_
- **2026-08-03** [`9a4fd57cac`](https://github.com/vllm-project/vllm/commit/9a4fd57cac) [#50688](https://github.com/vllm-project/vllm/pull/50688)
  [Model] Support jina-embeddings-v5-text-nano (EuroBERT encoder backbone) (#50688)
  _Files: `docs/models/pooling_models/embed.md`, `tests/models/language/pooling/test_jina_embeddings_v5.py`, `tests/models/language/pooling_mteb_test/mteb_embed_utils.py`, `tests/models/language/pooling_mteb_test/test_jina.py` _+2 more__

## KV Cache / Offload  (14 commits)

- **2026-08-10** [`81840a172f`](https://github.com/vllm-project/vllm/commit/81840a172f) [#48414](https://github.com/vllm-project/vllm/pull/48414)
  [KV Connector] Canonical CPU layout for parallelism-agnostic KV offload (#48414)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_config.py`, `tests/v1/kv_offload/cpu/test_canonical_layout.py`, `tests/v1/kv_offload/cpu/test_gpu_worker.py`, `tests/v1/kv_offload/cpu/test_shared_offload_region.py` _+8 more__
- **2026-08-09** [`c423998642`](https://github.com/vllm-project/vllm/commit/c423998642) [#51243](https://github.com/vllm-project/vllm/pull/51243)
  [KV Offload] Emit self-describing events for partial recurrent blocks (#51243)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_connector/unit/offloading_connector/test_events.py`, `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/events.py` _+1 more__
- **2026-08-09** [`1b0ce31f32`](https://github.com/vllm-project/vllm/commit/1b0ce31f32) [#49328](https://github.com/vllm-project/vllm/pull/49328)
  [KV Offload] Fix failed-load livelock by marking the lookup verdict as a miss (#49328)
  _Files: `csrc/fs_io.cpp`, `tests/v1/kv_offload/tiering/test_async_lookup.py`, `tests/v1/kv_offload/tiering/test_fs_tier.py`, `tests/v1/kv_offload/tiering/test_obj_tier.py` _+5 more__
- **2026-08-07** [`d4ecb75ba2`](https://github.com/vllm-project/vllm/commit/d4ecb75ba2) [#48758](https://github.com/vllm-project/vllm/pull/48758)
  [PD][NixlPush][Bugfix] Fix prefix caching (#48758)
  _Files: `tests/v1/kv_connector/unit/test_nixl_connector_hma.py`, `tests/v1/kv_connector/unit/test_nixl_push_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/base_worker.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/pull_worker.py` _+1 more__
- **2026-08-06** [`46e6a83ce1`](https://github.com/vllm-project/vllm/commit/46e6a83ce1) [#51227](https://github.com/vllm-project/vllm/pull/51227)
  [Bugfix][KV Offload] Clean up resources after initialization failure (#51227)
  _Files: `vllm/v1/kv_offload/cpu/spec.py`, `vllm/v1/kv_offload/tiering/spec.py`_
- **2026-08-06** [`ef2615c2e0`](https://github.com/vllm-project/vllm/commit/ef2615c2e0) [#51116](https://github.com/vllm-project/vllm/pull/51116)
  [Bugfix][KV Offload] Fall back when MADV_POPULATE_WRITE is unsupported (#51116)
  _Files: `tests/v1/kv_offload/cpu/test_shared_offload_region.py`, `vllm/v1/kv_offload/cpu/shared_offload_region.py`_
- **2026-08-06** [`5370461649`](https://github.com/vllm-project/vllm/commit/5370461649) [#51108](https://github.com/vllm-project/vllm/pull/51108)
  [BugFix][KV Cache] Fix hybrid prefix caching with hidden-state extraction (#51108)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/core/kv_cache_utils.py`_
- **2026-08-05** [`23c0f337b7`](https://github.com/vllm-project/vllm/commit/23c0f337b7) [#51180](https://github.com/vllm-project/vllm/pull/51180)
  [CI bug] Fix `Each KV cache group's real block_size must be divisible by has h_block_size` (#51180)
  _Files: `vllm/v1/core/kv_cache_utils.py`_
- **2026-08-05** [`8543522ca7`](https://github.com/vllm-project/vllm/commit/8543522ca7) [#51007](https://github.com/vllm-project/vllm/pull/51007)
  [KV Offload] Support out-of-tree secondary tier managers via `module_path` (#51007)
  _Files: `docs/features/kv_offloading_usage.md`, `tests/v1/kv_offload/tiering/test_factory.py`, `vllm/v1/kv_offload/cpu/policies/factory.py`, `vllm/v1/kv_offload/factory.py` _+2 more__
- **2026-08-05** [`62c5e21621`](https://github.com/vllm-project/vllm/commit/62c5e21621) [#50507](https://github.com/vllm-project/vllm/pull/50507)
  [KV Offloading] Support partial-tail prefix reuse with fine-grained prefix matching (#50507)
  _Files: `tests/v1/kv_connector/unit/offloading_connector/test_scheduler.py`, `vllm/distributed/kv_transfer/kv_connector/v1/offloading/scheduler.py`_
- **2026-08-05** [`b92352ca2c`](https://github.com/vllm-project/vllm/commit/b92352ca2c) [#50992](https://github.com/vllm-project/vllm/pull/50992)
  [Perf][KV Offload] Avoid quadratic ARC batch eviction (#50992)
  _Files: `tests/v1/kv_offload/cpu/test_manager.py`, `vllm/v1/kv_offload/cpu/policies/arc.py`_
- **2026-08-05** [`41a7e7da0c`](https://github.com/vllm-project/vllm/commit/41a7e7da0c) [#50321](https://github.com/vllm-project/vllm/pull/50321)
  [KV Offload] Support partial secondary-tier load results (#50321)
  _Files: `tests/v1/kv_offload/tiering/test_tiering_offloading.py`, `vllm/v1/kv_offload/tiering/base.py`, `vllm/v1/kv_offload/tiering/manager.py`_
- **2026-08-04** [`5f2ee2fa8c`](https://github.com/vllm-project/vllm/commit/5f2ee2fa8c) [#50462](https://github.com/vllm-project/vllm/pull/50462)
  [Bugfix][Core] Log KV cache capacity after block-size resolution (#50462)
  _Files: `vllm/v1/core/kv_cache_utils.py`, `vllm/v1/engine/core.py`_
- **2026-08-03** [`f0de1a604c`](https://github.com/vllm-project/vllm/commit/f0de1a604c) [#50823](https://github.com/vllm-project/vllm/pull/50823)
  [Bugfix] Shard UniformTypeKVCacheSpecs block table width under DCP (#50823)
  _Files: `tests/v1/core/test_kv_cache_utils.py`, `vllm/v1/kv_cache_interface.py`_

## Speculative Decoding  (7 commits)

- **2026-08-06** [`27930df9c2`](https://github.com/vllm-project/vllm/commit/27930df9c2) [#50939](https://github.com/vllm-project/vllm/pull/50939)
  [Model Runner V2] Fix -1 placeholder draft token ids in rejection sam… (#50939)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `vllm/v1/worker/gpu/spec_decode/rejection_sampler_utils.py`_
- **2026-08-06** [`c0202c5603`](https://github.com/vllm-project/vllm/commit/c0202c5603) [#48341](https://github.com/vllm-project/vllm/pull/48341)
  [Bugfix][Spec Decode] Auto-enable async scheduling for draft models (#48341)
  _Files: `tests/test_config.py`, `tests/v1/e2e/spec_decode/draft_model/test_draft_model.py`, `vllm/config/vllm.py`_
- **2026-08-06** [`81bc196913`](https://github.com/vllm-project/vllm/commit/81bc196913) [#50910](https://github.com/vllm-project/vllm/pull/50910)
  [Model Runner V2] Cache draft logits in model's LM head dtype (#50910)
  _Files: `tests/v1/spec_decode/test_rejection_sampler_utils.py`, `tests/v1/worker/test_gpu_gumbel_sample.py`, `vllm/v1/worker/gpu/sample/gumbel.py`, `vllm/v1/worker/gpu/spec_decode/dspark/speculator.py` _+2 more__
- **2026-08-05** [`4719a9b8f5`](https://github.com/vllm-project/vllm/commit/4719a9b8f5) [#51092](https://github.com/vllm-project/vllm/pull/51092)
  [Bugfix][Spec Decode] Fix EAGLE3 DeepSeek draft crash on non-YaRN rope configs (#51092)
  _Files: `vllm/model_executor/models/deepseek_eagle3.py`_
- **2026-08-03** [`952694e384`](https://github.com/vllm-project/vllm/commit/952694e384) [#49230](https://github.com/vllm-project/vllm/pull/49230)
  [Bugfix] Validate NIXL speculative config compatibility (#49230)
  _Files: `docs/features/nixl_connector_compatibility.md`, `tests/v1/kv_connector/unit/test_nixl_connector.py`, `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`_
- **2026-08-03** [`68ca6fd02c`](https://github.com/vllm-project/vllm/commit/68ca6fd02c) [#50869](https://github.com/vllm-project/vllm/pull/50869)
  [Bugfix] Remove bad startup assertion (#50869)
  _Files: `vllm/config/speculative.py`_
- **2026-08-03** [`5c4fe4b17e`](https://github.com/vllm-project/vllm/commit/5c4fe4b17e) [#49069](https://github.com/vllm-project/vllm/pull/49069)
  [Bugfix][KV Connector] Propagate EAGLE state across merged Mooncake store groups (#49069)
  _Files: `tests/v1/kv_connector/unit/test_mooncake_store_coordinator.py`, `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/coordinator.py`_

## Serving / API  (6 commits)

- **2026-08-07** [`ac70ce96e0`](https://github.com/vllm-project/vllm/commit/ac70ce96e0) [#50916](https://github.com/vllm-project/vllm/pull/50916)
  [Frontend] Disable uvicorn signal handlers instead of racing them (#50916)
  _Files: `tests/entrypoints/openai/test_dp_supervisor.py`, `vllm/entrypoints/launcher.py`, `vllm/entrypoints/openai/dp_supervisor.py`_
- **2026-08-06** [`865781e627`](https://github.com/vllm-project/vllm/commit/865781e627) [#50289](https://github.com/vllm-project/vllm/pull/50289)
  [Rust Frontend] Add standalone Rust renderer (#50289)
  _Files: `rust/README.md`, `rust/src/chat/src/lib.rs`, `rust/src/cmd/src/cli.rs`, `rust/src/cmd/src/cli/tests.rs` _+11 more__
- **2026-08-06** [`22170354d8`](https://github.com/vllm-project/vllm/commit/22170354d8) [#51089](https://github.com/vllm-project/vllm/pull/51089)
  [Feature] Parse request priority from HTTP header (#51089)
  _Files: `docs/serving/online_serving/openai_compatible_server.md`, `rust/src/server/src/routes/openai/chat_completions/convert.rs`, `rust/src/server/src/routes/openai/completions/convert.rs`, `rust/src/server/src/utils.rs` _+4 more__
- **2026-08-03** [`c4e9f09de7`](https://github.com/vllm-project/vllm/commit/c4e9f09de7) [#50746](https://github.com/vllm-project/vllm/pull/50746)
  [Bugfix][Frontend] Reject empty gRPC stop strings (#50746)
  _Files: `rust/src/server/src/grpc/tests.rs`, `rust/src/text/src/error.rs`, `rust/src/text/src/output/decoded.rs`, `rust/src/text/src/request.rs`_
- **2026-08-03** [`b3f97dae24`](https://github.com/vllm-project/vllm/commit/b3f97dae24) [#50816](https://github.com/vllm-project/vllm/pull/50816)
  [Frontend] Require cache_salt to be non-empty via schema (#50816)
  _Files: `vllm/entrypoints/openai/chat_completion/protocol.py`, `vllm/entrypoints/openai/completion/protocol.py`, `vllm/entrypoints/openai/responses/protocol.py`, `vllm/entrypoints/pooling/base/protocol.py` _+1 more__
- **2026-08-03** [`f5bb701fa2`](https://github.com/vllm-project/vllm/commit/f5bb701fa2) [#50764](https://github.com/vllm-project/vllm/pull/50764)
  [Bugfix][Frontend] Constrain Anthropic cache_salt to non-empty (#50764)
  _Files: `tests/entrypoints/anthropic/test_anthropic_messages_conversion.py`, `vllm/entrypoints/anthropic/protocol.py`_

## Perf / Benchmark  (5 commits)

- **2026-08-07** [`a801e71cb8`](https://github.com/vllm-project/vllm/commit/a801e71cb8) [#48735](https://github.com/vllm-project/vllm/pull/48735)
  [Perf] Improve `--linear-backend` filtering (#48735)
  _Files: `vllm/model_executor/kernels/linear/__init__.py`_
- **2026-08-06** [`7b4ed49628`](https://github.com/vllm-project/vllm/commit/7b4ed49628) [#50185](https://github.com/vllm-project/vllm/pull/50185)
  attn_res kernel latency improvements (#50185)
  _Files: `csrc/libtorch_stable/kimi_k3/attn_res_kernel.cu`_
- **2026-08-06** [`e07532b035`](https://github.com/vllm-project/vllm/commit/e07532b035) [#50981](https://github.com/vllm-project/vllm/pull/50981)
  [MISC][Bench] refactor throughput and reuse serve's get samples (#50981)
  _Files: `tests/benchmarks/test_throughput_cli.py`, `vllm/benchmarks/datasets/datasets.py`, `vllm/benchmarks/throughput.py`_
- **2026-08-04** [`72cd5424da`](https://github.com/vllm-project/vllm/commit/72cd5424da) [#50868](https://github.com/vllm-project/vllm/pull/50868)
  [Rust][Benchmark] Preserve UTF-8 across benchmark stream chunks (#50868)
  _Files: `rust/src/bench/src/backends/streaming.rs`_
- **2026-08-03** [`d9dac2b3d4`](https://github.com/vllm-project/vllm/commit/d9dac2b3d4) [#46870](https://github.com/vllm-project/vllm/pull/46870)
  fix: remove stray duplicate from serving benchmark config (#46870)
  _Files: `.pre-commit-config.yaml`_

## Compilation / CUDA Graph  (4 commits)

- **2026-08-08** [`7f58e8294a`](https://github.com/vllm-project/vllm/commit/7f58e8294a) [#51196](https://github.com/vllm-project/vllm/pull/51196)
  [Kimi][MM] disable kimi_vit's dynamic torch.compile for TPU (#51196)
  _Files: `vllm/model_executor/models/kimi_k25_vit.py`_
- **2026-08-07** [`021b7d985b`](https://github.com/vllm-project/vllm/commit/021b7d985b) [#49390](https://github.com/vllm-project/vllm/pull/49390)
  [Perf] Raise Blackwell CUDA graph capture default to 1024 (#49390)
  _Files: `tests/compile/test_config.py`, `vllm/config/compilation.py`, `vllm/config/vllm.py`_
- **2026-08-04** [`7cab4368f2`](https://github.com/vllm-project/vllm/commit/7cab4368f2) [#50929](https://github.com/vllm-project/vllm/pull/50929)
  [MM][CG] Support ViT full CUDA graph for Kimi-K2.5 (#50929)
  _Files: `vllm/model_executor/models/kimi_k25.py`_
- **2026-08-03** [`ec40f6a8a6`](https://github.com/vllm-project/vllm/commit/ec40f6a8a6) [#49960](https://github.com/vllm-project/vllm/pull/49960)
  [CPU] Fix torch.compile crash from torch.accelerator.synchronize on CPU-only hosts (#49960)
  _Files: `vllm/v1/worker/cpu/shm.py`, `vllm/v1/worker/cpu_model_runner.py`_

## Docs  (3 commits)

- **2026-08-07** [`0406ba22c4`](https://github.com/vllm-project/vllm/commit/0406ba22c4) [#51341](https://github.com/vllm-project/vllm/pull/51341)
  fix pre-commit broken (#51341)
  _Files: `docs/governance/committers.md`_
- **2026-08-06** [`9bca7d840d`](https://github.com/vllm-project/vllm/commit/9bca7d840d) [#51300](https://github.com/vllm-project/vllm/pull/51300)
  docs(governance): refresh committers list, add TSC note, update project leads (#51300)
  _Files: `docs/governance/committers.md`, `docs/governance/process.md`_
- **2026-08-03** [`005fa01756`](https://github.com/vllm-project/vllm/commit/005fa01756) [#50624](https://github.com/vllm-project/vllm/pull/50624)
  docs: document `reasoning_content` output removal as a breaking client change (#50624)
  _Files: `docs/features/reasoning_outputs.md`_

## LoRA  (3 commits)

- **2026-08-06** [`e7b8d59460`](https://github.com/vllm-project/vllm/commit/e7b8d59460) [#51247](https://github.com/vllm-project/vllm/pull/51247)
  Fully generalise input embedding handling in Transformers modelling backend (#51247)
  _Files: `tests/models/transformers/test_backend.py`, `vllm/lora/layers/vocal_parallel_embedding.py`, `vllm/model_executor/layers/vocab_parallel_embedding.py`, `vllm/model_executor/models/transformers/base.py` _+2 more__
- **2026-08-06** [`821717118f`](https://github.com/vllm-project/vllm/commit/821717118f) [#50890](https://github.com/vllm-project/vllm/pull/50890)
  [BugFix][Pooling] Skip weight-prefix probe when model has WeightsMapper (#50890)
  _Files: `tests/models/test_adapters.py`, `vllm/model_executor/models/adapters.py`_
- **2026-08-06** [`b50fdebce0`](https://github.com/vllm-project/vllm/commit/b50fdebce0) [#39935](https://github.com/vllm-project/vllm/pull/39935)
  [Bugfix] Fix level-2 sleep/wake/reload with enable_lora=True (#39935)
  _Files: `docs/features/sleep_mode.md`, `tests/basic_correctness/test_mem.py`, `tests/lora/test_layers.py`, `tests/lora/test_lora_manager.py` _+7 more__

---
_Generated 2026-08-10 09:45 UTC_