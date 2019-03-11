import logging, json
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *
from ..user import User

bp_driver = Blueprint('driver', __name__)
api = Api(bp_driver)

class DriverResource(Resource):
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

        qry = Driver.query

        driver_list = []
        if id == None:
            for driver in qry.limit(args['rp']).offset(offset).all():
                driver_list.append(marshal(driver, Driver.response_field))
        else:
            driver = Driver.query.filter_by(id=id).first()
            driver_list.append(marshal(driver, Driver.response_field))

        return driver_list, 200, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('buyer_id', location='json', required=True)
        parse.add_argument('seller_id', location='json', required=True)
        parse.add_argument('product_type', location='json', required=True)
        parse.add_argument('location', location='json', required=True)
        parse.add_argument('destination', location='json', required=True)
        parse.add_argument('amount', location='json', required=True)
        parse.add_argument('price', location='json', required=True)
        parse.add_argument('recomended_vehicle', location='json', required=True)
        parse.add_argument('description', location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        driver = Driver(None, args['buyer_id'], args['seller_id'], args['product_type'], args['location'], args['destination'], args['amount'], args['price'], args['recomended_vehicle'], args['description'], datetime.datetime.now(), (datetime.datetime.now() + datetime.timedelta(days=2)), args['status'], None)

        db.session.add(driver)
        db.session.commit()

        return marshal(driver, Driver.response_field), 200, {'Content-Type': 'application/json'}


    @jwt_required
    def put(self):
        parse = reqparse.RequestParser()
        parse.add_argument('id', type=int, location='json', required=True)
        parse.add_argument('status', location='json', required=True)
        parse.add_argument('asigned_driver_id', location='json', required=True)
        args = parse.parse_args()

        user = get_jwt_identity()
        identity = marshal(user, User.response_field)

        driver = Driver.query.filter_by(id=args['id']).first()

        driver.status = args['status']
        driver.asigned_driver_id = args['asigned_driver_id']
        db.session.commit()

        return marshal(driver, Driver.response_field)

    @jwt_required
    def delete(self, id):
        pass

class AdminDriver(Resource):
    @jwt_required    
    def delete(self, id):
        qry = Driver.query.filter_by(id=id).first()

        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return "Data Deleted", 200, { 'Content-Type': 'application/json' }
        else :
            return "Data Not Found", 404, { 'Content-Type': 'application/json' }


api.add_resource(DriverResource,'/public/couriers', '/public/couriers/<int:id>')
api.add_resource(AdminDriver, '/admin/couriers/<int:id>')