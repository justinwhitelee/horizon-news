---
layout: default
title: "Horizon Summary: 2026-08-10 (ZH)"
date: 2026-08-10
lang: zh
---

> 从 206 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [vLLM v0.27.0 发布：Kimi K3 支持、PyTorch 2.13 升级与 SM100 FP8 KV 缓存](#item-tech-news-1) ⭐️ 8.0/10
2. [索尼与台积电合资建传感器产线，投资约 1 万亿日元](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.27.0 发布：Kimi K3 支持、PyTorch 2.13 升级与 SM100 FP8 KV 缓存](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 8.0/10



github · khluu · 8月10日 21:18

#### 摘要

vLLM 项目发布了 v0.27.0 版本，包含来自 242 位贡献者（其中 64 位为新贡献者）的 561 个提交。本次重大更新包括 Kimi K3 模型的完整栈支持，涵盖核心模型文件、内核、Python 与 Rust 前端、AttnRes 内核、DeepGEMM 支持、compressed-tensors 量化检查点以及 DSpark AR 融合等。PyTorch 已升级至 2.13.0 版本，同时 torchvision 升级至 0.28.0、Triton 升级至 3.7.1，XPU 和 CPU 后端也跟随升级，属于破坏性环境变更。FlashAttention 4 在 SM100 上新增 FP8 KV 缓存和 headdim-256 支持，并引入新的 JIT 预热基础设施以消除首次请求的编译延迟。

#### 背景

vLLM 是一个广泛使用的开源大语言模型推理框架，支持多种模型架构和硬件平台。FlashAttention 是高效的注意力计算内核，SM100 指 NVIDIA Blackwell 架构 GPU。FP8 是一种 8 位浮点格式，可在保持精度的同时降低内存带宽需求。MLA（Multi-head Latent Attention）和 SSM（State Space Model）是 DeepSeek 等模型采用的先进架构技术。

#### 社区讨论

目前暂无社区评论可供总结。

**标签**: `#vLLM`, `#LLM inference`, `#PyTorch`, `#FlashAttention`, `#model support`

---

<a id="item-tech-news-2"></a>
### [索尼与台积电合资建传感器产线，投资约 1 万亿日元](https://www.bloomberg.com/news/articles/2026-08-10/sony-tsmc-to-invest-6-4-billion-in-joint-chip-plant-in-japan) ⭐️ 8.0/10



telegram · zaihuapd · 8月10日 04:01

#### 摘要

索尼集团与台积电计划在日本熊本县索尼半导体解决方案运营的图像传感器工厂内建设研发设施和生产线，投资规模约 1 万亿日元（约 63 亿至 64 亿美元）。合资企业将由索尼持股约 60%、台积电约 40%，计划最早于 2029 年开始量产下一代图像传感器，产品面向高性能相机、机器人和汽车等&quot;实体 AI&quot;应用。双方预计近期就量产投资达成协议，并在截至 2027 年 3 月的财年结束前成立合资企业，目前正与日本经济产业省商谈政府补贴可能性。

**标签**: `#hardware`, `#AI systems`, `#semiconductors`, `#robotics`, `#joint venture`

---