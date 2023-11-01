# Generated by Django 4.2.6 on 2023-10-31 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointCareApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointCareApp.hospital'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='patientDisease',
            field=models.CharField(max_length=50),
        ),
    ]
