import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# (a) 求系统的频率响应 H(e^(jω)) 的幅频和相频特性
# ------------------------------
a = 0.2  # 取 a = 0.2

# 定义频率采样区间：从 -π 到 π（rad/sample）
omega = np.linspace(-np.pi, np.pi, 1024)

# 计算频率响应：H(e^(jω)) = 1 / (1 - a e^(-jω))
H = 1.0 / (1 - a * np.exp(-1j * omega))

# 分别取幅值和相位
H_magnitude = np.abs(H)
H_phase = np.angle(H)

fig = plt.figure(figsize=(12, 5))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

ax1.plot(omega, H_magnitude, 'b', linewidth=2)
ax1.set_title("系统幅频特性")
ax1.set_xlabel("频率 ω (rad/sample)")
ax1.set_ylabel("$|H(e^{jω)}|$")
ax1.grid(True)

ax2.plot(omega, H_phase, 'r', linewidth=2)
ax2.set_title("系统相频特性")
ax2.set_xlabel("频率 ω (rad/sample)")
ax2.set_ylabel("Phase($H(e^{jω})$) (radians)")
ax2.grid(True)

# ------------------------------
# (b) 求系统的单位冲激响应 h[n]
# ------------------------------
# 根据理论，h[n] = a^n * u[n]，这里 u[n] 为单位阶跃（n>=0）
n = np.arange(0, 50)   # 取 n 从 0 到 49
h = a ** n             # 对于 n<0 h[n]=0

ax3.stem(n, h, basefmt=" ")
ax3.set_title("系统单位冲激响应 h[n]")
ax3.set_xlabel("n")
ax3.set_ylabel("h[n]")
ax3.grid(True)
plt.tight_layout()
plt.show()