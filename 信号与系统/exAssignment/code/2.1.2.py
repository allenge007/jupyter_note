import numpy as np # 导入numpy库
import matplotlib.pyplot as plt # 导入matplotlib库
import scipy.signal as sg # 导入scipy库中的信号处理模块

n1 = np.linspace(0, 5, 6)  # 时间序列[0 1 2 3 4 5]
x1 = [1, 2, 1, 1, 0, -3]  # 信号x[n]
n2 = np.linspace(0, 2, 3)  # 时间序列[0 1 2]
x2 = [1, -1, 1]  # 信号h[n]
y = sg.convolve(x1, x2, 'full')  # 卷积
n3 = np.linspace(0, 7, 8)

fig = plt.figure(figsize=(10, 8))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

ax1.stem(n1, x1, basefmt="-")
ax1.set_title('x[n]')
ax1.grid(True)

ax2.stem(n2, x2, basefmt="-")
ax2.set_title('h[n]')
ax2.set_xticks(np.arange(0, 3, step=1.0))
ax2.grid(True)

ax3.stem(n3, y, basefmt="-")
ax3.set_title('Conv Sum y[n]')
ax3.set_xlabel('Time index n')
ax3.grid(True)

plt.tight_layout()
plt.show()