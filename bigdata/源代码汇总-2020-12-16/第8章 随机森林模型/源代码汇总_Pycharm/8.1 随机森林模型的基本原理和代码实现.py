# # 8.1.3 随机森林模型的代码实现
from sklearn.ensemble import RandomForestClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = RandomForestClassifier(n_estimators=10, random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))

from sklearn.ensemble import RandomForestRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = RandomForestRegressor(n_estimators=10, random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))

