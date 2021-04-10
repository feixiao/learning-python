# **2.2.4 数据表拼接**
import pandas as pd
df1 = pd.DataFrame({'公司': ['万科', '阿里', '百度'], '分数': [90, 95, 85]})
df2 = pd.DataFrame({'公司': ['万科', '阿里', '京东'], '股价': [20, 180, 30]})

print(df1)
print(df2)

# (1) merge()函数
df3 = pd.merge(df1, df2)
print(df3)

df3 = pd.merge(df1, df2, how='outer')
print(df3)

df3 = pd.merge(df1, df2, how='left')
print(df3)

df3 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)

# **补充知识点：根据行索引合并的join()函数**
df3 = df1.join(df2, lsuffix='_x', rsuffix='_y')
print(df3)

# (2) concat()函数
df3 = pd.concat([df1,df2], axis=0)
print(df3)

df3 = pd.concat([df1,df2],axis=1)
print(df3)

# (3) append()函数
df3 = df1.append(df2)
print(df3)

df3 = df1.append({'公司': '腾讯', '分数': '90'}, ignore_index=True)
print(df3)