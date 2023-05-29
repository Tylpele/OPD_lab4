import unittest
from App import app
import requests


class TestApp(unittest.TestCase):

    def test_connect(self):
        URL = "http://127.0.0.1:5000"
        r = requests.get(URL)
        self.assertEqual(r.status_code, 200)

    def test_check_normal_int_answ_ball(self):
        tester = app.test_client(self)
        response = tester.post("/ball", content_type='multipart/form-data', data={'radius': 3, 'aim': 0})
        self.assertIn('113', response.data.decode())

    def test_check_negativ_radius_ball(self):
        tester = app.test_client(self)
        response = tester.post("/ball", content_type='multipart/form-data', data={'radius': -5, 'aim': 0})
        self.assertIn('524', response.data.decode())

    def test_check_round_ball(self):
        tester = app.test_client(self)
        response = tester.post("/ball", content_type='multipart/form-data', data={'radius': 3, 'aim': 3})
        self.assertIn('113.097', response.data.decode())




    def test_normal_int_answ_conus(self):
        tester = app.test_client(self)
        response = tester.post("/cone", content_type='multipart/form-data', data={'radius': 3, 'height': 3, 'aim': 0})
        self.assertIn('28', response.data.decode())

    def test_check_negativ_radius_conus(self):
        tester = app.test_client(self)
        response = tester.post("/cone", content_type='multipart/form-data', data={'radius': -5, 'height': 5, 'aim': 0})
        self.assertIn('131', response.data.decode())

    def test_check_round_conus(self):
        tester = app.test_client(self)
        response = tester.post("/cone", content_type='multipart/form-data', data={'radius': 1, 'height': 10, 'aim': 3})
        self.assertIn('10.472', response.data.decode())




    def test_normal_int_answ_cylinder(self):
        tester = app.test_client(self)
        response = tester.post("/cylinder", content_type='multipart/form-data', data={'radius': 3, 'height': 3, 'aim': 0})
        self.assertIn('85', response.data.decode())


    def test_negativ_var_cylinder(self):
        tester = app.test_client(self)
        response = tester.post("/cylinder", content_type='multipart/form-data', data={'radius': -3, 'height': 6, 'aim': 0})
        self.assertIn('170', response.data.decode())

    def test_check_round_cylinder(self):
        tester = app.test_client(self)
        response = tester.post("/cylinder", content_type='multipart/form-data', data={'radius': 7, 'height': 6, 'aim': 3})
        self.assertIn('923.628', response.data.decode())




    def test_normal_int_answ_prism(self):
        tester = app.test_client(self)
        response = tester.post("/prism", content_type='multipart/form-data', data={'squre': 3, 'height': 3, 'aim': 0})
        self.assertIn('9', response.data.decode())

    def test_check_negativ_var_prism(self):
        tester = app.test_client(self)
        response = tester.post("/prism", content_type='multipart/form-data', data={'squre': -5, 'height': 5, 'aim': 0})
        self.assertIn('25', response.data.decode())

    def test_check_round_prism(self):
        tester = app.test_client(self)
        response = tester.post("/prism", content_type='multipart/form-data', data={'squre': 4.3, 'height': 5.34, 'aim': 3})
        self.assertIn('22.962', response.data.decode())




    def test_normal_int_answ_pyramid(self):
        tester = app.test_client(self)
        response = tester.post("/pyramid", content_type='multipart/form-data', data={'squre': 3, 'height': 3, 'aim': 0})
        self.assertIn('3', response.data.decode())

    def test_check_negativ_var_pyramid(self):
        tester = app.test_client(self)
        response = tester.post("/pyramid", content_type='multipart/form-data', data={'squre': -5, 'height': 5, 'aim': 0})
        self.assertIn('8', response.data.decode())

    def test_check_round_pyramid(self):
        tester = app.test_client(self)
        response = tester.post("/pyramid", content_type='multipart/form-data', data={'squre': 4.3, 'height': 5.34, 'aim': 3})
        self.assertIn('7.654', response.data.decode())




    def test_normal_int_answ_quader(self):
        tester = app.test_client(self)
        response = tester.post("/quader", content_type='multipart/form-data', data={'height': 3, 'length': 3, 'width': 3, 'aim': 0})
        self.assertIn('27', response.data.decode())

    def test_check_negativ_var_quader(self):
        tester = app.test_client(self)
        response = tester.post("/quader", content_type='multipart/form-data',  data={'height': -3, 'length': -5, 'width': -7, 'aim': 0})
        self.assertIn('105', response.data.decode())

    def test_check_round_quader(self):
        tester = app.test_client(self)
        response = tester.post("/quader", content_type='multipart/form-data',  data={'height': 3.4, 'length': 6.5, 'width': 3.66, 'aim': 3})
        self.assertIn('80.886', response.data.decode())