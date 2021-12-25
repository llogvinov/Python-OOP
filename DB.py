import sqlite3
from sqlite3 import Error


PATH = "C:\\Users\\Лев\\Desktop\\Python-OOP\\sm_app.sqlite"


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_menu_pizza_table = """
CREATE TABLE IF NOT EXISTS menu_pizza (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price INTEGER NOT NULL,
  sauces TEXT NOT NULL,
  filling TEXT NOT NULL
);
"""

create_menu_drink_table = """
CREATE TABLE IF NOT EXISTS menu_drink (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price INTEGER NOT NULL
);
"""

create_pizzas = """
INSERT INTO
  menu_pizza (id, name, price, sauces, filling)
VALUES
  (101, 'Pepperoni', 250, 'Ketchup', 'cheese, salami'),
  (102, 'Barbecue', 400, 'BBQ', 'beef, pork, cheese'),
  (103, 'Seafood', 450, 'Mayonnaise', 'fish, shrimps, algae');
"""

create_drinks = """
INSERT INTO
  menu_drink (id, name, price)
VALUES
  (201, 'Pepsi', 80),
  (202, 'Fanta', 80),
  (203, 'Sprite', 80);
"""

connection = create_connection(PATH)

execute_query(connection, create_menu_pizza_table)
execute_query(connection, create_menu_drink_table) 

# execute_query(connection, create_pizzas) 
# execute_query(connection, create_drinks) 

select_pizzas = "SELECT * from menu_pizza"
select_drinks = "SELECT * from menu_drink"

pizzas = execute_read_query(connection, select_pizzas)
drinks = execute_read_query(connection, select_drinks)

for pizza in pizzas:
    print(pizza)

for drink in drinks:
    print(drink)