# # 13.1 KMeans算法
# # 13.1.2 KMeans算法的简单代码实现
# 1.构造数据
import numpy as np
data = np.array([[3, 2], [4, 1], [3, 6], [4, 7], [3, 9], [6, 8], [6, 6], [7, 7]])
print(data)

# 2.可视化展示
import matplotlib.pyplot as plt
plt.scatter(data[:, 0], data[:, 1], c="red", marker='o', label='samples')
plt.legend()
plt.show()

# 3.KMeans聚类（聚类成2类）
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=2)
kms.fit(data)

# 4.获取结果
label = kms.labels_
print(label)

# 5.结果可视化
plt.scatter(data[label == 0][:, 0], data[label == 0][:, 1], c="red", marker='o', label='class0')
plt.scatter(data[label == 1][:, 0], data[label == 1][:, 1], c="green", marker='*', label='class1')
plt.legend()

# 6.聚类成3类，并可视化呈现
kms_3 = KMeans(n_clusters=3)
kms_3.fit(data)
label_3 = kms_3.labels_
print(label_3)

plt.scatter(data[label_3 == 0][:, 0], data[label_3 == 0][:, 1], c="red", marker='o', label='class0')
plt.scatter(data[label_3 == 1][:, 0], data[label_3 == 1][:, 1], c="green", marker='*', label='class1')
plt.scatter(data[label_3 == 2][:, 0], data[label_3 == 2][:, 1], c="blue", marker='+', label='class2')
plt.legend()

# # 13.1.3 案例实战 - 银行客户分群模型
# 1.读取数据
import pandas as pd
data = pd.read_excel('客户信息.xlsx')
data.head()

# 2.可视化展示
import matplotlib.pyplot as plt
plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c="green", marker='*')
plt.xlabel('age')
plt.ylabel('salary')
plt.show()

# 3.数据建模
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=3, random_state=123)
kms.fit(data)
label = kms.labels_
label = kms.fit_predict(data)
print(label)

# 4.建模效果可视化展示
plt.scatter(data[label == 0].iloc[:, 0], data[label == 0].iloc[:, 1], c="red", marker='o', label='class0')
plt.scatter(data[label == 1].iloc[:, 0], data[label == 1].iloc[:, 1], c="green", marker='*', label='class1')
plt.scatter(data[label == 2].iloc[:, 0], data[label == 2].iloc[:, 1], c="blue", marker='+', label='class2')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()

# 5.补充知识点，查看各标签人的收入均值
print(data[label == 0].iloc[:, 1].mean())
print(data[label == 1].iloc[:, 1].mean())
print(data[label == 2].iloc[:, 1].mean())

