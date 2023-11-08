## Python 版本管理

### 工具对比

#### virtualenv

virtualenv 的解决方案是为每个项目创建一个独立的虚拟环境，在每个虚拟环境中安装的库，对其他虚拟环境完全无影响。

#### pyvenv

pyvenv 与 virtualenv 功能和用法类似。

不同点在于：

- pyvenv 只支持 Python 3.3 及更高版本，而 virtualenv 同时支持 Python 2.x 和 Python 3.x；
- pyvenv 是 Python 3.x 自带的工具，不需要安装，而 virtualenv 是第三方工具，需要安装。

#### pyenv

pyenv 不是用来管理同一个库的多个版本，而是用来管理一台机器上的多个 Python 版本。主要解决开发中有的项目需要用 Python 2.x，有的项目需要用 Python 3.x 的场景。

#### virtualenv

前面提到 pyenv 要解决的是多个 Python 的版本管理问题，virtualenv 要解决的是同一个库的版本管理问题。但如果两个问题都需要解决呢？分别使用不同工具就很麻烦了，而且容易有冲突。为此，pyenv 引入了了 virtualenv 插件，可以在 pyenv 中解决同一个库的版本管理问题。

### pyenv 和 virtualenv 组合使用

#### WSL2 安装

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# 配置
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins pyenv-virtualenv

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# 安装依赖
sudo apt-get update; sudo apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev


```

#### Window 10

```powershell
# Install pyenv-win in PowerShell.
pip install pyenv-win --target $HOME\.pyenv

# 添加环境变量
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```

#### 使用

```shell
# 查看已经安装的版本
# windows只有python，linux版本python的生态比较丰富
pyenv versions

# 查看可以安装的版本
pyenv install -l
pyenv install 3.12.0

# 就是从 https://npm.taobao.org/mirrors/python/ 上下载对应版本的 Python，放入到 ~/.pyenv/cache 目录里面，然后使用 pyenv install $v 即可
export v=3.12.0; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v

# 指定系统版本
pyenv global 3.12.0


# 以 3.8.12 建立虚拟环境
pyenv virtualenv 3.8.12 luffy
pyenv activate luffy
pyenv deactivate luffy
pyenv uninstall luffy
```

### 参考资料

- [《一文了解 virtualenv、pyvenv、pyenv、pyenv virtualenv》](https://cloud.tencent.com/developer/article/1593451)
- [《Ubuntu 安裝使用 pyenv + pyenv-virtualenv》](https://blog.kyomind.tw/ubuntu-pyenv/)
