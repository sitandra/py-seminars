import view_console as view
import model_handbook as model
import csv

def show_help() -> bool:
    text = ['/h - help', '/o - output data', '/i - input data', '/q - quit']
    view.echo_paragraph(text)
    return True

def output() -> bool:
    data = csv.output(view.get_find_text())
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
    phone = view.get_phone()
    while not model.check_phone(phone):
        view.echo('Некорректный ввод!')
        phone = view.get_phone()
    model.init(view.get_surname(), view.get_name(), view.get_patronimic(), view.get_birthdate(), phone)
    csv.input(model.get_data())
    return True

actions = {
    '/h': show_help,
    '/o': output,
    '/i': input,
    '/q': lambda: False # Выход из программы
}

def do_action():
    action = view.get_action()
    return actions.get(action, show_help)()

def go():
    while do_action():
        continue

