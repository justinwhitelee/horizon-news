---
layout: default
title: "Horizon Summary: 2026-11-04 (ZH)"
date: 2026-11-04
lang: zh
---

> 从 196 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [BlackX UEFI bootkit bypasses Secure Boot on patched Windows systems](#item-tech-news-1) ⭐️ 9.0/10
2. [Qwen 3.8 27B 本地演示权重空间编程能力](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest 2026-11-03 · Postman 静默安装 AI 插件并共享 API 数据](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [BlackX UEFI bootkit bypasses Secure Boot on patched Windows systems](https://arstechnica.com/security/2026/11/uefi-bootkit-infected-fully-patched-windows-machines-is-microsoft-to-blame/) ⭐️ 9.0/10



rss · Ars Technica · 11月3日 16:03

#### Summary

A UEFI bootkit named BlackX has been identified as infecting fully patched Windows machines by exploiting ambiguities in Microsoft&\#x27;s Secure Boot protections. The attack targets firmware-level security, demonstrating that Secure Boot&\#x27;s current implementation leaves gaps that can be leveraged even on systems with all latest patches applied. This raises serious questions about Microsoft&\#x27;s responsibilities for firmware security and the trust chain involving hardware OEMs. The exploit highlights a significant vulnerability in widely deployed systems, where firmware-level compromise can bypass traditional patching mechanisms entirely.

#### 背景

UEFI（统一可扩展固件接口）是取代传统 BIOS 的现代固件标准，负责在操作系统加载前初始化硬件。Secure Boot（安全启动）是 UEFI 的一项安全特性，通过验证启动加载程序的数字签名，防止未授权的代码在系统启动早期运行，从而抵御 bootkit 等恶意软件。然而，Secure Boot 依赖 OEM 厂商预置的密钥数据库，且其规范存在一些模糊地带，攻击者可利用这些漏洞绕过保护。BlackX 利用的正是此类问题——它通过所谓&quot;Baton Drop&quot;漏洞绕过 Secure Boot，在系统固件层面加载恶意驱动。

**标签**: `#UEFI security`, `#Secure Boot`, `#firmware exploitation`, `#Windows security`, `#bootkit`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B 本地演示权重空间编程能力](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10



rss · Simon Willison · 11月3日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=50355251)

#### 摘要

Simon Willison 测试了开源模型 Qwen 3.8 27B 执行「权重空间编程」的能力，这是继 GPT-6 Astra 等前沿模型后首次在本地 accessible 模型上验证该技术。研究团队 Rikiya Takehi、Jayden Teoh、Alex Zhang 和 Omar Khattab 发表的论文《Sparks of Weight-Space Programming》表明，GPT-6 Astra 仅通过观察原始权重就能推断神经网络训练目标，甚至无需环境反馈即可从零编写出超越 PPO 训练 1 亿步的网络。Willison 使用 LM Studio 加载 17GB 的 Qwen 3.8 27B GGUF 模型（Q4\_K\_M 量化版本），在 8192 上下文窗口下运行测试：将 Pac-Man 游戏网络的浮点权重喂给模型后询问其训练目标。经过 46 分 12 秒和 43,506 个推理 token，Qwen 3.8 27B 以 72% 置信度正确识别出游戏类型。这一发现扩展了权重空间编程的适用范围，从闭源前沿模型延伸至本地可运行的开源模型。

#### 背景

权重空间编程（Weight-Space Programming）指大语言模型直接读取和修改神经网络原始权重的能力，无需运行代码或工具。该概念由 Rikiya Takehi 等人于 2026 年 11 月提出，论文将此类研究分类为「博客文章」但具备学术论文形态。研究团队训练了四个简单 10×10 网格版本的经典游戏网络——Breakout、Pong、Pac-Man 和 Freeway（后者是 1981 年 Atari 2600 游戏），然后将权重作为浮点数序列输入 LLM 进行识别测试。相关 GitHub 仓库位于 RikiyaT/lm\_understand-logs，实验提示词位于 exp1\_which\_game 文件夹。

#### 社区讨论

社区对此项发现存在分歧：variaga 引用莎士比亚《亨利四世》中关于「召唤灵魂」的台词质疑解释的正确性，认为「我能解释权重，但那解释会正确吗？」；zkmon 则盛赞 Qwen-3.8-27B 为「AI 领域最佳事件」，认为其能达到前沿模型同等结果，只需扮演高级架构师角色即可。data-ottawa 关注训练与理解的区别，质疑同代模型未训练过拆解该代模型的内容，询问有多少是真正理解权重而非模式匹配。层 8 评论称这不意味着源代码时代终结，未来可能像生物一样——AI 变得像那样编辑自身权重。

**标签**: `#AI research`, `#model interpretability`, `#weight manipulation`, `#open source models`, `#LLM capabilities`

---

<a id="item-tech-news-3"></a>
### [HN Digest 2026-11-03 · Postman 静默安装 AI 插件并共享 API 数据](https://zeli.app/zh/digest/2026-11-03) ⭐️ 8.0/10

HN digest covering Postman&\#x27;s controversial silent AI plugin installation raising trust and security concerns, and a technical debunking of exaggerated claims about weight-only AI model modification.

rss · Zeli · 11月3日 23:59

**标签**: `#AI tools`, `#developer tools`, `#ML methodology`, `#security`, `#API engineering`

---