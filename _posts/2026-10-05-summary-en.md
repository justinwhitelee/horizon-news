---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 138 items, 1 important content pieces were selected

---

**Technology News**
1. [Strata runs 125B Qwen model on consumer RTX 4090 hardware](#item-tech-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Strata runs 125B Qwen model on consumer RTX 4090 hardware](https://github.com/Niko1221/Strata) ⭐️ 8.0/10



hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

#### Summary

A GitHub project called Strata \(Niko1221/Strata\) enables running the 125B-parameter Qwen 3.8 Flash Next model on consumer-grade NVIDIA RTX 4090 hardware, with the author reporting 124 tokens per second on an RTX 4090 paired with a Ryzen 7950X3D and 128GB DDR5. The discussion has drawn attention for demonstrating large-model inference on affordable hardware, but community testing reveals notable tradeoffs: on a 50-image vision coordinate-extraction benchmark, Strata produced a median error of 154.8 pixels compared to 46.5 pixels when running the same GGUF and vision adapter weights through llama.cpp. Quantization quality remains a concern below 4-bit, though some users report that Q4 quantization on RTX 6000 Pro workstation cards yields strong performance—up to 1,251 tokens/s prefill and 255 tokens/s decode for code tasks, with four concurrent streams at 400+ tokens/s. Skepticism about sustained hype has also been voiced as the project circulates widely on Hacker News.

#### Community Discussion

Community responses are mixed between enthusiasm for consumer-hardware accessibility and caution about accuracy and quantization quality. Jackson\_\_ reported that Strata&\#x27;s vision task accuracy significantly lagged llama.cpp on identical weights, while a11r questioned going below 4-bit quantization due to potential quality degradation. AntiRush praised the Q4 quant performance on RTX 6000 Pro, and jacquesm expressed skepticism that the breathless coverage will hold up past the initial hype cycle.

**Tags**: `#local inference`, `#quantization`, `#open source models`, `#consumer hardware`, `#performance benchmarking`

---