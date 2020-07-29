from django.test import TestCase, Client

client = Client()
class JustTest(TestCase):
    response = client.get('/view')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.json(),{
        "message": "SUCCESS"
    })

# Create your tests here.
