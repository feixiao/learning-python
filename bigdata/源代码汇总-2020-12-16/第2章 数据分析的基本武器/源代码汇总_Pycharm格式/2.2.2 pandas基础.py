# **2.2.2 Excel等文件的读取和写入**
import pandas as pd
data = pd.read_excel('data.xlsx')  # data为DataFrame结构
data.head()  # 通过head()可以查看前5行数据，如果写成head(10)则可以查看前10行数据

# 其中read_excel还可以设定参数，使用方式如下：
data = pd.read_excel('data.xlsx', sheet_name=0, encoding='utf-8')

data = pd.read_csv('data.csv')
data.head()

# read_csv也可以指定参数，使用方式如下：
data = pd.read_csv('data.csv', delimiter=',', encoding='utf-8')

# (2) 文件写入
data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A列','B列'])
data.to_excel('data_new.xlsx')

data.to_excel('data_new.xlsx', sheet_name=0, encoding='utf-8', index=False, columns=['A列','B列'])

data.to_csv('data_new.csv')

data.to_csv('演示.csv', index=False, encoding="utf_8_sig")
# **补充知识点：文件相对路径与绝对路径**
data.to_excel('E:\\大数据分析\\data.xlsx')  # 绝对路径推荐写法1，此时E盘要有一个名为“大数据分析”的文件夹
data.to_excel(r'E:\大数据分析\data.xlsx')  # 绝对路径推荐写法2，此时E盘要有一个名为“大数据分析”的文件夹

# **2.2.3 数据读取与筛选**
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
print(data)

# 1.按照行列进行数据筛选
# (1) 按照列来选取数据
a = data['c1']
print(a)

b = data[['c1']]
print(b)

c = data[['c1', 'c3']]
print(c)
# (2) 按照行来选取数据

a = data[1:3]
print(a)

b = data.iloc[1:3]
print(b)

c = data.iloc[-1]
print(c)

d = data.loc[['r2', 'r3']]
print(d)

e = data.head()
print(e)
# (3) 按照区块来选取
a = data[['c1', 'c3']][0:2]  # 也可写成data[0:2][['c1', 'c3']]
print(a)

b = data.iloc[0:2][['c1', 'c3']]
print(b)

c = data.iloc[0]['c3']
print(c)

d = data.loc[['r1', 'r2'], ['c1', 'c3']]
e = data.iloc[0:2, [0, 2]]  
print(d)
print(e)

f = data.ix[0:2, ['c1', 'c3']]
print(f)

