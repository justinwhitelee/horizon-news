---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> 从 206 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [EDK2 UEFI 固件关键漏洞危及全球多数服务器](#item-tech-news-1) ⭐️ 9.0/10
2. [Triton v3.9.0 发布：新增原子操作、近似除法与性能优化](#item-tech-news-2) ⭐️ 8.0/10
3. [Tailscale SSH 漏洞调查与修复更新](#item-tech-news-3) ⭐️ 8.0/10
4. [有限单群分类定理在 Lean 中完成形式化](#item-tech-news-4) ⭐️ 8.0/10
5. [Ars Technica 评测苹果 iPhone Duo 折叠屏手机](#item-tech-news-5) ⭐️ 8.0/10
6. [🤖 OpenAI 公布模型产出的三项科研结果](#item-tech-news-6) ⭐️ 8.0/10
7. [Anthropic 招聘经理停用编程面试](#item-tech-news-7) ⭐️ 8.0/10
8. [Google 提出睡眠框架，助大模型持续学习不遗忘](#item-tech-news-8) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [EDK2 UEFI 固件关键漏洞危及全球多数服务器](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/) ⭐️ 9.0/10



rss · Ars Technica · 10月27日 20:25

#### 摘要

Ars Technica 报道，EDK2（EFI 开发工具包）UEFI 固件实现中存在一个关键代码执行漏洞，允许攻击者在系统启动早期阶段执行任意代码。该漏洞影响全球大多数服务器，属于固件层面的高危缺陷，具有广泛的底层基础设施安全风险。攻击者可在操作系统加载前获得执行权限，从而绕过传统安全机制。

**标签**: `#UEFI firmware`, `#critical vulnerability`, `#EDK2`, `#server security`, `#boot-level exploit`

---

<a id="item-tech-news-2"></a>
### [Triton v3.9.0 发布：新增原子操作、近似除法与性能优化](https://github.com/triton-lang/triton/releases/tag/v3.9.0) ⭐️ 8.0/10



github · warrendeng · 10月27日 18:56

#### 概述

Triton 3.9.0 版本于 GitHub 发布，引入了 \`tl.atomic\_load\`、\`tl.atomic\_store\` 和 \`tl.atomic\_poll\` 原子操作，以及支持快速 FP32 近似的除法 \`tl.fdiv\(approx=True\)\`。该版本还改进了语言语法，支持链式比较、关键字参数和元组解包，并修复了 E8M0 标度解码（\`0x00\` 解码为 2^-127，\`0xFF\` 解码为 NaN）等关键错误。在编译器后端，原子操作默认使用 acquire/release 语义，并为多 CTA 内核添加了集群同步与代理围栏；NVIDIA 后端的批处理矩阵乘法性能最高提升 40 倍。此次更新对 GPU 内核开发人员和机器学习工程师具有重要意义，提供了更精确的内存原子原语和更强的性能优化。

#### 背景

Triton 是一个面向 GPU 编程的开源语言与编译器，广泛应用于人工智能/机器学习工作负载。其设计目标是通过高级原语简化 CUDA 内核编写，同时保持底层控制能力。v3.9.0 版本新增的原子操作（load/store/poll）填补了先前支持缺失的空白，而近似除法则为需要性能优先的计算场景提供了更快的选项。

**标签**: `#open source`, `#GPU programming`, `#machine learning`, `#compiler`, `#AI systems`

---

<a id="item-tech-news-3"></a>
### [Tailscale SSH 漏洞调查与修复更新](https://tailscale.com/ssh-investigation-update) ⭐️ 8.0/10



hackernews · figmert · 10月27日 19:55 · [社区讨论](https://news.ycombinator.com/item?id=50264857)

#### 概要

Tailscale 发布了一份关于其 SSH 功能的漏洞调查与修复更新报告。该事件引发了社区对 SSH/VPN 架构的深入讨论。多位用户在 Hacker News 上分享了各自的使用经验和观点。

#### 社区讨论

社区共识集中在两点：一是漏洞影响范围限于使用 Tailscale SSH 并开放 sudo 权限的场景；二是许多用户对 Tailscale 同时承担 VPN 和 SSH 功能表示担忧，认为这构成了单点故障风险，倾向退回传统 OpenSSH 方案。

**标签**: `#infrastructure security`, `#open source`, `#networking`, `#zero trust`

---

<a id="item-tech-news-4"></a>
### [有限单群分类定理在 Lean 中完成形式化](https://cfsg.axiommath.ai/) ⭐️ 8.0/10



hackernews · pfdietz · 10月27日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50261647)

#### 摘要

有限单群分类定理（Classification of Finite Simple Groups，简称 CFSG）已被完整形式化于 Lean 定理证明器中，项目地址为 https://cfsg.axiommath.ai/。该定理是 20 世纪代数学的里程碑成果，原始证明由约 100 位数学家合作完成，总篇幅超过 1000 页。形式化过程中，研究团队还发现并填补了原始证明中的一个漏洞。这一成果标志着大规模数学定理形式化进程的重要突破，为自动形式化和 AI 辅助定理证明领域提供了关键基础设施。

#### 背景

有限单群分类定理断言所有有限单群均可归类为若干无穷族和 26 个散在群（sporadic groups），其证明横跨代数、群论等多个分支，是数学史上规模最大、最复杂的证明之一。Lean 是由 Microsoft Research 和学术界共同开发的依赖类型定理证明器，近年来在形式化数学社区中迅速普及，已成为大规模数学定理形式化的主流工具之一。

#### 社区讨论

社区热议利用前沿 AI 模型对数学教材进行自动形式化的可行性，将其视为一次性的宏大工程，可为未来证明提供可复用库。同时有评论指出，尽管同伦论基础（homotopical foundations）派别未能主导形式化进程，当前工作仍以集合论为基础。另有参与者注意到，陶哲轩等人预测此类超大规模合作将在数学界愈发常见。

**标签**: `#formal verification`, `#theorem proving`, `#artificial intelligence`, `#mathematics`, `#Lean`

---

<a id="item-tech-news-5"></a>
### [Ars Technica 评测苹果 iPhone Duo 折叠屏手机](https://arstechnica.com/gadgets/2026/10/apple-iphone-duo-review-two-screens-two-experiences-two-thousand-dollars/) ⭐️ 8.0/10



rss · Ars Technica · 10月27日 14:20

#### 评测摘要

《Ars Technica》对苹果首款可折叠手机 iPhone Duo 进行了评测。该设备采用双屏设计，售价高达 2000 美元。评测人 Andrew Cunningham 认为苹果在可折叠手机领域的初次尝试值得尊重，双屏概念有一定可取之处，但实际体验并未完全令人满意。这部设备的发布标志着苹果正式进入可折叠智能手机市场，其定价策略和设计思路将对行业产生重要影响。

**标签**: `#apple`, `#foldable-phone`, `#smartphone`, `#product-review`

---

<a id="item-tech-news-6"></a>
### [🤖 OpenAI 公布模型产出的三项科研结果](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 8.0/10

Unverified claims that OpenAI models produced proofs of major results in computational complexity, harmonic analysis, and theoretical physics, with external expert verification underway.

telegram · zaihuapd · 10月27日 15:00

**标签**: `#AI for science`, `#formal verification`, `#computational complexity`, `#research breakthroughs`, `#open source`

---

<a id="item-tech-news-7"></a>
### [Anthropic 招聘经理停用编程面试](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) ⭐️ 8.0/10



telegram · zaihuapd · 10月28日 01:46

#### Anthropic 招聘经理停用编程面试

Anthropic 招聘经理 Felix Rieseberg 本月停止在面试中考核编程题，称 Claude 已比候选人更擅长这类题目，写代码不再是有效的筛选标准。他认为执行力成本下降后，资历不再决定影响力，建议初级工程师瞄准业务目标，借助新人视角，用一个周末做出单一原型争取支持。Claude Code 的图形界面原型由两名新人于周末完成，约八天后发布了首个公开版本。

**标签**: `#AI`, `#software engineering`, `#hiring practices`, `#Anthropic`, `#programmatic intelligence`

---

<a id="item-tech-news-8"></a>
### [Google 提出睡眠框架，助大模型持续学习不遗忘](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research proposes a sleep framework for LLM continual learning that mitigates catastrophic forgetting by alternately cycling between active interaction and an offline consolidation phase, reporting results surpassing GPT-4 and SFT baselines.

telegram · zaihuapd · 10月28日 01:46

**标签**: `#continual learning`, `#catastrophic forgetting`, `#large language models`, `#Google Research`

---