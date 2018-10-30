import json
from .base_tests import BaseTest
class TestProduct(BaseTest):
	def test_admin_post_product(self):
		response = self.client.post('/api/v2/products',
			headers=self.admin_header, data=product_data, 
			content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], '')
		self.assertEqual(response.status_code, 200)

	def test_attendant_post_product(self):
		response = self.client.post('/api/v2/products',
			headers=self.attendant_header, data=product_data)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], '')
		self.assertEqual(response.status_code, 200)

	def test_get_all_products(self):
		response = self.client.post('/api/v2/products')
		res=json.loads(response.data.decode())
		self.assertEqual(res['message'],'These are the products in your inventory')
		self.assertEqual(response.status_code,200)

	def test_get_one_product(self):
		"""These tests check  specific products record """
		response = self.client.get('/api/v2/products/1', content_type="application/json")
		self.assertTrue(response.status_code, 200)

	def test_wrong_products_id(self):
		"""Test check none existing products_id """
		response = self.client.get('/api/V1/products/a', content_type="application/json")
		self.assertEqual(response.status_code,404)

	def test_update_product(self):
		response = self.client.put('/api/v2/products/1',
			headers=self.admin_header, data=update_product,
			content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],'Product updated successfully!')
		self.assertEqual(response.status_code, 200)

	def test_delete_sale(self):
		response=self.client.delete('/api/v2/sales/1',
			headers=self.admin_header,
			content_type='application/json')
		result=json.loads(response.data.decode())
		print(result)
		self.assertEqual(result['message'], 'Product has been deleted!')
		self.assertEqual(response.status_code,200)