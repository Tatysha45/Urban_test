from pprint import pprint


def introspection_info(obj):
    type_name = type(obj).__name__

    attributes = dir(obj)

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    try:
        module_name = obj.__module__
    except AttributeError:
        module_name = "Неизвестно"

    other_properties = {}
    for attr in attributes:
        value = getattr(obj, attr)
        if isinstance(value, str):
            other_properties[attr] = value

    result = {
        "Тип": type_name,
        "Атрибуты": attributes,
        "Методы": methods,
        "Модуль": module_name,
        "Другие свойства": other_properties
    }

    return result

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, {self.name}!")


my_instance = MyClass("Python")
info = introspection_info(my_instance)
pprint(info)