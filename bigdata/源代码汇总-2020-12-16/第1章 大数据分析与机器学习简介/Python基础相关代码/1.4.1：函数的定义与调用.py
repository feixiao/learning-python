# =============================================================================
# 1.4.1函数的定义与调用 by 华能信托-王宇韬
# =============================================================================

# 定义及调用函数
def y(x):
    print(x+1)
y(1)  # 调用函数


def y(x):
    print(x+1)
y(1)  # 第一次调用函数
y(2)  # 第二次调用函数
y(3)  # 第三次调用函数

# 传入两个参数
def y(x, z):
    print(x + z + 1)
y(1, 2)


# 有时候不需要参数也可以定义函数，这个了解即可
def y():
    x = 1
    print(x+1)
y() # 调用函数


# 函数在实战中的应用展示
def baidu(company):
    # 这里是具体爬虫代码，之后会讲
    print(company + 'completed!')

companys = ['华能信托', '阿里巴巴', '百度集团', '腾讯', '京东', '万科', '华为集团']
for i in companys:
    baidu(i)

'''
复习：
对于"for i in 区域"来说，如果说这个区域是一个列表，那么那个i就表示这个列表里的每一个元素；
'''