import psycopg2
import datetime
import os
from app.db_con import init_db
from flask import Flask, jsonify, make_response

class Product():
	def __init__(self):
		self.db = init_db()
		


	def add_product(self, product_name, category, description,inventory, price):

		self.product_name = product_name
		self.category = category
		self.description = description
		self.inventory = inventory
		self.price = price
        


		payload =dict(
					product_name=product_name,
					category=category,
					description=description,
					inventory=inventory,
					price=price
					)
					
		

		product = """ INSERT INTO 
				  products (product_name, category, description, inventory, price)
				  VALUES (%(product_name)s, %(category)s, %(description)s, %(inventory)s, %(price)s)"""
		cur = self.db.cursor()
		cur.execute(product,payload)
		self.db.commit()
		return payload

	def get_all_products(self):

		cur = self.db.cursor()
		cur.execute("SELECT * FROM products")
		products = cur.fetchall()
		resp = []
		for i, productRecord, in enumerate (products):
			product_id, product_name, category, description, inventory, price = productRecord
			data = dict(
				product_id= int(product_id),
                product_name = product_name,
                category = category,
                description = description,
                inventory = int(inventory),
                price = int(price)
                )
			resp.append(data)
		return resp

	def get_one_product(self, product_id):

		cur = self.db.cursor()
		cur.execute("SELECT * FROM products WHERE  product_id = (%s);", (product_id,))
		one_product = cur.fetchall()
		resp = []
		for i, oneRecord, in enumerate (one_product):
			product_id, product_name, category, description, inventory, price = oneRecord
			data = dict(
				product_id= int(product_id),
                product_name = product_name,
                category = category,
                description = description,
                inventory = int(inventory),
                price = int(price)
                )
			resp.append(data)
		return resp
		

	def edit_product_record(self, product_name, category, description, inventory, price):

		self.product_name = product_name
		self.category = category
		self.description = description
		self.inventory = inventory
		self.price = price

		payload =dict(
					product_name=product_name,
					category=category,
					description=description,
					inventory=inventory,
					price=price
					)
		update_product = """UPDATE products SET product_name=%(product_name)s, category=%(category)s, description=%(description)s, inventory=%(inventory)s, price=%(price)s WHERE product_id = (product_id)"""

		cur = self.db.cursor()
		cur.execute(update_product,payload)
		self.db.commit()
		return payload


	def delete_product(self, product_id):
		cur = self.db.cursor()
		cur.execute("DELETE FROM products WHERE product_id = (%s);", (product_id,))
		self.db.commit()
		return {'message','deleted'}

