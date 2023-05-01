#!/usr/bin/python3
import os
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def end_session(f):
    """close the current session"""
    storage.close()

@app.errorhandler(404)
def handle_error(err):
    """function to handle 404 page not found error"""
    return make_response(jsonify(error='Not found'))

@app.errorhandler(400)
def handle_error(err):
    """handle 400 error json_page"""
    return make_response(jsonify(error=err.args))


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST'),
            port=os.getenv('HBNB_API_PORT'), threaded=True)