---
layout: default
title: "Horizon Summary: 2026-10-28 (EN)"
date: 2026-10-28
lang: en
---

> From 206 items, 8 important content pieces were selected

---

**Technology News**
1. [Critical EDK2 UEFI Firmware Flaw Lets Attackers Run Code at Boot](#item-tech-news-1) ⭐️ 9.0/10
2. [Triton v3.9.0 Release Brings Atomic Operations and Backend Optimizations](#item-tech-news-2) ⭐️ 8.0/10
3. [Tailscale SSH Vulnerabilities: Investigation and Remediation Update](#item-tech-news-3) ⭐️ 8.0/10
4. [Classification of Finite Simple Groups Formalized in Lean](#item-tech-news-4) ⭐️ 8.0/10
5. [Apple iPhone Duo foldable review: Respectable but not compelling](#item-tech-news-5) ⭐️ 8.0/10
6. [🤖 OpenAI 公布模型产出的三项科研结果](#item-tech-news-6) ⭐️ 8.0/10
7. [Anthropic Hiring Manager Stops Coding Interviews After Claude Outperforms Humans](#item-tech-news-7) ⭐️ 8.0/10
8. [Google 提出睡眠框架，助大模型持续学习不遗忘](#item-tech-news-8) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Critical EDK2 UEFI Firmware Flaw Lets Attackers Run Code at Boot](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/) ⭐️ 9.0/10



rss · Ars Technica · Oct 27, 20:25

#### Summary

A critical code-execution flaw in the EDK2 UEFI firmware implementation allows attackers to execute arbitrary code early in the boot process, before the operating system loads. The vulnerability affects the majority of servers worldwide, posing a significant risk to global infrastructure. As reported by Ars Technica&\#x27;s Dan Goodin, this firmware-level flaw gives adversaries the ability to establish persistence and potentially compromise systems at a level that is difficult to detect through conventional security measures.

**Tags**: `#UEFI firmware`, `#critical vulnerability`, `#EDK2`, `#server security`, `#boot-level exploit`

---

<a id="item-tech-news-2"></a>
### [Triton v3.9.0 Release Brings Atomic Operations and Backend Optimizations](https://github.com/triton-lang/triton/releases/tag/v3.9.0) ⭐️ 8.0/10

Triton, the open‑source compiler framework for GPU programming, has released version 3.9.0, introducing atomic operations in its dialect and frontend, significant backend and compiler improvements, and enhanced profiling capabilities—key updates for machine‑learning practitioners building GPU kernels.

github · warrendeng · Oct 27, 18:56

#### Summary

Triton v3.9.0 adds first‑class atomic loads \(\`tl.atomic\_load\`\), stores \(\`tl.atomic\_store\`\), and polling \(\`tl.atomic\_poll\`\) to the language and Gluon, defaulting to acquire/release semantics. The backend/compiler features a rewritten barrier‑insertion pass, fixes to multi‑CTA cluster synchronization, and up to 40× faster batched MMAv2 matmul on NVIDIA. Vendor‑specific updates include a separate LLVM pin for AMD/HIP and improved async‑copy and aliasing logic on NVIDIA. Proton profiling introduces a new \`Proton.custom\_metric\(\)\` API, while the release deprecates the legacy TMA PTX interface and enforces stricter compile‑time checks for common errors.

#### Background

Triton is a domain‑specific language and compiler designed to simplify the writing of high‑performance GPU kernels for AI/ML workloads. Its dialect‑front‑end/back‑end architecture allows developers to express tensor operations that are compiled to LLVM IR and then to target GPU ISA. This release focuses on expanding concurrency primitives, stabilizing multi‑CTA execution, and tightening correctness checks across both AMD and NVIDIA backends.

**Tags**: `#open source`, `#GPU programming`, `#machine learning`, `#compiler`, `#AI systems`

---

<a id="item-tech-news-3"></a>
### [Tailscale SSH Vulnerabilities: Investigation and Remediation Update](https://tailscale.com/ssh-investigation-update) ⭐️ 8.0/10



hackernews · figmert · Oct 27, 19:55 · [Discussion](https://news.ycombinator.com/item?id=50264857)

#### Summary

Tailscale published an investigation and remediation update regarding SSH vulnerabilities affecting its managed SSH service. The vulnerabilities only impact configurations where ACLs permit SSH access into a node via Tailscale SSH without granting sudoers or root path access. This distinction matters because users with properly restricted access controls were not exposed to the identified attack vectors.

#### Background

Tailscale SSH is a managed SSH service that integrates with Tailscale&\#x27;s zero-trust networking platform, allowing users to authenticate and access nodes through Tailscale&\#x27;s authentication mechanism rather than traditional SSH key distribution. Unlike standard OpenSSH implementations, Tailscale SSH operates as an additional layer that can intercept and manage SSH connections within tailnets.

#### Community Discussion

HN community members expressed concern about architectural single points of failure when Tailscale handles both VPN and SSH authentication simultaneously. Several commenters noted they prefer sticking with stock OpenSSH and traditional key-based authentication methods, while others suggested Tailscale should operate purely as a network layer rather than managing service authentication.

**Tags**: `#infrastructure security`, `#open source`, `#networking`, `#zero trust`

---

<a id="item-tech-news-4"></a>
### [Classification of Finite Simple Groups Formalized in Lean](https://cfsg.axiommath.ai/) ⭐️ 8.0/10



hackernews · pfdietz · Oct 27, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50261647)

#### Summary

The Classification of Finite Simple Groups, one of the largest theorems in mathematics, has been formalized in the Lean proof assistant. The original proof was a collaboration of roughly 100 mathematicians spread across more than 1,000 pages, and the formalization effort discovered and filled at least one previously overlooked gap in the published proof. This milestone is significant for the mathematical formalization community because it demonstrates that Lean can handle massive, highly non-trivial results that previously relied on informal, human-readable arguments.

#### Community Discussion

Commenters discussed the prospect of using frontier AI models to auto-formalize entire textbooks into Lean, raising both optimism and uncertainty about whether current models can reliably perform such large-scale conversions. Some noted that despite the maturity of formalization tools, work still relies on set-theoretic foundations rather than homotopical ones. Others highlighted the practical value of this formalization as a model for future large-scale collaborative theorem-proving projects and as a resource for learners approaching abstract algebra.

**Tags**: `#formal verification`, `#theorem proving`, `#artificial intelligence`, `#mathematics`, `#Lean`

---

<a id="item-tech-news-5"></a>
### [Apple iPhone Duo foldable review: Respectable but not compelling](https://arstechnica.com/gadgets/2026/10/apple-iphone-duo-review-two-screens-two-experiences-two-thousand-dollars/) ⭐️ 8.0/10



rss · Ars Technica · Oct 27, 14:20

#### Summary

Ars Technica has reviewed Apple&\#x27;s iPhone Duo, its first foldable phone, concluding that while the dual-screen concept is respectable, it falls short of being truly satisfying at its $2,000 price point. The review characterizes Apple&\#x27;s initial foray into foldable hardware as a design effort that shows promise but does not yet deliver a polished experience commensurate with the premium cost. Key factors include the dual-screen experience and the device&\#x27;s positioning in a market where competitors are already refining foldable form factors.

#### Community Discussion

No community comments are available for this article.

**Tags**: `#apple`, `#foldable-phone`, `#smartphone`, `#product-review`

---

<a id="item-tech-news-6"></a>
### [🤖 OpenAI 公布模型产出的三项科研结果](https://openai.com/index/building-scientific-understanding-with-academic-communities/) ⭐️ 8.0/10

Unverified claims that OpenAI models produced proofs of major results in computational complexity, harmonic analysis, and theoretical physics, with external expert verification underway.

telegram · zaihuapd · Oct 27, 15:00

**Tags**: `#AI for science`, `#formal verification`, `#computational complexity`, `#research breakthroughs`, `#open source`

---

<a id="item-tech-news-7"></a>
### [Anthropic Hiring Manager Stops Coding Interviews After Claude Outperforms Humans](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) ⭐️ 8.0/10



telegram · zaihuapd · Oct 28, 01:46

#### Summary

Anthropic hiring manager Felix Rieseberg has discontinued coding interviews, stating that Claude now outperforms human candidates on such tasks and writing code is no longer an effective screening criterion. Rieseberg argues that as execution costs drop with AI assistance, seniority matters less than impact, and he advises junior engineers to leverage AI to rapidly build prototypes targeting business goals—citing that the Claude Code GUI prototype was built over a single weekend by two junior engineers and reached its first public release in approximately eight days. The shift signals a broader industry reckoning with how AI capabilities are changing software engineering hiring practices.

#### Background

Felix Rieseberg is a well-known developer advocate at Anthropic who frequently shares insights on AI-assisted software development. Coding interviews—typically involving algorithm or data structure problems—are a standard technical hiring gate across the tech industry. Rieseberg&\#x27;s critique points to the growing tension between traditional assessment methods and the reality that AI coding assistants like Claude Code can already solve such problems faster and more accurately than most candidates.

#### Community Discussion

No community comments were available for this item.

**Tags**: `#AI`, `#software engineering`, `#hiring practices`, `#Anthropic`, `#programmatic intelligence`

---

<a id="item-tech-news-8"></a>
### [Google 提出睡眠框架，助大模型持续学习不遗忘](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/) ⭐️ 8.0/10

Google Research proposes a sleep framework for LLM continual learning that mitigates catastrophic forgetting by alternately cycling between active interaction and an offline consolidation phase, reporting results surpassing GPT-4 and SFT baselines.

telegram · zaihuapd · Oct 28, 01:46

**Tags**: `#continual learning`, `#catastrophic forgetting`, `#large language models`, `#Google Research`

---