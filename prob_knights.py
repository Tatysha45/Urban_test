# import random
# import time
# from collections import defaultdict
# from threading import Thread
#
#
# SKILL = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110)
#
# class Knight(Thread):
#     def __init__(self, name, skills, day, *args, **kwargs):
#         super(Knight, self).__init__(*args, **kwargs)
#         self.name = name
#         self.skills = skills
#         self.day = day
#         self.kill = defaultdict(int)
#     def run (self):
#         self.kill = defaultdict(int)
#         for skill in range(self.skills):
#             print(f'{self.name} сражается день {skill} врагов', flush=True)
#             _ = 5 ** (random.randint(50, 70) * 10000)
#             if skill is None:
#                 print(f'{self.name}: никто сегодня не напал')
#             else:
#                 print(f'{self.name} у меня сегодня {skill} врагов', flush=True)
#                 self.kill[skill] += 10
#         print(f'Итого {self.name} убил:')
#         for skills, count in self.kill.items():
#             print(f'    {skills} - {count}')
#
# knight1 = Knight(name='Sir_Lancelot', skills=10, day=10)
# knight2 = Knight(name='Sir_Galahad', skills=20, day=5)
#
# print('.' * 20, 'Sir_Lancelot, на нас напали!')
# print('.' * 20, 'Sir_Galahad, на нас напали!')
#
# knight1.start()
# knight2.start()
#
# print('.' * 5, 'Ждем')
#
# knight1.join()
# knight2.join()
#
# print('.' * 5, 'Битвы закончились!')
#
# for skills in ():
#     print(f'Итого  {knight1.name} убил:')
#     for kill, count in knight1.skills.items():
#         print(f'    {Knight} - {count}')
# for skills in ():
#     print(f'Итого  {knight2.name} убил:')
#     for kill, count in knight2.skills.items():
#         print(f'    {Knight} - {count}')




import time
from threading import Thread
class Knight(Thread):
    def __init__(self, name, skill, *args, enemys=100, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemys = enemys

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemys != 0:
            time.sleep(1)
            days += 1
            self.enemys -= self.skill
            print(f'{self.name}, сражается {days} день(дня)..., осталось {self.enemys} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')


