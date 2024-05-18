import sqlite3

# Подключение к БД. Если файла-бд нет, то он будет создан рядом
conn = sqlite3.connect('one_piece.db')
cur = conn.cursor()

# Создание таблицы с персонажами
cur.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        alias TEXT,
        age INTEGER,
        role TEXT,
        devil_fruit TEXT,
        crew TEXT,
        bounty INTEGER,
        biography TEXT
    )
''')

conn.commit()
cur.close()
conn.close()
