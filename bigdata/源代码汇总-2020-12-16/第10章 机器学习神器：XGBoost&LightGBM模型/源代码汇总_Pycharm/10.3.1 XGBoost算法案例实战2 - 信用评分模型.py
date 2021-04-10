# # 10.3 XGBoost算法案例实战2 - 信用评分模型
# **10.3.2 多元线性回归模型**
# 1.读取数据
import pandas as pd
df = pd.read_excel('信用评分卡模型.xlsx')
df.head()

# 2.提取特征变量和目标变量
X = df.drop(columns='信用评分')
Y = df['信用评分']

# 3.模型训练及搭建
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)

# 4.线性回归方程构造
print('各系数为:' + str(model.coef_))
print('常数项系数k0为:' + str(model.intercept_))

# 5.模型评估
import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
est.summary()

# **10.3.3 GBDT回归模型**
# 1.读取数据
import pandas as pd
df = pd.read_excel('信用评分卡模型.xlsx')

# 2.提取特征变量和目标变量
X = df.drop(columns='信用评分')
y = df['信用评分']

# 3.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# 5.模型预测及评估
y_pred = model.predict(X_test)
print(y_pred[0:10])

a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)

print(model.score(X_test, y_test))
