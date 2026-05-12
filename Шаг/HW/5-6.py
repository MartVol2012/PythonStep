class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Player:
    def __init__(self, name, damage):
        self.name = name
        self.hp = 100
        self.damage = damage
        self.inventory = []

    def info(self):
        print('Гравець:')
        print(self.name)
        print(self.hp)

    def show_inventory(self):
        print('Інвентар:')
        if len(self.inventory) == 0:
            print('Порожній')
        else:
            for item in self.inventory:
                print(item.name, '-', item.value)

    def add_item(self, item):
        self.inventory.append(item)

    def attack(self, enemy):
        print('-------------------')
        print(self.name, 'атакує', enemy.name)
        enemy.hp -= self.damage
        print(enemy.name, 'отримав шкоду')
        print('HP ворога', enemy.hp)


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def info(self):
        print('Ворог:')
        print(self.name)
        print(self.hp)

    def attack(self, player):
        print('-------------------')
        print(self.name, 'атакує', player.name)
        player.hp -= self.damage
        print(player.name, 'отримав шкоду')
        print('HP ворога', player.hp)

enemy = Enemy('Зомбі', 100, 10)
player = Player('Ben', 15)

item1 = Item('Зілля', 50)
item2 = Item('Щит', 100)

print('Виберіть предмет:')
print('1 - Зілля')
print('2 - Щит')
choice = input('Ваш вибір: ')
print('-------------------')

if choice == '1':
    player.add_item(item1)
elif choice == '2':
    player.add_item(item2)
else:
    print('Немає такого предмета')

player.info()
enemy.info()

while player.hp > 0 and enemy.hp > 0:
    player.attack(enemy)
    enemy.attack(player)

    if enemy.hp <= 0:
        print('-------------------')
        print(enemy.name, 'помер. Гравець виграв')
        print('-------------------')

    if player.hp <= 0:
        print('-------------------')
        print(player.name, 'помер. Ворог виграв')
        print('-------------------')

print('Бажаєта побачити інвентар?')
print('1 - Відкрити')
print('2 - Вихід')
choice2 = input('Ваш вибір: ')

if choice2 == '1':
    player.show_inventory()
elif choice2 == '2':
    print('Ви впевнені?')
else:
    print('Помилка')

print('Бажаєта вийти?')
print('1 - Так')
choice3 = input('Ваш вибір: ')

if choice3 == '1':
    print('Вихід...')
else:
    print('Помилка')