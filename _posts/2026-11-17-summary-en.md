---
layout: default
title: "Horizon Summary: 2026-11-17 (EN)"
date: 2026-11-17
lang: en
---

> From 209 items, 3 important content pieces were selected

---

**Technology News**
1. [vLLM v0.34.0 Released with Major Architectural Changes](#item-tech-news-1) ⭐️ 8.0/10
2. [US expands AI chip export controls on five nations over remote-access concerns](#item-tech-news-2) ⭐️ 8.0/10
3. [Mixed-dimensional CMOS advances post-Moore computing via multi-material integration](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [vLLM v0.34.0 Released with Major Architectural Changes](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10



github · khluu · Nov 16, 23:22

#### Summary

vLLM v0.34.0 introduces significant architectural changes and performance improvements across GPU hardware. The release enables extensible KV caching by default, which sizes memory from actual free space after warmup rather than estimates, increasing throughput for most models. Model Runner V1 has been removed entirely, consolidating on MRV2. Performance gains include up to 1.95× decode speedup on NVIDIA Blackwell GB200 systems and 1.6× throughput improvement on AMD MI355X hardware. Ten new models are now supported, including Mistral Large 4 with 52B active parameters, MiniMax-M3.1-Flash, and several NVIDIA speech and transcription models. Several breaking changes require attention during upgrade, including a default block size increase from 16 to 64 and dropping ROCm 7.2 artifacts in favor of ROCm 10.0.

#### Background

vLLM is an open-source LLM inference engine widely used for deploying large language models efficiently on GPU hardware. The KV cache stores key-value pairs computed during text generation to avoid redundant calculations, directly impacting throughput and latency. Model runners handle the execution pipeline for serving models on GPUs, and version management between runs simplifies deployment workflows.

**Tags**: `#LLM inference`, `#open source software`, `#GPU optimization`, `#model deployment`, `#performance engineering`

---

<a id="item-tech-news-2"></a>
### [US expands AI chip export controls on five nations over remote-access concerns](https://www.aljazeera.com/economy/2026/11/17/us-moves-to-block-chinas-remote-access-to-ai-chips-amid-nvidia-scandal?traffic_source=rss) ⭐️ 8.0/10



rss · Al Jazeera · Nov 17, 02:52

#### Summary

The Trump administration has introduced export license requirements for AI chips sold to Malaysia, Thailand, Indonesia, Singapore, and Brazil, according to a November 17, 2026 Al Jazeera report. The policy move follows reports of vulnerabilities involving remote access capabilities in Nvidia processors that raised concerns about China potentially exploiting such access. The additional licensing obligations extend existing U.S. semiconductor export controls aimed at limiting advanced computing hardware from reaching restricted end-users through intermediate countries.

#### Background

U.S. export controls on advanced AI chips have intensified in recent years to restrict China&\#x27;s access to high-performance computing hardware. These controls target both direct shipments to China and indirect routes through third-party countries. Nvidia GPUs used in AI training and inference have occasionally been scrutinized for firmware or connectivity features that could allow remote management functions, raising security questions when those chips are routed through unmonitored supply chains.

**Tags**: `#AI chips`, `#semiconductor policy`, `#export controls`, `#hardware security`

---

<a id="item-tech-news-3"></a>
### [Mixed-dimensional CMOS advances post-Moore computing via multi-material integration](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wYVFQb1FPNXlzRWFSRlNGTjBfekk2ZmZ1d0k5N09xRUc4UU1EUGRMX3h5WXJjdG5XQTVnZUhqeDRrRC05OHBXVWt1RjVQeGUzVHpPVHpDbjNYVTVXdVhv?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · Nov 16, 16:33

#### Summary

Research published in Nature reports a breakthrough in mixed-dimensional complementary metal–oxide–semiconductor \(CMOS\) technology that integrates materials of different dimensionalities—such as two-dimensional layers with conventional three-dimensional silicon structures—into advanced integrated circuit fabrication. The work addresses the continuing challenge of extending transistor scaling beyond the limits of traditional planar and fin-based approaches as Moore&\#x27;s Law slows. By combining distinct material dimensions within a single process flow, the approach aims to deliver higher performance per watt and greater design flexibility for next-generation chips.

#### Background

CMOS \(complementary metal–oxide–semiconductor\) is the dominant transistor technology used in modern integrated circuits, combining n-type and p-type field-effect transistors on a common substrate. As silicon CMOS scaling approaches fundamental physical limits, researchers have turned to two-dimensional \(2D\) materials such as molybdenum disulfide \(MoS₂\) and tungsten diselenide \(WSe₂\), which offer atomically thin channels and improved electrostatic control. Mixed-dimensional CMOS refers to the integration of these 2D semiconductor materials—typically grown by chemical vapor deposition—with conventional three-dimensional silicon process flows, enabling heterogeneous integration within a single chip rather than replacing existing infrastructure entirely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CMOS">CMOS - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/357009562_Complementary_Two-Dimensional_2-D_MoS_2_FET_Technology">Complementary Two- Dimensional (2-D) MoS 2 FET Technology</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/36748299/">High - Performance CMOS Inverter Array with Monolithic...</a></li>

</ul>
</details>

**Tags**: `#semiconductor technology`, `#integrated circuits`, `#CMOS`, `#post-Moore computing`, `#hardware research`

---