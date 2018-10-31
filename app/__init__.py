from flask import Flask,Blueprint
from instance.config import app_config
from app.api.v2 import app_v2
from .db_con import create_tables, destroy_tables
from flask_jwt_extended import (jwt_required, JWTManager, create_access_token, get_jwt_identity, get_raw_jwt)


def create_app(config_name):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	create_tables()

	app.config['JWT_SECRET_KEY'] = 'superpower'
	jwt = JWTManager(app)
	app.register_blueprint(app_v2)
	return app