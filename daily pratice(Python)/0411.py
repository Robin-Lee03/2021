# list_x = [2,4,6,8,10]
# print(sorted(list_x))
# list_x.reverse()
# print(list_x)
# list_y = list_x.copy()
# print(list_y)

# print(list(range(1,100)))
# name = ['My','name','is','RobinLee']
# sentence = ' ! '
# new_sentence = sentence.join(name)
# print(new_sentence)

dict = {
    'apple': '蘋果',
    5*2 : '10dollar',
    'Robin': [19990320],
    'z' : [777]
}

dict.update({'English':'英文'})   # dictionary 裡面增加新的key和value
dict['Robin'] = '0320'  # 更改dict 裡面的值

if dict.__contains__('z'):      # 從dict裡尋找是否有'z'這筆data
    print('z is in the data')
print(dict.keys())         # 印出所有的key
print(dict.values())       # 印出所有的value
print(dict['Robin'])
print(dict['z'])
print(dict['English'])
