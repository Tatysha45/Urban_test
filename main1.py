import json
# from typing import List
#
#
# def employees_rewrite(sort_type: str):
#     # Чтение исходного файла
#     with open('employees.json', 'r') as file:
#         data = json.load(file)
#
#     # Проверка наличия ключа в словаре
#     if sort_type not in ['firstName', 'lastName', 'department', 'salary']:
#         raise ValueError('Bad key for sorting')
#
#     # Сортировка списка сотрудников
#     sorted_employees = sorted(data['employees'], key=lambda x: x[sort_type])
#
#     # Формирование нового словаря с отсортированными данными
#     new_data = {
#         "employees": sorted_employees
#     }
#
#     # Сохранение результата в файл
#     filename = f'employees_{sort_type}_sorted.json'
#     with open(filename, 'w') as file:
#         json.dump(new_data, file, ensure_ascii=False, indent=4)
#
#
# # Пример использования функции
# try:
#     employees_rewrite('lastName')
# except ValueError as e:
#     print(e)


def employees_rewrite(sort_type):
    valid_keys = {"firstname", "lastname", "department", "salary"}
    sort_type = sort_type.lower()

    if sort_type not in valid_keys:
        raise ValueError('Bad key for sorting')

    with open("employees.json", "r") as file:
        data = json.load(file)

    sorted_data = sorted(data["employees"], key=lambda x: x[sort_type], reverse=(sort_type == "salary"))

    with open(f"employees_{sort_type}_sorted.json", "w") as file:
        json.dump({"employees": sorted_data}, file, indent=4)


# Пример вызова функции для сортировки по lastname
employees_rewrite('lastname')
# Пример вызова функции для сортировки по department
#employees_rewrite('department')
# Пример вызова функции для сортировки по salary
#employees_rewrite('salary')
# Пример вызова функции с неверным ключом для сортировки
# employees_rewrite('position')