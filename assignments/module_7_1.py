from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    

class Shop:
    def __init__(self):
        self.__file_name = 'assignments/files/products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = ''
        for line in file:
            products += (line.strip().split(',')[0]) + ' '
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        all_products = set(self.get_products())
        for product in products:
            # print(product.name)
            if isinstance(product, Product):
                if product.name not in self.get_products():
                    file.write(str(product)+'\n')
                    all_products.add(product.name)
                    # print(f'Добавлен продукт {product.name}')
                else:
                    print(f'Продукт {str(product)} уже есть в магазине.')
            else:
                print('Неверный тип данных.')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
