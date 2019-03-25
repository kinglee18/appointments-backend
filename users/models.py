# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    second_last_name = models.CharField(
        blank=True, null=True, max_length=150, verbose_name='second last name')
    email = models.EmailField(
        blank=True, max_length=254, verbose_name='email address', unique=True)
    bio = models.TextField(max_length=500, blank=True)

    def save(self, *args, **kwargs):
        if not self.check_password(self.password):
            self.set_password(self.password)
        self.username = self.email
        super().save(*args, **kwargs)
