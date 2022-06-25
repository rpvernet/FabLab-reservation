# Generated by Django 3.0.1 on 2020-01-28 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_machine_image'),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('opening_hours', models.TimeField()),
                ('closing_hours', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='default', max_length=60)),
                ('min_duration', models.IntegerField(default=0)),
                ('max_duration', models.IntegerField(default=0)),
                ('staff_point', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='staff_points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='finishing_hours',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='starting_hours',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_with_machine', models.BooleanField(default=False)),
                ('machineID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.Machine')),
            ],
        ),
    ]