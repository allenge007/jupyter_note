import numpy as np
import matplotlib.pyplot as plt

# 设置序列范围及定义 x[n]
N = 5
n = np.arange(-N, N+1)         # n从 -5 到 5，共 11 点
x = np.exp(-2 * np.abs(n))      # x[n] = e^(-2|n|)

fig = plt.figure(figsize=(12, 5))
ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
ax2 = plt.subplot2grid((2, 2), (1, 0))
ax3 = plt.subplot2grid((2, 2), (1, 1))

# 绘制 x[n]
ax1.stem(n, x)
ax1.set_title('x[n]')
ax1.set_xlabel('n')
ax1.grid(True)

# 选择均匀的频率网格：ω ∈ [-π, π)
num_w = 2048
w = np.linspace(-np.pi, np.pi, num_w, endpoint=False)
dw = w[1] - w[0]

# 计算 DTFT： X(e^(jω)) = Σₙ x[n] e^(-jωn)
# 利用矩阵乘法：令 x 为 (101,1) 的列向量，计算 exp(-j n ω) 得 (101, num_w) 数组，然后对 n 求和
X = np.sum(x[:, None] * np.exp(-1j * n[:, None] * w[None, :]), axis=0)

ax2.plot(w, X)
ax2.set_title(r'$X(e^{j\omega})$')
ax2.set_xlabel('ω (rad/sample)')
ax2.grid(True)


# 根据卷积特性，y[n] 的 DTFT = Y(e^(jω)) = X(e^(jω))^2
Y = X**2

# 计算逆 DTFT，求得 y[n] 的近似值
# 选取 n 范围为：从 -2N 到 2N（即 -100 到 100，共 201 点）
n_conv = np.arange(-2*N, 2*N+1)
y_freq = np.zeros(len(n_conv), dtype=complex)

# 离散化逆 DTFT公式： y[n] = (1/(2π)) Σ_{ω_i} Y(e^(jω_i)) exp(jω_i n) dw
for i, ni in enumerate(n_conv):
    y_freq[i] = np.sum(Y * np.exp(1j * w * ni)) * dw/(2*np.pi)
y_freq = y_freq.real   # 理论上 y[n] 为实数

# 绘制 |Y(e^(jω))|
ax3.plot(w, np.abs(Y))
ax3.set_title(r'$|Y(e^{j\omega})|$')
ax3.set_xlabel('ω (rad/sample)')
ax3.grid(True)

plt.tight_layout()
plt.show()

# 利用 np.convolve 进行卷积，mode='full' 得到长度 201 的序列
y_time = np.convolve(x, x, mode='full')
n_time = np.arange(-2*N, 2*N+1)  # 索引范围为 -100 到 100

# 绘制直接时域卷积的结果，与频域逆变换结果并排显示
plt.figure(figsize=(12,6))

# 左侧子图：频域逆变换得到的 y[n]
plt.subplot(1,2,1)
plt.stem(n_conv, y_freq, markerfmt='bo', basefmt='b-', label='频域逆变换')
plt.title('频域方法')
plt.xlabel('n')
plt.grid(True)
plt.legend(fontsize=10)

# 右侧子图：时域直接卷积得到的 y[n]
plt.subplot(1,2,2)
plt.stem(n_time, y_time, linefmt='r--', markerfmt='ro', basefmt='r-', label='时域卷积')
plt.title('时域卷积')
plt.xlabel('n')
plt.grid(True)
plt.legend(fontsize=10)

plt.suptitle('y[n] 比较：频域方法 vs. 时域卷积', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()