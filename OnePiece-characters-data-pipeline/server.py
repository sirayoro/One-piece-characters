from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Фласк веб-сервер представляет собой продюсера 
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Маршрут обработки запроса отправки персонажа в Kafka.
@app.route('/send', methods=['POST'])
def send():
    try:
        data = request.json
        key = data['key']
        value = data['value']
        producer.send('one-piece-topic', key=key.encode('utf-8'), value=value)
        producer.flush()
        return jsonify({"Сообщение": "Сообщение загружено в Kafka"}), 200
    except Exception as e:
        return jsonify({"Ошибка": str(e)}), 400

# Запуск flask-сервера на порту 3000
if __name__ == '__main__':
    app.run(port=3000)
