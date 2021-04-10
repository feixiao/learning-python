# # 第十四章 智能推荐系统 - 协同过滤算法
# # 14.2 相似度计算三种常见方法
# 14.2.1 欧式距离
import pandas as pd
df = pd.DataFrame([[5, 1, 5], [4, 2, 2], [4, 2, 1]], columns=['用户1', '用户2', '用户3'], index=['物品A', '物品B', '物品C'])
print(df)

import numpy as np
dist = np.linalg.norm(df.iloc[0] - df.iloc[1])
print(dist)

# # 14.2.2 余弦内置函数
import pandas as pd
df = pd.DataFrame([[5, 1, 5], [4, 2, 2], [4, 2, 1]], columns=['用户1', '用户2', '用户3'], index=['物品A', '物品B', '物品C'])
print(df)

from sklearn.metrics.pairwise import cosine_similarity
user_similarity = cosine_similarity(df)
pd.DataFrame(user_similarity, columns=['物品A', '物品B', '物品C'], index=['物品A', '物品B', '物品C'])

# # 14.2.3 皮尔逊相关系数简单版
from scipy.stats import pearsonr
X = [1, 3, 5, 7, 9]
Y = [9, 8, 6, 4, 2]
corr = pearsonr(X, Y)
print('相关系数r值为' + str(corr[0]) + '，显著性水平P值为' + str(corr[1]))

import pandas as pd
df = pd.DataFrame([[5, 4, 4], [1, 2, 2], [5, 2, 1]], columns=['物品A', '物品B', '物品C'], index=['用户1', '用户2', '用户3'])  
print(df)

A = df['物品A']
corr_A = df.corrwith(A)
print(corr_A)

print(df.corr())

