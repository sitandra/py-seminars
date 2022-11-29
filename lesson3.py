import random
print('\n    Задача 17. Задайте список из N элементов, заполненных числами из промежутка [-N,N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
n = int(input('Введите N: '))
n_list = [random.randint(-n, n) for _ in range(n)]
count = random.randint(1, n)
with open('file.txt', 'w+', encoding='utf-8') as f:
    for _ in range(n):
        f.write(f'{random.randint(0, n-1)}\n')
    f.seek(0,0)
    index_list = f.read().splitlines()
result = 1
for index in index_list:
    result *= n_list[int(index)]
    #pos1 = int(f.readline())
    #pos2 = int(f.readline(2))
#result = n_list[pos1] * n_list[pos2]
print(n_list)
print(f'Произведение чисел на позициях равно', result)

# 1. ввести кол-во строк, потом строки. Строки должны записаться в текстовый файл.
# После вводим число, если есть число в файле, то написать ДА
rows = int(input('Введите количество строк: '))
text = [input() for _ in range(rows)]
with open('text.txt','w',encoding='utf-8') as file:
    file.write('\n'.join(text))
number = int(input('Введите число: '))
with open('text.txt', 'r',encoding='utf-8') as file:
    text = file.read().splitlines()
line_count = 0
for line in text:
    pos_line = line.find(str(number))
    if pos_line != -1:
        print(line_count, pos_line)
        break
    line_count += 1
else:
    print('Ничего не нашел, увы и ах!')


def month_name(month_number, lang):
    month_list = \
        {
            'en':
                {
                    '1': 'Jan',
                    '2': 'Feb',
                    '3': 'Mar',
                    '4': 'Apr',
                    '5': 'May',
                    '6': 'Jun',
                    '7': 'Jul',
                    '8': 'Aug',
                    '9': 'Sep',
                    '10': 'Oct',
                    '11': 'Nov',
                    '12': 'Dec'
                },
            'ru':
                {
                    '1': 'Янв',
                    '2': 'Фев',
                    '3': 'Мар',
                    '4': 'Апр',
                    '5': 'Май',
                    '6': 'Июн',
                    '7': 'Июл',
                    '8': 'Авг',
                    '9': 'Сен',
                    '10': 'Окт',
                    '11': 'Ноя',
                    '12': 'Дек'
                }
        }
    return month_list[lang][month_number]
print(month_name(input('Введите номер месяца: '), input('Введите язык: ')))

def find_if_second(some_list, text):
    index = 0
    flag = False
    for line in some_list:
        if line == text:
            if flag == False:
                flag = True
            else:
                return index
        index += 1
    return -1
some_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(some_list, find_if_second(some_list, "qwe"))
some_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(some_list, find_if_second(some_list, "йцу"))
some_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
print(some_list, find_if_second(some_list, "йцу"))
some_list = ["123", "234", 123, "567"]
print(some_list, find_if_second(some_list, "123"))
some_list = []
print(some_list, find_if_second(some_list, "123"))

# Список
some_list = ["123", "234", 123, "567"]
# Кортеж
some_tuple = tuple(some_list) 
some_tuple2 = (2, 5 ,234)
# Множество - индексов нет, элементы уникальны
some_set = set(some_list)
some_set2 = {1, 4, 7, 9}
# Неизменяемое множество - индексов нет, элементы уникальны
some_frozenset = frozenset(some_list)
some_frozenset2 = frozenset((2, 5 ,234))
# Словари
some_dict = {
    'key': 'value)'
}