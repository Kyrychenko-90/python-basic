# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення - якщо
# користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

while True:
    first_number = float(input("Введіть перше число: "))
    second_number = float(input("Введіть друге число: "))
    math_operation = input("Введіть математичну дію (+, -, *, /): ")

    if math_operation == "+":
        print(first_number + second_number)
    elif math_operation == "-":
        print(first_number - second_number)
    elif math_operation == "*":
        print(first_number * second_number)
    elif math_operation == "/":
        if second_number == 0:
            print("Ділення на нуль неможливе!")
        else:
            print(first_number / second_number)
    continue_calculation = input("Продовжити? (y/yes): ")
    if continue_calculation.lower() not in ["y", "yes"]:
        break
