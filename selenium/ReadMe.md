

#### 环境准备
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip selenium
```


#### 运行
```shell
python main.py --url "https://en.macromicro.me/series/22748/cnn-fear-and-greed" --out "downloads/cnn-fg.mhtml"

# 打开生成文件
open -a "Google Chrome" downloads/xxx.mhtml
```