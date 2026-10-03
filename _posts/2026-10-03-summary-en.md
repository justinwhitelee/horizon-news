---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 190 items, 3 important content pieces were selected

---

**Technology News**
1. [AI defeats best-ever Stratego player with sample-efficient algorithm](#item-tech-news-1) ⭐️ 9.0/10
2. [arXiv caps submissions at 2 per author per month](#item-tech-news-2) ⭐️ 8.0/10
3. [Google Research introduces Cogentic multi-agent system for automated proof discovery](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AI defeats best-ever Stratego player with sample-efficient algorithm](https://arstechnica.com/science/2026/10/ai-finally-beat-the-best-stratego-player-in-history-and-did-it-on-a-budget/) ⭐️ 9.0/10



hackernews · PaulHoule · Oct 2, 14:11 · [Discussion](https://news.ycombinator.com/item?id=49933740)

#### Summary

A study published in Nature reports that an AI has defeated the best Stratego player in history, overcoming one of the most significant challenges in game-playing AI: imperfect information. The new algorithm learned far more efficiently than prior approaches, requiring roughly 34 times fewer games than DeepNash while ultimately achieving stronger play. This result follows up on a 2022 DeepMind effort titled &\#x27;Mastering the Game of Stratego with Model-Free Multiagent Reinforcement Learning,&\#x27; which had not yet reached human-elite level. Stratego&\#x27;s core difficulty lies in its hidden information—players cannot see their opponent&\#x27;s pieces, making traditional search-based reasoning far less effective and requiring AI systems to reason under uncertainty rather than perfect-information assumptions.

#### Community Discussion

Commenters expressed surprise that Stratego, a seemingly straightforward board game, had resisted AI conquest for so long. Several noted the 34x sample-efficiency improvement as the key practical achievement, since hidden information makes conventional look-ahead search unreliable. One commenter observed that the 2022 &\#x27;mastering&\#x27; paper fell short of human-elite strength and framed the new result as finally closing that gap.

**Tags**: `#artificial intelligence`, `#game-playing AI`, `#hidden information`, `#machine learning`, `#research breakthrough`

---

<a id="item-tech-news-2"></a>
### [arXiv caps submissions at 2 per author per month](https://www.huxiu.com/article/4895127.html) ⭐️ 8.0/10



telegram · zaihuapd · Oct 2, 06:21

#### Summary

arXiv has imposed a universal cap of 2 monthly submissions per author, effective October 1, across all disciplines including computer science, mathematics, and physics. Rejected papers also count toward the monthly quota. The policy responds to September&\#x27;s record 40,363 submissions—a 35-year high—driven largely by a sixfold increase in AI-category papers over two years and a surge of low-quality AI-generated submissions straining human peer-review resources. For multi-author papers, only the actual submitter is counted; other co-authors remain unaffected by the limit.

#### Background

arXiv is the world&\#x27;s largest preprint repository and a primary dissemination channel for research in computer science, machine learning, mathematics, and physics. Unlike traditional journals, it does not perform full peer review before publication, relying instead on community post-publication evaluation and moderation, which makes submission volume directly impactful on review capacity.

#### Community Discussion

No community comments were available for this item.

**Tags**: `#arXiv`, `#AI research`, `#preprint policy`, `#academic publishing`, `#machine learning`

---

<a id="item-tech-news-3"></a>
### [Google Research introduces Cogentic multi-agent system for automated proof discovery](https://arxiv.org/abs/2609.40324v1) ⭐️ 8.0/10



telegram · zaihuapd · Oct 2, 12:04

#### Summary

Google Research has published Cogentic \(arXiv:2609.40324v1\), a multi-agent system designed for automated theorem discovery. The system employs a prove-verify cycle in which multiple independent provers—built on the Gemini base model—explore distinct proof strategies simultaneously, while a dedicated adversarial verifier challenges those results. Confirmed proofs are recorded in a persistent validated ledger for reuse across subsequent attempts. The system produced new, expert-verified results on five open problems spanning online learning, auction theory, and mechanism design.

#### Background

Automated theorem proving has historically relied on specialized logic engines \(e.g., Coq, Lean\) that construct proofs in formally verified languages, but scaling these systems to open research problems has proven difficult. Large language models have recently been explored as flexible reasoning agents for mathematics, often using iterative generate-and-verify loops. Multi-agent frameworks partition such tasks among specialized roles—provers, verifiers, and curators—to improve coverage and reduce single-model bias. The concept of a persistent verified ledger draws from formal methods, where confirmed lemmas are stored for reuse across problems, enabling long-horizon theorem proving.

**Tags**: `#AI for Mathematics`, `#Multi-Agent Systems`, `#Automated Theorem Proving`, `#Machine Learning Theory`, `#Formal Verification`

---