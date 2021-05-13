# class PlayerCharacter:
#     membership = True
#     def __init__(self,name,age,sex):
#         self._name = name      # _name _ = private
#         self._age = age
#         self._sex = sex
#
#     def speak(self):
#         print(f'My name is {self._name}, and I\'m {self._age} year old')
#
# player1 = PlayerCharacter('Robin',22,'male')
# print(player1)
# print(player1._sex)
# player1.speak()


class PlayerCharacter:

    def __init__(self,name,age):     # __init__ =  建構式
        self._name = name      # _name _ = private
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter('Robin',22)
player1.speak()
# player1.name ='!!!'           # 應該看成一個 instantiation
# player1.speak = 'pppppp'
print(player1.speak())   # why?    124. - 4:00
# print(player1.name)
# print(player1.speak)    # why?  125. - 2:20
