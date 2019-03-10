import logging, json
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *
from ..user import User
from ..offer import Offer

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)

class TransactionResource(Resource):
    def __init__(self):
        pass
        # if User.query.first() is None:
        #     user = User(None, "trastanechora", "roadtoalterra", None, "maestro@alphatech.id", None, None, None, None, datetime.datetime.now(), None, None)
        #     db.session.add(user)
        #     db.session.commit()

    def get(self, id=None):
        parse = reqparse.RequestParser()
        parse.add_argument('p',type=int,location='args',default=1)
        parse.add_argument('rp',type=int,location='args',default=5)
        parse.add_argument('client_id',location='args')
        parse.add_argument('status',location='args')
        parse.add_argument('id', type=int, location="args")
                
        args = parse.parse_args()

        offset = args['p']*args['rp']-args['rp']

        qry = Transaction.query

        transaction_list = []
        if id == None:
            for transaction in qry.limit(args['rp']).offset(offset).all():
                transaction_list.append(marshal(transaction, Transaction.response_field))
        else:
            transaction = Transaction.query.filter_by(id=id).first()
            transaction_list.append(marshal(transaction, Transaction.response_field))

        return transaction_list, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('name', location='json', required=True)
        parse.add_argument('user_id', location='json', required=True)
        parse.add_argument('product_id', location='json', required=True)
        parse.add_argument('method', location='json', required=True)
        parse.add_argument('amount', location='json', required=True)
        parse.add_argument('bank', location='json', required=True)
        parse.add_argument('created_at', location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        parse.add_argument('delivery_provided', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        product = Product(None, args['name'], args['product_type'], args['category'], args['description'], args['amount'], args['price'], datetime.datetime.now(), identity['id'], args['location'], "OPEN", None, args['delivery_provided'])

        db.session.add(product)
        db.session.commit()

        return marshal(product, Product.response_field), 200, {'Content-Type': 'application/json'}


    @jwt_required
    def put(self, id):
        parse = reqparse.RequestParser()
        parse.add_argument('transaction_id', type=int, location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        transaction = Transaction.query.filter_by(id=args['transaction_id']).all()
        # transaction = marshal(transaction, Transaction.response_field)
        # dump = json.dumps(ofr)

        # out = Product.query.filter_by(id=args['product_id']).first()

        # out.offer = dump
        transaction.status = args['status']
        db.session.commit()


        # temp = json.loads(out.offer)
        # return temp
        # return marshal(out, Product.response_field)

        # temp2 = marshal(out, Product.response_field)
        # temp2['offer'] = temp

        return marshal(transaction, Transaction.response_field)

api.add_resource(TransactionResource,'/users/transactions', '/users/transactions/<int:id>')