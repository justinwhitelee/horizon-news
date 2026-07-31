---
layout: default
title: "Horizon Summary: 2026-07-31 (ZH)"
date: 2026-07-31
lang: zh
---

> 从 196 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [Kimi K3 三大工程创新解析：Delta Attention、量化平衡与微虚拟机 RL 训练](#item-tech-news-1) ⭐️ 8.0/10
2. [华为开源 505B 参数 MoE 大模型 openPangu-2.0-Pro](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Kimi K3 三大工程创新解析：Delta Attention、量化平衡与微虚拟机 RL 训练](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 8.0/10



reddit · r/MachineLearning · /u/noninertialframe96 · 7月30日 16:37

#### 摘要

Moonshot 的开源权重模型 Kimi K3 在 Artificial Analysis 的 580 个模型中排名第四，仅次于 Claude Opus 5、Fable 5 和 GPT-5.6 Sol。其 47 页技术报告披露了三项关键工程创新：一是 Kimi Delta Attention，用每个头一个 128×128 矩阵替换 93 层中的 69 层的 KV 缓存，使 100 万 token 上下文内存占用从 104.6 GiB 降至 27.2 GiB；二是 Quantile Balancing，在每层 896 个专家的场景下直接基于单批次路由器分数边际计算偏置，解决了 DeepSeek-V3 固定步长偏置调整在该规模下失效的问题；三是 AgentENV，基于 Firecracker 的微虚拟机运行时，已创建 5100 万个沙箱，支持 133 毫秒检查点和 49 毫秒恢复，使轨迹在模型推理期间可零成本暂停。

**标签**: `#AI models`, `#machine learning systems`, `#MoE architectures`, `#long-context inference`, `#RL training infrastructure`

---

<a id="item-tech-news-2"></a>
### [华为开源 505B 参数 MoE 大模型 openPangu-2.0-Pro](https://huggingface.co/openpangu/openPangu-2.0-Pro) ⭐️ 8.0/10



telegram · zaihuapd · 7月31日 06:50

#### 摘要

华为近日在 Hugging Face 开源了基于昇腾 NPU 训练的混合专家（MoE）大模型 openPangu-2.0-Pro，总参数约 505B，每 token 激活约 18B，支持 512k 上下文长度，训练数据约 34T tokens。该模型采用 MLA 注意力机制与 DSA+SWA 独立分层混合架构，并集成 3 头 MTP 自投机模块，后训练阶段完成快慢合一微调与多专项强化学习。其 Thinking 版本在 AIME 2026 数学测评中取得 95.4 分，GPQA-Diamond 得分为 87.9，展现出较强的数学推理能力。

**标签**: `#AI`, `#Large Language Models`, `#Open Source`, `#Machine Learning`, `#Chinese Tech`

---