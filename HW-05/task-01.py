# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної може містити символ _, але не може містити два символи __ підряд.
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

variable_name = input("Введіть ім'я змінної: ")

if (variable_name
        and not variable_name[0].isdigit()
        and variable_name.islower()
        and " " not in variable_name
        and all(char not in string.punctuation.replace("_", "") for char in variable_name)
        and "__" not in variable_name
        and variable_name not in keyword.kwlist):
    print(True)
else:
    print(False)