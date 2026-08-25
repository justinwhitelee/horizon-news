---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 201 items, 2 important content pieces were selected

---

**Technology News**
1. [OpenAI&\#x27;s Custom Inference Chip Jalapeño Reports Outperforming Nvidia Blackwell](#item-tech-news-1) ⭐️ 8.0/10
2. [Open-weights model Thomson shows continual learning can reach frontier performance](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI&\#x27;s Custom Inference Chip Jalapeño Reports Outperforming Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 8.0/10



hackernews · Semianalysis · Aug 25, 14:06 · [Discussion](https://news.ycombinator.com/item?id=49434378)

#### Summary

OpenAI has released initial test data for Jalapeño, its first self-designed inference ASIC developed in partnership with Broadcom, claiming it outperforms Nvidia&\#x27;s current offerings. In benchmarks using GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T models, Jalapeño delivered 1.5× to 1.9× more AI work per watt and 1.7× to 3.6× lower end-to-end latency compared to the Nvidia GB300 at peak throughput, with high-interaction scene performance 2.1× to 4.1× higher. The chip is rated at 700 watts but实测持续功耗不超过550瓦 \(measured sustained power draw does not exceed 550W\). OpenAI plans to deploy Jalapeño in its own compute infrastructure by the end of 2026, with a second generation already in deep development and a third in design. Notably, the chip was benchmarked against the GB300 rather than Nvidia&\#x27;s newer Vera Rubin platform, and it is designed exclusively for inference, not model training.

#### Background

An ASIC \(application-specific integrated circuit\) is a chip designed for a particular use rather than a general-purpose GPU, which can handle many types of computational workloads. Nvidia&\#x27;s Blackwell architecture \(exemplified by the GB300\) has been the dominant hardware for AI inference and training, while its next-generation Vera Rubin platform is slated for late-2026 deployment. Custom inference ASICs target lower cost per token and higher energy efficiency for running large language models, prompting major AI labs like OpenAI and Anthropic to explore in-house silicon as their inference scale grows.

#### Community Discussion

Commenters debated whether OpenAI should eventually bake specific LLM weights directly into custom silicon—as Anthropic and OpenAI now operate at scales where a chip running GPT Sol could cost $100M while being 10× faster and cheaper, potentially paying for itself if the chip remains relevant for two or more years. Others drew parallels to the early 3dfx/Riva/Mach/PowerVR era, questioning whether inference-specific chips will endure and who the dominant players will be. Several noted that industry reliance on DeepSeek and Kimi benchmarks signals a broader shift, while one observed that human speech remains 22× more energy-efficient than current AI hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://geniustechlab.com/posts/2026-06-26-openai-jalapeno-custom-inference-chip">OpenAI&#x27;s Jalapeño Chip: Why Custom Silicon Changes the ...</a></li>
<li><a href="https://siliconanalysts.com/analysis/inference-chip-economics-openai-vs-nvidia-vs-amd-2026-2">Inference Wars: Cost-Per-Token Is the New Metric</a></li>

</ul>
</details>

**Tags**: `#AI hardware`, `#custom ASIC`, `#OpenAI`, `#GPU industry`, `#inference chips`

---

<a id="item-tech-news-2"></a>
### [Open-weights model Thomson shows continual learning can reach frontier performance](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/Forsaken\_Scientist · Aug 25, 10:30

#### Summary

A new technical report and open-weights release from tri-fair-lab argues that frontier-level AI performance is achievable through continual learning on readily available open-weight models, rather than requiring the massive compute budgets associated with frontier labs. The researchers introduced Thomson, a general-purpose frontier model trained with enhanced focus on high-stakes professional domains such as legal, tax, multilingualism, agentic tasks, and large-scale Deep Research. Their continual learning approach leverages a modern mid- and post-training stack while introducing safeguards that preserve both plasticity and stability at each training stage, making only minimal high-impact parameter interventions. Evaluations showed a distinctive π-shaped pattern: distinct improvements across a wide range of capabilities, including those not explicitly targeted, while almost completely eliminating the forgetting problem common in narrow domain adaptation. The results suggest that ownership of key parts of the SovereignAI stack—model, tool infrastructure, values, and data privacy—becomes viable for institutions with substantially lower compute and personnel budgets than is commonly assumed.

#### Background

Continual learning refers to training AI models on new data over time without forgetting previously learned capabilities, addressing a key challenge where models tend to degrade on earlier knowledge after learning new tasks. Open-weight models are pre-trained models whose internal parameters are publicly available for modification, distinct from fully open-source models that also release training data and code. SovereignAI describes an organization&\#x27;s ability to independently build, deploy, and govern its own AI systems rather than relying exclusively on a small number of well-funded external providers.

**Tags**: `#continual learning`, `#open-weight models`, `#SovereignAI`, `#model access`, `#machine learning`

---