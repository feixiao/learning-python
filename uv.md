## 使用uv做Python 版本管理

#### UV安装
```shell
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

echo "export PATH=\"\$PATH:\$HOME/.local/bin\"" >> ~/.zshrc
```

#### 初始化项目
```shell
uv init test-uv
```

#### 项目结构
```shell
.
├── main.py
├── .venv
├── pyproject.toml  # 是项目配置信息
└── README.md
```

#### 运行脚本
```shell
# 自动关联虚拟环境, 优先使用.venv
uv run main.py 
```

#### 管理依赖
```shell
# 安装指定版本
uv add "flask>=2.0.0"

# 同步所有依赖（包括dev）
uv sync

# 仅同步生产依赖
uv sync --production

# 同步并清理多余包
uv sync --clean
```

#### 管理Python环境
```shell
# 列出可用的Python安装版本
uv python list 

uv python install 3.10  pypy@3.10

```

#### 参考资料
+ [《新一代Python管理UV完全使用指南》](https://zhuanlan.zhihu.com/p/1897568987136640818)
