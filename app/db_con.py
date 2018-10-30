import psycopg2
import os

url = "dbname='store_manager_api_v2' host='localhost' port='5432' user='postgres' password='qwerty'"


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(url)
    return con


def create_tables():
	queries = tables()
	conn = connection(url)
	cur = conn.cursor()

	for query in queries:
		cur.execute(query)
	conn.commit()


def destroy_tables():
    cur.execute("DROP TABLE IF EXISTS products CASCADE")
    cur.execute("DROP TABLE IF EXISTS sales CASCADE")
    cur.execute("DROP TABLE IF EXISTS users CASCADE")
    conn.commit()
    
    



def tables():
    products = """CREATE TABLE IF NOT EXISTS products (
	    product_id serial PRIMARY KEY NOT NULL,
	    product_name character varying(1000) NOT NULL,
	    category character varying(1000) NOT NULL,
	    description character varying(1000) NOT NULL,
	    inventory int  NOT NULL,
	    price int  NOT NULL
	    
	    
	    )"""

    sales = """CREATE TABLE IF NOT EXISTS sales (
	    sales_id serial PRIMARY KEY NOT NULL,
	    names character varying(200) NOT NULL,
	    cart int NOT NULL,
	    total_price int NOT NULL
	    
	    )"""

    users = """CREATE TABLE IF NOT EXISTS users (
	    employee_id serial PRIMARY KEY NOT NULL,
	    email character varying(50) NOT NULL,
	    password character varying(500) NOT NULL,
	    re_password character varying(500) NOT NULL
	    )"""

    queries = [products,sales,users]
    return queries
