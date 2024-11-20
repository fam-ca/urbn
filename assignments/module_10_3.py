import random
import threading
import time

import matplotlib.pyplot
class Bank:
    history = []
    def __init__(self, balance=0, lock=threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        '''
        выполняется 100 операции пополнения
        '''
        for i in range(100):
            random_value = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_value
            print(f'Пополнение: {random_value}. Баланс: {self.balance}.')
            time.sleep(0.001)
            Bank.history.append(self.balance)
        return self.balance
    
    def take(self):
        '''
        выполняется 100 операции снятия
        '''
        for i in range(100):
            random_value = random.randint(50, 500)
            print(f'Запрос на случайное число: {random_value}')
            if random_value <= self.balance:
                self.balance -= random_value
                print(f'Снятие: {random_value}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)
            Bank.history.append(self.balance)
        return self.balance

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

import matplotlib
inds = [x for x in range(len(Bank.history))]
matplotlib.pyplot.plot(inds, Bank.history, color='r')
# matplotlib.pyplot.show() # визуализация данных
    


