# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))
# tom = 'boy'
# txt = 'He is a {}'
# print(txt.format(tom))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# txt = 'My name is {},I\'m {} years old'.format('Robin',22)
# print(txt)


# 判斷是Odd or Even
# num = int(input('Enter a number 1~1000: '))
# if num < 1 or num > 1000:
#     print('loser')
# else:
#     if num % 2 == 0:
#         print('偶數')
#     else:
#         print('奇數')

#判斷數字
count = []
mind = str(input('What\'s are you thinking ?'))
for line in mind:
    count.append(line)

print(len(count))
