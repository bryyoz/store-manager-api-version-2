import psycopg2
import datetime
import os
from app.db_con import init_db
from flask import Flask, jsonify, make_response

class Sales():
    """This class defines the Sales Model and
        the various methods of manipulating the Sales data"""

    def __init__(self):
        """Initialize the Sales Model with constructor"""

        self.db = init_db()

    def add_sale(self, names, cart, total_price):

        self.names = names
        self.cart = cart
        self.total_price = total_price

        payload = dict(
            names = names,
            cart = cart,
            total_price = total_price
            )
            

        sale = """INSERT INTO
               sales (names, cart, total_price)
               VALUES (%(names)s, %(cart)s, %(total_price)s)"""
               
        cur = self.db.cursor()
        cur.execute(sale, payload)
        self.db.commit()
        return payload

    def get_all_sales(self):

        cur = self.db.cursor()
        cur.execute("SELECT * FROM sales")
        sales = cur.fetchall()
        resp = []
        for i, saleRecord, in enumerate (sales):
            sale_id, names, cart, total_price = saleRecord
            data = dict(
                sale_id = int(sale_id),
                names = names,
                cart = int(cart),
                total_price = int(total_price))
            resp.append(data)

        return resp

    def get_one_sale_record(self, sales_id):

        cur = self.db.cursor()
        cur.execute("SELECT * FROM sales WHERE sales_id = (%s);",(sales_id,))
        one_sale = cur.fetchall()
        resp = []
        for i, oneRecord, in enumerate (one_sale):
            sale_id, names, cart, total_price = oneRecord
            data = dict(
                sales_id = int(sales_id),
                names = names,
                cart = int(cart),
                total_price = int(total_price))
            resp.append(data)

        return resp

    def edit_sale_record(self, names, cart, total_price):

        self.names = names
        self.cart = cart
        self.total_price = total_price

        payload = dict(
            names = names,
            cart = cart,
            total_price = total_price
            )
            
        update_sales = """UPDATE sales SET names=%(names)s, cart=%(cart)s, total_price=%(total_price)s WHERE sales_id = (sales_id)"""

        cur = self.db.cursor()
        cur.execute(update_sales,payload)
        self.db.commit()
        return payload


    def delete_sales(self, sales_id):
        cur = self.db.cursor()
        cur.execute("DELETE FROM sales WHERE sales_id = (%s);", (sales_id,))
        self.db.commit()
        return {'message','deleted'}

