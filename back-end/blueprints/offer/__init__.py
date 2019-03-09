import random, logging
from blueprints import db
from flask_restful import fields

class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    description = db.Column(db.String(2000))
    destination = db.Column(db.String(50))
    created_at = db.Column(db.String(50))
    status = db.Column(db.String(12))

    response_field = {
        'id' : fields.Integer,
        'product_id' : fields.Integer,
        'buyer_id' : fields.Integer,
        'amount' : fields.Integer,
        'price' : fields.Integer,
        'description' : fields.String,
        'destination': fields.String,
        'created_at' : fields.String,
        'status' : fields.String
    }

    def __init__(self, id, product_id, buyer_id, amount, price, description, destination, created_at, status):
        self.id = id
        self.product_id = product_id
        self.buyer_id = buyer_id
        self.amount = amount
        self.price = price
        self.description = description
        self.destination = destination
        self.created_at = created_at
        self.status = status

    def __repr__(self):
        return '<Offer id %d>' % self.id
