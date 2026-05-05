"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Dog("Собака", 3)

print(s1.name)
print(s1.age)
"""
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print("Собаку зовут", self.name)

    def grow(self):
        self.age += 1
        print(self.name, "став старше", self.age)

s1 = Dog('Собака', 3)
s1.say_name()
s1.grow()
"""
"""
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "пес" + self.name

s1 = Dog("Собака")
print(s1)
"""
class Dog:
    def __init__(self, toy):
        self.toy = toy

    def __len__(self):
        return len(self.toy)

s1 = Dog(["м'ячик", "мишка", "шкарпетка"])
print(len(s1))