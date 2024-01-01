import copy
from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    def __init__(self, name, code):
        self.__name = name
        self.__code = code

    @property
    def get_name(self):
        return self.__name
    
    def set_name(self, n):
        self.__name = n

    @property
    def get_code(self):
        return self.__code
    
    def set_code(self, c):
        self.__code = c

    @abstractmethod
    def get_price(self):
        pass

    def __str__(self):
        return f"Product: \n- Name: {self.__name} \n- Code: {self.__code}"

    def __eq__(self, other):
        return self.get_code == other.get_code


class Elementary(Product):
    def __init__(self, name, code, purchase_price):
        super().__init__(name, code)
        self.__purchase_price = purchase_price

    @property
    def get_price(self):
        return self.__purchase_price

    def __str__(self):
        return f"{self.get_name}, Code: {self.get_code}, Purchase Price: {self.get_price}"

class Composition():
    def __init__(self, product, quantity):
        self.__product = copy.copy(product)
        self.__quantity = quantity

    @property
    def get_product(self):
        return self.__product

    
    def set_product(self, p):
        self.__product = p

    @property
    def get_quantity(self):
        return self.__quantity

    
    def set_quantity(self, q):
        self.__quantity = q

    def __str__(self):
        return f"\n{str(self.get_product)} \n- Quantity: {self.get_quantity}"

    def __eq__(self, other):
        return self.get_product == other.get_product and self.get_quantity == other.get_quantity

class Composite(Product):
    def __init__(self, name, code, man_cost, constituents, vat_rate=0.18):
        super().__init__(name, code)
        self.__man_cost = man_cost
        self.vat_rate = vat_rate
        self.__constituents = constituents

    @property
    def get_man_cost(self):
        return self.__man_cost

    @property
    def get_constituents(self):
        return self.__constituents

    def get_price(self):
        total = sum(x.get_product.get_price for x in self.__constituents)
        total += self.get_man_cost 
        return total

    def __str__(self):
        constituents_info = " ".join(f"{elem}" for elem in self.get_constituents)
        return f"- {self.get_name}\n- Code: {self.get_code}\
\n- Manufacturing Cost: {self.get_man_cost}\n- Constituents:{constituents_info}- Purchase Price: {self.get_price()}"


