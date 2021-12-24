from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, terminal, id):
        for i in terminal.pizzas_list:
            if i["id"] == id:
                self.set_information(i)

        for i in terminal.drinks_list:
            if i["id"] == id:
                self.set_information(i)

    # set base information about product (every product has a name and a price)
    def set_information(self, product_tuple):        
        self._name = product_tuple["name"]
        self._price = product_tuple["price"]

    # print base information about product (every product has a name and a price)
    def show_information(self):
        print("Name: {}".format(self._name))
        print("Price: {}".format(self._price))

    # getter for _price
    @property
    def price(self):
        return self._price

    # getter for _name
    @property
    def name(self):
        return self._name

    # setter for price
    @price.setter
    def price(self, price):
        if (price >= 0):
            self._price = price
        else:
            raise ValueError

    # abstract method that overrides in Pizza and Drink classes
    @abstractmethod
    async def prepare_self(self):
        pass