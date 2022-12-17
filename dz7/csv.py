file_name = 'dz7/handbook.csv'

def input(data: list) -> bool:
    global file_name
    row = ';'.join(map(lambda cell: '"'+str(cell)+'"', data))
    with open(file_name,'a',encoding='utf-8') as file:
        file.write(row + '\n')
    return True

def output(find_text: str) -> list:
    global file_name
    result = []
    with open(file_name,'r',encoding='utf-8') as file:
        for row in file:
            if find_text in row:
                result.append(list(map(lambda x: x.strip('"'), row.replace('\n', '').split(';'))))
    return result
