# Generated by Django 3.0.1 on 2020-02-24 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_auto_20200224_0845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='typeReservation',
            new_name='type_reservation',
        ),
    ]
