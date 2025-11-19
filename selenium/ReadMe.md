

#### 环境准备
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip selenium
```


#### 运行
```shell
python main.py --url "https://sc.macromicro.me/series/22748/cnn-fear-and-greed" --out "downloads/cnn-fg.mhtml"

# 打开生成文件
open -a "Google Chrome" downloads/xxx.mhtml
```

可选参数：
- `--no-headless`：以可见窗口运行，方便手动点 Cookie 同意等。
- `--delay <sec>`：在抓取前额外等待秒数（配合 `--no-headless` 使用）。
- `--chrome-binary <path>`：指定 Chrome/Chromium 可执行文件路径（macOS 常见：`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`）。
- `--driver-path <path>`：指定 `chromedriver` 可执行路径（若 Selenium Manager 无法自动获取）。

#### 常见问题（macOS）
1) 报错 `Unable to obtain driver for chrome`

```shell
# 安装 Google Chrome（如未安装）
brew install --cask google-chrome

# 若网络限制导致自动下载驱动失败，可手动安装 chromedriver：
brew install --cask chromedriver

# 运行时指定 driver 路径（按实际 Homebrew 路径选择其一）
python main.py --url "..." --driver-path /opt/homebrew/bin/chromedriver
# 或
python main.py --url "..." --driver-path /usr/local/bin/chromedriver

# 如 Chrome 不在默认路径，显式指定：
python main.py --url "..." --chrome-binary \
	"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# 升级 selenium 避免旧版本兼容问题
pip install -U selenium
```

2) 页面需要手动交互（如 Cookie 弹窗）
```shell
python main.py --url "..." --no-headless --delay 8
```

3) 输出文件未指定
不指定 `--out` 时，程序会默认保存到 `selenium/downloads/<slug>-<timestamp>.mhtml`，控制台会打印实际路径。