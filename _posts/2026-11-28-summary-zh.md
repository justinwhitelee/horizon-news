---
layout: default
title: "Horizon Summary: 2026-11-28 (ZH)"
date: 2026-11-28
lang: zh
---

> 从 164 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Trainium3 推理微架构深度解析与 GB300 TCO 对比](#item-tech-news-1) ⭐️ 8.0/10
2. [Linux 内核 NFS 服务器 9.8 分预认证堆溢出漏洞披露](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Trainium3 推理微架构深度解析与 GB300 TCO 对比](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 8.0/10



rss · Semianalysis · 11月27日 15:54

#### 核心内容

SemiAnalysis 发布了对 AWS Trainium3 推理微架构的首篇深度技术解析，采用基于物理的第一性原理分析方法，从架构底层拆解其推理性能表现。文章将 Trainium3 的 TCO（总拥有成本）与 NVIDIA GB300 进行了系统对比，评估其作为 AI 推理基础设施替代方案的竞争力。基准测试涵盖 MFU（模型浮点运算利用率）与 MBU（内存带宽利用率）两项关键指标，并通过 UBenchX 基准套件验证实际性能。分析指出 Trainium3 在推理场景下展现出低延迟特性，且 MFU 和 MBU 表现较为突出。该报告为正在构建或采购 AI 系统的工程师提供了架构级参考，是 AWS 在 AI 芯片领域挑战 NVIDIA 主导地位的重要技术评估。

#### 背景

AWS Trainium 是亚马逊云科技自研的机器学习加速器，其微架构以&quot;tile&quot;（数据块）为一等原语从底层专为 ML 负载设计，区别于通用 GPU 的&quot;线程海洋&quot;加外挂张量引擎的路线；Trainium3 每颗芯片包含八个 NeuronCore-v4 核心，并支持逻辑神经元核心配置（LNC），可将多个物理核心的计算与内存资源合并为单一逻辑核心。NVIDIA GB300 NVL72 基于 Blackwell Ultra GPU，采用全液冷机架级设计，将 72 颗 Blackwell Ultra GPU 与 36 颗 Arm 架构 Grace CPU 统一于单一平台，是 NVIDIA 面向 AI 数据中心的旗舰推理与训练方案。这一对比所处的行业背景是 AI 推理算力需求快速增长——Epoch AI 数据显示 AI 推理容量在一年内增长约 4.6 倍——超大规模云厂商自研芯片与 NVIDIA 通用加速器之间的竞争因此持续升温。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium3.html">Trainium3 Architecture — AWS Neuron Documentation</a></li>
<li><a href="https://newsletter.semianalysis.com/p/trainium3-inferencex">AWS Challenger: Trainium3 Inference and Microarchitecture ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">Designed for AI Reasoning Performance ... | NVIDIA GB 300 NVL72</a></li>
<li><a href="https://epoch.ai/data-insights/agentic-inference-capacity-growth">AI inference capacity grew 4.6× in one year | Epoch AI</a></li>

</ul>
</details>

**标签**: `#AWS Trainium3`, `#AI Hardware`, `#TCO Analysis`, `#Microarchitecture`, `#NVIDIA Competition`

---

<a id="item-tech-news-2"></a>
### [Linux 内核 NFS 服务器 9.8 分预认证堆溢出漏洞披露](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 8.0/10



telegram · zaihuapd · 11月27日 12:57

#### 事件摘要

OpenSec 披露了 Linux 内核 NFS 服务器（nfsd）中的一个预认证堆溢出漏洞（CVE-2026-99362），CVSS 评分为 9.8。攻击者无需任何身份验证，仅需向目标主机的 tcp/2049 端口发送一条连接即可触发内核堆越界写入，进而获取 root shell。该漏洞自 2014 年 Linux 3.16 起存在，影响所有启用 NFSv4.1 或 NFSv4.2 的主机，波及文件服务器、NAS 及集群存储节点。修复已合入 6.12.117、6.18.61、7.3.2 及 7.4-rc1 内核版本，需升级内核并重启系统；无法立即升级的环境应通过应用防火墙限制 tcp/2049 端口的访问作为临时缓解措施。该 CVE 于 2026 年 11 月 20 日正式公开。

#### 背景

NFS（Network File System，网络文件系统）是 Linux 内核自带的文件共享服务，nfsd 为其内核态守护进程，负责将本地文件系统通过 TCP/UDP 2049 端口暴露给远程客户端。NFSv4.1 和 NFSv4.2 是支持多通道与会话管理的现代协议版本，广泛应用于企业文件服务器、NAS 和集群存储场景。所谓&quot;预认证&quot;漏洞，指攻击者无需提供任何用户凭据即可触发，这使得暴露在局域网或广域网中的 NFS 服务成为高风险目标。

**标签**: `#Linux kernel security`, `#NFS vulnerability`, `#pre-authentication exploit`, `#CVE-2026-99362`, `#heap overflow`

---