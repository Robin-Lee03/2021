class PlayerCharacter:
    membership = True
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex



    def run_all(self):
        print(f'My name is {self.name} and I\'m {self.age}.')
        return 'golden membership'

    @classmethod
    def adding(cls,n1,n2):
        print(n1+n2)


player1 = PlayerCharacter('Robin',22,'Male')
player2 = PlayerCharacter('Kevin',25,'Male')

print(player1.adding(5,10))

# print(player1.run_all())
# print(player2.run_all())

# print(player2.name,player2.age,player2.membership)