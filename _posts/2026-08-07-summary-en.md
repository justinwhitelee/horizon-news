---
layout: default
title: "Horizon Summary: 2026-08-07 (EN)"
date: 2026-08-07
lang: en
---

> From 192 items, 7 important content pieces were selected

---

**Technology News**
1. [ByteDance trains 10-trillion-parameter AI model to rival Anthropic](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI Pauses Astra Development Over Critical Cyber Capability Risks](#item-tech-news-2) ⭐️ 9.0/10
3. [DeepSeek V4 Flash 0731 local performance and cost](#item-tech-news-3) ⭐️ 8.0/10
4. [Postgres analytics speedup via batching, fusion, and SIMD](#item-tech-news-4) ⭐️ 8.0/10
5. [AMD acquires Taalas for silicon-etched AI inference](#item-tech-news-5) ⭐️ 8.0/10
6. [TSMC and researchers achieve sub-1nm transistor breakthrough](#item-tech-news-6) ⭐️ 8.0/10
7. [US reviews China&\#x27;s offshore Nvidia chip access](#item-tech-news-7) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ByteDance trains 10-trillion-parameter AI model to rival Anthropic](https://arstechnica.com/ai/2026/08/bytedance-trains-massive-ai-model-in-bid-to-rival-anthropic/) ⭐️ 9.0/10



rss · Ars Technica · Aug 7, 13:29

#### Summary

ByteDance, the parent company of TikTok, is training a massive AI model with 10 trillion parameters in a direct bid to compete with Anthropic. This development marks a significant escalation in the competitive landscape for large language models, as ByteDance moves to match the scale of leading AI research labs. The move underscores the intensifying race among major technology companies to build increasingly powerful AI systems capable of rivaling specialized AI research organizations.

**Tags**: `#AI`, `#Large Language Models`, `#Industry News`, `#ByteDance`, `#Anthropic`

---

<a id="item-tech-news-2"></a>
### [OpenAI Pauses Astra Development Over Critical Cyber Capability Risks](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) ⭐️ 9.0/10



telegram · zaihuapd · Aug 7, 16:44

#### Summary

On August 7, 2026, OpenAI disclosed that its upcoming Astra model may have reached a &quot;critical&quot; threshold for autonomous cyber-attack capabilities, prompting a pause in related internal activities. Unlike previous models such as GPT-5.6-Sol, which were rated only &quot;high,&quot; Astra&\#x27;s internal assessments showed significant progress in agent coding and cybersecurity, raising the possibility that it could autonomously discover and exploit zero-day vulnerabilities in hardened systems or execute end-to-end attacks without human intervention. In response, OpenAI has implemented isolation testing environments, enhanced encryption, and universal monitoring while collaborating with government agencies and AI safety organizations for third-party testing. The company indicated that expanded safety testing could delay the model&\#x27;s release.

**Tags**: `#AI Safety`, `#Cybersecurity`, `#OpenAI`, `#Autonomous Agents`, `#AI Governance`

---

<a id="item-tech-news-3"></a>
### [DeepSeek V4 Flash 0731 local performance and cost](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10



hackernews · tosh · Aug 7, 17:56 · [Discussion](https://news.ycombinator.com/item?id=49214008)

#### Summary

DeepSeek V4 Flash 0731 is a locally deployable AI model release that users describe as significantly more capable than earlier previews, with strong performance for debugging and document analysis. On dual RTX Pro 6000 Blackwell GPUs, it achieves approximately 8,000 tokens per second during prefill and around 250 tokens per second on single-stream inference. Users report very low operational costs, with some running multiple concurrent sessions on consumer hardware for under $5 per day, and OpenCode Go offering temporary double token limits that effectively increase value. Despite these strengths, some users have encountered issues such as infinite loops, unintended tool call behavior, and occasional off-topic responses.

#### Community Discussion

The Hacker News thread is partially derailed by an unrelated account ban story involving Claude, but the technical discussion highlights strong local performance and cost efficiency for DeepSeek V4 Flash 0731. Users running it on consumer hardware like Raspberry Pi setups report it is &\#x27;good enough for almost everything&\#x27; at negligible cost. However, some users note reliability concerns including infinite loops and erratic topic shifts, particularly when using Pi agent.

**Tags**: `#AI Models`, `#Local LLMs`, `#Open Source`, `#Software Engineering`

---

<a id="item-tech-news-4"></a>
### [Postgres analytics speedup via batching, fusion, and SIMD](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10



hackernews · poly2it · Aug 7, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49208535)

#### Summary

A technical article describes how batching, operator fusion, and SIMD optimizations can make Postgres roughly 300 times faster for analytics workloads. The author, who is also promoting a project called pgrust, says correctness is the top priority and reports having formally verified or fuzz-tested over 1,000 user-facing functions against Postgres. Community discussion highlights both enthusiasm for features like adaptive planning and skepticism about adopting a non-core Postgres implementation due to trust, longevity, and continuity concerns. Commenters also raised interest in the project&\#x27;s I/O and thread scheduling design and suggested in-memory filesystems as a simpler performance workaround.

#### Background

Postgres is widely used for transactional workloads but has historically been optimized more for OLTP than for heavy analytical queries. Batching processes rows in groups rather than one at a time, operator fusion reduces intermediate materialization by combining query steps, and SIMD uses vector CPU instructions to accelerate data-parallel operations. These techniques are common in modern columnar and analytics engines, which is why community members noted that adaptive planning and better resource scheduling are features many Postgres users have long wanted.

#### Community discussion

Readers praised the performance direction but questioned whether users will adopt pgrust over Postgres because trust involves more than speed, including project continuity and stewardship. Some users expressed strong interest in adaptive planning and better I/O and thread scheduling to address noisy-neighbor issues. Others offered practical alternatives such as running Postgres on tmpfs for large in-memory workloads.

**Tags**: `#database optimization`, `#Postgres`, `#SIMD`, `#query engine`, `#operator fusion`

---

<a id="item-tech-news-5"></a>
### [AMD acquires Taalas for silicon-etched AI inference](https://zeli.app/zh/digest/2026-08-06) ⭐️ 8.0/10



rss · Zeli · Aug 6, 23:59

#### Summary

AMD has acquired AI chip startup Taalas to accelerate custom silicon inference by etching model weights directly into silicon rather than relying on HBM memory. The approach uses model-specific integrated circuits \(MSICs\), with Taalas&\#x27; first test chip HC1 reaching 16,960 tokens per second on Meta&\#x27;s Llama 3.1 8B model, outperforming Nvidia GPUs and Cerebras accelerators. AMD plans to integrate Taalas chips with its Instinct Helios rack architecture to reduce inference costs and improve speed, noting that updating models requires only two metal layer changes instead of full retraining. The digest also highlights a Pareto optimization analysis of Mario Kart 8 configurations, Qwen3.8 Max topping the Artificial Analysis agentic index, and OpenAI&\#x27;s GPT-5.6 update offering unlimited free chat.

#### Background

AI inference performance is often bottlenecked by memory bandwidth when models reside in HBM rather than being computed on-chip. Model-specific integrated circuits \(MSICs\) represent a specialized hardware approach where neural network weights are physically etched into silicon, trading flexibility for significantly higher throughput and lower latency. This contrasts with general-purpose GPUs and TPUs, which store weights in external memory and fetch them during computation.

#### Community Discussion

The AMD-Taalas acquisition generated 658 HN comments, indicating strong community interest in AMD&\#x27;s strategy to challenge Nvidia&\#x27;s AI hardware dominance. Discussion likely centered on the tradeoffs of fixed-function inference silicon versus programmable GPUs, and whether etching models into silicon is viable given rapid model iteration cycles.

**Tags**: `#AI Hardware`, `#M&amp;A`, `#Optimization`, `#Tech News`, `#Open Source`

---

<a id="item-tech-news-6"></a>
### [TSMC and researchers achieve sub-1nm transistor breakthrough](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOeENnZnVXeklGQ0l3MVQ0cUp4c09JZVR2RnZhdHBOY3NtbkR0WTNlRWZxV2d2SUMxYl9TekdDbG5wRXVQU2pkWlVKYWNZVWZjWlhmNzQ3YWVUdlVvWEZsTXFnaFB2VklJX2ZKc2tXVk9POXBzZXViMDJUYUxhRGZkS1pRU3lPT2J5RVBucHZnTTdSMU1aQzJiblRocktJalBjMkplSE5yN091ZXFSY3AwVmx2dlMyWDhrYnpKbEhkRWVVcUFzQUlibUhrYmtVWi1hbWxQQUJmalNvNTJUNWVFUzVSLUVYbndHMkHSAe8BQVVfeXFMUFkxNkluS0wybnl6WHdMeTFJbFBDak9UQnpFblF4a3d0aWhjUTNUV3lxbDhUZjBaZk5KbVpvM3FTWGpNLU9Lc25hTlJNbWRCZ3d0RkhHS3NDekJHeHJJVFlid3RkdkZwU0xlRzhVX3ZGTkczaE1YYks4Z21mTElQcHdiZHpqV1pJVDd2NVF0TmFnZmNabmE2MW9YUjhsdlduNVFXaWRjb0JPY21sSGtvdjBmTnZVbXJJWjdsblItcWVPYlp0Q3NzQjBmZ2tIZ1BxbnR1ZndkMHpUSWtlNlZZVVk4bjFoYU02SWFwV3E5M0k?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · Aug 7, 16:16

#### Summary

TSMC and collaborating researchers have announced a significant breakthrough in chip transistor technology as part of their ongoing effort to develop sub-1-nanometer manufacturing processes. This advancement represents a major step forward in semiconductor physics and fabrication techniques, potentially extending Moore&\#x27;s Law beyond current physical limitations. The specific technical details of the breakthrough were not provided in the initial report.

**Tags**: `#semiconductors`, `#hardware`, `#transistor technology`, `#manufacturing`, `#nanotechnology`

---

<a id="item-tech-news-7"></a>
### [US reviews China&\#x27;s offshore Nvidia chip access](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 8.0/10



telegram · zaihuapd · Aug 7, 11:18

#### Summary

The US Commerce Department&\#x27;s Bureau of Industry and Security \(BIS\) is systematically reviewing how Chinese AI firms access Nvidia chips overseas, including via remote cloud computing, following allegations of illegal procurement. This review was triggered after a White House official accused Moonshot AI of illegally obtaining Nvidia chips and accessing them remotely through Thailand, coinciding with the release of its Kimi K3 model. BIS is compiling two lists: countries with black markets for smuggled restricted chips and nations where Chinese companies remotely rent chip capacity. While remote access itself is not illegal, the US House has passed a bipartisan bill to clarify BIS&\#x27;s authority over such cloud computing agreements, though this faces opposition from tech companies like Nvidia. Additionally, Alibaba is under investigation for allegedly using a Singapore shell company controlled via the Cayman Islands to access Nvidia chips in Malaysia through Megaspeed.

**Tags**: `#AI policy`, `#hardware access`, `#Nvidia`, `#export controls`, `#cloud computing`

---