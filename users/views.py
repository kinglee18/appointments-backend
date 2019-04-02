from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserBasicSerializer, UserTokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'update']
    queryset = User.objects.all()
    serializer_class = UserBasicSerializer
        
    def get_permissions(self):
        if self.action == 'create':
            return []
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = UserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)