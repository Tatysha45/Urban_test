# -*- coding: utf-8 -*-

import random
import threading
import time
from collections import defaultdict
from threading import Thread

class BankAccount:
    def __init__(self, balance, deposit, withdraw, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.balance = balance
        self.deposit_amount = deposit
        self.withdraw_amount = withdraw
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(5):
            with self.lock:
                self.balance += self.deposit_amount

    def withdraw(self):
        for _ in range(5):
            with self.lock:
                if self.balance >= self.withdraw_amount:
                    self.balance -= self.withdraw_amount


account = BankAccount(1000, 100, 150)

deposit = threading.Thread(target=account.deposit)
withdraw = threading.Thread(target=account.withdraw)

deposit.start()
withdraw.start()

deposit.join()
withdraw.join()

print(f'Итого счет пополнен {account.deposit_amount * 5} , а снято со счета {account.withdraw_amount * 5}')
print(f'Итоговый балланс: {account.balance}')
