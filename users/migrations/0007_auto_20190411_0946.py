# Generated by Django 2.1.3 on 2019-04-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190411_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='schedule',
            new_name='user',
        ),
    ]
