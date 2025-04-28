import numpy as np # 导入numpy库
import matplotlib.pyplot as plt # 导入matplotlib库

# 定义单位阶跃函数
def u(t):
    return np.where(t >= 0, 1, 0)

# 定义 x(t)
def x(t):
    return u(t) - u(t - 2) + u(t - 0.5) - u(t - 1.5)

t = np.linspace(0, 3, 1000)

# 原始信号
y = x(t)
# x(-2t)
y1 = x(-2 * t)
# x(t/2 + 1)
y2 = x(t / 2 + 1)
# 5x(t)
y3 = 5 * x(t)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, y1)
plt.title(r'$x(-2t)$')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, y2)
plt.title(r'$x(\frac{t}{2}+1)$')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, y3)
plt.title(r'$5x(t)$')
plt.grid()

plt.tight_layout()
plt.show()