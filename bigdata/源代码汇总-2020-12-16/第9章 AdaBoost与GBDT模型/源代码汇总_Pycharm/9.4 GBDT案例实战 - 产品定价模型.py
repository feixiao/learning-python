# # 9.4 GBDT案例实战 - 产品定价模型
# # 9.4.2 模型搭建
# 1.读取数据
import pandas as pd
df = pd.read_excel('产品定价模型.xlsx')
df.head()

df['类别'].value_counts()

df['彩印'].value_counts()

df['纸张'].value_counts()

# 2.分类型文本变量处理
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['类别'] = le.fit_transform(df['类别'])  # 处理类别

df['类别'].value_counts()

# df['类别'] = df['类别'].replace({'办公类': 0, '技术类': 1, '教辅类': 2})
# df['类别'].value_counts()

le = LabelEncoder()
df['纸张'] = le.fit_transform(df['纸张'])

df.head()

# 3.提取特征变量和目标变量
X = df.drop(columns='价格')
y = df['价格']  

# 4.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 5.模型训练及搭建
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(random_state=123)
model.fit(X_train, y_train)

# 9.4.3 模型预测及评估
y_pred = model.predict(X_test)
print(y_pred[0:50])

a = pd.DataFrame()  # 创建一个空DataFrame
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

print(model.score(X_test, y_test))

from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)

print(model.feature_importances_)

features = X.columns  # 获取特征名称
importances = model.feature_importances_  # 获取特征重要性

importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)