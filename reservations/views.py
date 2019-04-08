from rest_framework.response import Response
from rest_framework import viewsets, status
from django.db.models import Q
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(Q(created_by=self.request.user) | Q(guest=self.request.user))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.cancel_reservation(self.request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
