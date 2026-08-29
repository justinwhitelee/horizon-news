---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 180 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [在 RP2350 微控制器上实现微型图像生成模型](#item-tech-news-1) ⭐️ 8.0/10
2. [智谱开源 GLM-5.3：聚焦智能体编程与网络防御](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [在 RP2350 微控制器上实现微型图像生成模型](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/cpldcpu · 8月28日 19:48

#### 摘要

开发者/u/cpldcpu 在 RP2350 微控制器上成功实现了一个仅 2.4~400 万参数的潜流 Transformer 图像生成模型，可生成 128×128 的人脸图像，最长推理耗时约 20 秒。该模型采用 int8 量化、12 层架构和 AdaLN-Zero 条件注入，并支持分类器自由引导（CFG）以提升图像质量。推理引擎利用 DMA 从 Flash 流式传输权重，同时计算前一层，并结合 ReLU²激活函数增加稀疏性，从而跳过部分计算以加速推理。这一成果展示了极小规模模型在边缘设备上运行生成式 AI 的可行性。

#### 背景

RP2350 是 Raspberry Pi 推出的新型双核 ARM Cortex-M33/M85 微控制器，具备较高的计算能力和 DMA 支持，适合嵌入式 AI 推理。潜流 Transformer（latent flow transformer）是一类将扩散过程转化为流匹配任务的图像生成架构，通常依赖于较大的模型参数和算力，此次在微控制器上的实现是对传统边缘 AI 推理范式的显著突破。

#### 社区讨论

目前没有可用的社区评论。

**标签**: `#edge AI`, `#microcontroller ML`, `#image generation`, `#model quantization`, `#embedded inference`

---

<a id="item-tech-news-2"></a>
### [智谱开源 GLM-5.3：聚焦智能体编程与网络防御](http://z.ai/) ⭐️ 8.0/10



telegram · zaihuapd · 8月28日 15:32

#### 摘要

智谱 AI 开源了 GLM-5.3 模型，主打智能体编程与网络防御场景，权重已开放下载、运行与定制。该模型与 GLM-5.2 共用同一基础模型，所有提升来自后训练阶段，在复杂编程和长周期任务方面能力明显增强：Terminal Bench 2.1 得分 88.2，DeepSWE 得分 66.9，均大幅领先 GLM-5.2。模型采用自定义 GLM-5.3 License：个人与中小企业可自由使用、微调与商用，但连续 12 个月营收超 100 亿美元且对外提供模型即服务的公司，须先通过 Z.AI 安全审查方可使用。

**标签**: `#open source`, `#large language models`, `#software engineering`, `#AI agents`

---