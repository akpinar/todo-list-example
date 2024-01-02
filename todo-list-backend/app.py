import os
from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

@app.route('/task', methods=['POST'])
def create():
    task_data = request.json

    task_id = len(tasks) + 1  # Use UUID
    tasks[task_id] = task_data

    return jsonify({'task_id': task_id, 'message': 'Task added successfully'})

@app.route('/get/<int:task_id>', methods=['GET'])
def get(task_id):
    if task_id in tasks:
        return jsonify({'task_id': task_id, 'task_data': tasks[task_id]})
    else:
        return jsonify({'message': 'Task not found'}), 404


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    # TODO: Add delete
    pass


@app.route('/task/<int:task_id>', methods=['PUT'])
def update(task_id):
    # TODO: Add put
    pass


if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.run(host=host,port=port)
