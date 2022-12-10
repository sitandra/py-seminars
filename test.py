print('26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
import time
def get_fibonacci1(number):
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
def get_fibonacci2(number):
    if number < 1:
        return [0]
    fibonacci = [1, 0, 1]
    first = 0
    second = 1
    for n in range(number-1):
        current = first + second
        fibonacci.append(current)
        if n % 2 == 0:
            fibonacci.insert(0, (-1) * current)
        else:
            fibonacci.insert(0, current)
        first, second = second, current
    return fibonacci

number = int(input('Введите число: '))
start = time.time()
end = time.time()
fib = get_fibonacci2(number)
duration = 200000

start = time.time()
for _ in range(duration):
    fib = get_fibonacci1(number)
end = time.time()
print(number, '->', fib)
print("get_fibonacci1 :", (end-start) * 10**3, "ms")
start = time.time()
for _ in range(duration):
    fib = get_fibonacci2(number)
end = time.time()
print(number, '->', fib)
print("get_fibonacci2 :", (end-start) * 10**3, "ms")