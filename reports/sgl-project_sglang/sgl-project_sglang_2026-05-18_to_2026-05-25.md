# sgl-project/sglang — Weekly Change Report
**Period:** 2026-05-18 → 2026-05-25  |  **Total commits:** 353

## ✨ New Features This Week

- **2026-05-25** [#25895](https://github.com/sgl-project/sglang/pull/25895) — [Diffusion][NPU] Disaggregation diffusion stages support for NPU (#25895)
- **2026-05-25** [#26267](https://github.com/sgl-project/sglang/pull/26267) — [NPU] Add torchaudio dependency for NPU platform (#26267)
- **2026-05-25** [#26273](https://github.com/sgl-project/sglang/pull/26273) — ci: add nightly Docker workflow for experimental sgl-router (#26273)
- **2026-05-25** [#25775](https://github.com/sgl-project/sglang/pull/25775) — [Perf][Qwen3.5] Add case 512 to topkGatingSoftmaxKernelLauncher, (#25775)
- **2026-05-25** [#25904](https://github.com/sgl-project/sglang/pull/25904) — :memo: docs(diffusion): add MXFP4 quantization docs (#25904)
- **2026-05-25** [#25874](https://github.com/sgl-project/sglang/pull/25874) — [CPU] add faster KV-cache writes (#25874)
- **2026-05-25** [#26149](https://github.com/sgl-project/sglang/pull/26149) — [VLM] feat: accept grid_thws from preprocessed metadata for kimi (#26149)
- **2026-05-24** [#26047](https://github.com/sgl-project/sglang/pull/26047) — Add --disable-attn-tp-gather opt-out for model-managed SP (#26047)
- **2026-05-24** [#25948](https://github.com/sgl-project/sglang/pull/25948) — [dsv4] support eplb (#25948)
- **2026-05-24** [#24610](https://github.com/sgl-project/sglang/pull/24610) — [observability] add ServerArgs.stat_loggers for pluggable metrics backend (#24610)
- _…and 69 more_

## 🔴 ROCm / AMD Spotlight

### Commits touching ROCm

- **2026-05-23** [`af8f66940e`](https://github.com/sgl-project/sglang/commit/af8f66940e) [#25898](https://github.com/sgl-project/sglang/pull/25898) — [AMD] Dsv4/pr1 fix run time issue (#25898)
- **2026-05-23** [`fd3e11973b`](https://github.com/sgl-project/sglang/commit/fd3e11973b) [#24587](https://github.com/sgl-project/sglang/pull/24587) — [AMD][aiter] Fix cuda_graph_kv_indices OOB under page_size>1 (#24587)
- **2026-05-23** [`a241659d18`](https://github.com/sgl-project/sglang/commit/a241659d18) [#25979](https://github.com/sgl-project/sglang/pull/25979) — [PD] Consolidate shared logic into common backend (#25979)
- **2026-05-22** [`a7555fc997`](https://github.com/sgl-project/sglang/commit/a7555fc997) [#25674](https://github.com/sgl-project/sglang/pull/25674) — [diffusion] fix: fix MOVA DAC bf16 on ROCm (#25674)
- **2026-05-21** [`d765dfd043`](https://github.com/sgl-project/sglang/commit/d765dfd043) [#26012](https://github.com/sgl-project/sglang/pull/26012) — refactor(attn): init hisparse_coordinator before attn_backend; replace lazy property with init-time capture (#26012)
- **2026-05-21** [`c5251a98a9`](https://github.com/sgl-project/sglang/commit/c5251a98a9) [#25983](https://github.com/sgl-project/sglang/pull/25983) — feat(model_runner): remove pool/backend refs from ForwardBatch via ForwardContext (#25983)
- **2026-05-21** [`8562d5ae94`](https://github.com/sgl-project/sglang/commit/8562d5ae94) [#25978](https://github.com/sgl-project/sglang/pull/25978) — [AMD] Relaxing Timeout for AMD stage-a (#25978)
- **2026-05-21** [`e72e3145a0`](https://github.com/sgl-project/sglang/commit/e72e3145a0) [#25896](https://github.com/sgl-project/sglang/pull/25896) — [AMD] Upgrade AITER (#25896)
- **2026-05-21** [`1b3d8da827`](https://github.com/sgl-project/sglang/commit/1b3d8da827) [#25965](https://github.com/sgl-project/sglang/pull/25965) — cap API quota for runner-utilization / amd-ci-job-monitor (#25965)
- **2026-05-21** [`45cadc215f`](https://github.com/sgl-project/sglang/commit/45cadc215f) [#25266](https://github.com/sgl-project/sglang/pull/25266) — [AMD][CI] Clean up AMD nightly + pr-test workflows (#25266)
- **2026-05-21** [`90efa9c83f`](https://github.com/sgl-project/sglang/commit/90efa9c83f) [#25932](https://github.com/sgl-project/sglang/pull/25932) — [AMD] Fix AMD stage-a-test-small-1-gpu (#25932)
- **2026-05-21** [`ddf3817924`](https://github.com/sgl-project/sglang/commit/ddf3817924) [#25917](https://github.com/sgl-project/sglang/pull/25917) — Revert "[AMD]fix: use CUDA event for targeted draft-to-verify sync in… (#25917)
- **2026-05-20** [`7fda3caea4`](https://github.com/sgl-project/sglang/commit/7fda3caea4) [#25356](https://github.com/sgl-project/sglang/pull/25356) — [AMD] test(sgl-kernel): seed RNG on ROCm in test_moe_topk_sigmoid to fix tie-break flake (#25356)
- **2026-05-19** [`aad00b0ed8`](https://github.com/sgl-project/sglang/commit/aad00b0ed8) [#25451](https://github.com/sgl-project/sglang/pull/25451) — Upgrade transformers to 5.8.1 (#25451)
- **2026-05-19** [`7c3f614e23`](https://github.com/sgl-project/sglang/commit/7c3f614e23) [#25740](https://github.com/sgl-project/sglang/pull/25740) — [AMD] Bump amd/Kimi-K2.5-MXFP4 revision to align with shared-experts fusion (#25740)
- **2026-05-18** [`866793c502`](https://github.com/sgl-project/sglang/commit/866793c502) [#24933](https://github.com/sgl-project/sglang/pull/24933) — Amd/deepseek v4 rebase main 0509 (#24933)
- **2026-05-18** [`abe2ec2aff`](https://github.com/sgl-project/sglang/commit/abe2ec2aff) [#25390](https://github.com/sgl-project/sglang/pull/25390) — [AMD] Enable shared-experts fusion with new KIMI-K2.5-MXFP4 model. (#25390)
- **2026-05-18** [`54eb2904a4`](https://github.com/sgl-project/sglang/commit/54eb2904a4) [#25178](https://github.com/sgl-project/sglang/pull/25178) — minor: docs include mac installation (#25178)
- **2026-05-18** [`7adb37bb52`](https://github.com/sgl-project/sglang/commit/7adb37bb52) [#25301](https://github.com/sgl-project/sglang/pull/25301) — [AMD] fix moriep unittest oom on mi300x ci (#25301)

### Open Issues mentioning ROCm / AMD

| # | Title | Labels | Updated |
|---|-------|--------|---------|
| [#26300](https://github.com/sgl-project/sglang/issues/26300) | [Bug] sglang中的使用export SGLANG_NPU_FUSED_MOE_MODE=2  --moe-a2a-backend  | — | 2026-05-25 |
| [#21302](https://github.com/sgl-project/sglang/issues/21302) | [AITER-Upgrade] PR readiness | — | 2026-05-25 |
| [#26246](https://github.com/sgl-project/sglang/issues/26246) | [Bug] HiSparse running on grace blackwell hits illegal memory access p | — | 2026-05-25 |
| [#25487](https://github.com/sgl-project/sglang/issues/25487) | [Bug] CUDA graph capture with ninja build error on CUDA 13 | — | 2026-05-25 |
| [#26196](https://github.com/sgl-project/sglang/issues/26196) | DeepEP Buffer initialization fails with 'invalid resource handle' on G | — | 2026-05-24 |
| [#24656](https://github.com/sgl-project/sglang/issues/24656) | [RFC] Agent-Aware KV Cache Phase 1 for Agentic Workloads | — | 2026-05-23 |
| [#25742](https://github.com/sgl-project/sglang/issues/25742) | GLM-5.1-MXFP4 on AMD MI355X — massive GSM8K accuracy degradation on v0 | — | 2026-05-23 |
| [#26092](https://github.com/sgl-project/sglang/issues/26092) | [Bug] HiCache on prefill + HiSparse on decode causes prefill scheduler | — | 2026-05-23 |
| [#26122](https://github.com/sgl-project/sglang/issues/26122) | [Bug] qwen 3.5 throws an error in l40 | — | 2026-05-22 |
| [#26061](https://github.com/sgl-project/sglang/issues/26061) | [Bug] Mooncake Master Node Shows 0 B SSD Capacity Despite Enabling SSD | — | 2026-05-22 |
| [#26087](https://github.com/sgl-project/sglang/issues/26087) | [Question] Does SGLang GLM-5 support NVIDIA SM120 GPUs? | — | 2026-05-22 |
| [#25972](https://github.com/sgl-project/sglang/issues/25972) | [Bug] PD disaggregation + decode radix cache double-counts cached_toke | — | 2026-05-21 |
| [#25887](https://github.com/sgl-project/sglang/issues/25887) | [Bug] CP+PP Occur RuntimeError: The size of tensor a (4) must match th | — | 2026-05-21 |
| [#21942](https://github.com/sgl-project/sglang/issues/21942) | [Bug] [AMD] spec v2 + DP Memory access fault | — | 2026-05-21 |
| [#23494](https://github.com/sgl-project/sglang/issues/23494) | AMD Development Roadmap (2026 Q2) | amd | 2026-05-20 |
| [#25797](https://github.com/sgl-project/sglang/issues/25797) | [Bug] [amd] [amd/deepseek_v4] HSA_STATUS_ERROR_OUT_OF_RESOURCES on MI3 | — | 2026-05-19 |
| [#25780](https://github.com/sgl-project/sglang/issues/25780) | Whisper Runtime Crash During Inference After Successful Server Startup | — | 2026-05-19 |
| [#22949](https://github.com/sgl-project/sglang/issues/22949) | Development Roadmap (2026 Q2) | — | 2026-05-19 |
| [#16565](https://github.com/sgl-project/sglang/issues/16565) | [Roadmap][Feature] Support Moore Threads (MUSA) GPU | mthreads | 2026-05-19 |
| [#24488](https://github.com/sgl-project/sglang/issues/24488) | [Help] [Performance] PD disaggregation on H200 shows no throughput gai | — | 2026-05-18 |

## Summary by Component

| Component | Commits |
|-----------|:-------:|
| Scheduler / Batching | 52 |
| Attention / FlashInfer | 47 |
| Prefill / Decode Disaggregation | 45 |
| Multimodal | 42 |
| MoE / Expert Parallel | 38 |
| CI / Build | 18 |
| Speculative Decoding | 17 |
| Other | 17 |
| KV Cache / Memory | 15 |
| Quantization | 14 |
| Triton / Kernels | 11 |
| Models | 10 |
| Tensor / Data Parallel | 9 |
| Docs / Examples | 6 |
| ROCm / AMD | 5 |
| Serving / API | 3 |
| LoRA | 2 |
| Structured Output | 2 |

## Scheduler / Batching  (52 commits)

- **2026-05-25** [`ca029e816b`](https://github.com/sgl-project/sglang/commit/ca029e816b) [#25404](https://github.com/sgl-project/sglang/pull/25404)
  Fix missing idle-batch handling in prepare_mlp_sync_batch_raw (#25404)
  _Files: `python/sglang/srt/managers/scheduler_components/dp_attn.py`_
- **2026-05-24** [`826a4de062`](https://github.com/sgl-project/sglang/commit/826a4de062) [#26165](https://github.com/sgl-project/sglang/pull/26165)
  [srt] store req input ids as arrays (#26165)
  _Files: `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-23** [`1e59ed7443`](https://github.com/sgl-project/sglang/commit/1e59ed7443) [#26129](https://github.com/sgl-project/sglang/pull/26129)
  compile _resolve_spec_extras gather kernels (#26129)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-23** [`208397affc`](https://github.com/sgl-project/sglang/commit/208397affc) [#26126](https://github.com/sgl-project/sglang/pull/26126)
  [RL] [Spec v2] Use stop-aware seqlen for returned topk metadata (#26126)
  _Files: `python/sglang/srt/managers/scheduler_components/batch_result_processor.py`_
- **2026-05-22** [`763174fa6c`](https://github.com/sgl-project/sglang/commit/763174fa6c) [#26108](https://github.com/sgl-project/sglang/pull/26108)
  FutureMap: debug-assert that gather sees a stashed value (#26108)
  _Files: `python/sglang/srt/managers/overlap_utils.py`_
- **2026-05-22** [`16d049f898`](https://github.com/sgl-project/sglang/commit/16d049f898) [#26068](https://github.com/sgl-project/sglang/pull/26068)
  Add sglang-cherrypick skill for batching bot-cherry-pick dispatches (#26068)
  _Files: `.claude/skills/sglang-cherrypick/SKILL.md`_
- **2026-05-21** [`44ec2ee18d`](https://github.com/sgl-project/sglang/commit/44ec2ee18d) [#25922](https://github.com/sgl-project/sglang/pull/25922)
  [core] Unify output_tokens_buf in FutureMap (#25922)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`_
- **2026-05-21** [`40faf44f7a`](https://github.com/sgl-project/sglang/commit/40faf44f7a) [#25366](https://github.com/sgl-project/sglang/pull/25366)
  [auto-detect] match Ring-2.6/Ling XML kv tool-call format via vocab signature (#25366)
  _Files: `python/sglang/srt/managers/template_detection.py`, `test/registered/unit/managers/test_template_manager.py`_
- **2026-05-21** [`791a2f057f`](https://github.com/sgl-project/sglang/commit/791a2f057f) [#25807](https://github.com/sgl-project/sglang/pull/25807)
  Add overridable hooks for custom chat serving implementations (#25807)
  _Files: `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/entrypoints/openai/protocol.py`, `python/sglang/srt/entrypoints/openai/serving_chat.py`, `python/sglang/srt/entrypoints/openai/sse_utils.py` _+3 more__
- **2026-05-20** [`24d27c2035`](https://github.com/sgl-project/sglang/commit/24d27c2035) [#24070](https://github.com/sgl-project/sglang/pull/24070)
  [BugFix] Fix rid_to_state leak for aborted queued requests (#24070)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`, `test/registered/unit/managers/test_tokenizer_manager_rid_cleanup.py`_
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

## Attention / FlashInfer  (47 commits)

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
- **2026-05-24** [`93fa577bb9`](https://github.com/sgl-project/sglang/commit/93fa577bb9) [#26205](https://github.com/sgl-project/sglang/pull/26205)
  Clean up server startup log noise (#26205)
  _Files: `.claude/skills/clean-startup-log/SKILL.md`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/managers/template_detection.py` _+5 more__
- **2026-05-24** [`0b65588c18`](https://github.com/sgl-project/sglang/commit/0b65588c18) [#25514](https://github.com/sgl-project/sglang/pull/25514)
  [diffusion] Clean up VSA attention hot path (#25514)
  _Files: `python/sglang/multimodal_gen/runtime/layers/attention/backends/sparse_linear_attn.py`, `python/sglang/multimodal_gen/runtime/layers/attention/backends/video_sparse_attn.py`, `python/sglang/multimodal_gen/runtime/models/dits/wanvideo.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py` _+1 more__
- **2026-05-23** [`a5a64a311a`](https://github.com/sgl-project/sglang/commit/a5a64a311a) [#25925](https://github.com/sgl-project/sglang/pull/25925)
  [Spec] trtllm mha supports overlap plan stream (#25925)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`_
- **2026-05-23** [`cb7b57955d`](https://github.com/sgl-project/sglang/commit/cb7b57955d) [#26170](https://github.com/sgl-project/sglang/pull/26170)
  fix tokenspeed_mla attn kernel jit (#26170)
  _Files: `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`_
- **2026-05-23** [`83a18e687d`](https://github.com/sgl-project/sglang/commit/83a18e687d) [#26134](https://github.com/sgl-project/sglang/pull/26134)
  Revert "[refactor] unify cuda-graph capture/replay across attention backends (#26134)" (#26166)
  _Files: `python/sglang/srt/layers/attention/cutlass_mla_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+1 more__
- **2026-05-23** [`5964d30233`](https://github.com/sgl-project/sglang/commit/5964d30233) [#26152](https://github.com/sgl-project/sglang/pull/26152)
  fix(swa): eliminate spurious translate_loc_from_full_to_swa warning in BCG and CG paths (#26152)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-23** [`fd3e11973b`](https://github.com/sgl-project/sglang/commit/fd3e11973b) [#24587](https://github.com/sgl-project/sglang/pull/24587)
  [AMD][aiter] Fix cuda_graph_kv_indices OOB under page_size>1 (#24587)
  _Files: `python/sglang/srt/layers/attention/aiter_backend.py`_
- **2026-05-23** [`7b7f1067bd`](https://github.com/sgl-project/sglang/commit/7b7f1067bd) [#26141](https://github.com/sgl-project/sglang/pull/26141)
  Add non-MTP DSV4 test coverage (#26141)
  _Files: `test/registered/models_e2e/test_deepseek_v4_flash_fp4_b200.py`, `test/registered/models_e2e/test_deepseek_v4_flash_fp4_h200.py`_
- **2026-05-23** [`d226f75669`](https://github.com/sgl-project/sglang/commit/d226f75669) [#26134](https://github.com/sgl-project/sglang/pull/26134)
  [refactor] unify cuda-graph capture/replay across attention backends (#26134)
  _Files: `python/sglang/srt/layers/attention/cutlass_mla_backend.py`, `python/sglang/srt/layers/attention/flashinfer_backend.py`, `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`, `python/sglang/srt/layers/attention/triton_backend.py` _+1 more__
- **2026-05-22** [`c112f7623a`](https://github.com/sgl-project/sglang/commit/c112f7623a) [#26017](https://github.com/sgl-project/sglang/pull/26017)
  Skip init_mha_chunk_metadata in trtllm_mla when not needed (#26017)
  _Files: `python/sglang/srt/layers/attention/trtllm_mla_backend.py`_
- **2026-05-22** [`cadfa2d025`](https://github.com/sgl-project/sglang/commit/cadfa2d025) [#23351](https://github.com/sgl-project/sglang/pull/23351)
  Support piecewise CUDA graph with NSA (#23351)
  _Files: `python/sglang/jit_kernel/hadamard.py`, `python/sglang/srt/compilation/piecewise_context_manager.py`, `python/sglang/srt/configs/model_config.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py` _+8 more__
- **2026-05-22** [`b73278e4e0`](https://github.com/sgl-project/sglang/commit/b73278e4e0) [#25110](https://github.com/sgl-project/sglang/pull/25110)
  [Fix]: BCG support for RadixLinearAttention (Qwen3.5 / linear-attn hybrid models) (#25110)
  _Files: `python/sglang/srt/layers/radix_linear_attention.py`_
- **2026-05-22** [`4374789abf`](https://github.com/sgl-project/sglang/commit/4374789abf) [#24751](https://github.com/sgl-project/sglang/pull/24751)
  fix(mm): make multimodal data loading non-blocking to prevent health check stalls (#24751)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/clip.py`, `python/sglang/srt/multimodal/processors/deepseek_ocr.py`, `python/sglang/srt/multimodal/processors/deepseek_vl_v2.py` _+31 more__
- **2026-05-21** [`7cf193fe1f`](https://github.com/sgl-project/sglang/commit/7cf193fe1f) [#25753](https://github.com/sgl-project/sglang/pull/25753)
  feat: support HybridLinearKVPool in chunked prefix cache handling (#25753)
  _Files: `python/sglang/srt/model_executor/forward_batch_deepseek_mha_mixin.py`_
- **2026-05-21** [`d765dfd043`](https://github.com/sgl-project/sglang/commit/d765dfd043) [#26012](https://github.com/sgl-project/sglang/pull/26012)
  refactor(attn): init hisparse_coordinator before attn_backend; replace lazy property with init-time capture (#26012)
  _Files: `python/sglang/srt/layers/attention/deepseek_v4_backend.py`, `python/sglang/srt/layers/attention/deepseek_v4_backend_hip_radix.py`, `python/sglang/srt/layers/attention/dsa_backend.py`, `python/sglang/srt/model_executor/model_runner.py` _+4 more__
- **2026-05-21** [`17dadebd4e`](https://github.com/sgl-project/sglang/commit/17dadebd4e) [#25923](https://github.com/sgl-project/sglang/pull/25923)
  [Docs] DeepSeek-V4: switch H200 FP4 Pro to flashinfer_mxfp4, Flash Balanced too (#25923)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-21** [`c3f9bc9818`](https://github.com/sgl-project/sglang/commit/c3f9bc9818) [#24376](https://github.com/sgl-project/sglang/pull/24376)
  Fix nixl mla key and backup skipping (#24376)
  _Files: `python/sglang/srt/mem_cache/storage/nixl/README.md`, `python/sglang/srt/mem_cache/storage/nixl/hicache_nixl.py`, `python/sglang/srt/mem_cache/storage/nixl/test_hicache_nixl_storage.py`_
- **2026-05-21** [`190488e9a8`](https://github.com/sgl-project/sglang/commit/190488e9a8) [#25839](https://github.com/sgl-project/sglang/pull/25839)
  [NPU] Support chunk prefill for Qwen3.5/Qwen3.6 models (#25839)
  _Files: `python/sglang/srt/hardware_backend/npu/attention/ascend_gdn_backend.py`, `python/sglang/srt/mem_cache/memory_pool.py`_
- **2026-05-21** [`84ea47eb22`](https://github.com/sgl-project/sglang/commit/84ea47eb22) [#8666](https://github.com/sgl-project/sglang/pull/8666)
  [CPU] Fix issues when running llama3.2-11B vision model with image tasks (#8666)
  _Files: `python/sglang/srt/layers/attention/intel_amx_backend.py`, `python/sglang/srt/layers/attention/torch_native_backend.py`, `python/sglang/srt/models/mllama.py`, `sgl-kernel/csrc/cpu/decode.cpp` _+11 more__
- **2026-05-21** [`79b937aefb`](https://github.com/sgl-project/sglang/commit/79b937aefb) [#25824](https://github.com/sgl-project/sglang/pull/25824)
  [Refactor] Encapsulate SWA loc translation inside SWAKVPool with per-batch cache invalidation (#25824)
  _Files: `python/sglang/srt/layers/attention/triton_backend.py`, `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/layers/radix_attention.py`, `python/sglang/srt/layers/radix_linear_attention.py` _+14 more__
- **2026-05-21** [`f9f82d238c`](https://github.com/sgl-project/sglang/commit/f9f82d238c) [#25646](https://github.com/sgl-project/sglang/pull/25646)
  fix deepseek v4 hisparse (#25646)
  _Files: `python/sglang/srt/layers/attention/dsv4/compressor_v2.py`_
- **2026-05-20** [`1a17d753f1`](https://github.com/sgl-project/sglang/commit/1a17d753f1) [#25460](https://github.com/sgl-project/sglang/pull/25460)
  [perf] prepare_prefill_qkv hook + fp8 quantize jit kernel (#25460)
  _Files: `python/sglang/jit_kernel/fp8_quantize.py`, `python/sglang/srt/layers/attention/tokenspeed_mla_backend.py`, `python/sglang/srt/layers/attention/trtllm_mla_backend.py`, `python/sglang/srt/models/deepseek_common/attention_forward_methods/forward_mha.py`_
- **2026-05-20** [`801d7e3eed`](https://github.com/sgl-project/sglang/commit/801d7e3eed) [#25859](https://github.com/sgl-project/sglang/pull/25859)
  [DSA] Make MQA logits free memory ratio configurable (#25859)
  _Files: `python/sglang/srt/environ.py`, `python/sglang/srt/layers/attention/dsa/dsa_indexer.py`_
- **2026-05-20** [`1f209b4433`](https://github.com/sgl-project/sglang/commit/1f209b4433) [#25681](https://github.com/sgl-project/sglang/pull/25681)
  Add support for generic num_tokens_per_bs in TARGET_VERIFY (#25681)
  _Files: `python/sglang/srt/layers/attention/trtllm_mha_backend.py`, `python/sglang/srt/model_executor/cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/speculative/spec_info.py` _+1 more__
- **2026-05-20** [`bdacb1be4d`](https://github.com/sgl-project/sglang/commit/bdacb1be4d) [#25861](https://github.com/sgl-project/sglang/pull/25861)
  Update CODEOWNERS to replace 'nsa' with 'dsa' (#25861)
  _Files: `.github/CODEOWNERS`_
- **2026-05-20** [`8131641bc6`](https://github.com/sgl-project/sglang/commit/8131641bc6) [#25821](https://github.com/sgl-project/sglang/pull/25821)
  [Refactor] Rename NSA → DSA: user-facing aliases, file/class/import rename (#25821)
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

## Prefill / Decode Disaggregation  (45 commits)

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
- **2026-05-23** [`a241659d18`](https://github.com/sgl-project/sglang/commit/a241659d18) [#25979](https://github.com/sgl-project/sglang/pull/25979)
  [PD] Consolidate shared logic into common backend (#25979)
  _Files: `python/sglang/srt/disaggregation/common/conn.py`, `python/sglang/srt/disaggregation/common/utils.py`, `python/sglang/srt/disaggregation/mooncake/conn.py`, `python/sglang/srt/disaggregation/mori/conn.py` _+1 more__
- **2026-05-22** [`085777210c`](https://github.com/sgl-project/sglang/commit/085777210c) [#25844](https://github.com/sgl-project/sglang/pull/25844)
  feat(kv-events): expose structured KV-event publisher block on /server_info (#25844)
  _Files: `python/sglang/srt/disaggregation/kv_events.py`, `python/sglang/srt/entrypoints/http_server.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/entrypoints/test_server_info.py`_
- **2026-05-22** [`06c23d55b5`](https://github.com/sgl-project/sglang/commit/06c23d55b5) [#25098](https://github.com/sgl-project/sglang/pull/25098)
  perf: migrate Req token-id storage to array.array('q') in Scheduler (#25098)
  _Files: `benchmark/scheduler/bench_token_storage.py`, `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/disaggregation/encode_receiver.py`, `python/sglang/srt/dllm/mixin/req.py` _+30 more__
- **2026-05-22** [`8c916a715c`](https://github.com/sgl-project/sglang/commit/8c916a715c) [#25168](https://github.com/sgl-project/sglang/pull/25168)
  [diffusion] feat: support role-based component loading and stage affinity (#25168)
  _Files: `python/sglang/multimodal_gen/runtime/disaggregation/roles.py`, `python/sglang/multimodal_gen/runtime/pipelines/hunyuan3d_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/mova_pipeline.py`, `python/sglang/multimodal_gen/runtime/pipelines/qwen_image.py` _+8 more__
- **2026-05-22** [`10751a4f0c`](https://github.com/sgl-project/sglang/commit/10751a4f0c) [#26085](https://github.com/sgl-project/sglang/pull/26085)
  drop `FutureIndices` wrapper class (#26085)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/managers/utils.py` _+1 more__
- **2026-05-22** [`c4b6b5ea1e`](https://github.com/sgl-project/sglang/commit/c4b6b5ea1e) [#26020](https://github.com/sgl-project/sglang/pull/26020)
  [core] step 2: drop seq_lens sentinel; SB maintains GPU as `seq_lens_cpu` mirror (#26020)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+2 more__
- **2026-05-22** [`3f0814974c`](https://github.com/sgl-project/sglang/commit/3f0814974c) [#25982](https://github.com/sgl-project/sglang/pull/25982)
  Fix disaggregation bootstrap server lifetime (#25982)
  _Files: `python/sglang/srt/managers/tokenizer_manager.py`_
- **2026-05-22** [`8b473aa0bc`](https://github.com/sgl-project/sglang/commit/8b473aa0bc) [#25944](https://github.com/sgl-project/sglang/pull/25944)
  [core] step 1: route non-spec `seq_lens` via `FutureMap` with per-mode bootstrap fixes (#25944)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+7 more__
- **2026-05-21** [`fbebdd5105`](https://github.com/sgl-project/sglang/commit/fbebdd5105) [#25990](https://github.com/sgl-project/sglang/pull/25990)
  [CI] Enable nixl disaggregation test for decode radix cache (#25990)
  _Files: `test/registered/distributed/test_disaggregation_decode_radix_cache.py`_
- **2026-05-21** [`baeac179f7`](https://github.com/sgl-project/sglang/commit/baeac179f7) [#25879](https://github.com/sgl-project/sglang/pull/25879)
  [Spec] Route seq_lens through FutureMap; drop verify_done.wait (#25879)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py` _+5 more__
- **2026-05-21** [`45cadc215f`](https://github.com/sgl-project/sglang/commit/45cadc215f) [#25266](https://github.com/sgl-project/sglang/pull/25266)
  [AMD][CI] Clean up AMD nightly + pr-test workflows (#25266)
  _Files: `.claude/skills/write-sglang-test/SKILL.md`, `.github/workflows/nightly-test-amd-rocm720.yml`, `.github/workflows/nightly-test-amd.yml`, `.github/workflows/pr-test-amd-rocm720.yml` _+8 more__
- **2026-05-21** [`643d44d699`](https://github.com/sgl-project/sglang/commit/643d44d699) [#24226](https://github.com/sgl-project/sglang/pull/24226)
  [BugFix] fix(hicache): fix two slot-reuse races in DecodeKVCacheOffloadManager (#24226)
  _Files: `python/sglang/srt/disaggregation/decode_kvcache_offload_manager.py`, `test/registered/disaggregation/test_disaggregation_decode_offload.py`, `test/registered/disaggregation/test_specv2_kvcache_offloading.py`_
- **2026-05-20** [`512d164916`](https://github.com/sgl-project/sglang/commit/512d164916) [#25862](https://github.com/sgl-project/sglang/pull/25862)
  Address overlap future token map by request-pool index (#25862)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/spec_info.py`_
- **2026-05-20** [`9b005d3608`](https://github.com/sgl-project/sglang/commit/9b005d3608) [#25819](https://github.com/sgl-project/sglang/pull/25819)
  disagg prebuilt: drop dead prepare_for_extend shift (#25819)
  _Files: `python/sglang/srt/disaggregation/decode_schedule_batch_mixin.py`, `python/sglang/srt/speculative/eagle_info.py`, `python/sglang/srt/speculative/eagle_utils.py`, `python/sglang/srt/speculative/eagle_worker.py` _+1 more__
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

## Multimodal  (42 commits)

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
- **2026-05-24** [`5c3775823e`](https://github.com/sgl-project/sglang/commit/5c3775823e) [#26214](https://github.com/sgl-project/sglang/pull/26214)
  [diffusion] chore: use model-aware vae channels_last_3d policy (#26214)
  _Files: `python/sglang/multimodal_gen/envs.py`, `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/test/server/test_component_accuracy_1_gpu.py`, `python/sglang/multimodal_gen/test/server/test_component_accuracy_2_gpu.py` _+2 more__
- **2026-05-24** [`b6f71d5850`](https://github.com/sgl-project/sglang/commit/b6f71d5850) [#26096](https://github.com/sgl-project/sglang/pull/26096)
  [VLM] avoid extra cuda-ipc staging for preprocessed input (#26096)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/multimodal/processors/base_processor.py`, `test/manual/vlm/test_mm_utils.py`_
- **2026-05-24** [`6447596501`](https://github.com/sgl-project/sglang/commit/6447596501) [#26167](https://github.com/sgl-project/sglang/pull/26167)
  [VLM] feat: replace small H2D calls with a single one for qwen-vl (#26167)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/models/qwen3_vl.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-05-24** [`4c2b32bfbf`](https://github.com/sgl-project/sglang/commit/4c2b32bfbf) [#26101](https://github.com/sgl-project/sglang/pull/26101)
  [VLM] accept precomputed multimodal metadata (#26101)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-05-24** [`d6d9f12444`](https://github.com/sgl-project/sglang/commit/d6d9f12444) [#26100](https://github.com/sgl-project/sglang/pull/26100)
  [VLM] adopt simplified get_rope_index for image-only requests (#26100)
  _Files: `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-05-23** [`2de74035a5`](https://github.com/sgl-project/sglang/commit/2de74035a5) [#25403](https://github.com/sgl-project/sglang/pull/25403)
  [FIX][2/2] fix step3-vl/deepseek-ocr image processor error (#25403)
  _Files: `python/sglang/srt/configs/deepseek_ocr.py`_
- **2026-05-23** [`774b29dade`](https://github.com/sgl-project/sglang/commit/774b29dade) [#26117](https://github.com/sgl-project/sglang/pull/26117)
  [VLM] feat: early-return in mm processor if the input is preprocessed (#26117)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/multimodal/processors/base_processor.py`_
- **2026-05-23** [`19b60a4f9e`](https://github.com/sgl-project/sglang/commit/19b60a4f9e) [#26116](https://github.com/sgl-project/sglang/pull/26116)
  [VLM] reuse pretokenized ids from preprocessed input for qwen-vl (#26116)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-05-23** [`8b9fb13c4a`](https://github.com/sgl-project/sglang/commit/8b9fb13c4a) [#24144](https://github.com/sgl-project/sglang/pull/24144)
  [BugFix][EPD] adapt for qwen3.5-mtp & del duplicated logs (#24144)
  _Files: `python/sglang/srt/multimodal/processors/qwen_vl.py`_
- **2026-05-23** [`c8cea6d4aa`](https://github.com/sgl-project/sglang/commit/c8cea6d4aa) [#26121](https://github.com/sgl-project/sglang/pull/26121)
  [diffusion] feat: auto-select vae channels_last_3d (#26121)
  _Files: `python/sglang/multimodal_gen/runtime/loader/component_loaders/vae_loader.py`, `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_common_utils.py`, `python/sglang/multimodal_gen/test/server/accuracy_hooks.py`, `python/sglang/multimodal_gen/test/server/accuracy_utils.py` _+4 more__
- **2026-05-22** [`b801a27ce6`](https://github.com/sgl-project/sglang/commit/b801a27ce6) [#26120](https://github.com/sgl-project/sglang/pull/26120)
  [diffusion] CI: disable torch compile in nightly comparison (#26120)
  _Files: `scripts/ci/utils/diffusion/comparison_configs.json`, `scripts/ci/utils/diffusion/run_comparison.py`_
- **2026-05-22** [`9bbd519f34`](https://github.com/sgl-project/sglang/commit/9bbd519f34) [#25985](https://github.com/sgl-project/sglang/pull/25985)
  [diffusion] fix: fix Wan channels_last_3d VAE decode corruption (#25985)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_common_utils.py`, `python/sglang/multimodal_gen/runtime/models/vaes/parallel/wan_dist_utils.py`, `python/sglang/multimodal_gen/test/test_utils.py`_
- **2026-05-22** [`f5ed2687ec`](https://github.com/sgl-project/sglang/commit/f5ed2687ec) [#26044](https://github.com/sgl-project/sglang/pull/26044)
  [diffusion] CI: guard gt publishing from corrupt output (#26044)
  _Files: `.github/workflows/diffusion-ci-gt-gen.yml`, `scripts/ci/utils/diffusion/publish_diffusion_gt.py`_
- **2026-05-22** [`e1dcbca220`](https://github.com/sgl-project/sglang/commit/e1dcbca220) [#24701](https://github.com/sgl-project/sglang/pull/24701)
  [FIX][1/2] fix step3-vl/deepseek-ocr image processor error (#24701)
  _Files: `python/sglang/srt/multimodal/processors/step3_vl.py`_
- **2026-05-22** [`cf5f496183`](https://github.com/sgl-project/sglang/commit/cf5f496183) [#25074](https://github.com/sgl-project/sglang/pull/25074)
  [MUSA][22/N] ci(musa): repack wheels with +musa metadata, refine path filters, sync multimodal tests, and add nightly workflow (#25074)
  _Files: `.github/workflows/nightly-test-musa.yml`, `.github/workflows/pr-test-musa.yml`, `python/sglang/multimodal_gen/test/run_suite_musa.py`, `python/sglang/multimodal_gen/test/server/musa/perf_baselines_musa.json` _+5 more__
- **2026-05-22** [`a7555fc997`](https://github.com/sgl-project/sglang/commit/a7555fc997) [#25674](https://github.com/sgl-project/sglang/pull/25674)
  [diffusion] fix: fix MOVA DAC bf16 on ROCm (#25674)
  _Files: `python/sglang/multimodal_gen/runtime/models/vaes/dac.py`_
- **2026-05-22** [`fa6f4dfb35`](https://github.com/sgl-project/sglang/commit/fa6f4dfb35) [#25910](https://github.com/sgl-project/sglang/pull/25910)
  improve: combine vit calls for images from different reqs from one batch (#25910)
  _Files: `python/sglang/srt/managers/mm_utils.py`, `python/sglang/srt/managers/schedule_batch.py`_
- **2026-05-22** [`ae7c4226eb`](https://github.com/sgl-project/sglang/commit/ae7c4226eb) [#25661](https://github.com/sgl-project/sglang/pull/25661)
  [diffusion] model: support FLUX.2-klein-base (#25661)
  _Files: `.github/workflows/diffusion-ci-gt-gen.yml`, `docs/diffusion/compatibility_matrix.md`, `docs_new/docs/sglang-diffusion/compatibility_matrix.mdx`, `docs_new/docs/sglang-diffusion/dynamic_batching.mdx` _+6 more__
- **2026-05-22** [`16b3edc84f`](https://github.com/sgl-project/sglang/commit/16b3edc84f) [#25988](https://github.com/sgl-project/sglang/pull/25988)
  [diffusion] feat: enable warmup for sglang serve by default (#25988)
  _Files: `python/sglang/multimodal_gen/runtime/entrypoints/cli/serve.py`, `python/sglang/multimodal_gen/runtime/managers/scheduler.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/text_encoding.py`, `python/sglang/multimodal_gen/test/server/gpu_cases.py` _+3 more__
- **2026-05-22** [`f6d98a17ba`](https://github.com/sgl-project/sglang/commit/f6d98a17ba) [#25893](https://github.com/sgl-project/sglang/pull/25893)
  [diffusion] optimize: reuse cached dynamic lora weights (#25893)
  _Files: `python/sglang/multimodal_gen/runtime/pipelines_core/lora_pipeline.py`, `python/sglang/multimodal_gen/test/server/perf_baselines.json`, `python/sglang/multimodal_gen/test/unit/test_lora_pipeline.py`_
- **2026-05-21** [`ca9dc17be4`](https://github.com/sgl-project/sglang/commit/ca9dc17be4) [#25930](https://github.com/sgl-project/sglang/pull/25930)
  [diffusion] chore: adjust layer wise-offload strategy (#25930)
  _Files: `python/sglang/multimodal_gen/configs/pipeline_configs/wan.py`, `python/sglang/multimodal_gen/runtime/server_args_auto_tune.py`, `python/sglang/multimodal_gen/test/server/test_server_common.py`, `python/sglang/multimodal_gen/test/server/test_server_utils.py` _+2 more__
- **2026-05-21** [`32f996b75a`](https://github.com/sgl-project/sglang/commit/32f996b75a) [#25956](https://github.com/sgl-project/sglang/pull/25956)
  Avoiding the problem of printing a large number of compatibility warn… (#25956)
  _Files: `python/sglang/test/ascend/gsm8k_ascend_mixin.py`, `python/sglang/test/ascend/vlm_utils.py`_
- **2026-05-21** [`c4f14650b9`](https://github.com/sgl-project/sglang/commit/c4f14650b9) [#23809](https://github.com/sgl-project/sglang/pull/23809)
  fix act fun for xpu (#23809)
  _Files: `python/sglang/multimodal_gen/runtime/layers/activation.py`, `python/sglang/multimodal_gen/runtime/layers/rotary_embedding/base.py`_
- **2026-05-21** [`1ac3e33622`](https://github.com/sgl-project/sglang/commit/1ac3e33622) [#25891](https://github.com/sgl-project/sglang/pull/25891)
  [diffusion] optimize: enable inference mode in pipeline executor (#25891)
  _Files: `python/sglang/multimodal_gen/runtime/layers/lora/linear.py`, `python/sglang/multimodal_gen/runtime/managers/memory_managers/layerwise_offload.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/parallel_executor.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py` _+5 more__
- **2026-05-21** [`e56db8bd24`](https://github.com/sgl-project/sglang/commit/e56db8bd24) [#21191](https://github.com/sgl-project/sglang/pull/21191)
  fix: use base GPU ID CUDA device for multimodal processor (#21191)
  _Files: `python/sglang/srt/multimodal/processors/base_processor.py`_
- **2026-05-20** [`47979fb252`](https://github.com/sgl-project/sglang/commit/47979fb252) [#25697](https://github.com/sgl-project/sglang/pull/25697)
  [diffusion] fix: fix GLM-Image /v1/images/edits support (#25697)
  _Files: `python/sglang/jit_kernel/diffusion/triton/scale_shift.py`, `python/sglang/multimodal_gen/configs/pipeline_configs/glm_image.py`, `python/sglang/multimodal_gen/runtime/layers/layernorm.py`, `python/sglang/multimodal_gen/runtime/pipelines_core/stages/model_specific_stages/glm_image.py`_
- **2026-05-20** [`e99f87c974`](https://github.com/sgl-project/sglang/commit/e99f87c974) [#25817](https://github.com/sgl-project/sglang/pull/25817)
  fix: add missing distro dependency to runtime docker image (#25817)
  _Files: `python/pyproject.toml`_
- **2026-05-20** [`af22390af7`](https://github.com/sgl-project/sglang/commit/af22390af7) [#25842](https://github.com/sgl-project/sglang/pull/25842)
  [codex] Align diffusion skills with nightly Nvidia benchmarks (#25842)
  _Files: `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/SKILL.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py`, `python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-performance/SKILL.md`_
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

## MoE / Expert Parallel  (38 commits)

- **2026-05-25** [`e27d4fb70f`](https://github.com/sgl-project/sglang/commit/e27d4fb70f) [#25775](https://github.com/sgl-project/sglang/pull/25775)
  [Perf][Qwen3.5] Add case 512 to topkGatingSoftmaxKernelLauncher, (#25775)
  _Files: `sgl-kernel/benchmark/bench_moe_topk_softmax.py`, `sgl-kernel/csrc/moe/moe_topk_softmax_kernels.cu`, `sgl-kernel/tests/test_moe_topk_softmax.py`_
- **2026-05-24** [`7f45bcdd2a`](https://github.com/sgl-project/sglang/commit/7f45bcdd2a) [#25948](https://github.com/sgl-project/sglang/pull/25948)
  [dsv4] support eplb (#25948)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`, `python/sglang/srt/models/deepseek_v4.py`_
- **2026-05-24** [`9d50cd9742`](https://github.com/sgl-project/sglang/commit/9d50cd9742) [#24610](https://github.com/sgl-project/sglang/pull/24610)
  [observability] add ServerArgs.stat_loggers for pluggable metrics backend (#24610)
  _Files: `python/sglang/srt/eplb/expert_distribution.py`, `python/sglang/srt/managers/tokenizer_manager.py`, `python/sglang/srt/mem_cache/base_prefix_cache.py`, `python/sglang/srt/mem_cache/hi_mamba_radix_cache.py` _+5 more__
- **2026-05-23** [`af8f66940e`](https://github.com/sgl-project/sglang/commit/af8f66940e) [#25898](https://github.com/sgl-project/sglang/pull/25898)
  [AMD] Dsv4/pr1 fix run time issue (#25898)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/c128_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c4_v2.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/c_plan.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/fused_norm_rope_v2.cuh` _+28 more__
- **2026-05-23** [`b0ce16d0c5`](https://github.com/sgl-project/sglang/commit/b0ce16d0c5) [#23292](https://github.com/sgl-project/sglang/pull/23292)
  [CP] 1/N: Support MLA Prefill Context Parallel (#23292)
  _Files: `python/sglang/srt/layers/attention/flashattention_backend.py`, `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/layers/communicator_dsa_cp.py`, `python/sglang/srt/layers/utils/cp_utils.py` _+17 more__
- **2026-05-23** [`81cd338fcc`](https://github.com/sgl-project/sglang/commit/81cd338fcc) [#26164](https://github.com/sgl-project/sglang/pull/26164)
  [docs] DeepSeek-V4 cookbook: balanced MegaMoE cap, H200 Pro FP4 mem-frac, nsa-* compat, PD-disagg fixes (#26164)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-23** [`75427c9ca4`](https://github.com/sgl-project/sglang/commit/75427c9ca4) [#25843](https://github.com/sgl-project/sglang/pull/25843)
  Route concat MLA to JIT and remove unused downcast (#25843)
  _Files: `python/sglang/jit_kernel/benchmark/bench_cast.py`, `python/sglang/jit_kernel/cast.py`, `python/sglang/jit_kernel/csrc/elementwise/cast.cuh`, `python/sglang/srt/layers/attention/utils.py` _+2 more__
- **2026-05-23** [`629b6c6a85`](https://github.com/sgl-project/sglang/commit/629b6c6a85) [#19918](https://github.com/sgl-project/sglang/pull/19918)
  correct allreduce fusion and dummy_run alignment in SCATTERED MLP mode (moe_dense_tp_size=1) (#19918)
  _Files: `python/sglang/srt/layers/communicator.py`, `python/sglang/srt/model_executor/model_runner.py`, `test/registered/moe/test_hybrid_dp_ep_tp_mtp.py`_
- **2026-05-22** [`2df9e8b4b3`](https://github.com/sgl-project/sglang/commit/2df9e8b4b3) [#25189](https://github.com/sgl-project/sglang/pull/25189)
  [perf] DeepSeekV3: drop redundant FP32 upcasts in trtllm MoE paths (#25189)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-22** [`bd6c7e713c`](https://github.com/sgl-project/sglang/commit/bd6c7e713c) [#26025](https://github.com/sgl-project/sglang/pull/26025)
  [fix] Fallback DeepGEMM activation for unsupported shapes (#26025)
  _Files: `python/sglang/srt/layers/moe/moe_runner/deep_gemm.py`_
- **2026-05-22** [`cc77c36029`](https://github.com/sgl-project/sglang/commit/cc77c36029) [#23220](https://github.com/sgl-project/sglang/pull/23220)
  Bugfix: Qwen3-VL-MoE adapt encoder_only (#23220)
- **2026-05-21** [`c5251a98a9`](https://github.com/sgl-project/sglang/commit/c5251a98a9) [#25983](https://github.com/sgl-project/sglang/pull/25983)
  feat(model_runner): remove pool/backend refs from ForwardBatch via ForwardContext (#25983)
  _Files: `python/sglang/srt/batch_overlap/operations.py`, `python/sglang/srt/batch_overlap/two_batch_overlap.py`, `python/sglang/srt/hardware_backend/musa/attention/flashattention_backend.py`, `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py` _+73 more__
- **2026-05-21** [`81d686d9fa`](https://github.com/sgl-project/sglang/commit/81d686d9fa) [#26004](https://github.com/sgl-project/sglang/pull/26004)
  Default MegaMoE to W4A8 for Max-Throughput recipe (#26004)
  _Files: `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-21** [`b765faee30`](https://github.com/sgl-project/sglang/commit/b765faee30) [#25678](https://github.com/sgl-project/sglang/pull/25678)
  [MoE Refactor] deprecate forward_npu and NpuFuseEPMoE (#25678)
  _Files: `python/sglang/srt/hardware_backend/npu/moe/fuseep.py`, `python/sglang/srt/hardware_backend/npu/quantization/fused_moe_method_npu.py`, `python/sglang/srt/layers/moe/ep_moe/layer.py`, `python/sglang/srt/layers/moe/fused_moe_triton/layer.py` _+4 more__
- **2026-05-21** [`a24c374f84`](https://github.com/sgl-project/sglang/commit/a24c374f84) [#25531](https://github.com/sgl-project/sglang/pull/25531)
  [lora] Remove synchronous .any().item() guard in LoRA MoE prefill path (#25531)
  _Files: `python/sglang/srt/lora/layers.py`, `python/sglang/srt/lora/lora_moe_runners.py`_
- **2026-05-21** [`19f55c0e6d`](https://github.com/sgl-project/sglang/commit/19f55c0e6d) [#25884](https://github.com/sgl-project/sglang/pull/25884)
  [Refactor] major JIT kernel clean up for dsv4 (#25884)
  _Files: `python/sglang/jit_kernel/csrc/deepseek_v4/topk_1024.cuh`, `python/sglang/jit_kernel/csrc/deepseek_v4/topk_v1.cuh`, `python/sglang/jit_kernel/deepseek_v4.py`, `python/sglang/jit_kernel/dsv4/__init__.py` _+19 more__
- **2026-05-21** [`8fa56a0ab1`](https://github.com/sgl-project/sglang/commit/8fa56a0ab1) [#25907](https://github.com/sgl-project/sglang/pull/25907)
  Fix FlashInfer A2A token cap sizing (#25907)
  _Files: `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`_
- **2026-05-21** [`e8608bdcb5`](https://github.com/sgl-project/sglang/commit/e8608bdcb5) [#25367](https://github.com/sgl-project/sglang/pull/25367)
  Fix EPLB redundant experts with shared expert fusion and Waterfill (#25367)
  _Files: `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`, `python/sglang/srt/layers/moe/topk.py`, `python/sglang/srt/model_executor/model_runner.py`_
- **2026-05-21** [`847cbada9c`](https://github.com/sgl-project/sglang/commit/847cbada9c) [#25054](https://github.com/sgl-project/sglang/pull/25054)
  Support Gemma4 MoE NVFP4 (#25054)
  _Files: `python/sglang/srt/layers/moe/cutlass_moe.py`, `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`, `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8_moe.py`, `python/sglang/srt/layers/quantization/fp8.py` _+5 more__
- **2026-05-21** [`74c6294ba9`](https://github.com/sgl-project/sglang/commit/74c6294ba9) [#25759](https://github.com/sgl-project/sglang/pull/25759)
  [BugFix][EPD]Fix Qwen3VLMoe encoder-only AttributeError (#25759)
  _Files: `python/sglang/srt/models/qwen3_vl_moe.py`_
- **2026-05-20** [`9f2bc24b35`](https://github.com/sgl-project/sglang/commit/9f2bc24b35) [#25892](https://github.com/sgl-project/sglang/pull/25892)
  Fix/dsv4 flash eagle dummy ima (#25892)
  _Files: `python/sglang/srt/layers/moe/hash_topk.py`_
- **2026-05-20** [`614672fea5`](https://github.com/sgl-project/sglang/commit/614672fea5) [#25831](https://github.com/sgl-project/sglang/pull/25831)
  [Test] Stage-a sanity kits; consolidate core/ + models_e2e/ tests (#25831)
  _Files: `python/sglang/test/kits/basic_api_contract_kit.py`, `python/sglang/test/kits/basic_decode_correctness_kit.py`, `python/sglang/test/kits/basic_scheduler_stress_kit.py`, `python/sglang/test/kits/server_sanity_kit.py` _+32 more__
- **2026-05-20** [`044649c23a`](https://github.com/sgl-project/sglang/commit/044649c23a) [#22669](https://github.com/sgl-project/sglang/pull/22669)
  feat: Support flashinfer_cutedsl MoE runner with flashinfer alltoall backend (#22669)
  _Files: `python/sglang/srt/layers/moe/moe_runner/flashinfer_cutedsl.py`, `python/sglang/srt/layers/moe/token_dispatcher/flashinfer.py`, `python/sglang/srt/layers/quantization/modelopt_quant.py`, `python/sglang/srt/models/qwen2_moe.py` _+2 more__
- **2026-05-20** [`7fda3caea4`](https://github.com/sgl-project/sglang/commit/7fda3caea4) [#25356](https://github.com/sgl-project/sglang/pull/25356)
  [AMD] test(sgl-kernel): seed RNG on ROCm in test_moe_topk_sigmoid to fix tie-break flake (#25356)
  _Files: `sgl-kernel/tests/test_moe_topk_sigmoid.py`_
- **2026-05-20** [`052abcc0dd`](https://github.com/sgl-project/sglang/commit/052abcc0dd) [#25825](https://github.com/sgl-project/sglang/pull/25825)
  [Refactor] Pass PP start_layer via model constructor instead of forward_batch.token_to_kv_pool (#25825)
  _Files: `python/sglang/srt/models/glm4_moe.py`, `python/sglang/srt/models/llama.py`, `python/sglang/srt/models/llama_eagle.py`, `python/sglang/srt/models/llama_eagle3.py` _+5 more__
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

## CI / Build  (18 commits)

- **2026-05-25** [`7c04b9e942`](https://github.com/sgl-project/sglang/commit/7c04b9e942) [#26279](https://github.com/sgl-project/sglang/pull/26279)
  fix(docker): generate Cargo.lock in chef stage for sgl-router build (#26279)
  _Files: `docker/sgl-router.Dockerfile`_
- **2026-05-25** [`81704ad602`](https://github.com/sgl-project/sglang/commit/81704ad602) [#26273](https://github.com/sgl-project/sglang/pull/26273)
  ci: add nightly Docker workflow for experimental sgl-router (#26273)
  _Files: `.github/workflows/nightly-experimental-sgl-router-docker.yml`_
- **2026-05-22** [`d4082eab4d`](https://github.com/sgl-project/sglang/commit/d4082eab4d) [#26110](https://github.com/sgl-project/sglang/pull/26110)
  [CI] pr-test-extra: add run_all_tests to workflow_dispatch inputs (#26110)
  _Files: `.github/workflows/pr-test-extra.yml`_
- **2026-05-22** [`4486a339a3`](https://github.com/sgl-project/sglang/commit/4486a339a3) [#26074](https://github.com/sgl-project/sglang/pull/26074)
  [CI] bot-cherry-pick: remove concurrency group to enable batch dispatch (#26074)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-22** [`63ecf2f62b`](https://github.com/sgl-project/sglang/commit/63ecf2f62b) [#26067](https://github.com/sgl-project/sglang/pull/26067)
  [CI] Drop unused 'environment: prod' from bot-cherry-pick job (#26067)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-22** [`6339295556`](https://github.com/sgl-project/sglang/commit/6339295556) [#26053](https://github.com/sgl-project/sglang/pull/26053)
  [XPU] add apache-tvm-ffi dependency (#26053)
  _Files: `docker/xpu.Dockerfile`, `docs_new/docs/hardware-platforms/xpu.mdx`_
- **2026-05-22** [`7c02ca7882`](https://github.com/sgl-project/sglang/commit/7c02ca7882) [#26035](https://github.com/sgl-project/sglang/pull/26035)
  cancel pr ci: cover closed-no-merge; widen workflows; rerun-test opt-in (#26035)
  _Files: `.github/workflows/cancel-pr-workflow-on-merge.yml`, `.github/workflows/cancel-unfinished-pr-tests.yml`_
- **2026-05-21** [`049bb83134`](https://github.com/sgl-project/sglang/commit/049bb83134) [#26001](https://github.com/sgl-project/sglang/pull/26001)
  [CI] bot-cherry-pick: surface created PR number/URL in job summary (#26001)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-21** [`32352f7edf`](https://github.com/sgl-project/sglang/commit/32352f7edf) [#25987](https://github.com/sgl-project/sglang/pull/25987)
  [CI] Fix bot-cherry-pick: use state == "MERGED" instead of invalid `merged` field (#25987)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-21** [`64f21b1589`](https://github.com/sgl-project/sglang/commit/64f21b1589) [#25981](https://github.com/sgl-project/sglang/pull/25981)
  [CI] Improve bot-cherry-pick: accept PR number, require merged, explicit title (#25981)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-21** [`b5b9c809e1`](https://github.com/sgl-project/sglang/commit/b5b9c809e1) [#25947](https://github.com/sgl-project/sglang/pull/25947)
  fix(model-gateway): rustfmt nightly in conversations/handlers.rs (#25947)
  _Files: `sgl-model-gateway/src/routers/conversations/handlers.rs`_
- **2026-05-21** [`4868b92d47`](https://github.com/sgl-project/sglang/commit/4868b92d47) [#25926](https://github.com/sgl-project/sglang/pull/25926)
  [CI] Fix bot-cherry-pick auth: GITHUB_TOKEN for push, dedicated PAT for PR (#25926)
  _Files: `.github/workflows/bot-cherry-pick.yml`_
- **2026-05-20** [`eccd5c8253`](https://github.com/sgl-project/sglang/commit/eccd5c8253) [#25872](https://github.com/sgl-project/sglang/pull/25872)
  pr-test: schedule 3x -> 2x; fix extra gate skipped on schedule (#25872)
  _Files: `.github/workflows/pr-test-extra.yml`, `.github/workflows/pr-test.yml`_
- **2026-05-20** [`a1843524a5`](https://github.com/sgl-project/sglang/commit/a1843524a5) [#25854](https://github.com/sgl-project/sglang/pull/25854)
  ci(sgl-router): add PR test workflow (pre-positioned for feature PR) (#25854)
  _Files: `.github/workflows/pr-test-sgl-router.yml`_
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

## Speculative Decoding  (17 commits)

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
- **2026-05-21** [`c9a0e55eb5`](https://github.com/sgl-project/sglang/commit/c9a0e55eb5) [#25962](https://github.com/sgl-project/sglang/pull/25962)
  [Spec] Polish FutureMap after #25879: rename callback, async guard, cleanup (#25962)
  _Files: `python/sglang/srt/managers/overlap_utils.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-05-21** [`90efa9c83f`](https://github.com/sgl-project/sglang/commit/90efa9c83f) [#25932](https://github.com/sgl-project/sglang/pull/25932)
  [AMD] Fix AMD stage-a-test-small-1-gpu (#25932)
  _Files: `test/registered/core/test_basic_sanity_eagle3.py`_
- **2026-05-21** [`ddf3817924`](https://github.com/sgl-project/sglang/commit/ddf3817924) [#25917](https://github.com/sgl-project/sglang/pull/25917)
  Revert "[AMD]fix: use CUDA event for targeted draft-to-verify sync in… (#25917)
  _Files: `python/sglang/srt/speculative/eagle_worker_v2.py`, `python/sglang/srt/speculative/multi_layer_eagle_worker_v2.py`_
- **2026-05-21** [`c4a7d12092`](https://github.com/sgl-project/sglang/commit/c4a7d12092) [#25795](https://github.com/sgl-project/sglang/pull/25795)
  Enable breakable CUDA graph for eagle (#25795)
  _Files: `python/sglang/srt/model_executor/breakable_cuda_graph_runner.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/server_args.py`, `python/sglang/srt/speculative/eagle_utils.py` _+1 more__
- **2026-05-20** [`34d3e23232`](https://github.com/sgl-project/sglang/commit/34d3e23232) [#25818](https://github.com/sgl-project/sglang/pull/25818)
  spec_v2: consolidate seq_lens_cpu/sum maintenance into helper (#25818)
  _Files: `python/sglang/srt/managers/schedule_batch.py`, `python/sglang/srt/managers/scheduler.py`, `python/sglang/srt/model_executor/forward_batch_info.py`, `python/sglang/srt/speculative/eagle_info_v2.py`_
- **2026-05-20** [`1bd4f94598`](https://github.com/sgl-project/sglang/commit/1bd4f94598) [#25886](https://github.com/sgl-project/sglang/pull/25886)
  [Test] Add fwd_occupancy sanity kit (#25886)
  _Files: `python/sglang/test/kits/fwd_occupancy_kit.py`, `python/sglang/test/kits/hellaswag_kit.py`, `python/sglang/test/test_programs.py`, `test/registered/core/test_basic_sanity.py` _+1 more__
- **2026-05-20** [`52eebc82ae`](https://github.com/sgl-project/sglang/commit/52eebc82ae) [#25359](https://github.com/sgl-project/sglang/pull/25359)
  [Docs] MiMo-V2.5 cookbook: B200 benchmarks + multi-layer EAGLE acceptance profile + long-context reference (#25359)
  _Files: `docs_new/cookbook/autoregressive/Xiaomi/MiMo-V2.5.mdx`, `docs_new/src/snippets/autoregressive/mimo-v25-deployment.jsx`_
- **2026-05-20** [`0aedc5678b`](https://github.com/sgl-project/sglang/commit/0aedc5678b) [#25748](https://github.com/sgl-project/sglang/pull/25748)
  loader: yield filtered MTP weights lazily to avoid OOM hang on multi-layer EAGLE (#25748)
  _Files: `python/sglang/srt/model_loader/loader.py`_
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

## Other  (17 commits)

- **2026-05-25** [`de3f6fb02e`](https://github.com/sgl-project/sglang/commit/de3f6fb02e) [#25856](https://github.com/sgl-project/sglang/pull/25856)
  Fix attr err (#25856)
- **2026-05-24** [`030bd5d3ed`](https://github.com/sgl-project/sglang/commit/030bd5d3ed) [#26230](https://github.com/sgl-project/sglang/pull/26230)
  [Test] test_session_latency: assert streaming tail/head stability (#26230)
  _Files: `test/registered/sessions/test_session_latency.py`_
- **2026-05-23** [`982f67d9a6`](https://github.com/sgl-project/sglang/commit/982f67d9a6) [#26169](https://github.com/sgl-project/sglang/pull/26169)
  Suppress cutlass-dsl noisy warning (#26169)
  _Files: `python/sglang/srt/utils/common.py`_
- **2026-05-22** [`06836aa38a`](https://github.com/sgl-project/sglang/commit/06836aa38a) [#26060](https://github.com/sgl-project/sglang/pull/26060)
  update code owner (#26060)
  _Files: `.github/CODEOWNERS`_
- **2026-05-22** [`610f55040d`](https://github.com/sgl-project/sglang/commit/610f55040d) [#26042](https://github.com/sgl-project/sglang/pull/26042)
  update npu codeowners (#26042)
  _Files: `.github/CODEOWNERS`_
- **2026-05-22** [`76b1efaffd`](https://github.com/sgl-project/sglang/commit/76b1efaffd) [#26034](https://github.com/sgl-project/sglang/pull/26034)
  Fix SMG service discovery Clippy lint (#26034)
  _Files: `sgl-model-gateway/src/service_discovery.rs`_
- **2026-05-21** [`4ea8282cb7`](https://github.com/sgl-project/sglang/commit/4ea8282cb7) [#25938](https://github.com/sgl-project/sglang/pull/25938)
  [Revert] nvidia-cutlass-dsl[cu13] 4.5.1 -> 4.5.0 (#25938)
  _Files: `python/pyproject.toml`_
- **2026-05-21** [`a449ee4822`](https://github.com/sgl-project/sglang/commit/a449ee4822) [#25576](https://github.com/sgl-project/sglang/pull/25576)
  [Deps] Use cu13 extra for nvidia cutlass dsl (#25576)
  _Files: `python/pyproject.toml`_
- **2026-05-21** [`a528eb7564`](https://github.com/sgl-project/sglang/commit/a528eb7564) [#25927](https://github.com/sgl-project/sglang/pull/25927)
  fix: rustfmt service_discovery.rs warn! line length (#25927)
  _Files: `sgl-model-gateway/src/service_discovery.rs`_
- **2026-05-20** [`b7d0df4b6f`](https://github.com/sgl-project/sglang/commit/b7d0df4b6f) [#25294](https://github.com/sgl-project/sglang/pull/25294)
  [SMG] Support regular worker discovery alongside PD workers in IGW mode (#25294)
  _Files: `sgl-model-gateway/bindings/python/src/lib.rs`, `sgl-model-gateway/src/main.rs`, `sgl-model-gateway/src/service_discovery.rs`_
- **2026-05-20** [`5e7bf73757`](https://github.com/sgl-project/sglang/commit/5e7bf73757) [#25298](https://github.com/sgl-project/sglang/pull/25298)
  Fix bench_serving non-stream reasoning content (#25298)
  _Files: `python/sglang/bench_serving.py`, `test/registered/bench_fn/test_bench_serving_reasoning_stream.py`_
- **2026-05-20** [`61ac6792e6`](https://github.com/sgl-project/sglang/commit/61ac6792e6) [#25908](https://github.com/sgl-project/sglang/pull/25908)
  Add DevashishLal-CB to CI_PERMISSIONS.json (#25908)
  _Files: `.github/CI_PERMISSIONS.json`_
- **2026-05-20** [`0d3a94f643`](https://github.com/sgl-project/sglang/commit/0d3a94f643) [#25786](https://github.com/sgl-project/sglang/pull/25786)
  [Bug] Correct Weight Offloader's Attribute Name for torch.nn.Parameter (#25786)
  _Files: `python/sglang/srt/utils/offloader.py`_
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

## KV Cache / Memory  (15 commits)

- **2026-05-25** [`e86fdf3a3c`](https://github.com/sgl-project/sglang/commit/e86fdf3a3c) [#26177](https://github.com/sgl-project/sglang/pull/26177)
  [Bug Fix][HiCache] TreeNode.get_prefix_hash_values @lru_cache can return mutated list (#26177)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/radix_cache.py`, `test/registered/unit/mem_cache/test_radix_cache_unit.py`_
- **2026-05-25** [`821d5f4a5b`](https://github.com/sgl-project/sglang/commit/821d5f4a5b) [#25874](https://github.com/sgl-project/sglang/pull/25874)
  [CPU] add faster KV-cache writes (#25874)
  _Files: `docker/xeon.Dockerfile`, `python/sglang/srt/mem_cache/memory_pool.py`, `sgl-kernel/csrc/cpu/common.h`, `sgl-kernel/csrc/cpu/kvcache.cpp` _+2 more__
- **2026-05-24** [`44922de48a`](https://github.com/sgl-project/sglang/commit/44922de48a) [#26225](https://github.com/sgl-project/sglang/pull/26225)
  fix(swa): downgrade translate_loc_from_full_to_swa key-change log from warning to debug (#26225)
  _Files: `python/sglang/srt/mem_cache/swa_memory_pool.py`_
- **2026-05-24** [`36eb72bf12`](https://github.com/sgl-project/sglang/commit/36eb72bf12) [#25065](https://github.com/sgl-project/sglang/pull/25065)
  [UnifiedTree] fix: backup SWA-split parent before child under write-through (#25065)
  _Files: `python/sglang/srt/mem_cache/unified_radix_cache.py`, `test/registered/unit/mem_cache/test_unified_radix_cache_unittest.py`_
- **2026-05-22** [`c9153da5dc`](https://github.com/sgl-project/sglang/commit/c9153da5dc) [#25805](https://github.com/sgl-project/sglang/pull/25805)
  Fix SWA double-free in disagg decode with MTP speculation (#25805)
  _Files: `python/sglang/srt/mem_cache/swa_memory_pool.py`_
- **2026-05-21** [`888a8794ef`](https://github.com/sgl-project/sglang/commit/888a8794ef) [#25889](https://github.com/sgl-project/sglang/pull/25889)
  [Fix] DSV4 cached_loc invalidated when SWA mapping is rebuilt (#25889)
  _Files: `python/sglang/srt/mem_cache/deepseek_v4_memory_pool.py`, `test/manual/core/test_dsv4_cached_loc_invalidation.py`, `test/manual/core/test_dsv4_hicache_swa_translation_cache.py`, `test/manual/core/test_dsv4_stale_loc_crash.py`_
- **2026-05-20** [`371b6c9ea0`](https://github.com/sgl-project/sglang/commit/371b6c9ea0) [#25741](https://github.com/sgl-project/sglang/pull/25741)
  [Scheduler] fix chunked prefill not always being full (#25741)
  _Files: `python/sglang/srt/managers/schedule_policy.py`_
- **2026-05-20** [`33c57b8716`](https://github.com/sgl-project/sglang/commit/33c57b8716) [#25770](https://github.com/sgl-project/sglang/pull/25770)
  [Bug][RadixTree] Fix LRU list reference cycle leak in radix_cache (#25770)
  _Files: `python/sglang/srt/mem_cache/mamba_radix_cache.py`, `python/sglang/srt/mem_cache/swa_radix_cache.py`, `python/sglang/srt/mem_cache/unified_radix_cache.py`_
- **2026-05-20** [`6e0b7f35ad`](https://github.com/sgl-project/sglang/commit/6e0b7f35ad) [#25101](https://github.com/sgl-project/sglang/pull/25101)
  [radix cache] pluggable RadixCache factory (--radix-cache-backend) (#25101)
  _Files: `python/sglang/srt/mem_cache/kv_cache_builder.py`, `python/sglang/srt/mem_cache/registry.py`, `python/sglang/srt/server_args.py`, `test/registered/unit/mem_cache/test_registry.py`_
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

## Quantization  (14 commits)

- **2026-05-25** [`aae04b1241`](https://github.com/sgl-project/sglang/commit/aae04b1241) [#25904](https://github.com/sgl-project/sglang/pull/25904)
  :memo: docs(diffusion): add MXFP4 quantization docs (#25904)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_quantization.mdx`, `docs_new/docs/sglang-diffusion/quantization.mdx`_
- **2026-05-22** [`88a37d7405`](https://github.com/sgl-project/sglang/commit/88a37d7405) [#26057](https://github.com/sgl-project/sglang/pull/26057)
  [docs] DeepSeek-V4 cookbook: split Quantization axis, add H100 SGLang FP8 (#26057)
  _Files: `docs_new/cookbook/autoregressive/DeepSeek/DeepSeek-V4.mdx`, `docs_new/src/snippets/autoregressive/deepseek-v4-deployment.jsx`_
- **2026-05-21** [`1a85586738`](https://github.com/sgl-project/sglang/commit/1a85586738) [#25974](https://github.com/sgl-project/sglang/pull/25974)
  [Fix]: Restrict Kimi-K2.5 shared-experts fusion to Quark MXFP4 checkpoints (#25974)
  _Files: `python/sglang/srt/models/deepseek_v2.py`_
- **2026-05-20** [`ccbbae00ea`](https://github.com/sgl-project/sglang/commit/ccbbae00ea) [#25857](https://github.com/sgl-project/sglang/pull/25857)
  [codex] Reland Wan2.2 ModelOpt CI checkpoints (#25857)
  _Files: `docs_new/docs/sglang-diffusion/quantization.mdx`, `python/sglang/jit_kernel/tests/diffusion/test_diffusion_nvfp4_scaled_mm.py`, `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py` _+6 more__
- **2026-05-20** [`da6d549ab2`](https://github.com/sgl-project/sglang/commit/da6d549ab2) [#25814](https://github.com/sgl-project/sglang/pull/25814)
  Update GLM-5 H200 FP8 (#25814)
  _Files: `docs_new/cookbook/autoregressive/GLM/GLM-5.mdx`, `docs_new/src/snippets/autoregressive/glm-5-deployment.jsx`_
- **2026-05-20** [`b7085d3860`](https://github.com/sgl-project/sglang/commit/b7085d3860) [#25532](https://github.com/sgl-project/sglang/pull/25532)
  [fp8] SM90 swap-AB scaled_mm dispatch (~1.16x kernel geomean, +5.8-18.5% end-to-end) (#25532)
  _Files: `sgl-kernel/benchmark/bench_fp8_gemm_swap_ab.py`, `sgl-kernel/csrc/cutlass_extensions/epilogue/broadcast_load_epilogue_c3x.hpp`, `sgl-kernel/csrc/cutlass_extensions/epilogue/scaled_mm_epilogues_c3x.hpp`, `sgl-kernel/csrc/cutlass_extensions/gemm/fp8_gemm_sm90_dispatch.cuh` _+2 more__
- **2026-05-20** [`a4b51d35ef`](https://github.com/sgl-project/sglang/commit/a4b51d35ef) [#25845](https://github.com/sgl-project/sglang/pull/25845)
  Revert "[codex] Update Wan2.2 ModelOpt CI checkpoints" (#25845)
  _Files: `docs_new/docs/sglang-diffusion/quantization.mdx`, `python/sglang/multimodal_gen/registry.py`, `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`, `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py` _+5 more__
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

## Triton / Kernels  (11 commits)

- **2026-05-24** [`fd94bd30b8`](https://github.com/sgl-project/sglang/commit/fd94bd30b8) [#26118](https://github.com/sgl-project/sglang/pull/26118)
  [Intel GPU] DeepSeek V4 2/N: Fix tvm ffi import (#26118)
  _Files: `python/sglang/jit_kernel/dsv4/compress.py`_
- **2026-05-22** [`acb8310183`](https://github.com/sgl-project/sglang/commit/acb8310183) [#26037](https://github.com/sgl-project/sglang/pull/26037)
  ci: self-heal $GITHUB_PATH/$GITHUB_ENV writes (#26037)
  _Files: `scripts/ci/cuda/ci_install_dependency.sh`, `scripts/ci/utils/install_rustup.sh`_
- **2026-05-21** [`caa9f08294`](https://github.com/sgl-project/sglang/commit/caa9f08294) [#25958](https://github.com/sgl-project/sglang/pull/25958)
  [CI] Force-reinstall nvidia-cutlass-dsl-libs-cu13 last to avoid wheel-mix TypeError (#25958)
  _Files: `python/pyproject.toml`, `scripts/ci/cuda/ci_install_dependency.sh`_
- **2026-05-21** [`34479c19bd`](https://github.com/sgl-project/sglang/commit/34479c19bd) [#25730](https://github.com/sgl-project/sglang/pull/25730)
  [XPU] upgrade triton-xpu version to 3.7.1 (#25730)
  _Files: `docker/xpu.Dockerfile`, `docs_new/docs/hardware-platforms/xpu.mdx`_
- **2026-05-20** [`ce7141ef98`](https://github.com/sgl-project/sglang/commit/ce7141ef98) [#25860](https://github.com/sgl-project/sglang/pull/25860)
  add git gemm warpper for dispatch_bf16_fp32_backend (#25860)
  _Files: `python/sglang/jit_kernel/deepseek_v4.py`_
- **2026-05-20** [`55ba03db6a`](https://github.com/sgl-project/sglang/commit/55ba03db6a) [#23925](https://github.com/sgl-project/sglang/pull/23925)
  [NPU]use triton split_qkvgate_gemma_rmsnorm_rope for Qwen3.5 and Qwen3_next (#23925)
  _Files: `python/sglang/srt/layers/rotary_embedding/mrope.py`, `python/sglang/srt/models/qwen3_5.py`, `python/sglang/srt/models/qwen3_next.py`_
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

## Models  (10 commits)

- **2026-05-23** [`8c78424701`](https://github.com/sgl-project/sglang/commit/8c78424701) [#26033](https://github.com/sgl-project/sglang/pull/26033)
  Reduce excessively long logs caused by transformer version updates. (#26033)
  _Files: `test/registered/ascend/basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_480b.py`_
- **2026-05-23** [`c69844f043`](https://github.com/sgl-project/sglang/commit/c69844f043) [#26069](https://github.com/sgl-project/sglang/pull/26069)
  [NPU]Ascend NPU Performance Profiling Guide and Ascend NPU Operator Development Guide (#26069)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_qwen3_5_examples.mdx`_
- **2026-05-22** [`80680dc3fe`](https://github.com/sgl-project/sglang/commit/80680dc3fe) [#25128](https://github.com/sgl-project/sglang/pull/25128)
  [Intel GPU] 1/N Fix tilelang import in deepseek v4 rope as optional (#25128)
  _Files: `python/sglang/srt/layers/deepseek_v4_rope.py`_
- **2026-05-21** [`b9ae8353d2`](https://github.com/sgl-project/sglang/commit/b9ae8353d2) [#25257](https://github.com/sgl-project/sglang/pull/25257)
  [NPU] Support model DeepSeek-OCR and DeepSeek-OCR-2 (#25257)
  _Files: `python/sglang/srt/models/deepseek.py`_
- **2026-05-21** [`3a6de13cd8`](https://github.com/sgl-project/sglang/commit/3a6de13cd8) [#25810](https://github.com/sgl-project/sglang/pull/25810)
  perf(dsv4): add MHC token-count prewarm (#25810)
  _Files: `python/sglang/srt/layers/mhc.py`, `python/sglang/srt/model_executor/model_runner.py`, `python/sglang/srt/models/deepseek_v4.py`, `python/sglang/srt/models/deepseek_v4_nextn.py`_
- **2026-05-21** [`e603beab55`](https://github.com/sgl-project/sglang/commit/e603beab55) [#25594](https://github.com/sgl-project/sglang/pull/25594)
  [NPU] Add Qwen3.5-397B-A17B best practice doc (#25594)
  _Files: `docs/platforms/ascend/ascend_npu_best_practice.md`_
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

## Tensor / Data Parallel  (9 commits)

- **2026-05-25** [`6e8fe176be`](https://github.com/sgl-project/sglang/commit/6e8fe176be) [#25851](https://github.com/sgl-project/sglang/pull/25851)
  sgl-router: experimental Rust HTTP router for SGLang worker pools (#25851)
- **2026-05-24** [`85471d253d`](https://github.com/sgl-project/sglang/commit/85471d253d) [#26047](https://github.com/sgl-project/sglang/pull/26047)
  Add --disable-attn-tp-gather opt-out for model-managed SP (#26047)
  _Files: `python/sglang/srt/server_args.py`, `python/sglang/srt/utils/common.py`_
- **2026-05-23** [`89ff2bc111`](https://github.com/sgl-project/sglang/commit/89ff2bc111) [#26026](https://github.com/sgl-project/sglang/pull/26026)
  [bug fix] Fix 3 issues when using Gemma4 MTP (#26026)
  _Files: `python/sglang/srt/models/gemma4_causal.py`, `python/sglang/srt/models/gemma4_mtp.py`, `python/sglang/srt/server_args.py`_
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

## Docs / Examples  (6 commits)

- **2026-05-25** [`a4db563c87`](https://github.com/sgl-project/sglang/commit/a4db563c87) [#26249](https://github.com/sgl-project/sglang/pull/26249)
  [hisparse]: update user guide (#26249)
  _Files: `docs/advanced_features/hisparse_guide.md`, `docs_new/docs/advanced_features/hisparse_guide.mdx`_
- **2026-05-22** [`b2631a9a4d`](https://github.com/sgl-project/sglang/commit/b2631a9a4d) [#25830](https://github.com/sgl-project/sglang/pull/25830)
  [NPU] Docs op performance optimize (#25830)
  _Files: `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_performance_optimizing.mdx`_
- **2026-05-21** [`ac83d8a339`](https://github.com/sgl-project/sglang/commit/ac83d8a339) [#25995](https://github.com/sgl-project/sglang/pull/25995)
  docs: delete deprecated args from npu supported features (#25995)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_support_features.mdx`_
- **2026-05-21** [`2e0d2d4c18`](https://github.com/sgl-project/sglang/commit/2e0d2d4c18) [#25875](https://github.com/sgl-project/sglang/pull/25875)
  [NPU][DOCS]Add best practice and benchmark result parameter description (#25875)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_best_practice.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_performance_testing.mdx`_
- **2026-05-21** [`f66881f03c`](https://github.com/sgl-project/sglang/commit/f66881f03c) [#25384](https://github.com/sgl-project/sglang/pull/25384)
  [NPU]Ascend NPU Performance Profiling Guide and Ascend NPU Operator Development Guide (#25384)
  _Files: `.codespellrc`, `docs_new/docs.json`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_operator_development.mdx`, `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_profiling.mdx`_
- **2026-05-19** [`d028697d17`](https://github.com/sgl-project/sglang/commit/d028697d17) [#25269](https://github.com/sgl-project/sglang/pull/25269)
  [NPU][Docs] Add Kimi-K2.5-W4A8 instance doc on NPU (#25269)
  _Files: `docs_new/docs/hardware-platforms/ascend-npus/ascend_npu_kimi_k2.5_examples.mdx`_

## ROCm / AMD  (5 commits)

- **2026-05-21** [`8562d5ae94`](https://github.com/sgl-project/sglang/commit/8562d5ae94) [#25978](https://github.com/sgl-project/sglang/pull/25978)
  [AMD] Relaxing Timeout for AMD stage-a (#25978)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`_
- **2026-05-21** [`e72e3145a0`](https://github.com/sgl-project/sglang/commit/e72e3145a0) [#25896](https://github.com/sgl-project/sglang/pull/25896)
  [AMD] Upgrade AITER (#25896)
  _Files: `docker/rocm.Dockerfile`_
- **2026-05-21** [`1b3d8da827`](https://github.com/sgl-project/sglang/commit/1b3d8da827) [#25965](https://github.com/sgl-project/sglang/pull/25965)
  cap API quota for runner-utilization / amd-ci-job-monitor (#25965)
  _Files: `.github/workflows/amd-ci-job-monitor.yml`, `.github/workflows/runner-utilization.yml`, `scripts/ci/utils/query_job_status.py`, `scripts/ci/utils/runner_utilization_report.py`_
- **2026-05-18** [`54eb2904a4`](https://github.com/sgl-project/sglang/commit/54eb2904a4) [#25178](https://github.com/sgl-project/sglang/pull/25178)
  minor: docs include mac installation (#25178)
  _Files: `docs_new/docs/get-started/install.mdx`, `docs_new/docs/hardware-platforms/amd_gpu.mdx`_
- **2026-05-18** [`7adb37bb52`](https://github.com/sgl-project/sglang/commit/7adb37bb52) [#25301](https://github.com/sgl-project/sglang/pull/25301)
  [AMD] fix moriep unittest oom on mi300x ci (#25301)
  _Files: `.github/workflows/pr-test-amd-rocm720.yml`, `.github/workflows/pr-test-amd.yml`, `test/registered/amd/test_moriep_small.py`_

## Serving / API  (3 commits)

- **2026-05-22** [`5e9bd21979`](https://github.com/sgl-project/sglang/commit/5e9bd21979) [#20700](https://github.com/sgl-project/sglang/pull/20700)
  fix(serving_chat): catch TypeError from tojson on Jinja2 Undefined variables (#20700)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`_
- **2026-05-22** [`f829cafa3e`](https://github.com/sgl-project/sglang/commit/f829cafa3e) [#25953](https://github.com/sgl-project/sglang/pull/25953)
  [perf] skip add_special_tokens=False kwarg on chat-template tokenize for slow tokenizers (#25953)
  _Files: `python/sglang/srt/entrypoints/openai/serving_chat.py`_
- **2026-05-19** [`1d19721394`](https://github.com/sgl-project/sglang/commit/1d19721394) [#23506](https://github.com/sgl-project/sglang/pull/23506)
  [gRPC] Native server: Rust crate (1/N) (#23506)
  _Files: `rust/sglang-grpc/Cargo.toml`, `rust/sglang-grpc/src/bridge.rs`, `rust/sglang-grpc/src/bridge/tests.rs`, `rust/sglang-grpc/src/lib.rs` _+7 more__

## LoRA  (2 commits)

- **2026-05-25** [`87e69d57c4`](https://github.com/sgl-project/sglang/commit/87e69d57c4) [#25413](https://github.com/sgl-project/sglang/pull/25413)
  [lora] Fix overlap loading for cancelled requests (#25413)
  _Files: `python/sglang/srt/lora/lora_overlap_loader.py`, `test/registered/lora/test_lora_overlap_loading.py`_
- **2026-05-21** [`cf1fd26d16`](https://github.com/sgl-project/sglang/commit/cf1fd26d16) [#25363](https://github.com/sgl-project/sglang/pull/25363)
  benchmark/lora: make number of LoRA adapters configurable (#25363)
  _Files: `benchmark/lora/launch_server.py`, `benchmark/lora/lora_bench.py`_

## Structured Output  (2 commits)

- **2026-05-22** [`6baa859a86`](https://github.com/sgl-project/sglang/commit/6baa859a86) [#25600](https://github.com/sgl-project/sglang/pull/25600)
  Add MiniCPM5 tool call parser for XML-style function calls (#25600)
  _Files: `python/sglang/srt/function_call/function_call_parser.py`, `python/sglang/srt/function_call/minicpm5_detector.py`, `python/sglang/srt/managers/template_detection.py`, `test/registered/unit/function_call/test_minicpm5_detector.py` _+1 more__
- **2026-05-20** [`dac78768f0`](https://github.com/sgl-project/sglang/commit/dac78768f0) [#24251](https://github.com/sgl-project/sglang/pull/24251)
  [RL][TITO] Preserve whitespace in reasoning parser outputs (#24251)
  _Files: `python/sglang/srt/function_call/deepseekv32_detector.py`, `python/sglang/srt/parser/reasoning_parser.py`, `test/registered/unit/entrypoints/openai/test_serving_chat.py`, `test/registered/unit/parser/test_reasoning_parser.py`_

---
_Generated 2026-05-25 12:00 UTC_