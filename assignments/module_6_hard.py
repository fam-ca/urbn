class Figure:
    def __init__(self, sides_count, color, *args):
        self.sides_count = sides_count
        self.filled = True
        self.__sides = []
        if self.sides_count==len(args): 
            for i in range(len(args)):
                self.__sides.append(args[i])
        elif len(args)==1:
            for i in range(self.sides_count):
                self.__sides.append(args[0])
        elif len(args)!=1:
            for i in range(self.sides_count):
                self.__sides.append(1)            
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def __is_valid_color(self, rgb):
        return 0<=rgb[0]<=255 and 0<=rgb[1]<=255 and 0<=rgb[2]<=255
    
    def set_color(self, r, g, b):
        if self.__is_valid_color((r,g,b)):
            self.__color = (r, g, b)
            flag = f'current color: {r, g, b}'
        else:
            flag = 'Invalid color'
        return flag
    
    def __is_valid_sides(self, sides_list):
        if self.sides_count==len(sides_list):
            for i in sides_list:
                if not isinstance(i, int) or i<=0:
                    return False
            return True
        else:
            return False
    
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        perimetr = 0
        # print(self.get_sides())
        sides = self.get_sides()
        # print(len(self.get_sides()))
        if self.__is_valid_sides(sides):
            for i in range(len(sides)):
                perimetr += sides[i]
        return perimetr
    
    def set_sides(self, *new_sides):
        if self.sides_count==len(new_sides):
            self.__sides = list(new_sides)
            return self.__sides

class Circle(Figure):
    def __init__(self, color, *args):
        self.sides_count = 1
        super().__init__(self.sides_count, color, *args)
        
        self.__radius = self.get_sides()[0] / (2*3.14)
        
    def get_radius(self):
        return self.__radius
    
    def get_square(self):
        return 3.14*self.__radius**2
    
    
class Triangle(Figure):
    def __init__(self, color, *args):
        self.sides_count = 3
        super().__init__(self.sides_count, color, *args)
    

    def get_square(self):
        p = len(self)/2
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        return (p*(p-a)*(p-b)*(p-c))**0.5


class Cube(Figure):
    def __init__(self, color, *args):
        self.sides_count = 12
        self.__sides = args
        super().__init__(self.sides_count, color, *args)

    def set_sides(self, *new_sides):
        if len(new_sides)==1:
            return [new_sides[0] for i in range(self.sides_count)]
        else:
            return self.__sides
        
    def get_volume(self):
        return self.__sides[0]**3
     

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# print(len(cube1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади треугольника
triangle1 = Triangle((200, 56, 0), 3, 4, 5)
print('Площадь треуг-ка: ', triangle1.get_square())
