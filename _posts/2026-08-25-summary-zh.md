---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 201 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [OpenAI 自研推理芯片 Jalapeño 测试数据公布](#item-tech-news-1) ⭐️ 8.0/10
2. [持续学习开源模型实现前沿 AI 性能，降低对大机构的依赖](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 自研推理芯片 Jalapeño 测试数据公布](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 8.0/10



hackernews · Semianalysis · 8月25日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

#### 摘要

OpenAI 公布了首款自研推理芯片 Jalapeño 的首批测试数据，该芯片由 OpenAI 与博通合作开发。在 GPT-OSS 120B、DeepSeek R1 670B 和 Kimi K2.5 1T 三款模型上，Jalapeño 的单位功耗 AI 吞吐量达到对比系统（英伟达 GB300）的 1.5 至 1.9 倍，端到端延迟低 1.7 至 3.6 倍，高交互场景性能高出 2.1 至 4.1 倍。芯片额定功耗 700 瓦，实测持续功耗不超过 550 瓦。OpenAI 计划今年年底前在自有算力设施中部署该芯片，第二代已深入开发中，第三代正在设计，但不用于模型训练，也未与英伟达新一代 Vera Rubin 进行比较。

#### 关于 OpenAI Jalapeño 芯片的背景

Jalapeño 是 OpenAI 首款自研推理专用 ASIC 芯片，与博通合作开发，采用台积电 3nm 工艺制造，配备 systolic array 架构和八个 HBM 堆栈。芯片额定功耗 700 瓦，从设计启动到流片仅耗时九个月，是业内最快的高端先进制程 ASIC 开发周期之一。其设计目标是在推理场景下将每 token 成本降低约 50%，主要对标英伟达 Blackwell/GB300 产品，但未与新一代 Vera Rubin 进行比较，也不用于模型训练，专注于大规模语言模型推理工作负载。

#### 社区讨论

社区普遍认为各大 AI 实验室自建定制硅片是行业趋势，有用户以 GPT-Sol 烘焙进芯片为例，认为规模化后专用芯片的经济回报可观。部分讨论将当前推理芯片竞争类比为早年 3dfx/Riva 显卡时代，关注市场最终会形成寡头还是持续分散。另有观点指出，DeepSeek 和 Kimi 成为各家芯片基准测试的共同参照，反映出行业对开源/开放模型生态的依赖正在加深。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks">OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — claims up to 1.9x throughput per kilowatt and 3.6x lower latency, co-developed with Broadcom | Tom&#x27;s Hardware</a></li>
<li><a href="https://geniustechlab.com/posts/2026-06-26-openai-jalapeno-custom-inference-chip">OpenAI&#x27;s Jalapeño Chip: Why Custom Silicon Changes the ...</a></li>
<li><a href="https://pinggy.io/blog/openai_jalapeno_custom_inference_chip/">OpenAI&#x27;s Jalapeño: What a Custom AI Inference Chip Actually ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#custom ASIC`, `#OpenAI`, `#GPU industry`, `#inference chips`

---

<a id="item-tech-news-2"></a>
### [持续学习开源模型实现前沿 AI 性能，降低对大机构的依赖](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/Forsaken\_Scientist · 8月25日 10:30

#### 摘要

一项名为 Thomson 的新模型通过持续学习（Continual Learning）技术，在公开的开源权重模型上实现了接近前沿水平的 AI 性能。该技术报告及开放权重模型的发布方指出，当前前沿模型开发被少数资金雄厚的机构垄断，造成了信息、经济和权力上的不对称。Thomson 采用现代中期与后期训练栈，同时在每个训练阶段引入 safeguards 以兼顾可塑性（plasticity）和稳定性（stability），并以最小的高影响干预修改模型参数。评估结果显示出独特的π形模式：在代理任务、安全性、法律、税务、多语言及大规模深度研究等多个领域具有竞争力，同时几乎完全消除了常见的遗忘问题。该方法所需的算力和人力预算远低于普遍认为的水平，为更广泛的行为者实现 SovereignAI（独立构建、部署和治理 AI 的能力）提供了可行路径。

#### 背景

Continual learning refers to the ability of a model to incrementally acquire new knowledge and skills over time without forgetting previously learned information—a core challenge in machine learning known as catastrophic forgetting. In the context of large language models, it involves updating pre-trained open-weight models with new data or tasks while preserving their existing capabilities. The Thomson model builds on prior checkpoints such as Snowdon-1.1-Small, which serves as a value-realigned starting point before mid-training begins.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tri-fair-lab/Thomson-1.0-Small">tri-fair-lab/Thomson-1.0-Small · Hugging Face</a></li>

</ul>
</details>

**标签**: `#continual learning`, `#open-weight models`, `#SovereignAI`, `#model access`, `#machine learning`

---