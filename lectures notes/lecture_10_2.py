import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.counter = counter
        self.delay = delay
        self.name = name

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1
    def run(self):
        print(f'Thread {self.name} started')
        self.timer(self.name, self.counter, self.delay)
        print(f'Thread {self.name} finished')


thread1 = MyThread('thread1', 5, 1)
thread2 = MyThread('thread2', 3, 0.5)
thread1.start()
thread2.start()