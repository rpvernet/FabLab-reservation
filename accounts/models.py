from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Patron(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	badges = models.ManyToManyField('reservation.Badges', blank=True)

	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Patron.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.patron.save()


class StaffProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	staff_point = models.IntegerField(default=6, null=False)

	def __str__(self):
		return str(self.user)
