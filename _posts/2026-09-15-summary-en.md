---
layout: default
title: "Horizon Summary: 2026-09-15 (EN)"
date: 2026-09-15
lang: en
---

> From 196 items, 3 important content pieces were selected

---

**Technology News**
1. [NVIDIA Vera Rubin NVL72 Claims 67x Performance Per Dollar for Agentic Inference](#item-tech-news-1) ⭐️ 8.0/10
2. [Semianalysis Compares Jetson Thor Edge vs B300 Cloud Inference TCO](#item-tech-news-2) ⭐️ 8.0/10
3. [Apple releases iOS 27 and macOS Golden Gate 27 with Siri AI and Liquid Glass updates](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [NVIDIA Vera Rubin NVL72 Claims 67x Performance Per Dollar for Agentic Inference](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 8.0/10



rss · Semianalysis · Sep 14, 22:08

#### Summary

SemiAnalysis reports that NVIDIA&\#x27;s Vera Rubin NVL72 platform claims 67x better performance per dollar for agentic inference workloads compared to prior generations. The analysis examines profit-per-watt metrics and highlights NVIDIA&\#x27;s co-design strategy, suggesting that higher-volume purchases yield greater returns. Additional themes from the coverage include AgentX and InferenceX workloads and what the author characterizes as conservative performance positioning by Jensen Huang.

#### Background

NVIDIA&\#x27;s NVL72 is a rack-scale GPU architecture that connects 72 GPUs via NVLink for high-throughput inference workloads. Agentic AI refers to autonomous AI systems that perform multi-step reasoning and tool use, such as coding agents, which demand sustained token throughput rather than single-prompt latency. TRTLLM \(TensorRT-LLM\) is NVIDIA&\#x27;s open-source inference optimization framework, and NVFP4 is a 4-bit floating-point quantization format that reduces memory bandwidth requirements while preserving accuracy for dense models.

**Tags**: `#NVIDIA`, `#AI inference`, `#hardware`, `#agentic AI`, `#GPU infrastructure`

---

<a id="item-tech-news-2"></a>
### [Semianalysis Compares Jetson Thor Edge vs B300 Cloud Inference TCO](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 8.0/10



rss · Semianalysis · Sep 14, 16:37

#### Summary

Semianalysis author Ivan Chiam examines whether large AI models should run on edge devices such as Nvidia&\#x27;s Jetson Thor or remain in datacenters using B300 accelerators, evaluating total cost of ownership across deployment scenarios. The analysis highlights silicon efficiency tradeoffs between onboard compute constrained by power and thermal limits and cloud flexibility limited by the so-called &quot;network wall&quot; — the bandwidth and latency costs of shuttling data to centralized GPUs. Concrete TCO figures and deployment conditions are presented to help AI engineers and infrastructure teams decide where inference should live as model sizes continue to outpace mobile compute capabilities.

#### Background

The NVIDIA Jetson Thor is a next-generation edge AI platform unveiled in early January 2026, delivering 2070 FP4 TFLOPS of AI performance with 128 GB of memory and 40–130 W power consumption. It introduces native FP4 quantization support via a next-generation Transformer Engine and offers 7.5× the AI performance and 3.5× the efficiency of its predecessor, the Jetson AGX Orin. The platform is designed for physical robotics workloads, including vision-language-action models like Isaac GR00T N1.5, and runs on JetPack 7.0 with CUDA 13.0 support. This edge hardware stands in contrast to datacenter GPUs like NVIDIA&\#x27;s B300, which prioritize raw throughput and flexibility over the power efficiency and latency advantages required for real-time onboard inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/">Jetson Thor | Advanced AI for Physical Robotics | NVIDIA</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/">Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI | NVIDIA Technical Blog</a></li>
<li><a href="https://www.rs-online.com/designspark/what-is-nvidia-jetson-thor">What is NVIDIA Jetson Thor?</a></li>

</ul>
</details>

**Tags**: `#AI Infrastructure`, `#Edge Computing`, `#Model Deployment`, `#TCO Analysis`, `#On-Device Inference`

---

<a id="item-tech-news-3"></a>
### [Apple releases iOS 27 and macOS Golden Gate 27 with Siri AI and Liquid Glass updates](https://arstechnica.com/apple/2026/09/apple-releases-ios-27-macos-golden-gate-27-with-siri-ai-and-liquid-glass-refinements/) ⭐️ 8.0/10



rss · Ars Technica · Sep 14, 19:28

#### Summary

Apple has released iOS 27 and macOS Golden Gate 27, both featuring a redesigned Siri with deeper AI integration and refinements to the Liquid Glass design language. iOS 27 rolls out on September 14 \(local time\), arriving in China around September 15, and supports iPhone 11 and later—though some AI features are limited to newer models. Notable additions include the ability for two iPhones to share the same phone number, pausing Find My location sharing with specific contacts, and watching videos through CarPlay while parked. macOS Golden Gate 27 is also significant as the final macOS version to support Rosetta for running Intel-based apps, marking the end of Apple&\#x27;s cross-architecture compatibility layer.

**Tags**: `#Apple`, `#Operating Systems`, `#AI`, `#Software Releases`, `#Developer Impact`

---