from django.db import models


class Machine(models.Model):
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    member_price = models.CharField(blank=True, max_length=120)
    no_member_price = models.CharField(blank=True, max_length=120)
    active = models.BooleanField()
    typeReservation = models.ManyToManyField('reservation.TypeReservation')
    context_with_badge = models.CharField(max_length=120,
                                          default="Qu'est-ce qui affiche avec le formulaire si la personne a la badge")
    context_without_badge = models.CharField(max_length=120,
                                             default="Qu'est-ce qui affiche avec le formulaire si la personne n'a pas la badge")
    number_machine = models.IntegerField(default=1, null=False, blank=False)
    image = models.ImageField(upload_to='photos/machines/', blank=True)

    def __str__(self):
        return self.name

