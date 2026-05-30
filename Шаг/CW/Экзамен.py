class Cadet:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.money = 300
        self.inventory = []

    def info(self):
        print("------------------")
        print("Ім'я:", self.name)
        print("HP:", self.hp)
        print("Гроші:", self.money)

    def show_inventory(self):
        print("------ ІНВЕНТАР ------")

        if len(self.inventory) == 0:
            print("Інвентар порожній")
        else:
            for item in self.inventory:
                print(item.name)


class Item:
    def __init__(self, name, rarity, price):
        self.name = name
        self.rarity = rarity
        self.price = price


class Weapon(Item):
    def __init__(self, name, rarity, price, damage):
        super().__init__(name, rarity, price)
        self.damage = damage


class Potion(Item):
    def __init__(self, name, rarity, price):
        super().__init__(name, rarity, price)


class Armor(Item):
    def __init__(self, name, rarity, price, protection):
        super().__init__(name, rarity, price)
        self.protection = protection


sword = Weapon("Меч", 30, 30, 20)
bow = Weapon("Лук", 20, 25, 10)
hammer = Weapon("Молот", 52, 40, 40)

health = Potion("Зілля здоров'я", 50, 60)
speed = Potion("Зілля швидкості", 40, 50)

socks = Armor("Пахучі носки", 100, 100, 100)
cap = Armor("Кепка", 30, 25, 30)

player = Cadet('Ярік')

while True:
    print("===== МАГАЗИН АКАДЕМІЇ =====")
    print("1 - Меч (30)")
    print("2 - Лук (25)")
    print("3 - Молот (40)")
    print("4 - Зілля здоров'я (60)")
    print("5 - Зілля швидкості (50)")
    print("6 - Пахучі носки (100)")
    print("7 - Кепка (25)")
    print("8 - Інвентар")
    print("9 - Інформація про кадета")
    print("0 - Вихід")
    print("------------------")

    choose = input("Ваш вибір: ")

    if choose == "0":
        print("До побачення!")
        break

    elif choose == "1":
        item = sword

    elif choose == "2":
        item = bow

    elif choose == "3":
        item = hammer

    elif choose == "4":
        item = health

    elif choose == "5":
        item = speed

    elif choose == "6":
        item = socks

    elif choose == "7":
        item = cap

    elif choose == "8":
        player.show_inventory()

    elif choose == "9":
        player.info()

    else:
        print("Невірний вибір!")

    if player.money >= item.price:
        player.money -= item.price
        player.inventory.append(item)

        print("Ви купили:", item.name)
        print("Залишилось грошей:", player.money)
    else:
        print("Недостатньо грошей!")



