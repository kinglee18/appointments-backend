from rest_framework import routers
from users.views import UserViewSet
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]