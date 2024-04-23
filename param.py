def print_params(param):
    print("вызвать функцию с параметром", param)

my_list = ['5', '7', '9']

for element in my_list:
    print('начало')
    print_params(element)
    print('конец')


def print_params():
    print('я функция')


for i in range(5):
        print_params()