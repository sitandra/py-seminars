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