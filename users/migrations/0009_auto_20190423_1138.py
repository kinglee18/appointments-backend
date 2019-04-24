# Generated by Django 2.1.3 on 2019-04-23 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190422_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='user',
            name='contacts',
            field=models.ManyToManyField(related_name='_user_contacts_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
