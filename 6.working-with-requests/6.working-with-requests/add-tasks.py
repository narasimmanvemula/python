from flask import Flask, flash, redirect, request, logging, make_response, jsonify
from flask_mysqldb import MySQL
from markupsafe import escape
import logging
from logging.handlers import RotatingFileHandler


app = Flask (__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# TODO Update secret key
# app.secret_key = '?'

# init MYSQL
mysql = MySQL(app)

@app.route('/api/v1')
def index():
    return {"version": "1.0.0"}

@app.route('/api/v1/echo', methods=['POST'])
def echo():
   return jsonify(request.json)

# List all tasks
@app.route('/api/v1/tasks')
def read_tasks():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT name, description FROM todo.tasks''')
    app.logger.info("Getting records from mysql")
    record_set = cursor.fetchall()
    return str(record_set)

# Add task
@app.route('/api/v1/tasks', methods=['POST'])
def create_tasks():
    if request.method == 'POST':
        contentJSON = request.get_json();
        name = contentJSON['name']
        description = contentJSON['description']
        # For querystrings, request.args('sortOder')

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO tasks(name, description) VALUES(%s, %s)", (escape(name), escape(description)))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        return make_response({"details": {"errors": "none", "message": "Successfully created the task"} }, 200)


if __name__ == "__main__":
    # initialize the log handler
    logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
    
    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)    
    
    app.run(debug=True)


