# # 12.2.3 数据划分与降维
import os
names = os.listdir('olivettifaces')
print(names[0:5])

from PIL import Image
img0 = Image.open('olivettifaces\\' + names[0])
img0.show()

print(img0)

# 2.人脸数据处理 - 特征变量提取
import numpy as np
img0 = img0.convert('L')
img0 = img0.resize((32, 32))
arr = np.array(img0)
print(arr)

import pandas as pd
pd.DataFrame(arr)
arr = arr.reshape(1, -1)
print(arr)

print(arr.flatten().tolist())

X = []
for i in names:
    img = Image.open('olivettifaces\\' + i)
    img = img.convert('L')
    img = img.resize((32, 32))
    arr = np.array(img)
    X.append(arr.reshape(1, -1).flatten().tolist())

import pandas as pd
X = pd.DataFrame(X)
print(X)

print(X.shape)
# 3.人脸数据处理 - 目标变量提取
print(int(names[0].split('_')[0]))

y = []
for i in names:
    img = Image.open('olivettifaces\\' + i)
    y.append(int(i.split('_')[0]))

print(y)
# 1.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 2.PCA数据降维
from sklearn.decomposition import PCA
pca = PCA(n_components=100)
pca.fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

print(X_train_pca.shape)
print(X_test_pca.shape)

# pd.DataFrame(X_train_pca).head()
# pd.DataFrame(X_test_pca).head()

# # 12.2.4 模型的搭建与使用
# 1.模型搭建
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()  # 建立KNN模型  
knn.fit(X_train_pca, y_train)  # 用降维后的训练集进行训练模型

# 2.模型预测
y_pred = knn.predict(X_test_pca)  # 用降维后的测试集进行测试
print(y_pred)  # 将对测试集的预测结果打印出来

import pandas as pd
a = pd.DataFrame()  # 创建一个空DataFrame 
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()  # 查看表格前5行

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

score = knn.score(X_test_pca, y_test)
print(score)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()  # 建立KNN模型  
knn.fit(X_train, y_train)  # 不使用数据降维，直接训练
y_pred = knn.predict(X_test)  # 不使用数据降维，直接测试

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)
