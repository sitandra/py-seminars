# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
print('22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')
import random
some_list = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
print(some_list, '->', sum(some_list[1::2]))

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
print('23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
import random
def product_of_pairs(some_list):
    idx = len(some_list) - 1
    result = []
    for num in range(round(len(some_list) / 2)):
        result.append(some_list[num] * some_list[idx])
        idx -= 1
    return result
some_list = [random.randint(1, 10) for _ in range(random.randint(2, 10))]
print(some_list, '->', product_of_pairs(some_list))

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
print('24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')
def get_diff_in_min_max_fractional_part(some_list):
    temp_list = [x%1 for x in some_list]
    temp_list.remove(0)
    return round(max(temp_list) - min(temp_list), 4)
some_list = [1.1, 1.2, 3.1, 5, 10.01]
print(some_list, '->', get_diff_in_min_max_fractional_part(some_list))

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
print('25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
def into_binary(number):
    binary = ''
    while (number > 0):
        binary = str(number % 2) + binary
        number = number // 2
    return binary
number = int(input('Введите десятичное число: '))
print(number, '->', into_binary(number))

# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
print('26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
def get_fibonacci(number):
    if number < 1:
        return [0]
    fibonacci = [1, 0, 1]
    first = 0
    second = 1
    for n in range(number-1):
        current = first + second
        fibonacci.append(current)
        fibonacci.insert(0, ((-1) ** (n + 1)) * current)
        first, second = second, current
    return fibonacci
number = int(input('Введите число: '))
print(number, '->', get_fibonacci(number))