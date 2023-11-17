import yaml

# 定义一个枚举类


class MyEnum1:
    def __init__(self, value):
        self.value = value

# 定义一个安全的Dumper类


class MySafeDumper(yaml.SafeDumper):
    def represent_data(self, data):
        if isinstance(data, MyEnum1):
            return self.represent_data(data.value)
        return super().represent_data(data)


# 示例数据
data = {
    'value_3': MyEnum1(3)
}

# 使用MySafeDumper输出
yaml_str = yaml.dump(data, Dumper=MySafeDumper)

print(yaml_str)
