---
layout: default
title: "Horizon Summary: 2026-11-03 (EN)"
date: 2026-11-03
lang: en
---

> From 207 items, 4 important content pieces were selected

---

**Technology News**
1. [High-severity Linux kernel CVE-2026-98432 enables unauthenticated RCE via IPv4 TCP](#item-tech-news-1) ⭐️ 9.0/10
2. [Astra can read and write weights to improve Qwen](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest: Weight-Space Programming, Ubuntu Security Gap, Postgres Delay](#item-tech-news-3) ⭐️ 8.0/10
4. [Marvell Technology to buy Lumentum in $115 billion AI connectivity deal](#item-tech-news-4) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [High-severity Linux kernel CVE-2026-98432 enables unauthenticated RCE via IPv4 TCP](https://telegram.me/zaihuapd/44866) ⭐️ 9.0/10



telegram · zaihuapd · Nov 3, 02:37

#### Summary

A high-severity use-after-free vulnerability, CVE-2026-98432, has been identified in the Linux kernel&\#x27;s IPv4 TCP stack, allowing unauthenticated remote code execution with no user interaction required. Anthropic has published RCE exploit demonstrations targeting MPTCP listen ports, confirming active exploitation potential. The vulnerability extends beyond MPTCP-only scenarios: Go&\#x27;s official security team warns that services running on Go 1.24 and later are exposed by default on Linux, since listen sockets automatically enable MPTCP from that version onward. Even services not explicitly using MPTCP remain vulnerable to the same class of attack. Kernel updates are urgently recommended for all internet-facing servers.

#### Background

MPTCP \(Multipath TCP\) is an extension to the standard TCP protocol that allows a connection to use multiple network paths simultaneously for improved reliability and throughput. The Linux kernel&\#x27;s implementation of MPTCP integrates with its IPv4 TCP stack, meaning flaws in the shared code paths can affect both MPTCP and standard TCP traffic. Use-after-free vulnerabilities occur when a program continues to use a pointer after the memory it references has been freed, potentially allowing attackers to execute arbitrary code by manipulating the reclaimed memory.

**Tags**: `#Linux kernel`, `#CVE`, `#remote code execution`, `#security`, `#networking`

---

<a id="item-tech-news-2"></a>
### [Astra can read and write weights to improve Qwen](https://rikiyat.github.io/blog/weight-space-programming/) ⭐️ 8.0/10

Astra, an LLM system that can read and write weights to directly improve Qwen model performance, including a reported 5x math improvement through weight-space manipulation, generating active HN discussion about its significance and claims.

hackernews · dbreunig · Nov 2, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50341174)

**Tags**: `#AI`, `#machine learning`, `#LLM research`, `#weight-space learning`, `#model manipulation`

---

<a id="item-tech-news-3"></a>
### [HN Digest: Weight-Space Programming, Ubuntu Security Gap, Postgres Delay](https://zeli.app/zh/digest/2026-11-02) ⭐️ 8.0/10



rss · Zeli · Nov 2, 23:59

#### Summary

Hacker News covered several technical developments this week, led by a breakthrough in &quot;weight-space programming&quot; where the LLM Astra directly reads and edits neural network weights without gradient descent, boosting Qwen3.5-0.8B&\#x27;s MATH-500 score from 7.9% to 48.1% by modifying just 0.016% of parameters. Separately, Ubuntu faced criticism for failing to patch CVE-2026-98432, a CVSS 9.8 kernel TCP vulnerability present since 2016 with a published root exploit, while Debian had already released a fix on October 16; the unpatched 22.04, 24.04, and 26.04 LTS kernels leave enterprise administrators exposed. Meanwhile, PostgreSQL 19&\#x27;s release slipped into November or later after a 74% surge in bug-fix commits during Beta, largely driven by LLM-identified defects that forced rollbacks of features like SQL/PGQ and consumed reviewer bandwidth that would have gone to new functionality.

#### Background

Weight-space programming is an emerging paradigm that treats neural network parameters as editable code rather than values optimized through backpropagation, allowing large language models to reason about model internals directly. CVE-2026-98432 affects the Linux kernel&\#x27;s TCP stack and has a long-standing code path that was never hardened against malicious packet manipulation. PostgreSQL&\#x27;s release cadence has historically been stable at roughly one major version per year, making this delay notable given the project&\#x27;s usual discipline around Beta feature gates.

#### Community Discussion

The Astra weight-space post generated the most engagement at 2,108 upvotes and 687 comments, reflecting strong interest in whether direct weight editing could become a practical alternative to fine-tuning. The Ubuntu CVE thread \(1,365 upvotes, 591 comments\) centered on enterprise trust erosion, with users noting that Debian, Arch, and Alpine already shipped patches while Canonical delayed despite a public commitment to timely fixes for critical vulnerabilities. Postgres 19&\#x27;s delay \(808 upvotes, 483 comments\) drew mixed reactions: some praised the community&\#x27;s insistence on rigor over speed, while others warned that AI-augmented bug discovery could become a permanent bottleneck for release cycles.

**Tags**: `#AI`, `#LLMs`, `#Machine Learning`, `#Linux Security`, `#Hacker News`

---

<a id="item-tech-news-4"></a>
### [Marvell Technology to buy Lumentum in $115 billion AI connectivity deal](https://news.google.com/rss/articles/CBMif0FVX3lxTFBCY3h0UFRmd1ZoV19QeTQ0N204Ul9SRFFHSHlDMGllWkh3SHRfOEY0X0FpUFRleVc2ODhuMzVNTk1GLTlLeW4zY2JiQm1XTlFqQnlHYmRJQTRBVVFyN3pyaTJkNWN2VHVTSkg3SG1aNURBbUgwV2dfLUZXeWhiUDQ?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · Nov 2, 14:00

#### Summary

Marvell Technology has announced a $115 billion acquisition of Lumentum, a major semiconductor company focused on AI connectivity capabilities. The deal represents one of the largest mergers and acquisitions in the semiconductor industry and is designed to strengthen Marvell&\#x27;s position in AI infrastructure networking. Lumentum brings expertise in optical interconnects and photonic technologies critical for high-performance computing and data center applications. This consolidation between two major players signals intensifying competition to supply connectivity solutions for rapidly expanding AI workloads.

#### Background

AI data centers rely on high-bandwidth optical interconnects to move massive amounts of data between GPU clusters, switches, and storage. Lumentum is a leading supplier of high-performance lasers and optical transceivers—components that convert electrical signals into light for fiber-optic cabling. Marvell specializes in switching silicon, electrical interconnects, and custom AI silicon. In large-scale AI architectures, networking is categorized into scale-out \(interconnecting many servers across a rack or facility\) and scale-up \(high-bandwidth links within a compute node or between GPUs\).

**Tags**: `#AI infrastructure`, `#semiconductors`, `#M&amp;A`, `#networking hardware`

---