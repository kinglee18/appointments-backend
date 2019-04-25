from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from users.serializers import UserSerializer


class UserCrudTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="alberto@hotmail.com")
        self.client = APIClient()

    def test_required_register_fields(self):
        required_fields = ['password', 'first_name', 'last_name']
        response = self.client.post("/users/", {}, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        for field in required_fields:
            assert field in response.data

    def test_user_registration(self):
        result_fields = ['first_name', 'last_name',
                         'id', 'email', 'second_last_name']
        data = {
            "first_name": "javier",
            "last_name": "hernandez",
            "second_last_name": "gaona",
            "email": "javier@gmail.com",
            "password": "hola"
        }
        response = self.client.post("/users/", data, format="json")
        for field in result_fields:
            assert field in response.data

    """
    excludes current user 
    """

    def test_contacts_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            "/users/",
            format="json")
        users = User.objects.exclude(id=self.user.id)
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        assert response.status_code == status.HTTP_200_OK

    """
    Create search test and order 
    """


class ContactsCrudTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="alberto@hotmail.com")
        self.client = APIClient()
    """
    Test contact addition
    """

    def test_contact_addition(self):
        contact = User.objects.create(email="jose@hotmail.com", is_active=True)
        data = {
            "contacts": [contact.id]
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            "/users/{0}/".format(self.user.id),
            data,
            format="json")
        assert self.user.contacts.first().id == contact.id
        assert response.status_code == status.HTTP_200_OK

    def test_contact_removal(self):
        contact = User.objects.create(email="jose@hotmail.com", is_active=True)
        self.user.contacts.add(contact)
        data = {
            "contacts": []
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            "/users/{0}/".format(self.user.id),
            data,
            format="json")
        assert self.user.contacts.count() == 0
        assert response.status_code == status.HTTP_200_OK
