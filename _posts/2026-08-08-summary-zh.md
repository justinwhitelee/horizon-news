---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> 从 141 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [SGLang v0.5.17 发布：Kimi K3 与 MiniMax-H3 首日支持](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepMind WeatherNext 在气旋预报上实现突破](#item-tech-news-2) ⭐️ 8.0/10
3. [macOS 屏幕共享高危漏洞 CVE-2026-65400，无需密码即可接管账户](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [SGLang v0.5.17 发布：Kimi K3 与 MiniMax-H3 首日支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.17) ⭐️ 8.0/10



github · Fridge003 · 8月8日 00:19

#### 摘要

SGLang v0.5.17 正式发布，包含来自 194 位贡献者的 582 个 PR。该版本新增对 Kimi K3 的首日支持——这是一个 2.8T 参数的多模态 LatentMoE 模型，拥有 100 万 token 上下文窗口和 MoonViT3d 视觉塔，采用 MXFP4 量化格式。同时支持 MiniMax-H3 视频生成模型，可在单次请求中生成视频与同步立体声音轨。其他重要更新包括 Rust 前端初始支持、DCP 通信后端扩展、MoE 预填充并行策略 DWDP，以及会话感知统一 Radix 缓存。验证硬件涵盖 NVIDIA GB300、B200、H100 和 AMD MI35x。

#### 背景

SGLang 是一个开源的大语言模型推理框架，专注于高效 serving 和推理优化。Kimi K3 是由 Moonshot AI 开发的 2.8T 参数多模态模型，采用 LatentMoE 架构（896 个专家，top-16 路由）。MiniMax-H3 是 MiniMax 的视频生成模型，支持文本到视频与音频的联合生成。

**标签**: `#AI inference`, `#LLM serving`, `#open source`, `#model deployment`, `#multimodal models`

---

<a id="item-tech-news-2"></a>
### [DeepMind WeatherNext 在气旋预报上实现突破](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10



hackernews · bhavansig · 8月8日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=49220126)

#### 摘要

DeepMind 宣布其 WeatherNext AI 模型在气旋预报方面取得突破性进展，性能超越传统数值天气预报（NWP）模型，同时推理效率高出数个数量级。该模型基于多层级图神经网络（hierarchical Graph Neural Networks）架构，延续了此前 Graphcast 的技术路线。社区评论指出，这类针对特定科学问题的专用 AI 模型比通用大语言模型更具实际影响力，其架构设计在气象预报领域具有开创性意义。

#### 社区讨论

社区普遍认为 WeatherNext 代表了 AI 在科学计算领域的重大突破，比当前的编程代理等应用更具实际价值。评论者特别提到多层级图神经网络架构值得深入研究，并推荐了原始 Graphcast 论文。部分讨论还延伸至气象预报能力对地缘政治的实际影响，以及个人用户通过 Zoom.Earth 等工具获取台风预报的体验。

**标签**: `#AI`, `#weather forecasting`, `#DeepMind`, `#graph neural networks`, `#scientific computing`

---

<a id="item-tech-news-3"></a>
### [macOS 屏幕共享高危漏洞 CVE-2026-65400，无需密码即可接管账户](https://x.com/calif_io/status/2086022794840793454) ⭐️ 8.0/10



telegram · zaihuapd · 8月8日 14:20

#### 摘要

安全研究人员公开了 macOS 屏幕共享功能中的关键漏洞 CVE-2026-65400 的 PoC。当屏幕共享处于开启状态时，任何网络攻击者均可在不知晓密码的情况下，以任意账户身份登录受影响的 Mac。苹果已在 macOS 26.6.1 中修复此漏洞，建议用户尽快升级。研究人员已逆向工程该补丁以厘清漏洞根因与利用路径，完整技术分析预计次日发布。

#### 背景

macOS 屏幕共享（Screen Sharing）是苹果内置的远程桌面功能，允许用户通过网络远程控制另一台 Mac。CVE-2026-65400 是近期披露的两项屏幕共享漏洞之一，另一项为 CVE-2026-43760；两者区别在于前者无需任何凭据即可利用，后者则需要攻击者掌握目标账户密码。该漏洞的根因在于认证过程中的状态管理缺陷，苹果通过改进状态管理逻辑在 macOS 26.6.1 中完成修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-65400">CVE - 2026 - 65400 : Authentication Vulnerability in macOS Products by...</a></li>
<li><a href="https://www.huntress.com/blog/macos-screen-sharing-rce-patched">From Screen Share to Root Access: Breaking Down CVE - 2026 -43760...</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-65400">NVD - CVE - 2026 - 65400</a></li>

</ul>
</details>

**标签**: `#macOS security`, `#vulnerability`, `#screen sharing`, `#CVE`, `#Apple`

---