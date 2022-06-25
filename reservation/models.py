from django.db import models
from django.contrib.auth.models import User
from accounts.models import StaffProfile
from machines.models import Machine
from datetime import timedelta, datetime
# Create your models here.models.ForeignKey(Machine, on_delete=models.CASCADE, null=False)


class Reservation(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    machineID = models.ForeignKey(Machine, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(null=False)
    starting_hours = models.DateTimeField(null=False, blank=False)
    finishing_hours = models.DateTimeField(null=False, blank=False)
    staff_points = models.IntegerField(null=False)
    type_reservation = models.CharField(max_length=120, default='Formation')

    def __str__(self):
        return self.machineID.name


class Holiday(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField(null=False)

    def __str__(self):
        return self.title


class OpeningHour(models.Model):
    class DayWeek(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6
    day_week = models.IntegerField(choices=DayWeek.choices)
    opening_hours = models.TimeField(null=False)
    closing_hours = models.TimeField(null=False)

    def __str__(self):
        return str(self.day_week)


class TypeReservation(models.Model):
    type = models.CharField(default='default', max_length=60)
    min_duration = models.DurationField(default=timedelta(minutes=15))
    max_duration = models.DurationField(default=timedelta(minutes=120))
    staff_point = models.IntegerField(default=0)

    def __str__(self):
        return self.type


class Badges(models.Model):
    name = models.CharField(default='default', max_length=90)
    machineID = models.ForeignKey(Machine, on_delete=models.CASCADE, null=False)
    badge_picture = models.ImageField(upload_to='photos/badges', blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    class DayWeek(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6
    day_week = models.IntegerField(choices=DayWeek.choices)
    staffID = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, null=False)
    shift_start = models.TimeField(null=False)
    shift_end = models.TimeField(null=False)

    def __str__(self):
        return str(self.day_week)
