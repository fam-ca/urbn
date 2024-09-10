immutable_var = 3, 4.5, 'True', 'String'
print('Immutable tuple: ', immutable_var)

# immutable_var[0] = 10
# объект кортежа не поддерживает присваивание его элементов
mutable_list = [1, 3, 'True', 'String']
mutable_list[2] = 'Modified'
print('Mutable list: ', mutable_list)
