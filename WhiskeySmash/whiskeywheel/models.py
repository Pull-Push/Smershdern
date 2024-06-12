from django.db import models

# Create your models here.
class TestClass(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.first



class PersonClass(models.Model):
    first = models.CharField(max_length=255),
    last = models.CharField(max_length=255)

    def __str__(self):
        return self.first