# def all_variants(text):
#     for i in text:
#         yield i
#     for el in range(len(text)):
#         if el > 1:
#             a = 0
#         else:
#             a = el
#         yield text[a: el + 2]
#
#
# for substr in all_variants('abc'):
#     print(substr)


def all_variants(text):


    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


for substr in all_variants('abcd'):
    print(substr)