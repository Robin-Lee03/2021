# import time
#
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#
# # 暂停一秒
# time.sleep(5)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pandas.DataFrame(mydataset)
#
# print(myvar)

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)