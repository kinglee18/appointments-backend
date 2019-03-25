from django.db import models

class Reservation(models.Model):
    date = models.DateTimeField()
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, related_name='Guest')
