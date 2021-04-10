# # 3.3 多元线性回归
# # 3.3.1 多元线性回归的数学原理和代码实现
# 2.读取数据
import pandas as pd
df = pd.read_excel('客户价值数据表.xlsx')
df.head()  # 显示前5行数据

X = df[['历史贷款金额', '贷款次数', '学历', '月收入', '性别']]
Y = df['客户价值']

# 3.模型搭建
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)

# 4.线性回归方程构造
regr.coef_

print('各系数为:' + str(regr.coef_))
print('常数项系数k0为:' + str(regr.intercept_))

# 5.模型评估
import statsmodels.api as sm  # 引入线性回归模型评估相关库
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
est.summary()

