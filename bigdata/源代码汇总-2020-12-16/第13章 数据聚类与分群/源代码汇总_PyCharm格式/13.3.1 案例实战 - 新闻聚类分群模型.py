# # 13.3 案例实战 - 新闻聚类分群模型
# # 13.3.2 文本数据的读取与处理
# # 1.读取数据
import pandas as pd
df = pd.read_excel('新闻.xlsx')
df.head()

print(df.shape)

# # 2.中文分词
# （1）简单演示
import jieba
word = jieba.cut('我爱北京天安门')
for i in word:
    print(i)

print(df.iloc[0]['标题'])

import jieba
word = jieba.cut(df.iloc[0]['标题'])
result = ' '.join(word)
print(result)

# （2）实战应用
import jieba
words = []
for i, row in df.iterrows():
    word = jieba.cut(row['标题'])
    result = ' '.join(word) 
    words.append(result)

print(words[0:3])

import jieba
words = []
for i, row in df.iterrows():
    words.append(' '.join(jieba.cut(row['标题'])))
print(words[0:3])

# （3）补充知识点：遍历DataFrame表格的函数 - iterrows()函数
for i, row in df.iterrows():
    print(i)
    print(row)

# # 3.文字转数字：通过建立词频矩阵构造特征变量
# ### 3.1 文本向量化基础：建立词频矩阵
from sklearn.feature_extraction.text import CountVectorizer
test = ['金融 科技 厉害', '华能 信托 厉害']
vect = CountVectorizer()
X = vect.fit_transform(test)
X = X.toarray()
print(X)

words_bag = vect.vocabulary_
print(words_bag)

# ### 3.2 将之前所有的新闻标题进行文本向量化，从而构造特征变量
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()
X = vect.fit_transform(words)
X = X.toarray()
print(X)

words_bag = vect.vocabulary_
print(words_bag)

print(len(words_bag))

# ### 3.3 简单示例 - 取前两条新闻演示
print(words[0])
print(words[1])

vect = CountVectorizer()  # 引入CountVectorizer()函数
X_test = vect.fit_transform(words[0:2])  # 将前两条新闻文本向量化
X_test = X_test.toarray()  # 将X_test转为数组
print(X_test)  # 查看生成的二维数组

words_bag = vect.vocabulary_  # 第一种查看词袋的方式
print(words_bag)  # 查看词袋

words_bag2 = vect.get_feature_names()  # 第二种查看词袋的方法
print(words_bag2)  # 第二种查看词袋的方式

import pandas as pd
df = pd.DataFrame(X_test, columns=words_bag2)
print(df)
