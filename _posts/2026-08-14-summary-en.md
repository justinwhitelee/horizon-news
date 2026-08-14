---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 193 items, 4 important content pieces were selected

---

**Technology News**
1. [macOS screen-sharing zero-day under active exploitation](#item-tech-news-1) ⭐️ 9.0/10
2. [Z.ai releases GLM-5.3 with autonomous security research capabilities](#item-tech-news-2) ⭐️ 8.0/10
3. [Gemini 3.7 Flash Launches with 1M Context; DeepSeek Releases Open-Source Agent Framework](#item-tech-news-3) ⭐️ 8.0/10
4. [Google ordered to remove third-party app store installation friction within a week](#item-tech-news-4) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [macOS screen-sharing zero-day under active exploitation](https://arstechnica.com/security/2026/08/vulnerability-giving-attackers-full-control-of-macs-is-under-active-exploitation/) ⭐️ 9.0/10



rss · Ars Technica · Aug 14, 18:32

#### Summary

A critical macOS zero-day vulnerability is being actively exploited in the wild, allowing remote attackers to take full control of a Mac without authentication. The flaw enables passwordless remote screen-sharing access, bypassing one of macOS&\#x27;s core security controls. The vulnerability grants complete remote compromise of affected systems, making it a high-severity issue for all Mac users. Apple has not yet released a patch as of the report date in August 2026, and the company is urged to address it urgently given the active exploitation.

#### Background

Screen Sharing is a built-in macOS feature that allows authorized users or administrators to remotely view and control a Mac over a network, commonly used for technical support and remote administration. CVE-2026-65400 represents a critical flaw in this feature that permits passwordless authentication, enabling attackers on a network to bypass the login process entirely and gain full remote access to an affected Mac. The vulnerability is particularly dangerous for shared Mac environments, CI/CD build infrastructure, and developer workstations that are regularly accessed remotely across corporate or shared networks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.servnetuk.com/news/macos-screen-sharing-vulnerability-exploit-2026">macOS Screen Sharing Vulnerability Exploited in 2026</a></li>
<li><a href="https://www.anonymoushackers.net/apple-news/macos-security-warning-critical-screen-sharing-vulnerability-fixed-in-latest-update/">macOS Security Warning: Critical Screen Sharing Vulnerability Fixed...</a></li>
<li><a href="https://macstadium.com/blog/what-you-need-to-know-about-the-macos-screen-sharing-vulnerability">What You Need to Know About the macOS Screen Sharing ...</a></li>

</ul>
</details>

**Tags**: `#macOS security`, `#zero-day vulnerability`, `#remote code execution`, `#active exploitation`, `#Apple software`

---

<a id="item-tech-news-2"></a>
### [Z.ai releases GLM-5.3 with autonomous security research capabilities](https://z.ai/blog/glm-5.3) ⭐️ 8.0/10



hackernews · pella · Aug 14, 05:19 · [Discussion](https://news.ycombinator.com/item?id=49294997)

#### Summary

Z.ai has released GLM-5.3, a frontier AI model notable for advanced coding abilities and autonomous security research capabilities, including the discovery and exploitation of vulnerabilities in open-source software such as WordPress plugins and Linux kernel components. The model is reportedly scanning open-source projects at scale, with findings disclosed through cvd.z.ai, where many critical and high-severity CVEs are currently under embargo. Community discussion on HackerNews highlights rapid adoption—with one user upgrading from an $18 to an $80 subscription plan after testing—and comparisons placing GLM-5.3 close behind models like Sol and Fable, while noting that Mythos 5 still leads on certain benchmark tasks.

#### Background

GLM-5.3 is a frontier language model developed by the Chinese startup Z.ai, built as a post-training continuation of the GLM-5.2 base model. Z.ai positions it as a leading open-source model specialized in long-horizon software engineering tasks and autonomous security research, featuring a 1-million-token context window and three configurable thinking-effort levels. The model is evaluated on Z.ai&\#x27;s internal Code Bench benchmark, on which GLM-5.3 reportedly improved by fifty percent over its predecessor. Z.ai also maintains a public vulnerability disclosure database \(cvd.z.ai\) where vulnerabilities discovered during automated scanning are tracked, many under embargo.

#### Community Discussion

HackerNews commenters report strong practical performance, with one user describing seamless execution of red-team scenarios including 0-day vulnerabilities and RCE exploitation. There is active discussion about the economic implications for developers and whether the model&\#x27;s capabilities narrow the gap enough to challenge OpenAI&\#x27;s dominance. Some users express interest in running quantized versions locally within weeks of weight release, while others note that much of the discovered vulnerability data remains under embargo.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.z.ai/guides/llm/glm-5.3">GLM - 5 . 3 - Overview - Z . AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://theunum.io/en/news/read/chinese-startup-z-ai-has-introduced-the-glm-53-language-model-for-programming">Chinese startup Z ai has introduced the GLM - 5 . 3 language model for...</a></li>
<li><a href="https://www.together.ai/models/glm-5-3">GLM - 5 . 3 API: Pricing, Benchmarks &amp; Docs | Together AI</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#automated security research`, `#LLM releases`, `#open-source vulnerability scanning`, `#software engineering tools`

---

<a id="item-tech-news-3"></a>
### [Gemini 3.7 Flash Launches with 1M Context; DeepSeek Releases Open-Source Agent Framework](https://zeli.app/zh/digest/2026-08-13) ⭐️ 8.0/10



rss · Zeli · Aug 13, 23:59

#### Summary

Google officially released Gemini 3.7 Flash, the latest high-performance native multimodal reasoning model in the Gemini 3 series, supporting up to 1 million input tokens and 65,000 output tokens across text, image, video, audio, and PDF formats. The model introduces adjustable Thinking modes \(low/medium/high\), code execution, function calling, file search, and Google Maps-based geographic grounding, though it currently lacks audio/image generation and Live API support. Meanwhile, DeepSeek AI launched DeepSeek Harness \(dsh\), an open-source agent framework built on the Cordis architecture with a &quot;everything is a plugin&quot; philosophy, now in developer preview with over 5,000 GitHub stars. The digest also covered Cerebras partnering with OpenAI to deliver GPT-5.6 Sol Ultrafast mode at 750 tokens per second, OpenAI integrating Codex into ChatGPT for multi-agent software engineering workflows, and Mistral releasing OCR 4.1 with paragraph-level bounding boxes and structural block tagging.

**Tags**: `#AI models`, `#open source`, `#agent frameworks`, `#multimodal AI`

---

<a id="item-tech-news-4"></a>
### [Google ordered to remove third-party app store installation friction within a week](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 8.0/10



telegram · zaihuapd · Aug 14, 09:55

#### Summary

U.S. District Judge James Donato has ordered Google to eliminate the multi-step installation barriers it places on third-party Android app stores within one week. The ruling, stemming from the Epic v. Google antitrust case, requires Google to remove extra warning popups and intermediate steps from the Play Store that currently make installing competing app markets deliberately cumbersome. A jury had previously found Google unlawfully monopolized Android app distribution, and the court determined that the &\#x27;view-then-install&\#x27; flow was anti-competitive friction designed to deter ordinary users. After compliance, installing a third-party app store must be as direct as installing any regular Android application.

#### Background

The Epic v. Google antitrust case centered on allegations that Google maintained an illegal monopoly over Android app distribution through the Google Play Store. In the prior phase of the trial, a jury found Google guilty of monopolizing the Android app distribution market, finding that its restrictions on sideloading and third-party app stores were anti-competitive rather than security-driven.

**Tags**: `#antitrust`, `#Android`, `#app distribution`, `#Google`, `#regulation`

---