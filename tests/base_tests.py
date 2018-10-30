import unittest 
import json
from app import create_app


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()

        with self.app_context:
            self.app_context.push()

        
        attendant_reg = json.dumps({
            "email":"attendant@gmail.com",
            "role":"attendant",
            "password":"1234",
            "re_password":"1234"
            })
        update_product = json.dumps({
            "product_id":1,
            "inventory":50})

        self.attendant_login = json.dumps({
            "email":"attendant@gmail.com",
            "password":"1234"
            })

        self.admin_login = json.dumps({
            "email":"admin@gmail.com",
            "password":"12345"
            })

        product_data = json.dumps({
             "product_id":1,
             "product_name":"television",
             "category":"electricals",
             "product_description":"oled",
             "inventory":50,
             "price":23450 
            })

        sales_data = json.dumps({
            "names":"josh kie",
            "cart":50,
            "total_price":2345
            })

        register_attendant = self.client.post('/api/v2/register', 
            data=attendant_reg, 
            content_type='application/json')

        attendant_result = self.client.post('/api/v2/login',
            data=self.attendant_login, 
            content_type='application/json' )

        admin_result = self.client.post('/api/v2/login',
            data=self.admin_login, 
            content_type='application/json' )

        admin_response = json.loads(admin_result.data.decode())
        admin_token = admin_response["token"]
        self.admin_header = {"Content-Type" : "application/json", "x-api-key" : admin_token}

        attendant_response = json.loads(attendant_result.data.decode())
        attendant_token = admin_response["token"]
        self.admin_header = {"Content-Type" : "application/json", "x-api-key" : attendant_token}

        post_product = self.client.post('/api/v2/register',
            data = product_data,
            content_type='application/json')

    def tearDown(self):
        """removes the db and the context"""
        with self.app_context:
            self.app_context.pop()


