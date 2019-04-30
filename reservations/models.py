from django.db import models
from django.core.validators import EmailValidator


class Reservation(models.Model):
    PENDING = "P"
    DECLINED = "D"
    ACCEPTED = "A"
    CANCELED_ORG = "CO"
    CANCELED_GUEST = "CG"
    ACCOMPLISHED = "AC"

    STATUS_LIST = (
        (PENDING, 'Pending'),
        (DECLINED, 'Declined'),
        (ACCEPTED, 'Accepted'),
        (CANCELED_ORG, 'Canceled by organizer'),
        (CANCELED_GUEST, 'Canceled by guest'),
        (ACCOMPLISHED, 'Accomplished'),
    )
    date = models.DateTimeField()
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    guest = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, null=True, related_name='Guest')
    guest_contact = models.CharField(max_length=100, null=True,  validators=[
        EmailValidator(
            message='Ingresa un correo electrónico',
        ),
    ])
    status = models.CharField(
        choices=STATUS_LIST, default="Pending", max_length=30)

    class Meta:
        unique_together = ['date', 'created_by', 'guest']

    def save(self, *args, **kwargs):
        if self.guest is None:
            self.status = self.ACCEPTED
        super().save(*args, **kwargs)

    def cancel_reservation(self, applicant):
        if self.created_by == applicant:
            self.status = self.CANCELED_ORG
        elif self.guest == applicant:
            self.status = self.CANCELED_GUEST
        self.save()