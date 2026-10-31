---
layout: default
title: "Horizon Summary: 2026-10-31 (EN)"
date: 2026-10-31
lang: en
---

> From 196 items, 3 important content pieces were selected

---

**Technology News**
1. [Five full cross-tenant compromises disclosed in Azure](#item-tech-news-1) ⭐️ 8.0/10
2. [Official Claude Code VS Code Extension Compromised with SSH Backdoor](#item-tech-news-2) ⭐️ 8.0/10
3. [Anthropic Becomes SpaceX&\#x27;s Largest Single Customer on $120.5B Compute Deal](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Five full cross-tenant compromises disclosed in Azure](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 8.0/10



hackernews · swq115 · Oct 30, 10:06 · [Discussion](https://news.ycombinator.com/item?id=50301854)

#### Summary

Security researcher swq115 disclosed five distinct full cross-tenant compromise vulnerabilities in Microsoft Azure on October 2, 2026, via Binary Security. The findings include a forgeable admin-consent callback tied to tenant ID exposure on login.microsoftonline.com, as well as path traversal and IDOR issues that could allow an attacker with knowledge of another tenant&\#x27;s ID to fully compromise it. The research was highlighted on Hacker News, where commenters noted the breadth of cross-tenant leak categories Azure has accumulated and questioned why enterprises continue to adopt the platform despite such risks.

#### Background

Azure is Microsoft&\#x27;s cloud platform, and Entra ID \(formerly Azure AD\) organizes its identity and access management into separate tenants, each representing an isolated organization. Cross-tenant attacks target the trust relationships and API boundaries between these tenants, which is a growing attack surface as enterprises increasingly share resources across organizational boundaries. The admin consent flow is an OAuth/OpenID Connect mechanism that allows a tenant administrator to grant permissions to an application on behalf of their organization; flaws in this flow can let attackers fabricate redirect callbacks to hijack authorization.

#### Community Discussion

Commenters praised the researcher&\#x27;s work while pressing Microsoft to fix the forgeable admin-consent callback flow rather than relying on documentation warnings about tenant ID exposure. Some observers drew parallels to past recommendations like adding randomness to resource names, suggesting these path traversal and IDOR issues may have been present since the features were introduced.

**Tags**: `#cloud security`, `#Azure`, `#cross-tenant compromise`, `#authentication vulnerabilities`, `#security research`

---

<a id="item-tech-news-2"></a>
### [Official Claude Code VS Code Extension Compromised with SSH Backdoor](https://zeli.app/zh/digest/2026-10-30) ⭐️ 8.0/10



rss · Zeli · Oct 30, 23:59

#### Summary

The official Claude Code VS Code extension available on the Cursor Marketplace was found to contain an implanted SSH backdoor in version 2.1.313. Researcher Phorion discovered that the malicious payload injected SSH public keys into ~/.ssh/authorized\_keys, attempted to enable SSH services, and established reverse tunnels for persistent remote access across macOS, Linux, and Windows. The payload also harvested sensitive environment variable names from affected machines. Cursor has since removed the compromised version, and Anthropic silently replaced it, though the company has not publicly disclosed the supply chain attack to its customer base. The incident has been linked to compromised developer environments at organizations including Binance.

#### Background

Supply chain attacks on developer tooling are among the most damaging compromise vectors because they target trusted code distribution channels. VS Code extensions and AI coding assistants like Claude Code run with elevated privileges on developer machines, making them high-value targets for attackers seeking persistent access to codebases and secrets. This incident joins a growing pattern of compromises affecting official AI tooling ecosystems, raising concerns about the security of automated update mechanisms across marketplace-distributed extensions.

#### Community Discussion

The Hacker News community expressed deep alarm at the breach of an officially distributed extension, with many emphasizing the erosion of trust in AI tooling supply chains. Kevin Beaumont and others noted that the incident challenges the fundamental assumption that official channel releases are safe, and the lack of public disclosure by Anthropic has drawn particular criticism. Community members are urging developers to audit any systems running version 2.1.313 and rotate credentials immediately.

**Tags**: `#supply chain security`, `#AI tooling`, `#SSH compromise`, `#VS Code extensions`, `#developer tooling`

---

<a id="item-tech-news-3"></a>
### [Anthropic Becomes SpaceX&\#x27;s Largest Single Customer on $120.5B Compute Deal](https://www.cls.cn/detail/2519914) ⭐️ 8.0/10



telegram · zaihuapd · Oct 30, 06:20

#### Summary

SpaceX disclosed in a regulatory filing that approximately 34.5% of its AI division&\#x27;s revenue came from a single customer last quarter, identified by insiders as Anthropic. The two companies signed a compute infrastructure agreement earlier this year, granting Anthropic access to SpaceX&\#x27;s data center in Memphis, Tennessee. According to Anthropic&\#x27;s own IPO filing, the contract commits up to $120.5 billion through 2029, which translates to roughly $3.1 billion per month in revenue for SpaceX&\#x27;s Super Intelligence division starting in December. The deal underscores the deepening financial tie between a leading AI developer and an infrastructure provider.

**Tags**: `#AI infrastructure`, `#Anthropic`, `#SpaceX`, `#compute contracts`, `#industry news`

---