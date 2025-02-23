from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
from src.database import create_connection
import sqlite3

app = Flask(__name__)
swagger = Swagger(app)

# getting all tasks
@app.route("/", methods=["GET"])
@swag_from({
    'responses': {
        '200': {
            'description': 'List of all tasks',
            'examples': {
                'application/json': [
                    {'id': 1, 'title': 'Task 1', 'description': 'First task', 'completed': False},
                    {'id': 2, 'title': 'Task 2', 'description': 'Second task', 'completed': True}
                ]
            }
        }
    }
})
def index():
    conn, c = create_connection()
    c.execute('SELECT * FROM tasks')
    rows = c.fetchall()
    column_names = [description[0] for description in c.description]

    tasks = [{column_names[i]: row[i] for i in range(len(column_names))} for row in rows]
    conn.close()
    return jsonify(tasks)

# Adding new task
@app.route('/add', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'title',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'The title of the task'
        },
        {
            'name': 'description',
            'in': 'body',
            'type': 'string',
            'required': True,
            'description': 'The description of the task'
        },
        {
            'name': 'completed',
            'in': 'body',
            'type': 'boolean',
            'required': True,
            'description': 'Task completion status'
        }
    ],
    'responses': {
        '201': {
            'description': 'Task successfully created',
            'examples': {
                'application/json': {'created': 'true'}
            }
        },
        '400': {
            'description': 'Bad request (title missing)',
            'examples': {
                'application/json': {'error': 'title is required'}
            }
        }
    }
})
def add_task():
    data = request.get_json()
    print("data", data)
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')

    if not title:
        return jsonify({"error": "title is required"}), 400

    conn, c = create_connection() 
    c.execute('INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)', (title, description, completed))
    conn.commit()
    conn.close()
    return jsonify({"created": "true"}), 201

# Deleting all tasks
@app.route('/delete', methods=['DELETE'])
@swag_from({
    'responses': {
        '200': {
            'description': 'All tasks successfully deleted',
            'examples': {
                'application/json': {'message': 'deleted all tasks'}
            }
        }
    }
})
def delete_all():
    conn, c = create_connection() 
    c.execute('DELETE FROM tasks')
    conn.commit()
    conn.close()
    return jsonify({"message": "deleted all tasks"}), 200

# Deleting task with task_id
@app.route('/delete/<int:task_id>', methods=['DELETE'])
@swag_from({
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task to be deleted'
        }
    ],
    'responses': {
        '200': {
            'description': 'Task successfully deleted',
            'examples': {
                'application/json': {'deleted': 'true', 'task_id': 1}
            }
        },
        '404': {
            'description': 'Task not found',
            'examples': {
                'application/json': {'error': 'task not found'}
            }
        }
    }
})
def delete_task(task_id):
    conn, c = create_connection() 
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    if c.rowcount > 0:
        conn.commit()
        conn.close()
        return jsonify({"deleted": "true", "task_id": task_id}), 200
    else:
        conn.close()
        return jsonify({"error": "task not found"}), 404

# Updating task with task_id
@app.route('/update/<int:task_id>', methods=['PATCH'])
@swag_from({
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the task to update'
        },
        {
            'name': 'title',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'Updated title of the task'
        },
        {
            'name': 'description',
            'in': 'body',
            'type': 'string',
            'required': False,
            'description': 'Updated description of the task'
        },
        {
            'name': 'completed',
            'in': 'body',
            'type': 'boolean',
            'required': False,
            'description': 'Updated completion status of the task'
        }
    ],
    'responses': {
        '200': {
            'description': 'Task successfully updated',
            'examples': {
                'application/json': {'updated': 'true', 'task_id': 1}
            }
        },
        '400': {
            'description': 'Bad request (no fields to update)',
            'examples': {
                'application/json': {'error': 'No fields to update'}
            }
        },
        '404': {
            'description': 'Task not found',
            'examples': {
                'application/json': {'error': 'task not found'}
            }
        }
    }
})
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')

    if not any([title, description, completed is not None]):
        return jsonify({"error": "No fields to update"}), 400

    updates = []
    params = []

    if title is not None:
        updates.append("title = ?")
        params.append(title)
    if description is not None:
        updates.append("description = ?")
        params.append(description)
    if completed is not None:
        updates.append("completed = ?")
        params.append(completed)

    query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
    params.append(task_id)

    conn, c = create_connection() 
    c.execute(query, params)
    if c.rowcount > 0:
        conn.commit()
        conn.close()
        return jsonify({"updated": "true", "task_id": task_id}), 200
    else:
        conn.close()
        return jsonify({"error": "task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
