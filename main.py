from tkinter import * 
from Terminal import Terminal

t = Terminal()

"""
try:
    t.get_player_input()
except ValueError:
    print("Invalid input")
except:
    print("Unknown error")
"""

form = Tk()
form.title("Welcom to our Pizza Cafe!")
form.geometry("600x450")

t.show_menu_on_form(form)

form.mainloop()