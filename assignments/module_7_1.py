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
    
    def add_product(self, product):
        return f'{self.get_products()}, {product.name}'

    def add(self, *products):
        file = open(self.__file_name, 'w')
        print(self.get_products())
        for product in products:
            print(product.name)
            if isinstance(product, Product):
                if product.name in self.get_products():
                    print(f'Продукт {str(product)} уже есть в магазине.')
                else:
                    file.write(str(product)+'\n')
                    self.add_product(product)


            else:
                print('Неверный тип данных.')
                break        
        file.close()




shop = Shop()
print(shop.get_products())
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# print(p1)
shop.add(p1, p2, p3)