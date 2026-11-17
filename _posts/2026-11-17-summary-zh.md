---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 209 条内容中筛选出 3 条重要资讯。

---

**科技新闻**
1. [vLLM 发布 v0.34.0：架构简化与性能提升](#item-tech-news-1) ⭐️ 8.0/10
2. [美国加强对华 AI 芯片出口管制，新增多国许可要求](#item-tech-news-2) ⭐️ 8.0/10
3. [Nature 发表混合维度 CMOS 技术研究](#item-tech-news-3) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM 发布 v0.34.0：架构简化与性能提升](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10



github · khluu · 11月16日 23:22

#### 摘要

vLLM 项目发布了 v0.34.0 版本，包含来自 412 名贡献者的 1,061 次提交。该版本最重要的架构变更是移除了 Model Runner V1，MRV2 成为唯一的 GPU 运行器；同时将可扩展 KV 缓存功能默认开启，使缓存大小基于实际可用内存进行分配。性能方面，在 NVIDIA Blackwell（GB200/GB300）和 AMD MI355X 平台上获得了显著提升，解码吞吐量最高提升 1.95 倍。新版本还支持了 Mistral Large 4、MiniMax-M3.1-Flash 等 10 款新模型，并为推理引擎引入了检查点保存与恢复功能。

#### 背景

vLLM 是一款广泛使用的大语言模型推理引擎，以其高效的 KV 缓存管理和 PagedAttention 技术而闻名。KV 缓存用于存储注意力机制中的键值张量，直接影响生成吞吐量和延迟。Model Runner 是 vLLM 中负责 GPU 端模型执行的组件，V2 版本引入了更好的并发控制和更灵活的调度策略。随着硬件生态的扩展，vLLM 持续优化对 AMD ROCm 及新一代 NVIDIA Blackwell 架构的支持。

**标签**: `#LLM inference`, `#open source software`, `#GPU optimization`, `#model deployment`, `#performance engineering`

---

<a id="item-tech-news-2"></a>
### [美国加强对华 AI 芯片出口管制，新增多国许可要求](https://www.aljazeera.com/economy/2026/11/17/us-moves-to-block-chinas-remote-access-to-ai-chips-amid-nvidia-scandal?traffic_source=rss) ⭐️ 8.0/10



rss · Al Jazeera · 11月17日 02:52

#### 摘要

特朗普政府近期引入针对马来西亚、泰国、印度尼西亚、新加坡和巴西等五个国家的 AI 芯片出口许可证要求。这一举措源于关于英伟达（Nvidia）芯片远程访问功能的担忧，涉及中国通过海外中转获取高端 AI 芯片的风险。该政策调整直接反映了美国对半导体出口管制的持续收紧趋势，旨在堵住可能被利用的供应链漏洞，限制中国远程访问 AI 计算资源的路径。此举对相关国家的芯片贸易合规要求将产生实质性影响，也凸显了 AI 硬件安全与地缘政治博弈之间的紧密关联。

**标签**: `#AI chips`, `#semiconductor policy`, `#export controls`, `#hardware security`

---

<a id="item-tech-news-3"></a>
### [Nature 发表混合维度 CMOS 技术研究](https://news.google.com/rss/articles/CBMiX0FVX3lxTE4wYVFQb1FPNXlzRWFSRlNGTjBfekk2ZmZ1d0k5N09xRUc4UU1EUGRMX3h5WXJjdG5XQTVnZUhqeDRrRC05OHBXVWt1RjVQeGUzVHpPVHpDbjNYVTVXdVhv?oc=5) ⭐️ 8.0/10



rss · Google News \(Tech\) · 11月16日 16:33

#### 摘要

《自然》杂志发表了一项关于混合维度互补金属氧化物半导体（CMOS）技术的研究，探索将不同维度的材料集成到先进半导体制造中。该研究涉及将二维材料与传统的三维结构相结合，代表后摩尔定律时代集成电路扩展的重要技术进展。这项工作在高性能集成电路制造领域具有潜在应用价值，为突破传统硅基器件的尺寸限制提供了新的技术路径。

#### 背景

CMOS（互补金属氧化物半导体）技术是现代集成电路的主流制造工艺，通过结合 NMOS 和 PMOS 晶体管实现低功耗逻辑电路。二维材料如 MoS₂和 WSe₂具有原子级厚度，展现出优异的电学特性，被视为后摩尔时代扩展晶体管缩放的潜在候选材料。混合维度 CMOS 技术旨在将二维半导体材料与传统的三维硅基 CMOS 工艺集成，从而在性能、功耗和制造兼容性之间取得平衡。近年来，基于化学气相沉积（CVD）生长的二维材料的单片三维 CMOS 反相器阵列已得到实验验证，为该技术路线的可行性提供了支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CMOS">CMOS - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/357009562_Complementary_Two-Dimensional_2-D_MoS_2_FET_Technology">Complementary Two- Dimensional (2-D) MoS 2 FET Technology</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/36748299/">High - Performance CMOS Inverter Array with Monolithic...</a></li>

</ul>
</details>

**标签**: `#semiconductor technology`, `#integrated circuits`, `#CMOS`, `#post-Moore computing`, `#hardware research`

---