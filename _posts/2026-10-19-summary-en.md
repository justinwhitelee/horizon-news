---
layout: default
title: "Horizon Summary: 2026-10-19 (EN)"
date: 2026-10-19
lang: en
---

> From 147 items, 2 important content pieces were selected

---

**Technology News**
1. [vLLM v0.32.0 introduces low-precision KV caches and structured output support](#item-tech-news-1) ⭐️ 8.0/10
2. [TempoPFN: Synthetic pre-training of linear RNNs for zero-shot time series forecasting](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.32.0 introduces low-precision KV caches and structured output support](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 8.0/10



github · khluu · Oct 18, 06:50

#### Summary

vLLM v0.32.0 is a major release from the open-source LLM serving framework featuring 814 commits from 363 contributors. The release extends low-precision KV cache support across GPU architectures, adding NVFP4 for SM8x, SM90, and SM12x, plus GLM-5.x FP8 KV cache defaults on SM100 that halve KV memory per rank with 2.3–5.5% throughput gains at 7–11% TTFT cost. A new POST /v1/systemone endpoint serves structured decision responses for choice, noul, and score questions, while a generic HF parser reads model checkpoint response templates to eliminate per-model parser configuration. Model Runner V2 becomes the default on ROCm, and startup performance improves via precompiled FlashInfer kernels, shared-memory tensor broadcasting, and least-loaded API worker distribution delivering 43–85% more requests per second on short sequences. The release drops Python 3.10 support, pins transformers to &gt;=5.16.1,&lt;5.20.0, restricts default CORS origins, and adds security fixes for resource exhaustion and token limit vulnerabilities.

#### Background

vLLM is a widely adopted open-source framework for serving large language models, known for PagedAttention and high-throughput inference. Low-precision KV caching stores key-value attention tensors in reduced bit-width formats like FP8 or NVFP4 to cut GPU memory consumption during long-context generation. Model Runner V2 is vLLM&\#x27;s next-generation execution backend that consolidates distributed parallelism strategies including tensor parallelism, pipeline parallelism, and speculative decoding into a unified runtime.

#### Community Discussion

No community comments were available for this release at the time of writing.

**Tags**: `#LLM serving`, `#vLLM`, `#low-precision compute`, `#structured output`, `#GPU optimization`

---

<a id="item-tech-news-2"></a>
### [TempoPFN: Synthetic pre-training of linear RNNs for zero-shot time series forecasting](https://www.reddit.com/r/MachineLearning/comments/1x97v19/tempopfn_synthetic_pretraining_of_linear_rnns_for/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/Yossarian\_1234 · Oct 18, 16:43

#### Summary

A paper accepted at NeurIPS 2026 introduces TempoPFN, a framework that enables zero-shot time series forecasting through synthetic pre-training of DeltaProduct-based linear recurrent neural networks. The authors—Vladyslav Moroshan, Julien Siems, Arber Zela, Timur Carstensen, and Frank Hutter—release a library of synthetic time series generators and augmentations designed to train time series foundation models. The synthetic data produced by this framework has already been applied in Toto-2 and TS-ICL. Open-source code and pre-trained models are available on GitHub \(github.com/automl/TempoPFN\) and Hugging Face \(Huggingface.co/AutoML-org/TempoPFN\), with the arXiv preprint at arxiv.org/abs/2510.25502.

**Tags**: `#machine learning`, `#time series`, `#foundation models`, `#neural networks`, `#open source`

---