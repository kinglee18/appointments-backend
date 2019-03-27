from rest_framework import routers
from reservations.views import ReservationViewSet
from django.conf.urls import url, include


router = routers.DefaultRouter()
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]