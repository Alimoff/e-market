import database

MENU_PROMPT = """ _-_-_- E-Market App -_-_-_

Please choose an option:

1) Sell product.
2) Add a new product to base.
3) Show all products.
4) Find a product by name.
5) Show products in alphabetical order.
6) Exit.


Your select:"""


def menu():
    connection = database.connect()
    # database.create_table(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            prompt_sell_product(connection)
        elif user_input == "2":
            prompt_add_new_product(connection)
        elif user_input == "3":
            prompt_show_all(connection)
        elif user_input == "4":
            prompt_by_name(connection)
        elif user_input == "5":
            prompt_get_products_in_alphabet(connection)
        else:
            print("Invalid input! Please try again")


def prompt_add_new_product(connection):
    name = input("Enter name of product: ")
    price = int(input(f"Enter price of '{name}': "))
    count = int(input(f"Enter count of '{name}': "))

    database.add_product(connection, name.lower(), price, count)

    products = database.all_products(connection)

    # for product in products:
    #     if name == product[1] and price == product[2]:
    #         update_prod = int(product[3]) + count
    #         database.update_base_sell(connection, update_prod, name)


def prompt_show_all(connection):
    products = database.all_products(connection)

    for product in products:
        print(f"{product[1]} - {product[2]:,} | {product[3]} pc's'")
        print()


def prompt_by_name(connection):
    name = input("Enter product name to find: ")
    products = database.get_by_name(connection, name.lower())

    for product in products:
        print(f"{product[1]} - {product[2]:,}  {product[3]} pc's'")

        if name != product[1]:
            print(f"We don't have {name} in our market.")


def prompt_get_products_in_alphabet(connection):
    products = database.products_in_alphabert(connection)

    for product in products:
        print(f"{product[1]} - ({product[2]:,}) | {product[3]} pc's'")


def prompt_sell_product(connection):
    name = input("Enter name of product: ")
    count = int(input(f"Enter count of {name} you want to buy: "))
    products = database.sell_product(connection)

    for product in products:
        if name == product[1] and count <= product[3]:
            left = int(product[3]) - count
            database.update_base_sell(connection, left, name)


menu()
