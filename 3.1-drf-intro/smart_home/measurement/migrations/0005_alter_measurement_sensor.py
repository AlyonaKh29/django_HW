# Generated by Django 5.1.5 on 2025-01-25 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_measurement_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor'),
        ),
    ]
