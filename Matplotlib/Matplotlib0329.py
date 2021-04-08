import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,5,20)   # 1~5 平均分成20個點
y1 = 2*x+1
y2 = 2**x

plt.figure(figsize=(9,5))               # 概念像是創造一個新的圖表 figure以下的程式就視為data
plt.plot(x,y1,color='hotpink',linestyle = '-.',label='up')

# plt.figure()
plt.plot(x,y2,color='lightblue',marker = 'o',label='down')
plt.legend(loc='best')  # 設定完label後 要讓它顯示出來
plt.xlim((0,10))
plt.ylim((0,40))
plt.xlabel('I am x')      # 給予縱軸和橫軸'標示'
plt.ylabel('I am y')

# new_ticks = np.linspace(-1,2,5)  # x軸的單位(ticks)-1~2分成五格間隔
# print(new_ticks)
# plt.xticks(new_ticks)
plt.yticks([5,10,15,20,40],
           ['bad','soso','good','excellent','perfect'])
plt.show()


