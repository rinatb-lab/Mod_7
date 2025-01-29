#from fileinput import close
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}\n'

class  Shop():
    __file_name = 'products.txt'
    file = open(__file_name, 'a')
    file.close()

    def get_products(self):
        f1 = open(self.__file_name, 'r')
        #pprint(f1.read())
        f = f1.read()
        f1.close()
        return f

    def add(self, *products):
        file = open(self.__file_name, 'r')
        file1 = file.read()
        file.close()
        for product in products:
            #print(product)
            if f'{product.name}, {product.weight}, {product.category}\n' in file1:
                print(f'Продукт,{product.name}, уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product.name}, {product.weight}, {product.category}\n')
                file.close()





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())


