from flask import Flask, Blueprint
from flask_restplus import Api

from .views.registration import ns_register
from .views.login import ns_login
from .views.products import ns_product
from .views.sales import ns_sales




app_v2 = Blueprint('V2',__name__)
api = Api(app_v2, title="Store Manager", version ="2",description="Store Manager v2")


api.add_namespace(ns_register,path='/api/v2/register')
api.add_namespace(ns_login, path='/api/v2/login')
api.add_namespace(ns_product, path='/api/v2/products')
api.add_namespace(ns_sales, path='/api/v2/sales')