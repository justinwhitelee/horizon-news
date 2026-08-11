---
layout: default
title: "Horizon Summary: 2026-08-11 (EN)"
date: 2026-08-11
lang: en
---

> From 198 items, 1 important content pieces were selected

---

**Technology News**
1. [Replay-Based Attack Extracts Encrypted LLM Reasoning Traces](#item-tech-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Replay-Based Attack Extracts Encrypted LLM Reasoning Traces](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 8.0/10

Researchers demonstrated a novel attack where encrypted chain-of-thought blocks from frontier LLMs could be replayed into weaker models to extract hidden reasoning in plaintext, exposing a shared encryption key vulnerability across major AI providers.

rss · Simon Willison · Aug 11, 22:40

#### Summary

A paper hosted at stolen-thoughts.com \(arxiv 2608.09867\) describes a replay-based attack against proprietary LLM APIs from Anthropic, OpenAI, and Google. These providers return encrypted chain-of-thought blocks to clients, which the researchers found could be replayed across sessions, users, and models within the same family because all models shared the same encryption key. By feeding the encrypted reasoning trace into a weaker model and jailbreaking it with a simple prompt requesting verbatim transcription, attackers could recover the stronger model&\#x27;s hidden reasoning in plaintext. Claude Haiku 4.5 was identified as the easiest target. The vulnerability has since been patched, with all providers acknowledging the report and confirming they could no longer be exploited. A secondary finding revealed that models treat their own reasoning traces as sacrosanct, making them susceptible to prompt injection variants that embed data-exfiltration instructions within the thinking trace itself.

#### Background

Modern frontier LLMs often produce a hidden chain-of-thought or reasoning trace alongside their visible output, intended for internal use rather than human consumption. These reasoning blocks are typically returned encrypted by API providers to prevent extraction of potentially sensitive intermediate reasoning. The vulnerability stems from a shared encryption key across model variants within a single family, allowing encrypted content from a powerful model to be decrypted by replaying it through a weaker sibling that outputs plaintext.

#### Community Discussion

No community comments were available for this item at time of publication.

**Tags**: `#LLM security`, `#adversarial attacks`, `#proprietary AI`, `#chain-of-thought`, `#privacy`

---