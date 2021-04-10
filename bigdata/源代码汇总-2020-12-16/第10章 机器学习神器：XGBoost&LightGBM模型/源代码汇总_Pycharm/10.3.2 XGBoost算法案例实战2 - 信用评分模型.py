# 1.读取数据
import pandas as pd
df = pd.read_excel('信用评分卡模型.xlsx')

# 2.提取特征变量和目标变量
X = df.drop(columns='信用评分')
Y = df['信用评分']

# 3.划分测试集和训练集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 4.模型训练及搭建
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)

# 5.模型预测及评估
y_pred = model.predict(X_test)
print(y_pred[0:10])

a = pd.DataFrame()  # 创建一个空DataFrame
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)

print(model.score(X_test, y_test))

# 6.查看特征重要性
features = X.columns
importances = model.feature_importances_

importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)

# **补充知识点1：XGBoost回归模型的参数调优**
from sklearn.model_selection import GridSearchCV
parameters = {'max_depth': [1, 3, 5], 'n_estimators': [50, 100, 150], 'learning_rate': [0.01, 0.05, 0.1, 0.2]}
clf = XGBRegressor()  # 构建回归模型
grid_search = GridSearchCV(model, parameters, scoring='r2', cv=5) 

grid_search.fit(X_train, y_train)
print(grid_search.best_params_ )

# {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 50}

model = XGBRegressor(max_depth=3, n_estimators=50, learning_rate=0.1)
model.fit(X_train, y_train)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)

# 0.688

# **补充知识点2：对于XGBoost模型，有必要做很多数据预处理吗？**
from sklearn.preprocessing import StandardScaler
X_new = StandardScaler().fit_transform(X)
print(X_new)

# 3.划分测试集和训练集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=123)

# 4.建模
from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X_train, y_train)

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)
