---
layout: default
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06
lang: zh
---

> 从 214 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [sshole: In-band signaling exploit bypasses OpenSSH password auth via crypt\(\)](#item-tech-news-1) ⭐️ 8.0/10
2. [MS Paint Remote Code Execution Vulnerability](#item-tech-news-2) ⭐️ 8.0/10
3. [Google TPU 进军推理市场，挑战 NVIDIA CUDA 霸权](#item-tech-news-3) ⭐️ 8.0/10
4. [An Inside Look at the First AI-Prescribing Technology - Drug Topics](#item-tech-news-4) ⭐️ 8.0/10
5. [Hugging Face 发布 MoE 训练完整手册，基于 80 万 GPU 小时经验](#item-tech-news-5) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [sshole: In-band signaling exploit bypasses OpenSSH password auth via crypt\(\)](https://sshhole.com/) ⭐️ 8.0/10



hackernews · josemrb · 11月5日 12:19 · [社区讨论](https://news.ycombinator.com/item?id=50378228)

#### Summary

A critical SSH vulnerability dubbed sshole allows attackers to log in as any user by exploiting in-band signaling abuse in the crypt\(\) function. When OpenSSH&\#x27;s sshd validates a password, it calls crypt\($pw, $hash\) and compares the result to $hash; the bug shows that an attacker can craft inputs so the comparison always succeeds, even for accounts with locked or no-password status \(indicated by hash values like &quot;\*&quot; or &quot;\!&quot;\). The musl-libc project had partially mitigated this class of issue in its DES-based crypt implementation, but a nearly identical vulnerable code path remained unfixed in its SHA-based crypt implementation. The vulnerability is categorized as a new in-band signaling abuse, continuing a pattern where special sentinel strings are misused as both error indicators and legitimate data within the same channel.

#### Background

In-band signaling is a vulnerability pattern where a single data channel carries both regular information and control signals, allowing an attacker to inject commands or bypass checks by manipulating what should be ordinary data. The crypt\(\) function is a legacy C password-hashing routine historically used by Unix systems and OpenSSH; it accepts a plaintext password and a salt/hash string and returns a hashed result. Sentinel values like &quot;\*&quot; or &quot;\!&quot; are used in /etc/passwd to indicate locked accounts, and the reuse of such strings across different layers of the authentication pipeline created the exploitable ambiguity.

#### Community Discussion

Community commenters identified the root cause as an in-band signaling abuse and noted that musl&\#x27;s existing workaround in crypt\_des was incomplete because it was not replicated in crypt\_sha. Commenters advocated for a general rule against magic sentinel strings, arguing that returning explicit failure values \(exceptions or Result&lt;T&gt;-style types\) would be safer than reusing strings like &quot;\*&quot; for multiple meanings. Some also noted that the problem is harder to eliminate in low-level C systems programming than in higher-level application code.

**标签**: `#security vulnerability`, `#OpenSSH`, `#C systems programming`, `#crypt`, `#in-band signaling`

---

<a id="item-tech-news-2"></a>
### [MS Paint Remote Code Execution Vulnerability](https://www.cve.org/CVERecord?id=CVE-2026-83844) ⭐️ 8.0/10

A CVE-level unauthenticated RCE vulnerability in MS Paint on Windows, prompting HackerNews discussion about its attack surface, affected versions, and patch availability.

hackernews · kuberwastaken · 11月5日 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50384233)

**标签**: `#cybersecurity`, `#vulnerability`, `#Windows`, `#RCE`, `#Microsoft`

---

<a id="item-tech-news-3"></a>
### [Google TPU 进军推理市场，挑战 NVIDIA CUDA 霸权](https://newsletter.semianalysis.com/p/tpu-strikes-the-king) ⭐️ 8.0/10



rss · Semianalysis · 11月5日 19:03

#### 摘要

Google TPU 正式进军 AI 推理市场，对 NVIDIA CUDA 的生态护城河发起有力挑战。文章指出 NVIDIA 因此感到压力，Jensen Huang 已做出回应性反击。Google 的新推理生态得到了 Kimi K3、Qwen、GLM5.3 等主流大模型的支持，并整合了 vLLM、SGLang、Ray、llm-d 等推理框架以及 TorchTPU 和 Muse Spark Open 等项目。这一竞争格局的转变有望重塑大语言模型部署的经济模型，标志着 AI 基础设施领域的重要转折。

**标签**: `#AI Infrastructure`, `#GPU/TPU Competition`, `#LLM Deployment`, `#CUDA Ecosystem`, `#Inference Market`

---

<a id="item-tech-news-4"></a>
### [An Inside Look at the First AI-Prescribing Technology - Drug Topics](https://news.google.com/rss/articles/CBMijgFBVV95cUxPMGdSVzFjbExhUXF2cEluaEdTZEpEX3MxWVdtRU5nZno4RDhHcGwzdzhBV3lONmJFclc4ZkloRVZSVFhDSU5RMGpma0NSS20zR0pKOXRJMDdZLWE0ckNDSDR1bzhyYVg0WlpBNms5MDZUd2J4cUpOZnc0bGVZRmxyTUFaM2lxcUROQUVkZ2F3?oc=5) ⭐️ 8.0/10

Analysis of pioneering AI technology capable of prescribing medications, marking a significant advancement in healthcare-AI intersection with potential industry-changing impact.

rss · Google News \(Tech\) · 11月5日 19:30

**标签**: `#artificial intelligence`, `#healthcare technology`, `#pharmaceuticals`, `#medical innovation`, `#AI regulation`

---

<a id="item-tech-news-5"></a>
### [Hugging Face 发布 MoE 训练完整手册，基于 80 万 GPU 小时经验](https://www.reddit.com/r/MachineLearning/comments/1xorgq0/the_ultimate_moe_training_handbook_training/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/Norlax\_42 · 11月5日 19:13

#### 摘要

Hugging Face 研究者 Nouamane 发布了一份详尽的 Mixture-of-Experts（MoE）训练手册，开源在 Hugging Face Spaces。该手册基于作者在瑞士 CSCS Alps 超算集群上使用约 80 万 GH200 GPU 小时的 MoE 训练实践经验撰写，面向已有稠密模型训练经验、计划转向 MoE 的工程师与研究者。手册第三章深度拆解 MoE 架构的每个组件（路由、负载均衡、专家布局、训练细节），并附带 Megatron-LM 代码、注意事项与推荐配置，同时对比了前沿 MoE 模型的选择；第四章延伸至推理部署与强化学习（RL）场景。配套资源包括 55 张插图画廊、可复现脚本以及所有推荐标志参数的聚合代码块。

#### 背景知识

MoE（Mixture-of-Experts，混合专家）是一种大语言模型架构，核心思想是将模型参数分散到多个

**标签**: `#Mixture-of-Experts`, `#Megatron-LM`, `#LLM training`, `#AI systems`, `#technical guide`

---