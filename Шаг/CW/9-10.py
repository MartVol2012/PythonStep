class Animal:
    def __init__(self, name, age, HP, danger):
        self.name = name
        self.age = age
        self.HP = 100
        self.danger = danger

    def info(self):
        print('-----------------')
        print('Назва:', self.name)
        print('Возраст:', self.age)
        print('Здоровя:', self.HP)
        print('Опасность:', self.danger)

class WildAnimal(Animal):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)
        self.danger = danger

class Predator(WildAnimal):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)

class Lion(Predator):
    def info(self):
        super().info()
        print("Лев гучно реве: Рррр!")

    def attack(self, Deer):
        Deer.HP -= 20
        print(self.name, 'атакуе', Deer.name, '(-20 HP)')

class Tiger(Predator):
    def info(self):
        super().info()
        print("Тигр гарчить: Рррр!")

    def attack(self, wildebeest):
        wildebeest.HP -= 20
        print(self.name, 'атакуе', wildebeest.name, '(-10 HP)')


class Wolf(Predator):
    def info(self):
        super().info()
        print("Вовк виє: Аууу")

    def attack(self, Hare):
        Hare.HP -= 20
        print(self.name, 'атакуе', Hare.name, '(-30 HP)')

class Herbivorous(WildAnimal):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)


class Wildebeest(Herbivorous):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)

    def info(self):
        super().info()
        print("Живий")

class Hare(Herbivorous):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)

    def info(self):
        super().info()
        print("Живий")

class Deer(Herbivorous):
    def __init__(self, name, age, HP, danger):
        super().__init__(name, age, HP, danger)

    def info(self):
        super().info()
        print("Живий")


lion = Lion('Лев', 7, 100, 70)
tiger = Tiger('Тигр', 9, 100, 80)
wolf = Wolf('Волк', 10, 100, 60)

wildebbest = Wildebeest('Антилопа', 6, 100 ,50)
hare = Hare('Заяц', 3, 100, 20)
deer = Deer('Олень', 8, 100, 40)

print("Інформація про хижаків")
lion.info()
tiger.info()
wolf.info()


print("Інформація про травоїдних")
wildebbest.info()
hare.info()
deer.info()






