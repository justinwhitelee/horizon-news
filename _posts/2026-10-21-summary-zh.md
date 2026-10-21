---
layout: default
title: "Horizon Summary: 2026-10-21 (ZH)"
date: 2026-10-21
lang: zh
---

> 从 201 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [eMudhra 中间 CA 私钥泄露事件](#item-tech-news-1) ⭐️ 9.0/10
2. [SpaceX 将首次尝试半空捕获星舰与助推器](#item-tech-news-2) ⭐️ 8.0/10
3. [Google 开源 TorchTPU，TPU 成为 PyTorch 原生选项](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [eMudhra 中间 CA 私钥泄露事件](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 9.0/10



rss · Simon Willison · 10月20日 23:50

#### 摘要

eMudhra 八个中间证书颁发机构（CA）的私钥遭泄露，这些证书受 Mozilla、Microsoft、Apple 和 Chrome 等主流根证书程序信任。任何捆绑可信证书列表的软件均需紧急更新，Linux 发行版需更新 ca-certificates 软件包，Python 生态的 uv 0.13.4、pip 26.2.2 和 certifi 2026.10.19 已发布新证书列表。社区指出部分私钥强度极弱（如单个字节“4”），引发对“泄露”性质的质疑；Mozilla 已通过 OneCRL 为 Firefox 用户提供自动修复，而 Chrome、Apple、Microsoft 也具备类似撤销机制，但其他生态系统缺乏同等投入。此外，许多软件供应商自带 CA 证书库，导致补丁难以全面覆盖，系统长期暴露于风险中。eMudhra 解释称事故源于生成 ECC 证书的 KGC 脚本缺陷。

#### 背景

证书颁发机构（CA）是信任链的核心，负责签发网站证书。中间 CA 由根证书授权，其私钥泄露可导致攻击者伪造任意证书。主流操作系统和浏览器通过内置根证书库验证 HTTPS 连接，若中间 CA 私钥泄露，需从信任列表中移除相关证书以维持安全。

#### 社区讨论

社区共识是 Mozilla 等主流平台已通过 OneCRL 和 CRLite 实现快速撤销，但大量非主流软件因捆绑独立 CA 证书库而难以及时修复。部分用户质疑泄露私钥强度过弱（如单字节“4”），认为不能简单称为“泄露”。eMudhra 官方解释为 KGC 脚本缺陷导致 ECC 密钥生成异常。

**标签**: `#cryptography`, `#certificate authority`, `#security incident`, `#software engineering`, `#Python tooling`

---

<a id="item-tech-news-2"></a>
### [SpaceX 将首次尝试半空捕获星舰与助推器](https://www.theverge.com/science/1014913/spacex-will-try-catching-starship-and-its-booster-for-first-time-musk-says) ⭐️ 8.0/10



rss · The Verge · 10月20日 21:02

#### 摘要

SpaceX CEO 埃隆·马斯克宣布，该公司将于下月首次尝试在半空中捕获

**标签**: `#space technology`, `#aerospace engineering`, `#reusable rockets`, `#propulsion systems`, `#industry milestones`

---

<a id="item-tech-news-3"></a>
### [Google 开源 TorchTPU，TPU 成为 PyTorch 原生选项](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus) ⭐️ 8.0/10



telegram · zaihuapd · 10月21日 00:47

#### 概述

Google Cloud 宣布与 Meta 的 PyTorch 团队共同开发的 TorchTPU 已在 GitHub 开源，TPU 由此成为与 GPU、CPU 并列的 PyTorch 原生执行选项，现有 PyTorch 代码几乎无需改动即可在 TPU 上运行。vLLM、SGLang、llm-d、TorchTitan 等主流 AI 框架已完成接入，Hugging Face Transformers v5 也可直接将模型部署到 TPU 硬件上。此举显著降低了 PyTorch 用户采用 TPU 的门槛，被视为对 NVIDIA GPU 在 AI 生态中主导地位的直接挑战，标志着 AI 基础设施领域的一次重要行业转变。

**标签**: `#AI infrastructure`, `#open source`, `#PyTorch`, `#TPU`, `#hardware`

---