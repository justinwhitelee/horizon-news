---
layout: default
title: "Horizon Summary: 2026-11-25 (EN)"
date: 2026-11-25
lang: en
---

> From 191 items, 6 important content pieces were selected

---

**Technology News**
1. [AI-assisted proof of Riemann hypothesis appears solid but implications unclear](#item-tech-news-1) ⭐️ 9.0/10
2. [GPT-6 generates protein minibinders via code, relies on specialized models downstream](#item-tech-news-2) ⭐️ 8.0/10
3. [Three LLM Inflection Points Over Twelve Months](#item-tech-news-3) ⭐️ 8.0/10
4. [WebAssembly runs Firefox in-browser; Anthropic dips below IPO; Tidal bans all-AI music](#item-tech-news-4) ⭐️ 8.0/10
5. [Amazon shifts satellite launches to Falcon 9 and Ariane 6 after ULA failures](#item-tech-news-5) ⭐️ 8.0/10
6. [T3 Code Default Telemetry Reads Local Auth Credentials](#item-tech-news-6) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AI-assisted proof of Riemann hypothesis appears solid but implications unclear](https://arstechnica.com/ai/2026/11/whats-going-on-with-the-riemann-hypothesis/) ⭐️ 9.0/10



rss · Ars Technica · Nov 24, 20:34

#### Summary

An AI-assisted proof of the Riemann hypothesis appears to be holding up under scrutiny, according to a report by Ars Technica author John Timmer. The Riemann hypothesis, one of mathematics&\#x27; most consequential unsolved problems, has resisted proof for over 160 years; it asserts that all non-trivial zeros of the Riemann zeta function lie on the critical line with real part equal to 1/2. If confirmed, the result would settle a central question in analytic number theory, but analysts say it remains unclear what broader mathematical implications the proof yields or how it advances understanding beyond confirmation. The case marks a notable development at the intersection of AI-assisted reasoning and formal verification in pure mathematics.

**Tags**: `#Artificial Intelligence`, `#Mathematics`, `#Formal Verification`, `#Riemann Hypothesis`, `#AI-Assisted Proof`

---

<a id="item-tech-news-2"></a>
### [GPT-6 generates protein minibinders via code, relies on specialized models downstream](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10



hackernews · acossta · Nov 24, 21:02 · [Discussion](https://news.ycombinator.com/item?id=50634658)

#### Summary

OpenAI reported that GPT‑6.2 generated three‑dimensional protein minibinder designs by writing code without directly using specialized protein AI models. Given the 3D structures of five target proteins and marked attachment sites, the model produced code to create potential minibinder geometries. This demonstrates an expansion of general‑purpose coding capability into scientific design workflows. However, translating those designs into testable amino acid sequences and predicting binding required dedicated tools such as SolubleMPNN and other specialized protein models. The announcement currently lacks experimental lab validation, with evidence heavily weighted toward computational exploration.

#### Community Discussion

Commenters debated whether GPT‑6.2 truly &quot;designed&quot; proteins, noting that a protein&\#x27;s sequence—not its 3D geometry—determines its functional properties. Others viewed the model as an effective orchestrator or &quot;glue layer&quot; that coordinates specialized downstream tools rather than replacing them. A final concern pointed out the absence of rigorous biological controls and an overreliance on computational results without wet‑lab validation.

**Tags**: `#artificial intelligence`, `#protein design`, `#software engineering`, `#machine learning`, `#biotechnology`

---

<a id="item-tech-news-3"></a>
### [Three LLM Inflection Points Over Twelve Months](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) ⭐️ 8.0/10



rss · Simon Willison · Nov 24, 23:02

#### Summary

Over roughly a year ending in late 2026, three distinct capability leaps transformed LLMs and coding agents from experimental tools into genuinely reliable work assistants. The first came in November 2025 with the release of Claude Opus 4.5 and OpenAI&\#x27;s GPT-5.1 series, which made coding agents like Claude Code and Codex consistently correct enough to be adopted as daily drivers. A second leap arrived in June/July 2026 with Claude Fable 5 and related &quot;Fable class&quot; models, which introduced relentlessly proactive problem solvers that could take an open-ended goal, deploy necessary tools autonomously, and brute-force solutions to complex tasks—from debugging display glitches to triangulating physical sound sources. The third milestone emerged in September/October 2026 when frontier models suddenly became credibly proficient at 3D modeling and game development, culminating in systems like Claude Opus 5.5 that could iterate autonomously on gameplay design and produce engaging interactive experiences.

#### Community Context

Simon Willison&\#x27;s keynote framing these as discrete inflection points has resonated within AI engineering circles discussing the rapid convergence of coding reliability, autonomous tool-use, and creative capability. Industry observers are noting parallels between current capability thresholds and earlier historical moments in software tooling, while gaming-industry debates over AI-assisted development underscore the cultural impact of these technological shifts.

**Tags**: `#LLMs`, `#coding agents`, `#AI models`, `#software engineering`, `#industry analysis`

---

<a id="item-tech-news-4"></a>
### [WebAssembly runs Firefox in-browser; Anthropic dips below IPO; Tidal bans all-AI music](https://zeli.app/zh/digest/2026-11-24) ⭐️ 8.0/10



rss · Zeli · Nov 24, 23:59

#### Summary

A major browser-based compute milestone has arrived early: using Domen Kožar&\#x27;s unkernel framework, developers have built trynix.dev, which runs over 300,000 Nix packages directly in the browser via WebAssembly with 2–32× performance gains, including full graphical, audio, and network stacks—and successfully launched Firefox inside a browser, achieving a true &quot;browser-in-a-browser&quot; stack. On the policy front, New York Governor Kathy Hochul signed legislation banning automakers from charging subscription fees for pre-installed vehicle features such as heated seats, effective February 27, 2027. In AI news, Anthropic shares briefly fell below their $83 IPO price in premarket trading on November 24 amid broader tech sector weakness. Streaming platform Tidal announced it will ban all AI-generated music starting December 9, expecting to remove millions of tracks and reject tens of thousands daily. Meanwhile, local AI models advanced with Ternary Bonsai 2.5 \(27B\), delivering improved agent-style coding and multi-turn tool use at just 5.9 GB while supporting both H100 and consumer RTX 4090 GPUs. On security, GreyNoise uncovered a sustained, professional intrusion campaign \(GT13\) against Check Point Security Management Servers exploiting CVE-2026-61500 and CVE-2026-16232, compromising at least 22 organizations across finance, energy, and government sectors.

#### Background

WebAssembly \(Wasm\) has long been seen as a pathway to bring near-native performance to browser environments, but historically struggled with full operating-system workloads and complex GUI applications. The &quot;unkernel&quot; approach—running OS-like software directly atop Wasm without a traditional kernel—represents a conceptual shift closer to Gary Bernhardt&\#x27;s vision of JavaScript/Wasm eventually hosting virtually all software. Quad9 is a privacy-focused, malware-blocking DNS resolver whose refusal to comply with France&\#x27;s court order highlights ongoing tensions between national content regulation and global internet infrastructure.

#### Community Discussion

The Firefox-in-browser story generated the most engagement \(370 comments, ~981 points\), with discussion centering on practical implications for sandboxed development, reproducible builds, and whether browser-bound compute can replace local machines. The Anthropic IPO dip drew 716 comments focusing on AI-sector volatility and investor expectations. Community members also expressed concern over the Check Point GT13 campaign, noting the suspected use of LLM-assisted attack tooling and the difficulty of attributing the persistent access. On Tidal&\#x27;s AI music ban, reactions were mixed: some praised the move as necessary quality control, while others questioned enforcement reliability and whether partial-AI or AI-assisted works would survive scrutiny.

**Tags**: `#WebAssembly`, `#browser computing`, `#LLM agents`, `#Nix`, `#open source`

---

<a id="item-tech-news-5"></a>
### [Amazon shifts satellite launches to Falcon 9 and Ariane 6 after ULA failures](https://arstechnica.com/space/2026/11/amazon-surges-launches-with-rival-spacex-after-ula-fails-to-deliver/) ⭐️ 8.0/10



rss · Ars Technica · Nov 24, 18:30

#### Summary

Amazon has turned to SpaceX&\#x27;s Falcon 9 and Arianespace&\#x27;s Ariane 6 to launch its satellite constellation after United Launch Alliance \(ULA\) failed to meet delivery commitments. The company currently has hundreds of satellites sitting in storage awaiting rides to orbit. This shift underscores the growing competitive pressures in commercial spaceflight, where reliability gaps at one launcher provider can force major customers toward rivals. It also highlights Amazon&\#x27;s urgency to deploy its Kuiper broadband network before competitors gain ground.

#### Background

United Launch Alliance operates the Atlas V and Vulcan Centaur rockets but has faced repeated delays and issues with its newer Vulcan rocket in recent years. SpaceX&\#x27;s Falcon 9 remains the most frequently flying launch vehicle globally, while Ariane 6 entered service more recently as Europe&\#x27;s answer to American heavy-lift demand. Amazon&\#x27;s Kuiper project aims to blanket the planet with thousands of low-Earth-orbit internet satellites.

**Tags**: `#space`, `#satellite`, `#Falcon 9`, `#Ariane 6`, `#ULA`

---

<a id="item-tech-news-6"></a>
### [T3 Code Default Telemetry Reads Local Auth Credentials](https://x.com/realchendahuang/status/2125153472450527440) ⭐️ 8.0/10



telegram · zaihuapd · Nov 24, 10:58

#### Summary

Developer @realchendahuang alleges that Theo&\#x27;s T3 Code project enables PostHog telemetry by default since PR \#174 was merged in March, and that PR \#21506, merged in October, reads local authentication files for Codex \(~/.codex/auth.json\) and Claude \(~/.claude.json\), extracting user\_id and accountUuid respectively alongside a device ID for unsalted SHA-256 hashing and upload. Four separate pull requests attempting to disable telemetry were rejected, and official documentation acknowledges that browser and mobile relay diagnostic tracking cannot be turned off. The claims include linked code references; the project team and @theo have not yet responded.

#### Background

T3 Code is an open-source desktop interface that aggregates multiple AI coding agents—including Claude Code, OpenAI Codex, and Cursor—into a single local control panel \[tool-1-3\]. PostHog is a product-analytics platform widely used for telemetry, collecting structured event data such as session traces, tool executions, and system metrics \[tool-1-2\]. In this incident, the tool was alleged to have enabled its PostHog integration by default, then read local authentication files \(~/.codex/auth.json and ~/.claude.json\) to extract non-sensitive identifiers like user IDs and account UUIDs. These identifiers were hashed with unsalted SHA-256 and uploaded alongside device IDs, raising concerns about unintended credential exposure.

<details><summary>References</summary>
<ul>
<li>Claude Code AI Observability installation - Docs - PostHog</li>
<li>GitHub - pingdotgg/t3code: The best way to control Claude Code, Codex ...</li>

</ul>
</details>

**Tags**: `#open source`, `#privacy`, `#telemetry`, `#security`, `#AI tools`

---