a = 'dragon'


def test_func():
    a = 'dinosaur'
    print(a)


test_func()
print(a)

print('a =', a)


def test_function():
    print('dinosaur')


def inner_function():
    print("Я в области видимости функции test_function")