import sqlite3
connection = sqlite3.connect("database.db")
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
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

initiate_db()

# # создание элементов
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f" Продукт {i}", f"Описание {i}", i*100))

def is_included(username):
    return cursor.execute("SELECT * FROM Users WHERE username = ?", (str(username),)).fetchone() is not None

def add_user(username, email, age):
    # print(is_included(username))
    if not is_included(username):
        cursor.execute(f'''
        INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
        ''', (str(username), str(email), age, 1000))
    else:
        print("Пользователь существует!")
    connection.commit()

# add_user("User 1", "user1@gmail.com", 20)
# add_user("User 1", "user34@gmail.com", 24)
# cursor.execute("DELETE FROM Users;")

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