
def read_file(filename):
	data = []
	with open(filename,'r',encoding='utf-8-sig') as f:    # utf-8 為了能夠讀取中文字 -sig 刪掉最前面那行多出來的文字
		for line in f:
			data.append(line.strip())      # .strip() 讓/n不會print出來
	return data


def title(rf):
	person = []
	name = None
	for line in rf:
		# print(line)
		s = line.split(' ')
		time = s[0]
		name = s[1]
		context = s[2: ]
		if name == 'Allen':
			print(context)
		elif name == 'Viki':
			print(context)

	return person


def write_file(filename, result):
	with open(filename,'w') as f:
		for line in result:
			f.write(line + '\n')


def main():
	rf = read_file('LINE-Viki.txt')
	result = title(rf)
	return result

main()

