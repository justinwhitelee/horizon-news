---
layout: default
title: "Horizon Summary: 2026-11-06 (EN)"
date: 2026-11-06
lang: en
---

> From 214 items, 5 important content pieces were selected

---

**Technology News**
1. [sshole exploits in-band signaling abuse in crypt\(\) to bypass SSH auth](#item-tech-news-1) ⭐️ 8.0/10
2. [MS Paint Remote Code Execution Vulnerability](#item-tech-news-2) ⭐️ 8.0/10
3. [Google&\#x27;s TPU Challenges NVIDIA&\#x27;s Inference Dominance](#item-tech-news-3) ⭐️ 8.0/10
4. [An Inside Look at the First AI-Prescribing Technology - Drug Topics](#item-tech-news-4) ⭐️ 8.0/10
5. [Hugging Face releases MoE training handbook with Megatron-LM runbooks](#item-tech-news-5) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [sshole exploits in-band signaling abuse in crypt\(\) to bypass SSH auth](https://sshhole.com/) ⭐️ 8.0/10



hackernews · josemrb · Nov 5, 12:19 · [Discussion](https://news.ycombinator.com/item?id=50378228)

#### Summary

A critical vulnerability named sshole allows attackers to bypass OpenSSH password authentication by exploiting in-band signaling abuse in the crypt\(\) function. By crafting a password that, when passed through crypt\(\), returns the account&\#x27;s hash value—including hashes like &quot;\*&quot; or &quot;\!&quot; used to indicate locked accounts—the attacker can log in as any user. The bug stems from crypt\(\) reusing &quot;\*&quot; as both a &quot;no password&quot; marker in /etc/passwd and an error sentinel, enabling password injection through the hashing routine itself. Musl-libc had partially addressed this class of issue in its DES-based crypt implementation but missed the SHA variant path, leaving some systems vulnerable.

#### Background

OpenSSH validates passwords by calling crypt\($pw, $hash\), where $hash is the stored password hash for the target account; a match confirms the user knows the correct password. In-band signaling occurs when a function reuses a special return value for multiple purposes—in this case, &quot;\*&quot; signals both a locked account and a hashing error in crypt\(\). Musl-libc, a lightweight C library, had patched a similar flaw in crypt\_des but overlooked the corresponding vulnerability in crypt\_sha.

#### Community Discussion

Commenters agreed the root cause is the reuse of &quot;\*&quot; as a magic string for two distinct semantic meanings. BoppreH criticized the pattern broadly, suggesting error codes or Result types would prevent such collisions. amluto noted the vulnerability persists in musl&\#x27;s SHA path despite a prior workaround in the DES path. aljgz advocated for a &quot;no magic strings&quot; rule in system programming, cautioning against reusing special characters as dual-purpose sentinels.

**Tags**: `#security vulnerability`, `#OpenSSH`, `#C systems programming`, `#crypt`, `#in-band signaling`

---

<a id="item-tech-news-2"></a>
### [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 8.0/10

A CVE-level unauthenticated RCE vulnerability in MS Paint on Windows, prompting HackerNews discussion about its attack surface, affected versions, and patch availability.

hackernews · kuberwastaken · Nov 5, 20:43 · [Discussion](https://news.ycombinator.com/item?id=50384233)

**Tags**: `#cybersecurity`, `#vulnerability`, `#Windows`, `#RCE`, `#Microsoft`

---

<a id="item-tech-news-3"></a>
### [Google&\#x27;s TPU Challenges NVIDIA&\#x27;s Inference Dominance](https://newsletter.semianalysis.com/p/tpu-strikes-the-king) ⭐️ 8.0/10



rss · Semianalysis · Nov 5, 19:03

#### Summary

Google is positioning its TPU as a viable alternative to NVIDIA&\#x27;s CUDA ecosystem for large-language-model inference, marking a significant competitive shift in AI infrastructure. The move targets NVIDIA&\#x27;s entrenched moat by aligning with frameworks such as vLLM, SGLang, llm-d, and Ray, while showcasing support for models including Kimi K3, Qwen, and GLM5.3. TorchTPU and the new Muse Spark Open initiative further extend PyTorch compatibility onto Google&\#x27;s custom silicon. For organizations deploying LLMs at scale, this introduces a potential alternative to CUDA-only deployment paths and could reshape the economics of inference. NVIDIA, led by Jensen Huang, is reportedly responding with intensified development efforts.

#### Background

TPUs \(Tensor Processing Units\) are Google&\#x27;s custom ASICs designed specifically for machine-learning workloads, historically used primarily for training and Google-internal inference. CUDA is NVIDIA&\#x27;s proprietary parallel-computing platform and programming model that has become the de facto standard for AI training and inference, creating a deep software ecosystem lock-in. Inference—the process of running deployed models to produce outputs—has become a major cost center as LLM usage scales, making it a strategically important frontier beyond training hardware.

**Tags**: `#AI Infrastructure`, `#GPU/TPU Competition`, `#LLM Deployment`, `#CUDA Ecosystem`, `#Inference Market`

---

<a id="item-tech-news-4"></a>
### [An Inside Look at the First AI-Prescribing Technology - Drug Topics](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMGdSVzFjbExhUXF2cEluaEdTZEpEX3MxWVdtRU5nZno4RDhHcGwzdzhBV3lONmJFclc4ZkloRVZSVFhDSU5RMGpma0NSS20zR0pKOXRJMDdZLWE0ckNDSDR1bzhyYVg0WlpBNms5MDZUd2J4cUpOZnc0bGVZRmxyTUFaM2lxcUROQUVkZ2F3?oc=5) ⭐️ 8.0/10

Analysis of pioneering AI technology capable of prescribing medications, marking a significant advancement in healthcare-AI intersection with potential industry-changing impact.

rss · Google News \(Tech\) · Nov 5, 19:30

**Tags**: `#artificial intelligence`, `#healthcare technology`, `#pharmaceuticals`, `#medical innovation`, `#AI regulation`

---

<a id="item-tech-news-5"></a>
### [Hugging Face releases MoE training handbook with Megatron-LM runbooks](https://www.reddit.com/r/MachineLearning/comments/1xorgq0/the_ultimate_moe_training_handbook_training/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/Norlax\_42 · Nov 5, 19:13

#### Summary

Nouamane, a researcher at Hugging Face, has published a comprehensive Mixture-of-Experts training handbook covering Megatron-LM configuration, MoE architecture internals, and serving/RL guidance. The guide is based on approximately 800,000 GH200 GPU-hours of MoE training experience on the Alps cluster at CSCS. Chapter 2 provides a step-by-step Megatron-LM runbook—from hardware testing through dense baselines to first MoE training on a single node—while Chapter 3 dissects the MoE layer, including router design, routing mechanics, load balancing, expert placement, block layout, and systems considerations, with code snippets and recommendations alongside frontier model choices. Chapter 4 addresses post-training deployment into serving and reinforcement learning. The accompanying resources include a 55-figure gallery, training scripts, and a consolidated block of all recommended Megatron-LM flags, all available on Hugging Face Spaces and GitHub Gist.

#### Background

Mixture-of-Experts \(MoE\) models are a type of large language model architecture where the feed-forward layers are split into multiple independent sub-networks called &quot;experts.&quot; During training and inference, a router dynamically selects a subset of these experts for each token, allowing the model to scale capacity significantly without proportionally increasing computation per token. Megatron-LM is a widely used PyTorch-based library for training large-scale transformer models, developed originally by NVIDIA, that provides distributed training strategies across GPU clusters. The complexity of MoE training stems from challenges like routing imbalance, expert placement across devices, and efficient communication patterns, which is why practical guidance grounded in large-scale experience is particularly valuable.

**Tags**: `#Mixture-of-Experts`, `#Megatron-LM`, `#LLM training`, `#AI systems`, `#technical guide`

---