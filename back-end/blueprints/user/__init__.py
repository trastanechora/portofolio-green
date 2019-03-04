import random, logging
from blueprints import db
from flask_restful import fields

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    display_fullname = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(15), unique=True)
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.String(50))
    # profile_picture = db.Column(db.String)
    address = db.Column(db.String(255))
    created_at = db.Column(db.String(50))
    updated_at = db.Column(db.String(50))
    status = db.Column(db.String(50))

    response_field = {
        'id' : fields.Integer,
        'username' : fields.String,
        'password' : fields.String,
        'display_fullname' : fields.String,
        'email' : fields.String,
        'phone' : fields.String,
        'gender' : fields.String,
        'date_of_birth' : fields.String,
        'address' : fields.String,
        'created_at' : fields.String,
        'updated_at' : fields.String,
        'status' : fields.String,
    }

    def __init__(self, id, username, password, display_fullname, email, phone, gender, date_of_birth, address, created_at, updated_at, status):
        self.id = id
        self.username = username
        self.password = password
        self.display_fullname = display_fullname
        self.email = email
        self.phone = phone
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.created_at = created_at
        self.updated_at = updated_at
        self.status = status

    def __repr__(self):
        return '<User id %d>' % self.id
