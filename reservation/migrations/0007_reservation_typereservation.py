# Generated by Django 3.0.1 on 2020-02-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20200202_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='typeReservation',
            field=models.ManyToManyField(to='reservation.TypeReservation'),
        ),
    ]
