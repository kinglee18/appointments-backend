from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    todo protect put and patch 
    """

    contacts = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        read_only=False,
        queryset=User.objects.filter()
    )

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'second_last_name', 'email', 'id', 'password', 'contacts']
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'first_name': {'required': True}, 'last_name': {'required': True}}
