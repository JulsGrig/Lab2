"asxjulausdd"
password = input('Введите пароль')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False

for char in password:
    if char.isnumeric():
        is_numeric = True
    elif char.islower():
        is_lower = True
    elif char.isupper() :
        is_upper = True
    elif char in "@#$%^" :
        is_spec = True

if len(password) > 4 and is_numeric and is_upper and is_lower and is_spec:
    print('Пароль принят')
else:
    print('Пароль не принят')