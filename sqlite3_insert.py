import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

people = [("cubinez85", 58), ("Ivan", 43), ("Kate", 24)]
cursor.executemany("INSERT INTO Users (name, age) VALUES (?, ?)", people)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
