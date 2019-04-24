# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

class Schedule(models.Model):
    day = models.IntegerField()
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

class User(AbstractUser):
    second_last_name = models.CharField(
        blank=True, null=True, max_length=150, verbose_name='second last name')
    email = models.EmailField(
        blank=True, max_length=254, verbose_name='email address', unique=True)
    bio = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='active')
    contacts = models.ManyToManyField('self', related_name='contacts')

    def save(self, *args, **kwargs):
        if not self.check_password(self.password):
            self.set_password(self.password)
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['first_name']

def post_register(sender, instance, **kwargs):
    pass

post_save.connect(post_register, sender=User)