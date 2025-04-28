import numpy as np
import matplotlib.pyplot as plt

# 信号周期和基本频率
T = 4.0     
omega0 = 2 * np.pi / T

# 定义周期三角波：当 0<=t<=T/2 时，x(t)=t；当 T/2<t<=T 时，x(t)=4-t
def x_triangle(t):
    t_mod = np.mod(t, T)
    return np.where(t_mod <= T/2, t_mod, 4 - t_mod)

# 定义周期方波：当 0<=t<T/2 时取 1，T/2<=t<T 时取 -1
def x_square(t):
    t_mod = np.mod(t, T)
    return np.where(t_mod < T/2, 1.0, -1.0)

# 采样点用于数值积分（在一个周期内）
t_period = np.linspace(0, T, 10000)

# 计算傅立叶系数
def compute_fourier_coeffs(x_func, N_coef):
    a_k = {}
    for k in range(-N_coef, N_coef+1):
        integrand = x_func(t_period) * np.exp(-1j * k * omega0 * t_period)
        a = (1/T) * np.trapz(integrand, t_period)
        a_k[k] = a
    return a_k

# 利用复指数形式重构信号
def reconstruct_signal(a_k, N, t):
    x_rec = np.zeros_like(t, dtype=complex)
    for k in range(-N, N+1):
        x_rec += a_k[k] * np.exp(1j * k * omega0 * t)
    return x_rec.real  # 原信号均为实值

# 为了得到较高精度的傅立叶系数，这里计算较宽的系数范围
N_coef_all = 1000  
a_k_triangle = compute_fourier_coeffs(x_triangle, N_coef_all)
a_k_square = compute_fourier_coeffs(x_square, N_coef_all)

# 构造时间轴用于重构（显示多个周期以便观察边缘）
t_full = np.linspace(-T, 2*T, 2000)

# 不同截断数
Ns = [10, 100, 1000]

# 绘制周期三角波的有限项逼近
plt.figure(figsize=(12, 8))
for i, N in enumerate(Ns, 1):
    x_rec = reconstruct_signal(a_k_triangle, N, t_full)
    plt.subplot(len(Ns), 1, i)
    plt.plot(t_full, x_triangle(t_full), 'k', lw=2, label='真实信号')
    plt.plot(t_full, x_rec, 'r--', lw=1.5, label=f'逼近 N={N}')
    plt.title(f'周期三角波 Fourier 级数逼近 (N={N})')
    plt.xlim(-T, 2*T)
    plt.ylim(-0.5, 4.5)
    plt.grid(True)
    if i == 1:
        plt.legend()
plt.tight_layout()
plt.show()

# 绘制周期方波的有限项逼近
plt.figure(figsize=(12, 8))
for i, N in enumerate(Ns, 1):
    x_rec = reconstruct_signal(a_k_square, N, t_full)
    plt.subplot(len(Ns), 1, i)
    plt.plot(t_full, x_square(t_full), 'k', lw=2, label='真实信号')
    plt.plot(t_full, x_rec, 'r--', lw=1.5, label=f'逼近 N={N}')
    plt.title(f'周期方波 Fourier 级数逼近 (N={N})')
    plt.xlim(-T, 2*T)
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    if i == 1:
        plt.legend()
plt.tight_layout()
plt.show()

# 分析说明
print("观察结果：")
print("1. 对于周期方波，因信号存在跳变，不连续点附近会出现明显的振铃现象，即吉布斯现象，该现象不会随截断项数无限增加而消失。")
print("2. 而周期三角波信号本身连续，虽然在导数处有不连续，其傅立叶逼近不会出现明显的振铃，逼近效果较好。")