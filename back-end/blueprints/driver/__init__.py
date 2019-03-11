import random, logging
from blueprints import db
from flask_restful import fields

class Driver(db.Model):
    __tablename__ = "driver"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buyer_id = db.Column(db.Integer)
    seller_id = db.Column(db.Integer)
    product_type = db.Column(db.String(20))
    location = db.Column(db.String(20))
    destination = db.Column(db.String(20))
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    recomended_vehicle = db.Column(db.String(50))
    description = db.Column(db.String(2000))
    created_at = db.Column(db.String(50))
    expired_at = db.Column(db.String(50))
    status = db.Column(db.String(50))
    asigned_driver_id = db.Column(db.String(50))

    response_field = {
        'id' : fields.Integer,
        'buyer_id' : fields.Integer,
        'seller_id' : fields.Integer,
        'product_type' : fields.String,
        'location' : fields.String,
        'destination' : fields.String,
        'amount': fields.Integer,
        'price': fields.Integer,
        'recomended_vehicle': fields.String,
        'description': fields.String,
        'created_at': fields.String,
        'expired_at': fields.String,
        'status': fields.String,
        'asigned_driver_id': fields.String
    }

    def __init__(self, id, buyer_id, seller_id, product_type, location, destination, amount, price, recomended_vehicle, description, created_at, expired_at, status, asigned_driver_id):
        self.id = id
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.product_type = product_type
        self.location = location
        self.destination = destination
        self.amount = amount
        self.price = price
        self.recomended_vehicle = recomended_vehicle
        self.description = description
        self.created_at = created_at
        self.expired_at = expired_at
        self.status = status
        self.asigned_driver_id = asigned_driver_id

    def __repr__(self):
        return '<Driver id %d>' % self.id
