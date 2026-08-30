---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 123 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [腾讯发布 Hy4 Preview 开源语言模型](#item-tech-news-1) ⭐️ 8.0/10
2. [索尼音乐与华纳查佩尔起诉 Anthropic 版权侵权](#item-tech-news-2) ⭐️ 8.0/10
3. [Eamonn Keogh 质疑 TSB-AD 基准的实用性](#item-tech-news-3) ⭐️ 8.0/10
4. [OpenAI 因 SpaceX 收购终止与 Cursor 的合作](#item-tech-news-4) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [腾讯发布 Hy4 Preview 开源语言模型](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 8.0/10



rss · Simon Willison · 8月29日 23:53

#### 概述

腾讯于 2026 年 8 月 29 日发布 Hy4 Preview，这是一个开源权重的纯文本大语言模型，整体参数达 770B，激活参数 49B，上下文窗口为 100 万 token，模型文件约 1.56TB，已托管在 Hugging Face。相比 2026 年 7 月发布的上一代 Hy3（295B 总参、21B 激活参、256K 上下文、598GB），Hy4 Preview 在参数量、激活参和上下文长度上均有显著提升。该模型默认启用高推理模式（reasoning\_effort=high），同时支持关闭思维链的 no\_think 模式，其推理过程以略微截断的英文呈现，兼顾效率与可读性。

**标签**: `#open-source LLM`, `#large language models`, `#model release`, `#Tencent`, `#AI infrastructure`

---

<a id="item-tech-news-2"></a>
### [索尼音乐与华纳查佩尔起诉 Anthropic 版权侵权](https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright) ⭐️ 8.0/10



rss · The Verge · 8月29日 18:19

#### 摘要

索尼音乐（Sony Music）和华纳查佩尔（Warner Chappell）已向美国加州北区联邦地区法院对 Anthropic 提起版权诉讼，指控其未经许可使用了数万件受版权保护的音乐作品用于 AI 模型训练。原告要求每部作品最高赔偿 15 万美元，并在可识别版权数据被移除的每个实例中追加索赔最高 2.5 万美元。此案若胜诉，将对 AI 行业获取和使用版权材料的方式产生重大警示影响。

**标签**: `#AI`, `#copyright`, `#Anthropic`, `#legal`, `#music industry`

---

<a id="item-tech-news-3"></a>
### [Eamonn Keogh 质疑 TSB-AD 基准的实用性](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

著名学者 Eamonn Keogh 指出，一个百年历史的统计过程控制方法在常用的时间序列异常检测基准上超越了当前最先进模型，呼吁社区反思基准设计的合理性。

reddit · r/MachineLearning · /u/eamonnkeogh · 8月29日 20:16

#### 摘要

Eamonn Keogh 在 Reddit 社区发表观点，认为常用于 NeurIPS、SIGKDD 等顶级会议的 TSB-AD-M 基准存在严重缺陷，因为一个简单的统计过程控制（SPC）算法——拥有百年历史——就能在多个测试案例上超越当前最先进的时间序列异常检测方法。他指出该基准过于简单，甚至一些标记为“TAO”的心电图轨迹也能被 SPC 完美解决。Keogh 承认自己通过 sled dogs、Tuna、Fuel Cells 和智能制造等更挑战性数据集中完成了约 90%的工作来引入更复杂的问题，但他强调整个社区需要对基准设计进行深刻反思，认为过去十年的大部分进展可能是虚假的。

**标签**: `#time series anomaly detection`, `#benchmark critique`, `#machine learning methodology`, `#statistical process control`, `#community debate`

---

<a id="item-tech-news-4"></a>
### [OpenAI 因 SpaceX 收购终止与 Cursor 的合作](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 8.0/10



telegram · zaihuapd · 8月29日 02:24

#### 摘要

OpenAI 宣布将终止通过 Cursor 提供模型的服务协议，建议停服日期为 2026 年 11 月 12 日。公司指出，SpaceX 收购 Cursor 后，OpenAI 无法确信 SpaceX 会遵守服务条款，理由是马斯克旗下企业存在违约先例：Twitter（现已并入 SpaceX）曾违反合同，xAI 在今年早些时候宣誓承认违反 OpenAI 服务条款。这一合作已持续近四年，定制协议中包含控制权变更时的限时取消条款。

#### 背景

Cursor 是一款广受欢迎的 AI 代码编辑器，与 OpenAI 建立了长达近四年的模型供应合作关系。OpenAI 作为全球领先的 AI 模型提供商，其服务条款通常包含控制变更条款，允许在合作方被收购时终止合作。SpaceX 创始人埃隆·马斯克同时拥有 xAI 和 Twitter/X 平台，此次事件反映了大型 AI 公司与被收购工具之间的合规紧张关系。

**标签**: `#AI tools`, `#OpenAI`, `#Cursor`, `#industry news`, `#software engineering`

---