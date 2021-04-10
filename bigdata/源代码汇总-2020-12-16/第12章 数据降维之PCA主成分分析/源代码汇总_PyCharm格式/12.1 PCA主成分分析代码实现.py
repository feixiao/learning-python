# # 12.1.2 PCA主成分分析代码实现
# 1.二维空间降维Python代码实现
import numpy as np
X = np.array([[1, 1], [2, 2], [3, 3]])
print(X)

import pandas as pd
X = pd.DataFrame([[1, 1], [2, 2], [3, 3]])
print(X)

from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)
X_transformed = pca.transform(X)

print(X_transformed)

print(X_transformed.shape)

print(pca.components_)

a = pca.components_[0][0]
b = pca.components_[0][1]
print(str(a) + ' * X + ' +  str(b) + ' * Y')

# 2.三维空间降维Python代码实现
import pandas as pd
X = pd.DataFrame([[45, 0.8, 9120], [40, 0.12, 2600], [38, 0.09, 3042], [30, 0.04, 3300], [39, 0.21, 3500]], columns=['年龄(岁)', '负债比率', '月收入(元)'])
print(X)

from sklearn.preprocessing import StandardScaler
X_new = StandardScaler().fit_transform(X)
print(X_new)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X_new)
X_transformed = pca.transform(X_new)

print(X_transformed)

print(pca.components_)

dim = ['年龄(岁)', '负债比率', '月收入(元)']
for i in pca.components_:
    formula = []
    for j in range(len(i)):
        formula.append(str(i[j]) + ' * ' + dim[j])
    print(" + ".join(formula))

dim = ['X', 'Y', 'Z']
for i in pca.components_:
    formula = []
    for j in range(len(i)):
        formula.append(str(i[j]) + ' * ' + dim[j])
    print(" + ".join(formula))

