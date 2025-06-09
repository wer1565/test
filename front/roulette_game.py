import random

def play_roulette():
    print("\nДобро пожаловать в Рулетку!")
    balance = 1000

    while True:
        print(f"Ваш текущий баланс: ${balance}")

        if balance <= 0:
            print("У вас закончились деньги! Игра окончена.")
            break

        while True:
            try:
                bet_amount = int(input("Введите сумму ставки: "))
                if bet_amount <= 0 or bet_amount > balance:
                    print(f"Неверная сумма ставки. Вы можете поставить от 1 до {balance}.")
                else:
                    break
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите целое число.")

        print("\nНа что вы хотите поставить?")
        print("1. Конкретное число (0-36)")
        print("2. Цвет (Красный/Черный)")
        print("3. Четное/Нечетное")

        while True:
            bet_type_choice = input("Введите выбор (1/2/3): ")
            if bet_type_choice in ['1', '2', '3']:
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

        bet_on = None
        if bet_type_choice == '1':
            while True:
                try:
                    bet_on = int(input("Введите число, на которое ставите (0-36): "))
                    if 0 <= bet_on <= 36:
                        break
                    else:
                        print("Неверный номер. Пожалуйста, введите число от 0 до 36.")
                except ValueError:
                    print("Неверный ввод. Пожалуйста, введите целое число.")
        elif bet_type_choice == '2':
            while True:
                bet_on = input("Введите цвет (Красный/Черный): ").lower()
                if bet_on in ['красный', 'черный']:
                    break
                else:
                    print("Неверный цвет. Пожалуйста, введите 'Красный' или 'Черный'.")
        elif bet_type_choice == '3':
            while True:
                bet_on = input("Введите Четное/Нечетное: ").lower()
                if bet_on in ['четное', 'нечетное']:
                    break
                else:
                    print("Неверный ввод. Пожалуйста, введите 'Четное' или 'Нечетное'.")

        print("\nКрутим колесо...")
        winning_number = random.randint(0, 36)
        print(f"Выпало число: {winning_number}")

        is_red = winning_number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        is_black = winning_number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

        won = False
        if bet_type_choice == '1':
            if bet_on == winning_number:
                won = True
                balance += bet_amount * 35
                print(f"Поздравляю! Вы выиграли ${bet_amount * 35}!")
        elif bet_type_choice == '2':
            if (bet_on == 'красный' and is_red) or \
               (bet_on == 'черный' and is_black):
                won = True
                balance += bet_amount
                print(f"Поздравляю! Вы выиграли ${bet_amount}!")
        elif bet_type_choice == '3':
            if (bet_on == 'четное' and winning_number % 2 == 0 and winning_number != 0) or \
               (bet_on == 'нечетное' and winning_number % 2 != 0):
                won = True
                balance += bet_amount
                print(f"Поздравляю! Вы выиграли ${bet_amount}!")

        if not won:
            balance -= bet_amount
            print(f"К сожалению, вы проиграли ${bet_amount}.")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            break

    print("Спасибо за игру в Рулетку!")

if __name__ == "__main__":
    play_roulette() 