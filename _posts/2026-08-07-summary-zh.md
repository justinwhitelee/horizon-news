---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 192 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [ByteDance 训练万亿参数 AI 模型对标 Anthropic](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI 称新模型 Astra 或达关键网络攻击能力](#item-tech-news-2) ⭐️ 9.0/10
3. [DeepSeek V4 Flash 0731 本地部署性能与成本分析](#item-tech-news-3) ⭐️ 8.0/10
4. [Postgres 分析查询性能提升 300 倍的技术路径](#item-tech-news-4) ⭐️ 8.0/10
5. [HN Digest 2026-08-06：AMD 收购 Taalas、Qwen3.8 Max 登顶、ChatGPT 升级](#item-tech-news-5) ⭐️ 8.0/10
6. [台积电与研究人员在次纳米晶体管技术上取得突破](#item-tech-news-6) ⭐️ 8.0/10
7. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-tech-news-7) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [ByteDance 训练万亿参数 AI 模型对标 Anthropic](https://arstechnica.com/ai/2026/08/bytedance-trains-massive-ai-model-in-bid-to-rival-anthropic/) ⭐️ 9.0/10



rss · Ars Technica · 8月7日 13:29

#### 摘要

据《金融时报》报道，字节跳动正在训练一个拥有 10 万亿参数的超大规模人工智能模型，旨在直接与 Anthropic 竞争。这一举动标志着 AI 行业竞争格局的重大转变，体现了在模型规模上的显著突破。作为 TikTok 的母公司，字节跳动此举显示出其在通用人工智能领域的雄心。该模型规模远超当前主流大语言模型，可能重新定义行业竞争标准。

**标签**: `#AI`, `#Large Language Models`, `#Industry News`, `#ByteDance`, `#Anthropic`

---

<a id="item-tech-news-2"></a>
### [OpenAI 称新模型 Astra 或达关键网络攻击能力](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) ⭐️ 9.0/10



telegram · zaihuapd · 8月7日 16:44

#### 摘要

OpenAI 于 2026 年 8 月 7 日披露，其即将推出的模型 Astra 在内部评估中显示出代理编码与网络安全方面的重大进展，初步结果强到无法排除达到「关键」网络能力阈值的可能性。此前 GPT-5.6-Sol 等模型在该评估中仅被评为「高」。根据 OpenAI 的预备框架，达到关键阈值意味着模型可在无需人工干预的情况下，自主发现并利用加固真实系统的零日漏洞，或仅凭高层目标策划和执行端到端的新型网络攻击。公司已暂停不符合强化安全要求的 Astra 相关内部活动，实施隔离测试环境、加密增强、通用监控等措施，并将与政府机构和 AI 安全组织合作开展第三方测试。

#### 背景

OpenAI 的“准备框架”（Preparedness Framework）将模型能力分为不同等级，其中“关键”（critical）级别指模型具备自主发现并利用真实系统零日漏洞，或仅凭高层目标策划并执行端到端新型网络攻击的能力。此前 GPT-5.6-Sol 等模型在该评估中仅被评为“高”（high），而 Astra 是首个被 OpenAI 认定为达到“关键”网络安全阈值的模型。这一分类标志着 AI 代理编码与网络攻防能力进入新阶段，引发了对自主攻击性 AI 系统的监管与安全控制关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/">Responding to the next frontier of critical cyber capabilities | OpenAI</a></li>
<li><a href="https://www.axios.com/2026/08/07/openai-astra-model-delay-cybersecurity-risks">Exclusive: OpenAI slows release of Astra model citing cyber capabilities</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-locks-down-astra-after-model-raises-first-ever-critical-cyber-capability-fears">OpenAI flags Astra model for critical cybersecurity capabilities</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Cybersecurity`, `#OpenAI`, `#Autonomous Agents`, `#AI Governance`

---

<a id="item-tech-news-3"></a>
### [DeepSeek V4 Flash 0731 本地部署性能与成本分析](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek V4 Flash 0731 版本在本地部署中展现出显著的性能提升和极低的运行成本，社区反馈普遍积极，但部分用户报告了循环调用等稳定性问题。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

#### 摘要

DeepSeek V4 Flash 0731 版本发布后，社区用户反馈其在本地部署中表现优异，成本极低且性能足以应对大多数任务。用户 LaurensBER 报告在 Oh My Pi 上运行多个会话时，每日成本不足 5 美元，OpenCode Go 的临时双倍限制进一步降低了实际支出。ak\_t 指出该版本相比之前的预览版有显著提升，在 2x RTX Pro 6000 Blackwell 上预填充速度约为 8k tok/s，单流速度约为 250 tok/s，特别适合调试和文档分析。然而，nylonstrung 报告在使用 Pi agent 时遇到无限循环和工具调用失败的问题，模型有时会偏离主题生成无关内容。

#### 背景

DeepSeek V4 Flash 是 DeepSeek 推出的轻量级开源模型，旨在提供高性价比的本地部署方案。0731 版本是对此前预览版的重大更新，优化了推理速度和稳定性。RTX Pro 6000 Blackwell 是 NVIDIA 推出的高性能 GPU，适用于大模型本地推理。Oh My Pi 和 Pi agent 是基于 Raspberry Pi 的本地 AI 部署工具，适合资源受限环境。

#### 社区讨论

社区普遍认可 DeepSeek V4 Flash 0731 的成本效益和性能，但部分用户报告了稳定性问题，如无限循环和工具调用失败。讨论中夹杂了与主题无关的 Claude 账户被封禁的 anecdote，分散了技术焦点。

**标签**: `#AI Models`, `#Local LLMs`, `#Open Source`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### [Postgres 分析查询性能提升 300 倍的技术路径](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

作者详细介绍了通过批处理、算子融合和 SIMD 优化使 Postgres 分析查询提速 300 倍的技术方案，并回应了社区对正确性与信任度的关注。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

#### 摘要

作者 Malis Per 在博客中详细阐述了如何通过批处理执行、算子融合和 SIMD 向量化优化，将 Postgres 的分析查询性能提升高达 300 倍。这些优化主要针对分析型工作负载，通过减少函数调用开销、合并相邻算子以及利用 CPU 向量指令来加速数据处理。作者同时推出了名为 pgrust 的替代实现，并强调正确性是其首要优先级，目前已通过形式化验证和差分模糊测试证明超过 1000 个用户可见函数与 Postgres 逻辑一致。社区讨论聚焦于信任与性能的权衡，部分用户认为即使技术更优，非 Postgres 核心团队维护的项目也难以获得长期信任，但也有用户期待自适应查询规划等特性的引入。

#### 社区讨论

作者亲自回应了关于 pgrust 信任度的问题，强调已通过形式化验证和模糊测试确保正确性。社区用户 sgt 指出，即使技术更优，非 Postgres 核心团队维护的项目也难以获得长期信任，因为信任不仅关乎性能，还涉及技术的 longevity 和连续性。用户 AsyncBanana 表达了对自适应查询规划的期待，认为该项目证明了该模型在非学术场景的可行性。用户 rastignack 则询问是否解决了 IO 调度和线程调度中的 noisy neighbor 问题。

**标签**: `#database optimization`, `#Postgres`, `#SIMD`, `#query engine`, `#operator fusion`

---

<a id="item-tech-news-5"></a>
### [HN Digest 2026-08-06：AMD 收购 Taalas、Qwen3.8 Max 登顶、ChatGPT 升级](https://zeli.app/zh/digest/2026-08-06) ⭐️ 8.0/10

本期 HN 摘要涵盖 AMD 收购 AI 芯片初创公司 Taalas、Qwen3.8 Max 在 agentic index 榜单登顶、ChatGPT 升级 GPT-5.6 等科技动态，同时包含 Mario Kart 8 帕累托优化分析与 Rust 性能优化技巧。

rss · Zeli · 8月6日 23:59

#### 摘要

AMD 宣布收购 AI 芯片初创公司 Taalas，后者采用将模型权重直接刻录到硅片的 MSIC 技术，首款测试芯片 HC1 在运行 Meta Llama 3.1 8B 模型时达到每秒 16,960 个 token，远超 Nvidia GPU 和 Cerebras 加速器。独立评测机构 Artificial Analysis 更新榜单，Qwen3.8 Max 凭借在 GDPval-AA v2 和𝜏³-Banking 等代理任务中的表现登顶 agentic index 榜首。OpenAI 宣布 ChatGPT 升级至 GPT-5.6，Plus 和 Pro 用户可使用 GPT-5.6 Sol 模型并新增思考深度调节滑块，免费用户默认切换为 GPT-5.6 Luna 并获得无限文本对话权限。

#### 背景

Pareto front（帕累托前沿）是多目标优化中的核心概念，指一组无法被其他方案在所有目标上同时超越的解集合。MSIC（模型专用集成电路）是一种将 AI 模型权重直接嵌入硅片的定制化芯片技术，与依赖 HBM 存储的传统 GPU 推理方式不同，有望大幅提升推理性能并降低成本。

#### 社区讨论

本期摘要未提供社区评论数据，无法总结共识或分歧。

**标签**: `#AI Hardware`, `#M&amp;A`, `#Optimization`, `#Tech News`, `#Open Source`

---

<a id="item-tech-news-6"></a>
### [台积电与研究人员在次纳米晶体管技术上取得突破](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOeENnZnVXeklGQ0l3MVQ0cUp4c09JZVR2RnZhdHBOY3NtbkR0WTNlRWZxV2d2SUMxYl9TekdDbG5wRXVQU2pkWlVKYWNZVWZjWlhmNzQ3YWVUdlVvWEZsTXFnaFB2VklJX2ZKc2tXVk9POXBzZXViMDJUYUxhRGZkS1pRU3lPT2J5RVBucHZnTTdSMU1aQzJiblRocktJalBjMkplSE5yN091ZXFSY3AwVmx2dlMyWDhrYnpKbEhkRWVVcUFzQUlibUhrYmtVWi1hbWxQQUJmalNvNTJUNWVFUzVSLUVYbndHMkHSAe8BQVVfeXFMUFkxNkluS0wybnl6WHdMeTFJbFBDak9UQnpFblF4a3d0aWhjUTNUV3lxbDhUZjBaZk5KbVpvM3FTWGpNLU9Lc25hTlJNbWRCZ3d0RkhHS3NDekJHeHJJVFlid3RkdkZwU0xlRzhVX3ZGTkczaE1YYks4Z21mTElQcHdiZHpqV1pJVDd2NVF0TmFnZmNabmE2MW9YUjhsdlduNVFXaWRjb0JPY21sSGtvdjBmTnZVbXJJWjdsblItcWVPYlp0Q3NzQjBmZ2tIZ1BxbnR1ZndkMHpUSWtlNlZZVVk4bjFoYU02SWFwV3E5M0k?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · 8月7日 16:16

#### 摘要

台积电（TSMC）与研究人员宣布在芯片晶体管技术上取得重大突破，这是其向次 1 纳米（sub-1-nanometer）制程技术迈进的重要组成部分。这一进展代表了半导体物理和制造领域的显著 advancement，旨在突破现有纳米级制造的技术瓶颈。尽管具体技术细节未在报道中详述，但该突破对于推动下一代高性能、低功耗芯片的发展具有重要意义。

**标签**: `#semiconductors`, `#hardware`, `#transistor technology`, `#manufacturing`, `#nanotechnology`

---

<a id="item-tech-news-7"></a>
### [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10



telegram · zaihuapd · 8月7日 11:18

#### 摘要

美国商务部工业与安全局（BIS）正系统性审查中国 AI 企业通过海外远程云计算获取英伟达芯片的渠道，包括整理黑市所在地和中国企业租用算力国家的名单。此次审查源于上月月之暗面发布 Kimi K3 模型后，一名白宫高官公开指控其非法获取芯片并经泰国远程访问。尽管远程访问本身不违法，美国众议院已通过两党法案拟明确授予 BIS 限制此类云计算协议的权力，但预计会遭英伟达等科技公司反对。报道还提及阿里巴巴通过开曼实体控制的新加坡壳公司，经被美方调查的 Megaspeed 使用位于马来西亚的英伟达芯片。

**标签**: `#AI policy`, `#hardware access`, `#Nvidia`, `#export controls`, `#cloud computing`

---