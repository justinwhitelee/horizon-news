---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 205 items, 2 important content pieces were selected

---

**Technology News**
1. [Qwen Releases Qwen3.8-2.4T MoE Model with Open Weights](#item-tech-news-1) ⭐️ 8.0/10
2. [Adam&\#x27;s per-coordinate adaptation breaks rotation invariance in factored models](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Qwen Releases Qwen3.8-2.4T MoE Model with Open Weights](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10



hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

#### Summary

Qwen has released Qwen3.8-2.4T-A95B, a large open-weight Mixture-of-Experts language model with 2.4 trillion total parameters and 95 billion active parameters per forward pass. The model claims performance between Claude Opus 4.8 and an unspecified Fable 5 tier, with native context length of 262,144 tokens expandable to approximately 1,010,000 tokens. Only BF16 \(4.9 TB\) and FP8 variants were released at launch; a 1bit-quantized version sits at approximately 397 GB with 95B active per MoE. The license permits free internal use and serving for organizations with under $50 million in annual revenue, mirroring terms similar to competing models like Kimi k3. Community observers note that the absence of QAT-based q4 quantization and missing features like vision input and full 1M context \(available only in the commercial Qwen3.8-Max\) may limit deployability compared to rivals at launch.

#### Background

Qwen3.8-2.4T uses a Mixture-of-Experts \(MoE\) architecture, which distributes parameters across many specialized &quot;experts&quot; so that only a subset \(95 billion here\) activates per token, allowing the model to scale to 2.4 trillion total parameters while keeping inference costs manageable. The open-weight release offers BF16 and FP8 precision variants; lower-precision quantizations \(e.g., 1-bit\) further reduce memory footprint, making it feasible to run on hardware with limited RAM. The model&\#x27;s native context length is 262,144 tokens and can be extended to approximately 1 million tokens, supporting long-horizon tasks.

#### Community Discussion

Hacker News and community commentary focuses on deployment challenges, noting the model is significantly larger than competitors like Kimi k3 due to the lack of aggressive quantization options at launch. Some discuss how a 1bit-quantized variant at 397 GB could deliver Opus 4.5-level performance on consumer-accessible hardware while still achieving usable tokens per second. Others point out that the open-weight release lags behind the commercial Qwen3.8-Max in capabilities, lacking vision support and extended context, while a concurrently announced DeepSeek V4-Pro \(1.6T-A49B\) reportedly benchmarks at Fable 5 level.

**Tags**: `#open source AI`, `#large language models`, `#Mixture of Experts`, `#model quantization`, `#AI benchmarks`

---

<a id="item-tech-news-2"></a>
### [Adam&\#x27;s per-coordinate adaptation breaks rotation invariance in factored models](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

#### Summary

A researcher demonstrated experimentally that Adam&\#x27;s per-coordinate second-moment adaptation breaks the rotation invariance inherent to factored models W = UV^T, causing these models to lose gradient descent&\#x27;s implicit low-rank bias. Testing nine optimizers on underdetermined matrix sensing at matched training loss revealed two clean clusters: GD, shared-scalar Adam, Muon, and Shampoo preserved the low-rank bias, while Adam, RMSProp, Lion, signum, and Adafactor did not. A one-parameter interpolation of Adam&\#x27;s denominator from per-coordinate to a single shared scalar showed recovery improving monotonically, isolating the anisotropy as the damaging factor rather than adaptivity generally. Muon was found to be exact on truly low-rank targets but degrades as spectral tail energy increases, with a crossover near 4% tail energy where GD takes over. The paper \(arXiv:2608.05136\) notes a caveat that hyperspectral data results used a train-only learning rate schedule that handed Adam its worst rate on the grid, though the mechanism claim does not depend on that number.

#### Background

In matrix factorization W = UV^T, the product is invariant to simultaneous rotation of the factors \(U,V\) → \(UQ, VQ\) for any orthogonal Q. Gradient descent on such factorized objectives has been shown to implicitly favor low-rank solutions, a phenomenon relevant to understanding generalization in overparameterized models. First-order optimizers like Adam compute per-coordinate running averages of squared gradients, which depend on the coordinate basis and therefore break this rotational symmetry even when the loss itself is rotation-invariant.

#### Community Discussion

No community comments were available for this post.

**Tags**: `#machine learning optimization`, `#matrix factorization`, `#optimizer behavior`, `#low-rank structure`, `#experimental ML`

---