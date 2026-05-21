class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100

    def info(self):
        print('Імя:', self.name)
        print('Вік:', self.age)
        print('HP:', self.health)

    def sound(self):
        print('Тварина видає звук')

class Dog(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def info(self):
        super().info()
        print('Швидкість', self.speed)
        print('---------------')

class Humster(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def info(self):
        super().info()
        print('Швидкість', self.speed)
        print('---------------')

class Cat(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age)
        self.speed = speed

    def info(self):
        super().info()
        print('Швидкість', self.speed)
        print('---------------')

dog = Dog('Рекс', 4, 40)
humster = Humster('Гога', 1, 100)
cat = Cat('Льова', 4, 60)

dog.info()
humster.info()
cat.info()
