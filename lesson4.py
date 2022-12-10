# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
some_numbers = list(map(int, input('Введите набор чисел через пробел: ').split()))
print(min(some_numbers), max(some_numbers))

# 28. Найдите корни квадратного уравнения Ax2 + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения;
# с помощью дополнительных библиотек Python.

a, b, c = map(float, input('Введите значения A, B, C через пробел: ').split())
d = b * b - 4 * a * c
if d < 0:
    print('Действительных корней нет')
elif d == 0:
    x = -b / (2 * a)
    print('Корень равен', x)
else:
    x1 = (-b - d ** 1/2) / (2 * a)
    x2 = (-b + d ** 1/2) / (2 * a)
    print('Корни уравнения Ax2 + Bx + C = 0:', x1, x2)

import sympy
x = sympy.symbols('x')
print(sympy.solveset(sympy.Eq(a * x**2 + b * x + c, 0), x))
print(sympy.solve(a * x**2 + b * x + c))

# 29. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.
from sympy import *
x, y = map(int, input('Введите два числа через пробел: ').split()) 
# Using sympy.lcm() method
gfg = lcm(x, y)
print(x, y, '– НОК:', gfg)