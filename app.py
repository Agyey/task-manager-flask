from flask import Flask, jsonify, request
from models import Task, User

# Initialize Flask app
app = Flask(__name__)

# Initialize the database tables
Task.init_table()
User.init_table()  # Placeholder for future implementation

# Task Management APIs

# GET: Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.get_all()
    tasks_json = [{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status} for task in tasks]
    return jsonify(tasks_json), 200

# GET: Retrieve a task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.get_by_id(id)
    if task:
        task_json = {'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status}
        return jsonify(task_json), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

# POST: Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if 'title' not in data or 'status' not in data:
        return jsonify({'error': 'Title and status are required'}), 400

    task = Task(title=data['title'], description=data.get('description', ''), status=data['status'])
    task.save()
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status}), 201

# PUT: Update an existing task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.get_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.json
    task.title = data['title']
    task.description = data.get('description', '')
    task.status = data['status']
    task.update()
    return jsonify({'message': 'Task updated successfully'}), 200

# DELETE: Delete a task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.get_by_id(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    Task.delete(id)
    return jsonify({'message': 'Task deleted successfully'}), 200

# Placeholder for User Management APIs

# POST: Register a new user
@app.route('/users', methods=['POST'])
def register_user():
    # Placeholder: Implement user registration functionality
    return jsonify({'message': 'User registration functionality not implemented'}), 501

# GET: Retrieve a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # Placeholder: Implement user retrieval functionality
    return jsonify({'message': 'User retrieval functionality not implemented'}), 501

# PUT: Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    # Placeholder: Implement user update functionality
    return jsonify({'message': 'User update functionality not implemented'}), 501

# DELETE: Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Placeholder: Implement user deletion functionality
    return jsonify({'message': 'User deletion functionality not implemented'}), 501

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
