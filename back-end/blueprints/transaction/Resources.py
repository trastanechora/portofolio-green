import logging, json
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *
from ..user import User

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)

class TransactionResource(Resource):
    def __init__(self):
        pass

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
        parse.add_argument('user_id', location='json', required=True)
        parse.add_argument('product_id', location='json', required=True)
        parse.add_argument('method', location='json', required=True)
        parse.add_argument('amount', location='json', required=True)
        parse.add_argument('bank', location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        transaction = Transaction(None, args['user_id'], args['product_id'], args['method'], args['amount'], args['bank'], datetime.datetime.now(), args['status'])

        db.session.add(transaction)
        db.session.commit()

        return marshal(transaction, Transaction.response_field), 200, {'Content-Type': 'application/json'}


    @jwt_required
    def put(self):
        parse = reqparse.RequestParser()
        parse.add_argument('transaction_id', type=int, location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        transaction = Transaction.query.filter_by(id=args['transaction_id']).first()

        transaction.status = args['status']
        db.session.commit()

        return marshal(transaction, Transaction.response_field)

class AdminTransaction(Resource):
    @jwt_required    
    def delete(self, id):
        qry = Transaction.query.filter_by(id=id).first()

        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return "Data Deleted", 200, { 'Content-Type': 'application/json' }
        else :
            return "Data Not Found", 404, { 'Content-Type': 'application/json' }

api.add_resource(TransactionResource,'/transactions', '/transactions/<int:id>')
api.add_resource(AdminTransaction, '/admin/transactions/<int:id>')