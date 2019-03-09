import random, logging
from blueprints import db
from flask_restful import fields

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    product_type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    posted_at = db.Column(db.String(50))
    posted_by = db.Column(db.Integer)
    location = db.Column(db.String(50))
    # photo = db.Column(db.File)
    status = db.Column(db.String(20))
    # offer = db.Column(db.ARRAY(db.String), server_default="[]")
    # offer = db.ARRAY(db.String), server_default='[]'
    offer = db.Column(db.String(2000))
    delivery_provided = db.Column(db.String(10))

    response_field = {
        'id' : fields.Integer,
        'name' : fields.String,
        'product_type' : fields.String,
        'category' : fields.String,
        'description' : fields.String,
        'amount': fields.Integer,
        'price': fields.Integer,
        'posted_at' : fields.String,
        'posted_by': fields.Integer,
        'location' : fields.String,
        'status' : fields.String,
        'offer' : fields.String,
        'delivery_provided' : fields.String
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
        # super(Product, self).__init__()

    def __repr__(self):
        return '<Product id %d>' % self.id
