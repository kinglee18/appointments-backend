from rest_framework.response import Response
from rest_framework import viewsets, status
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = Reservation.CANCELED
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
