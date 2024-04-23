def all_variants(text):
    for i in text:
        yield i
    for el in range(len(text)):
        if el > 1:
            a = 0
        else:
            a = el
        yield text[a: el + 2]


for substr in all_variants('abc'):
    print(substr)
