#!/usr/bin/env python3
"""Build static HTML site from Horizon daily Markdown summaries (科技仙岛).

Reads data/summaries/horizon-*-zh.md, parses each item into a structured card,
and writes:
  dist/index.html       -> daily index (newest first), with stats & previews
  dist/<date>.html      -> each day's full Chinese summary, card-based layout
  dist/kjxd-logo.png    -> brand logo (copied from assets/)

The dist/ folder is then uploaded to the serv00 web host (https://dao.serv00.net/horizon/)
via lftp in CI, and cross-linked from the main site's nav (mf-shell.js).
"""
from pathlib import Path
import re
import shutil
import markdown as md_lib

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "data" / "summaries"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"
DATE_RE = re.compile(r"horizon-(\d{4}-\d{2}-\d{2})-zh\.md$")
ITEM_RE = re.compile(
    r'<a id="(item-[^"]+)"></a>\s*###\s*\[([^\]]+)\]\(([^)]+)\)(?:\s*⭐️\s*([\d.]+)/10)?',
    re.MULTILINE,
)

# ─────────────── CSS（科技仙岛品牌色：深蓝 + 电青 + 金） ───────────────
CSS = """
:root {
  --bg: #f7f9fc;
  --fg: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --card: #ffffff;
  --brand: #0b1f3a;
  --brand-2: #06b6d4;
  --accent: #f59e0b;
  --tag-bg: #ecfeff;
  --tag-fg: #0e7490;
  --score-bg: linear-gradient(135deg,#06b6d4,#0ea5e9);
}
* { box-sizing: border-box; }
html,body { margin:0; padding:0; }
body {
  background: var(--bg);
  color: var(--fg);
  font: 16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 880px; margin: 0 auto; padding: 0 20px 64px; }

/* ── 频道横幅（位于站点统一外壳下方，标识「科技仙岛」频道） ── */
.kjxd-banner {
  display:flex; align-items:center; gap:16px; margin:22px 0 6px;
  padding:18px 20px; background:#fff; border:1px solid var(--line);
  border-radius:14px; box-shadow:0 1px 3px rgba(15,23,42,.04);
}
.kjxd-banner-logo { width:56px; height:56px; border-radius:12px; box-shadow:0 4px 14px rgba(6,182,212,.22); }
.kjxd-banner-title { font-size:22px; font-weight:800; color:var(--brand); letter-spacing:.3px; }
.kjxd-banner-sub { font-size:13px; color:var(--muted); margin-top:3px; }

/* ── Hero (date page) ── */
.hero { padding: 28px 0 16px; }
.hero .date { font-size:14px; color: var(--brand-2); font-weight:600; letter-spacing:1px; text-transform:uppercase; }
.hero h1 { font-size:30px; margin:6px 0 10px; color: var(--brand); font-weight:800; }
.hero .stats { display:flex; gap:20px; color: var(--muted); font-size:14px; flex-wrap:wrap; }
.hero .stats span strong { color: var(--fg); font-size:18px; font-weight:700; }

/* ── Cards ── */
.cards { display:flex; flex-direction:column; gap:16px; margin-top: 18px; }
.card {
  background: var(--card); border-radius:14px; padding:22px 24px;
  box-shadow: 0 1px 3px rgba(15,23,42,.04), 0 8px 24px rgba(15,23,42,.05);
  border:1px solid var(--line); transition: transform .15s, box-shadow .15s;
}
.card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(15,23,42,.06), 0 16px 32px rgba(15,23,42,.08); }
.card-head { display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:10px; }
.source-badge {
  display:inline-block; font-size:12px; font-weight:600; color: var(--brand);
  background: #e0f2fe; padding:3px 10px; border-radius:999px;
}
.score {
  display:inline-flex; align-items:center; gap:4px;
  background: var(--score-bg); color:#fff; font-size:12px; font-weight:700;
  padding:3px 10px; border-radius:999px;
}
.card h2 { font-size:19px; line-height:1.45; margin: 4px 0 10px; }
.card h2 a { color: var(--brand); text-decoration:none; }
.card h2 a:hover { color: var(--brand-2); }
.card .meta-line { font-size:13px; color: var(--muted); margin-bottom:10px; }
.card .summary {
  font-size:15.5px; line-height:1.75; color:#334155;
  background:#f8fafc; border-left:3px solid var(--brand-2);
  padding:12px 16px; border-radius:0 8px 8px 0; margin:12px 0;
}
.card .summary p:first-child { margin-top:0; }
.card .summary p:last-child { margin-bottom:0; }
.card .tags { display:flex; flex-wrap:wrap; gap:6px; margin-top:10px; }
.card .tag {
  font-size:12px; color: var(--tag-fg); background: var(--tag-bg);
  padding:2px 10px; border-radius:999px; font-weight:500;
}
.card .actions { margin-top:14px; }
.card .actions a {
  display:inline-block; font-size:13px; font-weight:600;
  color: var(--brand); background:#f1f5f9; padding:6px 14px;
  border-radius:8px; text-decoration:none; transition:.2s;
}
.card .actions a:hover { background: var(--brand); color:#fff; }

/* ── Index page cards ── */
.idx-card {
  background:#fff; border-radius:14px; padding:20px 24px; margin-bottom:14px;
  border:1px solid var(--line); box-shadow:0 1px 3px rgba(15,23,42,.04);
  display:flex; gap:20px; align-items:flex-start; transition:.15s;
}
.idx-card:hover { transform:translateY(-1px); box-shadow:0 6px 18px rgba(15,23,42,.06); }
.idx-card .date-pill {
  flex:0 0 90px; background: linear-gradient(135deg,var(--brand),var(--brand-2));
  color:#fff; border-radius:10px; padding:10px; text-align:center;
}
.idx-card .date-pill .d { font-size:22px; font-weight:800; line-height:1; }
.idx-card .date-pill .m { font-size:11px; opacity:.85; margin-top:4px; }
.idx-card .body { flex:1; min-width:0; }
.idx-card h3 { margin:0 0 8px; font-size:18px; }
.idx-card h3 a { color:var(--brand); text-decoration:none; }
.idx-card h3 a:hover { color:var(--brand-2); }
.idx-card .preview { color:var(--muted); font-size:14px; line-height:1.6; }
.idx-card .meta-line { font-size:12px; color:var(--muted); margin-top:6px; }
@media (max-width:560px){
  .idx-card { flex-direction:column; }
  .idx-card .date-pill { flex:none; align-self:flex-start; }
}

/* 页脚由全站统一外壳 mf-shell.js 注入，本页不再自带 footer */

/* ── Markdown body fallback ── */
article.body-md h2 { font-size:20px; margin-top:28px; color: var(--brand); }
article.body-md h3 { font-size:17px; margin-top:20px; }
article.body-md blockquote { border-left:3px solid var(--brand-2); margin:16px 0; padding:6px 16px; color: var(--muted); }
article.body-md code { background:#f1f5f9; padding:2px 6px; border-radius:4px; font-size:13px; }
article.body-md details { margin:10px 0; }
article.body-md details summary { cursor:pointer; color:var(--brand-2); font-weight:600; }
"""

