import matplotlib.pyplot as plt
import numpy as np


import scipy.io as sio

mat_data = sio.loadmat('data_need_cluster_finalWC5000.mat')

# print(mat_data)

FCemp = mat_data['data_need_cluster']['FCemp']

print("形状：", FCemp.shape)
print("数据类型：", type(FCemp))
print(FCemp)
print(FCemp[0][0])
fig, ax = plt.subplots()
ax.imshow(FCemp[0][0], origin='lower')
plt.show()