# Generated by Django 3.0.1 on 2020-02-02 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20200202_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typereservation',
            old_name='duration',
            new_name='min_duration',
        ),
        migrations.AddField(
            model_name='typereservation',
            name='max_duration',
            field=models.DurationField(default=datetime.timedelta(seconds=7200)),
        ),
    ]
