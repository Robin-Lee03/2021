# def test(num1,num2,num3):
#     print('num1: {} ,num2: {}, num3: {}'.format(num1,num2,num3))
#
# way1
# num = [1,3,5]
# test(*num)

# way2
# test(7,8,9)

# class practice
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age


def oldest(*args):
    return max(args)


cat1 = Cat('jack', 6)
cat2 = Cat('candy', 8)
cat3 = Cat('coco', 10)


print(f'The oldest cat is {oldest(cat1.age,cat2.age,cat3.age)} years old. ')
