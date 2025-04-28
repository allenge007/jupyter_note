import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif'] = ['SimSong']  # 指定支持中文的字体
matplotlib.rcParams['axes.unicode_minus'] = False    # 正确显示负号
# 信号参数
T = 4.0                     # 周期
omega0 = 2 * np.pi / T      # 基频
N_coef = 10                 # 计算系数范围：k=-10,...,10
t_period = np.linspace(0, T, 1000)  # 一个周期上的采样点

# 定义周期三角信号 x(t):
# 当 0<=t<=T/2 时，x(t)=t；当 T/2<t<=T 时，x(t)=4-t
def x_signal(t):
    t_mod = np.mod(t, T)  # 对 t 取模得到周期内坐标
    return np.where(t_mod <= T/2, t_mod, 4 - t_mod)

# 计算复指数傅立叶系数 a_k（在一个周期内积分）
a_k = {}
for k in range(-N_coef, N_coef+1):
    integrand = x_signal(t_period) * np.exp(-1j * k * omega0 * t_period)
    a = (1/T) * np.trapz(integrand, t_period)
    a_k[k] = a

# 将系数转换为数组便于绘图（按 k 从 -N_coef 到 N_coef排序）
k_vals = np.arange(-N_coef, N_coef+1)
a_vals = np.array([a_k[k] for k in k_vals])

# 绘制复指数傅立叶系数（实部、虚部及幅值、相位）
plt.figure(figsize=(12, 5))
plt.subplot(1,2,1)
plt.stem(k_vals, a_vals.real, basefmt=" ")
plt.stem(k_vals, a_vals.imag, linefmt='r--', markerfmt='ro', basefmt=" ")
plt.xlabel('k')
plt.ylabel('Coefficient')
plt.title('复指数傅立叶系数（实部：蓝，虚部：红）')
plt.grid(True)

plt.subplot(1,2,2)
plt.stem(k_vals, np.abs(a_vals), basefmt=" ")
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.title('傅立叶系数幅值')
plt.grid(True)
plt.tight_layout()
plt.show()

k_range = np.arange(0, N_coef+1)
cos_amp = [2 * a_k[k].real for k in k_range]    # 余弦项系数：2Re(aₖ)
sin_amp = [-2 * a_k[k].imag for k in k_range]   # 正弦项系数：-2Im(aₖ)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.stem(k_range, cos_amp, basefmt=" ")
plt.xlabel('k')
plt.ylabel('余弦项幅值')
plt.title('余弦项 ($2\Re(a_k)$)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(k_range, sin_amp, basefmt=" ")
plt.xlabel('k')
plt.ylabel('正弦项幅值')
plt.title('正弦项 ($-2\Im(aₖ)$)')
plt.grid(True)

plt.tight_layout()
plt.show()

# 构造时间轴用于重构和比较波形
t_full = np.linspace(-T, 2*T, 2000)
x_true = x_signal(t_full)

# 使用复指数形式重构有限项傅立叶级数：
# x_N(t) = sum_{k=-N}^{N} a_k * exp(j*k*omega0*t)
def reconstruct_complex(N, t):
    x_rec = np.zeros_like(t, dtype=complex)
    for k in range(-N, N+1):
        x_rec += a_k[k] * np.exp(1j * k * omega0 * t)
    return x_rec.real  # 原信号为实值

# 使用三角函数形式重构：
# 利用 a_0 和对于 k>=1, A_k=2|a_k| ，phi_k = angle(a_k)
def reconstruct_trig(N, t):
    a0 = a_k[0].real
    x_rec = a0 * np.ones_like(t)
    for k in range(1, N+1):
        A_k = 2 * np.abs(a_k[k])
        phi_k = np.angle(a_k[k])
        x_rec += A_k * np.cos(k * omega0 * t - phi_k)
    return x_rec

# 绘制有限项逼近：对 N=1,...,10 分别绘制复指数形式与三角函数形式的逼近结果
plt.figure(figsize=(12, 8))
for N in range(1, 11):
    x_rec_complex = reconstruct_complex(N, t_full)
    x_rec_trig = reconstruct_trig(N, t_full)
    plt.subplot(5, 2, N)
    plt.plot(t_full, x_true, 'k', label='真实信号')
    plt.plot(t_full, x_rec_complex, 'b--', label='复指数')
    plt.plot(t_full, x_rec_trig, 'r:', label='三角函数')
    plt.title(f'N = {N}')
    plt.xlim(-T, 2*T)
    plt.ylim(-0.5, 4.5)
    if N == 1:
        plt.legend(fontsize=8)
    plt.grid(True)
plt.tight_layout()
plt.show()