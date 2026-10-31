---
layout: default
title: "Horizon Summary: 2026-10-31 (ZH)"
date: 2026-10-31
lang: zh
---

> 从 196 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [Azure 曝五起跨租户漏洞，含可伪造的管理员同意回调](#item-tech-news-1) ⭐️ 8.0/10
2. [官方 Claude Code 扩展被植入 SSH 后门](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic 成为 SpaceX 最大单一客户，年度算力合约最高 1205 亿美元](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Azure 曝五起跨租户漏洞，含可伪造的管理员同意回调](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 8.0/10

安全研究员披露了 Azure 中的五起完整跨租户漏洞，其中一起涉及可伪造的管理员同意回调，暴露了租户 ID 相关的安全风险。

hackernews · swq115 · 10月30日 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50301854)

#### 摘要

安全研究员在 Azure 中披露了五起完整的跨租户漏洞，其中包括一个可伪造的管理员同意回调，该问题与租户 ID 暴露有关。其他漏洞还涉及路径遍历和 IDOR（越权访问）等问题。微软文档虽然已注明

#### 背景

Azure 采用多租户架构，每个客户拥有独立的租户（Tenant），通过 Microsoft Entra ID（原 Azure Active Directory）进行身份管理和访问控制。租户之间的资源隔离是云安全的基石，管理员同意（admin-consent）回调是 OAuth/OIDC 授权流程中的关键环节，用于将应用权限授权绑定到特定租户。Cross-Tenant Synchronization（CTS）是一项 Azure 功能，允许在不同租户之间同步对象和策略，若权限配置不当则可能被滥用。此次披露的漏洞利用租户 ID 暴露和认证回调伪造等手段，绕过了上述隔离机制。

**标签**: `#cloud security`, `#Azure`, `#cross-tenant compromise`, `#authentication vulnerabilities`, `#security research`

---

<a id="item-tech-news-2"></a>
### [官方 Claude Code 扩展被植入 SSH 后门](https://zeli.app/zh/digest/2026-10-30) ⭐️ 8.0/10



rss · Zeli · 10月30日 23:59

#### 摘要

安全研究员 Phorion 发现 Cursor Marketplace 上发布的官方 Claude Code for VS Code 扩展（版本 2.1.313）遭植入恶意 SSH 后门代码。该恶意载荷能在 macOS、Linux 和 Windows 三个平台上建立持久化访问：通过向~/.ssh/authorized\_keys 注入攻击者的公钥并尝试开启 SSH 服务，进而建立反向隧道获取长期远程控制权限。即使在 macOS 上因权限检查逻辑漏洞导致 SSH 服务无法成功启动，密钥仍已被写入磁盘；若用户此前已开启远程登录功能，则风险极高。此外，恶意代码还会收集主机信息并将敏感环境变量名称回传至攻击者服务器。目前 Cursor 已下架受感染版本，建议受影响用户立即排查。

#### 背景

此次事件本质上是供应链攻击，攻击者入侵了 Claude Code 扩展的发布渠道，在官方代码中植入恶意载荷后继续通过 IDE 自动更新机制分发。此类攻击利用了开发者对官方渠道的信任，绕过常规安全审查。与本次事件相关的另一条消息是，Anthropic 本身亦遭黑客入侵，导致受感染的扩展程序被推送至全球数百万开发者的机器上。

#### 社区讨论

安全研究者 Kevin Beaumont 在 cyberplace.social 发文指出，这一发现直接动摇了开发者对官方工具安全性的基本信任——当官方渠道分发的代码扩展本身都不可信时，整个开源生态的信任机制面临严峻拷问，提醒所有开发者在集成第三方代码时必须保持极高的警惕性。

**标签**: `#supply chain security`, `#AI tooling`, `#SSH compromise`, `#VS Code extensions`, `#developer tooling`

---

<a id="item-tech-news-3"></a>
### [Anthropic 成为 SpaceX 最大单一客户，年度算力合约最高 1205 亿美元](https://www.cls.cn/detail/2519914) ⭐️ 8.0/10



telegram · zaihuapd · 10月30日 06:20

#### 摘要

据 SpaceX 申报文件披露，其 AI 部门（现名 Super Intelligence）上季度约 34.5% 的营收来自单一客户，知情人士确认该客户为 Anthropic。双方今年早些时候签署协议，Anthropic 使用 SpaceX 位于田纳西州孟菲斯的数据中心算力，合同期至 2029 年，总支出最高达 1205 亿美元。自今年 12 月起，这一合约每月将为 SpaceX AI 部门贡献约 31 亿美元营收，凸显人工智能开发者与算力基础设施提供商之间日益紧密的战略绑定。

#### 背景

SpaceX 旗下 AI 计算部门 SpaceX SPCX--.AI（现更名为 Super Intelligence）为科技企业提供 GPU 算力服务，主要通过建设数据中心和部署 NVIDIA GPU 来满足 AI 公司的训练与推理需求。Anthropic 的 Claude 模型开发与 Elon Musk 创立的 xAI（生产 Grok 模型）存在直接竞争关系，但 Anthropic 仍选择将算力采购重心放在 SpaceX 而非竞争对手平台。这类长期算力采购协议在 AI 行业日益成为竞争战略的一部分，帮助云计算提供商锁定收入，同时为大模型公司保障关键基础设施供应。

**标签**: `#AI infrastructure`, `#Anthropic`, `#SpaceX`, `#compute contracts`, `#industry news`

---