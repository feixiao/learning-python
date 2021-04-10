# # 3.1 一元线性回归
# # 3.1.2 一元线性回归的代码实现
# 1.绘制散点图
import matplotlib.pyplot as plt
X = [[1], [2], [4], [5]]
Y = [2, 4, 6, 8]
plt.scatter(X, Y)
plt.show()

# 2.引入Scikit-learn库搭建模型
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)

# 3.模型预测
y = regr.predict([[1.5]])
print(y)

y = regr.predict([[1.5], [2.5], [4.5]])
print(y)

# 4.模型可视化
plt.scatter(X, Y)
plt.plot(X, regr.predict(X))
plt.show()

# 5.线性回归方程构造
print('系数a为:' + str(regr.coef_[0]))
print('截距b为:' + str(regr.intercept_))

# # 3.1.3 案例实战：工作年限与收入的线性回归模型

# 2.读取数据
import pandas as pd
df = pd.read_excel('IT行业收入表.xlsx')
df.head()

X = df[['工龄']]
Y = df['薪水']

from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.scatter(X,Y)
plt.xlabel('工龄')
plt.ylabel('薪水')
plt.show()

# 3.模型搭建
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X,Y)

# 4.模型可视化
plt.scatter(X,Y)
plt.plot(X, regr.predict(X), color='red')  # color='red'设置为红色
plt.xlabel('工龄')
plt.ylabel('薪水')
plt.show()

# 5.线性回归方程构造
print('系数a为:' + str(regr.coef_[0]))
print('截距b为:' + str(regr.intercept_))

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_ = poly_reg.fit_transform(X)

print(X_[0:5])

regr = LinearRegression()
regr.fit(X_, Y)

plt.scatter(X,Y)
plt.plot(X, regr.predict(X_), color='red')
plt.show()

print(regr.coef_)
print(regr.intercept_)

