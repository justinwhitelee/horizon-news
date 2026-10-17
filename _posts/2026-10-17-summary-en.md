---
layout: default
title: "Horizon Summary: 2026-10-17 (EN)"
date: 2026-10-17
lang: en
---

> From 196 items, 3 important content pieces were selected

---

**Technology News**
1. [Claude reveals NIST P-curve seeds came from lrand48 with Unix timestamps](#item-tech-news-1) ⭐️ 9.0/10
2. [Big Fish: 37-Year-Old Kernel Bug Exploited in OpenBSD](#item-tech-news-2) ⭐️ 8.0/10
3. [All the news about the iPhone Duo](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Claude reveals NIST P-curve seeds came from lrand48 with Unix timestamps](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10



hackernews · ahlCVA · Oct 16, 18:55 · [Discussion](https://news.ycombinator.com/item?id=50122800)

#### Summary

Claude AI deterministically traced the seeds behind the NIST P-192, P-224, P-256, P-384, and P-521 ECDSA curves back to the C library&\#x27;s lrand48 pseudorandom number generator, seeded with Unix timestamps. This resolves a decades-old open question about how these widely used cryptographic parameters were chosen, confirming they were not derived from any hash algorithm as some had suspected. The findings came from an investigation published on words.filippo.io. One seed, B-163, did not fit the pattern and remains unexplained—possibly due to a transcription error during publication. The result effectively dismantles a generation of conspiracy theories that the NSA had embedded backdoors into NIST curves through opaque parameter selection.

#### Community Discussion

Community reaction is mixed: while many celebrated the resolution of a long-standing mystery, some noted that confirming the generation method does not rule out deliberate selection by searching timestamps for curves with desirable properties. Others suggested the unexplained B-163 seed may simply be a typo. The broader sentiment framed the findings as devastating to NIST cryptography conspiracy theories, with speculation that the original NSA employee may have been unaware of the simplicity of the process.

**Tags**: `#cryptography`, `#AI research`, `#NIST standards`, `#ECDSA`, `#open problems`

---

<a id="item-tech-news-2"></a>
### [Big Fish: 37-Year-Old Kernel Bug Exploited in OpenBSD](https://calif.io/research/big-fish) ⭐️ 8.0/10



hackernews · rs\_rs\_rs\_rs\_rs · Oct 16, 14:44 · [Discussion](https://news.ycombinator.com/item?id=50118977)

#### Summary

A research paper titled &quot;Big Fish&quot; published on calif.io presents the discovery and exploitation of a 37-year-old kernel bug in OpenBSD, one of the most heavily audited operating system codebases. The bug originated in 1987 with 4.2BSD and persisted through multiple BSD derivatives before being independently found and exploited in OpenBSD. Although the vulnerability was accidentally fixed in NetBSD during a code rewrite in August 1999, the same flaw survived in OpenBSD for over three decades. The finding demonstrates that even extensive manual code review cannot catch every kernel vulnerability, highlighting practical limits of audit-based security approaches.

#### Background

OpenBSD is an operating system that prioritizes security and is known for its proactive code auditing process, where developers systematically review source code to find and fix vulnerabilities. This makes the persistence of a 37-year-old undetected kernel bug particularly notable, as it demonstrates the limitations of review-based vulnerability detection even in one of the most rigorously audited codebases. The bug in question relates to a kernel-level vulnerability that remained undiscovered despite decades of scrutiny, raising questions about whether automated techniques like fuzzing or static analysis could have caught it earlier.

#### Community Discussion

Commenters noted the bug was accidentally fixed in NetBSD during a rewrite in August 1999. Discussion focused on the difficulty of catching such kernel bugs through review alone, with debate over whether automated techniques like fuzzing or static analysis could have realistically detected this class of vulnerability or whether it required human exploit-oriented reasoning.

**Tags**: `#kernel security`, `#vulnerability research`, `#OpenBSD`, `#exploit development`, `#code auditing`

---

<a id="item-tech-news-3"></a>
### [All the news about the iPhone Duo](https://www.theverge.com/tech/1010131/apple-iphone-duo-news-announcements) ⭐️ 8.0/10

Apple announces the iPhone Duo, its first foldable phone featuring dual displays, Touch ID, and minimal crease design.

rss · The Verge · Oct 16, 23:36

**Tags**: `#Apple`, `#foldable phone`, `#hardware`, `#mobile`, `#iPhone`

---