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


@dataclass(frozen=True)
class NavItem:
    kind: str
    title: str
    url: str = ""
    level: int = 0


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


def attrs_from_mdx(raw_attrs: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in re.finditer(
        r"([A-Za-z_:][-A-Za-z0-9_:]*)\s*=\s*(\"[^\"]*\"|'[^']*'|\{[^}]*\})",
        raw_attrs,
        flags=re.DOTALL,
    ):
        value = match.group(2).strip()
        if value.startswith(('"', "'")):
            value = value[1:-1]
        elif value.startswith("{") and value.endswith("}"):
            value = value[1:-1].strip().strip('"').strip("'")
        attrs[match.group(1)] = value
    return attrs


def page_title_for_ref(ref: str, known_titles: dict[str, str]) -> str:
    normalized = ref.strip("/")
    candidates = [
        normalized,
        normalized + ".mdx",
        normalized + ".md",
        normalized + "/index.mdx",
        normalized + "/index.md",
    ]
    for candidate in candidates:
        if candidate in known_titles:
            return known_titles[candidate]
    return normalized.rsplit("/", 1)[-1].replace("-", " ").replace("_", " ").title()


def url_for_ref(ref: str, known_urls: dict[str, str]) -> str:
    normalized = ref.strip("/")
    candidates = [
        normalized,
        normalized + ".mdx",
        normalized + ".md",
        normalized + "/index.mdx",
        normalized + "/index.md",
    ]
    for candidate in candidates:
        if candidate in known_urls:
            return known_urls[candidate]
    return "/" + normalized + ".html"


def build_nav_items(
    build_dir: Path,
    known_urls: dict[str, str],
    known_titles: dict[str, str],
) -> list[NavItem]:
    docs_json = build_dir / "docs.json"
    if not docs_json.exists():
        return []
    try:
        data = json.loads(docs_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    items: list[NavItem] = []
    seen_pages: set[str] = set()

    def add_heading(title: str, level: int) -> None:
        title = title.strip()
        if title:
            items.append(NavItem("heading", title, level=level))

    def add_page(ref: str, level: int) -> None:
        url = url_for_ref(ref, known_urls)
        if url in seen_pages:
            return
        seen_pages.add(url)
        items.append(NavItem("page", page_title_for_ref(ref, known_titles), url, level))

    def walk(value: Any, level: int = 0) -> None:
        if isinstance(value, str):
            add_page(value, level)
            return
        if isinstance(value, list):
            for item in value:
                walk(item, level)
            return
        if not isinstance(value, dict):
            return

        label = (
            value.get("product")
            or value.get("item")
            or value.get("dropdown")
            or value.get("tab")
            or value.get("group")
            or value.get("anchor")
        )
        if isinstance(label, str):
            add_heading(label, level)

        if isinstance(value.get("root"), str):
            add_page(value["root"], level + 1)
        for key in ("pages", "tabs", "dropdowns", "menu", "groups", "anchors", "navigation"):
            if key in value:
                walk(value[key], level + 1)

    navigation = data.get("navigation", {})
    if isinstance(navigation, dict) and "products" in navigation:
        walk(navigation["products"])
    else:
        walk(navigation)
    return items


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


def rewrite_href(value: str) -> str:
    if not value:
        return ""
    if value.startswith(("http://", "https://", "#", "mailto:")):
        return value
    if value.endswith(".html"):
        return value
    if "#" in value:
        base, anchor = value.split("#", 1)
        return rewrite_href(base) + "#" + anchor
    return value.rstrip("/") + ".html"


def strip_jsx_braces(text: str) -> str:
    return re.sub(r"\s+[A-Za-z_:][-A-Za-z0-9_:]*=\{\{.*?\}\}", "", text, flags=re.DOTALL)


def transform_mdx_components(body: str) -> str:
    body = strip_jsx_braces(body)

    def card_group(match: re.Match[str]) -> str:
        attrs = attrs_from_mdx(match.group("attrs"))
        cols = html.escape(attrs.get("cols", "2"), quote=True)
        return f'\n<section class="card-grid cols-{cols}">\n{match.group("body")}\n</section>\n'

    body = re.sub(
        r"<CardGroup\b(?P<attrs>[^>]*)>(?P<body>.*?)</CardGroup>",
        card_group,
        body,
        flags=re.DOTALL,
    )

    def card(match: re.Match[str]) -> str:
        attrs = attrs_from_mdx(match.group("attrs"))
        title = html.escape(attrs.get("title", ""))
        href = html.escape(rewrite_href(attrs.get("href", "")), quote=True)
        cta = html.escape(attrs.get("cta", ""))
        inner = render_inline_markdown(match.group("body").strip())
        tag = "a" if href else "div"
        href_attr = f' href="{href}"' if href else ""
        cta_html = f'<span class="card-cta">{cta}</span>' if cta else ""
        title_html = f"<h3>{title}</h3>" if title else ""
        return f'\n<{tag} class="doc-card"{href_attr}>{title_html}<p>{inner}</p>{cta_html}</{tag}>\n'

    def self_closing_card(match: re.Match[str]) -> str:
        attrs = attrs_from_mdx(match.group("attrs"))
        title = html.escape(attrs.get("title", ""))
        href = html.escape(rewrite_href(attrs.get("href", "")), quote=True)
        tag = "a" if href else "div"
        href_attr = f' href="{href}"' if href else ""
        title_html = f"<h3>{title}</h3>" if title else ""
        return f'\n<{tag} class="doc-card"{href_attr}>{title_html}</{tag}>\n'

    body = re.sub(
        r"<Card\b(?P<attrs>[^>]*)/>",
        self_closing_card,
        body,
        flags=re.DOTALL,
    )

    body = re.sub(
        r"<Card\b(?P<attrs>[^>]*?)(?<!/)>(?P<body>.*?)</Card>",
        card,
        body,
        flags=re.DOTALL,
    )

    callout_labels = {
        "Callout": "提示",
        "Note": "提示",
        "Info": "信息",
        "Tip": "建议",
        "Warning": "警告",
        "Check": "检查",
        "Danger": "注意",
    }
    for tag, label in callout_labels.items():
        body = re.sub(
            rf"<{tag}\b[^>]*>",
            f'\n<aside class="callout"><strong>{label}</strong>\n',
            body,
            flags=re.DOTALL,
        )
        body = re.sub(rf"</{tag}>", "\n</aside>\n", body)

    def titled_block(tag: str, heading: str = "h3") -> None:
        nonlocal body

        def replace(match: re.Match[str]) -> str:
            attrs = attrs_from_mdx(match.group("attrs"))
            title = html.escape(attrs.get("title") or attrs.get("name") or attrs.get("label") or "")
            summary = f"<{heading}>{title}</{heading}>\n" if title else ""
            return f"\n<section class=\"mdx-block\">{summary}{match.group('body')}</section>\n"

        body = re.sub(
            rf"<{tag}\b(?P<attrs>[^>]*)>(?P<body>.*?)</{tag}>",
            replace,
            body,
            flags=re.DOTALL,
        )

    for tag in ("Tab", "Step", "Accordion", "Expandable"):
        titled_block(tag)

    body = re.sub(r"</?(Tabs|Steps|AccordionGroup|CodeGroup|Columns|Frame)\b[^>]*>", "", body)
    body = re.sub(r"</?div\b[^>]*>", "", body)
    body = re.sub(r"<([A-Z][A-Za-z0-9_.:-]*)(\s[^>]*)?/>", "", body)
    body = re.sub(r"</?([A-Z][A-Za-z0-9_.:-]*)(\s[^>]*)?>", "", body)
    return body


def mdx_to_markdown(text: str) -> str:
    frontmatter, body = strip_frontmatter(text)
    del frontmatter
    body = re.sub(r"(?s)\{/\*.*?\*/\}", "", body)
    body = re.sub(r"^\s*(import|export)\b.*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"^\s*</?fragment>\s*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"</?fragment>", "", body)

    return transform_mdx_components(body)


def render_inline_markdown(text: str) -> str:
    value = html.escape(re.sub(r"\s+", " ", text).strip())
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(rewrite_href(m.group(2)), quote=True)}">{m.group(1)}</a>',
        value,
    )
    return value


