calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    tuple = (len(string), string.upper(), string.lower())
    return tuple


def is_contains(str, list_to_search):
    count_calls()
    string = str.lower()
    list_new = []
    for i in range(len(list_to_search)):
            list_new.append(list_to_search[i].lower())
    if string in list_new:
                return True
    else:
        return False
    

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)