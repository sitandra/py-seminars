def get_data(label: str) -> str:
    return input(f'{label} > ')

def echo_paragraph(text: list) -> list:
    print(*text, sep="\n")
    return text

def echo(text: str) -> str:
    print(text)
    return text

def get_action() -> str:
    return get_data('Введите действие')
def get_surname() -> str:
    return get_data('Введите фамилию')
def get_name() -> str:
    return get_data('Введите имя')
def get_patronimic() -> str:
    return get_data('Введите отчество')
def get_birthdate() -> str:
    return get_data('Введите дату рождения')
def get_phone() -> str:
    return get_data('Введите номер телефона')
def get_find_text() -> str:
    return get_data('Введите искомую информацию')