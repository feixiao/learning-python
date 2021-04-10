# # 3.2 线性回归模型评估
# # 3.2.1 模型评估的编程实现
# 3.1.3 代码汇总 ：不同行业工作年限与收入的线性回归模型

import pandas as pd
df = pd.read_excel('IT行业收入表.xlsx')
df.head()

X = df[['工龄']]
Y = df['薪水']

import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
print(est.summary())

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_ = poly_reg.fit_transform(X)

import statsmodels.api as sm
X2 = sm.add_constant(X_)
est = sm.OLS(Y, X2).fit()
print(est.summary())

# 1.读取数据
import pandas
df = pandas.read_excel('IT行业收入表.xlsx')
X = df[['工龄']]
Y = df['薪水']

# 2.模型训练
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)

from sklearn.metrics import r2_score
r2 = r2_score(Y, regr.predict(X))
print(r2)
