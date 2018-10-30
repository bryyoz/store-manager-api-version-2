import psycopg2
import datetime
import os
import jwt
from app.db_con import init_db
from flask import Flask, jsonify, make_response
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_claims, get_jwt_identity,
get_current_user, get_raw_jwt)

class User:
    '''Class represents operations related to products'''  
    def __init__(self):  
        self.db = init_db()

    def add_attendant(self, email, password, re_password):
        """saves user information to db"""
        
        self.email = email
        self.password = password
        self.re_password = re_password
        
        payload = dict(
                email = email,
                password = password,
                re_password = re_password)
                
        
        
        user = """INSERT INTO
    		   users (email, password, re_password)
    		   VALUES 
    		   ( %(email)s, %(password)s, %(re_password)s)"""

        cur = self.db.cursor()
        cur.execute(user,payload)
        self.db.commit()
        return payload




    def login(self, email, password):
        """Login registered users"""
        cur = self.db.cursor()

        cur.execute("""SELECT email FROM users WHERE  email = '{}' AND password = '{}'""".format(email,password))
        
        data = cur.fetchone()
        return data





    def get_one_user(employee_id):
        cur.execute("SELECT * users WHERE employee_id=(%s);",(employee_id,))
        result = cur.fetchone()
        return result

    def get_all_users(self):
        cur.execute("SELECT * users;")
        users = cur.fetchall()
        return users
        



    def update_user(employee_id, email, role, password, re_password):
        """Update user information"""
        try:
            cur.execute ("UPDATE users SET email=(%s), role=(%s), password=(%s), re_password=(%s) WHERE employee_id=(%s)",
                        (email, role, password, re_password))
            conn.commit()
            return make_response(jsonify({'message':'user information has been updated'}))
        except:
            return make_response(jsonify({'message':'user does not exist'}))


    def delete_user(employee_id):
        """Deletes user information"""
        try:
            cur.execute("DELETE FROM users WHERE employee_id=(%s)",(employee_id,))
            conn.commit()
            return make_response(jsonify({'message':'The user has been deleted'}))
        except:
            return make_response(jsonify({'message':'user does not exist'}))
