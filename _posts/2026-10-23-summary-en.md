---
layout: default
title: "Horizon Summary: 2026-10-23 (EN)"
date: 2026-10-23
lang: en
---

> From 206 items, 6 important content pieces were selected

---

**Technology News**
1. [Disgraced eMudhra drops out of TLS business after using cert private key of 4](#item-tech-news-1) ⭐️ 9.0/10
2. [NVIDIA OpenShell: container-based runtime for secure autonomous AI agents](#item-tech-news-2) ⭐️ 8.0/10
3. [Personalized mRNA cancer vaccine cuts melanoma death and recurrence by 42%](#item-tech-news-3) ⭐️ 8.0/10
4. [Hackers got a four-day head start on epic PHP2Shell vulnerability](#item-tech-news-4) ⭐️ 8.0/10
5. [澳洲法院裁定苹果须向第三方应用商店开放 iPhone](#item-tech-news-5) ⭐️ 8.0/10
6. [Smart TVs transmit content data even with ACR disabled](#item-tech-news-6) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Disgraced eMudhra drops out of TLS business after using cert private key of 4](https://arstechnica.com/security/2026/10/disgraced-emudhra-drops-out-of-tls-business-following-certificate-debacle/) ⭐️ 9.0/10

eMudhra exits TLS business after a certificate signing failure allowed unauthorized web credentials to be minted for any site.

rss · Ars Technica · Oct 22, 20:17

**Tags**: `#PKI security`, `#TLS certificates`, `#infrastructure breach`, `#certificate authority`

---

<a id="item-tech-news-2"></a>
### [NVIDIA OpenShell: container-based runtime for secure autonomous AI agents](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10



hackernews · niemandhier · Oct 22, 17:44 · [Discussion](https://news.ycombinator.com/item?id=50198675)

#### Summary

NVIDIA has released OpenShell, an open-source container-based runtime designed to give autonomous AI agents useful capabilities while restricting their access to data, secrets, and untrusted networks. The tool addresses a practical concern in AI engineering—sandboxing agent fleets with bounded network access and credential management—without granting unrestricted privileges. Community discussion highlights both adoption interest and skepticism, noting that agents gain capability through access but security requires limiting that same access, creating an inherent trade-off rather than a complete solution.

#### Background

Autonomous AI agents are increasingly deployed to perform complex tasks that require reading files, installing packages, calling APIs, and using credentials. However, giving agents broad system access creates security and privacy risks, including potential data exfiltration. Containerization and sandboxing are common mitigation strategies, but managing these constraints across fleets of agents remains an engineering challenge.

#### Community Discussion

Commenters noted existing tools like iron proxy for network restrictions and credential swapping, while pointing out that preventing data exfiltration remains difficult even with domain-level controls. Some users praised container-based agent execution and OpenShell&\#x27;s management layer, while others argued the product blurs the line between capability and security, suggesting that true safety requires accepting inherent trade-offs rather than claiming both are fully achievable.

**Tags**: `#AI agents`, `#sandboxing`, `#container security`, `#open source`, `#ML infrastructure`

---

<a id="item-tech-news-3"></a>
### [Personalized mRNA cancer vaccine cuts melanoma death and recurrence by 42%](https://arstechnica.com/health/2026/10/personalized-mrna-cancer-vaccine-cut-melanoma-death-recurrence-by-42/) ⭐️ 8.0/10



rss · Ars Technica · Oct 22, 22:12

#### Summary

Moderna and Merck reported that their personalized mRNA cancer vaccine reduced death and recurrence by 42% in a clinical trial for melanoma patients. The top-line results were released after the companies had previously announced the trial had succeeded. This marks a significant advance in both oncology and mRNA therapeutic technology, demonstrating that patient-specific mRNA vaccines can meaningfully improve outcomes in cancer treatment.

**Tags**: `#mRNA vaccines`, `#cancer immunotherapy`, `#clinical trials`, `#biotechnology`, `#oncology`

---

<a id="item-tech-news-4"></a>
### [Hackers got a four-day head start on epic PHP2Shell vulnerability](https://arstechnica.com/security/2026/10/hackers-got-a-four-day-head-start-on-epic-php2shell-vulnerability/) ⭐️ 8.0/10

Hackers began probing a major PHP vulnerability four days before official disclosure, highlighting a real-world responsible-disclosure gap.

rss · Ars Technica · Oct 22, 15:25

**Tags**: `#cybersecurity`, `#PHP`, `#vulnerability disclosure`, `#exploit`, `#software engineering`

---

<a id="item-tech-news-5"></a>
### [澳洲法院裁定苹果须向第三方应用商店开放 iPhone](https://9to5mac.com/2026/10/21/apple-must-open-iphone-to-alternative-app-stores-in-australia-after-epic-games-ruling/) ⭐️ 8.0/10

Australian Federal Court orders Apple to open iPhone to third-party app stores and alternative payment methods from March 2027, following Epic Games&\#x27; antitrust case.

telegram · zaihuapd · Oct 22, 06:54

**Tags**: `#antitrust`, `#iOS`, `#App Store`, `#Epic Games`, `#mobile regulation`

---

<a id="item-tech-news-6"></a>
### [Smart TVs transmit content data even with ACR disabled](https://watchingthewatchers.github.io/watchingthewatchers/index.html) ⭐️ 8.0/10



telegram · zaihuapd · Oct 22, 09:50

#### Summary

Research from Watching the Watchers found that several smart TVs continue transmitting unencrypted content data even after automatic content recognition \(ACR\) is disabled in settings. The study conducted 5,943 controlled experiments across 12 TVs from 10 manufacturers and found that VIDAA OS sends data—including non-resettable device IDs and audio fingerprints—via plaintext MQTT, while Vizio&\#x27;s WatchFree+ leaks program names through unencrypted DNS queries. These telemetry flows cannot be turned off by users, raising significant privacy concerns for connected television devices.

**Tags**: `#IoT Privacy`, `#Smart TVs`, `#System Security`, `#Consumer Electronics`, `#Telemetry`

---