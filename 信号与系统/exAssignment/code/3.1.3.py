import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定义系统传递函数 H(s)=1/(s+2)
num = [1]       # 分子
den = [1, 2]    # 分母 s+2
system = signal.lti(num, den)

# 定义时间轴（例如观察两个周期）
t = np.linspace(0, 8, 8000)

# 定义周期三角波输入 x(t)
T = 4.0
def x_signal(t):
    t_mod = np.mod(t, T)  # 将 t 映射到 [0, T) 内
    return np.where(t_mod <= T/2, t_mod, 4 - t_mod)

x = x_signal(t)

# 利用 lsim 求解系统响应（初始条件默认为 0）
t_out, y_out, _ = signal.lsim(system, U=x, T=t)

# 绘制输入与输出
plt.figure(figsize=(10, 6))
plt.plot(t, x, 'k--', label='输入 x(t)')
plt.plot(t_out, y_out, 'r-', label='输出 y(t)')
plt.title('系统响应：H(jω)=1/(2+jω)')
plt.xlabel('时间 t')
plt.ylabel('响应 y(t)')
plt.legend()
plt.grid(True)
plt.show()