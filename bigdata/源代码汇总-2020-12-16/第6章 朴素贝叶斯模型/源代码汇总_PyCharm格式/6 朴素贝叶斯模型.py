# # 第六章 朴素贝叶斯模型
# # 1. 朴素贝叶斯模型简单代码演示
from sklearn.naive_bayes import GaussianNB
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]

model = GaussianNB()
model.fit(X, y)

print(model.predict([[5, 5]]))

# # 2.案例实战 - 肿瘤预测模型
# 2.1 读取数据

import pandas as pd
df = pd.read_excel('肿瘤数据.xlsx')
df.head()

# 2.2 划分特征变量和目标变量

X = df.drop(columns='肿瘤性质') 
y = df['肿瘤性质']   

# 2.3 模型搭建
# 2.3.1 划分训练集和测试集

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 2.3.2 朴素贝叶斯模型

from sklearn.naive_bayes import GaussianNB
nb_clf = GaussianNB()  # 高斯朴素贝叶斯模型
nb_clf.fit(X_train,y_train)
