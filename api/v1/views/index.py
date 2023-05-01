#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def status_response():
    """return the status code"""
    return jsonify(status='ok')

@app_views.route('/stats')
def get_count():
    """get the count of all entities in the database server"""
    from models.state import State
    from models.amenity import Amenity
    from models.review import Review
    from models.city import City
    from models.user import User
    from models.place import Place
    
    return (jsonify({
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User)
    }))
