# LangChain 中文文档自动化运维

## 上游与构建方式

官方文档源码在 `langchain-ai/docs`。当前官方 README 说明：

- `src/` 是可编辑文档源文件。
- `src/docs.json` 是 Mintlify 导航和站点配置。
- `pipeline/` 是预处理/构建代码。
- `build/` 是生成产物，不能手工编辑。
- 本地预览命令是 `make install` 和 `make dev`。
- 构建命令是 `make build`，底层会运行 `npm install` 和 `uv run pipeline build`。

本仓库的自动化流程是：

1. 拉取 `https://github.com/langchain-ai/docs.git` 的 `main`。
2. 用 MiniMax OpenAI-compatible API 将 `src/` 增量翻译到中文。
3. 将翻译后的 `src/` 放回官方仓库快照。
4. 运行官方 pipeline 生成 `build/`。
5. 优先使用 Mintlify CLI 将 `build/` 真实渲染/导出为 `site/`；仅在 CLI 不可用时使用兼容静态导出器。
6. 压缩超过免费静态托管单文件限制的 GIF 资源。
7. GitHub Actions 提交 `site/`，Cloudflare Pages 通过 Git 集成自动部署。

## 需要配置的密钥

在 GitHub 仓库 `Settings -> Secrets and variables -> Actions` 中添加：

- Secret: `MINIMAX_API_KEY`
- Variable: `MINIMAX_BASE_URL`，默认 `https://api.minimaxi.com/v1`
- Variable: `MINIMAX_MODEL`，默认 `MiniMax-M2.7-highspeed`

如果要让 GitHub Actions 直接发布到 Cloudflare Pages，再添加：

- Secret: `CLOUDFLARE_API_TOKEN`
- Variable: `CLOUDFLARE_ACCOUNT_ID`
- Variable: `CLOUDFLARE_PROJECT_NAME`，默认 `langchainzh`

如果只使用 Cloudflare Pages 的 GitHub 集成，上述 Cloudflare token 可以不配；Pages 会在
`main` 更新后自行构建 `site/`。

本机 `~/.serenity_env` 已有 `MINIMAX_API_KEY`。本仓库脚本会依次读取 `.env` 和 `~/.serenity_env`。
这台机器的 Token Plan key 已验证可用的 OpenAI-compatible base URL 是 `https://api.minimaxi.com/v1`。
脚本默认禁用系统代理调用 MiniMax；如需走代理，可设置 `MINIMAX_USE_PROXY=1`。

## 手动试跑

只翻译 3 个文件，用于验证 key、模型和构建：

```bash
export MINIMAX_API_KEY=...
python -m pip install -r requirements-docs.txt
python scripts/check_minimax.py
python scripts/sync_langchain_docs.py --force --limit 3
```

不调用 MiniMax 的本地烟测：

```bash
python scripts/sync_langchain_docs.py --mock-translator --force --limit 3 --skip-build
```

完整同步：

```bash
export MINIMAX_API_KEY=...
python -m pip install -r requirements-docs.txt
python scripts/sync_langchain_docs.py --force
```

使用真实 Mintlify 渲染导出：

```bash
export MINIMAX_API_KEY=...
DOCS_RENDERER=mintlify python scripts/sync_langchain_docs.py --force
```

也可以在已有 `.langchain-work-latest/upstream/build` 时单独导出：

```bash
python scripts/export_mintlify_site.py \
  --build-dir .langchain-work-latest/upstream/build \
  --out-dir site
```

`export_mintlify_site.py` 会在包含 `docs.json` 的目录运行 `mint export --output ...`，
解压官方预渲染结果到 `site/`。默认 Mintlify 命令是 `npx --yes mint@latest`；
如果 CI 已全局安装 CLI，可设置 `MINT_COMMAND=mint`。Mintlify 官方要求 Node.js
`20.17.0+`，并提供 `mint dev` 本地预览和 `mint export` 离线导出命令。
实测 Homebrew Node 26 会被 Mintlify CLI 拒绝，可使用 Codex runtime 的 Node 24 或其他 LTS Node：

```bash
PATH=/Users/a1/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH \
MINT_COMMAND=/private/tmp/mintlify-cli-test/node_modules/.bin/mint \
python3 scripts/export_mintlify_site.py \
  --build-dir .langchain-work-latest/upstream/build \
  --out-dir /private/tmp/langchain-mintlify-site
```

当前真实 Mintlify export 已能启动，但在现有 `.langchain-work-latest/upstream/build` 上会批量报
`failed to generate ... (status 404)`，并且早期还暴露过未闭合 MDX 标签问题。也就是说，
官方渲染路径已接入脚本，但还不能直接作为生产导出替换 fallback；下一步需要让翻译后的源文件和
官方 pipeline 产物通过 Mintlify 的路由与 MDX 解析规则。

更稳的完整同步参数：

```bash
TRANSLATION_WORKERS=1 TRANSLATION_MAX_CHARS=6000 TRANSLATION_TIMEOUT=90 \
python scripts/sync_langchain_docs.py --force
```

本机首次全量翻译时，MiniMax endpoint 偶尔会返回 400/401/429 或 SSL EOF。建议使用较低并发和失败日志续跑：

