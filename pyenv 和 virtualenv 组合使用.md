## pyenv 和 virtualenv 组合使用


### 安装
#### OSX
```shell
brew install pyenv
brew install pyenv-virtualenv
```

#### WSL2

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

 export PYTHON_BUILD_MIRROR_URL="https://registry.npmmirror.com/-/binary/python"
 export PYTHON_BUILD_MIRROR_URL_SKIP_CHECKSUM=1
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