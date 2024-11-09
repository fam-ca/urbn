class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step==0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step
        self.start = start
        self.stop = stop
        self.pointer = self.start
        
    # итератор использует ленивые вычисления, быстрее работают, экономят память
    def __iter__(self):
        self.pointer = self.start
        return self
    
    def __next__(self):
        if (self.step > 0 and self.pointer <= self.stop) or (self.step < 0 and self.pointer >= self.stop):
            current = self.pointer
            self.pointer += self.step
            return current
        raise StopIteration() # признак того, что нечего возвращать
        


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1) # ничего не вернет, поскольку шаг положительный, а нужно двигатьсяв отрицательную сторону


for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
