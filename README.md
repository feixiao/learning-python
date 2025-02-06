## 学习 Python

- [sqlalchemy](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014021031294178f993c85204e4d1b81ab032070641ce5000)

  ```shell
  pip install mysql-connector-python-rf
  ```

- [python 如何管理项目依赖包](https://www.jianshu.com/p/31c8349e5c9d)

  ```
  # 生成项目依赖包和版本列表文件(每次更新依赖包都需要更新这个文件)
  pip freeze > requirements.txt
  # 下载依赖项
  pip install -r requirements.txt
  ```

- [Python 环境管理](./Python版本管理.md)

  ```shell
  # 创建环境
  conda create --name py310 python=3.10
  # 安装好后，使用activate激活某个环境
  conda activate py310
  # 返回主环境
  conda deactivate py310
  # 查看环境
  conda info -e
  # 删除环境
  conda remove --name py310 --all

  # 对虚拟环境中安装额外的包
  conda install -n env_name [package]  # 未激活环境
  conda install [package]  # 如果已经激活环境
  ```

#### Python 高级编程

- [PythonAdvanced](https://github.com/feixiao/PythonAdvanced)
- [Expert-Python-Programming](https://github.com/feixiao/Expert-Python-Programming-Third-Edition)
- [《Python 最佳实践指南》](https://github.com/prodesire/python-guide-cn) Python 最佳实践指南
- [samplemod](https://github.com/feixiao/samplemod) 模块项目结构参考
- [poetry](https://github.com/python-poetry/poetry) 整体项目结构参考
#### 三方库

- [playsound](https://github.com/TaylorSMarks/playsound)
- [python-fire](https://github.com/google/python-fire/)
- [gitignore](https://github.com/github/gitignore)

#### 资料

- [《Python 3 面向对象编程》](https://book.douban.com/subject/26468916/)
- [《Python 高级编程（第二版）》](https://book.douban.com/subject/27133480/)
- [《Python 资源大全中文版》](https://github.com/jobbole/awesome-python-cn)
- [《awesome-python》](https://awesome-python.com/)
- [《Conda 使用教程》](https://zhuanlan.zhihu.com/p/483716942)
