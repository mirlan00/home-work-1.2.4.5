import random

class SlotMachine:
    def __init__(self, name):
        self.name = name
        self.user_balance = 100
        self.game_balance = 0

    def info(self):
        print(f"Имя игрока: {self.name}")
        print(f"Баланс пользователя: {self.user_balance}")
        print(f"Игровой баланс: {self.game_balance}")

    def balance_up(self, amount):
        if amount > 100:
            print("Вы можете пополнить до 100$")
            return
        self.user_balance -= amount
        self.game_balance += amount

    def top_up_balance(self):
        amount = int(input("Введите сумму для пополнения: "))
        self.balance_up(amount)

    def game(self):
        number = random.randint(1, 10)
        for _ in range(5):
            guess = int(input("Угадайте число от 1 до 10: "))
            if guess == number:
                print("Вы выиграли!")
                self.game_balance += 50
                return
        print("Вы проиграли")
        self.game_balance -= 10

    def con_money(self):
        if self.game_balance < 50:
            print("Вывести можно от 50$")
            return
        amount = int(input("Введите сумму для вывода: "))
        if amount > self.game_balance:
            print("Недостаточно средств на игровом балансе")
            return
        self.game_balance -= amount
        self.user_balance += amount

    def main(self):
        while True:
            command = int(input("Введите команду (1 - информация, 2 - пополнение, 3 - игра, 4 - вывод): "))
            if command == 1:
                self.info()
            elif command == 2:
                self.top_up_balance()
            elif command == 3:
                self.game()
            elif command == 4:
                self.con_money()
            else:
                print("Неверная команда")


s = SlotMachine("Аман")
s.main()
