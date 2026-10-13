---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 92 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Python 3.15 发布：支持显式懒导入与采样性能分析器](#item-tech-news-1) ⭐️ 8.0/10
2. [U-Space: Label-free Uncertainty Quantification for Reasoning LLMs via Hidden State Analysis](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Python 3.15 发布：支持显式懒导入与采样性能分析器](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 正式发布，引入多项新特性，同时发布负责人 Hugo van Kemenade 也负责了 3.14 版本的发布工作。

rss · Simon Willison · 10月12日 18:15

#### 主要变更

Python 3.15 已正式发布，由 Hugo van Kemenade 担任发布负责人。核心亮点包括 PEP 810 的显式懒导入功能，允许开发者使用 \`lazy import\` 和 \`lazy from\` 语法延迟模块加载，有效减少工具启动时间。PEP 798 引入了列表推导式中的解包语法，支持 \`\[ \*L for L in lists \]\` 等更简洁的展开写法。标准库新增 Tachyon 采样性能分析器（\`profiling.sampling\`），可通过低开销方式捕获堆栈跟踪并生成火焰图。性能方面整体与 3.14 持平，但实验性 JIT 在斐波那契测试中带来 1.2 倍加速，这是首次观察到有意义的 JIT 性能提升。

#### 背景说明

Python 3.10 已于 2026 年 10 月结束官方支持，因此开源项目维护者需要转向 3.11+ 版本以获得新特性和安全更新。采样性能分析器（如 py-spy）此前需借助第三方工具实现，Python 3.15 将其纳入标准库，降低了性能调优门槛。PEP 448 早在 2015 年 Python 3.5 中已引入展开语法，PEP 798 在此基础上扩展到了推导式场景。

**标签**: `#Python`, `#language release`, `#open source`, `#PEP 810`, `#lazy imports`

---

<a id="item-tech-news-2"></a>
### [U-Space: Label-free Uncertainty Quantification for Reasoning LLMs via Hidden State Analysis](https://www.reddit.com/r/MachineLearning/comments/1x44f9m/uspace_uncovering_when_and_why_uncertainty_arises/) ⭐️ 8.0/10

Researchers have introduced U-Lens, a single-pass, label-free method for quantifying and categorizing uncertainty in open-weight reasoning language models. The approach combines Jacobian lens directions with token entropy to produce interpretable uncertainty signals without requiring sampling, training, or correctness labels.

reddit · r/MachineLearning · /u/AdRevolutionary3242 · 10月12日 15:10

#### Summary

U-Lens estimates uncertainty by multiplying hidden-state projection onto &quot;doubt&quot; directions \(derived from the J-Lens framework\) by mean token entropy over reasoning tokens. It categorizes uncertainty into four types—ambiguity, missing information, conflicting evidence, or general uncertainty—without requiring correctness labels, fine-tuning, or multiple forward passes. In evaluations across Gemma 4, Qwen3.5, and Magistral models, it outperformed 5-pass, 10-pass, and supervised baselines. The only model-specific component is a pre-fitted J-Lens \(available on Hugging Face for models like Gemma 2/3/4, Qwen3/3.5/3.6, Llama 3.1/3.3, and OLMo 3\), which can be fitted with ~100 unlabeled prompts if needed.

#### Background

Uncertainty quantification in LLMs typically requires expensive techniques: test-time sampling \(5x+ forward passes\), external judge models, or labeled datasets for calibration. The J-Lens framework from Anthropic&\#x27;s global workspace paper provides a way to identify uncertainty directions in the embedding space via Jacobian analysis. U-Lens builds on this by combining directional signals with entropy already computed during generation, producing a cost-efficient uncertainty estimate at inference time.

#### Community Discussion

No community comments were available for this submission. The authors invite integration feedback and discussion around routing low-confidence answers to bigger models or humans, triggering retrieval when missing information is detected, asking clarifying questions for ambiguous inputs, and flagging conflicting evidence in RAG pipelines.

**标签**: `#artificial intelligence`, `#machine learning`, `#language models`, `#research`, `#uncertainty estimation`

---