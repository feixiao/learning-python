# # 1.读取数据
import pandas as pd
df = pd.read_excel('新闻.xlsx')
df.head()

import jieba
words = []
for i, row in df.iterrows():
    words.append(' '.join(jieba.cut(row['标题'])))
print(words[0:3])

# ### 3.4 将所有新闻文本向量化并展示
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

vect = CountVectorizer()
X = vect.fit_transform(words)  # 将分词后的内容文本向量化
X = X.toarray()

words_bag2 = vect.get_feature_names()  # 第二种查看词袋的方法
df = pd.DataFrame(X, columns=words_bag2)
df.head()

# # 如果想显示pandas中DataFrmae所有行，或者所有列，可以采用下面的代码
# import pandas as pd
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# df = pd.DataFrame(X, columns=words_bag2)
# df.head()

# # 13.3.3 模型搭建与使用
# # 1.通过KMeans算法进行聚类分群
from sklearn.cluster import KMeans
kms = KMeans(n_clusters=10, random_state=123)
k_data = kms.fit_predict(df)
print(k_data)

import numpy as np
words_ary = np.array(words)
print(words_ary[k_data == 1])  # 可以把数字1改成其他数字看看效果

# # 2.通过DBSCAN算法进行聚类分群
from sklearn.cluster import DBSCAN
dbs = DBSCAN(eps=1, min_samples=3)
d_data = dbs.fit_predict(df)
print(d_data)

# # 13.3.4 模型优化（利用余弦相似度进行优化）
# 1.余弦相似度基本概念
words_test = ['想去 华能 信托', '华能 信托 很好 想去', '华能 信托 很好 想去 华能 信托 很好 想去']

vect = CountVectorizer()
X_test = vect.fit_transform(words_test)  # 将分词后的内容文本向量化
X_test = X_test.toarray()

words_bag2 = vect.get_feature_names()  # 第二种查看词袋的方法
df_test = pd.DataFrame(X_test, columns=words_bag2)
df_test.head()

# 补充知识点：通过numpy库计算欧式距离
import numpy as np
dist = np.linalg.norm(df_test.iloc[0] - df_test.iloc[1])
print(dist)

from sklearn.metrics.pairwise import cosine_similarity
cosine_similarities  = cosine_similarity(df_test)
print(cosine_similarities)

# 2.余弦相似度实战 - 模型优化
from sklearn.metrics.pairwise import cosine_similarity
cosine_similarities  = cosine_similarity(df)
print(cosine_similarities)

from sklearn.cluster import KMeans
kms = KMeans(n_clusters=10, random_state=123)
k_data = kms.fit_predict(cosine_similarities)
print(k_data)

print(k_data == 3)

print(words[0:3])
words_ary = np.array(words)
print(words_ary[0:3])

import numpy as np
words_ary = np.array(words)
print(words_ary[k_data == 3])  # 可以把数字3改成其他数字看看效果

