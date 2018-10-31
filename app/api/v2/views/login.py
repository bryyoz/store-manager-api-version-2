import re
import jwt

from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Namespace, fields, reqparse, Resource, inputs
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_claims, get_jwt_identity,
get_current_user, get_raw_jwt)


from ..models.Users import User
from app.db_con import init_db,create_tables,connection

user = User()


ns_login = Namespace('Authentication')

login_model = ns_login.model('Login',{
		'email': fields.String,
        'password': fields.String

	})


@ns_login.route('')
class Login(Resource):


	
	@ns_login.expect(login_model)
	def post(self):
		"""Endpoint for user login"""
		parser = reqparse.RequestParser()

		parser.add_argument('email',required=True,help='please provide a valid email',
			type=inputs.regex(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"))
		parser.add_argument('password', required=True, help="password cannot be blank")



		info = parser.parse_args()
		email = info['email']
		password = info['password']

		user_login = user.login(email,password)
		if password == '' or password == None:
			return make_response(jsonify({'message': 'please enter your password',
                                              'status': 'failed'}), 401)
		if user_login:
			access_token = create_access_token(identity=email)
			return {'message' : 'Logged in succesful', 'access_token' : access_token }
		else:
			return {'message' : 'invalid password' }
