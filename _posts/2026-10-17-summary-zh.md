---
layout: default
title: "Horizon Summary: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
---

> 从 196 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Claude 揭示 NIST ECDSA 曲线的生成来源](#item-tech-news-1) ⭐️ 9.0/10
2. [Big Fish：利用 OpenBSD 中一个存在 37 年的内核漏洞](#item-tech-news-2) ⭐️ 8.0/10
3. [All the news about the iPhone Duo](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Claude 揭示 NIST ECDSA 曲线的生成来源](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10



hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

#### 摘要

Anthropic 的研究发现，NIST P-192、P-224、P-256、P-384 和 P-521 椭圆曲线种子均由 C 语言标准库中的 lrand48 伪随机数生成器产生，并以 Unix 时间戳作为种子。这一发现解决了密码学领域长达二十多年的悬而未决的问题，证实这些曲线并非通过复杂的哈希算法生成，而是源于一个简单的 PRNG。然而，第五个二进制种子 B-163 仍未找到匹配，可能的原因是在发布过程中发生了录入错误。

#### 社区讨论

社区普遍认为这一发现终结了针对 NIST 曲线的长期阴谋论，但也有人指出虽然方法已明确，仍无法排除通过搜索时间戳来有意选择特定属性的曲线。部分成员认为未解的 B-163 种子可能是发布时的输入错误所致。

**标签**: `#cryptography`, `#AI research`, `#NIST standards`, `#ECDSA`, `#open problems`

---

<a id="item-tech-news-2"></a>
### [Big Fish：利用 OpenBSD 中一个存在 37 年的内核漏洞](https://calif.io/research/big-fish) ⭐️ 8.0/10



hackernews · rs\_rs\_rs\_rs\_rs · 10月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50118977)

#### 摘要

研究论文《Big Fish》展示了在 OpenBSD 中发现并利用了一个存在 37 年的内核漏洞。该发现具有重要意义，因为 OpenBSD 是代码审计最为严格的操作系统之一，这样一个长期未被检测到的漏洞揭示了仅靠人工审查难以发现某些内核缺陷。研究团队通过针对性的漏洞利用分析，成功触发了这一经典漏洞原型。社区评论指出，该漏洞在 NetBSD 于 1999 年 8 月重写相关代码时被意外修复，进一步凸显了审计方法本身的局限性。

#### 背景

OpenBSD 以严格的代码审查和安全优先理念著称，其源代码库被广泛认为是最受审查的操作系统内核之一。正因如此，任何在 OpenBSD 中存活数十年的漏洞都格外引人注目。值得注意的是，AI 辅助漏洞发现已在安全研究界引发关注——Anthropic 的 Claude Mythos Preview 曾被报告自主发现了一个 OpenBSD 中存在 27 年的漏洞，而此次研究同样聚焦于一个长达 37 年的内核缺陷，反映出人类专家审查与自动化工具在漏洞检测方面的互补关系。

#### 社区讨论

社区成员对这一发现表示赞赏，并对该漏洞如何在高度审计的代码库中存活 37 年发出感叹。有评论指出 NetBSD 在 1999 年的代码重写中意外修复了同类问题。围绕审计局限性的讨论集中在：模糊测试（fuzzing）或静态分析是否足以发现此类漏洞，还是必须依赖人类研究者对漏洞原型的深入思考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/vidoc-security-lab_we-used-ai-to-find-0-days-in-the-linux-kernel-activity-7448293701514326020-7W6p">We used AI to find 0-days in the Linux Kernel before most people...</a></li>

</ul>
</details>

**标签**: `#kernel security`, `#vulnerability research`, `#OpenBSD`, `#exploit development`, `#code auditing`

---

<a id="item-tech-news-3"></a>
### [All the news about the iPhone Duo](https://www.theverge.com/tech/1010131/apple-iphone-duo-news-announcements) ⭐️ 8.0/10

Apple announces the iPhone Duo, its first foldable phone featuring dual displays, Touch ID, and minimal crease design.

rss · The Verge · 10月16日 23:36

**标签**: `#Apple`, `#foldable phone`, `#hardware`, `#mobile`, `#iPhone`

---