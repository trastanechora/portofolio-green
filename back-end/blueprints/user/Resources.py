import logging, json
import datetime
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprints import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import *

bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource):
    def __init__(self):
        if User.query.first() is None:
            user = User(None, "trastanechora", "roadtoalterra", None, "maestro@alphatech.id", None, None, None, None, datetime.datetime.now(), None, None)
            db.session.add(user)
            db.session.commit()

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username', location='json', required=True)
        parse.add_argument('password', location='json', required=True)
        parse.add_argument('email', location='json', required=True)
        args = parse.parse_args()

        user = User(None, args['username'], args['password'], None, args['email'], None, None, None, None, datetime.datetime.now(), None, None)

        db.session.add(user)
        db.session.commit()

        return marshal(user, User.response_field), 200, {'Content-Type': 'application/json'}

class AdminResource(Resource):
    def get(self, id=None):
        parse = reqparse.RequestParser()
        parse.add_argument('p',type=int,location='args',default=1)
        parse.add_argument('rp',type=int,location='args',default=5)
        parse.add_argument('client_id',location='args')
        parse.add_argument('status',location='args')
        
        args = parse.parse_args()

        offset = args['p']*args['rp']-args['rp']

        qry = User.query
        user_list = []

        if id is None:
            for user in qry.limit(args['rp']).offset(offset).all():
                user_list.append(marshal(user, User.response_field))
        else:
            user = User.query.filter_by(id=id).first()
            user_list.append(marshal(user, User.response_field))

        return user_list, 200, {'Content-Type': 'application/json'}

    @jwt_required    
    def delete(self, id):
        # return id
        qry = User.query.filter_by(id=id).first()
        # return marshal(qry, User.response_field)

        # user = get_jwt_identity()
        # identity = marshal(user, User.response_field)

        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return "Data Deleted", 200, { 'Content-Type': 'application/json' }
        else :
            return "Data Not Found", 404, { 'Content-Type': 'application/json' }
        

api.add_resource(UserResource,'/public/register')
api.add_resource(AdminResource, '/admin/users', '/admin/users/<int:id>')