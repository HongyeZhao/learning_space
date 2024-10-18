import numpy as np

# 使用 numpy arange 生成列表
start = 1.5
stop = 3.6
step = 0.1

# 注意：np.arange 的 stop 参数是不包含的，所以不需要 +1
values = np.arange(start, stop + step, step)
print(values.tolist())