---
layout: default
title: "Horizon Summary: 2026-09-23 (ZH)"
date: 2026-09-23
lang: zh
---

> 从 208 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [OpenAI 发布 GPT-6 Sol 和 Luna 模型，定价大幅下调](#item-tech-news-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5，OpenAI 推出 GPT-6 Sol/Luna，双雄降价竞逐](#item-tech-news-2) ⭐️ 9.0/10
3. [vLLM v0.30.0 发布：新增 DeepSeek-V4.1、FP4 支持、Fast Start GPU 缓存](#item-tech-news-3) ⭐️ 8.0/10
4. [Claude Opus 5.5](#item-tech-news-4) ⭐️ 8.0/10
5. [Claude Opus 5.5 多档位推理性能与定价分析](#item-tech-news-5) ⭐️ 8.0/10
6. [Claude Opus 5.5 与 GPT-6 系列发布，价格战白热化](#item-tech-news-6) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 发布 GPT-6 Sol 和 Luna 模型，定价大幅下调](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10



hackernews · OfficialTurkey · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

#### 摘要

OpenAI 正式发布 GPT-6 Sol 和 GPT-6 Luna 两款新模型。社区反馈显示，GPT-6 Luna 的定价仅为 GPT-5.6 Luna 的一半，这是一项重大降价。开发者同时关注到 GPT-6 Astra 的价格对比数据。部分长期使用 5.6 系列的开发者担心新一代模型虽然技术更强，但在协作手感上可能不如从前自然。关于使用配额，Codex 在 20x 计划下的可用性被认为优于 Claude Code，而 ChatGPT Plus 用户反映 Plus 订阅已基本实现不限量的使用体验。

#### 社区讨论

社区讨论集中在价格下降幅度、模型使用手感的变化以及不同平台间的套餐对比。有开发者表达了对 5.6 Sol 的偏好，认为其沟通风格和工程直觉更契合，担心升级版虽更强但合作感会下降。另有用户整理了 GPT-6 系列各模型的 pelicans 图表用于横向对比价格。关于配额，Codex Pro 20x 计划因无明确用量限制而更受青睐，尽管存在 20x 与 5x 计划之间非线性的用量计算问题。

**标签**: `#AI models`, `#machine learning`, `#product release`, `#OpenAI`, `#LLMs`

---

<a id="item-tech-news-2"></a>
### [Anthropic 发布 Claude Opus 5.5，OpenAI 推出 GPT-6 Sol/Luna，双雄降价竞逐](https://zeli.app/zh/digest/2026-09-22) ⭐️ 9.0/10



rss · Zeli · 9月22日 23:59

#### 摘要

Anthropic 正式推出 Claude Opus 5.5，作为 Claude 5.5 家族首款模型，其性能对标 Claude Fable 5.1，但输入输出 Token 成本降低 40%，同时 Pro、Max 和 Team 计划用量上限提升。OpenAI 紧随其后发布 GPT-6 Sol 和 GPT-6 Luna，API 价格较 GPT-5.6 系列直接下调 50%，在 AutomationBench 和 DeepSWE 等基准测试中超越竞品，并优化了 Prompt Caching 机制最高节省 90% 缓存成本。两大厂商在同一周期内大幅降价并提升性能，标志着主流 LLM 推理成本进入新一轮下行通道，对依赖 AI API 的软件工程和自动化应用将产生直接影响。Anthropic 还宣布将 Claude Opus 5.5 提交至开源项目 ClaudeForFoundationModels，支持从 low 到 max 的全层级 effort 设置及 adaptiveThinking、structuredOutput 等高级特性。

#### 背景

Claude 5.5 是 Anthropic 于 2026 年推出的模型代际系列，Opus 为该系列中的高性能旗舰定位；GPT-6 系列在 GPT-5.6 之后演进，Sol 与 Luna 为不同性能档位的子型号。Prompt Caching（提示词缓存）是主流云厂商提供的 API 优化功能，可将重复输入 token 的计费次数大幅削减，对高频调用场景尤为关键。

**标签**: `#AI models`, `#machine learning`, `#API pricing`, `#software engineering`, `#LLM benchmarking`

---

<a id="item-tech-news-3"></a>
### [vLLM v0.30.0 发布：新增 DeepSeek-V4.1、FP4 支持、Fast Start GPU 缓存](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 0.30.0 正式发布，包含 762 个提交、315 位贡献者，带来多项性能优化与新模型支持。

github · khluu · 9月22日 05:20

#### 发布摘要

vLLM v0.30.0 正式发布，包含 762 个提交、315 位贡献者（新增 104 位）。主要亮点包括：新增 Fast Start 持久 GPU 权重缓存（通过 \`--load-format ipc\_cache\` 避免磁盘重载）、DeepSeek-V4.1-Flash/GLM-5.3/K2-Horizon/Cohere Compass 等新模型支持、NVFP4/FP4 量化检查点优化、HiSparse 稀疏 MLA 主机内存溢出机制、多节点张量并行改进，以及 Model Runner V2 的 gc 冻结（引擎初始化从 28.9s 降至 8.2s）。

#### 背景

vLLM 是开源的大语言模型推理引擎，广泛用于生产环境部署 LLM。v0.30.0 在模型覆盖、量化优化和规模化服务方面有显著增强，特别是针对 DeepSeek-V4 系列的完整 FP8/MXFP8 支持和 CUDA SM100 硬件级优化。

**标签**: `#LLM inference`, `#vLLM`, `#GPU optimization`, `#model serving`, `#open source`

---

<a id="item-tech-news-4"></a>
### [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) ⭐️ 8.0/10

Anthropic&\#x27;s release of Claude Opus 5.5, featuring improved natural communication, significant price reductions, and community discussion around frontier pacing commitments.

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**标签**: `#AI models`, `#LLM releases`, `#cloud pricing`, `#Anthropic`, `#open source community`

---

<a id="item-tech-news-5"></a>
### [Claude Opus 5.5 多档位推理性能与定价分析](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 8.0/10



hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

#### 摘要

Artificial Analysis 对 Claude Opus 5.5 在不同推理档位（Max、XHigh、Medium）下的基准测试和定价进行了横向对比分析。Max 档位提供最高推理能力，但每个任务消耗 128,000 token 的推理预算，部分用户反馈模型在执行复杂任务时会出现预算耗尽、推理中断的情况。与 Opus 5 高努力模式相比，Opus 5.5 的单位任务成本降低约一半，显示出明显的定价优化。社区同时讨论了模型发布后性能回归的风险，以及闭源基础模型仅比开源权重模型略优但价格相差约 100 倍的性价比问题。

#### 社区讨论

部分用户对推理档位差异和 Max 档位的 128,000 token 预算限制表示关注，指出在某些生成任务中模型会因推理超预算而中断。另有评论提到模型发布数周后可能出现性能回落，并类比其他模型供应商发布后性能退化的案例。关于性价比，社区普遍认为当前顶级闭源模型与高质量开源替代方案之间仍存在巨大价差，引发对商业模式的担忧。

**标签**: `#artificial intelligence`, `#large language models`, `#model evaluation`, `#AI pricing`, `#LLM benchmarks`

---

<a id="item-tech-news-6"></a>
### [Claude Opus 5.5 与 GPT-6 系列发布，价格战白热化](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 8.0/10



rss · Simon Willison · 9月22日 23:46

#### 概述

Anthropic 于 2026 年 9 月 22 日发布 Claude Opus 5.5，OpenAI 随后发布 GPT-6 Sol 和 GPT-6 Luna。GPT-6 Luna 输入价格为每百万 token 0.10 美元、输出为 0.50 美元，约为 GPT-5.6 Luna 的一半；GPT-6 Sol 同样降价约 50%，输入 2 美元、输出 10 美元。Claude Opus 5.5 较前代降价 20%，输入从 5 美元降至 4 美元、输出从 25 美元降至 20 美元，缓存读取费用降低 60%。作者测试发现 Claude Opus 5.5 在 max 思考级别下因过度推理而超出 128,000 输出 token 上限导致任务失败，引发对 max 模式实用性的质疑。OpenAI 此前发布的 Grok 4.7（输入 2 美元、输出 6 美元）与 GPT-6 Sol 形成直接竞争，中端模型价格战持续加剧。Anthropic 已预告 Sonnet 5.5 和 Haiku 5.5 即将发布。

**标签**: `#AI models`, `#Large language models`, `#Pricing`, `#Product announcements`, `#Software engineering`

---