#!/usr/bin/env python3

# 📚 Review With Students:
    # Request-Response Cycle
    # Web Servers and WSGI/Werkzeug

# 1. ✅ Navigate to `models.py`

# 2. ✅ Set Up Imports
	# `Flask` from `flask`
	# `Migrate` from `flask_migrate`
	# db and `Production` from `models`

#Flask-SQLAlchemy...SQLAlchemy
#Flask-Migrate...alembic
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate 
from models import db, Production, Role
# 3. ✅ Initialize the App
    # Add `app = Flask(__name__)`


# models.py -> flask migrate -> app.db -> connected to app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

migrate = Migrate(app, db)

db.init_app(app)
    
@app.route('/')
def index():
    return 'this is flask'

@app.route('/productions')
def all_productions():
    q = Production.query.all()
    q_dict = []
    for prod in q:
        q_dict.append({
            "id": prod.id,
            "title": prod.title,
            "year": prod.year,
            "genre": prod.genre
        })
    return make_response(jsonify(q_dict), 200)

@app.route('/productions/<int:id>')
def one_production(id):
    q = Production.query.filter(Production.id==id).first()
    q_dict = {
        "id": q.id,
        "genre": q.genre,
        "title": q.title,
        "year": q.year
    }
    return make_response(q_dict, 200)
   
@app.route('/alphabetical-productions')
def ordered_prods():
    q = Production.query.order_by('title').limit(3)
    q_dict = [{
        "id": prod.id,
        "title": prod.title
    } for prod in q]

    return make_response(q_dict, 200)

@app.route('/roles')
def all_roles():
    q = Role.query.all()
    q_dict = [
        {"id": r.id, "name": r.name, "movie_id": r.movie_id}
        for r in q
    ]
    return make_response(q_dict, 200)

@app.route('/context')
def context():
    print("context request")
    return f'Path: {request.path} Host: {request.host}'

# 16.✅ View the path and host with request context

#helpful for when checking what users are logged in or what current data is before completing request
@app.before_request
def runs_before():
    print("before request sent")
# 17.✅ Use the before_request after_request hook, what this hook does is up to you. You could hit a breakpoint, print something to server console or anything else you can think of.

@app.after_request
def runs_after(response):
    print("after submitting request")
    #makes sure to return the response
    return response
# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

if __name__ == '__main__':
    app.run(port=5000, debug=True)
