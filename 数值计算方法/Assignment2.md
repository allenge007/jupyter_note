# 1(3)

$$
f(1)=0,\quad f(-1)=-3,\quad f(2)=4.
$$

$$
x_0=1,\quad x_1=-1,\quad x_2=2
$$

牛顿插值法：

$$
\begin{aligned}
f[x_0,x_1] &= \frac{-3-0}{-1-1} = \frac{3}{2} \\
f[x_1,x_2] &= \frac{4-(-3)}{2-(-1)} = \frac{7}{3} \\
f[x_0,x_1,x_2] &= \frac{\frac{7}{3}-\frac{3}{2}}{2-1} = \frac{5}{6}
\end{aligned}
$$

$$
P(x) = \frac{3}{2}(x-1) + \frac{5}{6}(x-1)(x+1)
$$


# 3

   $$
   \delta \le 0.5 \times 10^{-5}
   $$

 $h = 1' = \pi/10800 \rm rad$
   $$
   E_{} \le \frac{1}{8}\left(\frac{\pi}{10800}\right)^2
   $$

$$
总误差 \le E+\delta
$$


# 4(2)

证明：对任意整数 $1\le k\le n$，
$$
\sum_{j=0}^{n}(x_j-x)^k\ell_j(x) \equiv 0
$$

$$
\begin{aligned}
\sum_{j = 0}^n(x_j - x)^k\ell_j(x)&\equiv
\sum_{m = 0}^k\sum_{j = 0}^n(-1)^mx^mx_j^{k - m}\ell_j(x) \\ &\equiv
\sum_{m = 0}^k(-1)^mx^m\sum_{j = 0}^nx_j^{k - m}\ell_j(x)\\ &\equiv
\sum_{m = 0}^k (-1)^mx^mx^{k-m} \\ &\equiv 
(x - x)^k \\ &\equiv 
0
\end{aligned}
$$

# 6

二次插值误差 $≤10^{-6}$，求 $h$：

$$
R(x)=\frac{f^{(3)}(\xi)}{3!}(x-x_0)(x-x_1)(x-x_2),
$$

令，

$$
\quad x_1=x_0+h,\quad x_2=x_0+2h.
$$

$$
t=x-x_0,\quad\text{\quad  } t\in[0,2h].
$$

有

$$
R(t)=\frac{f^{(3)}(\xi)}{6}\,t\,(t-h)\,(t-2h).
$$


$$
|P(t)|=|t\,(t-h)\,(t-2h)|
$$

求导解得级值点

$$
t = h\Bigl(1- \frac{1}{\sqrt{3}}\Bigr),
$$

带入得到

$$
\max_{t\in[0,2h]}|t\,(t-h)\,(t-2h)| = \frac{2h^3}{3\sqrt{3}}.
$$

又因为，

$$
M_3 = e^4.
$$

所以

$$
\frac{e^4\, h^3}{9\sqrt{3}} \le 10^{-6}.
$$


# 7

证明：

1.
$$
F=cf \Rightarrow F[...] = c·f[...]
$$

- 归纳基

$$
  F[x_0] = F(x_0) = c\, f(x_0) = c\, f[x_0].
  $$

- 归纳步
  $$
  F[x_0,x_1,\dots,x_n] = \frac{ c\, f[x_1,x_2,\dots,x_n] - c\, f[x_0,x_1,\dots,x_{n-1}]}{x_n-x_0}
  $$
  $$
  F[x_0,x_1,\dots,x_n] = c\,f[x_0,x_1,\dots,x_n].
  $$

2. 
$$
F=f+g \Rightarrow F[...] = f[...] + g[...]
$$

- 归纳基

$$
  F[x_0] = F(x_0)= f(x_0)+g(x_0)= f[x_0]+g[x_0].
  $$

- 归纳步
$$
\begin{aligned}
  F[x_0,x_1,\dots,x_n] &= \frac{\Bigl(f[\dots, x_n] + g[\dots, x_n]\Bigr) - \Bigl(f[\dots,x_{n-1}] + g[\dots,x_{n-1}]\Bigr)}{x_n-x_0} \\
  &= f[\dots,x_n] + g[\dots,x_n].
  \end{aligned}
  $$



# 8

$$
f(x)=x^7+x^4+3x+1
$$

$$
f[x_0, x_1, \cdots, x_n]=\frac{f^{(n)}(\xi)}{n!}
$$

