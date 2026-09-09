---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 203 items, 3 important content pieces were selected

---

**Technology News**
1. [OpenAI Claims Breakthrough on Navier-Stokes Millennium Prize Problem](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepMind releases AlphaGenome Atlas, a high-resolution map of all possible human DNA changes](#item-tech-news-2) ⭐️ 8.0/10
3. [2.8T Kimi K3 model runs at 1 token/s on MacBook Pro via SSD streaming](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [OpenAI Claims Breakthrough on Navier-Stokes Millennium Prize Problem](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/) ⭐️ 9.0/10



reddit · r/MachineLearning · /u/Shizuka\_Kuze · Sep 8, 17:42

#### Summary

OpenAI announced on September 8, 2026 that it has resolved the Navier–Stokes existence and smoothness problem, one of the Clay Mathematics Institute&\#x27;s seven Millennium Prize Problems offering a $1,000,000 prize since 2000. The result was produced by an unreleased internal model, with agents reaching a resolution on September 5 after being prompted on September 1 following rumors of other Millennium Prize breakthroughs. Lean formalization and verification took an additional 17 hours via GPT‑6 Astra. Across all attempted problems the agents sent 4.9 million messages and used about 300 billion output tokens; resolving Navier–Stokes alone required 2.7 million messages and approximately 130 billion output tokens. At public API prices for GPT-6 Astra, that would equate to roughly $15 million.

#### Background

The Navier–Stokes existence and smoothness problem concerns whether smooth, general solutions to the Navier–Stokes equations—governing fluid motion—always exist, a question open for roughly 90 years. The Clay Mathematics Institute designated it one of seven Millennium Prize Problems in May 2000. Formal verification using proof assistants such as Lean has become an increasingly relevant tool for validating complex mathematical arguments generated or assisted by AI systems.

#### Community Discussion

NYU mathematics professor Tristan Buckmaster, who had collaborated with Anthropic&\#x27;s Levent Alpöge for nearly a year using Claude and Codex \(mainly GPT-5.6 Sol\), accused OpenAI of scooping their work after learning of their progress through internal rumors. Buckmaster noted OpenAI did not directly answer whether their model had been trained on or accessed data from his Codex sessions, though OpenAI acknowledged it cannot rule out that de-identified training data derived from user activity helped improve its models. OpenAI stated its proof differs significantly from Buckmaster and Alpöge&\#x27;s—even in the Euler case—and offered a joint announcement recognizing their priority, but declined to include Alpöge as a co-author due to his employment at Anthropic.

**Tags**: `#artificial intelligence`, `#machine learning`, `#mathematics`, `#research`, `#open source`

---

<a id="item-tech-news-2"></a>
### [DeepMind releases AlphaGenome Atlas, a high-resolution map of all possible human DNA changes](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 8.0/10



hackernews · utiiiD · Sep 8, 14:55 · [Discussion](https://news.ycombinator.com/item?id=49611251)

#### Summary

DeepMind has released AlphaGenome Atlas, a high-resolution predictive map covering every possible single-nucleotide change in the human genome. The tool extends DeepMind&\#x27;s AI-for-biology lineage—building on AlphaFold—into genomics, offering predictions for non-coding DNA variants rather than being limited to protein structure. It is available for researchers at deepmind.google.com/science/alphagenome/atlas, with integration via the AntiGravity platform for scientists looking to start using it. The atlas addresses a longstanding need in the field: interpreting the functional impact of genetic variants outside protein-coding regions.

#### Background

AlphaGenome Atlas extends DeepMind’s earlier AlphaFold system, which predicts protein structures, into the domain of whole-genome variant interpretation. It catalogues the molecular effects of all possible single-nucleotide substitutions across the roughly 3 billion base pairs of the human genome, yielding approximately 9 billion predictions \(tool-1-1\). Single-nucleotide variants are changes at a single DNA letter and are fundamental to understanding genetic disease and evolutionary variation.

#### Community Discussion

The Hacker News thread \(484 score, 115 comments\) raised several points: a user noted no explicit mention of promoter sequences in the release, though non-coding DNA coverage may encompass them; others clarified that the atlas tool requires no formal affiliation to access. Questions also arose about whether 23andMe genomes could be used with the tool to identify pathogenic mutations, and some commenters expressed cautious interest given mixed track records for DeepMind&\#x27;s prior biology models outside of AlphaFold.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas : Molecular predictions for 9 Billion human DNA ...</a></li>

</ul>
</details>

**Tags**: `#AI for biology`, `#genomics`, `#DeepMind`, `#variant prediction`, `#computational biology`

---

<a id="item-tech-news-3"></a>
### [2.8T Kimi K3 model runs at 1 token/s on MacBook Pro via SSD streaming](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10



hackernews · Argonautlabs · Sep 8, 20:07 · [Discussion](https://news.ycombinator.com/item?id=49616257)

#### Summary

Argonaut Labs has demonstrated running the 2.8T-parameter Kimi K3 language model at roughly 1 token per second on a MacBook Pro by streaming model weights from four SSDs instead of loading them into RAM. The project was shared on GitHub under the repository name deltafin. The approach is necessary because Apple Silicon Macs do not allow RAM upgrades, making the SSDs a practical workaround for handling the model&\#x27;s enormous memory requirements. The community has characterized the result as a notable engineering milestone, noting that fully local inference at this scale was previously considered infeasible on consumer hardware.

#### Community Discussion

Commenters broadly treated the work as a promising first step rather than a production-ready solution, with one noting that running a 2.8T model locally was previously impossible and calling this a &\#x27;good start.&\#x27; Others drew historical parallels, comparing the SSD-based workaround to old &\#x27;640KB ought to be enough&\#x27; jokes and referencing the fictional supercomputer Deep Thought. Some discussion focused on the novelty and technical approach, including curiosity about how the SSDs are connected, while one comment observed that generating a medium-length prompt still takes around 11 days, underscoring the extreme slowness of the setup.

**Tags**: `#AI inference`, `#large language models`, `#hardware efficiency`, `#open source`, `#local deployment`

---