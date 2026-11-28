---
layout: default
title: "Horizon Summary: 2026-11-28 (EN)"
date: 2026-11-28
lang: en
---

> From 164 items, 2 important content pieces were selected

---

**Technology News**
1. [SemiAnalysis Benchmarks AWS Trainium3 Inference Against NVIDIA GB300](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenSec Discloses CVSS 9.8 Pre-Auth NFS Heap Overflow in Linux Kernel](#item-tech-news-2) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [SemiAnalysis Benchmarks AWS Trainium3 Inference Against NVIDIA GB300](https://newsletter.semianalysis.com/p/trainium3-inferencex) ⭐️ 8.0/10



rss · Semianalysis · Nov 27, 15:54

#### Summary

SemiAnalysis published a first-principles microarchitecture deep dive into AWS Trainium3&\#x27;s inference performance, benchmarking it head-to-head against NVIDIA GB300 across total cost of ownership \(TCO\), model FLOPs utilization \(MFU\), and memory bandwidth utilization \(MBU\). The analysis takes a physics-based architectural approach to evaluate Trainium3&\#x27;s inference throughput and latency, finding that Trainium3 achieves better performance-per-dollar TCO compared to GB300. The article introduces a benchmark suite called UBenchX and reports high MFU and MBU figures alongside low-latency inference results for Trainium3. It also includes a comparison labeled &\#x27;Alisa Liu vs Eileen Gu,&\#x27; which appears to reference two distinct configurations or benchmark scenarios within the analysis. For engineers and procurement teams building large-scale inference infrastructure, the piece positions Trainium3 as a competitive alternative to NVIDIA&\#x27;s dominant GPU ecosystem, with concrete architectural reasoning behind the TCO advantage.

#### Background

Trainium3 is AWS&\#x27;s third-generation in-house AI accelerator, built around eight NeuronCore-v4 cores and a tile-first microarchitecture designed specifically for ML workloads rather than repurposing general-purpose GPU compute for tensor operations. Its primary competitor in this comparison is the NVIDIA GB300 NVL72, a liquid-cooled rack-scale platform housing 72 Blackwell Ultra GPUs and 36 Grace CPUs in a single chassis. The article benchmarks the two on total cost of ownership \(TCO\), model FLOPs utilization \(MFU\), and memory bandwidth utilization \(MBU\)—metrics that capture how effectively a system converts its hardware resources into usable inference throughput at a given price point.

<details><summary>References</summary>
<ul>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium3.html">Trainium3 Architecture — AWS Neuron Documentation</a></li>
<li><a href="https://newsletter.semianalysis.com/p/trainium3-inferencex">AWS Challenger: Trainium3 Inference and Microarchitecture ...</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">Designed for AI Reasoning Performance ... | NVIDIA GB 300 NVL72</a></li>

</ul>
</details>

**Tags**: `#AWS Trainium3`, `#AI Hardware`, `#TCO Analysis`, `#Microarchitecture`, `#NVIDIA Competition`

---

<a id="item-tech-news-2"></a>
### [OpenSec Discloses CVSS 9.8 Pre-Auth NFS Heap Overflow in Linux Kernel](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 8.0/10



telegram · zaihuapd · Nov 27, 12:57

#### Summary

OpenSec disclosed CVE-2026-99362, a pre-authentication heap overflow in the Linux kernel NFS server \(nfsd\) rated CVSS 9.8, which allows an unauthenticated attacker to obtain a root shell with a single connection to TCP port 2049. The out-of-bounds write on the kernel heap has existed since Linux 3.16, released in 2014, and affects any host running NFSv4.1 or NFSv4.2, including file servers, NAS appliances, and cluster storage nodes. Fixes were published in kernel releases 6.12.117, 6.18.61, 7.3.2, and 7.4-rc1; applying the update requires a reboot. Organizations unable to patch immediately should restrict access to TCP 2049 via an application firewall as an interim mitigation. The CVE was made public on November 20, 2026.

#### Background

The Network File System \(NFS\) lets a client mount remote filesystems over the network; versions 4.1 and 4.2 added features such as parallel I/O and stateful connections. A &quot;pre-authentication&quot; vulnerability means the flaw is reachable before any credential is presented, so an unauthenticated remote host can trigger it simply by opening a connection to the NFS service port \(TCP 2049\). Because the bug lives in kernel-space nfsd code, a successful exploit grants the attacker root-level code execution on the affected host.

**Tags**: `#Linux kernel security`, `#NFS vulnerability`, `#pre-authentication exploit`, `#CVE-2026-99362`, `#heap overflow`

---