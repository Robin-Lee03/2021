class User:
    def sign_in(self):
        print('logged in')
        return ''

    def introduce(self):
        print('do nothing')


class Wizard(User):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):

        print(f'{self.name} is {self.age} years old')
        User.introduce(self)


class Archer(User):

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def introduce(self):
        print(f'{self.name} has {self.height}cm')


user1 = Wizard('Tom',30)      # why  126. - 4:00
user2 = Archer('Robin',177)
user1.introduce()     # Because line19 
# user1.introduce()
# user2.introduce()
# user2.sign_in()


# print(isinstance(user2,User))
#
# for char in [user1,user2]:
#     char.introduce()
# print(user3.introduce())
