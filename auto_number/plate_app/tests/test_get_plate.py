import uuid

from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APITestCase

from plate_app.models import Plate
from plate_app.views import PlateGetView


class PlateGetViewTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='user1',
            password='password1'
        )
        self.plate = Plate.objects.create(plate_number='Р555РР')
        self.view = PlateGetView.as_view({'get': 'get'})
        self.plate_id = str(self.plate.id)

    def test_get_valid_plate(self):

        request = self.factory.get(f'/plate/get/?id={self.plate_id}')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"plate": {"id": self.plate_id, "plate_number": "Р555РР"}})

    def test_get_plate_with_missing_id(self):
        request = self.factory.get('/plate/get/')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {"error": "id is missing."})

    def test_get_plate_with_invalid_id(self):
        invalid_id = str(uuid.uuid4())
        request = self.factory.get(f'/plate/get/?id={invalid_id}')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {"error": "Plate not found."})
