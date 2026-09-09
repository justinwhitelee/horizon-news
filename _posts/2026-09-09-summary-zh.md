---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> 从 203 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [OpenAI 声称破解纳维-斯托克斯问题引发数据使用争议](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepMind 发布 AlphaGenome Atlas：人类 DNA 高解析度预测图谱](#item-tech-news-2) ⭐️ 8.0/10
3. [Kimi K3 2.8T 模型在 MacBook Pro 上通过 SSD 流式传输以 1 token/s 运行](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 声称破解纳维-斯托克斯问题引发数据使用争议](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/) ⭐️ 9.0/10



reddit · r/MachineLearning · /u/Shizuka\_Kuze · 9月8日 17:42

#### 主要内容

OpenAI 宣布使用内部模型成功证明纳维-斯托克斯存在性与光滑性问题，该问题是克雷数学研究所七个千禧年大奖难题之一，悬赏金额为 100 万美元。OpenAI 团队于 2026 年 9 月 1 日听闻相关传闻后启动项目，约 88 小时后智能体获得解答，随后花费 17 小时通过 GPT-6 Astra 完成 Lean 形式化验证；在整个尝试过程中共发送 490 万条消息、消耗约 3000 亿输出 token。争议随即而来：纽约大学数学教授 Tristan Buckmaster 与 Anthropic 研究员 Levent Alpöge 称其团队在过去一年中大量使用 Claude 和 Codex（主要为 GPT-5.6 Sol）研究同类问题，OpenAI 虽否认在求解过程中直接访问任何用户数据，但承认&quot;无法排除基于其产品使用的去标识化数据间接帮助改进模型&quot;的可能性，而双方证明方法亦存在显著差异。这一事件引发了关于 AI 模型训练数据来源透明度及数学研究伦理的广泛讨论。

#### 背景信息

纳维-斯托克斯方程描述流体运动的偏微分方程组，其解的存在性与光滑性问题自 19 世纪以来一直是数学与物理学的核心难题，被克雷数学研究所于 2000 年列入七个千禧年大奖难题之一。Lean 是一种形式化证明助手，可用于将数学证明转化为机器可验证的形式，在 AI 辅助定理证明领域具有重要意义。

**标签**: `#artificial intelligence`, `#machine learning`, `#mathematics`, `#research`, `#open source`

---

<a id="item-tech-news-2"></a>
### [DeepMind 发布 AlphaGenome Atlas：人类 DNA 高解析度预测图谱](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10



hackernews · utiiiD · 9月8日 14:55 · [社区讨论](https://news.ycombinator.com/item?id=49611251)

#### 摘要

Google DeepMind 发布了 AlphaGenome Atlas，这是人类基因组所有可能单核苷酸变化的精准预测图谱，将 DeepMind 的 AI 生物工具从蛋白质领域扩展至基因组学。该资源涵盖非编码 DNA 区域，可辅助研究人员解读致病突变与功能变异。目前 Atlas 已可通过 AntiGravity 平台供科学家访问使用，同时配套有入门教程视频。

#### 背景

AlphaGenome Atlas 是 Google DeepMind 推出的预测性基因组图谱，覆盖人类基因组中所有约 90 亿种可能的单核苷酸变异（人类基因组约含 30 亿个碱基对，每个位置最多有三种单核苷酸替换可能）。该工具基于此前 AlphaFold 系列模型在蛋白质结构预测上的积累，将 AI 驱动的生物预测扩展至非编码区基因组，涵盖启动子等调控序列的分子效应与 AVI（活动变异指数）评分。人类基因组中大部分序列属于非编码区，其功能注释一直是遗传学研究中的难题，此类预测图谱有助于解读致病突变与功能变异。

#### 社区讨论

社区讨论了访问方式、应用场景及模型比较等话题。有用户询问是否可用于分析 23andMe 基因组数据以识别致病变异；也有评论指出 DeepMind 此前部分生物学模型的影响力不及 AlphaFold，效果参差不齐。另有意见提到当前发布内容未充分讨论启动子序列及基因表达浓度层面的预测能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas : Molecular predictions for 9 Billion human DNA ...</a></li>
<li><a href="https://theoutpost.ai/news-story/google-deep-mind-unveils-alpha-genome-atlas-with-9-billion-human-genome-mutation-predictions-30577/">Google DeepMind &#x27;s AlphaGenome Atlas Maps 9 Billion Human ...</a></li>
<li><a href="https://spectrum.ieee.org/alphagenome-atlas">AlphaGenome Atlas Maps 9 Billion Possible DNA Variants</a></li>

</ul>
</details>

**标签**: `#AI for biology`, `#genomics`, `#DeepMind`, `#variant prediction`, `#computational biology`

---

<a id="item-tech-news-3"></a>
### [Kimi K3 2.8T 模型在 MacBook Pro 上通过 SSD 流式传输以 1 token/s 运行](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10



hackernews · Argonautlabs · 9月8日 20:07 · [社区讨论](https://news.ycombinator.com/item?id=49616257)

#### 摘要

Argonautlabs 在 GitHub（deltafin 项目）上展示了在 MacBook Pro 上运行 2.8 万亿参数 Kimi K3 模型的技术成果，推理速度约为每秒 1 个 token。该方案通过将模型权重从四个 SSD 流式传输到内存，克服了 Apple 设备 RAM 不可升级的硬件限制。社区对此评价不一：有评论者认为这是&\#x27;一个好的开始&\#x27;，暗示当前仍远未达到完全本地运行的理想状态，也有人提到完整 medium prompt 仅用了 11 天。这一工程尝试被视为消费者硬件上运行超大规模语言模型的重要探索。

#### 背景

Kimi K3 2.8T 是一个拥有 2.8 万亿参数的混合专家（MoE）大语言模型，其完整模型大小约 1.7 TB，远超任何消费级 Mac 的内存容量（例如 M5 Max MacBook Pro 配备 128 GB RAM）。Deltafin 是一种开源推理引擎，采用 SSD 流式传输技术，将每个（层、专家）以约 17.5 MB 的独立文件存储，并通过 pread + F\_NOCACHE 按需从磁盘读取，而非全部加载到内存中。该架构配合 Apple Metal/MPS 加速，利用四块 SSD（通过 Thunderbolt 5 扩展坞连接）实现参数流的低延迟访问，从而在消费级硬件上运行超大规模 MoE 模型。

#### 社区讨论

社区评论呈现积极但谨慎的态度：mandeepj 称其为&\#x27;好的开始&\#x27;，暗示本地运行 2.8T 模型的能力尚不成熟；dusted 提到完整 medium prompt 仅用 11 天完成，显示了可行性；amelius 将 SSD 流式传输与 Apple 不可升级 RAM 的架构限制联系起来，并引用了&\#x27;640KB 足够任何人&\#x27;的经典案例作类比；bluechair 对 SSD 的连接方式提出了技术疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49616257">Kimi K 3 ( 2 . 8 T ) at 1 token/s on a MacBook Pro , streamed from four...</a></li>
<li><a href="https://www.youtube.com/watch?v=_XrEgAQwweg">Kimi K 3 on a MacBook : How 1.56 TB Runs on 64 GB ( Deltafin )</a></li>
<li><a href="https://github.com/topics/ssd-streaming">ssd - streaming · GitHub Topics · GitHub</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#large language models`, `#hardware efficiency`, `#open source`, `#local deployment`

---