#!/usr/bin/env python3
"""Export built Mintlify-flavored Markdown/MDX into a simple static site."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DOC_EXTENSIONS = {".md", ".mdx"}
SKIP_PARTS = {"snippets", "code-samples", "code-samples-generated"}


@dataclass(frozen=True)
class Page:
    source_path: Path
    rel_path: Path
    out_path: Path
    url: str
    title: str
    body_text: str


def strip_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, text[end + 5 :]


def title_from_markdown(frontmatter: dict[str, str], body: str, rel_path: Path) -> str:
    if frontmatter.get("title"):
        return frontmatter["title"]
    match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    if match:
        return re.sub(r"<[^>]+>", "", match.group(1)).strip()
    if rel_path.stem == "index":
        return rel_path.parent.name.replace("-", " ").title() or "Home"
    return rel_path.stem.replace("-", " ").replace("_", " ").title()


def html_path_for(rel_path: Path) -> Path:
    if rel_path.name in {"index.md", "index.mdx"}:
        return rel_path.with_suffix(".html")
    return rel_path.with_suffix(".html")


def url_for(out_path: Path) -> str:
    value = "/" + out_path.as_posix()
    if value.endswith("/index.html"):
        return value[: -len("index.html")]
    return value


def is_doc_page(path: Path, build_dir: Path) -> bool:
    if path.suffix.lower() not in DOC_EXTENSIONS:
        return False
    rel_parts = set(path.relative_to(build_dir).parts)
    return not rel_parts.intersection(SKIP_PARTS)


def load_nav_order(build_dir: Path) -> list[str]:
    docs_json = build_dir / "docs.json"
    if not docs_json.exists():
        return []
    try:
        data = json.loads(docs_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    order: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, str):
            order.append(value.strip("/"))
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            if "pages" in value:
                walk(value["pages"])
            for key in ("tabs", "groups", "anchors", "navigation"):
                if key in value:
                    walk(value[key])

    walk(data)
    return order


def sort_pages(pages: list[Page], build_dir: Path) -> list[Page]:
    nav_order = load_nav_order(build_dir)
    rank: dict[str, int] = {}
    for index, item in enumerate(nav_order):
        rank[item] = index
        rank[item + ".mdx"] = index
        rank[item + ".md"] = index
        rank[item + "/index"] = index
        rank[item + "/index.mdx"] = index
        rank[item + "/index.md"] = index

    def key(page: Page) -> tuple[int, str]:
        rel = page.rel_path.as_posix()
        stem = rel.rsplit(".", 1)[0]
        return (rank.get(rel, rank.get(stem, 1_000_000)), rel)

    return sorted(pages, key=key)


def rewrite_links(markdown_text: str, known_urls: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2)
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)

        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor

        normalized = target.strip("/")
        candidates = [
            normalized,
            normalized + ".mdx",
            normalized + ".md",
            normalized + "/index.mdx",
            normalized + "/index.md",
        ]
        for candidate in candidates:
            if candidate in known_urls:
                return f"[{label}]({known_urls[candidate]}{anchor})"

        if target.endswith((".md", ".mdx")):
            target = target.rsplit(".", 1)[0] + ".html"
        return f"[{label}]({target}{anchor})"

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace, markdown_text)


def mdx_to_markdown(text: str) -> str:
    frontmatter, body = strip_frontmatter(text)
    del frontmatter
    body = re.sub(r"(?s)\{/\*.*?\*/\}", "", body)
    body = re.sub(r"^\s*(import|export)\b.*$", "", body, flags=re.MULTILINE)

    replacements = {
        "Note": "提示",
        "Info": "信息",
        "Tip": "建议",
        "Warning": "警告",
        "Check": "检查",
        "Danger": "注意",
    }
    for tag, label in replacements.items():
        body = re.sub(
            rf"<{tag}[^>]*>",
            f'\n<div class="callout"><strong>{label}</strong>\n\n',
            body,
        )
        body = re.sub(rf"</{tag}>", "\n</div>\n", body)

    title_tags = {
        "Accordion": "###",
        "Card": "###",
        "Step": "###",
        "Tab": "####",
    }
    for tag, prefix in title_tags.items():
        body = re.sub(
            rf"<{tag}[^>]*(?:title|name)=[\"']([^\"']+)[\"'][^>]*>",
            rf"\n{prefix} \1\n\n",
            body,
        )
        body = re.sub(rf"</{tag}>", "\n", body)

    removable_tags = [
        "AccordionGroup",
        "CardGroup",
        "CodeGroup",
        "Columns",
        "Frame",
        "Snippet",
        "Steps",
        "Tabs",
    ]
    for tag in removable_tags:
        body = re.sub(rf"</?{tag}[^>]*>", "", body)

    body = re.sub(r"<([A-Z][A-Za-z0-9_.:-]*)(\s[^>]*)?/>", "", body)
    body = re.sub(r"</?([A-Z][A-Za-z0-9_.:-]*)(\s[^>]*)?>", "", body)
    return body


def render_markdown(markdown_text: str) -> str:
    try:
        import markdown  # type: ignore

        return markdown.markdown(
            markdown_text,
            extensions=[
                "abbr",
                "attr_list",
                "def_list",
                "fenced_code",
                "md_in_html",
                "tables",
                "toc",
            ],
            output_format="html5",
        )
    except ImportError:
        escaped = html.escape(markdown_text)
        escaped = re.sub(r"^# (.+)$", r"<h1>\1</h1>", escaped, flags=re.MULTILINE)
        escaped = re.sub(r"^## (.+)$", r"<h2>\1</h2>", escaped, flags=re.MULTILINE)
        return "<pre>" + escaped + "</pre>"


def plain_text(markdown_text: str) -> str:
    text = re.sub(r"```.*?```", "", markdown_text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[#*_`>\[\]()]|https?://\S+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def render_shell(page: Page, pages: list[Page], content_html: str, title: str) -> str:
    nav = "\n".join(
        f'<a class="nav-link{" active" if item.url == page.url else ""}" '
        f'href="{html.escape(item.url)}">{html.escape(item.title)}</a>'
        for item in pages
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(page.title)} - {html.escape(title)}</title>
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="/">{html.escape(title)}</a>
    <input id="search" class="search" type="search" placeholder="搜索文档">
  </header>
  <div class="layout">
    <aside class="sidebar">{nav}</aside>
    <main class="content">
      <article class="doc">{content_html}</article>
      <section id="results" class="results" hidden></section>
    </main>
  </div>
  <script src="/assets/site.js"></script>
</body>
</html>
"""


