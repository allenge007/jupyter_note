import numpy as np # 导入numpy库
import matplotlib.pyplot as plt # 导入matplotlib库
import scipy.signal as sg # 导入scipy库中的信号处理模块

fs = 100
t1 = np.array([t/fs for t in range(-200,211)])
x1 = np.array([1 if t>=0 else 0 for t in t1])
x2 = np.array([np.exp(-3*t) if t>=0 else 0 for t in t1])
y1 = sg.convolve(x1, x2)/fs
n = len(y1)
tt = np.linspace(-4, 4.21, n)

fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

ax1.plot(t1, x1)
ax1.set_title('x1(t)')
ax1.grid()

ax2.plot(t1, x2)
ax2.set_title('x2(t)')
ax2.grid()

ax3.plot(tt, y1)
ax3.set_title('conv(x1, x2)')
ax3.grid()

plt.tight_layout()
plt.show()