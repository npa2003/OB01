# Задача с простой учетной системой банка

class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):   # Метод для внесения средств
        if money > 0:
            self.balance += money
            print(f"Счёт пополнен. Сумма на счете - {self.balance}")

    def withdraw(self, money):   # Функция для снятия денег
        if money > self.balance:
            print("Недостаточно средств на счёте")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")


man = Account(111222333, 600)
man.all_balance()
man.deposit(1000)
man.withdraw(852)
man.all_balance()
