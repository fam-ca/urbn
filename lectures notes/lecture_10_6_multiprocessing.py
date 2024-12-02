# import multiprocessing
# import time
# import threading

# counter = 0


# def first_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print('First worker changed the counter to ', counter)


# def second_worker(n):
#     global counter
#     for i in range(n):
#         counter += 1
#         time.sleep(1)
#     print('Second worker changed the counter to ', counter)

# if __name__== '__main__':
#     process1 = multiprocessing.Process(target=first_worker, args=(10,))
#     process2 = multiprocessing.Process(target=second_worker, args=(15,))
#     process1.start()
#     process2.start()

import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(counter)
