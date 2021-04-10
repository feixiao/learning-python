# # 10.6 LightGBM算法案例实战2 - 广告收益回归预测模型
# **10.6.2 模型搭建**
# 读取数据
import pandas as pd
df = pd.read_excel('广告收益数据.xlsx')
df.head()

# 1.提取特征变量和目标变量
X = df.drop(columns='收益') 
y = df['收益']  

# 2.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 3. 模型训练和搭建
from lightgbm import LGBMRegressor
model = LGBMRegressor()
model.fit(X_train, y_train)

# **10.6.3 模型预测及评估**
y_pred = model.predict(X_test)
print(y_pred[0:5])

a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

X = [[71, 11, 2]]
print(model.predict(X))

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)

print(model.score(X_test, y_test))

print(model.feature_importances_)

# **10.6.4 模型参数调优**
from sklearn.model_selection import GridSearchCV
parameters = {'num_leaves': [15, 31, 62], 'n_estimators': [20, 30, 50, 70], 'learning_rate': [0.1, 0.2, 0.3, 0.4]}
model = LGBMRegressor()  # 构建模型
grid_search = GridSearchCV(model, parameters,scoring='r2',cv=5)

grid_search.fit(X_train, y_train)
print(grid_search.best_params_)

model = LGBMRegressor(num_leaves=31, n_estimators=50,learning_rate=0.3)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

