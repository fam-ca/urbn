import os
import time

# print('Current directiry', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')

# print('Current directiry:', os.getcwd())

# print(os.listdir())
# for i in os.walk('.'):
#     print(i)

# os.chdir('/home/ruslan/urbn/assignments')
# print(os.getcwd())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(file)
# # print(dirs)
# os.startfile(file[0])
# # os.path.join()
# print(os.path.getmtime( os.getcwd()))

directory = '.'
for root, dirs, files in os.walk(directory):

    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
