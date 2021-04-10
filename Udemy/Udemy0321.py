import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 8, 10,15])
# y = np.array([3, 10, 12, 16, 20])

plt.plot(x,'o')         # 如果不設定y質 會自動從 0 1 2 3依照順序排下去
plt.show()

# x = np.array([1, 8])
# y = np.array([3, 10])
#
# plt.plot(x, y)
# plt.show()

# x = np.linspace(-1,5,30)    # -1~5 中間平均分配30個點
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure()
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()