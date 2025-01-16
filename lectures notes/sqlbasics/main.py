import sqlite3
from random import randint
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# # создание элементов
# for i in range(30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (f"newuser{i}", f"{i}example@gmail.com", str(randint(20, 60))))

# # обновление элементов
# cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29, "newuser"))

# # удаление элементов
# cursor.execute("DELETE FROM Users WHERE username = ?", ("newuser",))

# # считывать данные
# cursor.execute("SELECT * FROM Users")

# cursor.execute("SELECT username, age FROM Users WHERE age > ?", (29, ))

# cursor.execute("SELECT COUNT(*) FROM Users WHERE age > ?", (50, ))

# сумма возрастов всех пользователей
cursor.execute("SELECT SUM(age) FROM Users")
total1 = cursor.fetchone()[0]

# число пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total2 = cursor.fetchone()[0]
print(total1, f"Average age: {total1 / total2}")

cursor.execute("SELECT AVG(age) FROM Users")
avg_age = cursor.fetchone()[0]
print(avg_age)

cursor.execute("SELECT MIN(age) FROM Users")
min_age = cursor.fetchone()[0]
print(min_age)

cursor.execute("SELECT MAX(age) FROM Users")
max_age = cursor.fetchone()[0]
print(max_age)

connection.commit()
connection.close()

