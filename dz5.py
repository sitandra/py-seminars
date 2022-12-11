# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input('Введите текст: ').split()
deleted = ('а', 'б', 'в')
text = list(filter(lambda word: all(symbol not in word for symbol in deleted), text))
print(*text, ' ')

import random
# 40. Создайте программу для игры в "Крестики-нолики".
coordinates = {
    'a0': 0, 'b0': 1, 'c0': 2,
    'a1': 3, 'b1': 4, 'c1': 5,
    'a2': 6, 'b2': 7, 'c2': 8
}
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
field = [' ' for _ in range(9)]
def print_field(field: list):
    print('    |  a  |  b  |  c  |')
    print('———————————————————————')
    print(' 0', end='')
    for x in field[:3]:
        print('  |  ' + x, end='')
    print('  |')
    print('———————————————————————')
    print(' 1', end='')
    for x in field[3:6]:
        print('  |  ' + x, end='')
    print('  |')
    print('———————————————————————')
    print(' 2', end='')
    for x in field[6:]:
        print('  |  ' + x, end='')
    print('  |')
    print('———————————————————————')
def input_step(step: str, field: list) -> bool:
    if step in coordinates and field[coordinates[step]] == ' ':
        field[coordinates[step]] = 'x'
    else:
        return input_step(input('Ошибка! Выберите другой ход: '), field)
    return True
def output_step(line: tuple, field: list):
    for cell in line:
        if field[cell] == ' ':
            field[cell] = 'o'
            return   
def count_symbol(symbol: str, line: set, field: list) -> int:
    line_values = [x for k, x in enumerate(field) if k in line]
    if line_values.count(' ') > 0:
        return line_values.count(symbol)
    else:
        return -1
def check_win(symbol: str, field: list) -> bool:
    for line in win:
        line_values = [x for k, x in enumerate(field) if k in line]
        if line_values.count(symbol) == 3:
            for cell in line:
                field[cell] = str.upper(field[cell])
            return True
    else:
        return False
def go_step(field: list):
    cnt_x = [count_symbol('x', line, field) for line in win]
    cnt_o = [count_symbol('o', line, field) for line in win]
    for ind, o in enumerate(cnt_o):
        if o == 2:
            output_step(win[ind], field)
            return
    for ind, x in enumerate(cnt_x):
        if x == 2:
            output_step(win[ind], field)
            return
    variants = [k for k, x in enumerate(cnt_x) if x >= 0]
    if len(variants) > 0:
        output_step(win[random.choice(variants)], field)      

print('Привет! Сыграем в крестики-нолики')
print_field(field)
for i in range(5):
    input_step(input('Введите свой ход: '), field)
    if check_win('x', field):
        print_field(field)
        print('Поздравляю с победой!')
        break
    go_step(field)
    if check_win('o', field):
        print_field(field)
        print('Сообщаю о проигрыше!')
        break
    print_field(field)
else:
    print('Ничья!')

# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_incode(text: str) -> str:
    result = ''
    current_char = text[0]
    current_count = 1
    for char in text[1:]:
        if char == current_char:
            current_count += 1
        else:
            result += str(current_count) + current_char
            current_char = char
            current_count = 1
    return result + str(current_count) + current_char

def rle_decode(text: str) -> str:
    result = ''
    current_count = ''
    for char in text:
        if char.isdigit():
            current_count += char
        else:
            result += char * int(current_count)
            current_count = ''
    return result

with open('file42-input.txt','r',encoding='utf-8') as file:
    text = file.readline()
    print('Text before incode:', text)
with open('file42-output.txt','w',encoding='utf-8') as file:
    file.write(rle_incode(text))
with open('file42-output.txt','r',encoding='utf-8') as file:
    code = file.readline()
    print('Text before decode:', code)
if text == rle_decode(code): #check decode algorithm
    print('Success')
else:
    print('Fail')