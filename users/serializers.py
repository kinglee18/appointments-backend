from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'second_last_name', 'email', 'id', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'first_name': {'required': True}, 'last_name': {'required': True}}
