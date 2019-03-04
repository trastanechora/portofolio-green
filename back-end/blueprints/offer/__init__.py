import random, logging
from blueprints import db
from flask_restful import fields

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.String(2000))
    destination = db.Column(db.String(50))
    created_at = db.Column(db.String(20))
    status = db.Column(db.String(12))

    response_field = {
        'id' : fields.Integer,
        'product_id' : fields.Integer,
        'buyer_id' : fields.Integer,
        'amount' : fields.Integer,
        'price' : fields.Integer,
        'amount': fields.Integer,
        'price': fields.Integer,
        'description' : fields.String,
        'destination': fields.String,
        'created_at' : fields.String,
        'status' : fields.String
    }

    def __init__(self, id, name, product_type, category, description, amount, price, posted_at, posted_by, location, status, offer, delivery_provided):
        self.id = id
        self.name = name
        self.product_type = product_type
        self.category = category
        self.description = description
        self.amount = amount
        self.price = price
        self.posted_at = posted_at
        self.posted_by = posted_by
        self.location = location
        self.status = status
        self.offer = offer
        self.delivery_provided = delivery_provided

    def __repr__(self):
        return '<Product id %d>' % self.id
