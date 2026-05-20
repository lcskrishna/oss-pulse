# sgl-project/sglang — Weekly Change Report
**Period:** 2026-05-13 → 2026-05-20  |  **Total commits:** 359

## ✨ New Features This Week

- **2026-05-20** [#24641](https://github.com/sgl-project/sglang/pull/24641) — [Intel GPU]Support fused_topk for XPU (#24641)
- **2026-05-19** [#24934](https://github.com/sgl-project/sglang/pull/24934) — DeepSeek V4 MTP Support CP (#24934)
- **2026-05-19** [#24640](https://github.com/sgl-project/sglang/pull/24640) — Support spec v2 for FlashMLA speculative decoding (#24640)
- **2026-05-19** [#25284](https://github.com/sgl-project/sglang/pull/25284) — Support Gemma4 Pipeline Parallelism (#25284)
- **2026-05-19** [#25645](https://github.com/sgl-project/sglang/pull/25645) — [Diffusion] Support parallelism for GLM-Image (#25645)
- **2026-05-19** [#23482](https://github.com/sgl-project/sglang/pull/23482) — [Diffusion][NPU]Add attention backends for diffusion models for Ascend NPU (#23482)
- **2026-05-19** [#23606](https://github.com/sgl-project/sglang/pull/23606) — [HiSparse & PD] Support hisparse memory pool host page > 1 (#23606)
- **2026-05-19** [#22918](https://github.com/sgl-project/sglang/pull/22918) — [FlashInfer v0.6.11] [RL] Support FlashInfer per-token NVFP4 MoE (#22918)
- **2026-05-19** [#22338](https://github.com/sgl-project/sglang/pull/22338) — :sparkles: [diffusion][npu][quant] Add MXFP4 quantization support for Wan2.2 Diffusion on Ascend NPU (#22338)
- **2026-05-19** [#25588](https://github.com/sgl-project/sglang/pull/25588) — perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode (#25588)
- _…and 75 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-05-19** [`aad00b0ed8`](https://github.com/sgl-project/sglang/commit/aad00b0ed8) [#25451](https://github.com/sgl-project/sglang/pull/25451) — Upgrade transformers to 5.8.1 (#25451)
- **2026-05-19** [`7c3f614e23`](https://github.com/sgl-project/sglang/commit/7c3f614e23) [#25740](https://github.com/sgl-project/sglang/pull/25740) — [AMD] Bump amd/Kimi-K2.5-MXFP4 revision to align with shared-experts fusion (#25740)
- **2026-05-18** [`866793c502`](https://github.com/sgl-project/sglang/commit/866793c502) [#24933](https://github.com/sgl-project/sglang/pull/24933) — Amd/deepseek v4 rebase main 0509 (#24933)
- **2026-05-18** [`abe2ec2aff`](https://github.com/sgl-project/sglang/commit/abe2ec2aff) [#25390](https://github.com/sgl-project/sglang/pull/25390) — [AMD] Enable shared-experts fusion with new KIMI-K2.5-MXFP4 model. (#25390)
- **2026-05-18** [`54eb2904a4`](https://github.com/sgl-project/sglang/commit/54eb2904a4) [#25178](https://github.com/sgl-project/sglang/pull/25178) — minor: docs include mac installation (#25178)
- **2026-05-18** [`7adb37bb52`](https://github.com/sgl-project/sglang/commit/7adb37bb52) [#25301](https://github.com/sgl-project/sglang/pull/25301) — [AMD] fix moriep unittest oom on mi300x ci (#25301)
- **2026-05-17** [`be3c425788`](https://github.com/sgl-project/sglang/commit/be3c425788) [#23760](https://github.com/sgl-project/sglang/pull/23760) — [MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute (#23760)
- **2026-05-17** [`52875ab6f4`](https://github.com/sgl-project/sglang/commit/52875ab6f4) [#25260](https://github.com/sgl-project/sglang/pull/25260) — [AMD][CI] Register Eagle constrained decoding test (#25260)
- **2026-05-17** [`4ef9bad223`](https://github.com/sgl-project/sglang/commit/4ef9bad223) [#25208](https://github.com/sgl-project/sglang/pull/25208) — [AMD] ci: register 5 framework tests to run on AMD CI (#25208)
- **2026-05-15** [`4df42da658`](https://github.com/sgl-project/sglang/commit/4df42da658) [#24096](https://github.com/sgl-project/sglang/pull/24096) — Introduce CudaDeviceMixin and CudaSRTPlatform (#24096)
- **2026-05-15** [`fd9525436b`](https://github.com/sgl-project/sglang/commit/fd9525436b) [#25264](https://github.com/sgl-project/sglang/pull/25264) — move runs_on + rdma into runner_configs.yml (#25264)
- **2026-05-15** [`9dad37f254`](https://github.com/sgl-project/sglang/commit/9dad37f254) [#25112](https://github.com/sgl-project/sglang/pull/25112) — [AMD] Bump --timeout-per-file 1800->2400 for stage-b-test-1-gpu-small-amd (#25112)
- **2026-05-15** [`897587b03a`](https://github.com/sgl-project/sglang/commit/897587b03a) [#24978](https://github.com/sgl-project/sglang/pull/24978) — [MUSA]: Add flashinfer sampling backend (#24978)
- **2026-05-15** [`0fde61535f`](https://github.com/sgl-project/sglang/commit/0fde61535f) [#25326](https://github.com/sgl-project/sglang/pull/25326) — chore: bump sgl-kernel version to 0.4.2.post2 (#25326)
- **2026-05-14** [`bc265c5f82`](https://github.com/sgl-project/sglang/commit/bc265c5f82) [#25210](https://github.com/sgl-project/sglang/pull/25210) — [AMD] Add amd jit resolve token ids bench ci (#25210)
- **2026-05-14** [`7b128e143a`](https://github.com/sgl-project/sglang/commit/7b128e143a) [#25209](https://github.com/sgl-project/sglang/pull/25209) — [AMD] Add amd jit clamp position bench ci (#25209)
- **2026-05-14** [`22bfae0d1d`](https://github.com/sgl-project/sglang/commit/22bfae0d1d) [#25205](https://github.com/sgl-project/sglang/pull/25205) — [AMD]  Auto-fallback NSA indexer to page_size=1 when aiter preshuffle gluon kernel is unavailable (Deepseek v3.2) (#25205)
- **2026-05-14** [`34c0029f0a`](https://github.com/sgl-project/sglang/commit/34c0029f0a) [#21431](https://github.com/sgl-project/sglang/pull/21431) — [diffusion] [AMD] feat: support online MXFP4 and fp8 quantization (#21431)
- **2026-05-13** [`ff70aeac30`](https://github.com/sgl-project/sglang/commit/ff70aeac30) [#24491](https://github.com/sgl-project/sglang/pull/24491) — [diffusion] feat: add performance mode server args (#24491)
- **2026-05-13** [`cf92ccbf18`](https://github.com/sgl-project/sglang/commit/cf92ccbf18) [#24987](https://github.com/sgl-project/sglang/pull/24987) — [AMD] Run jit kernel PR test through run_suite.py register mechanism (#24987)
- **2026-05-13** [`fc20f5b114`](https://github.com/sgl-project/sglang/commit/fc20f5b114) [#24125](https://github.com/sgl-project/sglang/pull/24125) — [AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode (#24125)
- **2026-05-13** [`a9359707c1`](https://github.com/sgl-project/sglang/commit/a9359707c1) [#23562](https://github.com/sgl-project/sglang/pull/23562) — [AMD] Enable preshuffle paged MQA and page_size=64 for NSA indexer (#23562)
- **2026-05-13** [`839f7f2696`](https://github.com/sgl-project/sglang/commit/839f7f2696) [#24148](https://github.com/sgl-project/sglang/pull/24148) — [AMD] Add _skip_rope_for_aiter_fused_mla method and check to avoid double rotating with gfx950 and Aiter backend (#24148)
- **2026-05-13** [`66a9234246`](https://github.com/sgl-project/sglang/commit/66a9234246) [#24879](https://github.com/sgl-project/sglang/pull/24879) — [AMD] support fp8 blockwise quantization combine for mori ep (#24879)
- **2026-05-13** [`72b266d59b`](https://github.com/sgl-project/sglang/commit/72b266d59b) [#25039](https://github.com/sgl-project/sglang/pull/25039) — [AMD] Disable unittest fail-fast for deepseekv4 perf test (#25039)
- **2026-05-13** [`245f7d8026`](https://github.com/sgl-project/sglang/commit/245f7d8026) [#24572](https://github.com/sgl-project/sglang/pull/24572) — [AMD] Register 5 server-style 1-GPU tests for AMD PR CI (#24572)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#25672](https://github.com/sgl-project/sglang/issues/25672) | [Bug] GLM-5 on MI325X + aiter backend: concat_and_cast_mha_k_kernel Tr | — | 2026-05-19 |
| [#25797](https://github.com/sgl-project/sglang/issues/25797) | [Bug] [amd] [amd/deepseek_v4] HSA_STATUS_ERROR_OUT_OF_RESOURCES on MI3 | — | 2026-05-19 |
| [#25780](https://github.com/sgl-project/sglang/issues/25780) | Whisper Runtime Crash During Inference After Successful Server Startup | — | 2026-05-19 |
| [#25742](https://github.com/sgl-project/sglang/issues/25742) | GLM-5.1-MXFP4 on AMD MI355X — massive GSM8K accuracy degradation on v0 | — | 2026-05-19 |
| [#22949](https://github.com/sgl-project/sglang/issues/22949) | Development Roadmap (2026 Q2) | — | 2026-05-19 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-05-19 |
| [#24488](https://github.com/sgl-project/sglang/issues/24488) | [Help] [Performance] PD disaggregation on H200 shows no throughput gai | — | 2026-05-18 |
| [#25652](https://github.com/sgl-project/sglang/issues/25652) | [Bug] [NPU] DDR address of the MTE instruction is out of range when us | — | 2026-05-18 |
| [#23363](https://github.com/sgl-project/sglang/issues/23363) | [Bug] KimiK2Detector streaming parser silently drops / hangs on multi- | — | 2026-05-18 |
| [#25587](https://github.com/sgl-project/sglang/issues/25587) | [Bug] [NPU] Hybrid-GDN MTP speculative decoding is not lossless on Asc | — | 2026-05-18 |
| [#24656](https://github.com/sgl-project/sglang/issues/24656) | [RFC] Agent-Aware KV Cache Phase 1 for Agentic Workloads | — | 2026-05-18 |
| [#25526](https://github.com/sgl-project/sglang/issues/25526) | DSv4 Flash + HiCache breakable piecewise CUDA graph is gated and hits  | — | 2026-05-17 |
| [#25487](https://github.com/sgl-project/sglang/issues/25487) | [Bug] CUDA graph capture with ninja build error on CUDA 13 | — | 2026-05-16 |
| [#22474](https://github.com/sgl-project/sglang/issues/22474) | [RFC]: Real-Time Streaming Audio Input for ASR Models | — | 2026-05-15 |
| [#21837](https://github.com/sgl-project/sglang/issues/21837) | [Bug] PD separation scenario, Abort request results in D node unhealth | — | 2026-05-15 |
| [#22889](https://github.com/sgl-project/sglang/issues/22889) | [Feature] Free-Threaded Python (3.14t / nogil) Support for SGLang | — | 2026-05-15 |
| [#25330](https://github.com/sgl-project/sglang/issues/25330) | [Bug] [NPU] UB overflow in move_cache_dynamic_last_kernel_h_block when | — | 2026-05-15 |
| [#25187](https://github.com/sgl-project/sglang/issues/25187) | Accuracy collapses to ~0% on Qwen3.5-FP8 / B300 with --cuda-graph-max- | — | 2026-05-14 |
| [#24591](https://github.com/sgl-project/sglang/issues/24591) | [Bug] deepseek v4 pro base often outputs <｜end▁of▁file｜>\n<｜begin▁of▁f | — | 2026-05-14 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-05-14 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Scheduler / Batching | 57 |
| Prefill / Decode Disaggregation | 48 |
| Attention / FlashInfer | 42 |
| MoE / Expert Parallel | 41 |
| Multimodal | 27 |
| Other | 21 |
| KV Cache / Memory | 21 |
| CI / Build | 18 |
| Quantization | 15 |
| Triton / Kernels | 12 |
| Tensor / Data Parallel | 12 |
| Speculative Decoding | 11 |
| Docs / Examples | 11 |
| Models | 10 |
| ROCm / AMD | 8 |
| Serving / API | 3 |
| LoRA | 1 |
| Structured Output | 1 |

## Scheduler / Batching  (57 commits)

- **2026-05-19** [`2f70902329`](https://github.com/sgl-project/sglang/commit/2f70902329) [#25809](https://github.com/sgl-project/sglang/pull/25809)
  deflake priority below-threshold test (#25809)
  _Files: `test/registered/scheduler/test_priority_scheduling.py`_
- **2026-05-19** [`16bcc4583e`](https://github.com/sgl-project/sglang/commit/16bcc4583e) [#25465](https://github.com/sgl-project/sglang/pull/25465)
  verify_done: wait not synchronize (#25465)
  _Files: `.github/workflows/pr-gate.yml`, `.github/workflows/pr-test-extra.yml`, `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-19** [`e4d81e48c9`](https://github.com/sgl-project/sglang/commit/e4d81e48c9) [#25728](https://github.com/sgl-project/sglang/pull/25728)
  Pull the max-prefix-len computation into its own helper and rename the matched-token argument (#25728)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-19** [`170fe57cf0`](https://github.com/sgl-project/sglang/commit/170fe57cf0) [#25727](https://github.com/sgl-project/sglang/pull/25727)
  Encapsulate the pending-flush bookkeeping in a small wrapper (#25727)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/flush_wrapper.py`, `test/registered/unit/managers/test_scheduler_flush_cache.py`_
- **2026-05-19** [`5067da3eb6`](https://github.com/sgl-project/sglang/commit/5067da3eb6) [#25726](https://github.com/sgl-project/sglang/pull/25726)
  Confine req-pool-idx assignment to the pool allocator (#25726)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-19** [`2d2dff28da`](https://github.com/sgl-project/sglang/commit/2d2dff28da) [#25724](https://github.com/sgl-project/sglang/pull/25724)
  Return a mamba tracking entry from the cache lookup instead of mutating caller lists (#25724)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-19** [`3fd6a58e6c`](https://github.com/sgl-project/sglang/commit/3fd6a58e6c) [#25722](https://github.com/sgl-project/sglang/pull/25722)
  Inline the single-use split-prefill setup at its caller (#25722)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `test/manual/test_forward_split_prefill.py`_
- **2026-05-19** [`1f3e5aa1e0`](https://github.com/sgl-project/sglang/commit/1f3e5aa1e0) [#25721](https://github.com/sgl-project/sglang/pull/25721)
  Publish elastic-EP active ranks from a dedicated step (#25721)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-19** [`32f1259c91`](https://github.com/sgl-project/sglang/commit/32f1259c91) [#25719](https://github.com/sgl-project/sglang/pull/25719)
  Confine max-prefix-len to where it is used and drop the leftover variable (#25719)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-19** [`1cba3ab467`](https://github.com/sgl-project/sglang/commit/1cba3ab467) [#25718](https://github.com/sgl-project/sglang/pull/25718)
  Stop returning the unused prefix-computed flag from priority calc (#25718)
  _Files: `python/sglang/srt/managers/schedule_policy.py`_
- **2026-05-19** [`2d868656d0`](https://github.com/sgl-project/sglang/commit/2d868656d0) [#25717](https://github.com/sgl-project/sglang/pull/25717)
  Move the retract-decode ratio estimation onto the new-token-ratio tracker (#25717)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler_components/new_token_ratio_tracker.py`_
- **2026-05-19** [`1a882c5c63`](https://github.com/sgl-project/sglang/commit/1a882c5c63) [#25716](https://github.com/sgl-project/sglang/pull/25716)
  Pack scattered new-token-ratio state into a dedicated tracker (#25716)
  _Files: `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/new_token_ratio_tracker.py`_
- **2026-05-19** [`07b4f262b7`](https://github.com/sgl-project/sglang/commit/07b4f262b7) [#25713](https://github.com/sgl-project/sglang/pull/25713)
  Set up the idle sleeper outside of the IPC channel initialization (#25713)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-19** [`a740f8de33`](https://github.com/sgl-project/sglang/commit/a740f8de33) [#25710](https://github.com/sgl-project/sglang/pull/25710)
  Remove the dead hasattr fallback around the test-only crash counter (#25710)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-05-19** [`0e198f0f4f`](https://github.com/sgl-project/sglang/commit/0e198f0f4f) [#25709](https://github.com/sgl-project/sglang/pull/25709)
  Refactor batch_result_processor into per-step prefill/decode helpers (#25709)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-05-19** [`7e7cb969e9`](https://github.com/sgl-project/sglang/commit/7e7cb969e9) [#25708](https://github.com/sgl-project/sglang/pull/25708)
  Route streaming output through the accumulator's payload method instead of an inline send (#25708)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-05-19** [`da50e3d943`](https://github.com/sgl-project/sglang/commit/da50e3d943) [#25707](https://github.com/sgl-project/sglang/pull/25707)
  Log per-request time stats in a dedicated tail step (#25707)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-05-19** [`b911fd1673`](https://github.com/sgl-project/sglang/commit/b911fd1673) [#25706](https://github.com/sgl-project/sglang/pull/25706)
  Route streaming-accept decisions through the accumulator instead of an inline gate (#25706)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-05-19** [`d8f190dfba`](https://github.com/sgl-project/sglang/commit/d8f190dfba) [#25705](https://github.com/sgl-project/sglang/pull/25705)
  Pack scattered output-streamer state into a dedicated accumulator (#25705)
  _Files: `python/sglang/srt/managers/scheduler_components/output_streamer.py`_
- **2026-05-19** [`e8e55bb19b`](https://github.com/sgl-project/sglang/commit/e8e55bb19b) [#25703](https://github.com/sgl-project/sglang/pull/25703)
  Split the request-reception loop into smaller phases (#25703)
  _Files: `python/sglang/srt/managers/scheduler_components/request_receiver.py`_
- **2026-05-18** [`be64d875ad`](https://github.com/sgl-project/sglang/commit/be64d875ad) [#25641](https://github.com/sgl-project/sglang/pull/25641)
  Fix flush_cache AttributeError on is_stats_logging_rank (#25641)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-18** [`8b94e1d0cf`](https://github.com/sgl-project/sglang/commit/8b94e1d0cf) [#25639](https://github.com/sgl-project/sglang/pull/25639)
  Delete the now-unused is_work_request from scheduler.py (#25639)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-18** [`cf12070a0f`](https://github.com/sgl-project/sglang/commit/cf12070a0f) [#25631](https://github.com/sgl-project/sglang/pull/25631)
  Move idle-metrics logging to SchedulerMetricsReporter (#25631)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/metrics_reporter.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-18** [`8357d07569`](https://github.com/sgl-project/sglang/commit/8357d07569) [#25628](https://github.com/sgl-project/sglang/pull/25628)
  Move queue-load reporting to SchedulerLoadInquirer (#25628)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`bde932cbbb`](https://github.com/sgl-project/sglang/commit/bde932cbbb) [#25627](https://github.com/sgl-project/sglang/pull/25627)
  Carve out SchedulerLoadInquirer for queue-load state (#25627)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/load_inquirer.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`1213277879`](https://github.com/sgl-project/sglang/commit/1213277879) [#25626](https://github.com/sgl-project/sglang/pull/25626)
  Move KV-cache event emission to SchedulerKvEventsPublisher (#25626)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`0f888442c2`](https://github.com/sgl-project/sglang/commit/0f888442c2) [#25625](https://github.com/sgl-project/sglang/pull/25625)
  Stand up SchedulerKvEventsPublisher; migrate KV-event state to it (#25625)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/kv_events_publisher.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`f3dce08283`](https://github.com/sgl-project/sglang/commit/f3dce08283) [#25624](https://github.com/sgl-project/sglang/pull/25624)
  Move invariant checks to SchedulerInvariantChecker and retire runtime_checker mixin (#25624)
  _Files: `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-18** [`8a200464fd`](https://github.com/sgl-project/sglang/commit/8a200464fd) [#25623](https://github.com/sgl-project/sglang/pull/25623)
  Introduce SchedulerInvariantChecker to own invariant-check state (#25623)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-18** [`b463740953`](https://github.com/sgl-project/sglang/commit/b463740953) [#25622](https://github.com/sgl-project/sglang/pull/25622)
  Move create_scheduler_watchdog from runtime_checker mixin to scheduler.py (#25622)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-18** [`ee392a1e14`](https://github.com/sgl-project/sglang/commit/ee392a1e14) [#25621](https://github.com/sgl-project/sglang/pull/25621)
  Move pool-stats sampling to SchedulerPoolStatsObserver (#25621)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`9fdf73f393`](https://github.com/sgl-project/sglang/commit/9fdf73f393) [#25619](https://github.com/sgl-project/sglang/pull/25619)
  Add SchedulerPoolStatsObserver and route pool-stats state through it (#25619)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-18** [`c58b47bc86`](https://github.com/sgl-project/sglang/commit/c58b47bc86) [#25618](https://github.com/sgl-project/sglang/pull/25618)
  Move PoolStats dataclass to scheduler_components.pool_stats_observer (#25618)
  _Files: `python/sglang/srt/managers/scheduler_components/pool_stats_observer.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`, `test/registered/unit/managers/test_scheduler_pause_generation.py`_
- **2026-05-18** [`95d86e5c43`](https://github.com/sgl-project/sglang/commit/95d86e5c43) [#25617](https://github.com/sgl-project/sglang/pull/25617)
  Move on_idle from runtime_checker mixin into Scheduler (#25617)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-18** [`7851ba09f7`](https://github.com/sgl-project/sglang/commit/7851ba09f7) [#25616](https://github.com/sgl-project/sglang/pull/25616)
  Move weight-update RPC handlers to SchedulerWeightUpdaterManager (#25616)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/managers/scheduler_update_weights_mixin.py`_
- **2026-05-18** [`56f27635b8`](https://github.com/sgl-project/sglang/commit/56f27635b8) [#25615](https://github.com/sgl-project/sglang/pull/25615)
  Carve out SchedulerWeightUpdaterManager for weight-update state (#25615)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/weight_updater.py`, `python/sglang/srt/managers/scheduler_update_weights_mixin.py`_
- **2026-05-18** [`a35690f070`](https://github.com/sgl-project/sglang/commit/a35690f070) [#25614](https://github.com/sgl-project/sglang/pull/25614)
  Move profiler controls to SchedulerProfilerManager (#25614)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `test/registered/unit/utils/test_profile_merger.py`_
- **2026-05-18** [`b0a511560c`](https://github.com/sgl-project/sglang/commit/b0a511560c) [#25613](https://github.com/sgl-project/sglang/pull/25613)
  Stand up SchedulerProfilerManager; migrate profiler state to it (#25613)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/profiler_manager.py`, `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `test/registered/unit/utils/test_profile_merger.py`_
- **2026-05-18** [`768d347565`](https://github.com/sgl-project/sglang/commit/768d347565) [#25608](https://github.com/sgl-project/sglang/pull/25608)
  Pre-declare mode-conditional Scheduler fields with explicit defaults (#25608)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-18** [`60337abe24`](https://github.com/sgl-project/sglang/commit/60337abe24) [#25605](https://github.com/sgl-project/sglang/pull/25605)
  Hoist hisparse and decode-offload setup out of init_cache_with_memory_pool (#25605)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-18** [`6ccc5b807d`](https://github.com/sgl-project/sglang/commit/6ccc5b807d) [#25309](https://github.com/sgl-project/sglang/pull/25309)
  Optimize detokenization without HF decode kwargs (#25309)
  _Files: `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/utils/patch_tokenizer.py`, `test/registered/unit/utils/test_patch_tokenizer.py`_
- **2026-05-18** [`43e133208a`](https://github.com/sgl-project/sglang/commit/43e133208a) [#25548](https://github.com/sgl-project/sglang/pull/25548)
  Quiet test_bs_1_speed CI log (#25548)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/test/kits/spec_decoding_kit.py`, `python/sglang/test/send_one.py`_
- **2026-05-16** [`b3059e2d1e`](https://github.com/sgl-project/sglang/commit/b3059e2d1e) [#25445](https://github.com/sgl-project/sglang/pull/25445)
  Inject ParallelState into ProfilerV2 (#25445)
  _Files: `python/sglang/srt/managers/scheduler_profiler_mixin.py`, `python/sglang/srt/utils/profile_utils.py`_
- **2026-05-16** [`fa8b7c9647`](https://github.com/sgl-project/sglang/commit/fa8b7c9647) [#25442](https://github.com/sgl-project/sglang/pull/25442)
  Lift forward_ct/cur_batch and use direct access in watchdog (#25442)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_runtime_checker_mixin.py`_
- **2026-05-16** [`72eb231d28`](https://github.com/sgl-project/sglang/commit/72eb231d28) [#25441](https://github.com/sgl-project/sglang/pull/25441)
  Annotate dead max_running_requests_under_SLO (#25441)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-16** [`5c440cdc41`](https://github.com/sgl-project/sglang/commit/5c440cdc41) [#25439](https://github.com/sgl-project/sglang/pull/25439)
  Lift running_batch / running_mbs access — direct + PP-explicit (#25439)
  _Files: `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-16** [`80c3ce3204`](https://github.com/sgl-project/sglang/commit/80c3ce3204) [#25438](https://github.com/sgl-project/sglang/pull/25438)
  Convert forward_pass_device_timer to None-init (#25438)
  _Files: `python/sglang/srt/observability/scheduler_metrics_mixin.py`_
- **2026-05-16** [`40429248c8`](https://github.com/sgl-project/sglang/commit/40429248c8) [#25437](https://github.com/sgl-project/sglang/pull/25437)
  Drop dead hasattr guards (hisparse_coordinator, metrics_collector) (#25437)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-16** [`6a1b05d706`](https://github.com/sgl-project/sglang/commit/6a1b05d706) [#25435](https://github.com/sgl-project/sglang/pull/25435)
  Replace single-line defensive getattrs with direct access (#25435)
  _Files: `python/sglang/srt/managers/scheduler_output_processor_mixin.py`, `python/sglang/srt/managers/scheduler_pp_mixin.py`, `python/sglang/srt/managers/tokenizer_manager_score_mixin.py`_
- **2026-05-16** [`e065445236`](https://github.com/sgl-project/sglang/commit/e065445236) [#25433](https://github.com/sgl-project/sglang/pull/25433)
  Remove managers' unused fields (#25433)
  _Files: `python/sglang/srt/managers/cache_controller.py`, `python/sglang/srt/managers/data_parallel_controller.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py` _+2 more__
- **2026-05-16** [`824ad24149`](https://github.com/sgl-project/sglang/commit/824ad24149) [#25430](https://github.com/sgl-project/sglang/pull/25430)
  Convert local-only self.X attributes to locals (#25430)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-16** [`18c16f8660`](https://github.com/sgl-project/sglang/commit/18c16f8660) [#25419](https://github.com/sgl-project/sglang/pull/25419)
  Port SGLANG_OPT_SWA_EVICT_DROP_PAGE_MARGIN from deepseek_v4_dev (#25419)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-16** [`5ba69f50fb`](https://github.com/sgl-project/sglang/commit/5ba69f50fb) [#24944](https://github.com/sgl-project/sglang/pull/24944)
  Add multi-detokenizer support (#24944)
  _Files: `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/managers/detokenizer_manager.py`, `python/sglang/srt/managers/multi_tokenizer_mixin.py`, `python/sglang/srt/server_args.py` _+1 more__
- **2026-05-15** [`974948a701`](https://github.com/sgl-project/sglang/commit/974948a701) [#25340](https://github.com/sgl-project/sglang/pull/25340)
  fix: strip "[asctime]" prefix when parsing JSON log lines in nightly tests (#25340)
  _Files: `test/registered/bench_fn/test_bench_serving_functionality.py`, `test/registered/utils/test_request_logger.py`, `test/registered/utils/test_scheduler_status_logger.py`_
- **2026-05-15** [`7af4320d67`](https://github.com/sgl-project/sglang/commit/7af4320d67) [#25265](https://github.com/sgl-project/sglang/pull/25265)
  [perf] fix kimi tokenizer to improve ttft (#25265)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-14** [`421179c453`](https://github.com/sgl-project/sglang/commit/421179c453) [#25155](https://github.com/sgl-project/sglang/pull/25155)
  [perf] avoid hidden states d2h when return_hidden_states=false (#25155)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py`_
- **2026-05-13** [`8438709e9c`](https://github.com/sgl-project/sglang/commit/8438709e9c) [#25126](https://github.com/sgl-project/sglang/pull/25126)
  Fix scheduler admission for near-full KV requests (#25126)
  _Files: `python/sglang/srt/managers/scheduler.py`_

## Prefill / Decode Disaggregation  (48 commits)

- **2026-05-20** [`1fbee74fb6`](https://github.com/sgl-project/sglang/commit/1fbee74fb6) [#25677](https://github.com/sgl-project/sglang/pull/25677)
  [PD] Clean early abort logic in PD module (#25677)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-05-20** [`3b2178c412`](https://github.com/sgl-project/sglang/commit/3b2178c412) [#25287](https://github.com/sgl-project/sglang/pull/25287)
  [PD] Un-blacklist mooncake sessions when probe succeeds (#25287)
  _Files: `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/distributed/device_communicators/mooncake_transfer_engine.py`, `python/sglang/srt/environ.py`_
- **2026-05-20** [`ca29c2b0e7`](https://github.com/sgl-project/sglang/commit/ca29c2b0e7) [#25771](https://github.com/sgl-project/sglang/pull/25771)
  fix(dsv4): drop stale pp_size=1 guard for V4 PD disaggregation (#25771)
  _Files: `python/sglang/srt/arg_groups/deepseek_v4_hook.py`_
- **2026-05-20** [`7f154ba449`](https://github.com/sgl-project/sglang/commit/7f154ba449) [#25774](https://github.com/sgl-project/sglang/pull/25774)
  drop output ids (#25774)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/schedule_batch.py` _+2 more__
- **2026-05-19** [`67fd005b97`](https://github.com/sgl-project/sglang/commit/67fd005b97) [#23606](https://github.com/sgl-project/sglang/pull/23606)
  [HiSparse & PD] Support hisparse memory pool host page > 1 (#23606)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/managers/hisparse_coordinator.py` _+3 more__
- **2026-05-19** [`87c3c96bc8`](https://github.com/sgl-project/sglang/commit/87c3c96bc8) [#25699](https://github.com/sgl-project/sglang/pull/25699)
  [Bug][PD][NIXL] always send aux on is_last; only expects_state when truthy (#25699)
  _Files: `python/sglang/srt/disaggregation/nixl/conn.py`_
- **2026-05-19** [`6bcbf4de35`](https://github.com/sgl-project/sglang/commit/6bcbf4de35) [#25725](https://github.com/sgl-project/sglang/pull/25725)
  Fix the misnamed request finish-check method to reflect its mutating semantics (#25725)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py` _+4 more__
- **2026-05-19** [`fa37b68653`](https://github.com/sgl-project/sglang/commit/fa37b68653) [#25720](https://github.com/sgl-project/sglang/pull/25720)
  Rename the request mid-chunk flag to describe what it actually tracks (#25720)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py` _+5 more__
- **2026-05-19** [`954b5c5846`](https://github.com/sgl-project/sglang/commit/954b5c5846) [#25714](https://github.com/sgl-project/sglang/pull/25714)
  Pack scattered scheduler IPC channel state into a dedicated container (#25714)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/ipc_channels.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py`, `test/registered/unit/managers/test_scheduler_flush_cache.py`_
- **2026-05-19** [`2d40f45193`](https://github.com/sgl-project/sglang/commit/2d40f45193) [#25712](https://github.com/sgl-project/sglang/pull/25712)
  Pack scattered request logprob state into a dedicated container (#25712)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/utils.py`, `python/sglang/srt/layers/utils/logprob.py` _+5 more__
- **2026-05-19** [`fb7e49d4eb`](https://github.com/sgl-project/sglang/commit/fb7e49d4eb) [#25711](https://github.com/sgl-project/sglang/pull/25711)
  Expose can-run-cuda-graph as a regular property on the embedding result (#25711)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/utils.py`_
- **2026-05-18** [`f21fe6ad4d`](https://github.com/sgl-project/sglang/commit/f21fe6ad4d) [#25542](https://github.com/sgl-project/sglang/pull/25542)
  Fix PD disaggregation warmup: set request_name and improve error logging (#25542)
  _Files: `python/sglang/srt/entrypoints/http_server.py`_
- **2026-05-18** [`d1acd62d29`](https://github.com/sgl-project/sglang/commit/d1acd62d29) [#25561](https://github.com/sgl-project/sglang/pull/25561)
  fix(disagg): unstuck decode aborts under prealloc pressure (#25561)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-18** [`f04c522534`](https://github.com/sgl-project/sglang/commit/f04c522534) [#25599](https://github.com/sgl-project/sglang/pull/25599)
  [PD] Add conclude_state to fake KV backend (#25599)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`_
- **2026-05-18** [`99ad2b0894`](https://github.com/sgl-project/sglang/commit/99ad2b0894) [#25637](https://github.com/sgl-project/sglang/pull/25637)
  Move batch-result processing to SchedulerBatchResultProcessor and retire output_processor mixin (#25637)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`_
- **2026-05-18** [`7d0b0b6991`](https://github.com/sgl-project/sglang/commit/7d0b0b6991) [#25636](https://github.com/sgl-project/sglang/pull/25636)
  Carve out SchedulerBatchResultProcessor for batch-result state (#25636)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py` _+1 more__
- **2026-05-18** [`18a7eb9e58`](https://github.com/sgl-project/sglang/commit/18a7eb9e58) [#25635](https://github.com/sgl-project/sglang/pull/25635)
  Move output streaming to SchedulerOutputStreamer (#25635)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-05-18** [`dc88b4eeb4`](https://github.com/sgl-project/sglang/commit/dc88b4eeb4) [#25634](https://github.com/sgl-project/sglang/pull/25634)
  Stand up SchedulerOutputStreamer; migrate output-streaming state to it (#25634)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-05-18** [`2cbe01d044`](https://github.com/sgl-project/sglang/commit/2cbe01d044) [#25633](https://github.com/sgl-project/sglang/pull/25633)
  Move logprob assembly to SchedulerLogprobResultProcessor (#25633)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler_components/logprob_result_processor.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`_
- **2026-05-18** [`e737f61b29`](https://github.com/sgl-project/sglang/commit/e737f61b29) [#25632](https://github.com/sgl-project/sglang/pull/25632)
  Introduce SchedulerLogprobResultProcessor to own logprob state (#25632)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/logprob_result_processor.py`, `python/sglang/srt/managers/scheduler_output_processor_mixin.py`_
- **2026-05-18** [`fd97fbb096`](https://github.com/sgl-project/sglang/commit/fd97fbb096) [#25630](https://github.com/sgl-project/sglang/pull/25630)
  Move metrics reporting to SchedulerMetricsReporter and retire metrics mixin (#25630)
  _Files: `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-05-18** [`780d969699`](https://github.com/sgl-project/sglang/commit/780d969699) [#25629](https://github.com/sgl-project/sglang/pull/25629)
  Add SchedulerMetricsReporter and route metrics state through it (#25629)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/dllm/mixin/scheduler.py` _+6 more__
- **2026-05-18** [`4d6eec7b32`](https://github.com/sgl-project/sglang/commit/4d6eec7b32) [#25612](https://github.com/sgl-project/sglang/pull/25612)
  Move DP-attention adapter methods to SchedulerDPAttnAdapter (#25612)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py` _+4 more__
- **2026-05-18** [`8f37a8a3f3`](https://github.com/sgl-project/sglang/commit/8f37a8a3f3) [#25611](https://github.com/sgl-project/sglang/pull/25611)
  Introduce SchedulerDPAttnAdapter to own DP-attention state (#25611)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/dp_attn.py` _+2 more__
- **2026-05-18** [`0e9eab19a9`](https://github.com/sgl-project/sglang/commit/0e9eab19a9) [#25610](https://github.com/sgl-project/sglang/pull/25610)
  Move request-ingress methods to SchedulerRequestReceiver (#25610)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+3 more__
- **2026-05-18** [`e6f3dcd790`](https://github.com/sgl-project/sglang/commit/e6f3dcd790) [#25609](https://github.com/sgl-project/sglang/pull/25609)
  Add SchedulerRequestReceiver and route request-ingress state through it (#25609)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/managers/scheduler.py` _+3 more__
- **2026-05-18** [`784fe7e99b`](https://github.com/sgl-project/sglang/commit/784fe7e99b) [#24931](https://github.com/sgl-project/sglang/pull/24931)
  feat(mimo-v2): add EPD disaggregation support (#24931)
  _Files: `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/disaggregation/encode_server.py`, `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/tokenizer_manager.py` _+3 more__
- **2026-05-16** [`0f50ed86c9`](https://github.com/sgl-project/sglang/commit/0f50ed86c9) [#25476](https://github.com/sgl-project/sglang/pull/25476)
  fix(pd): fix kv pools without end_layer (#25476)
  _Files: `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/prefill.py`_
- **2026-05-16** [`162540e0a8`](https://github.com/sgl-project/sglang/commit/162540e0a8) [#24704](https://github.com/sgl-project/sglang/pull/24704)
  feat: add Pipeline Parallelism (PP) and PD support for DeepSeek-V4 (#24704)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/prefill.py` _+5 more__
- **2026-05-16** [`bda01d2435`](https://github.com/sgl-project/sglang/commit/bda01d2435) [#25380](https://github.com/sgl-project/sglang/pull/25380)
  [Disagg] Fix MegaMoE topk_ids dtype mismatch and FakeKVManager missing kv_args (#25380)
  _Files: `python/sglang/srt/disaggregation/fake/conn.py`, `python/sglang/srt/layers/moe/mega_moe.py`_
- **2026-05-16** [`43797cc804`](https://github.com/sgl-project/sglang/commit/43797cc804) [#25444](https://github.com/sgl-project/sglang/pull/25444)
  Bundle Scheduler rank/size fields into a frozen ParallelState (#25444)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py`, `python/sglang/srt/distributed/parallel_state_wrapper.py`, `python/sglang/srt/layers/dp_attention.py` _+10 more__
- **2026-05-16** [`27c3190215`](https://github.com/sgl-project/sglang/commit/27c3190215) [#25434](https://github.com/sgl-project/sglang/pull/25434)
  Remove fields that are never used in spec/engine/disagg (#25434)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/speculative/adaptive_spec_params.py`, `python/sglang/srt/speculative/cpp_ngram/ngram_corpus.py` _+1 more__
- **2026-05-15** [`f9caf43095`](https://github.com/sgl-project/sglang/commit/f9caf43095) [#25394](https://github.com/sgl-project/sglang/pull/25394)
  [CI] slash handler: lookup `runs_on` from `runner_configs.yml` (#25394)
  _Files: `.github/workflows/pr-states.yml`, `.github/workflows/rerun-test.yml`, `.github/workflows/slash-command-handler.yml`, `scripts/ci/utils/slash_command_handler.py` _+29 more__
- **2026-05-15** [`12408ec668`](https://github.com/sgl-project/sglang/commit/12408ec668) [#25125](https://github.com/sgl-project/sglang/pull/25125)
  [Disagg] Add retry with exponential backoff for prefill bootstrap reg… (#25125)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `test/registered/unit/disaggregation/test_register_to_bootstrap.py`_
- **2026-05-15** [`d89b678d69`](https://github.com/sgl-project/sglang/commit/d89b678d69) [#25316](https://github.com/sgl-project/sglang/pull/25316)
  move dead sglang.test files to test/manual (#25316)
  _Files: `python/sglang/test/attention/__init__.py`, `python/sglang/test/longbench_v2/__init__.py`, `test/manual/ascend/disaggregation_utils.py`, `test/manual/ascend/test_ascend_vocab_mask.py` _+25 more__
- **2026-05-14** [`ba214ef3d3`](https://github.com/sgl-project/sglang/commit/ba214ef3d3) [#24725](https://github.com/sgl-project/sglang/pull/24725)
  ci: tag-gated nightly migration — foundation + 40 whole-file moves (#24725)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`, `python/sglang/test/kits/streaming_session_kit.py` _+74 more__
- **2026-05-14** [`4be25f2428`](https://github.com/sgl-project/sglang/commit/4be25f2428) [#24378](https://github.com/sgl-project/sglang/pull/24378)
  fix(disagg): broadcast bootstrap port across multi-node prefill ranks (#24378)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`_
- **2026-05-14** [`0680f1b3d1`](https://github.com/sgl-project/sglang/commit/0680f1b3d1) [#23329](https://github.com/sgl-project/sglang/pull/23329)
  Add IntraNode NVLink configration in PD disaggregation docs (#23329)
  _Files: `docs/advanced_features/pd_disaggregation.md`, `docs_new/docs/advanced_features/pd_disaggregation.mdx`_
- **2026-05-14** [`be156d6804`](https://github.com/sgl-project/sglang/commit/be156d6804) [#24277](https://github.com/sgl-project/sglang/pull/24277)
  [HiCache] enable ssd offload support for mooncake store (#24277)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/mem_cache/storage/mooncake_store/README.md`, `python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py`_
- **2026-05-14** [`36c9495aaa`](https://github.com/sgl-project/sglang/commit/36c9495aaa) [#25236](https://github.com/sgl-project/sglang/pull/25236)
  ci: H200 conditional split + dsv4 est_time recalibration (h200 partition 6→2) (#25236)
  _Files: `test/registered/8-gpu-models/test_deepseek_v32_indexcache.py`, `test/registered/8-gpu-models/test_deepseek_v3_mtp.py`, `test/registered/8-gpu-models/test_dsa_models_mtp.py`, `test/registered/8-gpu-models/test_mimo_models.py` _+9 more__
- **2026-05-14** [`fd889097dc`](https://github.com/sgl-project/sglang/commit/fd889097dc) [#25064](https://github.com/sgl-project/sglang/pull/25064)
  [Bug Fix] Add priority property to DecodeRequest to fix AttributeError with --enable-priority-scheduling (#25064)
  _Files: `python/sglang/srt/disaggregation/decode.py`_
- **2026-05-13** [`3178a70577`](https://github.com/sgl-project/sglang/commit/3178a70577) [#25062](https://github.com/sgl-project/sglang/pull/25062)
  [PD Disaggregation] Fix priority scheduling in PD disaggregation mode (#25062)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/managers/scheduler.py`, `test/registered/unit/managers/test_priority_scheduling_disaggregation.py`_
- **2026-05-13** [`ff70aeac30`](https://github.com/sgl-project/sglang/commit/ff70aeac30) [#24491](https://github.com/sgl-project/sglang/pull/24491)
  [diffusion] feat: add performance mode server args (#24491)
  _Files: `docs/diffusion/api/cli.md`, `docs/diffusion/api/openai_api.md`, `docs/diffusion/performance/deployment_cookbook.md`, `docs/diffusion/performance/index.md` _+75 more__
- **2026-05-13** [`4984552cc9`](https://github.com/sgl-project/sglang/commit/4984552cc9) [#25145](https://github.com/sgl-project/sglang/pull/25145)
  Fix tests for decode radix cache (#25145)
  _Files: `test/registered/distributed/test_disaggregation_decode_radix_cache.py`_
- **2026-05-13** [`2a4d382b07`](https://github.com/sgl-project/sglang/commit/2a4d382b07) [#22536](https://github.com/sgl-project/sglang/pull/22536)
  [Disagg][NIXL] Add staging buffer support for heterogeneous TP KV transfer (#22536)
  _Files: `python/sglang/srt/disaggregation/common/staging_handler.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/nixl/conn.py`, `python/sglang/srt/server_args.py`_
- **2026-05-13** [`5227b07669`](https://github.com/sgl-project/sglang/commit/5227b07669) [#24973](https://github.com/sgl-project/sglang/pull/24973)
  [CI] Add DSV4 Flash disaggregation test (#24973)
  _Files: `test/registered/distributed/test_disaggregation_dsv4.py`_
- **2026-05-13** [`642ac9c916`](https://github.com/sgl-project/sglang/commit/642ac9c916) [#23893](https://github.com/sgl-project/sglang/pull/23893)
  [NPU]pp support mla kv transfer (#23893)
  _Files: `python/sglang/srt/disaggregation/ascend/conn.py`, `python/sglang/srt/disaggregation/base/conn.py`, `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/disaggregation/prefill.py` _+2 more__
- **2026-05-13** [`d6d3d0f599`](https://github.com/sgl-project/sglang/commit/d6d3d0f599) [#24857](https://github.com/sgl-project/sglang/pull/24857)
  Optimize SWA memory preallocation for disaggregated decode (#24857)
  _Files: `python/sglang/srt/disaggregation/decode.py`, `python/sglang/srt/mem_cache/swa_memory_pool.py`, `test/registered/unit/mem_cache/test_decode_radix_lock_ref.py`_

## Attention / FlashInfer  (42 commits)

- **2026-05-20** [`579fed2090`](https://github.com/sgl-project/sglang/commit/579fed2090) [#25737](https://github.com/sgl-project/sglang/pull/25737)
  Reduce excessively long logs caused by transformer version updates. (#25737)
  _Files: `test/registered/ascend/basic_function/HiCache/test_npu_hierarchical_cache_mla.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep.py`, `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py`, `test/registered/ascend/llm_models/test_npu_qwq_32b_w8a8.py` _+1 more__
- **2026-05-19** [`425dffbde3`](https://github.com/sgl-project/sglang/commit/425dffbde3) [#24934](https://github.com/sgl-project/sglang/pull/24934)
  DeepSeek V4 MTP Support CP (#24934)
  _Files: `python/sglang/srt/models/deepseek_v4_nextn.py`, `test/registered/dsv4/test_deepseek_v4_flash_fp4_b200.py`_
- **2026-05-19** [`beaff00331`](https://github.com/sgl-project/sglang/commit/beaff00331) [#25299](https://github.com/sgl-project/sglang/pull/25299)
  [NSA] Avoid repeated NSA MQA logits memory queries (#25299)
  _Files: `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`_
- **2026-05-19** [`b9d470f4a2`](https://github.com/sgl-project/sglang/commit/b9d470f4a2) [#24640](https://github.com/sgl-project/sglang/pull/24640)
  Support spec v2 for FlashMLA speculative decoding (#24640)
  _Files: `python/sglang/srt/layers/attention/flashmla_backend.py`, `python/sglang/srt/models/deepseek_v2.py`, `test/registered/mla/test_flashmla.py`_
- **2026-05-19** [`b9c2bf717b`](https://github.com/sgl-project/sglang/commit/b9c2bf717b) [#23331](https://github.com/sgl-project/sglang/pull/23331)
  [BugFix] Resolve adaptive speculative decoding conflicts for Qwen3.5 (hybrid GDN) (#23331)
  _Files: `python/sglang/srt/layers/attention/fla/fused_sigmoid_gating_recurrent.py`, `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/model_executor/model_runner_kv_cache_mixin.py`, `python/sglang/srt/models/qwen3_5_mtp.py` _+5 more__
- **2026-05-19** [`45a85efc3a`](https://github.com/sgl-project/sglang/commit/45a85efc3a) [#23482](https://github.com/sgl-project/sglang/pull/23482)
  [Diffusion][NPU]Add attention backends for diffusion models for Ascend NPU (#23482)
  _Files: `docs/diffusion/compatibility_matrix.md`, `docs/diffusion/performance/attention_backends.md`, `docs_new/docs/sglang-diffusion/attention_backends.mdx`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx` _+8 more__
- **2026-05-19** [`862d39e06c`](https://github.com/sgl-project/sglang/commit/862d39e06c) [#24954](https://github.com/sgl-project/sglang/pull/24954)
  [Mamba] Fix extra_buffer overlap schedule races (#24954)
  _Files: `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py`, `python/sglang/srt/mem_cache/mamba_radix_cache.py` _+4 more__
- **2026-05-19** [`d8e66e54e5`](https://github.com/sgl-project/sglang/commit/d8e66e54e5) [#25570](https://github.com/sgl-project/sglang/pull/25570)
  fix: use triton_attn as default vision attention on B300 (SM103) (#25570)
  _Files: `python/sglang/srt/layers/attention/vision.py`_
- **2026-05-19** [`d90bc65e30`](https://github.com/sgl-project/sglang/commit/d90bc65e30) [#25383](https://github.com/sgl-project/sglang/pull/25383)
  [NPU] Fix TypeError in get_state_buf_infos when index_head_dim is None on MLA (#25383)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-05-18** [`1f185c6ba8`](https://github.com/sgl-project/sglang/commit/1f185c6ba8) [#25489](https://github.com/sgl-project/sglang/pull/25489)
  Support draft extend cuda graph for tokenspeed_mla attention backend (#25489)
  _Files: `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`_
- **2026-05-18** [`b29e41e8b3`](https://github.com/sgl-project/sglang/commit/b29e41e8b3) [#25547](https://github.com/sgl-project/sglang/pull/25547)
  Respect user override for Gemma4 attention backend (#25547)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-05-18** [`c54b34c007`](https://github.com/sgl-project/sglang/commit/c54b34c007) [#25638](https://github.com/sgl-project/sglang/pull/25638)
  Move module-level helpers out of scheduler.py (#25638)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`, `python/sglang/srt/managers/scheduler_components/idle_sleeper.py`, `python/sglang/srt/managers/scheduler_components/invariant_checker.py` _+5 more__
- **2026-05-18** [`8d5ed330cc`](https://github.com/sgl-project/sglang/commit/8d5ed330cc) [#21668](https://github.com/sgl-project/sglang/pull/21668)
  [XPU] Enable qwen3.5 on XPU (#21668)
  _Files: `docker/xpu.Dockerfile`, `docs_new/docs/hardware-platforms/xpu.mdx`, `python/sglang/bench_one_batch.py`, `python/sglang/srt/hardware_backend/xpu/__init__.py` _+10 more__
- **2026-05-18** [`5147de26e4`](https://github.com/sgl-project/sglang/commit/5147de26e4) [#25180](https://github.com/sgl-project/sglang/pull/25180)
  Fix AMX GQA extend attention (#25180)
  _Files: `sgl-kernel/csrc/cpu/flash_attn.h`, `test/srt/cpu/test_extend.py`_
- **2026-05-18** [`2a357071ec`](https://github.com/sgl-project/sglang/commit/2a357071ec) [#25249](https://github.com/sgl-project/sglang/pull/25249)
  [NPU]fix:NPUMLATokenToKVPool object has no attribute "kv_buffer" (#25249)
  _Files: `python/sglang/srt/hardware_backend/npu/memory_pool_npu.py`_
- **2026-05-18** [`58ece60703`](https://github.com/sgl-project/sglang/commit/58ece60703) [#25516](https://github.com/sgl-project/sglang/pull/25516)
  refactor: remove ModelWorkerBatch indirection (#25516)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/srt/hardware_backend/mlx/scheduler_mixin.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/managers/overlap_utils.py` _+17 more__
- **2026-05-17** [`c67b287056`](https://github.com/sgl-project/sglang/commit/c67b287056) [#25006](https://github.com/sgl-project/sglang/pull/25006)
  Enable trtllm_mha as gemma4 default attn backend. (#25006)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-05-16** [`9869ef0849`](https://github.com/sgl-project/sglang/commit/9869ef0849) [#25488](https://github.com/sgl-project/sglang/pull/25488)
  Revert "[attn backend] avoid initing parent class's workspace buffer" (#25488)
  _Files: `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-05-16** [`2f81718773`](https://github.com/sgl-project/sglang/commit/2f81718773) [#25321](https://github.com/sgl-project/sglang/pull/25321)
  [attn backend] avoid initing parent class's workspace buffer (#25321)
  _Files: `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-05-16** [`aec4022e58`](https://github.com/sgl-project/sglang/commit/aec4022e58) [#25424](https://github.com/sgl-project/sglang/pull/25424)
  [Spec] Clean up draft-window-size handling; extract spec arg setup to arg_groups (#25424)
  _Files: `python/sglang/srt/arg_groups/argparse_actions.py`, `python/sglang/srt/arg_groups/speculative_hook.py`, `python/sglang/srt/models/llama_eagle3.py`, `python/sglang/srt/server_args.py` _+3 more__
- **2026-05-16** [`d1eb472a7a`](https://github.com/sgl-project/sglang/commit/d1eb472a7a) [#25473](https://github.com/sgl-project/sglang/pull/25473)
  fix(overlap): skip empty future interval for dp attention idle ranks (#25473)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-16** [`33d63aa7e1`](https://github.com/sgl-project/sglang/commit/33d63aa7e1) [#25432](https://github.com/sgl-project/sglang/pull/25432)
  Remove dead self.adder/can_run_list/running_bs writes in Scheduler._get_new_batch_prefill_raw (#25432)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-16** [`afc7c9f7f3`](https://github.com/sgl-project/sglang/commit/afc7c9f7f3) [#25103](https://github.com/sgl-project/sglang/pull/25103)
  [TRTLLM/SWA/Spec] fix trtllm mha + swa + spec accept length drop (#25103)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-05-15** [`ee93795476`](https://github.com/sgl-project/sglang/commit/ee93795476) [#25333](https://github.com/sgl-project/sglang/pull/25333)
  perf(mla): hybrid Triton fused cat+FP8-quantize for MLA chunked-prefill K/V (#25333)
  _Files: `python/sglang/jit_kernel/benchmark/bench_mla_kv_pack_quantize_fp8.py`, `python/sglang/jit_kernel/mla_kv_pack_quantize_fp8.py`, `python/sglang/jit_kernel/tests/test_mla_kv_pack_quantize_fp8.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`_
- **2026-05-15** [`34cb8e2842`](https://github.com/sgl-project/sglang/commit/34cb8e2842) [#24130](https://github.com/sgl-project/sglang/pull/24130)
  fix(sgl-kernel): sm90 compile flashmla failed (#24130)
  _Files: `sgl-kernel/cmake/flashmla.cmake`, `sgl-kernel/csrc/flashmla_extension.cc`_
- **2026-05-15** [`897587b03a`](https://github.com/sgl-project/sglang/commit/897587b03a) [#24978](https://github.com/sgl-project/sglang/pull/24978)
  [MUSA]: Add flashinfer sampling backend (#24978)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject_other.toml`, `python/sglang/srt/layers/sampler.py`, `sgl-kernel/csrc/common_extension_musa.cc` _+5 more__
- **2026-05-15** [`dca9ba6321`](https://github.com/sgl-project/sglang/commit/dca9ba6321) [#25311](https://github.com/sgl-project/sglang/pull/25311)
  perf(mla): TMA bulk-store set_mla_kv_buffer (up to 12× over baseline) (#25311)
  _Files: `python/sglang/jit_kernel/benchmark/bench_set_mla_kv_buffer.py`, `python/sglang/jit_kernel/csrc/elementwise/set_mla_kv_buffer.cuh`, `python/sglang/jit_kernel/set_mla_kv_buffer.py`, `python/sglang/jit_kernel/tests/test_set_mla_kv_buffer.py` _+1 more__
- **2026-05-15** [`1913cb4dbb`](https://github.com/sgl-project/sglang/commit/1913cb4dbb) [#25329](https://github.com/sgl-project/sglang/pull/25329)
  Skip CI tests added in #24816 (broken on main) (#25329)
  _Files: `test/registered/dsv4/test_deepseek_v4_flash_fp4_h200.py`, `test/registered/unit/layers/quantization/test_mxfp4_sm90_cutlass.py`_
- **2026-05-14** [`22bfae0d1d`](https://github.com/sgl-project/sglang/commit/22bfae0d1d) [#25205](https://github.com/sgl-project/sglang/pull/25205)
  [AMD]  Auto-fallback NSA indexer to page_size=1 when aiter preshuffle gluon kernel is unavailable (Deepseek v3.2) (#25205)
  _Files: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/layers/attention/nsa/utils.py`, `python/sglang/srt/mem_cache/memory_pool.py` _+1 more__
- **2026-05-14** [`3640116397`](https://github.com/sgl-project/sglang/commit/3640116397) [#25130](https://github.com/sgl-project/sglang/pull/25130)
  [NPU]Bugfix:Set default values for npu_wrapper_preprocess parameters (#25130)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/hardware_backend/npu/modules/qwen_vl_processor.py`_
- **2026-05-14** [`34c0029f0a`](https://github.com/sgl-project/sglang/commit/34c0029f0a) [#21431](https://github.com/sgl-project/sglang/pull/21431)
  [diffusion] [AMD] feat: support online MXFP4 and fp8 quantization (#21431)
  _Files: `docs/diffusion/api/cli.md`, `docs/diffusion/quantization.md`, `python/sglang/jit_kernel/flash_attention_v3.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py` _+6 more__
- **2026-05-14** [`7618ad7075`](https://github.com/sgl-project/sglang/commit/7618ad7075) [#24925](https://github.com/sgl-project/sglang/pull/24925)
  [attn backend] Integrate tokenspeed_mla prefill/decode kernels (fp8 kv cache, blackwell) (#24925)
  _Files: `python/pyproject.toml`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py` _+7 more__
- **2026-05-13** [`01a225ac6f`](https://github.com/sgl-project/sglang/commit/01a225ac6f) [#25001](https://github.com/sgl-project/sglang/pull/25001)
  [LoRA] MLA attention LoRA: q_b_proj / kv_b_proj support (#25001)
  _Files: `python/sglang/srt/lora/deepseek_mla_correction.py`, `python/sglang/srt/lora/triton_ops/__init__.py`, `python/sglang/srt/lora/triton_ops/kv_b_lora_absorbed.py`, `python/sglang/srt/lora/utils.py` _+3 more__
- **2026-05-13** [`e2290b155a`](https://github.com/sgl-project/sglang/commit/e2290b155a) [#24890](https://github.com/sgl-project/sglang/pull/24890)
  Port KV Compression V2 from deepseek_v4_dev (#24890)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_online_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh` _+19 more__
- **2026-05-13** [`fc20f5b114`](https://github.com/sgl-project/sglang/commit/fc20f5b114) [#24125](https://github.com/sgl-project/sglang/pull/24125)
  [AMD] Skip redundant CatArrayBatchedCopy in GLM-5 NSA TileLang decode (#24125)
  _Files: `python/sglang/srt/layers/attention/nsa_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-05-13** [`a9359707c1`](https://github.com/sgl-project/sglang/commit/a9359707c1) [#23562](https://github.com/sgl-project/sglang/pull/23562)
  [AMD] Enable preshuffle paged MQA and page_size=64 for NSA indexer (#23562)
  _Files: `python/sglang/srt/layers/attention/nsa/index_buf_accessor.py`, `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/server_args.py`_
- **2026-05-13** [`7d515c6d1f`](https://github.com/sgl-project/sglang/commit/7d515c6d1f) [#25152](https://github.com/sgl-project/sglang/pull/25152)
  docs: prepend SGLANG_JIT_DEEPGEMM_PRECOMPILE=0 for H200 FP8 Flash max-throughput (#25152)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-13** [`839f7f2696`](https://github.com/sgl-project/sglang/commit/839f7f2696) [#24148](https://github.com/sgl-project/sglang/pull/24148)
  [AMD] Add _skip_rope_for_aiter_fused_mla method and check to avoid double rotating with gfx950 and Aiter backend (#24148)
  _Files: `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mla.py`_
- **2026-05-13** [`51a9403104`](https://github.com/sgl-project/sglang/commit/51a9403104) [#25129](https://github.com/sgl-project/sglang/pull/25129)
  Update flashinfer to 0.6.11.post1 (#25129)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/utils/common.py`_
- **2026-05-13** [`72b266d59b`](https://github.com/sgl-project/sglang/commit/72b266d59b) [#25039](https://github.com/sgl-project/sglang/pull/25039)
  [AMD] Disable unittest fail-fast for deepseekv4 perf test (#25039)
  _Files: `test/registered/amd/test_deepseek_v4_flash_fp4.py`, `test/registered/amd/test_deepseek_v4_flash_fp8.py`, `test/registered/amd/test_deepseek_v4_pro_fp4.py`, `test/registered/amd/test_deepseek_v4_pro_fp8.py`_
- **2026-05-13** [`c665edec6e`](https://github.com/sgl-project/sglang/commit/c665edec6e) [#25120](https://github.com/sgl-project/sglang/pull/25120)
  [env] Make max KV chunk capacity configurable via `SGLANG_MAX_KV_CHUNK_CAPACITY` (#25120)
  _Files: `docs/references/environment_variables.md`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py` _+1 more__
- **2026-05-13** [`4e35c30cbe`](https://github.com/sgl-project/sglang/commit/4e35c30cbe) [#25022](https://github.com/sgl-project/sglang/pull/25022)
  [Bugfix, NSA HiCache] Fix missing override_kv_cache_dim in attach_hybrid_nsa_pool_to_hiradix_cache (#25022)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_

## MoE / Expert Parallel  (41 commits)

- **2026-05-20** [`65fe32379e`](https://github.com/sgl-project/sglang/commit/65fe32379e) [#24641](https://github.com/sgl-project/sglang/pull/24641)
  [Intel GPU]Support fused_topk for XPU (#24641)
  _Files: `python/sglang/srt/layers/moe/topk.py`_
- **2026-05-19** [`2bcb6d2f82`](https://github.com/sgl-project/sglang/commit/2bcb6d2f82) [#25524](https://github.com/sgl-project/sglang/pull/25524)
  [Bug Fix] Align glm4_moe_nextn NPU MTP loading with qwen3 MTP (#25524)
  _Files: `python/sglang/srt/models/glm4_moe_nextn.py`_
- **2026-05-19** [`78cb38ed5e`](https://github.com/sgl-project/sglang/commit/78cb38ed5e) [#22918](https://github.com/sgl-project/sglang/pull/22918)
  [FlashInfer v0.6.11] [RL] Support FlashInfer per-token NVFP4 MoE (#22918)
  _Files: `docs/references/environment_variables.md`, `docs_new/docs/references/environment_variables.mdx`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+2 more__
- **2026-05-19** [`31e324391b`](https://github.com/sgl-project/sglang/commit/31e324391b) [#24611](https://github.com/sgl-project/sglang/pull/24611)
  [Codex] Opt Mistral Large performace  (#24611)
  _Files: `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=128,N=1024,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8.json`, `python/sglang/srt/layers/moe/moe_runner/triton_utils/configs/triton_3_5_1/E=128,N=1024,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8_down.json`, `python/sglang/srt/server_args.py`_
- **2026-05-18** [`745abd6cc0`](https://github.com/sgl-project/sglang/commit/745abd6cc0) [#25688](https://github.com/sgl-project/sglang/pull/25688)
  Add no_combine support to cutlass_moe_fp4 (#25688)
  _Files: `python/sglang/srt/layers/moe/cutlass_moe.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`_
- **2026-05-18** [`878e6b8886`](https://github.com/sgl-project/sglang/commit/878e6b8886) [#25685](https://github.com/sgl-project/sglang/pull/25685)
  [SP] Fix runtime_max_tokens_per_rank for sequence parallelism (#25685)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`_
- **2026-05-18** [`6f892047ec`](https://github.com/sgl-project/sglang/commit/6f892047ec) [#25509](https://github.com/sgl-project/sglang/pull/25509)
  [misc] Throw error when single batch overlap is enabled on Hopper  (#25509)
  _Files: `python/sglang/srt/layers/moe/utils.py`_
- **2026-05-18** [`d96e593fd0`](https://github.com/sgl-project/sglang/commit/d96e593fd0) [#25571](https://github.com/sgl-project/sglang/pull/25571)
  [Benchmark] Add SGLANG_SIMULATE_UNIFORM_EXPERTS for balanced expert routing with dummy weights (#25571)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/topk.py`_
- **2026-05-18** [`866793c502`](https://github.com/sgl-project/sglang/commit/866793c502) [#24933](https://github.com/sgl-project/sglang/pull/24933)
  Amd/deepseek v4 rebase main 0509 (#24933)
  _Files: `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/attention_registry.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py` _+13 more__
- **2026-05-18** [`ba2ffcf156`](https://github.com/sgl-project/sglang/commit/ba2ffcf156) [#25569](https://github.com/sgl-project/sglang/pull/25569)
  Add DeepSeekV4 fused MoE Triton autotune support (#25569)
  _Files: `benchmark/kernels/fused_moe_triton/common_utils.py`, `benchmark/kernels/fused_moe_triton/tuning_fused_moe_triton.py`_
- **2026-05-18** [`1f9eda4ea1`](https://github.com/sgl-project/sglang/commit/1f9eda4ea1) [#25540](https://github.com/sgl-project/sglang/pull/25540)
  Use DeepGEMM BF16 for unquantized DeepEP LL MoE (#25540)
  _Files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/quantization/unquant.py`_
- **2026-05-18** [`6a21dd20b1`](https://github.com/sgl-project/sglang/commit/6a21dd20b1) [#25285](https://github.com/sgl-project/sglang/pull/25285)
  Fix EPLB mapping for TopK paths (#25285)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `test/registered/cpu/test_topk.py`_
- **2026-05-18** [`a080358cac`](https://github.com/sgl-project/sglang/commit/a080358cac) [#22822](https://github.com/sgl-project/sglang/pull/22822)
  [Refactor] Refactor DeepEP dispatcher (#22822)
  _Files: `docs/advanced_features/server_arguments.md`, `docs/platforms/ascend/ascend_npu_best_practice.md`, `docs/platforms/ascend/ascend_npu_deepseek_example.md`, `docs/platforms/ascend/ascend_npu_environment_variables.md` _+26 more__
- **2026-05-17** [`7158a255eb`](https://github.com/sgl-project/sglang/commit/7158a255eb) [#25525](https://github.com/sgl-project/sglang/pull/25525)
  [MoE Refactor] Migrate flashinfer_cutedsl + DeepEP to MoeRunner (#25525)
  _Files: `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py` _+1 more__
- **2026-05-17** [`be3c425788`](https://github.com/sgl-project/sglang/commit/be3c425788) [#23760](https://github.com/sgl-project/sglang/pull/23760)
  [MoE] Unify DeepEPMoE+MoriEPMoE through AITER MoeRunner pre/post-permute (#23760)
  _Files: `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/moe_runner/aiter.py`, `python/sglang/srt/layers/moe/moe_runner/runner.py` _+9 more__
- **2026-05-17** [`568ba7216a`](https://github.com/sgl-project/sglang/commit/568ba7216a) [#25522](https://github.com/sgl-project/sglang/pull/25522)
  Fix logging for inplace setting in the flashInfer-trtllm backend (#25522)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-05-17** [`229cadec04`](https://github.com/sgl-project/sglang/commit/229cadec04) [#25499](https://github.com/sgl-project/sglang/pull/25499)
  Update logging for inplace setting in MoE layer (#25499)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`_
- **2026-05-16** [`57eb5bdaf6`](https://github.com/sgl-project/sglang/commit/57eb5bdaf6) [#25412](https://github.com/sgl-project/sglang/pull/25412)
  [Doc] DSV4 cookbook: clean up env vars, add MegaMoE toggle, unify docker image (#25412)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-16** [`b2c6db0cc4`](https://github.com/sgl-project/sglang/commit/b2c6db0cc4) [#25406](https://github.com/sgl-project/sglang/pull/25406)
  [MoE] Decouple Mega MoE from DeepEP backend (#25406)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py` _+14 more__
- **2026-05-16** [`ce2506e1c6`](https://github.com/sgl-project/sglang/commit/ce2506e1c6) [#24314](https://github.com/sgl-project/sglang/pull/24314)
  Deprecate record_nolora_graph dual MoE CUDA graph capture (#24314)
  _Files: `python/sglang/srt/layers/moe/utils.py`, `python/sglang/srt/lora/lora_moe_runners.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/server_args.py`_
- **2026-05-16** [`d523ae127f`](https://github.com/sgl-project/sglang/commit/d523ae127f) [#25407](https://github.com/sgl-project/sglang/pull/25407)
  Fix Mistral Large 3 nightly test (#25407)
  _Files: `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a4_nvfp4_moe.py`_
- **2026-05-15** [`54221dd998`](https://github.com/sgl-project/sglang/commit/54221dd998) [#25379](https://github.com/sgl-project/sglang/pull/25379)
  feat(moe): reuse prev-layer output as symm_output for FP4 routed MoE (#25379)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/moe_runner/base.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py` _+1 more__
- **2026-05-15** [`1a1d69507d`](https://github.com/sgl-project/sglang/commit/1a1d69507d) [#25378](https://github.com/sgl-project/sglang/pull/25378)
  [Doc] Update MegaMoE usage (#25378)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-15** [`0c19540550`](https://github.com/sgl-project/sglang/commit/0c19540550) [#25335](https://github.com/sgl-project/sglang/pull/25335)
  [Fix] Fix gpt oss triton kernels and upgrade flashinfer back to 0.6.11.post1 (#25335)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py` _+9 more__
- **2026-05-15** [`ad4994dc1d`](https://github.com/sgl-project/sglang/commit/ad4994dc1d) [#25279](https://github.com/sgl-project/sglang/pull/25279)
  DeepseekV2MoE: defer shared experts when routed kernel is non-mutating (#25279)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-15** [`8d5b347edd`](https://github.com/sgl-project/sglang/commit/8d5b347edd) [#24906](https://github.com/sgl-project/sglang/pull/24906)
  Support Qwen3.5 NVFP4 MTP DeepEP (#24906)
  _Files: `python/sglang/srt/layers/attention/linear/gdn_backend.py`, `python/sglang/srt/layers/attention/linear/kernels/gdn_flashinfer.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`_
- **2026-05-14** [`67096f48bf`](https://github.com/sgl-project/sglang/commit/67096f48bf) [#25317](https://github.com/sgl-project/sglang/pull/25317)
  Revert "[MoE] Decouple Mega MoE from DeepEP backend" (#25317)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py` _+4 more__
- **2026-05-14** [`22dfcdaa04`](https://github.com/sgl-project/sglang/commit/22dfcdaa04) [#25310](https://github.com/sgl-project/sglang/pull/25310)
  revert flashinfer 0.6.11 bumps (#25310)
  _Files: `docker/Dockerfile`, `python/pyproject.toml`, `python/sglang/srt/entrypoints/engine.py`, `python/sglang/srt/layers/flashinfer_comm_fusion.py` _+3 more__
- **2026-05-14** [`37f030a0de`](https://github.com/sgl-project/sglang/commit/37f030a0de) [#24884](https://github.com/sgl-project/sglang/pull/24884)
  [MoE] Decouple Mega MoE from DeepEP backend (#24884)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py` _+4 more__
- **2026-05-14** [`4593bbdf31`](https://github.com/sgl-project/sglang/commit/4593bbdf31) [#25263](https://github.com/sgl-project/sglang/pull/25263)
  ci: dynamic partition + LPT from live sglang-ci-stats model (#25263)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test.yml`, `python/sglang/test/ci/ci_register.py` _+3 more__
- **2026-05-14** [`a6a6c3119b`](https://github.com/sgl-project/sglang/commit/a6a6c3119b) [#24717](https://github.com/sgl-project/sglang/pull/24717)
  LFM2: pass has_initial_state to causal_conv1d_fn for prefill (#24717)
  _Files: `python/sglang/srt/models/lfm2.py`, `python/sglang/srt/models/lfm2_moe.py`_
- **2026-05-14** [`c701a08765`](https://github.com/sgl-project/sglang/commit/c701a08765) [#19290](https://github.com/sgl-project/sglang/pull/19290)
  feat: [2/2][DeepEP] Add waterfill load balancing for shared expert dispatch (#19290)
  _Files: `docs/advanced_features/server_arguments.md`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/deepep_waterfill.py`, `python/sglang/srt/layers/moe/topk.py` _+4 more__
- **2026-05-14** [`426dd339da`](https://github.com/sgl-project/sglang/commit/426dd339da) [#25139](https://github.com/sgl-project/sglang/pull/25139)
  Migrate Intel CPU cases to the test/registered (#25139)
  _Files: `.github/workflows/pr-test-xeon.yml`, `.pre-commit-config.yaml`, `scripts/ci/check_registered_tests.py`, `test/registered/cpu/test_activation.py` _+23 more__
- **2026-05-14** [`1e308aec66`](https://github.com/sgl-project/sglang/commit/1e308aec66) [#25203](https://github.com/sgl-project/sglang/pull/25203)
  ci: B200 conditional split + LPT_SLOP removal (stage-c partition 8→3) (#25203)
  _Files: `scripts/ci/utils/compute_partitions.py`, `test/registered/4-gpu-models/test_gpt_oss_4gpu.py`, `test/registered/4-gpu-models/test_nvidia_nemotron_3_super_nvfp4.py`, `test/registered/4-gpu-models/test_qwen35_fp4_mtp_v2.py` _+15 more__
- **2026-05-14** [`b7f856df70`](https://github.com/sgl-project/sglang/commit/b7f856df70) [#25052](https://github.com/sgl-project/sglang/pull/25052)
  DeepSeek V4 w4a4 MegaMoE (#25052)
  _Files: `python/pyproject.toml`, `python/sglang/srt/environ.py`, `python/sglang/srt/layers/moe/mega_moe.py`, `test/registered/dsv4/test_deepseek_v4_flash_fp4_b200.py` _+1 more__
- **2026-05-13** [`37f18438c5`](https://github.com/sgl-project/sglang/commit/37f18438c5) [#24986](https://github.com/sgl-project/sglang/pull/24986)
  [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper (#24986)
  _Files: `python/sglang/jit_kernel/csrc/gemm/marlin_moe/moe_wna16_marlin.cuh`, `python/sglang/srt/layers/moe/fused_moe_triton/fused_marlin_moe.py`, `python/sglang/srt/layers/quantization/marlin_utils_fp4.py`, `python/sglang/srt/layers/quantization/mxfp4.py` _+3 more__
- **2026-05-13** [`28758d37dd`](https://github.com/sgl-project/sglang/commit/28758d37dd) [#24816](https://github.com/sgl-project/sglang/pull/24816)
  Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 (#24816)
  _Files: `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/layers/quantization/fp8.py`, `python/sglang/srt/layers/quantization/mxfp4.py`, `python/sglang/srt/layers/quantization/mxfp4_flashinfer_cutlass_moe.py` _+4 more__
- **2026-05-13** [`22012ba1bc`](https://github.com/sgl-project/sglang/commit/22012ba1bc) [#17392](https://github.com/sgl-project/sglang/pull/17392)
  Add BF16 support to EP-MoE for DeepGEMM (#17392)
  _Files: `python/sglang/srt/layers/deep_gemm_wrapper/compile_utils.py`, `python/sglang/srt/layers/deep_gemm_wrapper/entrypoint.py`, `python/sglang/srt/layers/moe/ep_moe/kernels.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py` _+6 more__
- **2026-05-13** [`9e00b7ca95`](https://github.com/sgl-project/sglang/commit/9e00b7ca95) [#24575](https://github.com/sgl-project/sglang/pull/24575)
  [NPU] add zbal support for npu (#24575)
  _Files: `python/sglang/srt/distributed/parallel_state.py`, `python/sglang/srt/environ.py`, `python/sglang/srt/hardware_backend/npu/utils.py`, `python/sglang/srt/layers/moe/token_dispatcher/deepep.py` _+3 more__
- **2026-05-13** [`66a9234246`](https://github.com/sgl-project/sglang/commit/66a9234246) [#24879](https://github.com/sgl-project/sglang/pull/24879)
  [AMD] support fp8 blockwise quantization combine for mori ep (#24879)
  _Files: `docker/rocm.Dockerfile`, `python/sglang/srt/layers/moe/token_dispatcher/moriep.py`_
- **2026-05-13** [`409d350fb6`](https://github.com/sgl-project/sglang/commit/409d350fb6) [#19329](https://github.com/sgl-project/sglang/pull/19329)
  Bugfix: fix symm not enabled due to incorrect registration of comm (#19329)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_nsa_cp.py`, `python/sglang/srt/layers/dp_attention.py`, `python/sglang/srt/layers/moe/token_dispatcher/standard.py`_

## Multimodal  (27 commits)

- **2026-05-20** [`5fe655bf26`](https://github.com/sgl-project/sglang/commit/5fe655bf26) [#24231](https://github.com/sgl-project/sglang/pull/24231)
  vlm: fix shared memory bug of deep copy mm_items (#24231)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-20** [`d69e9fbfdc`](https://github.com/sgl-project/sglang/commit/d69e9fbfdc) [#22289](https://github.com/sgl-project/sglang/pull/22289)
  [diffusion] fix: honor config precisions for delight/paint (#22289)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/hunyuan3d_paint.py`_
- **2026-05-20** [`549ae16c6f`](https://github.com/sgl-project/sglang/commit/549ae16c6f) [#21980](https://github.com/sgl-project/sglang/pull/21980)
  [diffusion] fix: respect configured precision in Qwen layered path (#21980)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/qwen_image.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/qwen_image_layered.py`_
- **2026-05-20** [`3a9d9d5832`](https://github.com/sgl-project/sglang/commit/3a9d9d5832) [#22729](https://github.com/sgl-project/sglang/pull/22729)
  [diffusion] fix: fix Hunyuan3D-2 DiT checkpoint param mapping (#22729)
  _Files: `python/sglang/multimodal_gen/configs/models/dits/hunyuan3d.py`_
- **2026-05-19** [`3b62604cec`](https://github.com/sgl-project/sglang/commit/3b62604cec) [#25645](https://github.com/sgl-project/sglang/pull/25645)
  [Diffusion] Support parallelism for GLM-Image (#25645)
  _Files: `python/pyproject_npu.toml`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/pipelines/glm_image.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/parallel_executor.py` _+2 more__
- **2026-05-19** [`58b5fe3e29`](https://github.com/sgl-project/sglang/commit/58b5fe3e29) [#25592](https://github.com/sgl-project/sglang/pull/25592)
  [Diffusion] [NPU] Fix HunyuanVideo crash on NPU (#25592)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/hunyuanvideo.py`_
- **2026-05-19** [`f0763859ed`](https://github.com/sgl-project/sglang/commit/f0763859ed) [#25588](https://github.com/sgl-project/sglang/pull/25588)
  perf(mimo-v2-epd): enable GPU image preprocess and parallel video decode (#25588)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/multimodal/processors/mimo_v2.py`, `python/sglang/srt/utils/video_decoder.py`_
- **2026-05-19** [`a7b3ced334`](https://github.com/sgl-project/sglang/commit/a7b3ced334) [#25596](https://github.com/sgl-project/sglang/pull/25596)
  [diffusion] fix: fix LTX2 resident defaults and stage profiling (#25596)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/diffusers_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/base.py`, `python/sglang/multimodal_gen/runtime/server_args.py` _+3 more__
- **2026-05-18** [`110bbdcad7`](https://github.com/sgl-project/sglang/commit/110bbdcad7) [#25591](https://github.com/sgl-project/sglang/pull/25591)
  [diffusion] fix: use dynamic LoRA for LTX2 original stage-two (#25591)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`_
- **2026-05-18** [`b3803164cb`](https://github.com/sgl-project/sglang/commit/b3803164cb) [#23294](https://github.com/sgl-project/sglang/pull/23294)
  [diffusion] fix: fix unipc device placement + flowunipc sigma_min crash (#23294)
  _Files: `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_flow_unipc_multistep.py`, `python/sglang/multimodal_gen/runtime/models/schedulers/scheduling_unipc_multistep.py`_
- **2026-05-17** [`89e501c5a8`](https://github.com/sgl-project/sglang/commit/89e501c5a8) [#25510](https://github.com/sgl-project/sglang/pull/25510)
  [diffusion] CI: tighten selected perf baselines (#25510)
  _Files: `python/sglang/multimodal_gen/runtime/server_args.py`, `python/sglang/multimodal_gen/test/server/ascend/perf_baselines_npu.json`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`_
- **2026-05-17** [`3bf7e346fc`](https://github.com/sgl-project/sglang/commit/3bf7e346fc) [#25256](https://github.com/sgl-project/sglang/pull/25256)
  [MUSA][Diffusion] Improve  wan model inference speed using torch.compile (#25256)
  _Files: `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`, `python/sglang/multimodal_gen/runtime/layers/elementwise.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`_
- **2026-05-17** [`eccfd6dea7`](https://github.com/sgl-project/sglang/commit/eccfd6dea7) [#25517](https://github.com/sgl-project/sglang/pull/25517)
  [diffusion] feat: configure encoder as layerwise-offload by default (#25517)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/transformer_loader.py`, `python/sglang/multimodal_gen/runtime/managers/gpu_worker.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py` _+22 more__
- **2026-05-17** [`46e0f5007d`](https://github.com/sgl-project/sglang/commit/46e0f5007d) [#22371](https://github.com/sgl-project/sglang/pull/22371)
  Fix image (random multimodal) dataset token statistics (#22371)
  _Files: `python/sglang/benchmark/datasets/image.py`_
- **2026-05-17** [`c1d9e37a52`](https://github.com/sgl-project/sglang/commit/c1d9e37a52) [#25457](https://github.com/sgl-project/sglang/pull/25457)
  [diffusion] feat: add memory-aware component load order (#25457)
  _Files: `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_loading_order.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_manager.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/component_resident_strategies.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/composed_pipeline_base.py` _+2 more__
- **2026-05-16** [`9f26697d6a`](https://github.com/sgl-project/sglang/commit/9f26697d6a) [#25410](https://github.com/sgl-project/sglang/pull/25410)
  [Docs] Update DeepSeek V4 cookbook to use the latest docker image (#25410)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`_
- **2026-05-16** [`596b45b373`](https://github.com/sgl-project/sglang/commit/596b45b373) [#25411](https://github.com/sgl-project/sglang/pull/25411)
  [diffusion] fix: change default qwen-image vae precision to bf16 (#25411)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/ltx_2.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/mova.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py` _+2 more__
- **2026-05-16** [`93bacc25ed`](https://github.com/sgl-project/sglang/commit/93bacc25ed) [#24732](https://github.com/sgl-project/sglang/pull/24732)
  [codex] Optimize LTX2 split rotary kernel (#24732)
  _Files: `python/sglang/jit_kernel/diffusion/triton/ltx2_rotary.py`_
- **2026-05-16** [`7f37ffae9d`](https://github.com/sgl-project/sglang/commit/7f37ffae9d) [#25241](https://github.com/sgl-project/sglang/pull/25241)
  [diffusion] CI: fix nightly CI (#25241)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines/ltx_2_pipeline.py`, `python/sglang/multimodal_gen/runtime/server_args.py`, `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-05-16** [`416fdbbb3d`](https://github.com/sgl-project/sglang/commit/416fdbbb3d) [#24593](https://github.com/sgl-project/sglang/pull/24593)
  [diffusion] feat: generalize layerwise offload residency mixin to all components (#24593)
  _Files: `docs/diffusion/api/cli.md`, `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/component_loader.py` _+62 more__
- **2026-05-15** [`fd9525436b`](https://github.com/sgl-project/sglang/commit/fd9525436b) [#25264](https://github.com/sgl-project/sglang/pull/25264)
  move runs_on + rdma into runner_configs.yml (#25264)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test-jit-kernel.yml` _+5 more__
- **2026-05-15** [`20123e0b16`](https://github.com/sgl-project/sglang/commit/20123e0b16) [#25328](https://github.com/sgl-project/sglang/pull/25328)
  [diffusion] fix: mount Cache-DiT before torch.compile in native denoising (#25328)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`_
- **2026-05-15** [`eff736cc0f`](https://github.com/sgl-project/sglang/commit/eff736cc0f) [#25322](https://github.com/sgl-project/sglang/pull/25322)
  Deprecate /rerun-stage; scrub CUDA target_stage infra (#25322)
  _Files: `.github/workflows/_pr-awareness-comment.yml`, `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-sgl-kernel-build.yml`, `.github/workflows/_pr-test-stage.yml` _+6 more__
- **2026-05-15** [`4b6b434dfe`](https://github.com/sgl-project/sglang/commit/4b6b434dfe) [#25305](https://github.com/sgl-project/sglang/pull/25305)
  [diffusion] fix: fix Z-Image Cache-DiT sequence-parallel override (#25305)
  _Files: `python/sglang/multimodal_gen/runtime/models/dits/zimage.py`_
- **2026-05-15** [`6cfa4c9c2f`](https://github.com/sgl-project/sglang/commit/6cfa4c9c2f) [#24988](https://github.com/sgl-project/sglang/pull/24988)
  [diffusion] fix: respect dit_precision config instead of hardcoded bfloat16 in DenoisingStagge (#24988)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`_
- **2026-05-14** [`41eb2d861b`](https://github.com/sgl-project/sglang/commit/41eb2d861b) [#24185](https://github.com/sgl-project/sglang/pull/24185)
  [fix] load_audio: fall back to soundfile when torchcodec fails on WAV with trailing metadata (#24185)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-05-13** [`d8f7b78a29`](https://github.com/sgl-project/sglang/commit/d8f7b78a29) [#20930](https://github.com/sgl-project/sglang/pull/20930)
  [diffusion] fix: plumb max_sequence_length via diffusers_kwargs (#20930)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/base.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/flux.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/qwen_image.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/zimage.py` _+4 more__

## Other  (21 commits)

- **2026-05-20** [`a8c82c652e`](https://github.com/sgl-project/sglang/commit/a8c82c652e) [#25750](https://github.com/sgl-project/sglang/pull/25750)
  fix(dsv4): make pool configurator PP-aware (#25750)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-05-20** [`0c8049d9ba`](https://github.com/sgl-project/sglang/commit/0c8049d9ba) [#25826](https://github.com/sgl-project/sglang/pull/25826)
  Update CI permissions and CODEOWNERS (#25826)
  _Files: `.github/CI_PERMISSIONS.json`, `.github/CODEOWNERS`_
- **2026-05-19** [`5073c82a37`](https://github.com/sgl-project/sglang/commit/5073c82a37) [#23922](https://github.com/sgl-project/sglang/pull/23922)
  transformers v5 adapt HFRunner (#23922)
  _Files: `python/sglang/test/runners.py`_
- **2026-05-18** [`0ab427d0e1`](https://github.com/sgl-project/sglang/commit/0ab427d0e1) [#25293](https://github.com/sgl-project/sglang/pull/25293)
  [SMG] Add /v1/models fallback for model name discovery (#25293)
  _Files: `sgl-model-gateway/src/core/steps/worker/local/discover_metadata.rs`, `sgl-model-gateway/tests/common/mock_worker.rs`, `sgl-model-gateway/tests/routing/mod.rs`, `sgl-model-gateway/tests/routing/worker_discovery_test.rs`_
- **2026-05-16** [`4c6eb12dea`](https://github.com/sgl-project/sglang/commit/4c6eb12dea) [#25450](https://github.com/sgl-project/sglang/pull/25450)
  Fix invalid suite name in test_multi_detokenizer (#25450)
  _Files: `test/registered/tokenizer/test_multi_detokenizer.py`_
- **2026-05-16** [`688b679af2`](https://github.com/sgl-project/sglang/commit/688b679af2) [#25449](https://github.com/sgl-project/sglang/pull/25449)
  Convert discarded-value ternary to a plain if statement (#25449)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-16** [`d0c38329b2`](https://github.com/sgl-project/sglang/commit/d0c38329b2) [#25448](https://github.com/sgl-project/sglang/pull/25448)
  Inline the trivial _build_model_config wrapper (#25448)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-16** [`4190328767`](https://github.com/sgl-project/sglang/commit/4190328767) [#25447](https://github.com/sgl-project/sglang/pull/25447)
  Replace defensive getattr in pool_configurator with direct access (#25447)
  _Files: `python/sglang/srt/model_executor/pool_configurator.py`_
- **2026-05-16** [`7c716e73e0`](https://github.com/sgl-project/sglang/commit/7c716e73e0) [#25443](https://github.com/sgl-project/sglang/pull/25443)
  Add mechanical-refactor-verify skill from miles (#25443)
  _Files: `.claude/skills/mechanical-refactor-verify/SKILL.md`, `.claude/skills/mechanical-refactor-verify/mechanical_refactor_verify_utils.py`_
- **2026-05-16** [`21e420b4c2`](https://github.com/sgl-project/sglang/commit/21e420b4c2) [#25429](https://github.com/sgl-project/sglang/pull/25429)
  [Test] Set default temperature to 0.0 in kl_test_utils (#25429)
  _Files: `python/sglang/test/kl_test_utils.py`_
- **2026-05-16** [`0071033ff6`](https://github.com/sgl-project/sglang/commit/0071033ff6) [#25436](https://github.com/sgl-project/sglang/pull/25436)
  Cache _linear_attn_registry_cache with sentinel (#25436)
  _Files: `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-15** [`3f7e538b2f`](https://github.com/sgl-project/sglang/commit/3f7e538b2f) [#25399](https://github.com/sgl-project/sglang/pull/25399)
  Add NPU condition for cosine and sine caching (#25399)
  _Files: `python/sglang/srt/layers/rotary_embedding/rope_variant.py`_
- **2026-05-14** [`2279b79f35`](https://github.com/sgl-project/sglang/commit/2279b79f35) [#25050](https://github.com/sgl-project/sglang/pull/25050)
  Add --model-config-parser registry for pluggable config formats (#25050)
  _Files: `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/configs/model_config_parser_registry.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/hf_transformers/config.py` _+1 more__
- **2026-05-14** [`8b9ff4a68c`](https://github.com/sgl-project/sglang/commit/8b9ff4a68c) [#24375](https://github.com/sgl-project/sglang/pull/24375)
  [SMG] Expand K8s integration tests: cross-namespace, lifecycle, multi-model (#24375)
  _Files: `sgl-model-gateway/e2e_test/k8s_integration/manifests/gateway-cluster-scoped.yaml`, `sgl-model-gateway/e2e_test/k8s_integration/manifests/gateway-multimodel.yaml`, `sgl-model-gateway/e2e_test/k8s_integration/manifests/gateway-restart.yaml`, `sgl-model-gateway/e2e_test/k8s_integration/manifests/rbac-cluster-scoped.yaml` _+3 more__
- **2026-05-14** [`e8d57e7243`](https://github.com/sgl-project/sglang/commit/e8d57e7243) [#25184](https://github.com/sgl-project/sglang/pull/25184)
  [SMG] Fix cache-aware policy pool isolation in PD mode (#25184)
  _Files: `sgl-model-gateway/src/core/steps/worker/local/remove_from_policy_registry.rs`, `sgl-model-gateway/src/core/steps/worker/shared/update_policies.rs`, `sgl-model-gateway/src/policies/cache_aware.rs`, `sgl-model-gateway/src/policies/registry.rs`_
- **2026-05-14** [`e51bde1e9f`](https://github.com/sgl-project/sglang/commit/e51bde1e9f) [#25212](https://github.com/sgl-project/sglang/pull/25212)
  fix: prefix matching against matrix-expanded job names (#25212)
  _Files: `.github/actions/check-stage-health/action.yml`, `.github/actions/wait-for-jobs/action.yml`_
- **2026-05-14** [`af7511e0e8`](https://github.com/sgl-project/sglang/commit/af7511e0e8) [#24719](https://github.com/sgl-project/sglang/pull/24719)
  [sgl-model-gateway] Close PyO3 binding gaps and add regression tests (#24719)
  _Files: `sgl-model-gateway/bindings/python/src/lib.rs`, `sgl-model-gateway/bindings/python/src/sglang_router/router.py`, `sgl-model-gateway/bindings/python/src/sglang_router/router_args.py`, `sgl-model-gateway/bindings/python/tests/test_pyo3_binding.py`_
- **2026-05-14** [`dd98153d17`](https://github.com/sgl-project/sglang/commit/dd98153d17) [#25192](https://github.com/sgl-project/sglang/pull/25192)
  chore(ci_monitor): drop post_bisect_to_slack (#25192)
  _Files: `scripts/ci_monitor/ci_auto_bisect.py`, `scripts/ci_monitor/post_bisect_to_slack.py`_
- **2026-05-13** [`371cb2ade2`](https://github.com/sgl-project/sglang/commit/371cb2ade2) [#25026](https://github.com/sgl-project/sglang/pull/25026)
  [Bench] Add MEM profile activity to bench_serving (#25026)
  _Files: `python/sglang/bench_serving.py`_
- **2026-05-13** [`0a2615df24`](https://github.com/sgl-project/sglang/commit/0a2615df24) [#25182](https://github.com/sgl-project/sglang/pull/25182)
  chore: add vLLM SPDX copyright headers to ported files (#25182)
- **2026-05-13** [`1ae3218d03`](https://github.com/sgl-project/sglang/commit/1ae3218d03) [#25104](https://github.com/sgl-project/sglang/pull/25104)
  Add jasonjk-park and charlotte12l to CI_PERMISSIONS.json (#25104)
  _Files: `.codespellrc`, `.github/CI_PERMISSIONS.json`_

## KV Cache / Memory  (21 commits)

- **2026-05-19** [`c2a212bfe2`](https://github.com/sgl-project/sglang/commit/c2a212bfe2) [#25282](https://github.com/sgl-project/sglang/pull/25282)
  [UnifiedTree] Support DeepSeek V4 host pool with multiple layouts. (#25282)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `python/sglang/srt/mem_cache/memory_pool_host.py`, `python/sglang/test/kl_multiturn_utils.py`, `test/registered/radix_cache/test_unified_radix_cache_kl.py` _+1 more__
- **2026-05-18** [`b7267e8fce`](https://github.com/sgl-project/sglang/commit/b7267e8fce) [#25684](https://github.com/sgl-project/sglang/pull/25684)
  [CI] Enable weight prefetch for 8-gpu-h200 basic tests (#25684)
  _Files: `test/registered/8-gpu-models/test_minimax_m25_basic.py`, `test/registered/radix_cache/test_unified_radix_cache_kl_hicache.py`_
- **2026-05-18** [`3e3661fd2f`](https://github.com/sgl-project/sglang/commit/3e3661fd2f) [#25607](https://github.com/sgl-project/sglang/pull/25607)
  Move build_kv_cache to mem_cache.kv_cache_builder (#25607)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-05-18** [`fed1197474`](https://github.com/sgl-project/sglang/commit/fed1197474) [#25606](https://github.com/sgl-project/sglang/pull/25606)
  Reshape init_cache_with_memory_pool to match the future build_kv_cache signature (#25606)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-05-18** [`8692bdd3de`](https://github.com/sgl-project/sglang/commit/8692bdd3de) [#25604](https://github.com/sgl-project/sglang/pull/25604)
  Move maybe_register_hicache_draft to mem_cache.kv_cache_builder (#25604)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-05-18** [`062f6f7ae8`](https://github.com/sgl-project/sglang/commit/062f6f7ae8) [#25602](https://github.com/sgl-project/sglang/pull/25602)
  Move get_draft_kv_pool to mem_cache.kv_cache_builder (#25602)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/scheduler_components/__init__.py`, `python/sglang/srt/mem_cache/kv_cache_builder.py`_
- **2026-05-17** [`e547f3f804`](https://github.com/sgl-project/sglang/commit/e547f3f804) [#24585](https://github.com/sgl-project/sglang/pull/24585)
  fix(unified radix cache w/ hicache): backup ancestor nodes before leaf in write_back eviction (#24585)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-16** [`0c017db916`](https://github.com/sgl-project/sglang/commit/0c017db916) [#25497](https://github.com/sgl-project/sglang/pull/25497)
  Update kl_div_thres to 0.02 in swa_radix_cache (#25497)
  _Files: `test/registered/radix_cache/test_swa_radix_cache_kl.py`_
- **2026-05-16** [`0be539024f`](https://github.com/sgl-project/sglang/commit/0be539024f) [#25477](https://github.com/sgl-project/sglang/pull/25477)
  [BugFix]: Fix DeepSeek V4 HiCache layer count logic (#25477)
  _Files: `python/sglang/srt/mem_cache/hybrid_cache/hybrid_pool_assembler.py`, `test/registered/radix_cache/test_unified_radix_cache_kl_hicache.py`, `test/registered/radix_cache/test_unified_radix_cache_kl_hicache_nightly.py`_
- **2026-05-15** [`4df42da658`](https://github.com/sgl-project/sglang/commit/4df42da658) [#24096](https://github.com/sgl-project/sglang/pull/24096)
  Introduce CudaDeviceMixin and CudaSRTPlatform (#24096)
  _Files: `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/mem_cache/memory_pool.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/model_loader/loader.py` _+6 more__
- **2026-05-15** [`21b3ac52b4`](https://github.com/sgl-project/sglang/commit/21b3ac52b4) [#25277](https://github.com/sgl-project/sglang/pull/25277)
  [UnifiedTree]: Fix UnifiedRadixCache device match semantics with HiCache (#25277)
  _Files: `python/sglang/srt/mem_cache/unified_cache_components/full_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/mamba_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/swa_component.py`, `python/sglang/srt/mem_cache/unified_cache_components/tree_component.py` _+3 more__
- **2026-05-15** [`fe7a5dd3bf`](https://github.com/sgl-project/sglang/commit/fe7a5dd3bf) [#25348](https://github.com/sgl-project/sglang/pull/25348)
  [UnifiedTree]: Add nightly hicache ci for dsa model (#25348)
  _Files: `test/registered/radix_cache/test_unified_radix_hicache_kl.py`_
- **2026-05-15** [`66ef97c00f`](https://github.com/sgl-project/sglang/commit/66ef97c00f) [#25252](https://github.com/sgl-project/sglang/pull/25252)
  [Lint] Fix `Optional[X] = (None,)` typo defaults in two dataclasses (#25252)
  _Files: `python/sglang/lang/ir.py`, `python/sglang/srt/mem_cache/hicache_storage.py`_
- **2026-05-15** [`aaaad9e7c2`](https://github.com/sgl-project/sglang/commit/aaaad9e7c2) [#24358](https://github.com/sgl-project/sglang/pull/24358)
  [Codex] Diffusion tune Hunyuan3D shape export chunks (#24358)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/hunyuan3d.py`_
- **2026-05-15** [`d9fa84b25b`](https://github.com/sgl-project/sglang/commit/d9fa84b25b) [#24691](https://github.com/sgl-project/sglang/pull/24691)
  [UnifiedTree]: Support HiCache For DeepSeek_V4 (#24691)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `python/sglang/srt/mem_cache/hicache_storage.py`, `python/sglang/srt/mem_cache/hiradix_cache.py`, `python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py` _+7 more__
- **2026-05-14** [`e4378ff37f`](https://github.com/sgl-project/sglang/commit/e4378ff37f) [#25088](https://github.com/sgl-project/sglang/pull/25088)
  [UnifiedRadixCache] Fix HiCache load back start node (#25088)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/schedule_policy.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/chunk_cache.py` _+15 more__
- **2026-05-13** [`d6b28b4a69`](https://github.com/sgl-project/sglang/commit/d6b28b4a69) [#25161](https://github.com/sgl-project/sglang/pull/25161)
  [Refactor] Remove dead key_convert_fn / convert_to_bigram_key (#25161)
  _Files: `python/sglang/srt/mem_cache/swa_radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`, `python/sglang/srt/mem_cache/utils.py`_
- **2026-05-13** [`c32f2dc1ac`](https://github.com/sgl-project/sglang/commit/c32f2dc1ac) [#24671](https://github.com/sgl-project/sglang/pull/24671)
  fix(nixl): close file descriptors after each FILE transfer (#24671)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `python/sglang/srt/mem_cache/storage/nixl/test_hicache_nixl_storage.py`_
- **2026-05-13** [`245f7d8026`](https://github.com/sgl-project/sglang/commit/245f7d8026) [#24572](https://github.com/sgl-project/sglang/pull/24572)
  [AMD] Register 5 server-style 1-GPU tests for AMD PR CI (#24572)
  _Files: `test/registered/distributed/test_parallel_state.py`, `test/registered/input_embedding/test_input_embeds_chunked.py`, `test/registered/openai_server/basic/test_http2_server.py`, `test/registered/prefill_only/test_embed_overrides.py` _+1 more__
- **2026-05-13** [`5ed9a494d0`](https://github.com/sgl-project/sglang/commit/5ed9a494d0) [#24943](https://github.com/sgl-project/sglang/pull/24943)
  [UnifiedTree] fix: allow partial match on evicted+backuped nodes (#24943)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-13** [`6140e45ef3`](https://github.com/sgl-project/sglang/commit/6140e45ef3) [#25068](https://github.com/sgl-project/sglang/pull/25068)
  [UnifiedTree]: Fix the leaf determination logic in _cascade_evict. (#25068)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_

## CI / Build  (18 commits)

- **2026-05-19** [`3ef832f885`](https://github.com/sgl-project/sglang/commit/3ef832f885) [#25812](https://github.com/sgl-project/sglang/pull/25812)
  pr-states: dispatch from pr-test* notify job (fix rerun status) (#25812)
  _Files: `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-19** [`e0273dcd31`](https://github.com/sgl-project/sglang/commit/e0273dcd31) [#25732](https://github.com/sgl-project/sglang/pull/25732)
  pr-test-extra: re-trigger on labeled event (#25732)
  _Files: `.claude/skills/ci-workflow-guide/SKILL.md`, `.github/workflows/pr-test-extra.yml`, `docs_new/docs/developer_guide/contribution_guide.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_contribution_guide.mdx` _+1 more__
- **2026-05-18** [`c904fdd20e`](https://github.com/sgl-project/sglang/commit/c904fdd20e) [#25687](https://github.com/sgl-project/sglang/pull/25687)
  ci: pr-states match renamed "PR Test Base" workflow_run (#25687)
  _Files: `.github/workflows/pr-states.yml`_
- **2026-05-18** [`79b6749669`](https://github.com/sgl-project/sglang/commit/79b6749669) [#25586](https://github.com/sgl-project/sglang/pull/25586)
  ci: pr-states no longer overwrites running run state when label is removed (#25586)
  _Files: `.github/workflows/pr-states.yml`_
- **2026-05-16** [`90d3d42ac1`](https://github.com/sgl-project/sglang/commit/90d3d42ac1) [#25475](https://github.com/sgl-project/sglang/pull/25475)
  pr-states: workflow_dispatch refresh on slash cmds (#25475)
  _Files: `.github/workflows/pr-states.yml`_
- **2026-05-16** [`af26b71ae8`](https://github.com/sgl-project/sglang/commit/af26b71ae8) [#25468](https://github.com/sgl-project/sglang/pull/25468)
  [Misc] Update release branch cut script (#25468)
  _Files: `.github/workflows/release-branch-cut.yml`_
- **2026-05-16** [`b674007026`](https://github.com/sgl-project/sglang/commit/b674007026) [#25452](https://github.com/sgl-project/sglang/pull/25452)
  [CI] Show distinct run-name per event in pr-test workflow (#25452)
  _Files: `.github/workflows/pr-test.yml`_
- **2026-05-16** [`b7d62bd724`](https://github.com/sgl-project/sglang/commit/b7d62bd724) [#25420](https://github.com/sgl-project/sglang/pull/25420)
  [CI] Rename basic CI `stage-a/b/c` -> `base-a/b/c` for symmetry with extra CI (#25420)
- **2026-05-15** [`293027aafa`](https://github.com/sgl-project/sglang/commit/293027aafa) [#25392](https://github.com/sgl-project/sglang/pull/25392)
  pr-states: fix fork-PR token + add run-ci label awareness (#25392)
  _Files: `.github/workflows/pr-states.yml`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-05-15** [`3117415c9b`](https://github.com/sgl-project/sglang/commit/3117415c9b) [#25387](https://github.com/sgl-project/sglang/pull/25387)
  ci: standalone PR awareness workflow (decouple from pr-test reusable chain) (#25387)
  _Files: `.github/workflows/_pr-awareness-comment.yml`, `.github/workflows/pr-states.yml`, `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-15** [`4adfc6cf7e`](https://github.com/sgl-project/sglang/commit/4adfc6cf7e) [#25320](https://github.com/sgl-project/sglang/pull/25320)
  ci: dispatch pr-test-extra.yml from pr-test.yml on the scheduled cron (#25320)
  _Files: `.github/workflows/_pr-awareness-comment.yml`, `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test-extra.yml` _+1 more__
- **2026-05-14** [`50f405816e`](https://github.com/sgl-project/sglang/commit/50f405816e) [#25234](https://github.com/sgl-project/sglang/pull/25234)
  ci: add Jialin to CI permissions (custom override) (#25234)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-05-14** [`d311f311bc`](https://github.com/sgl-project/sglang/commit/d311f311bc) [#25255](https://github.com/sgl-project/sglang/pull/25255)
  ci: read est_time from sglang-ci-stats instead of scraping CI logs (#25255)
  _Files: `.github/workflows/weekly-update-est-time.yml`, `scripts/ci/update_est_time.py`_
- **2026-05-14** [`5c11c2492f`](https://github.com/sgl-project/sglang/commit/5c11c2492f) [#25232](https://github.com/sgl-project/sglang/pull/25232)
  ci: emit machine-readable TIMINGS block at end of run_unittest_files (#25232)
  _Files: `python/sglang/test/ci/ci_utils.py`_
- **2026-05-14** [`f7efff321d`](https://github.com/sgl-project/sglang/commit/f7efff321d) [#25215](https://github.com/sgl-project/sglang/pull/25215)
  [Docker] Fix several dependencies in Dockerfile (#25215)
  _Files: `docker/Dockerfile`_
- **2026-05-13** [`9a32a0272f`](https://github.com/sgl-project/sglang/commit/9a32a0272f) [#25193](https://github.com/sgl-project/sglang/pull/25193)
  ci: compute matrix partition counts from `est_time` (#25193)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test.yml`, `scripts/ci/utils/compute_partitions.py`_
- **2026-05-13** [`b1db9f71ee`](https://github.com/sgl-project/sglang/commit/b1db9f71ee) [#25188](https://github.com/sgl-project/sglang/pull/25188)
  [SMG] Fix matrix-sibling concurrency collision in PR Test (SMG) (#25188)
  _Files: `.github/workflows/pr-test-rust.yml`_
- **2026-05-13** [`938198e91c`](https://github.com/sgl-project/sglang/commit/938198e91c) [#25132](https://github.com/sgl-project/sglang/pull/25132)
  ci: extract check-changes into reusable workflow (#25132)
  _Files: `.github/workflows/_pr-test-check-changes.yml`, `.github/workflows/pr-test.yml`_

## Quantization  (15 commits)

- **2026-05-20** [`80fc524809`](https://github.com/sgl-project/sglang/commit/80fc524809) [#25483](https://github.com/sgl-project/sglang/pull/25483)
  [diffusion] quant: update Wan2.2 modelOpt CI checkpoints (#25483)
  _Files: `docs_new/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py` _+5 more__
- **2026-05-19** [`fab097d66d`](https://github.com/sgl-project/sglang/commit/fab097d66d) [#25286](https://github.com/sgl-project/sglang/pull/25286)
  [Gemma4]: Fix FP8 Triton scale layout (#25286)
  _Files: `python/sglang/srt/layers/quantization/fp8_kernel.py`, `test/registered/quant/test_triton_scaled_mm.py`_
- **2026-05-19** [`0e4d1b49d3`](https://github.com/sgl-project/sglang/commit/0e4d1b49d3) [#25764](https://github.com/sgl-project/sglang/pull/25764)
  [Codex] Remove stale DeepSeek V4 JIT kernels (#25764)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/rmsnorm.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/silu_and_mul_masked_post_quant_tmp.cuh`, `python/sglang/jit_kernel/deepseek_v4.py`_
- **2026-05-19** [`79ea30d1f1`](https://github.com/sgl-project/sglang/commit/79ea30d1f1) [#25733](https://github.com/sgl-project/sglang/pull/25733)
  [Bug] Fix V4-Pro NaN on Blackwell by converting fp8_einsum input scale to ue8m0 (#25733)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-19** [`7c3f614e23`](https://github.com/sgl-project/sglang/commit/7c3f614e23) [#25740](https://github.com/sgl-project/sglang/pull/25740)
  [AMD] Bump amd/Kimi-K2.5-MXFP4 revision to align with shared-experts fusion (#25740)
  _Files: `test/registered/amd/test_kimi_k25_mxfp4.py`_
- **2026-05-19** [`4c9f31b85e`](https://github.com/sgl-project/sglang/commit/4c9f31b85e) [#22338](https://github.com/sgl-project/sglang/pull/22338)
  :sparkles: [diffusion][npu][quant] Add MXFP4 quantization support for Wan2.2 Diffusion on Ascend NPU (#22338)
  _Files: `python/sglang/multimodal_gen/runtime/layers/quantization/__init__.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelslim.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelslim_mxfp4_scheme.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/mxfp4_npu.py` _+3 more__
- **2026-05-18** [`abe2ec2aff`](https://github.com/sgl-project/sglang/commit/abe2ec2aff) [#25390](https://github.com/sgl-project/sglang/pull/25390)
  [AMD] Enable shared-experts fusion with new KIMI-K2.5-MXFP4 model. (#25390)
  _Files: `python/sglang/srt/layers/quantization/quark/quark.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-16** [`2fc217df4d`](https://github.com/sgl-project/sglang/commit/2fc217df4d) [#24599](https://github.com/sgl-project/sglang/pull/24599)
  [codex] Split diffusion quant CI coverage (#24599)
  _Files: `python/sglang/multimodal_gen/test/server/gpu_cases.py`, `python/sglang/multimodal_gen/test/server/test_server_b200.py`, `python/sglang/multimodal_gen/test/server/testcase_configs.py`, `scripts/ci/utils/diffusion/diffusion_case_parser.py`_
- **2026-05-16** [`a741d0cc56`](https://github.com/sgl-project/sglang/commit/a741d0cc56) [#25453](https://github.com/sgl-project/sglang/pull/25453)
  [CI] Lower mem-fraction-static for GLM-5.1 FP8 8-GPU test to 0.85 (#25453)
  _Files: `test/registered/8-gpu-models/test_glm_51_fp8.py`_
- **2026-05-14** [`88d3ed7df1`](https://github.com/sgl-project/sglang/commit/88d3ed7df1) [#25181](https://github.com/sgl-project/sglang/pull/25181)
  Enable SGLANG_OPT_FP8_WO_A_GEMM by default (#25181)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/server_args.py`_
- **2026-05-14** [`3fc60e5748`](https://github.com/sgl-project/sglang/commit/3fc60e5748) [#25221](https://github.com/sgl-project/sglang/pull/25221)
  [MLX] bench_one_batch: thread --quantization through to MlxModelRunner (#25221)
  _Files: `python/sglang/bench_one_batch.py`_
- **2026-05-14** [`90afd680f3`](https://github.com/sgl-project/sglang/commit/90afd680f3) [#25191](https://github.com/sgl-project/sglang/pull/25191)
  [Apple Silicon] [MLX] Auto-detect MLX-format quantization_config dict (#25191)
  _Files: `python/sglang/srt/layers/quantization/mlx.py`, `test/registered/unit/hardware_backend/mlx/test_quantization.py`_
- **2026-05-13** [`6c0633b0b1`](https://github.com/sgl-project/sglang/commit/6c0633b0b1) [#25190](https://github.com/sgl-project/sglang/pull/25190)
  fix(nvfp4): make process_weights_after_loading hot-reload-safe via alias-when-same-shape (#25190)
  _Files: `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/layers/utils/common.py`_
- **2026-05-13** [`6ac30192fa`](https://github.com/sgl-project/sglang/commit/6ac30192fa) [#24907](https://github.com/sgl-project/sglang/pull/24907)
  [MLX] Add on-the-fly --quantization mlx_q4 / mlx_q8 for Apple Silicon (#24907)
  _Files: `docs_new/docs/hardware-platforms/apple_metal.mdx`, `python/sglang/srt/hardware_backend/mlx/model_runner.py`, `python/sglang/srt/hardware_backend/mlx/tp_worker.py`, `python/sglang/srt/layers/quantization/__init__.py` _+3 more__
- **2026-05-13** [`d0913fca8d`](https://github.com/sgl-project/sglang/commit/d0913fca8d) [#24897](https://github.com/sgl-project/sglang/pull/24897)
  Port fused SiLU+clamp+FP8 quant from DSV4 dev branch (#24897)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_

## Triton / Kernels  (12 commits)

- **2026-05-19** [`cd012ada58`](https://github.com/sgl-project/sglang/commit/cd012ada58) [#25756](https://github.com/sgl-project/sglang/pull/25756)
  [Fix] Fix extra uninstall of cutlass packages (#25756)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-05-19** [`fbfddfd5c7`](https://github.com/sgl-project/sglang/commit/fbfddfd5c7) [#25695](https://github.com/sgl-project/sglang/pull/25695)
  fix (jit kernel): elementwise activation C++ error (#25695)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/activation.cuh`_
- **2026-05-19** [`2424303dfb`](https://github.com/sgl-project/sglang/commit/2424303dfb) [#24710](https://github.com/sgl-project/sglang/pull/24710)
  [codex] Optimize hidden-size 512 RMSNorm dispatch (#24710)
  _Files: `python/sglang/jit_kernel/csrc/elementwise/rmsnorm.cuh`, `python/sglang/jit_kernel/norm.py`, `python/sglang/jit_kernel/tests/test_rmsnorm.py`_
- **2026-05-19** [`dbac464726`](https://github.com/sgl-project/sglang/commit/dbac464726) [#25303](https://github.com/sgl-project/sglang/pull/25303)
  [Spec]: Make Triton standalone spec test deterministic (#25303)
  _Files: `python/sglang/test/server_fixtures/standalone_fixture.py`, `test/registered/spec/test_spec_standalone_extra.py`_
- **2026-05-18** [`b79e4b1e68`](https://github.com/sgl-project/sglang/commit/b79e4b1e68) [#25690](https://github.com/sgl-project/sglang/pull/25690)
  [Fix] Try to fix error caused by latest cutedsl packages  (#25690)
  _Files: `python/pyproject.toml`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-05-14** [`142ed710b7`](https://github.com/sgl-project/sglang/commit/142ed710b7) [#25248](https://github.com/sgl-project/sglang/pull/25248)
  [CI] Support new-style `register_cuda_ci(stage=, runner_config=)` in slash handler + est-time updater (#25248)
  _Files: `scripts/ci/update_est_time.py`, `scripts/ci/utils/slash_command_handler.py`_
- **2026-05-14** [`85d9c77c57`](https://github.com/sgl-project/sglang/commit/85d9c77c57) [#25138](https://github.com/sgl-project/sglang/pull/25138)
  ci: extract cuda stage actions + runner_config mapping (#25138)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test.yml`, `scripts/ci/runner_configs.py`, `scripts/ci/runner_configs.yml`_
- **2026-05-14** [`b71d74673c`](https://github.com/sgl-project/sglang/commit/b71d74673c) [#24253](https://github.com/sgl-project/sglang/pull/24253)
  ci: combine H200 8-GPU warmup steps and surface server log on every path (#24253)
  _Files: `.github/workflows/pr-test.yml`, `scripts/ci/cuda/warmup_deep_gemm.py`, `scripts/ci/cuda/warmup_server.py`_
- **2026-05-14** [`992fc0d6fe`](https://github.com/sgl-project/sglang/commit/992fc0d6fe) [#25206](https://github.com/sgl-project/sglang/pull/25206)
  ci(sgl-kernel-build): actually reclaim disk in the wheel-build cleanup step (#25206)
  _Files: `.github/workflows/_pr-test-sgl-kernel-build.yml`_
- **2026-05-14** [`22d3f3996c`](https://github.com/sgl-project/sglang/commit/22d3f3996c) [#25197](https://github.com/sgl-project/sglang/pull/25197)
  ci: decouple stage and runner for cuda registry (#25197)
- **2026-05-13** [`4d91a4f3a1`](https://github.com/sgl-project/sglang/commit/4d91a4f3a1) [#25135](https://github.com/sgl-project/sglang/pull/25135)
  ci: merge sgl-kernel-build-wheels x86+arm into reusable workflow (#25135)
  _Files: `.github/workflows/_pr-test-sgl-kernel-build.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-13** [`72b49bfac6`](https://github.com/sgl-project/sglang/commit/72b49bfac6) [#25113](https://github.com/sgl-project/sglang/pull/25113)
  docker, ci: swap GB DeepEP source from fzyzcjy fork to deepseek-ai/DeepEP@hybrid-ep (#25113)
  _Files: `docker/Dockerfile`, `scripts/ci/cuda/ci_install_deepep.sh`_

## Tensor / Data Parallel  (12 commits)

- **2026-05-19** [`4c0ce0345d`](https://github.com/sgl-project/sglang/commit/4c0ce0345d) [#25284](https://github.com/sgl-project/sglang/pull/25284)
  Support Gemma4 Pipeline Parallelism (#25284)
  _Files: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mm.py`, `python/sglang/srt/server_args.py`, `python/sglang/test/test_utils.py` _+1 more__
- **2026-05-19** [`aad00b0ed8`](https://github.com/sgl-project/sglang/commit/aad00b0ed8) [#25451](https://github.com/sgl-project/sglang/pull/25451)
  Upgrade transformers to 5.8.1 (#25451)
  _Files: `3rdparty/amd/wheel/sglang/pyproject.toml`, `python/pyproject.toml`, `python/pyproject_cpu.toml`, `python/pyproject_npu.toml` _+2 more__
- **2026-05-18** [`314dedf7c6`](https://github.com/sgl-project/sglang/commit/314dedf7c6) [#25686](https://github.com/sgl-project/sglang/pull/25686)
  Use SGLANG_CACHE_DIR env for gpu_p2p_access_cache path (#25686)
  _Files: `python/sglang/srt/distributed/device_communicators/custom_all_reduce_utils.py`_
- **2026-05-18** [`86c6c77f2f`](https://github.com/sgl-project/sglang/commit/86c6c77f2f) [#25585](https://github.com/sgl-project/sglang/pull/25585)
  [Bugfix] Fix missing group arg in get dp buffer (#25585)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-18** [`3e2a109636`](https://github.com/sgl-project/sglang/commit/3e2a109636) [#25401](https://github.com/sgl-project/sglang/pull/25401)
  Add output_gate_type to Qwen3NextConfig and update models to utilize it (#25401)
  _Files: `python/sglang/srt/configs/qwen3_next.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`_
- **2026-05-18** [`e5589843a3`](https://github.com/sgl-project/sglang/commit/e5589843a3) [#19524](https://github.com/sgl-project/sglang/pull/19524)
  feature: upstream cancel (#19524)
  _Files: `.pre-commit-config.yaml`, `sgl-model-gateway/Cargo.toml`, `sgl-model-gateway/benches/streaming_utils_bench.rs`, `sgl-model-gateway/src/core/mod.rs` _+9 more__
- **2026-05-17** [`6dcacb1159`](https://github.com/sgl-project/sglang/commit/6dcacb1159) [#25506](https://github.com/sgl-project/sglang/pull/25506)
  [Doc] Fix several places for dpsk v4 cookbook (#25506)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-16** [`48f85d464f`](https://github.com/sgl-project/sglang/commit/48f85d464f) [#25446](https://github.com/sgl-project/sglang/pull/25446)
  Fix V2 trace filename collisions when DP/PP/EP enabled (#25446)
  _Files: `python/sglang/srt/utils/profile_utils.py`_
- **2026-05-15** [`494ee71189`](https://github.com/sgl-project/sglang/commit/494ee71189) [#25318](https://github.com/sgl-project/sglang/pull/25318)
  split test_dsa_models_mtp into 4 files (#25318)
  _Files: `python/sglang/test/kits/eval_accuracy_kit.py`, `python/sglang/test/kits/spec_decoding_kit.py`, `python/sglang/test/server_fixtures/dsa_mtp_fixture.py`, `test/registered/8-gpu-models/test_dsa_models_mtp.py` _+4 more__
- **2026-05-14** [`2417a9da57`](https://github.com/sgl-project/sglang/commit/2417a9da57) [#25238](https://github.com/sgl-project/sglang/pull/25238)
  [CI] Bundle `check-changes` outputs + caller inputs into 2 JSON inputs (#25238)
  _Files: `.github/workflows/_pr-test-stage.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-14** [`856f13a916`](https://github.com/sgl-project/sglang/commit/856f13a916) [#25211](https://github.com/sgl-project/sglang/pull/25211)
  chore(codeowners): add kpham-sgl to frozen_kv_mtp files (#25211)
  _Files: `.github/CODEOWNERS`_
- **2026-05-13** [`10a005e4ea`](https://github.com/sgl-project/sglang/commit/10a005e4ea) [#24801](https://github.com/sgl-project/sglang/pull/24801)
  [CI][NPU] use internal HTTP cache for Rust toolchain via RUSTUP_CACHE (#24801)
  _Files: `.github/workflows/pr-test-npu.yml`, `scripts/ci/utils/install_rustup.sh`_

## Speculative Decoding  (11 commits)

- **2026-05-19** [`b45b52ee8f`](https://github.com/sgl-project/sglang/commit/b45b52ee8f) [#25689](https://github.com/sgl-project/sglang/pull/25689)
  Add spec_verify_calls_total metric for speculative decoding (#25689)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/observability/metrics_collector.py`_
- **2026-05-18** [`9e3bb9a307`](https://github.com/sgl-project/sglang/commit/9e3bb9a307) [#25566](https://github.com/sgl-project/sglang/pull/25566)
  [Spec] fold can_run_cuda_graph into EagleVerifyOutput; drop dead extend-after-decode check (#25566)
  _Files: `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/frozen_kv_mtp_worker.py` _+5 more__
- **2026-05-18** [`f5049709b3`](https://github.com/sgl-project/sglang/commit/f5049709b3) [#25454](https://github.com/sgl-project/sglang/pull/25454)
  fix(eagle3): drop +1 offset on aux layer ids when first id != 1 (#25454)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-18** [`189e0a4240`](https://github.com/sgl-project/sglang/commit/189e0a4240) [#25603](https://github.com/sgl-project/sglang/pull/25603)
  Decouple _maybe_register_hicache_draft from self (#25603)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-18** [`d1c04deba7`](https://github.com/sgl-project/sglang/commit/d1c04deba7) [#25601](https://github.com/sgl-project/sglang/pull/25601)
  Decouple _get_draft_kv_pool from self before extraction (#25601)
  _Files: `python/sglang/srt/managers/scheduler.py`_
- **2026-05-17** [`52875ab6f4`](https://github.com/sgl-project/sglang/commit/52875ab6f4) [#25260](https://github.com/sgl-project/sglang/pull/25260)
  [AMD][CI] Register Eagle constrained decoding test (#25260)
  _Files: `test/registered/spec/eagle/test_eagle_constrained_decoding.py`_
- **2026-05-16** [`daade9cc00`](https://github.com/sgl-project/sglang/commit/daade9cc00) [#25428](https://github.com/sgl-project/sglang/pull/25428)
  [Fix] Probe speculative draft config via sglang get_config (#25428)
  _Files: `python/sglang/srt/server_args.py`_
- **2026-05-15** [`3c2956d880`](https://github.com/sgl-project/sglang/commit/3c2956d880) [#24999](https://github.com/sgl-project/sglang/pull/24999)
  Add extension points on SpeculativeAlgorithm for custom spec v2 (#24999)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/cpu_graph_runner.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py` _+1 more__
- **2026-05-14** [`78408d2300`](https://github.com/sgl-project/sglang/commit/78408d2300) [#25204](https://github.com/sgl-project/sglang/pull/25204)
  Fix frozen kv MTP crash when bonus_tokens is None (#25204)
  _Files: `python/sglang/srt/speculative/frozen_kv_mtp_utils.py`_
- **2026-05-13** [`f9ff5fc154`](https://github.com/sgl-project/sglang/commit/f9ff5fc154) [#24858](https://github.com/sgl-project/sglang/pull/24858)
  multi_layer_eagle: add tracing hooks (#24858)
  _Files: `python/sglang/srt/speculative/multi_layer_eagle_worker.py`_
- **2026-05-13** [`adae4042a7`](https://github.com/sgl-project/sglang/commit/adae4042a7) [#25109](https://github.com/sgl-project/sglang/pull/25109)
  spec: defer verify() idle hidden_size to worker fixup (#25109)
  _Files: `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_worker.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker.py`_

## Docs / Examples  (11 commits)

- **2026-05-19** [`d028697d17`](https://github.com/sgl-project/sglang/commit/d028697d17) [#25269](https://github.com/sgl-project/sglang/pull/25269)
  [NPU][Docs] Add Kimi-K2.5-W4A8 instance doc on NPU (#25269)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_kimi_k2.5_examples.mdx`_
- **2026-05-16** [`435ea41cf0`](https://github.com/sgl-project/sglang/commit/435ea41cf0) [#24723](https://github.com/sgl-project/sglang/pull/24723)
  Delegate ModelExpress loading to package (#24723)
  _Files: `docs_new/docs/advanced_features/rfork.mdx`, `docs_new/docs/advanced_features/server_arguments.mdx`, `python/sglang/srt/configs/load_config.py`, `python/sglang/srt/model_executor/model_runner.py` _+3 more__
- **2026-05-15** [`33f1d3915f`](https://github.com/sgl-project/sglang/commit/33f1d3915f) [#25370](https://github.com/sgl-project/sglang/pull/25370)
  [NEW MODEL] Add H200 validation for Ring-2.6-1T cookbook (#25370)
  _Files: `docs_new/cookbook/autoregressive/InclusionAI/Ring-2.6-1T.mdx`, `docs_new/src/snippets/autoregressive/ring-26-1t-deployment.jsx`_
- **2026-05-15** [`c3daa77e9a`](https://github.com/sgl-project/sglang/commit/c3daa77e9a) [#25360](https://github.com/sgl-project/sglang/pull/25360)
  [NEW MODEL] Add Ring-2.6-1T cookbook (#25360)
  _Files: `docs_new/cookbook/autoregressive/InclusionAI/Ring-2.6-1T.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/autoregressive/ring-26-1t-deployment.jsx`_
- **2026-05-14** [`626fd61308`](https://github.com/sgl-project/sglang/commit/626fd61308) [#24935](https://github.com/sgl-project/sglang/pull/24935)
  :memo: docs: add canonical URL to fix Google indexing lmsysorg.mintlify.app instead of docs.sglang.io (#24935)
  _Files: `docs_new/docs.json`_
- **2026-05-14** [`edb1b3f8f5`](https://github.com/sgl-project/sglang/commit/edb1b3f8f5) [#24777](https://github.com/sgl-project/sglang/pull/24777)
  [NPU] add Ascend NPU Accuracy Evaluation and Faq docs (#24777)
  _Files: `.codespellrc`, `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx`_
- **2026-05-14** [`65e9f81c7d`](https://github.com/sgl-project/sglang/commit/65e9f81c7d) [#25114](https://github.com/sgl-project/sglang/pull/25114)
  [NPU] [DOC] add performance testing and optimization docs for npu (#25114)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_optimization.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_performance_testing.mdx`_
- **2026-05-13** [`f2a90094c9`](https://github.com/sgl-project/sglang/commit/f2a90094c9) [#25143](https://github.com/sgl-project/sglang/pull/25143)
  bench: fix wrong flag names in bench_one_batch{,_server} docstrings (#25143)
  _Files: `python/sglang/bench_one_batch.py`, `python/sglang/bench_one_batch_server.py`_
- **2026-05-13** [`b0018ad015`](https://github.com/sgl-project/sglang/commit/b0018ad015) [#25134](https://github.com/sgl-project/sglang/pull/25134)
  [Doc]: refactor Intern-S2-Preview cookbook with interactive command generator (#25134)
  _Files: `docs_new/cookbook/autoregressive/InternLM/Intern-S2-Preview.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json`, `docs_new/src/snippets/autoregressive/intern-s2-preview-deployment.jsx`_
- **2026-05-13** [`3f048c80b8`](https://github.com/sgl-project/sglang/commit/3f048c80b8) [#24874](https://github.com/sgl-project/sglang/pull/24874)
  Reject repetition_penalty=0 in SamplingParams.verify() (#24874)
  _Files: `docs/basic_usage/sampling_params.md`, `python/sglang/srt/sampling/sampling_params.py`, `test/registered/unit/sampling/test_sampling_params.py`_
- **2026-05-13** [`622baa17bd`](https://github.com/sgl-project/sglang/commit/622baa17bd) [#25115](https://github.com/sgl-project/sglang/pull/25115)
  [Doc]: add interns2preview in cookbook (#25115)
  _Files: `docs_new/cookbook/autoregressive/InternLM/Intern-S2-Preview.mdx`, `docs_new/cookbook/autoregressive/intro.mdx`, `docs_new/docs.json`_

## Models  (10 commits)

- **2026-05-19** [`8322fe09a7`](https://github.com/sgl-project/sglang/commit/8322fe09a7) [#25729](https://github.com/sgl-project/sglang/pull/25729)
  fix(dsv4): upgrade forward metadata on main stream for large PP size (#25729)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-19** [`de3fc46e3d`](https://github.com/sgl-project/sglang/commit/de3fc46e3d) [#25778](https://github.com/sgl-project/sglang/pull/25778)
  [NPU] [DOC] remove Qwen3-235B-A22B 2K+2K 100ms mixed mode benchmark (#25778)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`_
- **2026-05-19** [`7e0818038a`](https://github.com/sgl-project/sglang/commit/7e0818038a) [#25396](https://github.com/sgl-project/sglang/pull/25396)
  fix: fix deepseek v4 CP  error (#25396)
  _Files: `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-19** [`1f7bf155c3`](https://github.com/sgl-project/sglang/commit/1f7bf155c3) [#25735](https://github.com/sgl-project/sglang/pull/25735)
  [NPU] [DOCS] Improved the usability of Ascend NPU documents (#25735)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_accuracy_evaluation.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_deepseek_example.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_faq.mdx` _+4 more__
- **2026-05-15** [`17c8a2fa53`](https://github.com/sgl-project/sglang/commit/17c8a2fa53) [#25089](https://github.com/sgl-project/sglang/pull/25089)
  [Llama4] Use strided in-place fused QK RMSNorm to drop a redundant copy (#25089)
  _Files: `python/sglang/srt/models/llama4.py`_
- **2026-05-15** [`eec5ba26cf`](https://github.com/sgl-project/sglang/commit/eec5ba26cf) [#25080](https://github.com/sgl-project/sglang/pull/25080)
  Fix incorrect import in test case (#25080)
  _Files: `test/registered/ascend/llm_models/test_npu_qwen3_30b_attn_cp.py`_
- **2026-05-15** [`c7e879e43f`](https://github.com/sgl-project/sglang/commit/c7e879e43f) [#25369](https://github.com/sgl-project/sglang/pull/25369)
  Add hicache feature in dsv4 cookbook (#25369)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-14** [`373a22c225`](https://github.com/sgl-project/sglang/commit/373a22c225) [#25268](https://github.com/sgl-project/sglang/pull/25268)
  [NPU] [DOC] fix issues in ascend npu docs (#25268)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_environment_variables.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quick_start.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_qwen3_5_examples.mdx` _+1 more__
- **2026-05-14** [`1f119f6a44`](https://github.com/sgl-project/sglang/commit/1f119f6a44) [#25243](https://github.com/sgl-project/sglang/pull/25243)
  [Docs] update dsv4 cookbook with H100 deployment commands (#25243)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-13** [`9d0be860a4`](https://github.com/sgl-project/sglang/commit/9d0be860a4) [#21537](https://github.com/sgl-project/sglang/pull/21537)
  [NPU] recover accuracy for gemma3-4b-it from 54% to 72% (reduced by transformer5.3) (#21537)
  _Files: `python/sglang/srt/models/gemma3_causal.py`_

## ROCm / AMD  (8 commits)

- **2026-05-18** [`54eb2904a4`](https://github.com/sgl-project/sglang/commit/54eb2904a4) [#25178](https://github.com/sgl-project/sglang/pull/25178)
  minor: docs include mac installation (#25178)
  _Files: `docs_new/docs/get-started/install.mdx`, `docs_new/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-05-18** [`7adb37bb52`](https://github.com/sgl-project/sglang/commit/7adb37bb52) [#25301](https://github.com/sgl-project/sglang/pull/25301)
  [AMD] fix moriep unittest oom on mi300x ci (#25301)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_moriep_small.py`_
- **2026-05-17** [`4ef9bad223`](https://github.com/sgl-project/sglang/commit/4ef9bad223) [#25208](https://github.com/sgl-project/sglang/pull/25208)
  [AMD] ci: register 5 framework tests to run on AMD CI (#25208)
  _Files: `test/registered/core/test_engine_child_pids.py`, `test/registered/observability/test_tracing.py`, `test/registered/prefill_only/test_pooled_hidden_states.py`, `test/registered/sessions/test_session_control.py` _+1 more__
- **2026-05-15** [`9dad37f254`](https://github.com/sgl-project/sglang/commit/9dad37f254) [#25112](https://github.com/sgl-project/sglang/pull/25112)
  [AMD] Bump --timeout-per-file 1800->2400 for stage-b-test-1-gpu-small-amd (#25112)
  _Files: `.github/workflows/pr-test-amd.yml`_
- **2026-05-15** [`0fde61535f`](https://github.com/sgl-project/sglang/commit/0fde61535f) [#25326](https://github.com/sgl-project/sglang/pull/25326)
  chore: bump sgl-kernel version to 0.4.2.post2 (#25326)
  _Files: `.github/workflows/_pr-test-sgl-kernel-build.yml`, `sgl-kernel/CMakeLists.txt`, `sgl-kernel/pyproject.toml`, `sgl-kernel/pyproject_cpu.toml` _+3 more__
- **2026-05-14** [`bc265c5f82`](https://github.com/sgl-project/sglang/commit/bc265c5f82) [#25210](https://github.com/sgl-project/sglang/pull/25210)
  [AMD] Add amd jit resolve token ids bench ci (#25210)
  _Files: `python/sglang/jit_kernel/benchmark/bench_resolve_future_token_ids.py`_
- **2026-05-14** [`7b128e143a`](https://github.com/sgl-project/sglang/commit/7b128e143a) [#25209](https://github.com/sgl-project/sglang/pull/25209)
  [AMD] Add amd jit clamp position bench ci (#25209)
  _Files: `python/sglang/jit_kernel/benchmark/bench_clamp_position.py`_
- **2026-05-13** [`cf92ccbf18`](https://github.com/sgl-project/sglang/commit/cf92ccbf18) [#24987](https://github.com/sgl-project/sglang/pull/24987)
  [AMD] Run jit kernel PR test through run_suite.py register mechanism (#24987)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `python/sglang/jit_kernel/tests/test_store_cache.py`, `test/run_suite.py`_

## Serving / API  (3 commits)

- **2026-05-19** [`1d19721394`](https://github.com/sgl-project/sglang/commit/1d19721394) [#23506](https://github.com/sgl-project/sglang/pull/23506)
  [gRPC] Native server: Rust crate (1/N) (#23506)
  _Files: `rust/sglang-grpc/Cargo.toml`, `rust/sglang-grpc/src/bridge.rs`, `rust/sglang-grpc/src/bridge/tests.rs`, `rust/sglang-grpc/src/lib.rs` _+7 more__
- **2026-05-14** [`c016246b0f`](https://github.com/sgl-project/sglang/commit/c016246b0f) [#25046](https://github.com/sgl-project/sglang/pull/25046)
  [Rerank] Early-exit logprob scan and hoist math import (#25046)
  _Files: `python/sglang/srt/entrypoints/openai/serving_rerank.py`_
- **2026-05-14** [`5fb6bde6c0`](https://github.com/sgl-project/sglang/commit/5fb6bde6c0) [#25163](https://github.com/sgl-project/sglang/pull/25163)
  Add sglang:get_loads_duration_seconds metric (#25163)
  _Files: `python/sglang/srt/entrypoints/v1_loads.py`, `python/sglang/srt/observability/metrics_collector.py`, `test/registered/language/test_srt_backend.py`_

## LoRA  (1 commits)

- **2026-05-16** [`c8e5cf5768`](https://github.com/sgl-project/sglang/commit/c8e5cf5768) [#25440](https://github.com/sgl-project/sglang/pull/25440)
  Fix LoRA pool not appearing in /v1/loads (#25440)
  _Files: `python/sglang/srt/observability/scheduler_metrics_mixin.py`_

## Structured Output  (1 commits)

- **2026-05-15** [`7cb4669a04`](https://github.com/sgl-project/sglang/commit/7cb4669a04) [#25233](https://github.com/sgl-project/sglang/pull/25233)
  [Fix] DeepSeek-V3.2: build structural tag locally to encode both wrapper and invoke layers (#25233)
  _Files: `python/sglang/srt/function_call/deepseekv32_detector.py`_

---
_Generated 2026-05-20 04:13 UTC_