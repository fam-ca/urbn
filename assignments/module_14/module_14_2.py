import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

# # создание элементов
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

# # обновление элементов
# for i in range(1, 11):
#     if i % 2 != 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))

# # удаление элементов
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{i}",))

# # считывать данные
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60, ))
#
# # cursor.execute("SELECT username, age FROM Users GROUP BY age")
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

# -----------------------------------------------------------------------------------------------

# # удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE username = ?", ("User6",))

cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
# print(f"Общее количество записей: {count}")

cursor.execute("SELECT SUM(balance) FROM Users")
sum_all = cursor.fetchone()[0]
# print(f"Сумма всех балансов: {sum_all}")

print(f"Средний баланс: {sum_all / count}")


connection.commit()
connection.close()

