### 23. 解：

#### (1)

记两周需求量为 $Z = X + Y$，则有

$$f_Z(z) = \int_{-\infty}^{\infty} f_X(x)f_Y(z - x) dx$$

故，

$$
\begin{aligned}
f_Z(z) &=
\begin{cases}
    \int_0^z f(x)f(z - x) dx & z > 0 \\
    0 & z \leq 0
\end{cases}\\
&=
\begin{cases}
    e^{-z} \int_0^z x(z-x) dx & z > 0 \\
    0 & z \leq 0
\end{cases}\\
&=
\begin{cases}
    \frac{z^3e^{-z}}{6} & z > 0 \\
    0 & z \leq 0
\end{cases}
\end{aligned}
$$

#### (2)

记三周需求量为 $W = Z + X$，则有

$$
f_W(w) = \int_{-\infty}^\infty f_Z(x) f_X(w - x) dx
$$

故，

$$
\begin{aligned}
f_W(w)
&= 
\begin{cases}
    \int_0^{w} f_Z(x)f_X(w-x)dx & w > 0 \\
    0 & w \leq 0
\end{cases}\\
&=
\begin{cases}
    \int_0^{w} \frac{x^3e^{-z}}{6}(w-x)e^{x-w}dx & w > 0 \\
    0 & w \leq 0
\end{cases}\\
&=
\begin{cases}
    \frac{w^5e^{-w}}{5!} & w > 0\\
    0 & w \leq 0
\end{cases}
\end{aligned}
$$

```py
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import x, theta, sigma, r, z

pi = sym.pi

f_Z = 2*pi * 1/(2 * pi * sigma**2) * sym.exp(-r**2/(2 * sigma**2)) * r
sym.integrate(f_Z, (r, 0, z)).diff(z)
```

### 28. 解：

设 $Z$ 的分布函数为 $F_Z$，则，

$$
\begin{aligned}
    F_Z(Z\leq z) &= 
    \begin{cases}
        P(X^2+Y^2\leq z^2) & z \ge 0 \\
        0 & z < 0
    \end{cases}\\
    &=
    \begin{cases}
        \iint\limits_{x^2+y^2\leq z^2} f(x, y) dxdy & z \ge 0 \\
        0 & z < 0
    \end{cases}\\
    &=
    \begin{cases}
        \iint\limits_{x^2+y^2 \leq z^2} \frac{1}{2\pi\sigma^2}e^{\frac{-x^2-y^2}{2\sigma^2}}dxdy & z \ge 0\\
        0 & z < 0
    \end{cases}\\
    &=
    \begin{cases}
        \int_{0}^{2\pi} d\theta\int_0^z \frac{1}{2\pi\sigma^2}e^{\frac{-r^2}{2\sigma^2}} r dr & z \ge 0\\
        0 & z < 0
    \end{cases}\\
    &=
    \begin{cases}
        1 - e^{-\frac{z^2}{2\sigma^2}} & z \ge 0 \\
        0 & z < 0
    \end{cases}
\end{aligned}
$$

故，

$$
\begin{aligned}
    f_Z(z)&=\frac{d}{dz}F_Z(z)
    =\frac{z e^{- \frac{z^{2}}{2 \sigma^{2}}}}{\sigma^{2}}
\end{aligned}
$$

### 6. 解：

#### (2)

$$
\begin{aligned}
    E(\frac{1}{X+1}) &= \sum_{k = 0}^\infty \frac{1}{k + 1}P(X=k)\\
    &= \sum_{k = 0}^\infty \frac{\lambda^ke^{-k}}{(k + 1)!}\\
    &=\frac{e^{-k}}{\lambda}(\sum_{k = 0}^\infty \frac{\lambda^k}{k!}-1)\\
    &=\frac{e^{-\lambda}}{\lambda}(e^\lambda-1)\\
    &=\frac{1}{\lambda}(1-e^{-\lambda})
\end{aligned}
$$

### 7. 解：

#### (2)

设 $U$ 分布函数为 $F_U(U\leq u)$，则有

$$F_U(u)=\prod_{i=1}^n P(X\leq u) = u^n$$

故

$$
f_U=\frac{d}{du}F_U(u)=nu^{n-1}
$$

故

$$
\begin{aligned}
    E(U)
    &= \int_0^1 f_U(x)u du\\
    &= \int_0^1 nu^ndu\\
    &= \frac{nu^{n+1}}{n+1}\bigg|_{0}^1=\frac{n}{n+1}
\end{aligned}
$$