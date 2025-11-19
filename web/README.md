# 网页下载脚本（服务器可用）

`web/main.py` 支持三种下载方式：
- requests：保存原始 HTML（轻量，可能不含前端渲染结果）
- selenium：渲染后保存 HTML + 整页截图（需要 Chrome/Chromedriver）
- playwright：渲染后保存 HTML + 整页截图（推荐服务器，自动管理 Chromium）

## 快速开始（requests，最简单）

```zsh
python web/main.py \
  --method requests \
  --out web/cnn-fear-and-greed.html \
  'https://sc.macromicro.me/charts/50108/cnn-fear-and-greed'
```

## 服务器推荐（playwright）

```zsh
# 1) 安装依赖
pip install playwright
# 2) 安装浏览器及依赖（Linux 服务器推荐 --with-deps）
python -m playwright install --with-deps chromium

# 3) 运行渲染下载：保存渲染后的 HTML 和全页截图
python web/main.py \
  --method playwright \
  --out-html web/cnn-fear-and-greed_rendered.html \
  --out-png  web/cnn-fear-and-greed.png \
  --wait 6 \
  'https://sc.macromicro.me/charts/50108/cnn-fear-and-greed'
```

## 备选（selenium，本机有 Chrome 时）

```zsh
pip install selenium
python web/main.py \
  --method selenium \
  --out-html web/cnn-fear-and-greed_rendered.html \
  --out-png  web/cnn-fear-and-greed.png \
  --wait 8 \
  'https://sc.macromicro.me/charts/50108/cnn-fear-and-greed'
```

## 说明
- 仅保存 HTML 不会打包外部静态资源；若需要“所见即所得”，请使用 `playwright/selenium` 并查看 PNG 截图。
- `--wait` 用于等待页面的异步内容加载；可按网络情况调整。
- Playwright 会在首次运行后缓存浏览器，适合无桌面环境的服务器。