# Generated by Django 3.0.1 on 2021-04-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210422_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='vacation',
            field=models.DateField(null=True),
        ),
    ]
