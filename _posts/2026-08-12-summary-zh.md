---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 205 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Qwen 开源 MoE 模型 Qwen3.8-2.4T-A95B](#item-tech-news-1) ⭐️ 8.0/10
2. [Adam 的逐坐标自适应破坏旋转不变性，导致低秩偏置丢失](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Qwen 开源 MoE 模型 Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10



hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

#### 摘要

Qwen 发布开源权重 MoE 模型 Qwen3.8-2.4T-A95B，总参数量 2.4T，激活参数 95B，原生上下文长度 262,144 tokens，可扩展至 1,010,000 tokens。该模型声称性能介于 Opus 4.8 与 Fable 5 之间，直接对标 Kimi k3 和 DeepSeek V4-Pro 等顶级商业模型。目前官方提供 bf16（约 4.9TB）和 FP8 两种精度，unsloth.ai 已推出 1bit 量化版本（约 397GB）。需注意的是，开源版未包含视觉输入和 1M 上下文等 Qwen3.8-Max 商业版本的增强功能，许可协议与 Kimi k3 类似，对年收入超过 5000 万美元的用途设有限制。

#### 背景

Qwen3.8-2.4T-A95B 是阿里巴巴开源的最大参数规模 MoE 架构语言模型，原生支持 26.2 万 tokens 上下文（可扩展至 101 万），采用 2.4 万亿总参数、950 亿激活参数的混合专家设计。该模型开放 bf16 和 fp8 两种精度权重， licensing 允许年收入低于 5000 万美元的内部使用或商业部署。社区同时关注 DeepSeek V4-Pro 基准测试数据，以及与其他开源模型如 Kimi k3 的对比讨论。

#### 社区讨论

社区热议集中在三点：一是量化选项（FP8、1bit 约 397GB）使原本难以部署的模型变得可及；二是开源版缺少视觉输入和 1M 上下文长度，被部分用户视为遗憾；三是 bf16/FP8 首发无 QAT 量化版本，需要具备资源的一方投入大量校准数据才能完成高质量量化，存在一定门槛。

**标签**: `#open source AI`, `#large language models`, `#Mixture of Experts`, `#model quantization`, `#AI benchmarks`

---

<a id="item-tech-news-2"></a>
### [Adam 的逐坐标自适应破坏旋转不变性，导致低秩偏置丢失](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

#### 摘要

一项研究通过矩阵感知实验发现，在因式分解模型 W = UV^T 中，梯度下降（GD）保持旋转不变性及其隐式的低秩偏置，而 Adam 的逐坐标二阶矩自适应破坏了这一不变性，导致低秩结构丢失。实验对比了九种更新规则，在匹配训练损失后清晰分为两组：GD、共享标量 Adam、Muon 和 Shampoo 保留低秩偏置；Adam、RMSProp、Lion、signum 和 Adafactor 则丧失该偏置。通过一个将 Adam 分母从逐坐标调整为单一共享标量的一参数族验证，恢复误差随单调改善，确认损伤源于各向异性而非自适应本身。Muon 在无噪声低秩目标上精确，但随谱尾部能量增加退化最快，在约 4% 尾部能量处与 GD 交叉，同一轴线上同时印证了近期文献中的矛盾发现。作者指出，若允许各方法自选最佳学习率，Adam 在超光谱数据上的误差降低优势会缩小，但机制本身仍是核心主张。

#### 背景

因式分解模型 W = UV^T 将高维矩阵表示为两个低秩因子的乘积，常用于推荐系统、压缩感知等领域。旋转不变性指对因子同时进行正交变换（U,V）→ \(UQ, VQ\) 不改变目标损失，该性质在许多优化算法中具有隐含的低秩偏好，即梯度下降倾向于收敛到更简单的解。实际应用中，保持这种偏置有助于提升泛化能力与数值稳定性，因此不同优化器在此类结构下的行为差异受到关注。

**标签**: `#machine learning optimization`, `#matrix factorization`, `#optimizer behavior`, `#low-rank structure`, `#experimental ML`

---