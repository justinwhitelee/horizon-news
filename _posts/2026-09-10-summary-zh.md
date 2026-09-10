---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 209 条内容中筛选出 4 条重要资讯。

---

**科技新闻**
1. [vLLM v0.29.0 发布：Model Runner V2 成默认，支持腾讯 770B MoE](#item-tech-news-1) ⭐️ 8.0/10
2. [苹果发布 iPhone Duo 双屏折叠手机](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI’s sly mathematical breakthrough sends a chill through academia](#item-tech-news-3) ⭐️ 8.0/10
4. [Verge 员工点评 iPhone Duo：爱与不爱](#item-tech-news-4) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.29.0 发布：Model Runner V2 成默认，支持腾讯 770B MoE](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10



github · khluu · 9月9日 08:54

#### 摘要

vLLM v0.29.0 正式发布，包含来自 277 位贡献者（其中 91 位为新贡献者）的 594 个提交。最核心的变更是 Model Runner V2 成为所有模型的新默认后端，同时带来了 CUDA graph 内存分析、batch-sharded sampling（按 TP 将每步 logits 内存降至 1/TP）、prompt embeds 等增强功能。新支持模型包括腾讯 770B/49B-active MoE、Qwen3.8-Flash-Next（支持 BF16/FP8/NVFP4）、Kimi K3 NVFP4 以及 GraniteSWA 等。性能方面，Kimi K3 的 fused MXFP4 top-k 带来约 5% 端到端延迟优化，Mamba 预处理提速 6.6-7.6 倍，低延迟 GEMM 在 SM100 上的加速达 12.9-25.2%。同时有大量破坏性变更：十个已弃用模型架构被移除，FlexOlmo/Olmo3/Hunyuan V1/VL 迁移至 Transformers 后端，PyAV 视频解码器后端被移除，启动命令由 \`python -m vllm.entrypoints.openai.api\_server\` 改为 \`vllm serve\`。

**标签**: `#open source`, `#machine learning`, `#AI infrastructure`, `#LLM serving`, `#model optimization`

---

<a id="item-tech-news-2"></a>
### [苹果发布 iPhone Duo 双屏折叠手机](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果公司推出 iPhone Duo，一款双屏折叠设备，标志着其旗舰产品线自 2017 年以来最重要的更新。

hackernews · thecosmicfrog · 9月9日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

#### 概要

苹果公司正式发布 iPhone Duo，这是一款采用双屏折叠设计的 iPhone 设备。此次发布是苹果旗舰产品自 2017 年以来最重大的革新，由新任首席执行官 John Ternus 主持，并显示出苹果在折叠屏手机市场的重要布局。社区评论普遍认为该设计出色且屏幕折痕不明显，但部分用户持观望态度，期待后续产品迭代验证可靠性。该设备有望推动开发者为折叠屏优化应用，从而改善 Android 和 iOS 折叠设备上的屏幕空间利用体验。

#### 背景

折叠屏手机市场近年来由三星、华为等安卓厂商主导，推出了多款可折叠设备，但应用生态适配仍不完善。苹果此前未在折叠屏领域推出产品，此次 iPhone Duo 的亮相被视为其进入该细分市场的关键一步。

#### 社区讨论

社区对 iPhone Duo 的设计表示赞赏，有用户称实机效果优于发布会演示且折痕几乎不可见；同时，新一代发布会风格与以往 Tim Cook 模式有所不同。部分用户谨慎观望，计划等待几年后产品成熟再考虑更换；也有近期 Pixel 折叠屏用户期待苹果加入能促使开发者更好地适配折叠屏应用。

**标签**: `#hardware`, `#mobile`, `#foldable devices`, `#Apple`, `#product announcement`

---

<a id="item-tech-news-3"></a>
### [OpenAI’s sly mathematical breakthrough sends a chill through academia](https://www.theverge.com/ai-artificial-intelligence/992953/openai-math-millennium-prize-navier-stokes) ⭐️ 8.0/10

OpenAI reportedly solved a Millennium Prize problem in mathematics, though the announcement has been complicated by unresolved issues.

rss · The Verge · 9月9日 21:16

**标签**: `#artificial intelligence`, `#mathematics`, `#OpenAI`, `#research`, `#technology industry`

---

<a id="item-tech-news-4"></a>
### [Verge 员工点评 iPhone Duo：爱与不爱](https://www.theverge.com/tech/992830/apple-iphone-duo-foldable-verge-staffers-react) ⭐️ 8.0/10



rss · The Verge · 9月9日 19:45

#### 摘要

The Verge 编辑团队对苹果首款折叠屏 iPhone——iPhone Duo 发表了评测反应，内容涵盖其双屏设计、硬件规格及 iOS 适配。该机配备 5.4 英寸外屏和 7.6 英寸内屏，搭载双后置摄像头、Touch ID 认证以及 IP68 防尘防水等级，同时通过多种软件优化让 iOS 更好地适配折叠形态。这一产品发布被视为智能手机设计趋势的重要风向标，将对移动生态产生广泛影响。

#### iPhone Duo 折叠屏背景

折叠屏手机是指通过铰链结构实现屏幕折叠、具备内外双显示屏的移动设备，代表了一种可兼顾便携与大屏体验的新型形态。苹果在 2026 年 9 月的产品发布会上首次推出 iPhone Duo，配备 5.4 英寸外屏与 7.6 英寸内屏，并针对 iOS 进行了适配优化；该产品起售价为 1,999 美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/992830/apple-iphone-duo-foldable-verge-staffers-react">Verge staffers react to the iPhone Duo: What we love and don ...</a></li>
<li><a href="https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/">Apple unveils iPhone Duo</a></li>
<li><a href="https://www.nytimes.com/2026/09/09/technology/apple-iphone-duo-foldable-phone.html">Apple Unveils the iPhone Duo, a Foldable Phone That Costs ...</a></li>

</ul>
</details>

**标签**: `#hardware`, `#mobile`, `#consumer tech`, `#product launch`

---