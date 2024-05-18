from flask import Flask, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

# Коннект к бд
def get_db_connection():
    conn = sqlite3.connect('one_piece.db')
    conn.row_factory = sqlite3.Row
    return conn

"""
Запрос на получение всех персонажей из бд
 http://localhost:5000/analytics/total_characters
"""
@app.route('/analytics/total_characters', methods=['GET'])
def total_characters():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) as total FROM characters')
    total = cur.fetchone()['total']
    conn.close()
    return jsonify({'total_characters': total})

"""
 Запрос на получение топ 5 персонажей по награде
 http://localhost:5000/analytics/top_bounties
"""
@app.route('/analytics/top_bounties', methods=['GET'])
def top_bounties():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, bounty FROM characters ORDER BY bounty DESC LIMIT 5')
    characters = cur.fetchall()
    conn.close()
    top_bounties = [{'name': row['name'], 'bounty': row['bounty']} for row in characters]
    return jsonify({'top_bounties': top_bounties})

""""
 Запрос на получение среднего возраста персонажей
 http://localhost:5000/analytics/average_age
"""
@app.route('/analytics/average_age', methods=['GET'])
def average_age():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT AVG(age) as avg_age FROM characters WHERE age IS NOT NULL')
    avg_age = cur.fetchone()['avg_age']
    conn.close()
    return jsonify({'average_age': avg_age})

"""
# Запрос на вывод персонажей, съевших дьявольский фрукт
# http://localhost:5000/analytics/devil_fruit_users
"""
@app.route('/analytics/devil_fruit_users', methods=['GET'])
def devil_fruit_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) as total FROM characters WHERE devil_fruit IS NOT NULL AND devil_fruit != ""')
    total = cur.fetchone()['total']
    conn.close()
    return jsonify({'devil_fruit_users': total})

# Запуска flask-сервера на порту 5000 для вывода аналитик из бд
if __name__ == '__main__':
    app.run(port=5000)
