# # 9.2 案例实战 - AdaBoost信用卡精准营销模型
# # 9.2.2 模型搭建
# 1.读取数据
import pandas as pd
df = pd.read_excel('信用卡精准营销模型.xlsx')
df.head()

# 2.提取特征变量和目标变量
X = df.drop(columns='响应')
y = df['响应']

# 3.划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# 4.模型训练及搭建
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(random_state=123)
clf.fit(X_train, y_train)

# # 9.2.3 模型预测及评估
y_pred = clf.predict(X_test)
print(y_pred)

a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

y_pred_proba = clf.predict_proba(X_test)
print(y_pred_proba[0:5])

from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test.values, y_pred_proba[:,1])
import matplotlib.pyplot as plt
plt.plot(fpr, tpr)
plt.show()

from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_pred_proba[:,1])
print(score)

print(clf.feature_importances_)

features = X.columns  # 获取特征名称
importances = clf.feature_importances_  # 获取特征重要性

importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)

# 9.2.4 模型参数（选学）
from sklearn.ensemble import AdaBoostClassifier
AdaBoostClassifier?

from sklearn.ensemble import AdaBoostRegressor
AdaBoostRegressor?

