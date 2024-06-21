# 📚 Review With Students:
    # Review models
    # Review MVC
#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy

# 📚 Review With Students:
    # What SQLAlchemy() is replacing from SQLAlchemy in phase 3
     
db = SQLAlchemy()
# 1. ✅ Create a Production Model
	# tablename = 'Productions'
	# Columns:
        # title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 

class Production(db.Model):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    year = db.Column(db.Integer)

    # automatically handled by server
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Production id={self.id} title={self.title} genre={self.genre} year={self.year} />'
    
class Role(db.Model):
    __tablename__  = 'roles'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('productions.id'))

# 2. ✅ navigate to app.py