# 全站统一外壳（站点导航 + 页脚）由 /assets/mf-shell.js 注入：
#   <script src="/assets/mf-shell.js" data-mode="app" defer></script>
# 该外壳已内置「🚀 科技仙岛」频道入口，故本页只需提供频道横幅与内容。
SHELL_JS = '<script src="/assets/mf-shell.js" data-mode="app" defer></script>'

def strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    return text

def render_md(text: str) -> str:
    return md_lib.markdown(text or "", extensions=["extra", "tables", "fenced_code", "sane_lists"])

def parse_meta(meta_line: str):
    """Parse the meta line e.g. 'hackernews · r/LocalLLaMA · dnhkng · 7月31日 06:08 · [社区讨论](url)'"""
    parts = [p.strip() for p in re.split(r"\s*·\s*", meta_line) if p.strip()]
    src = parts[0] if parts else ""
    sub = parts[1] if len(parts) > 1 else ""
    author = parts[2] if len(parts) > 2 else ""
    when = parts[3] if len(parts) > 3 else ""
    discuss = ""
    m_disc = re.search(r"\[(.*?)\]\((.*?)\)", meta_line)
    if m_disc:
        discuss = m_disc.group(2)
    return {"src": src, "sub": sub, "author": author, "when": when, "discuss": discuss}

