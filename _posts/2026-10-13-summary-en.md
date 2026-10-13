---
layout: default
title: "Horizon Summary: 2026-10-13 (EN)"
date: 2026-10-13
lang: en
---

> From 92 items, 2 important content pieces were selected

---

**Technology News**
1. [Python 3.15 released with lazy imports and a sampling profiler](#item-tech-news-1) ⭐️ 8.0/10
2. [U-Space: Label-free Uncertainty Estimation for Reasoning LLMs](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Python 3.15 released with lazy imports and a sampling profiler](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10



rss · Simon Willison · Oct 12, 18:15

#### Summary

Python 3.15 has been released, with release manager Hugo van Kemenade curating the What&\#x27;s New guide. The standout feature is PEP 810, which introduces explicit lazy imports via the \`lazy\` keyword, deferring module loading until a symbol is first used—a practical solution for reducing startup time in CLI tools with heavy optional dependencies. PEP 798 adds unpacking syntax inside comprehensions, allowing expressions like \`\[\*L for L in lists\]\` to flatten nested iterables. Python&\#x27;s existing tracing profiler has been renamed to \`profiling.tracing\`, and a new low-overhead sampling profiler called Tachyon \(\`profiling.sampling\`\) ships in the standard library, capable of attaching to live processes and producing flame graphs and Firefox Profiler–compatible output. Performance is largely on par with 3.14, though the experimental JIT delivered a 1.2× speedup on a Fibonacci benchmark.

#### Background

Python releases a new version every year, and each typically drops support for the version released two years prior—here, Python 3.10 has reached end of life. Lazy imports and sampling profilers are established techniques in other languages; PEP 810 and Tachyon bring them into Python&\#x27;s standard library for the first time.

**Tags**: `#Python`, `#language release`, `#open source`, `#PEP 810`, `#lazy imports`

---

<a id="item-tech-news-2"></a>
### [U-Space: Label-free Uncertainty Estimation for Reasoning LLMs](https://www.reddit.com/r/MachineLearning/comments/1x44f9m/uspace_uncovering_when_and_why_uncertainty_arises/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/AdRevolutionary3242 · Oct 12, 15:10

#### Summary

Researchers released U-Space, a label-free method for estimating when and why open-weight reasoning language models are uncertain. The approach scores uncertainty in a single pass using hidden state patterns and token entropy, categorizing uncertainty as ambiguity, missing information, conflicting evidence, or general uncertainty. Evaluated across three models \(Gemma 4, Qwen3.5, Magistral\) and four benchmarks, U-Lens outperformed 5-pass, 10-pass, and supervised baselines. The system ships with 40+ pre-fitted J-Lens vectors on Hugging Face for popular architectures, with reference code to build custom lenses. The project is presented as open research code rather than a production package.

#### Background

Most uncertainty estimation methods for large language models either require multiple sampling passes to compute confidence distributions or depend on labeled datasets for training. U-Space departs from both approaches by reading uncertainty directly from the model&\#x27;s internal representations. The method reuses a J-Lens, originally developed by Anthropic to probe global workspace neurons, as a model-specific directional probe that can be fit on roughly 100 unlabeled prompts.

**Tags**: `#artificial intelligence`, `#machine learning`, `#language models`, `#research`, `#uncertainty estimation`

---