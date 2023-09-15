from statistics import mode
from django.db import models

# Create your models here.



class Player(models.Model):

    POS_CHOICES = (
        ('SF', 'Small Forward'),
        ('C', 'Center'),
        ('PF', 'Power Forward'),
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard')

    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pos = models.CharField(choices=POS_CHOICES, max_length=100)
    height = models.CharField(max_length=100)


    def __str__ (self):
        return f'{self.first_name} {self.last_name}'