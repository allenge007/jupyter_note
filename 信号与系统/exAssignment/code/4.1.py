import numpy as np
import matplotlib.pyplot as plt

# 为了近似无限长序列，设取 n 从 -50 到 50
N = 50
n = np.arange(-N, N+1)

# 定义双边指数衰减信号 x[n] = e^{-2|n|}
x = np.exp(-2 * np.abs(n))

# 定义频率网格（单位：rad/sample），覆盖 -π 到 π
w = np.linspace(-np.pi, np.pi, 1024)

# 计算 DTFT: X(w) = \sum_{n=-N}^N x[n] e^{-jωn}
X = np.sum(x[:, None] * np.exp(-1j * np.outer(n, w)), axis=0)

# 定义插值后的序列 x_k[n]
# 当 n 能被 3 整除时，令 m = n/3，x_k[n] = x[m] = e^{-2|m|}；否则为 0
xk = np.where(n % 3 == 0, np.exp(-2 * np.abs(n // 3)), 0)
Xk = np.sum(xk[:, None] * np.exp(-1j * np.outer(n, w)), axis=0)

# 绘制 x[n] 的 DTFT 幅频和相频曲线
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(w, np.abs(X))
plt.xlabel(r'$\omega$ (rad/sample)')
plt.ylabel('Magnitude')
plt.title(r'Magnitude of $X(e^{j\omega})$ for $x[n]=e^{-2|n|}$')
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(w, np.angle(X))
plt.xlabel(r'$\omega$ (rad/sample)')
plt.ylabel('Phase (rad)')
plt.title(r'Phase of $X(e^{j\omega})$ for $x[n]=e^{-2|n|}$')
plt.grid(True)
plt.tight_layout()
plt.show()

# 绘制 x_k[n] 的 DTFT 幅频和相频曲线
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(w, np.abs(Xk))
plt.xlabel(r'$\omega$ (rad/sample)')
plt.ylabel('Magnitude')
plt.title(r'Magnitude of $X_k(e^{j\omega})$ for interpolated $x_k[n]$ ($k=3$)')
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(w, np.angle(Xk))
plt.xlabel(r'$\omega$ (rad/sample)')
plt.ylabel('Phase (rad)')
plt.title(r'Phase of $X_k(e^{j\omega})$ for interpolated $x_k[n]$ ($k=3$)')
plt.grid(True)
plt.tight_layout()
plt.show()