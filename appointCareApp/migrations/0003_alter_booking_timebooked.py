# Generated by Django 4.2.6 on 2023-10-24 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointCareApp', '0002_alter_booking_timebooked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeBooked',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 24, 7, 24, 48, 390499, tzinfo=datetime.timezone.utc)),
        ),
    ]
