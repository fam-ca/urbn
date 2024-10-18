class Vehicle: 
    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'BLUE', 'RED']
    
    def __init__(self, owner,
                    __model = 'Toyota',
                    __color = 'black',
                    __engine_power = 750
                    ):
        '''
        owner: str
        __model: str
        __engine_power: int
        __color: str
        '''
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        
    def get_model(self):
        return f'Модель: {self.__model}'
    
    def get_horse_power(self):
        return f'Мощность двигателя: {self.__engine_power}'
    
    def get_color(self):
        return f'Цвет: {self.__color}'
    
    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horse_power()} \n{self.get_color()} \
               \nВладелец: {self.owner}')
    
    def set_color(self, new_color):
        if new_color.upper() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
    

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# # Проверяем что поменялось
vehicle1.print_info()

print(vehicle1._Sedan__PASSENGERS_LIMIT)



















# class Human:
#     head = True
#     _legs = True
#     __arms = True
#     def about(self):
#         print(self.head)
#         print(self._legs)
#         print(self.__arms)
    
        
# class Student(Human):
#     _legs = False


# human = Human()
# # human.about()

# student = Student()
# # student.about()

# # print(student.__arms) # error
# print(human._Human__arms) # _Human__arms is __arms in class Human