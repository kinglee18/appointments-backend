from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User


class ScheduleCrudTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="alberto@hotmail.com")
        self.client = APIClient()

    """
    Test a reservation
    """

    def test_make_reservation(self):
        guest = User.objects.create(email="jose@hotmail.com", is_active=True)
        data = {
            "date": "2019-03-03 11:11:00",
            "guest": guest.id
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/reservation/",
            data,
            format="json")
        assert response.status_code == status.HTTP_201_CREATED
        response = self.client.post(
            "/reservation/",
            data,
            format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_make_reservation_failures(self):
        data = {
            "date": "2019-03-03 11:11:00"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/reservation/",
            data,
            format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_make_reservation_contact_and_guest_failure(self):
        data = {
            "date": "2019-03-03 11:11:00",
            "guest":1,
            "guest_contact":"frfrfr@jkfjf.com"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            "/reservation/",
            data,
            format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

