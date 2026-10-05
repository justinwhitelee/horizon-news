---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 138 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [用 Strata 在 RTX 4090 上运行 125B Qwen 3.8 Flash Next](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [用 Strata 在 RTX 4090 上运行 125B Qwen 3.8 Flash Next](https://github.com/Niko1221/Strata) ⭐️ 8.0/10



hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

#### 摘要

项目 Strata（GitHub: Niko1221/Strata）展示了在消费级 RTX 4090 硬件上运行 125B 参数的 Qwen 3.8 Flash Next 模型，作者使用 RTX 4090 + 128GB DDR5 + Ryzen 7950X3D 配置实现了约 124 tokens/秒的推理速度。该项目的技术意义在于突破了大模型必须依赖专业 GPU 集群的传统认知，证明了量化后的大参数模型可以在消费级设备上运行。社区讨论中，有用户分享了在 RTX 6000 Pro 上使用 ds4 q4 量化的性能数据（prefill 1,251 tok/s，decode 255 tok/s），并支持 4 路并发流。

#### 社区讨论

社区对低于 4-bit 量化的质量下降表示担忧，但有用户报告 4-bit 量化在编码任务上质量足够。Vision 基准测试显示，相同 GGUF 权重下 llama.cpp 的坐标预测中位误差为 46.5 像素，而 Strata 为 154.8 像素，差距显著。另有评论质疑 Strata 是否会经历初期的 hype 消退期。

**标签**: `#local inference`, `#quantization`, `#open source models`, `#consumer hardware`, `#performance benchmarking`

---