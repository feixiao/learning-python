cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)


# 查找Python和pybind11依赖
#  pip install "pybind11[global]" 
find_package(pybind11 REQUIRED)


pybind11_add_module(cmake_example src/main.cpp)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(cmake_example
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
