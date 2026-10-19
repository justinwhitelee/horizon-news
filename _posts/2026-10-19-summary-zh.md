---
layout: default
title: "Horizon Summary: 2026-10-19 (ZH)"
date: 2026-10-19
lang: zh
---

> 从 147 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [vLLM v0.32.0：低精度 KV 缓存、结构化输出与 MRV2 默认化](#item-tech-news-1) ⭐️ 8.0/10
2. [TempoPFN：基于合成预训练线性 RNN 的零样本时序预测](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.32.0：低精度 KV 缓存、结构化输出与 MRV2 默认化](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 8.0/10



github · khluu · 10月18日 06:50

#### 摘要

vLLM 发布了 v0.32.0 版本，包含来自 363 位贡献者的 814 次提交。该版本的核心改进包括将 NVFP4 和 GLM-5.x FP8 低精度 KV 缓存扩展至 SM8x/SM9x/SM10x/SM12x 多代 GPU 架构，其中 GLM-5.x 在 SM100 上默认启用 FP8 KV 缓存，每 rank 内存减半，吞吐提升 2.3-5.5%。新增 \`POST /v1/systemone\` 结构化决策端点和基于 checkpoint \`response\_template\` 的通用 HF 解析器，减少对模型专属解析器的依赖。Model Runner V2（MRV2）现在成为 ROCm 的默认后端，同时支持 GPU n-gram 推测解码、弹性专家并行和 MLA 模型的流水线并行。

#### 背景

vLLM 是一个广泛使用的开源大语言模型推理服务框架，以 PagedAttention 和高效的 KV 缓存管理著称。低精度 KV 缓存通过降低键值对的存储精度来减少显存占用，从而在不显著牺牲生成质量的前提下提升吞吐量。MRV2 是 vLLM 的新一代模型运行器，引入推测解码、弹性并行等优化机制。

**标签**: `#LLM serving`, `#vLLM`, `#low-precision compute`, `#structured output`, `#GPU optimization`

---

<a id="item-tech-news-2"></a>
### [TempoPFN：基于合成预训练线性 RNN 的零样本时序预测](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 8.0/10

NeurIPS 2026 接收论文 TempoPFN，提出通过合成时序数据预训练 DeltaProduct 线性 RNN，实现零样本预测。

reddit · r/MachineLearning · /u/Yossarian\_1234 · 10月18日 16:43

#### 摘要

TempoPFN 是 NeurIPS 2026 接收的一项工作，由 Vladyslav Moroshan、Julien Siems、Arber Zela 等人提出。该框架利用一组合成的时序生成器和数据增强方法，对基于 DeltaProduct 的线性 RNN 进行预训练，从而实现零样本时序预测。合成数据已被用于 Toto-2 和 TS-ICL 项目中，验证了其有效性。该项目开源了代码（GitHub: automl/TempoPFN）及模型（Hugging Face: AutoML-org/TempoPFN），便于社区复现与扩展。

**标签**: `#machine learning`, `#time series`, `#foundation models`, `#neural networks`, `#open source`

---