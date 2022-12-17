import re

g_surname = ''
g_name = ''
g_patronimic = ''
g_birthday = ''
g_phone = ''

def init(surname, name, patronimic, birthday, phone):
    global g_surname
    global g_name
    global g_patronimic
    global g_birthday
    global g_phone
    g_surname = surname
    g_name = name
    g_patronimic = patronimic
    g_birthday = birthday
    g_phone = phone

def get_data() -> str:
    return [g_surname, g_name, g_patronimic, g_birthday, g_phone]
    
def about() -> str:
    return '    ' + ' '.join(filter(None,[g_surname, g_name, g_patronimic, g_birthday, g_phone]))

def check_phone(phone: str) -> bool:
    return bool(re.match("^\\+?[7][0-9]{9,9}$", phone))