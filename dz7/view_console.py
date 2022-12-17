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
def get_surname(storage: str) -> str:
    return get_data(f'{storage}: Введите фамилию')
def get_name(storage: str) -> str:
    return get_data(f'{storage}: Введите имя')
def get_patronimic(storage: str) -> str:
    return get_data(f'{storage}: Введите отчество')
def get_birthdate(storage: str) -> str:
    return get_data(f'{storage}: Введите дату рождения')
def get_phone(storage: str) -> str:
    return get_data(f'{storage}: Введите номер телефона')
def get_find_text(storage: str) -> str:
    return get_data(f'{storage}: Введите искомую информацию')
def get_storage() -> str:
    return get_data('Введите формат хранилища данных')