```bash
python scripts/translate_minimax.py \
  --source-dir .langchain-work/upstream/src \
  --target-dir .langchain-work/src.zh \
  --cache .translation-cache/minimax.json \
  --workers 4 \
  --retries 6 \
  --retry-delay 5 \
  --keep-going \
  --failure-log .translation-cache/failures.json
```

## GitHub Actions

`.github/workflows/langchain-docs-sync.yml` 每天北京时间 02:17 检查一次官方上游。
工作流会先比较 `langchain-ai/docs` 的当前 SHA 和本仓库 `.langchain-docs-upstream.json` 记录的 SHA。
如果是定时运行且上游没有变化，会直接跳过翻译。

也可以在 GitHub Actions 页面手动运行：

- `limit=3`：冒烟测试，手动运行的默认值。
- `limit=0`：翻译全部文档。
- `force=true`：忽略缓存，强制重翻。
- `mock=true`：不调用 MiniMax，只复制原文，用来测试拉取、构建和导出链路；mock 结果不会提交回 `main`。

`.github/workflows/deploy-static-site.yml` 只负责验证并部署当前 `site/`。
当 `site/` 推送到 `main` 时会自动运行；也可以在 GitHub Actions 页面手动运行，用来在补齐
Cloudflare 配置后立即发布现有静态站。

## 当前生产域名

生产域名使用：

- `https://langchain.asia`
- `https://www.langchain.asia`

如果访问返回 `402 DEPLOYMENT_DISABLED`，说明域名仍然落在已停用的 Vercel 项目上。
切换到 Cloudflare Pages 后，用下面命令验证：

```bash
npm run verify:domain
```

## Vercel 旧部署

仓库包含 `vercel.json`，会让 Vercel 跳过旧 Nextra 依赖安装，并从 `site/` 发布。
第一轮 Actions 成功后，`site/` 会从占位页替换成完整中文文档。
`package.json` 的 `build` 脚本也只会确保 `site/` 存在，不再运行旧 Next/Nextra 构建。

注意：当前 `langchain.asia` 的 Vercel 部署已被停用。后续生产环境以 Cloudflare Pages 免费版为准。
完整静态导出版较大，Vercel Hobby 静态上传额度可能不够；Vercel Pro 或 Cloudflare Pages 更合适。

在 Vercel 项目中设置：

- Framework Preset: `Other`
- Build Command: `python3 scripts/ensure_site.py`
- Output Directory: `site`

## Cloudflare Pages 部署

仓库包含 `wrangler.toml`，输出目录为 `site`。GitHub 已连通 Cloudflare 时，Pages 项目设置：

- Project name: `langchainzh`
- Repository: `liteli1987gmail/langchainzh`

- Production branch: `main`
- Build command: `python3 scripts/ensure_site.py`
- Build output directory: `site`

在 Cloudflare Pages 项目中添加 Custom domains：

- `langchain.asia`
- `www.langchain.asia`

Cloudflare Pages 免费计划有单文件大小限制。本仓库会在同步导出后运行
`scripts/optimize_site_assets.py`，自动压缩超限 GIF，并保持原路径不变。

GitHub Actions 中也包含一个可选的 Cloudflare Pages 直传步骤。只有当
`CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID` 都存在时才会执行；否则会跳过，
不影响翻译、构建和提交。

如果使用 Wrangler 直传，可在 `site/` 生成后执行：

```bash
npm run deploy:cloudflare
```

也可以直接运行底层脚本：

```bash
python3 scripts/deploy_cloudflare_pages.py --project-name langchainzh
```

脚本会先验证 `site/`，检查 Cloudflare Pages 免费计划的单文件大小限制，然后调用 Wrangler。
如果本机未登录 Cloudflare，请先运行 `wrangler login`，或设置
`CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID`。

## Mintlify 渲染策略

真实生产路径应使用 `DOCS_RENDERER=mintlify`。原因是官方 `pipeline build` 的输出仍是
Mintlify/MDX 文档树，而不是最终网页；`Card`、`Tabs`、`CodeGroup`、`Callout` 等控件需要
Mintlify 前端渲染层理解。仓库里的 `scripts/export_static_site.py` 只是兼容导出器，用于
Mintlify CLI 暂时不可用时生成可读页面，不能保证 1:1 复刻官方交互。

`scripts/verify_site.py` 已加入残留标签扫描，会拒绝明显未渲染的 `fragment`、
`Card/CardGroup`、`Callout/Tip/Note/Warning` 等可见残留。
兼容导出器已补充基础 Markdown 表格和有序列表渲染，能避免本地预览中把 `| a | b |`
表格或 `1.` 序号显示成普通文本；但复杂 Mintlify 交互仍应以后续真实 Mintlify 导出为准。

本机测试时，`npx --yes mint@latest version` 在 Puppeteer/Mintlify 客户端下载阶段耗时较长。
CI 中建议缓存 npm/Mintlify 相关目录，或预装 `mint` 后设置 `MINT_COMMAND=mint`。

## 注意

- `site/` 应优先由 Mintlify 官方 CLI 导出；兼容导出器只是 fallback。
- 翻译缓存保存源文件 hash、模型、时间和可复用的译文文件，不保存 MiniMax key。
  这样上游只改少量文件时，未变文件会直接从 `.translation-cache/translations/` 写回，不会重复消耗 MiniMax 额度。
- 当前仓库的旧 Nextra 站点文件暂时保留，等 `site/` 首次生成并确认部署后再删除更稳。