7次多项式8阶导为0，7阶导数为 $7!$

# 9

$$
Δ(f_k g_k) = f_kΔg_k + g_{k+1}Δf_k
$$

证明：

   $$
   f_{k+1}g_{k+1} - f_kg_k = \Bigl[f_{k+1}g_{k+1} - f_k g_{k+1}\Bigr] + \Bigl[f_k g_{k+1} - f_k g_k\Bigr].
   $$


   $$
   f_{k+1}g_{k+1} - f_kg_{k+1} = g_{k+1}\bigl(f_{k+1} - f_k\bigr) = g_{k+1}\,\Delta f_k,
   $$

   $$
   f_k g_{k+1} - f_k g_k = f_k\bigl(g_{k+1} - g_k\bigr) = f_k\,\Delta g_k.
   $$


# 10

证明求和公式：
$$
\sum f_kΔg_k = f_n g_n - f_0 g_0 - \sum g_{k+1}Δf_k
$$

**证明**：


   $$
   f_n g_n - f_0 g_0 = \sum_{k=0}^{n-1}\Bigl( f_{k+1}g_{k+1} - f_k g_k \Bigr).
   $$


   $$
   \Delta(f_k g_k) = f_k\,\Delta g_k + g_{k+1}\,\Delta f_k.
   $$

   $$
   f_{k+1}g_{k+1} - f_k g_k = f_k\Delta g_k + g_{k+1}\Delta f_k.
   $$


   $$
   f_n g_n - f_0 g_0 = \sum_{k=0}^{n-1}\Bigl( f_k\Delta g_k + g_{k+1}\Delta f_k\Bigr)
   $$

   $$
   \sum_{k=0}^{n-1}f_k\Delta g_k = f_n g_n - f_0 g_0 - \sum_{k=0}^{n-1} g_{k+1}\Delta f_k.
   $$


# 11

$$
\sum Δ^2 y_j = Δy_n - Δy_0
$$

证明：

$$
\Delta y_n - \Delta y_0 = \sum_{j = 0}^{n - 1}\Delta y_{j + 1} - \Delta y_j = \sum_{j = 0}^{n - 1}\Delta^2y_j
$$

# 12

$$
\sum \frac{x_j^k}{f'(x_j)} = 
\begin{cases}
0, & 0≤k≤n-2 \\
a_n^{-1}, & k=n-1
\end{cases}
$$

设

$$
\omega_n (x) = (x - x_1)(x - x_2)\cdots(x - x_n)
$$

原式可化为

$$
\sum_{j = 1}^n\frac{x_j^k}{f'(x_j)} = \sum_{j = 1}^n\frac{x_j^k}{a_n\omega_n'(x_j)}
$$

$$
\omega_n'(x_j)=\prod_{k\neq j}(x_j - x_k)
$$

令 $g(x) = x^k$，则 $g[\dots]=\sum_{j=1}^n\frac{x_j^k}{\omega'_n(x_j)}$

又因为

$$
g[\cdots]=\frac{g^{(n-1)}(\xi)}{(n-1)!}
$$

故

$$
原式=\frac{1}{a_n}g[\dots]=\begin{cases}
0, &k \le n-2 \\
a_n^{-1}, &\rm otherwise
\end{cases}
$$

# 13

构造满足条件的三次多项式
$$
\begin{aligned}
P(x_0) &= f(x_0), \\
P'(x_0) &= f'(x_0), \\
P''(x_0) &= f''(x_0), \\
P(x_1) &= f(x_1).
\end{aligned}
$$

设

$$
P(x) = a_0 + a_1 (x-x_0) + a_2 (x-x_0)^2 + a_3 (x-x_0)^3.
$$

$$
\begin{aligned}
P'(x) &= a_1 + 2a_2 (x-x_0) + 3a_3 (x-x_0)^2,\quad P'(x_0)=a_1,\\[1mm]
P''(x) &= 2a_2 + 6a_3 (x-x_0),\quad P''(x_0)=2a_2.
\end{aligned}
$$

故

$$
\begin{aligned}
a_0 &= f(x_0),\\[1mm]
a_1 &= f'(x_0),\\[1mm]
2a_2 &= f''(x_0) \quad \Longrightarrow \quad a_2 = \frac{f''(x_0)}{2}.
\end{aligned}
$$