# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

first_result = list(map(lambda x, y: x==y, first, second))
print(first_result)


# Функция высшего порядка
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for data in data_set:
                file.write(str(data)+'\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Повторение на работу с файлами
import os
os.chdir('assignments/module_9_4')

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        import random
        try:
            return random.choice(self.words)
        except IndexError:
            return 'Пустая строка'
        
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

second_ball = MysticBall()
print(f'Проверка на ввод пустой строки: {second_ball()}')