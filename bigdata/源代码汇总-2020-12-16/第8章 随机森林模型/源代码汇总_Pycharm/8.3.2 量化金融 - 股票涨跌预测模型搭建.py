# # 8.3.2 模型使用与评估
# **1.预测下一天的涨跌情况**
y_pred = model.predict(X_test)
print(y_pred)

a = pd.DataFrame()  # 创建一个空DataFrame 
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

y_pred_proba = model.predict_proba(X_test)
print(y_pred_proba[0:5])

# **2.模型准确度评估**
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)
print(model.score(X_test, y_test))

# **3.分析数据特征的重要性**
print(model.feature_importances_)

features = X.columns
importances = model.feature_importances_
a = pd.DataFrame()
a['特征'] = features
a['特征重要性'] = importances
a = a.sort_values('特征重要性', ascending=False)
print(a)

# # 8.3.3 参数调优
from sklearn.model_selection import GridSearchCV  # 网格搜索合适的超参数
parameters = {'n_estimators':[5, 10, 20], 'max_depth':[2, 3, 4, 5], 'min_samples_leaf':[5, 10, 20, 30]}
new_model = RandomForestClassifier(random_state=1)  # 构建分类器
grid_search = GridSearchCV(new_model, parameters, cv=6, scoring='accuracy')  # cv=6表示交叉验证6次，scoring='roc_auc'表示以ROC曲线的AUC评分作为模型评价准则, 默认为'accuracy', 即按准确度评分

grid_search.fit(X_train, y_train)  # 传入数据
print(grid_search.best_params_)  # 输出参数的最优值

# # 8.3.4 收益回测曲线绘制
X_test['prediction'] = model.predict(X_test)
X_test['p_change'] = (X_test['close'] - X_test['close'].shift(1)) / X_test['close'].shift(1)
X_test['origin'] = (X_test['p_change'] + 1).cumprod()
X_test['strategy'] = (X_test['prediction'].shift(1) * X_test['p_change'] + 1).cumprod()
X_test[['strategy', 'origin']].tail()

X_test[['strategy', 'origin']].dropna().plot()
plt.gcf().autofmt_xdate()
plt.show()
