---
layout: default
title: "Horizon Summary: 2026-11-18 (EN)"
date: 2026-11-18
lang: en
---

> From 204 items, 8 important content pieces were selected

---

**Technology News**
1. [Nvidia Board Will Not Reinstate Jensen Huang as CEO](#item-tech-news-1) ⭐️ 10.0/10
2. [Java4Shell: RCE in OpenJDK via Base64 Handling](#item-tech-news-2) ⭐️ 9.0/10
3. [Ole Rømer proved light has a finite speed 350 years ago](#item-tech-news-3) ⭐️ 9.0/10
4. [Google&\#x27;s AI Answers Cut Search Referral Traffic by 40%](#item-tech-news-4) ⭐️ 8.0/10
5. [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](#item-tech-news-5) ⭐️ 8.0/10
6. [Nvidia halts Singapore sales disclosure as subsidiary reports $104B](#item-tech-news-6) ⭐️ 8.0/10
7. [Datasette Lite rewritten to run full Python app in browser via Pyodide and service workers](#item-tech-news-7) ⭐️ 8.0/10
8. [Nvidia is abandoning China after Jensen Huang’s ouster](#item-tech-news-8) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Nvidia Board Will Not Reinstate Jensen Huang as CEO](https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo) ⭐️ 10.0/10



rss · The Verge · Nov 17, 22:05

#### Summary

Nvidia&\#x27;s new board chair Harvey Jones announced on Tuesday&\#x27;s quarterly earnings call that the board unanimously accepted Jensen Huang&\#x27;s resignation and does not intend to reinstate him as CEO. Huang had previously offered to return to his top role after resigning the prior week, but the board has shut down that possibility. Jones also stated the company would not address or take questions about the circumstances surrounding the resignation during the call. The announcement marks a significant leadership transition at one of the most influential companies in AI and hardware.

#### Background

Jensen Huang founded Nvidia in 1993 and has served as its CEO since, becoming one of the most prominent figures in the artificial intelligence industry as the company&\#x27;s GPUs became essential hardware for AI training and inference. His resignation came after public disclosure related to the company&\#x27;s sales activities involving China and national security concerns. An online petition calling for his reinstatement has garnered more than 180,000 signatures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/jensen-huang-nvidia-ceo-reinstatement-petition/">Nvidia&#x27;s board of directors is against bringing back Jensen ...</a></li>
<li><a href="https://www.reuters.com/legal/transactional/nvidia-board-says-it-does-not-intend-reinstate-jensen-huang-ceo-2026-11-17/">Nvidia board says it does not intend to reinstate Jensen ...</a></li>
<li><a href="https://apnews.com/article/nvidia-jensen-huang-china-national-security-chips-3026bcbe04ab57b844884382e583422a">Nvidia rejects Jensen Huang&#x27;s offer to return as CEO | AP News</a></li>

</ul>
</details>

**Tags**: `#corporate leadership`, `#AI hardware`, `#NVIDIA`, `#industry announcement`, `#executive transition`

---

<a id="item-tech-news-2"></a>
### [Java4Shell: RCE in OpenJDK via Base64 Handling](https://calif.io/java4shell/) ⭐️ 9.0/10



hackernews · werrett · Nov 17, 21:11 · [Discussion](https://news.ycombinator.com/item?id=50538240)

#### Summary

A remote code execution vulnerability dubbed Java4Shell has been disclosed in OpenJDK&\#x27;s Base64 decoding implementation, affecting all HotSpot-based JVMs including OpenJDK, Oracle JDK, and GraalVM. The exploit triggers when a specially crafted Base64 payload reaches vulnerable code paths in the JIT compiler, generating machine-code stubs that can be hijacked for arbitrary code execution. Successful exploitation requires remote heap grooming—an attacker must carefully arrange objects in the target JVM&\#x27;s memory over the network to gain control of execution flow. The attack was demonstrated over public IP addresses in production-relevant conditions, though it remains sensitive to network characteristics such as round-trip time and jitter, with low stable latency preferred for reliable exploitation. Detection tooling has already been released by Semgrep, which scans for five identifying conditions of the vulnerable configuration. An unconfirmed claim circulating on social media suggests the vulnerability may be linked to the AVX512-optimized Base64 decoder path, with a possible workaround via the -XX:UseAVX=2 JVM flag.

#### Community Discussion

Commenters noted the exploit requires specific hot-spot conditions and low-latency network connectivity to succeed reliably, but expressed concern that weaponization for attacks on critical infrastructure could follow within months. Detection coverage is considered strong given the early availability of free Semgrep rules. The broader takeaway from the community is that this vulnerability exposes deep attack surface in legacy Java stacks and may accelerate modernization efforts among organizations with inadequate security posture.

**Tags**: `#Java security`, `#RCE vulnerability`, `#OpenJDK`, `#Heap exploitation`, `#Critical CVE`

---

<a id="item-tech-news-3"></a>
### [Ole Rømer proved light has a finite speed 350 years ago](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969) ⭐️ 9.0/10



hackernews · dxs · Nov 17, 19:25 · [Discussion](https://news.ycombinator.com/item?id=50536813)

#### Summary

A 350th-anniversary piece marks Ole Rømer&\#x27;s 1676 demonstration that light travels at a finite speed—a landmark shift from the long-held assumption of instantaneous light. Rømer reached this conclusion by observing timing discrepancies in the eclipses of Jupiter&\#x27;s moon Io, which varied depending on Earth&\#x27;s distance from Jupiter. The discovery fundamentally changed astronomy and physics by providing the first quantitative evidence that light has a measurable speed rather than moving instantaneously across any distance. While the original 1676 observations could not yield the precise modern value, they established the conceptual breakthrough that light&\#x27;s propagation time was observable and quantifiable.

#### Community Discussion

Commenters shared supplementary materials including a web comic, an explanatory YouTube video, and Greg Egan&\#x27;s science-fiction trilogy exploring a variable speed of light. Some readers expressed confusion about the eclipse-measurement logic, noting surprise that 17th-century clocks were accurate enough for the observation. Others contributed related puzzles and party-trivia notes, highlighting how counterintuitive the discovery remains to many.

**Tags**: `#physics`, `#history-of-science`, `#astronomy`, `#paradigm-shift`, `#light-speed`

---

<a id="item-tech-news-4"></a>
### [Google&\#x27;s AI Answers Cut Search Referral Traffic by 40%](https://revscope.co/blog/search-seo-geo-2026/) ⭐️ 8.0/10



hackernews · slashdev · Nov 18, 00:17 · [Discussion](https://news.ycombinator.com/item?id=50540178)

#### Summary

Google&\#x27;s AI-generated answers are reducing search referral traffic to websites by approximately 40%, according to RevScope&\#x27;s analysis of SEO and GEO trends for 2026. This shift raises concerns about the sustainability of traditional search-dependent business models, the viability of SEO as a discipline, and the long-term health of the open web. The trend aligns with what The Verge has termed &quot;Google Zero,&quot; where Google increasingly serves answers directly in its interface rather than referring users to external sites. Community discussion reflects both resignation—some note that clickbait-laden results were already degrading discovery—and urgency, warning that without significant traffic from search engines, there may be little incentive for platforms to allow their content to be indexed at all.

#### Background

Search engines have historically driven massive referral traffic to websites through organic results, enabling a content economy built on ad revenue and subscriptions. Google&\#x27;s introduction of AI Overviews \(also called Generative Experience or GEO\) places LLM-generated summaries directly on the search results page, reducing the need for users to click through to source websites. This mirrors broader industry movement toward conversational AI interfaces like ChatGPT, which bypass traditional search altogether.

#### Community Discussion

Commenters express mixed reactions: some welcome the direct answers as an improvement over clickbait-heavy results, while others mourn the loss of content discovery and warn that the open web faces an existential threat if search engines no longer drive meaningful traffic. One user notes that ChatGPT has reduced their Google use even more dramatically than the reported 40%. There is concern that without traffic incentives, websites may resist being indexed, and a two-tier system could emerge between free, lower-quality AI answers and paid services offering better models.

**Tags**: `#search\_engine`, `#AI`, `#SEO`, `#open\_web`, `#LLM`

---

<a id="item-tech-news-5"></a>
### [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 8.0/10

Quad9&\#x27;s withdrawal from France amid regulatory pressure on DNS blocking raises concerns about internet freedom, corporate complicity, and the rollback of European digital rights that emerged in the early 2000s.

hackernews · subset · Nov 17, 22:13 · [Discussion](https://news.ycombinator.com/item?id=50538994)

**Tags**: `#internet governance`, `#DNS policy`, `#digital rights`, `#corporate compliance`, `#European regulation`

---

<a id="item-tech-news-6"></a>
### [Nvidia halts Singapore sales disclosure as subsidiary reports $104B](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) ⭐️ 8.0/10



hackernews · louiereederson · Nov 17, 17:12 · [Discussion](https://news.ycombinator.com/item?id=50534631)

#### Summary

Nvidia has stopped breaking out Singapore-related sales in its financial disclosures after its Singapore subsidiary reported $104 billion in external revenue for 2025. The shift comes amid U.S. investigations into whether the Singapore entity, known as Megaspeed, was used to route Nvidia GPUs to China in potential circumvention of export controls. The $104B figure represents revenue flowing through the Singapore entity, which serves as part of Nvidia&\#x27;s distribution channel through OEMs, ODMs, and resellers rather than direct end-customer sales.

#### Community Discussion

Hacker News commenters offered mixed interpretations. Some clarified that the $104B reflects routing through Nvidia&\#x27;s reseller network rather than direct sales, noting the article itself was unclear. Others speculated about sanctions evasion, with one commenter jokingly claiming Jensen Huang was fired over allegations tied to the Singapore-China chip pathway. A few respondents pushed back, characterizing the story as primarily an accounting attribution question rather than evidence of wrongdoing.

**Tags**: `#AI hardware`, `#semiconductors`, `#export controls`, `#corporate finance`, `#industry news`

---

<a id="item-tech-news-7"></a>
### [Datasette Lite rewritten to run full Python app in browser via Pyodide and service workers](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10



rss · Simon Willison · Nov 17, 16:48

#### Summary

Simon Willison has released a complete rewrite of Datasette Lite, which now runs the full server‑side Datasette Python application directly in the browser using Pyodide \(WebAssembly\) and service workers. The new version supports loading SQLite databases, JSON files, CSV files, and SQL scripts; selecting specific Datasette versions from PyPI or GitHub commits/tags; choosing among over 100 SQLite builds; and installing plugins from PyPI or wheel URLs. This makes it possible to share self‑contained, URL‑addressable demos of work‑in‑progress features or bug reproductions without spinning up a separate web server. The earlier version was a hack that could not run JavaScript‑based plugins, whereas the service‑worker‑based architecture allows the entire application—including interactive visualizations—to execute client‑side.

**Tags**: `#WebAssembly`, `#Python`, `#Web technology`, `#Open source tools`, `#Browser-based computing`

---

<a id="item-tech-news-8"></a>
### [Nvidia is abandoning China after Jensen Huang’s ouster](https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/) ⭐️ 8.0/10

Nvidia&\#x27;s interim CEO has reportedly ended chip sales to China, signaling a major strategic shift with implications for the AI hardware market.

rss · TechCrunch · Nov 17, 23:37

**Tags**: `#semiconductors`, `#AI hardware`, `#geopolitics`, `#Nvidia`, `#china trade`

---