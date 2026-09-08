---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 160 items, 3 important content pieces were selected

---

**Technology News**
1. [LLM-Guided Evolution Improves Circle-Packing Solutions on Packomania](#item-tech-news-1) ⭐️ 9.0/10
2. [InferenceX Externalizes Google TPU Inference Stack](#item-tech-news-2) ⭐️ 8.0/10
3. [KV Cache as an Agent Runtime for Interactive LLMs](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [LLM-Guided Evolution Improves Circle-Packing Solutions on Packomania](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 9.0/10



reddit · r/MachineLearning · /u/SIGH\_I\_CALL · Sep 7, 16:54

#### Summary

An LLM-driven algorithm evolution loop improved the best-known sum-of-radii for circle packing with N=101–114 on the Packomania benchmark by 2.4–5.4%, verified independently and published on arxiv \(2609.05093\). Starting from a simple seed solver, the LLM proposes algorithmic changes guided by a scoreboard of results and a history of prior attempts; each candidate is scored by an independent verifier, keeping improvements and discarding failures. The process completed in 15 iterations at a total LLM cost of $27.72, with Packomania accepting the results as new benchmarks. This demonstrates a novel approach to automated optimization algorithm design, yielding externally validated improvements on a classic mathematical packing problem.

#### Background

Circle packing is a classical optimization problem that seeks the largest possible non-overlapping arrangement of equal circles within a unit square for a given number of copies. Packomania maintains a curated repository of best-known solutions for this and related packing problems, serving as a standard benchmark for algorithm development. Improving known solutions for N=101–114 represents incremental progress in a long-standing research area where even small percentage gains are significant.

**Tags**: `#artificial intelligence`, `#optimization`, `#research`, `#algorithms`, `#machine learning`

---

<a id="item-tech-news-2"></a>
### [InferenceX Externalizes Google TPU Inference Stack](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

InferenceX is rapidly externalizing Google&\#x27;s TPU inference infrastructure, claiming significant cost-performance gains and growing adoption as companies seek alternatives to CUDA-dependent GPU stacks.

rss · Semianalysis · Sep 7, 20:00

#### Summary

InferenceX is making Google&\#x27;s TPU inference stack available as an external service, positioning it as a cost-effective alternative to NVIDIA GPU-based inference. The company claims up to 50% better performance per dollar compared to CUDA-dependent solutions, addressing growing industry pressure to reduce single-vendor lock-in. Adoption is expanding rapidly with a growing customer base seeking to diversify beyond NVIDIA&\#x27;s ecosystem. The initiative aligns with broader efforts to externalize specialized AI hardware stacks like Ironwood and TPUv8i, potentially weakening CUDA&\#x27;s competitive moat in the inference market.

#### Background

Google&\#x27;s Tensor Processing Unit \(TPU\) is a family of custom AI accelerators designed by Google specifically for machine learning workloads, used extensively in its own services and made available via Google Cloud. NVIDIA&\#x27;s CUDA platform has created a deep software ecosystem lock-in around its GPUs, often described as a &quot;moat,&quot; because most AI frameworks and tools are optimized for CUDA-first. InferenceX \(launched in October 2025 under the name InferenceMAX\) is an open-source benchmark that continuously measures large language model inference performance across different AI accelerators and serving software, providing vendor-neutral performance comparisons.

<details><summary>References</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/inferencex">InferenceX | AI Wiki</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#TPU`, `#GPU ecosystems`, `#CUDA`

---

<a id="item-tech-news-3"></a>
### [KV Cache as an Agent Runtime for Interactive LLMs](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

Yandex-affiliated researchers propose manipulating KV-cache inference state as a new axis for building more interactive LLM agents, with a preview of Qwen3.8-27B playing DOOM.

reddit · r/MachineLearning · /u/\_puhsu · Sep 7, 09:03

#### Summary

Researchers from a Yandex-affiliated team are exploring KV-cache manipulation as a novel approach to improve LLM interactivity and responsiveness. The idea builds on their prior published papers on Hogwild\! Inference and AsyncReasoning. They demonstrated a preview where a Qwen3.8-27B agent plays the DOOM environment interactively using these techniques. The core insight is that model inference/runtime design represents an under-explored axis of agent capability—situated between the extremes of abstract harness engineering \(too high-level\) and full model retraining \(too costly\). This suggests there may be practical middle-ground optimizations available through direct manipulation of the inference state.

#### Background

KV-cache \(key-value cache\) is a standard optimization in transformer inference that stores computed key and value states to avoid redundant calculations during autoregressive generation. Hogwild\! Inference and AsyncReasoning are prior works by this research group exploring parallel and asynchronous inference patterns. The DOOM environment is a popular benchmark for AI agents, testing real-time decision-making in a first-person shooter setting.

**Tags**: `#LLM inference optimization`, `#AI agents`, `#model runtime engineering`, `#KV-cache manipulation`, `#machine learning research`

---