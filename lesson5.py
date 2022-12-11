# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие А[i] - 1 = А[i-1]А[i]−1=А[i−1]. Найдите это число.
with open('file35.txt','r',encoding='utf-8') as file:
    numbers = list(enumerate(map(int, file.readline().split())))

diff = numbers[0][1] - numbers[0][0]
for i, num in numbers[1:]:
    if num - i != diff:
        print('Не хватает числа', numbers[i - 1][1] + 1)
        break
else:
    print('Все ОК')

# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
text = input('Введите текст: ').split()
deleted = ('а', 'б', 'в')
text = list(filter(lambda word: all(ext not in word for ext in deleted), text))
print(*text, ' ')