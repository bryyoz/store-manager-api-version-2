import re
# import jwt
from flask import Flask, jsonify, make_response, request
from flask_restplus import Api, Namespace, fields, reqparse, Resource, inputs

from ..models.Users import User
from app.db_con import init_db,create_tables,connection


ns_register = Namespace('Authentication')


user_model = ns_register.model('Registration',{
		'employee_id':fields.Integer(required=True),
		'email': fields.String(required=True),
		#'is_attendant':fields.Boolean(default=False),
        'password': fields.String(required=True),
        're_password': fields.String(required=True)
	})

user = User()

@ns_register.route('')
class UserRegistration(Resource):
	"""Endpoint for registreing a new user"""

	@ns_register.expect(user_model)
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('employee_id',required=True,help='please provide your employee_id',location=['json'])
		parser.add_argument('email',required=True,help='please provide a valid email',
			type=inputs.regex(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"))
		#parser.add_argument('is_attendant',required=False)
		parser.add_argument('password',required=True,help='password cannot be blank', location=['json'])
		parser.add_argument('re_password',required=True,help='password cannot be blank',location=['json'] )
		

		args = parser.parse_args()
		email = args['email']
		password = args['password']
		re_password = args['re_password']


		if  email == "" or password == "":
			return make_response(jsonify({'message':'fields cannot be empty'}))

		if password != re_password:
			return make_response(jsonify({'message':'passwords do not match',
										  'status':'failed'}), 401)
	
		attendant_result = user.add_attendant(email, password, re_password)
		return attendant_result, 201


