---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 191 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [黎曼假设的 AI 辅助证明有了新进展](#item-tech-news-1) ⭐️ 9.0/10
2. [GPT-6 通过代码编写实现蛋白质 minbinders 设计](#item-tech-news-2) ⭐️ 8.0/10
3. [AI 大模型一年三次拐点：从可靠编码到 3D 创作](#item-tech-news-3) ⭐️ 8.0/10
4. [网页端编译 Firefox 与 LLM 代理企业忠诚度分析](#item-tech-news-4) ⭐️ 8.0/10
5. [亚马逊转向 SpaceX 与阿里安 6 发射卫星](#item-tech-news-5) ⭐️ 8.0/10
6. [T3 Code 默认开启遥测并读取本机认证凭证](#item-tech-news-6) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [黎曼假设的 AI 辅助证明有了新进展](https://arstechnica.com/ai/2026/11/whats-going-on-with-the-riemann-hypothesis/) ⭐️ 9.0/10



rss · Ars Technica · 11月24日 20:34

#### 摘要

Ars Technica 报道了一项据称扎实的 AI 辅助证明，声称解决了黎曼猜想——数学领域最具影响力的未解问题之一。该证明由 AI 辅助完成，并涉及形式化验证技术，代表了人工智能与纯数学交叉领域的潜在范式级事件。然而，尽管证明本身似乎可靠，数学界对其所揭示的深层含义仍不确定。

**标签**: `#Artificial Intelligence`, `#Mathematics`, `#Formal Verification`, `#Riemann Hypothesis`, `#AI-Assisted Proof`

---

<a id="item-tech-news-2"></a>
### [GPT-6 通过代码编写实现蛋白质 minbinders 设计](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10



hackernews · acossta · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

#### 摘要

OpenAI 报告称，GPT-6（具体为 GPT-6.2）在获得五个靶蛋白的三维结构并标记结合位点之后，能够直接编写代码来生成潜在 minbinders 的三维设计，无需依赖专门的蛋白质 AI 模型。该能力的核心在于代码编写——当任务本质上是&quot;编写更好的代码&quot;时，通用模型的进步能直接转化为设计能力的提升。然而，将三维设计转化为可测试的氨基酸序列仍需使用专门的工具模型（如 SolubleMPNN），后续的选择和验证阶段也离不开其他专用蛋白质模型的支持。

#### 背景

蛋白质设计需要同时处理三维结构建模与氨基酸序列预测两个相互关联的问题：给定目标结构推导出能在实验室中正确折叠的氨基酸序列（通常由如 SolubleMPNN 等专用模型完成），以及选择既满足折叠稳定性又具备正确结合位点的候选分子。这一领域长期依赖高度专业化的计算模型，各子任务之间存在紧密耦合。

#### 社区讨论

社区观点呈现分歧：一方认为 GPT-6 充当了连接多个专业模型的&quot;胶水层&quot;，在协调子任务方面可能超越专门模型的表现；另一方则质疑其实际贡献，指出&quot;序列即结构&quot;，而序列和筛选均由专用模型完成，因此蛋白质设计的实质成果应归功于哪些模型仍存争议。此外，有评论认为论文的实验证据偏重计算探索而缺乏充分的生物控制对照，增加了结果的局限性。

**标签**: `#artificial intelligence`, `#protein design`, `#software engineering`, `#machine learning`, `#biotechnology`

---

<a id="item-tech-news-3"></a>
### [AI 大模型一年三次拐点：从可靠编码到 3D 创作](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 8.0/10



rss · Simon Willison · 11月24日 23:02

#### 摘要

Simon Willison 在最近一次主题演讲中，回顾了过去一年内 LLM 和编程 Agent 能力发展的三个关键拐点。第一个拐点在 2025 年 11 月，Claude Opus 4.5 发布，使编程 Agent 首次具备日常可靠性；第二个拐点出现在 2026 年 6 至 7 月的 Fable 系列模型，这类模型能在给定目标和工具后通过自主推理解决问题；第三个拐点是 2026 年 9 至 10 月前沿模型在 3D 建模和游戏开发领域的能力跃升，Opus 5.5 更是展现出对&quot;趣味性&quot;的理解与迭代优化。

#### 背景

自 2025 年 2 月 Claude 3.7 Sonnet 附带推出 Claude Code 以来，编程 Agent 经历了约九个月的迭代期才达到可靠性临界点。此后，各厂商竞相发布新一代模型——OpenAI 的 GPT-5.1 系列、Anthropic 的 Fable 系列（其原型 Mythos 因网络安全风险过大而暂缓发布）、以及 Gemini 4 系列等——推动了能力的快速演进。2026 年下半年独立游戏界也因此出现围绕 AI 辅助开发的激烈文化争论。

#### 社区讨论

3D 建模和游戏开发能力的突破引发了独立游戏圈的深度分歧：部分人担忧 AI 辅助编程正在改变游戏创作的本质，甚至有前 Take-Two 高管称 GTA VI 可能是&quot;最后一个前生成式 AI 时代的 3A 大作&quot;。Willison 本人在 2026 年 8 月至 10 月间多次测试表明，AI 可生成视觉可信的作品并实现游戏性迭代，但&quot;设计一款真正有趣的遊戲&quot;是否仍为人类独有领域，目前尚无定论。

**标签**: `#LLMs`, `#coding agents`, `#AI models`, `#software engineering`, `#industry analysis`

---

<a id="item-tech-news-4"></a>
### [网页端编译 Firefox 与 LLM 代理企业忠诚度分析](https://zeli.app/zh/digest/2026-11-24) ⭐️ 8.0/10



rss · Zeli · 11月24日 23:59

#### 摘要

Domen Kožar 开发的 unkernel 技术已实现在浏览器内通过 WebAssembly 直接运行超过 30 万个 Nix 包，带来 2 至 32 倍性能提升，完整图形、音频和网络功能均可流畅运行，甚至实现了浏览器内的 Firefox 嵌套运行。与此同时，关于 LLM 代理的研究显示其决策逻辑往往优先遵循母公司商业与合规要求而非用户利益；作者在使用 Claude Code 时发现该工具拒绝绕过 Bandcamp API 验证却仍愿协助下载 YouTube 歌曲的案例揭示了这一偏向。此外，GTA 6 PC 移植项目在 Vulkan 引擎支持下仅用不到 24 小时便实现了近乎完整的着色器效果，Tidal 平台宣布将从 12 月 9 日起全面封禁 AI 生成音乐并清理约 2900 万首相关曲目。

**标签**: `#WebAssembly`, `#browser computing`, `#LLM agents`, `#Nix`, `#open source`

---

<a id="item-tech-news-5"></a>
### [亚马逊转向 SpaceX 与阿里安 6 发射卫星](https://arstechnica.com/space/2026/11/amazon-surges-launches-with-rival-spacex-after-ula-fails-to-deliver/) ⭐️ 8.0/10



rss · Ars Technica · 11月24日 18:30

#### 概述

亚马逊因联合发射联盟（ULA）未能交付而加速使用猎鹰 9 号和阿里安 6 火箭发射数百颗卫星。这一策略调整凸显了商业航天领域的竞争压力，并表明 SpaceX 与阿丽亚娜太空公司能够承担紧急发射任务。目前仍有大量卫星积压等待升空，反映出大型星座部署对可靠发射能力的依赖。

#### 背景

联合发射联盟由波音和洛克希德·马丁合资运营，长期是美国政府与商业客户的主要发射提供商之一，但近年多次出现发射延迟或失败。猎鹰 9 号与阿里安 6 作为可重复使用与重型运载火箭的代表，正在吸引更多商业合同以填补市场缺口。

**标签**: `#space`, `#satellite`, `#Falcon 9`, `#Ariane 6`, `#ULA`

---

<a id="item-tech-news-6"></a>
### [T3 Code 默认开启遥测并读取本机认证凭证](https://x.com/realchendahuang/status/2125153472450527440) ⭐️ 8.0/10



telegram · zaihuapd · 11月24日 10:58

#### 摘要

开发者 @realchendahuang 于 11 月 24 日发文指控 Theo 旗下 T3 Code 存在隐私问题。该项目自今年 3 月合并 PR \#174 后默认启用 PostHog 遥测，同年 10 月合并的 PR \#21506 进一步读取本机 ~/.codex/auth.json 和 ~/.claude.json 文件，提取 Codex 的 user\_id 和 Claude 的 accountUuid，并将其与设备 ID 进行无盐 SHA-256 哈希后上传至服务器。开发者称提交了四份关闭遥测的 PR 均被拒绝，且官方文档已承认浏览器和移动端的远程诊断追踪功能无法禁用。项目方及 @theo 尚未对此作出公开回应。

#### 背景

PostHog 是一家提供产品分析平台的开源公司，支持遥测数据的采集与可视化。PR \#174 使 T3 Code 默认开启 PostHog 遥测；PR \#21506 在读取本地认证文件时将凭证数据做无盐哈希上传，未采用加盐等安全措施保护标识符。

**标签**: `#open source`, `#privacy`, `#telemetry`, `#security`, `#AI tools`

---