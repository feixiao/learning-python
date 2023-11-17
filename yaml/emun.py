import enum
import yaml


# 定义第一个枚举类


class MyEnum1(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

# 定义第二个枚举类


class MyEnum2(enum.Enum):
    A = 'a'
    B = 'b'
    C = 'c'

# 自定义输出函数


def enum_representer(dumper, data):
    if isinstance(data, MyEnum1):
        return dumper.represent_scalar('tag:yaml.org,2002:str', f'{data.__class__.__name__}.MyEnum1.{data.name}')
    elif isinstance(data, MyEnum2):
        return dumper.represent_scalar('tag:yaml.org,2002:null', '')


# 定制输出函数来避免输出 !!python/object/apply:__main__.MyEnum2
def custom_represent_none(dumper):
    return dumper.represent_scalar('tag:yaml.org,2002:null', '')


# yaml.add_representer(MyEnum2, custom_represent_none)
# yaml.add_representer(MyEnum2, enum_representer)
# yaml.add_representer(MyEnum1, custom_represent_none)

# 创建包含两种枚举类的字典
enum_dict = {
    'value_1': MyEnum1.FIRST,
    'value_2': MyEnum2.B,
    'value_3': MyEnum1.THIRD,
    'value_4': None,
    'value_5': MyEnum1.THIRD  # 会引用之前的枚举值 &id001 => *id001
}

enum_dict1 = {
    'value_1': MyEnum1.FIRST,
    'value_2': MyEnum2.B,
    'value_3': MyEnum1.THIRD,
    'value_4': None,
    'value_5': MyEnum1.THIRD  # 会引用之前的枚举值 &id001 => *id001
}


data = []
data.append(enum_dict)
data.append(enum_dict1)


def represent_myclass(dumper, data):
    return dumper.represent_mapping('tag:yaml.org,2002:map', {
        'name': data.name,
        'data': data.data
    })


class MyClass:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MyClass):
            return self.name == o.name
        return False


class MySafeDumper(yaml.SafeDumper):
    def represent_data(self, data):
        if isinstance(data, MyEnum1):
            return self.represent_data(data.value)
        if isinstance(data, MyEnum2):
            return self.represent_data(data.value)
        return super().represent_data(data)


MySafeDumper.add_representer(MyClass, represent_myclass)

# 将字典中的枚举值转储为 YAML 文件
# with open('multiple_enums.yaml', 'w') as file:
output_yaml = yaml.dump(
    data, Dumper=MySafeDumper, default_flow_style=False, allow_unicode=True)
print(output_yaml)

object = MyClass("test", data)
output_yaml = yaml.dump(object, Dumper=MySafeDumper,
                        default_flow_style=False, allow_unicode=True)
print(output_yaml)
