#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app 
from models import db, Production, Role

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`
with app.app_context():
    #delete everything productions
    Production.query.delete()
    #create new productions
    movie1 = Production(title="Wonder Woman", genre="Action", year=2017)
    movie2 = Production(title="Mulholland Drive", genre="Drama", year=2001)
    movie3 = Production(title="Erin Brockovich", genre="Biography", year=2000)
    movie4 = Production(title="Alien", genre="Sci-Fi", year=1979)
    movie5 = Production(title="The Hunger Games", genre="Adventure", year=2012)

    db.session.add_all([movie1, movie2, movie3, movie4, movie5])
    db.session.commit()

    roles = [Role(name='Michael Johnson', movie_id=3),
    Role(name='John Doe', movie_id=1),
    Role(name='Sarah Wilson', movie_id=5),
    Role(name='Chris Miller', movie_id=2),
    Role(name='Emily Davis', movie_id=4),
    Role(name='Kevin Clark', movie_id=3),
    Role(name='Rachel Taylor', movie_id=5),
    Role(name='David Brown', movie_id=1),
    Role(name='Amanda Lee', movie_id=3),
    Role(name='Jane Smith', movie_id=2)]

    db.session.add_all(roles)
    db.session.commit()

    #add new productions to table

# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# 8.✅ Create a query to delete all existing records from Production    
   
# 9.✅ Create some seeds for production and commit them to the database. 
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    