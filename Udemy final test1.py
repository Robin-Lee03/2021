

first_list = []
while True:
    number=int(input('Enter a Number: '))
    if number == -100:
        break
    else:
        first_list.append(number)

def find_max(first_list):
    if len(first_list) < 1:
        return 0
    max_n = first_list[0]
    if len(first_list) > 0:
        for num in first_list:
            while num > max_n:
                max_n = num
        return max_n

print(first_list)
max = find_max(first_list)
print(max)



# def main():
#     print(first_list)
#     max = find_max(first_list)
#     print(max)
#
# print(main())


# def find_max(first_list):
#     if len(first_list) < 1:
#         return 0
#     max_n = first_list[0]
#     if len(first_list) > 0:
#         for num in first_list:
#             while num > max_n:
#                 max_n = num
#         return max_n

