# Generated by Django 2.1.3 on 2019-03-26 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20190326_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest_contact',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='No es valido', regex='^77$')]),
        ),
    ]
