# # 9.1 AdaBoost模型简单代码实现
# 1.AdaBoost分类模型演示
from sklearn.ensemble import AdaBoostClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = AdaBoostClassifier(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))

# 2.AdaBoost回归模型演示
from sklearn.ensemble import AdaBoostRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = AdaBoostRegressor(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
