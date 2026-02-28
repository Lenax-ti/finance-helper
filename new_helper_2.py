import json


menu = '''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
'''

selection = input(menu)



with open('My expenses.json', 'r') as f:
    log_book = json.load(f)


def get_amount():
    while True:
        try:
            return float(input('Введите сумму: '))

        except ValueError:
            print('Сумма должна быть числом!')

def expenses(amount):

    category = input('Напишите категорию трат: ')

    if category in log_book:
        log_book[category] += float(amount)
        print("Сумма трат добавлена")
    else:
        log_book[category] = float(amount)
        print('Новая категория добавлена')


def full_balance():
    for key, value in log_book.items():
        print(key, value)

# Вместо рекурсии использовать цикл while
def specific_balance():
    while True:
        select_category = input('Напишите категорию: ')
        if select_category in log_book:
            print(log_book[select_category])
            break

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
                continue
            elif category_error == '1':
                continue


while selection:
    if selection == '1':

        sm = get_amount()
        expenses(sm)
        with open('My expenses.json', 'w') as file:
            json.dump(log_book, file, indent=15)

        print()
        selection = input(menu)




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



