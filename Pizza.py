from Product import Product
import asyncio

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
    async def prepare_self(self):
        print("Start prepearing {} pizza...".format(self.name))
        await asyncio.sleep(0.5)
        self._knead_dough()
        await asyncio.sleep(0.5)
        self._collect_ingredients(self.filling)
        await asyncio.sleep(1.5)
        self.bake_food(220)
        await asyncio.sleep(2)
        self._cut()
        await asyncio.sleep(0.5)
        self._pack()
        await asyncio.sleep(0.5)
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

