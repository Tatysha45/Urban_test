def print_params(a, b, c):
    return (a, b, c)

values_list = [1, 2, 3]
res = print_params(*values_list)
print(res)

values_list = [3, 25, [1, 2, 3]]
res = print_params(*values_list)
print(res)

values_list = (2.25, 10, 146)
res = print_params(*values_list)
print(res)

values_dict = {'a':2.25, 'b':10, 'c':146}
res = print_params(**values_dict)
print(res)

values_list = (5, 7)
values_dict = dict(c=9)
res = print_params(*values_list, **values_dict)
print(res)

values_list_2 = (2, 42)
res = print_params(*values_list)
print(res)