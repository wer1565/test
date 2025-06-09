import random

def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11  # For simplicity, Ace is always 11
    else:
        return int(card)

def play_higher_lower():
    print("\nДобро пожаловать в игру 'Больше или Меньше'!")
    deck = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)

    score = 0
    while True:
        if len(deck) < 2:
            print("Перемешиваю колоду...")
            deck = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A'] * 4
            random.shuffle(deck)

        current_card = deck.pop()
        print(f"Ваша текущая карта: {current_card}")

        while True:
            guess = input("Как вы думаете, следующая карта будет [Б]ольше или [М]еньше? (Б/М): ").upper()
            if guess in ['Б', 'М']:
                break
            else:
                print("Неверный ввод. Пожалуйста, введите 'Б' или 'М'.")

        next_card = deck.pop()
        print(f"Следующая карта: {next_card}")

        current_value = get_card_value(current_card)
        next_value = get_card_value(next_card)

        if (guess == 'Б' and next_value > current_value) or \
           (guess == 'М' and next_value < current_value):
            print("Поздравляю! Вы угадали!")
            score += 1
        elif next_value == current_value:
            print("Это ничья! Значения карт равны.")
        else:
            print("К сожалению, вы не угадали.")

        print(f"Ваш текущий счет: {score}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            break

    print(f"Спасибо за игру! Ваш итоговый счет: {score}")

if __name__ == "__main__":
    play_higher_lower() 