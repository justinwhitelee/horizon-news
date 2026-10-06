---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 188 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [vLLM v0.31.0 发布：SM100 优化与 FlashMLA 默认启用](#item-tech-news-1) ⭐️ 9.0/10
2. [Reflection AI 发布 Beam 501B 开源稀疏 MoE 模型](#item-tech-news-2) ⭐️ 8.0/10
3. [高通获授权华为 LogicFolding 芯片技术专利](#item-tech-news-3) ⭐️ 8.0/10
4. [丹麦政府数据库遭入侵，800 万公民信息泄露](#item-tech-news-4) ⭐️ 8.0/10
5. [Yandex Music Sona：单 Transformer 替代 15+ 推荐组件](#item-tech-news-5) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.31.0 发布：SM100 优化与 FlashMLA 默认启用](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 9.0/10



github · khluu · 10月5日 06:44

#### 摘要

vLLM 项目发布了 v0.31.0 重大版本，包含来自 307 位贡献者的 717 次提交。该版本将 FlashMLA 大注意力机制与 NVFP4 压缩 KV 缓存设为 SM100 GPU 的默认配置，显著提升 DeepSeek-V4.1-Flash 等模型的推理性能。新增 \`vllm preload\` 快速重启功能，通过权重缓存守护进程在引擎重启间保持量化后权重驻留显存；同时引入基于 CRIU 的实验性快照恢复。在大规模服务方面，支持 MoonEP 平衡 EP 后端、DeepEPv2 序列并行及 KV offloading 背压检测。安全方面新增请求级多模态参数网关和 prefix-cache 碰撞防护。此版本为 LLM 推理基础设施带来重要的性能与工程改进。

**标签**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#open source`, `#AI infrastructure`

---

<a id="item-tech-news-2"></a>
### [Reflection AI 发布 Beam 501B 开源稀疏 MoE 模型](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10



hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

#### 摘要

Reflection AI 发布了 Beam，一款 501B 总参数、23B 激活参数的稀疏混合专家（MoE）开源权重模型，专为编码、推理和智能体工作负载设计。模型在 23.8 万亿 token 的多样化预训练数据（涵盖网页和专有授权数据集）上进行预训练，并结合强化学习（RL）优化能力。在

#### 背景

稀疏混合专家（Mixture-of-Experts, MoE）是一种大规模语言模型架构，模型拥有大量总参数，但每次推理仅激活其中一部分（如 Beam 的 501B 总参数中仅 23B 被激活），从而兼顾模型容量与推理效率。开源权重模型指公开完整模型参数，允许社区自由下载、微调和使用，与仅开放 API 的闭源模型相对。

#### 社区讨论

社区在 Hacker News 上对 Beam 进行了积极讨论：用户 Ariarule 分享了 Beam 在

**标签**: `#open-source AI`, `#large language models`, `#sparse MoE`, `#model benchmarks`, `#AI infrastructure`

---

<a id="item-tech-news-3"></a>
### [高通获授权华为 LogicFolding 芯片技术专利](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech) ⭐️ 8.0/10

高通公司获得华为 LogicFolding 芯片架构的专利授权，标志着中国科技企业从技术引进方向输出方转变。

hackernews · 0xedb · 10月5日 07:46 · [社区讨论](https://news.ycombinator.com/item?id=49961861)

#### 事件概述

高通公司已与华为达成专利授权协议，获授 LogicFolding 芯片设计技术。该技术支持多层晶圆结构，通过层空间布线而非跨芯片布线来缩短信号传输距离，从而降低整体发热量。这一交易发生在美国将华为列入实体清单的背景下，引发关于合规性的讨论。华为从此前的西方技术采购方转变为技术提供方，被视为中国半导体产业技术输出的重要标志。

#### 技术背景

LogicFolding 是一种芯片架构设计技术，其核心思路是通过多层堆叠和层空间布线优化信号路径。传统芯片设计中，信号需在芯片平面内长距离传输，导致热量积累和性能损耗；而 LogicFolding 利用垂直方向的层间连接，显著缩短信号传播距离。该技术由华为研发团队开发，现已进入商业化授权阶段。

#### 社区讨论

技术社区对 LogicFolding 的设计思路表示认可，认为其巧妙利用垂直空间解决了散热与信号延迟问题。同时，多名用户关注华为处于美国实体清单下，高通与之达成此类协议是否存在合规风险。部分舆论将此交易与美国此前强调 5G 技术主导权的立场进行对比，质疑政策一致性。

**标签**: `#semiconductor`, `#chip design`, `#Huawei`, `#Qualcomm`, `#patent licensing`

---

<a id="item-tech-news-4"></a>
### [丹麦政府数据库遭入侵，800 万公民信息泄露](https://techcrunch.com/2026/10/05/hackers-steal-8-million-citizens-records-from-danish-government-database/) ⭐️ 8.0/10



rss · TechCrunch · 10月5日 14:58

#### 摘要

丹麦政府宣布其数据库遭黑客入侵，导致 800 万公民的个人记录泄露，包括姓名、地址和国家级身份证号。此次泄露的数据不仅涵盖在丹麦居住的公民，还包括居住在国外的丹麦人以及已故人员。该事件涉及敏感个人信息（PII）及国家颁发的身份标识，影响范围覆盖丹麦全国人口。

**标签**: `#cybersecurity`, `#data breach`, `#government`, `#privacy`, `#Denmark`

---

<a id="item-tech-news-5"></a>
### [Yandex Music Sona：单 Transformer 替代 15+ 推荐组件](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/SettingAccording8986 · 10月5日 10:07

#### 摘要

Yandex Music 的 Sona 是一个单一 Transformer 模型，在 A/B 测试中替代了原有由 15+ 个候选生成器、预排序和排序模型组成的生产推荐管道。该模型支持读取最长 8,192 条历史事件，通过名为 History Compression 的方法将推理成本降低约一半：将历史分为较旧的 6,144 条事件和最近的 2,048 条事件，两者通过交叉注意力交换信息，再经一层全历史自注意力后，仅对最近事件运行 7 层堆栈。在智能音箱上进行的 7 天 A/B 测试（每臂 15% 用户）显示，Sona 相比生产基线使活跃用户数提升 4.53%，总收听时长提升 6.30%，均在 p &lt; 0.01 水平上显著；但目录覆盖率低于现有生产方案，长期 A/B 测试正在进行中。

**标签**: `#Machine Learning`, `#Recommender Systems`, `#Transformers`, `#Large Language Models`, `#Production Engineering`

---