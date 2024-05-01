
from collections import defaultdict
import random
import threading
import queue
import time

FISH = [None, 'Лещ', 'Плотва', 'Окунь']


class Fisher(threading.Thread):

    def init(self, name, worms, catcher, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm}, забросил, ждем', flush=True)
            time.sleep(random.randint(5, 20)/ 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка', flush=True)
            else:
                print(f'{self.name}, {worm}:поймал {fish} и хочет положить его в садок', flush=True)
                if self.catcher.full():
                    print(f'{self.name}, {worm}:приемщик полон')
                self.catcher.put(fish)
                print(f'{self.name}, {worm}:наконец положил {fish} в садок', flush=True)


class Boat(threading.Thread):

    def __init__(self, worms_per_fisher = 10, *args, **kwargs):
        super(Boat, self).__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.catcher = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, catcher=self.catcher)
        self.fishers.append(fisher)

    def run(self):
        print('Лодка вышла в море', flush=True)

        for fisher in self.fishers:
            fisher.start()

        while True:
            try:
                fish = self.catcher.get(timeout = 1)
                print('Приемщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] +=1

            except queue.Empty:
                print('Приемщику нет рыбы  в течении 1 сек', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break

        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)

boat = Boat(worms_per_fisher=10)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый']

for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()

print(f'Лодка привезла {boat.fish_tank}')


