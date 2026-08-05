---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 197 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Shai-Hulud 供应链攻击入侵 Keyv 等 npm 包](#item-tech-news-1) ⭐️ 8.0/10
2. [谷歌为 Anthropic 搭建 2000 亿美元基础设施融资架构](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Shai-Hulud 供应链攻击入侵 Keyv 等 npm 包](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10



hackernews · cimi\_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

#### 摘要

活跃的 Shai-Hulud 供应链攻击已入侵 Keyv 及相关 npm 软件包，引发社区广泛关注。该攻击利用 npm 包的 pre-install 钩子机制进行传播，属于 worm 式扩散攻击。社区讨论了多种防御手段，包括使用 Packj 等静态与动态行为分析工具检测 compromised 指标（如 shell 调用、SSH 密钥使用、decode+eval 模式等），以及推广 devcontainer 以隔离依赖安装环境。多位评论者指出，npm 依赖系统的结构性脆弱是此类攻击得以成功的根本原因，并呼吁对新增 pre-install 钩子实施禁令。

#### 社区讨论

社区就检测工具和防御策略展开讨论：ashishbijlani 推荐 Packj 工具进行供应链攻击检测；xnorswap 主张全面禁止 pre-install/post-install 钩子；TimJRobinson 建议开发者采用 devcontainer 隔离依赖安装；ChrisMarshallNY 指出 npm 依赖系统的结构性缺陷是攻击成功的核心原因，并警告即使清理原始污染，连锁 compromised 仍将持续；phyzome 则质疑 GitHub 为何不能直接拦截 Shai-Hulud 外泄仓库的创建。

**标签**: `#supply chain security`, `#npm`, `#open source`, `#software security`, `#AI/ML infrastructure`

---

<a id="item-tech-news-2"></a>
### [谷歌为 Anthropic 搭建 2000 亿美元基础设施融资架构](https://www.ft.com/content/549f2e23-5aa2-49c7-9ea6-a9784ab7087c) ⭐️ 8.0/10



telegram · zaihuapd · 8月4日 10:52

#### 摘要

据《金融时报》8 月 4 日调查，谷歌已搭建规模约 2000 亿美元的基础设施融资架构，支持向 Anthropic 交付超 1500 亿美元的 AI 芯片，其中约八成与芯片直接挂钩。参与方包括博通、阿波罗、黑石、摩根士丹利及多家加密矿企。由于 Anthropic 没有信用评级，风险由各方分担：谷歌担保数据中心，博通购买并协助融资芯片，阿波罗与黑石出资购买硬件后回租给 Anthropic。今年 6 月，特殊目的载体 Compute SPV 完成首批交易，购入约 350 亿美元硬件，约合 1 吉瓦算力、100 万颗 TPU。该模式借鉴波音、GE 推销飞机和发动机的厂商融资玩法，使各方无需将数百亿美元 AI 硬件压在自家资产负债表上。

#### 背景

特殊目的载体（SPV）是一种为特定交易目的而设立的独立法律实体，常用于将资产和风险从母公司资产负债表中剥离，以降低融资成本和风险集中度。TPU（Tensor Processing Unit）是谷歌自主研发的专用人工智能芯片，专为机器学习工作负载优化，与英伟达的 GPU 形成竞争。Anthropic 是一家专注于 AI 安全研究的公司，其开发的 Claude 大语言模型是 OpenAI ChatGPT 的主要竞争对手之一。

**标签**: `#AI infrastructure`, `#financing models`, `#Google`, `#Anthropic`, `#hardware`

---