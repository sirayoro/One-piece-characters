import sqlite3

conn = sqlite3.connect('one_piece.db')
cur = conn.cursor()

cur.execute('SELECT * FROM characters')
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
