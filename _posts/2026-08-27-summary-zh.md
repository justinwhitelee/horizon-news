---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27
lang: zh
---

> 从 201 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [英伟达拟以 130 亿美元收购 Hugging Face](#item-tech-news-1) ⭐️ 9.0/10
2. [vLLM v0.28.0 发布：584 项提交，新增 Kimi-K3 与 DeepSeek V4 优化](#item-tech-news-2) ⭐️ 8.0/10
3. [智谱发布 GLM-5.3-Flash 开源模型](#item-tech-news-3) ⭐️ 8.0/10
4. [Qwen3.8-Flash-Next：125B 主模型+51B N-gram 嵌入的混合架构](#item-tech-news-4) ⭐️ 8.0/10
5. [美国司法部查封中国僵尸网络域名](#item-tech-news-5) ⭐️ 8.0/10
6. [用 57 万条 Photoshop 裁剪标签自动化书籍数字化，10 次校正胜过大模型](#item-tech-news-6) ⭐️ 8.0/10
7. [阿里通义发布 Qwen3.8-Flash 多模态 MoE 模型](#item-tech-news-7) ⭐️ 8.0/10
8. [中国首次实现地月双向高速激光通信](#item-tech-news-8) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [英伟达拟以 130 亿美元收购 Hugging Face](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) ⭐️ 9.0/10



hackernews · mfiguiere · 8月27日 01:12 · [社区讨论](https://news.ycombinator.com/item?id=49458161)

#### 摘要

据 The Information 和 TechCrunch 报道，英伟达已与开源 AI 平台 Hugging Face 达成收购协议，交易估值约为 129 亿至 130 亿美元。英伟达早在 2023 年 2 月就以 45 亿美元估值参与了 Hugging Face 2.35 亿美元的融资，目前仍是其股东；微软也曾接触洽购，但相关谈判已停止。消息来源指出双方尚未最终敲定，交易仍存在破裂可能。知情人士透露，此次收购若成行，将成为 AI 领域规模最大的收购案之一。

#### 背景

Hugging Face 成立于 2016 年，最初聚焦自然语言处理工具开发，2020 年推出 Transformers 库后迅速成为开源 AI 社区的核心平台。截至 2023 年 2 月，其融资估值约 45 亿美元；英伟达曾参与该轮 2.35 亿美元投资，成为少数股东之一。Ggml.ai（llama.cpp 团队）此前加入 Hugging Face 以确保 Local AI 的长期发展路径。

#### 社区讨论

社区对此反响强烈：批评者认为英伟达一贯倾向控制软件栈和专有 API，收购后将危及开源生态；也有人乐观推测开发者可获得更多免费或折扣的云端算力额度。另有评论担忧英伟达将获得 Hugging Face 平台上的硬件 Survey 数据和模型下载模式等高价值信息，构成潜在的反垄断风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8?op=1">Nvidia has been in talks to acquire Hugging Face for more than $13 billion</a></li>

</ul>
</details>

**标签**: `#AI`, `#acquisitions`, `#open source`, `#Nvidia`, `#Hugging Face`

---

<a id="item-tech-news-2"></a>
### [vLLM v0.28.0 发布：584 项提交，新增 Kimi-K3 与 DeepSeek V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 8.0/10



github · khluu · 8月26日 09:46

#### 概述

vLLM v0.28.0 正式发布，包含来自 270 位贡献者（其中 76 位新增）的 584 项提交。本次重大版本重点引入 Kimi-K3 全栈优化，包括 Decode Context Parallel \(DCP\) 支持、融合 FlashKDA 解码与预填充核，以及自适应推测 token 预算使 DSpark TTFT 提升约 60%；同时实现 DeepSeek V4 稀疏 MLA 端到端支持（涵盖 plain decode、MTP 和 DSpark 推测解码）。其他亮点包括 AMD Quark NVFP4 支持、Tiered KV 缓存磁盘卸载、模型 Runner V2 成熟化（E/P/D 分离、权重卸载、注意力自由模型），以及 \`max\_num\_batched\_tokens\` 默认值从 8192 提升至 16384。破坏性变更方面：bitsandbytes 迁移至树外插件，Transformers 升级至 5.15.0，已弃用的 \`calculate\_kv\_scales\` 运行时 KV 缩放计算与 \`override\_attention\_dtype\` 被移除。

#### 背景

vLLM 是目前最广泛使用的开源大语言模型推理引擎之一，支持多种 GPU 硬件与模型架构。DeepSeek V4 和 Kimi-K3 是近期发布的新型大模型，前者采用稀疏 MLA（Mixed Linear Attention）架构，后者为 Moonshot AI 的推理优化模型，涉及 MegaMoE 等结构。推测解码（speculative decoding）是一种通过小草稿模型加速大模型推理的技术，可显著降低首 token 延迟（TTFT）。

#### 社区讨论

暂无社区评论可供总结。

**标签**: `#LLM inference`, `#vLLM`, `#model optimization`, `#speculative decoding`, `#open source AI`

---

<a id="item-tech-news-3"></a>
### [智谱发布 GLM-5.3-Flash 开源模型](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10



hackernews · Philpax · 8月26日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49449507)

#### 摘要

Z.ai 发布 GLM-5.3-Flash 开源模型，该模型参数量和成本较先前版本显著降低。Hugging Face 上已提供权重下载，社区反馈显示其性能接近 GLM-5.3 原版，但参数减半、价格降至约五分之一，且在国产芯片上可部署。有用户评论指出，该模型在性价比上超越 DeepSeek V4 Flash，甚至以更低成本匹配 V4 Pro 性能。与此同时，部分用户对该模型的长期使用许可条款提出关切。

#### 社区讨论

Hacker News 社区对 GLM-5.3-Flash 的性价比表示认可，多位用户将其与 Luna 系列及 DeepSeek V4 进行对比，认为其在降低成本的同时保持较强性能。但也有用户指出 Z.ai 的服务条款包含宽泛的永久许可授权和模糊的限制条款，引发对数据使用和账户管理的担忧。

**标签**: `#AI models`, `#open source`, `#model release`, `#China AI`, `#LLMs`

---

<a id="item-tech-news-4"></a>
### [Qwen3.8-Flash-Next：125B 主模型+51B N-gram 嵌入的混合架构](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 8.0/10



hackernews · tosh · 8月26日 12:52 · [社区讨论](https://news.ycombinator.com/item?id=49448210)

#### 概述

Qwen3.8-Flash-Next 引入了混合架构，包含 125B 参数的主模型和 51B N-gram 嵌入，每 token 仅激活 6B 参数。该设计旨在通过稀疏激活在保持较大上下文记忆能力的同时降低计算开销。HackerNews 社区对其量化可行性与内存需求进行了热烈讨论，有用户报告在 QwenCloud 上以$0.45 成本完成了大规模代码分支合并与回归修复任务，实际调用量仅占周配额约 10%。另有测试者使用 Unsloth GGUF 变体在 DGX Spark 上运行不同推理级别，反馈其性能与上一代 27B 模型相比优势不明显。

#### Qwen3.8-Flash-Next 的混合 MoE 架构

Qwen3.8-Flash-Next 是阿里巴巴 Qwen 系列中的一个多模态超稀疏混合专家（MoE）模型。MoE 架构通过门控机制动态激活子网络，允许模型拥有庞大总参数量同时保持较低的每令牌计算成本。该模型总参数量为 125B，其中包含 51B N-gram 嵌入，但每个 token 仅激活 6B 参数，显著提高了内存效率。其架构结合了门控 DeltaNet（用于压缩历史信息）和 Qwen 稀疏注意力（用于长距离依赖检索），进一步优化了推理性能。

#### 社区讨论

社区主要关注三点：一是该模型总参数量约 176B，但 4-bit 量化后能否在 128GB 统一内存中运行仍存在疑虑；二是 N-gram 嵌入的技术直觉引发了关于 DeepSeek 与 Gemma 类似方案的讨论；三是实际性能表现褒贬不一，有用户对其代码能力印象深刻，也有测试者认为其在部分场景下未明显超越 Qwen3.8 27B 版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forums.developer.nvidia.com/t/qwen3-8-flash-next/381228">Qwen3.8-Flash-Next - DGX Spark / GB10 - NVIDIA Developer Forums</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-Flash-Next">Qwen/Qwen3.8-Flash-Next | vLLM Recipes</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#machine learning`, `#large language models`, `#model architecture`, `#open source`

---

<a id="item-tech-news-5"></a>
### [美国司法部查封中国僵尸网络域名](https://techcrunch.com/2026/08/26/us-seizes-domains-of-chinese-botnet-used-to-hack-nasa-justice-department-and-the-senate/) ⭐️ 8.0/10



rss · TechCrunch · 8月26日 17:01

#### 摘要

美国司法部于 2026 年 8 月 26 日宣布查封一个中国僵尸网络的域名，该僵尸网络曾被用于入侵美国国家航空航天局（NASA）、司法部（DOJ）和参议院。司法部表示，这些域名被硬编码进僵尸网络代码中，是其通信和核心运作的关键基础设施；查封行动使该僵尸网络及其命令与控制服务器完全失效。这是针对国家级网络威胁的一次重大执法行动，标志着美国在网络空间对抗中采取了直接的基础设施破坏手段。

**标签**: `#cybersecurity`, `#nation-state hacking`, `#botnet takedown`, `#domain seizure`, `#government compromise`

---

<a id="item-tech-news-6"></a>
### [用 57 万条 Photoshop 裁剪标签自动化书籍数字化，10 次校正胜过大模型](https://www.reddit.com/r/MachineLearning/comments/1vz2ojw/we_recovered_575k_crop_labels_from_a_decade_of/) ⭐️ 8.0/10

巴基斯坦 Ibteda 数字图书馆的研究者从十年手工数字化工作中回收了 575,729 条 Photoshop 裁剪标签，用于训练自动化裁剪模型。

reddit · r/MachineLearning · /u/laamaleph · 8月26日 16:53

#### 摘要

Ibteda 数字图书馆（巴基斯坦）从十年手工数字化 1,765 册乌尔都语书籍的过程中，回收了 575,729 张已完成的 Photoshop 裁剪决策，通过 SIFT+MAGSAC 配准将其映射回原始照片作为监督信号。研究发现扩大训练量（378 本增至 572 本）、改用 ResNet-50、输入分辨率提升至 1024px 以及增加空间头，均未能提升 hold-out 书籍的 pass@80 指标。根本原因在于每本书存在近乎恒定的偏移——即操作者偏好的页边距内缩，而这一偏好并不存在于新书的像素中。仅需每本书 10 个操作者校正裁剪（计算元素级中值残差），pass@80 便从 0.71 提升至 0.83，超越了所有扩展手段。在修 retouching 方面，U-Net 仅用于检测，经典 OpenCV 负责重建纸张，蒙版外区域与原文字节一致；引入 REMOVE/KEEP/IGNORE 标签状态，并以

**标签**: `#machine learning`, `#computer vision`, `#negative results`, `#data annotation`, `#dataset construction`

---

<a id="item-tech-news-7"></a>
### [阿里通义发布 Qwen3.8-Flash 多模态 MoE 模型](https://x.com/Alibaba_Qwen/status/2092591393424515114) ⭐️ 8.0/10



telegram · zaihuapd · 8月26日 13:36

#### 概述

阿里通义正式发布多模态 MoE 模型 Qwen3.8-Flash，该模型共 125B 参数，每 token 仅激活 6B，原生支持 262K 上下文长度并可扩展至 1M。阿里称其性能可比肩 Anthropic Opus 4.6 和 DeepSeek V4-Flash，并在编码与办公任务上较 Qwen3.7-Plus 表现更优。作为 Qwen4 架构预览版，开源版本命名为 Qwen3.8-Flash-Next。相比 Qwen3.7-Plus，训练成本仅约为其九分之一。API 定价为每百万输入 token 0.16 美元、输出 0.47 美元。

**标签**: `#AI Models`, `#Open Source`, `#Large Language Models`, `#Cost Efficiency`, `#MoE Architecture`

---

<a id="item-tech-news-8"></a>
### [中国首次实现地月双向高速激光通信](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 8.0/10

中国科学院空间应用工程与技术中心牵头，依托 DRO-A 卫星成功在超过 40 万公里的地月距离建立双向激光链路，首次实现地月双向高速激光通信。

telegram · zaihuapd · 8月27日 00:33

#### 摘要

中国科学院空间应用工程与技术中心牵头，依托 DRO-A 卫星，成功在超过 40 万公里的地月距离上建立双向激光通信链路，首次实现地月双向高速激光通信，标志着我国空间激光通信从近地轨道正式迈入地月空间。此次试验初步实现上行速率 1.25 Mbps、下行速率 100 Mbps。以 8K 月面高清图像为例，传统 5 Mbps 微波下传需约 4 到 5 分钟，而百 Mbps 激光通信仅需约 12 秒，传输效率提升数十倍，对月球探测及数据密集型任务具有显著实用价值。

**标签**: `#space communication`, `#laser communication`, `#lunar exploration`, `#aerospace engineering`

---