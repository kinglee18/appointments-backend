from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'update']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return super().create( request, args, kwargs)
        
    def get_permissions(self):
        if self.action == 'create':
            return []
        return [permission() for permission in self.permission_classes]
