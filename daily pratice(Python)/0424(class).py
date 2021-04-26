class PlayerCharacter:
    membership = True
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    # def run(self):
    #     print(f'My name is {player1.name} and I\'m {player1.age}.')
    #     return 'down'

    def run_all(self):
        print(f'My name is {self.name} and I\'m {self.age}.')
        return 'golden membership'



player1 = PlayerCharacter('Robin',22,'Male')
# player1.sex = 'Male'   # 如果上面沒有定義 可用這種方式加入屬性

player2 = PlayerCharacter('Kevin',25,'Male')


print(player1.run_all())
print(player2.run_all())

print(player2.name,player2.age,player2.membership)
# print(PlayerCharacter('cindy',18,'Female'))