---
layout: default
title: "Horizon Summary: 2026-10-26 (ZH)"
date: 2026-10-26
lang: zh
---

> 从 136 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Brotli 解码器高危漏洞可致远程代码执行](#item-tech-news-1) ⭐️ 8.0/10
2. [苹果将发布首款触屏 MacBook Pro](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Brotli 解码器高危漏洞可致远程代码执行](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 8.0/10

谷歌 Brotli 解码器曝出 CVE-2026-111497 高危漏洞，影响 Python 和 Node.js 等多个 HTTP 组件，攻击者可发送特制压缩流实现任意代码执行。

telegram · zaihuapd · 10月25日 02:42

#### 漏洞概况

谷歌 Brotli 解码器存在高危安全漏洞 CVE-2026-111497，影响 1.0.3 至 1.2.0 版本，CVSS 评分为 9.2。远程未认证攻击者可通过发送特制压缩流触发内存损坏、敏感数据泄露、进程崩溃，甚至可能执行任意代码。该漏洞最初以 Node2Shell 名称披露，后被称为 HTTP2Shell。Python 的 Brotli 需升级至 1.2.1，brotlicffi 至 1.2.1.0；Node.js 修复版本为 22.23.4、24.22.1 或 26.12.1。OpenAI 表示于今年 2 月发现该问题。

#### 背景信息

Brotli 是谷歌开发的通用无损压缩算法，广泛应用于 HTTP 压缩、Web 传输等领域。Python 和 Node.js 生态中的多个 HTTP 组件依赖 Brotli 进行数据解压，包括 requests、express 等流行库。该漏洞影响范围涉及数百万使用 Brotli 压缩的 Web 应用和服务。

**标签**: `#security vulnerability`, `#Brotli`, `#Python`, `#Node.js`, `#HTTP`

---

<a id="item-tech-news-2"></a>
### [苹果将发布首款触屏 MacBook Pro](https://www.bloomberg.com/news/newsletters/2026-10-25/apple-to-unveil-touch-screen-macbook-pro-executive-promotions-in-box-checker) ⭐️ 8.0/10

苹果将于本周三推出首款支持触控的 MacBook Pro，配备 OLED 屏幕与灵动岛，标志其长期坚持的笔记本无触控策略发生重大转变。

telegram · zaihuapd · 10月25日 14:25

#### 摘要

苹果将于本周三发布首款支持触控的 MacBook Pro，提供 14 英寸与 16 英寸版本，采用 OLED 显示屏并引入灵动岛功能，起售价高于现款 2499 美元机型。这是 Mac 产品线首次引入触控交互，终结了苹果高管多年以人体工学为由拒绝触屏笔记本的立场。触控设计将作为键盘和触控板的补充而非替代，主要驱动因素来自营收与营销考量。此次转变也反映出苹果在产品策略上更愿意反思和调整，不再固执己见或强行推动行业标准。

#### 背景

苹果长期以来坚持 Mac 系列笔记本电脑不支持触控功能，官方理由包括防止手指遮挡屏幕内容以及维护人体工学体验。OLED 显示屏能提供更高的对比度和更低的功耗，灵动岛则是苹果在 iPhone 14 Pro 系列上引入的动态交互设计，现已扩展至 MacBook 平台。

**标签**: `#Apple`, `#hardware`, `#touchscreen`, `#OLED`, `#MacBook`

---