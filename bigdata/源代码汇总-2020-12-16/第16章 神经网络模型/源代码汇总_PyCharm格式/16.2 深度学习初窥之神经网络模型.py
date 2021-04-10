# 1.数据读取
import pandas as pd
df = pd.read_excel('产品评价.xlsx')
df.head()

import jieba
words = []
for i, row in df.iterrows():
    words.append(' '.join(jieba.cut(row['评论'])))

# 3.文本向量化
from sklearn.feature_extraction.text import CountVectorizer
test = ['手机 外观 漂亮', '手机 图片 清晰']
vect = CountVectorizer()
X = vect.fit_transform(test)
X = X.toarray()

words_bag = vect.vocabulary_
print(words_bag)

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
X = vect.fit_transform(words)
X = X.toarray()
print(X)

words_bag = vect.vocabulary_
print(words_bag)
print(len(words_bag))


import pandas as pd
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.DataFrame(X).head()

# 4.目标变量提取
y = df['评价']
y.head()

# # 2.2 神经网络模型的搭建与使用
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

from sklearn.neural_network import MLPClassifier
mlp =MLPClassifier()  # 因为模型运行具有随机性，如果想让每次运行结果一致，可以设置random_state随机参数为任一数字，如MLPClassifier(random_state=123)
mlp.fit(X_train, y_train)

y_pred = mlp.predict(X_test)
print(y_pred)  # 因为模型运行具有随机性，所以这里得到的结果可能和书上的略有不同，如果想让每次运行结果一致，可以设置random_state随机参数为任一数字，如MLPClassifier(random_state=123)

a = pd.DataFrame()  # 创建一个空DataFrame
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

print(mlp.score(X_test, y_test))

comment = input('请输入您对本商品的评价：')
comment = [' '.join(jieba.cut(comment))]
print(comment)
X_try = vect.transform(comment)
y_pred = mlp.predict(X_try.toarray())
print(y_pred)

from sklearn.naive_bayes import GaussianNB
nb_clf = GaussianNB()
nb_clf.fit(X_train,y_train)

y_pred = nb_clf.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

