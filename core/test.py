from django.test import TestCase, Client


class CoreStaffTest(TestCase):
    def test_user_creation_middleware(self):
        client = Client()
        response = client.get('/api/v1/me/')

        self.assertIs(response.status_code, 200)
        self.assertTrue('username' in response.data)
