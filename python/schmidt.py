import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 假设你已经从 Maxima 中得到了以下向量
u1 = np.array([1, 0, 2])  # 替换为 Maxima 输出的 u1
u2 = np.array([0, 3, -1])  # 替换为 Maxima 输出的 u2
u3 = np.array([1, 4, 1])  # 替换为 Maxima 输出的 u3

# 原始向量
v1 = np.array([1, 0, 2])
v2 = np.array([0, 3, -1])
v3 = np.array([1, 4, 1])

# 创建图形和坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制原始向量
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', arrow_length_ratio=0.1, label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='g', arrow_length_ratio=0.1, label='v2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='b', arrow_length_ratio=0.1, label='v3')

# 绘制正交化后的向量
ax.quiver(0, 0, 0, u1[0], u1[1], u1[2], color='m', linestyle='dashed', arrow_length_ratio=0.1, label='u1')
ax.quiver(u1[0], u1[1], u1[2], u2[0], u2[1], u2[2], color='c', linestyle='dashed', arrow_length_ratio=0.1, label='u2')
ax.quiver(u1[0] + u2[0], u1[1] + u2[1], u1[2] + u2[2], u3[0], u3[1], u3[2], color='y', linestyle='dashed', arrow_length_ratio=0.1, label='u3')

# 设置坐标轴标签和图例
ax.set_xlim(-3, 4)
ax.set_ylim(-3, 7)
ax.set_zlim(-3, 5)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

# 显示图形
plt.show()
