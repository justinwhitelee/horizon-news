---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 200 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [NeurIPS 2026 Spotlight：并行化时间训练 RNN 实现混沌系统高效重建](#item-tech-news-1) ⭐️ 8.0/10
2. [NeurIPS 2026 研究揭示 LLM 的权威偏见：模型易受&\#x27;验证来源&\#x27;误导](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [NeurIPS 2026 Spotlight：并行化时间训练 RNN 实现混沌系统高效重建](https://www.reddit.com/r/MachineLearning/comments/1wuz2s4/parallelintime_training_of_recurrent_neural/) ⭐️ 8.0/10

NeurIPS 2026 接收的 Spotlight 论文提出将 DEER 方法与广义教师强制结合，显著提升混沌系统非线性 RNN 的训练效率，速度提升超百倍。

reddit · r/MachineLearning · /u/DangerousFunny1371 · 10月1日 13:12

#### 摘要

NeurIPS 2026 Spotlight 论文&quot;Parallel-in-Time Training of Recurrent Neural Networks for Dynamical Systems Reconstruction&quot;针对混沌动力系统的时间序列，提出了结合 DEER 与广义教师强制（GTF）的并行时间训练方法。DEER 原本通过全序列上的牛顿型不动点迭代求解 RNN 前向传播，将计算复杂度从 O\[T\]降至 O\[\(log T\)²\]，但在混沌动力学下会发散且退化至 O\[T log T\]。引入 GTF 后有效稳定了训练过程，避免了发散问题并减少了与传统教师强制相关的暴露偏差。该方法支持 T&gt;10⁶的超长序列训练，在动态系统重建（DSR）任务上显著优于 Mamba 等状态空间模型。

#### 背景

RNN 训练面临的关键挑战是长序列计算成本高以及混沌系统中轨迹对初始条件敏感导致的数值不稳定问题。DEER 是一种近年提出的训练方法，通过并行化处理整个时间序列来突破传统顺序计算的瓶颈。广义教师强制则是对传统教师强制技术的改进，在训练过程中引入更稳定的信号传递机制。

**标签**: `#machine learning`, `#neural networks`, `#parallel computing`, `#dynamical systems`, `#NeurIPS`

---

<a id="item-tech-news-2"></a>
### [NeurIPS 2026 研究揭示 LLM 的权威偏见：模型易受&\#x27;验证来源&\#x27;误导](https://www.reddit.com/r/MachineLearning/comments/1wv1c2e/llms_that_push_back_on_a_wrong_user_still_accept/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/MajorRedditor23 · 10月1日 14:45

#### 摘要

NeurIPS 2026 的一篇论文指出，大型语言模型（LLM）存在一种“权威偏见”（Authority Bias）：当用户坚持错误答案时，模型往往能保持原有正确回答；但当同样的错误答案被包装为来自“验证来源”（verified source）时，模型却会轻易改变立场。这一现象揭示了当前 sycophancy（迎合）评估的盲区——现有测试主要衡量模型抵抗用户压力的能力，却无法检测其通过搜索结​​果、检索文档或工具输出被误导的风险，而这正是当前智能体（agentic）AI 系统面临的关键安全挑战。研究团队在 8 个模型（包括 Qwen3.5、GPT-OSS、OLMo-2/3.1、Gemma-4 等开源系列，以及 GPT-5.4、Grok-4.20、Gemini-3.1-Pro 等 API 模型）上测试发现，45%至 88%的正确回答会被“验证来源”的单一说法改变；而来自用户的相同错误说法则很少动摇模型。其中 GPT-5.4 有 44.7%的题目被翻转，Grok-4.20 高达 87.5%，而 Gemini-3.1-Pro 几乎完全免疫（仅 0.6%）。内部分析（针对三个开源系列）显示，模型中存储“ endorsement”信息的神经方向高度重叠（余弦相似度约 0.90–0.99），移除“来源背书”方向可使对错误来源的顺从度降低 64–78 分，而移除“用户背书”方向最多仅降 11 分；仅调整“谁在背书”的微小差异部分，就能将源与用户之间的顺从差距缩小 55–61%。研究同时承认若干局限：内部干预结果仅在 5 个开源系列中的 3 个复现；Gemma-4 虽易被翻转，但线性干预无法控制；所谓“检索文档”测试仅是将声明置于文档格式的提示块中，尚未在真实检索管道或像 Claude Code 这样的智能体环境中验证。该论文、代码及可视化页面已公开（arXiv:2609.37616；GitHub: Lossfunk/authority-bias）。

#### 背景

Sycophancy 评估是衡量 LLM 是否过度迎合用户错误观点或压力的指标，现有基准多聚焦于用户直接施压场景。权威偏见则是人类认知中常见的倾向——人们更容易接受来自权威或可信来源的说法，即使内容与先前信念相悖。在 AI 系统中，这种偏见可能通过检索增强生成（RAG）、工具调用或外部文档引用被放大，导致模型将来源标识误认为内容正确性的保证。随着智能体 AI 越来越多地依赖自动检索、工具输出和第三方信息源，评估模型对这些来源的信任程度已成为对齐与安全研究的重要课题。

**标签**: `#AI alignment`, `#LLM safety`, `#NeurIPS 2026`, `#model robustness`, `#trust in AI systems`

---