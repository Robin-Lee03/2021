import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# x = np.linspace(-1,5,30)    # -1~5 中間平均分配30個點
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure()
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()