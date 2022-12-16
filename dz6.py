# 5. Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
import random
def get_ranges_list(some_list: list) -> list:
    some_list.sort()
    current = 0
    result = [[some_list[0], some_list[0]]]
    for i, n in list(enumerate(some_list))[1:]:
        if n - some_list[i-1] == 1:
            result[current][1] = n
        else:
            current += 1
            result.append([n, n])
    return list(map(lambda item: str(item[0]) if item[0] == item[1] else str(item[0]) + "-" + str(item[1]), result))

some_list = list({random.randint(0, 20) for _ in range(20)})
random.shuffle(some_list) # Имитируем неупорядоченный список уникальных значений
print(some_list, '=>', end=" ") # Печатаем список до
print(*get_ranges_list(some_list), sep=", ") # Печатаем результат

# 6. Дана строка (возможно, пустая), состоящая из букв A-Z. Нужно написать функцию RLE, которая сгенерирует ошибку, если на вход пришла невалидная строка.
def rle_encode(text: str) -> str:
    if (text == ''):
        raise ValueError('Пустая строка')
    text = list(filter(str.isalpha, text))
    result = ''
    current_char = text[0]
    current_count = 1
    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            result += current_char + (str(current_count) if current_count > 1 else '')
            current_char = char
            current_count = 1
    return result + current_char + (str(current_count) if current_count > 1 else '')

def rle_decode(text: str) -> str:
    if (text == ''):
        raise ValueError('Пустая строка')
    temp = ''
    for i, char in enumerate(text):
        if char.isdigit() and not text[i-1].isdigit():
            temp += ',' + char
        elif not char.isdigit():
            temp += '.' + char
        else:
            temp += char
    return ''.join(map(lambda item: item[0] * int(item[1]) if len(item) > 1 else item[0], [x.split(',') for x in temp.split('.') if not x == '']))

print('encode:', rle_encode('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB'))
print('decode:', rle_decode('A4B3C2XYZD4E3F3A6B28'))
print(rle_encode(''))