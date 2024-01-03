import os
from flask import Flask, request, jsonify
from uuid import uuid4
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
tasks = {}

@app.route('/task', methods=['POST'])
def create():
    data = request.json

    id = str(uuid4())
    data["status"] = "1"
    tasks[id] = data

    return jsonify({'id': id, 'message': 'Task added successfully'}), 200

@app.route('/task/<string:id>', methods=['GET'])
def get(id):
    if id in tasks:
        return jsonify({'id': id, 'data': tasks[id]}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/task/<string:id>', methods=['DELETE'])
def delete(id):
    if id in tasks:
        del tasks[id]
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/task/<string:id>', methods=['PUT'])
def update(id):
    if id in tasks:
        tasks[id] = request.json

        return jsonify({'id': id, 'message': 'Task updated successfully'}), 200
    else:
        return jsonify({'message': 'Task not found'}), 404

@app.route('/task/search/<int:status>', methods=['GET'])
def search(status):
    filtered_items = {key: value for key, value in tasks.items() if value.get('status') == str(status)}
    return jsonify({'data': filtered_items}), 200



if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.run(host=host,port=port)
