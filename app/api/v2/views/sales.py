"""Sales_Records get and post methods"""
import jwt
from flask_restplus import Namespace, Resource, reqparse, fields
from flask import make_response, jsonify

from ..models.Sales import Sales
#from ..views.login import jwt_required


ns_sales = Namespace('Sales')

sales_models = ns_sales.model("Store sales",{
	"sale_id":fields.Integer,
	"names":fields.String,
	"cart":fields.Integer,
	"total_price":fields.Integer
	})

upate_sales_models = ns_sales.model("Store sales",{
	"sale_id":fields.Integer,
	"names":fields.String,
	"cart":fields.Integer,
	"total_price":fields.Integer
	})

sales = Sales()
@ns_sales.route('')
class SalesRecords(Resource):

	@ns_sales.expect(sales_models)
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('names', required=True, help='Please input the your name', location=['json'])
		parser.add_argument('cart', required=True, help='Please input add products to cart', location=['json'])
		parser.add_argument('total_price', required=True, help='Please input the total price', location=['json'])
	

		args = parser.parse_args()
		names = args['names']
		cart = args['cart']
		total_price  = args['total_price']

		result = sales.add_sale(names, cart, total_price)
		return {'message':'Sale record has been created'}, 201

	def get(self):
		response = sales.get_all_sales()
		return {'output':'These are your sales records',
		"Sales Records":response}, 200

@ns_sales.route('<int:sales_id>')
class GetOneSale(Resource):
	@ns_sales.expect(upate_sales_models)
	def put(self, sales_id):
		parser = reqparse.RequestParser()
		parser.add_argument('names', required=True, help='Please input the your name', location=['json'])
		parser.add_argument('cart', required=True, help='Please input add products to cart', location=['json'])
		parser.add_argument('total_price', required=True, help='Please input the total price', location=['json'])
	

		args = parser.parse_args()
		names = args['names']
		cart = args['cart']
		total_price  = args['total_price']

		result = sales.edit_sales_record(sales_id)
		return result, 201

	def delete(self, sales_id):
		result = sales.delete_sales(sales_id)
		if not result:
			return {'message':'Sale record doesnt exist'}
		return {'message':'Sale record has been deleted'}

	def get(self, sales_id):
		one_sale = sales.get_one_sale_record(sales_id)
		if not one_sale:
			return {'message':'Record doesnt exist'}
		return {'message': 'This is your sale',
                'product': one_sale}, 200




