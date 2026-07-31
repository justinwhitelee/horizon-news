#!/usr/bin/env python3
"""Build static HTML site from Horizon daily Markdown summaries.

Reads data/summaries/horizon-*-zh.md, converts to HTML, and writes:
  dist/index.html        -> daily index (newest first)
  dist/<date>.html       -> each day's full Chinese summary

The dist/ folder is then uploaded to the serv00 web host via lftp in CI.
"""
from pathlib import Path
import re
import markdown

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "data" / "summaries"
DIST = ROOT / "dist"
DATE_RE = re.compile(r"horizon-(\d{4}-\d{2}-\d{2})-zh\.md$")

CSS = """
:root { --fg:#1a1a1a; --muted:#666; --line:#eaeaea; --accent:#2563eb; }
* { box-sizing: border-box; }
body { margin:0; background:#fff; color:var(--fg);
  font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }
.wrap { max-width:820px; margin:0 auto; padding:32px 20px 64px; }
header { border-bottom:1px solid var(--line); padding-bottom:12px; margin-bottom:24px; }
header a { color:var(--accent); text-decoration:none; font-size:14px; }
h1 { font-size:24px; margin:0 0 4px; }
h2 { font-size:20px; margin:28px 0 8px; }
h3 { font-size:17px; margin:20px 0 6px; }
.sub { color:var(--muted); font-size:14px; margin:0 0 24px; }
ul.list { list-style:none; padding:0; }
ul.list li { padding:10px 0; border-bottom:1px solid var(--line); }
ul.list .date { color:var(--muted); font-size:13px; margin-right:10px; }
ul.list a { color:var(--accent); text-decoration:none; }
article { font-size:16px; }
article a { color:var(--accent); }
blockquote { border-left:3px solid var(--line); margin:16px 0; padding:4px 16px; color:var(--muted); }
code { background:#f5f5f5; padding:2px 5px; border-radius:4px; font-size:14px; }
pre { background:#f5f5f5; padding:14px; border-radius:8px; overflow:auto; }
table { border-collapse:collapse; width:100%; margin:16px 0; }
th,td { border:1px solid var(--line); padding:8px 10px; text-align:left; }
footer { color:var(--muted); font-size:13px; margin-top:40px; border-top:1px solid var(--line); padding-top:16px; }
"""


def strip_front_matter(md_text: str) -> str:
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    return md_text


def convert(md_text: str) -> str:
    return markdown.markdown(
        strip_front_matter(md_text),
        extensions=["extra", "tables", "fenced_code"],
    )


def extract_title(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def page_html(date: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Horizon 每日科技新闻 · {date}</title><style>{CSS}</style></head>
<body><div class="wrap">
<header><a href="index.html">&larr; Horizon 每日科技新闻</a></header>
<h1>{date} 每日科技新闻</h1>
<article>{body}</article>
<footer>由 Horizon AI 聚合生成 · 新闻原始来源见各条目链接</footer>
</div></body></html>"""


def index_html(entries):
    items = "\n".join(
        f'<li><span class="date">{d}</span><a href="{href}">{title}</a></li>'
        for d, title, href, _ in entries
    )
    return f"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Horizon 每日科技新闻</title><style>{CSS}</style></head>
<body><div class="wrap">
<header><h1>Horizon 每日科技新闻</h1></header>
<p class="sub">AI 聚合 · 科技动态 + 全球热点</p>
<ul class="list">{items}</ul>
<footer>由 Horizon AI 聚合生成</footer>
</div></body></html>"""


def main():
    DIST.mkdir(exist_ok=True)
    entries = []
    for f in sorted(SUMMARIES.glob("horizon-*-zh.md"), reverse=True):
        m = DATE_RE.search(f.name)
        if not m:
            continue
        date = m.group(1)
        text = f.read_text(encoding="utf-8")
        body = convert(text)
        (DIST / f"{date}.html").write_text(page_html(date, body), encoding="utf-8")
        entries.append((date, extract_title(text) or date, f"{date}.html", ""))
    (DIST / "index.html").write_text(index_html(entries), encoding="utf-8")
    print(f"Built {len(entries)} daily pages -> {DIST}")


if __name__ == "__main__":
    main()
