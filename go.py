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
        fibonacci.insert(0, ((-1) ** (n+1)) * current)
        first, second = second, current
    return fibonacci
number = int(input('Введите число: '))
print(number, '->', get_fibonacci(number))