def site_css() -> str:
    return """
:root {
  color-scheme: light;
  --bg: #fbfaf7;
  --panel: #ffffff;
  --text: #202124;
  --muted: #667085;
  --line: #dedbd2;
  --accent: #087ea4;
  --accent-soft: #e7f6fb;
  --code: #f3f0e8;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.68;
}
.topbar {
  position: sticky;
  top: 0;
  z-index: 2;
  display: flex;
  gap: 16px;
  align-items: center;
  border-bottom: 1px solid var(--line);
  background: rgba(251, 250, 247, 0.96);
  padding: 12px 20px;
}
.brand {
  color: var(--text);
  font-weight: 700;
  text-decoration: none;
  white-space: nowrap;
}
.search {
  width: min(520px, 100%);
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--panel);
  color: var(--text);
  font-size: 14px;
  padding: 9px 11px;
}
.layout {
  display: grid;
  grid-template-columns: 280px minmax(0, 1fr);
  min-height: calc(100vh - 58px);
}
.sidebar {
  position: sticky;
  top: 58px;
  height: calc(100vh - 58px);
  overflow: auto;
  border-right: 1px solid var(--line);
  padding: 18px 12px;
}
.nav-link {
  display: block;
  border-radius: 6px;
  color: #344054;
  font-size: 14px;
  padding: 7px 10px;
  text-decoration: none;
}
.nav-link:hover, .nav-link.active {
  background: var(--accent-soft);
  color: #075f7a;
}
.content {
  min-width: 0;
  padding: 32px clamp(18px, 4vw, 64px);
}
.doc {
  max-width: 920px;
}
.doc h1, .doc h2, .doc h3, .doc h4 {
  line-height: 1.25;
  margin: 1.7em 0 0.55em;
}
.doc h1 {
  margin-top: 0;
  font-size: 34px;
}
.doc h2 { font-size: 25px; }
.doc h3 { font-size: 20px; }
.doc a { color: var(--accent); }
.doc pre {
  overflow: auto;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--code);
  padding: 14px;
}
.doc code {
  border-radius: 4px;
  background: var(--code);
  padding: 2px 4px;
  font-size: 0.94em;
}
.doc pre code {
  padding: 0;
  background: transparent;
}
.doc table {
  width: 100%;
  border-collapse: collapse;
  margin: 18px 0;
}
.doc th, .doc td {
  border: 1px solid var(--line);
  padding: 8px 10px;
  vertical-align: top;
}
.callout {
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 6px;
  margin: 16px 0;
  padding: 12px 14px;
}
.results {
  max-width: 920px;
  border-top: 1px solid var(--line);
  margin-top: 24px;
  padding-top: 18px;
}
.result {
  display: block;
  border-radius: 6px;
  color: var(--text);
  padding: 10px;
  text-decoration: none;
}
.result:hover { background: var(--accent-soft); }
.result small { color: var(--muted); }
@media (max-width: 860px) {
  .topbar { align-items: stretch; flex-direction: column; }
  .layout { display: block; }
  .sidebar {
    position: static;
    height: auto;
    max-height: 260px;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }
  .content { padding: 24px 18px; }
  .doc h1 { font-size: 28px; }
}
"""


