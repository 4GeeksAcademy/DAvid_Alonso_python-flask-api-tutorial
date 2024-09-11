from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False} ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# @app.route('/todos', methods=['GET'])
# def get_todos():
#     return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_todo = request.get_json()
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)
# test

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)