---
layout: default
title: "Horizon Summary: 2026-11-24 (EN)"
date: 2026-11-24
lang: en
---

> From 199 items, 8 important content pieces were selected

---

**Technology News**
1. [US states sue SpaceX over Grok CSAM generation](#item-tech-news-1) ⭐️ 9.0/10
2. [Reports: Russia may launch nuclear weapon into orbit as soon as next month](#item-tech-news-2) ⭐️ 9.0/10
3. [NariQ achieves BF16-level quality in 3-bit-and-below Qwen3.8-27B quantizations](#item-tech-news-3) ⭐️ 8.0/10
4. [Z.ai Releases GLM-5.4, Its First Loop Transformer Model](#item-tech-news-4) ⭐️ 8.0/10
5. [Amazon Acquires Decart&\#x27;s AI Optimization Tech for $7.5 Billion](#item-tech-news-5) ⭐️ 8.0/10
6. [Ladybird, the first new browser engine in years, is now available to test](#item-tech-news-6) ⭐️ 8.0/10
7. [Supply-Chain Attack on Codex2api Backdoors 21+ Repos](#item-tech-news-7) ⭐️ 8.0/10
8. [Anthropic 称内部 Claude 模型发现 VP≠VNP 并公开 Lean 4 证明](#item-tech-news-8) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [US states sue SpaceX over Grok CSAM generation](https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/) ⭐️ 9.0/10



rss · Ars Technica · Nov 23, 21:30

#### Summary

Multiple US state attorneys general have filed a lawsuit against SpaceX seeking an injunction to stop Grok from generating child sexual abuse material \(CSAM\) and revenge porn. The filing directly challenges X&\#x27;s claims that every Grok output is screened for harmful content, arguing the measures are insufficient given ongoing violations. If granted, the suit would establish a significant legal precedent in AI accountability and safety enforcement by holding an AI developer accountable through state-level litigation rather than voluntary compliance.

#### Background

Child sexual abuse material \(CSAM\) refers to visual depictions involving minors engaged in sexually explicit conduct, which is illegal to produce, distribute, or possess across all U.S. jurisdictions. Grok is an AI assistant developed by xAI, a company affiliated with Elon Musk and integrated into the X platform, featuring a configurable &quot;spicy mode&quot; that users can toggle to relax content filters for mature-themed outputs. In recent years, regulators have increasingly held tech companies accountable for failures to prevent their generative-AI products from producing harmful nonconsensual imagery, creating a growing framework for civil enforcement through state consumer-protection statutes when federal avenues fall short.

**Tags**: `#artificial intelligence`, `#tech policy`, `#ai safety`, `#csam prevention`, `#legal precedent`

---

<a id="item-tech-news-2"></a>
### [Reports: Russia may launch nuclear weapon into orbit as soon as next month](https://arstechnica.com/space/2026/11/russia-may-launch-a-nuclear-armed-satellite-far-sooner-than-we-thought/) ⭐️ 9.0/10

Reports indicate Russia may test a nuclear-armed satellite in orbit as early as next month, raising concerns about catastrophic damage to global satellite infrastructure from a nuclear detonation in space.

rss · Ars Technica · Nov 23, 19:28

**Tags**: `#nuclear weapons`, `#space technology`, `#satellite infrastructure`, `#geopolitics`, `#defense technology`

---

<a id="item-tech-news-3"></a>
### [NariQ achieves BF16-level quality in 3-bit-and-below Qwen3.8-27B quantizations](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) ⭐️ 8.0/10



hackernews · toebee · Nov 23, 13:42 · [Discussion](https://news.ycombinator.com/item?id=50611402)

#### Summary

Nari Labs has released NariQ, an ultra-low-bit quantization of the Qwen3.8-27B model that claims to retain near-BF16-level performance at 3-bit, 2.5-bit, and 2-bit precision. The team states this is the first 3-bit-or-lower quantization maintaining BF16-grade results on long-horizon agentic tasks. Published benchmarks cover DeepSWE \(41.0 / 41.9 / 28.6\), Terminal-Bench 2.1 \(63.8 / 60.2 / 52.4\), AIME 25+26 \(98.3 / 96.5 / 86.0\), MSGM \(93.1 / 91.8 / 90.6\), and RealWorldQA \(82.4 / 81.3 / 80.9\), comparing 3-bit, 2.5-bit, and 2-bit against the BF16 baseline. Context-length throughput was measured on an RTX PRO 6000 across 4K, 16K, and 64K sequences, including a comparison to Unsloth&\#x27;s UD-IQ3\_XXS. The GGUF files are available on Hugging Face, but inference currently requires a dedicated nari-labs fork of llama.cpp.

#### Community Discussion

Community feedback has been mixed but engaged. Some users praised the project for evaluating multiple long-horizon task types rather than narrowly optimizing for benchmark datasets. Others raised skepticism, noting that performance gains may partly stem from harness differences rather than model quality alone. Questions were also raised about what information is actually discarded at such low bit depths, Apple M-series compatibility constraints on consumer hardware like 16 GB Macs, and the broader landscape of competing quant methods such as TCQ and GSQ-RCO awaiting head-to-head benchmarks.

**Tags**: `#quantization`, `#LLM efficiency`, `#self-hosted AI`, `#model deployment`

---

<a id="item-tech-news-4"></a>
### [Z.ai Releases GLM-5.4, Its First Loop Transformer Model](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 8.0/10



rss · Simon Willison · Nov 23, 23:40

#### Summary

Z.ai has released GLM-5.4, the first model from the Chinese AI lab to use a looped transformer architecture, where weight-shared layers iterate multiple times per token to refine hidden states—producing a deeper effective network without increasing parameter count. The release follows another recent iteration of the same approach, Inkling 2 Mini from Thinking Machines Lab \(November 20\), which runs its middle layers three times per token to improve reasoning quality on agentic coding tasks. GLM-5.4 is not yet available as open weights; access requires signing up for Z.ai’s Coding Plan subscription, though it shares the same OpenAI-compatible Responses API endpoint at api.z.ai/api/v1. Testing by Simon Willison showed visual output quality comparable to GLM-5.3 and stylistically closer to OpenAI or Anthropic models than the more distinctive earlier GLM-5.1 and GLM-5.2 generations.

**Tags**: `#AI architectures`, `#transformer models`, `#LLMs`, `#model design`

---

<a id="item-tech-news-5"></a>
### [Amazon Acquires Decart&\#x27;s AI Optimization Tech for $7.5 Billion](https://techcrunch.com/2026/11/23/amazon-snaps-up-decarts-ai-optimization-tech-for-7-5b-as-it-prepares-to-sell-trainium-chips/) ⭐️ 8.0/10



rss · TechCrunch · Nov 23, 17:14

#### Summary

Amazon is acquiring Decart&\#x27;s AI optimization technology and research team in a reported $7.5 billion deal, according to a November 2026 report by TechCrunch. The acquisition positions Amazon to better support its upcoming sale of Trainium chips, its custom AI inference hardware line. The deal encompasses both Decart&\#x27;s optimization software and its research team, signaling Amazon&\#x27;s intent to deepen its software stack around its own silicon. This move reflects a broader industry trend of cloud providers integrating AI acceleration tooling directly with their proprietary hardware.

#### Background

Decart is an Israeli AI startup specializing in compiler and optimization technology for machine learning models. Their work focuses on translating high-level AI model specifications into efficient code tailored to specific silicon, a capability critical for custom AI chips like Amazon&\#x27;s Trainium series. Training and inference optimization compilers bridge the gap between software frameworks and proprietary hardware, allowing vendors to differentiate their chips through performance rather than raw compute alone.

**Tags**: `#AI infrastructure`, `#acquisition`, `#cloud computing`, `#hardware`

---

<a id="item-tech-news-6"></a>
### [Ladybird, the first new browser engine in years, is now available to test](https://www.theverge.com/tech/1040872/ladybird-indie-browser-engine-alpha-testing) ⭐️ 8.0/10

Ladybird, an independent browser built from scratch with a new rendering engine, has entered alpha testing on macOS and Linux after over four years of development.

rss · The Verge · Nov 23, 22:38

**Tags**: `#browser engine`, `#open source`, `#web technology`, `#systems software`

---

<a id="item-tech-news-7"></a>
### [Supply-Chain Attack on Codex2api Backdoors 21+ Repos](https://github.com/WormW/codex2api-incident-2026-11) ⭐️ 8.0/10

An attacker compromised the codex2api maintainer account and pushed a backdoored release that stripped authentication and exfiltrated repository secrets.

telegram · zaihuapd · Nov 23, 11:21

#### Summary

The maintainer account of the open-source project codex2api was compromised, and an attacker bypassed the main branch to push tag v3.1.11 containing a malicious release. This version removed authentication entirely, enabling unauthenticated remote code execution, while a workflow was added to exfiltrate over 16 GitHub Actions secrets per affected repository. The compromise spans at least 21 repositories under the same account. Users who installed or updated versions 3.1.10 through 3.1.12 are advised to immediately revert to v3.1.9 and rotate all exposed credentials, including GitHub tokens, SSH keys, database passwords, and DeepSeek API keys.

#### Background

Supply-chain attacks target open-source projects by compromising maintainers&\#x27; accounts or CI/CD pipelines to inject malicious code into widely distributed packages. Once attackers gain access to a trusted repository, they can modify releases or workflows to steal secrets, execute arbitrary commands, or spread further compromise downstream to every user and dependent project.

#### Community Discussion

No community comments were available for this item.

**Tags**: `#supply-chain attack`, `#open-source security`, `#credential compromise`, `#code backdoor`, `#security advisory`

---

<a id="item-tech-news-8"></a>
### [Anthropic 称内部 Claude 模型发现 VP≠VNP 并公开 Lean 4 证明](https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md) ⭐️ 8.0/10

Anthropic claims an internal Claude model discovered and formally proved VP≠VNP via Lean 4, but the result lacks human verification and has noted open discrepancies.

telegram · zaihuapd · Nov 24, 06:02

**Tags**: `#theoretical computer science`, `#AI research`, `#complexity theory`, `#formal verification`, `#Lean theorem prover`

---