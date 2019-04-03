from rest_framework import serializers
from users.models import User
from rest_framework.authtoken.models import Token


class UserBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'second_last_name', 'email', 'id']


class UserTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name', 'second_last_name', 'email', 'id', 'token', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required':True},
                        'first_name': {'required': True}, 'last_name': {'required': True}}
