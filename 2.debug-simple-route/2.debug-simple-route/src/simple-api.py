from flask import Flask
from flask_debug import Debug

app = Flask(__name__)
Debug(app)

@app.route('/api/v1')
def index_page():
	return {"message": "Welcome !"}

@app.route('/api/v1/version')
def api_software_version():
    return {"version": "1.0.0"}
