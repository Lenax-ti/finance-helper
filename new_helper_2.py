import json


menu = '''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
'''

selection = input(menu)



with open('My expenses.json', 'r') as f:
    log_book = json.load(f)


def expenses(amount):

    category = input('Напишите категорию трат: ')

    if category in log_book:
        log_book[category] += int(amount)
        print("Сумма трат добавлена")
    else:
        log_book[category] = int(amount)
        print('Новая категория добавлена')


def full_balance():
    for key, value in log_book.items():
        print(key, value)


def specific_balance():
    select_category = input('Напишите категорию: ')
    if select_category in log_book:
        print(log_book[select_category])

    else:
        print('Такой категории не существует!')
        print()
        category_error = input('''Что дальше:
1 - Ввести категорию заново
2 - Посмотреть список категорий
''')
        if category_error == '2':

            print(*log_book, sep='\n')
            print()
            specific_balance()
        elif category_error == '1':
            specific_balance()


while selection:
    if selection == '1':
        try:
            sm = float(input('Введите сумму: '))
            expenses(sm)
            with open('My expenses.json', 'w') as file:
                json.dump(log_book, file, indent=15)

            print()
            selection = input(menu)

        except ValueError:
            print('Сумма должна быть числом!')


    if selection == '2':
        question_about_balance = input('''Показать баланс:
1 - По всем категориям
2 - По конкретной категории
''')
        if question_about_balance == '1':
            full_balance()
            selection = input(menu)

        elif question_about_balance == '2':
            specific_balance()
            selection = input(menu)

    if selection == '3':
        break



