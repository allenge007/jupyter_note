import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg

# --- 连续时间卷积 ---
fs = 1000
t = np.arange(-1.1, 2.1, 1/fs)
u = lambda t: np.where(t >= 0, 1, 0)
x1 = t * u(t)
x2 = np.exp(-t) * u(t)
y = sg.convolve(x1, x2) / fs
# 卷积后时间轴
t_conv = np.arange(2*len(t)-1) / fs + (t[0] + t[0])

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.title(r'$x_1(t) = t u(t)$')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.title(r'$x_2(t) = e^{-t} u(t)$')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t_conv, y)
plt.title(r'$x_1(t) * x_2(t)$')
plt.grid()
plt.tight_layout()
plt.show()
