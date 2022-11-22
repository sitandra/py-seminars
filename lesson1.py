# Задача 1
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('да')
else:
    print('нет')


# some_str = input().split(', ')
# num1 = int(some_str[0])
# num2 = int(some_str[1])

# num1, num2 = map(int, input().split(', '))

# Задача 2
numbers = []
for _ in range(5):
    n = int(input())
    numbers.append(n)
print(', '.join(map(str, numbers)),'->', max(numbers))

# Задача 3
n = int(input('Введите N: '))
if n > 0:
    numbers = list(range(-n, n + 1))
else:
    numbers = list(range(-n, n - 1, -1))
print(n, '->', ', '.join(map(str, numbers)))
print(n, '->', end=' ')
print(*numbers, sep=', ')

# Задача 4
n = float(input('Введите дробь: '))
fraction = n % 1 * 10
print(n, '->', 'нет' if fraction == 0 else str(n % 1 * 10)[0])

some_str = input('Введите дробь: ')
if ',' in some_str:
    some_list = some_str.split(',')
    print(some_list[1][0])
else:
    print('нет')

some_str = input('Введите дробь: ')
if ',' in some_str:
    ind = some_str.index(',')
    print(some_str[ind + 1])
else:
    print('нет')

n = float(input('Введите дробь: '))
print(n, '->', 'нет' if int(n) == n else int(n * 10) % 10)

n = float(input('Введите дробь: '))
if int(n) == n:
    print(int(n), '-> нет')
else:
    print(n, '->', int(n * 10) % 10)

# Задача 5
n = int(input('Введите число: '))
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('да')
else:
    print('нет')