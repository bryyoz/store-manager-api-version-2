import json
from .base_tests import BaseTest
class TestProduct(BaseTest):
	def test_admin_post_sale(self):
		response = self.client.post('/api/v2/sales',
			headers=self.admin_header, data=product_data, 
			content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], '')
		self.assertEqual(response.status_code, 200)

	def test_attendnt_post_sale(self):
		response = self.client.post('/api/v2/sales',
			headers=self.attendant_header, data=product_data)
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], '')
		self.assertEqual(response.status_code, 200)

	def test_get_all_sales(self):
		response = self.client.post('/api/v2/sales')
		res=json.loads(response.data.decode())
		self.assertEqual(res['message'],'')
		self.assertEqual(response.status_code,200)

	def test_get_one_sale(self):
		"""These tests check  specific sales record """
		response = self.client.get('/api/v2/sales/1', content_type="application/json")
		self.assertTrue(response.status_code, 200)

	def test_wrong_sales_id(self):
		"""Test check none existing sales_id """
		response = self.client.get('/api/v2/sales/a', content_type="application/json")
		self.assertEqual(response.status_code,404)

	def test_update_sale(self):
		response = self.client.put('/api/v2/sales/1',
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
		self.assertEqual(result['message'], 'product has been deleted!')
		self.assertEqual(response.status_code,200)
