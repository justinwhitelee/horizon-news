---
layout: default
title: "Horizon Summary: 2026-07-31 (EN)"
date: 2026-07-31
lang: en
---

> From 196 items, 2 important content pieces were selected

---

**Technology News**
1. [Kimi K3 Engineering Breakthroughs in Long Context and MoE Routing](#item-tech-news-1) ⭐️ 8.0/10
2. [Huawei opensources 505B-parameter MoE model openPangu-2.0-Pro](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Kimi K3 Engineering Breakthroughs in Long Context and MoE Routing](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/noninertialframe96 · Jul 30, 16:37

#### Summary

Kimi K3 by Moonshot has reached the frontier as an open-weight model, ranking fourth among 580 models on Artificial Analysis behind Claude Opus 5, Fable 5, and GPT-5.6 Sol. The model introduces three significant engineering innovations documented in its 47-page technical report and released code. Kimi Delta Attention replaces the KV cache in 69 of 93 layers with a single 128x128 matrix per head, reducing memory usage for 1M-token context from 104.6 GiB to 27.2 GiB. Quantile Balancing maintains even load distribution across 896 experts per layer by computing routing bias directly from batch-level score margins, addressing limitations in DeepSeek-V3&\#x27;s fixed-step approach. AgentENV, a Firecracker microVM runtime for RL training, enabled creation of 51 million sandboxes with 133 ms checkpoint times and 49 ms resume times.

**Tags**: `#AI models`, `#machine learning systems`, `#MoE architectures`, `#long-context inference`, `#RL training infrastructure`

---

<a id="item-tech-news-2"></a>
### [Huawei opensources 505B-parameter MoE model openPangu-2.0-Pro](https://huggingface.co/openpangu/openPangu-2.0-Pro) ⭐️ 8.0/10



telegram · zaihuapd · Jul 31, 06:50

#### Summary

Huawei has open-sourced its 505B-parameter Mixture-of-Experts \(MoE\) large language model, openPangu-2.0-Pro, on Hugging Face. The model was trained on Ascend NPUs with approximately 34 trillion tokens and supports a 512k context window. It uses MLA attention, a DSA+SWA independently layered hybrid design, and a 3-head MTP self-speculation module, with post-training including fast-slow unification fine-tuning and multi-specialty reinforcement learning. The thinking variant achieves 95.4 on AIME 2026 and 87.9 on GPQA-Diamond.

**Tags**: `#AI`, `#Large Language Models`, `#Open Source`, `#Machine Learning`, `#Chinese Tech`

---