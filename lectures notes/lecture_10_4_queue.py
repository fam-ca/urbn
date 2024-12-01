from queue import Queue # для синхронизации потоков
# FIFO - first in first out
import time
import threading

def getter(queue):
    while True:
        time.sleep(2)
        item = queue.get()
        print(threading.current_thread(), 'Took eleement', item)

queue = Queue(maxsize=10)
thread1 = threading.Thread(target=getter, args=(queue,), daemon=True)
thread1.start()

for i in range(10):
    time.sleep(1)
    queue.put(i)
    print(threading.current_thread(), 'put the element to the queue', i)


q = Queue()
q.put(5)
print(q.get(timeout=2))
print('End')