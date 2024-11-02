def custom_write(file_name, strings):
    file = open(file_name, 'w')
    string_positions = {}
    for i in range(len(strings)):
        start = file.tell()
        file.write(strings[i] + ' \n')
        string_positions.update({(i+1, int(bytes(str(start), encoding = 'utf-8'))): strings[i]})
    file.close()
    return string_positions

# a = ['fret', 'df']
# print(bytes(a[0][1], encoding = 'utf-8'))


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)