# 2.按照特定条件筛选
a = data[data['c1'] > 1]
print(a)

b = data[(data['c1'] > 1) & (data['c2'] < 8)]
print(b)

# 3.数据整体情况查看
print(data.shape)

print(data.describe())

print(data['c1'].value_counts())

# 4.数据运算、排序与删除
# (1) 数据运算
data['c4'] = data['c3'] - data['c1']
data.head()

# (2) 数据排序
a = data.sort_values(by='c2', ascending=False)
print(a)

a = data.sort_values('c2', ascending=False)
print(a)

a = a.sort_index()
print(a)

# (3) 数据删除
a = data.drop(columns='c1')
print(a)

b = data.drop(columns=['c1', 'c3'])
print(b)

c = data.drop(index=['r1','r3'])
print(c)

data.drop(index=['r1','r3'], inplace=True)
print(data)

