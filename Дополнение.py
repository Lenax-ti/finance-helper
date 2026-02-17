menu = '''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
'''

selection = input(menu)


log_book = {}


def expenses():
    amount = input('Сумма: ')
    if amount.isdigit():
        category = input('Какая категория: ')
        log_book[category] = int(amount)

        yes_no = input('Вы хотели бы продолжить сеанс (Да\Нет)?: ')
        if yes_no == 'Нет':
            y_n = input('Показать баланс (Да\Нет)?: ')
            if y_n == 'Да':
                print(log_book)
                return False
            elif y_n == 'Нет':
                return False
        elif yes_no == 'Да':
            selection = input(menu)
            if selection == '1':
                return expenses()
            elif selection == '2':
                print(log_book)
            elif selection == '3':
                return False
    else:
        print('Сумма должна быть числом')
        return expenses()




while selection != '3':
    if selection == '1':
        expenses()


print(log_book)