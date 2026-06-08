from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)

# Logging
logging.basicConfig(level=logging.INFO)

# Prometheus Metrics
metrics = PrometheusMetrics(app)

users = []

@app.route('/')
def home():
    return "DevOps App Running"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    app.logger.info(f"User added: {data}")
    return jsonify({"message": "User added"}), 201

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < len(users):
        users.pop(index)
        app.logger.info(f"User deleted at index: {index}")
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "Invalid index"}), 400

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DevOps Project 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
