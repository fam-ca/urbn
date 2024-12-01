from queue import Queue # для синхронизации потоков
# FIFO - first in first out
import time
import threading
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
        sleep_for = random.randint(3, 10)
        # print(f'Thread start and finishes in {sleep_for} secs')
        time.sleep(sleep_for)
        # print('Thread complete')


class Cafe:
    def __init__(self, *args, queue: Queue = Queue()):
        self.tables = args
        self.queue = queue

    def free_table(self):
        fr_table = None
        for table in self.tables:
            if table.guest is None:
                fr_table = table
                break
        return fr_table

    def guest_arrival(self, *guests: Guest):
        for i in range(len(guests)):
            fr_table = self.free_table()
            if fr_table:
                fr_table.guest = guests[i]
                guests[i].start()
                print(f'{guests[i].name} сел(-а) за стол номер {fr_table.number}.')
            else: 
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди.')
    

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

            while not self.queue.empty():
                fr_table = self.free_table()
                if not fr_table:
                    break
                new_guest = self.queue.get()
                fr_table.guest = new_guest
                new_guest.start()
                print(f'{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {fr_table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
