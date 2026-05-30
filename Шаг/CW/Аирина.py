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
        print(' Каталог магазину:', self.title)
        for prod in self.products:
            print(f"- {prod.name}: {prod.price} монет")

    def find_by_price(self, max_price):
        print(f"\n Товары до {max_price} монет: ")
        found = False
        for prod in self.products:
            if prod.price <= max_price:
                print(f"- {prod.name}: {prod.price} монет")
                found = True
        if not found:
            print("- Нічого не знайдено")

    def find_product(self, name):
        for prod in self.products:
            if prod.name.lower() == name.lower():
                return prod
        return None


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

    def buy_product(self, shop, product_name):
        product = shop.find_product(product_name)

        if product is None:
            print(f"\n Товар '{product_name}' не знайдено в магазині!")
            return False

        if self.wallet < product.price:
            print(f"\n Недостатньо грошей! Потрібно {product.price} монет, у вас {self.wallet} монет.")

        self.wallet -= product.price
        self.inventory.append(product)
        shop.products.remove(product)

        print(f"\n {self.name} купив '{product.name}' за {product.price} монет!")
        print(f"   Залишок: {self.wallet} монет")


my_shop = Shop("IT STEP")

p1 = Product("Меч", 200)
p2 = Product("Лук", 250)
p3 = Product("Молот", 300)
p4 = Product("Зілля здоров'я", 60)
p5 = Product("Зілля швидкості", 60)
p6 = Product("Пахучі носки", 100)
p7 = Product("Кепка", 20)

my_shop.add_product(p1)
my_shop.add_product(p2)
my_shop.add_product(p3)
my_shop.add_product(p4)
my_shop.add_product(p5)
my_shop.add_product(p6)
my_shop.add_product(p7)

buyer = Buyer("Ярік", 1000)

print('Ти зайшов у магазин', my_shop.title)

while True:
    my_shop.show_catalog()
    buyer.view_inventory()

    print("Що ти хочеш зробити?")
    print("1. Купити товар (введи назву)")
    print("2. Фільтр за ціною (введи 'фільтр')")
    print("3. Напиши 'вихід', щоб завершити покупки.")

    choice = input("Твій вибір: ")

    if choice.lower() == "вихід":
        print("Дякуємо за покупки!")
        break
    elif choice.lower() == "фільтр":
        try:
            max_price = int(input("Введи максимальну ціну: "))
            my_shop.find_by_price(max_price)
        except ValueError:
            print(" Будь ласка, введи число!")
    else:
        buyer.buy_product(my_shop, choice)