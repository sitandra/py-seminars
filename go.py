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