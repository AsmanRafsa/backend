# Generated by Django 4.2.6 on 2023-10-21 16:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointCareApp', '0003_doctorsdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=255)),
                ('patientDisease', models.TextField()),
                ('patientContact', models.CharField(max_length=15)),
                ('patientAge', models.PositiveIntegerField()),
                ('timeBooked', models.DateTimeField(default=datetime.datetime(2023, 10, 21, 16, 22, 53, 253135, tzinfo=datetime.timezone.utc))),
                ('patientDoctor', models.CharField(max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
