import json
import sqlite3
from kafka import KafkaConsumer

# Настройка подключения к базе данных SQLite
conn = sqlite3.connect('one_piece.db')
cur = conn.cursor()

# Настройка Kafka consumer
consumer = KafkaConsumer(
    'one-piece-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='one-piece-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    key = message.key.decode('utf-8')

    # Извлечение данных из сообщения
    name = data.get('name')
    alias = data.get('alias')
    age = data.get('age')
    role = data.get('role')
    devil_fruit = data.get('devil_fruit')
    crew = data.get('crew')
    bounty = data.get('bounty')
    biography = data.get('biography')

    # Вставка данных в базу данных SQLite
    cur.execute('''
        INSERT OR IGNORE INTO characters (key, name, alias, age, role, devil_fruit, crew, bounty, biography)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (key, name, alias, age, role, devil_fruit, crew, bounty, biography))
    conn.commit()

cur.close()
conn.close()
