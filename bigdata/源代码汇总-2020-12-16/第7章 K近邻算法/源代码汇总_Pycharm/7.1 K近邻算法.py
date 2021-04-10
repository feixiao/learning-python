# # 第七章 K近邻算法
# # 1.K近邻算法简单代码演示
import pandas as pd
df = pd.read_excel('葡萄酒.xlsx')
print(df)

X_train = df[['酒精含量(%)','苹果酸含量(%)']]
y_train = df['分类']  

from sklearn.neighbors import KNeighborsClassifier as KNN
knn = KNN(n_neighbors=3)  
knn.fit(X_train, y_train)

X_test = [[7, 1]]  # X_test为测试集特征变量
answer = knn.predict(X_test)  
print(answer)

X_test = [[7, 1], [8, 3]]  # 这里能帮助理解为什么要写成二维数组的样式
answer = knn.predict(X_test)  
print(answer)

from sklearn.neighbors import KNeighborsRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = KNeighborsRegressor(n_neighbors=2)
model.fit(X, y)
print(model.predict([[5, 5]]))

# # 2.数据归一化代码演示
# 2.1 min-max标准化
import pandas as pd
df = pd.read_excel('葡萄酒2.xlsx')
X = df[['酒精含量(%)','苹果酸含量(%)']]
y = df['分类']  

from sklearn.preprocessing import MinMaxScaler
X_new = MinMaxScaler().fit_transform(X)
X_new

# 2.2 Z-score标准化
from sklearn.preprocessing import StandardScaler
X_new = StandardScaler().fit_transform(X)
X_new

# # 3.案例实战 - 手写数字识别模型
# 1.读取数据
import pandas as pd
df = pd.read_excel('手写字体识别.xlsx')
df.head()

# 2.提取特征变量和目标变
X = df.drop(columns='对应数字') 
y = df['对应数字']

# 3.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 4.模型搭建
from sklearn.neighbors import KNeighborsClassifier as KNN
knn = KNN(n_neighbors=5) 
knn.fit(X_train, y_train)

# 5.模型预测 - 预测数据结果
y_pred = knn.predict(X_test)
print(y_pred[0:100])

a = pd.DataFrame()  # 创建一个空DataFrame
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

score = knn.score(X_test, y_test)
print(score)
