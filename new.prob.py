import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, enemies=100, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.enemies = enemies

    def run(self):
        days = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies != 0:
            time.sleep(1)
            days += 1
            self.enemies -= self.skill
            print(f'{self.name}, сражается {days} день(дня)..., осталось {self.enemys} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней!')


knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')


def numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


def numbers_1():
    for i in range(ord('a'), ord('k')):
        print(chr(i))
        time.sleep(1)


t1 = Thread(target=numbers)
t2 = Thread(target=numbers_1)

t1.start()
t2.start()
t1.join()
t2.join()