def parse_items(md_text: str):
    md = strip_front_matter(md_text)
    items = []
    matches = list(ITEM_RE.finditer(md))
    for i, m in enumerate(matches):
        anchor, title, url, score = m.group(1), m.group(2), m.group(3), m.group(4) or ""
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        body = md[start:end].strip()
        # meta = first non-empty, non-heading line
        meta = ""
        for line in body.splitlines():
            if line.strip() and not line.startswith("#"):
                meta = line.strip(); break
        # summary
        summary_html = ""
        m_sum = re.search(r"####\s*摘要\s*\n+(.*?)(?=\n####|\n<details|\n---|\Z)", body, re.DOTALL)
        if m_sum:
            summary_html = render_md(m_sum.group(1).strip())
        # tags
        tags = []
        m_tags = re.search(r"\*\*标签\*\*:\s*(.*?)(?:\n|$)", body)
        if m_tags:
            tags = re.findall(r"`#([^`]+)`", m_tags.group(1))
        items.append({
            "anchor": anchor, "title": title, "url": url, "score": score,
            "meta": parse_meta(meta), "summary_html": summary_html, "tags": tags,
        })
    return items

def total_items(md_text: str) -> int:
    """Count from intro line '从 N 条内容中筛选出 M 条重要资讯。'"""
    m = re.search(r"从\s*(\d+)\s*条", md_text)
    if m: return int(m.group(1))
    return 0

def selected_count(md_text: str) -> int:
    m = re.search(r"筛选出\s*(\d+)\s*条", md_text)
    if m: return int(m.group(1))
    return 0

def banner_html() -> str:
    """频道横幅：在站点统一外壳（mf-shell）下方标识「科技仙岛」频道。"""
    return (
        '<div class="kjxd-banner">'
        '<img src="kjxd-logo.png" alt="科技仙岛" class="kjxd-banner-logo" />'
        '<div><div class="kjxd-banner-title">科技仙岛 · Horizon</div>'
        '<div class="kjxd-banner-sub">全球科技与新闻 · 每日 AI 精选聚合</div></div>'
        '</div>'
    )

def card_html(item) -> str:
    meta = item["meta"]
    meta_parts = []
    if meta["src"]: meta_parts.append(meta["src"])
    if meta["sub"] and meta["sub"] != meta["src"]: meta_parts.append(meta["sub"])
    if meta["author"]: meta_parts.append("作者 " + meta["author"])
    if meta["when"]: meta_parts.append(meta["when"])
    meta_line = " · ".join(meta_parts)

    score_html = f'<span class="score">⭐ {item["score"]}/10</span>' if item["score"] else ""
    summary_html = f'<div class="summary">{item["summary_html"]}</div>' if item["summary_html"] else ""
    tags_html = "".join(f'<span class="tag">#{t}</span>' for t in item["tags"])

    return (
        f'<article class="card" id="{item["anchor"]}">'
        f'<div class="card-head">'
        f'<span class="source-badge">{meta["src"] or "Source"}</span>'
        f'{score_html}'
        f'</div>'
        f'<h2><a href="{item["url"]}" target="_blank" rel="noopener">{item["title"]}</a></h2>'
        f'<div class="meta-line">{meta_line}</div>'
        f'{summary_html}'
        + (f'<div class="tags">{tags_html}</div>' if tags_html else "")
        + '<div class="actions">'
        + f'<a href="{item["url"]}" target="_blank" rel="noopener">阅读原文 →</a>'
        + (f' <a href="{meta["discuss"]}" target="_blank" rel="noopener">社区讨论</a>' if meta["discuss"] else "")
        + '</div>'
        + '</article>'
    )

