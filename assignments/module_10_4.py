from queue import Queue # для синхронизации потоков
# FIFO - first in first out
import time
import threading

# def getter(queue):
#     while True:
#         time.sleep(2)
#         item = queue.get()
#         print(threading.current_thread(), 'Took eleement', item)

# queue = Queue(maxsize=10)
# thread1 = threading.Thread(target=getter, args=(queue,), daemon=True)
# thread1.start()

# for i in range(10):
#     time.sleep(1)
#     queue.put(i)
#     print(threading.current_thread(), 'put the element to the queue', i)


# q = Queue()
# q.put(5)
# print(q.get(timeout=2))
# print('End')

import random
class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *args, queue: Queue = Queue()):
        self.tables = args
        self.queue = queue

    def is_empty(self):
        for table in tables:
            if table.guest != None:
                flag = False
            else:
                flag = True
        return flag

    def get_empty_table_idx(self):
        print(self.tables)
        for table in self.tables:
            if table.guest == None:
                return table.number
            else:
                continue

        
    def guest_arrival(self, *guests: Guest):
        i = 0
        while i<=len(guests): # while list of guests is not empty
            if self.is_empty():
                empty_table_idx = self.get_empty_table_idx()
                # print(empty_table_idx)
                self.tables[empty_table_idx].guest = guests[i]
                # print(self.tables[empty_table_idx].guest)

                print(self.tables[empty_table_idx].guest==None)
                print(f'{guests[i].name} сел(-а) за стол номер {empty_table_idx}.')
            else: 
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди.')
            i += 1
        return self.tables
    

    def discuss_guests(self):
        i = 0
        while not self.queue.empty():
            if self.tables[i].guest is not None and threading.current_thread().is_alive():
                print(f'{self.tables[i].guest} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {self.tables[i].number} свободен')
                self.tables[i].guest = None
                new_guest = self.queue.get()
                print(f'{new_guest} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}')
                thread_new_guest = threading.Thread(target=new_guest, )
                thread_new_guest.start()
            i += 1





# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
# cafe.discuss_guests()