def render_markdown_fallback(markdown_text: str) -> str:
    code_blocks: list[tuple[str, str]] = []

    def stash_code(match: re.Match[str]) -> str:
        info = html.escape(match.group(1).strip())
        code = html.escape(match.group(2).strip("\n"))
        token = f"@@CODE_BLOCK_{len(code_blocks)}@@"
        code_blocks.append((token, f'<pre><code data-language="{info}">{code}</code></pre>'))
        return "\n" + token + "\n"

    text = re.sub(r"```([^\n]*)\n(.*?)```", stash_code, markdown_text, flags=re.DOTALL)
    text = re.sub(r"^\s*---\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"<h([1-6])\b[^>]*>(.*?)</h\1>", r"\n\n<h\1>\2</h\1>\n\n", text, flags=re.DOTALL)

    blocks = re.split(r"\n{2,}", text)
    rendered: list[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            rendered.append("</ul>")
            in_list = False

    for block in blocks:
        raw = block.strip()
        if not raw:
            continue
        if raw.startswith("@@CODE_BLOCK_"):
            close_list()
            rendered.append(raw)
            continue
        if raw.startswith("<") and raw.endswith(">"):
            close_list()
            rendered.append(raw)
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", raw)
        if heading:
            close_list()
            level = len(heading.group(1))
            rendered.append(f"<h{level}>{render_inline_markdown(heading.group(2))}</h{level}>")
            continue
        lines = raw.splitlines()
        if all(re.match(r"^\s*[-*]\s+", line) for line in lines):
            if not in_list:
                rendered.append("<ul>")
                in_list = True
            for line in lines:
                rendered.append(f"<li>{render_inline_markdown(re.sub(r'^\\s*[-*]\\s+', '', line))}</li>")
            continue
        close_list()
        rendered.append(f"<p>{render_inline_markdown(raw)}</p>")

    close_list()
    html_text = "\n".join(rendered)
    for token, block_html in code_blocks:
        html_text = html_text.replace(token, block_html)
    return html_text


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
        return render_markdown_fallback(markdown_text)


def plain_text(markdown_text: str) -> str:
    text = re.sub(r"```.*?```", "", markdown_text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[#*_`>\[\]()]|https?://\S+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def render_shell(
    page: Page,
    pages: list[Page],
    nav_items: list[NavItem],
    content_html: str,
    title: str,
) -> str:
    if nav_items:
        nav_parts = []
        for item in nav_items:
            if item.kind == "heading":
                nav_parts.append(
                    f'<div class="nav-heading level-{item.level}">{html.escape(item.title)}</div>'
                )
            else:
                nav_parts.append(
                    f'<a class="nav-link level-{item.level}{" active" if item.url == page.url else ""}" '
                    f'href="{html.escape(item.url)}">{html.escape(item.title)}</a>'
                )
        nav = "\n".join(nav_parts)
    else:
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
.nav-link.level-2 { padding-left: 22px; }
.nav-link.level-3 { padding-left: 34px; }
.nav-link.level-4 { padding-left: 46px; }
.nav-heading {
  color: #667085;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0;
  margin: 18px 10px 6px;
  text-transform: uppercase;
}
.nav-heading.level-1 {
  color: #202124;
  font-size: 13px;
  text-transform: none;
}
.nav-heading.level-2,
.nav-heading.level-3,
.nav-heading.level-4 {
  display: none;
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
.card-grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  margin: 18px 0;
}
.doc-card {
  display: block;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  color: var(--text);
  padding: 16px;
  text-decoration: none;
}
.doc-card:hover {
  border-color: #9ccfe0;
  background: #f8fcfd;
}
.doc-card h3 {
  margin: 0 0 8px;
}
.doc-card p {
  margin: 0;
}
.card-cta {
  display: inline-block;
  color: var(--accent);
  font-size: 13px;
  font-weight: 650;
  margin-top: 12px;
}
.mdx-block {
  border-top: 1px solid var(--line);
  margin: 18px 0;
  padding-top: 8px;
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


def normalize_site_url(site_url: str) -> str:
    return site_url.rstrip("/")


def render_sitemap(pages: list[Page], site_url: str) -> str:
    base_url = normalize_site_url(site_url)
    entries = []
    for page in pages:
        entries.append(
            "  <url>\n"
            f"    <loc>{html.escape(base_url + page.url, quote=True)}</loc>\n"
            "  </url>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )


def render_robots(site_url: str) -> str:
    base_url = normalize_site_url(site_url)
    return f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n"


def strip_trailing_whitespace(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


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

    known_titles: dict[str, str] = {}
    for source_path in source_paths:
        rel = source_path.relative_to(build_dir)
        raw = source_path.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        page_title = title_from_markdown(frontmatter, body, rel)
        known_titles[rel.as_posix()] = page_title
        known_titles[rel.with_suffix("").as_posix()] = page_title

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
    nav_items = build_nav_items(build_dir, known_urls, known_titles)
    page_by_url = {page.url: page for page in ordered_pages}
    for url, content_html in rendered.items():
        page = page_by_url[url]
        output = out_dir / page.out_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            strip_trailing_whitespace(
                render_shell(page, ordered_pages, nav_items, content_html, title)
            ),
            encoding="utf-8",
        )
    return ordered_pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("site"))
    parser.add_argument("--title", default="LangChain 中文文档")
    parser.add_argument("--site-url", default="https://langchain.asia")
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
    (args.out_dir / "robots.txt").write_text(
        render_robots(args.site_url),
        encoding="utf-8",
    )
    (args.out_dir / "sitemap.xml").write_text(
        render_sitemap(pages, args.site_url),
        encoding="utf-8",
    )
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
