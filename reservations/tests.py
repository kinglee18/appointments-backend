from django.test import TestCase
from rest_framework import  status
from rest_framework.test import APIClient
from users.models import User

class ScheduleCrudTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="alberto@hotmail.com")
        self.client = APIClient()
