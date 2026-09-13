---
layout: default
title: "Horizon Summary: 2026-09-13 (EN)"
date: 2026-09-13
lang: en
---

> From 141 items, 4 important content pieces were selected

---

**Technology News**
1. [Clay Institute Announces Possible Resolution of Navier-Stokes Problem](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI Claims Solution to Millennium Prize Problem](#item-tech-news-2) ⭐️ 9.0/10
3. [HN Digest: AI-agent RubyGems attack, Google SERP changes, Android VPN flaw](#item-tech-news-3) ⭐️ 8.0/10
4. [NVIDIA in Talks to Invest Up to $10B in Anthropic&\#x27;s $100B Mega-IPO](#item-tech-news-4) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Clay Institute Announces Possible Resolution of Navier-Stokes Problem](https://www.claymath.org/news/navier-stokes-announcement/) ⭐️ 9.0/10



hackernews · rvz · Sep 12, 04:09 · [Discussion](https://news.ycombinator.com/item?id=49668706)

#### Summary

The Clay Mathematics Institute \(CMI\) announced that the Navier-Stokes existence and smoothness problem—one of the seven Millennium Prize Problems—appears to have been settled, with a Lean 4 formal proof circulating. The statement notably uses the qualifier &quot;apparently&quot; and avoids mentioning OpenAI, despite the proof being associated with them. CMI rules require solutions to be published in a qualifying outlet before a two-year review period begins, meaning the clock has not yet started ticking. Community discussion highlights concerns about whether the resolution introduces new mathematical techniques or merely adds a fact to existing knowledge.

#### Background

The Navier–Stokes existence and smoothness problem is one of the Clay Mathematics Institute&\#x27;s seven Millennium Prize Problems, posing the challenge of proving whether smooth solutions always exist for the equations describing fluid motion. A formal proof in Lean 4 is a machine-checked verification of a mathematical argument, ensuring every logical step conforms to formal axioms. The Clay Mathematics Institute requires that any proposed solution be published in a qualifying peer-reviewed outlet and remain under community review for at least two years before it can be considered for the prize.

#### Community Discussion

Commenters note CMI&\#x27;s cautious language and neutral stance, with one observing that the word &\#x27;OpenAI&\#x27; does not appear in the statement despite the proof&\#x27;s origin. Others question whether the result reveals new mathematical techniques or simply adds an unverified fact. The two-year publication rule means official recognition remains distant, and concerns about trust in AI-assisted mathematical work persist.

<details><summary>References</summary>
<ul>
<li><a href="https://www.claymath.org/news/navier-stokes-announcement/">Navier-Stokes Announcement - Clay Mathematics Institute</a></li>
<li><a href="https://theroboticsmedia.com/article/openai-navier-stokes-millennium-prize-lean-proof-gpt-6-astra-september-8-2026">OpenAI&#x27;s AI Resolves Navier-Stokes Millennium Prize Problem</a></li>

</ul>
</details>

**Tags**: `#mathematics`, `#formal verification`, `#AI-assisted theorem proving`, `#Millennium Prize Problems`, `#Navier-Stokes`

---

<a id="item-tech-news-2"></a>
### [OpenAI Claims Solution to Millennium Prize Problem](https://www.theverge.com/ai-artificial-intelligence/994255/openai-millennium-prize-problem-tristan-buckmaster-competition) ⭐️ 9.0/10



rss · The Verge · Sep 12, 11:00

#### Summary

OpenAI has claimed to solve one of the Millennium Prize problems, a set of seven renowned unsolved mathematics challenges. The announcement has sparked debate among mathematicians about the implications of AI-driven mathematical discovery. According to The Verge, while such an achievement would normally be celebrated as historic, many in the mathematics community have watched OpenAI&\#x27;s rapid advance with growing concern rather than pure enthusiasm.

#### Millennium Prize Problems and AI-Driven Mathematics

The Millennium Prize Problems are seven unsolved mathematical challenges designated by the Clay Mathematics Institute, each carrying a $1 million reward. The Navier-Stokes existence and smoothness problem, which concerns the behavior of fluid flows, is one of these seven and has remained unsolved since the list was published in 2000. OpenAI&\#x27;s claim involves an AI-generated solution to this specific problem, with a formal proof verified in Lean, a computer proof assistant used to validate mathematical correctness.

<details><summary>References</summary>
<ul>
<li><a href="https://emergent.sh/news/openai-claims-navier-stokes-millennium-prize">OpenAI Claims Navier-Stokes Millennium Prize Solution</a></li>
<li><a href="https://phys.org/news/2026-09-openai-ai-agents-math-hardest.html">OpenAI says 10,000 AI agents cracked one of math&#x27;s hardest...</a></li>

</ul>
</details>

**Tags**: `#artificial intelligence`, `#mathematics`, `#AI research`, `#Millennium Prize`

---

<a id="item-tech-news-3"></a>
### [HN Digest: AI-agent RubyGems attack, Google SERP changes, Android VPN flaw](https://zeli.app/zh/digest/2026-09-12) ⭐️ 8.0/10

This week&\#x27;s highlights include a coordinated AI-driven attack on the RubyGems ecosystem, Google quietly rewriting search result URLs to fight scrapers, and several security and performance stories from the open-source community.

rss · Zeli · Sep 12, 23:59

#### Summary

In May 2026, hundreds of AI-generated malicious packages were uploaded to RubyGems by what the community now calls &quot;GemStuffer&quot; — an operation using OpenAI agent tooling to exploit a vulnerability in RubyGems servers for API key theft and abuse RubyDoc.info&\#x27;s auto-build system for remote code execution to scrape UK local government data. The RubyGems team was forced to pause new user registrations for four days, though OpenAI has not acknowledged responsibility. Meanwhile, Google is silently redirecting all search result links through google.com/goto?url= proxies instead of exposing target URLs directly in HTML, raising the cost of SERP scraping for AI crawlers and SEO tools and forcing downstream developers to read Location headers instead of following redirects. On the security side, a new Android vulnerability allows malicious apps to route traffic around VPN tunneling even with &quot;block without VPN&quot; enforced, by exploiting UDP keep-alive connections at the hardware Wi-Fi or cellular modem level; GrapheneOS is working on a fix. In performance news, a benchmark article argues that Rust-based Polars and SQLite-style DuckDB outperform Pandas by tens of times on 1 billion-row workloads for the common sub-100GB dataset range, while a reverse-engineering deep-dive traces Apple Neural Engine&\#x27;s architectural evolution from CNN-era assumptions to the M5 chip&\#x27;s GPU-integrated design. Finally, Anthropic CEO Dario Amodei published a call to &quot;pace the frontier&quot; of AI capability growth, proposing embedded third-party safety evaluation — a move one HN commenter challenged by suggesting Anthropic should instead push for mandatory open-weight requirements to truly slow capable model iteration.

#### Background

RubyGems is the default package manager for Ruby, and RubyDoc.info auto-generates documentation from uploaded gems; compromise of either infrastructure can enable supply-chain attacks. Google&\#x27;s shift to goto URL rewriting mirrors similar anti-scraping tactics used by other search engines, but represents a notable change in scale for the largest search provider. The Android VPN bypass exploits the OS network stack&\#x27;s handling of low-level UDP keep-alive packets, which can circumvent VPN routing rules without requiring root or special permissions — a class of issue relevant to any system relying on VPN-only traffic enforcement.

**Tags**: `#AI security`, `#supply chain attacks`, `#open source`, `#search infrastructure`, `#malware`

---

<a id="item-tech-news-4"></a>
### [NVIDIA in Talks to Invest Up to $10B in Anthropic&\#x27;s $100B Mega-IPO](https://www.reuters.com/legal/transactional/nvidia-talks-invest-anthropics-mega-ipo-sources-say-2026-09-11/) ⭐️ 8.0/10



telegram · zaihuapd · Sep 12, 01:55

#### Summary

According to Reuters, NVIDIA is in discussions to serve as an anchor investor in Anthropic&\#x27;s planned initial public offering, potentially contributing up to $10 billion. Anthropic aims to raise as much as $100 billion in the offering, which could value the AI company at approximately $2 trillion. The plans remain under negotiation and are subject to change.

**Tags**: `#AI industry`, `#IPO news`, `#NVIDIA`, `#Anthropic`, `#major investment`

---