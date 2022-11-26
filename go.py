n = int(input('Введите N: '))
x = 1
print(f'Для N = {n}: 1', end='')
for i in range(1, n):
    x = (-3) ** i
    print(f', {x}', end='')