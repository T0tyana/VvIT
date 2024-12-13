from math import sqrt
from datetime import datetime
import my_module

# 1
num = int(input('Введите число: '))
print(f'Квадратный корень числа {num} равен {sqrt(num)}')
print()

now = str(datetime.today()).split()
print(f'Дата: {now[0]} \nВремя: {now[1]}')
print()

# 2
num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))
print(f'Сумма чисел: {my_module.summa(num_one, num_two)}')
print()

# 3
import test.strings
print(test.strings.big('dbght'))
