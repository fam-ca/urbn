# Task 2
my_dict = {'Alex': 1997, 'Vasya': 2000, 'Kirill': 1980}
print('Initial dictionary: ', my_dict)
print('Existing value: ', my_dict['Kirill'])
print('Non existing value: ', my_dict.get('Sveta'))

my_dict.update({'Roman':1996,
                'Petr':2002})

a = my_dict.pop('Vasya')
print('Deleted value: ', a)

print('Modified dictionary: ', my_dict, '\n')

# Task 3
my_set = {'String', True, 23, 3.6, True, 'String', 3.6}
print('Initial set: ', my_set)
my_set.add(30)
my_set.add(False)
my_set.discard('String')
print('Modified set: ', my_set)