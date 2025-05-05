import sqlite3

"""
    Payment Database
        Table: Checkout
            Fields: 
                Name -> string
                CreditCard -> long
                Product -> string
"""

def create_table_checkout():
    try:
        with sqlite3.connect('payment.db') as conn:
            crsr = conn.cursor()
            crsr.execute("DROP TABLE IF EXISTS Checkout")
            crsr.execute("CREATE TABLE Checkout (Name TEXT, CreditCard LONG, Product TEXT)")
            conn.commit()
    except sqlite3.OperationalError as e:
        print(e)


if __name__ == "__main__":
    create_table_checkout()