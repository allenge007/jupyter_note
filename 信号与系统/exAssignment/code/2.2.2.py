import numpy as np # 导入numpy库
import matplotlib.pyplot as plt # 导入matplotlib库
import scipy.signal as sg # 导入scipy库中的信号处理模块

# --- 离散时间卷积 ---
x = [3, 2, 1, -2, 1, 0, 4, 0, 3]
h = [-1, -2, 3, -4, 3, 2, 1]
y_dis = sg.convolve(x, h, 'full')
n_x = np.arange(0, len(x))
n_h = np.arange(0, len(h))
n_y = np.arange(0, len(y_dis))

fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

ax1.stem(n_x, x, basefmt="-")
ax1.set_title('x[n]')
ax1.grid(True)

ax2.stem(n_h, h, basefmt="-")
ax2.set_title('h[n]')
ax2.grid(True)

ax3.stem(n_y, y_dis, basefmt="-")
ax3.set_title('x[n] * h[n]')
ax3.set_xlabel('n')
ax3.grid(True)

plt.tight_layout()
plt.show()