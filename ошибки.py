# -*- coding: utf-8 -*-

# try:
#
#
# except MyException1 as e: #если случиться это исключение, мы
#     print(f"Ошибка {e}") # передадим эту информацию в
#     raise # вызвавшую функцию
#
# except MyException2 as e: # а если случиться это исключение
#     print(f"Внимание: {e}") # то вызвавшая функция не узнает что произошло исключение

class Exception:
    pass


class MyCustomException(Exception):
    pass
    raise MyCustomException("Это мое собственное исключение")

def __init__(self, message, extra_info):
    super().__init__(message)
    self.extra_info = extra_info



raise MyCustomException("Произошла ошибка", {"code": 400, "time": "12:34"})

try:
    raise MyCustomException("Произошла ошибка", {"code": 400, "time": "12:34"})
except MyCustomException as e:
    print(f"Сообщение об ошибке: {e}")
    print(f"Дополнительная информация: {e.extra_info}")
