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


lst = [1, 2, 3, 4, 5, 6, 7, 8]
iterator = iter(lst)

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

# генераторные выражения способ создания итерируемого объекта, не загружая память
squares = (x * x for x in range(10))
print(next(squares))
print(next(squares))

# генераторные последовательности
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
