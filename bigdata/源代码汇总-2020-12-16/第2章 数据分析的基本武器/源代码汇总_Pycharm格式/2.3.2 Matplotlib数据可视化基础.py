# **2.3.2 数据可视化常见小技巧**
# (1) 添加文字说明
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
plt.title('TITLE')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# (2) 添加图例
import numpy as np
import matplotlib.pyplot as plt
# 第一条线, 设定标签lable为y = x + 1
x1 = np.array([1, 2, 3])
y1 = x1 + 1
plt.plot(x1, y1, label='y = x + 1') 
# 第二条线, 设定标签lable为y = x*2
y2 = x1*2
plt.plot(x1, y2, color='red', linestyle='--', label='y = x*2')
plt.legend(loc='upper left')
plt.show()

# (3) 设置双坐标轴
import numpy as np
import matplotlib.pyplot as plt
# 第一条线, 设定标签lable为y = x
x1 = np.array([10, 20, 30])
y1 = x1
plt.plot(x1, y1, color='red', linestyle='--', label='y = x')
plt.legend(loc='upper left')
plt.twinx()
# 第二条线, 设定标签lable为y = x^2
y2 = x1*x1
plt.plot(x1, y2, label='y = x^2') 
plt.legend(loc='upper right')
plt.show()

# (4) 设置图片大小
plt.rcParams['figure.figsize'] = (8, 6)
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
plt.show()

# (4) 设置X轴角度
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
import pylab as pl
pl.xticks(rotation=45)
plt.show()
