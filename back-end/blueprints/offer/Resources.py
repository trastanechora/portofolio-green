import logging, json, jsonify
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *
from ..user import User
from ..product import Product

bp_offer = Blueprint('offer', __name__)
api = Api(bp_offer)

class OfferResource(Resource):
    def __init__(self):
        pass

    def get(self, id=None):
        parse = reqparse.RequestParser()
        parse.add_argument('p',type=int,location='args',default=1)
        parse.add_argument('rp',type=int,location='args',default=5)
        parse.add_argument('client_id',location='args')
        parse.add_argument('status',location='args')
        
        args = parse.parse_args()

        offset = args['p']*args['rp']-args['rp']

        qry = Offer.query

        offer_list = []
        for offer in qry.all():
            offer_list.append(marshal(offer, Offer.response_field))
        return offer_list, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        # ========= Get all required parameters as offer
        parse = reqparse.RequestParser()
        parse.add_argument('product_id', location='json', required=True)
        parse.add_argument('amount', location='json', required=True)
        parse.add_argument('price', location='json', required=True)
        parse.add_argument('description', location='json', required=True)
        parse.add_argument('destination', location='json', required=True)
        args = parse.parse_args()
        # =========

        # ========= Get the current logged in user
        user = get_jwt_identity()
        identity = marshal(user, User.response_field)
        # =========

        # ========= Put together the input parameters into JSON formated as offer
        offer = Offer(None, args['product_id'], identity['id'], args['amount'], args['price'], args['description'], args['destination'], datetime.datetime.now(), "WAITING")
        db.session.add(offer)
        db.session.commit()
        # =========

        # ========= Convert the offer JSON into plain string
        # temp = marshal(offer, Offer.response_field)
        # dumped_offer = json.dumps(temp)
        # =========

        # ========= Get the related offer list by product_id from database then convert into plain string
        offer = Offer.query.filter_by(product_id=args['product_id']).all()
        temp = marshal(offer, Offer.response_field)
        dumped_offer = json.dumps(temp)

        # ========= Get the offered product
        out = Product.query.filter_by(id=args['product_id']).first()
        # =========

        # ========= Update the offer field in product with the latters list of incoming offer
        out.offer = dumped_offer
        db.session.commit()
        # =========

        # ========= Return the current state of the product
        return marshal(out, Product.response_field)

        # Change back to json ===============================
        # temp = json.loads(out.offer)
        # temp2 = marshal(out, Product.response_field)
        # temp2['offer'] = temp
        # return temp2

    @jwt_required
    def put(self, id):
        parse = reqparse.RequestParser()
        parse.add_argument('status', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        offer = Offer.query.filter_by(id=id).first()
        offer.status = args['status']
        db.session.commit()
        return marshal(offer, Offer.response_field), 200, {'Content-Type': 'application/json'}
    
    @jwt_required
    def delete(self, id):
        pass

class AdminOffer(Resource):
    @jwt_required    
    def delete(self, id):
        qry = Offer.query.filter_by(id=id).first()

        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return "Data Deleted", 200, { 'Content-Type': 'application/json' }
        else :
            return "Data Not Found", 404, { 'Content-Type': 'application/json' }

api.add_resource(OfferResource, '/offers', '/offers/<int:id>')
api.add_resource(AdminOffer, '/admin/offers/<int:id>')