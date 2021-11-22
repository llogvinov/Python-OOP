from Terminal import Terminal

t = Terminal()
t.show_menu()


try:
    t.get_player_input()
except ValueError:
    print("Invalid input")
except:
    print("Unknown error")