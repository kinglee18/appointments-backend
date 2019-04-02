from django.db import models
from django.core.validators import RegexValidator


class Reservation(models.Model):
    PENDING = "P"
    DECLINED = "D"
    ACCEPTED = "A"
    CANCELED = "C"
    ACCOMPLISHED = "Ac"

    STATUS_LIST = (
        (PENDING, 'Pending'),
        (DECLINED, 'Declined'),
        (ACCEPTED, 'Accepted'),
        (CANCELED, 'Canceled'),
        (ACCOMPLISHED, 'Accomplished'),
    )
    date = models.DateTimeField()
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    guest = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, null=True, related_name='Guest')
    guest_contact = models.CharField(max_length=100, null=True,  validators=[
        RegexValidator(
            regex='^77$',
            message='Ingresa un número teléfonico o un correo electrónico',
        ),
    ])
    status = models.CharField(
        choices=STATUS_LIST, default="Pending", max_length=30)

    def save(self, *args, **kwargs):
        if self.guest is None:
            self.status = self.ACCEPTED
        super().save(*args, **kwargs)
