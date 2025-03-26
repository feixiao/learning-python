## pybind11入门


#### Python和C/C++ 交互
底层控制的核心在于绕过Python解释器的常规机制，直接操作内存、线程、系统资源等。推荐优先使用PyBind11简化开发，但在需要极致性能或直接操作系统时，需结合Python/C API或ctypes实现精细控制。

+ [《一文总结Python和C/C++的交互方式》](https://github.com/thb1314/python_interact_c/blob/main/tutorial.md)
+ [《pybind11_examples》](https://github.com/feixiao/pybind11_examples)  Examples for the usage of "pybind11"

#### 安装pybind11
```shell
pip install pybind11==2.10.1
```

#### 编译
```shell
# -undefined dynamic_lookup -arch x86_64
g++ -O3 -Wall -shared -std=c++11 -arch x86_64 -fPIC -undefined dynamic_lookup $(python3 -m pybind11 --includes) pybind11_sum.cpp -o pybind11_sum$(python3-config --extension-suffix) 
```