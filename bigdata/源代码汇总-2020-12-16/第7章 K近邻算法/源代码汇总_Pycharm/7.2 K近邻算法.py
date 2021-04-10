# # 4.补充知识点：图像识别原理详解
# 4.1 图片大小调整及显示
from PIL import Image
img = Image.open('数字4.png')
img = img.resize((32,32))
img.show()
img

# 4.2 图片灰度处理
img = img.convert('L')
print(img)

# 4.3 图片二值化处理
import numpy as np
img_new = img.point(lambda x: 0 if x > 128 else 1)
arr = np.array(img_new)
for i in range(arr.shape[0]):
    print(arr[i])

# 4.4 二维数组转一维数组
arr_new = arr.reshape(1, -1)
print(arr_new)

print(arr_new.shape)

answer = knn.predict(arr_new)
print('图片中的数字为：' + str(answer[0]))

# # 5.代码汇总与测试
# 1.训练模型
# 1.1 读取数据
import pandas as pd
df = pd.read_excel('手写字体识别.xlsx')

# 1.2 提取特征变量和目标变量
X = df.drop(columns='对应数字') 
y = df['对应数字']   

# 1.3 划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 1.4 训练模型
from sklearn.neighbors import KNeighborsClassifier as KNN
knn = KNN(n_neighbors=5) 
knn.fit(X_train, y_train)

# 2.处理图片
# 2.1 图片读取 & 大小调整 & 灰度处理
from PIL import Image
img = Image.open('测试图片.png')
img = img.resize((32,32))
img = img.convert('L')

# 2.2 图片二值化处理 & 二维数据转一维数据
import numpy as np
img_new = img.point(lambda x: 0 if x > 128 else 1)
arr = np.array(img_new)
arr_new = arr.reshape(1, -1)

# 3.预测手写数字
answer = knn.predict(arr_new) 
print('图片中的数字为：' + str(answer[0]))

