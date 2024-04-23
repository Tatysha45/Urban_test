import random
import time
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')

class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms

    def ran(self):
        self.catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{self.name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1
        print(f'Итого рыбак {self.name} поймал:')
        for fish, count in self.catch.items():
            print(f'    {fish} - {count}')

vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)

print('.' * 20, 'Они пошли на рыбалку')

vasya.start()
kolya.start()

print('.' * 20, 'Ждем пока они вернутся...')

vasya.join()
kolya.join()

print('.' * 20, 'Итак, они вернулись')

for fisher in (vasya, kolya):
    print(f'Итого рыбак {fisher.name} поймал:')
    for fish, count in fisher.catch.items():
        print(f'    {fish} - {count}')
