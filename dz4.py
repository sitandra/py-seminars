from sympy import *
import math
import random

# 30. Вычислить число c заданной точностью d
print('# 30')
cnt = len(input('Введите точность d: ').split('.')[1])
pi = round(math.pi, cnt)
print(pi)

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
print('# 31')
def is_prime(number):
    for i in range(2, number):
        if not number % i:
            return False
    return True

n = int(input('Введите натуральное число N: '))
multipliers = [x for x in range(1, n + 1) if not n % x and is_prime(x)]
print(multipliers)

# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
print('# 32')
some_list = [random.randint(0, 10) for _ in range(20)]
result = [x for x in some_list if some_list.count(x) == 1]
print(some_list, '=>', result)

# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
print('# 33')
def get_part(mult, k, is_last):
    if is_last:
        plus = ''
    else:
        plus = ' + '
    if not mult:
        return ''
    else:
        result = plus + str(mult)
    if not k:
        return result
    elif k == 1:
        return result + ' * x'
    else:
        return result + ' * x ** ' + str(k)

k = int(input('Задайте натуральную степень k: '))
mult_list = [random.randint(0, 100) for _ in range(k + 1)]
result = ' = 0'
for x in range(k + 1):
    result = get_part(mult_list[x], x, x == k) + result
print(result, 'in file33.txt')
with open('file33.txt','w',encoding='utf-8') as file:
    file.write(result)

# 35. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
