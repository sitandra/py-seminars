# 11
n = int(input('Введите N: '))
x = 1
print(f'Для N = {n}: {x}', end='', sep='')
for _ in range(n-1):
    x = x * -3
    print(f', {x}', end='', sep='')

n = int(input('Введите N: '))
x = 1
print(f'Для N = {n}: 1', end='')
for i in range(1, n):
    x = (-3) ** i
    print(f', {x}', end='')


# 12
n = int(input('Введите n: '))
n_list = {}
for i in range(1, n + 1):
    n_list[i] = 3 * i + 1
print(f'Для n = {n}: {n_list}')

# 13
str_1 = input('Введите 1 строку: ')
str_2 = input('Введите 2 строку: ')
cnt = max(str_1.count(str_2), str_2.count(str_1))
print(cnt)