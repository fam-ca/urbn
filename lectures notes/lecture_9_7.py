# декоратор возвращает функцию
# @ используется для декорирования функции за один шаг

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'



print(greet())


import time
import sys
def time_track(func):
    def surrogate(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {round(end-start, 4)} second(s).')
        return result
    return surrogate

def digits(*args):
    total = 1
    for number in args:
        total *= number **5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

result = digits(3456, 8655, 978, 7800)
print(result)