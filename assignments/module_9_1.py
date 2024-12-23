def apply_all_func(int_list, *functions):
    results = {}
    try:
        for function in functions:
            results[function.__name__] = function(int_list)
    except TypeError:
        return 'Некорректный тип данных'
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

print(apply_all_func(['svf', 20, 15, 9], len, sum, sorted))