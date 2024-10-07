class House:
    houses_history= []
    def __new__(cls, *args, **kwargs):
        '''
        The name of the house is added to the list of all houses
        after the object being created.
        '''
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, num):
        self.name = name
        self.number_of_floors = num

    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    
    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории.')
    
    
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует.')
        else:
            for i in range(new_floor):
                print(i+1)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Second argument in not a type of House.'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Second argument in not a type of House.'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Second argument in not a type of House.'
   
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Second argument in not a type of House.'
    
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Second argument in not a type of House.'
    
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Second argument in not a type of House.'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value
    
    


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
