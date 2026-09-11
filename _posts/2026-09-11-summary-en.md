---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 198 items, 3 important content pieces were selected

---

**Technology News**
1. [Microsoft designates Rust as tier-1 language](#item-tech-news-1) ⭐️ 8.0/10
2. [WebAssembly VM in browser runs any Nix package interactively](#item-tech-news-2) ⭐️ 8.0/10
3. [Calif Research demos zero-click WeChat worm built with AI](#item-tech-news-3) ⭐️ 8.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Microsoft designates Rust as tier-1 language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10



hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

#### Summary

Microsoft has elevated Rust to a tier-1 language, signaling a major institutional commitment to the systems programming language. The company has publicly stated a goal of converting up to 1 billion lines of code to Rust by 2030, leveraging automated tooling to enable large-scale migration. This move is expected to improve security across Microsoft&\#x27;s product portfolio, as approximately 70% of CVEs in their software stem from memory-safety issues. The announcement also opens the door for deeper MSVC toolchain integration and positions Rust alongside C and C++ as a supported language for greenfield development at one of the world&\#x27;s largest software vendors.

#### Background

Tier-1 status at Microsoft means a language receives first-class support in tooling, documentation, and engineering investment, typically including IDE integration, compiler support, and official guidance. Rust has grown steadily since its 1.0 release, and Microsoft previously contributed the MLIR-based Rust frontend, MlirRust, to the Rust compiler ecosystem.

#### Community Discussion

Commenters highlighted Microsoft&\#x27;s ambitious goal of rewriting 1 billion lines of code by 2030 using automated C-to-Rust conversion, with some referencing DARPA-funded efforts exploring multiple approaches to automate such migrations. Others noted that this announcement reinforces Rust&\#x27;s maturity relative to newer competitors like Zig and Odin, and expressed optimism that deeper MSVC integration would follow. A few commenters observed that strong native UI support across platforms, including WebAssembly, remains a remaining gap for full-stack Rust adoption.

**Tags**: `#systems programming`, `#industry announcement`, `#programming languages`, `#enterprise adoption`, `#Rust`

---

<a id="item-tech-news-2"></a>
### [WebAssembly VM in browser runs any Nix package interactively](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10



rss · Simon Willison · Sep 10, 23:44

#### Summary

trynix.dev provides an x86\_64 Linux virtual machine running entirely in the browser via qemu-wasm, capable of booting any Nix package from the past 13 years. Each package is addressable through a unique URL, allowing users to launch an interactive shell and explore reproducible environments without local setup. The tool has been extended with a GitHub action called trynix-preview, which posts a review link on pull requests so reviewers can boot and inspect PR builds directly in their browsers. This approach eliminates server infrastructure requirements and makes package testing and code review more accessible.

#### Background

Nix is a functional package manager that enables reproducible software environments by treating packages as immutable values. WebAssembly \(Wasm\) is a binary instruction format that allows compiled code to run in web browsers at near-native speed, and projects like qemu-wasm have made it possible to virtualize full operating systems within this sandboxed runtime.

**Tags**: `#WebAssembly`, `#Nix`, `#virtualization`, `#developer tooling`, `#open source`

---

<a id="item-tech-news-3"></a>
### [Calif Research demos zero-click WeChat worm built with AI](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10



rss · Simon Willison · Sep 10, 00:56

#### Summary

Calif Research released a demo of WeWorm, the first zero-click worm capable of spreading through WeChat calls on both iOS and Android. The exploit requires no interaction from the victim—even an answered call plays no sound and still triggers successful execution. Working with AI, the team discovered the underlying bug and built the first remote code execution \(RCE\) exploit in approximately two days, then spent one additional week assembling the full worm. A worm at this scale previously required a larger team and several months of effort; here, AI performed most of the technical work while the human team provided judgment on targeting and safe testing.

**Tags**: `#AI security`, `#zero-click exploit`, `#mobile security`, `#research`

---