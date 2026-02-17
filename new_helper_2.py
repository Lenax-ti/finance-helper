import json


menu = '''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
'''

selection = input(menu)


# log_book = {}   # Нужно, что бы данные были сохранены после выполнения кода, а не каждый раз создавались новые

# book = {'market': 1000, 'sport': 500, 'car': 1500, 'cafe': 2500}
#
# def recording_expenses():
#     pass

with open('My expenses.json', 'r') as f:
    log_book = json.load(f)

# Нужно усовершенствовать код с помощью функций\классов
while selection:

    if selection == '1':
        sm = input('Введите сумму: ')
        if sm.isdigit():
            category = input('Напишите категорию: ')

            if category in log_book:
                log_book[category] += int(sm)
            else:
                log_book[category] = int(sm)
            final_one = input('''Что дальше:
    1 - Перейти в главное меню
    2 - Выход
    ''')
            if final_one == '1':
                selection = input(menu)
            else:
                break
        else:
            print('Сумма, должна быть числом!')
            continue


    if selection == '2':
        question_about_balance = input('''Показать баланс:
    1 - По конкретной категории
    2 - По всем категориям
    ''')

        if question_about_balance == '1':
            select_category = input('Напишите категорию: ')
            if select_category in log_book:
                print(log_book[select_category])
                final_two = input('''
Что дальше:
1 - Перейти в главное меню
2 - Выход
''')
                if final_two == '1':
                    selection = input(menu)
                else:
                    break
            else:
                print('Категория указана не верно!')
                category_error = input('''
1 - Повторить ввод
2 - Показать список категорий
''')

                if category_error == '2':
                    print(*log_book.keys())



        '''
        Отсюда нужен выход в меню
        сейчас переходит в раздел "Показать баланс"
        '''
        if question_about_balance == '2':
            print(*log_book.values(), sep='\n')
            final_two = input('''
Что дальше:
1 - Перейти в главное меню
2 - Выход
''')
            if final_two == '1':
                selection = input(menu)
            else:
                break


    if selection == '3':
        break

with open('My expenses.json', 'w') as file:
    json.dump(log_book, file, indent=21)



