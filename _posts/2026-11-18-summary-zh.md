---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 204 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [英伟达宣布不接受黄仁勋重返 CEO 职位](#item-tech-news-1) ⭐️ 10.0/10
2. [Java4Shell：OpenJDK Base64 处理中存在远程代码执行漏洞](#item-tech-news-2) ⭐️ 9.0/10
3. [Ole Rømer 测得光速有限性——350 周年纪念](#item-tech-news-3) ⭐️ 9.0/10
4. [Google AI 答案使搜索流量下降 40%](#item-tech-news-4) ⭐️ 8.0/10
5. [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](#item-tech-news-5) ⭐️ 8.0/10
6. [NVIDIA ceases Singapore sales disclosure amid $104B subsidy revenue and US probe](#item-tech-news-6) ⭐️ 8.0/10
7. [Datasette Lite 重写：全浏览器运行 Datasette](#item-tech-news-7) ⭐️ 8.0/10
8. [Nvidia is abandoning China after Jensen Huang’s ouster](#item-tech-news-8) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [英伟达宣布不接受黄仁勋重返 CEO 职位](https://www.theverge.com/report/1035465/nvidia-says-it-will-not-reinstate-jensen-huang-as-ceo) ⭐️ 10.0/10



rss · The Verge · 11月17日 22:05

#### 摘要

在英伟达周二季度财报电话会上，新任董事会主席哈维·琼斯（Harvey Jones）宣布，董事会已一致接受前 CEO 黄仁勋的辞职，且无意将其 reinstatement。琼斯明确表示，本次电话会不受理关于黄仁勋辞职原因的提问。此前据报道，黄仁勋曾在上周辞职后提出重返 CEO 职位的请求，但此次董事会正式拒绝了这一请求。

#### 背景

Jensen Huang 为英伟达联合创始人暨前首席执行官，该公司为全球领先的 AI 芯片与图形处理器制造商。他于近期自愿辞去 CEO 一职，并在辞职后提出复职请求，但董事会已明确拒绝。此决定得到一份拥有逾 18 万签名的在线请愿书的支持，反映出公众对其领导的认可。英伟达的领导层更迭可能对人工智能硬件市场及公司未来方向产生重要影响。

#### 社区讨论

目前暂无可用社区评论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cbsnews.com/news/jensen-huang-nvidia-ceo-reinstatement-petition/">Nvidia&#x27;s board of directors is against bringing back Jensen ...</a></li>
<li><a href="https://www.reuters.com/legal/transactional/nvidia-board-says-it-does-not-intend-reinstate-jensen-huang-ceo-2026-11-17/">Nvidia board says it does not intend to reinstate Jensen ...</a></li>
<li><a href="https://apnews.com/article/nvidia-jensen-huang-china-national-security-chips-3026bcbe04ab57b844884382e583422a">Nvidia rejects Jensen Huang&#x27;s offer to return as CEO | AP News</a></li>

</ul>
</details>

**标签**: `#corporate leadership`, `#AI hardware`, `#NVIDIA`, `#industry announcement`, `#executive transition`

---

<a id="item-tech-news-2"></a>
### [Java4Shell：OpenJDK Base64 处理中存在远程代码执行漏洞](https://calif.io/java4shell/) ⭐️ 9.0/10

加利福尼亚网络安全创新中心披露了 OpenJDK Base64 解码中的远程代码执行漏洞（Java4Shell），攻击者可利用该漏洞在运行 HotSpot 虚拟机的系统中实现远程代码执行。

hackernews · werrett · 11月17日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=50538240)

#### 摘要

加利福尼亚网络安全创新中心（Calif）披露了一项名为 Java4Shell 的远程代码执行漏洞，存在于 OpenJDK 的 Base64 处理逻辑中，影响所有基于 HotSpot 的 JVM（包括 OpenJDK、Oracle JDK 和 GraalVM）。该漏洞利用了一种复杂的技术路径，涉及远程堆 groom（heap grooming），即通过精心构造的网络流量在网络环境中实现对内存布局的精细操控，最终触发恶意代码执行。这一漏洞的实际可利用性已在跨公网的生产环境条件下得到验证，意味着攻击门槛相比传统本地堆利用显著降低。鉴于 Java 在企业基础设施中的广泛部署，受影响系统数量庞大，立即检测与修复尤为关键。

#### 背景

Java4Shell（CVE-2026-114938）是 OpenJDK 17 中 Base64 解码器的一项严重远程代码执行漏洞，CVSS v4.0 评分为 9.2。漏洞位于 JVM 使用 AVX-512 指令集优化的 Base64 汇编实现中：攻击者只需发送精心构造的恶意 Base64 数据即可触发堆内存损坏，从而绕过正常权限控制实现 RCE。该漏洞仅影响 HotSpot 虚拟机（包括 OpenJDK、Oracle JDK、GraalVM），OpenJ9 等替代 VM 不受波及。目前临时缓解方案包括使用 \`-XX:UseAVX=2\` 标志禁用 AVX-512 扩展，同时 Semgrep 已发布免费检测脚本供企业扫描受影响实例。

#### 社区讨论

Semgrep 团队已发布免费的漏洞检测脚本，用于识别受影响的五类条件，特别指出仅 HotSpot VM 存在此漏洞，而 OpenJ9、GCJ 及 Azul Prime（Zing）不受影响。社区观察到该漏洞疑似与 AVX512 实现的 Base64 解码相关，可通过设置\`-XX:UseAVX=2\`标志临时规避；同时也有观点认为短期内将有恶意行为者利用此漏洞攻击关键基础设施。

**标签**: `#Java security`, `#RCE vulnerability`, `#OpenJDK`, `#Heap exploitation`, `#Critical CVE`

---

<a id="item-tech-news-3"></a>
### [Ole Rømer 测得光速有限性——350 周年纪念](https://www.sciencenorway.no/culture-history-history-of-science/350-years-ago-this-man-discovered-that-light-has-a-finite-speed/2737969) ⭐️ 9.0/10

今年纪念丹麦天文学家奥勒·罗默在 1676 年首次证明光以有限速度传播的 350 周年。这一发现被视为物理学史上的重大范式转移。

hackernews · dxs · 11月17日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=50536813)

#### 罗默测光速：三百年五十年纪念

《科学挪威》发文纪念丹麦天文学家奥勒·罗默（Ole Rømer）于 1676 年首次证明光具有有限传播速度的发现，距今已整整 350 年。该成果被分析视为物理学与天文学历史上的重大范式转移之一，彻底改变了人类对宇宙基本常数的认知。Hacker News 社区对此文进行了积极讨论，读者分享了相关科普漫画、解释视频以及格雷格·伊根（Greg Egan）探讨光速可变性的科幻小说系列。有评论者提出技术性问题，询问当时钟表的精度是否足以可靠测量食现象的时间差异，反映出公众对该历史实验机制的持续兴趣与好奇。

#### 社区讨论

HN 评论区未出现明显争议或共识分歧，主要表现为读者分享延伸资源（原创漫画、YouTube 科普视频、科幻小说推荐）和提出理解性问题。部分读者对罗默实验所用的计时精度表示惊讶，显示出对历史科学方法的技术好奇心；另有读者以脑筋急转弯互动，延续了科普讨论的趣味性。

**标签**: `#physics`, `#history-of-science`, `#astronomy`, `#paradigm-shift`, `#light-speed`

---

<a id="item-tech-news-4"></a>
### [Google AI 答案使搜索流量下降 40%](https://revscope.co/blog/search-seo-geo-2026/) ⭐️ 8.0/10



hackernews · slashdev · 11月18日 00:17 · [社区讨论](https://news.ycombinator.com/item?id=50540178)

#### 摘要

Google 的 AI 生成答案正在导致搜索推荐流量下降约 40%，引发行业对开放网络未来的担忧。这一趋势与所谓的&quot;Google Zero&quot;现象密切相关，即用户越来越无需点击任何搜索结果即可直接获得答案。分析认为，搜索引擎 SEO 模式已受到根本性冲击，传统搜索与直接的 LLM 答案平台之间的共存前景仍不明朗。

#### 背景

过去十余年，SEO（搜索引擎优化）构成了内容发现和经济模型的核心基础设施。随着大语言模型（LLM）逐渐嵌入搜索体验，用户获取答案的路径从&quot;搜索→浏览多个页面&quot;转变为直接在结果页中完成问答，这从根本上削弱了网站从搜索引擎获得的流量来源。

#### 社区讨论

社区普遍认为这是结构性转变而非短期波动。部分用户指出，直接提供答案本身就是更好的产品体验，同时怀念&quot;发现的乐趣&quot;正在消亡；也有评论质疑：如果搜索不再为网站导流，允许索引网站的意义何在，从而加速了&quot;开放网络&quot;的衰退。

**标签**: `#search\_engine`, `#AI`, `#SEO`, `#open\_web`, `#LLM`

---

<a id="item-tech-news-5"></a>
### [Quad9&\#x27;s withdrawal from France: A canary in the coal mine](https://blog.cloudflare.com/quad9-withdrawal-from-france/) ⭐️ 8.0/10

Quad9&\#x27;s withdrawal from France amid regulatory pressure on DNS blocking raises concerns about internet freedom, corporate complicity, and the rollback of European digital rights that emerged in the early 2000s.

hackernews · subset · 11月17日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=50538994)

**标签**: `#internet governance`, `#DNS policy`, `#digital rights`, `#corporate compliance`, `#European regulation`

---

<a id="item-tech-news-6"></a>
### [NVIDIA ceases Singapore sales disclosure amid $104B subsidy revenue and US probe](https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf) ⭐️ 8.0/10



hackernews · louiereederson · 11月17日 17:12 · [社区讨论](https://news.ycombinator.com/item?id=50534631)

#### Summary

NVIDIA has stopped disclosing its Singapore subsidiary&\#x27;s sales figures after Megaspeed, its Singapore entity, reported $104 billion in external revenue for 2025. The disclosure change comes as U.S. authorities investigate whether Megaspeed was used to route Nvidia GPUs to China in circumvention of export controls. Community discussion highlights that much of the $104B likely reflects orders routed through intermediary resellers rather than direct end-customer purchases, given NVIDIA&\#x27;s typical distribution model through OEMs and ODMs. Some commenters argue the story is primarily an accounting attribution question about how revenue is geographically recorded rather than evidence of where chips ultimately land, while others view it as confirmation of sanctions-evasion concerns.

#### Community Discussion

Commenters are divided on interpretation: some see the routed revenue and U.S. probe as consistent with sanctions-evading chip flows to China, while others stress that large intermediary throughput through Singapore is a normal part of NVIDIA&\#x27;s distribution architecture and does not itself prove end-use diversion. One commenter raised a practical observation that many AI developers never physically handle GPUs, since models are trained remotely in data centers, complicating assumptions about why China-based end users would need physical chip shipments.

**标签**: `#AI hardware`, `#semiconductors`, `#export controls`, `#corporate finance`, `#industry news`

---

<a id="item-tech-news-7"></a>
### [Datasette Lite 重写：全浏览器运行 Datasette](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison 发布了 Datasette Lite 的完整重写版本，现在可将整个 Datasette Python 应用直接在浏览器中运行。

rss · Simon Willison · 11月17日 16:48

#### 摘要

Simon Willison 发布了对 Datasette Lite 的完全重写，使用 Service Worker 和 Pyodide 在浏览器内直接运行完整的 Datasette Python Web 应用程序，几乎与服务器端版本无异。新版本支持通过精心构造的 URL 加载任意 SQLite 数据库、JSON 文件、CSV 文件或 SQL 脚本，可指定 Datasette 版本或 GitHub 仓库中的提交/标签/分支，并能从 PyPI 或 wheel 文件 URL 安装 100 多种 SQLite 版本和插件。该技术利用 WebAssembly 将 Python 运行时移植到客户端，使开发者无需部署完整服务器即可演示新功能或复现 bug，URL 地址的可复现性显著提升了协作效率。

**标签**: `#WebAssembly`, `#Python`, `#Web technology`, `#Open source tools`, `#Browser-based computing`

---

<a id="item-tech-news-8"></a>
### [Nvidia is abandoning China after Jensen Huang’s ouster](https://techcrunch.com/2026/11/17/nvidia-is-abandoning-china-after-jensen-huangs-ouster/) ⭐️ 8.0/10

Nvidia&\#x27;s interim CEO has reportedly ended chip sales to China, signaling a major strategic shift with implications for the AI hardware market.

rss · TechCrunch · 11月17日 23:37

**标签**: `#semiconductors`, `#AI hardware`, `#geopolitics`, `#Nvidia`, `#china trade`

---