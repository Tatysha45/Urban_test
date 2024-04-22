def all_variants(all_variants):
    for i in all_variants:
        yield i
    for el in range(len(all_variants)):
        if el > 1:
            a = 0
        else:
            a = el
        yield (all_variants[a: el + 2])

for substr in all_variants('abc'):
    print(substr)