def date_page_html(date: str, md_text: str) -> str:
    items = parse_items(md_text)
    total = total_items(md_text)
    cards = "\n".join(card_html(it) for it in items)
    sources = sorted({it["meta"]["src"] for it in items if it["meta"]["src"]})
    hero_stats = (
        f'<div class="stats">'
        f'<span><strong>{len(items)}</strong> 条精选</span>'
        f'<span><strong>{len(sources)}</strong> 个来源</span>'
        + (f'<span>原始抓取 <strong>{total}</strong> 条</span>' if total else "")
        + '</div>'
    )
    return f"""<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>科技仙岛 · {date} 每日精选</title>
<meta name="description" content="科技仙岛 — Horizon AI 每日精选全球科技与新闻，{date} 共 {len(items)} 条。">
<style>{CSS}</style>
{SHELL_JS}
</head><body>
<main class="wrap">
  {banner_html()}
  <section class="hero">
    <div class="date">{date}</div>
    <h1>今日精选 · 全球科技与新闻</h1>
    {hero_stats}
  </section>
  <section class="cards">{cards}</section>
</main>
</body></html>"""

def index_page_html(entries) -> str:
    """entries: list of (date, items, total)"""
    total_days = len(entries)
    total_items = sum(len(e[1]) for e in entries)
    cards = []
    for date, items, total in entries:
        # date pill: month/day
        m, d = date.split("-")[1:]
        preview_titles = [it["title"] for it in items[:3]]
        preview_html = "".join(
            f'<div class="preview">· <a href="{date}.html#{it["anchor"]}" style="color:inherit;text-decoration:none">{it["title"][:42]}</a></div>'
            for it in items[:3]
        )
        cards.append(
            f'<div class="idx-card">'
            f'<div class="date-pill"><div class="d">{int(d)}</div><div class="m">{int(m)}月</div></div>'
            f'<div class="body">'
            f'<h3><a href="{date}.html">{date} · 每日精选</a></h3>'
            f'<div class="meta-line">{len(items)} 条 · 抓取 {total} 条原始数据</div>'
            f'{preview_html}'
            f'</div></div>'
        )
    cards_html = "\n".join(cards)
    return f"""<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>科技仙岛 · 每日全球科技与新闻 AI 聚合</title>
<meta name="description" content="科技仙岛 — Horizon AI 每日自动聚合全球科技动态与重要新闻，由 AI 摘要去噪，保留高价值信号。">
<style>{CSS}</style>
{SHELL_JS}
</head><body>
<main class="wrap">
  {banner_html()}
  <section class="hero">
    <div class="date">Horizon · Daily AI Digest</div>
    <h1>每日精选 · 全球科技与新闻</h1>
    <div class="stats">
      <span>已收录 <strong>{total_days}</strong> 天</span>
      <span>累计 <strong>{total_items}</strong> 条 AI 摘要</span>
    </div>
    <p style="color:var(--muted);font-size:14px;margin-top:12px;line-height:1.7">
      由 GitHub Actions 每日自动运行 Horizon 抓取 Hacker News / Reddit / 科技博客 / 全球新闻 RSS，
      经 AI 摘要去噪后发布于此。原始来源见各条目链接。
    </p>
  </section>
  <section>{cards_html}</section>
</main>
</body></html>"""

def copy_assets():
    """Copy brand assets (logo) into dist/ so they ship with the site."""
    DIST.mkdir(exist_ok=True)
    if ASSETS.exists():
        for f in ASSETS.glob("*.png"):
            shutil.copy2(f, DIST / f.name)
        for f in ASSETS.glob("*.svg"):
            shutil.copy2(f, DIST / f.name)

def main():
    DIST.mkdir(exist_ok=True)
    copy_assets()
    entries = []
    for f in sorted(SUMMARIES.glob("horizon-*-zh.md"), reverse=True):
        m = DATE_RE.search(f.name)
        if not m: continue
        date = m.group(1)
        text = f.read_text(encoding="utf-8")
        items = parse_items(text)
        (DIST / f"{date}.html").write_text(date_page_html(date, text), encoding="utf-8")
        entries.append((date, items, total_items(text)))
    (DIST / "index.html").write_text(index_page_html(entries), encoding="utf-8")
    print(f"Built {len(entries)} daily pages + index -> {DIST}")

if __name__ == "__main__":
    main()