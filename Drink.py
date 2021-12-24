from Product import Product
from time import sleep


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

    def print_information(self):
        print("Start preparing {} drink...".format(self.name))
        sleep(0.5)

    def start_preparing(self):
        self.pour()
        sleep(1)

    def pour(self):
        print("Pouring {}...".format(self.name))

    