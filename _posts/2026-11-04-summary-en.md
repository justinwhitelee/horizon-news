---
layout: default
title: "Horizon Summary: 2026-11-04 (EN)"
date: 2026-11-04
lang: en
---

> From 196 items, 3 important content pieces were selected

---

**Technology News**
1. [BlackX UEFI Bootkit Bypasses Secure Boot on Fully Patched Windows](#item-tech-news-1) ⭐️ 9.0/10
2. [Qwen 3.8 27B demonstrates weight-space programming locally](#item-tech-news-2) ⭐️ 8.0/10
3. [HN Digest 2026-11-03 · Postman 静默安装 AI 插件并共享 API 数据](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [BlackX UEFI Bootkit Bypasses Secure Boot on Fully Patched Windows](https://arstechnica.com/security/2026/11/uefi-bootkit-infected-fully-patched-windows-machines-is-microsoft-to-blame/) ⭐️ 9.0/10



rss · Ars Technica · Nov 3, 16:03

#### Summary

The BlackX UEFI bootkit has been reported to infect fully patched Windows machines by exploiting ambiguities in Microsoft&\#x27;s Secure Boot protections. Published by Ars Technica on November 2026, the report questions whether Microsoft bears responsibility for the vulnerability given the gap between Secure Boot&\#x27;s intended guarantees and its actual enforcement. The bootkit operates at the firmware level, allowing it to persist even on systems with all current security updates installed. This represents a significant escalation in bootkit attacks, as Secure Boot was designed specifically to prevent such firmware-level compromises.

**Tags**: `#UEFI security`, `#Secure Boot`, `#firmware exploitation`, `#Windows security`, `#bootkit`

---

<a id="item-tech-news-2"></a>
### [Qwen 3.8 27B demonstrates weight-space programming locally](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10



rss · Simon Willison · Nov 3, 16:29 · [Discussion](https://news.ycombinator.com/item?id=50355251)

#### Summary

Simon Willison demonstrated that Qwen 3.8 27B, running locally on his laptop via LM Studio, can perform &quot;weight-space programming&quot;—interpreting raw floating-point model weights to identify what a neural network was trained to do. The test, adapted from a recent paper by Takehi, Teoh, Zhang, and Khattab, presented the model with weights from a reinforcement-learned game-playing network and asked it to name the game without any tools or code execution. After 46 minutes and 43,506 reasoning tokens, Qwen 3.8 27B correctly identified the Pac-Man variant with 72% confidence, matching a capability previously only shown on frontier models like GPT-6 Astra. The model also successfully identified Pong in a second attempt. The paper has drawn criticism from researchers including Matthew Honnibal and Sean Goedecke, who argue it conflates weight interpretation with tool-assisted weight modification and that the Qwen 3.5 weight-editing example follows steps a human ML researcher would take.

#### Background

Weight-space programming refers to an LLM&\#x27;s ability to analyze and modify the raw floating-point weights of a neural network without external tools or training loops. The concept builds on prior work in mechanistic interpretability and techniques like steering vectors, LoRAs, and J-spaces, which have long been used to influence model behavior through targeted weight modifications. The original paper trained four small networks to play simplified versions of Breakout, Pong, Pac-Man, and Freeway, then tested whether LLMs could deduce the game from weights alone.

#### Community Discussion

Hacker News commenters raised skepticism about whether models are genuinely understanding weights or merely pattern-matching, with one comparing it to Shakespeare&\#x27;s line about calling spirits from the deep. Others noted the distinction between trained-in capability and actual weight-space comprehension remains open. One commenter observed that same-generation models may not have been trained on sources dissecting their own architecture, raising questions about how much of this reflects true understanding versus statistical inference.

**Tags**: `#AI research`, `#model interpretability`, `#weight manipulation`, `#open source models`, `#LLM capabilities`

---

<a id="item-tech-news-3"></a>
### [HN Digest 2026-11-03 · Postman 静默安装 AI 插件并共享 API 数据](https://zeli.app/zh/digest/2026-11-03) ⭐️ 8.0/10

HN digest covering Postman&\#x27;s controversial silent AI plugin installation raising trust and security concerns, and a technical debunking of exaggerated claims about weight-only AI model modification.

rss · Zeli · Nov 3, 23:59

**Tags**: `#AI tools`, `#developer tools`, `#ML methodology`, `#security`, `#API engineering`

---