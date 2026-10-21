---
layout: default
title: "Horizon Summary: 2026-10-21 (EN)"
date: 2026-10-21
lang: en
---

> From 201 items, 3 important content pieces were selected

---

**Technology News**
1. [eMudhra Intermediate CA Private Keys Compromised](#item-tech-news-1) ⭐️ 9.0/10
2. [SpaceX to attempt first mid-air catch of Starship and booster](#item-tech-news-2) ⭐️ 8.0/10
3. [Google 开源 TorchTPU，TPU 成 PyTorch 原生选项](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [eMudhra Intermediate CA Private Keys Compromised](https://simonwillison.net/2026/Oct/20/emudhra-certificates/) ⭐️ 9.0/10

The private keys of eight eMudhra intermediate certificate authority certificates have been compromised, affecting systems relying on Mozilla, Microsoft, Apple, and Chrome root programs.

rss · Simon Willison · Oct 20, 23:50

#### Summary

The private keys for eight eMudhra intermediate CA certificates have been compromised. These certificates chain to root programs trusted by Mozilla, Microsoft, Apple, and Chrome, plus many downstream trust stores. Any software that bundles a certificate list requires updating to mitigate the incident. Linux distributions need to update their ca-certificates packages, while the Python ecosystem has already released new versions: uv 0.13.4, pip 26.2.2, and certifi 2026.10.19 with updated certificate lists.

#### Background

Certificate authorities issue digital certificates that establish trust for HTTPS connections. When a CA&\#x27;s private key is compromised, an attacker could forge certificates for any domain, enabling man-in-the-middle attacks. The eMudhra intermediate certificates were distributed through multiple root programs, making this a widespread infrastructure security incident affecting Linux distros, Python tooling, and other software ecosystems that bundle their own trusted certificate stores.

#### Community Discussion

The impact of this incident is unevenly spread across ecosystems. Firefox users were protected automatically via OneCRL and CRLite without requiring updates, while Chrome, Apple, and Microsoft have similar revocation tooling. However, many systems remain vulnerable due to vendors embedding their own CA stores rather than using system packages. Community concern was also raised about one compromised key being literally &quot;4&quot; \(a single byte\), highlighting potential issues with key generation quality in the original deployment.

**Tags**: `#cryptography`, `#certificate authority`, `#security incident`, `#software engineering`, `#Python tooling`

---

<a id="item-tech-news-2"></a>
### [SpaceX to attempt first mid-air catch of Starship and booster](https://www.theverge.com/science/1014913/spacex-will-try-catching-starship-and-its-booster-for-first-time-musk-says) ⭐️ 8.0/10



rss · The Verge · Oct 20, 21:02

#### Summary

SpaceX CEO Elon Musk announced that the company plans its first attempt to catch both the Starship upper stage and its Super Heavy booster mid-air next month. A successful recovery would mark the first time in history an orbital launch vehicle has been fully recovered after flight. The maneuver would represent a major milestone for reusable orbital launch technology, potentially transforming the economics of space access by eliminating the need to build new hardware for each launch.

#### Background

SpaceX has previously recovered Booster units by landing them vertically on launch pads or drone ships, and has caught boosters with mechanical arms during earlier Starship test flights. However, those efforts only recovered the first stage; the Starship upper stage has not yet been recovered intact. Full recovery of both stages would be the first completeorbital rocket recovery in history.

**Tags**: `#space technology`, `#aerospace engineering`, `#reusable rockets`, `#propulsion systems`, `#industry milestones`

---

<a id="item-tech-news-3"></a>
### [Google 开源 TorchTPU，TPU 成 PyTorch 原生选项](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus) ⭐️ 8.0/10



telegram · zaihuapd · Oct 21, 00:47

#### 摘要

Google Cloud 宣布与 Meta PyTorch 团队联合开发的 TorchTPU 已在 GitHub 开源，TPU 由此成为与 GPU、CPU 并列的 PyTorch 原生硬件选项。现有 PyTorch 代码几乎无需改动即可在 TPU 上运行，显著降低了从 NVIDIA GPU 迁移到 TPU 的门槛。vLLM、SGLang、llm-d、TorchTitan 等主流 AI 框架已接入支持，Hugging Face Transformers v5 可直接将模型部署至 TPU 硬件。此举使 TPU 成为 NVIDIA GPU 之外的可行替代方案，对 AI 基础设施生态格局构成实质性挑战。

#### 背景

Google 自 2016 年起研发 TPU（张量处理单元），专为神经网络推理与训练定制，历经五代迭代。近年来 NVIDIA GPU 凭借 CUDA 软件生态牢牢主导 AI 训练市场，形成较高的迁移锁定。PyTorch 作为全球使用最广的深度学习框架之一，长期对非 NVIDIA 硬件支持有限，限制了 TPU 等替代硬件的普及。TorchTPU 的开源填补了 PyTorch 原生 TPU 支持的空白，使开发者能在不重写代码的前提下切换硬件平台。

**Tags**: `#AI infrastructure`, `#open source`, `#PyTorch`, `#TPU`, `#hardware`

---