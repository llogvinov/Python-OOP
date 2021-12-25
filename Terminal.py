import json
from tkinter import *
from Order import Order
from DB import *


# SINGLETON PATTERN
class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]


class Terminal(metaclass=SingletonBaseClass):
    def __init__(self):
        self.read_from_db()
        
        # with open('Menu.json', 'r') as menu_json:
        #     json_data = json.load(menu_json)
        
        # self.pizzas_list = json_data["pizzas"]
        # self.drinks_list = json_data["drinks"]


    def read_from_db(self):
        connection = create_connection(PATH)
        pizzas = execute_read_query(connection, select_pizzas)
        drinks = execute_read_query(connection, select_drinks)

        self.pizzas_list = []
        for pizza in pizzas:
            self.pizzas_list.append({
                "id" : pizza[0],
                "name": pizza[1],
                "price": pizza[2],
                "sauces": pizza[3],
                "filling": pizza[4]
            })

        self.drinks_list = []
        for drink in drinks:
            self.drinks_list.append({
                "id" : drink[0],
                "name": drink[1],
                "price": drink[2]
            })


    def __str__(self) -> str:
        return "To see the menu invoke show_menu()"


    # method to print menu 
    def show_menu_on_form(self):
        menu_form = Tk()
        menu_form.title("Welcom to our Pizza Cafe!")
        menu_form.geometry("600x450")

        l_title = Label(menu_form, text="MENU", font=("Verdana", 30), padx=10, pady=10)
        l_title.grid(column=1,row=0)

        for count, pizza in enumerate(self.pizzas_list):
            s = ""
            s += pizza["name"] + "\n"
            s += str(pizza["price"]) + "\n"
            s += pizza["sauces"] + "\n"
            s += pizza["filling"] + "\n"
            l_pizza = Label(menu_form, text=s, font=("Verdana", 15), padx=10, pady=10)
            l_pizza.grid(column=count,row=2)

        for count, drink in enumerate(self.drinks_list):
            s = ""
            s += drink["name"] + "\n"
            s += str(drink["price"]) + "\n"
            l_drink = Label(menu_form, text=s, font=("Verdana", 15), padx=10, pady=10)
            l_drink.grid(column=count,row=3)

        b_new_order = Button(menu_form, text="Make a new order", font=("Verdana", 12), bg="black", fg="white")
        b_new_order.bind('<Button-1>', self.make_new_order)
        b_new_order.grid(column=1, row=5)

        menu_form.mainloop()


    def make_new_order(self, event):
        o1 = Order()
        o1.get_new_order(self)
        # o1.get_order(self)