from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'update']
    queryset = User.objects.filter()
    serializer_class = UserSerializer
        
    def get_permissions(self):
        if self.action == 'create':
            return []
        return [permission() for permission in self.permission_classes]
    
    def get_queryset(self):
        return self.queryset.exclude(id=self.request.user.id)