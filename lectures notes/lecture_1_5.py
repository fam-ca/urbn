# list список
# Особенности: элементы можно перебрать
# элементы можно изменить
# можно добавлять элементы в конец
# можно хранить элементы разных типов
# append добавляет целый элемент ввода
# extend добавляет поэлементно элемент ввода
# срезы работают также как в строках

# tuple кортеж неизменяемая! упорядоченность! можно зранить объекты разных типов
tuple = 1, 2, 3, 4
tuple_2 = (1, 2, 3, 4)
print(tuple)
print(tuple_2)
tuple = 1, 2, 3, 4, 'True', "String"
#tuple[0]= 200 # так нельзя писать!
print(tuple[0])

# кортеж занимает меньше места памяти, чем списки
tuple = 1, 2, 3, 4, 'True', "String"
list = [1, 2, 3, 4, 'True', "String"]
print(tuple.__sizeof__())
print(list.__sizeof__())
# но можно поменять часть элемента в кортеже, 
# например, когда в нем содержится список
tuple = [1,2], 2, 3, 4, 'True', "String"
tuple[0][0] = 2
print(tuple)
 
print(tuple*3)
