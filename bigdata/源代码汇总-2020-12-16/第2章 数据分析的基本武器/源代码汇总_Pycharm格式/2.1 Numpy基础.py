# # 2.1 Numpy基础

# **2.1.1 Numpy与数组**
import numpy as np
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
print(a)
print(b)
print(type(a))
print(type(b))

print(a[1])
print(b[1])
print(a[0:2]) 
print(b[0:2])

# **2.1.2 Numpy数组与列表的区别**
c = a * 2
d = b * 2
print(c)
print(d)

e = [[1,2], [3,4], [5,6]]
f = np.array([[1,2], [3,4], [5,6]])
print(e)
print(f)

# **2.1.3 创建数组的几种方式**
b = np.array([1, 2, 3, 4])
f = np.array([[1,2], [3,4], [5,6]])
print(b)
print(f)

x = np.arange(5)
y = np.arange(5,10)
z = np.arange(5, 10, 0.5)
print(x)
print(y)
print(z)

a = np.random.randn(3)
print(a)

a = np.arange(12).reshape(3,4)
print(a)

a = np.random.randint(0, 10, (4, 4))
print(a)