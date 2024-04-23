# import random
# import time
# from collections import defaultdict
# from threading import Thread
#
#
# SKILL = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
#
# class Knight(Thread):
#     def init(self, name, skills, day, *args, **kwargs):
#         super(Knight, self).init (*args,**kwargs)
#         self.name = name
#         self.skills = skills
#         self.day = day
#         self.catch = defaultdict(int)
#     def run (self):
#         self.catch = defaultdict(int)
#         for skills in range(self.skills):
#             print(f'{self.name} сражается день (дня) {skills} врагов', flush= True)
#             _ = 5**random.choice(SKILL)
#             if skills is None:
#                 print(f'{self.name}: никто сегодня не напал')
#             else:
#                 print(f'{self.name} у меня сегодня {skills} врагов', flush= True)
#                 self.catch[skills] += 1
#         print(f'Итого {self.name} убил:')
#         for skills, count in self.catch.items():
#             print(f'{skills} - {count}')
#
# Sir_Lanselot = Knight(name = 'Sir_Lanselot', SKILL=20, day = 5)
# Sir_Galahat = Knight(name = 'Sir_Galahat', SKILL=50, day = 3)
#
# print('.'*20, 'Sir_Lanselot, на нас напали!')
# print('.'*20, 'Sir_Galahat, на нас напали!')
# Sir_Lanselot.start()
#
# Sir_Galahat.start()
# print('.'*5, 'Ждем')
# Sir_Lanselot.join()
# Sir_Galahat.join()
# print('.'*5, 'Битвы закончились!')



def all_variants(text):
    for i in text:
        yield i
    for el in range(len(text)):
        if el > 1:
            a = 0
        else:
            a = el
        yield text[a: el + 2]


for substr in all_variants('abcd'):
    print(substr)