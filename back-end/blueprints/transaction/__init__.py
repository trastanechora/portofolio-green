import random, logging
from blueprints import db
from flask_restful import fields

class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    method = db.Column(db.String(20))
    amount = db.Column(db.Integer)
    bank = db.Column(db.String(20))
    created_at = db.Column(db.String(50))
    status = db.Column(db.String(20))

    response_field = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'product_id' : fields.Integer,
        'method' : fields.String,
        'amount' : fields.Integer,
        'bank' : fields.String,
        'created_at': fields.String,
        'status': fields.String
    }

    def __init__(self, id, user_id, product_id, method, amount, bank, created_at, status):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.method = method
        self.amount = amount
        self.bank = bank
        self.created_at = created_at
        self.status = status

    def __repr__(self):
        return '<Transaction id %d>' % self.id
