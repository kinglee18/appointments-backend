# Generated by Django 2.1.3 on 2019-04-08 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20190326_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('D', 'Declined'), ('A', 'Accepted'), ('CO', 'Canceled by organizer'), ('CG', 'Canceled by guest'), ('AC', 'Accomplished')], default='Pending', max_length=30),
        ),
    ]