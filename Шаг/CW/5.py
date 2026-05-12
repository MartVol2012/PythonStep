"""
class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def info(self):
        print('Имя гравця:', self.name)
        print('Рівень гравця:', self.level)


player1 = Character('Ben', 6)
player2 = Character('Den', 7)

player1.info()
player2.info()

print('------------------------------------')

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def info(self):
        print('Зброя:', self.name)
        print('Шкода:', self.damage)

sword = Weapon('Iron Sword', 25)
bow = Weapon('Wooden Bow', 15)
axe = Weapon('Divine Axe', 35)
staff = Weapon('Magic Staff', 20)

sword.info()
bow.info()
axe.info()
staff.info()

print('------------------------------------')
"""

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

class Character:
    def __init__(self, name, level, weapon, armor):
        self.name = name
        self.level = level
        self.weapon = weapon
        self.armor = armor
        self.health = 100

    def attack(self,enemy):
        print('-------------------')
        print(self.name, 'атакує', enemy.name)
        enemy.health -= self.weapon.damage
        print(enemy.name, 'отримав шкоду')
        print('HP ворога', enemy.health)

    def attack2(self, enemy):
        print('-------------------')
        print(self.name, 'атакує (сильна атака)', enemy.name)
        damage = self.weapon.damage
        enemy.health -= self.weapon.damage
        print(enemy.name, 'отримав шкоду')
        print('HP ворога', enemy.health)

    def show_stats(self):
        print('-------------------')
        print('Имя', self.name)
        print('HP', self.health)
        print('Зброя', self.weapon.name)
        print('Броня', self.armor.name)

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print('Ворог', self.name)
        print('HP', self.health)


enemy = Enemy('skeleton', 120)
enemy2 = Enemy('zombi', 100)

armor1 = Armor('Iron Armor', 15)
armor2 = Armor('Diamant Armor', 25)
armor3 = Armor('Golden Armor', 20)

weapon1 = Weapon('Iron Sword', 25)
weapon2 = Weapon('Wooden Bow', 15)
weapon3 = Weapon('Magic Staff', 20)

player = Character("Ben", 6, weapon1, armor1 )
player2 = Character("Den", 6, weapon2, armor2 )
player3 = Character("Pen", 6, weapon3, armor3 )

player.show_stats()
player2.show_stats()
player3.show_stats()


"""
def info(self):
        print('Имя гравця:', self.name)
        print('Рівень гравця:', self.level)

    def show_weapon(self):
        print(self.name, 'використовує', self.weapon.name)
"""

"""
sword = Weapon('Iron Sword', 25)
player = Character('Ben', 6, sword, armor1)
bow = Weapon('Wooden Bow', 15)
player2 = Character('Den', 7, bow, armor2)
staff = Weapon('Magic Staff', 20)
player3 = Character('Pen', 8, staff, armor3)

player.info()
player.show_weapon()
player2.info()
player2.show_weapon()
player3.info()
player3.show_weapon()
"""

"""
player.attack(enemy)
player2.attack(enemy2)
"""