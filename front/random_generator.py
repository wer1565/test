import random

def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

print("Генератор случайных чисел")

while True:
    try:
        min_num = int(input("Введите минимальное число: "))
        max_num = int(input("Введите максимальное число: "))

        if min_num > max_num:
            print("Ошибка: Минимальное число не может быть больше максимального.")
            continue

        random_number = generate_random_number(min_num, max_num)
        print(f"Случайное число между {min_num} и {max_num}: {random_number}")
        
        another_generation = input("Хотите сгенерировать еще одно число? (да/нет): ")
        if another_generation.lower() == "нет":
            break

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.") 