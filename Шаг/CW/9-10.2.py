"""
try:
    x = int(input('Веди чисто:'))
    resul = (10 / x)
except ZeroDivisionError:
    print('Не можна ділити на 0')
except:
    print('Треба вводити число')
else:
    print('Все добре, відповідь:', resul)
finally:
    print('Дякуємо!')


try:
    age = int(input('Введи вік:'))

    if age < 0:
        raise ValueError('Мінус не можна')

    print('Ok')

except ValueError as e:
    print('Помилка:', e)
"""
class BankAccount:
    def __init__(self, money):
        self.money = money

    def add_money(self, amount):

        if amount < 0:
            raise ValueError('Не можна додавати мінус')
        if amount == 0:
            raise ValueError('Не можна додавати нуль')

        self.money += amount
        print('Всього грошей:', self.money, 'грн')

    def withdraw(self, amount):

        if amount < 0:
            raise ValueError('Не можна знімати мінус')

        if amount == 0:
            raise ValueError('Не можна знімати нуль')

        if amount > self.money:
            credit = amount - self.money
            print(f'Недостатньо коштів. Ваш баланс:' ,self.money, 'грн.')
            print(f'Для зняття, ',amount ,'грн вам потрібен кредит у розмірі',credit ,'грн.')
            print('Умови: 3 грн/день до 30 днів, понад 30 днів — 4% від суми кредиту.')

            consent = input('Ви згодні взяти кредит? (так/ні): ')

            if consent == 'так':
                print('Кредит на суму', credit, 'грн зроблено')
                self.money += credit
            else:
                raise ValueError('Відмовлено в операції: недостатньо коштів і відхилено кредит.')

        if amount > self.money:
            raise ValueError('Недостатньо грошей')

        self.money -= amount
        print('Знято:', amount)
        print('Залишок:', self.money)


account = BankAccount(100)

choice = input('Що ви хочете зробити? (додати/зняти): ')

try:
    if choice == 'додати':
        add = int(input('Скільки хочете додати:'))
        account.add_money(add)
    elif choice == 'зняти':
        take = int(input('Скільки зняти?:'))
        account.withdraw(take)

    else:
        print('Невідома комада')

except ValueError as e:
    print('Помилка', e)
