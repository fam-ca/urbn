from threading import Thread, Event
import time
# Event используется для синхронизации потоков

def first_worker():
    print('First worker started the task')
    event.wait()
    print('First worker continued the task')
    time.sleep(5)
    print('First worker finished the task')

def second_worker():
    print('Second worker started the task')
    time.sleep(10)
    print('Second worker finished the task')
    event.set()

event = Event()


thread1 = Thread(target=first_worker)
thread2 = Thread(target=second_worker)
thread1.start()
thread2.start()

# print(event.set())
event.wait(timeout=5)
# print(event.is_set()) # if False - no events yet
# event.clear() # сброс флага event