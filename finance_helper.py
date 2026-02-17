
selection = input('''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
''')

def processing(x):
    pass


log_book = {}

while selection != '3':
    if selection == '1':
        amount = input('Сумма: ')
        if amount.isdigit():
            category = input('Какая категория: ')
            log_book[category] = int(amount)
            Yes_No = input('Вы хотели бы продолжить сеанс (Да\Нет)?: ')
            if Yes_No == 'Нет':
                y_n = input('Показать баланс (Да\Нет)?: ')
                if y_n == 'Да':
                    print(log_book)
                    break
                elif y_n == 'Нет':
                    break
            elif Yes_No == 'Да':
                selection = input('''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
    ''')

        else:
            print('Сумма должна быть числом')

print(log_book)