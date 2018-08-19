import sqlite3

def create(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


name = input("Enter name of database: ")
create(name)
n = int(input("How many products you want to enter: "))
for i in range(0,n):
    item= input("Enter item: ")
    quantity = input("Enter quantity of item: ")
    price = input("Enter price of the item: ")
    insert(item,quantity,price)
