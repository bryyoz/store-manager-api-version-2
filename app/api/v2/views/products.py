"""Product endpoints get and post methods"""
import jwt

from flask_restplus import Namespace, Resource, reqparse, fields
from flask import make_response, jsonify
from ..models.Products import Product
# from ..views.login import jwt_required


ns_product = Namespace('Products')

product_models = ns_product.model("Store products",{
  "product_id":fields.Integer,
  "product_name":fields.String,
  "category":fields.String,
  "description":fields.String,
  "inventory":fields.Integer,
  "price":fields.Integer
  })

update_product_models = ns_product.model("Store products",{
  "product_id":fields.Integer,
  "product_name":fields.String,
  "category":fields.String,
  "description":fields.String,
  "inventory":fields.Integer,
  "price":fields.Integer
  })



product = Product()
@ns_product.route('')
class ProductEndpoint(Resource):
	"""Contains all the endpoints for Product Model"""

	@ns_product.expect(product_models)
	def post(self):
		"""Contains POST method"""
		parser = reqparse.RequestParser()
		parser.add_argument('product_name', required=True, help='Please input the product name', location=['json'] )
		parser.add_argument('category', required=True, help='Please input category', location=['json'] )
		parser.add_argument('description', required=True, help='please input product description', location=['json'] )
		parser.add_argument('inventory', required=True, help='please input amount to be added to the inventory',location=['json'] )
		parser.add_argument('price', required=True, help='Please input product price', location=['json'])


		args = parser.parse_args()
		product_name = args['product_name']
		category = args['category'] 
		description = args['description']
		inventory  = args['inventory']
		price = args['price']

		result = product.add_product(product_name, category, description, inventory,price)
		return {'message':'Product created'}, 201

	def get(self):

		result = product.get_all_products()
		return {'message':'These are your Products',
				'Products':result}, 200
		if not result:
			return {'message':'There are no products'}


@ns_product.route('/<int:product_id>')
class GetOneProduct(Resource):

	def delete(self, product_id):
		result = product.delete_product(product_id)
		if not result:
			return {'message':'Product doesnt exist'}
		return {'message':'Product has been deleted'}

	@ns_product.expect(update_product_models)  
	def put(self, product_id):


		parser = reqparse.RequestParser()
		parser.add_argument('product_name', required=True, help='Please input the product name', location=['json'] )
		parser.add_argument('category', required=True, help='Please input category', location=['json'] )
		parser.add_argument('description', required=True, help='please input product description', location=['json'] )
		parser.add_argument('inventory', required=True, help='please input amount to be added to the inventory',location=['json'] )
		parser.add_argument('price', required=True, help='Please input product price', location=['json'])


		args = parser.parse_args()
		product_name = args['product_name']
		category = args['category'] 
		description = args['description']
		inventory  = args['inventory']
		price = args['price']


		result = product.edit_product_record(product_id)
		return result, 201

	def get(self, product_id):
		one_product = product.get_one_product(product_id)
		if not one_product:
			return {'message':'Product doesnt exist'}
		return {'message': 'This is your product',
                'product': one_product}, 200









