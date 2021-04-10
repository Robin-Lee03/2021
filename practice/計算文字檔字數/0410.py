
# 計算有幾個字
# mind = str(input('What\'s are you thinking about ? '))
# count = 1
#
# for line in mind:
#     if line == ' ':
#         count += 1
#
# print(count)

# 計算文字檔內有多少字  總共有71個字 不是算letter
word_count = 1
def read_file():
    lines = []

    with open('text(71).txt','r')as f:
        for line in f:
            lines.append(line.strip())
        # for i in lines[0: ]:
        #     if i
    return lines


lines = read_file()
for i in lines[0: ]:

    if i == ' ':
        word_count += 1

print(lines)
print(len(lines))
print(word_count)


