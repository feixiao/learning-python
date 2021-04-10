# # 10.4.3 LightGBM算法的简单代码实现
# 1.分类模型
from lightgbm import LGBMClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = LGBMClassifier()
model.fit(X, y)
print(model.predict([[5, 5]]))

# 2.回归模型
from lightgbm import LGBMRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]

model = LGBMRegressor()
model.fit(X, y)

print(model.predict([[5, 5]]))
