# # 2.3 Matplotlib数据可视化基础
# **2.3.1 基本图形绘制**
# (1) 折线图
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
import pylab as pl
pl.xticks(rotation=45)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x1 = np.array([1, 2, 3])
# 第一条线：y = x + 1
y1 = x1 + 1
plt.plot(x1, y1)
# 第二条线：y = x*2
y2 = x1*2
plt.plot(x1, y2, color='red', linewidth=3, linestyle='--')
plt.show()

# (2) 柱状图
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
plt.bar(x, y)
plt.show()

# (3) 散点图
import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y)
plt.show()

# (4) 直方图
import matplotlib.pyplot as plt
import numpy as np  
data = np.random.randn(10000)
plt.hist(data, bins=40, edgecolor='black')
plt.show()

# **补充知识点：在pandas库中的快捷绘图技巧**
import pandas as pd
df = pd.DataFrame(data)
df.hist(bins=40, edgecolor='black')

df.plot(kind='hist')

import pandas as pd
df = pd.DataFrame([[8000, 6000], [7000, 5000], [6500, 4000]], columns=['人均收入', '人均支出'], index=['北京', '上海', '广州'])
print(df)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df['人均收入'].plot(kind='line')
df['人均收入'].plot(kind='bar')

