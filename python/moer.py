import numpy as np
import matplotlib.pyplot as plt
# 给定的应力分量

sigma_xx = -4
sigma_yy = 2
sigma_zz = 6

# 计算平均应力
sigma_avg = (sigma_xx + sigma_yy + sigma_zz) / 3

# 计算莫尔圆的半径
# 由于没有给出切应力分量，我们假设 tau_xy = 0（平面应力状态下的常见情况）
radius = 0 / 2

# 计算主应力
sigma_1 = sigma_avg + radius
sigma_2 = sigma_avg - radius

# 计算主方向
# 在平面应力状态下，主方向可以通过以下公式计算：
theta = 0.5 * np.arctan2(2 * 0, sigma_xx - sigma_yy)

# 绘制莫尔圆
theta = np.linspace(0, 2 * np.pi, 100)
x = sigma_avg + radius * np.cos(theta)
y = radius * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='莫尔圆')
plt.plot([sigma_avg, sigma_avg], [0, 2*radius], 'k--', label='平均应力线')
plt.plot([sigma_avg, sigma_1], [0, 0], 'r-', label='主应力1')
plt.plot([sigma_avg, sigma_2], [0, 0], 'b-', label='主应力2')
plt.xlabel('应力 (MPa)')
plt.ylabel('应力 (MPa)')
plt.title('莫尔圆')
plt.legend()
plt.grid(True)
plt.show()

sigma_1, sigma_2, theta, radius, 2*radius
