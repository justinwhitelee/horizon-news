---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 160 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [LLM 进化圈填充算法，改进 Packomania 十个最优解](#item-tech-news-1) ⭐️ 9.0/10
2. [InferenceX 加速外部化 Google TPU 推理栈，宣称性能提升 50%](#item-tech-news-2) ⭐️ 8.0/10
3. [Yandex 团队提出将 KV 缓存作为智能体运行时](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [LLM 进化圈填充算法，改进 Packomania 十个最优解](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 9.0/10



reddit · r/MachineLearning · /u/SIGH\_I\_CALL · 9月7日 16:54

#### 摘要

研究者采用 LLM 驱动的算法进化方法，在 Packomania csqv（圆填充）基准测试上独立改进了 N=101 至 114 共十个问题的最优解，优化目标为半径之和，提升幅度达 2.4%至 5.4%，仅需 15 次迭代，总 LLM 成本 27.72 美元。该方法从简单种子求解器出发，由 LLM 提出算法变更提案，并由独立验证器评分筛选——改进被保留，失败被淘汰。Packomania 已独立接受这些结果，论文已发布于 arxiv（arxiv.org/abs/2609.05093），代码与解也一并公开（github.com/ucsandman/discovery-loop）。作者特别希望就其停滞检测停止规则获得批评意见。

**标签**: `#artificial intelligence`, `#optimization`, `#research`, `#algorithms`, `#machine learning`

---

<a id="item-tech-news-2"></a>
### [InferenceX 加速外部化 Google TPU 推理栈，宣称性能提升 50%](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10



rss · Semianalysis · 9月7日 20:00

#### 摘要

InferenceX 正在加速将 Google 的 TPU 推理栈外部化，并声称相比现有方案可获得高达 50% 的每美元性能提升。该举措涉及 Ironwood 平台及 TPUv8i 等硬件产品，客户群体正在快速增长。这一动向被视为减少市场对 CUDA 生态依赖的重要一步，对 AI 基础设施和硬件格局具有显著的战略意义。

**标签**: `#AI hardware`, `#TPU`, `#GPU ecosystems`, `#CUDA`

---

<a id="item-tech-news-3"></a>
### [Yandex 团队提出将 KV 缓存作为智能体运行时](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/\_puhsu · 9月7日 09:03

#### 摘要

来自 Yandex 关联研究团队的研究者提出了一种新方法：通过操作模型的 KV 缓存推理状态来提升 LLM 系统的交互性和响应速度。该思路延续自实验室此前的两篇论文《Hogwild\! Inference》和《AsyncReasoning》，并在预告工作中展示了使用 Qwen3.8-27B 智能体以类似技术交互式游玩 DOOM 环境的示例。研究者认为，除了更换模型或调整工具链之外，推理/运行时设计本身可能是一个尚未被充分探索的智能体能力维度。

#### 背景

KV 缓存（KV Cache）是 Transformer 模型推理过程中用于存储注意力机制中键（Key）和值（Value）张量的结构，可避免重复计算已有 token 的表示。当前主流 LLM 智能体系统通常采用

**标签**: `#LLM inference optimization`, `#AI agents`, `#model runtime engineering`, `#KV-cache manipulation`, `#machine learning research`

---