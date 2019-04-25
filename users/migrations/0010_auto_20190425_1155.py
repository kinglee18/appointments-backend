# Generated by Django 2.1.3 on 2019-04-25 16:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190423_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(related_name='solicitant', to=settings.AUTH_USER_MODEL),
        ),
    ]