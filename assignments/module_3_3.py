# Распаковка позиционных параметров

def print_params(a=1, b='String', c=True):
    print(a,b,c)

# part 1
print_params(b=25) # работает
print_params(c=[1,2,3]) # работает

# part 2
values_list = [23, 'Strstr', True]
values_dict = {'a': 160, 'b': 'Abracadabra', 
               'c': False}
print_params(*values_list)
print_params(**values_dict)

# part 3
values_list_2 = [2, 'Stroka']
print_params(*values_list_2, 42)