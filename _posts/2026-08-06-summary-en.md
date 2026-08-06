---
layout: default
title: "Horizon Summary: 2026-08-06 (EN)"
date: 2026-08-06
lang: en
---

> From 199 items, 2 important content pieces were selected

---

**Technology News**
1. [ChainDrop worm compromises over 1300 npm packages](#item-tech-news-1) ⭐️ 9.0/10
2. [Google DeepMind leadership shakeup: Hassabis to chair, Jeff Dean departs](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ChainDrop worm compromises over 1300 npm packages](https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/) ⭐️ 9.0/10



telegram · zaihuapd · Aug 5, 03:04

#### Summary

The ChainDrop self-propagating worm has compromised over 1,300 npm packages, with combined monthly downloads reaching approximately 2 billion. The attack began when hackers breached the GitHub account of the Keyv package maintainer and spread to packages associated with organizations including Deliveroo, Qlik, and ServiceTitan. Malicious versions were published through legitimate GitHub Actions workflows, carrying valid provenance signatures. Upon installation, a setup.mjs dropper and a Math\_Symbol.js credential-stealing script execute automatically, harvesting tokens from GitHub, npm, AWS, and Kubernetes before infecting other maintainers&\#x27; packages. Security researchers advise that any system that installed an affected version should be treated as compromised, with recommendations to rebuild the environment, rotate all credentials, and audit logs; npm-cache.com is identified as a key indicator of compromise. The attack is still actively spreading and the number of affected packages is expected to grow.

#### Background

Supply-chain attacks on npm packages are a growing threat because many packages are small, maintained by individuals, and widely depended upon. npm packages can include post-install scripts \(such as setup.mjs\) that run automatically during installation, giving attackers a direct execution path on user systems. Provenance verification, which confirms packages were built through trusted CI/CD pipelines, can be bypassed if an attacker gains access to a maintainer&\#x27;s account and publishes through the same legitimate workflow.

**Tags**: `#supply chain security`, `#npm`, `#credential theft`, `#worm`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Google DeepMind leadership shakeup: Hassabis to chair, Jeff Dean departs](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) ⭐️ 8.0/10

Google DeepMind announced a major leadership transition, with Demis Hassabis moving from CEO to chair and Jeff Dean leaving after 27 years. Sanjay Ghemawat is also departing alongside Dean to launch an independent public benefit corporation focused on ML, science, and engineering.

hackernews · colesantiago · Aug 5, 16:05 · [Discussion](https://news.ycombinator.com/item?id=49184755)

#### Summary

Google DeepMind announced that CEO Demis Hassabis will transition to chair while Jeff Dean departs after 27 years at Google. Dean and Google Senior Fellow Sanjay Ghemawat are launching an independent public benefit corporation to accelerate discoveries in machine learning, science, and engineering. The move positions Hassabis effectively as Chief Scientist across Alphabet. Google stock dropped approximately 5% following the announcement. The departures are part of a broader pattern of prominent AI talent leaving Google over recent months, including Oriol Vinyals, Quoc Le, Noam Shazeer, John Jumper, and others, with no Gemini frontier GA release in roughly 14 months.

#### Community Discussion

Hacker News commenters characterized the departures as the end of a golden era, noting that senior engineers had cited Dean and Ghemawat as key reasons for staying. Some observers questioned whether the environment at Google had become hostile to prominent researchers, pointing to the cumulative loss of talent and stalled Gemini progress. Others viewed Hassabis&\#x27;s role change as a promotion to Chief Scientist for Alphabet, while expressing optimism about his continued focus on AI for health.

**Tags**: `#AI leadership`, `#Google DeepMind`, `#industry news`, `#talent retention`, `#Alphabet`

---