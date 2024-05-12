from django.db import models

# Create your models here.
class SmashData(models.Model):
    fighterNumber = models.CharField(max_length=255)
    fighterName = models.CharField(max_length=255)