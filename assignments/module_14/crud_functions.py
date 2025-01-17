import sqlite3
connection = sqlite3.connect("products.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL 
    );    
    ''')

initiate_db()

# # создание элементов
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f" Продукт {i}", f"Описание {i}", i*100))

def get_all_products():
    products_list = cursor.execute("SELECT * FROM Products")
    message = ""
    for product in products_list:
        message += f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} \n"
    connection.commit()
    return message
# lst = get_all_products()
# print(lst.split(sep='\n'))
connection.commit()
# connection.close()