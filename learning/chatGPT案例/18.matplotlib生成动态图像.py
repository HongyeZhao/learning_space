import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 展示十条动态曲线

# 准备数据
x_data = np.linspace(0, 2 * np.pi, 100)
y_data = []

# 创建图形和轴
fig, ax = plt.subplots()

# 创建十条曲线的初始状态
lines = [ax.plot(x_data, np.sin(x_data + i * np.pi / 5))[0] for i in range(10)]

# 初始化函数，设置曲线的初始数据
def init():
    for line in lines:
        line.set_data(x_data, np.zeros(len(x_data)))
    return lines

# 更新函数，用于更新曲线的数据
def update(frame):
    for i, line in enumerate(lines):
        line.set_data(x_data, np.sin(x_data + (i * np.pi / 5) + frame / 10.0))
    return lines

# 创建动画
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init, blit=True)

# 显示图形
plt.show()