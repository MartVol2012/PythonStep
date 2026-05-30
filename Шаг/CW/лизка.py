class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self, title):
        self.title = title
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_catalog(self):
        print(f"\n Каталог магазину {self.title}:")
        for prod in self.products:
            print(f"- {prod.name}: {prod.price} монет")

    def find_by_price(self, max_price):
        print(f"\n Товары до {max_price} монет: ")
        for prod in self.products:
            if prod.price <= max_price:
                print(f"- {prod.name}: {prod.price} монет")


class Buyer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.inventory = []

    def view_inventory(self):
        print(f"\n Інвентар {self.name} (Залишок: {self.wallet} монет):")
        if not self.inventory:
            print("- Порожньо")
        for prod in self.inventory:
            print(f"- {prod.name}")


my_shop = Shop("IT STEP")

p1 = Product("Меч", 200)
p2 = Product("Лук", 250)
p3 = Product("Молот", 300)
p4 = Product("Зілля здоров'я", 60)
p5 = Product("Зілля швидкості", 60)
p6 = Product("Пахучі носкі", 100)
p7 = Product("Кепка", 20)

my_shop.add_product(p1)
my_shop.add_product(p2)
my_shop.add_product(p3)
my_shop.add_product(p4)
my_shop.add_product(p5)
my_shop.add_product(p6)
my_shop.add_product(p7)

buyer = Buyer("Ярік", 1000)

print(f"Ти зайшов у магазин {my_shop.title}.")

while True:
    my_shop.show_catalog()
    buyer.view_inventory()

    print("\nЩо ти хочеш зробити?")
    print("1. Купити ... ")
    print("2. Напиши 'вихід', щоб завершити покупки.")


    choice = input("\n Твій вибір: ")

    if choice.lower() == "вихід":
        print("\n Дякуємо за покупки")
        break

    buyer.product(my_shop, choice)
