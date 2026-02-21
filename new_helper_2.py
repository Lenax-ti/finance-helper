import json


menu = '''Что вы хотите сделать?:
    1 - Записать расходы
    2 - Показать баланс
    3 - Выйти
'''

selection = input(menu)



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
            selection = input(menu)
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
                selection = input(menu)

            else:
                print('Категория указана не верно!')
                category_error = input('''
1 - Повторить ввод
2 - Показать список категорий
3 - Выход
''')
                if category_error == '1':
                    continue
                    # Вернуться к началу цикла и попросит ввести категорию заново

                elif category_error == '2':
                    print(*log_book.keys(), sep='\n')
                    continue
                    # Что бы снова спросить категорию

                elif category_error == '3':
                    print('Хорошего дня!')
                    break

        if question_about_balance == '2':
            for key, value in log_book.items():
                print(key, value)
            selection = input(menu)


    if selection == '3':
        print('Хорошего дня!')
        break

with open('My expenses.json', 'w') as file:
    json.dump(log_book, file, indent=15)



