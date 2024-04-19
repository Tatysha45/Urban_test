# def string_to_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return f"Ошибка: невозможно преобразовать '{s} в целое число"
#
#
# def read_file(filename):
#     try:
#         with open(filename, 'r') as file: return file.read()
#     except FileNotFoundError:
#         return f"Ошибка ввода/вывода при работе с файлом '{filename}'."
#
#
# def divide_numbers(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'Ошибка! Деление на 0'
#     except TypeError:
#         return "Ошибка: аргументыне могут быть числами"
#
#
# def access_list_element(lst, index):
#     try:
#         return lst[index]
#     except IndexError:
#         return f"Ошибка: индекс {index} вне диапазона списка"
#     except TypeError:
#         return "Ошибка: индекс должен быть целым числом"



import  requests

url = 'http://ya.ru'
try:
    data = requests.get(url)
    print(data.text)
except requests.ConnectionError as exc:
    print(f'не могу соединиться с {url} потому что {exc}')