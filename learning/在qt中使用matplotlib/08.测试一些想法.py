import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax2.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()