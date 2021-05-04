"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

def connect_db(app):
    db.app = app
    db.init_app(app) 

# Models 
class User(db.Model):
    """User"""
    __tablename__ = 'users' 

    # define columns 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)#default=DEFAULT_IMG_URL)


