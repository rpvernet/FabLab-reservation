# Generated by Django 3.0.1 on 2021-01-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_badges_badge_picture'),
        ('accounts', '0002_auto_20210105_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='badges',
            field=models.ManyToManyField(blank=True, to='reservation.Badges'),
        ),
    ]
