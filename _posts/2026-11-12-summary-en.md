---
layout: default
title: "Horizon Summary: 2026-11-12 (EN)"
date: 2026-11-12
lang: en
---

> From 205 items, 2 important content pieces were selected

---

**Technology News**
1. [AWS releases open-source emulator built with AI agents](#item-tech-news-1) ⭐️ 8.0/10
2. [Voltage Glitching Unlocks Full HBM on Downgraded NVIDIA Mining Cards](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AWS releases open-source emulator built with AI agents](https://github.com/aws/aws-emulator) ⭐️ 8.0/10



hackernews · super\_linear · Nov 11, 18:21 · [Discussion](https://news.ycombinator.com/item?id=50456631)

#### Summary

AWS has released an open-source emulator at github.com/aws/aws-emulator for locally testing AWS services, built with the help of autonomous AI agents. The project generates active Hacker News discussion around its utility compared to existing alternatives like LocalStack and FakeCloud. A key differentiator is the use of agentic AI to cover AWS&\#x27;s extensive service catalog—a task that would be prohibitively expensive to do manually. However, AWS has documented significant security limitations: the emulator must not be used for testing IAM policies, resource-based policies, KMS key policies, cross-account or cross-region access, or other security controls.

#### Background

Local AWS emulators allow developers to test applications against simulated versions of AWS services without incurring cloud costs or needing live accounts. Tools like LocalStack and FakeCloud have long filled this niche, but building coverage across AWS&\#x27;s vast and rapidly evolving service catalog has been a steep engineering challenge. Autonomous AI agents—LLM-driven systems that can iteratively write, test, and refine code—have recently been applied to close that gap by generating implementation for many services at scale.

#### Community Discussion

Commenters expressed skepticism about whether this is a maintained product or merely an exercise, with some preferring alternatives like Floci and Testcontainers. Others were impressed by the feat of using agents to write code in a difficult language, calling it a sign of a new normal for developer tooling. Amazon employees praised the project&\#x27;s potential value for agentic development workflows, where mocked infrastructure inputs are critical.

**Tags**: `#cloud computing`, `#developer tools`, `#AWS`, `#AI agents`, `#open source`

---

<a id="item-tech-news-2"></a>
### [Voltage Glitching Unlocks Full HBM on Downgraded NVIDIA Mining Cards](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/) ⭐️ 8.0/10



hackernews · lae · Nov 11, 10:48 · [Discussion](https://news.ycombinator.com/item?id=50451903)

#### Summary

A technical blog post demonstrates using voltage glitching to permanently blow hardware fuses on downgraded NVIDIA CMP mining cards, unlocking the full 80 GB of HBM memory that was disabled in factory‑trimmed lower‑capacity versions. This technique turns otherwise cheaper mining‑specific GPUs into viable options for memory‑hungry machine learning workloads, directly addressing cost barriers in AI infrastructure. The method requires physically altering the GPU during operation, making it riskier than software‑based approaches that have shown limited success. Community discussion highlights concerns about whether fuses were intentionally blown due to manufacturing defects, as well as practical tips like using external PCIe risers to speed up the process.

#### Background

Voltage glitching involves momentarily disrupting the power supply to a chip to bypass security checks or trigger uncommitted circuit paths. NVIDIA’s Compute‑Only Platform \(CMP\) series are mining‑focused graphics cards that often ship with disabled memory regions; in this case, the 8 GB variant retains an underlying 80 GB HBM package that can be enabled by physically changing fuse states.

#### Community Discussion

Readers note the historical irony of disabling most high‑memory chips for mining, question whether fused‑off regions might stem from silicon defects rather than intentional trimming, and share that software‑only attempts remain unsuccessful for the 10 GB model. Several suggest practical improvements, such as isolating the target GPU on a separate PCIe riser with its own power supply so the host system can continue running during the glitching process.

**Tags**: `#GPU hardware`, `#reverse engineering`, `#AI infrastructure`, `#hardware hacking`, `#voltage glitching`

---