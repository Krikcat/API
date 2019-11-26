from django.test import TestCase
# Create your tests here.



class Tests(TestCase):
    def test_register(self):
        response = self.client.post('/api/register/', {"login":"afro", "password":"412536"}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/api/login/', {"login":"afro", "password":"412536"}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.delete('/api/login/', {"login": "afro", "password": "412536"}, content_type='application/json')
        self.assertEqual(response.status_code, 404)