from rest_framework import serializers
from reservations.models import Reservation
from users.models import User


class ReservationSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault())
    guest = serializers.PrimaryKeyRelatedField(
        many=False,
        required=False,
        read_only=False,
        queryset=User.objects.filter()
    )

    def validate(self, data):
        if 'guest' not in data and 'guest_contact' not in data:
            raise serializers.ValidationError('Ingresa un correo electrónico o asocia un usuario')
        elif 'guest' in data and 'guest_contact' in data:
            raise serializers.ValidationError('No se puede ingresar ambos datos')
        return data

    class Meta:
        model = Reservation
        fields = ['date', 'created_by', 'id', 'guest_contact', 'guest']
