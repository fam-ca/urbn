# список, строки - итерируемые объекты, внутри итерируемого объекта есть итератор __iter__, __next__
# итератор
# next - метод для получения следующего значения итератора
# у каждого итерируемого объекта есть функция next
# но применить next можно только к итератору
# next(list_) # не сработает!
lst = [1, 2, 3, 4, 5, 6, 7, 8]
iterator = iter(lst) # получение итератора

class Humans:
    def __init__(self, group):
        self.group = group
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.group):
            first = self.group[self.counter]
            self.counter += 1
            return first
        else:
            raise StopIteration

students = Humans(['Alice', 'Bob', 'Charlie'])
print(iter(students))

for i in students:
    print(i)

'''по-хорошему нужно реализовать отдельный класс для итератора и убрать __next__ 
внутри Humans, оставив только __iter__
Итерируемый объект - это тот, у кого есть итератор.
А внутри итератор определна логика, что мы будем передавать последующим элементом
'''

def choice_func(choice):
    x = 2
    y = 3
    if choice == 1:
        return lambda x, y: x + y
    if choice == 2:
        return lambda x, y: x ** y
    if choice == 3:
        return lambda x, y: x // y

# print(choice_func(1))


# map
list_square = list(map(lambda x: x**2, lst))
print(list_square)

# filter
evens = list(filter(lambda x: x%2==0, lst))
print(evens)

# reduce
from functools import reduce
total = reduce(lambda x, y: x+y, lst)
print(total)

'''
генераторные выражения способ создания итерируемого объекта, не загружая память
генератор помнит только о текущем элементе, который будут передавать
генератор - частное решение итератора 
'''

squares = (x * x for x in range(10))
print(next(squares))
print(next(squares))

# генераторные последовательности
# yield похож на return, но разница в том, что после yield функция продолжит работать
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        # return a, b

print()
f = fib()
print(next(f))
# print(next(f) )
# print(next(f) )
# print(next(f) )


# декоратор
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time {end-start}')
        return result
    return wrapper

@timer 
def generator():
    lst = [lambda x: x for i in range(1000000)]
    # lst = [i for i in range(1000000)]
    return lst

generator()
