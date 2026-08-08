---
layout: default
title: "Horizon Summary: 2026-08-08 (EN)"
date: 2026-08-08
lang: en
---

> From 141 items, 3 important content pieces were selected

---

**Technology News**
1. [SGLang v0.5.17 adds day-0 support for Kimi K3 and MiniMax-H3](#item-tech-news-1) ⭐️ 8.0/10
2. [DeepMind&\#x27;s WeatherNext achieves breakthrough in cyclone forecasting](#item-tech-news-2) ⭐️ 8.0/10
3. [macOS Screen Sharing Vulnerability Allows Unauthenticated Login](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [SGLang v0.5.17 adds day-0 support for Kimi K3 and MiniMax-H3](https://github.com/sgl-project/sglang/releases/tag/v0.5.17) ⭐️ 8.0/10



github · Fridge003 · Aug 8, 00:19

#### Summary

SGLang v0.5.17, a major release of the open-source AI inference framework, adds day-0 serving support for the 2.8T-parameter Kimi K3 multimodal LatentMoE model and MiniMax-H3 video generation model, along with a Rust frontend and several parallelism optimizations. The release includes 582 pull requests from 194 contributors, featuring DCP and DSpark speculative decoding for Kimi K3 verified on NVIDIA GB300 and AMD MI35x hardware, and a new DWDP prefill strategy that achieves 1.92x speedup over DEP4 on 4x B200 GPUs. Additional enhancements include session-aware radix caching for agentic workloads, faster engine recovery via weight caching, and updated dependencies like FlashInfer 0.6.15.post1. This release expands SGLang&\#x27;s capability to serve cutting-edge multimodal and video generation models with advanced inference optimizations across NVIDIA and AMD hardware.

#### Background

SGLang is an open-source framework for deploying and serving large language models, known for its high-performance inference optimizations. Kimi K3 is a 2.8T-parameter multimodal model using LatentMoE architecture with a 1M-token context window. The release adds support for these advanced models with specialized parallelism strategies like DCP and DWDP to improve throughput on multi-GPU setups.

**Tags**: `#AI inference`, `#LLM serving`, `#open source`, `#model deployment`, `#multimodal models`

---

<a id="item-tech-news-2"></a>
### [DeepMind&\#x27;s WeatherNext achieves breakthrough in cyclone forecasting](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) ⭐️ 8.0/10



hackernews · bhavansig · Aug 8, 09:18 · [Discussion](https://news.ycombinator.com/item?id=49220126)

#### Summary

DeepMind has announced WeatherNext, an AI model that achieves breakthrough performance in cyclone forecasting and outperforms traditional numerical weather prediction \(NWP\) models. The model is based on hierarchical Graph Neural Networks and delivers state-of-the-art accuracy while being orders of magnitude more efficient at inference than classic NWP approaches. This builds on DeepMind&\#x27;s earlier Graphcast work and represents a significant advance for operational weather prediction, particularly for tracking and forecasting intense tropical cyclones.

#### Community Discussion

Commenters expressed enthusiasm for problem-specific AI models like WeatherNext over the current LLM-focused trend, with several calling for more impactful scientific AI work. The hierarchical Graph Neural Network architecture was highlighted as a notable and under-discussed technical contribution, with the original Graphcast paper recommended for further reading. Some comments also touched on the real-world implications of improved cyclone forecasting and shared personal experiences using weather tracking tools.

**Tags**: `#AI`, `#weather forecasting`, `#DeepMind`, `#graph neural networks`, `#scientific computing`

---

<a id="item-tech-news-3"></a>
### [macOS Screen Sharing Vulnerability Allows Unauthenticated Login](https://x.com/calif_io/status/2086022794840793454) ⭐️ 8.0/10



telegram · zaihuapd · Aug 8, 14:20

#### Summary

Security researchers have published a proof-of-concept for CVE-2026-65400, a high-severity vulnerability in macOS Screen Sharing that allows any network attacker to log in as any user without a password when the feature is enabled. Apple has patched the vulnerability in macOS 26.6.1, and researchers have reverse-engineered the patch to understand the root cause and exploitation path. A full technical analysis is expected to be published soon. Users are advised to upgrade to macOS 26.6.1 immediately.

#### Background

macOS Screen Sharing is Apple&\#x27;s built-in remote desktop protocol \(based on VNC\) that allows users to remotely control another Mac over a network. Authentication vulnerabilities in remote access services are particularly dangerous because they can grant an attacker full interactive access to a machine without any credentials. CVE-2026-65400 stems from inadequate state management during the Screen Sharing authentication handshake, allowing an unauthenticated attacker to bypass password checks entirely. A related but distinct vulnerability, CVE-2026-43760, was disclosed around the same time and involved a different attack path that did require some form of credential access.

<details><summary>References</summary>
<ul>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-65400">CVE - 2026 - 65400 : Authentication Vulnerability in macOS Products by...</a></li>
<li><a href="https://www.huntress.com/blog/macos-screen-sharing-rce-patched">From Screen Share to Root Access: Breaking Down CVE - 2026 -43760...</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-65400">NVD - CVE - 2026 - 65400</a></li>

</ul>
</details>

**Tags**: `#macOS security`, `#vulnerability`, `#screen sharing`, `#CVE`, `#Apple`

---