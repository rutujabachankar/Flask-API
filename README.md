API with Flask —it’s lightweight, Pythonic, and lets you get a server up and running in minutes.

Here is your step-by-step guide to building a functional REST API.

Step 1: Set Up Your Environment
It is best practice to use a virtual environment to keep your dependencies organized and avoid version conflicts.

Create a project folder:

Bash
mkdir flask-api-project
cd flask-api-project
Create and activate a virtual environment:

Windows: python -m venv venv then venv\Scripts\activate

Mac/Linux: python3 -m venv venv then source venv/bin/activate

Step 2: Install Dependencies
For a basic API, you only need Flask. If you plan on handling complex data, flask-cors is also helpful for allowing requests from different origins.

Bash
pip install flask
Step 3: Create the API Code
Create a file named app.py and paste the following code. I've included a "Hello World" route and a dynamic route to show how to handle data.

Python
from flask import Flask, jsonify, request

app = Flask(_name_)

# Mock data - normally this would come from a database
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build an API", "done": False}
]

# 1. GET Route: Fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# 2. GET Route: Fetch a single task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((item for item in tasks if item["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# 3. POST Route: Add a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get('title', 'Untitled'),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if _name_ == '_main_':
    app.run(debug=True)
Step 4: Run and Test Your API
Start the server:

Bash
python app.py
You should see a message saying Running on http://127.0.0.1:5000.

Test it:

In your browser: Go to http://127.0.0.1:5000/tasks to see the JSON list.

Using Terminal (cURL):

Bash
curl http://127.0.0.1:5000/tasks
How the API works:
Component	Purpose
@app.route	The URL path where the API "listens" for requests.
methods	Defines if the route accepts GET (reading) or POST (writing).
jsonify	Converts Python dictionaries into JSON format for the browser/client.
debug=True	Automatically restarts the server when you save code changes.
