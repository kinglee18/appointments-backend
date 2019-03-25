from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name',
                  'last_name', 'second_last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}
