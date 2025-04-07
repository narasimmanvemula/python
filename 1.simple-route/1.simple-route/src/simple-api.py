from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def welcome_page():
	return {"message": "Welcome !"}


@app.route('/api/v1')
def version_page():
	return {"message": "Welcome to Version!"}

@app.route('/api/v1/version')
def api_employee_json():
    return {"version": "1.0.0"}
