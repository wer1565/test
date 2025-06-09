import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль!"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Ошибка: Нельзя извлечь квадратный корень из отрицательного числа!"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Ошибка: Неверные значения для логарифма!"
    return math.log(x, base)

calculation_history = []

def record_calculation(expression, result):
    calculation_history.append(f"{expression} = {result}")

def display_history():
    if not calculation_history:
        print("История вычислений пуста.")
    else:
        print("\nИстория вычислений:")
        for item in calculation_history:
            print(item)

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Извлечение квадратного корня")
print("7. Логарифм")
print("8. Показать историю")
print("9. Выход")

while True:
    choice = input("Введите выбор (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
                continue

            if choice == '1':
                result = add(num1, num2)
                expression = f"{num1} + {num2}"
            elif choice == '2':
                result = subtract(num1, num2)
                expression = f"{num1} - {num2}"
            elif choice == '3':
                result = multiply(num1, num2)
                expression = f"{num1} * {num2}"
            elif choice == '4':
                result = divide(num1, num2)
                expression = f"{num1} / {num2}"
            elif choice == '5':
                result = power(num1, num2)
                expression = f"{num1} ** {num2}"
        elif choice == '6': # Square Root
            try:
                num = float(input("Введите число для извлечения корня: "))
                result = square_root(num)
                expression = f"sqrt({num})"
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
                continue
        elif choice == '7': # Logarithm
            try:
                num = float(input("Введите число: "))
                base = float(input("Введите основание логарифма: "))
                result = logarithm(num, base)
                expression = f"log({num}, base={base})"
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")
                continue
        
        print(f"{expression} = {result}")
        if not isinstance(result, str):
            record_calculation(expression, result)

    elif choice == '8':
        display_history()
    elif choice == '9':
        print("Выход из калькулятора.")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите существующую операцию.") 