from datetime import datetime
from threading import Thread
from Pizza import Pizza
from Drink import Drink
from Product import Product


# decorator method
# writes data in text file
def write_added_position_to_file(method_to_decorate):
    def write_added_position(self, product):
        if not (isinstance(product, Product)):
            return

        with open("Orders.txt", "a") as order_file:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            order_file.write(dt_string + "\n")
            order_file.write("Added: " + product.name + "\n")
            order_file.write("Price: " + str(product.price) + "\n\n")
        return method_to_decorate(self, product)
    return write_added_position

def write_deleted_position_to_file(method_to_decorate):
    def write_deleted_position(self, product):
        if not (isinstance(product, Product)):
            return

        with open("Orders.txt", "a") as order_file:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            order_file.write(dt_string + "\n")
            order_file.write("Deleted: " + product.name + "\n")
            order_file.write("Price: " + str(product.price) + "\n\n")
        return method_to_decorate(self, product)
    return write_deleted_position

class Order:
    
    def __init__(self):
        self.ordered_products = []
        self.price = 0

    # add product and its price to order
    @write_added_position_to_file
    def add_position(self, product):
        self.add_product(product)
        self.add_price(product)

    def prepare_order(self):
        threads = []
        for product in self.ordered_products:
            new_thread = Thread(target=product.prepare_self())
            threads.append(new_thread)
            new_thread.start()
        
        for thread in threads:
            thread.join()

    def add_product(self, product):
        self.ordered_products.append(product)

    @write_deleted_position_to_file
    def delete_position(self, product):
        pass

    def delete_last_product(self):
        try:
            self.delete_position(self.ordered_products[-1])
            self.subtract_price(self.ordered_products[-1])
            self.ordered_products.pop(-1)
        except:
            print("Nothing to delete - the order is empty")

    # delete product by its number in order list
    def delete_product(self, number):
        try:
            self.delete_position(self.ordered_products[number - 1])
            self.subtract_price(self.ordered_products[number - 1])
            self.ordered_products.pop(number - 1)
        except:
            print("Invalid product number in order list")

    def add_price(self, product):
        self.price += product.price

    def subtract_price(self, product):
        self.price -= product.price

        if (self.price < 0):
            raise ValueError

    def clear_order(self):
        self.ordered_products.clear()

    # print information about an order
    def show_order(self):
        print("Ordered positions: {}".format(", ".join((x).name for x in self.ordered_products)))
        print("Final price is: {}\n".format(self.price))

    def get_order(self, terminal):
        while True:
            product = input("Do you want to add pizza or drink? p/d\nType e to end your order\n")

            if product == 'p':
                id = self.choose_pizza()
                p1 = Pizza(terminal, id)
                self.add_position(p1)
            elif product == 'd':
                id = self.choose_drink()
                d1 = Drink(terminal, id)
                self.add_position(d1)
            elif product == 'e':
                print("\n")
                self.check_order(terminal)
                return
            else:
                raise ValueError

    def choose_pizza(self) -> int:
        pizza_id = input("Select Pizza.. p/b/s\n")

        if pizza_id == 'p':
            return 101
        elif pizza_id == 'b':
            return 102
        elif pizza_id == 's':
            return 103
        else:
            raise ValueError

    def choose_drink(self) -> int:
        drink_id = input("Select Drink.. p/f/s/t/c\n")

        if drink_id == 'p':
            return 201
        elif drink_id == 'f':
            return 202
        elif drink_id == 's':
            return 203
        else:
            raise ValueError

    # prints infprmation about an order
    # asks customer if hi/she wants to edit an order
    def check_order(self, terminal):
        self.show_order()
        choice = input("Do you want to edit your order? y/n\n")
    
        if choice == 'n':
            self.confirm_order(terminal)
        elif choice == 'y':
            self.edit_order(terminal)
        else:
            raise ValueError

    def confirm_order(self, terminal):
        choice = input("Confirm and pay your order. y/n\n")

        if choice == 'n':
            self.edit_order(terminal)
        elif choice == 'y':
            self.prepare_order()
        else:
            raise ValueError

    def edit_order(self, terminal):
        choice = input("Do you want to add/delete last/delete by number any product? a/l/n\nType e to end editting your order\n")

        if choice == 'a':
            self.get_order(terminal)
        elif choice == 'l':
            self.delete_last_product()
            self.check_order(terminal)
        elif choice == 'n':
            self.delete_product(int(input("Type product number in your order\n")))
            self.check_order(terminal)
        elif choice == 'e':
            self.show_order()
            self.prepare_order()
        else:
            raise ValueError