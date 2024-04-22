from threading import Thread
import time

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
