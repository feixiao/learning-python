# # 10.1.3 XGBoost算法的简单代码实现
# 1.分类模型
from xgboost import XGBClassifier
import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = [0, 0, 0, 1, 1]

model = XGBClassifier()
model.fit(X, y)

print(model.predict(np.array([[5, 5]])))

# 2.回归模型
from xgboost import XGBRegressor
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = [1, 2, 3, 4, 5]

model = XGBRegressor()
model.fit(X, y)

print(model.predict(np.array([[5, 5]])))
