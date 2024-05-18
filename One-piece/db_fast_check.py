import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('one_piece.db')
cur = conn.cursor()

# Выполнение запроса для выборки всех значений из таблицы characters
cur.execute('SELECT * FROM characters')

# Получение всех строк результата
rows = cur.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие подключения
cur.close()
conn.close()
