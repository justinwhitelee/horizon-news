---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 204 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Payments Canada 推出全国实时支付基础设施 RTR](#item-tech-news-1) ⭐️ 8.0/10
2. [SwarmEvolve：使用潜在推理代理群加速数学发现](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Payments Canada 推出全国实时支付基础设施 RTR](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy) ⭐️ 8.0/10



hackernews · ocd · 11月9日 16:00 · [社区讨论](https://news.ycombinator.com/item?id=50427362)

#### 摘要

Payments Canada 已宣布推出加拿大实时轨道（Real-Time Rail，简称 RTR），这是一个全国性的 24/7 实时支付基础设施。该系统基于 Interac 现有的 e-Transfer 系统构建，并以开放公共基础设施的形式向所有银行和支付提供商提供。首批活跃参与者包括 Wealthsimple、KOHO、Peoples Trust Company、Paramount Commerce 以及美国 Bank of America 等机构，而非加拿大本土大型商业银行暂未参与。这一举措标志着加拿大将一个原本由 Interac 私有的支付系统转变为可供任何金融机构构建服务的公共产品，被视为金融科技基础设施的重要进步。

#### 背景信息

实时支付系统（Real-Time Payments，RTP）是一种允许资金在参与者账户之间即时结算的金融基础设施。Interac 是加拿大主要的电子转账网络，其现有的 e-Transfer 服务已广泛应用于个人间汇款，但长期以来属于私有系统，仅限特定银行和金融机构使用。Payments Canada 作为加拿大的国家级支付运营机构，负责设计和运营重要的国家支付系统，此次将 RTR 定位为开放的公共基础设施，仿照英国和澳大利亚等国家已部署的实时支付网络模式，旨在为更广泛的金融服务提供者提供统一、低成本的实时清算通道。

#### 社区讨论

社区评论普遍认为这是值得期待的进展，将 Interac 私有系统转化为公共服务被视作明智之举。有用户将 RTR 与美国 FedNow 系统进行对比，指出 FedNow 仅由少数银行支持且收取高达交易金额 0.75%的费用，而 RTR 作为开放公共基础设施更具普惠性。也有读者质疑加拿大主要商业银行均未参与初期启动，并期待观察后续落地效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.finder.com/ca/banking/your-guide-to-real-time-rail-payments-in-canada">Real - Time Rail Payments : RTR Explained | Finder Canada</a></li>
<li><a href="https://clearingpost.com/insights/canada-rtr-q3-2026-launch/">Canada &#x27;s Real - Time Rail Targets Q3 2026 Launch | ClearingPost</a></li>

</ul>
</details>

**标签**: `#financial infrastructure`, `#real-time payments`, `#open infrastructure`, `#fintech`, `#Canada`

---

<a id="item-tech-news-2"></a>
### [SwarmEvolve：使用潜在推理代理群加速数学发现](https://www.reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/QileHQ · 11月9日 15:30

#### 摘要

研究团队提出 SwarmEvolve，一种用于数学发现与优化的可扩展框架，通过在 Qwen3 8B、14B 和 32B 模型上运行数百个潜在推理代理来实现高效计算。该方法灵感来自 Google DeepMind 的 AlphaEvolve，但受 LatentMAS 启发，使代理在潜空间中推理而非输出文本，代理之间直接共享 KV 缓存以便想法混合，显著提升了吞吐量。实验显示，仅用 8B 模型在约 5 分钟内即可达到此前 OpenEvolve、ShinkaEvolve 和 CodeEvolve 需超过 1 小时才能实现的分数，甚至在圆堆积问题上匹配已知最佳结果；后续扩展到 Qwen3.5 和 Muse 模型后表现进一步提升。

#### 背景

AlphaEvolve 是 Google DeepMind 于 2024 年提出的方法，通过让大型语言模型编写程序、评分并迭代改进来探索更优算法，曾找到 4x4 复矩阵乘法的更快方案，打破自 1969 年以来的记录。然而该方法依赖 Gemini 闭源模型且实现速度慢、成本高昂，推动了开源等价方法的研发需求。潜空间推理代理群（LatentMAS）的相关工作则表明，无需将中间推理显式写出也能有效利用 LLM 能力，为 KV 缓存共享提供了理论依据。

#### 社区讨论

目前没有可用的社区评论可供总结。作者开放邀请对材料科学、生物学等真实科学发现问题的应用建议及合作机会。

**标签**: `#AI research`, `#Large Language Models`, `#Automated theorem proving`, `#Open source tools`, `#Machine learning`

---