import view_console as view
import model_handbook as model
import storage_csv
import storage_txt

storage = 'csv'
storages = {
    'txt': storage_txt,
    'csv': storage_csv
}

def show_help() -> bool:
    text = ['/h - help', '/s - change storage','/o - output data', '/i - input data', '/q - quit']
    view.echo_paragraph(text)
    return True

def storage_change() -> bool:
    valid = ['txt', 'csv']
    input_storage = view.get_storage()
    while input_storage not in valid:
        view.echo(f'Доступные форматы: {valid}')
        input_storage = view.get_storage()
    global storage
    storage = input_storage
    return True

def output() -> bool:
    data = storages.get(storage).output(view.get_find_text(storage))
    if len(data) == 0:
        view.echo('Ничего не найдено')
    else:
        rows = []
        for row in data:
            surname, name, patronimic, birthday, phone = row
            model.init(surname, name, patronimic, birthday, phone)
            rows.append(model.about())
        view.echo_paragraph(rows)
    return True

def input() -> bool:
    phone = view.get_phone(storage)
    while not model.check_phone(phone):
        view.echo('Некорректный ввод!')
        phone = view.get_phone(storage)
    model.init(view.get_surname(storage), view.get_name(storage), view.get_patronimic(storage), view.get_birthdate(storage), phone)
    storages.get(storage).input(model.get_data())
    return True

actions = {
    '/h': show_help,
    '/o': output,
    '/i': input,
    '/s': storage_change,
    '/q': lambda: False # Выход из программы
}

def do_action():
    action = view.get_action()
    return actions.get(action, show_help)()

def go():
    storage_change()
    while do_action():
        continue

