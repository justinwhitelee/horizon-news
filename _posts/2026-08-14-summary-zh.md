---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 193 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [macOS 屏幕共享零日漏洞正遭主动利用](#item-tech-news-1) ⭐️ 9.0/10
2. [GLM-5.3：具有自主安全研究能力的前沿编程模型](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest 2026-08-13：Gemini 3.7 Flash 发布与多项 AI/ML 进展](#item-tech-news-3) ⭐️ 8.0/10
4. [法官责令谷歌一周内取消第三方应用商店安装障碍](#item-tech-news-4) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [macOS 屏幕共享零日漏洞正遭主动利用](https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/) ⭐️ 9.0/10



rss · Ars Technica · 8月14日 18:32

#### 概述

Ars Technica 报道，macOS 中存在一个允许攻击者在无需密码的情况下远程访问屏幕共享的零日漏洞，目前已在野外被主动利用。该漏洞可使攻击者获得对 Mac 的全面控制权，无需用户身份验证即可完成远程屏幕共享登录。对于依赖 macOS 的软件工程师和安全从业者而言，这构成了直接且紧迫的安全威胁。目前尚不清楚受影响的具体 macOS 版本范围，用户应关注 Apple 后续的安全补丁更新。

#### 背景

macOS 的屏幕共享功能允许授权用户或管理员远程控制 Mac，常用于技术支持和远程访问。该功能存在一项被标记为 CVE-2026-65400 的漏洞，攻击者无需密码即可利用此漏洞获取完整系统控制权，并在真实环境中被用于加密货币挖矿等恶意活动。该漏洞影响范围不限于同一局域网，任何网络中的攻击者均可利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servnetuk.com/news/macos-screen-sharing-vulnerability-exploit-2026">macOS Screen Sharing Vulnerability Exploited in 2026</a></li>
<li><a href="https://www.anonymoushackers.net/apple-news/macos-security-warning-critical-screen-sharing-vulnerability-fixed-in-latest-update/">macOS Security Warning: Critical Screen Sharing Vulnerability Fixed...</a></li>

</ul>
</details>

**标签**: `#macOS security`, `#zero-day vulnerability`, `#remote code execution`, `#active exploitation`, `#Apple software`

---

<a id="item-tech-news-2"></a>
### [GLM-5.3：具有自主安全研究能力的前沿编程模型](https://z.ai/blog/glm-5.3) ⭐️ 8.0/10



hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

#### 摘要

Z.ai 发布了前沿 AI 模型 GLM-5.3，该模型在自动化编码和自主安全研究方面展现出显著能力，包括对开源软件进行自主漏洞发现。Z.ai 同时公开了 cvd.z.ai，披露了从广泛流行软件中发现的诸多 CVE，其中不少被评定为严重或高危级别。HN 社区讨论了该模型在红队场景中的实际应用，有用户报告其能够执行 WP 插件 0-day 挖掘、RCE 利用及 Linux 6.8 内核漏洞适配等任务。评论中还将 GLM-5.3 与 Sol、Fable、Mythos 5 等模型进行了性能比较，并关注了未来通过量化在本地部署的可能性。

#### 背景

Z.ai 是一家中国初创公司，其 GLM 系列大语言模型基于清华大学团队开发的开源 LLM 生态。GLM-5.3 以 GLM-5.2 为基础模型进行后训练，专注于长周期工程任务和安全研究，提供三种思考深度等级和 100 万 token 上下文窗口。在内部 Code Bench 编码基准上，GLM-5.3 相比前代提升了约 50%。

#### 社区讨论

HN 社区对 GLM-5.3 的技术能力持积极态度，有用户报告其在红队演练中表现出接近 Sol 和 Fable 的水平，但也有评论认为距离顶级模型仍有差距。社区关注了该模型商业化成本上升的问题（用户从 18 美元订阅快速升级至 80 美元计划），以及 Anthropic Project Glasswing 等竞品在同类任务上的进展。讨论还涉及该模型对开发者经济的影响，以及是否足以动摇 OpenAI 的市场地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theunum.io/en/news/read/chinese-startup-z-ai-has-introduced-the-glm-53-language-model-for-programming">Chinese startup Z ai has introduced the GLM - 5 . 3 language model for...</a></li>
<li><a href="https://www.together.ai/models/glm-5-3">GLM - 5 . 3 API: Pricing, Benchmarks &amp; Docs | Together AI</a></li>

</ul>
</details>

**标签**: `#AI models`, `#automated security research`, `#LLM releases`, `#open-source vulnerability scanning`, `#software engineering tools`

---

<a id="item-tech-news-3"></a>
### [HN Digest 2026-08-13：Gemini 3.7 Flash 发布与多项 AI/ML 进展](https://zeli.app/zh/digest/2026-08-13) ⭐️ 8.0/10

Google 正式发布 Gemini 3.7 Flash 原生多模态推理模型，支持 104 万输入 token 和 6.5 万输出 token，同时 DeepSeek 推出开源智能体框架 DeepSeek Harness。

rss · Zeli · 8月13日 23:59

#### 摘要

Google 正式推出 Gemini 3.7 Flash，作为 Gemini 3 系列最新高性能原生多模态推理模型，支持文本、图像、视频、音频及 PDF 等输入格式，输入 token 上限达 104 万，输出上限 6.5 万，引入可调节强度的 Thinking 模式（低/中/高三档），全面支持代码执行、函数调用和基于 Google Maps 的地理 grounding。DeepSeek AI 同步发布开源智能体框架 DeepSeek Harness（dsh），采用 Cordis 架构，核心理念为

**标签**: `#AI models`, `#open source`, `#agent frameworks`, `#multimodal AI`

---

<a id="item-tech-news-4"></a>
### [法官责令谷歌一周内取消第三方应用商店安装障碍](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10



telegram · zaihuapd · 8月14日 09:55

#### 概述

美国地区法官 James Donato 下令谷歌在一周内简化竞争对手安卓应用商店的安装流程，删除 Play Store 中的多余步骤与警告弹窗。法院认定这些要求在安装前需先&quot;查看&quot;等多步操作属于蓄意制造的&quot;反竞争摩擦&quot;，目的是吓退普通用户。该指令源自 Epic 诉谷歌反垄断案，此前陪审团已裁定谷歌在安卓应用分发市场构成非法垄断。

#### 背景

Epic 诉谷歌案是美国近年来最受关注的科技反垄断诉讼之一。2023 年，陪审团认定谷歌通过控制 Google Play 应用商店排挤竞争对手，构成了安卓应用分发市场的非法垄断。此命令是该案判决后的一项具体救济措施，旨在消除第三方应用商店在安卓设备上安装时的用户界面障碍。

#### 社区讨论

暂无社区评论。

**标签**: `#antitrust`, `#Android`, `#app distribution`, `#Google`, `#regulation`

---