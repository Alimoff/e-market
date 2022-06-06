import sqlite3


CREATE_MARKET_TABLE = """CREATE TABLE IF NOT EXISTS emarket (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, count INTEGER"""

INSERT_PRODUCT = "INSERT INTO emarket (name, price, count) VALUES (?,?,?)"

GET_ALL_PRODUCTS = "SELECT * FROM emarket"

GET_PRODUCT_BY_NAME = "SELECT * FROM emarket WHERE name = ?"

GET_PRODUCTS_IN_ALPHABETICAL_ORDER = "SELECT * FROM emarket ORDER BY name ASC"

UPDATE_BASE_SELL = "UPDATE emarket SET count = ? WHERE name = ?"

# UPDATE_BASE_INSERT_PRODUCT = "UPDATE emarket SET count = ? WHERE name = ?"


def connect():
    return sqlite3.connect("data.db")


def update_base_sell(connection, count, name):
    with connection:
        connection.execute(UPDATE_BASE_SELL, (count, name))


def create_table(connection):
    with connection:
        connection.execute(CREATE_MARKET_TABLE)


def add_product(connection, name, price, count):
    with connection:
        connection.execute(INSERT_PRODUCT, (name, price, count))


def all_products(connection):
    with connection:
        return connection.execute(GET_ALL_PRODUCTS).fetchall()


def get_by_name(connection, name):
    with connection:
        return connection.execute(GET_PRODUCT_BY_NAME, (name,)).fetchall()


def products_in_alphabert(connection):
    with connection:
        return connection.execute(GET_PRODUCTS_IN_ALPHABETICAL_ORDER).fetchall()


def sell_product(connection):
    with connection:
        return connection.execute(GET_ALL_PRODUCTS).fetchall()
