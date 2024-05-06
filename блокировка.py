# -*- coding: utf-8 -*-

import random
import threading
import time
from collections import defaultdict
from threading import Thread

class BankAccount:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print("Insufficient funds")


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit = threading.Thread(target=deposit_task, args=(account, 100))
withdraw = threading.Thread(target=withdraw_task, args=(account, 150))

deposit.start()
withdraw.start()

deposit.join()
withdraw.join()

print(f'Итого счет пополнен {account.deposit} , а снято со счета {account.withdraw}')
print(f'Итоговый балланс: {account.balance}')
