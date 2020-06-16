from app import app
import unittest

class FlaskappTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_users_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/users')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
