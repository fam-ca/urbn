import time
from multiprocessing import Pool
def reaf_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


import os
print(os.getcwd())
os.chdir('assignments/module_10_5')
print(os.getcwd())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов
start = time.time()
for i in range(4):
    reaf_info(filenames[i])

end = time.time()
print(f'{end-start} (линейный)')


# многопроцессный
start2 = time.time()
if __name__=='__main__':
    with Pool(4) as p:
        p.map(reaf_info, filenames)
end2 = time.time()
print(f'{end2-start2} (многопроцессный)')