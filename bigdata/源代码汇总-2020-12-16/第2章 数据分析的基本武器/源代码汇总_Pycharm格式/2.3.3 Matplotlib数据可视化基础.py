# (6) 中文显示问题
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
plt.title('中文标题')
plt.xlabel('中文X轴')
plt.ylabel('中文Y轴')
plt.show()

# (7) 绘制多图
import matplotlib.pyplot as plt
# 绘制第一个子图：折线图
ax1 = plt.subplot(221)  
plt.plot([1, 2, 3], [2, 4, 6])
# 绘制第二个子图：柱状图
ax2 = plt.subplot(222)  
plt.bar([1, 2, 3], [2, 4, 6])
# 绘制第三个子图：散点图
ax3 = plt.subplot(223)  
plt.scatter([1, 3, 5], [2, 4, 6])
# 绘制第四个子图：直方图
ax4 = plt.subplot(224)  
plt.hist([2, 2, 2, 3, 4])

plt.rcParams['figure.figsize'] = (8, 4)
plt.figure(1)
ax1 = plt.subplot(121)
plt.plot([1, 2, 3], [2, 4, 6])
ax2 = plt.subplot(122)
plt.plot([2, 4, 6], [4, 8, 10])
plt.figure(2)
plt.plot([1, 2, 3], [4, 5, 6])

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
ax1, ax2, ax3, ax4 = axes.flatten()
ax1.plot([1, 2, 3], [2, 4, 6])
ax2.bar([1, 2, 3], [2, 4, 6])
ax3.scatter([1, 3, 5], [2, 4, 6])
ax4.hist([2, 2, 2, 3, 4])

plt.rcParams['font.sans-serif'] = ['SimHei']
fig, axes = plt.subplots(2, 2, figsize=(10, 8)) 
ax1, ax2, ax3, ax4 = axes.flatten()
ax1.plot([1, 2, 3], [2, 4, 6])
ax1.set_title('子图1')
ax1.set_xlabel('日期')
ax1.set_ylabel('分数')
ax2.bar([1, 2, 3], [2, 4, 6])
ax3.scatter([1, 3, 5], [2, 4, 6])
ax4.hist([2, 2, 2, 3, 4])