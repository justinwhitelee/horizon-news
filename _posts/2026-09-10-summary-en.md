---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 209 items, 4 important content pieces were selected

---

**Technology News**
1. [vLLM v0.29.0: Model Runner V2 defaults, new model support, and performance gains](#item-tech-news-1) ⭐️ 8.0/10
2. [Apple unveils iPhone Duo foldable phone](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI’s sly mathematical breakthrough sends a chill through academia](#item-tech-news-3) ⭐️ 8.0/10
4. [Verge Staff Reacts to Apple’s First Foldable iPhone Duo](#item-tech-news-4) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.29.0: Model Runner V2 defaults, new model support, and performance gains](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10



github · khluu · Sep 9, 08:54

#### Summary

vLLM v0.29.0 introduces Model Runner V2 as the default for all models, completing the rollout that started with pooling models. The release adds support for several large-scale models including Tencent&\#x27;s 770B/49B-active MoE, Qwen3.8-Flash-Next with NVFP4, and Kimi K3 NVFP4 checkpoints. Key performance improvements include batch-sharded sampling reducing per-step logits memory by 1/TP, fused MXFP4 top-k finalization delivering ~5% E2E latency improvement for Kimi K3, and a 6.6-7.6x kernel speedup for K3 Mamba metadata preparation. Speculative decoding gained per-request acceptance stats in OpenAI API responses and adaptive verification extended to logprobs. Breaking changes include ten deprecated model architectures removed, PyAV video decoder backend removed, and \`python -m vllm.entrypoints.openai.api\_server\` deprecated in favor of \`vllm serve\`.

#### Background

vLLM is an open-source library for large language model inference serving, widely used in production AI infrastructure. Model Runner V2 is an architectural redesign of vLLM&\#x27;s execution engine that improves memory management and dispatch efficiency. Speculative decoding is a technique where a smaller draft model generates candidate tokens that a larger target model verifies in parallel, reducing latency.

**Tags**: `#open source`, `#machine learning`, `#AI infrastructure`, `#LLM serving`, `#model optimization`

---

<a id="item-tech-news-2"></a>
### [Apple unveils iPhone Duo foldable phone](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

Apple has announced the iPhone Duo, a dual-screen foldable smartphone representing its first major redesign of the iPhone lineup since 2017, and the company&\#x27;s debut entry into the foldable mobile market.

hackernews · thecosmicfrog · Sep 9, 18:15 · [Discussion](https://news.ycombinator.com/item?id=49630931)

#### Summary

Apple introduced the iPhone Duo, a dual-screen foldable device that marks the most noticeable overhaul of its flagship product since 2017 and signals the company&\#x27;s official entry into the foldable phone segment. The announcement was made under first-time CEO John Ternus, who appears to be shifting Apple&\#x27;s keynote presentation style away from the traditional Tim Cook format. Hands-on demonstrations suggest the fold features no visible crease, addressing a common consumer concern about durability and screen quality. Apple&\#x27;s involvement is expected to accelerate developer adoption of fold-optimized app designs, potentially improving the fragmented foldable ecosystem currently dominated by Android manufacturers such as Huawei, Samsung, and Google. Initial community reaction emphasizes cautious optimism, with many observers preferring to evaluate the device&\#x27;s long-term reliability and software maturity over the next few generations before considering a switch.

#### Background

Foldable smartphones use hinged displays that fold inward or outward to toggle between compact and tablet-like form factors, but they face challenges including screen creasing, mechanical durability, and inconsistent app adaptation to variable screen shapes. Apple has historically entered new hardware categories only after mature component supply chains and user-experience standards are established, making this its first confirmed move into the foldable phone market.

#### Community Discussion

Commenters praise the Duo&\#x27;s crease-less display and note a stylistic shift in Apple&\#x27;s keynote presentation under John Ternus. Several users prefer to wait until a second or third generation to assess long-term reliability, while Android foldable owners hope Apple&\#x27;s participation will push developers to build properly optimized fold-aware applications rather than simply stretching existing layouts. Some commenters also express interest in tri-fold formats to maximize screen area despite current fragility concerns.

**Tags**: `#hardware`, `#mobile`, `#foldable devices`, `#Apple`, `#product announcement`

---

<a id="item-tech-news-3"></a>
### [OpenAI’s sly mathematical breakthrough sends a chill through academia](https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes) ⭐️ 8.0/10

OpenAI reportedly solved a Millennium Prize problem in mathematics, though the announcement has been complicated by unresolved issues.

rss · The Verge · Sep 9, 21:16

**Tags**: `#artificial intelligence`, `#mathematics`, `#OpenAI`, `#research`, `#technology industry`

---

<a id="item-tech-news-4"></a>
### [Verge Staff Reacts to Apple’s First Foldable iPhone Duo](https://www.theverge.com/tech/992830/apple-iphone-duo-foldable-verge-staffers-react) ⭐️ 8.0/10



rss · The Verge · Sep 9, 19:45

#### Summary

Apple has announced its first foldable smartphone, the iPhone Duo, featuring a dual-screen design with a 5.4-inch outer display and a 7.6-inch inner foldable screen. The device includes two rear cameras, Touch ID authentication, and an IP68 water and dust resistance rating. iOS has been adapted with software tricks to make the operating system feel more at home on the larger, foldable form factor. Preorders for the new device are set to begin soon.

#### Background

Foldable smartphones have existed since Samsung launched its Galaxy Fold in 2019, establishing an inward-folding clamshell design that several Android manufacturers have since adopted. Apple has historically resisted entering the foldable-phone market despite years of supply-chain rumors, instead focusing on iterative improvements to its traditional slab-form iPhones. The iPhone Duo represents Apple&\#x27;s first entry into this category, arriving at a time when the foldable segment remains a small but growing niche within global smartphone sales.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/tech/992830/apple-iphone-duo-foldable-verge-staffers-react">Verge staffers react to the iPhone Duo: What we love and don ...</a></li>
<li><a href="https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/">Apple unveils iPhone Duo</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#mobile`, `#consumer tech`, `#product launch`

---