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
6. GitHub Actions 提交 `site/`，Vercel 或 Cloudflare Pages 通过 Git 集成自动部署。

## 需要配置的密钥

在 GitHub 仓库 `Settings -> Secrets and variables -> Actions` 中添加：

- Secret: `MINIMAX_API_KEY`
- Variable: `MINIMAX_BASE_URL`，默认 `https://api.minimax.io/v1`
- Variable: `MINIMAX_MODEL`，默认 `MiniMax-M2.7-highspeed`

MiniMax 官方 OpenAI-compatible 文档使用的 base URL 是 `https://api.minimax.io/v1`。

## 手动试跑

只翻译 3 个文件，用于验证 key、模型和构建：

```bash
export MINIMAX_API_KEY=...
python -m pip install -r requirements-docs.txt
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

## GitHub Actions

`.github/workflows/langchain-docs-sync.yml` 每天北京时间 02:17 检查一次官方上游。

也可以在 GitHub Actions 页面手动运行：

- `limit=3`：冒烟测试。
- `limit=0`：翻译全部文档。
- `force=true`：忽略缓存，强制重翻。

## Vercel 部署

第一轮 Actions 成功后，仓库会出现 `site/`。

在 Vercel 项目中设置：

- Framework Preset: `Other`
- Build Command: 留空或 `echo ready`
- Output Directory: `site`

也可以在确认 `site/` 已生成后添加：

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "buildCommand": "echo ready",
  "outputDirectory": "site"
}
```

## Cloudflare Pages 部署

GitHub 已连通 Cloudflare 时，Pages 项目建议设置：

- Production branch: `main`
- Build command: 留空或 `echo ready`
- Build output directory: `site`

如果使用 Wrangler 直传，可在 `site/` 生成后执行：

```bash
npx wrangler pages deploy site --project-name langchainzh
```

## 注意

- `site/` 是静态导出版，目标是免费部署可用；它不会完全复刻 Mintlify 的所有交互组件。
- 翻译缓存只保存源文件 hash、模型和时间，不保存 MiniMax key。
- 当前仓库的旧 Nextra 站点文件暂时保留，等 `site/` 首次生成并确认部署后再删除更稳。
