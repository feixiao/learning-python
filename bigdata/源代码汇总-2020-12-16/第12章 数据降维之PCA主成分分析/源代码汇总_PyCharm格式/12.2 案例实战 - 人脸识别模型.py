# # 12.2 案例实战 - 人脸识别模型
# # 12.2.2 人脸数据读取、处理与变量提取
# 1.读取人脸照片数据
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
