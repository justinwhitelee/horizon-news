---
layout: default
title: "Horizon Summary: 2026-10-16 (EN)"
date: 2026-10-16
lang: en
---

> From 202 items, 1 important content pieces were selected

---

**Technology News**
1. [Meta releases Muse Spark Open, largest US open-weight model optimized for Mac Studio](#item-tech-news-1) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Meta releases Muse Spark Open, largest US open-weight model optimized for Mac Studio](https://huggingface.co/blog/meta-muse-spark-open) ⭐️ 8.0/10



telegram · zaihuapd · Oct 16, 00:47

#### Summary

Meta has released Muse Spark Open, an 816B total-parameter \(42B activated\) open-weight multimodal model with a 1-million-token context window, optimized for Apple Silicon via the MLX framework. It is designed primarily for coding and agent tasks, and can run locally on two M5 Ultra Mac Studio machines using their unified memory architecture as a terabyte-scale system. Meta claims it outperforms Qwen 3.8, GLM 5.3, and Kimi K3 on benchmarks like JobBench, though it still trails paid proprietary models. Weights are available on Hugging Face and support NVIDIA, AMD, Intel, and Apple hardware acceleration.

#### Background

Apple&\#x27;s MLX framework is a machine-learning toolkit built for Apple Silicon, leveraging its unified memory architecture to run large models on consumer hardware. MoE \(mixture-of-experts\) models like Muse Spark Open activate only a subset of parameters per token, enabling large total parameter counts while keeping inference efficient—here, 42B of 816B parameters are active per forward pass.

**Tags**: `#开源大模型`, `#Meta`, `#Apple Silicon`, `#MLX`, `#多模态AI`

---