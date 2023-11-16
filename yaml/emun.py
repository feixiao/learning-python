import enum
import yaml
from ruamel.yaml.representer import Representer

# 定义一个枚举类


class MyEnum(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

# 自定义输出函数


def enum_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', f'MyEnum.{data.name}')


# 将自定义输出函数注册到Representer中
Representer.add_representer(MyEnum, enum_representer)

# 将枚举类转储为 YAML 文件
with open('enum.yaml', 'w') as file:
    yaml.dump({'enum_value': MyEnum.SECOND}, file,
              default_flow_style=False, allow_unicode=True)
