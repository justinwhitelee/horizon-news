---
layout: default
title: "Horizon Summary: 2026-08-21 (EN)"
date: 2026-08-21
lang: en
---

> From 202 items, 2 important content pieces were selected

---

**Technology News**
1. [Concise outputs cut LLM costs 1.5x; compressing inputs raises them](#item-tech-news-1) ⭐️ 8.0/10
2. [Changjiang Microelectronics STAR Market IPO accepted, seeking 33B RMB](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Concise outputs cut LLM costs 1.5x; compressing inputs raises them](https://www.reddit.com/r/MachineLearning/comments/1vulfei/does_telling_an_llm_to_be_concise_actually_save/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/ibubbles34 · Aug 21, 16:38

#### Summary

An empirical study across nine LLMs found that requesting concise outputs reduces API costs by roughly 1.5x on average—up to 3x in the best case—without sacrificing accuracy, while compressing input prompts does the opposite, costing up to 96% more and degrading accuracy. The study tested GPT-4o, GPT-5.4, Claude Haiku 4.5, Claude Sonnet 4.6, Qwen2.5-VL-7B, Qwen3.5-9B, DeepSeek-R1-Distill, Gemma-4-E4B, and Kimi-K2.6 on five short-answer datasets, a multi-language evaluation spanning English, German, Spanish, French, Swahili, Chinese, Japanese, Russian, Bengali, Thai, and Telugu, and a long-form summarization benchmark. Because output tokens are priced higher than input tokens, prompting for fewer output tokens yields net savings in single-turn tasks. The authors also noted that about half the time, shortened outputs produced different reasoning text even when the final answer remained correct, which they consider acceptable for answer-only use cases. The paper and code are available at alphaxiv.org/pdf/2606.24083v1 and github.com/danielle34/cavewoman.

#### Background

LLMs are notoriously verbose, producing outputs significantly longer than necessary for many tasks. In most commercial API pricing models, output tokens cost more than input tokens, creating a financial incentive to reduce output length. Prompt engineering techniques have long been used to steer model behavior, but their cost implications have not been systematically measured across a broad set of models and languages.

**Tags**: `#LLM cost optimization`, `#prompt engineering`, `#LLM efficiency`, `#empirical research`, `#production ML`

---

<a id="item-tech-news-2"></a>
### [Changjiang Microelectronics STAR Market IPO accepted, seeking 33B RMB](https://api3.cls.cn/share/article/2461025?os=android&amp;amp;sv=8.8.2&amp;amp;app=cailianpress) ⭐️ 8.0/10



telegram · zaihuapd · Aug 21, 14:26

#### Summary

Changjiang Microelectronics&\#x27; STAR Market IPO application has been accepted by the Shanghai Stock Exchange, with a planned raise of 33 billion RMB, according to documents released on the exchange&\#x27;s website. The sponsors are CITIC Securities and CITIC Construction Securities, and the company moved from tutoring acceptance to IPO acceptance in approximately three months, with its tutoring status changing on August 19. Prospectus figures show first-quarter 2026 revenue of 47.042 billion RMB and net profit of 33.379 billion RMB. Meanwhile, Counterpoint reported that the company entered the global NAND flash top three by shipment volume for the first time in Q2 2026.

#### Background

Changjiang Microelectronics \(Yinxiang\) is a Chinese NAND flash memory manufacturer that has been subject to U.S. export controls andEntity List restrictions since 2022, which have constrained its access to advanced semiconductor manufacturing equipment. The STAR Market \(Kechuangban\) is Shanghai Stock Exchange&\#x27;s board aimed at supporting innovative technology companies, analogous to China&\#x27;s equivalent of a NASDAQ-style listing venue.

**Tags**: `#semiconductors`, `#NAND flash memory`, `#IPO`, `#China tech industry`, `#hardware`

---