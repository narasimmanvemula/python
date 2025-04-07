#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route('/api/v1/greet', methods=['GET'])
def greet():
	firstname   = request.args['firstname']
	lastname	= request.args['lastname']
	msg = f'Hello {lastname}'
	return msg;


@app.route('/')
def index():
    return 'Home'


"""
Careful on the order !

"""