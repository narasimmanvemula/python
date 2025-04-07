from flask import Flask, flash, redirect, request, logging, make_response, jsonify
from flask_mysqldb import MySQL
from markupsafe import escape
import logging
from logging.handlers import RotatingFileHandler

from flask import session
from flask_session_extended import Session


app = Flask (__name__)
Session(app)

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

        if not request.cookies.get('x_app_name'):
            print("No cookie 'x_app_name' is found")
        else:
            print("Cookie 'x_app_name' is found : " + request.cookies.get('x_app_name'))

        print (session.get('x_cloud_provider', "No session key  'x_cloud_provider' exists."))
        
        response = make_response({"details": {"errors": "none", "message": "Successfully created the task"} }, 200)

        response.set_cookie("x_app_name", "TasksList", max_age=60*60*24*365)

        response.set_cookie("x_owner", "TBD")

        session['x_cloud_provider'] = 'aws'

        return response


@app.route('/api/v1/cookies', methods=['DELETE'])
def delete_cookie_appName():

    response = make_response({"message": "Cookie 'appName' is deleted."})

    response.delete_cookie("appName")

    response.delete_cookie("owner")
    
    return response





if __name__ == "__main__":
    # initialize the log handler
    logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)
    
    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)    
    
    app.run(debug=True)


