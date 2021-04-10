# # 10.5 LightGBM算法案例实战1 - 客户违约预测模型
# **10.5.2 模型搭建**
# 1.读取数据
import pandas as pd
df = pd.read_excel('客户信息及违约表现.xlsx')
df.head()

# 2.提取特征变量和目标变量
X = df.drop(columns='是否违约')
Y = df['是否违约']

# 3.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=123)

# 4.模型训练及搭建
from lightgbm import LGBMClassifier
model = LGBMClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

print(model.score(X_test, y_test))

y_pred_proba = model.predict_proba(X_test)

from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:,1])
import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.show()

from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_pred_proba[:,1])
print(score)

print(model.feature_importances_)

features = X.columns
importances = model.feature_importances_

importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)

# **10.5.4 模型参数调优**
from sklearn.model_selection import GridSearchCV
parameters = {'num_leaves': [10, 15, 31], 'n_estimators': [10, 20, 30], 'learning_rate': [0.05, 0.1, 0.2]}
model = LGBMClassifier()  # 构建分类器
grid_search = GridSearchCV(model, parameters, scoring='roc_auc', cv=5)

grid_search.fit(X_train, y_train)
print(grid_search.best_params_)

model = LGBMClassifier(num_leaves=15, n_estimators=20,learning_rate=0.1)
model.fit(X_train, y_train)

y_pred_proba = model.predict_proba(X_test)
from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:,1])
import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.show()

y_pred_proba = model.predict_proba(X_test)
from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_pred_proba[:, 1])
print(score)

