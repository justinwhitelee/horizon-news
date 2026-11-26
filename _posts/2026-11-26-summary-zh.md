---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
---

> 从 184 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [FCC 授权 SpaceX 部署 100 万颗 AI 卫星](#item-tech-news-1) ⭐️ 9.0/10
2. [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest：1Password 安全事件与 AI 证明重大数学难题](#item-tech-news-3) ⭐️ 8.0/10
4. [Minecraft Java 版曝高危 RCE 漏洞，资源包字体可触发远程代码执行](#item-tech-news-4) ⭐️ 8.0/10
5. [三星、SK 海力士将获长江存储 Xtacking 技术授权](#item-tech-news-5) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [FCC 授权 SpaceX 部署 100 万颗 AI 卫星](https://arstechnica.com/space/2026/11/the-fcc-has-authorized-spacex-to-deploy-1-million-satellites/) ⭐️ 9.0/10



rss · Ars Technica · 11月25日 18:22

#### 概述

美国联邦通信委员会（FCC）于周三宣布，已批准 SpaceX 部署多达 100 万颗搭载 AI 芯片的卫星，作为其&quot;Starmind&quot;计划的一部分。这一星座将把轨道上的卫星数量增加约 50 倍，是太空基础设施和宽带通信领域的里程碑式决定。Google 和 Blue Origin 等公司也在探索将 AI 数据中心部署到太空的方案，但这是监管机构首次批准此类倡议。

#### 背景与技术意义

传统卫星星座（如 Starlink）主要提供互联网接入，而 Starmind 计划引入了完全不同的架构思路：每颗卫星都是一颗在轨 AI 计算节点。这种&quot;太空边缘计算&quot;范式意味着数据无需回传地球即可处理，大幅降低延迟并节省带宽成本。当前轨道上约有数千颗在轨卫星，100 万颗的数量级跃升涉及严重的碎片管理、频谱协调和发射节奏规划挑战。

**标签**: `#satellites`, `#space infrastructure`, `#telecommunications`, `#regulatory`, `#SpaceX`

---

<a id="item-tech-news-2"></a>
### [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

Scott Aaronson reacts enthusiastically to a new result placing the matrix multiplication exponent at 9/4, sparking extensive discussion on HackerNews about its significance and broader implications.

hackernews · Kotlopou · 11月25日 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**标签**: `#theoretical computer science`, `#algorithms`, `#computational complexity`, `#mathematics`

---

<a id="item-tech-news-3"></a>
### [HN Digest：1Password 安全事件与 AI 证明重大数学难题](https://zeli.app/zh/digest/2026-11-25) ⭐️ 8.0/10



rss · Zeli · 11月25日 23:59

#### 摘要

2026 年 11 月，1Password 遭遇安全事件，攻击者通过入侵员工 GitHub 账户获取部分源代码并窃取用户元数据，但零知识架构确保用户保险库（vaults）及加密密钥均未泄露，官方已将验证码从六位升至十位。与此同时，OpenAI 和 Anthropic 接连宣称在 AI 辅助下证明了多项理论计算机科学重大问题：矩阵乘法指数ω精确等于 9/4、VP≠VNP，以及广义黎曼猜想针对 Dirichlet L-functions 的机器验证；相关论文已发布预印本。此外，有关 OpenAI 或 Anthropic 找到破解 RSA 方法的传闻已在学术界引发讨论，但专家提醒即便 P 类分解问题解决也不等同于直接攻破 RSA。开源社区亦有动态：Windows 响度均衡功能被逆向移植至 Linux PipeWire，1998-2006 年经典 GPU 演示被移植到浏览器运行。

**标签**: `#security`, `#artificial intelligence`, `#theoretical computer science`, `#zero-knowledge architecture`

---

<a id="item-tech-news-4"></a>
### [Minecraft Java 版曝高危 RCE 漏洞，资源包字体可触发远程代码执行](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10



telegram · zaihuapd · 11月25日 12:46

#### 摘要

11 月 22 日公开的 minecraft2shell 项目披露了 Minecraft Java 版的高危远程代码执行漏洞：服务器资源包中的特制 TrueType 字体可触发 FreeType 库越界写入，进而允许攻击者在客户端执行任意代码。该漏洞影响 1.20.5 至 1.21.10 正式版及 26.1 至 26.4 快照版本，1.20.4 及更早版本和基岩版不受影响。Mojang 目前仍使用存在问题的 lwjgl-freetype 3.4.3，尚未发布官方补丁。社区临时修复方案 m2sfix 1.0.0 于 11 月 24 日发布，通过 Java Agent 或 Mod 关闭字体 hinting 以规避风险。

#### 背景

Minecraft Java 版使用 lwjgl-freetype 库来渲染字体，当加载服务器下发的资源包时会自动处理其中的 TrueType 字体文件。FreeType 是一个开源的字体渲染引擎，其 2.14.3 及更早版本存在越界写入漏洞，攻击者可通过精心构造的字体文件触发内存破坏，在特定条件下实现远程代码执行。此类漏洞在游戏平台中尤为危险，因为服务器资源包是玩家日常使用的正常功能。

**标签**: `#security vulnerability`, `#remote code execution`, `#Java`, `#gaming software`

---

<a id="item-tech-news-5"></a>
### [三星、SK 海力士将获长江存储 Xtacking 技术授权](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 8.0/10



telegram · zaihuapd · 11月25日 14:33

#### 摘要

三星电子和 SK 海力士已通过交叉许可协议，同意在 3D NAND 闪存中采用长江存储（YMTC）的 Xtacking 堆叠技术。Xtacking 的核心做法是将存储单元阵列和控制电路（CMOS）分别制作在两片晶圆上，再通过键合工艺将它们合并为一片，两部分可以各自独立生产和优化。Omdia 高级分析师指出，这一方案使厂商能够自行生产存储阵列，而将逻辑电路外包给晶圆代工厂，从而使用更先进的制程节点。三方均对此拒绝置评，但有分析认为，与传统 NAND 制造工艺相比，该键合方案具有明显优势。此举被视为全球内存芯片行业格局的一次重要转变——中国企业在先进存储领域的角色正从技术接受者逐渐转向技术输出方。

#### 背景：Xtacking 技术与长江存储

长江存储（YMTC）是中国主要的 NAND 闪存制造商，其 Xtacking 技术是一种 3D NAND 架构方案，将存储单元阵列和 CMOS 控制电路分别制造在两片晶圆上，再通过键合工艺合并，使两部分能够独立生产和优化。Omdia 分析师指出，这种设计允许厂商自行生产存储阵列，而将逻辑电路外包给代工厂以采用更先进制程。三星、SK 海力士与长江存储此前并无公开的交叉许可关系；2024 年长江存储曾在美国对美光提起诉讼，指控其 NAND 专利侵权（tool-1-1）。此次协议据日经新闻报道，三方均拒绝置评（tool-1-2，tool-1-3）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.trendforce.com/news/2026/11/25/news-sk-hynix-reportedly-joins-samsung-in-licensing-ymtcs-xtacking-technology-as-nand-race-heats-up/">[News] SK hynix Reportedly Joins Samsung in Licensing ...</a></li>
<li><a href="https://www.techpowerup.com/355199/samsung-and-sk-hynix-to-license-ymtcs-xtacking-technology">Samsung and SK hynix to License YMTC &#x27;s Xtacking ... | TechPowerUp</a></li>

</ul>
</details>

**标签**: `#semiconductor memory`, `#3D NAND`, `#chip manufacturing`, `#cross-licensing`, `#Y.M.Tech`

---