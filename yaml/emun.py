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
        return dumper.represent_scalar('tag:yaml.org,2002:str', f'MyEnum2')


# 创建包含两种枚举类的字典
enum_dict = {
    'value_1': MyEnum1.FIRST,
    'value_2': MyEnum2.B,
    'value_3': MyEnum1.THIRD,
    'value_4': None,
    'value_5': MyEnum1.THIRD  # 会引用之前的枚举值 &id001 => *id001
}

# 将字典中的枚举值转储为 YAML 文件
# with open('multiple_enums.yaml', 'w') as file:
output_yaml = yaml.dump(
    enum_dict, default_flow_style=False, allow_unicode=True)
print(output_yaml)
