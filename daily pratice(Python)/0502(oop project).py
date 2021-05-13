# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Candy(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
#
# sally = Sally('Sally',9)
# simon = Simon('Simon',8)
# candy = Candy('Candy',10)
# my_cats = [sally,simon,candy]
# my_pets = Pets(my_cats)
# my_pets.walk()
# print(sally.walk())
# print(simon.walk())
# print(candy.walk())

class Cat():
    cats = []
    def __init__(self,cats):
        self.cats = cats

    def speak(self):
        for i in self.cats:
            print(f'{self.name} is just walking around')


class Simon(Cat):
    def cat(self,name,age):
        return 0


class Candy(Cat):
    def cat(self,name,age):
        return 0

# sally = Sally('Sally',9)
simon = Simon('Simon',8)
candy = Candy('Candy',10)
my_cats = [simon,candy]
my_pets = Cat(my_cats)
my_pets.speak()