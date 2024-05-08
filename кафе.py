import threading
import queue
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Cafe:

    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):
            time.sleep(1)
            print(f"Посетитель номер {i} прибыл")
            customer = {"number": i}
            self.queue.put(customer)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer['number']} ожидает свободный стол (помещение в очередь)")
                time.sleep(5)
                table.is_busy = False
                print(f"Посетитель номер {customer['number']} сел за стол {table.number} (начало обслуживания)")
                return print(f"Посетитель номер {customer['number']} покушал и ушёл (конец обслуживания)")
        self.queue.put(customer)


def customer_thread(cafe):
    while True:
        customer = cafe.queue.get()
        cafe.serve_customer(customer)
        cafe.queue.task_done()
        if cafe.queue.empty():
            break


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

for _ in range(3):
    t = threading.Thread(target=customer_thread, args=(cafe,))
    t.start()

customer_arrival_thread.join()
