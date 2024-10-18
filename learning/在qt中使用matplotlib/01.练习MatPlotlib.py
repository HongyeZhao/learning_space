import matplotlib.pyplot as plt
import numpy as np
# #
# # A simple example
# fig, ax = plt.subplots() # 创建只包含一个Axes的图表 fig：这个图表，或则说这个窗口 ax：Axes，这个坐标系 ax中包含了对这个坐标系的操作
# # 在matplotlib中，Axes和Axis需要区分一下，Axes代表坐标系，Axis代表坐标轴
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # 设定参数
# ax.grid()
# #plt.show()
#
# #Figure
# fig = plt.figure()              # 创建一个空的窗口,注意 不会返回Axes
# fig, ax = plt.subplots()        # 创建一个包含一个坐标系的窗口
# fig, axs = plt.subplots(2, 2)   # 含有2*2 网格装的4个坐标系
# fig, axs = plt.subplot_mosaic([['left', 'right_top'],
#                                ['left', 'right_bottom']]) # 创建一个左边一个坐标系，右边一上一下各一个坐标系的窗口
# #plt.show()
#
# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# fig, ax = plt.subplots(figsize=(5, 2.7)) # figsize是指窗口的长宽比，但是这个窗口是指的装坐标轴的最小的那个窗口，而不是整个程序的窗口
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()
#
# # use the OO-style to create Figures and Axes
# x = np.linspace(0, 2, 100)  # Sample data.
# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x label')  # Add an x-label to the Axes.
# ax.set_ylabel('y label')  # Add a y-label to the Axes.
# ax.set_title("Simple Plot")  # Add a title to the Axes.
# ax.legend()  # Add a legend.
# plt.show()
#
# # use the pyplot-style to create Figures and Axes
# x = np.linspace(0, 2, 100)  # Sample data.
#
# plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.figure()
# plt.show()
#
# """
# 所谓OO-style和pyplot-style就是，画图时你可以通过
#     plt.subplots()来创建并获取到Figure和Axes对象，然后通过这两个对象来对图表进行设置
#     另外，就算是plt.subplots()也是内部调用了plt.figure()方法来创建的Figure对象 （Figure对象中就包含了Axes、Axis...等对象）
# 也可以
#     直接使用plt.figure来创建对象，并直接使用plt在对图表进行设置
#     调用的方法都是一样的（细微的方法名的变化，把set_去掉了），只是调用对象从Figure和Axes变成了pyplot(plt)而已
# 官方建议使用OO-style
# """
#
# # Making a helper functions 制作一个帮助方法
# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out
#
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# out1 = my_plotter(ax1, data1, data2, {'marker': 'x'})
# out2 = my_plotter(ax2, data3, data4, {'marker': 'o'})
# print(type(out1))
# plt.show()
#
# # Styling Artists 装饰Artists，Artists指Figure，Axes，Axis...等所有的东西
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# print(type(l))
# l.set_linestyle(':')
# plt.show()
#
# # Colors
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
# plt.show()
#
# # Linewidths, linestyles, and markersizes
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, ax = plt.subplots(figsize = (5, 2.7))
# ax.plot(data1, 'o', label='data1')
# ax.plot(data2, 'd', label='data2')
# ax.plot(data3, 'v', label='data3')
# ax.plot(data4, 's', label='data4')
# ax.legend()
# plt.show()
#
# # Labelling plots
# mu, sigma = 115, 15
# x = mu + sigma * np.random.randn(1000)
# fig, ax = plt.subplots(figsize=(5,2.7), layout='constrained')
# n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
#
# ax.set_xlabel('Length [cm]')
# ax.set_ylabel('Probability')
# ax.set_title('Aardvark lengths\n (not really)')
# ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
# print(ax.axis([55, 175, 0, 0.03]))
# print(ax.axis())
# ax.grid(True)
# plt.show()
#
# # Using mathematical expressions in text
#
# # Annotations
# fig, ax = plt.subplots(figsize=(5, 2.7))
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = ax.plot(t, s, lw=2)
# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.set_ylim(-2, 2)
# plt.show()
#
# # Legends
#
# # Axis scales and ticks
#
# # Tick locators and formatters
# data1, data2, data3, data4 = np.random.randn(4, 100)
# xdata = np.arange(len(data1))
# fig, axs = plt.subplots(2, 1, layout='constrained')
# axs[0].plot(xdata, data1)
# axs[0].set_title('Automatic ticks')
#
# axs[1].plot(xdata, data1)
# axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
# axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
# axs[1].set_title('Manual ticks')
# plt.show()
#
# # Plotting dates and strings
# from matplotlib.dates import ConciseDateFormatter
#
# print(np.datetime64('2021-11-15'))
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
#                   np.timedelta64(1, 'h'))
# print(dates)
# data = np.cumsum(np.random.randn(len(dates)))
# ax.plot(dates, data)
# ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))
# plt.show()
#
# # Additional Axis objects
# fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
# l1, = ax1.plot(t, s)
# ax2 = ax1.twinx()
# l2, = ax2.plot(t, range(len(t)), 'C1')
# ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])
#
# ax3.plot(t, s)
# ax3.set_xlabel('Angle [rad]')
# ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
# ax4.set_xlabel('Angle [°]')
#
# # Color mapped data
# from matplotlib.colors import LogNorm
# data1, data2, data3, data4 = np.random.randn(4, 100)
# X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
# Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
#
# fig, axs = plt.subplots(2, 2, layout='constrained') # 使用axs列表来接收4个坐标轴
# pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
# fig.colorbar(pc, ax=axs[0, 0])
# axs[0, 0].set_title('pcolormesh()')
#
# co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
# fig.colorbar(co, ax=axs[0, 1])
# axs[0, 1].set_title('contourf()')
#
# pc = axs[1, 0].imshow(Z**2 * 100, cmap='RdBu_r', norm=LogNorm(vmin=0.01, vmax=100))
# fig.colorbar(pc, ax=axs[1, 0], extend='both')
# axs[1, 0].set_title('imshow() with LogNorm()')
#
# pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
# fig.colorbar(pc, ax=axs[1, 1], extend='both')
# axs[1, 1].set_title('scatter()')
# plt.show()
#
# # Colormaps
#
# # Normalizations
#
# # Colorbars
#
# Working with multiple Figures and Axes
import matplotlib
# matplotlib.use('TKAgg')
print(matplotlib.get_backend()) # 默认使用是就是QtAgg
fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['lowleft'].set_title('lowleft')
axd['right'].set_title('right')
plt.show()
