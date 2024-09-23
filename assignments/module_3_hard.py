def data_structure_count_size(data_structure, *args):
    count = 0

    if isinstance(data_structure, list) or isinstance(data_structure, tuple) or isinstance(data_structure, set):
        for i in data_structure:
            count += data_structure_count_size(i)
    elif isinstance(data_structure, dict):
        for ks, vls in data_structure.items():
            count += data_structure_count_size(ks)
            count += data_structure_count_size(vls)
    elif isinstance(data_structure, int):
        count += data_structure
    elif isinstance(data_structure, bool):
        count += int(data_structure)
    elif isinstance(data_structure, str):
        count += len(data_structure)

    return count

# print(data_structure_count_size([2,'trurr', {'ad': 1, 'b': 2, 'c': 3}]))
# print(data_structure_count_size([4]))
# print(data_structure_count_size([True]))
# print(data_structure_count_size(['Hello!']))

# dict = {'ad': 1, 'b': 2, 'c': 3}
# print(dict.items())


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(data_structure_count_size(data_structure))