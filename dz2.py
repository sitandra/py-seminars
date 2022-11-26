# 14 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = float(input('Введите вещественное число: '))
sum = 0
for i in str(number):
    if i != '.':
        sum += int(i)
print(f'{number} -> {sum}')

# 15 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import prod
n = int(input('Введите n: '))
n_arr = [1] * n
n_str_arr = [' '] * n
for i in range(1, n + 1):
    i_numbers = range(1, i + 1)
    n_arr[i - 1] = n_arr[i - 1] * prod(i_numbers)
    n_str_arr[i - 1] = '*'.join(map(str, list(i_numbers)))
description = '(' + ', '.join(n_str_arr) + ')'
print(f'Пусть N = {n}, тогда', n_arr, description)

# 16 Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
n = int(input('Введите n: '))
n_list = {}
n_sum = 0
for i in range(1, n + 1):
    i_num = (1 + 1 / i) ** i
    n_list[i] = round(i_num, 2)
    n_sum += i_num
print(f'Для n = {n}:', n_list)
print('Сумма', round(n_sum,2))

# 17 Задайте список из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите N: '))
n_list = list(range(-n, n + 1))
with open('file.txt', 'r') as f:
    pos1 = int(f.readline())
    pos2 = int(f.readline(2))
result = n_list[pos1] * n_list[pos2]
print(n_list)
print(f'Произведение чисел на позициях {pos1} и {pos2} равно', result)

# 18 Реализуйте алгоритм перемешивания списка.
import random
some_list = list(range(10))
print(some_list)
for i in range(10):
    one = random.randint(0, 9)
    two = random.randint(0, 9)
    (some_list[one], some_list[two]) = (some_list[two], some_list[one])
print(some_list)