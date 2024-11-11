# декоратор возвращает функцию
# @ используется для декорирования функции за один шаг

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(1, result-1):
            if result %i == 0:
                flag = 'Составное'
            else:
                flag = 'Простое'
        print(flag)
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)