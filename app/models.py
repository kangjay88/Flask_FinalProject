from secrets import token_hex
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

# create our Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    apitoken = db.Column(db.String, default=None, nullable=True)



    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'token': self.apitoken
        }

class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False, unique=True)
    weight = db.Column(db.Integer, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False, unique=True)
    gender = db.Column(db.String(50), nullable=False, unique=True)
    calories = db.Column(db.Integer, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, height, weight, age, gender, calories, user_id):
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.calories = calories
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, height, weight, age, gender, calories, user_id):
        return {
        'height': self.height, 
        'weight': self.weight,
        'age': self.age,
        'gender': self.gender, 
        'calories':self.calories, 
        'user_id': self.user_id 
    }
