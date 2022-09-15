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



# class USE FOR PROFILE(db.Model):
#     goal = db.Column(db.String(50), nullable=False, unique=True)
#     gender = db.Column(db.String(50), nullable=False, unique=True)
#     age = db.Column(db.Integer, nullable=False, unique=True)
#     activity = db.Column(db.String(50), nullable=False, unique=True)
#     bmi = db.Column(db.Integer, nullable=False, unique=True)

#     def __init__(self,)


#     self.goal = goal
#         self.gender = gender
#         self.age = age
#         self.activity = activity
#         self.bmi = bmi
#         self.apitoken = token_hex(16)
