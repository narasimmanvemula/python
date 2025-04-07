from flask import Flask, flash, redirect, url_for, request, logging
from flask_mysqldb import MySQL
from markupsafe import escape

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

# List all tasks
@app.route('/api/v1/tasks', methods=['GET'])
def read_tasks():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT name, description FROM todo.tasks''')
    record_set = cursor.fetchall()
    return str(record_set)

# Add task
@app.route('/api/v1/tasks', methods=['POST'])
def create_tasks():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        # For querystrings, request.args.get('sortOder')

        # Create Cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO tasks(name, description) VALUES(%s, %s)", (escape(name), escape(description)))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)