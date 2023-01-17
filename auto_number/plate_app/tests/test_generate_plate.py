from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User


class PlateGenerateViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='password1')
        self.client.force_authenticate(user=self.user)

    def test_generate_plate_with_valid_amount(self):
        response = self.client.get('/plate/generate/', {'amount': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['plates']), 3)

    def test_generate_plate_without_amount(self):
        response = self.client.get('/plate/generate/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['plates']), 1)
