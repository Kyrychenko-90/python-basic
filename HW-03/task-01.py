# Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

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