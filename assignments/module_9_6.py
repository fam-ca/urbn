# генератор работает с помощью ключевого слова yield
# yield с помощью магического next возвращает итератор
# генератор использует ленивые вычисления


def all_variants(text):
    for i in range(1,len(text)+1):
        for k in range(len(text)-i+1):
            yield text[k:i+k]

a = all_variants("abc")
for i in a:
    print(i)