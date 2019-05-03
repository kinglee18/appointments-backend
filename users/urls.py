from rest_framework import routers
from users.views import UserViewSet, Account
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'account', Account.as_view())
]