import matplotlib.pyplot as plt
import numpy as np


x = np.array([2,9])
y = np.array([3,12])

# 更改y軸的單位區間
new_yticks = np.linspace(0,12,25)  # 0~12 分成25個間格
print(new_yticks)
plt.yticks(new_yticks)

# 更改x軸的單位區間
new_xticks = np.linspace(0,12,25)
print(new_xticks)
plt.xticks(new_xticks)

# plt.plot(x,y)  # plot() function draws a line from point to point.
plt.plot(x,y,'o',color='hotpink')  # wiithout line version
# plt.show()

"""
    If we do not specify the points in the x-axis
    they will get the default values 0, 1, 2, 3,
"""
ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.plot(ypoints,marker='o')  # Use 'marker' to emphasize each point with a specified marker
plt.plot(ypoints,marker='D')
plt.show()
