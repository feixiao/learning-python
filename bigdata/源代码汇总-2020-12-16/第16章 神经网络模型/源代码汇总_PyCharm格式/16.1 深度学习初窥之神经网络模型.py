# # 第16章 深度学习初窥之神经网络模型 - by 王宇韬
# # 1.神经网络模型简单代码实现
X = [[1, 0], [5, 1], [6, 4], [4, 2], [3, 2]]
y = [0, 1, 1, 0, 0]
from sklearn.neural_network import MLPClassifier
mlp =MLPClassifier()
mlp.fit(X, y)
y_pred = mlp.predict(X)

import pandas as pd
a = pd.DataFrame()  # 创建一个空DataFrame 
a['预测值'] = list(y_pred)
a['实际值'] = list(y)
print(a)

# 补充知识点 - 神经网络回归模型：MLPRegressor
from sklearn.neural_network import MLPRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = MLPRegressor(random_state=123)  # 设置random_state随机状态参数，使得每次训练的模型都是一样的
model.fit(X, y)
print(model.predict([[5, 5]]))

# # 2.案例实战 - 用户评论情感分析
# # 2.1 数据读取、中文分词、文本向量化
# 1.数据读取
import pandas as pd
df = pd.read_excel('产品评价.xlsx')
df.head()
# 2.中文分词
# jieba库分词示例
import jieba
word = jieba.cut('我爱北京天安门')
for i in word:
    print(i)
print(df.iloc[0])

import jieba
word = jieba.cut(df.iloc[0]['评论'])
result = ' '.join(word)
print(result)

words = []
for i, row in df.iterrows():
    word = jieba.cut(row['评论'])
    result = ' '.join(word) 
    words.append(result)
print(words[0:3])

words = []
for i, row in df.iterrows():
    words.append(' '.join(jieba.cut(row['评论'])))

# # iterrows()函数相关知识点，不熟悉DataFrame数据表遍历的话，可以把下面的注释取消了，看看效果
# for i, row in df.iterrows():
#     print(i)
#     print(row)