def site_js() -> str:
    return """
const input = document.getElementById('search');
const results = document.getElementById('results');
let index = [];
fetch('/search-index.json').then((response) => response.json()).then((data) => {
  index = data;
});
input?.addEventListener('input', () => {
  const query = input.value.trim().toLowerCase();
  if (!query) {
    results.hidden = true;
    results.innerHTML = '';
    return;
  }
  const hits = index.filter((item) =>
    item.title.toLowerCase().includes(query) ||
    item.text.toLowerCase().includes(query)
  ).slice(0, 12);
  results.hidden = false;
  results.innerHTML = '<h2>搜索结果</h2>' + hits.map((item) => `
    <a class="result" href="${item.url}">
      <strong>${item.title}</strong><br>
      <small>${item.url}</small>
    </a>
  `).join('');
});
"""


def copy_assets(build_dir: Path, out_dir: Path) -> None:
    for path in build_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in DOC_EXTENSIONS:
            continue
        rel = path.relative_to(build_dir)
        target = out_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def build_pages(build_dir: Path, out_dir: Path, title: str) -> list[Page]:
    source_paths = sorted(
        path for path in build_dir.rglob("*") if path.is_file() and is_doc_page(path, build_dir)
    )
    known_urls: dict[str, str] = {}
    for source_path in source_paths:
        rel = source_path.relative_to(build_dir)
        out_path = html_path_for(rel)
        url = url_for(out_path)
        known_urls[rel.as_posix()] = url
        known_urls[rel.with_suffix("").as_posix()] = url

    pages: list[Page] = []
    rendered: dict[str, str] = {}
    for source_path in source_paths:
        rel = source_path.relative_to(build_dir)
        raw = source_path.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        title = title_from_markdown(frontmatter, body, rel)
        markdown_body = mdx_to_markdown(raw)
        markdown_body = rewrite_links(markdown_body, known_urls)
        content_html = render_markdown(markdown_body)
        text = plain_text(markdown_body)
        out_path = html_path_for(rel)
        page = Page(
            source_path=source_path,
            rel_path=rel,
            out_path=out_path,
            url=url_for(out_path),
            title=title,
            body_text=text,
        )
        pages.append(page)
        rendered[page.url] = content_html

    ordered_pages = sort_pages(pages, build_dir)
    page_by_url = {page.url: page for page in ordered_pages}
    for url, content_html in rendered.items():
        page = page_by_url[url]
        output = out_dir / page.out_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            render_shell(page, ordered_pages, content_html, title),
            encoding="utf-8",
        )
    return ordered_pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("site"))
    parser.add_argument("--title", default="LangChain 中文文档")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.build_dir.exists():
        raise SystemExit(f"Build directory does not exist: {args.build_dir}")
    if args.out_dir.exists():
        shutil.rmtree(args.out_dir)
    args.out_dir.mkdir(parents=True)

    copy_assets(args.build_dir, args.out_dir)
    pages = build_pages(args.build_dir, args.out_dir, args.title)
    assets_dir = args.out_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    (assets_dir / "site.css").write_text(site_css(), encoding="utf-8")
    (assets_dir / "site.js").write_text(site_js(), encoding="utf-8")
    (args.out_dir / ".nojekyll").write_text("", encoding="utf-8")
    (args.out_dir / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    (args.out_dir / "search-index.json").write_text(
        json.dumps(
            [
                {"title": page.title, "url": page.url, "text": page.body_text}
                for page in pages
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"exported {len(pages)} pages to {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
