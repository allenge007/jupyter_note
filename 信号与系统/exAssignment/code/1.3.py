import numpy as np # 导入numpy库
import matplotlib.pyplot as plt # 导入matplotlib库

# 定义 x[n]
def x_n(n):
    n = np.array(n)
    result = np.zeros_like(n, dtype=float)
    result[n < -2] = -1
    mask1 = (n >= -2) & (n <= 1)
    result[mask1] = n[mask1]
    mask2 = n > 1
    result[mask2] = 1 / n[mask2]
    return result

n = np.arange(-20, 21)

# x[-n]
y1 = x_n(-n)
# x[2n + 2]
y2 = x_n(2 * n + 2)
# x[n / 2]
# 由于 n/2 可能不是整数，这里用插值法
n_half = n / 2
y3 = x_n(n_half)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.stem(n, y1)
plt.title(r'$x[-n]$')
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, y2)
plt.title(r'$x[2n+2]$')
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n, y3)
plt.title(r'$x[n/2]$')
plt.grid()

plt.tight_layout()
plt.show()