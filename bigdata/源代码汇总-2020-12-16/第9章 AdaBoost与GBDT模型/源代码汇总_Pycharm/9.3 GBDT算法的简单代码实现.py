# # 9.3 GBDT算法的简单代码实现
# 1.GBDT分类模型演示
from sklearn.ensemble import GradientBoostingClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = GradientBoostingClassifier(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))

# 2.GBDT回归模型演示
from sklearn.ensemble import GradientBoostingRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = GradientBoostingRegressor(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
