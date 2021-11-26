import json
from tkinter import *
from Order import Order

class Terminal:
    
    def __init__(self):
        with open('Menu.json', 'r') as menu_json:
            json_data = json.load(menu_json)
        
        self.pizzas_list = json_data["pizzas"]
        self.drinks_list = json_data["drinks"]

    def __str__(self) -> str:
        return "To see the menu invoke show_menu()"

    # method to print menu 
    def show_menu_on_form(self, form):
        l_title = Label(form, text="MENU", font=("Verdana", 30), padx=10, pady=10)
        l_title.grid(column=1,row=0)

        for count, pizza in enumerate(self.pizzas_list):
            s = ""
            s += pizza["name"] + "\n"
            s += str(pizza["price"]) + "\n"
            s += ", ".join(str(x) for x in pizza["sauces"]) + "\n"
            s += ", ".join(str(x) for x in pizza["filling"]) + "\n"
            l_pizza = Label(form, text=s, font=("Verdana", 15), padx=10, pady=10)
            l_pizza.grid(column=count,row=2)

        for count, drink in enumerate(self.drinks_list):
            s = ""
            s += drink["name"] + "\n"
            s += str(drink["price"]) + "\n"
            s += str(drink["size"]) + "\n"
            l_drink = Label(form, text=s, font=("Verdana", 15), padx=10, pady=10)
            l_drink.grid(column=count,row=3)

        b_new_order = Button(form, text="Make a new order", font=("Verdana", 12), bg="black", fg="white")
        b_new_order.bind('<Button-1>', self.make_new_order)
        b_new_order.grid(column=1, row=5)

    def make_new_order(self, event):
        o1 = Order()
        o1.get_order(self)