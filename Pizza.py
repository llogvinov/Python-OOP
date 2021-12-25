from Product import Product
from time import sleep


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
        self.sauces = product_tuple["sauces"]
        self.filling = product_tuple["filling"]


    # show base and additional information
    def show_information(self):
        super().show_information()
        print("Sauce: {}".format(self.sauces))
        print("Filling: {}".format(self.filling))


    # abstract method
    def print_information(self):
        print("Start prepearing {} pizza...".format(self.name))
        sleep(0.5)


    # abstract method
    # FACADE PATTERN
    def start_preparing(self):
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
        print('\n')


    def _knead_dough(self):
        print("Knead the dough")


    def _collect_ingredients(self, filling):
        print("Collect ingredients: {}".format(filling))


    def _cut(self):
        print("Cut the pizza")


    def _pack(self):
        print("Pack the pizza: {}".format(self.name))