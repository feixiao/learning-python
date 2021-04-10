# # 2.2 pandas基础
# **2.2.0 引言**
import pandas as pd
s1 = pd.Series(['丁一', '王二', '张三'])
print(s1)

print(s1[1])
# **2.2.1 二维数据表格DataFrame的创建**
import pandas as pd
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
print(a)
a  # 在Jupyter Nobebook中，代码框中最后一行代码可以只输入变量名称，即可自动打印，而无需通过print()函数

a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
print(a)

a = pd.DataFrame()
date = [1, 3, 5]
score = [2, 4, 6]
a['date'] = date
a['score'] = score
print(a)

# (2) 通过字典创建DataFrame
b = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'])
print(b)

c = pd.DataFrame.from_dict({'a': [1, 3, 5], 'b': [2, 4, 6]}, orient="index")
print(c)

# **补充知识点：通过.T来对表格进行转置**
b = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]})
print(b)
print(b.T)

# (3) 通过二维数组创建
import numpy as np
c=np.arange(12).reshape(3,4)
print(c)

import numpy as np
d = pd.DataFrame(np.arange(12).reshape(3,4), index=[1, 2, 3], columns=['A', 'B', 'C', 'D'])
print(d)

# **补充知识点：修改行索引或列索引名称**
a = pd.DataFrame([[1, 2], [3, 4]], columns=['date', 'score'], index=['A', 'B'])
print(a)

a = a.rename(index={'A':'阿里', 'B':'腾讯'}, columns={'date':'日期','score':'分数'})
print(a)

# 补充知识点：这里通过rename之后并没有改变原表格结构，需要重新赋值给a才能改变原表格;或者在rename()中设置inplace参数为True，也能实现真正替换，代码如下：
a = pd.DataFrame([[1, 2], [3, 4]], columns=['date', 'score'], index=['A', 'B'])
#a = a.rename(index={'A':'阿里', 'B':'腾讯'}, columns={'date':'日期','score':'分数'})
a.rename(index={'A':'阿里', 'B':'腾讯'}, columns={'date':'日期','score':'分数'}, inplace=True)  # 另一种方法
print(a)

print(a.index.values)

a.index.name = '公司'
print(a)

a = a.set_index('日期')
print(a)

a = a.reset_index()
print(a)