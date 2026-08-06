---
layout: default
title: "Horizon Summary: 2026-08-06 (ZH)"
date: 2026-08-06
lang: zh
---

> 从 199 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [ChainDrop 蠕虫入侵 npm 超 1300 个包，月下载量达 20 亿](#item-tech-news-1) ⭐️ 9.0/10
2. [Google DeepMind 领导层重大变动：Hassabis 转任主席，Jeff Dean 离职](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [ChainDrop 蠕虫入侵 npm 超 1300 个包，月下载量达 20 亿](https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/) ⭐️ 9.0/10



telegram · zaihuapd · 8月5日 03:04

#### 摘要

自我传播蠕虫 ChainDrop 已入侵 npm 仓库超过 1300 个包，合计月下载量达 20 亿次，涉及 Keyv、Cacheable 等热门缓存工具。攻击始于黑客攻破 Keyv 维护者的 GitHub 账号，随后蔓延至 Deliveroo、Qlik、ServiceTitan 等机构相关包，恶意版本通过正常的 GitHub Actions 流程发布并带有合法来源证明。中毒包内的 setup.mjs 投放器与 Math\_Symbol.js 窃密脚本会在执行 npm install 时自动运行，窃取 GitHub、npm、AWS、Kubernetes 等凭证并感染其他维护者的包。安全公司建议安装过受影响版本的用户视系统已被攻破，需重建环境、轮换所有令牌并检查日志，npm-cache\[.\]com 域名可作为失陷指标，且攻击仍在扩散中。

**标签**: `#supply chain security`, `#npm`, `#credential theft`, `#worm`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Google DeepMind 领导层重大变动：Hassabis 转任主席，Jeff Dean 离职](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) ⭐️ 8.0/10

Google DeepMind 宣布重大领导层变动：联合创始人 Demis Hassabis 从 CEO 转任主席，Jeff Dean 在 Google 任职 27 年后离职，与 Sanjay Ghemawat 共同创立独立公益公司。

hackernews · colesantiago · 8月5日 16:05 · [社区讨论](https://news.ycombinator.com/item?id=49184755)

#### 摘要

Google DeepMind 宣布 Demis Hassabis 从 CEO 转任主席，Jeff Dean 在 Google 任职 27 年后离职，两人将共同创立一家独立公益公司，专注于加速机器学习、科学与工程领域的发现。Sanjay Ghemawat 也随 Jeff Dean 一同离开 Google。分析认为，Hassabis 实际上将接替 Jeff Dean 成为 Alphabet 首席科学家。此次变动发生在 Google 近 14 个月未发布 Gemini 前沿 GA 版本、且多位知名研究人员（包括 Oriol Vinyals、Quoc Le、Noam Shazeer、John Jumper 等）相继离职的背景下，市场反应为 Google 股价下跌约 5%。

#### 社区讨论

社区普遍认为这是 Google AI 黄金时代的结束，多位资深工程师表示 Jeff 和 Sanjay 的存在曾是留任的重要理由。有评论指出，Google 在失去众多知名人才的同时并未带来 Gemini 前沿版本的发布，暗示工作环境可能存在问题。也有声音对 Hassabis 将重心转向 AI 医疗（如攻克癌症）表示支持。

**标签**: `#AI leadership`, `#Google DeepMind`, `#industry news`, `#talent retention`, `#Alphabet`

---