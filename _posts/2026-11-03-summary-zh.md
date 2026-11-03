---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 207 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [Linux 内核 IPv4 TCP 存在高危 UAF 漏洞（CVE-2026-98432）](#item-tech-news-1) ⭐️ 9.0/10
2. [Astra can read and write weights to improve Qwen](#item-tech-news-2) ⭐️ 8.0/10
3. [Astra 实现权重空间编程，Ubuntu 安全响应迟缓引发争议](#item-tech-news-3) ⭐️ 8.0/10
4. [Marvell 以 1150 亿美元收购 Lumentum](#item-tech-news-4) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Linux 内核 IPv4 TCP 存在高危 UAF 漏洞（CVE-2026-98432）](https://telegram.me/zaihuapd/44866) ⭐️ 9.0/10



telegram · zaihuapd · 11月3日 02:37

#### 摘要

Linux 内核 IPv4 TCP 模块被披露存在高危释放后使用（use-after-free）漏洞（CVE-2026-98432），攻击者无需认证且不需要用户交互即可从网络侧远程利用该漏洞获取代码执行权限。Anthropic 已公布针对 MPTCP 监听端口的远程代码执行（RCE）利用示例。该漏洞的影响范围不限于 MPTCP 场景；Go 官方安全团队提示，自 Go 1.24 起 Linux 上的 listen socket 默认启用 MPTCP，使用 Go 编写的服务默认处于暴露状态，即使未启用 MPTCP 监听也可能遭受同类攻击。

**标签**: `#Linux kernel`, `#CVE`, `#remote code execution`, `#security`, `#networking`

---

<a id="item-tech-news-2"></a>
### [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 8.0/10

Astra, an LLM system that can read and write weights to directly improve Qwen model performance, including a reported 5x math improvement through weight-space manipulation, generating active HN discussion about its significance and claims.

hackernews · dbreunig · 11月2日 18:21 · [社区讨论](https://news.ycombinator.com/item?id=50341174)

**标签**: `#AI`, `#machine learning`, `#LLM research`, `#weight-space learning`, `#model manipulation`

---

<a id="item-tech-news-3"></a>
### [Astra 实现权重空间编程，Ubuntu 安全响应迟缓引发争议](https://zeli.app/zh/digest/2026-11-02) ⭐️ 8.0/10



rss · Zeli · 11月2日 23:59

#### 摘要

Hacker News 头条报道 Astra 模型展现出“权重空间编程”能力，可不经梯度下降直接读取并修改神经网络权重。在实验中，该模型仅调整 Qwen3.5-0.8B 的 0.016% 权重，便将 MATH-500 基准测试得分从 7.9% 大幅提升至 48.1%，标志着 LLM 开始能像理解代码一样直接编辑模型参数。与此同时，Ubuntu 因迟迟未修复 CVSS 评分高达 9.8 的内核漏洞 CVE‑2026‑98432，而 Debian 等发行版迅速响应，引发企业用户对 Ubuntu 安全支持体系的信任危机。PostgreSQL 19 发布延期被归因于 LLM 辅助审查使历史代码缺陷曝光量激增 74%，挤占了新功能开发资源。此外，BYD 单月纯电动汽车销售突破 30 万辆，超越美国整个第三季度市场，凸显中国电动车产业的全球领先地位；德国研究者还揭示全球电池存储系统在整点同步进行电量检测，导致电网频率每分钟出现规律性波动，随机化检测时间可有效缓解这一问题。

**标签**: `#AI`, `#LLMs`, `#Machine Learning`, `#Linux Security`, `#Hacker News`

---

<a id="item-tech-news-4"></a>
### [Marvell 以 1150 亿美元收购 Lumentum](https://news.google.com/rss/articles/CBMif0FVX3lxTFBCY3h0UFRmd1ZoV19QeTQ0N204Ul9SRFFHSHlDMGllWkh3SHRfOEY0X0FpUFRleVc2ODhuMzVNTk1GLTlLeW4zY2JiQm1XTlFqQnlHYmRJQTRBVVFyN3pyaTJkNWN2VHVTSkg3SG1aNURBbUgwV2dfLUZXeWhiUDQ?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · 11月2日 14:00

#### 概述

Marvell Technology 宣布将以 1150 亿美元收购 Lumentum，该交易聚焦于人工智能连接技术领域。这是半导体行业近年来规模最大的并购之一，旨在整合两家公司的技术能力以强化 AI 基础设施供应链。此次收购若完成，将重塑高速光通信和 AI 网络连接市场的竞争格局。

#### 背景

Marvell Technology（马维尔科技）是一家专注于定制半导体和存储解决方案的美国公司，在数据中心网络和交换芯片领域具有重要地位。Lumentum Holdings 是一家专注于高性能激光、光收发器和光学信号处理技术的半导体公司，产品广泛应用于数据通信和电信领域。此次合并的核心逻辑在于，AI 集群需要大量高速互连技术，而电气互连与光学互连（optical I/O）分别由两家公司主导，整合后可形成从芯片到系统层的完整 AI 连接方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity">Marvell buys Lumentum in $115B AI networking power play</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/marvell-115-billion-lumentum-deal-221208604.html?fr=sycsrp_catchall">Marvell’s $115 Billion Lumentum Deal Could Reshape AI Networking</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#semiconductors`, `#M&amp;A`, `#networking hardware`

---