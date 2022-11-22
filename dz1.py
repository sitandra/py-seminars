# 6  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

weekday = int(input('Введите номер дня недели: '))
if weekday < 1 or weekday > 7:
    print('Неверный ввод')
elif weekday < 6:
    print(weekday, '-> нет')
else:
    print(weekday, '-> да')

# 7  Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

predicates = [0, 1]
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in predicates:
    for y in predicates:
        for z in predicates:
            result = (not (x or y or z)) == (not x and not y and not z)
            print('x =', x, ', y =', y, ', z =', z, '–' , result)

# 8  Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('x = '))
y = int(input('y = '))
print('x=', x, '; y=', y , sep='', end=' -> ')
if x == 0 and y == 0:
    print('Центр')
elif x == 0:
    print('Ось Y')
elif y == 0:
    print('Ось X')
elif x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print('this is magic')

# 9  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))
result = {
    1: 'x > 0 and y > 0',
    2: 'x < 0 and y > 0',
    3: 'x < 0 and y < 0',
    4: 'x > 0 and y < 0'
}
try:
    print(result[quarter])
except KeyError as e:
    print(f'Некорректный номер четверти: {quarter}')

# 10 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
a = [int(input('Ax = ')), int(input('Ay = '))]
b = [int(input('Bx = ')), int(input('By = '))]
distance = round(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2), 2)
a_str = ', '.join(map(str, a))
b_str = ', '.join(map(str, b))
print(f'A ({a_str}); B ({b_str}) -> {distance}')