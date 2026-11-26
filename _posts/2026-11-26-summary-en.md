---
layout: default
title: "Horizon Summary: 2026-11-26 (EN)"
date: 2026-11-26
lang: en
---

> From 184 items, 5 important content pieces were selected

---

**Technology News**
1. [FCC authorizes SpaceX to deploy 1 million AI-equipped satellites](#item-tech-news-1) ⭐️ 9.0/10
2. [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest: 1Password breach validates zero-knowledge design; AI proves major CS conjectures](#item-tech-news-3) ⭐️ 8.0/10
4. [Minecraft Java Edition Critical RCE via Malicious Font in Resource Packs](#item-tech-news-4) ⭐️ 8.0/10
5. [Samsung, SK Hynix to license YMTC Xtacking 3D NAND tech](#item-tech-news-5) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [FCC authorizes SpaceX to deploy 1 million AI-equipped satellites](https://arstechnica.com/space/2026/11/the-fcc-has-authorized-spacex-to-deploy-1-million-satellites/) ⭐️ 9.0/10



rss · Ars Technica · Nov 25, 18:22

#### Summary

On Wednesday, the Federal Communications Commission \(FCC\) authorized SpaceX to deploy up to 1 million AI chip-equipped satellites under its &quot;Starmind&quot; initiative, marking the first such approval by the agency for a space-based AI data center project. The constellation would increase the number of satellites in orbit by roughly 50 times the current count. Other companies, including Google and Blue Origin, are also pursuing similar initiatives for placing AI infrastructure in space. This landmark authorization represents a significant shift in space policy and could reshape orbital bandwidth, broadband communications, and space traffic management.

#### Background

SpaceX&\#x27;s Starlink constellation currently operates tens of thousands of satellites providing global internet coverage. The FCC has historically approved mega-constellations in the low Earth orbit \(LEO\) regime, but never at scales approaching one million units. Putting AI computing chips in orbit raises new questions about radiation-hardened hardware, power budgets, satellite-to-satellite networking, and the regulatory framework needed to manage dense orbital traffic and avoid collisions.

**Tags**: `#satellites`, `#space infrastructure`, `#telecommunications`, `#regulatory`, `#SpaceX`

---

<a id="item-tech-news-2"></a>
### [Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

Scott Aaronson reacts enthusiastically to a new result placing the matrix multiplication exponent at 9/4, sparking extensive discussion on HackerNews about its significance and broader implications.

hackernews · Kotlopou · Nov 25, 19:11 · [Discussion](https://news.ycombinator.com/item?id=50646108)

**Tags**: `#theoretical computer science`, `#algorithms`, `#computational complexity`, `#mathematics`

---

<a id="item-tech-news-3"></a>
### [HN Digest: 1Password breach validates zero-knowledge design; AI proves major CS conjectures](https://zeli.app/zh/digest/2026-11-25) ⭐️ 8.0/10



rss · Zeli · Nov 25, 23:59

#### Summary

A November 25, 2026 Hacker News digest highlighted two major developments in security and theoretical computer science. In the 1Password incident, attackers compromised employee GitHub accounts to access source code and steal backend metadata \(names, emails, account info\), but never reached user vaults or encryption keys, reaffirming the company&\#x27;s zero-knowledge architecture. Meanwhile, reports emerged that OpenAI and Anthropic used AI assistance to prove several long-standing mathematical results, including VP≠VNP, the Generalized Riemann Hypothesis for Dirichlet L-functions \(via a Lean 4 formalization by Anthropic/Claude\), and that the matrix multiplication exponent ω equals 9/4—down from prior best bounds. A separate OpenAI preprint \(Nov 2026\) details the ω=9/4 proof achieving O\(n^2.25\) matrix multiplication complexity.

#### Background

Zero-knowledge architecture means a service provider never has access to users&\#x27; decrypted data; encryption keys are derived client-side from passwords, so server compromises cannot expose vault contents. VP≠VNP is a central open problem in algebraic complexity theory, analogous to P≠NP in the algebraic setting, concerning whether verifying polynomial identities is inherently harder than constructing them. The matrix multiplication exponent ω measures the fastest possible algorithm for multiplying n×n matrices, with the naive bound of 3 slowly improving over decades.

**Tags**: `#security`, `#artificial intelligence`, `#theoretical computer science`, `#zero-knowledge architecture`

---

<a id="item-tech-news-4"></a>
### [Minecraft Java Edition Critical RCE via Malicious Font in Resource Packs](https://github.com/bikini/minecraft2shell) ⭐️ 8.0/10



telegram · zaihuapd · Nov 25, 12:46

#### Summary

On November 22, the minecraft2shell exploit was publicly disclosed, revealing a high-severity remote code execution vulnerability in Minecraft Java Edition. A specially crafted TrueType font embedded in a server resource pack can trigger an out-of-bounds write in lwjgl-freetype 3.4.3 and earlier, allowing arbitrary code execution on affected clients running on Windows. Versions 1.20.5 through 1.21.10 and snapshots 26.1–26.4 are vulnerable; versions 1.20.4 and earlier, as well as the Bedrock Edition, are unaffected. As of now, Mojang has not released an official patch. The community responded on November 24 with m2sfix 1.0.0, a temporary fix delivered as a Java agent or mod that disables font hinting to mitigate the flaw.

#### Background

lwjgl-freetype is a native JNI wrapper around the FreeType font-rendering library used by Minecraft Java Edition to process typefaces in resource packs. When FreeType&\#x27;s font hinting logic processes malformed glyph data, it can perform an out-of-bounds memory write, which attackers can exploit to execute arbitrary code on the client side. This vulnerability class—remote code execution via trusted-looking font files—is particularly dangerous because resource packs are commonly installed without careful scrutiny.

**Tags**: `#security vulnerability`, `#remote code execution`, `#Java`, `#gaming software`

---

<a id="item-tech-news-5"></a>
### [Samsung, SK Hynix to license YMTC Xtacking 3D NAND tech](https://tech.ifeng.com/c/8yLRPKxQy4L) ⭐️ 8.0/10



telegram · zaihuapd · Nov 25, 14:33

#### Summary

Samsung Electronics and SK Hynix have entered into a cross-licensing agreement with Yangtze Memory Technologies Corporation \(YMTC\) to adopt certain Xtacking chip-stacking technology in their 3D NAND flash products. Under the Xtacking approach, memory arrays and CMOS logic circuits are fabricated separately on two distinct wafers and then bonded together using wafer-bonding technology, allowing each layer to be independently optimized. An Omdia senior analyst noted that this architecture enables manufacturers to produce storage arrays in-house while outsourcing logic circuit production to foundries capable of running more advanced process nodes. The agreement marks a notable shift in the global memory chip industry, as Chinese firms have historically been technology adopters rather than licensors in advanced semiconductor manufacturing. All three companies declined to comment on the deal.

#### Background

YMTC \(Yangtze Memory Technologies Corporation\) is a Chinese NAND flash memory manufacturer founded in Wuhan, China, and has developed the proprietary Xtacking architecture, which separates the memory array and CMOS control circuitry onto two different wafers that are later bonded together via wafer-level bonding technology. This architecture allows each component to be fabricated on its own optimal process node, enabling memory arrays and logic circuits to scale independently. The deal follows YMTC&\#x27;s 2024 U.S. court lawsuit against Micron alleging NAND patent infringement.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductor memory`, `#3D NAND`, `#chip manufacturing`, `#cross-licensing`, `#Y.M.Tech`

---