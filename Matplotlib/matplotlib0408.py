import matplotlib.pyplot as plt
import numpy as np
# font1 = {'family':'serif','color':'hotpink','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
# plt.title('population',fontdict=font1)
# plt.xlabel('age',fontdict=font2)
# plt.ylabel('direction',fontdict=font2)
plt.figure()
y = np.array([1,3,8,5,-3,1])
x = np.array([-1,6,7,9,3,8])

font1 = {'family':'serif','color':'hotpink','size':20}  # w3 'labels'
font2 = {'family':'serif','color':'darkred','size':15}
plt.title('population',fontdict=font1)
plt.xlabel('age',fontdict=font2)
plt.ylabel('direction',fontdict=font2)

plt.plot(y,c = '#4CAF50',lw=3.5,label='male')  # c = color , lw = line width
plt.plot(x,c='lightblue', lw=2,label='female') # 小label 註明每條線代表什麼
plt.legend(loc='best')       # plt.legend() 才會把label印出來 loc=位置
# plt.plot(x,y)
#plt.figure()
plt.show()
