from itertools import count

log_book = {"market": 1000,
            "sport": 500,
            "try": 100}


# def not_category():
#     print(' Такой категории не существует!')
#     print()
#     while True:
#         category_error = input('''Что дальше:
#  1 - Ввести категорию заново
#  2 - Посмотреть список категорий
#  ''')
#         if category_error == '2':
#
#             print(*log_book, sep='\n')
#             print()
#             break
#         elif category_error == '1':
#             print()
#             break
#         else:
#             print('Нет такой команды, попробуй снова!')
#             print()
#             continue
#
# # Вместо рекурсии использовать цикл while
# def specific_balance():
#     # select_category = input('Напишите категорию: ')
#     while True:
#         select_category = input('Напишите категорию: ')
#         if select_category in log_book:
#             print(log_book[select_category])
#             break
#
#
#         else:
#             not_category()
#         #     print('Такой категории не существует!')
#         #     print()
#         #
#         #     category_error = input('''Что дальше:
#         # 1 - Ввести категорию заново
#         # 2 - Посмотреть список категорий
#         # ''')
#         #     if category_error == '2':
#         #
#         #         print(*log_book, sep='\n')
#         #         print()
#         #         continue
#         #     elif category_error == '1':
#         #         continue
#         #
#         #     else:
#         #         print('Нет такой команды, попробуй снова!')
#
# specific_balance()

print(*log_book, sep='\n')
del_category = input('''Какую категорию хотите удалить: 
''')














