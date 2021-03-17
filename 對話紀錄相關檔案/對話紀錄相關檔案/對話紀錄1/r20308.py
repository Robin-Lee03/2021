
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
		if line == 'Allen':
			name = 'Allen'
			continue
		if line == 'Tom':
			name = 'Tom'
			continue
		# print(name + ': ' + line)
		if name:
			person.append(name + ': ' + line)
	return person


def write_file(filename, result):
	with open(filename,'w') as f:
		for line in result:
			f.write(line + '\n')


def main():
	rf = read_file('input.txt')      # 'input.txt'回傳至上方的filename 開始讀取
	result = title(rf)
	write_file('out_put.txt',result)
	return result


print(main())