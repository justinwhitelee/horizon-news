---
layout: default
title: "Horizon Summary: 2026-09-15 (ZH)"
date: 2026-09-15
lang: zh
---

> 从 196 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [NVIDIA Vera Rubin NVL72：67 倍性能价格比的 AI 推理平台](#item-tech-news-1) ⭐️ 8.0/10
2. [边缘计算与数据中心推理：Jetson Thor 与 B300 的 TCO 对比](#item-tech-news-2) ⭐️ 8.0/10
3. [苹果发布 iOS 27 与 macOS Golden Gate 27：Siri AI 全面升级，Liquid Glass 优化](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [NVIDIA Vera Rubin NVL72：67 倍性能价格比的 AI 推理平台](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10



rss · Semianalysis · 9月14日 22:08

#### 摘要

SemiAnalysis 报道了 NVIDIA 发布的 Vera Rubin NVL72 平台，声称在智能体（agentic）推理工作负载方面实现了每美元 67 倍的更高性能。该分析还强调了利润每瓦时的提升——据称年利润每千兆瓦时提高 2 倍，并涉及 NVIDIA 的协同设计（co-design）策略。这一发布目标明确指向 AI 推理基础设施领域，反映了 NVIDIA 针对智能体 AI 工作负载进行硬件优化的技术路线。

#### 背景

NVIDIA Vera Rubin NVL72 是英伟达推出的新一代推理平台，定位为针对 Agentic AI（智能体 AI）工作负载优化的推理基础设施。Agentic AI 指能够自主执行复杂多步任务的 AI 系统，常见场景包括代码编写、工具调用和链式推理（如 Kimi-K2-Thinking 等模型）；与单次问答相比，这类工作负载的 token 吞吐和能效更为关键。Vera Rubin NVL72 在性能指标上对标此前发布的 GB300 NVL72，通过更激进的芯片与系统级协同设计（co-design）来降低每百万 token 的成本并提升每瓦特算力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/">Up to 30x More Work Per Watt: NVIDIA Vera Rubin NVL72 Sets a New Efficiency Standard for AI Agents</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/">NVIDIA Vera Rubin NVL72 | Co-Designed Infrastructure for Agentic AI</a></li>
<li><a href="https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference">Rubin NVL72 Agentic Inference: 67x better Performance per Dollar</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI inference`, `#hardware`, `#agentic AI`, `#GPU infrastructure`

---

<a id="item-tech-news-2"></a>
### [边缘计算与数据中心推理：Jetson Thor 与 B300 的 TCO 对比](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 8.0/10



rss · Semianalysis · 9月14日 16:37

#### 概述

Semianalysis 的文章探讨了大型 AI 模型应运行在 Jetson Thor 等边缘设备上还是留在数据中心使用 B300 进行推理，分析了两种方案的总体拥有成本（TCO）以及机载计算与云灵活性之间的约束。文章重点关注硅效率的权衡以及网络瓶颈问题，为 AI 工程师在基础设施决策上提供了具有实际部署场景支撑的分析。

#### Background

NVIDIA Jetson Thor is an edge AI computing platform announced in January 2026, offering 2070 FP4 TFLOPS of AI performance with 128 GB of memory and 40–130 W power consumption. It represents a significant step up from its predecessor, the AGX Orin, delivering 7.5× the AI performance and 3.5× the efficiency while supporting native FP4 quantization and generative AI models for real-time robotics applications. The B300 is NVIDIA&\#x27;s datacenter GPU designed for large-scale AI inference workloads. The core tension in modern AI deployment is between running models directly on edge devices—enabling low-latency, offline operation—and leveraging cloud datacenter infrastructure, which offers greater compute flexibility but introduces network dependency and data transfer costs.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/">Jetson Thor | Advanced AI for Physical Robotics | NVIDIA</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/">Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI | NVIDIA Technical Blog</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Edge Computing`, `#Model Deployment`, `#TCO Analysis`, `#On-Device Inference`

---

<a id="item-tech-news-3"></a>
### [苹果发布 iOS 27 与 macOS Golden Gate 27：Siri AI 全面升级，Liquid Glass 优化](https://arstechnica.com/apple/2026/09/apple-releases-ios-27-macos-golden-gate-27-with-siri-ai-and-liquid-glass-refinements/) ⭐️ 8.0/10

苹果于 9 月 14 日正式推送 iOS 27 与 macOS Golden Gate 27，Siri 迎来深度 AI 重构，同时 macOS Golden Gate 27 成为最后一代支持 Rosetta 转译 Intel 应用的系统版本。

rss · Ars Technica · 9月14日 19:28

#### 核心要点

苹果当地时间 9 月 14 日推送 iOS 27 与 macOS Golden Gate 27，北京时间预计在 9 月 15 日凌晨 1 点左右开放下载。iOS 27 支持 iPhone 11 系列及后续机型，核心更新包括重新设计的 Siri、更个性化的 AI 功能，以及系统性能提升；同时新增两台 iPhone 共用同一号码切换使用、暂停向特定联系人共享「查找」位置、停车状态下通过 CarPlay 观看视频等功能，部分 AI 功能仅支持较新机型。macOS Golden Gate 27 则在 Siri AI 与 Liquid Glass 视觉设计上持续优化，并标志着 macOS 最后一代支持 Rosetta 转译 Intel 应用，Intel 兼容时代就此落幕。

#### 背景信息

Rosetta 是苹果在 2020 年转向 Apple Silicon 芯片后推出的 Intel 应用转译工具，历经多代 macOS 更新一直提供向下兼容支持。iOS 27 的 Siri AI 深度整合反映了苹果近年来在人工智能领域的持续投入，Liquid Glass 则是苹果 2025 年 WWDC 上推出的全新视觉设计语言。

**标签**: `#Apple`, `#Operating Systems`, `#AI`, `#Software Releases`, `#Developer Impact`

---