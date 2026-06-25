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
5. 将 `build/` 转成可直接部署的静态站点 `site/`。
6. 压缩超过免费静态托管单文件限制的 GIF 资源。
7. GitHub Actions 提交 `site/`，Vercel 或 Cloudflare Pages 通过 Git 集成自动部署。

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

更稳的完整同步参数：

```bash
TRANSLATION_WORKERS=2 TRANSLATION_MAX_CHARS=6000 \
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

## Vercel 部署

仓库包含 `vercel.json`，会让 Vercel 跳过旧 Nextra 依赖安装，并从 `site/` 发布。
第一轮 Actions 成功后，`site/` 会从占位页替换成完整中文文档。
`package.json` 的 `build` 脚本也只会确保 `site/` 存在，不再运行旧 Next/Nextra 构建。

注意：完整静态导出版较大，Vercel Hobby 静态上传额度可能不够；Vercel Pro 或 Cloudflare Pages 更合适。

在 Vercel 项目中设置：

- Framework Preset: `Other`
- Build Command: `python3 scripts/ensure_site.py`
- Output Directory: `site`

## Cloudflare Pages 部署

仓库包含 `wrangler.toml`，输出目录为 `site`。GitHub 已连通 Cloudflare 时，Pages 项目建议设置：

- Production branch: `main`
- Build command: `python3 scripts/ensure_site.py`
- Build output directory: `site`

Cloudflare Pages 免费计划有单文件大小限制。本仓库会在同步导出后运行
`scripts/optimize_site_assets.py`，自动压缩超限 GIF，并保持原路径不变。

GitHub Actions 中也包含一个可选的 Cloudflare Pages 直传步骤。只有当
`CLOUDFLARE_API_TOKEN` 和 `CLOUDFLARE_ACCOUNT_ID` 都存在时才会执行；否则会跳过，
不影响翻译、构建和提交。

如果使用 Wrangler 直传，可在 `site/` 生成后执行：

```bash
npx wrangler pages deploy site --project-name langchainzh
```

## 注意

- `site/` 是静态导出版，目标是免费部署可用；它不会完全复刻 Mintlify 的所有交互组件。
- 翻译缓存保存源文件 hash、模型、时间和可复用的译文文件，不保存 MiniMax key。
  这样上游只改少量文件时，未变文件会直接从 `.translation-cache/translations/` 写回，不会重复消耗 MiniMax 额度。
- 当前仓库的旧 Nextra 站点文件暂时保留，等 `site/` 首次生成并确认部署后再删除更稳。
