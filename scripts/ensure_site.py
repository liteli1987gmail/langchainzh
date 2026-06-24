#!/usr/bin/env python3
"""Ensure the Vercel/Cloudflare output directory exists.

This is intentionally small: GitHub Actions generates the real translated docs
into site/. Hosting providers can still deploy a clear setup page before the
first full sync has produced that directory.
"""

from __future__ import annotations

from pathlib import Path


SITE_DIR = Path("site")
INDEX = SITE_DIR / "index.html"


def main() -> int:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    if INDEX.exists():
        print("site/index.html already exists")
        return 0

    (SITE_DIR / "assets").mkdir(exist_ok=True)
    (SITE_DIR / "assets" / "site.css").write_text(
        """
:root {
  color-scheme: light;
  --bg: #fbfaf7;
  --text: #202124;
  --muted: #667085;
  --accent: #087ea4;
}
body {
  margin: 0;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: var(--bg);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
main {
  max-width: 720px;
  padding: 40px 24px;
}
h1 {
  font-size: clamp(30px, 5vw, 48px);
  line-height: 1.12;
  margin: 0 0 16px;
}
p {
  color: var(--muted);
  font-size: 17px;
  line-height: 1.7;
}
a { color: var(--accent); }
code {
  background: #f1eee6;
  border-radius: 4px;
  padding: 2px 5px;
}
""".lstrip(),
        encoding="utf-8",
    )
    INDEX.write_text(
        """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LangChain 中文文档</title>
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <main>
    <h1>LangChain 中文文档</h1>
    <p>
      自动同步与翻译流水线已经配置完成。请在 GitHub Actions 中添加
      <code>MINIMAX_API_KEY</code>，运行
      <code>Sync LangChain Chinese Docs</code> 工作流后，这里会发布完整中文文档。
    </p>
    <p>
      运维说明见仓库中的
      <a href="https://github.com/liteli1987gmail/langchainzh/blob/main/docs/operations.md">docs/operations.md</a>。
    </p>
  </main>
</body>
</html>
""",
        encoding="utf-8",
    )
    (SITE_DIR / "search-index.json").write_text("[]\n", encoding="utf-8")
    (SITE_DIR / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    print("created setup site in site/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
