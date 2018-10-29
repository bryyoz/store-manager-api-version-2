import unittest
from flask import json
from app import create_app

from .base_tests import BaseTest


class TestAuthentication(BaseTest):
	def test_login(self):
		response = self.client.post('/api/v2/login',
			data=self.attendant_login,
			content_type='application/json')
		self.assertEqual(response['message'], 'Logged in successfully!')
		self.assertEqual(response.status_code, 200)

	def test_login_invalid_email(self):
		payload = json.dumps({"email":"@gmail.com", "password":"12345"})
		response = self.client.post('/api/v2/login',
			data=payload,
			content_type='application/json')
		self.assertEqual(response['message'], '')
		self.assertEqual(response.status_code, 400)

	def test_login_wrong_email(self):
		payload = json.dumps({"email":"q@gmail.com", "password":"12345"})
		response = self.client.post('/api/v2/login',
			data=payload,
			content_type='application/json')
		self.assertEqual(response['message'], '')
		self.assertEqual(response.status_code, 400)

	def test_login_invalid_password(self):
		payload = json.dumps({"email":"admin@gmail.com", "password":"12345"})
		response = self.client.post('/api/v2/login',
			data=payload,
			content_type='application/json')
		self.assertEqual(response['message'], '')
		self.assertEqual(response.status_code, 400)

	def test_sign_up(self):
		payload = json.dumps({"email":"attendant@gmail.com", "password":"1234", "re_password":"1234"})
		response = self.client.post('/api/v2/register',
			data=payload,
			content_type='application/json')
		self.assertEqual(response['message'], '')
		self.assertEqual(response.status_code, 201)

	def test_sign_up_different_passwords(self):
		payload = json.dumps({"email":"attendant@gmail.com", "password":"1234", "re_password":"12345"})
		response = self.client.post('/api/v2/register',
			data=payload,
			content_type='application/json')
		self.assertEqual(response['message'], '')
		self.assertEqual(response.status_code, 400)




