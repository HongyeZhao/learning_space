import matplotlib.pyplot as plt
import numpy as np

# 创建一些数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建一个图形和坐标轴
fig, ax = plt.subplots()

# 绘制数据
ax.plot(x, y)

# 去掉坐标轴
ax.axis('off')

# 显示图形
plt.show()