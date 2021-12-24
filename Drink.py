from Product import Product
import asyncio

class Drink(Product):
    
    def __init__(self, terminal, id):
        super().__init__(terminal, id)

    def __str__(self) -> str:
        return "Drink class"

    # set base and additional information
    def set_information(self, product_tuple):
        super().set_information(product_tuple)
        self.size = product_tuple["size"]
    
    # show base and additional information
    def show_information(self):
        super().show_information()
        print("Size {}".format(self.size))

    # abstract method
    async def prepare_self(self):
        print("Pouring {}...".format(self.name))
        await asyncio.sleep(1)
        print('\n')

    