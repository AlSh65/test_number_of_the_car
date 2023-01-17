from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from plate_app.models import Plate


class PlateAddViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='user1', password='password1')
        self.client.force_authenticate(user=self.user)
        self.plate_data = {'plate': 'Р555РР'}

    def test_add_valid_plate(self):
        response = self.client.post('/plate/add/', self.plate_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data.get('id'))
        self.assertEqual(Plate.objects.count(), 1)
        self.assertEqual(Plate.objects.first().plate_number, 'Р555РР')

    def test_add_invalid_plate(self):
        plate_data = {'plate': 'ф5642вс'}
        response = self.client.post('/plate/add/', plate_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Invalid plate number.')
        self.assertEqual(Plate.objects.count(), 0)

    def test_add_without_plate(self):
        response = self.client.post('/plate/add/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'plate is missing.')
        self.assertEqual(Plate.objects.count(), 0)
