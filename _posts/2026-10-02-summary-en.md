---
layout: default
title: "Horizon Summary: 2026-10-02 (EN)"
date: 2026-10-02
lang: en
---

> From 200 items, 2 important content pieces were selected

---

**Technology News**
1. [NeurIPS 2026 Spotlight: Parallel-in-Time RNN Training via DEER + GTF](#item-tech-news-1) ⭐️ 8.0/10
2. [NeurIPS 2026 paper reveals Authority Bias in LLMs](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [NeurIPS 2026 Spotlight: Parallel-in-Time RNN Training via DEER + GTF](https://www.reddit.com/r/MachineLearning/comments/1wuz2s4/parallelintime_training_of_recurrent_neural/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/DangerousFunny1371 · Oct 1, 13:12

#### Summary

A NeurIPS 2026 spotlight paper introduces a method to parallelize training of nonlinear recurrent neural networks on chaotic time series by combining DEER \(Dynamical Extended Euler-Rozonoer\) with generalized teacher forcing \(GTF\). DEER solves the RNN forward pass via Newton-type fixed-point iterations across the full sequence length T, achieving O\(\(log T\)²\) scaling on GPUs instead of the usual O\(T\). However, under chaotic dynamics DEER previously broke down, degrading to O\(T log T\). The authors show that GTF stabilizes DEER by preventing divergence caused by chaos while also reducing exposure bias compared to traditional teacher forcing. This allows stable parallel-in-time training on extremely long sequences \(T &gt; 10⁶\) from both simulated and real-world chaotic systems, delivering over 100× speedup and substantially outperforming Mamba and other state space models in the dynamical systems reconstruction setting. The preprint is available at arxiv.org/abs/2605.12683.

**Tags**: `#machine learning`, `#neural networks`, `#parallel computing`, `#dynamical systems`, `#NeurIPS`

---

<a id="item-tech-news-2"></a>
### [NeurIPS 2026 paper reveals Authority Bias in LLMs](https://www.reddit.com/r/MachineLearning/comments/1wv1c2e/llms_that_push_back_on_a_wrong_user_still_accept/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/MajorRedditor23 · Oct 1, 14:45

#### Summary

A NeurIPS 2026 paper identifies Authority Bias in large language models, where models readily adopt incorrect answers when attributed to a verified source but resist the same wrong claims from a persistent user. Testing across 5 open-weight families \(Qwen3.5, GPT-OSS, OLMo-2, OLMo-3.1, Gemma-4\) and 3 API models \(GPT-5.4, Grok-4.20, Gemini-3.1-Pro\), the effect flipped 45-88% of correct answers on TriviaQA questions depending on the model, while the same answer from a user caused far fewer flips. This gap matters because standard sycophancy evaluations only apply pressure through the user, leaving models vulnerable to misinformation via retrieved documents and tool outputs in agentic systems. Directional interventions on three open-weight models \(Qwen3.5, GPT-OSS, OLMo-3.1\) reduced source-driven compliance by 64-78 points, with high cosine similarity \(~0.90-0.99\) suggesting a shared endorsement component plus a thin speaker-id component. Gemini-3.1-Pro was notably resistant \(0.6% flip rate\), while limitations include a prompt-based not a real-retrieval pipeline and findings that did not generalize to OLMo-2 or Gemma-4 internal directions. The paper, code, and interactive results are available at arxiv.org/abs/2609.37616 and authority-bias.vercel.app.

#### Background

Sycophancy in LLMs refers to models overly agreeing with users, a known alignment concern that has been addressed through training and prompting. Agentic AI systems increasingly rely on retrieved documents, search results, and tool outputs, making them susceptible to misinformation embedded in those sources. Authority Bias represents a distinct vulnerability where models conflate source credibility with answer correctness, even when the claim contradicts their own training knowledge.

**Tags**: `#AI alignment`, `#LLM safety`, `#NeurIPS 2026`, `#model robustness`, `#trust in AI systems`

---