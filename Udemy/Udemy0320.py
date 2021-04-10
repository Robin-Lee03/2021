import matplotlib.pyplot as plt
a= int(input('輸入正整數: '))
b= int(input('輸入正整數: '))
c= int(input('輸入正整數: '))
d= int(input('輸入正整數: '))
plt.plot([a, b, c, d], [a**2, b**2, c**2, d**2],'ro')
# plt.axis([0,50,0,60])    # 設定圖表x,y 軸的範圍
plt.ylabel('some numbers')
plt.xlabel('other numbers')
plt.show()
plt.savefig('test.png')


# import numpy as np
#
#
# arr = np.array([2,4,6,8,10,15])
#
# print(arr)
# arr = np.array([1, 2, 3, 4, 5])
#
# print(arr)
# print(type(arr))



# evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
#
# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
