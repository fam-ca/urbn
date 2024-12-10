# from module_6_2
class Vehicle: 
    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'BLUE', 'RED']
    
    def __init__(self, owner: str,
                    __model: str = 'Toyota',
                    __color: str = 'black',
                    __engine_power: int = 750
                    ):
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



def introspection_info(obj):
    info = {}
    info['type']= type(obj).__name__ #obj.__class__.__name__
    info['attributes'] = dir(obj)
    info['methods'] = [method for method in dir(obj) if not (method.startswith('__') or method.startswith('_') ) ]
    info['module'] = obj.__module__
    return info

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print(introspection_info(vehicle1))