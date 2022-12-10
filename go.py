from sympy import *
import math
import random
# 35. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
with open('file35-1.txt','r',encoding='utf-8') as file:
    poly1 = file.readline()
with open('file35-2.txt','r',encoding='utf-8') as file:
    poly2 = file.readline()