import threading
import time
import os

os.chdir('assignments/module_10_1')
print(os.getcwd())

def write_words(word_count, file_name):
    start = time.time()
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write('Какое-то слово № ' + str(i+1) + '\n')
            time.sleep(0.1)
    stop = time.time()
    print(f'Завершилась запись в файл {file_name}')
    return stop-start

start1 = time.time()
word_counts = [10, 30, 200, 100]
file_names = ['example1.txt', 'example2.txt', 'example3.txt', 'example4.txt']
for i in range(4):
    write_words(word_counts[i], file_names[i])
stop1 = time.time()
print(f'Работа потоков: {(stop1-start1)} с.')


# работа с потоками
file_names = ['example5.txt', 'example6.txt', 'example7.txt', 'example8.txt']
start2 = time.time()

threads = [threading.Thread(target=write_words, args=(word_counts[i], file_names[i])) for i in range(4)]

for t in threads:
    t.start()

for t in threads:
    t.join()

stop2 = time.time()
print(f'Работа потоков: {(stop2-start2)} с.')