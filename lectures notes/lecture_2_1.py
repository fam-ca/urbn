# import this

# *args используется, когда мы не знаем, какое количество переменных будет передаваться в аргумент функции
# def func(*args, **kwargs): 

a = 5
b = 10 
def func():
    a = 2
    b = 2
    print(a, b)

func()
print(a, b)