class Student:
    def __init__(self, name, money=100, knowledge=50):
        self.name = name
        self.money = money
        self.knowledge = knowledge

    def work(self):
        print('студент', {self.name}, 'працює...')
        self.money += 50
        self.knowledge -= 5

    def study(self):
        print('студент', {self.name}, 'вчиться...')
        self.knowledge += 10
        self.money -= 10

    def rest(self):
        print('Студент', {self.name}, 'відпочиває...')
        self.money -= 20
        self.knowledge -= 2

    def live_day(self):
        print('День студента', {self.name})
        print('Гроші:', {self.money}, 'Знання:', {self.knowledge})

        if self.money < 20:
          self.work()
        elif self.knowledge <40:
            self.study()
        else:
            self.rest()

s1 = Student('Вася')

for day in range(356):
    s1.live_day()

print('Фінальний стан:')
print('Гроші:', {s1.money}, 'Знання:', {s1.knowledge})