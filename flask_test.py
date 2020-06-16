from app import app
import unittest


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_users_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/api/v1/users/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_tweets_status_code(self):
        result = self.app.get('/api/v2/tweets/')
        self.assertEqual(result.status_code, 200)

    def test_info_code(self):
        result = self.app.get('/api/v1/info/')
        self.assertEqual(result.status_code, 200)

    def test_addUsers_status_code(self):
        result = self.app.post('/api/v1/users/', data='{ "username":"Ovestint", '
                                                      '"email": "ronaldrvera@jourrapide.com",'
                                                      ' "password": "juzahpei6e", "name":"Ronald R. Vera"}',
                               content_type='application/json')
        print(result)
        self.assertEqual(result.status_code, 201)

    def test_updateUsers_status_code(self):
        # sends HTTP PUT request to the application
        # on the specified path
        result = self.app.put('/api/v1/users/2/', data='{"username":"Tagning", "emailid": "leolaLguertin@teleworm.us"}',
                              content_type='application/json')
        # assert the status code of the response
        self.assertEquals(result.status_code, 200)

    def test_addTweets_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.post('/api/v2/tweets/', data='{"username":"Tagning", "body": "It Works!#Awesome"}',
                               content_type='application/json')

        # assert the status code of the response
        self.assertEqual(result.status_code, 201)

    def test_deleteUsers_status_code(self):
        # sends HTTP Delete request to the application
        # on the specified path
        result = self.app.delete('/api/v1/users/', data='{"username":"Ovestint"}', content_type='application/json')
        print (result)
        # assert the status code of the response
        self.assertEquals(result.status_code, 200)