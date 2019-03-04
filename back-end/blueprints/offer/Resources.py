import logging, json
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *
from ..user import User

bp_offer = Blueprint('offer', __name__)
api = Api(bp_offer)

class OfferResource(Resource):
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
        
        args = parse.parse_args()

        offset = args['p']*args['rp']-args['rp']

        qry = Product.query

        product_list = []
        for product in qry.limit(args['rp']).offset(offset).all():
            product_list.append(marshal(product, Product.response_field))
        return product_list, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('name', location='json', required=True)
        parse.add_argument('product_type', location='json', required=True)
        parse.add_argument('category', location='json', required=True)
        parse.add_argument('description', location='json')
        parse.add_argument('amount', location='json', required=True)
        parse.add_argument('price', location='json', required=True)
        parse.add_argument('location', location='json', required=True)
        parse.add_argument('delivery_provided', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        product = Product(None, args['name'], args['product_type'], args['category'], args['description'], args['amount'], args['price'], datetime.datetime.now(), identity['id'], args['location'], "OPEN", None, args['delivery_provided'])

        db.session.add(product)
        db.session.commit()

        return marshal(product, Product.response_field), 200, {'Content-Type': 'application/json'}

api.add_resource(OfferResource,'/users/offers')