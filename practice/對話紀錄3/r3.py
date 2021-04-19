

lines = []
with open('3.txt','r',encoding='utf-8')as f:
	for line in f:        # f檔案裡的每一行稱做line
		lines.append(line.strip())    # 把每一行line加到lines清單裡面

for line in lines:
	s = line.split()
	time = s[0][ :5]
	name = s[0][5: ]
	context = s[1]

	print(time,name,context)