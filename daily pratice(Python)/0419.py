# tree
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# # 第一種方法
# new = ''
# for row in picture:
# 	new += '\n'
# 	for pixel in row:
#
# 		if pixel == 1:
# 			new += '*'
# 		else:
# 			new += ' '
#
# print(new)

# 第二種方法
# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')


# rocket
SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def lower():
	lower_img = ''
	for i in range(1,SIZE+1):
		for j in range(1):
			lower_img += '|'
		for j in range(i - 1):
			lower_img += '.'
		for j in range(i,SIZE+1):
			lower_img += '\\/'
		for j in range(i-1):
			lower_img += '.'
		for j in range(1):
			lower_img += '|'
		if i != SIZE:
			lower_img += '\n'


	print(lower_img)


def upper():
    upper_img = ''
	for i in range(1,SIZE+1):
		for j in range(1):
			upper_img += '|'
		for j in range(SIZE-i):
			upper_img += '.'
		for j in range(i):
			upper_img += '/\\'
		for j in range(SIZE-i):
			upper_img += '.'
		for j in range(1):
			upper_img += '|'
		if i != SIZE:
			upper_img += '\n'


	print(upper_img)


def head():
	head_img = ''
	for i in range(1,SIZE+1):
		for j in range(i,SIZE+1):
			head_img += ' '
		for j in range(i):
			head_img += '/'
		for j in range(i):
			head_img += '\\'
		if i != SIZE:
			head_img += '\n'

	print(head_img)


def belt():
	belt_img = ''
	belt_img += '+'
	for i in range(SIZE+SIZE):
		belt_img += '='
	belt_img += '+'
	print(belt_img)


#%%



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

# check the duplicates data
some_list = ['a','b','c','d','c','a','a','c','e']
new_list = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in new_list:
            new_list.append(i)

print(new_list)

#%%

# parameters

def hello(name,sentence):
    print(f'Hello {name} {sentence}')

# 盡量按照函數的順序撰寫
hello('Robin','how are you :)')
hello('Allen','how are you :)')
hello('Tom','how are you :)')

# 這樣寫較複雜
hello(sentence='you are so beautiful today!',name = 'Lily !')


