def get_multiplier_v1(n):
    if n == 7:
        def multiplier(x):
            return x * 7
    elif n == 3:
        def multiplier(x):
            return x / 3
    else:
        raise Exception('умножаем на 7, делим на 3')
    return multiplier


my_checklist = [7, 2, 6, 9, 12, 1, 5, 32]

by_2 = get_multiplier_v1(n=7)
by_3 = get_multiplier_v1(n=3)
result = map(by_2, my_checklist)
print(list(result))
result = map(by_3, my_checklist)
print(list(result))

result = map(lambda x: x * x, my_checklist)
print(list(result))


class Multiplaer:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        self.new_x = []
        for el in x:
            self.new_x.append(el * 40)
        return self.new_x

my_checklist = [7, 2, 6, 9, 12, 1, 5, 32]
by_width = Multiplaer(n = 40)
result = by_width(x = my_checklist)
print(result)