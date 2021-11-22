from threading import Thread
from time import sleep
from Product import Product

# mixin class for products that can be baked (pizza, pie, ..)
class BakingMixin:
    
    def bake_food(self, temp):
        print("Bake at a tempreture {} degrees".format(temp))


class Pizza(Product, BakingMixin):
    
    def __init__(self, terminal, id):
        super().__init__(terminal, id)

    def __str__(self) -> str:
        return "Pizza class"

    # set base and additional information
    def set_information(self, product_tuple):
        super().set_information(product_tuple)
        self.sauce = product_tuple["sauces"]
        self.filling = product_tuple["filling"]

    # show base and additional information
    def show_information(self):
        super().show_information()
        print("Sauce: {}".format(", ".join(str(x) for x in self.sauce)))
        print("Filling: {}".format(", ".join(str(x) for x in self.filling)))

    # abstract method
    def prepare_self(self):
        print("New thread: starting")
        sleep(1)
        print("Start prepearing {} pizza...".format(self.name))
        sleep(0.5)
        self._knead_dough()
        sleep(0.5)
        self._collect_ingredients(self.filling)
        sleep(1.5)
        self.bake_food(220)
        sleep(2)
        self._cut()
        sleep(0.5)
        self._pack()
        sleep(0.5)
        print("New thread: finishing")
        print('\n')

    def _knead_dough(self):
        print("Knead the dough")

    def _collect_ingredients(self, filling):
        ingredients = ", ".join(str(x) for x in filling)
        print("Collect ingredients: {}".format(ingredients))

    def _cut(self):
        print("Cut the pizza")

    def _pack(self):
        print("Pack the pizza: {}".format(self.name))

