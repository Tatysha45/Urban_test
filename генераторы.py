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



# all_variants = 'abc'
# for i in all_variants:
#     print(i)
# for el in range(len(all_variants)):
#     if el > 1:
#         a = 0
#     else:
#         a = el
#     print(all_variants[a: el + 2])


# from itertools import combinations
#
# def all_subsequences(s):
#     out = set()
#     for r in range(1, len(s) + 1):
#         for c in combinations(s, r):
#             out.add(''.join(c))
#     return sorted(out)