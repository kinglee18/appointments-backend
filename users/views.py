from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import action
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name',
                     'last_name', 'second_last_name', 'email']

    def get_permissions(self):
        if self.action == 'create':
            return []
        return [permission() for permission in self.permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            self.get_queryset()).exclude(id=self.request.user.id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Account(APIView):
    permission_classes = []
    def post(self, request, format=None):
        try:
            token = Token.objects.get(key=request.data['token'])
            user = User.objects.get(pk=token.user_id)
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        